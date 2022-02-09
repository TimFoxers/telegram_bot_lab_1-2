from telebot import TeleBot, types

bot = TeleBot('2055691120:AAE2LyMbUracihKWO2NavwkBYBZuMRaxFYs')

dataClass = {'Воин':0,
             'Паладин':0,
             'Охотник':0,
             'Разбойник':0,
             'Жрец':0,
             'Шаман':0,
             'Маг':0,
             'Чернокнижник':0,
             'Друид':0
    }

dataRace = {'Человек':0,
            'Дворф':0,
            'Ночной эльф':0,
            'Гном':0,
            'Дреней':0,
            'Ворген':0,
            'Орк':0,
            'Нежить':0,
            'Тролль':0,
            'Эльф крови':0,
            'Гоблин':0,
            'Таурен':0
    }

forbiddenCombinations = {'Человек':'Шаман',
            'Человек':'Друид',
            'Дворф':'Друид',
            'Ночной эльф': 'Паладин',
            'Ночной эльф': 'Шаман',
            'Ночной эльф': 'Чернокнижник',
            'Гном': 'Паладин',
            'Гном': 'Шаман',
            'Гном': 'Друид',
            'Дреней':'Разбойник',
            'Дреней':'Чернокнижник',
            'Дреней':'Друид',
            'Ворген':'Паладин',
            'Ворген':'Шаман',
            'Орк':'Паладин',
            'Орк':'Жрец',
            'Орк':'Друид',
            'Нежить':'Паладин',
            'Нежить':'Шаман',
            'Нежить':'Друид',
            'Тролль':'Паладин',
            'Эльф крови':'Шаман',
            'Эльф крови':'Друид',
            'Гоблин':'Паладин',
            'Гоблин':'Друид',
            'Таурен':'Маг',
            'Таурен':'Чернокнижник'
    }

