# Страница-передача смарт-баннера: только визуальные параметры
OUT = '/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/smart-banner-spec.html'


def demo(installed, light_banner, lang="ru"):
    sub = {
        ("ru", False): "Учиться удобнее",
        ("ru", True): "Открыть в приложении",
        ("en", False): "Faster in the app",
        ("en", True): "Open in the app",
    }[(lang, installed)]
    cta = {("ru", False): "Скачать", ("ru", True): "Открыть",
           ("en", False): "Get", ("en", True): "Open"}[(lang, installed)]
    cls = "demo demo--light" if light_banner else "demo"
    return ('<div class="' + cls + '">'
            '<span class="demo__close"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" '
            'stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></span>'
            '<span class="demo__icon">A</span>'
            '<span class="demo__text"><span class="demo__title">Open Academy</span>'
            '<span class="demo__sub">' + sub + '</span></span>'
            '<span class="demo__cta">' + cta + '</span>'
            '</div>')


# только то, что нужно кодеру: цвета, кегли, вес, прозрачности, интерлиньяж, размер кнопки
SPEC = [
    ("Подложка", [
        ("Тёмный баннер", "#141416"),
        ("Светлый баннер", "#F4F4F6"),
    ]),
    ("Название", [
        ("Кегль", "16 px"),
        ("Вес", "500"),
        ("Интерлиньяж", "1.1"),
        ("Цвет на тёмном", "#FFFFFF, прозрачность 95%"),
        ("Цвет на светлом", "#000000, прозрачность 95%"),
    ]),
    ("Подпись", [
        ("Кегль", "13 px"),
        ("Вес", "400"),
        ("Интерлиньяж", "1.15"),
        ("Отступ от названия", "3 px"),
        ("Цвет на тёмном", "#FFFFFF, прозрачность 50%"),
        ("Цвет на светлом", "#000000, прозрачность 45%"),
    ]),
    ("Кнопка", [
        ("Размер", "высота 32 px, боковые отступы 16 px, радиус 999"),
        ("Фон", "#0A84FF"),
        ("Текст", "15 px, вес 500, #FFFFFF, прозрачность 95%"),
    ]),
    ("Крестик", [
        ("Размер", "28 × 28, иконка 18 px"),
        ("Цвет на тёмном", "#FFFFFF, прозрачность 45%"),
        ("Цвет на светлом", "#000000, прозрачность 35%"),
    ]),
    ("Иконка приложения", [
        ("Размер", "44 × 44, радиус 11 px"),
        ("Заливка", "градиент 160°, #B98CFF → #7B2EFF"),
    ]),
]

rows = ""
for group, items in SPEC:
    rows += '<tr class="group"><td colspan="2">' + group + '</td></tr>'
    for k, v in items:
        rows += '<tr><td>' + k + '</td><td>' + v + '</td></tr>'

