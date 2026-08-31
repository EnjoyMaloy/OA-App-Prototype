# Страница-передача смарт-баннера разработчику сайта
from html import escape

OUT = '/tmp/claude-0/-home-user-OA-App-Prototype/056fdada-85c9-5018-8a39-7019b881de22/scratchpad/smart-banner-spec.html'

REACT = '''import { useEffect, useRef, useState } from "react";

/**
 * Смарт-баннер приложения.
 * Липнет к верху страницы, закрывается крестиком, инвертируется по теме.
 */
export function SmartAppBanner({ installed = false, href = "#", lang = "ru" }) {
  const [hidden, setHidden] = useState(false);
  const ref = useRef(null);

  // Высота баннера уходит в CSS-переменную: по ней сдвигаются фиксированные
  // элементы страницы (кнопка «назад», шапка и т.п.)
  useEffect(() => {
    const root = document.documentElement;
    const apply = () => {
      const h = !hidden && ref.current ? ref.current.offsetHeight : 0;
      root.style.setProperty("--app-banner-h", `${h}px`);
    };
    apply();
    window.addEventListener("resize", apply);
    return () => {
      window.removeEventListener("resize", apply);
      root.style.setProperty("--app-banner-h", "0px");
    };
  }, [hidden, lang]);

  if (hidden) return null;

  const t = {
    ru: { install: "В приложении удобнее", open: "Открыть в приложении", get: "Установить", launch: "Открыть", close: "Закрыть" },
    en: { install: "Faster in the app", open: "Open in the app", get: "Get", launch: "Open", close: "Dismiss" },
  }[lang];

  return (
    <div
      ref={ref}
      className="sticky top-0 z-[60] flex items-center gap-3 px-3 py-2.5 md:hidden bg-[#141416] dark:bg-[#F4F4F6]"
      style={{ paddingTop: "max(10px, env(safe-area-inset-top))" }}
    >
      <button
        onClick={() => setHidden(true)}
        aria-label={t.close}
        className="w-7 h-7 shrink-0 flex items-center justify-center rounded-full text-white/45 dark:text-black/35"
      >
        {/* иконка «крестик» 18×18 */}
      </button>

      <span
        aria-hidden
        className="w-11 h-11 shrink-0 rounded-[11px] flex items-center justify-center text-white text-[24px] font-bold leading-none"
        style={{
          background: "linear-gradient(160deg, #B98CFF 0%, #7B2EFF 100%)",
          boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14)",
        }}
      >
        A
      </span>

      <span className="min-w-0 flex-1 flex flex-col">
        <span className="text-[16px] font-normal leading-[1.1] text-white/95 dark:text-black/95 truncate">
          Open Academy
        </span>
        <span className="text-[13px] leading-[1.15] mt-[3px] truncate text-white/50 dark:text-black/45">
          {installed ? t.open : t.install}
        </span>
      </span>

      <a
        href={href}
        className="shrink-0 inline-flex items-center justify-center h-8 px-4 rounded-full text-[15px] font-medium text-white/95"
        style={{ background: "#0A84FF" }}
      >
        {installed ? t.launch : t.get}
      </a>
    </div>
  );
}'''

HTML_CODE = '''<div class="app-banner" id="appBanner">
  <button class="app-banner__close" type="button" aria-label="Закрыть">
    <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor"
         stroke-width="2.2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>
  </button>

  <span class="app-banner__icon" aria-hidden="true">A</span>

  <span class="app-banner__text">
    <span class="app-banner__title">Open Academy</span>
    <span class="app-banner__subtitle">В приложении удобнее</span>
  </span>

  <a class="app-banner__cta" href="https://apps.apple.com/...">Установить</a>
</div>'''

CSS_CODE = '''.app-banner {
  position: sticky;
  top: 0;
  z-index: 60;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 10px 12px;
  padding-top: max(10px, env(safe-area-inset-top));
  background: #141416;
}
@media (min-width: 768px) { .app-banner { display: none } }          /* только мобильные */
@media (prefers-color-scheme: dark) { .app-banner { background: #F4F4F6 } }

.app-banner__close {
  flex: 0 0 auto; width: 28px; height: 28px; display: flex;
  align-items: center; justify-content: center;
  border: 0; background: none; cursor: pointer; color: rgba(255,255,255,.45);
}
.app-banner__icon {
  flex: 0 0 auto; width: 44px; height: 44px; border-radius: 11px;
  display: flex; align-items: center; justify-content: center;
  font-size: 24px; font-weight: 700; line-height: 1; color: #fff;
  background: linear-gradient(160deg, #B98CFF 0%, #7B2EFF 100%);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.14);
}
.app-banner__text { flex: 1; min-width: 0; display: flex; flex-direction: column }
.app-banner__title,
.app-banner__subtitle { overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.app-banner__title { font-size: 16px; font-weight: 400; line-height: 1.1; color: rgba(255,255,255,.95) }
.app-banner__subtitle { font-size: 13px; line-height: 1.15; margin-top: 3px; color: rgba(255,255,255,.5) }
.app-banner__cta {
  flex: 0 0 auto; height: 32px; padding: 0 16px; border-radius: 999px;
  display: inline-flex; align-items: center; justify-content: center;
  font-size: 15px; font-weight: 500; text-decoration: none;
  color: rgba(255,255,255,.95); background: #0A84FF;
}
@media (prefers-color-scheme: dark) {
  .app-banner__close { color: rgba(0,0,0,.35) }
  .app-banner__title { color: rgba(0,0,0,.95) }
  .app-banner__subtitle { color: rgba(0,0,0,.45) }
}'''

