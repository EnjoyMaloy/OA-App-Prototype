# 20 вариантов управления сортировкой в каталоге
OUT = '/home/user/OA-App-Prototype/prototypes/sort.html'

CHEV = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>')
ARROWS = ('<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round"><path d="M7 4v16"/><path d="m3 8 4-4 4 4"/>'
          '<path d="M17 20V4"/><path d="m13 16 4 4 4-4"/></svg>')
DOWN = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
        'stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14"/><path d="m6 13 6 6 6-6"/></svg>')
UP = DOWN.replace('d="M12 5v14"/><path d="m6 13 6 6 6-6"', 'd="M12 19V5"/><path d="m6 11 6-6 6 6"')
CHECK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" '
         'stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>')
X = ('<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" '
     'stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>')
CLOCK = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
         'stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>')
FIRE = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2c1 3.5-1.5 4.5-2.5 6.5'
        'C8.3 10.9 9 13 11 13c1.6 0 2-1.3 1.8-2.6 2 1.4 3.2 3.2 3.2 5.1 0 3-2.5 5.5-5.5 5.5S5 18.5 5 15.5c0-4.5 5.5-6.5 7-13.5z"/></svg>')
STAR = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5l2.9 5.9 6.5.9-4.7 4.6'
        '1.1 6.5-5.8-3-5.8 3 1.1-6.5L2.6 9.3l6.5-.9z"/></svg>')

BUF = []
def block(code, name, cap, html):
    BUF.append(f'''  <section class="variant">
    <h2>{code}. {name}</h2>
    <p class="variant__cap">{cap}</p>
{html}
  </section>
''')

block("S1", "Как сейчас", "Текстовая ссылка со стрелкой у правого края.",
      f'''    <div class="right"><button class="ghost">Сначала новые{CHEV}</button></div>''')

block("S2", "Пилюля-селект", "Значение в плашке — заметнее и попадаешь пальцем.",
      f'''    <div class="right"><button class="sel">{ARROWS}<span>Сначала новые</span>{CHEV}</button></div>''')

block("S3", "Сегмент-контрол", "Три режима сразу на виду, переключение в один тап.",
      '''    <div class="seg">
      <button class="seg__i seg__i--on">Новые</button>
      <button class="seg__i">Популярные</button>
      <button class="seg__i">Дешевле</button>
    </div>''')

block("S4", "Чипы сортировки", "Тот же язык, что у фильтров-чипов.",
      f'''    <div class="row">
      <button class="chip chip--on">{CLOCK}Новые</button>
      <button class="chip">{FIRE}Популярные</button>
      <button class="chip">{STAR}По рейтингу</button>
      <button class="chip">Дешевле</button>
    </div>''')

block("S5", "Только иконка", "Минимум места: иконка сортировки без подписи.",
      f'''    <div class="right"><button class="icobtn">{ARROWS}</button></div>''')

block("S6", "Результат и сортировка", "Слева сколько нашлось, справа порядок.",
      f'''    <div class="bar"><span class="muted">24 курса</span><button class="ghost">Сначала новые{CHEV}</button></div>''')

block("S7", "Открытое меню", "Выпадающий список с галочкой у текущего значения.",
      f'''    <div class="right rel">
      <button class="sel sel--open">Сначала новые{CHEV}</button>
      <div class="menu">
        <button class="menu__i menu__i--on">Сначала новые{CHECK}</button>
        <button class="menu__i">Сначала популярные</button>
        <button class="menu__i">По рейтингу</button>
        <button class="menu__i">Сначала дешёвые</button>
      </div>
    </div>''')

block("S8", "Лист сортировки", "Нижний лист с радио-списком — удобно большим пальцем.",
      f'''    <div class="sheet">
      <span class="grabber"></span>
      <span class="sheet__t">Сортировка</span>
      <button class="li li--on"><span>Сначала новые</span><i class="radio radio--on"></i></button>
      <button class="li"><span>Сначала популярные</span><i class="radio"></i></button>
      <button class="li"><span>По рейтингу</span><i class="radio"></i></button>
      <button class="li"><span>Сначала дешёвые</span><i class="radio"></i></button>
    </div>''')

