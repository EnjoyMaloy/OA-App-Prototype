# Генератор черновика: 20 способов показать, что курс пройден на 100%
import json
OUT = '/home/user/OA-App-Prototype/prototypes/completed.html'
IMGS = json.load(open('/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/imgs.json'))

TITLE = "Инвестиции с нуля: собираем первый портфель"
COVER_BG = "linear-gradient(135deg,#E8DCFB,#A66CFF)"

CHECK = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>')
MEDAL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
         'stroke-linejoin="round"><path d="M7.21 15 2.66 7.14a2 2 0 0 1 .13-2.2L4.4 2.8A2 2 0 0 1 6 2h12a2 2 0 0 1 1.6.8l1.6 2.14a2 2 0 0 1 .14 2.2L16.79 15"/>'
         '<path d="m11 12 5.7-9.5"/><path d="m13 12-5.7-9.5"/><circle cx="12" cy="17" r="5"/></svg>')
CERT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
        'stroke-linejoin="round"><path d="M5 3h9l5 5v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/>'
        '<path d="M14 3v6h5"/><path d="m9 15 2 2 4-4"/></svg>')
REPEAT = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
          'stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M21 3v5h-5"/>'
          '<path d="M21 12a9 9 0 0 1-15 6.7L3 16"/><path d="M3 21v-5h5"/></svg>')

BUF = []


def block(code, title, cap, card):
    BUF.append('  <section class="variant">\n'
               '    <h2>' + code + '. ' + title + '</h2>\n'
               '    <p class="variant__cap">' + cap + '</p>\n'
               '    <div class="grid">' + card + card.replace(TITLE, "Трейдинг на споте: стратегии и риск-менеджмент")
               .replace('im-coin', 'im-nft') + '</div>\n'
               '  </section>\n')


def card(cover_extra="", body="", cls="", cover_cls=""):
    return ('<article class="c ' + cls + '">'
            '<span class="cov ' + cover_cls + '" style="background:' + COVER_BG + '">'
            '<span class="obj im-coin"></span>' + cover_extra + '</span>'
            '<span class="body"><span class="ttl">' + TITLE + '</span>' + body + '</span></article>')


def bar(pct="100%", label="100%", cls=""):
    lab = '<span class="pct">' + label + '</span>' if label else ''
    return ('<span class="row"><span class="bar ' + cls + '"><i style="width:' + pct + '"></i></span>' + lab + '</span>')


# ---------------------------------------------------------------- варианты
block("F1", "Полоска с процентом", "Как сейчас: зелёная полоса и «100%» справа.",
      card(body=bar()))

block("F2", "Полоска без цифры", "Заполненная полоса без подписи — тише и чище.",
      card(body=bar(label="")))

block("F3", "Полоска и галочка", "Вместо процента — галочка в конце полосы.",
      card(body='<span class="row"><span class="bar"><i style="width:100%"></i></span>'
                '<span class="mini ok">' + CHECK + '</span></span>'))

block("F4", "Галочка на обложке", "Кружок с галочкой в правом верхнем углу картинки.",
      card(cover_extra='<span class="badge ok">' + CHECK + '</span>'))

block("F5", "Галочка у заголовка", "Маленькая зелёная галочка перед названием.",
      card(body='', cls="c--inline"))

block("F6", "Плашка «Пройден»", "Чип под названием — словами, без процентов.",
      card(body='<span class="chip ok-soft">' + CHECK + 'Пройден</span>'))

block("F7", "Уголок-лента", "Диагональная лента в углу обложки.",
      card(cover_extra='<span class="ribbon">Пройден</span>', cover_cls="cov--clip"))

block("F8", "Кольцо 100%", "Кольцо прогресса с галочкой внутри, поверх обложки.",
      card(cover_extra='<span class="ring">'
                       '<svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="19" class="ring__bg"/>'
                       '<circle cx="22" cy="22" r="19" class="ring__on"/></svg>'
                       '<i class="ring__i">' + CHECK + '</i></span>'))