JS_CODE = '''const banner = document.getElementById("appBanner");
const root = document.documentElement;

// Высота баннера — в переменную, чтобы фиксированные элементы вставали под ним:
//   .back-button { top: calc(var(--app-banner-h, 0px) + 14px) }
const syncHeight = () => root.style.setProperty("--app-banner-h", banner ? banner.offsetHeight + "px" : "0px");
syncHeight();
addEventListener("resize", syncHeight);

banner.querySelector(".app-banner__close").addEventListener("click", () => {
  banner.remove();
  root.style.setProperty("--app-banner-h", "0px");
  localStorage.setItem("app-banner-dismissed", "1");   // не показываем снова
});

if (localStorage.getItem("app-banner-dismissed")) {
  banner.remove();
  root.style.setProperty("--app-banner-h", "0px");
}'''


def demo(installed, dark, lang="ru"):
    title = "Open Academy"
    sub = {
        ("ru", False): "В приложении удобнее",
        ("ru", True): "Открыть в приложении",
        ("en", False): "Faster in the app",
        ("en", True): "Open in the app",
    }[(lang, installed)]
    cta = {("ru", False): "Установить", ("ru", True): "Открыть",
           ("en", False): "Get", ("en", True): "Open"}[(lang, installed)]
    cls = "demo demo--light" if dark else "demo"
    return ('<div class="' + cls + '">'
            '<span class="demo__close"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" '
            'stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></span>'
            '<span class="demo__icon">A</span>'
            '<span class="demo__text"><span class="demo__title">' + title + '</span>'
            '<span class="demo__sub">' + sub + '</span></span>'
            '<span class="demo__cta">' + cta + '</span>'
            '</div>')


def code(lang, src):
    return ('<figure class="code"><figcaption>' + lang + '</figcaption>'
            '<pre><code>' + escape(src) + '</code></pre></figure>')


SPEC_ROWS = [
    ("Ширина", "во всю ширину экрана, без скруглений и теней"),
    ("Высота", "64 px при стандартном шрифте; задаётся содержимым, не фиксируется"),
    ("Отступы", "12 px по бокам, 10 px сверху и снизу; сверху — max(10px, safe-area-inset-top)"),
    ("Иконка", "44×44, радиус 11, фирменный градиент #B98CFF → #7B2EFF"),
    ("Название", "16 px, вес 400, межстрочный 1.1, белый 95%"),
    ("Подпись", "13 px, межстрочный 1.15, отступ сверху 3 px, белый 50%"),
    ("Кнопка", "высота 32, радиус 999, 15 px medium, фон #0A84FF — синий App Store, без капса"),
    ("Крестик", "28×28, иконка 18, белый 45%; область нажатия не меньше 44×44 на проде"),
    ("Тема", "на светлой странице баннер тёмный (#141416), на тёмной — светлый (#F4F4F6)"),
    ("Прилипание", "position: sticky; top: 0; z-index выше шапки"),
    ("Только мобильные", "скрыт от 768 px и выше"),
    ("Закрытие", "крестик убирает баннер и пишет флаг в localStorage"),
    ("Смещение контента", "высота уходит в --app-banner-h; фиксированные элементы считают top от неё"),
]

