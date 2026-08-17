# Генератор: 20 вариантов — текст прозрачный или тон-в-тон с подложкой
import math
OUT = '/home/user/OA-App-Prototype/prototypes/continue-text-2.html'

TITLE = "Стратегии торговли на вторичном рынке"
PROG, LEFT = 61, 2
R, SW, SIZE = 23, 8, 56
CIRC = 2 * math.pi * R

CARD = "linear-gradient(105deg, #FFE7DA 0%, #FFEDE3 55%, #FFFFFF 100%)"
CARD_DEEP = "linear-gradient(105deg, #FF8F5A 0%, #FFA97C 55%, #FFC7A8 100%)"

def ring(track="rgba(32,32,32,.10)", pct_cls=""):
    off = CIRC * (1 - PROG / 100)
    return (f'<span class="ring"><svg width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
            f'<defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#FF5C1A"/><stop offset="1" stop-color="#FFB088"/></linearGradient>'
            f'<linearGradient id="gw" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="rgba(255,255,255,.7)"/></linearGradient></defs>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="{track}" stroke-width="{SW}"/>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="url(#{"gw" if pct_cls == "on-deep" else "ga"})" '
            f'stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-dasharray="{CIRC:.1f}" stroke-dashoffset="{off:.1f}"/></svg>'
            f'<span class="pct {pct_cls}">{PROG}%</span></span>')

BUF = []
def block(code, title, cap, body, card=CARD, cls="", deep=False, wm=""):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {title}</h2>
    <p class="variant__cap">{cap}</p>
    <div class="cont {cls}" style="background:{card}">
      {wm}
      {ring("rgba(255,255,255,.35)" if deep else "rgba(32,32,32,.10)", "on-deep" if deep else "")}
      <span class="body">{body}</span>
      <span class="chev {'chev--w' if deep else ''}">›</span>
    </div>
  </section>