@bot.message_handler(commands=['start','text'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('мужчина', 'женщина')
    msg = bot.send_message(message.chat.id, 'Вы мужчина или женщина?', reply_markup=markup)
    bot.register_next_step_handler(msg, sex_step)

def sex_step(message):
    answer = message.text
    if answer == "мужчина":
        dataClass['Воин']+=1
        dataRace['Орк']+=1
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('да', 'нет')
        msg = bot.send_message(message.chat.id, 'Вы чувствуете влечение к мужчинам?', reply_markup=markup)
        bot.register_next_step_handler(msg, gay_step)
    else:
        dataClass['Друид']+=1
        dataClass['Жрец']+=1
        dataRace['Эльф крови']+=1
        dataRace['Ночной эльф']+=1
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('да', 'нет')
        msg = bot.send_message(message.chat.id, 'Вы считаете себя скучным человеком?', reply_markup=markup)
        bot.register_next_step_handler(msg, boring_step)

def gay_step(message):
    answer = message.text
    if answer == "да":
        dataClass['Разбойник']+=1
        dataRace['Эльф крови']+=5
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вы считаете себя скучным человеком?', reply_markup=markup)
    bot.register_next_step_handler(msg, boring_step)

def boring_step(message):
    answer = message.text
    if answer == "да":
        dataRace['Человек']+=3
        dataRace['Эльф крови']+=1
    else:
        dataRace['Тролль']+=1
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вы считаете себя ответственным человеком?', reply_markup=markup)
    bot.register_next_step_handler(msg, responsibility_step)

def responsibility_step(message):
    answer = message.text
    if answer == "да":
        dataClass['Воин']+=1
        dataClass['Шаман']+=1
        dataClass['Друид']+=2
        dataClass['Паладин']+=2
        dataClass['Жрец']+=2
    else:
        dataClass['Разбойник']+=1
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вы спокойный человек?', reply_markup=markup)
    bot.register_next_step_handler(msg, good_step)

def good_step(message):
    answer = message.text
    if answer == "да":
        dataRace['Дреней']+=1
        dataRace['Таурен']+=1
        dataRace['Дворф']+=1
        dataClass['Друид']+=1
    else:
        dataRace['Гоблин']+=1
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вам часто говорят,что вы назойливы?', reply_markup=markup)
    bot.register_next_step_handler(msg, annoy_step)

def annoy_step(message):
    answer = message.text
    if answer == "да":
        dataRace['Гном']+=5
        dataRace['Гоблин']+=2
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Фэнтези', 'Научная фантастика')
    markup.add('Зомби', 'Оборотни')
    markup.add('Комедия', 'Криминальный')
    msg = bot.send_message(message.chat.id, 'Фильмы какого жанра вы предпочитаете?', reply_markup=markup)
    bot.register_next_step_handler(msg, genre_step)

def genre_step(message):
    answer = message.text
    if answer == "Фэнтези":
        dataRace['Ночной эльф']+=2
    elif answer == "Научная фантастика":
        dataRace['Дреней']+=3
    elif answer == "Зомби":
        dataRace['Нежить']+=2
        dataClass['Чернокнижник']+=1
    elif answer == "Оборотни":
        dataRace['Ворген']+=2
        dataClass['Друид']+=1
    elif answer =="Комедия":
        dataRace['Гном']+=1
        dataRace['Гоблин']+=2
    elif answer =="Криминальный":
        dataClass['Разбойник']+=3
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Любите ли вы часто менять образы?', reply_markup=markup)
    bot.register_next_step_handler(msg, look_step)

def look_step(message):
    answer = message.text
    if answer == "да":
        dataClass['Друид']+=2
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вы принимаете галлюциногенные или иные запрещенные вещества?', reply_markup=markup)
    bot.register_next_step_handler(msg, weed_step)

def weed_step(message):
    answer = message.text
    if answer == "да":
        dataRace['Тролль']+=5
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Вам нравится экстрим?', reply_markup=markup)
    bot.register_next_step_handler(msg, risk_step)

def risk_step(message):
    answer = message.text
    if answer == "да":
        dataClass['Маг']+=2
        dataClass['Разбойник']+=1
    else:
        dataRace['Таурен']+=1
        dataRace['Дворф']+=1
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Пиво', 'Водка')
    markup.add('Коктейли', 'Ром')
    markup.add('Чем кислотнее выглядит, тем лучше','Не пью')
    msg = bot.send_message(message.chat.id, 'Какой алкоголь вы предпочитаете?', reply_markup=markup)
    bot.register_next_step_handler(msg, alcohol_step)

def alcohol_step(message):
    answer = message.text
    if answer == "Пиво":
        dataRace['Дворф']+=2
        dataRace['Таурен']+=2
        dataClass['Шаман']+=1
    elif answer == "Водка":
        dataRace['Дреней']+=2
        dataClass['Воин']+=1
        dataClass['Чернокнижник']+=1
    elif answer == "Коктейли":
        dataRace['Эльф крови']+=2
        dataClass['Маг']+=1
        dataClass['Паладин']+=1
    elif answer == "Ром":
        dataClass['Разбойник']+=2
    elif answer =="Чем кислотнее выглядит, тем лучше":
        dataRace['Орк']+=3
        dataClass['Чернокнижник']+=3
    elif answer =="Не пью":
        dataRace['Ночной эльф']+=1
        dataClass['Жрец']+=2
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Меч', 'Молот')
    markup.add('Посох', 'Топор')
    markup.add('Кинжал', 'Лук')
    markup.add('Ружье')
    msg = bot.send_message(message.chat.id, 'Какое оружие вам больше по душе?', reply_markup=markup)
    bot.register_next_step_handler(msg, weapon_step)

def weapon_step(message):
    answer = message.text
    if answer == "Меч":
        dataRace['Человек']+=2
        dataClass['Воин']+=2
        dataClass['Паладин']+=1
    elif answer == "Молот":
        dataRace['Дворф']+=1
        dataClass['Воин']+=1
        dataClass['Шаман']+=2
        dataClass['Паладин']+=3
        dataRace['Дреней']+=1
    elif answer == "Топор":
        dataRace['Орк']+=2
        dataRace['Дворф']+=1
        dataClass['Шаман']+=2
        dataClass['Воин']+=2
    elif answer == "Кинжал":
        dataClass['Разбойник']+=3
        dataRace['Нежить']+=1
    elif answer == "Посох":
        dataClass['Маг']+=3
        dataClass['Жрец']+=3
        dataClass['Друид']+=2
        dataClass['Шаман']+=1
    elif answer =="Лук":
        dataRace['Ночной эльф']+=1
        dataClass['Охотник']+=3
    elif answer =="Ружье":
        dataRace['Дворф']+=1
        dataClass['Охотник']+=3
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Халк', 'Железный человек')
    markup.add('Тор', 'Соколиный глаз/Зеленая стрела')
    markup.add('Супермен', 'Человек-паук')
    markup.add('Бэтмен', 'Доктор Стрендж')
    markup.add('Никем')
    msg = bot.send_message(message.chat.id, 'Кем из героев комиксов вы хотели бы быть?', reply_markup=markup)
    bot.register_next_step_handler(msg, comics_step)

def comics_step(message):
    answer = message.text
    if answer == "Халк":
        dataRace['Орк']+=5
        dataRace['Таурен']+=1
        dataClass['Воин']+=1
        dataClass['Друид']+=1
    elif answer == "Железный человек":
        dataRace['Дреней']+=1
        dataClass['Маг']+=2
        dataClass['Чернокнижник']+=2
        dataClass['Охотник']+=1
    elif answer == "Тор":
        dataRace['Дворф']+=2
        dataClass['Паладин']+=3
        dataClass['Шаман']+=3
    elif answer == "Соколиный глаз/Зеленая стрела":
        dataClass['Охотник']+=3
        dataRace['Ночной эльф']+=1
    elif answer == "Супермен":
        dataRace['Человек']+=1
        dataClass['Паладин']+=2
    elif answer =="Бэтмен":
        dataRace['Нежить']+=1
        dataRace['Ворген']+=1
        dataClass['Разбойник']+=2
    elif answer =="Человек-паук":
        dataClass['Друид']+=3
    elif answer =="Доктор Стрендж":
        dataClass['Маг']+=4
        dataClass['Чернокнижник']+=4
    elif answer =="Никем":
        dataRace['Человек']+=3
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Молния', 'Огонь')
    markup.add('Лед', 'Природа')
    markup.add('Свет', 'Тьма')
    markup.add('Стихией тумаков')
    msg = bot.send_message(message.chat.id, 'Какой стихией вы бы хотели повелевать?', reply_markup=markup)
    bot.register_next_step_handler(msg, elements_step)

def elements_step(message):
    answer = message.text
    if answer == "Молния":
        dataClass['Шаман']+=3
    elif answer == "Огонь":
        dataClass['Маг']+=3
        dataClass['Шаман']+=2
    elif answer == "Лед":
        dataClass['Маг']+=3
    elif answer == "Природа":
        dataClass['Шаман']+=2
        dataClass['Друид']+=3
    elif answer == "Свет":
        dataClass['Жрец']+=3
        dataClass['Паладин']+=2
        dataRace['Нежить']-=1
        dataRace['Дреней']+=1
    elif answer =="Тьма":
        dataRace['Нежить']+=1
        dataClass['Чернокнижник']+=2
        dataClass['Разбойник']+=2
    elif answer =="Стихия тумаков":
        dataClass['Воин']+=3
        dataRace['Орк']+=1
        dataClass['Паладин']+=1
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('да', 'нет')
    msg = bot.send_message(message.chat.id, 'Часто ли вы ходите в церковь?', reply_markup=markup)
    bot.register_next_step_handler(msg, church_step)

def church_step(message):
    answer = message.text
    if answer == "да":
        dataClass['Жрец']+=3
    else:
        dataClass['Разбойник']-=3
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add('Волк', 'Медведь')
    markup.add('Олень', 'Ворон')
    markup.add('Бык', 'Змея')
    markup.add('Мёртвое')
    msg = bot.send_message(message.chat.id, 'Какое ваше любимо животное?', reply_markup=markup)
    bot.register_next_step_handler(msg, animal_step)

def animal_step(message):
    answer = message.text
    if answer == "Волк":
        dataClass['Шаман']+=3
        dataRace['Ворген']+=3
    elif answer == "Медведь":
        dataClass['Друид']+=3
        dataRace['Орк']+=1
    elif answer == "Олень":
        dataClass['Друид']+=3
    elif answer == "Ворон":
        dataClass['Друид']+=2
        dataClass['Маг']+=3
    elif answer == "Бык":
        dataRace['Таурен']+=4
    elif answer =="Змея":
        dataClass['Разбойник']+=1
    elif answer =="Мёртвое":
        dataClass['Чернокнижник']+=2
        dataRace['Нежить']+=2

    mc = 0;
    mci = ''
    for i, j in dataClass.items():
        if j>mc:
            mc = j
            mci = i

    mr = 0
    mri = ''
    for i, j in dataRace.items():
        if j>mr and forbiddenCombinations[i]!=mci:
            mr = j
            mri = i
    msg = bot.send_message(message.chat.id, "Лучшее сочетание расы и класса для вас: " + mri + ' ' + mci)

    for i, j in dataClass.items():
        dataClass[i] = 0
            
    for i, j in dataRace.items():
        dataClass[i] = 0
            
bot.polling()
