# Генератор: 50 вариантов категорий на основе понравившихся A7, J3, J4, C8, K6, K10
OUT = '/home/user/OA-App-Prototype/prototypes/categories-3.html'

P = {
 "ai": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
 "crypto": '<path d="M11.767 19.089c4.924.868 6.14-6.025 1.216-6.894m-1.216 6.894L5.86 18.047m5.908 1.042-.347 1.97m1.563-8.864c4.924.869 6.14-6.025 1.215-6.893m-1.215 6.893-3.94-.694m5.155-6.2L8.29 4.26m5.908 1.042.348-1.97M7.48 20.364l3.126-17.727"/>',
 "security": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "trading": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "invest": '<path d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z"/><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>',
 "web3": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
 "tools": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}

def ico(k, s=48, sw=2, color="currentColor"):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{P[k]}</svg>')

CATS = [
 ("ai",       "AI-навыки",      "AI-навыки",     5),
 ("crypto",   "Основы\nкрипты", "Основы крипты", 2),
 ("security", "Безопасность",   "Безопасность",  1),
 ("trading",  "Трейдинг",       "Трейдинг",      3),
 ("invest",   "Инвестиции",     "Инвестиции",    4),
 ("web3",     "Web3 и DeFi",    "Web3 и DeFi",   4),
 ("tools",    "Инструменты",    "Инструменты",   1),
]
ICOVAR = {"ai": "--cat-ai-icon", "trading": "--cat-trading-icon"}

def c(k):  return f"hsl(var(--cat-{k}))"
def ci(k): return f"hsl(var({ICOVAR.get(k, '--cat-' + k)}))"
def bgv(k): return f"hsl(var(--cat-{k}-bg))"
def mix(k, pct, other="white"): return f"color-mix(in srgb, hsl(var(--cat-{k})) {pct}%, {other})"

# градиентные заливки на основе A7
def gr(k, kind="down"):
    g = {
      "down":  f"linear-gradient(160deg,{mix(k,20)} 0%,#fff 100%)",
      "up":    f"linear-gradient(340deg,{mix(k,20)} 0%,#fff 100%)",
      "diag":  f"linear-gradient(120deg,{mix(k,24)} 0%,#fff 92%)",
      "soft":  f"linear-gradient(160deg,{mix(k,14)} 0%,#fff 100%)",
      "deep":  f"linear-gradient(155deg,{mix(k,38)} 0%,{mix(k,8)} 100%)",
      "three": f"linear-gradient(160deg,{mix(k,32)} 0%,{mix(k,12)} 55%,#fff 100%)",
      "rad":   f"radial-gradient(120% 110% at 18% 14%,{mix(k,30)} 0%,#fff 78%)",
      "corner":f"radial-gradient(90% 90% at 100% 100%,{mix(k,28)} 0%,#fff 80%)",
    }
    return g[kind]

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

def tile(k, l, bg, pc, cls="", ic=None, extra="", label=None, lcls=""):
    """Базовая плитка: заливка bg, цвет паттерна pc, содержимое."""
    ic = ico(k, 46) if ic is None else ic
    label = l if label is None else label
    return (f'<button class="t t--rel {cls}" style="--bg:{bg};--c:{c(k)};--pc:{pc}{extra}">'
            f'{ic}<span class="t__l {lcls}">{label}</span></button>')

def wm(k, size=86, sw=1.6, cls="wm"):
    return f'<span class="{cls}" style="color:{ci(k)}">{ico(k, size, sw)}</span>'

