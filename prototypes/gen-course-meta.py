# 30 вариантов метаданных карточки: картинка, подложка и заголовок неизменны
import json
OUT = '/home/user/OA-App-Prototype/prototypes/course-meta.html'
IMGS = json.load(open('/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/imgs.json'))

C = [
 dict(k="rocket", t="Быстрый старт в Telegram Gifts", cat="Web3 и DeFi", r=4.9, s=406,
      bg="linear-gradient(135deg,#E8DCFB,#A66CFF)", a="#A66CFF", ago="2 дня назад", les=12),
 dict(k="coin", t="Инвестиции с нуля за шесть часов", cat="Инвестиции", r=4.9, s=35419,
      bg="linear-gradient(135deg,#FFF1CC,#F5B02E)", a="#F5B02E", ago="неделю назад", les=18),
 dict(k="nft", t="Криптовалюты: первый шаг", cat="Основы крипты", r=4.7, s=1024,
      bg="linear-gradient(135deg,#FFDFD1,#FF7D60)", a="#FF7D60", ago="месяц назад", les=9),
]
def nfmt(n): return f"{n:,}".replace(",", " ")

GRID = ('<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
        '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/>'
        '<rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>')
USERS = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" '
         'stroke-linecap="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/>'
         '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/></svg>')
HIST = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
        'stroke-linecap="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/><path d="M12 8v4l3 2"/></svg>')
STAR = ('<svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M7 1L8.854 4.756L13 5.362L10 8.284'
        'L10.708 12.412L7 10.468L3.292 12.412L4 8.284L1 5.362L5.146 4.756L7 1Z" fill="#FF7D60"/></svg>')
STARG = STAR.replace('#FF7D60', '#8A8A8A')

BUF = []
def block(code, name, cap, meta_fn, cover_fn=None):
    cards = []
    for c in C[:2]:
        inner = cover_fn(c) if cover_fn else ""
        cards.append(f'''      <article class="card">
        <span class="cov" style="background:{c["bg"]}"><span class="obj im-{c["k"]}"></span>{inner}</span>
        <span class="ttl">{c["t"]}</span>
        {meta_fn(c)}
      </article>''')
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
    <div class="rail">
{chr(10).join(cards)}
    </div>
  </section>
