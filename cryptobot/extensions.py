
import telebot
from config import dic_help
from keys import TOKEN
import requests
import json

bot = telebot.TeleBot(TOKEN)

#язык пользователя {message.from_user.id: language}
dic_person_lang = {}

class APIException(Exception):
    pass

# возможные ошибки
# в списке языков язык есть а в словаре диалогов диалога нет

class ValutaConverter:
    @staticmethod
    def get_price(message: telebot.types.Message):
        lang = dic_person_lang[message.from_user.id][1:] #в словаре язык записан как '/sq' а нужно получить 'sq'
        text = message.text.lower()
        L = text.split(' ')

        try:
            if len(L) != 3:
                raise APIException(f"неверно введены параметры {message.text}")

            try:
                valuta1 = L[0]
                base = dic_help[lang]['valuta_list'][valuta1]
            except KeyError:
                raise APIException(f"неверно указана первая валюта {L[0]}")

            try:
                valuta2 = L[1]
                quote = dic_help[lang]['valuta_list'][valuta2]
            except KeyError:
                raise APIException(f"неверно указана вторая валюта {L[1]}")

            if base == quote:
                raise APIException(f"нет смысла переводить из {base} в {quote}")

            try:
                amount = float(L[2].replace(",", "."))
            except ValueError:
                raise APIException(f"неверно указано количество {L[2]}")
        except APIException as e:
            return  f"ошибка пользователя\n{e}"
        except Exception as e:
            return f"не удалось обработать команду {e}"
        else:
            r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}")
            t = json.loads(r.content)
            total = float(t[quote] * amount)
            return f"{amount} {base} = {total} {quote}"
