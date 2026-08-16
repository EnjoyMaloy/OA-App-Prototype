# Генератор черновика: 40 вариантов блока «Категории»
OUT = '/home/user/OA-App-Prototype/prototypes/categories.html'

# ---------- иконки lucide (те же, что в приложении) ----------
P = {
 "ai": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
 "crypto": '<path d="M11.767 19.089c4.924.868 6.14-6.025 1.216-6.894m-1.216 6.894L5.86 18.047m5.908 1.042-.347 1.97m1.563-8.864c4.924.869 6.14-6.025 1.215-6.893m-1.215 6.893-3.94-.694m5.155-6.2L8.29 4.26m5.908 1.042.348-1.97M7.48 20.364l3.126-17.727"/>',
 "security": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "trading": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "invest": '<path d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z"/><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>',
 "web3": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
 "tools": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}

def ico(k, s=48, sw=2, color="currentColor", op=1):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="opacity:{op}">{P[k]}</svg>')

# id, подпись в две строки, подпись в строку, эмодзи
CATS = [
 ("ai",       "AI-навыки",       "AI-навыки",     "✨"),
 ("crypto",   "Основы\nкрипты",  "Основы крипты", "₿"),
 ("security", "Безопасность",    "Безопасность",  "🛡️"),
 ("trading",  "Трейдинг",        "Трейдинг",      "📈"),
 ("invest",   "Инвестиции",      "Инвестиции",    "💰"),
 ("web3",     "Web3 и DeFi",     "Web3 и DeFi",   "❄️"),
 ("tools",    "Инструменты",     "Инструменты",   "🔧"),
]
# у двух категорий иконка красится отдельным токеном — как в приложении
ICOVAR = {"ai": "--cat-ai-icon", "trading": "--cat-trading-icon"}

def c(k):    return f"hsl(var(--cat-{k}))"
def ci(k):   return f"hsl(var({ICOVAR.get(k, '--cat-' + k)}))"
def bg(k):   return f"hsl(var(--cat-{k}-bg))"
def mix(k, pct, other="white"):
    return f"color-mix(in srgb, hsl(var(--cat-{k})) {pct}%, {other})"

# бренд-градиенты из брендбука
PAIRS = [("#A66CFF", "#FF8645"), ("#FF96C8", "#FFDD31"), ("#88C5FD", "#CCEF40")]
def pair(i): return PAIRS[i % 3]

OUTBUF = []

def block(code, title, cap, body):
    OUTBUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
{body}
  </section>
