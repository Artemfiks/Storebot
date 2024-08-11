import telebot
from telebot import types

config = [6095232417, 6024629666]

bot = telebot.TeleBot('7243584949:AAFQiavoiZaWgyWEQInOf3uDY3IXOwUJtVo')

@bot.message_handler(commands=['start'])
def handle_start(message):
  print(message)
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button1 = types.KeyboardButton(text='Ассортимент')
  keyboard.add(button1)

  # Отправка сообщения с клавиатурой
  bot.send_message(message.chat.id, 'Здравствуйте, вы попали в магазин temshik_store. \n\n⬇️Нажмите на кнопку ниже⬇️.', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == 'Ассортимент':
    kb = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Telegram', callback_data='tgpremium')
    btn2 = types.InlineKeyboardButton(text='Приватный впн', callback_data='vpn')
    btn3 = types.InlineKeyboardButton(text='Дефф', callback_data='deff')
    btn4 = types.InlineKeyboardButton(text='Мануалы', callback_data='manual')
    btn5 = types.InlineKeyboardButton(text='Софты', callback_data='softs')
    kb.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text='Наш ассортимент:', reply_markup=kb)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == 'tgpremium':
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Premium 30d', callback_data='tgpremium30d')
        btn2 = types.InlineKeyboardButton(text='Premium 360d', callback_data='tgpremium360d')
        btn4 = types.InlineKeyboardButton(text='Мануал по рефаунду TG Premium', callback_data='tgrefound')
        btn5 = types.InlineKeyboardButton(text='Мануал по абузу TG Premium', callback_data='tgabuz')
        btn6 = types.InlineKeyboardButton(text='Виртуальные прогретые аккаунты TG', callback_data='tgvirt')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn2, btn4, btn5, btn6, btn3)
        bot.send_message(call.message.chat.id,'Выберите подходящий Вам вариант', reply_markup=kb)
    elif call.data[:2] == 'tg':
        price = 'Произошла ошибка, попробуйте еще раз.'
        if call.data == 'tgpremium30d':
            price = '2.5$'
        elif call.data == 'tgpremium360d':
            price = '16.5$'
        elif call.data == 'tgrefound':
            price = '5$'
        elif call.data == 'tgabuz':
            price = '5$'
        elif call.data == 'tgvirt':
            price = '2.5$'
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'send{call.data}')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате {price} на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data == 'softs':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Софт для рассылки(лс/общие чаты)', callback_data='softrass')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id, 'Выберите подходящий Вам вариант', reply_markup=kb)
    elif call.data[:4] == 'soft':
        price = 'Произошла ошибка, попробуйте еще раз.'
        if call.data == 'softrass':
            price = '10$'
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'send{call.data}')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате {price} на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data == 'deff':
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='Дефф 7 дней', callback_data='deff7d')
        btn2 = types.InlineKeyboardButton(text='Дефф навсегда', callback_data='deffforever')
        kb.add(btn1, btn2)
        bot.send_message(call.message.chat.id, 'Выберите срок дефа', reply_markup=kb)
    elif call.data == 'deff7d':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'senddeff7d')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате 5$ на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data == 'deffforever':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'senddeffforever')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате 13.5$ на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data == 'manual':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Посредничество на фриланс биржах', callback_data='manualposrfreelans')
        btn2 = types.InlineKeyboardButton(text='Посредничество на продаже услуг', callback_data='manualposrsellservice')
        btn3 = types.InlineKeyboardButton(text='Полный гайд по заработку на YouTube', callback_data='manualguideyoutube')
        btn4 = types.InlineKeyboardButton(text='Все способы заработка+', callback_data='manualallway')
        btn5 = types.InlineKeyboardButton(text='Бизнес на цветах легал (комфортные вложения 100$)', callback_data='manualbuisnessflower')
        btn6 = types.InlineKeyboardButton(text='Схема+(собраны 40 схем заработка)', callback_data='manualscheme40')
        btn7 = types.InlineKeyboardButton(text='Мануал по рефаунду Amazone', callback_data='manualamazon')
        btn8 = types.InlineKeyboardButton(text='Мануал по рефаунду Aliexpress', callback_data='manualaliexpress')
        btn9 = types.InlineKeyboardButton(text='Мануал по рефаунду eBay',callback_data='manualebay')
        btn10 = types.InlineKeyboardButton(text='Мануал по заработку на реф. ссылках', callback_data='manualref')
        btn11 = types.InlineKeyboardButton(text='Пакет мануалов по анонимности в интернете', callback_data='manualanonim')
        btn12 = types.InlineKeyboardButton(text='Мануал по безопасности в интернете', callback_data='manualsec')
        btn13 = types.InlineKeyboardButton(text='Как защититься от взлома(соцсети, телефон)', callback_data='manualdeffvzlov')
        btn14 = types.InlineKeyboardButton(text='Переход на 2 страницу', callback_data='2strmanual')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите подходящий вам вариант из списка ниже', reply_markup=kb)
    elif call.data == '2strmanual':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Деньги на посредничестве арбитража трафика', callback_data='manualarbtraff')
        btn2 = types.InlineKeyboardButton(text='Деньги на схемном трафике', callback_data='manualshemtraff')
        btn3 = types.InlineKeyboardButton(text='Деньги на УБТ с тик тока',
                                          callback_data='manualubttiktok')
        btn4 = types.InlineKeyboardButton(text='Деньги на УБТ+ИИ', callback_data='manualubtii')
        btn5 = types.InlineKeyboardButton(text='Решение проблем по заливу УБТ(Tik Tok, Shorts)',
                                          callback_data='manualproblemzaliv')
        btn6 = types.InlineKeyboardButton(text='Пакет курсов от других людей', callback_data='manualpaketkurs')
        btn7 = types.InlineKeyboardButton(text='Мануал по рефаунду Amazone', callback_data='manualamazon')
        btn14 = types.InlineKeyboardButton(text='Переход на 1 страницу', callback_data='manual')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn14)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Выберите подходящий вам вариант из списка ниже', reply_markup=kb)
    elif call.data[:6] == 'manual':
        price = 'Произошла ошибка, попробуйте еще раз.'
        if call.data == 'manualposrfreelans':
            price = '5$'
        elif call.data == 'manualposrsellservice':
            price = '5$'
        elif call.data == 'manualguideyoutube':
            price = '5$'
        elif call.data == 'manualallway':
            price = '4$'
        elif call.data == 'manualbuisnessflower':
            price = '5$'
        elif call.data == 'manualscheme40':
            price = '6$'
        elif call.data == 'manualamazon':
            price = '8$'
        elif call.data == 'manualaliexpress':
            price = '8$'
        elif call.data == 'manualebay':
            price = '8$'
        elif call.data == 'manualref':
            price = '5$'
        elif call.data == 'manualposrsellservice':
            price = '5$'
        elif call.data == 'manualanonim':
            price = '5$'
        elif call.data == 'manualsec':
            price = '5$'
        elif call.data == 'manualdeffvzlov':
            price = '4$'
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'send{call.data}')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате {price} на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data == 'vpn':
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='London, UK 🇬🇧 ', callback_data='london')
        btn2 = types.InlineKeyboardButton(text='Amsterdam, Netherlands 🇳🇱', callback_data='amsterdam')
        btn3 = types.InlineKeyboardButton(text='Gavle, Sweden 🇸🇪', callback_data='gavle')
        btn4 = types.InlineKeyboardButton(text='Zurich, Switzerland 🇨🇭', callback_data='zurich')
        btn5 = types.InlineKeyboardButton(text='Des Moines, USA 🇺🇸', callback_data='des_moines')
        btn6 = types.InlineKeyboardButton(text='Toronto, Canada 🇨🇦', callback_data='toronto')
        btn7 = types.InlineKeyboardButton(text='Paris, France 🇫🇷', callback_data='paris')
        btn8 = types.InlineKeyboardButton(text='Warsaw, Poland 🇵🇱', callback_data='warsaw')
        btn9 = types.InlineKeyboardButton(text='Milan, Italy 🇮🇹', callback_data='milan')
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(call.message.chat.id, 'Выберите из списка нужную вам страну', reply_markup=kb)
    elif call.data in ['london', 'amsterdam', 'gavle', 'zurich', 'des_moines', 'toronto', 'paris', 'warsaw', 'milan']:
        kb = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton(text='30d - 2$', callback_data=f'vpn{call.data}30d')
        btn2 = types.InlineKeyboardButton(text='60d - 3.5$', callback_data=f'vpn{call.data}60d')
        btn3 = types.InlineKeyboardButton(text='90d - 5$', callback_data=f'vpn{call.data}90d')
        btn4 = types.InlineKeyboardButton(text='180d - 9.5$', callback_data=f'vpn{call.data}180d')
        btn5 = types.InlineKeyboardButton(text='360d - 16$', callback_data=f'vpn{call.data}360d')
        kb.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(call.message.chat.id, text='Выберите, на сколько времени вам нужен впн', reply_markup=kb)
    elif call.data == 'menu':
        handle_start(call.message)
    elif call.data[:3] == 'vpn':
        price = 'Произошла ошибка, попробуйте еще раз.'
        if '30d' in call.data:
            price = '2$'
        elif '60d' in call.data:
            price = '3.5$'
        elif '90d' in call.data:
            price = '5$'
        elif '180d' in call.data:
            price = '9.5$'
        elif '360d' in call.data:
            price = '16$'
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Оплатил', callback_data=f'send{call.data}')
        btn3 = types.InlineKeyboardButton(text='Главное меню', callback_data='menu')
        kb.add(btn1, btn3)
        bot.send_message(call.message.chat.id,
                         f'К оплате {price} на криптокошелек в сети TRC20 \n\n<code>TTBa9Rmkejid9dsFWvPnPnvmum8TannNQN</code>\n\nЕсли у вас возникли проблемы с оплатой, свяжитесь с администратором @ArtemfikWW',
                         parse_mode='html', reply_markup=kb)
    elif call.data[:7] == 'sendvpn' or 'sendtgpremium' in call.data or 'senddeff' in call.data or 'sendmanual' in call.data or 'sendtg' in call.data or 'sendsoft' in call.data:
        bot.send_message(call.message.chat.id, 'Ожидайте, пока с вами свяжется администратор')
        for id in config:
            bot.send_message(id,
                         f'Покупатель @{call.message.chat.username} оплатил заказ {call.data}, проверьте оплату и свяжитесь с покупателем')


bot.infinity_polling()