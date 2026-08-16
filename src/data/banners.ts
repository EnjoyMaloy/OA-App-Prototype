import imgCoin from "@/assets/3d-coin.png";
import imgRocket from "@/assets/3d-rocket.png";
import imgNft from "@/assets/3d-nft.png";
import bannerOpenClaw from "@/assets/banner-openclaw.jpg";
import bannerIllustrator from "@/assets/banner-illustrator.jpg";
import bannerCard from "@/assets/banner-card.jpg";

export interface Banner {
  id: string;
  /** Куда ведёт баннер */
  to: string;
  /** Готовый баннер картинкой: текст уже внутри, поверх ничего не рисуем */
  imageFull?: string;
  /** Поля ниже нужны только баннерам, которые собираются версткой */
  eyebrowRu?: string;
  eyebrowEn?: string;
  titleRu?: string;
  titleEn?: string;
  ctaRu?: string;
  ctaEn?: string;
  background?: string;
  image?: string;
}

export const banners: Banner[] = [
  { id: "openclaw", to: "/catalog", imageFull: bannerOpenClaw },
  { id: "illustrator", to: "/catalog", imageFull: bannerIllustrator },
  { id: "payment-card", to: "/catalog", imageFull: bannerCard },
  {
    id: "premium",
    eyebrowRu: "Премиум",
    eyebrowEn: "Premium",
    titleRu: "Все курсы по подписке — первый месяц бесплатно",
    titleEn: "Every course by subscription — first month free",
    ctaRu: "Попробовать",
    ctaEn: "Try it",
    to: "/catalog",
    background: "linear-gradient(135deg, #7E63A8 0%, #A66CFF 100%)",
    image: imgNft,
  },
  {
    id: "new-course",
    eyebrowRu: "Новый курс",
    eyebrowEn: "New course",
    titleRu: "Быстрый старт в Telegram Gifts",
    titleEn: "Quick start with Telegram Gifts",
    ctaRu: "Начать",
    ctaEn: "Start",
    to: "/my-courses",
    background: "linear-gradient(135deg, #FF9E7D 0%, #FF7D60 100%)",
    image: imgRocket,
  },
  {
    id: "referral",
    eyebrowRu: "Приглашай друзей",
    eyebrowEn: "Invite friends",
    titleRu: "500 звёзд за каждого, кто пройдёт первый урок",
    titleEn: "500 stars for every friend who finishes lesson one",
    ctaRu: "Позвать",
    ctaEn: "Invite",
    to: "/profile",
    background: "linear-gradient(135deg, #F5B02E 0%, #E88A1A 100%)",
    image: imgCoin,
  },
];
