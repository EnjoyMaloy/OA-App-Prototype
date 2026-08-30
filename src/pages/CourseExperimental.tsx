import { useEffect, useRef, useState } from "react";
import { useLocation, useNavigate, useSearchParams, useParams } from "react-router-dom";
import { useLanguage } from "@/contexts/LanguageContext";
import { usePurchaseStore } from "@/hooks/usePurchaseStore";
import {
  ChevronLeft,
  Heart,
  Star,
  Users,
  Calendar,
  ChevronRight,
  Play,
  Send,
  Twitter,
  Youtube,
  Instagram,
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { formatRating, pluralRu } from "@/lib/utils";
import ReviewCard, { type Review } from "@/components/ReviewCard";
import CourseCard from "@/components/CourseCard";
import authorPhoto from "@/assets/author-photo.jpg";
import { courses as allCourses, getCategoryLabel } from "@/data/courses";
import courseHeroAsset from "@/assets/course-experimental-hero.png.asset.json";
// Картинки берём из проекта: внешние ссылки в прототипе не грузятся
import coverGifts from "@/assets/cover-gifts.jpg";
import coverInvest from "@/assets/cover-invest.jpg";
import coverHamster from "@/assets/cover-hamster.jpg";
import coverTools from "@/assets/cover-tools.jpg";
import avatarAlex from "@/assets/avatar-alex.jpg";
import avatarAnna from "@/assets/avatar-anna.jpg";
import avatarDmitry from "@/assets/avatar-dmitry.jpg";
import avatarSychev from "@/assets/avatar-sychev.jpg";

type Scenario = "free" | "sub" | "sub-trial" | "paid" | "paid-trial";
/** Из чего состоит урок: у одного урока может быть сразу видео, квиз и инструкция */
type LessonType = "video" | "quiz" | "guide";

interface CourseConfig {
  id: string;
  scenario: Scenario;
  titleRu: string;
  titleEn: string;
  descriptionRu: string;
  descriptionEn: string;
  categoryRu: string;
  categoryEn: string;
  levelRu: string;
  levelEn: string;
  image: string;
  rating: number;
  reviewCount: number;
  students: number;
  updatedRu: string;
  updatedEn: string;
  price: number | null;        // one-time price (paid scenarios)
  monthlyFrom?: number;        // shown for subscription scenarios
  trialLessons?: number;       // for *-trial scenarios
  color: { base: string; light: string; superLight: string; dark: string };
  lessons: { titleRu: string; titleEn: string; min: number; types: LessonType[] }[];
  reviews: Review[];
}

const COLORS = {
  red:   { base: "#FF3D4D", light: "#FFD8DC", superLight: "#FFEEF0", dark: "#7A0A14" },
  blue:  { base: "#3D8BFF", light: "#D5E5FF", superLight: "#EDF3FF", dark: "#0A2E7A" },
  green: { base: "#22C55E", light: "#CFF3DC", superLight: "#ECFBF0", dark: "#0D4A24" },
  amber: { base: "#F59E0B", light: "#FCE7BD", superLight: "#FEF5E1", dark: "#7A4A07" },
  purple:{ base: "#A66CFF", light: "#E5D6FF", superLight: "#F3ECFF", dark: "#460466" },
  teal:  { base: "#14B8A6", light: "#C7F0EA", superLight: "#E7F8F5", dark: "#0D4A44" },
};

const REVIEWS_DEMO: Review[] = [
  {
    username: "Shahriyar2100",
    avatar: avatarAlex,
    rating: 5,
    timeRu: "1 неделю назад",
    timeEn: "1 week ago",
    textRu: "Да, это именно те шаблоны. Хотите сделать один специально для своего курса? Просто напишите мне: 1. *Название курса* 2. *Оценка*, которую вы бы поставили из 5 3. *1-2 вещи*, которые вам понравились 4. *1 вещь*, которую вы бы улучшили. Я превращу это в аккуратный отзыв, который вы сможете опубликовать за 10 секунд.",
    textEn: "Yep, those are the templates. Want to make one specific to your course? Just drop me: 1. *Course name* 2. *Rating* you'd give /5 3. *1-2 things you liked* 4. *1 thing you'd improve* I'll turn it into a clean review you can post in 10 seconds."
  },
  {
    username: "pawansatoshi",
    avatar: avatarAnna,
    rating: 5,
    timeRu: "1 неделю назад",
    timeEn: "1 week ago",
    textRu: "Отличное введение. Курс четко объясняет ключевые понятия и даёт практические инсайты. Легко понять новичкам, при этом полезно и продвинутым.",
    textEn: "Great introduction. The course clearly explains the key concepts and gives practical insights. Easy to understand for beginners while still useful for advanced users."
  },
  {
    username: "mgnt_eth",
    avatar: avatarDmitry,
    rating: 5,
    timeRu: "2 недели назад",
    timeEn: "2 weeks ago",
    textRu: "Проходил в метро по 15 минут в день — за две недели закрыл весь курс. Формат уроков как раз под такой ритм.",
    textEn: "Took it on the subway, 15 minutes a day, and finished in two weeks. The lesson format fits that rhythm perfectly.",
  },
  {
    username: "denis.web3",
    avatar: avatarSychev,
    rating: 4,
    timeRu: "3 недели назад",
    timeEn: "3 weeks ago",
    textRu: "Практики хотелось бы ещё больше, но база собрана отлично: после третьего блока наконец перестала бояться кошельков.",
    textEn: "I'd love even more practice, but the basics are solid: after the third module I finally stopped being scared of wallets.",
  },
];

const REVIEWS_FREE: Review[] = [
  {
    username: "crypto_fan",
    avatar: avatarDmitry,
    rating: 5,
    timeRu: "2 месяца назад",
    timeEn: "2 months ago",
    textRu: "Отличный бесплатный курс для начинающих! Всё понятно объясняется, быстро разобрался с Telegram Gifts.",
    textEn: "Great free course for beginners! Everything is explained clearly, I quickly figured out Telegram Gifts.",
  },
  REVIEWS_DEMO[1],
  REVIEWS_DEMO[2],
  REVIEWS_DEMO[3],
];

const REVIEWS_INVEST: Review[] = [
  {
    username: "elijah_andikan",
    avatar: avatarSychev,
    rating: 5,
    timeRu: "5 месяцев назад",
    timeEn: "5 months ago",
    textRu: "Рекомендую на 100%. Я новичок в крипте, и часто видел, как KOL и блогеры рекомендуют проекты — всегда было интересно, как они их выбирают. Курс закрыл этот вопрос.",
    textEn: "I 100% recommend this course. I'm a newbie in crypto and I usually see how KOLs recommend projects on Twitter — I always wondered how they pick them. This course solved that.",
  },
  {
    username: "patr1ckk",
    avatar: avatarAlex,
    rating: 5,
    timeRu: "5 месяцев назад",
    timeEn: "5 months ago",
    textRu: "Курс отличный. По делу, без воды, чётко по шагам — что и зачем проверять в проекте.",
    textEn: "Great course. To the point, no fluff, clear steps — what to check in a project and why.",
  },
];

const COURSE_CONFIGS: Record<string, CourseConfig> = {
  "1": {
    id: "1",
    scenario: "free",
    titleRu: "Telegram Gifts: цифровые подарки и NFT",
    titleEn: "Telegram Gifts: digital gifts & NFTs",
    descriptionRu: "Бесплатный курс о том, как использовать Telegram Gifts: создавать уникальные цифровые подарки, собирать коллекции и зарабатывать на NFT-подарках в экосистеме Telegram.",
    descriptionEn: "A free course on Telegram Gifts: create unique digital gifts, build collections, and earn from NFT gifts inside the Telegram ecosystem.",
    categoryRu: "Web3 и DeFi",
    categoryEn: "Web3 & DeFi",
    levelRu: "Начальный",
    levelEn: "Beginner",
    image: coverGifts,
    rating: 4.9,
    reviewCount: 85,
    students: 371,
    updatedRu: "Обновлён 10.04.26",
    updatedEn: "Updated 04/10/26",
    price: null,
    color: COLORS.green,
    lessons: [
      { titleRu: "Что такое Telegram Gifts", titleEn: "What are Telegram Gifts", min: 6, types: ["video"] },
      { titleRu: "Создание первого подарка", titleEn: "Creating your first gift", min: 10, types: ["video", "quiz"] },
      { titleRu: "Коллекции и редкость", titleEn: "Collections & rarity", min: 12, types: ["video", "guide"] },
      { titleRu: "Монетизация подарков", titleEn: "Monetizing gifts", min: 14, types: ["video", "quiz", "guide"] },
    ],
    reviews: REVIEWS_FREE,
  },
  "2": {
    id: "2",
    scenario: "sub",
    titleRu: "Анализ проектов: как выбирать перспективное",
    titleEn: "Project analysis: picking winners",
    descriptionRu: "Научимся анализировать потенциальные проекты для инвестиций: читать whitepaper, проверять токеномику и оценивать команду. Понятные инструменты для выбора и защиты от скама.",
    descriptionEn: "Learn to analyze investment projects: read whitepapers, verify tokenomics, and evaluate teams. Clear tools for picking projects and avoiding scams.",
    categoryRu: "Инвестиции",
    categoryEn: "Investments",
    levelRu: "Средний",
    levelEn: "Intermediate",
    image: coverInvest,
    rating: 4.9,
    reviewCount: 1010,
    students: 35419,
    updatedRu: "Обновлён 07.04.26",
    updatedEn: "Updated 04/07/26",
    price: null,
    monthlyFrom: 6,
    color: COLORS.blue,
    lessons: [
      { titleRu: "Введение в анализ", titleEn: "Introduction to analysis", min: 10, types: ["video"] },
      { titleRu: "Чтение Whitepaper", titleEn: "Reading whitepapers", min: 18, types: ["video", "quiz"] },
      { titleRu: "Токеномика", titleEn: "Tokenomics", min: 22, types: ["video", "guide"] },
      { titleRu: "Оценка команды", titleEn: "Evaluating the team", min: 16, types: ["video", "quiz", "guide"] },
      { titleRu: "Чек-лист: красные флаги", titleEn: "Red flags checklist", min: 14, types: ["video"] },
    ],
    reviews: REVIEWS_INVEST,
  },
  "6": {
    id: "6",
    scenario: "sub-trial",
    titleRu: "Основы крипты с триалом",
    titleEn: "Crypto basics with trial",
    descriptionRu: "Курс с триалом — пройдите первые 2 урока бесплатно, чтобы оценить материал. Доступ к остальным урокам открывается по подписке Premium.",
    descriptionEn: "A course with a trial — complete the first 2 lessons for free to evaluate the material. The rest unlocks with a Premium subscription.",
    categoryRu: "Основы крипты",
    categoryEn: "Crypto Basics",
    levelRu: "Начальный",
    levelEn: "Beginner",
    image: coverHamster,
    rating: 4.7,
    reviewCount: 312,
    students: 1024,
    updatedRu: "Обновлён 01.06.26",
    updatedEn: "Updated 06/01/26",
    price: null,
    monthlyFrom: 6,
    trialLessons: 2,
    color: COLORS.purple,
    lessons: [
      { titleRu: "Знакомство", titleEn: "Introduction", min: 8, types: ["video"] },
      { titleRu: "Основные концепции", titleEn: "Core concepts", min: 12, types: ["video", "quiz"] },
      { titleRu: "Практика (Премиум)", titleEn: "Practice (Premium)", min: 18, types: ["video", "guide"] },
      { titleRu: "Продвинутые темы", titleEn: "Advanced topics", min: 22, types: ["video", "quiz", "guide"] },
    ],
    reviews: REVIEWS_DEMO,
  },
  "7": {
    id: "7",
    scenario: "paid",
    titleRu: "Инструменты Web3-исследователя",
    titleEn: "Web3 researcher toolkit",
    descriptionRu: "Самостоятельный платный курс, не входит в подписку Premium. Доступ открывается только после разовой покупки.",
    descriptionEn: "A standalone paid course, not included in the Premium subscription. Access is granted only after a one-time purchase.",
    categoryRu: "Инструменты",
    categoryEn: "Tools",
    levelRu: "Средний",
    levelEn: "Intermediate",
    image: coverTools,
    rating: 4.6,
    reviewCount: 128,
    students: 512,
    updatedRu: "Обновлён 05.06.26",
    updatedEn: "Updated 06/05/26",
    price: 79,
    color: COLORS.amber,
    lessons: [
      { titleRu: "Введение", titleEn: "Introduction", min: 8, types: ["video"] },
      { titleRu: "Основы", titleEn: "Basics", min: 16, types: ["video", "quiz"] },
      { titleRu: "Боевые кейсы", titleEn: "Real-world cases", min: 24, types: ["video", "guide"] },
      { titleRu: "Практика", titleEn: "Hands-on practice", min: 28, types: ["video", "quiz", "guide"] },
      { titleRu: "Итог", titleEn: "Summary", min: 10, types: ["video"] },
    ],
    reviews: REVIEWS_DEMO,
  },
  "8": {
    id: "8",
    scenario: "paid-trial",
    titleRu: "Глубокая практика с триалом",
    titleEn: "Deep practice with trial",
    descriptionRu: "Самостоятельный платный курс вне подписки. Первые 3 урока доступны бесплатно — далее открывайте доступ покупкой курса.",
    descriptionEn: "Standalone paid course outside the subscription. First 3 lessons are free — unlock the rest with a one-time purchase.",
    categoryRu: "Инструменты",
    categoryEn: "Tools",
    levelRu: "Продвинутый",
    levelEn: "Advanced",
    image: coverGifts,
    rating: 4.7,
    reviewCount: 156,
    students: 640,
    updatedRu: "Обновлён 08.06.26",
    updatedEn: "Updated 06/08/26",
    price: 89,
    trialLessons: 3,
    color: COLORS.teal,
    lessons: [
      { titleRu: "Урок 1 (бесплатно)", titleEn: "Lesson 1 (free)", min: 8, types: ["video"] },
      { titleRu: "Урок 2 (бесплатно)", titleEn: "Lesson 2 (free)", min: 12, types: ["video", "quiz"] },
      { titleRu: "Урок 3 (бесплатно)", titleEn: "Lesson 3 (free)", min: 14, types: ["video", "guide"] },
      { titleRu: "Урок 4 (после покупки)", titleEn: "Lesson 4 (after purchase)", min: 18, types: ["video", "quiz", "guide"] },
      { titleRu: "Урок 5 (после покупки)", titleEn: "Lesson 5 (after purchase)", min: 22, types: ["video"] },
    ],
    reviews: REVIEWS_DEMO,
  },
  "9": {
    id: "9",
    scenario: "sub",
    titleRu: "Экспериментальная стр курса",
    titleEn: "Experimental course page",
    descriptionRu: "Полностью переосмысленная страница курса — больше визуала, больше воздуха, больше пользы. Узнайте, как мы экспериментируем с подачей образовательного контента.",
    descriptionEn: "A fully rethought course page — more visual, more breathing room, more value. See how we experiment with educational delivery.",
    categoryRu: "Web3 и DeFi",
    categoryEn: "Web3 & DeFi",
    levelRu: "Средний",
    levelEn: "Intermediate",
    image: courseHeroAsset.url,
    rating: 4.95,
    reviewCount: 128,
    students: 2480,
    updatedRu: "Обновлён 12.06.26",
    updatedEn: "Updated 06/12/26",
    price: null,
    monthlyFrom: 6,
    color: COLORS.red,
    lessons: [
      { titleRu: "Что такое эксперименты в Web3", titleEn: "What are Web3 experiments", min: 8, types: ["video"] },
      { titleRu: "Подготовка окружения", titleEn: "Setting up environment", min: 12, types: ["video", "quiz"] },
      { titleRu: "Первый сценарий", titleEn: "First scenario", min: 12, types: ["video", "guide"] },
      { titleRu: "Архитектура решений", titleEn: "Solution architecture", min: 18, types: ["video", "quiz", "guide"] },
      { titleRu: "Практика: запуск", titleEn: "Practice: launch", min: 22, types: ["video"] },
      { titleRu: "Разбор кейсов", titleEn: "Case studies", min: 30, types: ["video", "quiz"] },
      { titleRu: "Постановка задачи", titleEn: "Define the task", min: 15, types: ["video", "guide"] },
      { titleRu: "Реализация", titleEn: "Build", min: 25, types: ["video", "quiz", "guide"] },
      { titleRu: "Защита и фидбек", titleEn: "Review & feedback", min: 15, types: ["video"] },
    ],
    reviews: REVIEWS_DEMO,
  },
};

/** Отзывы лентой: листается вбок бесконечно, снизу точки текущей карточки */
const ReviewsRail = ({ reviews, lang }: { reviews: Review[]; lang: "ru" | "en" }) => {
  const railRef = useRef<HTMLDivElement>(null);
  const [active, setActive] = useState(0);
  // Три копии подряд: доходя до края, незаметно возвращаемся в среднюю — лента не кончается
  const loop = [...reviews, ...reviews, ...reviews];

  useEffect(() => {
    const el = railRef.current;
    if (el) el.scrollLeft = el.scrollWidth / 3;
  }, [reviews]);

  const onScroll = () => {
    const el = railRef.current;
    if (!el) return;
    const set = el.scrollWidth / 3;
    if (el.scrollLeft < set * 0.5) el.scrollLeft += set;
    else if (el.scrollLeft > set * 1.5) el.scrollLeft -= set;
    const card = set / reviews.length;
    setActive(Math.round((el.scrollLeft % set) / card) % reviews.length);
  };

  return (
    <>
      <div
        ref={railRef}
        onScroll={onScroll}
        className="flex items-stretch gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory scroll-pl-4 -mx-4 px-4 md:mx-0 md:px-0 md:scroll-pl-0 pb-1"
      >
        {loop.map((r, i) => (
          <div key={i} className="flex-shrink-0 snap-start w-[86%] md:w-[420px]">
            <ReviewCard review={r} lang={lang} clamp />
          </div>
        ))}
      </div>

      {/* Точки: какая карточка сейчас перед глазами */}
      <div className="flex justify-center items-center gap-2 pt-1">
        {reviews.map((_, i) => (
          <span
            key={i}
            className={`h-2 rounded-full transition-all ${
              i === active ? "w-5 bg-foreground/70" : "w-2 bg-foreground/20"
            }`}
          />
        ))}
      </div>
    </>
  );
};

/** Плей со скруглёнными углами: треугольник обводится сам собой с round-стыками */
const PlayRounded = ({ className = "" }: { className?: string }) => (
  <svg viewBox="0 0 24 24" className={className} fill="currentColor" stroke="currentColor" strokeWidth={3.6} strokeLinejoin="round" strokeLinecap="round">
    <path d="M9 6.2v11.6L18.4 12z" />
  </svg>
);

const CourseExperimental = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { lang } = useLanguage();
  const [liked, setLiked] = useState(false);
  const store = usePurchaseStore();
  const [searchParams] = useSearchParams();
  const searchQuery = searchParams.get("q") || "";
  const { id: routeId } = useParams<{ id: string }>();

  const config = COURSE_CONFIGS[routeId ?? "9"] ?? COURSE_CONFIGS["9"];
  const COURSE_ID = config.id;
  const COURSE_COLOR = config.color;
  const IMG = config.image;
  const lessons = config.lessons;
  const reviews = config.reviews;

  const title = lang === "ru" ? config.titleRu : config.titleEn;
  const description = lang === "ru" ? config.descriptionRu : config.descriptionEn;
  const updated = lang === "ru" ? config.updatedRu : config.updatedEn;

  const isPurchased = store.purchasedCourses.includes(COURSE_ID);
  const hasSubscription = store.subscription?.active;
  const isStandalone = config.scenario === "paid" || config.scenario === "paid-trial";
  const isFree = config.scenario === "free";
  // Оплата и триал на странице пока не показываются, но статус нужен карточкам в лентах
  const isOwned = isFree || isPurchased || (!isStandalone && hasSubscription);

  // Курсы для лент внизу страницы: остальные курсы автора и соседи по категории
  const currentCategoryId = allCourses.find((c) => c.id === COURSE_ID)?.categoryId;
  const otherCourses = allCourses.filter((c) => c.id !== COURSE_ID);
  const similarCourses = otherCourses.filter((c) => c.categoryId === currentCategoryId);

  // Подпись кнопки «назад»: раздел, из которого открыли курс
  const fromPath = (location.state as { fromPath?: string } | null)?.fromPath ?? "";
  const backLabel = (() => {
    if (fromPath.startsWith("/catalog")) return lang === "ru" ? "Каталог" : "Catalog";
    if (fromPath.startsWith("/my-courses")) return lang === "ru" ? "Мои курсы" : "My courses";
    if (fromPath.startsWith("/collection/new")) return lang === "ru" ? "Новое" : "New";
    if (fromPath.startsWith("/collection/trending")) return lang === "ru" ? "В тренде" : "Trending";
    if (fromPath === "/") return lang === "ru" ? "Главная" : "Home";
    return lang === "ru" ? "Назад" : "Back";
  })();

  const startCourse = () => navigate(`/course/${COURSE_ID}/lessons`);

  const filteredLessons = lessons.filter(l => {
    const q = searchQuery.toLowerCase();
    return (
      l.titleRu.toLowerCase().includes(q) ||
      l.titleEn.toLowerCase().includes(q)
    );
  });

  const totalMin = filteredLessons.reduce((s, l) => s + l.min, 0);

  return (
    <div className="min-h-screen bg-background">
      {/* HERO: обложка с градиентом сверху, ниже — обычный белый фон страницы */}
      <div className="relative">
        {/* И картинка, и её градиентная подложка растворяются книзу по общей маске */}
        <div
          className="relative aspect-[4/3] md:aspect-[21/9]"
          style={{
            backgroundColor: COURSE_COLOR.superLight,
            backgroundImage: `radial-gradient(120% 90% at 100% 0%, ${COURSE_COLOR.light} 0%, transparent 60%), radial-gradient(120% 80% at 0% 100%, ${COURSE_COLOR.base}2E 0%, transparent 55%)`,
            maskImage: "linear-gradient(to bottom, #000 68%, transparent 100%)",
            WebkitMaskImage: "linear-gradient(to bottom, #000 68%, transparent 100%)",
          }}
        >
          <img src={IMG} alt={title} className="absolute inset-0 w-full h-full object-cover" />
        </div>

        {/* Кнопки поверх обложки — вне маски, поэтому не растворяются */}
        <button
          onClick={() => navigate(-1)}
          // Кнопка «назад» держится у верхнего края и при прокрутке
          className="glass fixed left-4 top-[max(14px,env(safe-area-inset-top))] z-50 h-11 pl-2.5 pr-4 rounded-full inline-flex items-center gap-1 text-[16px] font-medium text-foreground active:scale-95 transition-transform"
        >
          <ChevronLeft strokeWidth={2.4} className="w-[21px] h-[21px]" />
          {backLabel}
        </button>

        {/* Избранное и поделиться — столбиком у правого края */}
        <div className="absolute right-3 top-[max(14px,env(safe-area-inset-top))]">
          <button
            onClick={() => setLiked((v) => !v)}
            aria-label={lang === "ru" ? "В избранное" : "Save"}
            aria-pressed={liked}
            className="w-11 h-11 -mr-1 flex items-center justify-center active:scale-95 transition-transform"
          >
            {/* Сердце белое, при нажатии заливается красным — белый контур остаётся */}
            <Heart
              strokeWidth={liked ? 2 : 1.6}
              className="w-[26px] h-[26px] transition-colors"
              stroke={liked ? "#FFFFFF" : "rgba(0,0,0,0.38)"}
              fill={liked ? "#FF3B5C" : "#FFFFFF"}
              style={{ filter: "drop-shadow(0 1px 3px rgba(0,0,0,0.28))" }}
            />
          </button>

        </div>

        {/* Заголовок, чип с информацией и кнопка — по центру */}
        <div className="px-6 pb-9 -mt-4 md:-mt-10 flex flex-col items-center text-center">
          <h1 className="text-[32px] md:text-[48px] leading-[1.05] font-medium tracking-[-0.02em] text-foreground max-w-[640px]">
            {title}
          </h1>
          <p className="mt-3 text-[16px] md:text-[19px] leading-[1.45] text-muted-foreground max-w-[520px]">
            {description}
          </p>

          {/* Чип с информацией о курсе */}
          <div className="mt-5 inline-flex items-center gap-2 h-[38px] px-4 rounded-full bg-muted text-[14px] text-muted-foreground">
            <Star className="w-[15px] h-[15px] fill-orange-400 text-orange-400" />
            <span className="font-semibold text-foreground">{formatRating(config.rating)}</span>
            <span aria-hidden className="opacity-40">·</span>
            <span>
              {config.students.toLocaleString("ru-RU")}{" "}
              {lang === "ru"
                ? pluralRu(config.students, ["ученик", "ученика", "учеников"])
                : "students"}
            </span>
            <span aria-hidden className="opacity-40">·</span>
            <span>{totalMin} {lang === "ru" ? "мин" : "min"}</span>
          </div>

        </div>
      </div>

      <div className="w-full px-4 md:px-8 py-8 pb-[calc(96px+env(safe-area-inset-bottom))]">
        <div>
          {/* MAIN COL */}
          <div className="min-w-0 space-y-10">
            {/* Lessons */}
            <section>
              <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-6">
                <div className="flex items-end justify-between sm:justify-start sm:gap-4 flex-1">
                  <h2 className="text-[28px] md:text-[32px] font-semibold tracking-tight text-foreground">
                    {lang === "ru" ? "Программа курса" : "Curriculum"}
                  </h2>
                  <span className="text-[14px] text-muted-foreground">
                    {totalMin} {lang === "ru" ? "мин" : "min"}
                  </span>
                </div>
              </div>

              {filteredLessons.length > 0 ? (
                /* Полосы во всю ширину: номер, название, форматы урока и длительность */
                <div className="rounded-2xl bg-sidebar overflow-hidden">
                  {filteredLessons.map((l, i) => {
                    const originalIndex = lessons.findIndex((orig) => orig.titleRu === l.titleRu);
                    const lessonNo = originalIndex !== -1 ? originalIndex + 1 : i + 1;
                    return (
                      <div
                        key={i}
                        className={`flex items-start gap-3 px-4 py-3.5 ${i > 0 ? "border-t border-border/40" : ""}`}
                      >
                        <span className="w-6 flex-shrink-0 pt-0.5 text-[15px] text-muted-foreground tabular-nums">
                          {String(lessonNo).padStart(2, "0")}
                        </span>

                        <div className="min-w-0 flex-1">
                          <p className="text-[18px] font-medium leading-[1.25] text-foreground">
                            {lang === "ru" ? l.titleRu : l.titleEn}
                          </p>

                        </div>

                        <span className="flex-shrink-0 pt-0.5 text-[14px] text-muted-foreground">
                          {l.min} {lang === "ru" ? "мин" : "min"}
                        </span>
                      </div>
                    );
                  })}
                </div>
              ) : (
                <div className="rounded-xl bg-sidebar p-8 text-center text-muted-foreground text-[15px]">
                  {lang === "ru" ? "Уроки не найдены" : "No lessons found"}
                </div>
              )}
            </section>

            {/* Reviews */}
            <section className="space-y-6">
              <div className="flex items-center justify-between">
                <h2 className="text-[28px] md:text-[32px] font-semibold text-foreground tracking-tight">
                  {lang === "ru" ? `Отзывы (${config.reviewCount})` : `Reviews (${config.reviewCount})`}
                </h2>
                <button
                  onClick={() => navigate(`/course/${COURSE_ID}/reviews`)}
                  className="text-[15px] text-muted-foreground font-normal transition-colors inline-flex items-center gap-1"
                >
                  {lang === "ru" ? "Показать все" : "View All"}
                  <ChevronRight className="w-4 h-4" />
                </button>
              </div>

              <ReviewsRail reviews={reviews} lang={lang} />
            </section>

            {/* Кто создал курс: фото 1:1 слева, имя, строка описания и соцсети справа */}
            <section>
              <h2 className="text-[28px] md:text-[32px] font-semibold tracking-tight text-foreground mb-6">
                {lang === "ru" ? "Кто создал курс" : "Who made this course"}
              </h2>

              {/* Высота строки задана аватаркой: описание помещается в три строки, соцсети прижаты к её низу */}
              <div className="flex items-stretch gap-5">
                <img
                  src={authorPhoto}
                  alt="OpenCore Club"
                  className="w-[160px] h-[160px] flex-shrink-0 rounded-[24px] object-cover border border-border"
                />

                <div className="min-w-0 flex-1 flex flex-col">
                  <p className="text-[21px] font-medium text-foreground">OpenCore Club</p>
                  <p className="mt-1.5 text-[15px] leading-[1.4] text-muted-foreground line-clamp-3">
                    {lang === "ru"
                      ? "Практики Web3 и инвестиций. Объясняем сложное простым языком."
                      : "Web3 and investing practitioners. Complex things in plain words."}
                  </p>

                  <div className="flex items-center gap-2 mt-auto pt-4">
                    {[
                      { Icon: Send, label: "Telegram" },
                      { Icon: Twitter, label: "X" },
                      { Icon: Youtube, label: "YouTube" },
                      { Icon: Instagram, label: "Instagram" },
                    ].map(({ Icon, label }) => (
                      <a
                        key={label}
                        href="#"
                        aria-label={label}
                        className="w-10 h-10 rounded-full border border-border flex items-center justify-center text-foreground active:bg-muted transition-colors"
                      >
                        <Icon className="w-[17px] h-[17px]" strokeWidth={1.8} />
                      </a>
                    ))}
                  </div>
                </div>
              </div>
            </section>

            {/* Больше от автора и похожие курсы — ленты листаются вбок, как на главной */}
            {[
              {
                key: "author",
                titleRu: "Больше от автора",
                titleEn: "More from the author",
                list: otherCourses,
              },
              {
                key: "similar",
                titleRu: "Похожие курсы",
                titleEn: "Similar courses",
                list: similarCourses,
              },
            ].map((rail) =>
              rail.list.length === 0 ? null : (
                <section key={rail.key}>
                  <h2 className="text-[28px] md:text-[32px] font-semibold tracking-tight text-foreground mb-6">
                    {lang === "ru" ? rail.titleRu : rail.titleEn}
                  </h2>
                  <div className="flex gap-4 overflow-x-auto scrollbar-hide snap-x snap-mandatory scroll-pl-4 -mx-4 px-4 lg:mx-0 lg:px-0 lg:scroll-pl-0 pb-1">
                    {rail.list.map((c) => (
                      <div key={c.id} className="flex-shrink-0 snap-start w-[260px] sm:w-[300px]">
                        <CourseCard
                          id={c.id}
                          titleRu={c.titleRu}
                          titleEn={c.titleEn}
                          categoryLabel={getCategoryLabel(c.categoryId, lang)}
                          rating={c.rating}
                          students={c.students}
                          image={c.image}
                          imageBg={c.imageBg}
                          premium={c.premium}
                          price={c.price}
                          isNew={c.isNew}
                          trending={c.trending}
                          updatedDaysAgo={c.updatedDaysAgo}
                          isOwned={
                            store.purchasedCourses.includes(c.id) ||
                            (!!c.premium && !!store.subscription?.active)
                          }
                        />
                      </div>
                    ))}
                  </div>
                </section>
              )
            )}
          </div>

        </div>
      </div>


      {/* Кнопка курса закреплена внизу экрана */}
      <div
        className="fixed inset-x-0 bottom-0 z-40 px-4 pt-3 pb-[max(14px,env(safe-area-inset-bottom))] flex justify-center"
        style={{
          background: "linear-gradient(180deg, hsl(var(--background) / 0) 0%, hsl(var(--background) / 0.92) 32%, hsl(var(--background)) 100%)",
          backdropFilter: "blur(10px)",
          WebkitBackdropFilter: "blur(10px)",
        }}
      >
        {/* Переливающийся бордюр — как у премиума в шапке */}
        <div
          className="w-full max-w-[420px] p-[3px] rounded-[22px] animate-gradient-border"
          style={{
            background: "linear-gradient(270deg, #924CFE, #BF96FF, #D9C0FF, #A66CFF, #924CFE)",
            backgroundSize: "300% 300%",
          }}
        >
          <button
            onClick={startCourse}
            className="w-full h-[56px] rounded-[19px] bg-primary text-primary-foreground text-[19px] font-medium inline-flex items-center justify-center gap-2.5 active:brightness-95 transition-[filter]"
          >
            <PlayRounded className="w-[20px] h-[20px]" />
            {lang === "ru" ? "Начать курс" : "Start course"}
          </button>
        </div>
      </div>
    </div>
  );
};

/** Отзывы курса для страницы «Все отзывы» */
export const getCourseReviews = (id?: string) =>
  (COURSE_CONFIGS[id ?? "9"] ?? COURSE_CONFIGS["9"]).reviews;

export const EXPERIMENTAL_COURSE_IDS = ["1", "2", "6", "7", "8", "9"];

export default CourseExperimental;
