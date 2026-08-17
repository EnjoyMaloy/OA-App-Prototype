# Генератор: 20 вариантов рамки блока «Продолжить обучение»
import math
OUT = '/home/user/OA-App-Prototype/prototypes/continue-border.html'

TITLE = "Стратегии торговли на вторичном рынке"
SUB = "Осталось 2 урока"
PROG = 61
R, SW, SIZE = 23, 8, 56
CIRC = 2 * math.pi * R
CARD = "linear-gradient(105deg, #FFE7DA 0%, #FFEDE3 55%, #FFFFFF 100%)"

RING = (f'<span class="ring"><svg width="{SIZE}" height="{SIZE}" viewBox="0 0 {SIZE} {SIZE}">'
        f'<defs><linearGradient id="ga" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="#FF5C1A"/><stop offset="1" stop-color="#FFB088"/></linearGradient></defs>'
        f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="rgba(32,32,32,.10)" stroke-width="{SW}"/>'
        f'<circle cx="28" cy="28" r="{R}" fill="none" stroke="url(#ga)" stroke-width="{SW}" stroke-linecap="round" '
        f'stroke-dasharray="{CIRC:.1f}" stroke-dashoffset="{CIRC * (1 - PROG / 100):.1f}"/></svg>'
        f'<span class="pct">{PROG}%</span></span>')

CHEV = ('<svg class="chev" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="rgba(32,32,32,.4)" '
        'stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>')

BUF = []
def block(code, name, cap, cls="", style="", bed=False, card=CARD):
    inner = f'''<div class="cont {cls}" style="background:{card};{style}">
        {RING}
        <span class="body">
          <span class="ttl">{TITLE}</span>
          <span class="sub">{SUB}</span>
        </span>
        {CHEV}
      </div>'''
    if bed:
        inner = f'<div class="bed">{inner}</div>'
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
    {inner}
  </section>
