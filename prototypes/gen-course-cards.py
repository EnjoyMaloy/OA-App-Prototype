# Генератор черновика: 100 вариантов карточки курса
import json
OUT = '/home/user/OA-App-Prototype/prototypes/course-cards.html'
IMGS = json.load(open('/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/imgs.json'))

C = [
 dict(k="rocket",   t="Основы Web3 и DeFi",       cat="Web3 и DeFi",    r=4.9, s=371,   bg="linear-gradient(135deg,#E8DCFB,#A66CFF)", a="#A66CFF", tag="new",     price=0,  old=None, lessons=12, hours="4 ч",  lvl="Начальный", prog=0),
 dict(k="coin",     t="Инвестиции с нуля",        cat="Инвестиции",     r=4.9, s=35419, bg="linear-gradient(135deg,#FFF1CC,#F5B02E)", a="#F5B02E", tag="trend",   price=49, old=79,   lessons=18, hours="6 ч",  lvl="Средний",   prog=61),
 dict(k="nft",      t="Криптовалюты: первый шаг", cat="Основы крипты",  r=4.7, s=1024,  bg="linear-gradient(135deg,#FFDFD1,#FF7D60)", a="#FF7D60", tag="premium", price=49, old=None, lessons=9,  hours="3 ч",  lvl="Начальный", prog=100),
 dict(k="security", t="Безопасность кошелька",    cat="Безопасность",   r=4.6, s=512,   bg="linear-gradient(135deg,#FFD6EC,#EE49A4)", a="#EE49A4", tag="premium", price=79, old=None, lessons=7,  hours="2 ч",  lvl="Продвинутый", prog=35),
]
def nfmt(n): return f"{n:,}".replace(",", " ")

BUF = []
def fam(t): BUF.append(f'  <h2 class="fam">{t}</h2>\n')
def block(code, title, cap, body):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
{body}
  </section>
