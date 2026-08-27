# Генератор черновика: 10 вариантов шторки урока (взгляд «эппловского» дизайнера)
OUT = '/home/user/OA-App-Prototype/prototypes/lesson-sheet.html'

TITLE = "Стратегии торговли на вторичном рынке"
DESC = "Разберём основные стратегии покупки и продажи подарков."

def ico(d, w=2, size=18, fill="none"):
    return ('<svg viewBox="0 0 24 24" width="' + str(size) + '" height="' + str(size) + '" fill="' + fill + '" '
            'stroke="currentColor" stroke-width="' + str(w) + '" stroke-linecap="round" stroke-linejoin="round">'
            + d + '</svg>')

PLAY = ico('<path d="M9 6.2v11.6L18.4 12z"/>', 3.4, 16, "currentColor")
BOOK = ico('<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>')
QUIZ = ico('<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3 2.4V13"/><path d="M12 16.5v.01"/>')
DOC = ico('<path d="M5 3h9l5 5v13a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M14 3v6h5"/><path d="M8 13h8M8 17h5"/>')
CHEV = ico('<path d="m9 18 6-6-6-6"/>', 2.2, 17)
LOCK = ico('<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>')
CHECK = ico('<path d="M20 6 9 17l-5-5"/>', 3, 18)
STAR = ico('<path d="M12 2.6 14.9 9l6.6.6-5 4.4 1.5 6.4L12 17l-6 3.4L7.5 14l-5-4.4L9.1 9z"/>', 1.8, 17)
FIRE = ico('<path d="M12 2c1 3.5-1.5 4.5-2.5 6.5C8.3 10.9 9 13 11 13c1.6 0 2-1.3 1.8-2.6 2 1.4 3.2 3.2 3.2 5.1 0 3-2.5 5.5-5.5 5.5S5 18.5 5 15.5C5 11 10.5 9 12 2z"/>', 1.8, 16)

BUF = []


def sheet(code, name, cap, body, height=90):
    BUF.append('  <section class="variant">\n'
               '    <h2>' + code + '. ' + name + '</h2>\n'
               '    <p class="variant__cap">' + cap + '</p>\n'
               '    <div class="stage">\n'
               '      <div class="map"></div>\n'
               '      <div class="sheet"><span class="grab"></span>\n' + body + '\n      </div>\n'
               '    </div>\n'
               '  </section>\n')


def kicker(t):
    return '        <p class="kicker">' + t + '</p>'


def h(t):
    return '        <h3 class="ttl">' + t + '</h3>'


def desc(t=DESC):
    return '        <p class="desc">' + t + '</p>'


def bar(pct=45, label="Пройдено", right="45%"):
    return ('        <div class="prow"><span>' + label + '</span><span class="pval">' + right + '</span></div>\n'
            '        <div class="track"><i style="width:' + str(pct) + '%"></i></div>')


def btn(t="Продолжить", cls="btn"):
    return '        <button class="' + cls + '">' + t + '</button>'


def rows(items):
    out = ['        <div class="list">']
    for icon, title, meta, extra in items:
        out.append('          <div class="li ' + extra + '"><span class="li__i">' + icon + '</span>'
                   '<span class="li__t">' + title + '</span>'
                   '<span class="li__m">' + meta + '</span>'
                   '<span class="li__c">' + CHEV + '</span></div>')
    out.append('        </div>')
    return "\n".join(out)


def chips(items):
    return ('        <div class="chips">'
            + "".join('<span class="chip">' + i + '</span>' for i in items)
            + '</div>')


# ---------------------------------------------------------------- 1
sheet("A1", "Тихий лист",
      "Ничего лишнего: надзаголовок с номером и временем, крупное имя урока, тонкий прогресс и одно действие. "
      "Так выглядит типовой iOS-шит: одна мысль на экран.",
      "\n".join([kicker("Урок 6 · 12 мин"), h(TITLE), desc(), bar(), btn()]))

