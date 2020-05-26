import discord
from discord.ext import commands
from time import sleep
from random import randint, choice

TOKEN = 'NzAyNTUxNzk2NDcxNjkzMzcz.XqBtqw.-DNiBSWDS6E4jsJTzyMr4sSwEuI'
bot = commands.Bot(command_prefix='!')

game = {"day": 1, "members": {}, "exposeds": set(), "don": None, "commissioner": None, "doctor": None, "balance": 0.4, "deadToday": None, "healToday": None}

mafiamasterMessage = None
mafiatextMessage = None

names = ['Абеле', 'Абрэмо', 'Агостино', 'Агэпето', 'Агэпито', 'Адамо', 'Адольфо', 'Адриано', 'Адэлберто', 'Адэлфири', 'Алберто', 'Алвиз', 'Aлдо', 'Алессандро', 'Алессио', 'Алонзо', 'Алпфонсо', 'Алфео', 'Алфонсо', 'Алфредо', 'Амадео', 'Амато', 'Амброджино', 'Амброжино', 'Амедео', 'Америго', 'Ампелайо', 'Амэндо', 'Анаклето', 'Анастасио', 'Анджело', 'Андреа', 'Анжело', 'Анселмо', 'Антонелло', 'Антонино', 'Антонио', 'Анэтолайо', 'Ардуино', 'Арканджело', 'Армандо', 'Арналдо', 'Аролдо', 'Арриго', 'Арсенио', 'Артуро', 'Аттилайо', 'Аугусто', 'Аурелио', 'Ачиль', 'Балдассаре', 'Балдовино', 'Бартоло', 'Бартоломео', 'Бартоломмео', 'Басилио', 'Баттиста', 'Бенвенуто', 'Бенедетто', 'Бениамино', 'Бенигно', 'Беппе', 'Бернардино', 'Бернардо', 'Бертолдо', 'Бертрандо', 'Беттино', 'Биаджио', 'Биажио', 'Биэджино', 'Валентино', 'Валерио', 'Венцеслао', 'Викензо', 'Вико', 'Виникайо', 'Винсенте', 'Винцензо', 'Виргилио', 'Витале', 'Вито', 'Витторе', 'Витторино', 'Витторио', 'Вэнни', 'Габриэль', 'Гаспар', 'Гаспаро', 'Гастон', 'Гаэтано', 'Гоффредо', 'Грегэрайо', 'Грэзиэно', 'Гуалтиеро', 'Гуглиелмо', 'Гуерино', 'Гуидо', 'Густаво', 'Гэвино', 'Давид', 'Даниэле', 'Данте', 'Дарио', 'Дези', 'Дезидерио', 'Деметрио', 'Дерэнт', 'Джакопо', 'Дженнаро', 'Джероламо', 'Джеронимо', 'Джианни', 'Джиацинто', 'Джино', 'Джиоакчино', 'Джиоачино', 'Джиованни', 'Джиозу', 'Джиорджино', 'Джироламо', 'Джиэмпиро', 'Джиэмпэоло', 'Джиэнмарко', 'Джиэнмэрия', 'Джиэннино', 'Джиэнпиро', 'Джиэнпэоло', 'Джордано', 'Джорджио', 'Джузеппе', 'Джулиано', 'Джулио', 'Джустино', 'Дино', 'Доменико', 'Донато', 'Донэтелло', 'Дориэно', 'Дрэго', 'Дуилайо', 'Дэмиэно', 'Жакоб', 'Жакомо', 'Жамбатиста', 'Жанкарло', 'Жанлуиджи', 'Жанлука', 'Жанфранко', 'Жерардо', 'Жервасио', 'Жермано', 'Жиральдо', 'Игнацио', 'Илэрайо', 'Инноцензо', 'Ипполито', 'Исайа', 'Итало', 'Калвино', 'Каллисто', 'Камилло', 'Карло', 'Карлос', 'Кармин', 'Касимиро', 'Киприано', 'Кириако', 'Кирилло', 'Кирино', 'Киро', 'Клаудио', 'Клементе', 'Клето', 'Коломбано', 'Коломбо', 'Конкетто', 'Коррадо', 'Косимо', 'Космо', 'Костанзо', 'Костэнтино', 'Крескензо', 'Крест', 'Кристиано', 'Кристофоро', 'Крокифиссо', 'Кроккификсайо', 'Куирино', 'Кэлоджеро', 'Ладислао', 'Лаззаро', 'Ласэрайо', 'Лауро', 'Леон', 'Леонардо', 'Леонзайо', 'Леопольдо', 'Либерэтор', 'Либорайо', 'Ливио', 'Линдро', 'Лино', 'Лодовико', 'Лоренцо', 'Лудовико', 'Луиджи', 'Луиджино', 'Лука', 'Лусио', 'Лучиано', 'Макарио', 'Манфредо', 'Мариано', 'Марио', 'Маркеллино', 'Марко', 'Марселло', 'Мартино', 'Марцио', 'Масо', 'Массимилиано', 'Массимо', 'Маттео', 'Маттиа', 'Маурицио', 'Мауро', 'Мелчиоре', 'Мео', 'Микелянджело', 'Михель', 'Модесто', 'Мэльволайо', 'Мэнлайо', 'Мэрино', 'Назарио', 'Нанзайо', 'Наполеоне', 'Наркизо', 'Невайо', 'Нерайо', 'Неро', 'Нестор', 'Никколо', 'Нико', 'Никодемо', 'Никола', 'Николо', 'Никомедо', 'Никострэто', 'Нино', 'Нолдо', 'Нэйтанэел', 'Овидайо', 'Орацио', 'Орландо', 'Орсино', 'Орсо', 'Орфео', 'Освальдо', 'Оттавиано', 'Оттавио', 'Паоло', 'Паскуале', 'Патрицио', 'Пеллегрино', 'Пино', 'Пио', 'Плинайо', 'Плэкидо', 'Помпео', 'Понзио', 'Порфирайо', 'Прима', 'Просперо', 'Прудензайо', 'Пьеро', 'Пьетро', 'Пэлмиро', 'Пэнкрэзайо', 'Пэнтэлеон', 'Пэнфило', 'Пэолино', 'Пэрайд', 'Пэскуэлино', 'Раггиро', 'Райль', 'Раймондо', 'Ремиджио', 'Ремо', 'Ренато', 'Рензо', 'Риккардо', 'Рико', 'Ринальдо', 'Рино', 'Роберто', 'Родолфо', 'Рокко', 'Романо', 'Ромео', 'Ромоло', 'Руджеро', 'Руфино', 'Рэниро', 'Рэффэел', 'Рэффэелло', 'Саверио', 'Самуэле', 'Сандро', 'Сантино', 'Санто', 'Себастиано', 'Северино', 'Севериэно', 'Северо', 'Селестино', 'Селсо', 'Серафино', 'Серджио', 'Сесилио', 'Сесто', 'Сеттимайо', 'Силайо', 'Силвано', 'Силвестро', 'Силвио', 'Силино', 'Симоне', 'Сисэрино', 'Ссевола', 'Стефано', 'Сэбино', 'Сэвайо', 'Сэвино', 'Сэнсоун', 'Сэтернино', 'Таддео', 'Теобальдо', 'Теодозайо', 'Теодоро', 'Теофило', 'Терензайо', 'Терзо', 'Тизиано', 'Тимотео', 'Тито', 'Томмазо', 'Тонайо', 'Торе', 'Торелло', 'Тэкито', 'Тэммэро', 'Тэнкредо', 'Уберто', 'Уго', 'Улдерико', 'Уллисе', 'Умберто', 'Урбано', 'Фабиано', 'Фабио', 'Фабрицио', 'Файорензо', 'Фальвайо', 'Фаустино', 'Фаусто', 'Федел', 'Федериго', 'Федерико', 'Фелис', 'Фелисиано', 'Фердинандо', 'Ферро', 'Ферруссио', 'Филиберто', 'Филипо', 'Филиппо', 'Филлипо', 'Фирмино', 'Флавио', 'Флориэно', 'Фонз', 'Фонзи', 'Фонс', 'Фонси', 'Фортунато', 'Франко', 'Францеско', 'Фредиэно', 'Фредо', 'Хирономо', 'Чезаре', 'Эджидио', 'Эдмондо', 'Эдоардо', 'Эззелин', 'Эзио', 'Элайодоро', 'Элиа', 'Элиджио', 'Элисео', 'Элмо', 'Элпидайо', 'Элэрайо', 'Эмануэле', 'Эмилио', 'Эмилиэно', 'Энзо', 'Эннио', 'Энрико', 'Эрколе', 'Эрманно', 'Эрмете', 'Эрминайо', 'Эрнесто', 'Эстэчайо', 'Этторе', 'Эугенио', 'Эусибио', 'Эусторжио', 'Эфизайо', 'Юстэчайо']
surnames = ['Аллегретти', 'Альберти', 'Альфьери', 'Альчато', 'Амманити', 'Анджони', 'Арджилли', 'Аретино', 'Ариосто', 'Базиле', 'Баккаларио', 'Бальбо', 'Банделло', 'Барбаро', 'Баретти', 'Барикко', 'Бассани', 'Баттисти', 'Беккариа', 'Бембо', 'Бенедетти', 'Бенни', 'Бенцони', 'Бергамо', 'Берлускони', 'Берни', 'Бетокки', 'Блази', 'Бренцони', 'Бонтемпелли', 'Бордоне', 'Босси', 'Бракко', 'Бранкати', 'Брокки', 'Бруни', 'Бруно', 'Буццати', 'Бьянки', 'Веккьони', 'Вердидзотти', 'Виванти', 'Вико', 'Витторини', 'Гверрацци', 'Гверцони', 'Гвидо', 'Герарди', 'Гисланцони', 'Гольдони', 'Гоцци', 'Грациани', 'Граццини', 'Гриффи', 'Гросси', 'Грото', 'Гуарини', 'Джаннини', 'Джордано', 'Джерманетто', 'Джоберти', 'Джованьоли', 'Джордано', 'Джорджио', 'Джусти', 'Дзабарелла', 'Дзанини', 'Дзамбони', 'Дзанетти', 'Дзендрини', 'Дзено', 'Джакомо', 'Дио', 'Донати', 'Еро', 'Кавальканти', 'Казони', 'Калассо', 'Кальвино', 'Кальцабиджи', 'Канини', 'Капаччо', 'Капелла', 'Капеллони', 'Капитини', 'Каприано', 'Кардуччи', 'Каркано', 'Карпани', 'Кастильоне', 'Квадрио', 'Корелли', 'Корренти', 'Коста', 'Кьяри', 'Ландино', 'Ландольфи', 'Леви', 'Леоне', 'Леопарди', 'Литтиццетто', 'Лоренцо', 'Луци', 'Лучано', 'Мадзини', 'Макиавелли', 'Малапарте', 'Мандзони', 'Манетти', 'Манфреди', 'Манчини', 'Марани', 'Маринетти', 'Марино', 'Мариньолли', 'Маркетти', 'Маручелли', 'Мартини', 'Масси', 'Мерлино', 'Милани', 'Милли', 'Монтанелли', 'Моравиа', 'Моранте', 'Муни', 'Муцио', 'Негри', 'Нуцци', 'Олива', 'Павезе', 'Пазолини', 'Паладини', 'Палмери', 'Панарелло', 'Папини', 'Парини', 'Патрици', 'Пачини', 'Патуцци', 'Петруччелли', 'Пьяджи', 'Риччи', 'Рокка', 'Ровере', 'Родари', 'Розетти', 'Розини', 'Рокколини', 'Ролли', 'Романо', 'Ромеи', 'Росси', 'Руссо', 'Савиано', 'Саккетти', 'Сальви', 'Сальгари', 'Сапиенца', 'Серафино', 'Серени', 'Силоне', 'Солера', 'Спациани', 'Спероне', 'Страффи', 'Табукки', 'Таркетти', 'Тассо', 'Тассони', 'Тезауро', 'Тиррито', 'Томази', 'Тоцци', 'Унгаретти', 'Фаббри', 'Фаллачи', 'Фалько', 'Фарина', 'Фарини', 'Фенольо', 'Феррари', 'Фиори', 'Фичино,', 'Марсилио', 'Фогаццаро', 'Фосколо', 'Франко', 'Фьоритто', 'Чамполи', 'Чезари', 'Черонетти', 'Эвола', 'Эко']

