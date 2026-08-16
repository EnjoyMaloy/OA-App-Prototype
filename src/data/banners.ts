import bannerOpenClaw from "@/assets/banner-openclaw.jpg";
import bannerIllustrator from "@/assets/banner-illustrator.jpg";
import bannerCard from "@/assets/banner-card.jpg";

export interface Banner {
  id: string;
  /** Готовый макет баннера: текст уже внутри картинки */
  image: string;
  /** Куда ведёт баннер */
  to: string;
}

export const banners: Banner[] = [
  { id: "openclaw", image: bannerOpenClaw, to: "/catalog" },
  { id: "illustrator", image: bannerIllustrator, to: "/catalog" },
  { id: "payment-card", image: bannerCard, to: "/catalog" },
];