''')

def T(t, cls=""):  return f'<span class="ttl {cls}">{t}</span>'
def S(t, cls=""):  return f'<span class="sub {cls}">{t}</span>'

# =====================================================================
block("U1", "Подпись оранжевая 45%",
 "Полутон не серый, а цвет дуги с прозрачностью.",
 T(TITLE) + S("Осталось 2 урока", "c-or-45"))

block("U2", "Подпись оранжевая 28%",
 "Ещё тише — почти растворяется в персике.",
 T(TITLE) + S("Осталось 2 урока", "c-or-28"))

block("U3", "Подпись в цвет подложки",
 "Тон-в-тон: тёплый оттенок самой карточки, без серого.",
 T(TITLE) + S("Осталось 2 урока", "c-tone"))

block("U4", "Весь текст тёплый",
 "Заголовок глубокий терракотовый, подпись — он же на 45%.",
 T(TITLE, "c-deep") + S("Осталось 2 урока", "c-deep-45"))

block("U5", "Заголовок градиентом",
 "Заливка текста тем же градиентом, что у дуги и процента.",
 T(TITLE, "grad") + S("Осталось 2 урока", "c-or-45"))

block("U6", "Градиент и затухание",
 "Градиент в тексте плюс прозрачность к правому краю.",
 T(TITLE, "grad fade") + S("Осталось 2 урока", "c-or-40"))

block("U7", "Цифра водяным знаком",
 "Крупная «2» цветом подложки лежит за текстом.",
 T(TITLE) + S("Осталось 2 урока", "c-or-45"), wm='<span class="wm">2</span>')

block("U8", "Процент водяным знаком",
 "За текстом — крупные 61% в тон карточке.",
 T(TITLE) + S("Осталось 2 урока", "c-or-45"), wm='<span class="wm wm--pct">61%</span>')

block("U9", "Умножение",
 "mix-blend-mode: multiply — текст замешан в подложку.",
 T(TITLE, "bl-mul") + S("Осталось 2 урока", "bl-mul sub--tone"))

block("U10", "Наложение",
 "mix-blend-mode: overlay — текст живёт внутри градиента.",
 T(TITLE, "bl-ovl") + S("Осталось 2 урока", "bl-ovl"))

block("U11", "Белый по персику",
 "Насыщенная подложка, текст белый с прозрачностью — как у Apple.",
 T(TITLE, "c-w") + S("Осталось 2 урока", "c-w-65"), card=CARD_DEEP, deep=True)

block("U12", "Белый, два уровня",
 "Заголовок белый 100%, подпись 55% — тот же приём, тише.",
 T(TITLE, "c-w") + S("Осталось 2 урока", "c-w-55"), card=CARD_DEEP, deep=True)

block("U13", "Только оттенки персика",
 "Ни серого, ни чёрного: заголовок и подпись — два оттенка фона.",
 T(TITLE, "c-tone-strong") + S("Осталось 2 урока", "c-tone"))

block("U14", "Тон-в-тон и плотная цифра",
 "Слова растворяются, число остаётся читаемым.",
 T(TITLE) + S('<span class="c-tone">Осталось</span> <span class="c-deep">2 урока</span>'))

block("U15", "Мягкая терракота",
 "Заголовок 85% терракоты, подпись 35% — карточка звучит одним цветом.",
 T(TITLE, "c-deep-85") + S("Осталось 2 урока", "c-deep-35"))

block("U16", "Подпись гаснет вправо",
 "Маска: строка растворяется к концу.",
 T(TITLE) + S("Осталось 2 урока · 12 минут", "c-or-50 fade"))

block("U17", "Заголовок гаснет вправо",
 "Хвост длинного названия уходит в подложку.",
 T(TITLE, "fade one") + S("Осталось 2 урока", "c-or-45"))

block("U18", "Подпись в цвет дуги",
 "Полная плотность оранжевого — подпись становится акцентом.",
 T(TITLE, "c-graph-85") + S("Осталось 2 урока", "c-or-100"))

block("U19", "Контурная цифра",
 "Крупная «2» только обводкой в тон подложке.",
 T(TITLE) + S("Осталось 2 урока", "c-or-45"), wm='<span class="wm wm--out">2</span>')

block("U20", "Три оттенка персика",
 "Заголовок, число и слово — три плотности одного тёплого цвета.",
 T(TITLE, "c-deep-85") + S('<span class="c-deep">2 урока</span> <span class="c-deep-35">осталось</span>'))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .cont { position: relative; overflow: hidden; display: flex; align-items: center; gap: 14px;
    width: 100%; padding: 16px; border-radius: 16px; cursor: pointer; isolation: isolate }
  .ring { position: relative; flex: 0 0 auto; width: 56px; height: 56px }
  .ring svg { transform: rotate(-90deg) }
  .pct { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 700; background-image: linear-gradient(120deg,#FF5C1A,#FFB088);
    -webkit-background-clip: text; background-clip: text; color: transparent }
  .pct.on-deep { background: none; color: #fff }
  .body { position: relative; flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px }
  .chev { position: relative; flex: 0 0 auto; font-size: 22px; color: rgba(32,32,32,.35); line-height: 1 }
  .chev--w { color: rgba(255,255,255,.7) }

  .ttl { display: block; font-size: 17px; font-weight: 500; line-height: 1.2; color: #202020 }
  .sub { display: block; font-size: 13px; line-height: 1.25; color: rgba(32,32,32,.5) }

  /* оранжевый цвета дуги с разной прозрачностью */
  .c-or-100 { color: #FF5C1A } .c-or-50 { color: rgba(255,92,26,.5) }
  .c-or-45 { color: rgba(255,92,26,.45) } .c-or-40 { color: rgba(255,92,26,.4) }
  .c-or-28 { color: rgba(255,92,26,.28) }
  /* тон-в-тон с персиковой подложкой */
  .c-tone { color: #E7A886 } .c-tone-strong { color: #D98A5F }
  .c-deep { color: #B2541F } .c-deep-85 { color: rgba(178,84,31,.85) }
  .c-deep-45 { color: rgba(178,84,31,.45) } .c-deep-35 { color: rgba(178,84,31,.35) }
  .c-graph-85 { color: rgba(32,32,32,.85) }
  .c-w { color: #fff } .c-w-65 { color: rgba(255,255,255,.65) } .c-w-55 { color: rgba(255,255,255,.55) }

  .grad { background-image: linear-gradient(100deg,#FF5C1A,#FFB088);
    -webkit-background-clip: text; background-clip: text; color: transparent }
  .fade { -webkit-mask-image: linear-gradient(90deg,#000 55%,transparent 100%);
    mask-image: linear-gradient(90deg,#000 55%,transparent 100%) }
  .one { display: -webkit-box; -webkit-line-clamp: 1; -webkit-box-orient: vertical; overflow: hidden }
  .bl-mul { mix-blend-mode: multiply; color: #C24E14 }
  .bl-ovl { mix-blend-mode: overlay; color: #7A2A00 }
  .sub--tone { color: #D2703A }

  /* водяные знаки цветом подложки */
  .wm { position: absolute; right: 14px; top: 50%; transform: translateY(-50%); font-size: 82px; font-weight: 800;
    line-height: 1; color: rgba(255,255,255,.75); z-index: 0 }
  .wm--pct { font-size: 56px; color: rgba(255,138,90,.16) }
  .wm--out { color: transparent; -webkit-text-stroke: 2px rgba(255,138,90,.35) }
</style>
'''

HEAD = '''<title>Продолжить · прозрачный текст</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Прозрачность и тон-в-тон · 20</h1>
    <p class="text-caption-14">Текст не серый: либо цвет дуги с прозрачностью, либо оттенок самой подложки, либо белый на насыщенном персике. Карточка и кольцо везде одинаковые.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