HTML = '''<title>Смарт-баннер Open Academy</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
  :root {
    --ink: #14161B;
    --ink-soft: #5C626E;
    --paper: #FBFBFC;
    --card: #FFFFFF;
    --line: #E3E5EB;
    --blue: #0A84FF;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --ink: #ECEDF1; --ink-soft: #9AA0AC; --paper: #0D0F13; --card: #14171D; --line: #262B33;
    }
  }
  :root[data-theme="dark"] {
    --ink: #ECEDF1; --ink-soft: #9AA0AC; --paper: #0D0F13; --card: #14171D; --line: #262B33;
  }

  * { box-sizing: border-box }
  body {
    margin: 0; background: var(--paper); color: var(--ink);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 16px; line-height: 1.55; -webkit-font-smoothing: antialiased;
  }
  .wrap { max-width: 760px; margin: 0 auto; padding: 56px 20px 96px; display: flex; flex-direction: column; gap: 40px }

  header { display: flex; flex-direction: column; gap: 12px }
  .eyebrow { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12px; letter-spacing: .12em;
             text-transform: uppercase; color: var(--ink-soft) }
  h1 { margin: 0; font-size: 36px; line-height: 1.12; font-weight: 600; letter-spacing: -.02em; text-wrap: balance }
  .lead { margin: 0; max-width: 60ch; color: var(--ink-soft) }

  section { display: flex; flex-direction: column; gap: 16px }
  h2 { margin: 0; font-size: 20px; font-weight: 600; letter-spacing: -.01em }

  .previews { display: grid; gap: 14px; grid-template-columns: 1fr }
  @media (min-width: 700px) { .previews { grid-template-columns: 1fr 1fr } }
  .frame { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--card) }
  .frame__label { font-family: "IBM Plex Mono", monospace; font-size: 12px; letter-spacing: .06em;
                  text-transform: uppercase; color: var(--ink-soft); padding: 12px 14px;
                  border-bottom: 1px solid var(--line); margin: 0 }
  .frame__page { padding: 16px 14px 20px; font-size: 14px }
  .frame__page--dark { background: #0E1014; color: #8A909C }
  .frame__page--light { background: #F1EEFA; color: #6B6478 }

  .demo { display: flex; align-items: center; gap: 12px; padding: 10px 12px; background: #141416 }
  .demo--light { background: #F4F4F6 }
  .demo__close { flex: 0 0 auto; width: 28px; height: 28px; display: flex; align-items: center;
                 justify-content: center; color: rgba(255,255,255,.45) }
  .demo--light .demo__close { color: rgba(0,0,0,.35) }
  .demo__icon { flex: 0 0 auto; width: 44px; height: 44px; border-radius: 11px; display: flex; align-items: center;
                justify-content: center; font-size: 24px; font-weight: 700; line-height: 1; color: #fff;
                background: linear-gradient(160deg, #B98CFF 0%, #7B2EFF 100%);
                box-shadow: inset 0 0 0 1px rgba(255,255,255,.14) }
  .demo__text { flex: 1; min-width: 0; display: flex; flex-direction: column }
  .demo__title, .demo__sub { overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
  .demo__title { font-size: 16px; font-weight: 500; line-height: 1.1; color: rgba(255,255,255,.95) }
  .demo__sub { font-size: 13px; line-height: 1.15; margin-top: 3px; color: rgba(255,255,255,.5) }
  .demo--light .demo__title { color: rgba(0,0,0,.95) }
  .demo--light .demo__sub { color: rgba(0,0,0,.45) }
  .demo__cta { flex: 0 0 auto; height: 32px; padding: 0 16px; border-radius: 999px; display: inline-flex;
               align-items: center; justify-content: center; font-size: 15px; font-weight: 500;
               color: rgba(255,255,255,.95); background: #0A84FF }

  .table { width: 100%; border-collapse: collapse; font-size: 15px }
  .table td { padding: 10px 0; border-top: 1px solid var(--line); vertical-align: top }
  .table td:first-child { width: 42%; padding-right: 20px }
  .table td:last-child { color: var(--ink-soft); font-family: "IBM Plex Mono", monospace; font-size: 14px }
  .table .group td { padding-top: 26px; border-top: 0; font-family: "IBM Plex Sans", sans-serif;
                     font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--blue) }
  .table tr:first-child td { padding-top: 0 }
  .scroll { overflow-x: auto }
</style>

<div class="wrap">
  <header>
    <p class="eyebrow">Open Academy · смарт-баннер</p>
    <h1>Полоса с приложением</h1>
    <p class="lead">Баннер над контентом мобильного сайта. На светлой странице он тёмный, на тёмной — светлый.</p>
  </header>

  <section>
    <div class="previews">
      <div class="frame">
        <p class="frame__label">Светлая страница · не установлено</p>
        <div>DEMO_A<div class="frame__page frame__page--light">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Светлая страница · установлено</p>
        <div>DEMO_B<div class="frame__page frame__page--light">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Тёмная страница · не установлено</p>
        <div>DEMO_C<div class="frame__page frame__page--dark">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Тёмная страница · установлено</p>
        <div>DEMO_D<div class="frame__page frame__page--dark">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">English · not installed</p>
        <div>DEMO_E<div class="frame__page frame__page--light">site content</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">English · installed</p>
        <div>DEMO_F<div class="frame__page frame__page--light">site content</div></div>
      </div>
    </div>
  </section>

  <section>
    <h2>Значения</h2>
    <div class="scroll">
      <table class="table"><tbody>SPEC_ROWS</tbody></table>
    </div>
  </section>
</div>
'''

out = (HTML
       .replace("DEMO_A", demo(False, False))
       .replace("DEMO_B", demo(True, False))
       .replace("DEMO_C", demo(False, True))
       .replace("DEMO_D", demo(True, True))
       .replace("DEMO_E", demo(False, False, "en"))
       .replace("DEMO_F", demo(True, False, "en"))
       .replace("SPEC_ROWS", rows))

open(OUT, 'w').write(out)
print("готово:", len(out), "байт")
