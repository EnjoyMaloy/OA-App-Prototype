# Генератор: 20 вариантов текста в блоке «Продолжить обучение»
# Приём из приложений Apple — одна строка, но разная плотность/прозрачность слов.
import math
OUT = '/home/user/OA-App-Prototype/prototypes/continue-text.html'

TITLE = "Стратегии торговли на вторичном рынке"
SHORT = "Стратегии торговли"
PROG, LEFT, DONE, TOTAL, MIN = 61, 2, 5, 8, 12

R, SW, SIZE = 23, 8, 56
CIRC = 2 * math.pi * R
def ring():
    off = CIRC * (1 - PROG / 100)
    return (f'<span class="ring"><svg width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
            f'<defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#FF5C1A"/><stop offset="1" stop-color="#FFB088"/></linearGradient></defs>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="rgba(32,32,32,.10)" stroke-width="{SW}"/>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="url(#ga)" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-dasharray="{CIRC:.1f}" stroke-dashoffset="{off:.1f}"/></svg>'
            f'<span class="pct">{PROG}%</span></span>')

BUF = []
def block(code, title, cap, body):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
    <div class="cont">
      {ring()}
      <span class="body">{body}</span>
      <span class="chev">›</span>
    </div>
  </section>
''')

# плотности: s — плотный, m — средний, l — лёгкий, x — совсем тихий
def s(t, cls=""):  return f'<span class="s {cls}">{t}</span>'
def m(t, cls=""):  return f'<span class="m {cls}">{t}</span>'
def l(t, cls=""):  return f'<span class="l {cls}">{t}</span>'
def x(t, cls=""):  return f'<span class="x {cls}">{t}</span>'
def line(*parts, cls=""): return f'<span class="ln {cls}">' + " ".join(parts) + '</span>'

block("T1", "Как сейчас", "Заголовок плотный, подпись серая — для сравнения.",
 line(s(TITLE), cls="t17") + line(l("Осталось 2 урока"), cls="t13"))

block("T2", "Цифра плотная", "В подписи выделен только счёт — приём «10 Days Journaled».",
 line(s(TITLE), cls="t17") + line(l("Осталось"), s(f"{LEFT} урока"), cls="t14"))

block("T3", "Урок 5 из 8", "Служебные слова уходят в прозрачность, цифры остаются.",
 line(s(TITLE), cls="t17") + line(l("Урок"), s(str(DONE)), l("из"), s(str(TOTAL)), cls="t14"))

block("T4", "Инверсия", "Плотное — то, что осталось; «Осталось» тихо.",
 line(s(TITLE), cls="t17") + line(x("Осталось"), s(f"{LEFT} урока"), cls="t15"))

block("T5", "Заголовок в две плотности", "Первое слово держит, хвост уходит в полутон.",
 line(s("Стратегии"), m("торговли на вторичном рынке"), cls="t17") + line(l("Осталось 2 урока"), cls="t13"))

block("T6", "Общее смягчение", "Заголовок 85%, подпись 40% — вся карточка тише.",
 line(m(TITLE), cls="t17") + line(x("Осталось 2 урока"), cls="t13"))

block("T7", "Как «Entry This Year»", "Крупное число, под ним слово плотное и слово прозрачное.",
 line(s(str(LEFT), "big"), cls="big-row") + line(s("урока"), x("осталось"), cls="t15") + line(x(SHORT), cls="t13"))

block("T8", "Категория сверху", "Мелкая тихая рубрика над плотным заголовком.",
 line(x("ТРЕЙДИНГ", "caps"), cls="t11") + line(s(TITLE), cls="t17") + line(l("Осталось 2 урока"), cls="t13"))

block("T9", "Через точку", "Метрики одной строкой, прозрачность держит иерархию.",
 line(s(TITLE), cls="t17") + line(s(f"{PROG}%"), x("·"), l("осталось"), s("2 урока"), cls="t14"))

block("T10", "Цифры и единицы", "Числа плотные, единицы измерения прозрачные.",
 line(s(TITLE), cls="t17") + line(s(str(LEFT)), l("урока"), x("·"), s(str(MIN)), l("мин"), cls="t14"))

block("T11", "Три уровня", "Один размер, три плотности: 100 / 60 / 35.",
 line(s("Стратегии торговли"), cls="t16") + line(m("на вторичном рынке"), cls="t16") + line(x("осталось 2 урока"), cls="t16"))

block("T12", "Затухание к концу", "Строка гаснет слева направо.",
 line(s(TITLE), cls="t17") + line(m("Осталось"), l("2 урока"), x("· 12 минут"), cls="t14"))

block("T13", "Вес плюс прозрачность", "Полужирное плотное и обычное полупрозрачное рядом.",
 line(s("Урок 5", "bold"), l("из 8 — вторичный рынок"), cls="t16") + line(x("12 минут до конца"), cls="t13"))

block("T14", "Глагол тихо", "«Продолжить» уходит в фон, название держит.",
 line(x("Продолжить"), s(SHORT), cls="t17") + line(l("Урок 5 из 8"), cls="t14"))

block("T15", "Две подписи", "Плотная строка прогресса и тихая строка времени.",
 line(s(TITLE), cls="t17") + line(m("Урок 5 из 8"), cls="t14") + line(x("осталось 12 минут"), cls="t13"))

block("T16", "Процент словами", "Число плотное, «пройдено» прозрачное.",
 line(s(TITLE), cls="t17") + line(s(f"{PROG}%"), l("пройдено"), cls="t14"))

block("T17", "Одна строка и контекст", "Заголовок в одну строку, под ним тихий контекст.",
 line(s(TITLE, "one"), cls="t17") + line(x("Трейдинг · 8 уроков · 3 часа"), cls="t13"))

block("T18", "Крупное число", "Приём Apple: цифра большая, пояснение мелкое и тихое.",
 line(s(str(LEFT), "big2"), l("урока", "aside"), cls="big-row") + line(x(TITLE, "one"), cls="t13"))

block("T19", "Цветная прозрачность", "Полутон не серый, а оранжевый — в тон дуге.",
 line(s(TITLE), cls="t17") + line('<span class="warm">Осталось</span>', s("2 урока"), cls="t14"))

block("T20", "Метка и хвост", "Плотная метка урока и прозрачный хвост со временем.",
 line(s(TITLE), cls="t17") + line(s("Урок 5 из 8"), x("· 12 мин"), cls="t14"))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .cont { display: flex; align-items: center; gap: 14px; width: 100%; padding: 16px; border-radius: 16px;
    background: linear-gradient(105deg, #FFE7DA 0%, #FFEDE3 55%, #FFFFFF 100%); cursor: pointer }
  .ring { position: relative; flex: 0 0 auto; width: 56px; height: 56px }
  .ring svg { transform: rotate(-90deg) }
  .pct { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 700; background-image: linear-gradient(120deg,#FF5C1A,#FFB088);
    -webkit-background-clip: text; background-clip: text; color: transparent }
  .body { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px }
  .chev { flex: 0 0 auto; font-size: 22px; color: rgba(32,32,32,.35); line-height: 1 }

  .ln { display: block; line-height: 1.25 }
  .t17 { font-size: 17px } .t16 { font-size: 16px } .t15 { font-size: 15px }
  .t14 { font-size: 14px } .t13 { font-size: 13px } .t11 { font-size: 11px }
  .big-row { display: flex; align-items: baseline; gap: 8px }

  /* четыре плотности одного цвета — приём Apple */
  .s { color: rgba(32,32,32,1);   font-weight: 500 }
  .m { color: rgba(32,32,32,.62); font-weight: 500 }
  .l { color: rgba(32,32,32,.45); font-weight: 400 }
  .x { color: rgba(32,32,32,.32); font-weight: 400 }
  .warm { color: rgba(255,92,26,.5); font-weight: 500; font-size: inherit }

  .bold { font-weight: 700 }
  .big { font-size: 34px; font-weight: 700; line-height: 1 }
  .big2 { font-size: 30px; font-weight: 700; line-height: 1 }
  .aside { font-size: 15px }
  .caps { letter-spacing: .1em; font-weight: 600 }
  .one { display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden }
</style>
'''

HEAD = '''<title>Продолжить обучение · текст</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Текст в блоке · 20</h1>
    <p class="text-caption-14">Карточка, кольцо и процент везде одинаковые — меняется только текст: слова разной плотности в одной строке, как в приложениях Apple.</p>
  </div>

'''
TAIL = '''
  <p class="note">Плотности: 100% — то, что важно; 62% — контекст; 45% — служебное; 32% — совсем тихое. Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
