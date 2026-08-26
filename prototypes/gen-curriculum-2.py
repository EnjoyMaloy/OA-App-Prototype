# Генератор черновика: 30 вариантов «Программы курса» без прогресса.
# Состояний всего два: урок открыт (бесплатно) или закрыт замком у частично платного курса.
OUT = '/home/user/OA-App-Prototype/prototypes/curriculum-2.html'

# Частично платный курс: первые два урока открыты, остальные под замком
L = [
    dict(n="01", t="Что такое Telegram Gifts", d="6 мин", kind="video", free=True),
    dict(n="02", t="Создаём первый подарок", d="10 мин", kind="video", free=True),
    dict(n="03", t="Коллекции и редкость", d="12 мин", kind="quiz", free=False),
    dict(n="04", t="Монетизация подарков", d="14 мин", kind="text", free=False),
    dict(n="05", t="Продажа на маркетплейсах", d="9 мин", kind="video", free=False),
    dict(n="06", t="Ошибки новичков", d="7 мин", kind="text", free=False),
]
MOD = [("Основы", L[:3]), ("Практика", L[3:])]

PLAY = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linejoin="round"><path d="m6 3 14 9-14 9z"/></svg>')
LOCK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        'stroke-linecap="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>')
LOCKS = ('<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
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


def fam(t):
    BUF.append('  <h2 class="fam">' + t + '</h2>\n')


def wrap(cls, inner):
    return '    <div class="' + cls + '">\n' + inner + '\n    </div>'


def rows(fn, cls="l", items=None):
    src = items if items is not None else L
    return wrap(cls, "\n".join('      ' + fn(i, c) for i, c in enumerate(src)))


def li(inner, cls=""):
    return '<div class="li ' + cls + '">' + inner + '</div>'


def numbox(c, cls=""):
    return '<span class="numbox ' + cls + '">' + c["n"] + '</span>'


def ttl(c, cls=""):
    return '<span class="ttl ' + cls + '">' + c["t"] + '</span>'


def dur(c, icon=PLAY):
    return '<span class="dur">' + icon + c["d"] + '</span>'


def durplain(c):
    return '<span class="dur">' + c["d"] + '</span>'


def lockmark(c):
    return '<span class="dur dur--lock">' + LOCK + '</span>' if not c["free"] else dur(c)


def freetag(c):
    return '<span class="free">Бесплатно</span>' if c["free"] else '<span class="dur dur--lock">' + LOCK + '</span>'


# ============================================================ A. Раскладка
fam("A. Раскладка и типографика — без состояний")

block("R1", "Ровный список", "Номер, название, длительность. Ничего лишнего — базовая строка.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + durplain(c)), "l l--card l--div"))

block("R2", "Номер над названием", "Номер уходит в надстрочную подпись, название начинается от левого края.",
      rows(lambda i, c: li('<span class="col"><span class="over">Урок ' + c["n"] + '</span>' + ttl(c) + '</span>'
                           + durplain(c), "li--air"), "l l--rule"))

block("R3", "Формат в подписи", "Под названием строка «Видео · 6 мин» — тип урока виден без иконок.",
      rows(lambda i, c: li(numbox(c) + '<span class="col">' + ttl(c) + '<span class="sub">' + KIND_RU[c["kind"]]
                           + ' · ' + c["d"] + '</span></span>', "li--air"), "l l--card l--div"))

block("R4", "Колонка времени справа", "Длительности выровнены в колонку — программу можно просканировать по времени.",
      rows(lambda i, c: li(numbox(c, "numbox--ghost") + ttl(c) + '<span class="tnum">' + c["d"].replace(" мин", "")
                           + '<i>мин</i></span>'), "l l--rule"))

block("R5", "Оглавление книги", "Название и время связаны точечной выноской, как в содержании книги.",
      rows(lambda i, c: li('<span class="lead"><b>' + c["n"] + '</b><span class="lead__t">' + c["t"]
                           + '</span><span class="lead__d"></span><span class="lead__v">' + c["d"] + '</span></span>',
                           "li--lead"), "l"))

block("R6", "Без номеров", "Только названия и время: программа читается как список тем, а не как нумерованный план.",
      rows(lambda i, c: li(ttl(c) + durplain(c)), "l l--rule"))

block("R7", "«Урок 1» словами", "Номер подписан словом — понятнее для новичка, чем голая цифра.",
      rows(lambda i, c: li('<span class="col"><span class="ttl">' + c["t"] + '</span>'
                           '<span class="sub">Урок ' + str(i + 1) + ' · ' + c["d"] + '</span></span>', "li--air"),
           "l l--card l--div"))

block("R8", "Крупные заголовки", "18px и много воздуха: программа выглядит как оглавление лонгрида.",
      rows(lambda i, c: li('<span class="col">' + ttl(c, "ttl--lg") + '<span class="sub">' + c["d"] + '</span></span>'
                           + '<span class="numbox numbox--ghost">' + c["n"] + '</span>', "li--air"), "l l--rule"))

block("R9", "Иконка формата", "Слева иконка видео, конспекта или квиза — строки перестают быть одинаковыми.",
      rows(lambda i, c: li('<span class="kind">' + ICON[c["kind"]] + '</span>' + ttl(c) + durplain(c)),
           "l l--card l--div"))

block("R10", "Миниатюра урока", "Цветное превью слева: страница выглядит как плейлист.",
      rows(lambda i, c: li('<span class="thumb" style="background:' + THUMB[c["kind"]] + '">' + c["n"] + '</span>'
                           + '<span class="col">' + ttl(c) + '<span class="sub">' + KIND_RU[c["kind"]] + ' · '
                           + c["d"] + '</span></span>', "li--thumb"), "l l--gap"))

# ============================================================ B. Бесплатно и замок
fam("B. Частично платный курс: что открыто, что под замком")

block("R11", "Замок вместо времени", "У закрытых уроков справа замок, у открытых — длительность.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + lockmark(c)), "l l--card l--div"))

block("R12", "Плашка «Бесплатно»", "Явно помечено то, что можно посмотреть сразу.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + freetag(c)), "l l--card l--div"))

block("R13", "Приглушённые закрытые", "Закрытые уроки тише по контрасту — открытые сами притягивают взгляд.",
      rows(lambda i, c: li(numbox(c, "" if c["free"] else "numbox--ghost") + ttl(c, "" if c["free"] else "ttl--dim")
                           + lockmark(c), "" if c["free"] else "li--dim"), "l l--card l--div"))

block("R14", "Две группы", "Программа делится на «Открыто сейчас» и «После покупки» — граница платного очевидна.",
      wrap("l l--card l--div",
           '      <div class="ghead">Открыто сейчас</div>\n'
           + "\n".join('      ' + li(numbox(c) + ttl(c) + durplain(c)) for c in L if c["free"]) + '\n'
           + '      <div class="ghead ghead--lock">' + LOCKS + 'После покупки</div>\n'
           + "\n".join('      ' + li(numbox(c, "numbox--ghost") + ttl(c, "ttl--dim") + durplain(c))
                       for c in L if not c["free"])))

block("R15", "Замок в номере", "Вместо цифры у закрытых уроков — замок в той же плашке, ряд не сбивается.",
      rows(lambda i, c: li(numbox(c) if c["free"] else '<span class="numbox numbox--lock">' + LOCK + '</span>'
                           + '', "") if False else li(
          (numbox(c) if c["free"] else '<span class="numbox numbox--lock">' + LOCK + '</span>') + ttl(c) + durplain(c)),
          "l l--card l--div"))

block("R16", "Кромка у бесплатных", "Зелёная полоска слева отмечает открытые уроки — тише, чем плашка.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + durplain(c), "li--edge" if c["free"] else ""), "l l--card l--div"))

block("R17", "Пунктир у закрытых", "Закрытые уроки обведены пунктиром: видно, что содержимое ещё не ваше.",
      rows(lambda i, c: li(numbox(c) + ttl(c) + (durplain(c) if c["free"] else '<span class="dur dur--lock">' + LOCK + '</span>'),
                           "li--card" if c["free"] else "li--card li--dash"), "l l--gap"))

block("R18", "Бейдж «Превью»", "Открытые уроки помечены как превью курса — честная формулировка для платного курса.",
      rows(lambda i, c: li(numbox(c) + '<span class="col">' + ttl(c)
                           + ('<span class="prev">Превью</span>' if c["free"] else '') + '</span>'
                           + lockmark(c), "li--air"), "l l--card l--div"))

block("R19", "Шторка на закрытых", "Названия закрытых уроков размыты, поверх — кнопка покупки.",
      wrap("l l--card l--div veil",
           "\n".join('      ' + li(numbox(c) + ttl(c) + durplain(c)) for c in L if c["free"])
           + '\n      <div class="veil__w">\n'
           + "\n".join('        ' + li(numbox(c) + ttl(c) + durplain(c)) for c in L if not c["free"])
           + '\n        <div class="veil__b"><span class="btn">' + LOCKS + 'Открыть все 6 уроков</span></div>\n      </div>'))

block("R20", "Счётчик в шапке", "Строка над списком говорит, сколько уроков открыто и сколько ждёт покупки.",
      wrap("l l--card l--div",
           '      <div class="phead"><span>2 урока открыты</span><span class="phead__l">' + LOCKS
           + '4 после покупки</span></div>\n'
           + "\n".join('      ' + li(numbox(c) + ttl(c) + lockmark(c)) for c in L)))

# ============================================================ C. Группировка
fam("C. Модули, сетки и плотность")

def acc(cls="acc", opened=0):
    out = []
    for mi, (name, items) in enumerate(MOD):
        op = mi == opened
        mins = sum(int(c["d"].split()[0]) for c in items)
        body = ('<div class="acc__b">' + "".join(li(numbox(c) + ttl(c) + lockmark(c)) for c in items) + '</div>') if op else ''
        out.append('      <div class="acc__i"><div class="acc__h">'
                   '<span class="acc__n">' + str(mi + 1) + '</span>'
                   '<span class="col"><span class="ttl">' + name + '</span>'
                   '<span class="sub">' + str(len(items)) + ' урока · ' + str(mins) + ' мин</span></span>'
                   '<span class="acc__c">' + (CHEVD if op else CHEV) + '</span></div>' + body + '</div>')
    return wrap(cls, "\n".join(out))


block("R21", "Аккордеон модулей", "Модули сворачиваются: программа из двадцати уроков помещается на экран.",
      acc())

block("R22", "Заголовки-разделители", "Без аккордеона: модуль — просто подзаголовок над своей группой уроков.",
      wrap("l l--card l--div",
           "\n".join('      <div class="ghead">' + name + ' · ' + str(len(items)) + ' урока</div>\n'
                     + "\n".join('      ' + li(numbox(c) + ttl(c) + lockmark(c)) for c in items)
                     for name, items in MOD)))

block("R23", "Нумерация 1.1, 1.2", "Номер показывает модуль и место в нём — удобно для больших программ.",
      wrap("l l--rule",
           "\n".join("\n".join('      ' + li('<span class="numdot">' + str(mi + 1) + '.' + str(li_ + 1) + '</span>'
                                             + ttl(c) + lockmark(c)) for li_, c in enumerate(items))
                     for mi, (name, items) in enumerate(MOD))))

block("R24", "Таймлайн", "Вертикальная нить связывает уроки в маршрут, замок висит на закрытых.",
      rows(lambda i, c: li('<span class="tl"><i></i></span><span class="col">' + ttl(c)
                           + '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></span>'
                           + ('' if c["free"] else '<span class="dur dur--lock">' + LOCK + '</span>'), "li--tl"),
           "l l--tl"))

block("R25", "Сетка 2×", "Короткие названия ложатся в две колонки — программа занимает вдвое меньше высоты.",
      wrap("grid2", "\n".join('      ' + li('<span class="col">' + '<span class="over">Урок ' + c["n"] + '</span>'
                                            + ttl(c) + '<span class="sub">' + c["d"] + '</span></span>'
                                            + ('' if c["free"] else '<span class="dur dur--lock">' + LOCK + '</span>'),
                                            "li--card li--grid") for c in L)))

block("R26", "Лента вбок", "Уроки листаются карточками, как курсы на главной.",
      wrap("rail2", "\n".join(
          '      <div class="rcard"><span class="rcard__i" style="background:' + THUMB[c["kind"]] + '">'
          + (ICON[c["kind"]] if c["free"] else LOCK) + '</span>'
          '<span class="rcard__n">Урок ' + c["n"] + '</span><span class="rcard__t">' + c["t"] + '</span>'
          '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></div>' for c in L)))

block("R27", "Компактный", "Строки 44px: двадцать уроков видно без бесконечной прокрутки.",
      rows(lambda i, c: li('<span class="numbox numbox--sm">' + c["n"] + '</span>' + ttl(c, "ttl--sm")
                           + (durplain(c) if c["free"] else '<span class="dur dur--lock">' + LOCKS + '</span>'),
                           "li--tight"), "l l--card l--div"))

block("R28", "Только текст", "Ни плашек, ни подложек — номер, название и время одной строкой.",
      rows(lambda i, c: li('<span class="plainnum">' + c["n"] + '</span>' + ttl(c)
                           + (durplain(c) if c["free"] else '<span class="dur dur--lock">' + LOCKS + '</span>'),
                           "li--plain"), "l"))

block("R29", "Таблица", "Три колонки: формат, название, время — самый информационный вариант.",
      rows(lambda i, c: li('<span class="kind kind--sm">' + ICON[c["kind"]] + '</span>' + ttl(c, "ttl--sm")
                           + '<span class="tcell">' + (c["d"] if c["free"] else LOCKS) + '</span>', "li--tight"),
           "l l--card l--div"))

block("R30", "Цифра фоном", "Крупный номер живёт подложкой карточки, замок — в правом верхнем углу.",
      rows(lambda i, c: li('<span class="ghostnum">' + c["n"] + '</span><span class="col">' + ttl(c)
                           + '<span class="sub">' + KIND_RU[c["kind"]] + ' · ' + c["d"] + '</span></span>'
                           + ('' if c["free"] else '<span class="dur dur--lock">' + LOCK + '</span>'),
                           "li--card li--ghost"), "l l--gap"))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .fam { font-size: 12px; letter-spacing: .08em; text-transform: uppercase;
         color: hsl(var(--muted-foreground)); margin: 14px 0 -10px }

  .l { display: flex; flex-direction: column }
  .l--card { background: hsl(var(--muted)); border-radius: 16px; padding: 4px 0 }
  .l--div .li + .li, .l--rule .li + .li { border-top: 1px solid hsl(var(--border) / .7) }
  .l--gap { gap: 10px }

  .li { display: flex; align-items: center; gap: 12px; min-height: 62px; padding: 10px 14px }
  .li--card { background: hsl(var(--muted)); border-radius: 14px }
  .li--air { min-height: 72px }
  .li--tight { min-height: 44px; padding: 6px 14px }
  .li--plain { min-height: 44px; padding: 8px 0 }
  .li--dim { opacity: .62 }
  .li--dash { background: none; border: 1px dashed hsl(var(--border)) }
  .li--edge { position: relative }
  .li--edge::before { content: ''; position: absolute; left: 0; top: 10px; bottom: 10px; width: 3px;
                      border-radius: 0 3px 3px 0; background: hsl(152 55% 45%) }
  .li--lead { padding: 9px 0; min-height: 0 }
  .li--grid { align-items: flex-start; padding: 12px }
  .li--ghost { position: relative; overflow: hidden }

  .ttl { flex: 1; min-width: 0; font-size: 16px; font-weight: 500; line-height: 1.25 }
  .ttl--dim { color: hsl(var(--muted-foreground)) }
  .ttl--sm { font-size: 15px }
  .ttl--lg { font-size: 18px }
  .col { flex: 1; min-width: 0; display: flex; flex-direction: column }
  .sub { font-size: 13px; color: hsl(var(--muted-foreground)); margin-top: 3px }
  .over { font-size: 12px; letter-spacing: .04em; text-transform: uppercase;
          color: hsl(var(--muted-foreground)); margin-bottom: 3px }

  .numbox { flex: 0 0 auto; width: 42px; height: 42px; border-radius: 12px; background: hsl(var(--background));
            display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: 500 }
  .numbox--ghost { background: transparent; color: hsl(var(--muted-foreground)); width: 28px }
  .numbox--sm { width: 32px; height: 32px; border-radius: 9px; font-size: 13px }
  .numbox--lock { color: hsl(var(--muted-foreground)) }
  .numdot { flex: 0 0 auto; width: 34px; font-size: 14px; font-weight: 500;
            color: hsl(var(--muted-foreground)) }
  .plainnum { flex: 0 0 auto; width: 26px; font-size: 15px; color: hsl(var(--muted-foreground)) }
  .ghostnum { position: absolute; right: 14px; bottom: -8px; font-size: 52px; font-weight: 700;
              color: hsl(var(--foreground) / .06); line-height: 1 }

  .dur { flex: 0 0 auto; display: inline-flex; align-items: center; gap: 6px; font-size: 14px;
         color: hsl(var(--muted-foreground)) }
  .dur--lock { color: hsl(var(--muted-foreground) / .75) }
  .tnum { flex: 0 0 auto; width: 46px; text-align: right; font-size: 18px; font-weight: 600 }
  .tnum i { font-style: normal; font-size: 11px; font-weight: 400; color: hsl(var(--muted-foreground));
            margin-left: 3px }
  .tcell { flex: 0 0 auto; width: 58px; text-align: right; font-size: 14px;
           color: hsl(var(--muted-foreground)) }

  .free { flex: 0 0 auto; font-size: 12px; font-weight: 500; padding: 5px 10px; border-radius: 999px;
          background: hsl(152 55% 92%); color: hsl(152 55% 30%) }
  .prev { display: inline-flex; align-self: flex-start; font-size: 12px; font-weight: 500; padding: 3px 8px;
          border-radius: 999px; background: hsl(var(--background)); color: hsl(var(--muted-foreground));
          margin-top: 5px }
  .btn { display: inline-flex; align-items: center; gap: 8px; font-size: 15px; font-weight: 500;
         padding: 13px 22px; border-radius: 999px; background: hsl(var(--foreground));
         color: hsl(var(--background)) }

  .ghead { padding: 12px 14px 6px; font-size: 13px; letter-spacing: .04em; text-transform: uppercase;
           color: hsl(var(--muted-foreground)); display: flex; align-items: center; gap: 6px }
  .ghead--lock { border-top: 1px solid hsl(var(--border) / .7); margin-top: 4px; padding-top: 14px }
  .phead { display: flex; align-items: center; justify-content: space-between; padding: 12px 14px 10px;
           font-size: 13px; color: hsl(var(--muted-foreground));
           border-bottom: 1px solid hsl(var(--border) / .7) }
  .phead__l { display: inline-flex; align-items: center; gap: 6px }

  /* оглавление с выноской */
  .lead { display: flex; align-items: baseline; gap: 10px; width: 100%; font-size: 16px }
  .lead b { font-weight: 500; color: hsl(var(--muted-foreground)); font-size: 14px }
  .lead__t { font-weight: 500 }
  .lead__d { flex: 1; border-bottom: 1.5px dotted hsl(var(--border)); transform: translateY(-4px) }
  .lead__v { font-size: 14px; color: hsl(var(--muted-foreground)) }

  /* шторка */
  .veil__w { position: relative }
  .veil__w .li { filter: blur(3px); opacity: .5 }
  .veil__w .li + .li { border-top: 1px solid hsl(var(--border) / .7) }
  .veil__b { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center }

  /* таймлайн */
  .l--tl { padding-left: 2px }
  .li--tl { align-items: flex-start; padding: 12px 14px 12px 0; min-height: 0 }
  .tl { position: relative; flex: 0 0 auto; width: 32px; align-self: stretch; display: flex; justify-content: center }
  .tl::before { content: ''; position: absolute; top: -14px; bottom: -14px; width: 2px; background: hsl(var(--border)) }
  .li--tl:first-child .tl::before { top: 10px }
  .li--tl:last-child .tl::before { bottom: calc(100% - 10px) }
  .tl i { position: relative; width: 10px; height: 10px; margin-top: 5px; border-radius: 50%;
          background: hsl(var(--background)); box-shadow: 0 0 0 2px hsl(var(--border)) }

  /* аккордеон */
  .acc { display: flex; flex-direction: column; gap: 10px }
  .acc__i { background: hsl(var(--muted)); border-radius: 16px; overflow: hidden }
  .acc__h { display: flex; align-items: center; gap: 12px; padding: 14px }
  .acc__n { width: 30px; height: 30px; border-radius: 9px; background: hsl(var(--background));
            display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600 }
  .acc__c { color: hsl(var(--muted-foreground)) }
  .acc__b { border-top: 1px solid hsl(var(--border) / .7) }
  .acc__b .li + .li { border-top: 1px solid hsl(var(--border) / .7) }

  /* прочее */
  .kind { flex: 0 0 auto; width: 38px; height: 38px; border-radius: 11px; background: hsl(var(--background));
          display: flex; align-items: center; justify-content: center; color: hsl(var(--muted-foreground)) }
  .kind--sm { width: 30px; height: 30px; border-radius: 9px; background: none }
  .thumb { flex: 0 0 auto; width: 72px; height: 48px; border-radius: 10px; display: flex; align-items: center;
           justify-content: center; font-size: 14px; font-weight: 600; color: hsl(var(--foreground) / .55) }
  .li--thumb { padding: 10px }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px }
  .grid2 .ttl { font-size: 15px }
  .rail2 { display: flex; gap: 12px; overflow-x: auto; margin: 0 -16px; padding: 0 16px 4px; scrollbar-width: none }
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

HEAD = ('<title>Программа курса · вторая серия</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Программа курса · ещё 30</h1>
    <p class="text-caption-14">Без прогресса: уроки не «пройдены» и не «текущие». Состояний два — урок открыт
      или закрыт замком у частично платного курса. Курс в примере платный: первые два урока открыты, четыре под замком.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
