import telebot;
import utils
import sqlalchemy
from telebot import types
import pickle
import Gaming
import education
import time
bot = telebot.TeleBot('1293857426:AAFY2TmAg1X_mmqv9Mp01TDhCXUZGS9MOL0');

@bot.message_handler(commands=["start"])
def send_start(message):
    session = utils.simpleSession(message.chat.id)
    utils.sessions[message.chat.id] = session
    output = open('data.pkl', 'wb')
    pickle.dump(utils.sessions, output, 2)
    output.close()
    button1 = types.InlineKeyboardButton(text="Проверим знания! 👨‍🎓", callback_data="start_educ")
    button2 = types.InlineKeyboardButton(text="Приступим к обучению! 📚", callback_data="skip_educ")
    keyboard1 = types.InlineKeyboardMarkup()
    keyboard1.add(button1)
    keyboard1.add(button2)
    session.start_wait = True
    bot.send_photo(message.chat.id, open("C:\\Users\\Дима\\PycharmProjects\\pythonProject1\\5.png", 'rb'),reply_markup=keyboard1)

@bot.callback_query_handler(func=lambda c: c.data)
def pages(c):
    try:
        session = utils.sessions[c.message.chat.id]
    except Exception:
        session = utils.simpleSession(c.message.chat.id)
        utils.sessions[c.message.chat.id] = session
    if c.data == "true" and session.first_test == True:
        if session.question_number <= 8:
            if session.question_number == 8:
                session.points_1[session.question_number-1] += 1
                session.first_test = False
                bot.send_message(c.message.chat.id,
                                 "По следующим категориям у тебя есть пробелы в знаниях!\nПерейдем к обучению?",
                                 parse_mode='Markdown')

                education.iswinner(bot, session, c.message)
            else:
                session.points_1[session.question_number - 1] += 1
                Gaming.first_exam(bot,session,c.message)

        else:
            session.first_test = False
            bot.send_message(c.message.chat.id,
                             "По следующим категориям у тебя есть пробелы в знаниях!\nПерейдем к обучению?",
                             parse_mode='Markdown')

            education.iswinner(bot, session, c.message)
    if c.data == "false" and session.first_test == True:
        if session.question_number < 8:
            Gaming.first_exam(bot,session,c.message)
        else:
            session.first_test = False
            bot.send_message(c.message.chat.id,"По следующим категориям у тебя есть пробелы в знаниях!\nПерейдем к обучению?", parse_mode='Markdown')
            education.iswinner(bot,session,c.message)
    if c.data == "start_educ" and session.start_wait == True:
        session.start_wait = False
        bot.send_message(c.message.chat.id, "Давай проверим!", parse_mode='Markdown')
        Gaming.first_exam(bot, session,c.message)
    #пропустим обучение#
    if c.data == "skip_educ":
        education.iswinner(bot, session, c.message)
        session.start_wait = False
    #Далее обработка второго теста по категориям
    #cat1
    if c.data == "cat1" and session.start_wait == False:
        education.teach_cat1_preview(bot,session,c.message)
    if c.data == "teach_cat1_start" and session.start_wait == False:
        education.teach_cat1_1(bot,session,c.message)
    if c.data == "teach_cat1_true_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Совершенно верно!", parse_mode='Markdown')
        time.sleep(5)
        education.teach_cat1_2(bot, session, c.message)
        session.points_1[0]=1
    if c.data == "teach_cat1_true_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не является фишингом. Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        session.points_1[1] = 1
        education.iswinner(bot,session,c.message)
    if c.data == "teach_cat1_false_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не фишинг\nОтвет неверный!\n ❗От Сбербанка сообщения приходят с единого номера 900 или 9000\n❗Сообщение похоже на оригинальное, однако пришло не с номера 900 или 9000\n❗Сообщение с просьбой о возврате пришло с того же номера, с которого пришла информация о поступлении платежа на счет. Операция явно мошенническая", parse_mode='Markdown')
        time.sleep(8)
        education.teach_cat1_2(bot, session, c.message)
        session.points_1[0] = 1
    if c.data == "teach_cat1_false_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Фишинг\nОтвет неверный!\n❗Это не фишинг. Сообщение отправлено с единого номера Сбербанка 900", parse_mode='Markdown')
        session.points_1[1] = 1
        education.iswinner(bot, session, c.message)
    #cat2
    if c.data == "cat2" and session.start_wait == False:
        education.teach_cat2_preview(bot,session,c.message)
    if c.data == "teach_cat2_start" and session.start_wait == False:
        education.teach_cat2_1(bot,session,c.message)
    if c.data == "teach_cat2_true_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Совершенно верно!", parse_mode='Markdown')
        time.sleep(5)
        education.teach_cat2_2(bot, session, c.message)
        session.points_1[2]=1
    if c.data == "teach_cat2_true_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Фишинг обнаружен. Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        session.points_1[3] = 1
        education.iswinner(bot,session,c.message)
    if c.data == "teach_cat2_false_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не фишинг\nОтвет неверный!\n❗Звонок совершается с телефона отличного от номера банка\n❗Работники Банка никогда не запрашивают данные банковских карт, не звонят, чтобы сообщить о мошенничестве", parse_mode='Markdown')
        time.sleep(8)
        education.teach_cat2_2(bot, session, c.message)
        session.points_1[2] = 1
    if c.data == "teach_cat2_false_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не фишинг\nОтвет неверный!\n❗Звонок совершается с телефона отличного от номера банка\nРаботники Банка никогда не запрашивают данные банковских карт, не звонят, чтобы сообщить о мошенничестве", parse_mode='Markdown')
        session.points_1[3] = 1
        education.iswinner(bot, session, c.message)
    #cat3
    if c.data == "cat3" and session.start_wait == False:
        education.teach_cat3_preview(bot,session,c.message)
    if c.data == "teach_cat3_start" and session.start_wait == False:
        education.teach_cat3_1(bot,session,c.message)
    if c.data == "teach_cat3_true_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не стану переходить по ссылке. Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        education.teach_cat3_2(bot, session, c.message)
        session.points_1[4]=1
    if c.data == "teach_cat3_true_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Фишинг. Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        session.points_1[5] = 1
        education.iswinner(bot,session,c.message)
    if c.data == "teach_cat3_false_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Конечно, кликну, и отправлю в ответ другую открытку. \nОтвет неверный!\n❗Это фишинг! Иногда преступники используют гиперссылки, чтобы обмануть невнимательных пользователей. Текст, выглядящий как ссылка, на самом деле ведет на другой сайт!", parse_mode='Markdown')
        time.sleep(8)
        education.teach_cat3_2(bot, session, c.message)
        session.points_1[4] = 1
    if c.data == "teach_cat3_false_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не фишинг\nОтвет неверный!\n❗Письмо отправлено с общественного домена, а адрес отправителя имеет подозрительный вид и не совпадает с именем.\n❗Отсутствие контактных данных в подписи", parse_mode='Markdown')
        session.points_1[5] = 1
        education.iswinner(bot, session, c.message)
    #cat4#
    if c.data == "cat4" and session.start_wait == False:
        education.teach_cat4_prewiew(bot,session,c.message)
    if c.data == "teach_cat4_start" and session.start_wait == False:
        education.teach_cat4_1(bot,session,c.message)
    if c.data == "teach_cat4_true_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Не стану вводить данные карты.  Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        education.teach_cat4_2(bot, session, c.message)
        session.points_1[6]=1
    if c.data == "teach_cat4_true_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Всё верно!", parse_mode='Markdown')
        time.sleep(5)
        session.points_1[7] = 1
        education.iswinner(bot,session,c.message)
    if c.data == "teach_cat4_false_1" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Введу данные карты\nОтвет неверный!\n❗Это мошенничество! Зная ваши банковские данные, злоумышленники легко украдут ваши деньги. Вводить их стоит только на известных ресурсах при наличии защищенного соединения.", parse_mode='Markdown')
        time.sleep(8)
        education.teach_cat4_2(bot, session, c.message)
        session.points_1[6] = 1
    if c.data == "teach_cat4_false_2" and session.start_wait == False:
        bot.send_message(c.message.chat.id, "Ответ неверный!\nВсе в порядке: есть защищенное соединение и домен принадлежит магазину. Так что можно оплачивать покупки без проблем.", parse_mode='Markdown')
        session.points_1[7] = 1
        education.iswinner(bot, session, c.message)
    output = open('data.pkl', 'wb')
    pickle.dump(utils.sessions, output, 2)
    output.close()


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        session = utils.sessions[message.chat.id]
    except Exception:
        session = utils.simpleSession(message.chat.id)
        utils.sessions[message.chat.id] = session
        output = open('data.pkl', 'wb')
        pickle.dump(utils.sessions, output, 2)
        output.close()
    bot.send_message(message.chat.id, "Извини, я не понял тебя!\n Отправь команду /start", parse_mode='Markdown')
    output = open('data.pkl', 'wb')
    pickle.dump(utils.sessions, output, 2)
    output.close()


bot.polling(none_stop=True, interval=0)