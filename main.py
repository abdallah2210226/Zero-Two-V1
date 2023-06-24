import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import re
import random
from datetime import datetime
import time
import sys
from PIL import Image, ImageDraw,ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import psutil
import arabic_reshaper
from googletrans import Translator
import random
from kt_tweet_sowal import *
import random
import unicodedata
from random import choice, randint
start2 = time.time()

ping_photo = "https://telegra.ph//file/8fe4f9f6c2b0135b67085.jpg"
start_photo = "https://telegra.ph//file/61904cf0cb3b74844679d.jpg"
help_photo = "https://telegra.ph//file/7588af20e99f430ab4c7e.jpg"

TOKEN = "5081332593:AAE3uucLd5CQn6Fqb9h0PmGtp5Vpj3aGY48"
bot = telebot.TeleBot(TOKEN)
current_page = {}
episodes = []
developer_id = 1448333343
allowed_ids_file = 'database/allowed_ids.json'
channels_file = 'database/channels.json'
url = "https://api.prodia.com/v1/job"
# قاعدة بيانات المستخدمين في ملف JSON
user_data_file = 'user_data.json'
with open(user_data_file, 'r') as file:
    user_data = json.load(file)
banned_words = ["booty","2g1c", "2 girls 1 cup", "acrotomophilia", "alabama hot pocket", "alaskan pipeline", "anal", "anilingus", "anus", "apeshit", "arsehole", "ass", "asshole", "assmunch", "auto erotic", "autoerotic", "babeland", "baby batter", "baby juice", "ball gag", "ball gravy", "ball kicking", "ball licking", "ball sack", "ball sucking", "bangbros", "bareback", "barely legal", "barenaked", "bastard", "bastardo", "bastinado", "bbw", "bdsm", "beaner", "beaners", "beaver cleaver", "beaver lips", "bestiality", "big black", "big breasts", "big knockers", "big tits", "bimbos", "birdlock", "bitch", "bitches", "black cock", "blonde action", "blonde on blonde action", "blowjob", "blow job", "blow your load", "blue waffle", "blumpkin", "bollocks", "bondage", "boner", "boob", "boobs", "booty call", "brown showers", "brunette action", "bukkake", "bulldyke", "bullet vibe", "bullshit", "bung hole", "bunghole", "busty", "butt", "buttcheeks", "butthole", "camel toe", "camgirl", "camslut", "camwhore", "carpet muncher", "carpetmuncher", "chocolate rosebuds", "circlejerk", "cleveland steamer", "clit", "clitoris", "clover clamps", "clusterfuck", "cock", "cocks", "coprolagnia", "coprophilia", "cornhole", "coon", "coons", "creampie", "cum", "cumming", "cunnilingus", "cunt", "darkie", "date rape", "daterape", "deep throat", "deepthroat", "dendrophilia", "dick", "dildo", "dingleberry", "dingleberries", "dirty pillows", "dirty sanchez", "doggie style", "doggiestyle", "doggy style", "doggystyle", "dog style", "dolcett", "domination", "dominatrix", "dommes", "donkey punch", "double dong", "double penetration", "dp action", "dry hump", "dvda", "eat my ass", "ecchi", "ejaculation", "erotic", "erotism", "escort", "eunuch", "faggot", "fecal", "felch", "fellatio", "feltch", "female squirting", "femdom", "figging", "fingerbang", "fingering", "fisting", "foot fetish", "footjob", "frotting", "fuck", "fuck buttons", "fuckin", "fucking", "fucktards", "fudge packer", "fudgepacker", "futanari", "gang bang", "gay sex", "genitals", "giant cock", "girl on", "girl on top", "girls gone wild", "goatcx", "goatse", "god damn", "gokkun", "golden shower", "goodpoop", "goo girl", "goregasm", "grope", "group sex", "g-spot", "guro", "hand job", "handjob", "hard core", "hardcore", "hentai", "homoerotic", "honkey", "hooker", "hot carl", "hot chick", "how to kill", "how to murder", "huge fat", "humping", "incest", "intercourse", "jack off", "jail bait", "jailbait", "jelly donut", "jerk off", "jigaboo", "jiggaboo", "jiggerboo", "jizz", "juggs", "kike", "kinbaku", "kinkster", "kinky", "knobbing", "leather restraint", "leather straight jacket", "lemon party", "lolita", "lovemaking", "make me come", "male squirting", "masturbate", "menage a trois", "milf", "missionary position", "motherfucker", "mound of venus", "mr hands", "muff diver", "muffdiving", "nambla", "nawashi", "negro", "neonazi", "nigga", "nigger", "nig nog", "nimphomania", "nipple", "nipples", "nsfw images", "nude", "nudity", "nympho", "nymphomania", "octopussy", "omorashi", "one cup two girls", "one guy one jar", "orgasm", "orgy", "paedophile", "paki", "panties", "panty", "pedobear", "pedophile", "pegging", "penis", "phone sex", "piece of shit", "pissing", "piss pig", "pisspig", "playboy", "pleasure chest", "pole smoker", "ponyplay", "poof", "poon", "poontang", "punany", "poop chute", "poopchute", "porn", "porno", "pornography", "prince albert piercing", "pthc", "pubes", "pussy", "queaf", "queef", "quim", "raghead", "raging boner", "rape", "raping", "rapist", "rectum", "reverse cowgirl", "rimjob", "rimming", "rosy palm", "rosy palm and her 5 sisters", "rusty trombone", "sadism", "santorum", "scat", "schlong", "scissoring", "semen", "sex", "sexo", "sexy", "shaved beaver", "shaved pussy", "shemale", "shibari", "shit", "shitblimp", "shitty", "shota", "shrimping", "skeet", "slanteye", "slut", "s&m", "smut", "snatch", "snowballing", "sodomize", "sodomy", "spic", "splooge", "splooge moose", "spooge", "spread legs", "spunk", "strap on", "strapon", "strappado", "strip club", "style doggy", "suck", "sucks", "suicide girls", "sultry women", "swastika", "swinger", "tainted love", "taste my", "tea bagging", "threesome", "throating", "tied up", "tight white", "tit", "tits", "titties", "titty", "tongue in a", "topless", "tosser", "towelhead", "tranny", "tribadism", "tub girl", "tubgirl", "tushy", "twat", "twink", "twinkie", "two girls one cup", "undressing", "upskirt", "urethra play", "urophilia", "vagina", "venus mound", "vibrator", "violet wand", "vorarephilia", "voyeur", "vulva", "wank", "wetback", "wet dream", "white power", "wrapping men", "wrinkled starfish", "xx", "xxx", "yaoi", "yellow showers", "yiffy", "zoophilia", "🖕","كسمك", "سكس", "طيز", "شرج", "لعق", "لحس", "مص", "تمص", "بيضان", "ثدي", "بز", "بزاز", "حلمة", "مفلقسة", "بظر", "كس", "فرج", "شهوة", "شاذ", "مبادل", "عاهرة", "جماع", "قضيب", "زب", "لوطي", "لواط", "سحاق", "سحاقية", "اغتصاب", "خنثي", "احتلام", "نيك", "متناك", "متناكة", "شرموطة", "عرص", "خول", "قحبة", "لبوة", "تتناك", "قحبه", "زبر","عرث"]
user_processing = {}  # قاموس لتتبع حالة الضغط لكل مستخدم
models = {
"Analog V1": "analog-diffusion-1.0.ckpt [9ca13f02]",
"Anything V3": "anythingv3_0-pruned.ckpt [2700c435]",
"Anything V4.5": "anything-v4.5-pruned.ckpt [65745d25]",
"Anything V5": "anythingV5_PrtRE.safetensors [893e49b9]",
"AbyssOrangeMix V3": "AOM3A3_orangemixs.safetensors [9600da17]",
"Deliberate V2": "deliberate_v2.safetensors [10ec4b29]",
"Dreamlike Diffusion V1": "dreamlike-diffusion-1.0.safetensors [5c9fd6e0]",
"Dreamlike Diffusion V2": "dreamlike-diffusion-2.0.safetensors [fdcf65e7]",
"Dreamshaper 5 baked vae": "dreamshaper_5BakedVae.safetensors [a3fbf318]",
"Dreamshaper 6 baked vae": "dreamshaper_6BakedVae.safetensors [114c8abb]",
"Elldreth's Vivid": "elldreths-vivid-mix.safetensors [342d9d26]",
"Lyriel V1.5": "lyriel_v15.safetensors [65d547c5]",
"Lyriel V1.6": "lyriel_v16.safetensors [68fceea2]",
"MeinaMix Meina V9": "meinamix_meinaV9.safetensors [2ec66ab0]",
"Openjourney V4": "openjourney_V4.ckpt [ca2f377f]",
"Portrait V1": "portrait+1.0.safetensors [1400e684]",
"Realistic Vision V1.4": "Realistic_Vision_V1.4-pruned-fp16.safetensors [8d21810b]",
"Realistic Vision V2.0": "Realistic_Vision_V2.0.safetensors [79587710]",
"ReV Animated V1.2.2": "revAnimated_v122.safetensors [3f4fefd9]",
"SD V1.4": "sdv1_4.ckpt [7460a6fa]",
"SD V1.5": "v1-5-pruned-emaonly.ckpt [81761151]",
"Shonin's Beautiful People V1.0": "shoninsBeautiful_v10.safetensors [25d8c546]",
"TheAlly's Mix II": "theallys-mix-ii-churned.safetensors [5d9225a4]",
"Timeless V1": "timeless-1.0.ckpt [7c4971d4]"
}
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Sat", 60 * 60 * 24 * 7),
    ("Day", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),)
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = [" ث", " د", " س", " ي"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)

def bot_sys_stats():
    bot_uptime = int(time.time() - start2)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK

bot.set_my_commands(commands=[telebot.types.BotCommand('start','إبدأ ⚡️')
    ,telebot.types.BotCommand('avatar','أفاتارت أنمي🖼')
    ,telebot.types.BotCommand('ping','حالة البوت📊')
    ,telebot.types.BotCommand('quote','إقتباس📌')
    ,telebot.types.BotCommand('news','لرؤيه أخر أخبار الأنميات🗞')
    ,telebot.types.BotCommand('admin','أوامر للمطور(خاص بالمطور فقط)🔒')])
@bot.message_handler(commands=['reset_war'])
def reset_user_data(message):
    user_id = message.from_user.id
    # التحقق من صحة الصلاحيات
    if user_id != 1448333343:
        bot.reply_to(message, "You are not authorized to use this command.")
        return
    # استلام معرف المستخدم المراد تصفير بياناته
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Please provide the user ID.")
        return
    target_user_id = int(message.text.split()[1])
    # تصفير بيانات المستخدم
    reset_war(target_user_id)
    bot.reply_to(message, "User data has been reset.")
def reset_war(user_id):
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        user['warnings'] = 0
        userid = user['user_id']
        save_user_data()
        bot.send_message(userid,"تم تصفير الانذارات في أمر الذكاء الاصطناعي")
@bot.message_handler(commands=['reset_img'])
def reset_user_data(message):
    user_id = message.from_user.id
    # التحقق من صحة الصلاحيات
    if user_id != 1448333343:
        bot.reply_to(message, "You are not authorized to use this command.")
        return
    # استلام معرف المستخدم المراد تصفير بياناته
    if len(message.text.split()) < 2:
        bot.reply_to(message, "Please provide the user ID.")
        return
    target_user_id = int(message.text.split()[1])
    # تصفير بيانات المستخدم
    reset_war(target_user_id)
    bot.reply_to(message, "User data has been reset.")
def reset_war(user_id):
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        user['photos_used'] = 0
        userid = user['user_id']
        save_user_data()
        bot.send_message(userid,"تم تصفير الصور في أمر الذكاء الاصطناعي")
