# 20 вариантов кнопки «Весь каталог» в конце главной
OUT = '/home/user/OA-App-Prototype/prototypes/catalog-button.html'
LBL = "Весь каталог"

ARROW = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>')
CHEV = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>')
GRID = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/>'
        '<rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>')

BUF = []
def block(code, name, cap, html):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
    {html}
  </section>
''')

def b(cls="", inner=None, style=""):
    inner = inner or LBL
    return f'<button class="btn {cls}" style="{style}">{inner}</button>'

block("K1", "Как сейчас", "Контур 1px, скругление 12, текст 16.", b())
block("K2", "Пилюля", "То же, но полностью скруглённая.", b("r-full"))
block("K3", "Серая заливка", "Без контура, фон muted.", b("solid-muted"))
block("K4", "Графит", "Тёмная кнопка — главное действие экрана.", b("solid-dark"))
block("K5", "Бренд-фиолет", "Заливка OA Purple, белый текст.", b("solid-brand"))
block("K6", "Светлый фиолет", "Мягкая фиолетовая заливка и цветной текст.", b("soft-brand"))
block("K7", "Бренд-градиент", "Purple → Orange из брендбука.", b("grad"))
block("K8", "Градиентный контур", "Заливка белая, рамка из бренд-пары.", b("grad-border"))
block("K9", "Со стрелкой", "Стрелка справа подсказывает переход.", b("", f'<span>{LBL}</span>{ARROW}'))
block("K10", "Стрелка у текста", "Иконка стоит вплотную к подписи по центру.", b("", f'<span class="inline">{LBL} {CHEV}</span>'))
block("K11", "С иконкой каталога", "Сетка слева от подписи.", b("", f'{GRID}<span>{LBL}</span>'))
block("K12", "Со счётчиком", "Сколько курсов ждёт в каталоге.", b("", f'<span>{LBL}</span><span class="count">24</span>'))
block("K13", "Стеклянная", "Тот же стиль, что у таб-бара.", '<div class="bed">' + b("glassy") + '</div>')
block("K14", "С тенью", "Белая кнопка приподнята над фоном.", b("shadowed"))
block("K15", "Кнопочное дно", "Цветная кромка снизу — тактильная.", b("solid-brand deep"))
block("K16", "Крупная", "Высота 60 и текст 18 — заметнее.", b("big"))
block("K17", "Компактная", "Высота 44, текст 15.", b("small"))
block("K18", "Только текст", "Ссылка без рамки, по центру.", b("ghost", f'<span class="inline">{LBL} {CHEV}</span>'))
block("K19", "Пунктирная", "Штриховая рамка — «здесь ещё есть».", b("dashed"))
block("K20", "Строкой с разделителями", "Линии по бокам, как «показать ещё».", '<div class="rule"><span></span>' + b("ghost inline-btn") + '<span></span></div>')

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .btn { display: flex; align-items: center; justify-content: center; gap: 8px; width: 100%; height: 52px;
    border: 1px solid hsl(var(--border)); border-radius: 12px; background: hsl(var(--background));
    color: hsl(var(--foreground)); font: inherit; font-size: 16px; font-weight: 500; letter-spacing: .01em; cursor: pointer }
  .inline { display: inline-flex; align-items: center; gap: 6px }

  .r-full { border-radius: 999px }
  .solid-muted { background: hsl(var(--muted)); border-color: transparent }
  .solid-dark { background: #202020; color: #fff; border-color: transparent }
  .solid-brand { background: hsl(var(--primary)); color: #fff; border-color: transparent }
  .soft-brand { background: #EFE6FF; color: #7B2EFF; border-color: transparent }
  .grad { background: linear-gradient(100deg, #A66CFF, #FF8645); color: #fff; border-color: transparent }
  .grad-border { position: relative; border: 0 }
  .grad-border::before { content: ''; position: absolute; inset: 0; border-radius: inherit; padding: 1.6px;
    background: linear-gradient(100deg, #A66CFF, #FF8645);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor; mask-composite: exclude }
  .count { min-width: 26px; height: 22px; padding: 0 7px; border-radius: 999px; background: hsl(var(--muted));
    display: inline-flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600;
    color: hsl(0 0% 35%) }
  .bed { background: linear-gradient(120deg, #A66CFF, #FF8645); padding: 14px; border-radius: 16px }
  .glassy { border: 0; background: rgba(255,255,255,.42); color: #fff;
    -webkit-backdrop-filter: blur(24px) saturate(180%); backdrop-filter: blur(24px) saturate(180%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.9), inset 0 0 0 1px rgba(255,255,255,.5), 0 8px 24px rgba(17,12,34,.2) }
  .shadowed { border-color: transparent; box-shadow: 0 8px 20px rgba(32,32,32,.12) }
  .deep { box-shadow: 0 4px 0 0 #7B2EFF }
  .big { height: 60px; font-size: 18px; border-radius: 14px }
  .small { height: 44px; font-size: 15px; border-radius: 10px }
  .ghost { border-color: transparent; background: transparent; color: #7B2EFF; font-weight: 500 }
  .dashed { border-style: dashed; border-color: rgba(32,32,32,.22) }
  .rule { display: flex; align-items: center; gap: 12px }
  .rule span { flex: 1; height: 1px; background: hsl(var(--border)) }
  .inline-btn { width: auto; height: auto; padding: 6px 2px }
</style>
'''

HEAD = '''<title>Кнопка каталога · 20</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Кнопка «Весь каталог» · 20</h1>
    <p class="text-caption-14">Кнопка стоит в конце главной, под лентами курсов. Ширина везде во весь экран.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''
open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