# ---------------------------------------------------------------- 2
sheet("A2", "Кольцо прогресса",
      "Прогресс уходит в кольцо у заголовка и перестаёт занимать строку. Под именем — сухая строка фактов.",
      "\n".join([
          '        <div class="head">',
          '          <div class="head__t">' + kicker("Урок 6").strip() + h(TITLE).strip() + '</div>',
          '          <span class="ring"><svg viewBox="0 0 44 44"><circle class="r-bg" cx="22" cy="22" r="19"/>'
          '<circle class="r-on" cx="22" cy="22" r="19" stroke-dasharray="119.4" stroke-dashoffset="65.7"/></svg>'
          '<i>45%</i></span>',
          '        </div>',
          desc(),
          '        <p class="facts">Видео · 12 мин · Инструкция</p>',
          btn(),
      ]))

# ---------------------------------------------------------------- 3
sheet("A3", "Что внутри",
      "Урок разложен на части: видно, что придётся посмотреть, решить и прочитать. Ожидания совпадают с реальностью.",
      "\n".join([
          kicker("Урок 6 · 12 мин"), h(TITLE),
          rows([(PLAY, "Видео", "6 мин", ""), (QUIZ, "Квиз", "5 вопросов", ""), (DOC, "Конспект", "PDF", "")]),
          btn(),
      ]))

# ---------------------------------------------------------------- 4
sheet("A4", "Список действий",
      "Тот же материал, но каждая строка — действие, как в настройках iOS. Можно вернуться к любой части урока.",
      "\n".join([
          kicker("Урок 6"), h(TITLE),
          rows([(PLAY, "Смотреть видео", "6 мин", "li--done"),
                (QUIZ, "Пройти квиз", "5 вопросов", ""),
                (DOC, "Открыть конспект", "", "")]),
          bar(45, "Пройдено", "45%"),
          btn("Продолжить с видео"),
      ]))

# ---------------------------------------------------------------- 5
sheet("A5", "С обложкой",
      "Кадр урока сверху: шит перестаёт быть текстовым и получает опору для взгляда. Кнопка — поверх низа обложки.",
      "\n".join([
          '        <div class="cover"><span class="cover__play">' + PLAY + '</span>'
          '<span class="cover__t">12 мин</span></div>',
          kicker("Урок 6"), h(TITLE), desc(), bar(), btn(),
      ]))

# ---------------------------------------------------------------- 6
sheet("A6", "Награда",
      "Мотивация вынесена в чипы: сколько баллов даёт урок и как он держит стрик. Уместно там, где есть геймификация.",
      "\n".join([
          kicker("Урок 6 · 12 мин"), h(TITLE), desc(),
          chips([STAR + "+50 баллов", FIRE + "Стрик 5 дней"]),
          bar(), btn(),
      ]))

# ---------------------------------------------------------------- 7
sheet("A7", "Урок в курсе",
      "Сегменты показывают место урока в курсе: шесть закрыто, этот идёт, впереди ещё два. Прогресс без процентов.",
      "\n".join([
          kicker("Урок 6 из 8"), h(TITLE), desc(),
          '        <div class="segs">' + "".join(
              '<i class="' + ("on" if i < 5 else ("now" if i == 5 else "")) + '"></i>' for i in range(8)) + '</div>',
          btn(),
      ]))

# ---------------------------------------------------------------- 8
sheet("A8", "Две кнопки",
      "Главное действие — заливкой, второстепенное — текстом. По гайдлайну Apple вторая кнопка не спорит с первой.",
      "\n".join([
          kicker("Урок 6 · 12 мин"), h(TITLE), desc(), bar(),
          btn(), '        <button class="btn btn--plain">Открыть инструкцию</button>',
      ]))

