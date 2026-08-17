# Генератор: заливка P9 (градиент в три стопа) + 22 разных паттерна
OUT = '/home/user/OA-App-Prototype/prototypes/categories-4.html'

P = {
 "ai": '<path d="M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z"/><path d="M20 3v4"/><path d="M22 5h-4"/><path d="M4 17v2"/><path d="M5 18H3"/>',
 "crypto": '<path d="M11.767 19.089c4.924.868 6.14-6.025 1.216-6.894m-1.216 6.894L5.86 18.047m5.908 1.042-.347 1.97m1.563-8.864c4.924.869 6.14-6.025 1.215-6.893m-1.215 6.893-3.94-.694m5.155-6.2L8.29 4.26m5.908 1.042.348-1.97M7.48 20.364l3.126-17.727"/>',
 "security": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "trading": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "invest": '<path d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z"/><path d="M21.21 15.89A10 10 0 1 1 8 2.83"/>',
 "web3": '<line x1="2" x2="22" y1="12" y2="12"/><line x1="12" x2="12" y1="2" y2="22"/><path d="m20 16-4-4 4-4"/><path d="m4 8 4 4-4 4"/><path d="m16 4-4 4-4-4"/><path d="m8 20 4-4 4 4"/>',
 "tools": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
}

def ico(k, s=46, sw=2):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{P[k]}</svg>')

CATS = [
 ("ai", "AI-навыки"), ("crypto", "Основы\nкрипты"), ("security", "Безопасность"),
 ("trading", "Трейдинг"), ("invest", "Инвестиции"), ("web3", "Web3 и DeFi"), ("tools", "Инструменты"),
]

def c(k): return f"hsl(var(--cat-{k}))"
def mix(k, pct, other="white"): return f"color-mix(in srgb, hsl(var(--cat-{k})) {pct}%, {other})"
# P9: насыщенный верх → светлая середина → белый низ
def fill(k): return f"linear-gradient(160deg,{mix(k,32)} 0%,{mix(k,12)} 55%,#fff 100%)"

BUF = []
def block(code, title, cap, cls, pcpct=32, pcolor=None):
    tiles = []
    for k, l in CATS:
        pc = pcolor or mix(k, pcpct)
        tiles.append(f'        <button class="t {cls}" style="--bg:{fill(k)};--c:{c(k)};--pc:{pc}">'
                     f'{ico(k)}<span class="t__l">{l}</span></button>')
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
    <div class="rail">
{chr(10).join(tiles)}
    </div>
  </section>
