import { forwardRef } from "react";

export const AppleIcon = ({ className = "" }: { className?: string }) => (
  <svg viewBox="0 0 24 24" fill="currentColor" className={className} aria-hidden="true">
    <path d="M16.4 12.7c0-2.2 1.8-3.3 1.9-3.3-1-1.5-2.7-1.7-3.3-1.7-1.4-.1-2.7.8-3.4.8-.7 0-1.8-.8-3-.8-1.5 0-2.9.9-3.7 2.3-1.6 2.7-.4 6.8 1.1 9 .7 1.1 1.6 2.3 2.8 2.3 1.1 0 1.5-.7 2.9-.7 1.3 0 1.7.7 2.9.7 1.2 0 2-1.1 2.7-2.2.9-1.2 1.2-2.4 1.2-2.5 0 0-2.3-.9-2.3-3.5ZM14.2 6.2c.6-.7 1-1.7.9-2.7-.9 0-2 .6-2.6 1.3-.6.6-1.1 1.7-.9 2.6 1 .1 2-.5 2.6-1.2Z" />
  </svg>
);

/** Google Play в фирменных цветах. Без градиентов и defs — чтобы не ловить
 *  конфликт одинаковых svg-id, когда иконка встречается на странице несколько раз. */
export const GooglePlayIcon = ({ className = "" }: { className?: string }) => (
  <svg viewBox="0 0 24 24" fill="none" className={className} aria-hidden="true">
    {/* Все четыре сегмента сходятся в одной точке (13.4, 12), внешние рёбра
        идут из углов сгиба в правый кончик — иначе логотип «разъезжается». */}
    <path d="M3 2.2 13.4 12 3 21.8Z" fill="#00A0FF" />
    <path d="M3 2.2 16.8 9.88 13.4 12Z" fill="#00E676" />
    <path d="M3 21.8 16.8 14.12 13.4 12Z" fill="#FF3A44" />
    <path d="M16.8 9.88 20.6 12 16.8 14.12 13.4 12Z" fill="#FFCE00" />
  </svg>
);

/** Цветная плитка App Store — как иконка приложения на домашнем экране */
export const AppStoreTile = ({ className = "" }: { className?: string }) => (
  <span
    className={`inline-flex items-center justify-center rounded-[9px] ${className}`}
    style={{ background: "linear-gradient(180deg, #1FBCFD 0%, #0578F5 100%)" }}
  >
    <svg
      viewBox="0 0 24 24"
      fill="none"
      stroke="#fff"
      strokeWidth="2.2"
      strokeLinecap="round"
      className="w-[62%] h-[62%]"
      aria-hidden="true"
    >
      <path d="M12 5.8 6.6 16.8" />
      <path d="m12 5.8 5.4 11" />
      <path d="M8.2 13.6h8.6" />
    </svg>
  </span>
);

/** Цветная плитка Google Play */
export const GooglePlayTile = ({ className = "" }: { className?: string }) => (
  <span
    className={`inline-flex items-center justify-center rounded-[9px] bg-white border border-border ${className}`}
  >
    <GooglePlayIcon className="w-[58%] h-[58%]" />
  </span>
);

/** Классический бейдж стора: светлая кнопка, иконка + две строки */
type StoreBadgeProps = {
  store: "appStore" | "googlePlay";
  /** внешняя ссылка на стор; без неё бейдж рендерится кнопкой (например, как триггер поповера) */
  href?: string;
  onClick?: () => void;
  className?: string;
};

export const StoreBadge = forwardRef<HTMLElement, StoreBadgeProps>(
  ({ store, href, onClick, className = "", ...rest }, ref) => {
    const isApple = store === "appStore";
    const cls = `flex items-center justify-center gap-2.5 h-[54px] px-5 min-w-[160px] rounded-[14px] bg-background border border-border hover:bg-muted transition-colors whitespace-nowrap ${className}`;

    const content = (
      <>
        {isApple ? (
          <AppleIcon className="w-6 h-6 text-foreground flex-shrink-0" />
        ) : (
          <GooglePlayIcon className="w-6 h-6 flex-shrink-0" />
        )}
        <span className="text-[17px] font-medium text-foreground leading-none">
          {isApple ? "App Store" : "Google Play"}
        </span>
      </>
    );

    if (!href) {
      return (
        <button
          type="button"
          ref={ref as React.Ref<HTMLButtonElement>}
          onClick={onClick}
          className={cls}
          {...rest}
        >
          {content}
        </button>
      );
    }

    return (
      <a
        ref={ref as React.Ref<HTMLAnchorElement>}
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        onClick={onClick}
        className={cls}
        {...rest}
      >
        {content}
      </a>
    );
  }
);
StoreBadge.displayName = "StoreBadge";