# ---------------------------------------------------------------- 9
sheet("A9", "Закрытый урок",
      "Состояние, которого сейчас нет: урок ещё не открыт. Объясняем причину и даём выход, а не глухой замок.",
      "\n".join([
          '        <div class="lockhead"><span class="lockhead__i">' + LOCK + '</span>'
          '<span class="hgroup">' + kicker("Урок 6 · 12 мин").strip() + h(TITLE).strip() + '</span></div>',
          desc("Откроется, когда пройдёте пятый урок. Осталось 4 минуты видео и квиз."),
          '        <div class="track"><i style="width:82%"></i></div>',
          '        <p class="facts">Урок 5 пройден на 82%</p>',
          btn("Вернуться к уроку 5"),
          '        <button class="btn btn--plain">Что внутри урока</button>',
      ]))

# ---------------------------------------------------------------- 10
sheet("A10", "Пройденный урок",
      "Финальное состояние: подтверждаем результат, показываем оценку квиза и предлагаем следующий шаг, а не только «пройти снова».",
      "\n".join([
          '        <div class="donehead"><span class="donehead__i">' + CHECK + '</span>'
          '<span class="hgroup"><p class="kicker">Урок 6 · пройден 12 апреля</p>'
          '<h3 class="ttl">' + TITLE + '</h3></span></div>',
          '        <div class="stats"><div><b>8/10</b><span>Квиз</span></div>'
          '<div><b>12 мин</b><span>Время</span></div><div><b>+50</b><span>Баллов</span></div></div>',
          btn("Следующий урок"),
          '        <button class="btn btn--plain">Пройти снова</button>',
      ]))

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; line-height: 1.4; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }

  /* сцена: кусок карты и шит поверх */
  .stage { border-radius: 22px; overflow: hidden; background: hsl(268 65% 93%) }
  .map { height: 78px; background-image: radial-gradient(circle, hsl(268 52% 87%) 11px, transparent 12px),
                                          radial-gradient(circle, hsl(268 52% 87%) 11px, transparent 12px);
         background-size: 44px 44px, 44px 44px; background-position: 0 0, 22px 22px }

  .sheet { position: relative; background: hsl(var(--background)); border-radius: 26px 26px 22px 22px;
           padding: 8px 20px 20px; display: flex; flex-direction: column }
  .grab { align-self: center; width: 36px; height: 5px; border-radius: 3px; background: #D8D8DC; margin-bottom: 14px }

  .kicker { margin: 0; font-size: 13px; font-weight: 500; letter-spacing: .04em; text-transform: uppercase;
            color: hsl(var(--muted-foreground)) }
  .ttl { margin: 6px 0 0; font-size: 22px; font-weight: 600; line-height: 1.2; letter-spacing: -.02em }
  .desc { margin: 8px 0 0; font-size: 15px; line-height: 1.45; color: hsl(var(--muted-foreground)) }
  .facts { margin: 10px 0 0; font-size: 14px; color: hsl(var(--muted-foreground)) }

  .prow { display: flex; justify-content: space-between; align-items: baseline; margin-top: 18px;
          font-size: 14px; color: hsl(var(--muted-foreground)) }
  .pval { font-weight: 600; color: hsl(var(--foreground)) }
  .track { height: 5px; border-radius: 3px; background: hsl(var(--muted)); margin-top: 8px; overflow: hidden }
  .track i { display: block; height: 100%; border-radius: 3px; background: hsl(var(--primary)) }

  .btn { margin-top: 18px; height: 54px; border-radius: 16px; background: hsl(var(--primary)); color: #fff;
         font: inherit; font-size: 17px; font-weight: 500; border: 0; cursor: pointer }
  .btn--plain { margin-top: 6px; height: 46px; background: none; color: hsl(var(--primary)); font-weight: 500 }

  /* заголовок с кольцом */
  .head { display: flex; align-items: flex-start; gap: 14px }
  .head__t { flex: 1; min-width: 0 }
  .ring { position: relative; flex: 0 0 auto; width: 46px; height: 46px }
  .ring svg { width: 46px; height: 46px; transform: rotate(-90deg) }
  .r-bg { fill: none; stroke: hsl(var(--muted)); stroke-width: 4 }
  .r-on { fill: none; stroke: hsl(var(--primary)); stroke-width: 4; stroke-linecap: round }
  .ring i { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
            font-size: 12px; font-weight: 600; font-style: normal }

  /* строки-действия */
  .list { margin-top: 16px; border-radius: 14px; background: hsl(var(--muted)); overflow: hidden }
  .li { display: flex; align-items: center; gap: 12px; padding: 13px 14px; font-size: 16px }
  .li + .li { box-shadow: inset 0 1px 0 hsl(var(--border) / .8) }
  .li__i { display: flex; color: hsl(var(--primary)) }
  .li__t { flex: 1; min-width: 0 }
  .li__m { font-size: 14px; color: hsl(var(--muted-foreground)) }
  .li__c { display: flex; color: hsl(var(--muted-foreground) / .7) }
  .li--done .li__t { color: hsl(var(--muted-foreground)) }
  .li--done .li__i { color: hsl(152 45% 42%) }

  /* обложка */
  .cover { position: relative; height: 132px; border-radius: 16px; margin-bottom: 16px;
           background: linear-gradient(135deg, #E8DCFB, #A66CFF); display: flex; align-items: center;
           justify-content: center }
  .cover__play { width: 46px; height: 46px; border-radius: 50%; background: rgba(255,255,255,.92);
                 color: hsl(var(--primary)); display: flex; align-items: center; justify-content: center }
  .cover__t { position: absolute; right: 10px; bottom: 10px; font-size: 12px; font-weight: 600; color: #fff;
              background: rgba(0,0,0,.35); padding: 3px 8px; border-radius: 999px }

  /* чипы */
  .chips { display: flex; gap: 8px; margin-top: 14px; flex-wrap: wrap }
  .chip { display: inline-flex; align-items: center; gap: 6px; height: 30px; padding: 0 12px; border-radius: 999px;
          background: hsl(var(--muted)); font-size: 14px; font-weight: 500 }
  .chip svg { color: hsl(var(--primary)) }

  /* сегменты курса */
  .segs { display: flex; gap: 5px; margin-top: 18px }
  .segs i { flex: 1; height: 5px; border-radius: 3px; background: hsl(var(--muted)) }
  .segs i.on { background: hsl(var(--primary) / .45) }
  .segs i.now { background: hsl(var(--primary)) }

  /* закрытый и пройденный */
  .lockhead, .donehead { display: flex; gap: 14px; align-items: flex-start }
  .lockhead__i, .donehead__i { flex: 0 0 auto; width: 42px; height: 42px; border-radius: 50%;
                               display: flex; align-items: center; justify-content: center; margin-top: 2px }
  .lockhead__i { background: hsl(var(--muted)); color: hsl(var(--muted-foreground)) }
  .donehead__i { background: hsl(152 55% 92%); color: hsl(152 55% 32%) }
  .hgroup { flex: 1; min-width: 0 }
  .lockhead p, .lockhead h3, .donehead p, .donehead h3 { margin: 0 }
  .lockhead h3, .donehead h3 { margin-top: 6px }

  .stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 18px;
           border-radius: 14px; background: hsl(var(--muted)); padding: 14px 6px }
  .stats div { display: flex; flex-direction: column; align-items: center; gap: 3px }
  .stats b { font-size: 19px; font-weight: 600 }
  .stats span { font-size: 13px; color: hsl(var(--muted-foreground)) }
</style>
'''

HEAD = ('<title>Шторка урока · 10 вариантов</title>\n' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Шторка урока · 10</h1>
    <p class="text-caption-14">Разбор текущего шита и десять пересборок: что показывать до входа в урок, как подавать
      прогресс и какое действие делать главным. Кнопка везде в брендовом фиолетовом — чёрная спорила с палитрой
      приложения, а на карте урока и так много контраста.</p>
  </div>

''')
TAIL = '''
  <p class="note">Скажи код — соберу в приложении.</p>

</div>
'''

open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", len(BUF))