def getChannels():
    mafiamasterChannel = bot.get_channel(703171338646585345)

    mafiatextChannel = bot.get_channel(703170704069230594)
    mafiamafiaChannel = bot.get_channel(703170171849801798)
    mafiadonChannel = bot.get_channel(703170052647550996)
    mafiacommissionerChannel = bot.get_channel(703170136718180392)
    mafiadoctorChannel = bot.get_channel(703170021039276125)

    mafiavoiceChannel = bot.get_channel(703167135219974150)
    return {"text": mafiatextChannel, "voice": mafiavoiceChannel, "master": mafiamasterChannel, "mafia": mafiamafiaChannel, "don": mafiadonChannel, "commissioner": mafiacommissionerChannel, "doctor": mafiadoctorChannel}

def getMaster():
    channels = getChannels()
    for member in channels["master"].members:
        if not member.bot:
            return member

    return {"text": mafiatextChannel, "voice": mafiavoiceChannel, "master": mafiamasterChannel}

async def getStart(roles = []):
    global game, names, surnames
    embed = discord.Embed(title="[НАЧАЛО] Выдача ролей", colour=16711680)

    channels = getChannels()

    if len(roles) == 0:
        roles = ["" for i in range(len(channels["voice"].members))]
    else:
        for roleNumber in range(len(roles)):
            roles[roleNumber] = " (%s)"%(roles[roleNumber])

    memberNumber = 0
    for member in channels["voice"].members:

        isMaster = False
        for role in member.roles:
            if role.name == "Гей(м) мастер":
                isMaster = True
                break

        if not isMaster: 
            try:
                game["members"][memberNumber + 1]
            except:
                game["members"][memberNumber + 1] = {"id": member.id, "name": choice(names) + " " + choice(surnames), "realname": member.name, "alive": True, "role": None, "peacefulRole": None, "healedCount": 0}
                try:
                    await member.edit(nick = "(" + str(memberNumber + 1) + ") " + game["members"][memberNumber + 1]["name"])
                except:
                    print("Rename Permission Error")

            embed.add_field(name = "Игрок (%s)"%(str(memberNumber + 1)), value = game["members"][memberNumber + 1]["name"] + roles[memberNumber])
            memberNumber += 1

    embed.add_field(name = "Правила:", value = "По команде ведущего бот отправит вам вашу роль.", inline = False)
    embed.set_footer(text="Далее: День")
    return embed

