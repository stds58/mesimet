import telebot
from config import COMMANDA, dic_lang, dic_help
from extensions import ValutaConverter, dic_person_lang, bot, APIException


def f_user(message):
    if message.chat.username is None:
        if message.chat.first_name is None:
            user = message.chat.last_name
        else:
            user = message.chat.first_name
    else:
        user = message.chat.username
    return user
#message.chat.first_name,message.chat.first_name,message.chat.username


def proverka_lang(func):
    def wrapper(message: telebot.types.Message):
        try:
            dic_person_lang[message.from_user.id]
        except Exception:
            for key,value in dic_lang.items():
                bot.send_message(message.chat.id, f"{key} {value}\n")
        else:
            func(message)
    return wrapper


#выбрать язык
@bot.message_handler(commands=['language'])
def handle_language(message: telebot.types.Message):
    for key,value in dic_lang.items():
        bot.send_message(message.chat.id, f"{key} {value}\n")


#привествие и помощь
@bot.message_handler(commands=['start', 'help'])
@proverka_lang
def handle_start(message: telebot.types.Message):
    user = f_user(message)  # message.chat.first_name,message.chat.first_name,message.chat.username
    lang = dic_person_lang[message.from_user.id][1:]
    bot.send_message(message.chat.id, f"{dic_help[lang][2]} {user} \n {dic_help[lang][1]}")


#выбор языка
@bot.message_handler(commands=COMMANDA)
def handle_help(message: telebot.types.Message):
    user = f_user(message)
    dic_person_lang[message.from_user.id] = message.text #добавить выбранный язык в словарь
    #print(dic_person_lang)
    try:
        try:
            bot.send_message(message.chat.id,f"{dic_help[message.text[1:]][2]} {user} \n {dic_help[message.text[1:]][1]}")
        except KeyError:
            raise APIException(f"не переведён диалог для вашего языка")
    except APIException as e:
        bot.send_message(message.chat.id, e)

#список валют
@bot.message_handler(commands=['values'])  #здесь вылезет ошибка если не выбран язык
@proverka_lang
def handle_valuta(message: telebot.types.Message):
    lang = dic_person_lang[message.from_user.id][1:]
    bot.send_message(message.chat.id, dic_help[lang][4])
    for key2, value2 in dic_help[lang][3].items():
        bot.send_message(message.chat.id, f"{key2} {value2}")


@bot.message_handler(content_types=['text'])
@proverka_lang
def handle_request(message: telebot.types.Message):
    bot.send_message(message.chat.id, ValutaConverter.get_price(message))



bot.polling(none_stop=True)