''')

def rail(fn, cls="rail"):
    return f'    <div class="{cls}">\n' + "\n".join("      " + fn(i, *cat) for i, cat in enumerate(CATS)) + "\n    </div>"

# =========================================================================
# A. Плитка-карточка
# =========================================================================
OUTBUF.append('  <h2 class="fam">A. Плитка-карточка</h2>\n')

block("A1", "Как сейчас", "Иконка сверху, подпись снизу, пастельная заливка.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("A2", "Иконка в белом кружке", "Кружок отделяет иконку от фона — плитка выглядит собраннее.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:{bg(k)};--c:{c(k)}"><span class="circ" style="color:{ci(k)}">{ico(k,26)}</span><span class="t__l">{l}</span></button>'))

block("A3", "Иконка водяным знаком", "Крупная иконка уходит в фон, подпись читается первой.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="wm" style="color:{ci(k)}">{ico(k,92,1.6)}</span><span class="t__l t__l--end">{l}</span></button>'))

block("A4", "Иконка в углу", "Иконка прижата вправо-вверх, подпись — влево-вниз.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel" style="--bg:{bg(k)};--c:{c(k)}"><span class="corner" style="color:{ci(k)}">{ico(k,34)}</span><span class="t__l t__l--end">{l}</span></button>'))

block("A5", "Белая с цветным контуром", "Светлый интерфейс, цвет держится в контуре и иконке.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--outline" style="--bg:#fff;--c:{c(k)};border-color:{mix(k,28)}">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("A6", "Белая с тенью", "Плитка приподнята над фоном, цвет — только в иконке и подписи.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--shadow" style="--bg:#fff;--c:{c(k)}">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("A7", "Градиент в белый", "Заливка светлеет к низу — плитка не выглядит плоской.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:linear-gradient(160deg,{mix(k,18)} 0%,#fff 100%);--c:{c(k)}">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("A8", "Цветная шапка", "Тонкая полоса сверху маркирует категорию.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel t--cap" style="--bg:#fff;--c:{c(k)};--bar:{c(k)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))

block("A9", "По центру", "Иконка и подпись выровнены по центру — спокойнее, но менее плотно.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--center" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,44)}<span class="t__l t__l--c">{l1}</span></button>'))

block("A10", "Широкая 2:1", "Иконка слева, подпись справа — помещается длинное название.",
 rail(lambda i,k,l,l1,e: f'<button class="tw" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,34)}<span class="tw__l">{l1}</span></button>'))

# =========================================================================
# B. Пилюли
# =========================================================================
OUTBUF.append('  <h2 class="fam">B. Пилюли</h2>\n')

block("B1", "Пастельная пилюля", "Самый компактный вариант — экономит вертикаль на главной.",
 rail(lambda i,k,l,l1,e: f'<button class="p" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,20)}<span>{l1}</span></button>'))

block("B2", "Контурная пилюля", "Белый фон, цветной контур — воздушнее.",
 rail(lambda i,k,l,l1,e: f'<button class="p p--out" style="--bg:#fff;--c:{c(k)};border-color:{mix(k,30)}">{ico(k,20)}<span>{l1}</span></button>'))

block("B3", "С кружком иконки", "Иконка в цветном кружке, текст графитовый.",
 rail(lambda i,k,l,l1,e: f'<button class="p p--out" style="--bg:#fff;--c:#202020;border-color:hsl(var(--border))"><span class="dotc" style="background:{bg(k)};color:{ci(k)}">{ico(k,16)}</span><span>{l1}</span></button>'))

block("B4", "Графитовая", "Тёмная пилюля с цветной иконкой — контрастный акцент.",
 rail(lambda i,k,l,l1,e: f'<button class="p" style="--bg:#202020;--c:#fff">{ico(k,20,2,c(k))}<span>{l1}</span></button>'))

block("B5", "Только текст", "Без иконок — как фильтры в каталоге.",
 rail(lambda i,k,l,l1,e: f'<button class="p" style="--bg:{bg(k)};--c:{c(k)}"><span>{l1}</span></button>'))

block("B6", "В две строки", "Пилюли переносятся — видно все категории без скролла.",
 rail(lambda i,k,l,l1,e: f'<button class="p" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,18)}<span>{l1}</span></button>', cls="wrap"))

block("B7", "С точкой-маркером", "Нейтральная пилюля, цвет — в точке слева.",
 rail(lambda i,k,l,l1,e: f'<button class="p" style="--bg:hsl(var(--muted));--c:#202020"><i class="dot" style="background:{c(k)}"></i><span>{l1}</span></button>'))

block("B8", "Эмодзи", "Живее иконок, но выпадает из линейного стиля.",
 rail(lambda i,k,l,l1,e: f'<button class="p p--lg" style="--bg:{bg(k)};--c:{c(k)}"><span class="em">{e}</span><span>{l1}</span></button>'))

block("B9", "Бренд-градиент", "Пары градиентов из брендбука, белый текст.",
 rail(lambda i,k,l,l1,e: f'<button class="p p--lg" style="--bg:linear-gradient(100deg,{pair(i)[0]},{pair(i)[1]});--c:#fff">{ico(k,20)}<span>{l1}</span></button>'))

block("B10", "Белая с тенью", "Цветной текст на белом, мягкая тень.",
 rail(lambda i,k,l,l1,e: f'<button class="p p--sh" style="--bg:#fff;--c:{c(k)}">{ico(k,20)}<span>{l1}</span></button>'))

# =========================================================================
# C. Круги и сетки
# =========================================================================
OUTBUF.append('  <h2 class="fam">C. Круги и сетки</h2>\n')

block("C1", "Круг и подпись", "Как сторис: круглая иконка, подпись под ней.",
 rail(lambda i,k,l,l1,e: f'<button class="cr"><span class="cr__i" style="background:{bg(k)};color:{ci(k)}">{ico(k,30)}</span><span class="cr__l">{l1}</span></button>'))

block("C2", "Круг в градиентном кольце", "Кольцо из бренд-градиента вокруг иконки.",
 rail(lambda i,k,l,l1,e: f'<button class="cr"><span class="cr__ring" style="background:linear-gradient(135deg,{pair(i)[0]},{pair(i)[1]})"><span class="cr__i cr__i--in" style="background:#fff;color:{ci(k)}">{ico(k,28)}</span></span><span class="cr__l">{l1}</span></button>'))

block("C3", "Тёмный круг", "Графитовый круг, иконка в цвете категории.",
 rail(lambda i,k,l,l1,e: f'<button class="cr"><span class="cr__i" style="background:#202020;color:{c(k)}">{ico(k,30)}</span><span class="cr__l">{l1}</span></button>'))

block("C4", "Сетка 2×: строки", "Две колонки строк — вся навигация видна сразу.",
 rail(lambda i,k,l,l1,e: f'<button class="row2" style="--c:{c(k)}"><span class="sq" style="background:{bg(k)};color:{ci(k)}">{ico(k,20)}</span><span class="row2__l">{l1}</span></button>', cls="grid2"))

block("C5", "Сетка 3× квадратами", "Плитки без скролла, подпись под иконкой.",
 rail(lambda i,k,l,l1,e: f'<button class="g3" style="background:{bg(k)};color:{c(k)}">{ico(k,32)}<span class="g3__l">{l1}</span></button>', cls="grid3"))

block("C6", "Сетка 4× кружками", "Максимально компактно, подпись в одну строку.",
 rail(lambda i,k,l,l1,e: f'<button class="cr cr--sm"><span class="cr__i" style="background:{bg(k)};color:{ci(k)}">{ico(k,22)}</span><span class="cr__l cr__l--sm">{l1}</span></button>', cls="grid4"))

block("C7", "Список строками", "Формат каталога: квадрат иконки, название, шеврон.",
 rail(lambda i,k,l,l1,e: f'<button class="li"><span class="sq" style="background:{bg(k)};color:{ci(k)}">{ico(k,22)}</span><span class="li__l">{l1}</span><span class="li__ch">›</span></button>', cls="list"))

block("C8", "Сетка 2× с фоновой иконкой", "Широкие плитки, иконка уходит в фон.",
 rail(lambda i,k,l,l1,e: f'<button class="g2 t--rel" style="background:{bg(k)};color:{c(k)}"><span class="wm wm--r" style="color:{ci(k)}">{ico(k,72,1.6)}</span><span class="g2__l">{l1}</span></button>', cls="grid2"))

block("C9", "Первая крупная", "Акцент на приоритетной категории, остальные мельче.",
 rail(lambda i,k,l,l1,e: (f'<button class="t t--big" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,56)}<span class="t__l">{l}</span></button>' if i == 0
      else f'<button class="t t--sm" style="--bg:{bg(k)};--c:{c(k)}">{ico(k,32)}<span class="t__l t__l--sm">{l1}</span></button>')))

block("C10", "Круг с подписью внутри", "Подпись живёт внутри круга — самый плотный вариант.",
 rail(lambda i,k,l,l1,e: f'<button class="cin" style="background:{bg(k)};color:{c(k)}">{ico(k,22)}<span class="cin__l">{l1}</span></button>'))

# =========================================================================
# D. Брендбук
# =========================================================================
OUTBUF.append('  <h2 class="fam">D. Паттерны и цвет брендбука</h2>\n')

block("D1", "Паттерн: сетка квадратов", "Модульная сетка из знака «А» проступает на заливке.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel pat pat--grid" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,40)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))

block("D2", "Паттерн: диагонали", "Диагональные полосы из брендбука.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel pat pat--diag" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,26)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))

block("D3", "Паттерн: ромбы", "Рассыпанные ромбы — самый игривый из трёх.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel pat pat--dia" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,32)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))

block("D4", "Градиент Purple + Orange", "Первая пара брендбука на всех плитках, белая иконка.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:linear-gradient(140deg,#A66CFF,#FF8645);--c:#fff">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("D5", "Градиент Pink + Yellow", "Вторая пара — теплее и мягче.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:linear-gradient(140deg,#FF96C8,#FFDD31);--c:#202020">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("D6", "Градиент Blue + Lime", "Третья пара — холодная.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:linear-gradient(140deg,#88C5FD,#CCEF40);--c:#202020">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("D7", "Своя пара на каждой", "Плитки чередуют три бренд-пары — лента выглядит нарядно.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:linear-gradient(140deg,{pair(i)[0]},{pair(i)[1]});--c:{"#fff" if i%3==0 else "#202020"}">{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("D8", "Эмодзи на тёплом нейтральном", "Warm Neutral из брендбука, вместо иконок — эмодзи.",
 rail(lambda i,k,l,l1,e: f'<button class="t" style="--bg:#FFFCF5;--c:{c(k)};border:1px solid rgba(32,32,32,.06)"><span class="em em--lg">{e}</span><span class="t__l">{l}</span></button>'))

block("D9", "Графит и неон", "Тёмная плитка, цвет светится изнутри.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel" style="--bg:#202020;--c:{c(k)}"><span class="glowbg" style="background:radial-gradient(60px 60px at 30% 25%,{c(k)},transparent 70%)"></span>{ico(k,48)}<span class="t__l">{l}</span></button>'))

block("D10", "Шейп в углу", "Четверть-круг — фигура из фирменной геометрии.",
 rail(lambda i,k,l,l1,e: f'<button class="t t--rel shape" style="--bg:{bg(k)};--c:{c(k)};--pc:{mix(k,45)}">{ico(k,44)}<span class="t__l">{l}</span></button>'))

# =========================================================================
CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .fam { font-size: 24px; font-weight: 600; margin: 16px 0 0; letter-spacing: -.01em }
  button { font: inherit; border: 0; cursor: pointer; -webkit-tap-highlight-color: transparent }

  .wrap { display: flex; flex-wrap: wrap; gap: 8px }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 10px }
  .grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px }
  .grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px }
  .list { display: flex; flex-direction: column; gap: 2px }

  /* --- плитка --- */
  .t { display: flex; flex-direction: column; justify-content: space-between; text-align: left;
       width: 148px; height: 126px; padding: 12px; border-radius: 16px; background: var(--bg); color: var(--c) }
  .t__l { font-size: 18px; font-weight: 500; line-height: 1.15; white-space: pre-line; color: var(--c) }
  .t__l--sm { font-size: 15px }
  .t__l--c { text-align: center }
  .t__l--end { margin-top: auto }
  .t--rel { position: relative; overflow: hidden }
  .t--rel > * { position: relative }
  .t--outline { border: 1.5px solid }
  .t--shadow { box-shadow: 0 6px 18px rgba(32,32,32,.08) }
  .t--center { align-items: center; justify-content: center; gap: 10px }
  .t--cap::before { content: ''; position: absolute; left: 0; right: 0; top: 0; height: 5px; background: var(--bar) }
  .t--big { width: 180px; height: 152px }
  .t--sm { width: 120px; height: 106px }
  .circ { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px;
          border-radius: 999px; background: rgba(255,255,255,.75) }
  .wm { position: absolute; right: -14px; top: -10px; opacity: .22 }
  .wm--r { right: 8px; top: 50%; transform: translateY(-50%) }
  .corner { position: absolute; right: 10px; top: 10px }
  .glowbg { position: absolute; inset: 0; opacity: .45; filter: blur(2px) }

  .tw { display: flex; align-items: center; gap: 10px; width: 200px; height: 74px; padding: 14px;
        border-radius: 16px; background: var(--bg); color: var(--c) }
  .tw__l { font-size: 17px; font-weight: 500; line-height: 1.15 }

  /* --- пилюли --- */
  .p { display: inline-flex; align-items: center; gap: 8px; height: 42px; padding: 0 16px;
       border-radius: 999px; background: var(--bg); color: var(--c); font-size: 16px; font-weight: 500; white-space: nowrap }
  .p--out { border: 1.5px solid }
  .p--lg { height: 48px; font-size: 17px; padding: 0 18px }
  .p--sh { box-shadow: 0 4px 14px rgba(32,32,32,.09) }
  .dot { width: 9px; height: 9px; border-radius: 999px; display: inline-block }
  .dotc { display: inline-flex; align-items: center; justify-content: center; width: 26px; height: 26px;
          border-radius: 999px; margin-left: -6px }
  .em { font-size: 19px; line-height: 1 }
  .em--lg { font-size: 40px; line-height: 1 }

  /* --- круги --- */
  .cr { display: flex; flex-direction: column; align-items: center; gap: 8px; width: 76px; background: none }
  .cr--sm { width: auto }
  .cr__i { display: flex; align-items: center; justify-content: center; width: 64px; height: 64px; border-radius: 999px }
  .cr__ring { display: flex; align-items: center; justify-content: center; width: 68px; height: 68px;
              border-radius: 999px; padding: 2.5px }
  .cr__i--in { width: 100%; height: 100%; }
  .cr__l { font-size: 13px; font-weight: 500; color: hsl(var(--foreground)); text-align: center; line-height: 1.2 }
  .cr__l--sm { font-size: 12px }
  .cin { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px;
         width: 92px; height: 92px; border-radius: 999px }
  .cin__l { font-size: 13px; font-weight: 500; text-align: center; line-height: 1.15; padding: 0 8px }

  .sq { display: inline-flex; align-items: center; justify-content: center; width: 40px; height: 40px; border-radius: 11px; flex: 0 0 auto }
  .row2 { display: flex; align-items: center; gap: 10px; padding: 8px; border-radius: 14px;
          background: hsl(var(--background)); border: 1px solid hsl(var(--border)) }
  .row2__l { font-size: 15px; font-weight: 500; color: hsl(var(--foreground)); text-align: left; line-height: 1.15 }
  .g3 { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px;
        aspect-ratio: 1; border-radius: 16px }
  .g3__l { font-size: 13px; font-weight: 500; text-align: center; line-height: 1.15 }
  .g2 { display: flex; align-items: center; height: 78px; padding: 14px; border-radius: 16px }
  .g2__l { font-size: 16px; font-weight: 500; text-align: left }
  .li { display: flex; align-items: center; gap: 12px; width: 100%; padding: 8px 4px; background: none }
  .li__l { flex: 1; text-align: left; font-size: 16px; font-weight: 500; color: hsl(var(--foreground)) }
  .li__ch { font-size: 20px; color: hsl(var(--muted-foreground)) }

  /* --- паттерны брендбука --- */
  .pat::before { content: ''; position: absolute; inset: 0; pointer-events: none }
  .pat--grid::before { background-image: linear-gradient(var(--pc) 1.5px, transparent 1.5px),
                       linear-gradient(90deg, var(--pc) 1.5px, transparent 1.5px); background-size: 14px 14px; opacity: .5 }
  .pat--diag::before { background-image: repeating-linear-gradient(45deg, var(--pc) 0 5px, transparent 5px 12px); opacity: .55 }
  .pat--dia::before { background-image: radial-gradient(var(--pc) 2.5px, transparent 2.6px); background-size: 20px 20px; opacity: .6 }
  .shape::before { content: ''; position: absolute; right: -26px; bottom: -26px; width: 86px; height: 86px;
                   border-radius: 999px; background: var(--pc); opacity: .55 }
</style>
'''

HEAD = '''<title>Категории · 40 вариантов</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Категории · 40</h1>
    <p class="text-caption-14">Четыре семейства: плитка-карточка, пилюли, круги и сетки, паттерны брендбука. Ленты листаются вбок, как на главной. Скажи код — поставлю в приложение.</p>
  </div>

'''
TAIL = '''
  <p class="note">Коды можно смешивать: например, форма из A2 с паттерном из D1 или цветом из D7.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(OUTBUF) + TAIL)
print("вариантов:", sum(1 for x in OUTBUF if x.strip().startswith("<section")))
