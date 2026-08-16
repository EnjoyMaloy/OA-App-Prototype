import { useNavigate } from "react-router-dom";
import { ChevronRight } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import BannerCarousel from "@/components/BannerCarousel";
import { categories, courses, getCategoryLabel } from "@/data/courses";
import { lessonsData, courseProgress, currentLessonIndex } from "@/data/lessons";
import { pluralRu } from "@/lib/utils";

// Кольцо прогресса: оранжевая градиентная дуга на сплошном сером треке
const RING_R = 23;
const RING_LENGTH = 2 * Math.PI * RING_R;

const SectionHeader = ({
  title,
  actionLabel,
  onAction,
}: {
  title: string;
  actionLabel?: string;
  onAction?: () => void;
}) => (
  <div className="flex items-center justify-between gap-3 mb-4">
    <h2 className="text-[24px] font-semibold leading-[1.1] tracking-[-0.01em] text-foreground">{title}</h2>
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
  const lessonsRemaining = lessonsData.filter((l) => l.progress < 100).length;
  const lessonsLeft =
    lang === "ru"
      ? `Осталось ${lessonsRemaining} ${pluralRu(lessonsRemaining, ["урок", "урока", "уроков"])}`
      : `${lessonsRemaining} ${lessonsRemaining === 1 ? "lesson" : "lessons"} left`;
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

        {/* Continue learning — персиковая подложка, оранжевая дуга, вся карточка кликабельна */}
        <section className="mb-8">
          <SectionHeader title={t("home.continueTitle")} />
          <button
            onClick={() => navigate("/my-courses")}
            className="w-full flex items-center gap-3.5 rounded-2xl p-4 text-left hover:brightness-[0.98] transition-all"
            // Персик держится почти до правого края и растворяется у самой стрелки
            style={{ background: "linear-gradient(105deg, #FFE7DA 0%, #FFEDE3 55%, #FFFFFF 100%)" }}
          >
            <span className="relative flex-shrink-0 w-14 h-14">
              <svg width="56" height="56" viewBox="0 0 56 56" className="-rotate-90">
                <defs>
                  <linearGradient id="continueArc" x1="0" y1="0" x2="1" y2="1">
                    <stop offset="0" stopColor="#FF5C1A" />
                    <stop offset="1" stopColor="#FFB088" />
                  </linearGradient>
                </defs>
                <circle cx="28" cy="28" r={RING_R} fill="none" stroke="rgba(32,32,32,0.10)" strokeWidth="8" />
                <circle
                  cx="28"
                  cy="28"
                  r={RING_R}
                  fill="none"
                  stroke="url(#continueArc)"
                  strokeWidth="8"
                  strokeLinecap="round"
                  strokeDasharray={RING_LENGTH}
                  strokeDashoffset={RING_LENGTH * (1 - courseProgress / 100)}
                />
              </svg>
              {/* Процент залит тем же градиентом, что и дуга */}
              <span
                className="absolute inset-0 flex items-center justify-center text-[15px] font-bold"
                style={{
                  backgroundImage: "linear-gradient(120deg, #FF5C1A, #FFB088)",
                  WebkitBackgroundClip: "text",
                  backgroundClip: "text",
                  color: "transparent",
                }}
              >
                {courseProgress}%
              </span>
            </span>

            <span className="min-w-0 flex-1 flex flex-col gap-1.5">
              <span className="block text-[17px] font-medium leading-[1.2]" style={{ color: "#202020" }}>
                {currentLesson.title}
              </span>
              <span className="block text-[13px]" style={{ color: "rgba(32,32,32,0.5)" }}>
                {lessonsLeft}
              </span>
            </span>

            <ChevronRight className="w-5 h-5 flex-shrink-0" style={{ color: "rgba(32,32,32,0.35)" }} />
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
                  <Icon style={{ color: cat.iconColor }} className="w-9 h-9" />
                  <div className="text-left w-full">
                    {/* Название категории живёт в акцентном цвете самой категории */}
                    <span
                      className="text-[14px] font-medium leading-[1.15] block whitespace-pre-line"
                      style={{ color: cat.labelColor }}
                    >
                      {label}
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