block("F9", "Затемнение и галочка", "Обложка притушена, по центру крупная галочка.",
      card(cover_extra='<span class="veil"><span class="veil__i">' + CHECK + '</span></span>'))

block("F10", "Заливка низа обложки", "Полупрозрачная зелёная полоса по нижнему краю картинки.",
      card(cover_extra='<span class="strip">' + CHECK + 'Курс пройден</span>'))

block("F11", "Зелёная рамка", "Карточка обведена зелёным — статус читается целиком.",
      card(body=bar(label=""), cls="c--edge"))

block("F12", "Дата прохождения", "Чип с датой: когда именно закрыли курс.",
      card(body='<span class="chip ok-soft">' + CHECK + 'Пройден 12 апреля</span>'))

block("F13", "Медаль", "Иконка медали вместо галочки — награда, а не отметка.",
      card(body='<span class="row row--meta"><span class="mini gold">' + MEDAL + '</span>'
                '<span class="meta">Курс пройден</span></span>'))

block("F14", "Сертификат", "Строка с иконкой документа: есть что показать.",
      card(body='<span class="row row--meta"><span class="mini ok">' + CERT + '</span>'
                '<span class="meta">Сертификат получен</span></span>'))

block("F15", "Линия сверху карточки", "Тонкая зелёная кромка по верхнему краю — самый тихий вариант.",
      card(body='<span class="meta">Пройден</span>', cls="c--top"))

block("F16", "Галочка в углу с выносом", "Кружок наезжает на край обложки, как стикер.",
      card(cover_extra='<span class="sticker ok">' + CHECK + '</span>'))

block("F17", "Обложка в сером", "Пройденный курс уходит в оттенки серого, статус — чипом.",
      card(cover_extra='<span class="badge ok">' + CHECK + '</span>', cover_cls="cov--gray"))

block("F18", "Пилюля «100%»", "Процент вынесен на обложку пилюлей.",
      card(cover_extra='<span class="pill">100%</span>'))

block("F19", "Кнопка «Пройти снова»", "Вместо метрик — действие: вернуться к материалу.",
      card(body='<span class="btn">' + REPEAT + 'Пройти снова</span>'))

