import { Sparkles, Bitcoin, ShieldCheck, BarChart3, PieChart, Snowflake, Wrench } from "lucide-react";
import imgRocket from "@/assets/3d-rocket.png";
import imgCoin from "@/assets/3d-coin.png";
import imgNft from "@/assets/3d-nft.png";
import imgSecurity from "@/assets/3d-security.png";
import imgMascot from "@/assets/mascot-success.png";
import imgLogo from "@/assets/logo.png";
// Обложки-иллюстрации: занимают всю карточку, поэтому без градиентной подложки
import coverGifts from "@/assets/cover-gifts.jpg";
import coverInvest from "@/assets/cover-invest.jpg";
import coverHamster from "@/assets/cover-hamster.jpg";
import coverTools from "@/assets/cover-tools.jpg";

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
  { id: "1", titleRu: "Telegram Gifts: как зарабатывать на подарках", titleEn: "Telegram Gifts: how to earn on digital gifts", categoryId: "web3", rating: 4.9, students: 371, image: coverGifts, isNew: true, updatedDaysAgo: 2 },
  { id: "2", titleRu: "Инвестиции с нуля: собираем первый портфель", titleEn: "Investing from scratch: building your first portfolio", categoryId: "invest", rating: 4.9, students: 35419, image: coverInvest, premium: true, price: 49, trending: true, updatedDaysAgo: 9 },
  { id: "6", titleRu: "Криптовалюты с нуля: биржи, кошельки, сделки", titleEn: "Crypto from scratch: exchanges, wallets, trades", categoryId: "crypto", rating: 4.7, students: 1024, image: coverHamster, premium: true, price: 49, isNew: true, updatedDaysAgo: 21 },
  { id: "7", titleRu: "Безопасность кошелька: как не потерять деньги", titleEn: "Wallet security: how not to lose your funds", categoryId: "tools", rating: 4.6, students: 512, image: coverTools, premium: true, price: 79, isNew: true, updatedDaysAgo: 45 },
  { id: "8", titleRu: "Трейдинг на споте: стратегии и риск-менеджмент", titleEn: "Spot trading: strategies and risk management", categoryId: "tools", rating: 4.7, students: 640, image: coverHamster, premium: true, price: 89, isNew: true, updatedDaysAgo: 120 },
  { id: "9", titleRu: "Web3-карьера: как войти в индустрию", titleEn: "Web3 career: how to enter the industry", categoryId: "web3", rating: 4.95, students: 2480, image: coverGifts, premium: true, price: 59, isNew: true, trending: true, updatedDaysAgo: 400 },
];

export const getCategoryLabel = (catId: string, lang: "ru" | "en") => {
  const cat = categories.find((c) => c.id === catId);
  if (!cat) return "";
  return lang === "ru" ? cat.labelRu : cat.labelEn;
};
