import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import { ChevronDown, Search, X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import Footer from "@/components/Footer";
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

        {/* Категории */}
        <div className="flex gap-2 overflow-x-auto scrollbar-hide -mx-4 px-4 pb-1 mb-6">
          {categories.map((cat) => {
            const Icon = cat.icon;
            const active = selectedCategory === cat.id;
            return (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(active ? null : cat.id)}
                className={`flex-shrink-0 inline-flex items-center gap-2 h-11 pl-3 pr-4 rounded-full border transition-all ${
                  active
                    ? "border-transparent bg-foreground text-background"
                    : "border-border bg-background text-foreground hover:bg-muted"
                }`}
              >
                <Icon className="w-4 h-4" style={active ? undefined : { color: cat.iconColor }} />
                <span className="text-[15px] whitespace-nowrap">
                  {(lang === "ru" ? cat.labelRu : cat.labelEn).replace("\n", " ")}
                </span>
              </button>
            );
          })}
        </div>

        {/* Сортировка */}
        <div className="flex justify-end mb-4">
          <div className="relative">
            <button
              onClick={() => setSortOpen(!sortOpen)}
              className="inline-flex items-center gap-1 text-[14px] text-muted-foreground hover:text-foreground transition-colors"
            >
              {sortBy === "newest" ? t("instructions.newest") : t("instructions.popular")}
              <ChevronDown className={`w-4 h-4 transition-transform ${sortOpen ? "rotate-180" : ""}`} />
            </button>
            {sortOpen && (
              <div className="absolute top-full right-0 mt-1 bg-background border border-border rounded-lg shadow-lg z-20 min-w-[200px] py-1">
                <button
                  onClick={() => {
                    setSortBy("newest");
                    setSortOpen(false);
                  }}
                  className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${
                    sortBy === "newest" ? "text-primary font-medium" : "text-foreground"
                  }`}
                >
                  {t("instructions.newest")}
                </button>
                <button
                  onClick={() => {
                    setSortBy("popular");
                    setSortOpen(false);
                  }}
                  className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${
                    sortBy === "popular" ? "text-primary font-medium" : "text-foreground"
                  }`}
                >
                  {t("instructions.popular")}
                </button>
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
                categoryId={course.categoryId}
                categoryLabel={getCategoryLabel(course.categoryId, lang)}
                rating={course.rating}
                students={course.students}
                image={course.image}
                imageBg={course.imageBg}
                premium={course.premium}
                price={course.price}
                isNew={course.isNew}
                trending={course.trending}
                isOwned={isOwned}
              />
            );
          })}
        </div>

        {sortedCourses.length === 0 && (
          <div className="text-center py-16 text-muted-foreground text-[16px]">{t("instructions.notFound")}</div>
        )}
      </div>
      <Footer />
    </div>
  );
};

export default Catalog;
