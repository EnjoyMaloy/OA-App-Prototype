import { MessageCircle, Send, Linkedin } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { STORE_LINKS } from "@/lib/storeLinks";
import logo from "@/assets/main_full_logo_color_light.png.asset.json";

const XIcon = ({ className = "" }: { className?: string }) => (
  <svg viewBox="0 0 24 24" fill="currentColor" className={className} aria-hidden="true">
    <path d="M18.24 2.25h3.31l-7.23 8.26 8.5 11.24h-6.65l-5.22-6.82-5.97 6.82H1.66l7.73-8.84L1.25 2.25h6.82l4.71 6.23 5.46-6.23Zm-1.16 17.52h1.83L7.01 4.13H5.05l12.03 15.64Z" />
  </svg>
);

type LinkItem = { ru: string; en: string; href: string; badge?: string };

const columns: { titleRu: string; titleEn: string; links: LinkItem[] }[] = [
  {
    titleRu: "Приложение",
    titleEn: "App",
    links: [
      { ru: "Telegram Mini App", en: "Telegram Mini App", href: "#" },
      { ru: "App Store", en: "App Store", href: STORE_LINKS.appStore },
      { ru: "Google Play", en: "Google Play", href: STORE_LINKS.googlePlay },
    ],
  },
  {
    titleRu: "Продукты",
    titleEn: "Products",
    links: [
      { ru: "Обзор", en: "Overview", href: "#" },
      { ru: "Studio", en: "Studio", href: "#", badge: "JOIN WL" },
      { ru: "The Early Squirrels", en: "The Early Squirrels", href: "https://squirrels.open-academy.app/" },
    ],
  },
  {
    titleRu: "Документы",
    titleEn: "Documents",
    links: [
      { ru: "Вайтпейпер", en: "Whitepaper", href: "#" },
      { ru: "Токеномика", en: "Tokenomics", href: "#" },
      { ru: "Политика конфиденциальности", en: "Privacy Policy", href: "#" },
      { ru: "Условия использования", en: "Terms of Use", href: "#" },
      { ru: "Политика cookie", en: "Cookie Policy", href: "#" },
    ],
  },
  {
    titleRu: "Контакты",
    titleEn: "Contacts",
    links: [
      { ru: "Поддержка", en: "Support", href: "#" },
      { ru: "Обратная связь", en: "Feedback", href: "#" },
      { ru: "Партнёрство", en: "Partnership", href: "#" },
    ],
  },
];

const socials = [
  { label: "Chat", Icon: MessageCircle, href: "#" },
  { label: "Telegram", Icon: Send, href: "#" },
  { label: "X", Icon: XIcon, href: "#" },
  { label: "LinkedIn", Icon: Linkedin, href: "#" },
];

const Footer = () => {
  const { lang } = useLanguage();
  const ru = lang === "ru";

  return (
    <footer className="hidden md:block border-t border-border mt-10">
      <div className="px-4 md:px-9 py-10 md:py-12">
        <div className="grid grid-cols-2 gap-x-8 gap-y-10 md:grid-cols-[150px_0.9fr_1fr_1.5fr_1fr_1fr] md:gap-x-8">
          {/* Логотип */}
          <div className="col-span-2 md:col-span-1">
            <img src={logo.url} alt="Open Academy" className="h-12 object-contain" />
          </div>

          {/* Колонки со ссылками */}
          {columns.map((col) => (
            <div key={col.titleEn}>
              <p className="text-[13px] font-medium uppercase tracking-[0.06em] text-muted-foreground mb-5">
                {ru ? col.titleRu : col.titleEn}
              </p>
              <ul className="flex flex-col gap-5">
                {col.links.map((link) => (
                  <li key={link.en}>
                    <a
                      href={link.href}
                      target={link.href.startsWith("http") ? "_blank" : undefined}
                      rel={link.href.startsWith("http") ? "noopener noreferrer" : undefined}
                      className="inline-flex items-center gap-2 text-[16px] text-foreground hover:text-primary transition-colors"
                    >
                      {ru ? link.ru : link.en}
                      {link.badge && (
                        <span className="text-[10px] font-semibold tracking-wide text-primary-foreground bg-primary px-1.5 py-0.5 rounded">
                          {link.badge}
                        </span>
                      )}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}

          {/* Соцсети */}
          <div>
            <p className="text-[13px] font-medium uppercase tracking-[0.06em] text-muted-foreground mb-5">
              {ru ? "Мы в соцсетях" : "Follow us"}
            </p>
            <div className="flex items-center gap-2.5">
              {socials.map(({ label, Icon, href }) => (
                <a
                  key={label}
                  href={href}
                  aria-label={label}
                  className="w-11 h-11 rounded-[10px] border border-border flex items-center justify-center text-muted-foreground hover:text-foreground hover:bg-muted transition-colors"
                >
                  <Icon className="w-[18px] h-[18px]" />
                </a>
              ))}
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