block("S9", "Поле и направление", "Отдельно «по чему», отдельно «в какую сторону».",
      f'''    <div class="row">
      <button class="sel">По дате{CHEV}</button>
      <button class="icobtn icobtn--pair">{DOWN}</button>
    </div>''')

block("S10", "Табы", "Сортировка как вкладки над списком.",
      '''    <div class="tabs">
      <button class="tab tab--on">Новые</button>
      <button class="tab">Популярные</button>
      <button class="tab">По рейтингу</button>
    </div>''')

block("S11", "В поле поиска", "Иконка сортировки живёт справа в строке поиска.",
      f'''    <div class="search">
      <span class="search__i">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
      </span>
      <span class="search__p">Найти курс...</span>
      <button class="search__b">{ARROWS}</button>
    </div>''')

block("S12", "Одной плашкой", "Количество и сортировка в общей серой панели.",
      f'''    <div class="panel"><span class="muted">Найдено 24</span><span class="dot"></span><button class="ghost">Сначала новые{CHEV}</button></div>''')

block("S13", "Со сбросом", "Активная сортировка снимается крестиком.",
      f'''    <div class="right"><button class="chip chip--on">Сначала дешёвые{X}</button></div>''')

block("S14", "Тихая подпись", "Мелкий серый текст с иконкой — почти незаметно.",
      f'''    <div class="right"><button class="quiet">{ARROWS}<span>сначала новые</span></button></div>''')

block("S15", "Двухпозиционный", "Переключатель на два состояния — если вариантов всего два.",
      '''    <div class="seg seg--two">
      <button class="seg__i seg__i--on">Новые</button>
      <button class="seg__i">Популярные</button>
    </div>''')

block("S16", "Экшен-шит", "Список действий в стиле iOS с кнопкой «Отмена».",
      '''    <div class="sheet sheet--as">
      <div class="as">
        <span class="as__t">Сортировать по</span>
        <button class="as__i as__i--on">Дате добавления</button>
        <button class="as__i">Популярности</button>
        <button class="as__i">Рейтингу</button>
      </div>
      <button class="as__cancel">Отмена</button>
    </div>''')

block("S17", "Стеклянная пилюля", "Плавает над списком, как таб-бар.",
      f'''    <div class="floatbed">
      <div class="ghostcards"><span></span><span></span></div>
      <button class="float glassy">{ARROWS}<span>Сначала новые</span>{CHEV}</button>
    </div>''')

block("S18", "Липкая полоса", "Панель прилипает к верху при прокрутке.",
      f'''    <div class="sticky">
      <span class="muted">24 курса</span>
      <button class="sel sel--sm">Новые{CHEV}</button>
    </div>
    <div class="ghostcards ghostcards--sm"><span></span></div>''')

block("S19", "Кнопка с бейджем", "Подпись «Сортировка», текущее значение — бейджем.",
      f'''    <div class="right"><button class="sel">Сортировка<i class="badge">Новые</i>{CHEV}</button></div>''')

block("S20", "Направление в сегменте", "Стрелки задают порядок внутри выбранного поля.",
      f'''    <div class="row">
      <button class="sel">По рейтингу{CHEV}</button>
      <div class="seg seg--icons">
        <button class="seg__i seg__i--on">{UP}</button>
        <button class="seg__i">{DOWN}</button>
      </div>
    </div>''')

