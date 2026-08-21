# Генератор: 20 карточек курса по логике YouTube
import json
OUT = '/home/user/OA-App-Prototype/prototypes/course-cards-yt.html'
IMGS = json.load(open('/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/imgs.json'))

C = [
 dict(k="rocket",   t="Основы Web3 и DeFi: с чего начать",   cat="Web3 и DeFi",   s=371,   bg="linear-gradient(135deg,#E8DCFB,#A66CFF)", a="#A66CFF", au="Open Academy", ago="2 недели назад",  les=12, hrs="4:20", prog=0),
 dict(k="coin",     t="Инвестиции с нуля за 6 часов",        cat="Инвестиции",    s=35419, bg="linear-gradient(135deg,#FFF1CC,#F5B02E)", a="#F5B02E", au="Павел Сычёв",   ago="3 дня назад",     les=18, hrs="6:05", prog=61),
 dict(k="nft",      t="Криптовалюты: первый шаг",            cat="Основы крипты", s=1024,  bg="linear-gradient(135deg,#FFDFD1,#FF7D60)", a="#FF7D60", au="Open Academy", ago="месяц назад",     les=9,  hrs="3:10", prog=100),
 dict(k="security", t="Безопасность кошелька",               cat="Безопасность",  s=512,   bg="linear-gradient(135deg,#FFD6EC,#EE49A4)", a="#EE49A4", au="Анна Ким",     ago="вчера",           les=7,  hrs="2:45", prog=35),
]
def nfmt(n): return f"{n:,}".replace(",", " ")

DOTS = ('<svg class="dots" width="18" height="18" viewBox="0 0 24 24" fill="currentColor">'
        '<circle cx="12" cy="5" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="12" cy="19" r="1.8"/></svg>')
VERIF = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" class="vf">'
         '<path d="M12 2l2.3 2.1 3.1-.4 1 3 2.8 1.4-1.1 2.9 1.1 2.9-2.8 1.4-1 3-3.1-.4L12 22l-2.3-2.1-3.1.4-1-3-2.8-1.4L3.9 13 2.8 10.1l2.8-1.4 1-3 3.1.4z" opacity=".9"/>'
         '<path d="M10.6 15.4l-2.9-2.9 1.2-1.2 1.7 1.7 4-4 1.2 1.2z" fill="#fff"/></svg>')
LIST = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
        '<path d="M4 6h11M4 12h11M4 18h7"/><path d="M17 14l5 4-5 4z" fill="currentColor" stroke="none"/></svg>')
CHECK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg>')

BUF = []
def block(code, name, cap, body):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
{body}
  </section>
''')
def rail(fn, n=3, cls="rail"):
    return f'    <div class="{cls}">\n' + "\n".join("      " + fn(i, C[i]) for i in range(n)) + "\n    </div>"

def thumb(c, cls="", inner="", objcls=""):
    return (f'<span class="th {cls}" style="background:{c["bg"]}">'
            f'<span class="obj im-{c["k"]} {objcls}"></span>{inner}</span>')
def dur(c):     return f'<span class="dur">{c["hrs"]}</span>'
def lescnt(c):  return f'<span class="dur">{c["les"]} уроков</span>'
def prog(c):    return f'<span class="pbar"><i style="width:{c["prog"]}%"></i></span>'
def ava(c):     return f'<span class="ava" style="background:{c["bg"]}"></span>'
def meta(c, views=True):
    left = f'{nfmt(c["s"])} учеников' if views else f'{c["les"]} уроков'
    return f'<span class="mt">{left} · {c["ago"]}</span>'

# ---------------------------------------------------------------- варианты
block("Y1", "Классика YouTube",
 "Обложка 16:9, аватар автора слева, два ряда серых метаданных, три точки справа.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span>{DOTS}</span></article>'''))

