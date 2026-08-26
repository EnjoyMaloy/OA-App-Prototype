# Генератор черновика: 30 вариантов блока «Программа курса»
OUT = '/home/user/OA-App-Prototype/prototypes/curriculum.html'

L = [
    dict(n="01", t="Что такое Telegram Gifts", d="6 мин", kind="video", st="done"),
    dict(n="02", t="Создаём первый подарок", d="10 мин", kind="video", st="current"),
    dict(n="03", t="Коллекции и редкость", d="12 мин", kind="quiz", st="next"),
    dict(n="04", t="Монетизация подарков", d="14 мин", kind="text", st="locked"),
]

PLAY = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linejoin="round"><path d="m6 3 14 9-14 9z"/></svg>')
PLAYF = '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="m6 3 14 9-14 9z"/></svg>'
CHECK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>')
LOCK = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>')
CHEV = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>')
CHEVD = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>')
ICON = {
    "video": ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
              'stroke-linejoin="round"><rect x="2" y="5" width="14" height="14" rx="3"/><path d="m16 12 6-4v8z"/></svg>'),
    "quiz": ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
             'stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3 2.4V13"/>'
             '<path d="M12 16.5v.01"/></svg>'),
    "text": ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
             'stroke-linecap="round"><path d="M5 3h9l5 5v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/>'
             '<path d="M14 3v6h5"/><path d="M8 13h8M8 17h5"/></svg>'),
}
KIND_RU = {"video": "Видео", "quiz": "Квиз", "text": "Конспект"}
THUMB = {"video": "linear-gradient(135deg,#DCE9FB,#A9C7F5)", "quiz": "linear-gradient(135deg,#FFE7DA,#FFB68F)",
         "text": "linear-gradient(135deg,#E8DCFB,#C4A6FF)"}

BUF = []


def block(code, title, cap, body):
    BUF.append('  <section class="variant">\n'
               '    <h2>' + code + '. ' + title + '</h2>\n'
               '    <p class="variant__cap">' + cap + '</p>\n'
               + body + '\n  </section>\n')


def wrap(cls, inner):
    return '    <div class="' + cls + '">\n' + inner + '\n    </div>'


def rows(fn, cls="l", items=None):
    src = items if items is not None else L
    return wrap(cls, "\n".join('      ' + fn(i, c) for i, c in enumerate(src)))


def numbox(c, cls=""):
    return '<span class="numbox ' + cls + '">' + c["n"] + '</span>'


def dur(c, icon=PLAY):
    return '<span class="dur">' + icon + c["d"] + '</span>'


def ttl(c, cls=""):
    return '<span class="ttl ' + cls + '">' + c["t"] + '</span>'


def li(inner, cls=""):
    return '<div class="li ' + cls + '">' + inner + '</div>'