block("F20", "Полоска и подпись", "Полоса, а под ней строка «Пройден · 6 уроков».",
      card(body=bar(label="") + '<span class="meta meta--mt">Пройден · 6 уроков</span>'))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px }

  .c { position: relative; display: flex; flex-direction: column; background: hsl(var(--muted));
       border-radius: 20px; padding: 4px 4px 14px }
  .c--edge { box-shadow: inset 0 0 0 2px #22C55E }
  .c--top::before { content: ''; position: absolute; left: 18px; right: 18px; top: 0; height: 3px;
                    border-radius: 0 0 3px 3px; background: #22C55E }

  .cov { position: relative; display: block; width: 100%; aspect-ratio: 16 / 10; border-radius: 16px;
         overflow: hidden }
  .cov--clip { overflow: hidden }
  .cov--gray .obj { filter: grayscale(1); opacity: .75 }
  .obj { position: absolute; inset: 0; background-size: cover; background-position: center }
  .im-coin { background-image: url("IMG_COIN") }
  .im-nft { background-image: url("IMG_NFT") }

  .body { display: flex; flex-direction: column; padding: 12px 8px 0 }
  .ttl { font-size: 16px; font-weight: 500; line-height: 1.25; display: -webkit-box; -webkit-line-clamp: 2;
         -webkit-box-orient: vertical; overflow: hidden; min-height: 40px }
  .c--inline .ttl::before { content: '✓'; color: #16A34A; font-weight: 700; margin-right: 6px }

  .row { display: flex; align-items: center; gap: 10px; margin-top: 12px }
  .row--meta { gap: 8px }
  .bar { flex: 1; height: 6px; border-radius: 3px; background: hsl(var(--background)); overflow: hidden }
  .bar i { display: block; height: 100%; border-radius: 3px; background: #22C55E }
  .pct { font-size: 13px; color: hsl(var(--muted-foreground)) }
  .meta { font-size: 13px; color: hsl(var(--muted-foreground)) }
  .meta--mt { margin-top: 8px }

  .mini { display: inline-flex; align-items: center; justify-content: center; width: 22px; height: 22px;
          border-radius: 50%; flex: 0 0 auto }
  .mini svg { width: 13px; height: 13px }
  .ok { background: #DCFCE7; color: #15803D }
  .gold { background: #FEF3C7; color: #B45309 }

  .chip { display: inline-flex; align-items: center; gap: 6px; align-self: flex-start; margin-top: 12px;
          height: 26px; padding: 0 11px; border-radius: 999px; font-size: 12px; font-weight: 600 }
  .chip svg { width: 12px; height: 12px }
  .ok-soft { background: #DCFCE7; color: #15803D }

  .badge { position: absolute; top: 8px; right: 8px; width: 28px; height: 28px; border-radius: 50%;
           background: #22C55E; color: #fff; display: flex; align-items: center; justify-content: center;
           box-shadow: 0 2px 8px rgba(0,0,0,.18) }
  .badge svg { width: 15px; height: 15px }

  .sticker { position: absolute; top: -6px; right: -6px; width: 34px; height: 34px; border-radius: 50%;
             background: #22C55E; color: #fff; display: flex; align-items: center; justify-content: center;
             box-shadow: 0 0 0 4px hsl(var(--muted)) }
  .sticker svg { width: 17px; height: 17px }

  .ribbon { position: absolute; top: 12px; left: -34px; width: 130px; transform: rotate(-45deg);
            background: #22C55E; color: #fff; font-size: 11px; font-weight: 700; letter-spacing: .04em;
            text-transform: uppercase; text-align: center; padding: 5px 0 }

  .ring { position: absolute; top: 8px; right: 8px; width: 40px; height: 40px }
  .ring > svg { width: 40px; height: 40px; transform: rotate(-90deg) }
  .ring__bg { fill: none; stroke: rgba(255,255,255,.55); stroke-width: 4 }
  .ring__on { fill: none; stroke: #22C55E; stroke-width: 4; stroke-linecap: round }
  .ring__i { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
             color: #15803D }
  .ring__i svg { width: 16px; height: 16px }

  .veil { position: absolute; inset: 0; background: rgba(16,24,20,.42); display: flex; align-items: center;
          justify-content: center }
  .veil__i { width: 52px; height: 52px; border-radius: 50%; background: rgba(255,255,255,.92); color: #15803D;
             display: flex; align-items: center; justify-content: center }
  .veil__i svg { width: 26px; height: 26px }

  .strip { position: absolute; left: 0; right: 0; bottom: 0; display: flex; align-items: center; gap: 6px;
           padding: 7px 10px; background: rgba(34,197,94,.92); color: #fff; font-size: 12px; font-weight: 600 }
  .strip svg { width: 13px; height: 13px }

  .pill { position: absolute; top: 8px; right: 8px; height: 24px; padding: 0 10px; border-radius: 999px;
          background: rgba(255,255,255,.92); color: #15803D; font-size: 12px; font-weight: 700;
          display: flex; align-items: center }

  .btn { display: inline-flex; align-items: center; justify-content: center; gap: 8px; margin-top: 12px;
         height: 38px; border-radius: 999px; background: hsl(var(--background)); font-size: 14px;
         font-weight: 500 }
  .btn svg { width: 15px; height: 15px }
</style>
'''.replace("IMG_COIN", IMGS["coin"]).replace("IMG_NFT", IMGS["nft"])

HEAD = ('<title>Курс пройден · 20 вариантов</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Курс пройден · 20</h1>
    <p class="text-caption-14">Одна и та же карточка завершённого курса — двадцать способов показать, что он
      пройден на 100%: полосы, галочки, кружки, ленты и подписи.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