''')

block("W1", "Белый волосяной кант", "Внутренняя линия 1px — карточка выглядит как стекло.", "b-hair")
block("W2", "Персиковый контур", "Тонкая рамка на тон темнее подложки.", "b-peach")
block("W3", "Контур цвета дуги", "Оранжевый 35% — рамка перекликается с прогрессом.", "b-orange")
block("W4", "Двойной кант", "Светлая рамка снаружи, белая линия внутри.", "b-double")
block("W5", "Толстая рамка", "3px персика — плотная и заметная.", "b-thick")
block("W6", "Градиент Purple + Orange", "Фирменная пара по контуру.", "b-grad1")
block("W7", "Оранжевый градиент", "Контур в тех же цветах, что дуга.", "b-grad2")
block("W8", "Градиент с растворением", "Рамка гаснет слева направо, как и подложка.", "b-grad3")
block("W9", "Стекло", "Полупрозрачная карточка с размытием на цветном фоне.", "b-glass", bed=True,
      card="rgba(255,255,255,.45)")
block("W10", "Стекло с тёплым кантом", "То же стекло, но кант оранжевый.", "b-glass b-glassorange", bed=True,
      card="rgba(255,255,255,.4)")
block("W11", "Кромка снизу", "Цветная линия по низу — как у кнопки.", "b-bottom")
block("W12", "Кайма слева", "Вертикальная полоса 4px в цвет дуги.", "b-left")
block("W13", "Пунктир", "Штриховая рамка — черновой, «в процессе» вид.", "b-dash")
block("W14", "Рамка и тень в тон", "Контур плюс мягкая оранжевая тень.", "b-shadow")
block("W15", "Внешняя обводка", "Контур с отступом от карточки.", "b-outline")
block("W16", "Выпуклая", "Светлый кант сверху, тень снизу — объём.", "b-emboss")
block("W17", "Нейтральная на белом", "Без персика: белая карточка и тёплая серая рамка.", "b-neutral",
      card="#FFFFFF")
block("W18", "Градиент и белый кант", "Внешний градиент плюс внутренняя белая линия.", "b-grad2 b-hair")
block("W19", "Врезка", "Толстая рамка цвета фона экрана — карточка как будто утоплена.", "b-inset")
block("W20", "Только верх и низ", "Две горизонтальные линии, боков нет.", "b-updown")

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .cont { position: relative; display: flex; align-items: center; gap: 14px; width: 100%; padding: 16px;
    border-radius: 16px; cursor: pointer; isolation: isolate }
  .ring { position: relative; flex: 0 0 auto; width: 56px; height: 56px }
  .ring svg { transform: rotate(-90deg) }
  .pct { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-size: 15px; font-weight: 700; background-image: linear-gradient(120deg,#FF5C1A,#FFB088);
    -webkit-background-clip: text; background-clip: text; color: transparent }
  .body { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px }
  .ttl { display: block; font-size: 19px; font-weight: 500; line-height: 1.2; color: #C24E14; mix-blend-mode: multiply }
  .sub { display: block; font-size: 15px; line-height: 1.25; color: #D2703A; mix-blend-mode: multiply }
  .chev { flex: 0 0 auto }
  .bed { background: linear-gradient(120deg,#A66CFF,#FF8645); padding: 14px; border-radius: 20px }

  /* --- рамки --- */
  .b-hair   { box-shadow: inset 0 0 0 1px rgba(255,255,255,.85) }
  .b-peach  { border: 1px solid #FFD0B6 }
  .b-orange { border: 1.5px solid rgba(255,92,26,.35) }
  .b-double { border: 1px solid #FFCDB1; box-shadow: inset 0 0 0 2px rgba(255,255,255,.9) }
  .b-thick  { border: 3px solid #FFD5BE }
  .b-dash   { border: 1.5px dashed rgba(255,92,26,.45) }
  .b-bottom { box-shadow: 0 3px 0 0 #FFC3A4 }
  .b-left   { border-left: 4px solid #FF5C1A; border-radius: 6px 16px 16px 6px }
  .b-shadow { border: 1px solid rgba(255,92,26,.25); box-shadow: 0 12px 24px rgba(255,124,60,.28) }
  .b-outline{ outline: 1.5px solid rgba(255,92,26,.3); outline-offset: 3px }
  .b-emboss { box-shadow: inset 0 1.5px 0 rgba(255,255,255,.95), inset 0 -1.5px 0 rgba(194,78,20,.18),
              0 6px 14px rgba(194,78,20,.12) }
  .b-neutral{ border: 1px solid #EFE3DC }
  .b-inset  { box-shadow: 0 0 0 6px hsl(var(--background)), 0 0 0 7px #FFD9C4 }
  .b-updown { border-top: 1.5px solid #FFCDB1; border-bottom: 1.5px solid #FFCDB1; border-radius: 0 }

  /* градиентные рамки: маска вырезает середину */
  .b-grad1::before, .b-grad2::before, .b-grad3::before {
    content: ''; position: absolute; inset: 0; border-radius: inherit; padding: 1.5px; pointer-events: none;
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor; mask-composite: exclude }
  .b-grad1::before { background: linear-gradient(120deg,#A66CFF,#FF8645) }
  .b-grad2::before { background: linear-gradient(120deg,#FF5C1A,#FFB088) }
  .b-grad3::before { background: linear-gradient(100deg,#FF5C1A,rgba(255,176,136,0)) }

  /* стекло */
  .b-glass { backdrop-filter: blur(18px) saturate(1.6); -webkit-backdrop-filter: blur(18px) saturate(1.6);
    box-shadow: inset 0 0 0 1px rgba(255,255,255,.75) }
  .b-glass .ttl, .b-glass .sub { mix-blend-mode: normal }
  .b-glass .ttl { color: #7A2E06 } .b-glass .sub { color: rgba(122,46,6,.65) }
  .b-glassorange { box-shadow: inset 0 0 0 1.5px rgba(255,92,26,.5) }
</style>
'''

HEAD = '''<title>Продолжить · рамки</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Рамки блока · 20</h1>
    <p class="text-caption-14">Содержимое везде одинаковое — меняется только рамка: волосяные канты, цветные контуры, градиентные обводки и стекло.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
