import { History, Users } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { useNavigate } from "react-router-dom";
import { agoLabel } from "@/lib/utils";

interface CourseCardProps {
  id: string;
  titleRu: string;
  titleEn: string;
  categoryLabel: string;
  rating: number;
  students: number;
  image: string;
  /** Градиент под 3D-объектом обложки */
  imageBg?: string;
  premium?: boolean;
  price?: number;
  isNew?: boolean;
  trending?: boolean;
  isOwned?: boolean;
  /** Сколько дней назад обновляли курс */
  updatedDaysAgo: number;
  /** Прогресс прохождения: рисуется полоской под метриками, если передан */
  progress?: number;
}

const CourseCard = ({
  id,
  titleRu,
  titleEn,
  rating,
  students,
  image,
  imageBg,
  updatedDaysAgo,
  progress,
}: CourseCardProps) => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const title = lang === "ru" ? titleRu : titleEn;

  return (
    <div
      onClick={() => navigate(`/course/${id}`)}
      className="flex flex-col cursor-pointer rounded-[20px] pb-3.5 bg-muted overflow-hidden"
    >
      {/* Обложка во всю ширину: книзу растворяется в подложке карточки */}
      <div
        className="relative w-full aspect-video"
        style={imageBg ? { background: imageBg } : undefined}
      >
        <img
          src={image}
          alt={title}
          className={`w-full h-full ${imageBg ? "object-contain p-4" : "object-cover"}`}
          style={{
            maskImage: "linear-gradient(to bottom, #000 62%, transparent 100%)",
            WebkitMaskImage: "linear-gradient(to bottom, #000 62%, transparent 100%)",
          }}
          loading="lazy"
        />
      </div>

      {/* Заголовок по центру, всегда в две строки — карточки в ленте одной высоты */}
      <h3
        className="px-4 -mt-3 text-center text-[18px] font-medium leading-[1.2] line-clamp-2 min-h-[43px]"
        style={{ color: "hsl(0 0% 6%)" }}
      >
        {title}
      </h3>

      {/* Под заголовком: компактный ряд иконок с цифрами, без плашек */}
      <div className="flex flex-wrap items-center justify-center gap-x-1.5 gap-y-1 px-4 pt-2.5">
        <span className="inline-flex items-center gap-1 text-[15px] text-foreground">
          <svg width="15" height="15" viewBox="0 0 14 14" fill="none" aria-hidden>
            <path
              d="M7 1L8.854 4.756L13 5.362L10 8.284L10.708 12.412L7 10.468L3.292 12.412L4 8.284L1 5.362L5.146 4.756L7 1Z"
              fill="#FF7D60"
            />
          </svg>
          {rating}
        </span>

        <span className="inline-flex items-center gap-1 text-[15px]" style={{ color: "hsl(0 0% 42%)" }}>
          <Users className="w-[17px] h-[17px]" strokeWidth={1.5} />
          {students.toLocaleString("ru-RU")}
        </span>

        {/* Когда курс обновляли — как «2 недели назад» на YouTube */}
        <span className="inline-flex items-center gap-1 text-[15px]" style={{ color: "hsl(0 0% 42%)" }}>
          <History className="w-4 h-4" strokeWidth={1.6} />
          {agoLabel(updatedDaysAgo, lang)}
        </span>
      </div>

      {/* Полоска прогресса — только там, где он передан (раздел «Мои курсы») */}
      {typeof progress === "number" && (
        <div className="flex items-center gap-2 px-4 pt-3">
          <span className="flex-1 h-1.5 rounded-full bg-background overflow-hidden">
            <span
              className="block h-full rounded-full"
              style={{
                width: `${Math.min(100, Math.max(0, progress))}%`,
                background: progress >= 100 ? "#1BB07A" : "hsl(var(--primary))",
              }}
            />
          </span>
          <span className="text-[13px]" style={{ color: "hsl(0 0% 42%)" }}>
            {progress}%
          </span>
        </div>
      )}
    </div>
  );
};

export default CourseCard;