def getDay():
    embeds = dict()

    msgEmbed = discord.Embed(title="[ДЕНЬ %s] Город просыпается"%(str(game["day"])), colour=7506394)
    msgEmbed.add_field(name = "Правила:", value = "Во время **Коллективного Обсуждения** говорят все живые игроки. \n\nВо время **Одинычных Высказываний** право говорить будет передаваться по очереди всем живым игрокам^. \nПосле речи игрок в праве выставить другого игрока на голосование^^. \n\nВо время **Оправдательных речей** право говорить будет дано каждому выставленному игроку^^^. \n\nВо время **Голосования** все игроки молчат и голосуют за одного из кандидатов. \n\nВо время **Последнего слова** говорит только выставленный игрок, набравший наибольшее количество голосов. \n\n\n*^ Права предоставляются игрокам в порядке возрастания их номера со смещением относительно номера дня.* \n*^^ Игрок открывающий круг обязан выставить другого игрока.* \n*^^^ Права предоставляются игрокам в том порядке, в котором они были выставлены.*", inline = False)
    msgEmbed.set_footer(text="Далее: Коллективное обсуждение")
    embeds["text"] = msgEmbed

    msgEmbed = discord.Embed(title="[ДЕНЬ %s] Город просыпается"%(str(game["day"])), colour=7506394)
    msgEmbed.add_field(name = "Команды:", value = "👨‍👨‍👦‍👦 — Коллективное обсуждение \n\n🙎‍♂️ — Одиночные выссказываения \n\n🙅‍♂️ — Оправдательные речи \n\n🤔 — Голосование \n⚠ — Проверить честность голосования \n\n🗯 — Последнее слово \n\n 🌙 — Уйти в ночь", inline = False)
    embeds["master"] = msgEmbed

    msgEmbed = discord.Embed(title="[ВЫСТАВЛЕННЫЕ ИГРОКИ]", colour=7506394)
    msgEmbed.add_field(name = "Команды:", value = "Нажмине на 0️⃣, чтобы выставить (0) ИмяИгрока", inline = False)
    embeds["exposeds"] = msgEmbed

    return embeds

def getNight():
    embeds = dict()

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Город спит"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Правила:", value = "Если вы **Мирный Житель** — спите. \n\nЕсли вы **Мафия** — зайдите в `текстовый канал мафии` и выберите кандидата. \n\nЕсли вы **Дон** — выполняйте тоже, что и **Мафия**, после этого зайдите в `текстовый канал дона` и проверьте одного из игроков. \n\nЕсли вы **Комиссар** — зайдите в `текстовый канал комиссара` и проверьте одного игрока. \n\nЕсли вы **Доктор** — зайдите в `текстовый канал доктора` и исцелите одного игрока (одного и того же игрока можно исцелять __**дважды, но не подряд**__). \n\n\n Все выборы и голосования происходят посредством выбора реакции под соответствующим сообщением. \n\n __***Внимание!***__ Если у вас выбрано несколько реакций действие совершится только с тем игроком, который имеет наименьший номер!", inline = False)
    msgEmbed.set_footer(text="Далее: Просыпается мафия")
    embeds["text"] = msgEmbed

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Просыпается МАФИЯ"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Правила:", value = "Мафии необходимо выбрать ровно одну жертву с помощью голосования. \n\n__***Внимание!***__ Если у вас выбрано несколько реакций действие совершится только с тем игроком, который имеет наименьший номер!", inline = False)
    msgEmbed.set_footer(text="Далее: Просыпается дон")
    embeds["mafia"] = msgEmbed

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Просыпается ДОН"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Правила:", value = "Дону необходимо выбрать ровно одного игрока для проверки. \n\n\n**👍 — выбранный игрок является комиссаром** \n\n**👎 — выбранный игрок НЕ является комиссаром**. \n\n\n__***Внимание!***__ Если у вас выбрано несколько реакций действие совершится только с тем игроком, который имеет наименьший номер!", inline = False)
    msgEmbed.set_footer(text="Далее: Просыпается комиссар")
    embeds["don"] = msgEmbed

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Просыпается КОМИССАР"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Правила:", value = "Комиссару необходимо выбрать ровно одного игрока для проверки. \n\n\n**👍 — выбранный игрок является мафией** \n\n**👎 — выбранный игрок НЕ является мафией**. \n\n\n__***Внимание!***__ Если у вас выбрано несколько реакций действие совершится только с тем игроком, который имеет наименьший номер!", inline = False)
    msgEmbed.set_footer(text="Далее: Просыпается доктор")
    embeds["commissioner"] = msgEmbed

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Просыпается ДОКТОР"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Правила:", value = "Доктору необходимо выбрать ровно одного игрока для исцеления (одного и того же игрока можно исцелять __**дважды, но не подряд**__). \n\n\n__***Внимание!***__ Если у вас выбрано несколько реакций действие совершится только с тем игроком, который имеет наименьший номер!", inline = False)
    msgEmbed.set_footer(text="Далее: Просыпается доктор")
    embeds["doctor"] = msgEmbed

    msgEmbed = discord.Embed(title="[НОЧЬ %s] Город спит"%(str(game["day"])), colour=0)
    msgEmbed.add_field(name = "Команды", value = "🕵 — Просыпается мафия \n\n 🕵️‍♀️ — Просыпается дон \n\n 👮 — Просыпается комиссар \n\n 👩‍⚕️ — Просыпается доктор \n\n ☀ — Начать день")
    embeds["master"] = msgEmbed

    return embeds

