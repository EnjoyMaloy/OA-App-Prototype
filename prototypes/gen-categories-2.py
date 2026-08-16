# Генератор черновика: ещё 100 вариантов блока «Категории» (семейства E–N)
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad')

OUT = '/home/user/OA-App-Prototype/prototypes/categories-2.html'

P = {
 "ai": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
 "crypto": '<path d="M11.767 19.089c4.924.868 6.14-6.025 1.216-6.894m-1.216 6.894L5.86 18.047m5.908 1.042-.347 1.97m1.563-8.864c4.924.869 6.14-6.025 1.215-6.893m-1.215 6.893-3.94-.694m5.155-6.2L8.29 4.26m5.908 1.042.348-1.97M7.48 20.364l3.126-17.727"/>',
 "security": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "trading": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "invest": '<path d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z"/><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>',
 "web3": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
 "tools": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}

def ico(k, s=48, sw=2, color="currentColor", extra=""):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{extra}>{P[k]}</svg>')

def ico_grad(k, uid, a, b, s=48, sw=2):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="url(#{uid})" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs>{P[k]}</svg>')

#  id, подпись в две строки, в строку, эмодзи, курсов, время
CATS = [
 ("ai",       "AI-навыки",      "AI-навыки",     "✨", 5, "4 ч"),
 ("crypto",   "Основы\nкрипты", "Основы крипты", "🪙", 2, "3 ч"),
 ("security", "Безопасность",   "Безопасность",  "🛡️", 1, "1 ч"),
 ("trading",  "Трейдинг",       "Трейдинг",      "📈", 3, "6 ч"),
 ("invest",   "Инвестиции",     "Инвестиции",    "💰", 4, "5 ч"),
 ("web3",     "Web3 и DeFi",    "Web3 и DeFi",   "🌐", 4, "7 ч"),
 ("tools",    "Инструменты",    "Инструменты",   "🔧", 1, "2 ч"),
]
ICOVAR = {"ai": "--cat-ai-icon", "trading": "--cat-trading-icon"}

def c(k):  return f"hsl(var(--cat-{k}))"
def ci(k): return f"hsl(var({ICOVAR.get(k, '--cat-' + k)}))"
def bg(k): return f"hsl(var(--cat-{k}-bg))"
def mix(k, pct, other="white"): return f"color-mix(in srgb, hsl(var(--cat-{k})) {pct}%, {other})"

PAIRS = [("#A66CFF", "#FF8645"), ("#FF96C8", "#FFDD31"), ("#88C5FD", "#CCEF40")]
def pair(i): return PAIRS[i % 3]

import math
def svg_ring(k, pct, s=46, r=18, sw=5):
    C = 2 * math.pi * r
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" style="transform:rotate(-90deg)">'
            f'<circle cx="{s/2}" cy="{s/2}" r="{r}" fill="none" stroke="{mix(k,22)}" stroke-width="{sw}"/>'
            f'<circle cx="{s/2}" cy="{s/2}" r="{r}" fill="none" stroke="{c(k)}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-dasharray="{C:.1f}" stroke-dashoffset="{C*(1-pct/100):.1f}"/></svg>')

def newbadge(k, on):
    return f'<span class="new" style="background:{c(k)}">Новое</span>' if on else ""
def lockbadge(on):
    return '<span class="lock">🔒</span>' if on else ""
def checkbadge(k, on):
    return f'<span class="chk" style="background:{c(k)}">✓</span>' if on else ""
def avatars(n):
    dots = "".join(f'<i style="background:{PAIRS[j%3][0]}"></i>' for j in range(3))
    return f'<span class="avs">{dots}<b>+{n*17}</b></span>'
def previews(i):
    return '<span class="prev">' + "".join(f'<i style="background:{PAIRS[(i+j)%3][j%2]}"></i>' for j in range(3)) + '</span>'

def firstbold(l):
    if "\n" in l:
        a, b = l.split("\n")
        return f"<b>{a}</b>\n{b}"
    parts = l.split(" ")
    return f"<b>{parts[0]}</b> " + " ".join(parts[1:]) if len(parts) > 1 else f"<b>{l}</b>"

BUF = []
def fam(t): BUF.append(f'  <h2 class="fam">{t}</h2>\n')
def block(code, title, cap, body):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
{body}
  </section>
