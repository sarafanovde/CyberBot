from telebot import types


def first_exam(bot,session, message):
    if session.question_number == 0:
        q1_guestion(bot,session,message)
    if session.question_number == 1:
        q2_guestion(bot, session, message)
    if session.question_number == 2:
        q3_guestion(bot, session, message)
    if session.question_number == 3:
        q4_guestion(bot, session, message)
    if session.question_number == 4:
        q5_guestion(bot, session, message)
    if session.question_number == 5:
        q6_guestion(bot,session,message)
    if session.question_number == 6:
        q8_guestion(bot, session, message)
    if session.question_number == 7:
        q9_guestion(bot, session, message)
    #NOT USED#
    if session.question_number == 8:
        q10_guestion(bot, session, message)
    if session.question_number == 9:
        q10_guestion(bot, session, message)
    if session.question_number == 10:
        q11_guestion(bot, session, message)
    if session.question_number == 11:
        q12_guestion(bot, session, message)
    session.question_number += 1

def q1_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="false"))
    #btnsPH.append(types.InlineKeyboardButton(text="3 ответ", callback_data="false"))
    #btnsPH.append(types.InlineKeyboardButton(text="4 ответ", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Тебе поступило СМС с номера +900. В сообщении говорится, что с Вашей банковской карты, вот-вот будет произведен перевод денежных средств, и предполагается отправить в ответном сообщении код для отмены операции. Какие Ваши действия?\n\n1. Проигнорировать сообщение\n2. Отправить СМС с кодом отмены", parse_mode='Markdown', reply_markup=keyboardPH)
def q2_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="3️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="4️⃣", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Вам поступило СМС с номера +7900000000. В сообщении говорится, что Вы выиграли крупный денежный приз, а так же предлагает перейти по ссылке, чтобы узнать подробности. Какие действия Вы предпримете?\n\n1. Перейду по ссылке с домашнего ПК\n2. Перейду по ссылке\n3. Проверю номер отправителя и перейду по ссылке\n4. Проигнорирую сообщение", parse_mode='Markdown', reply_markup=keyboardPH)
def q3_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="3️⃣", callback_data="false"))
    #btnsPH.append(types.InlineKeyboardButton(text="4 ответ", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Как Вы поступите если Вам позвонит человек, представится работником банка и сообщит о мошенничестве, совершенном в отношении Вас и попросит назвать кодовое слово для подтверждения Вашей личности?\n\n1. Удостоверюсь, что звонок совершается с номера телефона банка и назову кодовое слов\n2. Откажусь называть кодовое слово и завершу разговор\n3. Назову кодовое слово", parse_mode='Markdown', reply_markup=keyboardPH)
def q4_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="3️⃣", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Как Вы поступите если Вам позвонит человек, представится работником банка и сообщит о мошенничестве, совершенном в отношении Вас и попросит назвать номер банковской карты и CVC код для подтверждения Вашей личности?\n\n1. Удостоверюсь, что звонок совершается с номера телефона банка и сообщу номер карты и CVC код\n2. Назову номер карты и CVC код\n3. Откажусь сообщать номер карты и CVC код завершу разговор", parse_mode='Markdown', reply_markup=keyboardPH)
def q5_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Перед Новым годом вы решили продать что-то на Интернет-барахолке. Вам пришло такое SMS:", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q5.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Перейду по ссылке или позвоню отправителю. Вдруг там что-то хорошее.\n2. Выглядит подозрительно, не стану отвечать или переходить по ссылке из смс.",
                     parse_mode='Markdown', reply_markup=keyboardPH)
def q6_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Купив подарки в Сети, вы получили письмо от банка. Кажется, покупок было слишком много и у вас образовалась задолженность.", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q6.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Похоже, что-то пошло не так. Перейду по ссылке - надо разобраться.\n2. Не стану переходить по ссылке. Лучше позвоню в банк и узнаю, в чем дело.",parse_mode='Markdown', reply_markup=keyboardPH)
#NOT USED#
def q7_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Кто-то решил поздравить вас с праздником! Вы кликнете по ссылке, чтобы узнать, от кого открытка?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q7.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Конечно, кликну, и отправлю в ответ другую открытку.\n2. Не стану переходить по ссылке.",parse_mode='Markdown', reply_markup=keyboardPH)
def q8_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Вы выбрали подарок на сайте, осталось все оплатить — вот на этой странице. Ваши действия?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q8.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Я бы не рискнул вводить здесь данные своей карты.\n2. Все нормально, я оплачиваю.",parse_mode='Markdown', reply_markup=keyboardPH)
def q9_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1️⃣", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="2️⃣", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Вас просят оплатить покупку на Ozon. Это снова обман?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q9.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Напротив, все в порядке.\n2. Это фишинг!",parse_mode='Markdown', reply_markup=keyboardPH)
#NOT USED#
def q10_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2", callback_data="true"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Вы ищете подарок в Сети, на очередном сайте всплывает такое окно. Что вы сделаете?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q10.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Введу данные карты. Вдруг именно мне повезет?\n2. Не стану вводить данные карты. Сначала узнаю в банке, есть ли у них такая акция.",parse_mode='Markdown', reply_markup=keyboardPH)
def q11_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="2", callback_data="false"))
    btnsPH.append(types.InlineKeyboardButton(text="3", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="4", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Скоро полночь, самое время поздравить друзей в Facebook. На какой из указанных ниже страниц вы введете свои логин и пароль?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q11_1.jpg", 'rb'))
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q11_2.jpg", 'rb'))
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q11_3.jpg", 'rb'))
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q11_4.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов (1-4):\n",parse_mode='Markdown', reply_markup=keyboardPH)
def q12_guestion (bot,session,message):
    keyboardPH = types.InlineKeyboardMarkup()
    btnsPH = []
    btnsPH.append(types.InlineKeyboardButton(text="1", callback_data="true"))
    btnsPH.append(types.InlineKeyboardButton(text="2", callback_data="false"))
    keyboardPH.add(*btnsPH)
    bot.send_message(message.chat.id, "Для оформления заказа в интернет-магазине вас просят ввести свои учетные данные. Что вы сделаете?", parse_mode='Markdown')
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\q12.jpg", 'rb'))
    bot.send_message(message.chat.id,"Варианты ответов:\n\n1. Введу данные.\n2. Наверное, это фишинг. Воздержусь.",parse_mode='Markdown', reply_markup=keyboardPH)
