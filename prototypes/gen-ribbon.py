# Генератор черновика: 20 зелёных градиентов для ленты «Пройден»
import json
OUT = '/home/user/OA-App-Prototype/prototypes/ribbon.html'
IMGS = json.load(open('/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/imgs.json'))

TITLE = "Инвестиции с нуля: собираем первый портфель"
TITLE2 = "Трейдинг на споте: стратегии и риск-менеджмент"
COVER_BG = "linear-gradient(135deg,#E8DCFB,#A66CFF)"

V = [
    ("G1", "Изумруд → лайм", "Классическая пара: тёмный изумруд уходит в сочный лайм.",
     "linear-gradient(135deg, #059669 0%, #84CC16 100%)", "", "#fff"),
    ("G2", "Три стопа", "Мята, трава и лес в одной ленте — цвет не плоский.",
     "linear-gradient(135deg, #6EE7B7 0%, #22C55E 48%, #15803D 100%)", "", "#fff"),
    ("G3", "С бликом сверху", "Поверх градиента белая вуаль, гаснущая к низу.",
     "linear-gradient(180deg, rgba(255,255,255,.42) 0%, rgba(255,255,255,0) 62%), "
     "linear-gradient(135deg, #10B981 0%, #4D7C0F 100%)", "", "#fff"),
    ("G4", "Конический", "Conic-градиент даёт перелом света посередине ленты.",
     "conic-gradient(from 210deg at 30% 50%, #16A34A, #84CC16, #059669, #16A34A)", "", "#fff"),
    ("G5", "Радиальный свет", "Светлое пятно в левом верхнем углу, как подсветка.",
     "radial-gradient(120% 180% at 15% 0%, #A3E635 0%, transparent 55%), "
     "linear-gradient(135deg, #15803D 0%, #065F46 100%)", "", "#fff"),
    ("G6", "Диагональный блик", "Узкая светлая полоса пересекает ленту наискось.",
     "linear-gradient(105deg, transparent 38%, rgba(255,255,255,.45) 50%, transparent 62%), "
     "linear-gradient(135deg, #047857 0%, #22C55E 100%)", "", "#fff"),
    ("G7", "Стекло", "Полупрозрачный зелёный с размытием — сквозь ленту видно обложку.",
     "linear-gradient(135deg, rgba(34,197,94,.72) 0%, rgba(5,150,105,.72) 100%)", "glass", "#fff"),
    ("G8", "Неон", "Кислотный лайм с зелёным свечением вокруг.",
     "linear-gradient(135deg, #BEF264 0%, #22C55E 100%)", "neon", "#14532D"),
    ("G9", "Сочный", "Лайм → изумруд → еловый: самый насыщенный вариант.",
     "linear-gradient(135deg, #A3E635 0%, #10B981 55%, #047857 100%)", "", "#fff"),
    ("G10", "Морская волна", "Бирюза уходит в травяной — прохладный зелёный.",
     "linear-gradient(135deg, #2DD4BF 0%, #16A34A 100%)", "", "#fff"),
    ("G11", "Олива", "Приглушённая пара для спокойных обложек.",
     "linear-gradient(135deg, #A7C957 0%, #386641 100%)", "", "#fff"),
    ("G12", "Металлик", "Повторяющиеся полосы дают эффект шлифованного металла.",
     "repeating-linear-gradient(115deg, #16A34A 0 6px, #22C55E 6px 10px, #15803D 10px 16px)", "", "#fff"),
    ("G13", "Пастель", "Светлая лента с тёмно-зелёной надписью — не спорит с картинкой.",
     "linear-gradient(135deg, #DCFCE7 0%, #86EFAC 100%)", "", "#14532D"),
    ("G14", "Градиентный контур", "Прозрачная лента с градиентной рамкой.",
     "transparent", "outline", "#15803D"),
    ("G15", "Жёсткая граница", "Два цвета встык, без перехода.",
     "linear-gradient(135deg, #22C55E 0%, #22C55E 50%, #065F46 50%, #065F46 100%)", "", "#fff"),
    ("G16", "Объём", "Светлая кромка сверху и тень снизу внутри ленты.",
     "linear-gradient(180deg, #34D399 0%, #059669 60%, #065F46 100%)", "emboss", "#fff"),
    ("G17", "Малахит", "Тёмная основа с холодным зелёным отблеском.",
     "radial-gradient(140% 120% at 80% 100%, #34D399 0%, transparent 60%), "
     "linear-gradient(135deg, #064E3B 0%, #065F46 100%)", "", "#D1FAE5"),
    ("G18", "С фактурой", "Поверх градиента мелкая диагональная штриховка.",
     "repeating-linear-gradient(45deg, rgba(255,255,255,.14) 0 2px, transparent 2px 6px), "
     "linear-gradient(135deg, #15803D 0%, #4ADE80 100%)", "", "#fff"),
    ("G19", "Ледяная мята", "Почти белый верх и мятный низ, тёмная надпись.",
     "linear-gradient(180deg, #F0FDF4 0%, #86EFAC 55%, #34D399 100%)", "", "#065F46"),
    ("G20", "С растворением", "Края ленты тают: цвет плотный в центре и прозрачный по концам.",
     "linear-gradient(90deg, rgba(21,128,61,0) 0%, #16A34A 22%, #4ADE80 50%, #16A34A 78%, rgba(21,128,61,0) 100%)",
     "", "#fff"),
]