# =====================================================================
fam("P. Градиент и текстура")
block("P1", "Градиент + точки", "A7 и J3 вместе: заливка светлеет, поверх — точечная сетка.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots")))
block("P2", "Точки только снизу", "Текстура растворяется кверху — иконка остаётся чистой.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,38), "dots dots--fade")))
block("P3", "Диагональный градиент + плюсы", "Заливка идёт по диагонали, паттерн — знак «+».",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"diag"), mix(k,32), "plus")))
block("P4", "Крупные редкие плюсы", "Паттерн крупнее и реже — спокойнее.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "plus plus--lg")))
block("P5", "Крупные точки", "Разреженная сетка точек, шаг 18.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,38), "dots dots--lg")))
block("P6", "Мелкая плотная сетка", "Точки почти сливаются в фактуру бумаги.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,40), "dots dots--sm")))
block("P7", "Градиент снизу вверх", "Цвет внизу, светлое сверху — плитка «стоит на земле».",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"up"), mix(k,32), "dots")))
block("P8", "Радиальный от иконки", "Свет исходит из угла с иконкой.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"rad"), mix(k,32), "dots")))
block("P9", "Градиент в три стопа", "Насыщенный верх, светлая середина, белый низ.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"three"), mix(k,30), "plus")))
block("P10", "Плотный градиент", "Заливка держит цвет — паттерн белый, а не цветной.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), "rgba(255,255,255,.75)", "dots")))

# =====================================================================
fam("Q. Фоновая иконка")
block("Q1", "Иконка справа", "C8 в вертикальной плитке: иконка уходит в фон.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,88) + f'<span class="ph"></span>', lcls="t__l--end")))
block("Q2", "Иконка снизу справа", "Обрезана краем — плитка кажется больше кадра.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,96,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end")))
block("Q3", "Иконка сверху справа", "Классическая подача водяного знака.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,92,1.6,"wm wm--tr") + '<span class="ph"></span>', lcls="t__l--end")))
block("Q4", "Иконка по центру", "Текст ложится поверх симметричного знака.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,100,1.5,"wm wm--ctr") + '<span class="ph"></span>', lcls="t__l--end")))
block("Q5", "Иконка и точки", "Водяной знак поверх точечной сетки.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=wm(k,88) + '<span class="ph"></span>', lcls="t__l--end")))
block("Q6", "Толстый контур", "Иконка фоном, но линия жирная — читается как графика.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,92,2.6) + '<span class="ph"></span>', lcls="t__l--end")))
block("Q7", "Иконка и маленькая копия", "Крупная в фоне, маленькая — как обычная иконка.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,92) + ico(k,30), lcls="")))
block("Q8", "Иконка и плюсы", "Знак поверх «+»-паттерна.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"diag"), mix(k,30), "plus", ic=wm(k,88,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end")))
block("Q9", "Иконка на всю плитку", "Знак заполняет карточку и обрезается со всех сторон.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,130,1.4,"wm wm--full") + '<span class="ph"></span>', lcls="t__l--end")))
block("Q10", "Слабый знак", "Прозрачность 12% — почти неуловимая фактура.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", ic=wm(k,96,1.8,"wm wm--faint") + '<span class="ph"></span>', lcls="t__l--end")))

# =====================================================================
fam("R. Тень и глянец")
block("R1", "Градиент и цветная тень", "K10: заливка с переходом плюс тень в тон.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "", extra=f";box-shadow:0 12px 24px {mix(k,40)}")))
block("R2", "Тень глубже", "Плитка сильнее отрывается от фона.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "", extra=f";box-shadow:0 18px 30px -6px {mix(k,55)}")))
block("R3", "Глянец по диагонали", "K6: светлая полоса пересекает плитку.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "gloss")))
block("R4", "Блик сверху", "Свет ложится на верхнюю треть.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "gloss gloss--top")))
block("R5", "Глянец и тень", "Стеклянная плитка с тенью своего цвета.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "gloss", extra=f";box-shadow:0 12px 24px {mix(k,40)}")))
block("R6", "Глянец и точки", "Текстура под бликом.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), "rgba(255,255,255,.7)", "dots gloss")))
block("R7", "Внутренний кант", "Белая волосяная линия по краю — как у стекла.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "hair")))
block("R8", "Кант, глянец и тень", "Все три приёма вместе — самая «дорогая» подача.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "hair gloss", extra=f";box-shadow:0 14px 26px {mix(k,42)}")))
block("R9", "Свет из угла", "Мягкое радиальное свечение вместо полосы.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"corner"), mix(k,30), "", extra=f";box-shadow:0 12px 24px {mix(k,35)}")))
block("R10", "Пастель и тень", "Светлый вариант A7 с цветной тенью — легче, чем K10.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,30), "", extra=f";box-shadow:0 10px 22px {mix(k,32)}")))

# =====================================================================
fam("S. Широкие плитки 2×")
def wide(k, l1, bg, pc, cls="", extra="", icon_size=72, label_first=True, sub=None):
    ic = f'<span class="wm wm--wide" style="color:{ci(k)}">{ico(k, icon_size, 1.6)}</span>'
    body = f'<span class="g2__l">{l1}</span>' + (f'<span class="g2__s">{sub}</span>' if sub else "")
    return (f'<button class="g2 t--rel {cls}" style="--bg:{bg};--c:{c(k)};--pc:{pc}{extra}">'
            f'{ic}<span class="g2__b">{body}</span></button>')

block("S1", "Как есть", "C8: широкая плитка, иконка уходит в фон.",
 rail(lambda i,k,l,l1,n: wide(k, l1, bgv(k), mix(k,30)), cls="grid2"))
block("S2", "С градиентом", "Заливка светлеет по диагонали.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30)), cls="grid2"))
block("S3", "С точками", "Точечная сетка на градиенте.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,35), "dots"), cls="grid2"))
block("S4", "С плюсами", "«+»-паттерн вместо точек.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30), "plus"), cls="grid2"))
block("S5", "С цветной тенью", "Плитки приподняты, тень в тон.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30), "", f";box-shadow:0 10px 20px {mix(k,35)}"), cls="grid2"))
block("S6", "С глянцем", "Диагональный блик по стеклу.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"deep"), mix(k,30), "gloss"), cls="grid2"))
block("S7", "Иконка слева", "Знак работает как аватар категории.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30), "g2--left"), cls="grid2"))
block("S8", "Со счётчиком", "Под названием — сколько курсов.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30), "g2--tall", sub=f'{n} курс{"" if n==1 else "а" if n<5 else "ов"}'), cls="grid2"))
block("S9", "В одну колонку", "Широкие строки на всю ширину экрана.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,30), "g2--full", icon_size=86), cls="list list--gap"))
block("S10", "Всё вместе", "Градиент, точки, фоновая иконка и цветная тень.",
 rail(lambda i,k,l,l1,n: wide(k, l1, gr(k,"diag"), mix(k,32), "dots", f";box-shadow:0 10px 20px {mix(k,32)}"), cls="grid2"))

# =====================================================================
fam("T. Комбинации")
block("T1", "Градиент + точки + знак", "Три любимых приёма в вертикальной плитке.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=wm(k,86,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end")))
block("T2", "Плюсы и цветная тень", "Паттерн «+», заливка с переходом, тень в тон.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"diag"), mix(k,30), "plus", extra=f";box-shadow:0 10px 22px {mix(k,32)}")))
block("T3", "Знак, глянец, тень", "Иконка фоном под бликом, плитка приподнята.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"deep"), mix(k,30), "gloss", ic=wm(k,90,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end",
      extra=f";box-shadow:0 12px 24px {mix(k,40)}")))
block("T4", "Квадрат 1:1", "Крупная плитка: градиент, точки, знак.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=wm(k,100,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end",
      extra=";width:152px;height:152px")))
block("T5", "Вертикальная 3:4", "Узкая и высокая с той же отделкой.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=wm(k,80,1.6,"wm wm--br") + '<span class="ph"></span>', lcls="t__l--end",
      extra=";width:122px;height:162px")))
block("T6", "Иконка в белом кружке", "Кружок поверх градиента и точек.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=f'<span class="circ" style="color:{ci(k)}">{ico(k,26)}</span>')))
block("T7", "Крупная подпись", "22px semibold поверх градиента и знака.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"diag"), mix(k,30), "", ic=wm(k,90,1.6,"wm wm--br") + '<span class="ph"></span>',
      lcls="t__l--end big", extra=";width:160px")))
block("T8", "Сетка 2× без скролла", "Всё то же, но плитки в сетке — лента не нужна.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k), mix(k,35), "dots", ic=wm(k,80,1.6,"wm wm--br") + '<span class="ph"></span>',
      lcls="t__l--end", extra=";width:auto;height:128px"), cls="grid2"))
block("T9", "Пастель и мягкая тень", "Светлее T1: пастельный градиент, лёгкая тень.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"soft"), mix(k,28), "dots", ic=wm(k,86,1.6,"wm wm--br") + '<span class="ph"></span>',
      lcls="t__l--end", extra=f";box-shadow:0 8px 18px {mix(k,26)}")))
block("T10", "Финальный кандидат", "Градиент в белый, точки, знак в углу, кант и тень в тон.",
 rail(lambda i,k,l,l1,n: tile(k, l, gr(k,"three"), mix(k,32), "dots hair", ic=wm(k,88,1.6,"wm wm--br") + '<span class="ph"></span>',
      lcls="t__l--end", extra=f";box-shadow:0 12px 24px {mix(k,34)}")))

PLUS_SVG = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='20' height='20'%3E"
            "%3Cpath d='M10 6v8M6 10h8' stroke='%23000' stroke-width='1.7' stroke-linecap='round'/%3E%3C/svg%3E\")")
PLUS_LG = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E"
           "%3Cpath d='M15 9v12M9 15h12' stroke='%23000' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E\")")

CSS = f'''
<style>
  .variant {{ display: flex; flex-direction: column; gap: 10px }}
  .variant__cap {{ font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }}
  .variant h2 {{ font-size: 17px; font-weight: 600; margin: 0 }}
  .fam {{ font-size: 24px; font-weight: 600; margin: 16px 0 0; letter-spacing: -.01em }}
  button {{ font: inherit; border: 0; cursor: pointer; background: none; -webkit-tap-highlight-color: transparent }}

  .grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px }}
  .list {{ display: flex; flex-direction: column }}
  .list--gap {{ gap: 10px }}

  .t {{ display: flex; flex-direction: column; justify-content: space-between; text-align: left;
       width: 148px; height: 126px; padding: 12px; border-radius: 16px; background: var(--bg); color: var(--c) }}
  .t__l {{ font-size: 18px; font-weight: 500; line-height: 1.15; white-space: pre-line; color: var(--c) }}
  .t__l--end {{ margin-top: auto }}
  .t__l.big {{ font-size: 22px; font-weight: 600; letter-spacing: -.01em }}
  .t--rel {{ position: relative; overflow: hidden }}
  .t--rel > * {{ position: relative }}
  .ph {{ display: block; height: 0 }}
  .circ {{ display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px;
          border-radius: 999px; background: rgba(255,255,255,.8) }}

  /* фоновая иконка */
  .wm {{ position: absolute; right: -12px; top: 50%; transform: translateY(-50%); opacity: .22; line-height: 0 }}
  .wm--br {{ right: -14px; top: auto; bottom: -14px; transform: none }}
  .wm--tr {{ right: -14px; top: -14px; transform: none }}
  .wm--ctr {{ left: 50%; top: 50%; right: auto; transform: translate(-50%,-50%) }}
  .wm--full {{ left: 50%; top: 50%; right: auto; transform: translate(-50%,-50%); opacity: .16 }}
  .wm--faint {{ opacity: .12 }}
  .wm--wide {{ right: 10px; top: 50%; transform: translateY(-50%); opacity: .25 }}

  /* паттерны */
  .dots::before {{ content: ''; position: absolute; inset: 0; pointer-events: none;
                  background-image: radial-gradient(var(--pc) 1.5px, transparent 1.6px); background-size: 13px 13px }}
  .dots--lg::before {{ background-image: radial-gradient(var(--pc) 2.2px, transparent 2.3px); background-size: 19px 19px }}
  .dots--sm::before {{ background-image: radial-gradient(var(--pc) 1.1px, transparent 1.2px); background-size: 9px 9px }}
  .dots--fade::before {{ -webkit-mask-image: linear-gradient(transparent 18%, #000 78%);
                        mask-image: linear-gradient(transparent 18%, #000 78%) }}
  .plus::before {{ content: ''; position: absolute; inset: 0; pointer-events: none; background: var(--pc);
                  -webkit-mask-image: {PLUS_SVG}; mask-image: {PLUS_SVG};
                  -webkit-mask-size: 20px 20px; mask-size: 20px 20px }}
  .plus--lg::before {{ -webkit-mask-image: {PLUS_LG}; mask-image: {PLUS_LG};
                      -webkit-mask-size: 30px 30px; mask-size: 30px 30px }}

  /* глянец и кант */
  .gloss::after {{ content: ''; position: absolute; inset: 0; pointer-events: none;
                  background: linear-gradient(118deg, rgba(255,255,255,.72) 0%, rgba(255,255,255,0) 46%) }}
  .gloss--top::after {{ background: linear-gradient(180deg, rgba(255,255,255,.7) 0%, rgba(255,255,255,0) 42%) }}
  .hair {{ box-shadow: inset 0 0 0 1px rgba(255,255,255,.7) }}

  /* широкие плитки */
  .g2 {{ display: flex; align-items: center; height: 78px; padding: 14px; border-radius: 16px;
        background: var(--bg); color: var(--c); text-align: left }}
  .g2--tall {{ height: 92px }}
  .g2--full {{ height: 88px; width: 100% }}
  .g2--left {{ flex-direction: row }}
  .g2--left .wm--wide {{ left: 14px; right: auto }}
  .g2--left .g2__b {{ margin-left: 74px }}
  .g2__b {{ display: flex; flex-direction: column; gap: 3px }}
  .g2__l {{ font-size: 17px; font-weight: 500; line-height: 1.15 }}
  .g2__s {{ font-size: 13px; color: rgba(32,32,32,.45) }}
</style>
'''

HEAD = '''<title>Категории · 50 на основе выбранных</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Категории · 50</h1>
    <p class="text-caption-14">Развитие понравившихся A7 (градиент в белый), J3 (точки), J4 (плюсы), C8 (широкая плитка с фоновой иконкой), K6 (глянец) и K10 (градиент с цветной тенью).</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — соберу в приложении. Можно смешивать: например заливка из P9, паттерн из P4 и тень из R2.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for x in BUF if x.strip().startswith("<section")))
