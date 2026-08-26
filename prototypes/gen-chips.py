# Генератор черновика: 10 цветовых форматов чипов урока
OUT = '/home/user/OA-App-Prototype/prototypes/chips.html'

PLAY = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="m6 3 14 9-14 9z"/></svg>'
SPARK = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">'
         '<path d="M12 2.5 13.7 8 19 9.7 13.7 11.4 12 17l-1.7-5.6L5 9.7 10.3 8z"/>'
         '<path d="M18.5 14.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/></svg>')
BOOK = ('<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M12 7v14"/>'
        '<path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/></svg>')
UNLOCK = ('<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/>'
          '<path d="M7 11V7a5 5 0 0 1 9.9-1"/></svg>')

# тип: подпись, иконка, основной цвет, светлый цвет градиента, пастельная подложка
T = [
    ("Видео", PLAY, "#2C6BD6", "#6FA8FF", "#E5EFFE"),
    ("Квиз", SPARK, "#E4712A", "#F5A26A", "#FFEBDF"),
    ("Инструкция", BOOK, "#7B2EFF", "#B98CFF", "#EDE4FF"),
    ("Бесплатно", UNLOCK, "#12A06E", "#5FD3A6", "#DFF3EA"),
]

LESSON = ("Основные концепции", "12 мин", "02")

BUF = []


def block(code, title, cap, chipfn):
    chips = "".join(chipfn(*t) for t in T)
    BUF.append('  <section class="variant">\n'
               '    <h2>' + code + '. ' + title + '</h2>\n'
               '    <p class="variant__cap">' + cap + '</p>\n'
               '    <div class="chips">' + chips + '</div>\n'
               '    <div class="l">\n'
               '      <div class="li"><span class="num">' + LESSON[2] + '</span>'
               '<span class="col"><span class="ttl">' + LESSON[0] + '</span>'
               '<span class="chips chips--row">' + chipfn(*T[0]) + chipfn(*T[1]) + chipfn(*T[2]) + '</span></span>'
               '<span class="dur">' + LESSON[1] + '</span></div>\n'
               '    </div>\n'
               '  </section>\n')


def k1(label, icon, c, light, pastel):
    return ('<span class="chip chip--fill" style="background:linear-gradient(135deg,' + light + ' 0%,' + c + ' 100%)">'
            + icon + label + '</span>')


def k2(label, icon, c, light, pastel):
    return '<span class="chip chip--fill" style="background:' + c + '">' + icon + label + '</span>'


def k3(label, icon, c, light, pastel):
    return '<span class="chip" style="background:' + pastel + ';color:' + c + '">' + icon + label + '</span>'


def k4(label, icon, c, light, pastel):
    return ('<span class="chip chip--out" style="border-color:' + c + '55;color:' + c + '">' + icon + label + '</span>')


def k5(label, icon, c, light, pastel):
    return ('<span class="chip chip--soft"><i class="d" style="background:' + c + '"></i>' + label + '</span>')


def k6(label, icon, c, light, pastel):
    return '<span class="chip chip--bare" style="color:' + c + '">' + icon + label + '</span>'


def k7(label, icon, c, light, pastel):
    return ('<span class="chip chip--dark"><i class="ic" style="color:' + light + '">' + icon + '</i>' + label + '</span>')


def k8(label, icon, c, light, pastel):
    return ('<span class="chip chip--white" style="box-shadow:0 4px 12px ' + c + '33, inset 0 0 0 1px ' + c + '1f">'
            '<i class="ic" style="color:' + c + '">' + icon + '</i>' + label + '</span>')


def k9(label, icon, c, light, pastel):
    return ('<span class="chip chip--gradline" style="--g:linear-gradient(135deg,' + light + ',' + c + ');color:' + c + '">'
            + icon + label + '</span>')


def k10(label, icon, c, light, pastel):
    return ('<span class="chip chip--badge"><i class="cir" style="background:linear-gradient(135deg,' + light + ',' + c
            + ')">' + icon + '</i>' + label + '</span>')


def k11(label, icon, c, light, pastel):
    return ('<span class="chip chip--fill chip--glow" style="background:linear-gradient(135deg,' + light + ' 0%,' + c
            + ' 100%);box-shadow:0 6px 16px ' + c + '4d">' + icon + label + '</span>')


