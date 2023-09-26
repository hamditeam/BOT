import telebot,time,requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
from BR import ST
from colorama import Fore
import pytz
from datetime import datetime
# إنشاء البوت باستخدام التوكن
bot = telebot.TeleBot("6380486607:AAHPKftNWswL80j5u_KoQT-t4JvohQJ4k00")
id=[1911223261]
										#CHK COMMANDS 
@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.chat.id)
    with open('user_id.txt', 'r') as f:
        existing_ids = f.read().splitlines()
    if user_id not in existing_ids:
        with open('user_id.txt', 'a') as f:
            f.write(f"{user_id}\n")
    with open('user_id.txt', 'r') as f:
        num_lines = len(f.readlines())
    bot.reply_to(message, f"""
🤖 Bot Status ⇾ Operational ✅

< Total use bot ✅ >: {num_lines}

Send /cmds for see all commands 🔥    
    """)
@bot.message_handler(commands=['cmds'])
def handle_message(message):
    keyboard = types.InlineKeyboardMarkup()
    menu_button = types.InlineKeyboardButton("🔥 COMMANDS 🔥", callback_data="menu")
    # إنشاء لوحة المفاتيح الخاصة بالزر
    keyboard.add(menu_button)
    # إرسال رسالة تحتوي على الزر
    bot.send_message(message.chat.id, "اضغط علي COMMANDS", reply_markup=keyboard)

# دالة لمعالجة اختيار المستخدم للزر
@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    if call.data == "menu":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        # إنشاء زر "ss"
        ss_button = types.InlineKeyboardButton("⭐ Braintree 🔥", callback_data="ss")
        # إنشاء زر "ch"
        ch_button = types.InlineKeyboardButton("💯 Stripe 🔥", callback_data="ch")
        # إنشاء لوحة المفاتيح الخاصة بالأزرار
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(ss_button, ch_button)
        # إرسال رسالة تحتوي على الأزرار
        bot.send_message(call.message.chat.id, "Choose gate \n اختار البوابة", reply_markup=keyboard)
    elif call.data == "ss":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "/chk >> BRAINTREE")
    elif call.data == "ch":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "/st >> STRIOE")
@bot.message_handler(commands=['chk'])
def chk(message):
    text = message.text[4:].replace(' ','')
    if len(text) == 0:
    	bot.reply_to(message, """Invalid format, type it CORRECTLY!
Format: XXXXXXXXXXXXXXXX|MM|YYYY|CVV.""")
    else:
        t = time.time()
        visa = text.split('|')[0]
        bin=visa[:6]
        mes = text.split('|')[1]
        ano = text.split('|')[2][-2:]
        cvv = text.split('|')[3]
        card=f"{visa}|{mes}|{ano}|{cvv}"
        bot.reply_to(message, "Checking your card...⌛")
        url=f'https://lookup.binlist.net/{bin}'
        try:
        	req=requests.get(url).json()
        except:
        	pass
        try:
        	inf=req['scheme']
        except:
        	inf='UNKOWM'
        try:
        	type=req['type']
        except:
        	type='UNKOWN'
        try:
        	brand=req['brand']
        except:
        	brand='UNKOWN'
        try:
        	info=inf+ '-' +type+ '-' +brand
        except:
        	info='UNKOWN'
        try:
        	ii=info.upper()
        except:
        	ii='UNKOWN'
        try:
        	bank=req['bank']['name'].upper()
        except:
        	bank='UNKOWN'
        try:
        	do = req['country']['name']+' '+req['country']['emoji'].upper()
        except:
        					do='UNKOWN'
        try:
        	last = str(ST(card))
        except Exception as e:
        	print(e)
        	try:
        		last = str(ST(card))
        	except:
        		print(e)
    if "Insufficient Funds" in last:
        	tt = time.time()
        	d = tt - t
        	timer = round(d,2)
        	bot.delete_message(message.chat.id, message.message_id + 1)
        	print(Fore.YELLOW+card+"->"+Fore.GREEN+last)
        	bot.reply_to(message,f""" 
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {card}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 1
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 1000: Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗧𝗼𝗼𝗸 {timer} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀""")
    elif "Status code avs: Gateway Rejected: avs" in last or "Nice! New payment method added:" in last or "Duplicate card exists in the vault." in last or "Approved" in last:
        	tt = time.time()
        	d = tt - t
        	timer = round(d,2)
        	bot.delete_message(message.chat.id, message.message_id + 1)
        	bot.reply_to(message,f""" 
𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅

𝗖𝗖 ⇾ {card}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 1
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 1000: Approved

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗧𝗼𝗼𝗸 {timer} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
    	""")
        	print(Fore.YELLOW+card+"->"+Fore.GREEN+last)
    else:
        	tt = time.time()
        	d = tt - t
        	timer = round(d,2)
        	bot.delete_message(message.chat.id, message.message_id + 1)
        	bot.reply_to(message,f""" 
𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌

𝗖𝗖 ⇾ {card}
𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 1
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {last}

𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: {ii}
𝗕𝗮𝗻𝗸: {bank}
𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {do}

𝗧𝗼𝗼𝗸 {timer} 𝘀𝗲𝗰𝗼𝗻𝗱𝘀
    	""")
        	print(Fore.YELLOW+card+"->"+Fore.RED+last)
bot.infinity_polling()