import { useEffect, useRef, useState } from "react";
import { X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";

interface SmartAppBannerProps {
  /** Приложение уже стоит на устройстве — тогда предлагаем открыть, а не скачать */
  installed?: boolean;
  /** Куда ведёт кнопка: диплинк в приложение или страница загрузки */
  href?: string;
}

/**
 * Смарт-баннер приложения: тёмная полоса над контентом с иконкой,
 * названием, подписью и компактной кнопкой. Закрывается крестиком.
 */
const SmartAppBanner = ({ installed = false, href = "#" }: SmartAppBannerProps) => {
  const { lang } = useLanguage();
  const [hidden, setHidden] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  // Высота баннера уезжает в переменную: по ней сдвигаются фиксированные кнопки экранов
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

  const subtitle = installed
    ? lang === "ru"
      ? "Открой в приложении"
      : "Open in the app"
    : lang === "ru"
      ? "Установи наше приложение"
      : "Install our app";

  const action = installed
    ? lang === "ru"
      ? "Открыть"
      : "Open"
    : lang === "ru"
      ? "Скачать"
      : "Install";

  return (
    <div
      ref={ref}
      // Баннер липнет к верху экрана и остаётся при прокрутке
      // На светлой теме баннер тёмный, на тёмной — светлый: он всегда контрастен странице
      className="sticky top-0 z-[60] flex items-center gap-3 px-3 py-2.5 md:hidden bg-[#141416] dark:bg-[#F4F4F6]"
      style={{ paddingTop: "max(10px, env(safe-area-inset-top))" }}
    >
      <button
        onClick={() => setHidden(true)}
        aria-label={lang === "ru" ? "Закрыть" : "Dismiss"}
        className="w-7 h-7 flex-shrink-0 flex items-center justify-center rounded-full text-white/50 dark:text-black/40 active:scale-95 transition-transform"
      >
        <X className="w-[18px] h-[18px]" strokeWidth={2.2} />
      </button>

      {/* Иконка приложения: брендовая плитка с фирменной «А» */}
      <span
        aria-hidden
        className="w-11 h-11 flex-shrink-0 rounded-[11px] flex items-center justify-center text-white text-[24px] font-bold leading-none"
        style={{
          background: "linear-gradient(160deg, #B98CFF 0%, #7B2EFF 100%)",
          boxShadow: "inset 0 0 0 1px rgba(255,255,255,0.14)",
        }}
      >
        A
      </span>

      <span className="min-w-0 flex-1 flex flex-col">
        <span className="text-[16px] font-semibold leading-[1.1] text-white dark:text-[#141416] truncate">
          Open Academy
        </span>
        <span className="text-[13px] leading-[1.15] truncate text-white/55 dark:text-black/50">
          {subtitle}
        </span>
      </span>

      <a
        href={href}
        // Голубая кнопка как в App Store
        className="flex-shrink-0 inline-flex items-center justify-center h-8 px-4 rounded-full text-[15px] font-medium text-white active:brightness-90 transition-[filter]"
        style={{ background: "#0A84FF" }}
      >
        {action}
      </a>
    </div>
  );
};

export default SmartAppBanner;