''')
def rail(fn, cls="rail"):
    return f'    <div class="{cls}">\n' + "\n".join("      " + fn(i, *cat) for i, cat in enumerate(CATS)) + "\n    </div>"
def some(fn, n, cls="rail", extra=""):
    return (f'    <div class="{cls}">\n'
            + "\n".join("      " + fn(i, *cat) for i, cat in enumerate(CATS[:n]))
            + ("\n      " + extra if extra else "") + "\n    </div>")

T = 'class="t" style="--bg:{};--c:{}"'

# =====================================================================
fam("E. Форма плитки")
block("E1", "Мягкий квадрат r8", "Меньше скругления — интерфейс строже.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};border-radius:8px">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E2", "Сквиркл r28", "Крупное скругление — мягче и «эппловее».",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};border-radius:28px">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E3", "Асимметричные углы", "Два угла круглые, два острые — плитка получает характер.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};border-radius:28px 10px 28px 10px">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E4", "Вертикальная 3:4", "Узкая и высокая — в ленту влезает больше категорий.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};width:120px;height:160px">{ico(k,40)}<span class="t__l">{l}</span></button>'))
block("E5", "Квадрат 1:1", "Крупная плитка, иконка дышит.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};width:150px;height:150px">{ico(k,52)}<span class="t__l">{l}</span></button>'))
block("E6", "С вырезом", "Круглая выемка сверху — как отрывной билет.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel notch" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E7", "Наклонённая иконка", "Иконка чуть повёрнута — лента живее.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="tilt">{ico(k,46)}</span><span class="t__l">{l}</span></button>'))
block("E8", "Двойная обводка", "Контур с отступом — приём из брендбука.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t dbl" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,35)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E9", "Срезанный угол", "Скос вместо скругления справа-снизу.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t cut" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("E10", "Карточка в карточке", "Иконка сидит на белой подложке внутри плитки.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};padding:10px"><span class="inner" style="color:{ci(k)}">{ico(k,34)}</span><span class="t__l" style="padding:0 2px 2px">{l}</span></button>'))

# =====================================================================
fam("F. Типографика подписи")
block("F1", "Капслок мелким", "Подпись как рубрика — строго и по-редакторски.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l caps">{l1}</span></button>'))
block("F2", "Крупная жирная", "22px bold — подпись главнее иконки.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};width:158px">{ico(k,38)}<span class="t__l big">{l}</span></button>'))
block("F3", "Первое слово жирным", "Иерархия внутри самой подписи.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{firstbold(l)}</span></button>'))
block("F4", "С номером", "Нумерация задаёт порядок изучения.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="num">{i+1:02d}</span>{ico(k,40)}<span class="t__l">{l}</span></button>'))
block("F5", "Со счётчиком", "Вернули число курсов, но нейтральным серым.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,42)}<span><span class="t__l">{l}</span><span class="cnt">{n} курс{"" if n==1 else "а" if n<5 else "ов"}</span></span></button>'))
block("F6", "Вертикальная подпись", "Текст вдоль левого края — витринный приём.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="tv" style="background:{bg(k)};color:{c(k)}"><span class="vert">{l1}</span>{ico(k,40)}</button>'))
block("F7", "Разрежённый трекинг", "Широкие межбуквенные — подпись читается спокойнее.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l track">{l}</span></button>'))
block("F8", "С подчёркиванием", "Цветная линия под подписью — маркер раздела.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,42)}<span class="t__l und" style="border-color:{mix(k,55)}">{l}</span></button>'))
block("F9", "Подпись поверх иконки", "Текст ложится на просвечивающую иконку.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel over" style="--bg:{bg(k)};--c:{c(k)}"><span class="wmc" style="color:{ci(k)}">{ico(k,100,1.5)}</span><span class="t__l ovl">{l}</span></button>'))
block("F10", "Инициал знаком", "Крупная буква вместо иконки — типографская подача.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="init">{l1[0]}</span><span class="t__l" style="font-size:15px">{l}</span></button>'))

# =====================================================================
fam("G. Цвет и контраст")
block("G1", "Насыщенная заливка", "Цвет категории на всю плитку, контент белый.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{c(k)};--c:#fff">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G2", "Заливка 55%", "Средняя насыщенность — ярче пастели, мягче полного цвета.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{mix(k,55)};--c:#202020">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G3", "Монохром бренда", "Всё в OA Purple — категории не спорят с обложками курсов.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:#EDE4FF;--c:#7B2EFF">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G4", "Warm Neutral", "Тёплый нейтральный фон, цвет живёт только в иконке.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:#FFFCF5;--c:#202020;border:1px solid rgba(32,32,32,.07)">{ico(k,46,2,ci(k))}<span class="t__l">{l}</span></button>'))
block("G5", "Графит", "Тёмные плитки, цветные иконки, белая подпись.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:#202020;--c:#fff">{ico(k,46,2,c(k))}<span class="t__l">{l}</span></button>'))
block("G6", "Через одну", "Чередование цветных и белых плиток задаёт ритм.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t{"" if i%2 else " t--shadow"}" style="--bg:{"#fff" if i%2==0 else bg(k)};--c:{c(k)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G7", "Дуотон", "Две плотности одного цвета по диагонали.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:linear-gradient(120deg,{mix(k,38)} 0 50%,{bg(k)} 50% 100%);--c:{c(k)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G8", "Цветная тень", "Плитка отбрасывает тень своего же цвета.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};box-shadow:0 10px 22px {mix(k,45)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("G9", "Стекло", "Полупрозрачные плитки поверх бренд-градиента.",
 f'    <div class="glassbed">\n' + rail(lambda i,k,l,l1,e,n,h: f'<button class="t glass" style="--c:#202020">{ico(k,46,2,ci(k))}<span class="t__l">{l}</span></button>') + '\n    </div>')
block("G10", "Подпись под плиткой", "Цветной квадрат с иконкой, текст снаружи — как в iOS.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="out"><span class="out__b" style="background:{c(k)};color:#fff">{ico(k,34)}</span><span class="out__l">{l1}</span></button>'))

# =====================================================================
fam("H. Подача иконки")
block("H1", "Тонкий штрих", "Линия 1,25 — иконка становится деликатной.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,48,1.25)}<span class="t__l">{l}</span></button>'))
block("H2", "Жирный штрих", "Линия 2,75 — иконка звучит громче подписи.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,48,2.75)}<span class="t__l">{l}</span></button>'))
block("H3", "В белой плашке", "Квадратная подложка со скруглением 12.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="plate" style="color:{ci(k)}">{ico(k,26)}</span><span class="t__l">{l}</span></button>'))
block("H4", "Двойная иконка", "Светлая копия со сдвигом — плоский 3D.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="duo">{ico(k,46,2,mix(k,45))}{ico(k,46)}</span><span class="t__l">{l}</span></button>'))
block("H5", "Круг-обводка", "Иконка в кольце — аккуратный медальон.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="ringc" style="border-color:{mix(k,40)}">{ico(k,24)}</span><span class="t__l">{l}</span></button>'))
block("H6", "Огромная иконка", "64px — иконка почти во всю плитку.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};height:140px">{ico(k,64)}<span class="t__l">{l}</span></button>'))
block("H7", "Иконка снизу справа", "Подпись сверху, иконка ушла в правый нижний угол.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="t__l">{l}</span><span class="brc" style="color:{ci(k)}">{ico(k,42)}</span></button>'))
block("H8", "Градиентный штрих", "Обводка иконки залита бренд-парой.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico_grad(k, "h8"+k, *pair(i), s=48)}<span class="t__l">{l}</span></button>'))
block("H9", "Пятно под иконкой", "Неровный блоб — мягкая органика.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="blob" style="background:{mix(k,32)};color:{ci(k)}">{ico(k,26)}</span><span class="t__l">{l}</span></button>'))
block("H10", "С бейджем", "Точка-счётчик на иконке — есть новое.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="bdg-wrap">{ico(k,46)}<i class="bdg">{n}</i></span><span class="t__l">{l}</span></button>'))

# =====================================================================
fam("I. Компоновка ленты")
block("I1", "Первая — баннер", "Приоритетная категория занимает двойную ширину.",
 rail(lambda i,k,l,l1,e,n,h: (f'<button class="t t--rel" style="--bg:linear-gradient(120deg,{mix(k,40)},{bg(k)});--c:{c(k)};width:250px"><span class="wm wm--r" style="color:{ci(k)}">{ico(k,86,1.6)}</span><span class="t__l" style="font-size:22px;font-weight:600">{l1}</span></button>'
      if i == 0 else f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span></button>')))
block("I2", "Лента в два ряда", "Скролл вбок, но плитки идут парами — вдвое компактнее.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--sm2" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,28)}<span class="t__l" style="font-size:15px">{l1}</span></button>', cls="rail rail--2row"))
block("I3", "Активная крупнее", "Текущая категория выделена размером.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t{"" if i else " t--big"}" style="--bg:{bg(k)};--c:{c(k)};opacity:{1 if i==0 else .75}">{ico(k,56 if i==0 else 42)}<span class="t__l">{l}</span></button>'))
block("I4", "С плиткой «Все»", "В конце ленты — переход в полный каталог.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span></button>')
 .replace('\n    </div>', '\n      <button class="t t--all"><span class="allc">→</span><span class="t__l">Все<br>категории</span></button>\n    </div>'))
block("I5", "Сетка с разной высотой", "Плитки-«кирпичи» — сетка перестаёт быть скучной.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="brick" style="background:{bg(k)};color:{c(k)};height:{[110,140,140,110,110,140,110][i]}px">{ico(k,36)}<span class="t__l" style="font-size:16px">{l1}</span></button>', cls="grid2"))
block("I6", "Пик следующей", "Узкие плитки — видно, что лента продолжается.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};width:104px;height:104px">{ico(k,32)}<span class="t__l" style="font-size:14px">{l}</span></button>'))
block("I7", "Табы с подчёркиванием", "Категории как фильтр, а не как карточки.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="tab{" tab--on" if i==0 else ""}" style="--c:{c(k)}">{l1}</button>'))
block("I8", "Сегмент-контрол", "Все категории в одном сером контейнере.",
 f'    <div class="seg">\n' + "\n".join(f'      <button class="segb{" segb--on" if i==0 else ""}" style="--c:{c(k)}">{ico(k,18)}<span>{l1}</span></button>' for i,(k,l,l1,e,n,h) in enumerate(CATS)) + '\n    </div>')
block("I9", "Впритык с разделителями", "Плитки склеены в одну ленту, разделены линией.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="glue" style="background:{bg(k)};color:{c(k)}">{ico(k,34)}<span class="t__l" style="font-size:15px">{l1}</span></button>', cls="rail rail--glue"))
block("I10", "Четыре и «Ещё»", "Показываем главное, остальное прячем за кнопкой.",
 some(lambda i,k,l,l1,e,n,h: f'<button class="g3" style="background:{bg(k)};color:{c(k)}">{ico(k,30)}<span class="g3__l">{l1}</span></button>', 4,
      cls="grid2", extra='<button class="more">Ещё 3 категории</button>'))

# =====================================================================
fam("J. Декор и паттерны")
DEC = [
 ("J1", "Волна снизу", "Мягкая волна из фирменной геометрии.", "dec--wave"),
 ("J2", "Полукруг сверху", "Круг выходит за верхний край плитки.", "dec--half"),
 ("J3", "Точечная сетка", "Та же текстура, что на карте уроков.", "dec--dots"),
 ("J4", "Плюсы", "Мелкий знак «+» — техничный паттерн.", "dec--plus"),
 ("J5", "Зигзаг", "Диагональная ломаная по низу.", "dec--zig"),
 ("J6", "Бабблы", "Круги разного размера в углу.", "dec--bub"),
 ("J7", "Треугольники", "Острые формы для динамики.", "dec--tri"),
 ("J8", "Пунктирный кант", "Штриховая рамка внутри плитки.", "dec--dash"),
 ("J9", "Буква A знаком", "Фирменная «А» водяным знаком.", "dec--letter"),
 ("J10", "Градиентная рамка", "Контур из бренд-пары.", "dec--grad"),
]
for code, title, cap, cls in DEC:
    block(code, title, cap,
     rail(lambda i,k,l,l1,e,n,h,cls=cls: f'<button class="t t--rel dec {cls}" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,35)};--g1:{pair(i)[0]};--g2:{pair(i)[1]}">{ico(k,42)}<span class="t__l">{l}</span></button>'))

# =====================================================================
fam("K. Объём")
block("K1", "Подъём", "Мягкая тень отрывает плитку от фона.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};box-shadow:0 10px 24px rgba(32,32,32,.12)">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K2", "Неоморфизм", "Свет сверху, тень снизу — плитка «выдавлена».",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};box-shadow:6px 6px 14px rgba(32,32,32,.10),-6px -6px 14px rgba(255,255,255,.9)">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K3", "Кнопочное дно", "Цветная кромка снизу — как у кнопки «Продолжить».",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};box-shadow:0 5px 0 0 {mix(k,42)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K4", "Перспектива", "Плитки чуть наклонены к зрителю.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t persp" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K5", "Тень у иконки", "Объём только у иконки, плитка плоская.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="ish" style="filter:drop-shadow(0 5px 6px {mix(k,55)})">{ico(k,46)}</span><span class="t__l">{l}</span></button>'))
block("K6", "Глянец", "Диагональный блик по стеклу.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel gloss" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K7", "Внутренняя тень", "Плитка выглядит утопленной.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)};box-shadow:inset 0 3px 10px {mix(k,35)}">{ico(k,46)}<span class="t__l">{l}</span></button>'))
block("K8", "Стопка", "За плиткой видно вторую — намёк на курсы внутри.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t stack2" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,30)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("K9", "Иконка за краем", "Иконка выходит за границу плитки.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel esc" style="--bg:{bg(k)};--c:{c(k)}"><span class="escic" style="color:{ci(k)}">{ico(k,64)}</span><span class="t__l t__l--end">{l}</span></button>'))
block("K10", "Градиент и цветная тень", "Заливка с переходом плюс тень в тон.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:linear-gradient(150deg,{mix(k,45)},{bg(k)});--c:#202020;box-shadow:0 12px 24px {mix(k,40)}">{ico(k,46,2,ci(k))}<span class="t__l">{l}</span></button>'))

# =====================================================================
fam("L. Данные на плитке")
block("L1", "Прогресс по категории", "Тонкая полоска показывает, сколько пройдено.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,40)}<span class="t__l" style="font-size:16px">{l}</span><span class="bar" style="background:{mix(k,25)}"><i style="background:{c(k)};width:{[70,30,100,45,15,60,0][i]}%"></i></span></button>'))
block("L2", "Бейдж «Новое»", "Отмечаем категории, где появились курсы.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span>{newbadge(k, i in (0,3,5))}</button>'))
block("L3", "Счётчик в углу", "Число курсов кружком справа-сверху.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="cnum" style="background:{c(k)}">{n}</span>{ico(k,44)}<span class="t__l">{l}</span></button>'))
block("L4", "Кто учится", "Аватары учеников — социальное доказательство.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,38)}<span class="t__l" style="font-size:16px">{l}</span>{avatars(n)}</button>'))
block("L5", "Премиум-замок", "Часть категорий закрыта подпиской.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)};opacity:{.55 if i in (1,4,6) else 1}">{ico(k,44)}<span class="t__l">{l}</span>{lockbadge(i in (1,4,6))}</button>'))
block("L6", "Выбранная категория", "Активное состояние — контур и галочка.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)};{"box-shadow:0 0 0 2.5px "+c(k) if i==0 else ""}">{ico(k,44)}<span class="t__l">{l}</span>{checkbadge(k, i==0)}</button>'))
block("L7", "Рейтинг", "Средняя оценка курсов категории.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,38)}<span><span class="t__l" style="font-size:16px">{l}</span><span class="cnt">★ {4.5 + i*0.05:.1f}</span></span></button>'))
block("L8", "Длительность", "Сколько часов займёт вся категория.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,38)}<span><span class="t__l" style="font-size:16px">{l}</span><span class="cnt">{h} · {n} курс{"" if n==1 else "а" if n<5 else "ов"}</span></span></button>'))
block("L9", "Превью курсов", "Три цветных корешка — намёк на содержимое.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{previews(i)}<span class="t__l" style="font-size:16px">{l}</span></button>'))
block("L10", "Кольцо вместо иконки", "Прогресс категории кольцом — рифма с блоком «Продолжить».",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="rg">{svg_ring(k, [70,30,100,45,15,60,0][i])}</span><span class="t__l" style="font-size:16px">{l}</span></button>'))

# =====================================================================
fam("M. Минимализм")
block("M1", "Через точку", "Список категорий одной строкой — самый лёгкий вариант.",
 f'    <p class="dotline">' + ' <i>·</i> '.join(f'<a style="color:{c(k)}">{l1}</a>' for k,l,l1,e,n,h in CATS) + '</p>')
block("M2", "Точка и текст", "Без плашек: только цветной маркер и название.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="bare"><i class="dot" style="background:{c(k)}"></i><span>{l1}</span></button>'))
block("M3", "Ссылками", "Подчёркнутые названия — как в вебе.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="bare link" style="--c:{c(k)}">{l1}</button>', cls="wrap"))
block("M4", "Серые рамки", "Нейтральный контур, цвет только при выборе.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="p p--out" style="--bg:#fff;--c:hsl(var(--muted-foreground));border-color:hsl(var(--border))"><span>{l1}</span></button>'))
block("M5", "Крупным списком", "Меню-простыня: категории как заголовки.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="menu" style="--c:{c(k)}"><span>{l1}</span><i>{n}</i></button>', cls="list"))
block("M6", "Иконка и текст без фона", "Никаких плашек — иконка и подпись прямо на фоне.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="bare2" style="--c:{c(k)}">{ico(k,30)}<span>{l1}</span></button>'))
block("M7", "С разделителями", "Вертикальные палочки между названиями.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="bare sep" style="--c:{c(k)}">{l1}</button>'))
block("M8", "Плотно и мелко", "13px, минимальные отступы — для продвинутых.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="p p--xs" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,14)}<span>{l1}</span></button>', cls="wrap"))
block("M9", "Только иконки", "Круги без подписей — для тех, кто уже знает разделы.",
 rail(lambda i,k,l,l1,e,n,h: f'<span class="cr__i" style="background:{bg(k)};color:{ci(k)};flex:0 0 auto">{ico(k,28)}</span>'))
block("M10", "Иконки без фона", "Совсем голая лента иконок.",
 rail(lambda i,k,l,l1,e,n,h: f'<span style="flex:0 0 auto;color:{ci(k)};padding:6px">{ico(k,34)}</span>'))

# =====================================================================
fam("N. Эмодзи")
block("N1", "Эмодзи в плитке", "Тёплая подача вместо линейных иконок.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="em em--lg">{e}</span><span class="t__l">{l}</span></button>'))
block("N2", "Эмодзи в кружке", "Кружок собирает эмодзи в единый ритм.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="circ"><span class="em">{e}</span></span><span class="t__l">{l}</span></button>'))
block("N3", "Эмодзи водяным знаком", "Крупное полупрозрачное — фон, а не иконка.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="emwm">{e}</span><span class="t__l t__l--end">{l}</span></button>'))
block("N4", "На бренд-градиенте", "Эмодзи поверх пар из брендбука.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:linear-gradient(140deg,{pair(i)[0]},{pair(i)[1]});--c:#202020"><span class="em em--lg">{e}</span><span class="t__l">{l}</span></button>'))
block("N5", "Круги-сторис", "Компактная лента кружков с эмодзи.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="cr"><span class="cr__i" style="background:{bg(k)}"><span class="em em--lg">{e}</span></span><span class="cr__l">{l1}</span></button>'))
block("N6", "Пилюли", "Самый компактный эмодзи-вариант.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="p p--lg" style="--bg:{bg(k)};--c:{c(k)}"><span class="em">{e}</span><span>{l1}</span></button>'))
block("N7", "В углу", "Эмодзи как стикер в правом верхнем углу.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="corner"><span class="em em--lg">{e}</span></span><span class="t__l t__l--end">{l}</span></button>'))
block("N8", "Подпись под плиткой", "Квадрат с эмодзи, текст снаружи.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="out"><span class="out__b" style="background:{bg(k)}"><span class="em em--lg">{e}</span></span><span class="out__l">{l1}</span></button>'))
block("N9", "На тёплом нейтральном", "Warm Neutral с тонкой рамкой — спокойный фон для ярких эмодзи.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="t" style="--bg:#FFFCF5;--c:#202020;border:1px solid rgba(32,32,32,.08)"><span class="em em--lg">{e}</span><span class="t__l">{l}</span></button>'))
block("N10", "Сетка 3×", "Все категории на экране, без скролла.",
 rail(lambda i,k,l,l1,e,n,h: f'<button class="g3" style="background:{bg(k)};color:{c(k)}"><span class="em em--lg">{e}</span><span class="g3__l">{l1}</span></button>', cls="grid3"))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .fam { font-size: 24px; font-weight: 600; margin: 16px 0 0; letter-spacing: -.01em }
  button { font: inherit; border: 0; cursor: pointer; background: none; -webkit-tap-highlight-color: transparent }

  .wrap { display: flex; flex-wrap: wrap; gap: 8px }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px }
  .list { display: flex; flex-direction: column; gap: 2px }
  .rail--2row { display: grid; grid-auto-flow: column; grid-template-rows: auto auto; gap: 10px }
  .rail--glue { gap: 0 }

  /* базовая плитка */
  .t { display: flex; flex-direction: column; justify-content: space-between; text-align: left;
       width: 148px; height: 126px; padding: 12px; border-radius: 16px; background: var(--bg); color: var(--c) }
  .t__l { font-size: 18px; font-weight: 500; line-height: 1.15; white-space: pre-line; color: var(--c) }
  .t__l b { font-weight: 700 }
  .t__l--end { margin-top: auto }
  .t--rel { position: relative; overflow: hidden }
  .t--rel > * { position: relative }
  .t--shadow { box-shadow: 0 6px 18px rgba(32,32,32,.08) }
  .t--big { width: 176px; height: 150px }
  .t--sm2 { width: 132px; height: 92px }
  .t--all { background: hsl(var(--muted)); color: hsl(var(--foreground)); align-items: flex-start }
  .allc { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px;
          border-radius: 999px; background: #fff; font-size: 20px }
  .tv { display: flex; flex-direction: column; align-items: flex-start; justify-content: space-between;
        width: 96px; height: 150px; padding: 12px; border-radius: 16px; flex: 0 0 auto }
  .vert { writing-mode: vertical-rl; transform: rotate(180deg); font-size: 16px; font-weight: 500 }
  .circ { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px;
          border-radius: 999px; background: rgba(255,255,255,.75) }
  .plate { display: inline-flex; align-items: center; justify-content: center; width: 42px; height: 42px;
           border-radius: 12px; background: rgba(255,255,255,.8) }
  .ringc { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px;
           border-radius: 999px; border: 1.5px solid }
  .blob { display: inline-flex; align-items: center; justify-content: center; width: 46px; height: 46px;
          border-radius: 62% 38% 46% 54% / 54% 42% 58% 46% }
  .inner { display: flex; align-items: center; justify-content: center; height: 62px; border-radius: 12px;
           background: rgba(255,255,255,.8) }
  .duo { position: relative; display: inline-block; height: 46px }
  .duo svg:first-child { position: absolute; left: 4px; top: 4px }
  .ish { display: inline-block; line-height: 0 }
  .tilt { display: inline-block; transform: rotate(-10deg) }
  .brc { position: absolute; right: 8px; bottom: 8px }
  .escic { position: absolute; right: -12px; top: -6px }
  .bdg-wrap { position: relative; display: inline-block; line-height: 0 }
  .bdg { position: absolute; right: -4px; top: -4px; min-width: 18px; height: 18px; border-radius: 999px;
         background: #FF5C1A; color: #fff; font-size: 11px; font-weight: 700; font-style: normal;
         display: flex; align-items: center; justify-content: center; padding: 0 4px }
  .notch::after { content: ''; position: absolute; right: 18px; top: -12px; width: 24px; height: 24px;
                  border-radius: 999px; background: hsl(var(--background)) }
  .dbl { outline: 1.5px solid var(--pc); outline-offset: -6px }
  .cut { clip-path: polygon(0 0, 100% 0, 100% 74%, 74% 100%, 0 100%) }
  .persp { transform: perspective(600px) rotateY(-8deg) }
  .stack2 { position: relative }
  .stack2::before { content: ''; position: absolute; inset: 8px -8px -8px 8px; border-radius: 16px;
                    background: var(--pc); z-index: -1 }
  .gloss::after { content: ''; position: absolute; inset: 0; pointer-events: none;
                  background: linear-gradient(120deg, rgba(255,255,255,.75) 0%, rgba(255,255,255,0) 45%) }
  .glassbed { background: linear-gradient(120deg,#A66CFF,#FF8645); padding: 14px 0; border-radius: 16px; margin: 0 -16px }
  .glassbed .rail { margin: 0 -0px; padding: 0 14px }
  .glass { background: rgba(255,255,255,.55); backdrop-filter: blur(14px) saturate(1.4);
           border: 1px solid rgba(255,255,255,.6) }

  .caps { font-size: 13px; font-weight: 600; letter-spacing: .09em; text-transform: uppercase }
  .big { font-size: 22px; font-weight: 700; letter-spacing: -.01em }
  .track { font-size: 15px; letter-spacing: .07em }
  .und { border-bottom: 2.5px solid; padding-bottom: 4px; align-self: flex-start }
  .num { position: absolute; right: 12px; top: 10px; font-size: 13px; font-weight: 700; opacity: .45 }
  .cnt { display: block; font-size: 13px; color: rgba(32,32,32,.45); margin-top: 3px }
  .init { font-size: 46px; font-weight: 900; line-height: .9; letter-spacing: -.03em }
  .wmc { position: absolute; left: 50%; top: 46%; transform: translate(-50%,-50%); opacity: .22 }
  .ovl { text-align: center; margin: auto 0; width: 100% }
  .over { justify-content: center }
  .wm { position: absolute; right: -14px; top: -10px; opacity: .22 }
  .wm--r { right: 6px; top: 50%; transform: translateY(-50%) }
  .corner { position: absolute; right: 10px; top: 10px }

  /* пилюли и «голые» */
  .p { display: inline-flex; align-items: center; gap: 8px; height: 42px; padding: 0 16px; border-radius: 999px;
       background: var(--bg); color: var(--c); font-size: 16px; font-weight: 500; white-space: nowrap; flex: 0 0 auto }
  .p--out { border: 1.5px solid }
  .p--lg { height: 48px; font-size: 17px; padding: 0 18px }
  .p--xs { height: 30px; font-size: 13px; padding: 0 10px; gap: 5px }
  .dot { width: 9px; height: 9px; border-radius: 999px; display: inline-block; flex: 0 0 auto }
  .bare { display: inline-flex; align-items: center; gap: 8px; font-size: 16px; font-weight: 500;
          color: hsl(var(--foreground)); padding: 6px 2px; flex: 0 0 auto; white-space: nowrap }
  .bare2 { display: inline-flex; flex-direction: column; align-items: center; gap: 6px; color: var(--c);
           font-size: 13px; font-weight: 500; flex: 0 0 auto; width: 78px; text-align: center }
  .link { color: var(--c); text-decoration: underline; text-underline-offset: 4px }
  .sep { color: var(--c); position: relative; padding-right: 14px }
  .sep::after { content: ''; position: absolute; right: 0; top: 12px; bottom: 12px; width: 1px; background: hsl(var(--border)) }
  .dotline { font-size: 17px; line-height: 1.9; margin: 0 }
  .dotline a { font-weight: 500; text-decoration: none }
  .dotline i { color: hsl(var(--muted-foreground)); font-style: normal }
  .menu { display: flex; align-items: center; justify-content: space-between; width: 100%; padding: 12px 2px;
          font-size: 22px; font-weight: 600; color: var(--c); border-bottom: 1px solid hsl(var(--border)) }
  .menu i { font-size: 14px; font-style: normal; color: hsl(var(--muted-foreground)); font-weight: 500 }

  /* круги, сетки */
  .cr { display: flex; flex-direction: column; align-items: center; gap: 8px; width: 78px; flex: 0 0 auto }
  .cr__i { display: flex; align-items: center; justify-content: center; width: 64px; height: 64px; border-radius: 999px }
  .cr__l { font-size: 13px; font-weight: 500; color: hsl(var(--foreground)); text-align: center; line-height: 1.2 }
  .out { display: flex; flex-direction: column; align-items: center; gap: 8px; width: 92px; flex: 0 0 auto }
  .out__b { display: flex; align-items: center; justify-content: center; width: 72px; height: 72px; border-radius: 20px }
  .out__l { font-size: 13px; font-weight: 500; color: hsl(var(--foreground)); text-align: center; line-height: 1.2 }
  .g3 { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;
        aspect-ratio: 1; border-radius: 16px }
  .g3__l { font-size: 13px; font-weight: 500; text-align: center; line-height: 1.15 }
  .brick { display: flex; flex-direction: column; justify-content: space-between; text-align: left;
           padding: 12px; border-radius: 16px }
  .glue { display: flex; flex-direction: column; justify-content: space-between; text-align: left;
          width: 120px; height: 112px; padding: 12px; border-right: 1px solid rgba(255,255,255,.75); flex: 0 0 auto }
  .glue:first-child { border-radius: 16px 0 0 16px }
  .glue:last-child { border-radius: 0 16px 16px 0; border-right: 0 }
  .more { grid-column: span 2; height: 46px; border-radius: 999px; background: hsl(var(--muted));
          color: hsl(var(--foreground)); font-size: 15px; font-weight: 500 }
  .tab { padding: 8px 2px; font-size: 17px; font-weight: 500; color: hsl(var(--muted-foreground));
         border-bottom: 2.5px solid transparent; flex: 0 0 auto; white-space: nowrap }
  .tab--on { color: var(--c); border-color: var(--c) }
  .seg { display: flex; gap: 4px; padding: 4px; border-radius: 14px; background: hsl(var(--muted));
         overflow-x: auto; margin: 0 -16px; padding-left: 16px; padding-right: 16px }
  .seg::-webkit-scrollbar { display: none }
  .segb { display: inline-flex; align-items: center; gap: 6px; height: 38px; padding: 0 12px; border-radius: 10px;
          font-size: 15px; font-weight: 500; color: hsl(var(--muted-foreground)); white-space: nowrap; flex: 0 0 auto }
  .segb--on { background: #fff; color: var(--c); box-shadow: 0 1px 3px rgba(32,32,32,.12) }

  /* данные */
  .bar { display: block; height: 5px; border-radius: 999px; overflow: hidden; margin-top: 8px }
  .bar i { display: block; height: 100% }
  .new { position: absolute; right: 8px; top: 8px; padding: 3px 8px; border-radius: 999px;
         font-size: 11px; font-weight: 600; color: #fff }
  .cnum { position: absolute; right: 10px; top: 10px; width: 22px; height: 22px; border-radius: 999px;
          color: #fff; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center }
  .lock { position: absolute; right: 10px; top: 10px; font-size: 15px }
  .chk { position: absolute; right: 8px; top: 8px; width: 20px; height: 20px; border-radius: 999px; color: #fff;
         font-size: 12px; display: flex; align-items: center; justify-content: center }
  .avs { display: flex; align-items: center; gap: 4px; margin-top: 8px }
  .avs i { width: 18px; height: 18px; border-radius: 999px; border: 1.5px solid #fff; margin-right: -8px }
  .avs b { margin-left: 12px; font-size: 12px; font-weight: 500; color: rgba(32,32,32,.5) }
  .prev { display: flex; gap: 3px }
  .prev i { width: 22px; height: 30px; border-radius: 4px }
  .rg { line-height: 0 }

  /* эмодзи */
  .em { font-size: 19px; line-height: 1 }
  .em--lg { font-size: 38px; line-height: 1 }
  .emwm { position: absolute; right: -6px; top: -6px; font-size: 74px; line-height: 1; opacity: .3 }

  /* декор */
  .dec::before { content: ''; position: absolute; inset: 0; pointer-events: none }
  .dec--wave::before { background: var(--pc); clip-path: path('M0 96 Q 37 76 74 96 T 148 96 L148 126 L0 126 Z'); opacity: .6 }
  .dec--half::before { background: var(--pc); border-radius: 999px; inset: -46px -30px auto -30px; height: 92px; opacity: .5 }
  .dec--dots::before { background-image: radial-gradient(var(--pc) 1.4px, transparent 1.5px); background-size: 12px 12px; opacity: .8 }
  .dec--plus::before { background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20'%3E%3Cpath d='M10 6v8M6 10h8' stroke='%23202020' stroke-width='1.6' stroke-linecap='round'/%3E%3C/svg%3E");
                       background-size: 20px 20px; opacity: .16 }
  .dec--zig::before { background-image: repeating-linear-gradient(135deg, var(--pc) 0 3px, transparent 3px 9px);
                      inset: auto 0 0 0; height: 40px; opacity: .55 }
  .dec--bub::before { background: radial-gradient(circle 22px at 92% 18%, var(--pc) 99%, transparent 100%),
                                  radial-gradient(circle 12px at 70% 42%, var(--pc) 99%, transparent 100%),
                                  radial-gradient(circle 7px at 88% 52%, var(--pc) 99%, transparent 100%); opacity: .6 }
  .dec--tri::before { background: var(--pc); clip-path: polygon(100% 0, 100% 52%, 54% 0, 0 100%, 34% 100%, 0 58%); opacity: .5 }
  .dec--dash::before { border: 1.5px dashed var(--pc); border-radius: 12px; inset: 5px }
  .dec--letter::before { content: 'A'; font-size: 96px; font-weight: 900; color: var(--pc); opacity: .45;
                         line-height: .8; left: auto; right: -8px; top: -14px; inset: -14px -8px auto auto }
  .dec--grad::before { border-radius: 16px; padding: 2px; background: linear-gradient(135deg, var(--g1), var(--g2));
                       -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
                       -webkit-mask-composite: xor; mask-composite: exclude }
</style>
'''

HEAD = '''<title>Категории · ещё 100</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Категории · ещё 100</h1>
    <p class="text-caption-14">Десять семейств: форма плитки, типографика, цвет, подача иконки, компоновка ленты, декор, объём, данные на плитке, минимализм и эмодзи. Ленты листаются вбок, как на главной.</p>
  </div>

'''
TAIL = '''
  <p class="note">Коды из этого набора и из предыдущих сорока можно смешивать: форма из одного, декор из другого, данные из третьего.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for x in BUF if x.strip().startswith("<section")))
