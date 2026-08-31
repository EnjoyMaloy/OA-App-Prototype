import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";
import { useLanguage } from "@/contexts/LanguageContext";
import flagEn from "@/assets/flag-en.png";
import flagRu from "@/assets/flag-ru.png";

/**
 * Переключатели темы и языка. Живут внизу экрана, чтобы до них доставал большой палец
 * и они не спорили с контентом в шапке.
 */
const AppSettingsDock = () => {
  const { lang, setLang } = useLanguage();
  const { theme, setTheme } = useTheme();

  return (
    <div
      className="fixed left-3 z-40 flex flex-col gap-2"
      style={{ bottom: "calc(88px + env(safe-area-inset-bottom))" }}
    >
      <button
        onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
        aria-label={lang === "ru" ? "Тема" : "Theme"}
        className="glass w-10 h-10 rounded-full flex items-center justify-center text-foreground active:scale-95 transition-transform"
      >
        {theme === "dark" ? <Sun className="w-[18px] h-[18px]" /> : <Moon className="w-[18px] h-[18px]" />}
      </button>

      <button
        onClick={() => setLang(lang === "ru" ? "en" : "ru")}
        aria-label={lang === "ru" ? "Язык" : "Language"}
        className="glass w-10 h-10 rounded-full flex items-center justify-center active:scale-95 transition-transform"
      >
        <img
          src={lang === "ru" ? flagRu : flagEn}
          alt=""
          className="w-[22px] h-[15px] rounded-[3px] object-cover"
        />
      </button>
    </div>
  );
};

export default AppSettingsDock;
