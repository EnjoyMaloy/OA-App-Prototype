import { Sparkles, Bitcoin, ShieldCheck, BarChart3, PieChart, Snowflake, Wrench } from "lucide-react";

export interface CategoryItem {
  id: string;
  labelRu: string;
  labelEn: string;
  countRu: string;
  countEn: string;
  countColor: string;
  icon: React.ElementType;
  iconColor: string;
  bg: string;
}

export const categories: CategoryItem[] = [
  { id: "ai", labelRu: "AI-навыки", labelEn: "AI Skills", countRu: "Скоро", countEn: "Soon", countColor: "hsl(var(--cat-ai))", icon: Sparkles, iconColor: "hsl(var(--cat-ai-icon))", bg: "hsl(var(--cat-ai-bg))" },
  { id: "crypto", labelRu: "Основы\nкрипты", labelEn: "Crypto\nBasics", countRu: "2 курса", countEn: "2 courses", countColor: "hsl(var(--cat-crypto))", icon: Bitcoin, iconColor: "hsl(var(--cat-crypto))", bg: "hsl(var(--cat-crypto-bg))" },
  { id: "security", labelRu: "Безопасность", labelEn: "Security", countRu: "1 курс", countEn: "1 course", countColor: "hsl(var(--cat-security))", icon: ShieldCheck, iconColor: "hsl(var(--cat-security))", bg: "hsl(var(--cat-security-bg))" },
  { id: "trading", labelRu: "Трейдинг", labelEn: "Trading", countRu: "3 курса", countEn: "3 courses", countColor: "hsl(var(--cat-ai))", icon: BarChart3, iconColor: "hsl(var(--cat-trading-icon))", bg: "hsl(var(--cat-trading-bg))" },
  { id: "invest", labelRu: "Инвестиции", labelEn: "Investments", countRu: "4 курса", countEn: "4 courses", countColor: "hsl(var(--cat-invest))", icon: PieChart, iconColor: "hsl(var(--cat-invest))", bg: "hsl(var(--cat-invest-bg))" },
  { id: "web3", labelRu: "Web3 и DeFi", labelEn: "Web3 & DeFi", countRu: "4 курса", countEn: "4 courses", countColor: "hsl(var(--cat-web3))", icon: Snowflake, iconColor: "hsl(var(--cat-web3))", bg: "hsl(var(--cat-web3-bg))" },
  { id: "tools", labelRu: "Инструменты", labelEn: "Tools", countRu: "1 курс", countEn: "1 course", countColor: "hsl(var(--cat-tools))", icon: Wrench, iconColor: "hsl(var(--cat-tools))", bg: "hsl(var(--cat-tools-bg))" },
];

export interface CourseData {
  id: string;
  titleRu: string;
  titleEn: string;
  categoryId: string;
  rating: number;
  students: number;
  image: string;
  premium?: boolean;
  price?: number;
  isNew?: boolean;
  trending?: boolean;
}

export const courses: CourseData[] = [
  { id: "1", titleRu: "1 курс — Бесплатный", titleEn: "1 — Free course", categoryId: "web3", rating: 4.9, students: 371, image: "https://images.unsplash.com/photo-1621504450181-5d356f61d307?w=400&h=300&fit=crop", isNew: true },
  { id: "2", titleRu: "2 курс — В подписке без триала", titleEn: "2 — Subscription, no trial", categoryId: "invest", rating: 4.9, students: 35419, image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=400&h=300&fit=crop", premium: true, price: 49, trending: true },
  { id: "6", titleRu: "3 курс — В подписке с триалом", titleEn: "3 — Subscription with trial", categoryId: "crypto", rating: 4.7, students: 1024, image: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=400&h=300&fit=crop", premium: true, price: 49, isNew: true },
  { id: "7", titleRu: "4 курс — Платный без триала", titleEn: "4 — Paid, no trial", categoryId: "tools", rating: 4.6, students: 512, image: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=400&h=300&fit=crop", premium: true, price: 79, isNew: true },
  { id: "8", titleRu: "5 курс — Платный с триалом", titleEn: "5 — Paid with trial", categoryId: "tools", rating: 4.7, students: 640, image: "https://images.unsplash.com/photo-1483058712412-4245e9b90334?w=400&h=300&fit=crop", premium: true, price: 89, isNew: true },
  { id: "9", titleRu: "Экспериментальная стр курса", titleEn: "Experimental course page", categoryId: "web3", rating: 4.95, students: 2480, image: "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=400&h=300&fit=crop", premium: true, price: 59, isNew: true, trending: true },
];

export const getCategoryLabel = (catId: string, lang: "ru" | "en") => {
  const cat = categories.find((c) => c.id === catId);
  if (!cat) return "";
  return lang === "ru" ? cat.labelRu : cat.labelEn;
};