async def rolesReaction():
    global game, mafiamasterMessage

    channels = getChannels()

    mafiasCount = 1
    donsCount = 1
    peacefulsCount = 4
    doctorsCount = 1
    commissionerCount = 1

    roles = []
    for i in range(mafiasCount):
        roles.append("Мафия")
    for i in range(donsCount):
        roles.append("Дон")
    for i in range(peacefulsCount):
        roles.append("Мирный")
    for i in range(doctorsCount):
        roles.append("Доктор")
    for i in range(commissionerCount):
        roles.append("Комиссар")

    for channelName in channels:
        if channelName != "text" and channelName != "master":
            channel = channels[channelName]
            for member in channel.members:
                await channel.set_permissions(member, overwrite=None)

    resultRoles = []
    for memberNumber in game["members"]:
        roleNumber = randint(0, len(roles) - 1)

        role = roles[roleNumber]
        roles.pop(roleNumber)

        game["members"][memberNumber]["role"] = role
        memberChannel = bot.get_user(game["members"][memberNumber]["id"])
        await memberChannel.send("Ваша роль в этой игре: " + role)

        for member in channels["voice"].members:
            if member.id == game["members"][memberNumber]["id"]:
                if (role == "Мафия"):
                    await channels["mafia"].set_permissions(member, read_messages=True, send_messages=True)
                elif (role == "Дон"):
                    await channels["don"].set_permissions(member, read_messages=True, send_messages=True)
                    await channels["mafia"].set_permissions(member, read_messages=True, send_messages=True)
                    game["don"] = memberNumber
                elif (role == "Комиссар"):
                    await channels["commissioner"].set_permissions(member, read_messages=True, send_messages=True)
                    game["commissioner"] = memberNumber
                elif (role == "Доктор"):
                    await channels["doctor"].set_permissions(member, read_messages=True, send_messages=True)
                    game["doctor"] = memberNumber

        resultRoles.append(role)
    msgEmbed = await getStart(resultRoles)
    await mafiamasterMessage.edit(embed = msgEmbed)

