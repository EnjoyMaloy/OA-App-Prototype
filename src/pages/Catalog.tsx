import { useState } from "react";
import { useSearchParams } from "react-router-dom";
import { ChevronDown, LayoutGrid, X } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import Footer from "@/components/Footer";
import { categories, courses, getCategoryLabel } from "@/data/courses";

const Catalog = () => {
  const { lang, t } = useLanguage();
  const [searchParams, setSearchParams] = useSearchParams();
  const searchQuery = searchParams.get("q") || "";
  // Category can be preselected from the home screen: /catalog?cat=web3
  const [selectedCategory, setSelectedCategory] = useState<string | null>(searchParams.get("cat"));
  const [sortOpen, setSortOpen] = useState(false);
  const [sortBy, setSortBy] = useState<"newest" | "popular">("newest");
  const [catDropdownOpen, setCatDropdownOpen] = useState(false);
  const store = usePurchaseStore();

  const filteredCourses = courses.filter((c) => {
    const matchesCategory = !selectedCategory || c.categoryId === selectedCategory;
    const matchesSearch = !searchQuery || c.titleRu.toLowerCase().includes(searchQuery.toLowerCase()) || c.titleEn.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const sortedCourses = [...filteredCourses].sort((a, b) =>
    sortBy === "popular" ? b.students - a.students : 0
  );

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 py-8 md:py-10">
        {/* Subtitle */}
        <p className="text-[16px] text-muted-foreground mb-8">
          {t("catalog.subtitle")}
        </p>

        {/* Активный поиск — приходит с кнопки поиска в таб-баре */}
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

        {/* Category cards row */}
        <div className="flex gap-3 overflow-x-auto pb-4 mb-8 scrollbar-hide">
          {categories.map((cat) => {
            const Icon = cat.icon;
            const label = lang === "ru" ? cat.labelRu : cat.labelEn;
            return (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(selectedCategory === cat.id ? null : cat.id)}
                className={`flex-shrink-0 flex flex-col justify-between rounded-2xl p-4 transition-all ${
                  selectedCategory === cat.id ? "ring-2 ring-primary ring-offset-2 scale-[1.03]" : "hover:scale-[1.03]"
                }`}
                style={{
                  background: cat.bg,
                  width: 160,
                  height: 160,
                }}
              >
                <Icon style={{ color: cat.iconColor }} className="w-7 h-7" />
                <div className="text-left">
                  <span className="text-[16px] font-medium leading-[1.2] text-foreground block whitespace-pre-line">
                    {label}
                  </span>
                  <span className="text-[14px] font-medium mt-1 block" style={{ color: cat.countColor }}>
                    {lang === "ru" ? cat.countRu : cat.countEn}
                  </span>
                </div>
              </button>
            );
          })}
        </div>

        {/* Filters row */}
        <div className="flex items-center justify-between mb-6 flex-wrap gap-3">
          {/* Categories dropdown */}
          <div className="relative">
            <button
              onClick={() => setCatDropdownOpen(!catDropdownOpen)}
              className="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg border border-border bg-background text-[14px] font-medium text-foreground hover:bg-muted transition-colors"
            >
              <LayoutGrid className="w-4 h-4" />
              {t("catalog.categories")}
              <ChevronDown className={`w-4 h-4 transition-transform ${catDropdownOpen ? "rotate-180" : ""}`} />
            </button>
            {catDropdownOpen && (
              <div className="absolute top-full left-0 mt-1 bg-background border border-border rounded-lg shadow-lg z-20 min-w-[180px] py-1">
                <button
                  onClick={() => { setSelectedCategory(null); setCatDropdownOpen(false); }}
                  className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${!selectedCategory ? "text-primary font-medium" : "text-foreground"}`}
                >
                  {t("instructions.allTopics")}
                </button>
                {categories.map((cat) => (
                  <button
                    key={cat.id}
                    onClick={() => { setSelectedCategory(cat.id); setCatDropdownOpen(false); }}
                    className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${selectedCategory === cat.id ? "text-primary font-medium" : "text-foreground"}`}
                  >
                    {lang === "ru" ? cat.labelRu : cat.labelEn}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Sort dropdown */}
          <div className="relative">
            <button
              onClick={() => setSortOpen(!sortOpen)}
              className="inline-flex items-center gap-1 text-[14px] text-muted-foreground hover:text-foreground transition-colors"
            >
              {t("instructions.sort")} {sortBy === "newest" ? t("instructions.newest") : t("instructions.popular")}
              <ChevronDown className={`w-4 h-4 transition-transform ${sortOpen ? "rotate-180" : ""}`} />
            </button>
            {sortOpen && (
              <div className="absolute top-full right-0 mt-1 bg-background border border-border rounded-lg shadow-lg z-20 min-w-[200px] py-1">
                <button
                  onClick={() => { setSortBy("newest"); setSortOpen(false); }}
                  className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${sortBy === "newest" ? "text-primary font-medium" : "text-foreground"}`}
                >
                  {t("instructions.newest")}
                </button>
                <button
                  onClick={() => { setSortBy("popular"); setSortOpen(false); }}
                  className={`w-full text-left px-4 py-2 text-[14px] hover:bg-muted transition-colors ${sortBy === "popular" ? "text-primary font-medium" : "text-foreground"}`}
                >
                  {t("instructions.popular")}
                </button>
              </div>
            )}
          </div>
        </div>

        {/* Course cards grid */}
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
          <div className="text-center py-16 text-muted-foreground text-[16px]">
            {t("instructions.notFound")}
          </div>
        )}
      </div>
      <Footer />
    </div>
  );
};

export default Catalog;
