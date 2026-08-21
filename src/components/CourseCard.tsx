import { MoreVertical } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { useNavigate } from "react-router-dom";
import { categories } from "@/data/courses";
import { pluralRu } from "@/lib/utils";

interface CourseCardProps {
  id: string;
  titleRu: string;
  titleEn: string;
  categoryId: string;
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
}

// Крупные числа сокращаются, как счётчик просмотров: 35 419 → 35 тыс.
const shortCount = (n: number, lang: "ru" | "en") => {
  if (n < 1000) return String(n);
  const k = (n / 1000).toFixed(n < 10000 ? 1 : 0).replace(/[.,]0$/, "");
  return lang === "ru" ? `${k.replace(".", ",")} тыс.` : `${k}K`;
};

const CourseCard = ({
  id,
  titleRu,
  titleEn,
  categoryId,
  categoryLabel,
  rating,
  students,
  image,
  imageBg,
  premium,
  price,
  isOwned,
}: CourseCardProps) => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const title = lang === "ru" ? titleRu : titleEn;
  const cat = categories.find((c) => c.id === categoryId);
  const Icon = cat?.icon;

  // Плашка в углу обложки — на месте длительности ролика
  const corner = isOwned
    ? lang === "ru" ? "Куплен" : "Owned"
    : premium
      ? lang === "ru" ? "Премиум" : "Premium"
      : price
        ? `${price} $`
        : lang === "ru" ? "Бесплатно" : "Free";

  const counted =
    lang === "ru"
      // У сокращённых чисел («35 тыс.») склонение всегда множественное
      ? `${shortCount(students, lang)} ${students < 1000 ? pluralRu(students, ["ученик", "ученика", "учеников"]) : "учеников"}`
      : `${shortCount(students, lang)} students`;

  return (
    <div onClick={() => navigate(`/course/${id}`)} className="flex flex-col gap-3 cursor-pointer group">
      {/* Обложка 16:9 со скруглением */}
      <div
        className="relative w-full aspect-video rounded-xl overflow-hidden bg-muted"
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
        <span className="absolute right-1.5 bottom-1.5 px-1.5 py-[2px] rounded-[4px] bg-black/80 text-white text-[12px] font-semibold leading-[16px]">
          {corner}
        </span>
      </div>

      {/* Строка под обложкой: аватар категории, заголовок, метаданные, три точки */}
      <div className="flex gap-3">
        {Icon && (
          <span
            className="flex-shrink-0 w-9 h-9 rounded-full flex items-center justify-center"
            style={{ background: cat?.bg, color: cat?.iconColor }}
          >
            <Icon className="w-[18px] h-[18px]" />
          </span>
        )}
        <div className="min-w-0 flex-1 flex flex-col gap-0.5">
          <h3 className="text-[16px] font-semibold leading-[1.3] line-clamp-2" style={{ color: "hsl(0 0% 6%)" }}>
            {title}
          </h3>
          <p className="text-[13px] leading-[1.35] truncate" style={{ color: "hsl(0 0% 38%)" }}>
            {categoryLabel} · {counted} · ★ {rating}
          </p>
        </div>
        <button
          onClick={(e) => e.stopPropagation()}
          aria-label="Ещё"
          className="flex-shrink-0 -mr-1 self-start"
          style={{ color: "hsl(0 0% 38%)" }}
        >
          <MoreVertical className="w-[18px] h-[18px]" />
        </button>
      </div>
    </div>
  );
};

export default CourseCard;