@bot.command(pass_context=True)
async def start(ctx):
    global game, mafiamasterMessage, mafiatextMessage
    channels = getChannels()

    numbersEmoji = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    if ctx.channel.id == channels["master"].id:
        msgEmbed = await getStart();

        mafiamasterMessage = await channels["master"].send(embed = msgEmbed)
        await mafiamasterMessage.add_reaction('❔')
        await mafiamasterMessage.add_reaction("☀")

        mafiatextMessage = await channels["text"].send(embed = msgEmbed)

        needBreak = False
        while True:
            mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
            for reaction in mafiamasterMessage.reactions:
                if reaction.count == 2:
                    if (reaction.emoji == "❔"):
                        await rolesReaction()
                        await reaction.remove(getMaster())
                    if (reaction.emoji == "☀"):
                        needBreak = True
                        break
                        
            if needBreak:
                break

        while True:

            for member in channels["voice"].members:
                for memberNumber in game["members"]:
                    if member.id == game["members"][memberNumber]["id"] and game["members"][memberNumber]["alive"]:
                        await member.edit(mute = True)

            #Получения embeds дня
            embeds = getDay()

            mafiatextMessage = await channels["text"].send(embed = embeds["text"])

            mafiamasterMessage = await channels["master"].send(embed = embeds["master"])
            await mafiamasterMessage.add_reaction('👨‍👨‍👦‍👦')
            await mafiamasterMessage.add_reaction('🙎‍♂️')
            await mafiamasterMessage.add_reaction('🙅‍♂️')
            await mafiamasterMessage.add_reaction('🤔')
            await mafiamasterMessage.add_reaction('⚠')
            await mafiamasterMessage.add_reaction('🗯')
            await mafiamasterMessage.add_reaction('🌙')

            needBreak = False
            while not needBreak:
                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                for reaction in mafiamasterMessage.reactions:
                    if reaction.count == 2:
                        if (reaction.emoji == "👨‍👨‍👦‍👦"):

                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Коллективное обсуждение"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Коллективное обсуждение"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Одиночные высказывания")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            for member in channels["voice"].members:
                                for memberNumber in game["members"]:
                                    if member.id == game["members"][memberNumber]["id"] and game["members"][memberNumber]["alive"]:
                                        await member.edit(mute = False)

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "👨‍👨‍👦‍👦":
                                        for member in channels["voice"].members:
                                            for memberNumber in game["members"]:
                                                if member.id == game["members"][memberNumber]["id"] and game["members"][memberNumber]["alive"]:
                                                    await member.edit(mute = True)
                                        needBreak = True

                            needBreak = False
                            continue
                        
                        if (reaction.emoji == "🙎‍♂️"):
                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Одиночные высказывания"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Одиночные высказывания"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Оправдательные речи")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            for reaction in mafiamasterMessage.reactions:
                                await reaction.clear()

                            mafiamasterMessageExposeds = await channels["master"].send(embed = embeds["exposeds"])

                            for memberNumber in game["members"]:
                                if game["members"][memberNumber]["alive"]:
                                    await mafiamasterMessage.add_reaction(numbersEmoji[memberNumber])
                            await mafiamasterMessage.add_reaction("⬅")


                            for memberNumber in game["members"]:
                                if game["members"][memberNumber]["alive"]:
                                    await mafiamasterMessageExposeds.add_reaction(numbersEmoji[memberNumber])

                            
                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if (reaction.count == 2):
                                        if (reaction.emoji != "⬅"):
                                            sayerEmoji = reaction.emoji
                                            sayerNumber = numbersEmoji.index(reaction.emoji)
                                            seyerMember = None
                                            for member in channels["voice"].members:
                                                if member.id == game["members"][sayerNumber]["id"]:
                                                    seyerMember = member
                                                    await seyerMember.edit(mute = False)
                                                    break
                                            while not needBreak:
                                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                                for reaction in mafiamasterMessage.reactions:
                                                    if reaction.count == 1 and reaction.emoji == sayerEmoji:
                                                        await seyerMember.edit(mute = True)
                                                        needBreak = True
                                                        break
                                            needBreak = False
                                        else:

                                            mafiamasterMessageExposeds = await channels["master"].fetch_message(mafiamasterMessageExposeds.id)
                                            for reaction in mafiamasterMessageExposeds.reactions:
                                                if reaction.count == 2:
                                                    exposedNumber = numbersEmoji.index(reaction.emoji)
                                                    game["exposeds"].add(exposedNumber)
                                            await mafiamasterMessageExposeds.delete()

                                            for reaction in mafiamasterMessage.reactions:
                                                await reaction.clear()
                                            await mafiamasterMessage.add_reaction('👨‍👨‍👦‍👦')
                                            await mafiamasterMessage.add_reaction('🙎‍♂️')
                                            await mafiamasterMessage.add_reaction('🙅‍♂️')
                                            await mafiamasterMessage.add_reaction('🤔')
                                            await mafiamasterMessage.add_reaction('⚠')
                                            await mafiamasterMessage.add_reaction('🗯')
                                            await mafiamasterMessage.add_reaction('🌙')

                                            needBreak = True
                                            break
                            needBreak = False
                            continue

                        if (reaction.emoji == "🙅‍♂️"):
                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Оправдательные речи"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Оправдательные речи"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Голосование")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            for reaction in mafiamasterMessage.reactions:
                                await reaction.clear()

                            for memberNumber in game["members"]:
                                if memberNumber in game["exposeds"]:
                                    await mafiamasterMessage.add_reaction(numbersEmoji[memberNumber])

                            await mafiamasterMessage.add_reaction("⬅")
                            
                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if (reaction.count == 2):
                                        if (reaction.emoji != "⬅"):
                                            sayerEmoji = reaction.emoji
                                            sayerNumber = numbersEmoji.index(reaction.emoji)
                                            seyerMember = None
                                            for member in channels["voice"].members:
                                                if member.id == game["members"][sayerNumber]["id"]:
                                                    seyerMember = member
                                                    await seyerMember.edit(mute = False)
                                                    break
                                            while not needBreak:
                                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                                for reaction in mafiamasterMessage.reactions:
                                                    if reaction.count == 1 and reaction.emoji == sayerEmoji:
                                                        await seyerMember.edit(mute = True)
                                                        needBreak = True
                                                        break
                                            needBreak = False
                                        else:
                                            for reaction in mafiamasterMessage.reactions:
                                                await reaction.clear()
                                            await mafiamasterMessage.add_reaction('👨‍👨‍👦‍👦')
                                            await mafiamasterMessage.add_reaction('🙎‍♂️')
                                            await mafiamasterMessage.add_reaction('🙅‍♂️')
                                            await mafiamasterMessage.add_reaction('🤔')
                                            await mafiamasterMessage.add_reaction('⚠')
                                            await mafiamasterMessage.add_reaction('🗯')
                                            await mafiamasterMessage.add_reaction('🌙')

                                            needBreak = True
                                            break
                            needBreak = False
                            continue

                        if (reaction.emoji == "🤔"):

                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Голосование"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Голосование"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Последнее слово")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            for reaction in mafiatextMessage.reactions:
                                await reaction.clear()

                            for memberNumber in game["members"]:
                                if memberNumber in game["exposeds"]:
                                    await mafiatextMessage.add_reaction(numbersEmoji[memberNumber])
                            await mafiatextMessage.add_reaction("⛔")

                            dayEmbed = discord.Embed(title="[ДЕНЬ %s] Голосование"%(str(game["day"])), colour=7506394)
                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "🤔":
                                        mafiatextMessage = await channels["text"].fetch_message(mafiatextMessage.id)
                                        max = {}
                                        for reaction in mafiatextMessage.reactions:
                                            try:
                                                max[reaction.count - 1].append(reaction.emoji)
                                            except:
                                                max[reaction.count - 1] = []
                                                max[reaction.count - 1].append(reaction.emoji)

                                        maxValue = sorted(max, reverse = True)[0]

                                        game["exposeds"].clear()
                                        if (len(max[maxValue]) > 1):
                                            for emoji in max[maxValue]:
                                                try:
                                                    game["exposeds"].add(numbersEmoji.index(emoji))
                                                except:
                                                    if len(max[maxValue]) == 2:
                                                        msgEmbed = mafiamasterMessage.embeds[0]
                                                        msgEmbed.set_footer(text = "⚠ Голосованием выбран (%s) %s"%(str(list(game["exposeds"])[0]), game["members"][list(game["exposeds"])[0]]["name"]))
                                                        dayEmbed.add_field(name = "Результат:", value= "**(%s) %s** убит."%(str(list(game["exposeds"])[0]), game["members"][list(game["exposeds"])[0]]["name"]), inline = False)
                                                        game["members"][list(game["exposeds"])[0]]["alive"] = False
                                                        await mafiamasterMessage.edit(embed = msgEmbed)
                                                        needBreak = True
                                                        break
                                            if needBreak:
                                                break

                                            msgEmbed = mafiamasterMessage.embeds[0]
                                            msgEmbed.set_footer(text = "⚠ Голосование не выявило единственного кандидата — создан новый список кандидатов")
                                            dayEmbed.add_field(name = "Результат:", value= "Никто не погиб.", inline = False)
                                            await mafiamasterMessage.edit(embed = msgEmbed)
                                        else:
                                            if max[maxValue][0] != "⛔":
                                                game["exposeds"].add(numbersEmoji.index(max[maxValue][0]))
                                                msgEmbed = mafiamasterMessage.embeds[0]
                                                msgEmbed.set_footer(text = "⚠ Голосованием выбран (%s) %s"%(str(list(game["exposeds"])[0]), game["members"][list(game["exposeds"])[0]]["name"]))
                                                dayEmbed.add_field(name = "Результат:", value= "**(%s) %s** убит."%(str(list(game["exposeds"])[0]), game["members"][list(game["exposeds"])[0]]["name"]), inline = False)
                                                game["members"][list(game["exposeds"])[0]]["alive"] = False
                                                await mafiamasterMessage.edit(embed = msgEmbed)
                                            else:
                                                msgEmbed = mafiamasterMessage.embeds[0]
                                                msgEmbed.set_footer(text = "⚠ Голосование не выявило единственного кандидата — создан новый список кандидатов")
                                                dayEmbed.add_field(name = "Результат:", value= "Никто не погиб.", inline = False)
                                                await mafiamasterMessage.edit(embed = msgEmbed)

                                        needBreak = True
                                        break
                                    
                                    if reaction.count == 2 and reaction.emoji == "⚠":
                                        errors = dict()
                                        mafiatextMessage = await channels["text"].fetch_message(mafiatextMessage.id)
                                        for voteReaction in mafiatextMessage.reactions:
                                            reactionMembers = await voteReaction.users().flatten()
                                            for member in reactionMembers:
                                                try:
                                                    errors[member.display_name]["votes"].append(voteReaction.emoji)
                                                except:
                                                    for memberNumber in game["members"]:
                                                        if game["members"][memberNumber]["id"] == member.id:
                                                            if game["members"][memberNumber]["alive"]:
                                                                errors[member.display_name] = {"alive": True, "votes": [voteReaction.emoji]}
                                                            else:
                                                                errors[member.display_name] = {"alive": False, "votes": [voteReaction.emoji]}
                                        errorMessage = ""
                                        for memberName in errors:
                                            if errors[memberName]["alive"]:
                                                if len(errors[memberName]["votes"]) > 1:
                                                    errorMessage += "\n%s одновременно проголосовал за — "%(memberName) + " ".join(errors[memberName]["votes"])
                                            else:
                                                errorMessage += "\n%s мертв, но одновременно проголосовал за — "%(memberName) + " ".join(errors[memberName]["votes"])

                                        for memberNumber in game["members"]:
                                            if game["members"][memberNumber]["alive"]:
                                                if not "(%s) %s"%(memberNumber, game["members"][memberNumber]["name"]) in errors:
                                                    errorMessage += "\n(%s) %s не проголосовал"%(memberNumber, game["members"][memberNumber]["name"])

                                        if len(errorMessage) == 0:
                                            errorMessage += "Голосование проводится правильно"

                                        msgEmbed = mafiamasterMessage.embeds[0]
                                        msgEmbed.set_footer(text=errorMessage)
                                        await mafiamasterMessage.edit(embed = msgEmbed)

                                        await reaction.remove(getMaster())


                            for reaction in mafiatextMessage.reactions:
                                members = await reaction.users().flatten() 
                                delta = 0
                                for memberNumber in range(len(members)):
                                    memberNumber -= delta
                                    if members[memberNumber].bot:
                                        members.pop(memberNumber)
                                        delta += 1
                                    else:
                                        members[memberNumber] = members[memberNumber].display_name


                                if len(members) == 0:
                                    members = ["Никто"]

                                try:
                                    memberNumber = numbersEmoji.index(reaction.emoji)
                                    dayEmbed.add_field(name = "(%s) %s:"%(memberNumber, game["members"][memberNumber]["name"]), value = "\n".join(members), inline = False)
                                except:
                                    dayEmbed.add_field(name = "Воздержались:", value = "\n".join(members), inline = False)
                                await reaction.clear()

                            dayEmbed.set_footer(text="Далее: Последнее слово")
                            await mafiatextMessage.edit(embed = dayEmbed)
                            
                            needBreak = False
                            continue

                        if (reaction.emoji == "🗯"):
                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Последнее слово"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] Последнее слово"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Завершение дня")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            print(1)
                            for member in channels["voice"].members:
                                if member.id == game["members"][list(game["exposeds"])[0]]["id"]:
                                    seyerMember = member
                                    await seyerMember.edit(mute = False)

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "🗯":
                                        await seyerMember.edit(mute = True)
                                        needBreak = True
                            needBreak = False
                            continue

                        if (reaction.emoji == "🌙"):
                            msgEmbed = mafiamasterMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] ЗАВЕРШЕН"%(game["day"])
                            await mafiamasterMessage.edit(embed = msgEmbed)

                            msgEmbed = mafiatextMessage.embeds[0]
                            msgEmbed.title = "[ДЕНЬ %s] ЗАВЕРШЕН"%(game["day"])
                            msgEmbed.set_footer(text = "Далее: Ночь")
                            await mafiatextMessage.edit(embed = msgEmbed)

                            needBreak = True

            mafia = 0
            all = 0
            for memberNumber in game["members"]:
                if game["members"][memberNumber]["alive"]:
                    all += 1
                    if game["members"][memberNumber]["role"] in ["Мафия", "Дон"]:
                        mafia += 1
            game["balance"] = mafia / all

            if not 0 < game["balance"] < 0.5:
                if game["balance"] >= 0.5:
                    resultEmbed = discord.Embed(title="[МАФИЯ] ЗАВЕРШЕНА", colour=0)
                    resultEmbed.add_field(name = "Победила:", value = "Мафия", inline = False)
                elif game["balance"] == 0:
                    resultEmbed = discord.Embed(title="[МАФИЯ] ЗАВЕРШЕНА", colour=65280)
                    resultEmbed.add_field(name = "Победили:", value = "Мирные", inline = False)

                for member in channels["voice"].members:
                    await member.edit(mute = False)

                mafiatextMessage = await channels["text"].send(embed = resultEmbed)
                mafiatextMessage = await channels["master"].send(embed = resultEmbed)
                break

            #Получения embeds ночи
            embeds = getNight()

            mafiatextMessage = await channels["text"].send(embed = embeds["text"])

            mafiamasterMessage = await channels["master"].send(embed = embeds["master"])
            await mafiamasterMessage.add_reaction("🕵")
            await mafiamasterMessage.add_reaction("⚠")
            await mafiamasterMessage.add_reaction("🕵️‍♀️")
            await mafiamasterMessage.add_reaction("👮")
            await mafiamasterMessage.add_reaction("👩‍⚕️")
            await mafiamasterMessage.add_reaction("☀")

            needBreak = False
            while not needBreak:
                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                for reaction in mafiamasterMessage.reactions:
                    if reaction.count == 2:
                        if (reaction.emoji == "🕵"):
                            mafiamafiaMessage = await channels["mafia"].send(embed = embeds["mafia"])
                            for memberNumber in game["members"]:
                                if game["members"][memberNumber]["alive"]:
                                    await mafiamafiaMessage.add_reaction(numbersEmoji[memberNumber])
                            await mafiamafiaMessage.add_reaction('⛔')

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "🕵":
                                        mafiamafiaMessage = await channels["mafia"].fetch_message(mafiamafiaMessage.id)
                                        max = ["", 1]
                                        for reaction in mafiamafiaMessage.reactions:
                                            if max[1] < reaction.count:
                                                max[0] = reaction.emoji
                                                max[1] = reaction.count
                                            await reaction.clear()

                                        msgEmbed = discord.Embed(title="[НОЧЬ] ЗАВЕРШЕНА", colour=0)

                                        try:
                                            killNumber = numbersEmoji.index(max[0])
                                            game["deadToday"] = killNumber
                                            msgEmbed.add_field(name = "Результат:", value = "Убит: (" + str(killNumber) + ") " + game["members"][killNumber]["name"], inline = False)
                                        except:
                                            game["deadToday"] = None
                                            msgEmbed.add_field(name = "Результат:", value = "Никто не был убит.", inline = False)

                                        msgEmbed.set_footer(text="Далее: Просыпается дон")
                                        await mafiamafiaMessage.edit(embed = msgEmbed)
                                        needBreak = True

                                    if reaction.count == 2 and reaction.emoji == "⚠":
                                        errors = dict()
                                        mafiamafiaMessage = await channels["mafia"].fetch_message(mafiamafiaMessage.id)
                                        for voteReaction in mafiamafiaMessage.reactions:
                                            reactionMembers = await voteReaction.users().flatten()
                                            for member in reactionMembers:
                                                try:
                                                    errors[member.display_name]["votes"].append(voteReaction.emoji)
                                                except:
                                                    for memberNumber in game["members"]:
                                                        if game["members"][memberNumber]["id"] == member.id:
                                                            if game["members"][memberNumber]["alive"]:
                                                                errors[member.display_name] = {"alive": True, "votes": [voteReaction.emoji]}
                                                            else:
                                                                errors[member.display_name] = {"alive": False, "votes": [voteReaction.emoji]}
                                        errorMessage = ""
                                        print(errors)
                                        for memberName in errors:
                                            if errors[memberName]["alive"]:
                                                if len(errors[memberName]["votes"]) > 1:
                                                    errorMessage += "\n%s одновременно проголосовал за — "%(memberName) + " ".join(errors[memberName]["votes"])
                                            else:
                                                errorMessage += "\n%s мертв, но одновременно проголосовал за — "%(memberName) + " ".join(errors[memberName]["votes"])

                                        for memberNumber in game["members"]:
                                            if game["members"][memberNumber]["alive"] and (game["members"][memberNumber]["role"] == "Мафия" or game["members"][memberNumber]["role"] == "Дон"):
                                                if not "(%s) %s"%(memberNumber, game["members"][memberNumber]["name"]) in errors:
                                                    errorMessage += "\n(%s) %s не проголосовал"%(memberNumber, game["members"][memberNumber]["name"])

                                        if len(errorMessage) == 0:
                                            errorMessage += "Голосование проводится правильно"

                                        msgEmbed = mafiamasterMessage.embeds[0]
                                        msgEmbed.set_footer(text=errorMessage)
                                        await mafiamasterMessage.edit(embed = msgEmbed)

                                        await reaction.remove(getMaster())
                            needBreak = False
                            continue

                        if (reaction.emoji == "🕵️‍♀️"):
                            mafiadonMessage = await channels["don"].send(embed = embeds["don"])
                            if game["members"][game["don"]]["alive"]:
                                for memberNumber in game["members"]:
                                    if game["members"][memberNumber]["alive"]:
                                        await mafiadonMessage.add_reaction(numbersEmoji[memberNumber])
                                await mafiadonMessage.add_reaction('⛔')

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "🕵️‍♀️":
                                        mafiadonMessage = await channels["don"].fetch_message(mafiadonMessage.id)
                                        checkEmoji = None
                                        for reaction in mafiadonMessage.reactions:
                                            if reaction.count == 2 and checkEmoji == None:
                                                checkEmoji = reaction.emoji
                                            await reaction.clear()

                                        msgEmbed = discord.Embed(title="[НОЧЬ] ЗАВЕРШЕНА", colour=0)

                                        try:
                                            checkNumber = numbersEmoji.index(checkEmoji)
                                            if game["members"][checkNumber]["role"] == "Комиссар":
                                                msgEmbed.add_field(name = "Результат:", value = "(" + str(checkNumber) + ") " + game["members"][checkNumber]["name"] + " — 👍", inline = False)
                                            else: 
                                                msgEmbed.add_field(name = "Результат:", value = "(" + str(checkNumber) + ") " + game["members"][checkNumber]["name"] + " — 👎", inline = True)
                                        except:
                                            game["deadToday"] = None
                                            msgEmbed.add_field(name = "Результат:", value = "Никто не был проверен.", inline = False)

                                        msgEmbed.set_footer(text="Далее: Просыпается комиссар")
                                        await mafiadonMessage.edit(embed = msgEmbed)
                                        needBreak = True
                            needBreak = False
                            continue

                        if (reaction.emoji == "👮"):
                            mafiacommissionerMessage = await channels["commissioner"].send(embed = embeds["commissioner"])
                            if game["members"][game["commissioner"]]["alive"]:
                                for memberNumber in game["members"]:
                                    if game["members"][memberNumber]["alive"]:
                                        await mafiacommissionerMessage.add_reaction(numbersEmoji[memberNumber])
                                await mafiacommissionerMessage.add_reaction('⛔')

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "👮":
                                        mafiacommissionerMessage = await channels["commissioner"].fetch_message(mafiacommissionerMessage.id)
                                        checkEmoji = None
                                        for reaction in mafiacommissionerMessage.reactions:
                                            if reaction.count == 2 and checkEmoji == None:
                                                checkEmoji = reaction.emoji
                                            await reaction.clear()

                                        msgEmbed = discord.Embed(title="[НОЧЬ] ЗАВЕРШЕНА", colour=0)

                                        try:
                                            checkNumber = numbersEmoji.index(checkEmoji)
                                            if game["members"][checkNumber]["role"] == "Мафия" or game["members"][checkNumber]["role"] == "Дон":
                                                msgEmbed.add_field(name = "Результат:", value = "(" + str(checkNumber) + ") " + game["members"][checkNumber]["name"] + " — 👍", inline = False)
                                            else: 
                                                msgEmbed.add_field(name = "Результат:", value = "(" + str(checkNumber) + ") " + game["members"][checkNumber]["name"] + " — 👎", inline = True)
                                        except:
                                            msgEmbed.add_field(name = "Результат:", value = "Никто не был проверен.", inline = False)

                                        msgEmbed.set_footer(text="Далее: Просыпается доктор")
                                        await mafiacommissionerMessage.edit(embed = msgEmbed)
                                        needBreak = True
                            needBreak = False
                            continue

                        if (reaction.emoji == "👩‍⚕️"):
                            mafiadoctorMessage = await channels["doctor"].send(embed = embeds["doctor"])
                            if game["members"][game["doctor"]]["alive"]:
                                for memberNumber in game["members"]:
                                    if game["members"][memberNumber]["alive"] and memberNumber != game["healToday"] and game["members"][memberNumber]["healedCount"] < 2:
                                        await mafiadoctorMessage.add_reaction(numbersEmoji[memberNumber])
                                await mafiadoctorMessage.add_reaction('⛔')

                            needBreak = False
                            while not needBreak:
                                mafiamasterMessage = await channels["master"].fetch_message(mafiamasterMessage.id)
                                for reaction in mafiamasterMessage.reactions:
                                    if reaction.count == 1 and reaction.emoji == "👩‍⚕️":
                                        mafiadoctorMessage = await channels["doctor"].fetch_message(mafiadoctorMessage.id)
                                        healEmoji = None
                                        for reaction in mafiadoctorMessage.reactions:
                                            if reaction.count == 2 and healEmoji== None:
                                                healEmoji= reaction.emoji
                                            await reaction.clear()

                                        msgEmbed = discord.Embed(title="[НОЧЬ] ЗАВЕРШЕНА", colour=0)

                                        try:
                                            healNumber = numbersEmoji.index(healEmoji)
                                            game["members"][healNumber]["healedCount"] += 1
                                            game["healToday"] = healNumber
                                            if game["deadToday"] == healNumber:
                                                game["deadToday"] = None
                                            msgEmbed.add_field(name = "Результат:", value = "(" + str(healNumber) + ") " + game["members"][healNumber]["name"] + " — исцелен", inline = True)
                                        except ValueError:
                                            msgEmbed.add_field(name = "Результат:", value = "Никто не был исцелен.", inline = False)

                                        msgEmbed.set_footer(text="Далее: Просыпается город")
                                        await mafiadoctorMessage.edit(embed = msgEmbed)
                                        needBreak = True
                            needBreak = False
                            continue 

                        if (reaction.emoji == "☀"):

                            print(game["deadToday"], game["healToday"])

                            embeds["text"] = discord.Embed(title="[НОЧЬ %s] ЗАВЕРШЕНА"%(game["day"]), colour=0)
                            if (game["deadToday"] != None):
                                embeds["text"].add_field(name = "Результат:", value = "Убит: (" + str(killNumber) + ") " + game["members"][killNumber]["name"], inline = False)
                                game["members"][game["deadToday"]]["alive"] = False
                            else:
                                embeds["text"].add_field(name = "Результат:", value = "Никто не был убит.", inline = False)
                            embeds["text"].set_footer(text="Далее: Просыпается город")

                            await mafiatextMessage.edit(embed = embeds["text"])
                            needBreak = True
                            break

            mafia = 0
            all = 0
            for memberNumber in game["members"]:
                if game["members"][memberNumber]["alive"]:
                    all += 1
                    if game["members"][memberNumber]["role"] in ["Мафия", "Дон"]:
                        mafia += 1
            game["balance"] = mafia / all

            if not 0 < game["balance"] < 0.5:
                if game["balance"] >= 0.5:
                    resultEmbed = discord.Embed(title="[МАФИЯ] ЗАВЕРШЕНА", colour=0)
                    resultEmbed.add_field(name = "Победила:", value = "Мафия", inline = False)
                elif game["balance"] == 0:
                    resultEmbed = discord.Embed(title="[МАФИЯ] ЗАВЕРШЕНА", colour=65280)
                    resultEmbed.add_field(name = "Победили:", value = "Мирные", inline = False)

                for member in channels["voice"].members:
                    await member.edit(mute = False)

                mafiatextMessage = await channels["text"].send(embed = resultEmbed)
                mafiatextMessage = await channels["master"].send(embed = resultEmbed)
                break

            game["exposeds"].clear()
            game["day"] += 1

        for member in channels["voice"].members:
            for memberNumber in game["members"]:
                if member.id == game["members"][memberNumber]["id"]:
                    await member.edit(name = game["members"][memberNumber]["realname"])


