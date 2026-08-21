import { Sparkles, Bitcoin, ShieldCheck, BarChart3, PieChart, Snowflake, Wrench } from "lucide-react";
import imgRocket from "@/assets/3d-rocket.png";
import imgCoin from "@/assets/3d-coin.png";
import imgNft from "@/assets/3d-nft.png";
import imgSecurity from "@/assets/3d-security.png";
import imgMascot from "@/assets/mascot-success.png";
import imgLogo from "@/assets/logo.png";

export interface CategoryItem {
  id: string;
  labelRu: string;
  labelEn: string;
  labelColor: string;
  icon: React.ElementType;
  iconColor: string;
  bg: string;
}

export const categories: CategoryItem[] = [
  { id: "ai", labelRu: "AI-навыки", labelEn: "AI Skills", labelColor: "hsl(var(--cat-ai))", icon: Sparkles, iconColor: "hsl(var(--cat-ai-icon))", bg: "hsl(var(--cat-ai-bg))" },
  { id: "crypto", labelRu: "Основы\nкрипты", labelEn: "Crypto\nBasics", labelColor: "hsl(var(--cat-crypto))", icon: Bitcoin, iconColor: "hsl(var(--cat-crypto))", bg: "hsl(var(--cat-crypto-bg))" },
  { id: "security", labelRu: "Безопасность", labelEn: "Security", labelColor: "hsl(var(--cat-security))", icon: ShieldCheck, iconColor: "hsl(var(--cat-security))", bg: "hsl(var(--cat-security-bg))" },
  { id: "trading", labelRu: "Трейдинг", labelEn: "Trading", labelColor: "hsl(var(--cat-trading))", icon: BarChart3, iconColor: "hsl(var(--cat-trading-icon))", bg: "hsl(var(--cat-trading-bg))" },
  { id: "invest", labelRu: "Инвестиции", labelEn: "Investments", labelColor: "hsl(var(--cat-invest))", icon: PieChart, iconColor: "hsl(var(--cat-invest))", bg: "hsl(var(--cat-invest-bg))" },
  { id: "web3", labelRu: "Web3 и DeFi", labelEn: "Web3 & DeFi", labelColor: "hsl(var(--cat-web3))", icon: Snowflake, iconColor: "hsl(var(--cat-web3))", bg: "hsl(var(--cat-web3-bg))" },
  { id: "tools", labelRu: "Инструменты", labelEn: "Tools", labelColor: "hsl(var(--cat-tools))", icon: Wrench, iconColor: "hsl(var(--cat-tools))", bg: "hsl(var(--cat-tools-bg))" },
];

export interface CourseData {
  id: string;
  titleRu: string;
  titleEn: string;
  categoryId: string;
  rating: number;
  students: number;
  /** 3D-объект обложки: лежит в проекте, поэтому грузится и без сети */
  image: string;
  /** Подложка под объектом — градиент в цветах категории. Без неё картинка заполняет обложку целиком */
  imageBg?: string;
  premium?: boolean;
  price?: number;
  isNew?: boolean;
  trending?: boolean;
  /** Сколько дней назад курс обновляли — из этого считается «2 недели назад» */
  updatedDaysAgo: number;
}

export const courses: CourseData[] = [
  { id: "1", titleRu: "1 курс — Бесплатный", titleEn: "1 — Free course", categoryId: "web3", rating: 4.9, students: 371, image: imgRocket, imageBg: "linear-gradient(135deg, #E8DCFB 0%, #A66CFF 100%)", isNew: true, updatedDaysAgo: 2 },
  { id: "2", titleRu: "2 курс — В подписке без триала", titleEn: "2 — Subscription, no trial", categoryId: "invest", rating: 4.9, students: 35419, image: imgCoin, imageBg: "linear-gradient(135deg, #FFF1CC 0%, #F5B02E 100%)", premium: true, price: 49, trending: true, updatedDaysAgo: 9 },
  { id: "6", titleRu: "3 курс — В подписке с триалом", titleEn: "3 — Subscription with trial", categoryId: "crypto", rating: 4.7, students: 1024, image: imgNft, imageBg: "linear-gradient(135deg, #FFDFD1 0%, #FF7D60 100%)", premium: true, price: 49, isNew: true, updatedDaysAgo: 21 },
  { id: "7", titleRu: "4 курс — Платный без триала", titleEn: "4 — Paid, no trial", categoryId: "tools", rating: 4.6, students: 512, image: imgSecurity, imageBg: "linear-gradient(135deg, #FFD6EC 0%, #EE49A4 100%)", premium: true, price: 79, isNew: true, updatedDaysAgo: 45 },
  { id: "8", titleRu: "5 курс — Платный с триалом", titleEn: "5 — Paid with trial", categoryId: "tools", rating: 4.7, students: 640, image: imgMascot, imageBg: "linear-gradient(135deg, #CFF3E9 0%, #34C8A0 100%)", premium: true, price: 89, isNew: true, updatedDaysAgo: 120 },
  { id: "9", titleRu: "Экспериментальная стр курса", titleEn: "Experimental course page", categoryId: "web3", rating: 4.95, students: 2480, image: imgLogo, imageBg: "linear-gradient(135deg, #FFFFFF 0%, #EFECF7 100%)", premium: true, price: 59, isNew: true, trending: true, updatedDaysAgo: 400 },
];

export const getCategoryLabel = (catId: string, lang: "ru" | "en") => {
  const cat = categories.find((c) => c.id === catId);
  if (!cat) return "";
  return lang === "ru" ? cat.labelRu : cat.labelEn;
};
