import telebot
import webbrowser
import requests

bot = telebot.TeleBot('6666956230:AAFUdeDeq1U5HGnZWzZX-1M21qnKa6znS38')


@bot.message_handler(commands=['start'])
def main(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("/help")
    item2 = telebot.types.KeyboardButton("/source")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}! Выберите команду:', reply_markup=markup) #получение id чата, отправка сообщения


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<strike>Тут должна быть помощь...</strike>', parse_mode='html')


@bot.message_handler(commands=['source'])
def source(message):
    bot.send_message(message.chat.id, f'Вы были перенаправлены на веб-страницу. Если вдруг этого не произошло, пожалуйста, нажмите на ссылку: <a>https://github.com/passionatepumpkin/</a>', parse_mode='html')
    webbrowser.open('https://github.com/passionatepumpkin/')


@bot.message_handler(commands=['image'])
def search_image(message):
    query = message.text.split("/image ", 1)[1]  # Извлечь поисковой запрос из команды. разделить 1 раз, извлечь часть строки с индексом [1]
    search_url = f"https://yandex.ru/images/search?text={query}"
    # Выполнить запрос к поисковой системе и обработать результаты
    response = requests.get(search_url)
    if response.status_code == 200: #код успешно выполненного запроса HTTPS
        images = response.json()[""]
        for image in images:
            image_url = image["url"]
            bot.send_photo(message.chat.id, image_url)
        else:
            bot.send_message(message.chat.id, "Извините, не удалось найти изображения.")






bot.polling(none_stop=True)