''')

# ---- порядок вариантов ----
block("M1", "Как на карте курса", "Один в один паттерн с карты уроков: точки 1px, шаг 16, но в цвете категории.", "map")
block("M2", "Карта курса, фиолетовые", "Тот же рисунок, но точки брендового фиолетового — общая нитка с картой уроков.", "map", pcolor="hsl(var(--violet-dark) / .35)")
block("M3", "Карта курса, плотнее", "Тот же рисунок, шаг 12 — фактура заметнее.", "map map--12")
block("M4", "Карта курса, крупнее", "Шаг 22, точка 1.6 — спокойный ритм.", "map map--22")
block("M5", "Точки контрастнее", "Тот же шаг 16, но точка ярче и толще.", "dots", pcpct=42)
block("M6", "Точки в шахматку", "Ряды смещены — рисунок перестаёт быть строгой сеткой.", "checker", pcpct=38)
block("M7", "Точки с растворением", "Текстура тает кверху, иконка остаётся на чистом.", "dots fade", pcpct=40)
block("M8", "Плюсы", "Знак «+» — техничнее точек.", "plus")
block("M9", "Крупные плюсы", "Шаг 30 — паттерн читается как графика.", "plusL")
block("M10", "Косые кресты", "«×» вместо «+» — динамичнее.", "cross")
block("M11", "Тонкие диагонали", "Полосы 45°, шаг 10.", "diag")
block("M12", "Широкие диагонали", "Редкие широкие полосы — самый заметный из линейных.", "diagW")
block("M13", "Клетка", "Линейная сетка — модульность брендбука в чистом виде.", "grid")
block("M14", "Миллиметровка", "Мелкая клетка с крупной поверх.", "graph")
block("M15", "Ромбы", "Ромбы из брендбука, шаг 22.", "diamond")
block("M16", "Квадратные модули", "Квадраты из знака «А».", "square")
block("M17", "Шевроны", "Ломаная «птичка» рядами.", "chev")
block("M18", "Волны", "Мягкая синусоида — самый плавный паттерн.", "wave")
block("M19", "Кольца", "Окружности вместо точек.", "ring")
block("M20", "Штрихи", "Короткие тире по диагонали.", "dash")
block("M21", "Искры", "Мелкая четырёхлучевая звезда — рифма с иконкой AI.", "spark")
block("M22", "Соты", "Шестиугольная сетка.", "hex")

def mask(svg, size):
    u = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
         f"width='{size[0]}' height='{size[1]}'%3E{svg}%3C/svg%3E\")")
    return (f"background: var(--pc); -webkit-mask-image: {u}; mask-image: {u}; "
            f"-webkit-mask-size: {size[0]}px {size[1]}px; mask-size: {size[0]}px {size[1]}px;")

S = lambda d, w=1.7: f"%3Cpath d='{d}' stroke='%23000' stroke-width='{w}' fill='none' stroke-linecap='round'/%3E"

CSS = f'''
<style>
  .variant {{ display: flex; flex-direction: column; gap: 10px }}
  .variant__cap {{ font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }}
  .variant h2 {{ font-size: 17px; font-weight: 600; margin: 0 }}
  button {{ font: inherit; border: 0; cursor: pointer; background: none }}

  .t {{ position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between;
       text-align: left; width: 148px; height: 126px; padding: 12px; border-radius: 16px;
       background: var(--bg); color: var(--c) }}
  .t > * {{ position: relative }}
  .t__l {{ font-size: 18px; font-weight: 500; line-height: 1.15; white-space: pre-line; color: var(--c) }}
  .t::before {{ content: ''; position: absolute; inset: 0; pointer-events: none }}

  /* точечные */
  .map::before  {{ background-image: radial-gradient(circle, var(--pc) 1px, transparent 1px); background-size: 16px 16px }}
  .map--12::before {{ background-size: 12px 12px }}
  .map--22::before {{ background-image: radial-gradient(circle, var(--pc) 1.6px, transparent 1.7px); background-size: 22px 22px }}
  .dots::before {{ background-image: radial-gradient(var(--pc) 1.6px, transparent 1.7px); background-size: 16px 16px }}
  .checker::before {{ background-image: radial-gradient(var(--pc) 1.5px, transparent 1.6px),
                                        radial-gradient(var(--pc) 1.5px, transparent 1.6px);
                     background-size: 20px 20px, 20px 20px; background-position: 0 0, 10px 10px }}
  .fade::before {{ -webkit-mask-image: linear-gradient(transparent 16%, #000 76%);
                  mask-image: linear-gradient(transparent 16%, #000 76%) }}

  /* линейные — без маски */
  .diag::before {{ background-image: repeating-linear-gradient(45deg, var(--pc) 0 1.6px, transparent 1.6px 10px) }}
  .diagW::before {{ background-image: repeating-linear-gradient(45deg, var(--pc) 0 6px, transparent 6px 22px); opacity: .75 }}
  .grid::before {{ background-image: linear-gradient(var(--pc) 1.2px, transparent 1.2px),
                                     linear-gradient(90deg, var(--pc) 1.2px, transparent 1.2px);
                  background-size: 18px 18px }}
  .graph::before {{ background-image: linear-gradient(var(--pc) 1.4px, transparent 1.4px),
                                      linear-gradient(90deg, var(--pc) 1.4px, transparent 1.4px),
                                      linear-gradient(var(--pc) .8px, transparent .8px),
                                      linear-gradient(90deg, var(--pc) .8px, transparent .8px);
                   background-size: 30px 30px, 30px 30px, 6px 6px, 6px 6px }}

  /* маска + svg */
  .plus::before    {{ {mask(S("M10 6v8M6 10h8"), (20, 20))} }}
  .plusL::before   {{ {mask(S("M15 9v12M9 15h12", 2), (30, 30))} }}
  .cross::before   {{ {mask(S("M6 6l8 8M14 6l-8 8"), (20, 20))} }}
  .diamond::before {{ {mask("%3Cpath d='M11 3l8 8-8 8-8-8z' stroke='%23000' stroke-width='1.6' fill='none'/%3E", (22, 22))} }}
  .square::before  {{ {mask("%3Crect x='6' y='6' width='7' height='7' rx='1.5' fill='%23000'/%3E", (18, 18))} }}
  .chev::before    {{ {mask(S("M2 13l7-6 7 6"), (18, 16))} }}
  .wave::before    {{ {mask(S("M0 11q6 -7 12 0t12 0"), (24, 16))} }}
  .ring::before    {{ {mask("%3Ccircle cx='11' cy='11' r='4.5' stroke='%23000' stroke-width='1.5' fill='none'/%3E", (22, 22))} }}
  .dash::before    {{ {mask(S("M4 14l7-7"), (18, 18))} }}
  .spark::before   {{ {mask("%3Cpath d='M10 4c.6 3.6 1.8 4.8 5.4 5.4-3.6.6-4.8 1.8-5.4 5.4-.6-3.6-1.8-4.8-5.4-5.4C8.2 8.8 9.4 7.6 10 4z' fill='%23000'/%3E", (22, 22))} }}
  .hex::before     {{ {mask("%3Cpath d='M7 2l6 0 3 5-3 5-6 0-3-5z' stroke='%23000' stroke-width='1.4' fill='none'/%3E", (20, 20))} }}
</style>
'''

HEAD = '''<title>Категории · паттерны</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Паттерны на P9</h1>
    <p class="text-caption-14">Заливка везде одна — градиент в три стопа из P9. Меняется только паттерн. Первые четыре — тот самый рисунок с карты уроков.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение. Плотность и прозрачность любого паттерна легко подкрутить.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for x in BUF if x.strip().startswith("<section")))
