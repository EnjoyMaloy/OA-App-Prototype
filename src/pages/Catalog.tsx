import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import { ChevronDown, Search, X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCardTall from "@/components/CourseCardTall";
import Footer from "@/components/Footer";
import { categories, courses, getCategoryLabel, type CourseData } from "@/data/courses";

const Catalog = () => {
  const { lang, t } = useLanguage();
  const [searchParams, setSearchParams] = useSearchParams();
  const searchQuery = searchParams.get("q") || "";
  // Категория может прийти с главной: /catalog?cat=web3
  const [selectedCategory, setSelectedCategory] = useState<string | null>(searchParams.get("cat"));
  const [sortOpen, setSortOpen] = useState(false);
  const [sortBy, setSortBy] = useState<"newest" | "popular">("newest");
  const store = usePurchaseStore();

  const isOwned = (course: CourseData) =>
    store.purchasedCourses.includes(course.id) || (!!course.premium && !!store.subscription?.active);

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

  // Ленты показываем только на «чистом» каталоге: с поиском или фильтром нужен один список
  const isFiltered = !!searchQuery || !!selectedCategory;
  const newCourses = courses.filter((c) => c.isNew);
  const trendingCourses = courses.filter((c) => c.trending);

  const renderCard = (course: CourseData, className: string) => (
    <CourseCardTall
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
      isOwned={isOwned(course)}
      className={className}
    />
  );

  const renderRail = (title: string, list: CourseData[], onSeeAll: () => void) => (
    <section className="mb-8">
      <div className="flex items-baseline justify-between mb-3">
        <h2 className="text-h2 text-foreground">{title}</h2>
        <button
          onClick={onSeeAll}
          className="text-[14px] text-muted-foreground hover:text-foreground transition-colors flex-shrink-0"
        >
          {t("catalog.seeAll")}
        </button>
      </div>
      <div className="flex gap-3 overflow-x-auto scrollbar-hide snap-x snap-mandatory -mx-4 px-4 pb-1">
        {list.map((course) => renderCard(course, "flex-shrink-0 snap-start w-[220px] sm:w-[240px]"))}
      </div>
    </section>
  );

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 py-6 md:py-10">
        {/* Заголовок и поиск */}
        <div className="flex items-center justify-between gap-3 mb-5">
          <h1 className="text-h1 text-foreground">{t("sidebar.catalog")}</h1>
          <button
            onClick={() => window.dispatchEvent(new Event("open-search"))}
            className="md:hidden flex-shrink-0 w-11 h-11 rounded-full flex items-center justify-center border border-border bg-background shadow-[0_2px_8px_rgba(0,0,0,0.06)] active:scale-95 transition-transform"
            aria-label={t("nav.searchCourse")}
          >
            <Search className="w-5 h-5 text-foreground" strokeWidth={2.2} />
          </button>
        </div>

        {/* Быстрые фильтры по категориям */}
        <div className="flex gap-2 overflow-x-auto scrollbar-hide -mx-4 px-4 pb-1 mb-7">
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

        {/* Активный поиск */}
        {searchQuery && (
          <button
            onClick={() => setSearchParams({})}
            className="inline-flex items-center gap-2 mb-6 pl-3 pr-2 py-2 rounded-full bg-muted text-[14px] text-foreground hover:brightness-95 transition-all"
          >
            <span>
              {t("catalog.searchFor")} «{searchQuery}»
            </span>
            <X className="w-4 h-4 text-muted-foreground" />
          </button>
        )}

        {!isFiltered && (
          <>
            {newCourses.length > 0 && renderRail(t("home.new"), newCourses, () => setSelectedCategory(null))}
            {trendingCourses.length > 0 &&
              renderRail(t("home.trending"), trendingCourses, () => setSelectedCategory(null))}
          </>
        )}

        {/* Полный список */}
        <section>
          <div className="flex items-baseline justify-between gap-3 mb-3">
            <h2 className="text-h2 text-foreground">
              {searchQuery
                ? t("catalog.results")
                : selectedCategory
                ? getCategoryLabel(selectedCategory, lang).replace("\n", " ")
                : t("catalog.allCourses")}
            </h2>
            <div className="relative flex-shrink-0">
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

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
            {sortedCourses.map((course) => renderCard(course, "w-full"))}
          </div>

          {sortedCourses.length === 0 && (
            <div className="text-center py-16 text-muted-foreground text-[16px]">{t("instructions.notFound")}</div>
          )}
        </section>
      </div>
      <Footer />
    </div>
  );
};

export default Catalog;
