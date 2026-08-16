import { useNavigate } from "react-router-dom";
import { ChevronRight, Play } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import BannerCarousel from "@/components/BannerCarousel";
import continueCover from "@/assets/continue-cover.jpg";
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
        {/* Промо-баннеры */}
        <section className="mb-8">
          <BannerCarousel />
        </section>

        {/* Continue learning — афиша: обложка курса на весь блок, подписи поверх затемнения */}
        <section className="mb-8">
          <SectionHeader title={t("home.continueTitle")} />
          <button
            onClick={() => navigate("/my-courses")}
            className="group relative w-full h-[220px] md:h-[280px] rounded-2xl overflow-hidden text-left"
          >
            <img
              src={continueCover}
              alt=""
              aria-hidden
              className="absolute inset-0 w-full h-full object-cover group-hover:scale-[1.03] transition-transform duration-300"
            />
            <span
              className="absolute inset-0"
              style={{
                // Обложка светлая, поэтому затемнение плотнее обычного
                background:
                  "linear-gradient(to top, rgba(0,0,0,0.92) 0%, rgba(0,0,0,0.78) 42%, rgba(0,0,0,0.35) 70%, rgba(0,0,0,0) 100%)",
              }}
            />

            <span className="absolute inset-x-0 bottom-0 p-4 flex flex-col gap-2.5">
              <span
                className="block text-white text-[20px] font-medium leading-[1.15]"
                style={{ textShadow: "0 1px 12px rgba(0,0,0,0.45)" }}
              >
                {currentLesson.title}
              </span>
              <span className="block h-1.5 w-full rounded-full overflow-hidden" style={{ background: "rgba(255,255,255,0.3)" }}>
                <span className="block h-full rounded-full bg-white" style={{ width: `${courseProgress}%` }} />
              </span>
              <span
                className="inline-flex items-center justify-center gap-2 h-11 rounded-xl text-white text-[16px] font-medium"
                style={{
                  background: "rgba(255,255,255,0.22)",
                  backdropFilter: "blur(12px)",
                  WebkitBackdropFilter: "blur(12px)",
                  border: "1px solid rgba(255,255,255,0.25)",
                }}
              >
                <Play className="w-4 h-4" fill="#FFFFFF" />
                {t("index.continue")} · {courseProgress}%
              </span>
            </span>
          </button>
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
