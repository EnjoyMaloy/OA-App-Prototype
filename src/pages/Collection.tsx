import { useNavigate, useParams } from "react-router-dom";
import { ArrowLeft } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import CourseCard from "@/components/CourseCard";
import { courses, getCategoryLabel } from "@/data/courses";

/** Подборки с главной: «Новое» и «В тренде» открываются отдельным экраном */
const collections = {
  new: {
    titleRu: "Новое",
    titleEn: "New",
    filter: (c: (typeof courses)[number]) => !!c.isNew,
  },
  trending: {
    titleRu: "В тренде",
    titleEn: "Trending",
    filter: (c: (typeof courses)[number]) => !!c.trending,
  },
} as const;

const Collection = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { lang } = useLanguage();
  const store = usePurchaseStore();

  const collection = collections[id as keyof typeof collections];
  const list = collection ? courses.filter(collection.filter) : [];
  const title = collection
    ? lang === "ru"
      ? collection.titleRu
      : collection.titleEn
    : lang === "ru"
      ? "Подборка"
      : "Collection";

  const isOwned = (courseId: string, premium?: boolean) =>
    store.purchasedCourses.includes(courseId) || (!!premium && !!store.subscription?.active);

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 pt-[max(12px,env(safe-area-inset-top))] pb-6 md:pt-10 md:pb-10">
        {/* Стеклянная кнопка «назад» липнет к верху при прокрутке */}
        <button
          onClick={() => navigate(-1)}
          aria-label={lang === "ru" ? "Назад" : "Back"}
          className="glass sticky top-[max(12px,env(safe-area-inset-top))] z-50 w-11 h-11 rounded-full flex items-center justify-center active:scale-95 transition-transform md:hidden"
        >
          <ArrowLeft strokeWidth={2.2} className="w-[22px] h-[22px] text-foreground" />
        </button>

        <h1 className="text-[28px] font-semibold leading-[1.1] tracking-[-0.01em] text-foreground mt-3 mb-4">{title}</h1>

        {/* Карточки идут столбиком и листаются вниз */}
        <div className="flex flex-col gap-4">
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
            />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Collection;
