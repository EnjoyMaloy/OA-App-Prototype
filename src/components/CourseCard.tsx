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
}: CourseCardProps) => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const title = lang === "ru" ? titleRu : titleEn;

  return (
    <div
      onClick={() => navigate(`/course/${id}`)}
      className="flex flex-col cursor-pointer group rounded-[20px] p-1.5 pb-3.5 bg-muted"
    >
      {/* Обложка 16:9 со скруглением, внутри общей подложки */}
      <div
        className="relative w-full aspect-video rounded-[14px] overflow-hidden bg-background"
        style={imageBg ? { background: imageBg } : undefined}
      >
        <img
          src={image}
          alt={title}
          className={`w-full h-full transition-transform duration-300 group-hover:scale-105 ${
            imageBg ? "object-contain p-4" : "object-cover"
          }`}
          loading="lazy"
        />
      </div>

      {/* Заголовок всегда занимает две строки, чтобы карточки в ленте были одной высоты */}
      <h3
        className="px-1.5 pt-3 text-[17px] font-medium leading-[1.3] line-clamp-2 min-h-[45px]"
        style={{ color: "hsl(0 0% 6%)" }}
      >
        {title}
      </h3>

      {/* Под заголовком: компактный ряд иконок с цифрами, без плашек */}
      <div className="flex flex-wrap items-center gap-x-1.5 gap-y-1 px-1.5 pt-2.5">
        <span className="inline-flex items-center gap-1 text-[14px] text-foreground">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden>
            <path
              d="M7 1L8.854 4.756L13 5.362L10 8.284L10.708 12.412L7 10.468L3.292 12.412L4 8.284L1 5.362L5.146 4.756L7 1Z"
              fill="#FF7D60"
            />
          </svg>
          {rating}
        </span>

        <span className="inline-flex items-center gap-1 text-[14px]" style={{ color: "hsl(0 0% 42%)" }}>
          <Users className="w-4 h-4" strokeWidth={1.5} />
          {students.toLocaleString("ru-RU")}
        </span>

        {/* Когда курс обновляли — как «2 недели назад» на YouTube */}
        <span className="inline-flex items-center gap-1 text-[14px]" style={{ color: "hsl(0 0% 42%)" }}>
          <History className="w-[15px] h-[15px]" strokeWidth={1.6} />
          {agoLabel(updatedDaysAgo, lang)}
        </span>
      </div>
    </div>
  );
};

export default CourseCard;
