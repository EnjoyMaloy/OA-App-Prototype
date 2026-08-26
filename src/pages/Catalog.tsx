import { useEffect, useRef, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { Check, ChevronDown, Search, X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import { categories, courses, getCategoryLabel } from "@/data/courses";

const Catalog = () => {
  const { lang, t } = useLanguage();
  const [searchParams, setSearchParams] = useSearchParams();
  const searchQuery = searchParams.get("q") || "";
  // Категория может прийти с главной: /catalog?cat=web3
  const [selectedCategory, setSelectedCategory] = useState<string | null>(searchParams.get("cat"));
  const [sortOpen, setSortOpen] = useState(false);
  const [sortBy, setSortBy] = useState<"newest" | "popular">("newest");
  const store = usePurchaseStore();
  const searchRef = useRef<HTMLInputElement>(null);

  // Кнопка поиска в таб-баре присылает сюда ?focus=1 — фокусируем поле и убираем флаг
  useEffect(() => {
    if (!searchParams.get("focus")) return;
    searchRef.current?.focus();
    const next = new URLSearchParams(searchParams);
    next.delete("focus");
    setSearchParams(next, { replace: true });
  }, [searchParams, setSearchParams]);

  // Запрос живёт в адресе: его же выставляет поиск из таб-бара
  const setQuery = (value: string) => {
    const next = new URLSearchParams(searchParams);
    if (value) next.set("q", value);
    else next.delete("q");
    setSearchParams(next, { replace: true });
  };

  const filteredCourses = courses.filter((c) => {
    const matchesCategory = !selectedCategory || c.categoryId === selectedCategory;
    const matchesSearch =
      !searchQuery ||
      c.titleRu.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.titleEn.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const sortedCourses = [...filteredCourses].sort((a, b) =>
    sortBy === "popular" ? b.students - a.students : 0
  );

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 py-5 md:py-10">
        {/* Поиск */}
        <div className="relative mb-5">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-muted-foreground pointer-events-none" />
          <input
            ref={searchRef}
            type="text"
            value={searchQuery}
            onChange={(e) => setQuery(e.target.value)}
            placeholder={t("nav.searchCourse")}
            className="w-full h-14 pl-12 pr-12 rounded-full bg-muted border-none text-[17px] text-foreground placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary/30 transition-all"
          />
          {searchQuery && (
            <button
              onClick={() => setQuery("")}
              className="absolute right-4 top-1/2 -translate-y-1/2 w-6 h-6 rounded-full flex items-center justify-center bg-foreground/35"
              aria-label="clear-search"
            >
              <X className="w-3.5 h-3.5 text-background" strokeWidth={3} />
            </button>
          )}
        </div>

        {/* Категории — те же пилюли, что на главной; активной может быть только одна */}
        <div className="overflow-x-auto scrollbar-hide -mx-4 px-4 pb-1 mb-6">
          <div className="w-max flex flex-col gap-2.5">
            {[
              categories.slice(0, Math.ceil(categories.length / 2)),
              categories.slice(Math.ceil(categories.length / 2)),
            ].map((row, rowIndex) => (
              <div key={rowIndex} className="flex gap-2.5">
                {row.map((cat) => {
                  const Icon = cat.icon;
                  const active = selectedCategory === cat.id;
                  const label = (lang === "ru" ? cat.labelRu : cat.labelEn).replace("\n", " ");
                  return (
                    <button
                      key={cat.id}
                      onClick={() => setSelectedCategory(active ? null : cat.id)}
                      className="inline-flex items-center gap-2 h-[40px] px-[14px] rounded-full text-[17px] font-medium whitespace-nowrap transition-colors"
                      // Выбранная категория заливается своим цветом целиком, остальные — пастелью
                      style={{
                        background: active ? cat.labelColor : cat.bg,
                        color: active ? "#fff" : cat.labelColor,
                      }}
                    >
                      <Icon
                        className="w-[19px] h-[19px] flex-shrink-0"
                        style={{ color: active ? "#fff" : cat.iconColor }}
                      />
                      {label}
                    </button>
                  );
                })}
              </div>
            ))}
          </div>
        </div>

        {/* Сортировка */}
        <div className="flex justify-end mb-4">
          <div className="relative">
            <button
              onClick={() => setSortOpen(!sortOpen)}
              className="inline-flex items-center gap-1 text-[14px] text-muted-foreground"
            >
              {sortBy === "newest" ? t("instructions.newest") : t("instructions.popular")}
              <ChevronDown className={`w-4 h-4 transition-transform ${sortOpen ? "rotate-180" : ""}`} />
            </button>
            {sortOpen && (
              // Меню как в S7: скруглённая карточка с тенью, у выбранного пункта галочка
              <div className="absolute top-full right-0 mt-2 z-20 min-w-[220px] p-1.5 rounded-2xl bg-background shadow-[0_12px_30px_rgba(15,15,15,0.16)] ring-1 ring-border">
                {([
                  ["newest", t("instructions.newest")],
                  ["popular", t("instructions.popular")],
                ] as const).map(([value, label]) => {
                  const active = sortBy === value;
                  return (
                    <button
                      key={value}
                      onClick={() => {
                        setSortBy(value);
                        setSortOpen(false);
                      }}
                      className={`w-full flex items-center justify-between gap-2.5 px-2.5 py-2.5 rounded-xl text-[15px] text-left transition-colors ${
                        active ? "bg-primary/[0.08] text-primary font-medium" : "text-foreground active:bg-muted"
                      }`}
                    >
                      {label}
                      {active && <Check className="w-4 h-4 flex-shrink-0" strokeWidth={2.6} />}
                    </button>
                  );
                })}
              </div>
            )}
          </div>
        </div>

        {/* Курсы — карточки те же, что на главной */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {sortedCourses.map((course) => {
            const isPurchased = store.purchasedCourses.includes(course.id);
            const hasSubscription = store.subscription?.active;
            const isOwned = isPurchased || (course.premium && hasSubscription) || false;

            return (
              <CourseCard
                key={course.id}
                id={course.id}
                titleRu={course.titleRu}
                titleEn={course.titleEn}
                categoryLabel={getCategoryLabel(course.categoryId, lang)}
                rating={course.rating}
                students={course.students}
                image={course.image}
                imageBg={course.imageBg}
                premium={course.premium}
                price={course.price}
                isNew={course.isNew}
                trending={course.trending}
                updatedDaysAgo={course.updatedDaysAgo}
              large
                isOwned={isOwned}
              />
            );
          })}
        </div>

        {sortedCourses.length === 0 && (
          <div className="text-center py-16 text-muted-foreground text-[16px]">{t("instructions.notFound")}</div>
        )}
      </div>
    </div>
  );
};

export default Catalog;