''')
def rail(fn, n=3, cls="rail"):
    return f'    <div class="{cls}">\n' + "\n".join("      " + fn(i, C[i]) for i in range(n)) + "\n    </div>"

# ---------- кирпичики ----------
def cov(c, cls="", inner="", objcls=""):
    return (f'<span class="cov {cls}" style="background:{c["bg"]}">'
            f'<span class="obj im-{c["k"]} {objcls}"></span>{inner}</span>')

STAR = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 1L8.854 4.756L13 5.362L10 8.284L10.708 12.412L7 10.468L3.292 12.412L4 8.284L1 5.362L5.146 4.756L7 1Z" fill="#FF7D60"/></svg>'
USERS = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/></svg>'
GRID = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>'
BOOK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>'
CLOCK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
MARK = '<svg width="13" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>'
LOCK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>'
CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>'
PSTAR = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l2.4 6.2L21 9.3l-4.6 4.3 1.2 6.4-5.6-3.1-5.6 3.1 1.2-6.4L3 9.3l6.6-1.1z"/></svg>'
FIRE = '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c1 3.5-1.5 4.5-2.5 6.5C8.3 10.9 9 13 11 13c1.6 0 2-1.3 1.8-2.6 2 1.4 3.2 3.2 3.2 5.1 0 3-2.5 5.5-5.5 5.5S5 18.5 5 15.5c0-4.5 5.5-6.5 7-13.5z"/></svg>'

def badge_prem():  return f'<span class="bdg bdg--prem">{PSTAR} Премиум</span>'
def badge_trend(): return f'<span class="bdg bdg--prem">{FIRE} В тренде</span>'
def badge_new():   return '<span class="bdg bdg--new">Новое</span>'
def badges(c):
    return {"new": badge_new(), "premium": badge_prem(), "trend": badge_trend()}[c["tag"]]
def topbar(c, right=""):
    return f'<span class="top"><span class="top__l">{badges(c)}</span>{right}</span>'
def bmark(): return f'<span class="bm">{MARK}</span>'

def chip(c):       return f'<span class="chip">{GRID}<span>{c["cat"]}</span></span>'
def chip_soft(c):  return f'<span class="chip chip--soft" style="background:color-mix(in srgb,{c["a"]} 14%,#fff);color:{c["a"]}">{c["cat"]}</span>'
def chip_caps(c):  return f'<span class="caps" style="color:{c["a"]}">{c["cat"]}</span>'
def title(c, cls=""): return f'<span class="ttl {cls}">{c["t"]}</span>'
def meta(c):
    return (f'<span class="meta"><span class="rate">{STAR}{c["r"]}</span>'
            f'<span class="pill">{USERS}{nfmt(c["s"])}</span></span>')
def meta_dot(c):   return f'<span class="meta meta--plain">★ {c["r"]} · {nfmt(c["s"])} учеников</span>'
def meta_rate(c):  return f'<span class="meta"><span class="rate">{STAR}{c["r"]}</span></span>'
def meta_les(c):   return f'<span class="meta meta--icons">{BOOK} {c["lessons"]} уроков <i></i> {CLOCK} {c["hours"]}</span>'
def meta_lvl(c):   return f'<span class="meta"><span class="pill">{c["lvl"]}</span><span class="pill">{c["hours"]}</span></span>'
def meta_av(c):
    dots = "".join(f'<i style="background:{x}"></i>' for x in ("#A66CFF", "#FF8645", "#88C5FD"))
    return f'<span class="meta"><span class="avs">{dots}</span><span class="muted">{nfmt(c["s"])} учатся</span></span>'
def meta_pill(c):  return f'<span class="meta"><span class="pill pill--wide">{STAR}{c["r"]}<i class="sep"></i>{USERS}{nfmt(c["s"])}</span></span>'
def meta_prog(c):
    return (f'<span class="meta meta--col"><span class="bar"><i style="width:{c["prog"]}%;background:{c["a"]}"></i></span>'
            f'<span class="muted">{c["prog"]}% пройдено</span></span>')
def price(c, kind="row"):
    p = "Бесплатно" if c["price"] == 0 else f'{c["price"]} $'
    if kind == "row":   return f'<span class="price">{p}</span>'
    if kind == "big":   return f'<span class="price price--big">{p}</span>'
    if kind == "old":   return f'<span class="price">{p} <s>{c["old"] or 99} $</s></span>'
    if kind == "free":  return f'<span class="price" style="color:#1BB07A">{p}</span>'
    if kind == "sub":   return '<span class="chip chip--soft" style="background:#EDE4FF;color:#7B2EFF">В подписке</span>'
    if kind == "btn":   return f'<button class="btn">Купить за {p}</button>'
    if kind == "btn2":  return f'<span class="row-end"><span class="price">{p}</span><button class="btn btn--sm">Купить</button></span>'
    if kind == "cont":  return f'<button class="btn btn--ghost">{CHECK} Продолжить</button>'
    return ""

def card(c, parts, cover_cls="", cover_inner="", objcls="", wrap="", style=""):
    return (f'<article class="c {wrap}" style="{style}">{cov(c, cover_cls, cover_inner, objcls)}'
            f'<span class="body">{"".join(parts)}</span></article>')

STD = lambda c, **kw: card(c, [chip(c), title(c), meta(c)], **kw)

# =====================================================================
fam("A. Компоновка")
block("A1", "Как сейчас", "Обложка, чип категории, заголовок, рейтинг и ученики.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c, bmark()))))
block("A2", "Метрики сверху", "Рейтинг поднят над заголовком — цифры считываются первыми.",
 rail(lambda i, c: card(c, [meta(c), title(c), chip(c)], cover_inner=topbar(c))))
block("A3", "Категория на обложке", "Чип переехал на картинку — текстовый блок стал короче.",
 rail(lambda i, c: card(c, [title(c), meta(c)], cover_inner=f'<span class="top"><span class="top__l">{chip(c)}</span>{badges(c)}</span>')))
block("A4", "Заголовок на обложке", "Название лежит на затемнении внизу картинки.",
 rail(lambda i, c: card(c, [meta(c)], cover_cls="cov--dark", cover_inner=f'{topbar(c)}<span class="onttl">{c["t"]}</span>')))
block("A5", "Горизонтальная", "Обложка слева, текст справа — экономит вертикаль.",
 rail(lambda i, c: f'<article class="h">{cov(c, "cov--sq")}<span class="body">{chip(c)}{title(c, "ttl--sm")}{meta_dot(c)}</span></article>', cls="list"))
block("A6", "Горизонтальная крупная", "Обложка 120px, три строки текста.",
 rail(lambda i, c: f'<article class="h h--lg">{cov(c, "cov--sq")}<span class="body">{chip(c)}{title(c)}{meta(c)}</span></article>', cls="list"))
block("A7", "Компактная строка", "Мини-обложка и заголовок в одну строку.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body"><span class="ttl ttl--sm">{c["t"]}</span>{meta_dot(c)}</span></article>', cls="list"))
block("A8", "Квадратная обложка", "1:1 вместо 16:9 — картинка крупнее.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_cls="cov--sq1", cover_inner=topbar(c))))
block("A9", "Постер 3:4", "Вертикальная обложка, текст под ней.",
 rail(lambda i, c: card(c, [title(c), meta(c)], cover_cls="cov--tall", cover_inner=topbar(c), wrap="c--narrow")))
def poster(c):
    inner = topbar(c) + ('<span class="onbody"><span class="onttl">' + c["t"] + '</span>'
                         '<span class="onmeta">★ ' + str(c["r"]) + ' · ' + nfmt(c["s"]) + '</span></span>')
    return '<article class="c c--narrow">' + cov(c, "cov--tall cov--dark", inner) + '</article>'
block("A10", "Всё на обложке", "Карточка-постер: текст и метрики поверх картинки.",
 rail(lambda i, c: poster(c)))

# =====================================================================
fam("B. Обложка")
for code, t, cap, cc, oc in [
 ("B1", "Скругление 10", "Как сейчас.", "", ""),
 ("B2", "Скругление 16", "Мягче, ближе к скруглению карточек категорий.", "cov--r16", ""),
 ("B3", "Скругление 24", "Совсем округлая обложка.", "cov--r24", ""),
 ("B4", "Без скругления", "Острые углы — строгая витрина.", "cov--r0", ""),
 ("B5", "Объект крупнее", "3D-объект почти во всю обложку.", "", "obj--lg"),
 ("B6", "Объект мельче", "Больше воздуха вокруг объекта.", "", "obj--sm"),
 ("B7", "Внутренняя рамка", "Белый кант по краю обложки.", "cov--hair", ""),
 ("B8", "Тень под объектом", "Объект отрывается от подложки.", "", "obj--shadow"),
 ("B9", "Точки на обложке", "Та же текстура, что на плитках категорий.", "cov--dots", ""),
 ("B10", "Глянец", "Диагональный блик поверх градиента.", "cov--gloss", ""),
]:
    block(code, t, cap, rail(lambda i, c, cc=cc, oc=oc: card(c, [chip(c), title(c), meta(c)], cover_cls=cc, objcls=oc, cover_inner=topbar(c))))

# =====================================================================
fam("C. Бейджи")
block("C1", "Как сейчас", "Премиум и «В тренде» пилюлей слева сверху.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c))))
block("C2", "Только иконка", "Премиум сжат до кружка со звездой.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="ic-bdg">{PSTAR}</span></span>')))
block("C3", "Цветной «Новое»", "Бейдж в цвете категории.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="bdg" style="background:{c["a"]};color:#fff;border:0">Новое</span></span>')))
block("C4", "Снизу слева", "Бейдж прижат к нижнему краю обложки.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="bot"><span class="top__l">{badges(c)}</span></span>')))
block("C5", "На стыке", "Бейдж наполовину выходит за обложку.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_cls="cov--ovf", cover_inner=f'<span class="hang">{badges(c)}</span>')))
block("C6", "Уголок", "Диагональная лента в углу.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="corner" style="background:{c["a"]}">NEW</span>')))
block("C7", "Огонёк", "«В тренде» с иконкой пламени на всех.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="bdg bdg--fire">{FIRE} В тренде</span></span>')))
block("C8", "Цена бейджем", "Стоимость прямо на обложке.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="top__l">{badges(c)}</span><span class="bdg bdg--price">{"Бесплатно" if c["price"]==0 else str(c["price"])+" $"}</span></span>')))
block("C9", "Точка-маркер", "Минимальная метка: цветной кружок.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><i class="dotb" style="background:{c["a"]}"></i></span>')))
block("C10", "Без бейджей", "Чистая обложка, вся служебная информация в тексте.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)])))

# =====================================================================
fam("D. Метрики")
for code, t, cap, fn in [
 ("D1", "Звезда и ученики", "Как сейчас.", meta),
 ("D2", "Только рейтинг", "Минимум цифр.", meta_rate),
 ("D3", "Через точку", "Метрики строкой без плашек.", meta_dot),
 ("D4", "Аватары", "Кто уже учится — социальное доказательство.", meta_av),
 ("D5", "Уроки и часы", "Объём курса вместо популярности.", meta_les),
 ("D6", "Уровень", "Сложность и длительность чипами.", meta_lvl),
 ("D7", "Прогресс", "Для начатых курсов — полоска прохождения.", meta_prog),
 ("D8", "Одной пилюлей", "Рейтинг и ученики в общей плашке.", meta_pill),
]:
    block(code, t, cap, rail(lambda i, c, fn=fn: card(c, [chip(c), title(c), fn(c)], cover_inner=topbar(c))))
block("D9", "Метрики на обложке", "Рейтинг лежит на картинке.",
 rail(lambda i, c: card(c, [chip(c), title(c)], cover_inner=f'{topbar(c)}<span class="bot"><span class="bdg bdg--price">{STAR} {c["r"]}</span></span>')))
block("D10", "Серым мелким", "Без иконок и плашек — самая тихая подача.",
 rail(lambda i, c: card(c, [chip(c), title(c), f'<span class="muted sm">{c["r"]} · {nfmt(c["s"])} учеников · {c["lessons"]} уроков</span>'], cover_inner=topbar(c))))

# =====================================================================
fam("E. Цена и действие")
for code, t, cap, kind in [
 ("E1", "Цена в строке метрик", "Стоимость справа от рейтинга.", "row"),
 ("E2", "Цена крупно", "Отдельной строкой, 20px.", "big"),
 ("E3", "Со скидкой", "Старая цена зачёркнута.", "old"),
 ("E4", "Кнопка на всю ширину", "Прямое действие в карточке.", "btn"),
 ("E5", "Цена и кнопка", "Стоимость слева, кнопка справа.", "btn2"),
 ("E6", "Бесплатно зелёным", "Акцент на бесплатных курсах.", "free"),
 ("E7", "В подписке", "Фиолетовый чип вместо цены.", "sub"),
 ("E9", "Куплено", "Кнопка «Продолжить» для своих курсов.", "cont"),
]:
    block(code, t, cap, rail(lambda i, c, kind=kind: card(c, [chip(c), title(c), meta(c), price(c, kind)], cover_inner=topbar(c))))
block("E8", "Цена на обложке", "Ценник как на витрине.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'{topbar(c)}<span class="bot bot--r"><span class="bdg bdg--price">{"Бесплатно" if c["price"]==0 else str(c["price"])+" $"}</span></span>')))
block("E10", "Без цены", "Карточка только про содержание.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c))))

# =====================================================================
fam("F. Контейнер")
for code, t, cap, wrap, style in [
 ("F1", "Без фона", "Как сейчас — карточка живёт на фоне экрана.", "", ""),
 ("F2", "Белая с тенью", "Карточка приподнята над фоном.", "c--box c--shadow", ""),
 ("F3", "С рамкой", "Тонкий контур вместо тени.", "c--box c--border", ""),
 ("F4", "На сером", "Подложка из muted.", "c--box c--muted", ""),
 ("F5", "В цвете категории", "Фон карточки — светлый оттенок обложки.", "c--box", "background:color-mix(in srgb,var(--a) 10%,#fff)"),
 ("F6", "Градиентная", "Заливка светлеет книзу.", "c--box", "background:linear-gradient(180deg,color-mix(in srgb,var(--a) 16%,#fff),#fff)"),
 ("F7", "Скругление 20", "Крупное скругление всей карточки.", "c--box c--shadow c--r20", ""),
 ("F8", "Цветная тень", "Тень в тон обложке.", "c--box", "box-shadow:0 14px 28px color-mix(in srgb,var(--a) 30%,transparent)"),
 ("F9", "Тёмная", "Графитовая карточка, белый текст.", "c--box c--dark", ""),
 ("F10", "Стеклянная", "Полупрозрачная карточка на цветном фоне.", "c--box c--glass", ""),
]:
    body = lambda i, c, wrap=wrap, style=style: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c), wrap=wrap, style=f'--a:{c["a"]};{style}')
    block(code, t, cap, (f'    <div class="bedgrad">\n' + rail(body) + '\n    </div>') if code == "F10" else rail(body))

# =====================================================================
fam("G. Типографика")
block("G1", "Как сейчас", "Заголовок 18/600, две строки максимум.", rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c))))
block("G2", "Крупный заголовок", "20px bold — карточка звучит громче.", rail(lambda i, c: card(c, [chip(c), title(c, "ttl--lg"), meta(c)], cover_inner=topbar(c))))
block("G3", "Мелкий заголовок", "16px medium — плотнее.", rail(lambda i, c: card(c, [chip(c), title(c, "ttl--sm"), meta(c)], cover_inner=topbar(c))))
block("G4", "В одну строку", "Длинные названия обрезаются многоточием.", rail(lambda i, c: card(c, [chip(c), title(c, "ttl--one"), meta(c)], cover_inner=topbar(c))))
block("G5", "С описанием", "Под заголовком — две строки пояснения.", rail(lambda i, c: card(c, [chip(c), title(c), '<span class="desc">Разбираем на практике, шаг за шагом, с примерами и домашками.</span>', meta(c)], cover_inner=topbar(c))))
block("G6", "Категория капсом", "Вместо чипа — мелкая рубрика.", rail(lambda i, c: card(c, [chip_caps(c), title(c), meta(c)], cover_inner=topbar(c))))
block("G7", "Категория цветным чипом", "Чип в цвете обложки.", rail(lambda i, c: card(c, [chip_soft(c), title(c), meta(c)], cover_inner=topbar(c))))
block("G8", "Заголовок первым", "Название выше категории.", rail(lambda i, c: card(c, [title(c), chip(c), meta(c)], cover_inner=topbar(c))))
block("G9", "По центру", "Весь текст выровнен по центру.", rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=topbar(c), wrap="c--center")))
block("G10", "С автором", "Строка «Ведёт …» под заголовком.", rail(lambda i, c: card(c, [chip(c), title(c), '<span class="muted sm">Ведёт Павел Сычёв</span>', meta(c)], cover_inner=topbar(c))))

# =====================================================================
fam("H. Списки и сетки")
block("H1", "Строка списка", "Обложка 64, заголовок, метрики.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}{meta_dot(c)}</span></article>', n=4, cls="list"))
block("H2", "Строка с шевроном", "Явный переход дальше.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}{meta_dot(c)}</span><span class="chev">›</span></article>', n=4, cls="list"))
block("H3", "Строка с кнопкой", "Действие прямо в списке.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}<span class="muted sm">{c["lessons"]} уроков · {c["hours"]}</span></span><button class="btn btn--sm">Открыть</button></article>', n=4, cls="list"))
block("H4", "Строка с прогрессом", "Формат «Мои курсы».",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}{meta_prog(c)}</span></article>', n=4, cls="list"))
block("H5", "Сетка 2×", "Мелкие карточки без скролла.",
 rail(lambda i, c: card(c, [title(c, "ttl--sm"), meta_dot(c)], cover_inner=topbar(c), wrap="c--grid"), n=4, cls="grid2"))
block("H6", "Сетка 2× квадратами", "Квадратная обложка в сетке.",
 rail(lambda i, c: card(c, [title(c, "ttl--sm"), meta_rate(c)], cover_cls="cov--sq1", wrap="c--grid"), n=4, cls="grid2"))
block("H7", "Нумерованный топ", "Позиция в подборке слева.",
 rail(lambda i, c: f'<article class="h h--sm"><span class="num">{i+1}</span>{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}{meta_dot(c)}</span></article>', n=4, cls="list"))
block("H8", "Строка-таблица", "Название слева, цена справа.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}<span class="muted sm">{c["cat"]}</span></span>{price(c)}</article>', n=4, cls="list"))
block("H9", "Без обложки", "Только иконка категории и текст.",
 rail(lambda i, c: f'<article class="h h--sm"><span class="sq" style="background:color-mix(in srgb,{c["a"]} 16%,#fff);color:{c["a"]}">{GRID}</span><span class="body">{title(c, "ttl--sm")}{meta_dot(c)}</span></article>', n=4, cls="list"))
block("H10", "С закладкой", "Избранное прямо в строке.",
 rail(lambda i, c: f'<article class="h h--sm">{cov(c, "cov--mini")}<span class="body">{title(c, "ttl--sm")}{meta_dot(c)}</span><span class="bm bm--st">{MARK}</span></article>', n=4, cls="list"))

# =====================================================================
fam("I. Состояния")
block("I1", "Куплено", "Галочка и контур в цвете категории.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="bdg bdg--ok">{CHECK} Куплено</span></span>', wrap="c--box c--own", style=f'--a:{c["a"]}')))
block("I2", "Под замком", "Курс доступен по подписке.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_cls="cov--lock", cover_inner=f'{topbar(c)}<span class="lock">{LOCK}</span>')))
block("I3", "Скоро", "Заглушка для будущих курсов.",
 rail(lambda i, c: card(c, [chip(c), title(c), '<span class="muted sm">Запуск в сентябре</span>'], cover_cls="cov--soon", cover_inner='<span class="top"><span class="bdg">Скоро</span></span>', wrap="c--dim")))
block("I4", "В процессе", "Прогресс полоской поверх обложки.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'{topbar(c)}<span class="ovbar"><i style="width:{c["prog"]}%;background:{c["a"]}"></i></span>')))
block("I5", "Завершён", "Курс пройден полностью.",
 rail(lambda i, c: card(c, [chip(c), title(c), '<span class="muted sm">Курс пройден · сертификат получен</span>'], cover_inner=f'<span class="top"><span class="bdg bdg--ok">{CHECK} 100%</span></span>')))
block("I6", "Новинка точкой", "Яркая точка вместо бейджа.",
 rail(lambda i, c: card(c, [f'<span class="row-start">{chip(c)}<i class="dotb dotb--sm" style="background:{c["a"]}"></i></span>', title(c), meta(c)])))
block("I7", "Скидка", "Процент скидки и старая цена.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c), price(c, "old")], cover_inner=f'<span class="top"><span class="bdg bdg--sale">−40%</span></span>')))
block("I8", "Рекомендуем", "Выделенная подборкой карточка.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="bdg bdg--prem">{PSTAR} Выбор редакции</span></span>', wrap="c--box c--own", style=f'--a:{c["a"]}')))
block("I9", "В избранном", "Активная закладка на обложке.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_inner=f'<span class="top"><span class="top__l">{badges(c)}</span><span class="bm bm--on">{MARK}</span></span>')))
block("I10", "В архиве", "Приглушённая карточка.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], wrap="c--dim")))

# =====================================================================
fam("J. Брендбук")
PAIRS = [("#A66CFF", "#FF8645"), ("#FF96C8", "#FFDD31"), ("#88C5FD", "#CCEF40"), ("#A66CFF", "#88C5FD")]
def brand(i, c, g, cc="", inner=None, objcls=""):
    inner = topbar(c) if inner is None else inner
    return (f'<article class="c"><span class="cov {cc}" style="background:{g}">'
            f'<span class="obj im-{c["k"]} {objcls}"></span>{inner}</span>'
            f'<span class="body">{chip(c)}{title(c)}{meta(c)}</span></article>')
block("J1", "Purple + Orange", "Первая пара брендбука на всех обложках.",
 rail(lambda i, c: brand(i, c, "linear-gradient(135deg,#A66CFF,#FF8645)")))
block("J2", "Pink + Yellow", "Вторая пара.", rail(lambda i, c: brand(i, c, "linear-gradient(135deg,#FF96C8,#FFDD31)")))
block("J3", "Blue + Lime", "Третья пара.", rail(lambda i, c: brand(i, c, "linear-gradient(135deg,#88C5FD,#CCEF40)")))
block("J4", "Своя пара каждой", "Обложки чередуют бренд-градиенты.",
 rail(lambda i, c: brand(i, c, f'linear-gradient(135deg,{PAIRS[i % 4][0]},{PAIRS[i % 4][1]})')))
block("J5", "Точки на обложке", "Паттерн с карты уроков поверх градиента.",
 rail(lambda i, c: brand(i, c, c["bg"], "cov--dots2")))
block("J6", "Диагонали", "Полосы из брендбука.", rail(lambda i, c: brand(i, c, c["bg"], "cov--diag")))
block("J7", "Знак «А»", "Фирменная буква водяным знаком.", rail(lambda i, c: brand(i, c, c["bg"], "cov--letter")))
block("J8", "Цветная кайма", "Полоса категории слева от текста.",
 rail(lambda i, c: card(c, [f'<span class="edge" style="border-color:{c["a"]}">{chip(c)}{title(c)}{meta(c)}</span>'], cover_inner=topbar(c))))
block("J9", "Полароид", "Белая рамка вокруг обложки.",
 rail(lambda i, c: card(c, [chip(c), title(c), meta(c)], cover_cls="cov--polaroid", cover_inner=topbar(c))))
block("J10", "Номер курса", "Крупная цифра на обложке — как в серии.",
 rail(lambda i, c: brand(i, c, c["bg"], "cov--num", inner=f'{topbar(c)}<span class="bignum">{i+1:02d}</span>')))

IMGCSS = "\n".join(f'  .im-{k} {{ background-image: url({v}) }}' for k, v in IMGS.items())

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .fam { font-size: 24px; font-weight: 600; margin: 16px 0 0; letter-spacing: -.01em }
  button { font: inherit; border: 0; cursor: pointer; background: none }

  .list { display: flex; flex-direction: column; gap: 10px }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px }

  /* карточка */
  .c { display: flex; flex-direction: column; gap: 10px; width: 262px; flex: 0 0 auto; cursor: pointer }
  .c--narrow { width: 190px }
  .c--grid { width: auto }
  .c--box { padding: 10px; border-radius: 16px; background: #fff }
  .c--shadow { box-shadow: 0 8px 22px rgba(32,32,32,.10) }
  .c--border { border: 1px solid hsl(var(--border)) }
  .c--muted { background: hsl(var(--muted)) }
  .c--r20 { border-radius: 22px }
  .c--dark { background: #202020 }
  .c--dark .ttl, .c--dark .rate { color: #fff }
  .c--dark .chip, .c--dark .pill { background: rgba(255,255,255,.12); color: #fff }
  .c--glass { background: rgba(255,255,255,.6); backdrop-filter: blur(16px) saturate(1.3); border: 1px solid rgba(255,255,255,.7) }
  .c--own { box-shadow: 0 0 0 2px var(--a) }
  .c--center { text-align: center; align-items: center }
  .c--dim { opacity: .5 }
  .bedgrad { background: linear-gradient(120deg,#A66CFF,#FF8645); padding: 14px 0; border-radius: 16px; margin: 0 -16px }
  .bedgrad .rail { padding: 0 14px }

  .body { display: flex; flex-direction: column; gap: 8px; min-width: 0 }

  /* обложка */
  .cov { position: relative; display: block; width: 100%; aspect-ratio: 328/181; border-radius: 10px; overflow: hidden }
  .cov--r16 { border-radius: 16px } .cov--r24 { border-radius: 24px } .cov--r0 { border-radius: 0 }
  .cov--sq1 { aspect-ratio: 1 } .cov--tall { aspect-ratio: 3/4 }
  .cov--sq { width: 96px; aspect-ratio: 1; flex: 0 0 auto }
  .cov--mini { width: 64px; aspect-ratio: 1; flex: 0 0 auto; border-radius: 12px }
  .cov--hair { box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.7) }
  .cov--ovf { overflow: visible }
  .cov--polaroid { border: 8px solid #fff; box-shadow: 0 6px 16px rgba(32,32,32,.14); border-radius: 6px }
  .obj { position: absolute; inset: 14px; background: center/contain no-repeat }
  .obj--lg { inset: 4px } .obj--sm { inset: 26px }
  .obj--shadow { filter: drop-shadow(0 10px 12px rgba(32,32,32,.28)) }
  .cov--dark::after, .cov--lock::after, .cov--soon::after { content: ''; position: absolute; inset: 0 }
  .cov--dark::after { background: linear-gradient(180deg, transparent 40%, rgba(0,0,0,.72) 100%) }
  .cov--lock::after { background: rgba(20,10,40,.42) }
  .cov--soon::after { background: rgba(255,255,255,.55) }
  .cov--dots::before, .cov--dots2::before { content: ''; position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,255,255,.55) 1.5px, transparent 1.6px); background-size: 14px 14px }
  .cov--gloss::before { content: ''; position: absolute; inset: 0;
    background: linear-gradient(118deg, rgba(255,255,255,.6) 0%, rgba(255,255,255,0) 46%) }
  .cov--diag::before { content: ''; position: absolute; inset: 0;
    background-image: repeating-linear-gradient(45deg, rgba(255,255,255,.35) 0 4px, transparent 4px 14px) }
  .cov--letter::before { content: 'A'; position: absolute; right: -6px; top: -26px; font-size: 130px; font-weight: 900;
    color: rgba(255,255,255,.34); line-height: 1 }
  .bignum { position: absolute; right: 10px; bottom: 2px; font-size: 56px; font-weight: 900; color: rgba(255,255,255,.5); line-height: 1 }

  /* бейджи поверх обложки */
  .top, .bot { position: absolute; left: 8px; right: 8px; display: flex; align-items: center; justify-content: space-between; gap: 6px }
  .top { top: 8px } .bot { bottom: 8px } .bot--r { justify-content: flex-end }
  .top__l { display: flex; gap: 5px }
  .bdg { display: inline-flex; align-items: center; gap: 4px; padding: 5px 9px; border-radius: 999px;
    background: linear-gradient(0deg, rgba(217,192,255,.5), rgba(217,192,255,.5)), #fff;
    border: 1px solid rgba(146,76,254,.1); font-size: 12px; font-weight: 500; color: #460466; white-space: nowrap }
  .bdg--new { background: #fff; color: #202020 }
  .bdg--fire { background: #fff; color: #FF5C1A; border-color: rgba(255,92,26,.2) }
  .bdg--price { background: rgba(255,255,255,.92); color: #202020; border: 0; font-weight: 600 }
  .bdg--ok { background: #E7F8F0; color: #12805B; border: 0 }
  .bdg--sale { background: #FF5C1A; color: #fff; border: 0; font-weight: 600 }
  .ic-bdg { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px;
    border-radius: 999px; background: #fff; color: #7B2EFF }
  .dotb { width: 12px; height: 12px; border-radius: 999px; display: inline-block }
  .dotb--sm { width: 8px; height: 8px }
  .bm { display: inline-flex; align-items: center; justify-content: center; width: 32px; height: 32px;
    border-radius: 999px; background: #fff; color: #202020; flex: 0 0 auto }
  .bm--on { color: #7B2EFF }
  .bm--st { background: hsl(var(--muted)) }
  .hang { position: absolute; left: 10px; bottom: -12px }
  .corner { position: absolute; right: -26px; top: 12px; transform: rotate(45deg); width: 96px; text-align: center;
    color: #fff; font-size: 11px; font-weight: 700; padding: 4px 0; letter-spacing: .06em }
  .lock { z-index: 1; position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); color: #fff }
  .ovbar { z-index: 1; position: absolute; left: 0; right: 0; bottom: 0; height: 5px; background: rgba(255,255,255,.5) }
  .ovbar i { display: block; height: 100% }
  .onttl { position: relative; color: #fff; font-size: 17px; font-weight: 600; line-height: 1.2 }
  .onbody { position: absolute; left: 12px; right: 12px; bottom: 12px; display: flex; flex-direction: column; gap: 4px }
  .cov--dark > .onttl { position: absolute; left: 12px; right: 12px; bottom: 12px }
  .onmeta { color: rgba(255,255,255,.85); font-size: 13px }

  /* текст */
  .chip { display: inline-flex; align-items: center; gap: 6px; padding: 5px 8px; border-radius: 6px;
    background: hsl(var(--muted)); color: hsl(0 0% 27.5%); font-size: 14px; width: fit-content }
  .chip--soft { padding: 5px 10px; border-radius: 999px; font-weight: 500; font-size: 13px }
  .caps { font-size: 12px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase }
  .ttl { font-size: 18px; font-weight: 600; line-height: 1.25; color: #000; display: -webkit-box;
    -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden }
  .ttl--lg { font-size: 20px; font-weight: 700 }
  .ttl--sm { font-size: 16px; font-weight: 500 }
  .ttl--one { -webkit-line-clamp: 1 }
  .desc { font-size: 13px; line-height: 1.35; color: rgba(32,32,32,.55) }
  .muted { color: rgba(32,32,32,.5); font-size: 14px }
  .sm { font-size: 13px }

  .meta { display: flex; align-items: center; gap: 6px; font-size: 14px }
  .meta--plain { color: rgba(32,32,32,.5) }
  .meta--icons { color: rgba(32,32,32,.55); gap: 5px }
  .meta--icons i { width: 3px; height: 3px; border-radius: 999px; background: currentColor; display: inline-block; margin: 0 3px }
  .meta--col { flex-direction: column; align-items: stretch; gap: 5px }
  .rate { display: inline-flex; align-items: center; gap: 4px }
  .pill { display: inline-flex; align-items: center; gap: 5px; padding: 3px 8px; border-radius: 999px;
    background: hsl(var(--muted)); color: hsl(0 0% 27.5%); font-size: 14px }
  .pill--wide { gap: 8px }
  .sep { width: 1px; height: 12px; background: rgba(32,32,32,.15) }
  .avs { display: flex }
  .avs i { width: 20px; height: 20px; border-radius: 999px; border: 2px solid #fff; margin-right: -8px }
  .bar { display: block; height: 5px; border-radius: 999px; background: rgba(32,32,32,.1); overflow: hidden }
  .bar i { display: block; height: 100% }

  .price { font-size: 16px; font-weight: 600; color: #202020 }
  .price--big { font-size: 20px; font-weight: 700 }
  .price s { color: rgba(32,32,32,.4); font-weight: 400; margin-left: 6px }
  .btn { height: 40px; border-radius: 999px; background: #202020; color: #fff; font-size: 15px; font-weight: 500; padding: 0 18px }
  .btn--sm { height: 34px; font-size: 14px; padding: 0 14px }
  .btn--ghost { background: hsl(var(--muted)); color: #202020; display: inline-flex; align-items: center; gap: 6px }
  .row-end { display: flex; align-items: center; justify-content: space-between; gap: 10px }
  .row-start { display: flex; align-items: center; gap: 8px }

  /* горизонтальные */
  .h { display: flex; align-items: center; gap: 12px; width: 100%; cursor: pointer }
  .h .body { flex: 1 }
  .h--lg .cov--sq { width: 120px }
  .h--sm .body { gap: 5px }
  .chev { font-size: 22px; color: rgba(32,32,32,.35) }
  .num { font-size: 20px; font-weight: 700; color: rgba(32,32,32,.25); width: 22px; text-align: center; flex: 0 0 auto }
  .sq { display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; border-radius: 12px; flex: 0 0 auto }
  .edge { display: flex; flex-direction: column; gap: 8px; border-left: 3px solid; padding-left: 10px }
</style>
'''

HEAD = '''<title>Карточки курсов · 100</title>
''' + CSS.replace('</style>', IMGCSS + '\n</style>') + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Карточки курсов · 100</h1>
    <p class="text-caption-14">Десять семейств: компоновка, обложка, бейджи, метрики, цена, контейнер, типографика, списки, состояния и брендбук. Ленты листаются вбок, как на главной.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — соберу в приложении. Можно смешивать: компоновка из одного, обложка из другого, метрики из третьего.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for x in BUF if x.strip().startswith("<section")))