COPY_ROWS = [
    ("Приложение не установлено", "В приложении удобнее", "Установить", "Faster in the app", "Get"),
    ("Приложение установлено", "Открыть в приложении", "Открыть", "Open in the app", "Open"),
]

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
    --violet: #7B2EFF;
    --code-bg: #14161B;
    --code-ink: #E7E9EF;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --ink: #ECEDF1;
      --ink-soft: #9AA0AC;
      --paper: #0D0F13;
      --card: #14171D;
      --line: #262B33;
      --code-bg: #090A0D;
      --code-ink: #DFE2E9;
    }
  }
  :root[data-theme="dark"] {
    --ink: #ECEDF1;
    --ink-soft: #9AA0AC;
    --paper: #0D0F13;
    --card: #14171D;
    --line: #262B33;
    --code-bg: #090A0D;
    --code-ink: #DFE2E9;
  }

  * { box-sizing: border-box }
  body {
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 16px;
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
  }
  .wrap { max-width: 880px; margin: 0 auto; padding: 56px 20px 96px; display: flex; flex-direction: column; gap: 48px }

  header { display: flex; flex-direction: column; gap: 14px }
  .eyebrow { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12px; letter-spacing: .12em;
             text-transform: uppercase; color: var(--ink-soft) }
  h1 { margin: 0; font-size: 38px; line-height: 1.12; font-weight: 600; letter-spacing: -.02em; text-wrap: balance }
  .lead { margin: 0; max-width: 62ch; color: var(--ink-soft) }

  section { display: flex; flex-direction: column; gap: 18px }
  h2 { margin: 0; font-size: 21px; font-weight: 600; letter-spacing: -.01em }
  h2 .num { font-family: "IBM Plex Mono", monospace; font-size: 13px; color: var(--blue); margin-right: 10px }
  .hint { margin: 0; color: var(--ink-soft); font-size: 15px; max-width: 62ch }

  /* превью баннера */
  .previews { display: grid; gap: 16px; grid-template-columns: 1fr; }
  @media (min-width: 720px) { .previews { grid-template-columns: 1fr 1fr } }
  .frame { border: 1px solid var(--line); border-radius: 16px; overflow: hidden; background: var(--card) }
  .frame__label { font-family: "IBM Plex Mono", monospace; font-size: 12px; letter-spacing: .06em;
                  text-transform: uppercase; color: var(--ink-soft); padding: 12px 14px;
                  border-bottom: 1px solid var(--line) }
  .frame__body { padding: 0 }
  .frame__page { padding: 18px 14px 22px; font-size: 14px; color: var(--ink-soft) }
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
  .demo__title { font-size: 16px; font-weight: 400; line-height: 1.1; color: rgba(255,255,255,.95) }
  .demo__sub { font-size: 13px; line-height: 1.15; margin-top: 3px; color: rgba(255,255,255,.5) }
  .demo--light .demo__title { color: rgba(0,0,0,.95) }
  .demo--light .demo__sub { color: rgba(0,0,0,.45) }
  .demo__cta { flex: 0 0 auto; height: 32px; padding: 0 16px; border-radius: 999px; display: inline-flex;
               align-items: center; justify-content: center; font-size: 15px; font-weight: 500;
               color: rgba(255,255,255,.95); background: #0A84FF }

  /* таблицы */
  .table { width: 100%; border-collapse: collapse; font-size: 15px }
  .table th { text-align: left; font-family: "IBM Plex Mono", monospace; font-size: 12px; letter-spacing: .06em;
              text-transform: uppercase; color: var(--ink-soft); font-weight: 500; padding: 0 0 10px }
  .table td { padding: 11px 0; border-top: 1px solid var(--line); vertical-align: top }
  .table td:first-child { width: 34%; padding-right: 20px; color: var(--ink) }
  .table td:not(:first-child) { color: var(--ink-soft) }
  .scroll { overflow-x: auto }
  .copy td:first-child { width: 28% }
  .copy td + td { width: 18% }

  /* код */
  .code { margin: 0; border-radius: 14px; overflow: hidden; border: 1px solid var(--line) }
  .code figcaption { font-family: "IBM Plex Mono", monospace; font-size: 12px; letter-spacing: .06em;
                     text-transform: uppercase; color: var(--ink-soft); padding: 11px 14px;
                     background: var(--card); border-bottom: 1px solid var(--line) }
  .code pre { margin: 0; padding: 16px; overflow-x: auto; background: var(--code-bg) }
  .code code { font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 13px; line-height: 1.6;
               color: var(--code-ink); white-space: pre }

  .stack { display: flex; flex-direction: column; gap: 14px }
  .note { border-left: 2px solid var(--blue); padding: 2px 0 2px 14px; color: var(--ink-soft); font-size: 15px }
  code.inline { font-family: "IBM Plex Mono", monospace; font-size: 13px; background: var(--card);
                border: 1px solid var(--line); border-radius: 6px; padding: 1px 6px; color: var(--ink) }
</style>

<div class="wrap">
  <header>
    <p class="eyebrow">Open Academy · передача в вёрстку</p>
    <h1>Смарт-баннер приложения</h1>
    <p class="lead">Полоса над контентом мобильного сайта: предлагает поставить приложение, а если оно уже стоит —
      открыть страницу в нём. Ниже живые превью, размеры и готовый код: React с Tailwind и чистые HTML + CSS + JS.</p>
  </header>

  <section>
    <h2><span class="num">01</span>Как выглядит</h2>
    <p class="hint">Баннер всегда контрастен странице: на светлой теме он тёмный, на тёмной — светлый.
      Состояний два — приложение не установлено и установлено.</p>
    <div class="previews">
      <div class="frame">
        <p class="frame__label">Светлая страница · не установлено</p>
        <div class="frame__body">DEMO_A<div class="frame__page frame__page--light">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Светлая страница · установлено</p>
        <div class="frame__body">DEMO_B<div class="frame__page frame__page--light">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Тёмная страница · не установлено</p>
        <div class="frame__body">DEMO_C<div class="frame__page frame__page--dark">контент сайта</div></div>
      </div>
      <div class="frame">
        <p class="frame__label">Светлая страница · English</p>
        <div class="frame__body">DEMO_D<div class="frame__page frame__page--light">site content</div></div>
      </div>
    </div>
  </section>

  <section>
    <h2><span class="num">02</span>Параметры</h2>
    <div class="scroll">
      <table class="table">
        <thead><tr><th>Параметр</th><th>Значение</th></tr></thead>
        <tbody>SPEC_ROWS</tbody>
      </table>
    </div>
    <p class="note">Про <code class="inline">--app-banner-h</code>: баннер прилипает к верху, поэтому любые
      фиксированные элементы страницы должны вставать под ним. Компонент пишет свою высоту в переменную, а они
      считают отступ так: <code class="inline">top: calc(var(--app-banner-h, 0px) + 14px)</code>.</p>
  </section>

  <section>
    <h2><span class="num">03</span>Тексты</h2>
    <p class="hint">Подпись объясняет выгоду, кнопка называет действие одним словом. «Установить» и «Get» —
      формулировки сторов: в App Store бесплатное приложение подписано Get, в Google Play — Install.</p>
    <div class="scroll">
      <table class="table copy">
        <thead><tr><th>Состояние</th><th>RU подпись</th><th>RU кнопка</th><th>EN подпись</th><th>EN кнопка</th></tr></thead>
        <tbody>COPY_ROWS</tbody>
      </table>
    </div>
  </section>

  <section>
    <h2><span class="num">04</span>Код</h2>
    <p class="hint">Первый вариант — как компонент собран у нас: React и Tailwind. Дальше тот же баннер на чистых
      HTML, CSS и JS, если на сайте нет React.</p>
    <div class="stack">
      CODE_REACT
      CODE_HTML
      CODE_CSS
      CODE_JS
    </div>
  </section>

  <section>
    <h2><span class="num">05</span>Поведение</h2>
    <div class="scroll">
      <table class="table">
        <tbody>
          <tr><td>Показ</td><td>только мобильная ширина (&lt; 768 px) и только если баннер не закрывали раньше</td></tr>
          <tr><td>Ссылка кнопки</td><td>не установлено — страница приложения в сторе; установлено — диплинк
            вида <code class="inline">openacademy://course/123</code> с фолбэком на стор</td></tr>
          <tr><td>Определение платформы</td><td>по user-agent: iOS — App Store и «Get», Android — Google Play
            и «Install»</td></tr>
          <tr><td>Закрытие</td><td>крестик прячет баннер и запоминает выбор; вернуть показ — очистить ключ
            <code class="inline">app-banner-dismissed</code></td></tr>
          <tr><td>Доступность</td><td>у крестика <code class="inline">aria-label</code>, область нажатия
            не меньше 44×44, у иконки <code class="inline">aria-hidden</code></td></tr>
        </tbody>
      </table>
    </div>
  </section>
</div>
'''

spec_rows = "".join('<tr><td>' + k + '</td><td>' + v + '</td></tr>' for k, v in SPEC_ROWS)
copy_rows = "".join('<tr><td>' + r[0] + '</td><td>' + r[1] + '</td><td>' + r[2] + '</td><td>' + r[3]
                    + '</td><td>' + r[4] + '</td></tr>' for r in COPY_ROWS)

out = (HTML
       .replace("DEMO_A", demo(False, False))
       .replace("DEMO_B", demo(True, False))
       .replace("DEMO_C", demo(False, True))
       .replace("DEMO_D", demo(True, False, "en"))
       .replace("SPEC_ROWS", spec_rows)
       .replace("COPY_ROWS", copy_rows)
       .replace("CODE_REACT", code("React + Tailwind", REACT))
       .replace("CODE_HTML", code("HTML", HTML_CODE))
       .replace("CODE_CSS", code("CSS", CSS_CODE))
       .replace("CODE_JS", code("JavaScript", JS_CODE)))

open(OUT, 'w').write(out)
print("готово:", len(out), "байт")