block("Y2", "Без аватара",
 "Как в сетке подписок: текст начинается от левого края.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row"><span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]} · {nfmt(c["s"])} учеников</span></span>{DOTS}</span></article>'''))

block("Y3", "Длительность в углу",
 "Плашка справа снизу — у нас это часы курса или число уроков.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=lescnt(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span></span></article>'''))

block("Y4", "Полоса прогресса",
 "Красная линия YouTube — у нас оранжевая: докуда дошёл ученик.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c) + prog(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span><span class="mt">Осталось {max(1, c["les"] - round(c["les"] * c["prog"] / 100))} уроков</span></span></span></article>'''))

block("Y5", "Компактная строка",
 "Формат поиска: обложка слева, три строки текста справа.",
 rail(lambda i, c: f'''<article class="ys">{thumb(c, "th--sm", dur(c))}
        <span class="txt"><span class="ttl ttl--sm">{c["t"]}</span>{meta(c)}
        <span class="mt">{c["au"]}</span></span>{DOTS}</article>''', n=4, cls="list"))

block("Y6", "Смотреть позже",
 "Плотный список: мини-обложка и заголовок в две строки.",
 rail(lambda i, c: f'''<article class="ys ys--xs">{thumb(c, "th--xs", dur(c))}
        <span class="txt"><span class="ttl ttl--sm">{c["t"]}</span><span class="mt">{c["au"]} · {c["les"]} уроков</span></span>{DOTS}</article>''',
      n=4, cls="list"))

block("Y7", "Плейлист",
 "Стопка сзади и панель с числом уроков — как плейлист YouTube.",
 rail(lambda i, c: f'''<article class="yc"><span class="stack">{thumb(c, inner=f'<span class="plist">{LIST} {c["les"]}</span>')}</span>
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]} · Курс</span><span class="mt">Смотреть весь курс</span></span></span></article>'''))

block("Y8", "Идёт набор",
 "Аналог LIVE: красная плашка и счётчик участников.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner='<span class="live">НАБОР</span>')}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span><span class="mt">{nfmt(c["s"])} участников сейчас</span></span></span></article>'''))

block("Y9", "Метка «Новое»",
 "YouTube ставит бейдж под каналом, а не на обложке.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span><span class="mtrow">{meta(c)}<span class="tag">Новое</span></span></span></span></article>'''))

block("Y10", "Чипы над лентой",
 "Строка фильтров, как под шапкой YouTube.",
 '    <div class="chips"><span class="chip chip--on">Все</span><span class="chip">Крипта</span>'
 '<span class="chip">Трейдинг</span><span class="chip">Инвестиции</span><span class="chip">Безопасность</span></div>\n'
 + rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span></span></article>'''))

block("Y11", "Кнопки на обложке",
 "«Смотреть позже» и «В очередь» — как при наведении на десктопе.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner='<span class="acts"><span class="act">Позже</span><span class="act">В очередь</span></span>' + dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span></span></article>'''))

block("Y12", "Заголовок в одну строку",
 "Плотнее: название обрезается многоточием.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl ttl--one">{c["t"]}</span>
        <span class="mt">{c["au"]} · {nfmt(c["s"])} учеников</span></span>{DOTS}</span></article>'''))

block("Y13", "Метрики одной строкой",
 "Всё через точку, без иконок — фирменная манера YouTube.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]} · {nfmt(c["s"])} учеников · {c["ago"]}</span></span></span></article>'''))

block("Y14", "Автор с галочкой",
 "Верификация рядом с именем — доверие к автору курса.",
 rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt mt--vf">{c["au"]} {VERIF}</span>{meta(c)}</span></span></article>'''))

block("Y15", "Сетка 2 колонки",
 "Планшетная раскладка: две карточки в ряд.",
 rail(lambda i, c: f'''<article class="yc yc--grid">{thumb(c, inner=dur(c))}
        <span class="row"><span class="txt"><span class="ttl ttl--sm">{c["t"]}</span>
        <span class="mt">{c["au"]}</span><span class="mt">{nfmt(c["s"])} учеников</span></span></span></article>''',
      n=4, cls="grid2"))

block("Y16", "Вертикальные, как Shorts",
 "Обложка 9:16, подпись под ней в две строки.",
 rail(lambda i, c: f'''<article class="yc yc--short">{thumb(c, "th--tall", f'<span class="dur dur--bl">{c["les"]} уроков</span>')}
        <span class="txt"><span class="ttl ttl--sm">{c["t"]}</span><span class="mt">{nfmt(c["s"])} учеников</span></span></article>''', n=4))

block("Y17", "Полка раздела",
 "Заголовок ленты и «Показать все» справа — структура главной YouTube.",
 '    <div class="shelf"><span class="shelf__t">Продолжить обучение</span><span class="shelf__a">Показать все</span></div>\n'
 + rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c) + prog(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span></span></article>'''))

block("Y18", "С описанием",
 "Как в результатах поиска: две строки описания под метаданными.",
 rail(lambda i, c: f'''<article class="ys">{thumb(c, "th--sm", dur(c))}
        <span class="txt"><span class="ttl ttl--sm">{c["t"]}</span>{meta(c)}
        <span class="mt">{c["au"]}</span>
        <span class="desc">Разбираем на практике: инструменты, примеры и домашние задания после каждого урока.</span></span></article>''',
      n=3, cls="list"))

block("Y19", "Тёмная тема",
 "Тот же макет на тёмном фоне.",
 '    <div class="dark">\n' + rail(lambda i, c: f'''<article class="yc">{thumb(c, inner=dur(c))}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span>{DOTS}</span></article>''') + '\n    </div>')

block("Y20", "Пройденное",
 "Обложка приглушена, полоса на 100%, метка «Пройдено».",
 rail(lambda i, c: f'''<article class="yc yc--seen">{thumb(c, "th--seen", f'<span class="seen">{CHECK} Пройдено</span>' + '<span class="pbar"><i style="width:100%"></i></span>')}
        <span class="row">{ava(c)}<span class="txt"><span class="ttl">{c["t"]}</span>
        <span class="mt">{c["au"]}</span>{meta(c)}</span></span></article>'''))

IMGCSS = "\n".join(f'  .im-{k} {{ background-image: url({v}) }}' for k, v in IMGS.items())

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .list { display: flex; flex-direction: column; gap: 14px }
  .grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px }

  /* карточка в духе YouTube: без контейнера, плоско на фоне */
  .yc { display: flex; flex-direction: column; gap: 10px; width: 300px; flex: 0 0 auto; cursor: pointer }
  .yc--grid, .yc--short { width: auto }
  .yc--short { width: 148px }
  .row { display: flex; gap: 12px; align-items: flex-start }
  .txt { display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1 }
  .ttl { font-size: 16px; font-weight: 600; line-height: 1.3; color: #0F0F0F;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden }
  .ttl--sm { font-size: 15px; font-weight: 500 }
  .ttl--one { -webkit-line-clamp: 1 }
  .mt { font-size: 13px; line-height: 1.35; color: #606060 }
  .mtrow { display: flex; align-items: center; gap: 6px; flex-wrap: wrap }
  .mt--vf { display: inline-flex; align-items: center; gap: 4px }
  .vf { color: #909090 }
  .desc { font-size: 13px; line-height: 1.35; color: #606060; margin-top: 6px;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden }
  .dots { color: #606060; flex: 0 0 auto; margin-top: 2px }
  .ava { width: 36px; height: 36px; border-radius: 999px; flex: 0 0 auto }

  /* обложка */
  .th { position: relative; display: block; width: 100%; aspect-ratio: 16/9; border-radius: 12px; overflow: hidden }
  .th--sm { width: 168px; aspect-ratio: 16/9; flex: 0 0 auto; border-radius: 10px }
  .th--xs { width: 120px; aspect-ratio: 16/9; flex: 0 0 auto; border-radius: 8px }
  .th--tall { aspect-ratio: 9/16; border-radius: 12px }
  .th--seen .obj { filter: saturate(.4) }
  .th--seen::after { content: ''; position: absolute; inset: 0; background: rgba(255,255,255,.45) }
  .obj { position: absolute; inset: 12%; background: center/contain no-repeat }

  .dur { position: absolute; right: 6px; bottom: 6px; padding: 2px 5px; border-radius: 4px;
    background: rgba(0,0,0,.8); color: #fff; font-size: 12px; font-weight: 600; letter-spacing: .01em }
  .dur--bl { right: auto; left: 6px }
  .pbar { position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(255,255,255,.45); z-index: 2 }
  .pbar i { display: block; height: 100%; background: #FF5C1A }
  .live { position: absolute; left: 6px; bottom: 6px; padding: 2px 6px; border-radius: 4px;
    background: #E5322D; color: #fff; font-size: 11px; font-weight: 700; letter-spacing: .04em }
  .plist { position: absolute; right: 0; top: 0; bottom: 0; width: 92px; background: rgba(0,0,0,.72);
    color: #fff; display: flex; align-items: center; justify-content: center; gap: 6px; font-size: 14px; font-weight: 500 }
  .stack { position: relative; display: block }
  .stack::before, .stack::after { content: ''; position: absolute; left: 8px; right: 8px; border-radius: 10px 10px 0 0 }
  .stack::before { top: -6px; height: 6px; background: rgba(15,15,15,.22) }
  .stack::after { top: -11px; left: 16px; right: 16px; height: 5px; background: rgba(15,15,15,.12) }
  .acts { position: absolute; right: 6px; top: 6px; display: flex; flex-direction: column; gap: 4px; align-items: flex-end }
  .act { padding: 4px 8px; border-radius: 4px; background: rgba(0,0,0,.75); color: #fff; font-size: 12px; font-weight: 500 }
  .seen { position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); z-index: 2;
    display: inline-flex; align-items: center; gap: 5px; padding: 5px 10px; border-radius: 6px;
    background: rgba(0,0,0,.78); color: #fff; font-size: 13px; font-weight: 500 }
  .tag { padding: 1px 6px; border-radius: 4px; background: #F2F2F2; color: #0F0F0F; font-size: 12px; font-weight: 500 }

  /* строка */
  .ys { display: flex; gap: 12px; align-items: flex-start; cursor: pointer }
  .ys .txt { gap: 3px }
  .ys--xs .ttl { -webkit-line-clamp: 2 }

  /* чипы и полка */
  .chips { display: flex; gap: 8px; overflow-x: auto; margin: 0 -16px 12px; padding: 0 16px }
  .chips::-webkit-scrollbar { display: none }
  .chip { flex: 0 0 auto; padding: 7px 12px; border-radius: 8px; background: #F2F2F2; color: #0F0F0F;
    font-size: 14px; font-weight: 500; white-space: nowrap }
  .chip--on { background: #0F0F0F; color: #fff }
  .shelf { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px }
  .shelf__t { font-size: 18px; font-weight: 700; color: #0F0F0F }
  .shelf__a { font-size: 14px; font-weight: 500; color: #065FD4 }

  /* тёмная тема */
  .dark { background: #0F0F0F; margin: 0 -16px; padding: 14px 0; border-radius: 12px }
  .dark .rail { padding: 0 16px }
  .dark .ttl { color: #F1F1F1 }
  .dark .mt, .dark .dots { color: #AAAAAA }
</style>
'''

HEAD = '''<title>Карточки курсов · YouTube</title>
''' + CSS.replace('</style>', IMGCSS + '\n</style>') + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">По логике YouTube · 20</h1>
    <p class="text-caption-14">Плоские карточки без контейнера, обложка 16:9 со скруглением 12, аватар автора, два ряда серых метаданных через точку, длительность плашкой в углу и полоса прогресса.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — соберу в приложении.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