@bot.message_handler(commands=['ai'])
def send_welcome(message):
    global prompt
    prompt = message.text.split("ai")[1]
    user_id = message.from_user.id
    if prompt == "":
        bot.send_message(message.chat.id, "/ai + {الوصف}")
    else :
        # التحقق من الحد اليومي لعدد الصور المستخدمة للمستخدم
        if not check_photos_limit(user_id):
            remaining_time = calculate_remaining_time(user_id)
            remaining_time_str = format_remaining_time(remaining_time)
            messagee = f"لقد بلغت الحد اليومي لعدد الصور البالغ 25 صورة.\n\nالوقت المتبقي : {remaining_time_str}"
            bot.reply_to(message, f"{messagee}")
            return
        else:
            if get_user_warnings(user_id) >= 5:
                bot.send_message(message.chat.id, "لا يُسمح لك باستخدام البوت بعد تجاوز الحد المسموح لعدد الإنذارات.")
                return
            elif any(word in message.text for word in banned_words):
                # إرسال تحذير للمستخدم
                bot.send_message(message.chat.id, "تم استخدام كلمة محظورة")
                # تحقق من عدد الإنذارات السابقة للمستخدم وإرسال عدد الإنذارات المتبقية
                warnings = get_user_warnings(message.from_user.id)
                remaining_warnings = 3 - warnings
                bot.send_message(message.chat.id, f"لديك {remaining_warnings} من التحذيرات المتبقية.")
                if warnings < 3:
                    add_warning_to_user(message.from_user.id)
            else:
                keyboard = create_model_keyboard(user_id)
                bot.reply_to(message, "اختار موديل:", reply_markup=keyboard)
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.message_handler(commands=['ping'])
def ping(m):
    botname = bot.get_me().first_name
    botusername = bot.get_me().username
    start = time.time()
    current_time = datetime.utcnow()
    reply = bot.send_message(m.chat.id, "جاري الحساب ... ", reply_to_message_id=m.id)
    delta_ping = time.time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = _human_time_duration(int(uptime_sec))
    UP, CPU, RAM, DISK = bot_sys_stats()
    bot.send_photo(m.chat.id, ping_photo,caption=f"""
⿻ بوت ❲ [{botname}](https://t.me/{botusername}) ❳  يتم الان تشغيلة علي بينج ↤ ❲ {delta_ping * 1000:.3f} ms ❳  .
⿻ البوت قيد التشغيل من ❲ {UP} ❳ .
⿻ يتم استخدام ❲ {DISK} ❳ من مساحة السيرفر .
⿻ يتم استهلاك ❲ {CPU} ❳ من المعالج , ويتم استهلاك ❲ {RAM} ❳ من الرام .
""",parse_mode="markdown",reply_to_message_id=m.message_id)
    bot.delete_message(m.chat.id, reply.message_id)
    if m.from_user.id != 1448333343:
        bot.forward_message(developer_id, m.chat.id,m.message_id)
@bot.message_handler(commands=['start'], chat_types =["private"])
def handle_start(message):
    UP, CPU, RAM, DISK = bot_sys_stats()
    user_id = message.from_user.id

    idd = message.from_user.id
    id = message.from_user.id
    f2 = message.from_user.first_name
    t2 = message.from_user.username
    id_o = message.chat.id
    mention = f"[{f2}](tg://user?id={idd})"
    divfirst_name = bot.get_chat(1448333343).first_name
    botname = bot.get_me().first_name
    botusername = bot.get_me().username
    with open(channels_file, 'r') as file:
        channels_data = json.load(file)
        channel_ids = channels_data['channel_ids']

    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = []

    for ch in channel_ids:
        ch_tit = bot.get_chat(ch).title
        ch_user = bot.get_chat(ch).username
        invite_link = bot.export_chat_invite_link(ch)
        if not is_user_subscribed(user_id, ch):
            button = types.InlineKeyboardButton(text=ch_tit, url=invite_link)
            buttons.append(button)

    if buttons:
        buttons.append(types.InlineKeyboardButton(text="تم", callback_data="done"))
        markup.add(*buttons)
        bot.reply_to(message, "أنت لم تشترك في القنوات المطلوبة. الرجاء الاشتراك في جميع القنوات المطلوبة لاستخدام هذا البوت.", reply_markup=markup)
    else:
        save_user_subscription(user_id)
        startkey = types.InlineKeyboardMarkup()
        dev = types.InlineKeyboardButton("• 𝗗𝗘𝗩 •",url=f'tg://user?id=1448333343')
        ch = types.InlineKeyboardButton("• 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 •",url='https://t.me/Anime1Forest')
        gr = types.InlineKeyboardButton("• 𝐎𝐔𝐑 𝐂𝐇𝐀𝐓 •",url='https://t.me/AnimeForestgroup')
        sug = types.InlineKeyboardButton("• التواصل مع المطور•",callback_data='SUG')
        search_button = types.InlineKeyboardButton('• بحث عن الأنمي •', callback_data='search')
        profile_button = types.InlineKeyboardButton('• 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 •', callback_data='profile')
        startkey.add(search_button, profile_button)
        startkey.add(dev,ch)
        startkey.add(gr,sug)
        bot.send_photo(message.chat.id,start_photo,caption=f"""
⿻ أوهايو {mention} 👋🏻🎌.
⿻ أهلا بك في بوت ↤ ❲ [{botname}](https://t.me/{botusername}) ❳  .
⿻ أرسل اسم الانمي لعرض النتائج .
⿻ اضغط علي زر ( بحث عن الانمي ) وأرسل حرف الانمي لعرض النتائج .
⿻ يمكنك استخدام امر /ai + (الوصف) لتوليد صور بالذكاء الاصطناعي .
⿻ مطور البوت  ↤ ❲ [{divfirst_name}](https://t.me/YUUI4I) ❳  .
⿻ البوت قيد التشغيل من ❲ {UP} ❳ .
""",parse_mode="markdown", reply_markup=startkey)
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.message_handler(commands=['rules'])
def rules(message):
    chat_id = message.chat.id
    group_user = bot.get_chat(chat_id).username
    group_name = bot.get_chat(chat_id).first_name
    rulesphoto = "https://t.me/hohcusc9us/152"
    bot.send_photo(message.chat.id,rulesphoto,f"""
- اهلا بك في جروب  <a href="t.me/{group_user}">{message.chat.title}</a>
القوانين :
- أحترام آدمن والمالك
- يمنع السب تنحظر🔇
- منع نشر الروابط📥
- منع نشر المحتوى اباحي ودموي🔞
- منع ألتحدث بالسياسة والدين❌
- تخرب المجموعة نخرب وجهك
💙بقروب كلنا أصدقاء وتشرفونا❤️
""", parse_mode="HTML", reply_to_message_id=message.message_id)
@bot.message_handler(commands=["quote"], chat_types =["private"])
def ainmesay(message):
    qoute = types.InlineKeyboardMarkup(row_width=3)
    click1 = types.InlineKeyboardButton(text="⁣• اقتباس عشوائي.",  callback_data="randqout")
    click2 = types.InlineKeyboardButton(text="⁣• اقتباس من أنمي محدد.",  callback_data="animeqouet")
    click3 = types.InlineKeyboardButton(text="⁣• اقتباس من شخصية محددة.",  callback_data="chqouet")
    qoute.add(click1,click2)
    qoute.add(click3)
    bot.send_message(message.chat.id,"- اختار من الأزرار أدناه",reply_markup=qoute)
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id, message.message_id)
@bot.message_handler(commands=['avatar'])
def Get(message):
        n = random.randint(2, 10831)
        avanime = "https://t.me/whusdviwhdiw29ehs8dg/" + str(n)
        id = message.from_user.id
        avtar = types.InlineKeyboardMarkup(row_width=3)
        chng = types.InlineKeyboardButton("تغيير🔄", callback_data=f"HERE:{message.from_user.id}")
        avtar.add(chng)
        try:
            bot.send_photo(message.chat.id, avanime, reply_markup=avtar,reply_to_message_id=message.message_id)
            if message.from_user.id != 1448333343:
                    bot.forward_message(developer_id, message.chat.id, message.message_id)
        except:
            n+= 1
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_photo(message.chat.id, avanime, reply_markup=avtar,reply_to_message_id=message.message_id)

@bot.message_handler(commands=['news'], chat_types =["private"])
def News(message):
    try:

        j = requests.get("https://www.crunchyroll.com/ar/news")
        soup = BeautifulSoup(j.content, 'html.parser')
        k = soup.find("p", {'dir': 'rtl'}).text  ##1st news

        all = "\n       ◎ ─━───━─ 𖡦─━───━─ ◎\n - ".join(
            re.findall("<p dir=\"rtl\">(.*?)</p>", str(soup)))

        if len(all) > 4096:
            for x in range(322, len(all), 4096):
                bot.reply_to(message, all[x:x + 4096])
        if len(all) < 4096:
            for y in range(322, len(all), 4096):
                bot.reply_to(message, all[y:y + 4096])

        if message.from_user.id != 1448333343:
            bot.forward_message(developer_id, message.chat.id, message.message_id)

    except Exception as e:
        bot.send_message(developer_id, f'{e}\nError on line {sys.exc_info()[-1].tb_lineno}')
        bot.send_message(message.chat.id, "حدث خطأ")
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.message_handler(commands=['anime','search'], chat_types =["private"])
def handle_anime_command(message):
    reply = types.ForceReply(selective=True)
    bot.reply_to(message, 'ارسل الحرف لتري الانميات المتاحه', reply_markup=reply)
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.message_handler(commands=['admin'], chat_types =["private"])
def handle_admin(message):
    with open('database/subscribed_users.json', 'r') as file:
        data = json.load(file)
        count = len(data['users'])

    user_id = message.from_user.id
    if user_id == developer_id or user_id in get_admins():
        markup = types.InlineKeyboardMarkup(row_width=2)
        sub = types.InlineKeyboardButton(text=f'عدد المشتركين : {count} .', callback_data='sub')
        broadcast_button = types.InlineKeyboardButton("إذاعة", callback_data="broadcast")
        broadcast_pin = types.InlineKeyboardButton('أذاعه بالتثبيت .', callback_data="broadcast_pin")
        forward_button = types.InlineKeyboardButton("توجيه", callback_data="forward")
        add_channel_button = types.InlineKeyboardButton("إضافة قناة", callback_data="addchannel")
        view_channels_button = types.InlineKeyboardButton("عرض قنوات الاشتراك الإجباري", callback_data="viewchannels")
        delete_channel_button = types.InlineKeyboardButton("حذف قناة الاشتراك الإجباري", callback_data="deletechannel")
        backup_button = types.InlineKeyboardButton("نسخة احتياطية للمشتركين", callback_data="backup")
        backup_data = types.InlineKeyboardButton("نسخة احتياطية للداتا", callback_data="backupdata")
        add_admin_button = types.InlineKeyboardButton("إضافة مشرف", callback_data="addadmin")
        view_admins_button = types.InlineKeyboardButton("عرض المشرفين", callback_data="viewadmins")
        delete_admin_button = types.InlineKeyboardButton("حذف مشرف", callback_data="deleteadmin")
        code = telebot.types.InlineKeyboardButton(f'تغير الكود', callback_data=f'code')
        code2 = telebot.types.InlineKeyboardButton(f'مسح الصور', callback_data=f'reset_all_img')
        code3 = telebot.types.InlineKeyboardButton(f'مسح الانذارات', callback_data=f'reset_all_war')

        markup.add(sub,backup_button)
        markup.add(broadcast_button,broadcast_pin,add_channel_button,view_channels_button, delete_channel_button, forward_button, add_admin_button, view_admins_button, delete_admin_button,backup_data)
        markup.add(code,code2,code3)
        bot.reply_to(message, "اختر الإجراء المطلوب:", reply_markup=markup)
    else:
        bot.reply_to(message, "عذرًا، هذا الأمر مخصص للمشرفين والمطور فقط.")
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.message_handler(commands=['id', 'Id'])
def id(message):
    user = message.from_user.username
    id = message.from_user.id
    bio = bot.get_chat(message.from_user.id).bio
    typ = message.chat.type
    dat = message.date
    fr = message.from_user.first_name
    now = datetime.now()
    a = (now.strftime('%I:%M %p'))

    user_profile = bot.get_user_profile_photos(id)
    if user_profile.total_count == 0:
        bot.send_message(message.chat.id,
                         f""" ╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{message.from_user.id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}""", parse_mode="HTML", reply_to_message_id=message.message_id)

    if user_profile.total_count != 0:
        # yess profile
        bot.send_photo(message.chat.id,user_profile.photos[0][0].file_id,
                           f""" ╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{message.from_user.id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}""", parse_mode="HTML", reply_to_message_id=message.message_id)
    if message.from_user.id != 1448333343:
        bot.forward_message(developer_id, message.chat.id,message.message_id)
