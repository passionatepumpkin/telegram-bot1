import telebot
import webbrowser
import requests
from github import Github
github_token = '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'
bot = telebot.TeleBot('6666956230:AAFUdeDeq1U5HGnZWzZX-1M21qnKa6znS38')
github_username = 'passionatepumpkin'
repo_name = 'telegram-bot1'

@bot.message_handler(commands=['start'])
def main(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("/help")
    item2 = telebot.types.KeyboardButton("/source")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}!', reply_markup=markup) #получение id чата, отправка сообщения


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'<b>Доступные команды:</b> \n \
/start - Начать взаимодействие с ботом.\n \
/help - Показать список доступных команд и их описания.\n \
/source - Получить ссылку на исходный код бота.\n \
/image - Получить изображение из репозитория.\n \
/audio - Получить аудио из репозитория.', parse_mode='html')


@bot.message_handler(commands=['source'])
def source(message):
    bot.send_message(message.chat.id, f'Вы были перенаправлены на веб-страницу. Если вдруг этого не произошло, пожалуйста, нажмите на ссылку: <a>https://github.com/passionatepumpkin/telegram-bot1/blob/main/main.py</a>', parse_mode='html')
    webbrowser.open('https://github.com/passionatepumpkin/telegram-bot1/blob/main/main.py')


@bot.message_handler(commands=['image'])
def get_image(message):
    try:
        g = Github(github_token)
        repo = g.get_user(github_username).get_repo(repo_name)
        file_contents = repo.get_contents("photo_8_2023-03-30_19-05-29.jpg")
        if file_contents:
            image_url = file_contents.download_url
            bot.send_photo(message.chat.id, requests.get(image_url).content)
        else:
            bot.reply_to(message, "Изображение не найдено в репозитории.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")


@bot.message_handler(commands=['audio'])
def get_audio(message):
    try:
        g = Github(github_token)
        repo = g.get_user(github_username).get_repo(repo_name)
        file_contents = repo.get_contents("Lana Del Rey - Pink Champagne.mp3")
        if file_contents:
            audio_url = file_contents.download_url
            bot.send_audio(message.chat.id, requests.get(audio_url).content)
        else:
            bot.reply_to(message, "Аудио не найдено в репозитории.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {str(e)}")


bot.polling(none_stop=True)
