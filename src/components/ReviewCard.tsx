import { Star } from "lucide-react";

export interface Review {
  username: string;
  avatar: string;
  rating: number;
  timeRu: string;
  timeEn: string;
  textRu: string;
  textEn: string;
}

/** Карточка отзыва: одна и та же в ленте на странице курса и в списке «Все отзывы» */
const ReviewCard = ({
  review: r,
  lang,
  clamp = false,
}: {
  review: Review;
  lang: "ru" | "en";
  /** В ленте текст обрезается на пятой строке, чтобы карточки были одной высоты */
  clamp?: boolean;
}) => (
  <div className="h-full rounded-xl bg-sidebar p-6">
    <div className="flex gap-4 items-start mb-5">
      <div className="w-14 h-14 rounded-full overflow-hidden flex-shrink-0 border border-border/10">
        <img src={r.avatar} alt={r.username} className="w-full h-full object-cover" />
      </div>
      <div className="flex-1 min-w-0">
        <p className="text-[19px] font-semibold text-foreground tracking-tight leading-none mb-1.5">{r.username}</p>
        <div className="flex items-center justify-between gap-2">
          <div className="flex gap-1">
            {Array.from({ length: r.rating }).map((_, si) => (
              <Star key={si} className="w-[15px] h-[15px] fill-[#FF6B57] text-[#FF6B57]" />
            ))}
          </div>
          <span className="text-[13px] text-muted-foreground/80 font-normal whitespace-nowrap">
            {lang === "ru" ? r.timeRu : r.timeEn}
          </span>
        </div>
      </div>
    </div>
    <p className={`text-[15px] leading-[1.65] font-normal text-foreground/90${clamp ? " line-clamp-5" : ""}`}>
      {lang === "ru" ? r.textRu : r.textEn}
    </p>
  </div>
);

export default ReviewCard;