CSS = '''
<style>
  .variant { display: flex; flex-direction: column; gap: 10px }
  .variant__cap { font-size: 13px; color: hsl(var(--muted-foreground)); margin: 0 }
  .variant h2 { font-size: 17px; font-weight: 600; margin: 0 }
  button { font: inherit; border: 0; background: none; cursor: pointer; color: inherit }

  .right { display: flex; justify-content: flex-end }
  .rel { position: relative }
  .row { display: flex; gap: 8px; overflow-x: auto; margin: 0 -16px; padding: 0 16px 2px; scrollbar-width: none }
  .row::-webkit-scrollbar { display: none }
  .bar, .panel, .sticky { display: flex; align-items: center; justify-content: space-between; gap: 10px }
  .muted { font-size: 15px; color: hsl(var(--muted-foreground)) }

  .ghost { display: inline-flex; align-items: center; gap: 4px; font-size: 15px }
  .quiet { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: hsl(var(--muted-foreground)) }
  .sel { display: inline-flex; align-items: center; gap: 8px; height: 40px; padding: 0 12px 0 14px;
    border-radius: 999px; background: hsl(var(--muted)); font-size: 15px; font-weight: 500; white-space: nowrap }
  .sel--sm { height: 34px; font-size: 14px }
  .sel--open { background: hsl(var(--background)); box-shadow: 0 0 0 1px hsl(var(--border)) }
  .icobtn { width: 40px; height: 40px; border-radius: 12px; background: hsl(var(--muted));
    display: inline-flex; align-items: center; justify-content: center }
  .icobtn--pair { border-radius: 999px }
  .badge { font-style: normal; padding: 3px 8px; border-radius: 999px; background: hsl(var(--background));
    font-size: 13px; font-weight: 600 }

  .chip { flex: 0 0 auto; display: inline-flex; align-items: center; gap: 6px; height: 38px; padding: 0 14px;
    border-radius: 999px; background: hsl(var(--muted)); font-size: 15px; font-weight: 500; white-space: nowrap }
  .chip--on { background: #0F0F0F; color: #fff }

  .seg { display: flex; gap: 4px; padding: 4px; border-radius: 14px; background: hsl(var(--muted)) }
  .seg--two { max-width: 260px }
  .seg--icons { padding: 3px; border-radius: 12px }
  .seg__i { flex: 1; display: inline-flex; align-items: center; justify-content: center; gap: 6px; height: 36px;
    padding: 0 12px; border-radius: 10px; font-size: 15px; font-weight: 500; color: hsl(var(--muted-foreground));
    white-space: nowrap }
  .seg--icons .seg__i { flex: 0 0 auto; width: 38px; height: 32px; padding: 0 }
  .seg__i--on { background: hsl(var(--background)); color: hsl(var(--foreground)); box-shadow: 0 1px 3px rgba(15,15,15,.14) }

  .tabs { display: flex; gap: 18px; border-bottom: 1px solid hsl(var(--border)) }
  .tab { padding: 8px 0 10px; font-size: 16px; font-weight: 500; color: hsl(var(--muted-foreground));
    border-bottom: 2.5px solid transparent }
  .tab--on { color: hsl(var(--foreground)); border-color: hsl(var(--primary)) }

  .menu { position: absolute; top: 46px; right: 0; min-width: 220px; padding: 6px; border-radius: 14px;
    background: hsl(var(--background)); box-shadow: 0 12px 30px rgba(15,15,15,.16), 0 0 0 1px hsl(var(--border)) }
  .menu__i { display: flex; align-items: center; justify-content: space-between; gap: 10px; width: 100%;
    padding: 10px 10px; border-radius: 10px; font-size: 15px; text-align: left }
  .menu__i--on { color: hsl(var(--primary)); font-weight: 500; background: hsl(var(--primary) / .08) }

  .sheet { display: flex; flex-direction: column; gap: 10px; padding: 10px 14px 14px;
    border-radius: 22px 22px 16px 16px; background: hsl(var(--background));
    box-shadow: 0 -8px 30px rgba(15,15,15,.14), 0 0 0 1px hsl(var(--border)) }
  .sheet--as { background: none; box-shadow: none; padding: 0; gap: 8px }
  .grabber { width: 40px; height: 4px; border-radius: 999px; background: rgba(15,15,15,.18); align-self: center }
  .sheet__t { font-size: 20px; font-weight: 600; margin-bottom: 2px }
  .li { display: flex; align-items: center; justify-content: space-between; padding: 12px 2px; font-size: 16px;
    border-bottom: 1px solid hsl(var(--border)) }
  .li:last-child { border-bottom: 0 }
  .li--on { color: hsl(var(--primary)); font-weight: 500 }
  .radio { width: 20px; height: 20px; border-radius: 999px; box-shadow: inset 0 0 0 1.5px rgba(15,15,15,.25) }
  .radio--on { box-shadow: inset 0 0 0 6px hsl(var(--primary)) }

  .as { display: flex; flex-direction: column; border-radius: 16px; overflow: hidden; background: hsl(var(--muted)) }
  .as__t { padding: 12px; font-size: 13px; color: hsl(var(--muted-foreground)); text-align: center }
  .as__i { padding: 15px; font-size: 17px; border-top: 1px solid hsl(var(--background)) }
  .as__i--on { color: hsl(var(--primary)); font-weight: 600 }
  .as__cancel { padding: 15px; border-radius: 16px; background: hsl(var(--background));
    box-shadow: 0 0 0 1px hsl(var(--border)); font-size: 17px; font-weight: 600 }

  .search { display: flex; align-items: center; gap: 10px; height: 52px; padding: 0 8px 0 16px;
    border-radius: 999px; background: hsl(var(--muted)) }
  .search__i { color: hsl(var(--muted-foreground)); display: inline-flex }
  .search__p { flex: 1; font-size: 16px; color: hsl(var(--muted-foreground)) }
  .search__b { width: 38px; height: 38px; border-radius: 999px; background: hsl(var(--background));
    display: inline-flex; align-items: center; justify-content: center }

  .panel { padding: 10px 14px; border-radius: 14px; background: hsl(var(--muted)) }
  .dot { width: 4px; height: 4px; border-radius: 999px; background: rgba(15,15,15,.25) }

  .sticky { padding: 10px 12px; border-radius: 14px; background: hsl(var(--background));
    box-shadow: 0 6px 18px rgba(15,15,15,.10), 0 0 0 1px hsl(var(--border)) }
  .ghostcards { display: flex; flex-direction: column; gap: 10px }
  .ghostcards span { display: block; height: 84px; border-radius: 16px; background: hsl(var(--muted)) }
  .ghostcards--sm span { height: 56px; margin-top: 10px }

  .floatbed { position: relative }
  .float { position: absolute; left: 50%; bottom: 14px; transform: translateX(-50%);
    display: inline-flex; align-items: center; gap: 8px; height: 46px; padding: 0 18px; border-radius: 999px;
    font-size: 16px; font-weight: 500; color: #0F0F0F }
  .glassy { background: rgba(255,255,255,.6); -webkit-backdrop-filter: blur(24px) saturate(180%);
    backdrop-filter: blur(24px) saturate(180%);
    box-shadow: 0 10px 28px rgba(15,15,15,.18), inset 0 1px 0 rgba(255,255,255,.9), inset 0 0 0 1px rgba(255,255,255,.5) }
</style>
'''

HEAD = '''<title>Сортировка · 20</title>
''' + CSS + '''
<div class="screen stack stack-8">

  <div class="stack stack-2">
    <h1 class="text-h1">Сортировка · 20</h1>
    <p class="text-caption-14">Двадцать способов переключить порядок курсов в каталоге: от тихой ссылки до нижнего листа.</p>
  </div>

'''
TAIL = '''
  <p class="note">Скажи код — соберу в каталоге.</p>

</div>
'''
open(OUT, 'w').write(HEAD + "".join(BUF) + TAIL)
print("вариантов:", sum(1 for b in BUF if b.strip().startswith("<section")))