def k12(label, icon, c, light, pastel):
    return ('<span class="chip" style="background:' + pastel + ';color:' + c + '">'
            '<i class="cir cir--sm" style="background:' + c + '">' + icon + '</i>' + label + '</span>')


block("K1", "Градиент", "Как сейчас: заливка градиентом, белый текст и иконка.", k1)
block("K2", "Плоский цвет", "Та же логика, но без градиента — спокойнее и ближе к системным стилям.", k2)
block("K3", "Пастель", "Светлая подложка и цветной текст: чипы не спорят с обложкой и кнопками.", k3)
block("K4", "Контур", "Прозрачный фон и цветная обводка — самый лёгкий вариант.", k4)
block("K5", "Точка-индикатор", "Нейтральная пилюля, цвет — только в точке. Максимально тихо.", k5)
block("K6", "Без плашки", "Только цветная иконка и подпись — чипы перестают быть плашками.", k6)
block("K7", "Тёмный чип", "Графитовая пилюля с цветной иконкой: цвет остаётся акцентом, а не фоном.", k7)
block("K8", "Белый с цветной тенью", "Белая пилюля, цветная иконка и мягкая тень в цвет — «стеклянный» вариант.", k8)
block("K9", "Градиентная обводка", "Цвет живёт в рамке, середина прозрачная.", k9)
block("K10", "Иконка в кружке", "Градиентный кружок с иконкой слева, дальше нейтральная подпись.", k10)
block("K11", "Градиент со свечением", "Тот же градиент, но с цветной тенью — чипы «подсвечены».", k11)
block("K12", "Пастель с кружком", "Пастельная пилюля и плотный цветной кружок с иконкой.", k12)

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  .chips { display: flex; flex-wrap: wrap; gap: 8px }
  .chips--row { margin-top: 8px; gap: 6px }

  .chip { display: inline-flex; align-items: center; gap: 6px; height: 28px; padding: 0 12px 0 9px;
          border-radius: 999px; font-size: 13px; font-weight: 500; white-space: nowrap;
          background: hsl(var(--muted)); color: hsl(var(--foreground)) }
  .chip svg { flex: 0 0 auto }
  .chip--fill { color: #fff }
  .chip--out { background: none; border: 1.5px solid }
  .chip--soft { background: hsl(var(--background)); color: hsl(var(--foreground)); padding: 0 12px }
  .chip--bare { background: none; padding: 0 }
  .chip--dark { background: hsl(var(--foreground)); color: hsl(var(--background)) }
  .chip--white { background: hsl(var(--background)) }
  .chip--badge { background: hsl(var(--background)); padding: 3px 12px 3px 3px; height: 30px }
  .chip .ic { display: inline-flex }
  .chip .d { width: 8px; height: 8px; border-radius: 50%; flex: 0 0 auto }
  .chip .cir { display: inline-flex; align-items: center; justify-content: center; width: 24px; height: 24px;
               border-radius: 50%; color: #fff; flex: 0 0 auto }
  .chip .cir--sm { width: 20px; height: 20px; margin-left: -3px }
  .chip--gradline { position: relative; background: hsl(var(--background)) }
  .chip--gradline::before { content: ''; position: absolute; inset: 0; border-radius: 999px; padding: 1.5px;
    background: var(--g); -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor; mask-composite: exclude; pointer-events: none }

  .l { background: hsl(var(--muted)); border-radius: 16px }
  .li { display: flex; align-items: flex-start; gap: 12px; padding: 14px }
  .num { width: 24px; flex: 0 0 auto; font-size: 15px; color: hsl(var(--muted-foreground)) }
  .col { flex: 1; min-width: 0 }
  .ttl { display: block; font-size: 16px; font-weight: 500; line-height: 1.25 }
  .dur { flex: 0 0 auto; font-size: 14px; color: hsl(var(--muted-foreground)) }
</style>
'''

HEAD = ('<title>Чипы форматов · 12 вариантов</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Цветные чипы · 12</h1>
    <p class="text-caption-14">Один набор — видео, квиз, инструкция и «Бесплатно» — в разных цветовых форматах.
      Под каждым вариантом строка урока, чтобы видеть чипы в контексте.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — поставлю в приложение.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