''')

# ---- кирпичики метаданных ----
def chip_cat(c, cls="chip"):   return f'<span class="{cls}">{GRID}<span>{c["cat"]}</span></span>'
def chip_users(c, cls="chip"): return f'<span class="{cls}">{USERS}<span>{nfmt(c["s"])}</span></span>'
def rate(c, g=False):          return f'<span class="rate">{STARG if g else STAR}{c["r"]}</span>'
def ago(c, cls="soft"):        return f'<span class="{cls}">{HIST}{c["ago"]}</span>'
def row(*p, cls="meta"):       return f'<span class="{cls}">' + "".join(p) + '</span>'

# =====================================================================
block("N1", "Как сейчас", "Белые чипы категории и учеников, звезда, дата обновления.",
      lambda c: row(chip_cat(c), rate(c), chip_users(c), ago(c)))
block("N2", "Только текст", "Никаких плашек: всё серой строкой через точку.",
      lambda c: f'<span class="plain">{c["cat"]} · {nfmt(c["s"])} учеников · {c["ago"]}</span>')
block("N3", "Категория чипом", "Плашка осталась только у категории, остальное — текст.",
      lambda c: row(chip_cat(c), f'<span class="plain">★ {c["r"]} · {nfmt(c["s"])} · {c["ago"]}</span>'))
block("N4", "Цвет категории в тексте", "Категория набрана своим цветом, метрики серые.",
      lambda c: f'<span class="plain"><b style="color:{c["a"]}">{c["cat"]}</b> · {nfmt(c["s"])} учеников · {c["ago"]}</span>')
block("N5", "Всё в одной плашке", "Один чип с разделителями внутри.",
      lambda c: row(f'<span class="chip chip--wide">{c["cat"]}<i class="sep"></i>★ {c["r"]}<i class="sep"></i>{nfmt(c["s"])}</span>'))
block("N6", "Метрики без иконок", "Серым мелким, только цифры.",
      lambda c: row(chip_cat(c), f'<span class="plain">{c["r"]} · {nfmt(c["s"])}</span>'))
block("N7", "Рубрика капсом", "Категория мелкими прописными над метриками.",
      lambda c: f'<span class="caps" style="color:{c["a"]}">{c["cat"]}</span>'
                f'<span class="plain">{nfmt(c["s"])} учеников · {c["ago"]}</span>')
block("N8", "Категория на обложке", "Чип уехал на картинку, снизу — только метрики.",
      lambda c: row(rate(c), chip_users(c), ago(c)),
      cover_fn=lambda c: f'<span class="onbl">{chip_cat(c, "chip chip--glass")}</span>')
block("N9", "Категория сверху на обложке", "Плашка в левом верхнем углу картинки.",
      lambda c: f'<span class="plain">★ {c["r"]} · {nfmt(c["s"])} учеников · {c["ago"]}</span>',
      cover_fn=lambda c: f'<span class="ontl">{chip_cat(c, "chip chip--glass")}</span>')
block("N10", "Обновление на обложке", "Дата в углу картинки, как длительность у ролика.",
      lambda c: row(chip_cat(c), rate(c), chip_users(c)),
      cover_fn=lambda c: f'<span class="onbr"><span class="dur">{c["ago"]}</span></span>')
block("N11", "Чипы с тенью", "Белые плашки чуть приподняты над подложкой.",
      lambda c: row(chip_cat(c, "chip chip--sh"), rate(c), chip_users(c, "chip chip--sh"), ago(c)))
block("N12", "Контурные чипы", "Прозрачный фон, тонкая обводка.",
      lambda c: row(chip_cat(c, "chip chip--out"), rate(c), chip_users(c, "chip chip--out"), ago(c)))
block("N13", "Чипы в цвете категории", "Мягкая заливка и цветной текст.",
      lambda c: row(f'<span class="chip" style="background:color-mix(in srgb,{c["a"]} 14%,#fff);color:{c["a"]}">{GRID}<span>{c["cat"]}</span></span>',
                    rate(c), chip_users(c), ago(c)))
block("N14", "Точка вместо иконки", "Цветной маркер категории, дальше серый текст.",
      lambda c: f'<span class="plain"><i class="dot" style="background:{c["a"]}"></i>{c["cat"]} · {nfmt(c["s"])} · {c["ago"]}</span>')
block("N15", "Категория цветным текстом", "Без плашки, но цвет сохраняется.",
      lambda c: row(f'<span class="cat-col" style="color:{c["a"]}">{c["cat"]}</span>', rate(c), chip_users(c)))
block("N16", "Акцент на рейтинге", "Рейтинг крупнее и в оранжевом, остальное тихо.",
      lambda c: row(f'<span class="rate rate--big">{STAR}{c["r"]}</span>',
                    f'<span class="plain">{c["cat"]} · {nfmt(c["s"])} учеников</span>'))
block("N17", "Акцент на учениках", "Число учеников крупное, остальное мелкое.",
      lambda c: f'<span class="big">{nfmt(c["s"])} <span class="big__u">учеников</span></span>'
                f'<span class="plain">{c["cat"]} · ★ {c["r"]} · {c["ago"]}</span>')
block("N18", "Свежесть первой", "Дата обновления идёт до категории.",
      lambda c: row(ago(c, "soft soft--first"), chip_cat(c), rate(c)))
block("N19", "Разделители-палочки", "Вертикальные линии вместо точек.",
      lambda c: f'<span class="plain">{c["cat"]}<i class="bar"></i>★ {c["r"]}<i class="bar"></i>{nfmt(c["s"])}<i class="bar"></i>{c["ago"]}</span>')
block("N20", "Только иконки и цифры", "Компактный ряд без слов.",
      lambda c: row(rate(c), f'<span class="ico">{USERS}{nfmt(c["s"])}</span>', f'<span class="ico">{HIST}{c["ago"]}</span>', cls="meta meta--tight"))
block("N21", "Две строки", "Категория и рейтинг сверху, ученики и дата снизу.",
      lambda c: row(chip_cat(c), rate(c)) + row(chip_users(c), ago(c)))
block("N22", "По краям", "Категория слева, рейтинг у правого края.",
      lambda c: f'<span class="meta meta--between">{chip_cat(c)}{rate(c)}</span>'
                f'<span class="plain">{nfmt(c["s"])} учеников · {c["ago"]}</span>')
block("N23", "Одна строка", "Минимум: всё в одну серую строку.",
      lambda c: f'<span class="plain one">{c["cat"]} · {nfmt(c["s"])} · {c["ago"]}</span>')
block("N24", "Категория и свежесть", "Без рейтинга и учеников.",
      lambda c: row(chip_cat(c), ago(c)))
block("N25", "Только рейтинг", "Одна цифра — максимум воздуха.",
      lambda c: row(rate(c)))
block("N26", "Без метрик", "Только превью и название — фокус на обложке.",
      lambda c: "")
block("N27", "Заметные чипы", "Плашки темнее и контрастнее подложки.",
      lambda c: row(chip_cat(c, "chip chip--dark"), rate(c), chip_users(c, "chip chip--dark"), ago(c)))
block("N28", "Незаметные метрики", "Текст 45% без иконок и плашек.",
      lambda c: f'<span class="ghost">{c["cat"]} · {nfmt(c["s"])} · {c["ago"]}</span>')
block("N29", "Плотно и мелко", "12px, минимальные отступы.",
      lambda c: row(chip_cat(c, "chip chip--xs"), f'<span class="plain xs">★ {c["r"]} · {nfmt(c["s"])} · {c["ago"]}</span>', cls="meta meta--tight"))
block("N30", "Метрики на обложке", "Всё лежит на картинке, под заголовком пусто.",
      lambda c: "",
      cover_fn=lambda c: '<span class="scrim"></span><span class="onbl onbl--row">'
                         f'{chip_cat(c, "chip chip--glass")}<span class="chip chip--glass">★ {c["r"]}</span>'
                         f'<span class="chip chip--glass">{nfmt(c["s"])}</span></span>')

IMGCSS = "\n".join(f'  .im-{k} {{ background-image: url({v}) }}' for k, v in IMGS.items())

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  /* неизменная часть: подложка, обложка, заголовок */
  .card { width: 262px; flex: 0 0 auto; display: flex; flex-direction: column; gap: 0;
    background: hsl(var(--muted)); border-radius: 20px; padding: 8px 8px 14px; cursor: pointer }
  .cov { position: relative; display: block; width: 100%; aspect-ratio: 16/9;
    border-radius: 14px; overflow: hidden }
  .obj { position: absolute; inset: 12%; background: center/contain no-repeat }
  .ttl { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
    min-height: 42px; padding: 12px 6px 0; font-size: 16px; font-weight: 500; line-height: 1.3; color: #0F0F0F }

  /* метаданные */
  .meta { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 8px; padding: 10px 6px 0 }
  .meta--tight { gap: 6px }
  .meta--between { display: flex; justify-content: space-between; align-items: center; padding: 10px 6px 0 }
  .plain { display: block; padding: 8px 6px 0; font-size: 14px; line-height: 1.35; color: hsl(0 0% 42%) }
  .plain.one, .plain.xs { padding-top: 0 }
  .xs { font-size: 12px }
  .ghost { display: block; padding: 8px 6px 0; font-size: 13px; color: rgba(15,15,15,.45) }
  .caps { display: block; padding: 10px 6px 0; font-size: 12px; font-weight: 600; letter-spacing: .08em; text-transform: uppercase }
  .cat-col { font-size: 14px; font-weight: 500 }

  .chip { display: inline-flex; align-items: center; gap: 6px; padding: 5px 9px; border-radius: 10px;
    background: hsl(var(--background)); color: hsl(0 0% 27.5%); font-size: 14px; white-space: nowrap }
  .chip--wide { gap: 8px; border-radius: 999px }
  .chip--sh { box-shadow: 0 2px 6px rgba(15,15,15,.08) }
  .chip--out { background: transparent; border: 1px solid rgba(15,15,15,.14) }
  .chip--dark { background: rgba(15,15,15,.08); color: #0F0F0F }
  .chip--xs { font-size: 12px; padding: 3px 7px; border-radius: 8px }
  .chip--glass { background: rgba(255,255,255,.9); color: #0F0F0F; border-radius: 999px; font-size: 13px; padding: 4px 9px }
  .sep { width: 1px; height: 12px; background: rgba(15,15,15,.15); display: inline-block }
  .bar { width: 1px; height: 11px; background: rgba(15,15,15,.2); display: inline-block; margin: 0 7px; vertical-align: -1px }
  .dot { width: 8px; height: 8px; border-radius: 999px; display: inline-block; margin-right: 7px }

  .rate { display: inline-flex; align-items: center; gap: 4px; font-size: 14px; color: #0F0F0F }
  .rate--big { font-size: 18px; font-weight: 600; color: #FF5C1A }
  .soft { display: inline-flex; align-items: center; gap: 5px; font-size: 14px; color: hsl(0 0% 45%) }
  .soft--first { order: -1 }
  .ico { display: inline-flex; align-items: center; gap: 5px; font-size: 14px; color: hsl(0 0% 42%) }
  .big { display: block; padding: 10px 6px 0; font-size: 20px; font-weight: 700; color: #0F0F0F }
  .big__u { font-size: 14px; font-weight: 400; color: hsl(0 0% 45%) }

  /* поверх обложки */
  .ontl { position: absolute; left: 8px; top: 8px }
  .onbl { position: absolute; left: 8px; bottom: 8px }
  .onbl--row { display: flex; gap: 6px; right: 8px; flex-wrap: wrap }
  .onbr { position: absolute; right: 8px; bottom: 8px }
  .dur { padding: 3px 7px; border-radius: 6px; background: rgba(0,0,0,.75); color: #fff; font-size: 12px; font-weight: 600 }
  .scrim { position: absolute; inset: 0; background: linear-gradient(180deg, transparent 45%, rgba(0,0,0,.35) 100%) }
</style>
'''

HEAD = '''<title>Карточка · метаданные</title>
''' + CSS.replace('</style>', IMGCSS + '\n</style>') + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Метаданные карточки · 30</h1>
    <p class="text-caption-14">Обложка, подложка и заголовок везде одинаковые. Меняются только чипы и метрики: с плашками и без, заметные и тихие, снизу и поверх картинки.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''
open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
