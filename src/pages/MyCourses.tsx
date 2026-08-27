import { useState } from "react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import SegmentedTabs from "@/components/SegmentedTabs";
import { courses, getCategoryLabel } from "@/data/courses";

type TabId = "learning" | "finished" | "favorites";

const MyCourses = () => {
  const { lang } = useLanguage();
  const store = usePurchaseStore();
  const [tab, setTab] = useState<TabId>("learning");

  const tabs = [
    { id: "learning", label: lang === "ru" ? "Прохожу" : "In progress" },
    { id: "finished", label: lang === "ru" ? "Завершил" : "Finished" },
    { id: "favorites", label: lang === "ru" ? "Избранные" : "Saved" },
  ];

  const lists: Record<TabId, typeof courses> = {
    learning: courses.filter((c) => typeof c.progress === "number" && c.progress > 0 && c.progress < 100),
    finished: courses.filter((c) => c.progress === 100),
    favorites: courses.filter((c) => c.favorite),
  };
  const list = lists[tab];

  const empty =
    lang === "ru"
      ? { learning: "Пока нет курсов в работе", finished: "Ещё ни одного завершённого курса", favorites: "Избранное пустое" }[tab]
      : { learning: "Nothing in progress yet", finished: "No finished courses yet", favorites: "Nothing saved yet" }[tab];

  const isOwned = (courseId: string, premium?: boolean) =>
    store.purchasedCourses.includes(courseId) || (!!premium && !!store.subscription?.active);

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 pt-[max(12px,env(safe-area-inset-top))] pb-6 md:pt-10 md:pb-10">
        <h1 className="text-[28px] font-semibold leading-[1.1] tracking-[-0.01em] text-foreground mb-4">
          {lang === "ru" ? "Мои курсы" : "My courses"}
        </h1>

        <SegmentedTabs tabs={tabs} value={tab} onChange={(id) => setTab(id as TabId)} className="mb-5" />

        {list.length === 0 ? (
          <p className="text-[15px] text-muted-foreground py-10 text-center">{empty}</p>
        ) : (
          <div className="grid grid-cols-2 gap-3 md:gap-4">
            {list.map((course) => (
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
                isOwned={isOwned(course.id, course.premium)}
                // У пройденного курса вместо полосы 100% — галочка на обложке
                progress={tab === "favorites" || course.progress === 100 ? undefined : course.progress}
                // В «Прохожу» и «Завершил» метрики не нужны — важен только сам курс
                hideMeta={tab !== "favorites"}
                completed={course.progress === 100}
                // В «Избранных» сердечко видно и сразу активно
                likeable={tab === "favorites"}
                defaultLiked={tab === "favorites"}
              />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default MyCourses;