@bot.channel_post_handler(func=lambda message: True)
def repeat_all_messages(message):

    if message.chat.id == -1001827472195 :
        with open('database/subscribed_users.json', 'r') as file:
            data = json.load(file)
            allowed_ids = data['users']
        for user_id in allowed_ids:
            sent_message = bot.forward_message(user_id, message.chat.id, message.message_id)
            bot.pin_chat_message(chat_id=user_id, message_id=sent_message.message_id)
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    global id
    if message.chat.type == "private":
        current_page[message.from_user.id] = 1
        id = message.from_user.id
        user_id = message.from_user.id
        with open(channels_file, 'r') as file:
            channels_data = json.load(file)
            channel_ids = channels_data['channel_ids']
        markup = types.InlineKeyboardMarkup(row_width=1)
        buttons = []
        for ch in channel_ids:
            ch_tit = bot.get_chat(ch).title
            ch_user = bot.get_chat(ch).username
            invite_link = bot.export_chat_invite_link(ch)
            if not is_user_subscribed(user_id, ch):
                button = types.InlineKeyboardButton(text=ch_tit, url=invite_link)
                buttons.append(button)
        if buttons:
            buttons.append(types.InlineKeyboardButton(text="تم", callback_data="done"))
            markup.add(*buttons)
            bot.reply_to(message, "أنت لم تشترك في القنوات المطلوبة. الرجاء الاشتراك في جميع القنوات المطلوبة لاستخدام هذا البوت.", reply_markup=markup)
        else:

            save_user_subscription(user_id)
            if message.reply_to_message and message.reply_to_message.text == 'ارسل الحرف لتري الانميات المتاحه':
                sear = bot.send_message(chat_id=message.chat.id, text="🔎")
                with open("database/witanime.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                anime_name2 = message.text.lower()
                anime_name2 = message.text.lower()[0]  # الحرف الأول من رسالة المستخدم
                filtered_animes = [anime for anime in data if anime["Title"].lower().startswith(anime_name2)]
                if filtered_animes:
                    responseee = f"قائمة ببعض الأنميات التي تبدأ بحرف {anime_name2}:"
                    for anime in filtered_animes:
                        responseee += f"\n- `{anime['Title']}`"
                    # تقسيم النص إلى أسطر
                    response_lines = responseee.split('\n')
                    # تجميع الأسطر في رسائل مجمعة
                    messages = []
                    temp_message = ""
                    for line in response_lines:
                        temp_message += line + "\n"
                        if len(temp_message.split('\n')) >= 20:
                            messages.append(temp_message)
                            temp_message = ""
                    # إرسال رسائل مجمعة
                    for message_text in messages:
                        bot.delete_message(message.chat.id, sear.message_id)
                        bot.send_message(chat_id=message.chat.id, text=message_text, parse_mode="markdown")
                else:
                    responseee = f"عذرًا، لم يتم العثور على أي أنمي يبدأ بحرف {anime_name2}."
                    bot.delete_message(message.chat.id,  sear.message_id)
                    bot.send_message(chat_id=message.chat.id, text=responseee, parse_mode="markdown")

            elif message.text:
                sear = bot.send_message(chat_id=message.chat.id, text="🔎")
                with open("database/witanime.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                anime_name = message.text.lower()
                closest_animes = process.extractBests(anime_name, [title.lower() for anime in data for title in anime['names']], score_cutoff=80, limit=30)
                if closest_animes:
                    response = f"نتائج البحث عن ❲ {anime_name} ❳"
                    keyboard = InlineKeyboardMarkup()
                    added_titles = set()  # مجموعة لتتبع العناوين المضافة
                    sorted_animes = sorted(data, key=lambda x: x['Title'].lower())  # ترتيب الأفلام بالترتيب الأبجدي
                    for anime in sorted_animes:
                        for title in anime['names']:
                            if title.lower() in [match.lower() for match, score in closest_animes]:
                                tit = anime['Title']
                                if tit not in added_titles:  # التحقق من عدم تكرار العناوين
                                    button = InlineKeyboardButton(anime['Title'], callback_data=f"¥{tit}")
                                    keyboard.add(button)
                                    added_titles.add(tit)  # إضافة العنوان إلى المجموعة المضافة
                    bot.delete_message(message.chat.id,  sear.message_id)
                    bot.send_message(chat_id=message.chat.id, text=response, reply_markup=keyboard)
                else:
                    bot.delete_message(message.chat.id,  sear.message_id)
                    bot.send_message(chat_id=message.chat.id, text="عذرًا، لم يتم العثور على نتائج مطابقة.")
        if message.from_user.id != 1448333343:
            bot.forward_message(developer_id, message.chat.id,message.message_id)
    if message.text == "المطور" or message.text == "مطور" or message.text == "المبرمج":
            p3 = types.InlineKeyboardMarkup()
            e4 = types.InlineKeyboardButton(text="المطور .", url="tg://user?id=1448333343")
            p3.add(e4)
            botname = bot.get_me().first_name
            botusername = bot.get_me().username
            divfirst_name = bot.get_chat(1448333343).first_name
            bio = bot.get_chat(1448333343).bio
            h = f"""
• ❲ N𝐚𝐦𝐞 𝐛𝐨𝐭 ↦ [{botname}](https://t.me/{botusername}) ❳
━━━━━━━━━━━
- N𝐚𝐦𝐞 ↦ [{divfirst_name}](https://t.me/YUUI4I)
- B𝐢𝐨 ↦ {bio}"""
            bot.send_photo(message.chat.id,photo="https://telegra.ph//file/9171b9ddd4ff3ce53ff62.jpg",caption={h},
                           parse_mode="markdown",
                           reply_markup=p3,
                           reply_to_message_id=message.message_id)

    if message.chat.type == "supergroup" or message.chat.type == "group":
        if any(word in message.text for word in banned_words):
            # إرسال تحذير للمستخدم
            mention = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
            bot.delete_message(message.chat.id, message.id)
            bot.send_photo(message.chat.id,photo="https://telegra.ph//file/ff7b9f02ae3a97489cd5c.jpg",caption=f" عيب ❲{mention}❳", parse_mode="markdown")
        msg = message.text.split()
        user = message.from_user.username
        id = message.from_user.id
        bio = bot.get_chat(message.from_user.id).bio
        typ = message.chat.type
        fr = message.from_user.first_name
        now = datetime.now()
        a = (now.strftime('%I:%M %p'))
        if msg[0].lower() in ["id","ايدي","ا"]:
            user_profile = bot.get_user_profile_photos(id)
            if user_profile.total_count == 0:
                bot.send_message(message.chat.id,
                                 f""" ╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{message.from_user.id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}""", parse_mode="HTML", reply_to_message_id=message.message_id)
            if user_profile.total_count != 0:
                bot.send_photo(message.chat.id,user_profile.photos[0][0].file_id,
                               f""" ╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{message.from_user.id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}""", parse_mode="HTML",reply_to_message_id=message.message_id)
        if message.text == "كشف":
            user = message.reply_to_message.from_user.username
            id = message.reply_to_message.from_user.id
            bio = bot.get_chat(message.reply_to_message.from_user.id).bio
            typ = message.chat.type
            fr = message.reply_to_message.from_user.first_name
            now = datetime.now()
            a = (now.strftime('%I:%M %p'))
            if message.reply_to_message:
                user_profile = bot.get_user_profile_photos(id)
                if user_profile.total_count == 0:
                    bot.send_message(message.chat.id, f""" ╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={id}">{fr}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}""", parse_mode="HTML", reply_to_message_id=message.message_id)
                if user_profile.total_count != 0:
                    bot.send_photo(message.chat.id,user_profile.photos[0][0].file_id,f"""
╭━━❰𝐔𝐒𝐄𝐑 𝐈𝐍𝐅𝐎𝐑𝐌𝐀𝐓𝐈𝐎𝐍❱━━➣
┣⪼  𝐍𝐀𝐌𝐄 ⌯ <a href="tg://user?id={id}">{fr}</a>
┣⪼  𝐔𝐒𝐄𝐑 ⌯ @{user}
┣⪼  𝐈𝐃 ⌯ <code>{id}</code>
┣⪼  𝐓𝐘𝐏𝐄 ⌯ {typ}
┣⪼  𝐃𝐀𝐓𝐄 𝐌𝐒𝐆 ⌯ {a}
┣⪼  {bio}
""", parse_mode="HTML",reply_to_message_id=message.message_id)
        if message.text == 'كت' or message.text == 'كت تويت' or message.text == 'kt' or message.text == 'kt twitt' or  message.text == 'اسئله' or message.text == 'اسئلة':
            typekt = random.choice(game_kt_twitt)
            global htr
            bot.reply_to(message, f'{typekt}')
        if "قولي" in message.text:
            qouly = "قولي"
            try:
                i = message.text.split(qouly,1)[1]
                bot.reply_to(message, i)
            except:
                pass
        if message.text == 'بوت' or message.text == 'بوته' :
            typekt = random.choice(rd_el_bot1)
            global htr
            bot.reply_to(message, f'{typekt}')
        if message.text == 'الاسرع' and message.chat.type == 'supergroup':
            game_1(message)
        if message.text == 'انمي' or message.text == 'صور' and message.chat.type == 'supergroup' :
            game_2(message)
        if message.text == 'ايموجي' and message.chat.type == 'supergroup' :
            game_3(message)
        if message.text == 'اعلام' and message.chat.type == 'supergroup' :
            game_4(message)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global current_page
    global response
    global title
    global episodes
    global user_id
    user_id = call.from_user.id
    if call.data == "randqout":
        try:
            anmesay = requests.get(f"https://animechan.vercel.app/api/random").json()
            name = anmesay['anime']
            say = anmesay['character']
            quo = anmesay['quote']
            ch = "@Anime1Forest"
            translator = Translator()
            translation = translator.translate(f"{quo}", dest="ar")
            bot.answer_callback_query(call.id, show_alert=False)
            bot.send_message(call.message.chat.id,f"""
═══════ ≪ °❈° ≫ ═══════
⛩┇› A Random Quote Was Found For You
⛩┇› Anime : {name} .
⛩┇› Say : {say} .
⛩┇› Quote : \n`{quo}`
        ══════════════
⛩┇› أخترت لك إقتباس 🗣
⛩┇› من أنمي : {name} .
⛩┇› القائل : {say} .
⛩┇› الأقتباس :\n `{translation.text}` .
═══════ ≪ °❈° ≫ ═══════
""",parse_mode="markdown")
        except:
            bot.send_message(call.message.chat.id,"حدث خطأ")
    if call.data == "animeqouet":
        bot.answer_callback_query(call.id, show_alert=False)
        mesgg=bot.send_message(call.message.chat.id,"- أرسل اسم الأنمي .\n- يرجي كتابة اسم الأنمي بلغة الأنجليزية .")
        bot.register_next_step_handler(mesgg, animeee)
    if call.data == "chqouet":
        bot.answer_callback_query(call.id, show_alert=False)
        mesgg = bot.send_message(call.message.chat.id, "- أرسل اسم الشخصية\n- يرجي كتابة اسم الشخصية بالغة الأنجليزية .")
        bot.register_next_step_handler(mesgg, character)
    if call.data == "SUG":
        id = call.from_user.id
        f2 = call.from_user.first_name
        t2 = call.from_user.username
        sug = types.InlineKeyboardMarkup()
        a2 = types.InlineKeyboardButton("• ارسال رسالة •", callback_data="suggg")
        a15 = types.InlineKeyboardButton("• الغاء •", callback_data="cancel")
        sug.add(a2)
        sug.add(a15)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, text="-اهلا بك عزيزي\n-ارسل رسالتك وسيتم الرد عليك في اقرب وقت 😊",
                            reply_markup=sug)
    if call.data == "suggg":
        mesgg = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text= "- حسناً عزيزي يرجي ارسل رسالتك الان ❤️")
        bot.register_next_step_handler(mesgg, st)

    if call.data == "a13":
        a13(call.message)

    if call.data.startswith("HERE"):
        user_id = int(call.data.split(":")[1])
        if not call.from_user.id == user_id:
            bot.answer_callback_query(call.id, f"- الامر ليس لك يرجي ارسال /avatar لتري الافاتارات",
                                        show_alert=True)
            return
        else:
            try:
                n = random.randint(2, 10831)
                avanime = "https://t.me/whusdviwhdiw29ehs8dg/" + str(n)
                avtar = types.InlineKeyboardMarkup(row_width=3)
                chng = types.InlineKeyboardButton("تغيير🔄", callback_data=f"HERE:{call.from_user.id}")
                avtar.add(chng)
                bot.answer_callback_query(call.id, show_alert=False)
                bot.edit_message_media(media=types.InputMedia(type='photo', media=avanime),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=avtar)
            except:
                n+= 1
                bot.delete_message(call.chat.id, call.message_id)
                bot.send_photo(call.chat.id, avanime, reply_markup=avtar,reply_to_message_id=call.message_id)

    with open(channels_file, 'r') as file:
        channels_data = json.load(file)
        channel_ids = channels_data['channel_ids']
    if call.data == "done":
        if all(is_user_subscribed(user_id, ch) for ch in channel_ids):
            save_user_subscription(user_id)
            bot.answer_callback_query(call.id, "تم!")
            bot.delete_message(call.message.chat.id, call.message.message_id)
            UP, CPU, RAM, DISK = bot_sys_stats()
            user_id = call.from_user.id
            idd = call.from_user.id
            id = call.from_user.id
            f2 = call.from_user.first_name
            t2 = call.from_user.username
            id_o = call.chat.id
            mention = f"[{f2}](tg://user?id={idd})"
            divfirst_name = bot.get_chat(1448333343).first_name
            botname = bot.get_me().first_name
            botusername = bot.get_me().username
            startkey = types.InlineKeyboardMarkup()
            dev = types.InlineKeyboardButton("• 𝗗𝗘𝗩 •",url=f'tg://user?id=1448333343')
            ch = types.InlineKeyboardButton("• 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 •",url='https://t.me/Anime1Forest')
            gr = types.InlineKeyboardButton("• 𝐎𝐔𝐑 𝐂𝐇𝐀𝐓 •",url='https://t.me/AnimeForestgroup')
            sug = types.InlineKeyboardButton("• التواصل مع المطور•",callback_data='SUG')
            search_button = types.InlineKeyboardButton('• بحث عن الأنمي •', callback_data='search')
            profile_button = types.InlineKeyboardButton('• 𝐏𝐑𝐎𝐅𝐈𝐋𝐄 •', callback_data='profile')
            startkey.add(search_button, profile_button)
            startkey.add(dev,ch)
            startkey.add(gr,sug)
            bot.send_photo(call.message.chat.idstart_photo,caption=f"""
⿻ أوهايو {mention} 👋🏻🎌.
⿻ أهلا بك في بوت ↤ ❲ [{botname}](https://t.me/{botusername}) ❳  .
⿻ أرسل اسم الانمي لعرض النتائج .
⿻ اضغط علي زر ( بحث عن الانمي ) وأرسل حرف الانمي لعرض النتائج .
⿻ مطور البوت  ↤ ❲ [{divfirst_name}](https://t.me/YUUI4I) ❳  .
⿻ البوت قيد التشغيل من ❲ {UP} ❳ .
""",parse_mode="markdown", reply_markup=startkey)
        else:
            bot.answer_callback_query(call.id, "أنت لم تشترك في جميع القنوات المطلوبة بعد.", show_alert=True)

    with open("database/witanime.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    found_anime = None
    if call.data == "search":
        reply = types.ForceReply(selective=True)
        bot.send_message(chat_id=call.message.chat.id, text='ارسل الحرف لتري الانميات المتاحه', reply_markup=reply)
    if "@" in call.data:
        watched = call.data.split("@")
        watchedanime = watched[1]
        user_id = call.from_user.id
        username = call.from_user.username
        with open("database/database.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        if str(user_id) in users:
            if "watched" in users[str(user_id)]:
                if watchedanime in users[str(user_id)]["watched"]:
                    users[str(user_id)]["watched"].remove(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                else:
                    users[str(user_id)]["watched"].append(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
            else:
                users[str(user_id)]["watched"] = [watchedanime]
        else:
            users[str(user_id)] = {"watched": [watchedanime]}

        with open("database/database.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        keyboard = create_keyboard(title,episodes,current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    elif "#" in call.data:
        watched = call.data.split("#")
        watchedanime = watched[1]
        user_id = call.from_user.id
        username = call.from_user.username
        with open("database/database.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        if str(user_id) in users:
            if "watching" in users[str(user_id)]:
                if watchedanime in users[str(user_id)]["watching"]:
                    users[str(user_id)]["watching"].remove(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)

                else:
                    users[str(user_id)]["watching"].append(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
            else:
                users[str(user_id)]["watching"] = [watchedanime]
        else:
            users[str(user_id)] = {"watching": [watchedanime]}

        with open("database/database.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    elif "%" in call.data:
        watched = call.data.split("%")
        watchedanime = watched[1]
        user_id = call.from_user.id
        username = call.from_user.username
        with open("database/database.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        if str(user_id) in users:
            if "favorite" in users[str(user_id)]:
                if watchedanime in users[str(user_id)]["favorite"]:
                    users[str(user_id)]["favorite"].remove(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                else:
                    users[str(user_id)]["favorite"].append(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
            else:
                users[str(user_id)]["favorite"] = [watchedanime]
        else:
            users[str(user_id)] = {"favorite": [watchedanime]}

        with open("database/database.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    elif "$" in call.data:
        watched = call.data.split("$")
        watchedanime = watched[1]
        user_id = call.from_user.id
        username = call.from_user.username
        with open("database/database.json", "r", encoding="utf-8") as file:
            users = json.load(file)

        if str(user_id) in users:
            if "upcoming" in users[str(user_id)]:
                if watchedanime in users[str(user_id)]["upcoming"]:
                    users[str(user_id)]["upcoming"].remove(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                else:
                    users[str(user_id)]["upcoming"].append(watchedanime)
                    bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
            else:
                users[str(user_id)]["upcoming"] = [watchedanime]
        else:
            users[str(user_id)] = {"upcoming": [watchedanime]}
        with open("database/database.json", "w", encoding="utf-8") as file:
            json.dump(users, file, indent=4)
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if ">" in call.data:
        watched = call.data.split(">")
        watchedanime = watched[1]
        user_id = call.from_user.id

        with open("database/rate.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        rating = "onestar"  # تعيين التقييم هنا (مثال: onestar)

        # Check if user ID is already in any of the other rating lists
        other_ratings = ["twostar", "threestar", "fourstar", "fivestar"]
        for other_rating in other_ratings:
            if any(d.get(other_rating) for d in data):
                for item in data:
                    if item.get(other_rating):
                        if item[other_rating].get(watchedanime):
                            if str(user_id) in item[other_rating][watchedanime]:
                                bot.answer_callback_query(call.id, "لا يمكنك التصويت مرة أخرى", show_alert=True)
                                return

        # Continue with original code
        if not any(d.get(rating) for d in data):
            data.append({rating: {watchedanime: [str(user_id)]}})
            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
        else:
            for item in data:
                if item.get(rating):
                    if item[rating].get(watchedanime):
                        if str(user_id) in item[rating][watchedanime]:
                            item[rating][watchedanime].remove(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                            break
                        else:
                            item[rating][watchedanime].append(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                            break
                    else:
                        item[rating][watchedanime] = [str(user_id)]
                        bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                        break
            else:
                data.append({rating: {watchedanime: [str(user_id)]}})
                bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

        with open("database/rate.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if "*" in call.data:
        watched = call.data.split("*")
        watchedanime = watched[1]
        user_id = call.from_user.id

        with open("database/rate.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        rating = "threestar"  # تعيين التقييم هنا (مثال: onestar)

        # Check if user ID is already in any of the other rating lists
        other_ratings = ["onestar", "twostar", "fourstar", "fivestar"]
        for other_rating in other_ratings:
            if any(d.get(other_rating) for d in data):
                for item in data:
                    if item.get(other_rating):
                        if item[other_rating].get(watchedanime):
                            if str(user_id) in item[other_rating][watchedanime]:
                                bot.answer_callback_query(call.id, "لا يمكنك التصويت مرة أخرى", show_alert=True)
                                return

        # Continue with original code
        if not any(d.get(rating) for d in data):
            data.append({rating: {watchedanime: [str(user_id)]}})
            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
        else:
            for item in data:
                if item.get(rating):
                    if item[rating].get(watchedanime):
                        if str(user_id) in item[rating][watchedanime]:
                            item[rating][watchedanime].remove(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                            break
                        else:
                            item[rating][watchedanime].append(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                            break
                    else:
                        item[rating][watchedanime] = [str(user_id)]
                        bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                        break
            else:
                data.append({rating: {watchedanime: [str(user_id)]}})
                bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

        with open("database/rate.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if "؟" in call.data:
        watched = call.data.split("؟")
        watchedanime = watched[1]
        user_id = call.from_user.id

        with open("database/rate.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        rating = "twostar"  # تعيين التقييم هنا (مثال: onestar)

        # Check if user ID is already in any of the other rating lists
        other_ratings = ["onestar", "threestar", "fourstar", "fivestar"]
        for other_rating in other_ratings:
            if any(d.get(other_rating) for d in data):
                for item in data:
                    if item.get(other_rating):
                        if item[other_rating].get(watchedanime):
                            if str(user_id) in item[other_rating][watchedanime]:
                                bot.answer_callback_query(call.id, "لا يمكنك التصويت مرة أخرى", show_alert=True)
                                return

        # Continue with original code
        if not any(d.get(rating) for d in data):
            data.append({rating: {watchedanime: [str(user_id)]}})
            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
        else:
            for item in data:
                if item.get(rating):
                    if item[rating].get(watchedanime):
                        if str(user_id) in item[rating][watchedanime]:
                            item[rating][watchedanime].remove(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                            break
                        else:
                            item[rating][watchedanime].append(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                            break
                    else:
                        item[rating][watchedanime] = [str(user_id)]
                        bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                        break
            else:
                data.append({rating: {watchedanime: [str(user_id)]}})
                bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

        with open("database/rate.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if "<" in call.data:
        watched = call.data.split("<")
        watchedanime = watched[1]
        user_id = call.from_user.id

        with open("database/rate.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        rating = "fourstar"  # تعيين التقييم هنا (مثال: onestar)

        # Check if user ID is already in any of the other rating lists
        other_ratings = ["onestar", "twostar", "threestar", "fivestar"]
        for other_rating in other_ratings:
            if any(d.get(other_rating) for d in data):
                for item in data:
                    if item.get(other_rating):
                        if item[other_rating].get(watchedanime):
                            if str(user_id) in item[other_rating][watchedanime]:
                                bot.answer_callback_query(call.id, "لا يمكنك التصويت مرة أخرى", show_alert=True)
                                return

        # Continue with original code
        if not any(d.get(rating) for d in data):
            data.append({rating: {watchedanime: [str(user_id)]}})
            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
        else:
            for item in data:
                if item.get(rating):
                    if item[rating].get(watchedanime):
                        if str(user_id) in item[rating][watchedanime]:
                            item[rating][watchedanime].remove(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                            break
                        else:
                            item[rating][watchedanime].append(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                            break
                    else:
                        item[rating][watchedanime] = [str(user_id)]
                        bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                        break
            else:
                data.append({rating: {watchedanime: [str(user_id)]}})
                bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

        with open("database/rate.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if "~" in call.data:
        watched = call.data.split("~")
        watchedanime = watched[1]
        user_id = call.from_user.id

        with open("database/rate.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        rating = "fivestar"  # تعيين التقييم هنا (مثال: onestar)

        # Check if user ID is already in any of the other rating lists
        other_ratings = ["onestar", "twostar", "threestar", "fourstar"]
        for other_rating in other_ratings:
            if any(d.get(other_rating) for d in data):
                for item in data:
                    if item.get(other_rating):
                        if item[other_rating].get(watchedanime):
                            if str(user_id) in item[other_rating][watchedanime]:
                                bot.answer_callback_query(call.id, "لا يمكنك التصويت مرة أخرى", show_alert=True)
                                return

        # Continue with original code
        if not any(d.get(rating) for d in data):
            data.append({rating: {watchedanime: [str(user_id)]}})
            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)
        else:
            for item in data:
                if item.get(rating):
                    if item[rating].get(watchedanime):
                        if str(user_id) in item[rating][watchedanime]:
                            item[rating][watchedanime].remove(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الازاله من القائمه", show_alert=True)
                            break
                        else:
                            item[rating][watchedanime].append(str(user_id))
                            bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                            break
                    else:
                        item[rating][watchedanime] = [str(user_id)]
                        bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه", show_alert=True)

                        break
            else:
                data.append({rating: {watchedanime: [str(user_id)]}})
                bot.answer_callback_query(call.id, "تمت الاضافه الي القائمه")

        with open("database/rate.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
        time.sleep(.1)
    if "profile" in call.data:
        user_id = call.from_user.id
        database = read_database()

        watched_anime = database.get(str(user_id), {}).get('watched', [])
        watching_anime = database.get(str(user_id), {}).get('watching', [])
        favorite_anime = database.get(str(user_id), {}).get('favorite', [])
        upcoming_anime = database.get(str(user_id), {}).get('upcoming', [])

        markup = telebot.types.InlineKeyboardMarkup(row_width=1)
        watched_button = telebot.types.InlineKeyboardButton(f'انميات تمت مشاهدتها ({len(watched_anime)})', callback_data='watched')
        watching_button = telebot.types.InlineKeyboardButton(f'انميات اشاهدها حاليا ({len(watching_anime)})', callback_data='watching')
        favorite_button = telebot.types.InlineKeyboardButton(f'انميات المفضلة ({len(favorite_anime)})', callback_data='favorite')
        upcoming_button = telebot.types.InlineKeyboardButton(f'انميات اشاهدها لاحقا ({len(upcoming_anime)})', callback_data='upcoming')
        markup.add(watched_button, watching_button, favorite_button, upcoming_button)
        profile_pic = "https://telegra.ph/anyia-05-21"
        bot.send_photo(call.message.chat.id,profile_pic,caption="مرحبًا بك في الملف الشخصي!\nيرجى اختيار الخيار المناسب:", reply_markup=markup)
    if call.data.startswith("watched"):
        user_id = call.from_user.id
        database = read_database()
        watched_anime = database[str(user_id)]['watched']
        if watched_anime:
            markup = types.InlineKeyboardMarkup(row_width=1)
            buttons = [types.InlineKeyboardButton(index, callback_data=f'¥{index}') for index in watched_anime]
            markup.add(*buttons)
            bot.send_message(call.message.chat.id, f"انميات تمت مشاهدتها ({len(watched_anime)}):\nيرجى اختيار أحد الأنميات:", reply_markup=markup)

        else:
            bot.send_message(call.message.chat.id,"لا يوجد أنميات في القائمة .")
    if call.data.startswith("watching"):
        user_id = call.from_user.id
        database = read_database()
        watched_anime = database[str(user_id)]['watching']
        if watched_anime:
            markup = types.InlineKeyboardMarkup(row_width=1)
            buttons = [types.InlineKeyboardButton(index, callback_data=f'¥{index}') for index in watched_anime]
            markup.add(*buttons)
            bot.send_message(call.message.chat.id, f"انميات اشاهدها ({len(watched_anime)}):\nيرجى اختيار أحد الأنميات:", reply_markup=markup)

        else:
            bot.send_message(call.message.chat.id,"لا يوجد أنميات في القائمة .")
    if call.data.startswith("favorite"):
        user_id = call.from_user.id
        database = read_database()
        watched_anime = database[str(user_id)]['favorite']
        if watched_anime:
            markup = types.InlineKeyboardMarkup(row_width=1)
            buttons = [types.InlineKeyboardButton(index, callback_data=f'¥{index}') for index in watched_anime]
            markup.add(*buttons)
            bot.send_message(call.message.chat.id, f"انميات مفضلة ({len(watched_anime)}):\nيرجى اختيار أحد الأنميات:", reply_markup=markup)

        else:
            bot.send_message(call.message.chat.id,"لا يوجد أنميات في القائمة .")
    if call.data.startswith("upcoming"):
        user_id = call.from_user.id
        database = read_database()
        watched_anime = database[str(user_id)]['upcoming']
        if watched_anime:
            markup = types.InlineKeyboardMarkup(row_width=1)
            buttons = [types.InlineKeyboardButton(index, callback_data=f'¥{index}') for index in watched_anime]
            markup.add(*buttons)
            bot.send_message(call.message.chat.id, f"انميات اشاهدها لاحقا ({len(watched_anime)}):\nيرجى اختيار أحد الأنميات:", reply_markup=markup)

        else:
            bot.send_message(call.message.chat.id, "لا يوجد أنميات في القائمة .")

    if "¥" in call.data:
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        time.sleep(.1)
        nameofanime1 = call.data.split("¥")
        nameofanime = nameofanime1[1]
        for anime in data:
            if nameofanime == anime['Title']:
                found_anime = anime
                break
        if found_anime:
            title = found_anime['Title']
            description = found_anime['Story']
            genres = found_anime['Genres']
            info = found_anime['info']
            image = found_anime['image']
            episodes = found_anime['ep']
            keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)

            response = f"""
⿻ الاسم : ❲{title}❳
⿻ القصة :
    ◎ ─━───━─ 𖡦─━───━─ ◎
    {description}
    ◎ ─━───━─ 𖡦─━───━─ ◎
⿻ التصنيف : {genres}
{info}"""

            bot.send_photo(call.message.chat.id, image, caption=response, reply_markup=keyboard)
    if call.data == "next":
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        current_page[user_id] += 1
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
    if call.data == "nexttt":
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        current_page[user_id] = (len(episodes) + 36 - 1) // 36
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
    elif call.data == "previousss":
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        time.sleep(.1)
        current_page[user_id] = 1
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)
    elif call.data == "previous":
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        time.sleep(.1)
        current_page[user_id] = current_page.get(user_id, 0) - 1
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    reply_markup=keyboard)

    elif call.data == "back_to_main":
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        time.sleep(.1)
        keyboard = create_keyboard(title,episodes, current_page,found_anime,user_id)
        bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                caption=response, reply_markup=keyboard)
    with open("database/witanime.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        for anime in data:
            for episode in episodes:
                if episode['name'] == call.data:
                    bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
                    episode_servers = episode['servers']
                    keyboard2 = InlineKeyboardMarkup(row_width=1)
                    for server in episode_servers:
                        quality = server['quality']
                        button = InlineKeyboardButton("• " + quality + " •", callback_data=f"{episode['name']}|{quality}")
                        keyboard2.add(button)
                    back_button = InlineKeyboardButton("الرجوع للقائمة الرئيسية", callback_data="back_to_main")
                    keyboard2.row(back_button)  # إضافة زر الرجوع في الصف الأخير

                    caption = "اختر جودة الحلقة:"
                    bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                            caption=caption, reply_markup=keyboard2)

                    return
    if "|" in call.data:
        bot.answer_callback_query(call.id, f"أنتظر قليلا ...", show_alert=True)
        time.sleep(.1)
        episode_namee = call.data.split("|")[0]
        quality = call.data.split("|")[1]
        for anime in data:
            for episode in episodes:
                if episode['name'] == episode_namee:
                    for server in episode['servers']:
                        if server['quality'] == quality:
                            episode_servers = server['servers']
                            buttons_per_row = 2  # عدد الأزرار في كل صف
                            buttons_per_column = 3  # عدد الأزرار في كل عمود
                            keyboard3 = InlineKeyboardMarkup(row_width=buttons_per_row)

                            buttons_count = 0
                            row = []
                            for server_link in episode_servers:
                                server_name = server_link['server']
                                server_link = server_link['url']
                                button = InlineKeyboardButton(server_name, url=server_link)
                                row.append(button)
                                buttons_count += 1
                                if buttons_count == buttons_per_row:
                                    keyboard3.row(*row)
                                    row = []
                                    buttons_count = 0
                            if buttons_count > 0:
                                keyboard3.row(*row)
                            back_button = InlineKeyboardButton("الرجوع للقائمة الرئيسية", callback_data="back_to_main")
                            keyboard3.row(back_button)
                            bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                                    caption="اختر سيرفر التحميل :", reply_markup=keyboard3)

                            return
    if call.data == 'reset_all_img':
        if user_id == 1448333343:
            for user in user_data:
                user['photos_used'] = 0
                allowed_ids = user['user_id']
                bot.send_message(allowed_ids,"تم تصفير الصور في أمر الذكاء الاصطناعي")
            save_user_data()
            bot.send_message(call.message.chat.id, text=f"images has been reset for {len(user_data)} users.")
    if call.data == 'reset_all_war':
        if user_id == 1448333343:
            for user in user_data:
                user['warnings'] = 0
                allowed_ids = user['user_id']
                bot.send_message(allowed_ids,"تم تصفير الانذارات أمر الذكاء الاصطناعي")
            save_user_data()
            bot.send_message(call.message.chat.id, text=f"warnings has been reset for {len(user_data)} users.")
    if call.data == 'code':
        mesgg = bot.send_message(call.message.chat.id, text='ارسال الكود الجديد', parse_mode='markdown')
        bot.register_next_step_handler(mesgg, process_code_step)
    if call.data.startswith("confirm"):
        code_api = call.data.split("ك")[1]
        with open('x_prodia_key.txt', 'w') as file:
            file.write(code_api)
        bot.send_message(call.message.chat.id,text='تمت إضافة الكود.')
        bot.delete_message(call.message.chat.id, call.message.message_id)  # Delete the original message
    if call.data == 'cancel':
        bot.send_message(call.message.chat.id, text='تم إلالغاء .')
        bot.delete_message(call.message.chat.id, call.message.message_id)  # Delete the original message
    if "ا" in call.data:
        print(user_processing)
        model = call.data.split("ا")[1]
        id_user = int(call.data.split("ا")[0])
        if call.from_user.id == id_user:
            if user_id in user_processing and user_processing[user_id] == False:
                    bot.answer_callback_query(call.id, 'يتم تنفيذ عملية أخرى حاليًا. يرجى انتظار انتهاء العملية الحالية.', show_alert=True)
                    return
            user_processing[user_id] = False
            print(user_processing)
            if not check_photos_limit(user_id):
                remaining_time = calculate_remaining_time(user_id)
                remaining_time_str = format_remaining_time(remaining_time)
                message = f"لقد بلغت الحد اليومي لعدد الصور البالغ 30 صورة.\n\nالوقت المتبقي: {remaining_time_str}"
                bot.answer_callback_query(call.id, message, show_alert=True)
                bot.send_message(call.message.chat.id, message)
                user_processing[user_id] = False
                print(user_processing)
                return
            bot.answer_callback_query(call.id, f"تمت الإضافة إلى القائمة. يرجى الانتظار.", show_alert=True)
            with open("x_prodia_key.txt", "r") as key_file:
                x_prodia_key = key_file.read().strip()
            payload = {
                "prompt": prompt,
                "steps": 25,
                "cfg_scale": 7,
                "upscale": True,
                "sampler": "Euler",
                "negative_prompt": "badly drawn",
                "aspect_ratio": "square",
                "model": models[model]
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-Prodia-Key": x_prodia_key
            }
            response = requests.post(url, json=payload, headers=headers).text
            if response == "Key Not Recognised":
                bot.send_message(call.message.chat.id, "تم انتهاء صلاحية الكود، يرجى التواصل مع المطور لتحديثه.")
            else:
                result = json.loads(response)
                result2 = result["job"]
                url_check = "https://api.prodia.com/v1/job/" + result2
                headers_check = {
                    "accept": "application/json",
                    "X-Prodia-Key": x_prodia_key
                }
                generating_message = None
                message_sent = False  # متغير يحدد ما إذا تم إرسال الرسالة بالفعل أم لا
                seconds = 0
                while True:
                    time.sleep(1)
                    response_check = requests.get(url_check, headers=headers_check).text
                    check = json.loads(response_check)
                    status = check["status"]
                    if status == "queued":
                        if not message_sent:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=generating_message.message_id, text=f"تمت إضافة طلبك إلى قائمة الانتظار .....")
                            quend = bot.send_message(call.message.chat.id, "✏️")
                            message_sent = True
                    elif status == "succeeded":
                        if generating_message is not None:
                            bot.delete_message(call.message.chat.id, clock.message_id)
                            bot.delete_message(call.message.chat.id, generating_message.message_id)
                        image = "https://images.prodia.xyz/" + result2 + ".png"
                        # زيادة عدد الصور المستخدمة للمستخدم بعد الاستجابة الناجحة
                        increment_photos_used(user_id)
                        user = next((u for u in user_data if u['user_id'] == user_id), None)
                        num_left = user['photos_used']
                        mention = f"[{call.from_user.first_name}](tg://user?id={call.from_user.id})"
                        caption_ai = f"⇜ من 「 {mention} 」 \nتم إكمال الصورة.\nالوصف : {prompt}\nالموديل : {model}\nالوقت المستغرق : {seconds} ث \n تم استخدام {num_left} من 25 صورة"
                        bot.send_photo(call.message.chat.id, photo=image, caption=caption_ai,parse_mode="markdown", reply_to_message_id=call.message.message_id)

                        break
                    elif status == "generating":
                        seconds += 1
                        if generating_message is not None:
                            bot.edit_message_text(chat_id=call.message.chat.id, message_id=generating_message.message_id, text=f"جارٍ توليد الصورة... مضت {seconds} ثانية.")
                        else:
                            generating_message = bot.send_message(call.message.chat.id, f"جارٍ توليد الصورة... مضت {seconds} ثانية.")
                            clock = bot.send_message(call.message.chat.id, "⏳")
                        if message_sent:
                            bot.delete_message(call.message.chat.id, quend.message_id)
                        message_sent = False  # إعادة تعيين المتغير للسماح بإرسال رسالة جديدة في الدورة القادمة
            print(user_processing)
            user_processing[user_id] = True
            print(user_processing)

        else:
            bot.answer_callback_query(call.id, f"- الامر ليس لك",
                                        show_alert=True)
            return

    if user_id == developer_id or user_id in get_admins():
        if call.data == "broadcast_pin":
            # إجراء الإذاعة
            bot.send_message(call.message.chat.id, "قم بإرسال الرسالة للإذاعة. ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, broadcast_message_pin)
        if call.data == "broadcast":
            # إجراء الإذاعة
            bot.send_message(call.message.chat.id,"قم بإرسال الرسالة للإذاعة.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, broadcast_message)
        elif call.data == "forward":
            # إجراء التوجيه
            bot.send_message(call.message.chat.id,"قم بتوجيه الرسالة.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, forward_message)
        elif call.data == "backup":
            # إجراء النسخة الاحتياطية
            bot.answer_callback_query(call.id, "تم حفظ نسخة احتياطية ")
            backup_subscribed_users()
        elif call.data == "backupdata":
            # إجراء النسخة الاحتياطية
            bot.answer_callback_query(call.id, "تم حفظ نسخة احتياطيةل ")
            backup_data()
        elif call.data == "addadmin":
            # إجراء إضافة مشرف
            bot.send_message(call.message.chat.id, "قم بإرسال معرّف المشرف.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, add_admin)
        elif call.data == "viewadmins":
            # إجراء عرض المشرفين
            bot.answer_callback_query(call.id, "جارٍ عرض المشرفين")
            view_admins(call.message)
        elif call.data == "deleteadmin":
            # إجراء حذف مشرف
            bot.send_message(call.message.chat.id,"قم بإرسال معرّف المشرف للحذف.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, delete_admin)
        elif call.data == "addchannel":
            # إجراء إضافة القناة
            bot.send_message(call.message.chat.id, "قم بإرسال معرّف القناة.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, add_channel)
        elif call.data == "viewchannels":
            # إجراء عرض قنوات الاشتراك الإجباري
            view_channels(call.message)
        elif call.data == "deletechannel":
            # إجراء حذف قناة الاشتراك الإجباري
            bot.send_message(call.message.chat.id, "قم بإرسال معرّف القناة للحذف.ارسل `cancel` للالغاء",parse_mode="markdown")
            bot.register_next_step_handler(call.message, delete_channel)
        elif call.data == "sub":
            view_subscribed_users(call.message)
    else:
        bot.answer_callback_query(call.id, "عذرًا، هذا الأمر مخصص للمشرفين والمطور فقط.", show_alert=True)
@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def bot_func(message):
    bot.delete_message(message.chat.id, message.message_id)
    if message.content_type == 'new_chat_members':
        user = message.from_user.username
        id = message.from_user.id
        bio = bot.get_chat(message.from_user.id).bio
        typ = message.chat.type
        fr = message.from_user.first_name
        user_profile = bot.get_user_profile_photos(id)
        chat_id = message.chat.id
        group_user = bot.get_chat(chat_id).username
        group_name = bot.get_chat(chat_id).first_name
        CH_username = bot.get_chat(-1001770331451).username
        CH_name = bot.get_chat(-1001770331451).title
        s = 1
        if user_profile.total_count == 0:
            myFont = ImageFont.truetype('greeting/ar_en.ttf', 60)
            img = Image.open('greeting/cover.jpg')
            I1 = ImageDraw.Draw(img)
            reshaped_text = arabic_reshaper.reshape(fr)
            bidi_text = get_display(reshaped_text)
            I1.text((925, 480), u"{}".format(bidi_text), font=myFont, fill=(19, 44, 108), stroke_width=3,
                    stroke_fill=(19, 44, 108))
            I1.text((922, 477), u"{}".format(bidi_text), font=myFont, fill=(250, 250, 250), stroke_width=3,
                    stroke_fill=(19, 44, 108))
            img.save("greeting/greetingwithoutpfp.jpg")
            try:
                bot.delete_message(message.chat.id, s)
            except: pass
            y = bot.send_photo(message.chat.id,photo=open(r'greeting/greetingwithoutpfp.jpg', 'rb'),caption=f"""
𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 <a href="t.me/{CH_username}">{message.chat.title}</a>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑵𝑨𝑴𝑬  ⌯ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
⿻ 𝐔𝐒𝐄𝐑 ⌯ @{user}
⿻ 𝐈𝐃  ⌯ <code>{message.from_user.id}</code>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑻𝑶 𝑪𝑶𝑵𝑻𝑨𝑪𝑻 𝑻𝑯𝑬 𝑶𝑾𝑵𝑬𝑹 ⌯ <a href="tg://user?id=1448333343">{bot.get_chat(1448333343).first_name}</a>
⿻ 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 ⌯ <a href="t.me/{CH_username}">{CH_name}</a>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑻𝑯𝑬 𝑹𝑼𝑳𝑬𝑺  ⌯ /rules""", parse_mode="HTML")
            s = y.message_id
        if user_profile.total_count != 0:
            file_id = bot.get_user_profile_photos(message.from_user.id).photos[0][-1].file_id
            file_info = bot.get_file(file_id)
            dx = bot.download_file(file_info.file_path)
            with open("greeting/pfp.jpg", "wb") as new_file:
                new_file.write(dx)
            im1 = Image.open('greeting/cover.jpg')
            im2 = Image.open("greeting/pfp.jpg")
            mask1 = Image.open('greeting/mask5.png')
            new_image = im2.resize((297, 297))
            new_image.save('greeting/image.jpg')
            image = Image.open('greeting/image.jpg')
            mask_im = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask_im)
            draw.ellipse((0,0,297, 297), fill=255)
            mask_im.save('greeting/mask_circle2.jpg', quality=95)
            back_im = im1.copy()
            back_im.paste(image,(881,118), mask_im)
            back_im.save('greeting/rocket_pillow_paste.jpg', quality=95)
            myFont = ImageFont.truetype('greeting/ar_en.ttf', 60)
            img = Image.open('greeting/rocket_pillow_paste.jpg')
            I1 = ImageDraw.Draw(img)
            reshaped_text = arabic_reshaper.reshape(fr)
            bidi_text = get_display(reshaped_text)
            I1.text((925, 480), u"{}".format(bidi_text), font=myFont, fill=(19, 44, 108), stroke_width=3,
                    stroke_fill=(19, 44, 108))
            I1.text((922, 477), u"{}".format(bidi_text), font=myFont, fill=(250, 250, 250), stroke_width=3,
                    stroke_fill=(19, 44, 108))
            img.save("greeting/greetingwithpfp.jpg")
            try:
                bot.delete_message(message.chat.id, s)
            except: pass
            bot.send_photo(message.chat.id,photo=open(r'greeting/greetingwithpfp.jpg', 'rb'),caption=f"""
𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 <a href="t.me/{CH_username}">{message.chat.title}</a>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑵𝑨𝑴𝑬  ⌯<a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
⿻ 𝐔𝐒𝐄𝐑 ⌯ @{user}
⿻ 𝐈𝐃  ⌯ <code>{message.from_user.id}</code>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑻𝑶 𝑪𝑶𝑵𝑻𝑨𝑪𝑻 𝑻𝑯𝑬 𝑶𝑾𝑵𝑬𝑹 ⌯ <a href="tg://user?id=1448333343">{bot.get_chat(1448333343).first_name}</a>
⿻ 𝑪𝑯𝑨𝑵𝑵𝑬𝑳 ⌯ <a href="t.me/{CH_username}">{CH_name}</a>
◎ ─━───━─ 𖡦─━───━─ ◎
⿻ 𝑻𝑯𝑬 𝑹𝑼𝑳𝑬𝑺  ⌯ /rules""", parse_mode="HTML")
            s = y.message_id

def game_1(message):
    emoji = choice(EMOJIS)
    re = f"{emoji}"
    t3 = time.time()
    ask = bot.send_message(
        message.chat.id,
        f"اسرع واحد يرسل الايموجي : `{emoji}`",
        reply_to_message_id=message.message_id,
        parse_mode='Markdown'
    )
    bot.register_next_step_handler(ask, check_answer2, re,t3)
def game_2(message):
    celeb = choice(data)
    nameeeee = celeb['name']
    image = celeb['image']
    print(image)
    print(nameeeee)
    x = bot.send_photo(
        message.chat.id,
        image,caption= "ايش اسم شخصية الانمي ؟",reply_to_message_id=message.message_id
    )
    t3 = time.time()
    bot.register_next_step_handler(x, check_answer,t3 ,nameeeee)
def game_3(message):
    A = choice(anime_emoji)
    emo = A['title']
    print(emo)
    ans = A['answers']
    print(ans)
    cor = A['correct']
    re = f"{cor}"
    t3 = time.time()
    # اختيار الإجابات العشوائية
    random_answers = random.sample(ans, len(ans))
    # تنسيق الإجابات في النص
    answers_text = "\n".join([f"- `{answer}`" for answer in random_answers])
    ask = bot.send_message(
        message.chat.id,
        f"""
اسرع واحد يرسل معنى الايموجي {emo}
الإجابات:
{answers_text}
""",
        reply_to_message_id=message.message_id,
        parse_mode='Markdown'
    )
    bot.register_next_step_handler(ask, check_answer2, re, t3)
def game_4(message):
    A = choice(FLAGS)
    ans = A['country']
    emo = A['emoji']
    print(emo)
    print(ans)
    ask = bot.send_message(
        message.chat.id,
        f"اسرع واحد يرسل اسم الدولة {emo}",
        reply_to_message_id=message.message_id
    )
    t3 = time.time()
    re = f"{ans}"
    bot.register_next_step_handler(ask, check_answer3, ans,t3)

###############
def check_answer(message, t3,nameeeee):
        user_answer = unicodedata.normalize('NFKD', message.text).strip().lower().split()
        for yyyy in user_answer:
            user_answer2 = yyyy
        best_match = None
        best_ratio = 0
        print(nameeeee)
        for celebbb in nameeeee:
            lasttt = celebbb.split()
            for xxxx in lasttt:
                print(lasttt)
                normalized_name = unicodedata.normalize('NFKD', xxxx).lower()
                ratio = fuzz.ratio(user_answer2, normalized_name)
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match = lasttt
                    print(ratio)
        if best_match and best_ratio > 80:
            t5 = time.time()
            timee = round((t5 - t3), 2)
            bot.reply_to(message, f"صح عليك {message.from_user.first_name}✔️\n⏰الوقت: {timee} ثانية\n༄")
        elif message.text == 'الاسرع' :
            game_1(message)
        elif message.text == 'انمي':
            bot.reply_to(message, f"الاجابة السابقة: {xxxx} ")
            game_2(message)
        elif message.text == 'ايموجي' :
            game_3(message)
        elif message.text == 'اعلام' :
            game_4(message)
        else:
            bot.register_next_step_handler(message, check_answer,t3 ,nameeeee)

def check_answer3(message, ans, t3):
        user_answer = unicodedata.normalize('NFKD', message.text).strip().lower()
        best_match = None
        best_ratio = 0

        normalized_name = unicodedata.normalize('NFKD', ans).lower()
        ratio = fuzz.ratio(user_answer, normalized_name)
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = ans
            print(ratio)
        if best_match and best_ratio > 80:
            t5 = time.time()
            timee = round((t5 - t3), 2)
            bot.reply_to(message, f"صح عليك {message.from_user.first_name}✔️\n⏰الوقت: {timee} ثانية\n༄")
        elif message.text == 'الاسرع' :
            game_1(message)
        elif message.text == 'انمي':
            game_2(message)
        elif message.text == 'ايموجي' :
            game_3(message)
        elif message.text == 'اعلام' :
            bot.reply_to(message, f"الاجابة السابقة: {ans} ")
            game_4(message)
        else:
            bot.register_next_step_handler(message, check_answer3, ans,t3)
def check_answer2(message, answer_regex, t3):
    if message.text and answer_regex and message.text.strip().lower() == answer_regex.strip().lower():
        t5 = time.time()
        timee = round((t5 - t3), 2)
        bot.reply_to(message, f"صح عليك {message.from_user.first_name}✔️\n⏰الوقت: {timee} ثانية\n༄")
    elif message.text == 'الاسرع' :
        game_1(message)
    elif message.text == 'انمي' :
        game_2(message)
    elif message.text == 'ايموجي' :
        game_3(message)
    elif message.text == 'اعلام' :
        game_4(message)
    else:
        bot.register_next_step_handler(message, check_answer2, answer_regex,t3)

def character(message):
    try:
        textname = message.text
        to_en = Translator()
        translation_to_en = to_en.translate(f"{textname}", dest="en").text
        character = requests.get(f"https://animechan.vercel.app/api/random/character?name={textname}").json()
        name = character['anime']
        say = character['character']
        quo = character['quote']
        ch = "@Anime1Forest"
        translator = Translator()
        translation = translator.translate(f"{quo}", dest="ar")
        bot.send_message(message.chat.id,
                         f"═══════ ≪ °❈° ≫ ═══════\n⛩┇› A Random Quote Was Found For You\n⛩┇› Anime : {name} .\n⛩┇› Say : {say} .\n⛩┇› Quote : \n`{quo}`\n        ══════════════\n⛩┇› أخترت لك إقتباس 🗣\n⛩┇› من أنمي : {name} .\n⛩┇› القائل : {say} .\n⛩┇› الأقتباس :\n `{translation.text}` .\n═══════ ≪ °❈° ≫ ═══════",
                         reply_to_message_id=message.message_id, parse_mode="markdown")
        if message.from_user.id != 1448333343:
            bot.forward_message(developer_id, message.chat.id, message.message_id)
    except Exception as e:
        bot.send_message(developer_id, f'{e}\nError on line {sys.exc_info()[-1].tb_lineno}')
        bot.send_message(message.chat.id,"لايوجد")
def animeee(message):
    try:
        textname = message.text
        to_en = Translator()
        translation_to_en = to_en.translate(f"{textname}", dest="en").text
        anmesay = requests.get(f"https://animechan.vercel.app/api/random/character?name={textname}").json()
        name = anmesay['anime']
        say = anmesay['character']
        quo = anmesay['quote']
        ch = "@Anime1Forest"
        translator = Translator()
        translation = translator.translate(f"{quo}", dest="ar")
        bot.send_message(message.chat.id,
                         f"═══════ ≪ °❈° ≫ ═══════\n⛩┇› A Random Quote Was Found For You\n⛩┇› Anime : {name} .\n⛩┇› Say : {say} .\n⛩┇› Quote : \n`{quo}`\n        ══════════════\n⛩┇› أخترت لك إقتباس 🗣\n⛩┇› من أنمي : {name} .\n⛩┇› القائل : {say} .\n⛩┇› الأقتباس :\n `{translation.text}` .\n═══════ ≪ °❈° ≫ ═══════",
                         reply_to_message_id=message.message_id, parse_mode="markdown")
        if message.from_user.id != 1448333343:
            bot.forward_message(developer_id, message.chat.id, message.message_id)
    except Exception as e:
        bot.send_message(developer_id, f'{e}\nError on line {sys.exc_info()[-1].tb_lineno}')
        bot.send_message(message.chat.id,"لايوجد")
def st(message):
    bot.forward_message("1448333343", message.chat.id, message.message_id)
    m = message.text
    abd = types.InlineKeyboardMarkup()
    a13 = types.InlineKeyboardButton("• ارسل الرد  •", callback_data="a13")
    abd.add(a13)
    id = message.from_user.id
    f2 = message.from_user.first_name
    t2 = message.from_user.username
    mention = f"[{f2}](tg://user?id={id})"
    if message.from_user.id == id:
        bot.send_message(1448333343, f"رسالة واردة من {mention}\nالأسم : {mention}\nاليوزر : @{t2}\nالاي دي : "
                                     f"`{id}`\nالرسالة هي "
                                     f":\n\n{m}\n\n`ردد {id}` + الرسالة", reply_markup=abd, parse_mode="markdown")
    bot.send_message(message.chat.id,
                     text="- تم ارسال رسالتك الى المطور بنجاح سوف يتم الرد عليك بأقرب وقت 😇🫡 .\n- مطور البوت  ↤ [𝐘𝐔𝐔𝐈4𝐈](https://t.me/YUUI4I)  .",
                     disable_web_page_preview=True, reply_to_message_id=message.message_id, parse_mode="markdown")
def a13(message):
    id = message.from_user.id
    bot.send_message(message.chat.id,"*حسناً عزيزي ارسل الرد*",parse_mode="markdown")

    bot.register_next_step_handler(message,q)
def q(message):
    if "ردد" in message.text:
        i = message.text.split()[1]
        ii = message.text.split(None, 2)[2]
        bot.send_message(i, ii)
def read_database():
    try:
        with open('database/database.json', 'r') as file:
            database = json.load(file)
    except FileNotFoundError:
        database = {}
    return database
def create_keyboard(title,episodes, current_page,found_anime,user_id):
    buttons_per_page = 36  # عدد الأزرار في كل صفحة
    buttons_per_column = 3  # عدد الأزرار في كل عمود

    start_index = (current_page[user_id] - 1) * buttons_per_page
    end_index = start_index + buttons_per_page

    keyboard = InlineKeyboardMarkup(row_width=2)  # تعديل عرض الصف ليكون 2

    for i in range(start_index, end_index, buttons_per_column):
        row = []
        for episode in episodes[i:i+buttons_per_column]:
            episode_name = episode['name']
            button = InlineKeyboardButton("• " + episode_name + " •", callback_data=episode_name)
            row.append(button)
        keyboard.row(*row)

    # إضافة زر لعرض عدد الصفحات
    total_pages = (len(episodes) + buttons_per_page - 1) // buttons_per_page
    page_button = InlineKeyboardButton(f" {current_page[user_id]} / {total_pages}", callback_data="page_count")
    try:
        if "telegram" in found_anime :
            telegram_link = found_anime["telegram"]
            telegram_button = telebot.types.InlineKeyboardButton("مشاهده علي تيليجرام 🎥", url=telegram_link)
            keyboard.add(telegram_button)
        if "link_box" in found_anime :
            link_box_link = found_anime["link_box"]
            telegram_button = telebot.types.InlineKeyboardButton("مشاهده علي لينك بوكس 🎥", url=link_box_link)
            keyboard.add(telegram_button)
    except:pass
    line = InlineKeyboardButton(f"◎ ─━───━─ 𖡦─━───━─ ◎ ", callback_data="line")
    keyboard.add(line)

    # إضافة أزرار التنقل بين الصفحات
    navigation_buttons = []
    if current_page[user_id] > 1:
        navigation_buttons.append(InlineKeyboardButton("«««", callback_data="previousss"))
        navigation_buttons.append(InlineKeyboardButton("السابق", callback_data="previous"))
    if current_page[user_id] < total_pages:
        navigation_buttons.append(InlineKeyboardButton("التالي", callback_data="next"))
        navigation_buttons.append(InlineKeyboardButton("»»»", callback_data="nexttt"))
    if navigation_buttons:
        keyboard.row(*navigation_buttons)

    keyboard.add(page_button)
    keyboard.add(line)

    database = read_database()

    watched_anime = database.get(str(id), {}).get('watched', [])
    watching_anime = database.get(str(id), {}).get('watching', [])
    favorite_anime = database.get(str(id), {}).get('favorite', [])
    upcoming_anime = database.get(str(id), {}).get('upcoming', [])
    inn = "✅"
    noo = "❌"
    if title in watched_anime :
        watched_button = telebot.types.InlineKeyboardButton(f'• تمت مشاهدتها {inn} •', callback_data=f'@{title}')
    else:
        watched_button = telebot.types.InlineKeyboardButton(f'• تمت مشاهدتها {noo} •', callback_data=f'@{title}')

    if title in watching_anime :
        watching_button = telebot.types.InlineKeyboardButton(f'• اشاهدها حاليا {inn} •', callback_data=f'#{title}')
    else:
        watching_button = telebot.types.InlineKeyboardButton(f'• اشاهدها حاليا {noo} •', callback_data=f'#{title}')

    if title in favorite_anime :
        favorite_button = telebot.types.InlineKeyboardButton(f'• المفضلة {inn} •', callback_data=f'%{title}')
    else:
        favorite_button = telebot.types.InlineKeyboardButton(f'• المفضلة {noo} •', callback_data=f'%{title}')

    if title in upcoming_anime :
        upcoming_button = telebot.types.InlineKeyboardButton(f'• اشاهدها لاحقا {inn} •', callback_data=f'${title}')
    else:
        upcoming_button = telebot.types.InlineKeyboardButton(f'• اشاهدها لاحقا {noo} •', callback_data=f'${title}')

    keyboard.add(watched_button,watching_button)
    keyboard.add(favorite_button,upcoming_button)
    keyboard.add(line)
    with open('database/rate.json', 'r') as file:
        database = json.load(file)

    found_title = False
    onestarr_count = 0
    twostarr_count = 0
    threestarr_count = 0
    fourstarr_count = 0
    fivestarr_count = 0
    for rate in database:
        if 'onestar' in rate and title in rate['onestar']:
            onestarr = rate['onestar'][title]
            onestarr_count = len(onestarr)
            found_title = True
            break
    if not found_title:
        onestarr_count = 0
    for rate in database:
        if 'twostar' in rate and title in rate['twostar']:
            twostarr = rate['twostar'][title]
            twostarr_count = len(twostarr)
            found_title = True
            break

    if not found_title:
        twostarr_count = 0
    for rate in database:
        if 'threestar' in rate and title in rate['threestar']:
            threestarr = rate['threestar'][title]
            threestarr_count = len(threestarr)
            found_title = True
            break

    if not found_title:
        threestarr_count = 0
    for rate in database:
        if 'fourstar' in rate and title in rate['fourstar']:
            fourstarr = rate['fourstar'][title]
            fourstarr_count = len(fourstarr)
            found_title = True
            break

    if not found_title:
        fourstarr_count = 0
    for rate in database:
        if 'fivestar' in rate and title in rate['fivestar']:
            fivestarr = rate['fivestar'][title]
            fivestarr_count = len(fivestarr)
            found_title = True
            break

    if not found_title:
        fivestarr_count = 0

    onestar = telebot.types.InlineKeyboardButton(f'1X⭐️❲{onestarr_count}❳', callback_data=f'>{title}')
    twostar = telebot.types.InlineKeyboardButton(f'2X⭐️❲{twostarr_count}❳', callback_data=f'؟{title}')
    threestar = telebot.types.InlineKeyboardButton(f'3X⭐️❲{threestarr_count}❳', callback_data=f'*{title}')
    fourstar = telebot.types.InlineKeyboardButton(f'4X⭐️❲{fourstarr_count}❳', callback_data=f'<{title}')
    fivestar = telebot.types.InlineKeyboardButton(f'5X⭐️❲{fivestarr_count}❳', callback_data=f'~{title}')
    keyboard.add(onestar,twostar)
    keyboard.add(threestar,fourstar,fivestar)

    return keyboard
def is_user_subscribed(user_id, channel_id):
    chat_member = bot.get_chat_member(channel_id, user_id)
    if chat_member.status == 'left' or chat_member.status == 'kicked':
        return False
    return True
def save_user_subscription(user_id):
    with open('database/subscribed_users.json', 'r+') as file:
        data = json.load(file)

        if int(user_id) not in data['users']:
            data['users'].append(int(user_id))
            count = len(data['users'])
            file.seek(0)
            json.dump(data, file, indent=4)
            name = bot.get_chat(user_id).first_name
            user = bot.get_chat(user_id).username
            mention = f"[{name}](tg://user?id={user_id})"
            bot.send_message(developer_id,f"""
⚠️𝐒𝐎𝐌𝐄𝐎𝐍𝐄 𝐒𝐓𝐀𝐑𝐓 𝐓𝐇𝐄 𝐁𝐎𝐓⚠️
╭━━❰ɴᴇᴡ ᴍᴇᴍʙᴇʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ❱━━➣
┣⪼  The name :  {mention}
┣⪼ User :  @{user}
┣⪼  ID : `{user_id}`
┣⪼  total number of members :  ({count})
╰━━━━━━━━━━━━━━━━➣""",parse_mode="markdown")
def get_admins():
    with open('database/allowed_ids.json', 'r') as file:
        data = json.load(file)
        admins = data.get('admins', [])
    return admins
def view_subscribed_users(message):
    with open('database/subscribed_users.json', 'r') as file:
        data = json.load(file)
        subscribed_users = data['users']

    if subscribed_users:
        sub_info = []
        for sub_id in subscribed_users:
            sub_user = bot.get_chat(sub_id)
            sub_fr = bot.get_chat(sub_id).first_name

            if sub_user.username:
                sub_info.append(f"ID: <code>{sub_id}</code>\nUsername: @{sub_user.username}\nName: <a href='tg://user?id={sub_id}'>{sub_fr}</a>")
            else:
                sub_info.append(f"ID: <code>{sub_id}</code>\nName: <a href='tg://user?id={sub_id}'>{sub_fr}</a>")

        sub_text = "\n\n".join(sub_info)
        bot.reply_to(message, f"المشتركين في البوت :\n\n{sub_text}", parse_mode="HTML")
    else:
        bot.reply_to(message, "لا يوجد مشتركين")

def add_channel(message):
    if message.text == "cancel":
        bot.reply_to(message, "تم الالغاء")
    else:
        channel_id = message.text
        with open(channels_file, 'r') as file:
            channels_data = json.load(file)
            channel_ids = channels_data['channel_ids']

            if channel_id in channel_ids:
                bot.reply_to(message, f"المعرف موجود بالفعل: {channel_id}")
            else:
                channel_ids.append(channel_id)

                with open(channels_file, 'w') as file:
                    json.dump(channels_data, file, indent=4)

                bot.reply_to(message, f"تمت إضافة القناة بنجاح: {channel_id}")
def view_channels(message):
    with open(channels_file, 'r') as file:
        channels_data = json.load(file)
        channel_ids = channels_data['channel_ids']

    if channel_ids:
        channels_info = []
        for channel_id in channel_ids:
            channel_info = bot.get_chat(channel_id)
            invite_link = bot.export_chat_invite_link(channel_id)
            if channel_info.username:
                channels_info.append(f"ID: <code>{channel_id}</code>\nUsername: @{channel_info.username}\nInvite Link: {invite_link}")
            else:
                channels_info.append(f"ID: <code>{channel_id}</code>\nInvite Link: {invite_link}")

        channels_text = "\n\n".join(channels_info)
        bot.reply_to(message, f"قنوات الاشتراك الإجباري:\n\n{channels_text}",parse_mode="HTML",disable_web_page_preview=True)
    else:
        bot.reply_to(message, "لا توجد قنوات اشتراك إجباري حاليًا.")
def delete_channel(message):
    if message.text == "cancel":
        bot.reply_to(message, "تم الإلغاء")
    else:
        channel_id = message.text
        with open(channels_file, 'r') as file:
            channels_data = json.load(file)
            channel_ids = channels_data['channel_ids']

            if channel_id in channel_ids:
                channel_ids.remove(channel_id)

                with open(channels_file, 'w') as file:
                    json.dump(channels_data, file, indent=4)

                bot.reply_to(message, f"تم حذف قناة الاشتراك الإجباري: {channel_id}")
            else:
                bot.reply_to(message, f"لا يوجد قناة اشتراك إجباري بالمعرّف: {channel_id}")
def broadcast_message_pin(message):
    if message.text == "cancel":
        bot.reply_to(message, "تم الإلغاء")
    else:
        with open('database/subscribed_users.json', 'r') as file:
                data = json.load(file)
                allowed_ids = data['users']
        if message.photo:
            for user_id in allowed_ids:
                sent_message = bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
                bot.pin_chat_message(sent_message.chat.id, sent_message.message_id)
        elif message.video:
            for user_id in allowed_ids:
                sent_message = bot.send_video(user_id, message.video.file_id, caption=message.caption)
                bot.pin_chat_message(sent_message.chat.id, sent_message.message_id)
        else:
            for user_id in allowed_ids:
                sent_message = bot.send_message(user_id, message.text)
                bot.pin_chat_message(sent_message.chat.id, sent_message.message_id)

def broadcast_message(message):
    if message.text == "cancel":
        bot.reply_to(message, f"تم الالغاء")
    else:
        with open('database/subscribed_users.json', 'r') as file:
            data = json.load(file)
            allowed_ids = data['users']
        if message.photo:
            for user_id in allowed_ids:
                sent_message = bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
        elif message.video:
            for user_id in allowed_ids:
                sent_message = bot.send_video(user_id, message.video.file_id, caption=message.caption)
        else:
            for user_id in allowed_ids:
                sent_message = bot.send_message(user_id, message.text)
def forward_message(message):
    if message.text == "cancel":
        bot.reply_to(message, f"تم الالغاء")
    else:
        with open('database/subscribed_users.json', 'r') as file:
            data = json.load(file)
            allowed_ids = data['users']

        for user_id in allowed_ids:
            bot.forward_message(user_id, message.chat.id, message.message_id)
def backup_subscribed_users():
    bk = open('database/subscribed_users.json', 'r')
    bot.send_document(developer_id, bk)
def backup_data():
    bk = open('database/witanime.json', 'r')
    bot.send_document(developer_id, bk)
    bk2 = open('database/rate.json', 'r')
    bot.send_document(developer_id, bk2)
    bk3 = open('database/database.json', 'r')
    bot.send_document(developer_id, bk3)
def add_admin(message):
    if message.text == "cancel":
        bot.reply_to(message, f"تم الالغاء")
    else:
        admin_id = int(message.text)  # تحويل المعرّف إلى نوع عدد صحيح

        with open(allowed_ids_file, 'r') as file:
            data = json.load(file)
            admins = data.get('admins', [])

        if admin_id in admins:
            bot.reply_to(message, f"المشرف بالمعرّف {admin_id} موجود بالفعل.")
        else:
            admins.append(admin_id)
            data['admins'] = admins

            with open(allowed_ids_file, 'w') as file:
                json.dump(data, file, indent=4)

            bot.reply_to(message, f"تمت إضافة المشرف بنجاح: {admin_id}")
def view_admins(message):
    if message.text == "cancel":
        bot.reply_to(message, f"تم الالغاء")
    else:
        admins = get_admins()
        if admins:
            admins_info = [bot.get_chat(admin) for admin in admins]
            admins_list = [f"ID: <code>{info.id}</code>\nUsername: @{info.username}\nName: <a href='tg://user?id={info.id}'>{info.first_name}</a>" if info.username else f"ID: {info.id}\nName: <a href='tg://user?id={info.id}'>{info.first_name}</a>" for info in admins_info]
            admins_text = "\n\n".join(admins_list)
            bot.send_message(message.chat.id, f"قائمة المشرفين:\n\n{admins_text}", parse_mode='HTML')
        else:
            bot.reply_to(message, "لا يوجد مشرفين حاليًا.")
def delete_admin(message):
    if message.text == "cancel":
        bot.reply_to(message, f"تم الالغاء")
    else:
        admin_id =  int(message.text)
        with open(allowed_ids_file, 'r') as file:
            data = json.load(file)
            admins = data.get('admins', [])
            if admin_id in admins:
                admins.remove(admin_id)
                data['admins'] = admins

        with open(allowed_ids_file, 'w') as file:
            json.dump(data, file, indent=4)

        bot.reply_to(message, f"تمت حذف المشرف بنجاح: {admin_id}")
###
def process_code_step(message):
    keyboard = types.InlineKeyboardMarkup()
    confirm_button = types.InlineKeyboardButton('تأكيد', callback_data=f'confirmك{message.text}')
    cancel_button = types.InlineKeyboardButton('إلغاء', callback_data='cancel')
    keyboard.row(confirm_button, cancel_button)
    bot.send_message(message.chat.id, f'هل ترغب في تأكيد إضافة الكود؟\n\n{message.text}', reply_markup=keyboard)
def create_model_keyboard(user_id):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    # تحويل القائمة إلى قائمتين ضمن قائمة النماذج
    models_list = list(models.items())
    split_index = len(models_list) // 2
    models_list_1 = models_list[:split_index]
    models_list_2 = models_list[split_index:]
    for model_1, model_2 in zip(models_list_1, models_list_2):
        button_1 = telebot.types.InlineKeyboardButton(text=model_1[0], callback_data=f"{user_id}ا{model_1[0]}")
        button_2 = telebot.types.InlineKeyboardButton(text=model_2[0], callback_data=f"{user_id}ا{model_2[0]}")
        keyboard.add(button_1, button_2)
    # إضافة زر إضافي للنموذج الوحيد الذي قد لا يكون له زميل في العمود الثاني
    if len(models_list) % 2 != 0:
        last_model = models_list[-1]
        button = telebot.types.InlineKeyboardButton(text=last_model[0], callback_data=f"{user_id}ا{last_model[0]}")
        keyboard.add(button)
    return keyboard
def increment_photos_used(user_id):
    today = datetime.now().date().isoformat()
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        last_date = user['last_date']
        if last_date != today:
            user['photos_used'] = 0
            user['last_date'] = today
            save_user_data()
        user['photos_used'] += 1
        save_user_data()
    else:
        user_data.append({
            'user_id': user_id,
            'photos_used': 1,
            'last_date': today
        })
        save_user_data()
def check_photos_limit(user_id):
    today = datetime.now().date().isoformat()
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        last_date = user['last_date']
        if last_date != today:
            user['photos_used'] = 0
            user['last_date'] = today
            save_user_data()
            return True
        else:
            photos_used = user['photos_used']
            if photos_used < 25:
                return True
            else:
                return False
    else:
        return True
def save_user_data():
    with open(user_data_file, 'w') as file:
        json.dump(user_data, file, indent=4)
def get_user_warnings(user_id):
    with open(user_data_file, 'r') as file:
        user_data = json.load(file)
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        return user.get('warnings', 0)
    else:
        return 0
def calculate_remaining_time(user_id):
    current_time = datetime.now().time()
    reset_time = datetime.time(0, 0)  # تعيين وقت إعادة التفعيل إلى منتصف الليل
    if current_time >= reset_time:
        remaining_time = datetime.combine(datetime.date.today() + datetime.timedelta(days=1), reset_time) - datetime.now()
    else:
        remaining_time = datetime.combine(datetime.date.today(), reset_time) - datetime.now()
    return remaining_time
def format_remaining_time(remaining_time):
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    remaining_time_str = f"\n{hours} س\n {minutes} د\n {seconds} ث"
    return remaining_time_str
def add_warning_to_user(user_id):
    user = next((u for u in user_data if u['user_id'] == user_id), None)
    if user:
        if 'warnings' in user:
            user['warnings'] += 1
        else:
            user['warnings'] = 1
        save_user_data()
def CODE_API(message):
    CODE_API = message.text
    with open("x_prodia_key.txt", "w") as file:
        file.write(CODE_API)
    bot.reply_to(message, "تمت اضافه الكود")

bot.infinity_polling(skip_pending=True)
