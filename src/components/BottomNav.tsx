import { Link, useLocation, useNavigate } from "react-router-dom";
import { Home, LayoutGrid, BookOpen, FileText, User, ArrowLeft, GraduationCap, Trophy, Search } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";

interface NavItem {
  label: string;
  icon: React.ElementType;
  path: string;
  disabled?: boolean;
  action?: () => void;
}

/** Стеклянная подложка «пилюли» и круглых кнопок — описана в index.css */
const GLASS = "glass";

const BottomNav = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { t } = useLanguage();
  // Пункты курса нужны на карте уроков; сам раздел «Мои курсы» — обычный список
  const isLessonMap = location.pathname.endsWith("/lessons");
  const currentTab = new URLSearchParams(location.search).get("tab");

  // Поиск живёт в каталоге: кнопка уводит туда и фокусирует поле сверху
  const openSearch = () => navigate("/catalog?focus=1");

  const defaultItems: NavItem[] = [
    { label: t("sidebar.home"), icon: Home, path: "/" },
    { label: t("sidebar.catalog"), icon: LayoutGrid, path: "/catalog" },
    { label: t("sidebar.myCourses"), icon: BookOpen, path: "/my-courses" },
    { label: t("bottomNav.profile"), icon: User, path: "/profile" },
  ];

  const courseItems: NavItem[] = [
    { label: t("bottomNav.back"), icon: ArrowLeft, path: "back", action: () => navigate("/") },
    { label: t("bottomNav.course"), icon: GraduationCap, path: location.pathname },
    { label: t("sidebar.instructions"), icon: FileText, path: `${location.pathname}?tab=instructions` },
    { label: t("bottomNav.quest"), icon: Trophy, path: "/quest", disabled: true },
  ];

  const items = isLessonMap ? courseItems : defaultItems;

  const isActive = (item: NavItem) => {
    if (item.disabled) return false;
    if (isLessonMap && item.path.endsWith("?tab=instructions")) return currentTab === "instructions";
    if (isLessonMap && item.path === location.pathname) return !currentTab;
    if (item.path === "/") return location.pathname === "/";
    // Без авторизации профиль уводит на /auth — пункт остаётся выбранным
    if (item.path === "/profile") return location.pathname === "/profile" || location.pathname === "/auth";
    return location.pathname.startsWith(item.path);
  };

  return (
    <>
      {/* Плавающая панель: «пилюля» с разделами + отдельная кнопка поиска */}
      <div className="fixed inset-x-0 bottom-0 z-50 md:hidden pointer-events-none px-3 pb-[max(12px,env(safe-area-inset-bottom))]">
        <div className="flex items-end gap-2 pointer-events-auto">
          <nav className={`flex-1 min-w-0 flex items-stretch gap-1 h-16 p-1 rounded-full ${GLASS}`}>
            {items.map((item) => {
              const active = isActive(item);
              const Icon = item.icon;

              // Активный раздел — брендовый фиолетовый и залитая иконка
              const content = (
                <Icon
                  strokeWidth={2.2}
                  fill={active ? "currentColor" : "none"}
                  className={`w-[22px] h-[22px] flex-shrink-0 transition-colors ${
                    item.disabled ? "text-foreground/25" : active ? "text-primary" : "text-foreground"
                  }`}
                />
              );

              // Ячейки одной ширины, поэтому иконки не сдвигаются при переключении,
              // а подсветка занимает всю высоту пилюли
              const className = `flex-1 basis-0 min-w-0 flex items-center justify-center h-full rounded-full transition-colors ${
                active ? "bg-primary/[0.14]" : ""
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
            onClick={openSearch}
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
