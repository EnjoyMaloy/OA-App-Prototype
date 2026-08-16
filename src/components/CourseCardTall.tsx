import { LayoutGrid, Star, Check } from "lucide-react";
import { useNavigate } from "react-router-dom";
import PremiumStarIcon from "@/components/icons/PremiumStarIcon";
import { useLanguage } from "@/contexts/LanguageContext";

interface CourseCardTallProps {
  id: string;
  titleRu: string;
  titleEn: string;
  categoryLabel: string;
  rating: number;
  students: number;
  image: string;
  imageBg?: string;
  premium?: boolean;
  isOwned?: boolean;
  /** Ширина задаётся снаружи: в ленте фиксированная, в сетке — вся ячейка */
  className?: string;
}

/** Вертикальная карточка-афиша: обложка на весь блок, подписи поверх неё. */
const CourseCardTall = ({
  id,
  titleRu,
  titleEn,
  categoryLabel,
  rating,
  students,
  image,
  imageBg,
  premium,
  isOwned,
  className = "",
}: CourseCardTallProps) => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const title = lang === "ru" ? titleRu : titleEn;

  return (
    <button
      onClick={() => navigate(`/course/${id}`)}
      className={`group relative aspect-[3/4] rounded-[20px] overflow-hidden text-left ${className}`}
      style={imageBg ? { background: imageBg } : undefined}
    >
      <img
        src={image}
        alt={title}
        loading="lazy"
        className={`absolute inset-0 w-full h-full group-hover:scale-[1.04] transition-transform duration-300 ${
          imageBg ? "object-contain p-6" : "object-cover"
        }`}
      />

      {/* Затемнение снизу, чтобы подписи читались на любой обложке */}
      <div
        className="absolute inset-x-0 bottom-0 h-3/5 pointer-events-none"
        style={{ background: "linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.35) 45%, rgba(0,0,0,0) 100%)" }}
      />

      {/* Категория занимает верх целиком: в узкой карточке ей иначе не хватает места */}
      <span
        className="absolute top-3 left-3 max-w-[calc(100%-24px)] inline-flex items-center gap-1.5 rounded-full px-2.5 py-1 text-[11px] font-medium uppercase tracking-[0.04em] text-white"
        style={{ background: "rgba(0,0,0,0.35)", backdropFilter: "blur(8px)", WebkitBackdropFilter: "blur(8px)" }}
      >
        <LayoutGrid className="w-3 h-3 flex-shrink-0" strokeWidth={2.5} />
        <span className="truncate">{categoryLabel}</span>
      </span>

      <span className="absolute inset-x-0 bottom-0 p-3.5 block">
        <span className="block text-white text-[17px] font-medium leading-[1.2] line-clamp-2">{title}</span>
        <span className="flex items-center justify-between gap-2 mt-2">
          <span className="min-w-0 flex items-center gap-2 text-white/85 text-[13px] whitespace-nowrap overflow-hidden">
            <Star className="w-3.5 h-3.5 flex-shrink-0" fill="#FF7D60" strokeWidth={0} />
            {rating}
            <span className="text-white/50">·</span>
            <span className="truncate">{students.toLocaleString()}</span>
          </span>

          {/* Статус — иконкой: подпись не помещается рядом со счётчиком в узкой карточке */}
          {(premium || isOwned) && (
            <span
              className="flex-shrink-0 w-7 h-7 rounded-full inline-flex items-center justify-center text-white"
              style={{ background: "rgba(255,255,255,0.22)", backdropFilter: "blur(8px)", WebkitBackdropFilter: "blur(8px)" }}
              title={isOwned ? (lang === "ru" ? "Открыт" : "Owned") : lang === "ru" ? "Премиум" : "Premium"}
            >
              {isOwned ? (
                <Check className="w-4 h-4" strokeWidth={3} />
              ) : (
                <PremiumStarIcon className="w-4 h-4" fill="#FFFFFF" />
              )}
            </span>
          )}
        </span>
      </span>
    </button>
  );
};

export default CourseCardTall;