@bot.command(pass_context=True)
async def check(ctx):
    global game
    channels = getChannels()
    if ctx.channel.id == channels["master"].id:

        print(bot.channels)

        #msgEmbed = discord.Embed(title="Коллективное обсуждение (60)", colour=7506394)
        #msgEmbed.add_field(name = "Правила", value = "Во время коллективного обсуждения могут говорить все живые игроки")
        #msgEmbed.set_footer(text="Далее одиночные высказывания")

        #msgEmbed = discord.Embed(title="[ДЕНЬ] Одиночные высказывания (60)", colour=7506394)
        #msgEmbed.add_field(name = "Говорил:", value = "(2) TRTL2fast4u")
        #msgEmbed.add_field(name = "Говорит:", value = "(1) G4meOv3r")
        #msgEmbed.add_field(name = "Будет говорить:", value = "(3) KITmani")
        #msgEmbed.add_field(name = "Правила:", value = "Во время одиночных высказываний может говорить только конкретный игрок. После речи игрок в праве выставить другого игрока на голосование.", inline = False)
        #msgEmbed.add_field(name = "Выставлены:", value = "(1) G4meOv3r, (2) TRTL2fast4u, (3) KITmani", inline = False)
        #msgEmbed.set_footer(text="Далее: Голосование")

        embeds = getDay()
        msg = await ctx.send(embed = embeds["day"])

        #embeds = getNight()
        #msg = await ctx.send(embed = embeds["text"])
        #msg = await ctx.send(embed = embeds["mafia"])
        #msg = await ctx.send(embed = embeds["don"])
        #msg = await ctx.send(embed = embeds["commissioner"])
        #msg = await ctx.send(embed = embeds["doctor"])
        #msg = await ctx.send(embed = embeds["master"])

        #await msg.add_reaction('1️⃣')
        #await msg.add_reaction('2️⃣')
        #await msg.add_reaction('3️⃣')
        #await msg.add_reaction('4️⃣')
        #await msg.add_reaction('5️⃣')
        #await msg.add_reaction('6️⃣')
        #await msg.add_reaction('7️⃣')
        #await msg.add_reaction('8️⃣')
        #await msg.add_reaction('9️⃣')
        #await msg.add_reaction('🔟')
        #await msg.add_reaction('⏩')
        #await msg.add_reaction('⏭')

bot.run(TOKEN)