BUF = []
for code, name, cap, bg, cls, color in V:
    ribbon = ('<span class="ribbon ' + cls + '" style="background:' + bg + ';color:' + color + '">Пройден</span>')
    cards = ""
    for title, obj in ((TITLE, "im-coin"), (TITLE2, "im-nft")):
        cards += ('<article class="c"><span class="cov" style="background:' + COVER_BG + '">'
                  '<span class="obj ' + obj + '"></span>' + ribbon + '</span>'
                  '<span class="body"><span class="ttl">' + title + '</span></span></article>')
    BUF.append('  <section class="variant">\n'
               '    <h2>' + code + '. ' + name + '</h2>\n'
               '    <p class="variant__cap">' + cap + '</p>\n'
               '    <div class="grid">' + cards + '</div>\n'
               '  </section>\n')

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px }

  .c { display: flex; flex-direction: column; background: hsl(var(--muted)); border-radius: 20px;
       padding: 4px 4px 14px }
  .cov { position: relative; display: block; width: 100%; aspect-ratio: 16 / 10; border-radius: 16px;
         overflow: hidden }
  .obj { position: absolute; inset: 0; background-size: cover; background-position: center }
  .im-coin { background-image: url("IMG_COIN") }
  .im-nft { background-image: url("IMG_NFT") }
  .body { padding: 12px 8px 0 }
  .ttl { font-size: 16px; font-weight: 500; line-height: 1.25; display: -webkit-box; -webkit-line-clamp: 2;
         -webkit-box-orient: vertical; overflow: hidden; min-height: 40px }

  /* лента в углу обложки */
  .ribbon { position: absolute; top: 14px; left: -36px; width: 136px; transform: rotate(-45deg);
            font-size: 11px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
            text-align: center; padding: 6px 0; z-index: 2 }

  .glass { backdrop-filter: blur(6px) saturate(160%); -webkit-backdrop-filter: blur(6px) saturate(160%);
           box-shadow: inset 0 1px 0 rgba(255,255,255,.5) }
  .neon { box-shadow: 0 0 14px rgba(132,204,22,.75), 0 0 4px rgba(34,197,94,.9) }
  .emboss { box-shadow: inset 0 1px 0 rgba(255,255,255,.55), inset 0 -1px 0 rgba(6,78,59,.5) }
  .outline { position: absolute; background: rgba(255,255,255,.92) }
  .outline::before { content: ''; position: absolute; inset: 0; padding: 2px;
    background: linear-gradient(135deg, #A3E635, #059669);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor; mask-composite: exclude; pointer-events: none }
</style>
'''.replace("IMG_COIN", IMGS["coin"]).replace("IMG_NFT", IMGS["nft"])

HEAD = ('<title>Лента «Пройден» · 20 градиентов</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Лента «Пройден» · 20</h1>
    <p class="text-caption-14">Один и тот же уголок на обложке — двадцать зелёных заливок: многослойные градиенты,
      блики, стекло, неон, фактура и растворение.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", len(V))
