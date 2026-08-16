import { useNavigate } from "react-router-dom";
import { ChevronRight, Play } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import BannerCarousel from "@/components/BannerCarousel";
import { categories, courses, getCategoryLabel } from "@/data/courses";
import { lessonsData, courseProgress, currentLessonIndex } from "@/data/lessons";

const SectionHeader = ({
  title,
  actionLabel,
  onAction,
}: {
  title: string;
  actionLabel?: string;
  onAction?: () => void;
}) => (
  <div className="flex items-center justify-between mb-3">
    <h2 className="text-h3 text-foreground">{title}</h2>
    {actionLabel && (
      <button
        onClick={onAction}
        className="inline-flex items-center gap-0.5 text-[14px] text-muted-foreground hover:text-foreground transition-colors"
      >
        {actionLabel}
        <ChevronRight className="w-4 h-4" />
      </button>
    )}
  </div>
);

const Home = () => {
  const { lang, t } = useLanguage();
  const navigate = useNavigate();
  const store = usePurchaseStore();

  const currentLesson = lessonsData[currentLessonIndex];
  const newCourses = courses.filter((c) => c.isNew);
  const trendingCourses = courses.filter((c) => c.trending);

  const isOwned = (courseId: string, premium?: boolean) =>
    store.purchasedCourses.includes(courseId) || (!!premium && !!store.subscription?.active);

  const renderRail = (list: typeof courses) => (
    <div className="flex gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory -mx-4 px-4 pb-1">
      {list.map((course) => (
        <div key={course.id} className="flex-shrink-0 snap-start w-[260px] sm:w-[300px]">
          <CourseCard
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
            isOwned={isOwned(course.id, course.premium)}
          />
        </div>
      ))}
    </div>
  );

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 py-6 md:py-10">
        {/* Greeting */}
        <div className="mb-5">
          <h1 className="text-h1 text-foreground mb-2">{t("home.greeting")}</h1>
          <p className="text-[16px] text-muted-foreground">{t("home.subtitle")}</p>
        </div>

        {/* Промо-баннеры */}
        <section className="mb-8">
          <BannerCarousel />
        </section>

        {/* Continue learning */}
        <section className="mb-8">
          <SectionHeader title={t("home.continueTitle")} />
          <div
            className="relative rounded-2xl overflow-hidden p-4"
            style={{
              background:
                "linear-gradient(180deg, hsl(270 60% 88% / 0.7) 0%, hsl(270 70% 85% / 1) 50%, hsl(270 60% 88% / 0.7) 100%)",
            }}
          >
            {/* Dot pattern — same texture as the lesson map */}
            <div
              className="absolute inset-0 opacity-15 pointer-events-none"
              style={{
                backgroundImage:
                  "radial-gradient(circle, hsl(var(--violet-primary) / 0.3) 1px, transparent 1px)",
                backgroundSize: "16px 16px",
              }}
            />

            <div className="relative z-10 bg-background rounded-xl p-4">
              <span className="text-caption-12 font-medium text-violet-light">
                {t("index.lesson")} {currentLesson.number}
              </span>
              <h3 className="text-[20px] font-normal leading-[110%] text-foreground mt-1.5">
                {currentLesson.title}
              </h3>
              <p className="text-[14px] leading-[140%] text-muted-foreground mt-1.5">
                {t("index.title")}
              </p>

              <div className="flex items-center justify-between mt-4 mb-2">
                <span className="text-[14px] text-muted-foreground">{t("index.completed")}</span>
                <span className="text-[14px] font-semibold text-foreground">{courseProgress}%</span>
              </div>
              <div className="h-1.5 w-full bg-muted rounded-full overflow-hidden">
                <div
                  className="h-full bg-primary rounded-full transition-all"
                  style={{ width: `${courseProgress}%` }}
                />
              </div>

              <div className="flex items-center gap-3 mt-4">
                <button
                  onClick={() => navigate("/my-courses")}
                  className="flex-1 md:flex-none md:w-[260px] inline-flex items-center justify-center gap-2 text-[16px] font-medium tracking-[0.01em] hover:opacity-90 transition-opacity"
                  style={{ background: "#232323", color: "#FFFFFF", borderRadius: 12, height: 52 }}
                >
                  <Play className="w-4 h-4" fill="#FFFFFF" />
                  {t("index.continue")}
                </button>
                <div className="flex flex-col items-end flex-shrink-0" style={{ gap: 6 }}>
                  <span className="text-[14px] leading-[100%] text-muted-foreground">
                    {t("index.reward")}
                  </span>
                  <div className="flex items-center" style={{ gap: 6 }}>
                    <span
                      className="inline-flex items-center justify-center rounded-full text-[11px] font-bold"
                      style={{ width: 22, height: 22, background: "#FF7D60", color: "#FFFFFF" }}
                    >
                      S
                    </span>
                    <span className="text-[22px] font-semibold leading-[100%] tracking-[-0.01em] text-foreground">
                      {currentLesson.reward.toLocaleString()}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Categories */}
        <section className="mb-8">
          <SectionHeader
            title={t("catalog.categories")}
            actionLabel={t("instructions.all")}
            onAction={() => navigate("/catalog")}
          />
          <div className="flex gap-3 overflow-x-auto scrollbar-hide -mx-4 px-4 pb-1">
            {categories.map((cat) => {
              const Icon = cat.icon;
              const label = lang === "ru" ? cat.labelRu : cat.labelEn;
              return (
                <button
                  key={cat.id}
                  onClick={() => navigate(`/catalog?cat=${cat.id}`)}
                  className="flex-shrink-0 flex flex-col justify-between rounded-2xl p-3 transition-all hover:scale-[1.03]"
                  style={{ background: cat.bg, width: 116, height: 116 }}
                >
                  <Icon style={{ color: cat.iconColor }} className="w-6 h-6" />
                  <div className="text-left w-full">
                    <span className="text-[14px] font-medium leading-[1.15] text-foreground block whitespace-pre-line">
                      {label}
                    </span>
                    <span
                      className="text-[12px] font-medium mt-1 block"
                      style={{ color: cat.countColor }}
                    >
                      {lang === "ru" ? cat.countRu : cat.countEn}
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </section>

        {/* New courses */}
        {newCourses.length > 0 && (
          <section className="mb-8">
            <SectionHeader
              title={t("home.new")}
              actionLabel={t("instructions.all")}
              onAction={() => navigate("/catalog")}
            />
            {renderRail(newCourses)}
          </section>
        )}

        {/* Trending courses */}
        {trendingCourses.length > 0 && (
          <section className="mb-8">
            <SectionHeader
              title={t("home.trending")}
              actionLabel={t("instructions.all")}
              onAction={() => navigate("/catalog")}
            />
            {renderRail(trendingCourses)}
          </section>
        )}

        {/* All courses */}
        <button
          onClick={() => navigate("/catalog")}
          className="w-full text-[16px] font-medium tracking-[0.01em] border border-border rounded-xl text-foreground hover:bg-muted transition-colors"
          style={{ height: 52 }}
        >
          {t("home.allCourses")}
        </button>
      </div>
    </div>
  );
};

export default Home;
