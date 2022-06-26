import telebot
from telebot import types


bot = telebot.TeleBot('5545195671:AAHrpplJIOD8mE4lqjObRq9_JPULdpMeH4s')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(text='Давай начнем?', callback_data='question1')
        keyboard.add(but1)
        text_welc1="Рада тебя видеть!"
        text_welc2='Здесь можно ознакомиться с услугами, записатьcя на процедуру, оставить отзыв'+\
                  '\n'+'\nТакже можешь поучаствовать в программе 🎉🎉🎉"Скидка постоянным клиентам"'
        bot.send_photo(message.chat.id, open('img\start.png', 'rb'))
        bot.send_message(message.chat.id,text_welc1)
        bot.send_message(message.from_user.id,text_welc2,reply_markup=keyboard)


    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")


    elif message.text == "📌Услуги":
        global keyboard2
        keyboard2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        button1 = types.KeyboardButton('📍Коррекция')
        button2 = types.KeyboardButton('📍Окрашивание бровей')
        button3 = types.KeyboardButton('📍Ламинирование бровей')
        button4 = types.KeyboardButton('📍Окрашивание ресниц')
        button5 = types.KeyboardButton('📍Ламинирование ресниц')
        button6 = types.KeyboardButton('📍Удаление волос воском')
        button7 = types.KeyboardButton('Вернуться в меню ↩️')
        keyboard2.add(button1, button2)
        keyboard2.add(button3, button4)
        keyboard2.add(button5, button6)
        keyboard2.add(button7)
        bot.send_message(message.from_user.id, 'Выбери,что интересует', reply_markup=keyboard2)

    elif message.text == '📍Коррекция':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\corr.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='Коррекция бровей представляет собой оформление бровей с помощью пинцета ' \
                              'или воска с учетом особенностей бровей и формы лица'
                              '🌿Стоимость услуги-10 рублей🌿', reply_markup=back_keyboard)

    elif message.text == '📍Окрашивание бровей':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\color_hna.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='В данную процедуру входит окрашивание бровей краской или хной,'
                              ' цвет подбиратеся с учетом цветиотипа и пожеланий'
                              '🌿Стоимость услуги-13 рублей🌿', reply_markup=back_keyboard)

    elif message.text == '📍Ламинирование бровей':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\lami_br.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='Процедура делает брови более послушными и укладывавет '
                              'их в нужном направлении, за счет питания волоски '
                              'становятся плотными.Брови выгдядят '
                              'более объемными и естественно густыми '
                              '🌿Стоимость услуги-20 рублей🌿', reply_markup=back_keyboard)


    elif message.text == '📍Окрашивание ресниц':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\color_lash.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='Окрашивание ресниц без дополнительных процедур.'
                              'Для клиентов,которые не любят постоянно пользоваться '
                              'тушью для ресниц'
                              '🌿Стоимость услуги-8 рублей🌿', reply_markup=back_keyboard)


    elif message.text == '📍Ламинирование ресниц':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\lami_lash.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='Ламинирование ресниц-это процедура,которая удлиняет,'
                              'завивает и укрепляет структуру ресниц благодаря'
                              'входящим в состав средствам.Длительный результат '
                              'позволяет не пользваться тушью и другой декоративной '
                              'косметикой'
                              '🌿Стоимость услуги-15 рублей🌿', reply_markup=back_keyboard)


    elif message.text == '📍Удаление волос воском':
        back_keyboard = types.InlineKeyboardMarkup()
        back_key = types.InlineKeyboardButton(text='Назад ⬅ в "Услуги"', callback_data="back")
        back_keyboard.add(back_key)
        bot.send_photo(message.chat.id, open('img\dep.png', 'rb'))
        bot.send_message(message.from_user.id,
                         text='Процедура удаления нежелательных волосков в области'
                              'верхней губы, подбородка'
                              '🌿Стоимость услуги-8 рублей🌿', reply_markup=back_keyboard)

    elif message.text == 'Вернуться в меню ↩️':
        bot.send_message(message.from_user.id, text='Меню⤵️', reply_markup=main_menu_keyboard)



    elif message.text == '📋Прайс':
        bot.send_photo(message.from_user.id, open('img\photo.png', 'rb'))
        bot.send_message(message.from_user.id, text='Получить консультацию можно по телефону 📞80162555555', reply_markup=main_menu_keyboard)

    elif message.text == '📝☎ Запись':
        bot.send_message(message.from_user.id, text='Супер')
        bot.send_sticker(message.chat.id, open('AnimatedSticker.tgs', 'rb'))
        serv_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        serv1 = types.KeyboardButton(text='📞80162555555')
        serv_keyboard.add(serv1)
        bot.send_message(message.from_user.id, 'Записаться можно по телефону ⬇️⬇️⬇️',
                         reply_markup=serv_keyboard)


    elif message.text == '📞80162555555':
        bot.send_message(message.chat.id, text='Меню⤵️', reply_markup=main_menu_keyboard)

    elif message.text == '💌Отзывы':
        show_otz_keyboard = types.InlineKeyboardMarkup()
        show_button = types.InlineKeyboardButton(text='Жми', callback_data='show')
        show_otz_keyboard.add(show_button)
        bot.send_sticker(message.chat.id, open('AnimatedSticker2.tgs', 'rb'))
        bot.send_message(message.chat.id,text='Читать отзывы',reply_markup=show_otz_keyboard)
        bot.send_message(message.chat.id, text='Меню⤵️', reply_markup=main_menu_keyboard)

    elif message.text == '🎁 Акции и скидки':
        disc_keyboard = types.InlineKeyboardMarkup()
        disc_button1 = types.InlineKeyboardButton(text='⚡⚡Акция месяца⚡⚡', callback_data='discount1')
        disc_button2 = types.InlineKeyboardButton(text='✨✨Карта постоянного клиента✨✨', callback_data='discount2')
        disc_keyboard.add(disc_button1)
        disc_keyboard.add(disc_button2)
        bot.send_message(message.chat.id, text='Выбери нужный раздел', reply_markup=disc_keyboard)
        bot.send_message(message.chat.id, text='Меню⤵️', reply_markup=main_menu_keyboard)


    elif message.text == '📒 Курсы':
        bot.send_message(message.chat.id,
        text='Курсы'+ '\n💥💥"Обучение профессии бровист"💥💥'+'\nНабор группы 2-4 человека'+\
        '\nСтарт 25 июля 2022 года'+'\n'+'\nКурс'+''
        '\n 💥💥"Ламимейкер"💥💥'+'\nНабор группы 2-4 человека'+''
        '\nСтарт 01 августа 2022 года'+'\n'+'\n📝Запись по телефону 80162555555')
        bot.send_message(message.chat.id, text='Меню⤵️', reply_markup=main_menu_keyboard)


    elif message.text == '💜 Оставить отзыв':
        otz_keyboard = types.InlineKeyboardMarkup()
        otz_but = types.InlineKeyboardButton(text='Оставить отзыв', callback_data='otz')
        otz_keyboard.add(otz_but)
        bot.send_photo(message.from_user.id, open('img\otz.png', 'rb'))
        bot.send_message(message.chat.id,'Буду очень тебе признательна,если оценишь мою работу😉',reply_markup=otz_keyboard)
        bot.send_message(message.chat.id, text='Меню⤵️',reply_markup=main_menu_keyboard)


    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func=lambda call: True)
