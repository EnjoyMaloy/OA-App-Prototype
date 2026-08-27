import { Check, History, Users } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { useLocation, useNavigate } from "react-router-dom";
import { agoLabelShort, compactNumber, formatRating } from "@/lib/utils";

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
  /** Крупная карточка во всю ширину: больше заголовок, метрики и воздух между ними */
  large?: boolean;
  /** Скрыть ряд метрик — например, в завершённых курсах они не нужны */
  hideMeta?: boolean;
  /** Курс пройден: на обложке появляется зелёная галочка */
  completed?: boolean;
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
  large = false,
  hideMeta = false,
  completed = false,
}: CourseCardProps) => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const location = useLocation();
  const title = lang === "ru" ? titleRu : titleEn;

  return (
    <div
      // Откуда пришли — подписываем кнопку «назад» на странице курса
      onClick={() => navigate(`/course/${id}`, { state: { fromPath: location.pathname } })}
      className="flex flex-col cursor-pointer rounded-[20px] p-1 pb-3.5 bg-muted"
    >
      {/* Обложка 16:9 со скруглением, внутри общей подложки */}
      <div
        className="relative w-full aspect-video rounded-[14px] overflow-hidden bg-background"
        style={imageBg ? { background: imageBg } : undefined}
      >
        <img
          src={image}
          alt={title}
          className={`w-full h-full ${
            imageBg ? "object-contain p-4" : "object-cover"
          }`}
          loading="lazy"
        />

        {/* Пройденный курс отмечен галочкой в углу обложки */}
        {completed && (
          <span
            className={`absolute flex items-center justify-center rounded-full text-white ${
              large ? "top-2.5 right-2.5 w-8 h-8" : "top-2 right-2 w-7 h-7"
            }`}
            style={{
              background: "linear-gradient(135deg, #4ADE80 0%, #16A34A 100%)",
              boxShadow: "0 2px 8px rgba(6, 78, 59, 0.28)",
            }}
            aria-label="Курс пройден"
          >
            <Check className={large ? "w-[18px] h-[18px]" : "w-4 h-4"} strokeWidth={3} />
          </span>
        )}
      </div>

      {/* Заголовок всегда занимает две строки, чтобы карточки в ленте были одной высоты */}
      <h3
        className={`px-1.5 line-clamp-2 font-medium ${
          large ? "pt-4 text-[24px] leading-[1.15] min-h-[56px]" : "pt-3 text-[18px] leading-[1.2] min-h-[43px]"
        }`}
        style={{ color: "hsl(0 0% 6%)" }}
      >
        {title}
      </h3>

      {/* Под заголовком: компактный ряд иконок с цифрами, без плашек */}
      {!hideMeta && (
        <div
          // Метрики всегда в одну строку: числа компактные, дата при нехватке места обрезается
          className={`flex items-center min-w-0 px-1.5 ${
            large ? "gap-x-4 pt-4 text-[17px]" : "gap-x-2.5 pt-2.5 text-[15px]"
          }`}
        >
          <span className="inline-flex items-center gap-[3px] flex-shrink-0 text-foreground">
            <svg width={large ? 17 : 15} height={large ? 17 : 15} viewBox="0 0 14 14" fill="none" aria-hidden>
              <path
                d="M7 1L8.854 4.756L13 5.362L10 8.284L10.708 12.412L7 10.468L3.292 12.412L4 8.284L1 5.362L5.146 4.756L7 1Z"
                fill="#FF7D60"
              />
            </svg>
            {formatRating(rating)}
          </span>

          <span className="inline-flex items-center gap-[3px] flex-shrink-0" style={{ color: "hsl(0 0% 42%)" }}>
            <Users className={large ? "w-[19px] h-[19px]" : "w-[17px] h-[17px]"} strokeWidth={1.5} />
            {compactNumber(students, lang)}
          </span>

          {/* Когда курс обновляли — как «2 недели назад» на YouTube */}
          <span className="inline-flex items-center gap-[3px] min-w-0" style={{ color: "hsl(0 0% 42%)" }}>
            <History className={`flex-shrink-0 ${large ? "w-[18px] h-[18px]" : "w-4 h-4"}`} strokeWidth={1.6} />
            <span className="truncate">{agoLabelShort(updatedDaysAgo, lang)}</span>
          </span>
        </div>
      )}

      {/* Полоска прогресса — только там, где он передан (раздел «Мои курсы») */}
      {typeof progress === "number" && (
        <div className="flex items-center gap-2 px-1.5 pt-3">
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
