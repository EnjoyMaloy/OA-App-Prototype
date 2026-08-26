import { useNavigate, useParams } from "react-router-dom";
import { ArrowLeft } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import ReviewCard from "@/components/ReviewCard";
import { getCourseReviews } from "@/pages/CourseExperimental";

/** Все отзывы курса: столбик карточек со стеклянной кнопкой «назад» */
const CourseReviews = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const { lang } = useLanguage();
  const reviews = getCourseReviews(id);

  return (
    <div className="min-h-screen bg-background">
      <div className="max-w-6xl mx-auto px-4 pt-[max(12px,env(safe-area-inset-top))] pb-6 md:pt-10 md:pb-10">
        <button
          onClick={() => navigate(-1)}
          aria-label={lang === "ru" ? "Назад" : "Back"}
          className="glass sticky top-[max(12px,env(safe-area-inset-top))] z-50 w-11 h-11 rounded-full flex items-center justify-center active:scale-95 transition-transform md:hidden"
        >
          <ArrowLeft strokeWidth={2.2} className="w-[22px] h-[22px] text-foreground" />
        </button>

        <h1 className="text-[28px] font-semibold leading-[1.1] tracking-[-0.01em] text-foreground mt-5 mb-4">
          {lang === "ru" ? "Все отзывы" : "All reviews"}
        </h1>

        <div className="flex flex-col gap-4">
          {reviews.map((r, i) => (
            <ReviewCard key={i} review={r} lang={lang} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default CourseReviews;