def callback_func1(call):
    if call.data == 'question1':
        msg1 = 'Отлично!'
        global main_menu_keyboard
        main_menu_keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        key1 = types.KeyboardButton('📌Услуги')
        key2 = types.KeyboardButton('📋Прайс')
        key3 = types.KeyboardButton('📝☎ Запись')
        key4 = types.KeyboardButton('💌Отзывы')
        key5 = types.KeyboardButton('🎁 Акции и скидки')
        key6 = types.KeyboardButton('📒 Курсы')
        key7 = types.KeyboardButton('💜 Оставить отзыв ')
        main_menu_keyboard.add(key1, key2, key3, key4, key5, key6, key7)

        bot.send_message(call.message.chat.id, msg1)
        bot.send_message(call.message.chat.id, 'Ты можешь посмотреть, что тебе интересно👇',
                         reply_markup=main_menu_keyboard)

    if call.data == 'discount1':
        discount_keyboard=types.InlineKeyboardMarkup()
        disc_key = types.InlineKeyboardButton(text='Ссылка на прайс', callback_data='disc_adv')
        disc_key2 = types.InlineKeyboardButton(text='Вернуться в меню ↩️', callback_data='disc_back')
        discount_keyboard.row(disc_key,disc_key2 )
        bot.send_photo(call.message.chat.id, open('img\disc1.png', 'rb'))
        bot.send_message(call.message.chat.id, '🎈🎈🎈Стань обладательницей роскошных бровей уже сейчас!')


    if call.data == 'discount2':
        discount2_keyboard = types.InlineKeyboardMarkup()
        disc2_key = types.InlineKeyboardButton(text='Заявка на карту', callback_data='disc_adv2')
        disc2_key2 = types.InlineKeyboardButton(text='Вернуться в меню ↩️', callback_data='disc_back2')
        discount2_keyboard.row(disc2_key, disc2_key2)
        bot.send_message(call.message.chat.id,'✨Карта постоянного клиента✨'+''
        '\n'+'\n'+'📣При втором посещении моего кабинета ты получаешь'+''
        '\nавтоматически карту постоянного клиента.'+''
        '\n‼️А при каждом пятом посещении-скидку 5% на любой вид услуг!'+''
        '\nБуду рада предоставить тебе этот подарок 🎁!')

    elif call.data == 'back':
        bot.send_message(call.message.chat.id, text='Переходи к следующей услуге', reply_markup=keyboard2)


    elif call.data == 'otz':
        global otz_back_keyboard
        otz_back_keyboard = types.InlineKeyboardMarkup()
        otz_back_key = types.InlineKeyboardButton(text='Вернуться в меню ↩️', callback_data='otz_back')
        otz_back_keyboard.row(otz_back_key)
        bot.send_message(call.message.chat.id,text='Мне важно твое мнение!')
        my_otz = bot.send_message(call.message.chat.id,'Пиши здесь')
        bot.register_next_step_handler(my_otz, otz_2)

    elif call.data == 'show':
        bot.send_message(call.message.chat.id,'📌Галерея отзывов обновляется')


def otz_2(message):
    bot.send_message(message.chat.id,text='Спасибо!',reply_markup=main_menu_keyboard)


bot.polling(non_stop=True, interval=0)
