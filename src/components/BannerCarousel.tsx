import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ChevronRight } from "lucide-react";
import { useLanguage } from "@/contexts/LanguageContext";
import { banners } from "@/data/banners";

/** Лента промо-баннеров: листается смахиванием, снизу точки-индикаторы. */
const BannerCarousel = () => {
  const { lang } = useLanguage();
  const navigate = useNavigate();
  const trackRef = useRef<HTMLDivElement>(null);
  const [active, setActive] = useState(0);

  // Считаем по реальным позициям слайдов: их ширина меньше контейнера на отступы и зазор
  const onScroll = () => {
    const el = trackRef.current;
    if (!el) return;
    const center = el.scrollLeft + el.clientWidth / 2;
    const slides = Array.from(el.children) as HTMLElement[];
    const index = slides.findIndex((s) => s.offsetLeft <= center && s.offsetLeft + s.offsetWidth >= center);
    if (index >= 0) setActive(index);
  };

  const goTo = (index: number) => {
    const el = trackRef.current;
    if (!el) return;
    const slide = el.children[index] as HTMLElement | undefined;
    if (!slide) return;
    el.scrollTo({ left: slide.offsetLeft - (el.clientWidth - slide.offsetWidth) / 2, behavior: "smooth" });
  };

  return (
    <div>
      <div
        ref={trackRef}
        onScroll={onScroll}
        className="flex overflow-x-auto scrollbar-hide snap-x snap-mandatory -mx-4 px-4 gap-3"
      >
        {banners.map((banner) => (
          <button
            key={banner.id}
            onClick={() => navigate(banner.to)}
            className={`relative flex-shrink-0 snap-center w-full h-[164px] rounded-[20px] overflow-hidden text-left ${
              banner.imageFull ? "" : "p-4 pr-28"
            }`}
            style={banner.background ? { background: banner.background } : undefined}
          >
            {banner.imageFull ? (
              // Готовый макет: показываем как есть, ничего сверху не накладываем
              <img src={banner.imageFull} alt="" className="absolute inset-0 w-full h-full object-cover" />
            ) : (
              <>
                <img
                  src={banner.image}
                  alt=""
                  aria-hidden
                  className="absolute -right-3 -bottom-3 w-32 h-32 object-contain pointer-events-none"
                />
                <span className="relative flex flex-col h-full justify-between">
                  <span className="block text-[12px] font-medium uppercase tracking-[0.06em] text-white/75">
                    {lang === "ru" ? banner.eyebrowRu : banner.eyebrowEn}
                  </span>
                  <span className="block text-white text-[20px] font-medium leading-[1.15] line-clamp-3">
                    {lang === "ru" ? banner.titleRu : banner.titleEn}
                  </span>
                  <span className="inline-flex items-center gap-0.5 text-[14px] font-medium text-white">
                    {lang === "ru" ? banner.ctaRu : banner.ctaEn}
                    <ChevronRight className="w-4 h-4" />
                  </span>
                </span>
              </>
            )}
          </button>
        ))}
      </div>

      <div className="flex items-center justify-center gap-1.5 mt-3">
        {banners.map((banner, index) => (
          <button
            key={banner.id}
            onClick={() => goTo(index)}
            aria-label={`${index + 1}`}
            className={`h-1.5 rounded-full transition-all ${
              index === active ? "w-5 bg-foreground/70" : "w-1.5 bg-foreground/20"
            }`}
          />
        ))}
      </div>
    </div>
  );
};

export default BannerCarousel;