# ================================================================ A. Списки
block("P1", "Как сейчас", "Общая подложка, номер в белом квадрате, длительность справа.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + dur(c)), "l l--card l--div"))

block("P2", "Без подложки, разделители", "Список лежит прямо на фоне, строки разделены линиями — легче и воздушнее.",
      rows(lambda i, c: li(numbox(c, "numbox--ghost") + ttl(c) + dur(c)), "l l--rule"))

block("P3", "Каждый урок — карточка", "Отдельные карточки: удобно тапать, видно границу урока.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + dur(c), "li--card"), "l l--gap"))

block("P4", "Крупная цифра", "Номер — крупная светлая цифра без плашки, взгляд идёт по колонке номеров.",
      rows(lambda i, c: li('<span class="bignum">' + c["n"] + '</span>' + ttl(c) + dur(c)), "l l--card l--div"))

block("P5", "Точки-маркеры", "Вместо номеров — точки: список читается как оглавление, а не как таблица.",
      rows(lambda i, c: li('<span class="dot"></span>' + ttl(c) + dur(c)), "l l--rule"))

# ================================================================ B. Прогресс
def ring(pct, label):
    import math
    r = 13
    circ = 2 * math.pi * r
    off = circ * (1 - pct / 100)
    return ('<span class="ring"><svg width="34" height="34" viewBox="0 0 34 34">'
            '<circle cx="17" cy="17" r="' + str(r) + '" fill="none" stroke="hsl(var(--border))" stroke-width="3"/>'
            '<circle cx="17" cy="17" r="' + str(r) + '" fill="none" stroke="hsl(var(--primary))" stroke-width="3" '
            'stroke-linecap="round" stroke-dasharray="' + format(circ, '.1f') + '" '
            'stroke-dashoffset="' + format(off, '.1f') + '" transform="rotate(-90 17 17)"/></svg>'
            '<i>' + label + '</i></span>')


PCT = {"done": 100, "current": 40, "next": 0, "locked": 0}
block("P6", "Кольцо прогресса", "У каждого урока своё кольцо: сразу видно, что начато и что дочитано.",
      rows(lambda i, c: li(ring(PCT[c["st"]], c["n"]) + ttl(c) + dur(c)), "l l--card l--div"))

def state_mark(c):
    if c["st"] == "done":
        return '<span class="mark mark--done">' + CHECK + '</span>'
    if c["st"] == "current":
        return '<span class="mark mark--now">' + PLAYF + '</span>'
    return '<span class="mark">' + c["n"] + '</span>'


block("P7", "Галочки и текущий урок", "Пройденное отмечено галочкой, текущее — плей, остальное просто номер.",
      rows(lambda i, c: li(state_mark(c) + ttl(c, "ttl--dim" if c["st"] in ("next", "locked") else "") + dur(c)),
           "l l--card l--div"))

def with_bar(i, c):
    bar = ('<span class="bar"><i style="width:' + str(PCT[c["st"]]) + '%"></i></span>') if c["st"] == "current" else ''
    return li('<span class="col">' + '<span class="row">' + state_mark(c) + ttl(c) + dur(c) + '</span>' + bar + '</span>')


block("P8", "Полоска под уроком", "Тонкая полоса показывает, сколько урока пройдено — как в плеере.",
      rows(with_bar, "l l--card l--div"))

block("P9", "«Вы здесь»", "Текущий урок выделен заливкой и подписью — точка возврата видна с прокрутки.",
      rows(lambda i, c: li(state_mark(c) + '<span class="col">' + ttl(c)
                           + ('<span class="here">Продолжить отсюда</span>' if c["st"] == "current" else '')
                           + '</span>' + dur(c), "li--now" if c["st"] == "current" else ""),
           "l l--card l--div"))

head_progress = ('      <div class="phead"><span class="phead__t">Пройден 1 из 4 уроков</span>'
                 '<span class="phead__p">25%</span></div>\n'
                 '      <div class="pbar"><i style="width:25%"></i></div>\n')
block("P10", "Прогресс всего курса сверху", "Шапка со счётчиком и полосой: сколько уже позади, до списка уроков.",
      wrap("l l--card l--div", head_progress + "\n".join(
          '      ' + li(state_mark(c) + ttl(c) + dur(c)) for c in L)))

# ================================================================ C. Таймлайн
block("P11", "Таймлайн", "Вертикальная линия связывает уроки в маршрут, точки — состояние.",
      rows(lambda i, c: li('<span class="tl"><i class="' + ('tl--on' if c["st"] == "done" else '') + '"></i></span>'
                           + '<span class="col">' + ttl(c) + '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></span>',
                           "li--tl"), "l l--tl"))

block("P12", "Пунктир как на карте курса", "Тот же приём, что в карте уроков: пунктирная нить и точки-станции.",
      rows(lambda i, c: li('<span class="tl tl--dash"><i class="' + ('tl--on' if c["st"] == "done" else '') + '"></i></span>'
                           + '<span class="col">' + ttl(c) + '<span class="sub">' + c["d"] + '</span></span>',
                           "li--tl"), "l l--tl l--tldash"))

snake = "\n".join(
    '      <div class="snake__i" style="margin-left:' + str([0, 56, 112, 56][i]) + 'px">'
    '<span class="snake__c ' + ('snake__c--on' if c["st"] == "done" else ('snake__c--now' if c["st"] == "current" else '')) + '">'
    + (CHECK if c["st"] == "done" else (PLAYF if c["st"] == "current" else c["n"])) + '</span>'
    '<span class="snake__l">' + c["t"] + '</span></div>' for i, c in enumerate(L))
block("P13", "Путь-змейка", "Уроки идут дорожкой, как в игровых курсах — движение вперёд читается физически.",
      wrap("snake", snake))

block("P14", "Колонка длительности", "Слева время урока крупно, справа название — как расписание.",
      rows(lambda i, c: li('<span class="time">' + c["d"].replace(" мин", "") + '<i>мин</i></span>' + '<span class="col">'
                           + ttl(c) + '<span class="sub">' + KIND_RU[c["kind"]] + '</span></span>', "li--time"), "l l--rule"))

# ================================================================ D. Модули
MOD = [("Основы", L[:2]), ("Практика", L[2:])]

def acc(open_first=True, preview=0):
    out = []
    for mi, (name, items) in enumerate(MOD):
        opened = open_first and mi == 0
        body = ""
        show = items if opened else items[:preview]
        if show:
            body = '<div class="acc__b">' + "".join(
                li(state_mark(c) + ttl(c) + dur(c)) for c in show) + '</div>'
        out.append('      <div class="acc__i">'
                   '<div class="acc__h"><span class="acc__n">' + str(mi + 1) + '</span>'
                   '<span class="col"><span class="ttl">' + name + '</span>'
                   '<span class="sub">' + str(len(items)) + ' урока · ' + str(sum(int(c["d"].split()[0]) for c in items)) + ' мин</span></span>'
                   '<span class="acc__c">' + (CHEVD if opened else CHEV) + '</span></div>' + body + '</div>')
    return "\n".join(out)


block("P15", "Аккордеон модулей", "Модули свёрнуты, открыт только текущий — длинная программа помещается на экран.",
      wrap("acc", acc()))

block("P16", "Модуль с описанием", "У модуля своя строка-подпись: чему научит и сколько займёт.",
      wrap("acc acc--plain", acc()))

block("P17", "Превью двух уроков", "Свёрнутый модуль показывает первые уроки — понятно, что внутри, без раскрытия.",
      wrap("acc", acc(open_first=False, preview=2)))

tabs = ('      <div class="tabs"><span class="tabs__i tabs__i--on">Основы</span>'
        '<span class="tabs__i">Практика</span><span class="tabs__i">Бонусы</span></div>\n'
        + "\n".join('      ' + li(state_mark(c) + ttl(c) + dur(c)) for c in L[:2]))
block("P18", "Табы модулей", "Модули переключаются табами — список всегда короткий.",
      wrap("l l--card l--div", tabs))

# ================================================================ E. Тип контента
block("P19", "Иконка типа урока", "Видео, конспект и квиз различаются иконкой — программа перестаёт быть однородной.",
      rows(lambda i, c: li('<span class="kind">' + ICON[c["kind"]] + '</span>' + ttl(c) + dur(c)), "l l--card l--div"))

block("P20", "Миниатюра урока", "Слева превью кадра: страница выглядит как плейлист.",
      rows(lambda i, c: li('<span class="thumb" style="background:' + THUMB[c["kind"]] + '">' + c["n"] + '</span>'
                           + '<span class="col">' + ttl(c) + '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></span>',
                           "li--thumb"), "l l--gap"))

block("P21", "Чипы формата", "Формат и длительность вынесены в чипы под названием.",
      rows(lambda i, c: li(numbox(c) + '<span class="col">' + ttl(c)
                           + '<span class="chips"><span class="chip">' + KIND_RU[c["kind"]] + '</span>'
                           '<span class="chip">' + c["d"] + '</span></span></span>', "li--chips"), "l l--card l--div"))

# ================================================================ F. Доступ
def access(i, c):
    locked = c["st"] == "locked" or i >= 2
    right = ('<span class="dur dur--lock">' + LOCK + '</span>') if locked else dur(c)
    return li(numbox(c, "numbox--ghost" if locked else "") + ttl(c, "ttl--dim" if locked else "") + right)


block("P22", "Замки на закрытых", "Первые уроки открыты, дальше замок — видно, за что платишь.",
      rows(access, "l l--card l--div"))

block("P23", "Плашка «бесплатно»", "Открытые уроки помечены явно, замки не нужны.",
      rows(lambda i, c: li(numbox(c) + '<span class="col">' + ttl(c) + '</span>'
                           + ('<span class="free">Бесплатно</span>' if i < 2 else '<span class="dur dur--lock">' + LOCK + '</span>')),
           "l l--card l--div"))

block("P24", "Кнопка на текущем уроке", "У активного урока — настоящая кнопка «Смотреть», остальные строки спокойные.",
      rows(lambda i, c: li(state_mark(c) + ttl(c)
                           + ('<span class="btn">' + PLAYF + 'Смотреть</span>' if c["st"] == "current" else dur(c)),
                           "li--now" if c["st"] == "current" else ""), "l l--card l--div"))

# ================================================================ G. Плотность
block("P25", "Компактный", "Строки 48px: вся программа из 12 уроков помещается без прокрутки.",
      rows(lambda i, c: li('<span class="numbox numbox--sm">' + c["n"] + '</span>' + ttl(c, "ttl--sm") + dur(c)),
           "l l--card l--div l--tight"))

block("P26", "Крупно и с воздухом", "Заголовки 19px, строки высокие — программа читается как содержание книги.",
      rows(lambda i, c: li(numbox(c, "numbox--lg") + '<span class="col">' + ttl(c, "ttl--lg")
                           + '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></span>', "li--air"),
           "l l--rule"))

block("P27", "Две колонки", "На широком экране программа складывается в две колонки и не растягивается в километр.",
      wrap("grid2", "\n".join('      ' + li(numbox(c) + ttl(c) + dur(c), "li--card") for c in L)))

# ================================================================ H. Эксперименты
block("P28", "Цифра фоном", "Номер живёт подложкой карточки — программа выглядит как разворот журнала.",
      rows(lambda i, c: li('<span class="ghostnum">' + c["n"] + '</span>' + '<span class="col">' + ttl(c)
                           + '<span class="sub">' + c["d"] + '</span></span>', "li--card li--ghost"), "l l--gap"))

block("P29", "Пилюли", "Каждый урок — пилюля со скруглением на всю высоту, длительность справа в кружке.",
      rows(lambda i, c: li(numbox(c, "numbox--pill") + ttl(c) + '<span class="pilldur">' + c["d"] + '</span>',
                           "li--pill"), "l l--gap"))

rail = "\n".join(
    '      <div class="rcard"><span class="rcard__i" style="background:' + THUMB[c["kind"]] + '">' + ICON[c["kind"]] + '</span>'
    '<span class="rcard__n">Урок ' + c["n"] + '</span><span class="rcard__t">' + c["t"] + '</span>'
    '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></div>' for c in L)
block("P30", "Лента уроков", "Программа листается вбок карточками — тот же приём, что у курсов на главной.",
      wrap("rail2", rail))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .fam { font-size: 13px; letter-spacing: .08em; text-transform: uppercase;
         color: hsl(var(--muted-foreground)); margin: 12px 0 -8px }

  /* ---------- база списка ---------- */
  .l { display: flex; flex-direction: column }
  .l--card { background: hsl(var(--muted)); border-radius: 16px; padding: 4px 0 }
  .l--div .li + .li { border-top: 1px solid hsl(var(--border) / .7) }
  .l--rule .li + .li { border-top: 1px solid hsl(var(--border) / .7) }
  .l--gap { gap: 10px }
  .l--tight .li { min-height: 48px; padding: 6px 14px }

  .li { display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 10px 14px }
  .li--card { background: hsl(var(--muted)); border-radius: 14px }
  .li--now { background: hsl(var(--primary) / .1); border-radius: 12px }
  .li--air { min-height: 78px }
  .li--chips { align-items: flex-start; padding-top: 12px; padding-bottom: 12px }

  .ttl { flex: 1; min-width: 0; font-size: 16px; font-weight: 500; line-height: 1.25 }
  .ttl--dim { color: hsl(var(--muted-foreground)) }
  .ttl--sm { font-size: 15px }
  .ttl--lg { font-size: 19px }
  .sub { display: block; font-size: 13px; color: hsl(var(--muted-foreground)); margin-top: 3px }
  .col { flex: 1; min-width: 0; display: flex; flex-direction: column }
  .row { display: flex; align-items: center; gap: 12px; width: 100% }

  .numbox { flex: 0 0 auto; width: 42px; height: 42px; border-radius: 12px; background: hsl(var(--background));
            display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500 }
  .numbox--ghost { background: transparent; color: hsl(var(--muted-foreground)); width: 30px }
  .numbox--sm { width: 34px; height: 34px; border-radius: 10px; font-size: 13px }
  .numbox--lg { width: 48px; height: 48px; border-radius: 14px; font-size: 17px }
  .numbox--pill { border-radius: 999px }
  .bignum { flex: 0 0 auto; width: 42px; font-size: 26px; font-weight: 600; line-height: 1;
            color: hsl(var(--foreground) / .18); text-align: center }
  .ghostnum { position: absolute; right: 12px; top: 50%; transform: translateY(-50%); font-size: 46px;
              font-weight: 700; color: hsl(var(--foreground) / .07); line-height: 1 }
  .li--ghost { position: relative; overflow: hidden }
  .dot { flex: 0 0 auto; width: 8px; height: 8px; border-radius: 50%; background: hsl(var(--primary)); margin: 0 11px }

  .dur { flex: 0 0 auto; display: inline-flex; align-items: center; gap: 6px; font-size: 14px;
         color: hsl(var(--muted-foreground)) }
  .dur--lock { color: hsl(var(--muted-foreground) / .8) }
  .pilldur { flex: 0 0 auto; font-size: 13px; color: hsl(var(--muted-foreground));
             background: hsl(var(--background)); border-radius: 999px; padding: 5px 10px }
  .li--pill { background: hsl(var(--muted)); border-radius: 999px; padding: 8px 8px 8px 8px }
  .li--time { align-items: center }
  .time { flex: 0 0 auto; width: 52px; text-align: center; font-size: 22px; font-weight: 600; line-height: 1 }
  .time i { display: block; font-size: 11px; font-weight: 400; font-style: normal;
            color: hsl(var(--muted-foreground)); margin-top: 2px }

  .mark { flex: 0 0 auto; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center;
          justify-content: center; font-size: 14px; background: hsl(var(--background));
          color: hsl(var(--muted-foreground)) }
  .mark--done { background: hsl(152 55% 92%); color: hsl(152 55% 32%) }
  .mark--now { background: hsl(var(--primary)); color: #fff }
  .ring { position: relative; flex: 0 0 auto; width: 34px; height: 34px }
  .ring i { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
            font-style: normal; font-size: 12px; font-weight: 600 }

  .bar { display: block; height: 4px; border-radius: 2px; background: hsl(var(--border)); margin-top: 8px }
  .bar i { display: block; height: 100%; border-radius: 2px; background: hsl(var(--primary)) }
  .here { display: block; font-size: 13px; font-weight: 500; color: hsl(var(--primary)); margin-top: 3px }
  .phead { display: flex; align-items: center; justify-content: space-between; padding: 12px 14px 8px }
  .phead__t { font-size: 14px; color: hsl(var(--muted-foreground)) }
  .phead__p { font-size: 14px; font-weight: 600 }
  .pbar { height: 6px; border-radius: 3px; background: hsl(var(--border)); margin: 0 14px 10px }
  .pbar i { display: block; height: 100%; border-radius: 3px; background: hsl(var(--primary)) }

  /* ---------- таймлайн ---------- */
  .l--tl { position: relative; padding-left: 4px }
  .li--tl { align-items: flex-start; padding: 12px 14px 12px 0; min-height: 0 }
  .tl { position: relative; flex: 0 0 auto; width: 34px; align-self: stretch; display: flex; justify-content: center }
  .tl::before { content: ''; position: absolute; top: -14px; bottom: -14px; width: 2px;
                background: hsl(var(--border)) }
  .tl--dash::before { background: none; border-left: 2px dashed hsl(var(--border)) }
  .li--tl:first-child .tl::before { top: 12px }
  .li--tl:last-child .tl::before { bottom: calc(100% - 12px) }
  .tl i { position: relative; width: 12px; height: 12px; margin-top: 4px; border-radius: 50%;
          background: hsl(var(--background)); box-shadow: 0 0 0 2px hsl(var(--border)) }
  .tl i.tl--on { background: hsl(var(--primary)); box-shadow: 0 0 0 2px hsl(var(--primary)) }

  /* ---------- змейка ---------- */
  .snake { display: flex; flex-direction: column; gap: 14px }
  .snake__i { display: flex; align-items: center; gap: 12px }
  .snake__c { width: 46px; height: 46px; border-radius: 50%; display: flex; align-items: center;
              justify-content: center; font-size: 15px; font-weight: 600; background: hsl(var(--muted));
              color: hsl(var(--muted-foreground)) }
  .snake__c--on { background: hsl(152 55% 92%); color: hsl(152 55% 32%) }
  .snake__c--now { background: hsl(var(--primary)); color: #fff }
  .snake__l { font-size: 15px; font-weight: 500 }

  /* ---------- аккордеон ---------- */
  .acc { display: flex; flex-direction: column; gap: 10px }
  .acc__i { background: hsl(var(--muted)); border-radius: 16px; overflow: hidden }
  .acc--plain .acc__i { background: none; border: 1px solid hsl(var(--border)) }
  .acc__h { display: flex; align-items: center; gap: 12px; padding: 14px }
  .acc__n { width: 30px; height: 30px; border-radius: 9px; background: hsl(var(--background));
            display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600 }
  .acc__c { color: hsl(var(--muted-foreground)) }
  .acc__b { border-top: 1px solid hsl(var(--border) / .7) }
  .acc__b .li + .li { border-top: 1px solid hsl(var(--border) / .7) }

  /* ---------- прочее ---------- */
  .tabs { display: flex; gap: 6px; padding: 10px 12px }
  .tabs__i { font-size: 14px; padding: 7px 14px; border-radius: 999px; color: hsl(var(--muted-foreground)) }
  .tabs__i--on { background: hsl(var(--background)); color: hsl(var(--foreground)); font-weight: 500 }
  .kind { flex: 0 0 auto; width: 38px; height: 38px; border-radius: 11px; background: hsl(var(--background));
          display: flex; align-items: center; justify-content: center; color: hsl(var(--muted-foreground)) }
  .thumb { flex: 0 0 auto; width: 72px; height: 48px; border-radius: 10px; display: flex; align-items: center;
           justify-content: center; font-size: 14px; font-weight: 600; color: hsl(var(--foreground) / .55) }
  .li--thumb { padding: 10px }
  .chips { display: flex; gap: 6px; margin-top: 7px }
  .chip { font-size: 12px; padding: 4px 9px; border-radius: 999px; background: hsl(var(--background));
          color: hsl(var(--muted-foreground)) }
  .free { flex: 0 0 auto; font-size: 12px; font-weight: 500; padding: 5px 10px; border-radius: 999px;
          background: hsl(152 55% 92%); color: hsl(152 55% 30%) }
  .btn { flex: 0 0 auto; display: inline-flex; align-items: center; gap: 6px; font-size: 14px; font-weight: 500;
         padding: 9px 14px; border-radius: 999px; background: hsl(var(--primary)); color: #fff }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px }
  /* в узкой колонке длительность уезжает под заголовок, иначе карточка не помещается */
  .grid2 .li { flex-wrap: wrap; align-items: flex-start; padding: 12px }
  .grid2 .ttl { font-size: 15px }
  .grid2 .dur { width: 100%; margin-top: 8px }
  .rail2 { display: flex; gap: 12px; overflow-x: auto; margin: 0 -16px; padding: 0 16px 4px;
           scrollbar-width: none }
  .rail2::-webkit-scrollbar { display: none }
  .rcard { flex: 0 0 auto; width: 190px; background: hsl(var(--muted)); border-radius: 16px; padding: 12px;
           display: flex; flex-direction: column }
  .rcard__i { width: 100%; height: 84px; border-radius: 12px; display: flex; align-items: center;
              justify-content: center; color: hsl(var(--foreground) / .5); margin-bottom: 10px }
  .rcard__n { font-size: 12px; letter-spacing: .04em; text-transform: uppercase;
              color: hsl(var(--muted-foreground)) }
  .rcard__t { font-size: 15px; font-weight: 500; line-height: 1.25; margin-top: 3px }
</style>
'''

HEAD = ('<title>Программа курса · 30 вариантов</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Программа курса · 30</h1>
    <p class="text-caption-14">Содержание везде одно и то же — четыре урока бесплатного курса. Меняется только то,
      как показан порядок, состояние и формат уроков. Скажи код — поставлю в приложение.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
