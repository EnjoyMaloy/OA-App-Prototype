# Генератор: 20 оттенков текста в режиме multiply, шрифт крупнее
import math
OUT = '/home/user/OA-App-Prototype/prototypes/continue-text-3.html'

TITLE = "Стратегии торговли на вторичном рынке"
SUB = "Осталось 2 урока"
PROG = 61
R, SW, SIZE = 23, 8, 56
CIRC = 2 * math.pi * R
CARD = "linear-gradient(105deg, #FFE7DA 0%, #FFEDE3 55%, #FFFFFF 100%)"

def ring():
    off = CIRC * (1 - PROG / 100)
    return (f'<span class="ring"><svg width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
            f'<defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="#FF5C1A"/><stop offset="1" stop-color="#FFB088"/></linearGradient></defs>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="rgba(32,32,32,.10)" stroke-width="{SW}"/>'
            f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="url(#ga)" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-dasharray="{CIRC:.1f}" stroke-dashoffset="{off:.1f}"/></svg>'
            f'<span class="pct">{PROG}%</span></span>')

CHEV = ('<svg class="chev" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(32,32,32,.4)" '
        'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>')

BUF = []
def block(code, name, cap, tcol, scol, ttl_extra="", sub_extra=""):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
    <div class="cont" style="background:{CARD}">
      {ring()}
      <span class="body">
        <span class="ttl" style="color:{tcol};{ttl_extra}">{TITLE}</span>
        <span class="sub" style="color:{scol};{sub_extra}">{SUB}</span>
      </span>
      {CHEV}
    </div>
  </section>
''')

# оттенки: (код, имя, пояснение, цвет заголовка, цвет подписи)
V = [
 ("V1",  "Терракота",        "Текущий цвет, но шрифт крупнее.",                  "#C24E14", "#D2703A"),
 ("V2",  "Тёмная терракота", "Заголовок глубже, подпись мягче.",                 "#A33F10", "#C9612B"),
 ("V3",  "Жжёный оранж",     "Ярче и живее, ближе к цвету дуги.",                "#B5410A", "#E0762F"),
 ("V4",  "Кирпич",           "Приглушённый красно-коричневый.",                  "#A8442A", "#C97A5C"),
 ("V5",  "Шоколад",          "Тёплый коричневый — спокойнее оранжевого.",        "#6E3B22", "#9A6244"),
 ("V6",  "Кофе",             "Почти нейтральный, но с тёплым подтоном.",         "#5A3A2E", "#8C6553"),
 ("V7",  "Вишня",            "Красный уводит карточку в сторону акции.",         "#8E2F2F", "#B25C55"),
 ("V8",  "Бордо",            "Винный оттенок, благородный и тихий.",             "#7A2440", "#A85C72"),
 ("V9",  "Слива",            "Переход к фиолетовому через тёплый пурпур.",       "#6B3A6E", "#96679A"),
 ("V10", "Бренд-фиолет",     "OA Purple в multiply на персике.",                 "#7B2EFF", "#A66CFF"),
 ("V11", "Тёмный фиолет",    "Глубокий вариант брендового цвета.",               "#4B1E8C", "#7A4FBF"),
 ("V12", "Индиго",           "Холодный контраст к тёплой подложке.",             "#2F3A8C", "#6B75B8"),
 ("V13", "Тёмно-синий",      "Спокойный синий, сильно приглушается multiply.",   "#1F3D63", "#5C7793"),
 ("V14", "Изумруд",          "Зелёный на персике даёт мягкий хаки.",             "#14614A", "#4F8F7C"),
 ("V15", "Олива",            "Тёплая зелень, почти горчица.",                    "#5C5A18", "#8A8747"),
 ("V16", "Тёплый графит",    "Почти чёрный, но с коричневым подтоном.",          "#2B2320", "#6B5A52"),
 ("V17", "Графит и терракота","Заголовок нейтральный, подпись тёплая.",          "#202020", "#C9612B"),
 ("V18", "Терракота и графит","Наоборот: цвет в заголовке, подпись нейтральная.", "#B5410A", "#4A4340"),
 ("V19", "Один цвет, две плотности", "Терракота 100% и 55% — только прозрачность.", "#B5410A", "rgba(181,65,10,.55)"),
]
for code, name, cap, t, s in V:
    block(code, name, cap, t, s)

# V20 — заголовок залит градиентом
BUF.append(f'''  <section class="variant">
    <h2>V20. Градиент в заголовке</h2>
    <p class="variant__cap">Заголовок залит градиентом дуги, подпись — терракота.</p>
    <div class="cont" style="background:{CARD}">
      {ring()}
      <span class="body">
        <span class="ttl grad">{TITLE}</span>
        <span class="sub" style="color:#C9612B">{SUB}</span>
      </span>
      {CHEV}
    </div>
  </section>
''')

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .cont { display: flex; align-items: center; gap: 14px; width: 100%; padding: 16px;
    border-radius: 16px; cursor: pointer; isolation: isolate }
  .ring { position: relative; flex: 0 0 auto; width: 56px; height: 56px }
  .ring svg { transform: rotate(-90deg) }
  .pct { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 700; background-image: linear-gradient(120deg,#FF5C1A,#FFB088);
    -webkit-background-clip: text; background-clip: text; color: transparent }
  .body { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px }
  .chev { flex: 0 0 auto }

  /* крупнее прежнего: заголовок 19, подпись 15 — и оба в multiply */
  .ttl { display: block; font-size: 19px; font-weight: 500; line-height: 1.2; mix-blend-mode: multiply }
  .sub { display: block; font-size: 15px; line-height: 1.25; mix-blend-mode: multiply }
  .grad { background-image: linear-gradient(100deg,#B5410A,#FF8645);
    -webkit-background-clip: text; background-clip: text; color: transparent; mix-blend-mode: normal }
</style>
'''

HEAD = '''<title>Продолжить · оттенки текста</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Оттенки текста · 20</h1>
    <p class="text-caption-14">Везде режим multiply, как в U9 — меняется только оттенок. Заголовок 19px, строка про уроки 15px.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
