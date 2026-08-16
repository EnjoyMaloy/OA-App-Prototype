import { useEffect, useRef, useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { Home, LayoutGrid, BookOpen, FileText, User, ArrowLeft, GraduationCap, Trophy, Search, X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";

interface NavItem {
  label: string;
  icon: React.ElementType;
  path: string;
  disabled?: boolean;
  action?: () => void;
}

/**
 * Стеклянная подложка «пилюли» и круглых кнопок.
 * Контур собран как у Apple: внешняя тонкая тёмная грань и внутренняя светлая —
 * вместе они отделяют стекло от любой подложки под ним.
 */
const GLASS =
  "backdrop-blur-2xl backdrop-saturate-150 bg-background/75 border border-black/[0.08] dark:border-white/15 " +
  "shadow-[0_10px_30px_rgba(0,0,0,0.12),inset_0_0_0_1px_rgba(255,255,255,0.55),inset_0_1px_0_rgba(255,255,255,0.9)] " +
  "dark:shadow-[0_10px_30px_rgba(0,0,0,0.5),inset_0_0_0_1px_rgba(255,255,255,0.08)]";

const BottomNav = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { t } = useLanguage();
  const [searchOpen, setSearchOpen] = useState(false);
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);

  const isMyCourses = location.pathname === "/my-courses";
  const currentTab = new URLSearchParams(location.search).get("tab");

  useEffect(() => {
    if (searchOpen) inputRef.current?.focus();
  }, [searchOpen]);

  const submitSearch = (e: React.FormEvent) => {
    e.preventDefault();
    const q = query.trim();
    navigate(q ? `/catalog?q=${encodeURIComponent(q)}` : "/catalog");
    setSearchOpen(false);
    setQuery("");
  };

  const defaultItems: NavItem[] = [
    { label: t("sidebar.home"), icon: Home, path: "/" },
    { label: t("sidebar.catalog"), icon: LayoutGrid, path: "/catalog" },
    { label: t("sidebar.myCourses"), icon: BookOpen, path: "/my-courses" },
    { label: t("bottomNav.profile"), icon: User, path: "/profile" },
  ];

  const courseItems: NavItem[] = [
    { label: t("bottomNav.back"), icon: ArrowLeft, path: "back", action: () => navigate("/") },
    { label: t("bottomNav.course"), icon: GraduationCap, path: "/my-courses" },
    { label: t("sidebar.instructions"), icon: FileText, path: "/my-courses?tab=instructions" },
    { label: t("bottomNav.quest"), icon: Trophy, path: "/quest", disabled: true },
  ];

  const items = isMyCourses ? courseItems : defaultItems;

  const isActive = (item: NavItem) => {
    if (item.disabled) return false;
    if (isMyCourses && item.path === "/my-courses?tab=instructions") return currentTab === "instructions";
    if (isMyCourses && item.path === "/my-courses") return !currentTab;
    if (item.path === "/") return location.pathname === "/";
    // Без авторизации профиль уводит на /auth — пункт остаётся выбранным
    if (item.path === "/profile") return location.pathname === "/profile" || location.pathname === "/auth";
    return location.pathname.startsWith(item.path);
  };

  return (
    <>
      {/* Поиск: лист над таб-баром */}
      {searchOpen && (
        <div className="fixed inset-0 z-[60] md:hidden" onClick={() => setSearchOpen(false)}>
          <div className="absolute inset-0 bg-black/20 backdrop-blur-[2px]" />
          <form
            onSubmit={submitSearch}
            onClick={(e) => e.stopPropagation()}
            className={`absolute left-3 right-3 bottom-[calc(88px+env(safe-area-inset-bottom))] flex items-center gap-2 rounded-full pl-4 pr-2 h-14 ${GLASS}`}
          >
            <Search className="w-5 h-5 flex-shrink-0 text-muted-foreground" />
            <input
              ref={inputRef}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder={t("nav.searchCourse")}
              className="flex-1 min-w-0 bg-transparent border-none text-[17px] text-foreground placeholder:text-muted-foreground focus:outline-none"
            />
            <button
              type="button"
              onClick={() => setSearchOpen(false)}
              className="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center text-muted-foreground hover:text-foreground transition-colors"
              aria-label="close-search"
            >
              <X className="w-5 h-5" />
            </button>
          </form>
        </div>
      )}

      {/* Плавающая панель: «пилюля» с разделами + отдельная кнопка поиска */}
      <div className="fixed inset-x-0 bottom-0 z-50 md:hidden pointer-events-none px-3 pb-[max(12px,env(safe-area-inset-bottom))]">
        <div className="flex items-end gap-2 pointer-events-auto">
          <nav className={`flex-1 min-w-0 flex items-center justify-around gap-1 h-16 px-2 rounded-full ${GLASS}`}>
            {items.map((item) => {
              const active = isActive(item);
              const Icon = item.icon;

              // Без подписей: активный раздел помечается только светлой капсулой
              const content = (
                <Icon
                  strokeWidth={2.2}
                  className={`w-[22px] h-[22px] flex-shrink-0 ${
                    item.disabled ? "text-foreground/25" : "text-foreground"
                  }`}
                />
              );

              // Выбранный пункт — широкая капсула вокруг иконки
              const className = `flex items-center justify-center h-12 rounded-full transition-all flex-shrink-0 ${
                active ? "w-[74px] bg-foreground/[0.12]" : "w-12"
              }`;

              if (item.action) {
                return (
                  <button key={item.path} onClick={item.action} className={className} aria-label={item.label}>
                    {content}
                  </button>
                );
              }

              if (item.disabled) {
                return (
                  <div key={item.path} className={`${className} cursor-default`} aria-label={item.label}>
                    {content}
                  </div>
                );
              }

              return (
                <Link key={item.path} to={item.path} className={className} aria-label={item.label}>
                  {content}
                </Link>
              );
            })}
          </nav>

          <button
            onClick={() => setSearchOpen(true)}
            className={`flex-shrink-0 w-16 h-16 rounded-full flex items-center justify-center active:scale-95 transition-transform ${GLASS}`}
            aria-label={t("nav.searchCourse")}
          >
            <Search strokeWidth={2.2} className="w-[22px] h-[22px] text-foreground" />
          </button>
        </div>
      </div>
    </>
  );
};

export default BottomNav;
