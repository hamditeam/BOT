import telebot,time,requests,csv,threading
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types
from BR import ST
from colorama import Fore
import pytz
from datetime import datetime
user_data = {}
CSV_FILE = 'ids_anti-spam.csv'
ANTI_SPAM_INTERVAL = 25
# إنشاء البوت باستخدام التوكن
bot = telebot.TeleBot("6481463767:AAEOItbUS-0NYyhwTNCqDY7HbIMjmPjZNZA")
allowed_users = [994383066, 1911223261]
allowed_groups = [-1001847235996]
										#CHK COMMANDS 
@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id not in allowed_users and message.chat.id not in allowed_groups:
        bot.send_message(message.chat.id, text="البوت مدفوع لكن مجاني في شات مزيكا وجوكر وبس")
        return
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
    if message.from_user.id not in allowed_users and message.chat.id not in allowed_groups:
        bot.send_message(message.chat.id, text="البوت مدفوع لكن مجاني في شات مزيكا وجوكر وبس")
        return
    keyboard = types.InlineKeyboardMarkup()
    menu_button = types.InlineKeyboardButton("🔥 COMMANDS 🔥", callback_data="menu")
    # إنشاء لوحة المفاتيح الخاصة بالزر
    keyboard.add(menu_button)
    # إرسال رسالة تحتوي على الزر
    bot.send_message(message.chat.id, "اضغط علي COMMANDS", reply_markup=keyboard)

# دالة لمعالجة اختيار المستخدم للزر
@bot.callback_query_handler(func=lambda call: True)
def handle_button(call):
    if message.from_user.id not in allowed_users and message.chat.id not in allowed_groups:
        bot.send_message(message.chat.id, text="البوت مدفوع لكن مجاني في شات مزيكا وجوكر وبس")
        return
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
def bb(message):
    user_id = message.from_user.id
    current_time = time.time()
    
    if user_id in user_data:
        last_command_time = user_data[user_id]
        time_diff = current_time - last_command_time
        
        if time_diff < ANTI_SPAM_INTERVAL:
            remaining_time = int(ANTI_SPAM_INTERVAL - time_diff)
            bot.reply_to(message, f"ANTI_SPAM: Try again after {remaining_time} seconds.")
            return

    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user_id, message.from_user.username])
    
    user_data[user_id] = current_time

    threading.Timer(ANTI_SPAM_INTERVAL, delete_user_data, args=[user_id]).start()
    text = message.text.replace('/chk ','')
    if len(text) == 0:
    	bot.reply_to(message, """Invalid format, type it CORRECTLY!
Format: XXXXXXXXXXXXXXXX|MM|YYYY|CVV.""")
    else:
        t = time.time()
        visa = text.split('|')[0]
        bin=visa[:6]
        print(bin)
        mes = text.split('|')[1]
        ano = text.split('|')[2][-2:]
        cvv = text.split('|')[3]
        card=f"{visa}|{mes}|{ano}|{cvv}"
        bot.reply_to(message, "Checking your card...⌛")
        r=requests.session()
        url=f'https://lookup.binlist.net/{bin}'
        req=requests.get(url).json()
        #print(req)
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
        r=requests.session()
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
def delete_user_data(user_id):
    user_data.pop(user_id, None)
    with open(CSV_FILE, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader if row[0] != str(user_id)]
    with open(CSV_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)
bot.infinity_polling()
