from telebot import types
import Gaming
import time

def iswinner(bot,session,message):
    cat1 = session.points_1[0] + session.points_1[1]
    cat2 = session.points_1[2] + session.points_1[3]
    cat3 = session.points_1[4] + session.points_1[5]
    cat4 = session.points_1[6] + session.points_1[7]
    keyboardPH = types.InlineKeyboardMarkup(row_width=1)
    btnsPH = []
    iswinnerFL = True
    if cat1 < 2:
        keyboardPH.add(types.InlineKeyboardButton(text="📱 SMS - фишинг", callback_data="cat1"))
        iswinnerFL = False
    if cat2 < 2:
        keyboardPH.add(types.InlineKeyboardButton(text="☎ Телефонный фишинг", callback_data="cat2"))
        iswinnerFL = False
    if cat3 < 2:
        keyboardPH.add(types.InlineKeyboardButton(text="✉ Фишинговые письма", callback_data="cat3"))
        iswinnerFL = False
    if cat4 < 2:
        keyboardPH.add(types.InlineKeyboardButton(text="🌐 Фишинговые сайты", callback_data="cat4"))
        iswinnerFL = False
    if iswinnerFL == True:
        bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\finish.png", 'rb'))
    else:
        #keyboardPH.add(*btnsPH)
        bot.send_message(message.chat.id, "Выбери модуль:", parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat1_preview(bot,session,message):
    bot.send_message(message.chat.id,
                     "В последнее время стали поступать сообщения об участившихся случаях мобильного мошенничества при помощи SMS.",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\fishing_SMS.jpg", 'rb'))
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="Приступить к тесту", callback_data="teach_cat1_start"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Теперь проверим, сможешь ли ты распознать смс-фишинг", parse_mode='Markdown', reply_markup=keyboardPH)


def teach_cat1_1 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat1_true_1"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat1_false_1"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Определите, является ли сообщение фишинговым или безопасным",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\sms_1.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Фишинг\n2. Не фишинг",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat1_2 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat1_false_2"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat1_true_2"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Определите, является ли сообщение фишинговым или безопасным?",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\sms_2.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Фишинг\n2. Не фишинг",
                     parse_mode='Markdown', reply_markup=keyboardPH)


def teach_cat2_preview(bot,session,message):
    bot.send_message(message.chat.id,
                     "Вчера кто-то позвонил Миссис Хадсон, представился сотрудником банка и попросил предоставить личные данные. Давай рассмотрим, как себя надо вести в подобных ситуациях.",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\fishing_phone.jpg", 'rb'))
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="Приступить к тесту", callback_data="teach_cat2_start"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Теперь проверим, сможешь ли ты распознать телефонный фишинг", parse_mode='Markdown', reply_markup=keyboardPH)


def teach_cat2_1 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat2_true_1"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat2_false_1"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Определите, является ли звонок фишинговым или безопасным",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\phone_1.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Фишинг\n2. Не фишинг",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat2_2 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat2_true_2"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat2_false_2"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Определите, является ли звонок фишинговым или безопасным",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\phone_2.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Фишинг\n2. Не фишинг",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat3_preview(bot,session,message):
    bot.send_message(message.chat.id,
                     "Методы киберпреступников становятся все более изощренными, письма из интернет рассылок выглядят очень достоверно.",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\fishing_latters.jpg", 'rb'))
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="Приступить к тесту", callback_data="teach_cat3_start"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Теперь проверим, сможете ли вы отличить мошенничество от реальных писем", parse_mode='Markdown', reply_markup=keyboardPH)


def teach_cat3_1 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat3_false_1"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat3_true_1"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Кто-то решил поздравить вас с праздником! Вы кликнете по ссылке, чтобы узнать, от кого открытка?",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q7.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Конечно, кликну, и отправлю в ответ другую открытку.\n2. Не стану переходить по ссылке.",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat3_2 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat3_true_2"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat3_false_2"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Является ли письмо фишинговым?",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q2_1.png", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Фишинг\n2. Не фишинг",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat4_prewiew (bot,session, message):
    bot.send_message(message.chat.id,
                     "На этот раз интернет-мошенники решили подловить нас на фишинговых сайтах.",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\fishing_web.jpg", 'rb'))
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="Приступить к тесту", callback_data="teach_cat4_start"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Теперь проверим, сможешь ли ты распознать фишинговый сайт", parse_mode='Markdown', reply_markup=keyboardPH)


def teach_cat4_1 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat4_false_1"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat4_true_1"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,"Вы ищете подарок в Сети, на очередном сайте всплывает такое окно. Что вы сделаете?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q10.jpg", 'rb'))
    bot.send_message(message.chat.id,
                     "Варианты ответов:\n\n1. Введу данные карты. Вдруг именно мне повезет? \n2. Не стану вводить данные карты. Сначала узнаю в банке, есть ли у них такая акция.",
                     parse_mode='Markdown', reply_markup=keyboardPH)

def teach_cat4_2 (bot,session, message):

    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="teach_cat4_true_2"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="teach_cat4_false_2"))

    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id,
                     "Для оформления заказа в интернет-магазине вас просят ввести свои учетные данные. Что вы сделаете?",
                     parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q12.jpg", 'rb'))

    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Введу данные.\n2. Наверное, это фишинг. Воздержусь.",parse_mode='Markdown', reply_markup=keyboardPH)
