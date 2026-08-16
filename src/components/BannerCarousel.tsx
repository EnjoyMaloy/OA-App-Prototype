import { useRef, useState } from "react";
import { useNavigate } from "react-router-dom";
import { banners } from "@/data/banners";

/** Лента промо-баннеров: листается смахиванием, снизу точки-индикаторы. */
const BannerCarousel = () => {
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
            className="flex-shrink-0 snap-center w-full rounded-[10px] overflow-hidden"
          >
            {/* Высоту задаёт сама картинка — макет показывается в исходных пропорциях */}
            <img src={banner.image} alt="" className="block w-full h-auto" />
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
