import { useEffect, useState } from "react";
import { BadgeCheck, ArrowRight, Clock, XCircle, ExternalLink } from "lucide-react";
import { toast } from "sonner";
import { useSearchParams } from "react-router-dom";
import { useLanguage } from "@/contexts/LanguageContext";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { StoreBadge } from "@/components/StoreIcons";
import DownloadAppPopover from "@/components/DownloadAppPopover";
import { STORE_LINKS } from "@/lib/storeLinks";
import { useTokenStore, completeAppTask, convertScToOa, resetTokenStore } from "@/hooks/useTokenStore";

type Currency = "SC" | "OA";

/** Сколько SC нужно за 1 $OA */
const SC_PER_OA = 1000;

const OA_BASE_BALANCE = 212484;

/** Дедлайн клейма — 60 дней. Заменить на реальную дату окончания сезона. */
const CLAIM_DEADLINE = new Date("2026-10-23T23:59:59");

/** Тикающий обратный отсчёт до дедлайна */
const useCountdown = (target: Date) => {
  const [now, setNow] = useState(() => Date.now());

  useEffect(() => {
    const id = window.setInterval(() => setNow(Date.now()), 1000);
    return () => window.clearInterval(id);
  }, []);

  const ms = Math.max(0, target.getTime() - now);
  return {
    days: Math.floor(ms / 86400000),
    hours: Math.floor(ms / 3600000) % 24,
    minutes: Math.floor(ms / 60000) % 60,
    seconds: Math.floor(ms / 1000) % 60,
    expired: ms === 0,
  };
};

const pad = (n: number) => String(n).padStart(2, "0");

const SQUIRREL_CLUB_LINK = "https://squirrels.open-academy.app/";

/** Ссылки на мобильное приложение — заменить на реальные */
/* ------------------------------------------------------------------ */
/*  За что начислены SC: критерий → ставка → сколько накоплено         */
/* ------------------------------------------------------------------ */

type Criterion = {
  id: string;
  titleRu: string;
  titleEn: string;
  rateRu: string;
  rateEn: string;
  progressRu: string;
  progressEn: string;
  amount: number;
};

const criteria: Criterion[] = [
  {
    id: "courses",
    titleRu: "Пройденные курсы",
    titleEn: "Completed courses",
    rateRu: "15 000 SC за курс",
    rateEn: "15,000 SC per course",
    progressRu: "14 курсов",
    progressEn: "14 courses",
    amount: 210000,
  },
  {
    id: "lessons",
    titleRu: "Завершённые уроки",
    titleEn: "Completed lessons",
    rateRu: "2 000 SC за урок",
    rateEn: "2,000 SC per lesson",
    progressRu: "186 уроков",
    progressEn: "186 lessons",
    amount: 372000,
  },
  {
    id: "quizzes",
    titleRu: "Квизы без ошибок",
    titleEn: "Perfect quizzes",
    rateRu: "3 500 SC за квиз",
    rateEn: "3,500 SC per quiz",
    progressRu: "92 квиза",
    progressEn: "92 quizzes",
    amount: 322000,
  },
  {
    id: "streak",
    titleRu: "Ежедневная серия",
    titleEn: "Daily streak",
    rateRu: "1 200 SC за день",
    rateEn: "1,200 SC per day",
    progressRu: "56 дней подряд",
    progressEn: "56 days in a row",
    amount: 67200,
  },
  {
    id: "guides",
    titleRu: "Прочитанные инструкции",
    titleEn: "Guides read",
    rateRu: "800 SC за инструкцию",
    rateEn: "800 SC per guide",
    progressRu: "143 инструкции",
    progressEn: "143 guides",
    amount: 114400,
  },
  {
    id: "referrals",
    titleRu: "Реферальные вознаграждения",
    titleEn: "Referral rewards",
    rateRu: "1–3 уровень, ставка зависит от активности друга",
    rateEn: "Levels 1–3, rate depends on the friend's activity",
    progressRu: "412 приглашённых",
    progressEn: "412 invited",
    amount: 1381701,
  },
  {
    id: "penalties",
    titleRu: "Списания за заморозку серии",
    titleEn: "Streak freeze deductions",
    rateRu: "−10 SC за пропущенный день",
    rateEn: "−10 SC per missed day",
    progressRu: "1 день",
    progressEn: "1 day",
    amount: -10,
  },
];

const SC_BALANCE = criteria.reduce((sum, c) => sum + c.amount, 0);

const formatNumber = (value: number) => Math.abs(value).toLocaleString("en-US");
const formatSigned = (value: number) => `${value < 0 ? "−" : ""}${formatNumber(value)}`;

const formatDate = (iso: string) => {
  const [y, m, d] = iso.slice(0, 10).split("-");
  return `${d}/${m}/${y}`;
};

/* ------------------------------------------------------------------ */
/*  Правила награды: баланс SC + награды за конкретные действия         */
/* ------------------------------------------------------------------ */

type Rule = {
  id: string;
  titleRu: string;
  titleEn: string;
  oa: number;
};

const CERTIFICATES = { count: 14, rate: 50 };
const STREAK = { days: 56, rate: 20 };
const REVIEWS = { count: 23, rate: 5 };
const PURCHASES = { spentUsd: 412, usdPerOa: 10 };
const ROYALE_SC = 250;
const ROYALE_MMR = 0;

/** Начисление по каждой номинации. Сумма этих строк = что уходит на баланс. */
const rewardRules: Rule[] = [
  {
    id: "certificates",
    titleRu: "Сертификаты",
    titleEn: "Certificates",
    oa: CERTIFICATES.count * CERTIFICATES.rate,
  },
  {
    id: "sc-balance",
    titleRu: "Баланс SC",
    titleEn: "SC balance",
    oa: Math.floor(SC_BALANCE / SC_PER_OA),
  },
  {
    id: "streak",
    titleRu: "Стрик",
    titleEn: "Streak",
    oa: STREAK.days * STREAK.rate,
  },
  {
    id: "reviews",
    titleRu: "Отзывы",
    titleEn: "Reviews",
    oa: REVIEWS.count * REVIEWS.rate,
  },
  {
    id: "purchases",
    titleRu: "Оплата курсов, VIP и подписки",
    titleEn: "Course, VIP and subscription purchases",
    oa: Math.floor(PURCHASES.spentUsd / PURCHASES.usdPerOa),
  },
  {
    id: "royale-sc",
    titleRu: "Рояль: SC",
    titleEn: "Royale: SC",
    oa: ROYALE_SC,
  },
  {
    id: "royale-mmr",
    titleRu: "Рояль: MMR",
    titleEn: "Royale: MMR",
    oa: ROYALE_MMR,
  },
];

/** Отсортировано по убыванию — как в сводке по сезону */
const sortedRewardRules = [...rewardRules].sort((a, b) => b.oa - a.oa);
const TOTAL_REWARD_OA = rewardRules.reduce((sum, r) => sum + r.oa, 0);

/* ------------------------------------------------------------------ */
/*  Условия допуска к награде                                           */
/* ------------------------------------------------------------------ */

/** Минимальный баланс SC для допуска */
const MIN_SC_FOR_REWARD = 1000;

/** Подробная статья об итогах сезона и условиях допуска */
const ARTICLE_LINK = "https://learn.open-academy.app/guides/ru/guide/itogi-vtorogo-sezona-open-academy";

/** Дата снимка, на которую проверяются условия */
const SNAPSHOT_DATE = { ru: "17 августа 2026", en: "17 August 2026" };

const eligibilityRules: { id: string; ru: string; en: string }[] = [
  {
    id: "two-certs",
    ru: "Получить 2 сертификата или больше",
    en: "Earn 2 certificates or more",
  },
  {
    id: "one-cert-plus",
    ru: `Получить 1 сертификат и что-то ещё: написать отзыв, поиграть в Рояль, поднять рейтинг, иметь активный стрик на момент снимка (${SNAPSHOT_DATE.ru}) или набрать от 10 000 SC`,
    en: `Earn 1 certificate and something else: write a review, play Royale, raise your rating, have an active streak at the snapshot (${SNAPSHOT_DATE.en}) or collect 10,000 SC`,
  },
  {
    id: "sc-50k",
    ru: "Набрать от 50 000 SC",
    en: "Collect 50,000 SC or more",
  },
  {
    id: "purchase",
    ru: "Купить курс, VIP или подписку",
    en: "Buy a course, VIP or a subscription",
  },
];

/* ------------------------------------------------------------------ */
/*  FAQ по токену                                                      */
/* ------------------------------------------------------------------ */

const faq: { id: string; qRu: string; qEn: string; aRu: string; aEn: string }[] = [
  {
    id: "sc",
    qRu: "Что такое SC?",
    qEn: "What is SC?",
    aRu: "Внутренние баллы за обучение и активность — старая система второго сезона Open Academy. Сейчас их нельзя заработать: баланс SC один раз учитывается в награде второго сезона, если вы проходите по условиям.",
    aEn: "Internal points for learning and activity — the legacy system from Open Academy season two. They can no longer be earned: your SC balance is counted once in the Season 2 Reward, if you meet the conditions.",
  },
  {
    id: "oa",
    qRu: "Что такое $OA?",
    qEn: "What is $OA?",
    aRu: "Комьюнити-токен проекта Open Academy. Он ещё не залистен. Токен получит свои ютилити внутри проекта, а сейчас начисляется за крупные достижения и за вклад в развитие платформы.",
    aEn: "The Open Academy community token. It is not listed yet. The token will get its own utilities inside the project; for now it is credited for major achievements and for contributing to the platform.",
  },
  {
    id: "emission",
    qRu: "Какая эмиссия у $OA?",
    qEn: "What is the $OA supply?",
    aRu: "Общая эмиссия — 1 000 000 000 $OA (1 миллиард). Это фиксированный объём, дополнительной эмиссии не будет.",
    aEn: "The total supply is 1,000,000,000 $OA (1 billion). The amount is fixed — there will be no additional emission.",
  },
  {
    id: "deadline",
    qRu: "Сколько времени есть на клейм?",
    qEn: "How long do I have to claim?",
    aRu: "На получение награды даётся 60 дней. Если не успеть до конца отсчёта, награда сгорает — забрать её позже будет нельзя.",
    aEn: "You have 60 days to claim the reward. If you miss the deadline, the reward burns and cannot be claimed later.",
  },
  {
    id: "more",
    qRu: "Как получить больше $OA?",
    qEn: "How do I get more $OA?",
    aRu: "Сейчас основная раздача идёт в The Early Squirrels Club — за помощь в развитии платформы.",
    aEn: "Right now the main distribution runs in The Early Squirrels Club — for helping to grow the platform.",
  },
];

/* ------------------------------------------------------------------ */
/*  История начислений                                                 */
/* ------------------------------------------------------------------ */

type Entry = {
  id: string;
  titleRu: string;
  titleEn: string;
  amount: number;
  currency: Currency;
  date: string; // ISO
};

const entries: Entry[] = [
  { id: "1", titleRu: "Заморозка серии за 1 пропущенных дней", titleEn: "Streak freeze for 1 missed day", amount: -10, currency: "SC", date: "2026-08-20" },
  { id: "2", titleRu: "Реферальное вознаграждение 3 уровня от пользователя Cergcant", titleEn: "Level 3 referral reward from Cergcant", amount: 1, currency: "SC", date: "2026-08-17" },
  { id: "3", titleRu: "Реферальное вознаграждение 1 уровня от пользователя stillnef", titleEn: "Level 1 referral reward from stillnef", amount: 84, currency: "SC", date: "2026-08-17" },
  { id: "4", titleRu: "Реферальное вознаграждение 1 уровня от пользователя stillnef", titleEn: "Level 1 referral reward from stillnef", amount: 77, currency: "SC", date: "2026-08-17" },
  { id: "5", titleRu: "Реферальное вознаграждение 1 уровня от пользователя stillnef", titleEn: "Level 1 referral reward from stillnef", amount: 70, currency: "SC", date: "2026-08-17" },
  { id: "6", titleRu: "Реферальное вознаграждение 1 уровня от пользователя stillnef", titleEn: "Level 1 referral reward from stillnef", amount: 63, currency: "SC", date: "2026-08-17" },
  { id: "7", titleRu: "Реферальное вознаграждение 1 уровня от пользователя stillnef", titleEn: "Level 1 referral reward from stillnef", amount: 56, currency: "SC", date: "2026-08-17" },
  { id: "8", titleRu: "Награда за прохождение курса «Быстрый старт в Telegram Gifts»", titleEn: "Reward for completing “Quick Start with Telegram Gifts”", amount: 15000, currency: "SC", date: "2026-08-16" },
  { id: "9", titleRu: "Награда за урок «Как устроен вторичный рынок»", titleEn: "Reward for the lesson “How the secondary market works”", amount: 2000, currency: "SC", date: "2026-08-16" },
  { id: "10", titleRu: "Бонус за серию 50 дней", titleEn: "50-day streak bonus", amount: 1200, currency: "SC", date: "2026-08-14" },
  { id: "11", titleRu: "Квиз без ошибок «Основы Web3»", titleEn: "Perfect quiz “Web3 Basics”", amount: 3500, currency: "SC", date: "2026-08-12" },
  { id: "12", titleRu: "Прочитана инструкция «Как завести кошелёк»", titleEn: "Guide read “How to set up a wallet”", amount: 800, currency: "SC", date: "2026-08-11" },
];

/* ------------------------------------------------------------------ */

const BalanceCard = ({
  currency,
  amount,
  label,
  className = "",
  check,
}: {
  currency: Currency;
  amount: number;
  label: string;
  className?: string;
  /** не задан — галочки нет; false — серая неактивная; true — зелёная */
  check?: boolean;
}) => {
  const isSc = currency === "SC";
  const accent = isSc ? "#F65C39" : "#924CFE";

  return (
    <div
      className={`rounded-2xl flex flex-col justify-between md:justify-end p-4 md:p-7 min-h-[112px] md:min-h-[205px] ${className}`}
      style={{
        background: isSc
          ? "linear-gradient(105deg, #FFF4EE 0%, #FFDECD 48%, #FF7A4E 88%, #F65C39 100%)"
          : "linear-gradient(105deg, #F6F0FF 0%, #E2D2FF 48%, #A97BFF 88%, #924CFE 100%)",
      }}
    >
      {/* Мобильная версия: кружок токена сверху */}
      <span
        className="md:hidden w-9 h-9 rounded-full flex items-center justify-center text-[17px] font-medium text-white"
        style={{
          background: isSc
            ? "linear-gradient(135deg, #FF8E70, #FF6545)"
            : "linear-gradient(135deg, #B88AFF, #9A5CFF)",
        }}
      >
        {isSc ? "S" : "A"}
      </span>

      {/* Десктоп: подпись внутри карточки */}
      <p className="hidden md:block text-[16px] font-normal leading-none mb-3" style={{ color: accent }}>
        {label}
      </p>

      <p className="text-[20px] md:text-[30px] font-medium leading-none flex items-center gap-2 md:gap-2.5 mt-3 md:mt-0">
        <span className="hidden md:inline" style={{ color: accent }}>
          {isSc ? "SC" : "$OA"}
        </span>
        <span style={{ color: "#232323" }}>{formatNumber(amount)}</span>
        <span className="md:hidden" style={{ color: accent }}>
          {isSc ? "SC" : "$OA"}
        </span>
        {check !== undefined && (
          <BadgeCheck
            className="w-[20px] h-[20px] md:w-[24px] md:h-[24px] flex-shrink-0"
            strokeWidth={2}
            style={{ color: check ? "hsl(var(--success))" : "rgba(35, 35, 35, 0.25)" }}
          />
        )}
      </p>
    </div>
  );
};

const MyToken = () => {
  const { lang } = useLanguage();
  const ru = lang === "ru";
  const store = useTokenStore();
  const [confirmOpen, setConfirmOpen] = useState(false);
  const left = useCountdown(CLAIM_DEADLINE);

  // Демо-переключатель состояния: /token?eligible=0 — не прошёл по условиям
  const [searchParams, setSearchParams] = useSearchParams();
  const eligible = searchParams.get("eligible") !== "0";

  // Срок вышел: SC и весь блок награды исчезают навсегда
  const expired = left.expired || searchParams.get("expired") === "1";

  // Что уже неактуально: награда забрана или сгорела
  const rewardOver = store.converted || expired;

  const oaFromConversion = TOTAL_REWARD_OA;
  const oaBalance = store.converted ? OA_BASE_BALANCE + store.receivedOa : OA_BASE_BALANCE;

  // Задание: установить приложение и авторизоваться
  // Молча отмечаем переход в стор — никаких проверок и уведомлений
  const handleInstall = () => completeAppTask();

  const handleConvert = () => {
    convertScToOa(SC_BALANCE, oaFromConversion);
    setConfirmOpen(false);
    toast.success(
      ru
        ? `Начислено ${formatNumber(oaFromConversion)} $OA`
        : `${formatNumber(oaFromConversion)} $OA credited`
    );
  };

  // Виджет клуба: на мобильных — под промо приложения, на десктопе — в правой колонке
  const clubWidget = (
        <div
        className="rounded-2xl p-5 md:p-6"
        style={{ background: "linear-gradient(140deg, #F6F0FF 0%, #E4D5FF 55%, #C9AEFF 100%)" }}
      >
        <div className="flex items-center gap-3 mb-3">
          <img src="/squirrel-club.svg" alt="" className="w-12 h-12 object-contain flex-shrink-0" />
          <p className="text-[18px] font-medium leading-none" style={{ color: "#5B21B6" }}>
            The Early Squirrels Club
          </p>
        </div>
        <p className="text-[15px] leading-snug" style={{ color: "#3B2A5A" }}>
          {ru
            ? "Сейчас $OA раздаются в The Early Squirrels Club — тем, кто помогает развивать платформу: тестирует новое, пишет инструкции, приводит и обучает новичков."
            : "Right now $OA is distributed in The Early Squirrels Club — to those who help grow the platform: testing new features, writing guides, bringing in and mentoring newcomers."}
        </p>
        <a
          href={SQUIRREL_CLUB_LINK}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-4 inline-flex items-center gap-2 h-11 px-5 rounded-[10px] bg-primary text-primary-foreground text-[15px] font-medium hover:brightness-110 transition-all"
        >
          {ru ? "Вступить в клуб" : "Join the club"}
          <ArrowRight className="w-4 h-4" />
        </a>
      </div>
  );

  const historyEntries: Entry[] = store.converted
    ? [
        {
          id: "conversion",
          titleRu: `Награда второго сезона · ${formatNumber(store.burnedSc)} SC списаны`,
          titleEn: `Season 2 Reward · ${formatNumber(store.burnedSc)} SC burned`,
          amount: store.receivedOa,
          currency: "OA",
          date: store.convertedAt ?? new Date().toISOString(),
        },
        ...entries,
      ]
    : entries;

  return (
    <div className="w-full px-4 md:px-9 py-6 md:py-10">
      <div className="max-w-[1400px]">
        {/* Заголовок */}
        <h1 className="text-[24px] md:text-[28px] font-medium leading-none text-foreground mb-5">
          {ru ? "Мой токен" : "My Token"}
        </h1>

        <div className="flex flex-col lg:flex-row gap-5 lg:gap-6 items-start">
          {/* Левая колонка */}
          <div className="flex-1 min-w-0 w-full max-w-[1024px]">

        {/* Балансы */}
        <p className="md:hidden text-[16px] text-muted-foreground mb-3">
          {ru ? "Текущий баланс" : "Current balance"}
        </p>
        <div className="grid grid-cols-2 gap-3 md:gap-5 mb-6">
          {!rewardOver && (
            <BalanceCard currency="SC" amount={SC_BALANCE} label={ru ? "Текущий баланс" : "Current balance"} />
          )}
          <BalanceCard
            currency="OA"
            amount={oaBalance}
            label={ru ? "Текущий баланс" : "Current balance"}
            check={store.appTaskDone}
            className={rewardOver ? "col-span-2" : ""}
          />
        </div>

        {/* Награда второго сезона. Пропадает после получения и после дедлайна. */}
        {!rewardOver && (
          <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6 mb-6">
            <h2 className="text-[20px] md:text-[22px] font-medium leading-none text-foreground">
              {ru ? "Награда второго сезона" : "Season 2 Reward"}
            </h2>
            {eligible ? (
              <>
                <div className="mt-4 flex flex-wrap items-center gap-x-2.5 gap-y-1">
                  <span className="flex items-center gap-2 flex-shrink-0" style={{ color: "#F65C39" }}>
                    <Clock className="w-[18px] h-[18px]" />
                    <span className="text-[16px] md:text-[18px] font-medium tabular-nums">
                      {left.expired
                        ? ru ? "Время вышло" : "Time is up"
                        : `${left.days} ${ru ? "дн" : "d"} ${pad(left.hours)}:${pad(left.minutes)}:${pad(left.seconds)}`}
                    </span>
                  </span>
                  <span className="text-muted-foreground/50">|</span>
                  <span className="text-[14px] md:text-[15px] text-muted-foreground">
                    {ru ? "Успей забрать награду" : "Claim your reward in time"}
                  </span>
                </div>

                <button
                  type="button"
                  onClick={() => setConfirmOpen(true)}
                  disabled={left.expired}
                  className="mt-5 w-full flex items-center justify-center gap-2 h-12 px-6 rounded-[10px] text-[16px] font-medium whitespace-nowrap transition-all bg-primary text-primary-foreground hover:brightness-110 disabled:bg-muted-foreground/20 disabled:text-muted-foreground disabled:cursor-not-allowed disabled:hover:brightness-100"
                >
                  {ru ? "Забрать" : "Claim"} {formatNumber(oaFromConversion)} $OA
                </button>
              </>
            ) : (
              <>
                <p className="mt-4 text-[16px] md:text-[18px] font-medium text-muted-foreground">
                  {ru ? "Награда недоступна" : "Reward unavailable"}
                </p>
                <p className="text-[14px] md:text-[15px] text-muted-foreground mt-1">
                  {ru
                    ? `Нужно выполнить любое одно условие из списка и иметь на балансе не меньше ${formatNumber(MIN_SC_FOR_REWARD)} SC`
                    : `You need any one condition from the list and at least ${formatNumber(MIN_SC_FOR_REWARD)} SC on the balance`}
                </p>

                <div className="mt-4 rounded-xl bg-background border border-border divide-y divide-border">
                  {eligibilityRules.map((rule) => (
                    <div key={rule.id} className="flex items-start gap-3 px-4 py-3.5">
                      <XCircle
                        className="w-5 h-5 flex-shrink-0 mt-0.5 text-muted-foreground/45"
                        strokeWidth={2}
                      />
                      <p className="text-[15px] md:text-[16px] text-muted-foreground leading-snug">
                        {ru ? rule.ru : rule.en}
                      </p>
                    </div>
                  ))}
                </div>
              </>
            )}


            <a
              href={ARTICLE_LINK || "#"}
              target={ARTICLE_LINK ? "_blank" : undefined}
              rel={ARTICLE_LINK ? "noopener noreferrer" : undefined}
              onClick={(e) => {
                if (!ARTICLE_LINK) e.preventDefault();
              }}
              className="mt-4 inline-flex items-center gap-2 h-11 px-5 rounded-[10px] border border-border bg-background text-foreground text-[15px] font-medium hover:bg-muted transition-colors"
            >
              {ru ? "Подробнее об условиях" : "More about the conditions"}
              <ExternalLink className="w-4 h-4" />
            </a>
          </section>
        )}

        {/* Промо приложения — отдельный блок, с наградой не связан.
            После установки скрывается. */}
        {!store.appTaskDone && (
        <section className="relative overflow-hidden rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6 mb-6">
          {/* Большой знак верификации по центру блока */}
          <BadgeCheck
            className="pointer-events-none absolute top-0 left-[38%] -translate-x-1/2 h-[165%] w-auto"
            strokeWidth={1.1}
            style={{ color: "hsl(var(--muted-foreground) / 0.15)" }}
            aria-hidden="true"
          />

          <div className="relative flex flex-wrap items-center gap-x-4 gap-y-3">
            <p className="flex-1 min-w-[220px] text-[16px] md:text-[18px] text-foreground leading-snug">
              {ru
                ? "Скачивай наше мобильное приложение"
                : "Get our mobile app"}
            </p>

            {/* Мобильные — сразу в стор, QR там не нужен */}
            <div className="md:hidden grid grid-cols-2 gap-2 w-full">
              <StoreBadge
                store="appStore"
                href={STORE_LINKS.appStore}
                onClick={handleInstall}
                className="w-full min-w-0"
              />
              <StoreBadge
                store="googlePlay"
                href={STORE_LINKS.googlePlay}
                onClick={handleInstall}
                className="w-full min-w-0"
              />
            </div>

            {/* Десктоп — поповер с QR */}
            <div className="hidden md:flex items-center gap-2 flex-shrink-0">
              <DownloadAppPopover store="appStore" onStoreClick={handleInstall}>
                <StoreBadge store="appStore" />
              </DownloadAppPopover>
              <DownloadAppPopover store="googlePlay" onStoreClick={handleInstall}>
                <StoreBadge store="googlePlay" />
              </DownloadAppPopover>
            </div>
          </div>
        </section>
        )}

        {/* Клуб: на мобильных под призывом скачать приложение */}
        <div className="md:hidden mb-6">{clubWidget}</div>

        {/* История начислений */}
        <section className="rounded-2xl bg-muted overflow-hidden">
          <h2 className="text-[20px] md:text-[22px] font-medium leading-none text-foreground px-5 md:px-6 py-5 md:py-6">
            {ru ? "История начислений" : "Rewards history"}
          </h2>

          <div className="bg-background rounded-t-2xl border-x border-b border-border divide-y divide-border">
            {historyEntries.map((entry) => (
              <div key={entry.id} className="flex items-start justify-between gap-4 px-5 md:px-6 py-4 md:py-5">
                <div className="min-w-0">
                  <p className="text-[16px] md:text-[18px] font-normal text-foreground leading-snug">
                    {ru ? entry.titleRu : entry.titleEn}
                  </p>
                  <p className="text-[14px] md:text-[15px] text-muted-foreground mt-1.5">
                    {formatDate(entry.date)}
                  </p>
                </div>
                <p className="text-[16px] md:text-[18px] font-medium text-foreground whitespace-nowrap flex-shrink-0">
                  {formatSigned(entry.amount)}{" "}
                  <span className="font-normal text-muted-foreground">
                    {entry.currency === "OA" ? "$OA" : "SC"}
                  </span>
                </p>
              </div>
            ))}
          </div>
        </section>


        {/* ---------------------------------------------------------------- */}
        {/*  Демо-панель: только для показа состояний, в прод не идёт         */}
        {/* ---------------------------------------------------------------- */}
        <section className="rounded-2xl border-2 border-dashed border-border p-5 md:p-6 mt-10">
          <p className="text-[13px] font-medium uppercase tracking-[0.06em] text-muted-foreground">
            {ru ? "Демо · состояния экрана" : "Demo · screen states"}
          </p>

          <div className="flex flex-wrap gap-2 mt-4">
            {[
              {
                label: ru ? "Награда доступна" : "Reward available",
                onClick: () => {
                  resetTokenStore();
                  setSearchParams({});
                },
              },
              {
                label: ru ? "Не прошёл по условиям" : "Not eligible",
                onClick: () => {
                  resetTokenStore();
                  setSearchParams({ eligible: "0" });
                },
              },
              {
                label: ru ? "Приложение установлено" : "App installed",
                onClick: () => {
                  setSearchParams({});
                  completeAppTask();
                },
              },
              {
                label: ru ? "Награда получена" : "Reward claimed",
                onClick: () => {
                  setSearchParams({});
                  convertScToOa(SC_BALANCE, TOTAL_REWARD_OA);
                },
              },
              {
                label: ru ? "Срок вышел (60 дней)" : "Deadline passed",
                onClick: () => {
                  resetTokenStore();
                  setSearchParams({ expired: "1" });
                },
              },
            ].map((b) => (
              <button
                key={b.label}
                type="button"
                onClick={b.onClick}
                className="h-10 px-4 rounded-[10px] border border-border bg-background text-[15px] text-foreground hover:bg-muted transition-colors"
              >
                {b.label}
              </button>
            ))}
          </div>

          <h3 className="text-[17px] md:text-[18px] font-medium text-foreground mt-7">
            {ru ? "Как это должно работать" : "How it should work"}
          </h3>

          <ol className="mt-3 flex flex-col gap-2.5 text-[15px] md:text-[16px] text-foreground leading-snug list-decimal pl-5">
            {(ru
              ? [
                  "Пока идёт отсчёт, человек видит две карточки баланса — SC и $OA — и блок награды с таймером.",
                  "Награду можно забрать сразу. Кнопка активна всегда, никаких заданий для неё выполнять не нужно.",
                  "Если человек не проходит по условиям сезона, вместо таймера и кнопки показывается «Награда недоступна» и список условий с крестиками. Забрать нельзя.",
                  "Блок «Скачивай наше мобильное приложение» — просто реклама, к награде отношения не имеет. После перехода в магазин мы проверяем, установил человек приложение или нет. Если установил — блок пропадает и рядом с балансом $OA появляется зелёная галочка.",
                  "Значок рядом с балансом $OA виден всегда: серый — приложение не установлено, зелёный — установлено. Подписи к нему нигде нет и быть не должно.",
                  "Когда человек забирает награду: карточка SC исчезает, остаётся только $OA с увеличенным балансом, а в истории появляется строка о начислении.",
                  "Через 60 дней отсчёт заканчивается. Карточка SC и весь блок награды исчезают навсегда — даже если человек ничего не забрал. Награда сгорает, вернуть её нельзя.",
                  "Что остаётся на экране всегда: баланс $OA, история начислений, FAQ и блок клуба белок.",
                  "На телефоне подвала нет, окно с правилами выезжает снизу, а кнопки магазинов ведут сразу в App Store или Google Play — без QR-кода.",
                ]
              : [
                  "While the countdown runs, the user sees two balance cards — SC and $OA — and the reward block with a timer.",
                  "The reward can be claimed right away. The button is always active and requires no tasks.",
                  "If the user does not meet the season conditions, the timer and button are replaced by “Reward unavailable” and the list of conditions with crosses. Claiming is not possible.",
                  "The “Get our mobile app” block is pure promotion and has nothing to do with the reward. After the user goes to the store we check whether the app was installed. If it was — the block disappears and a green check appears next to the $OA balance.",
                  "The mark next to the $OA balance is always visible: grey means the app is not installed, green means it is. It must stay unlabelled everywhere.",
                  "When the user claims: the SC card disappears, only $OA remains with the increased balance, and a line about the credit appears in the history.",
                  "After 60 days the countdown ends. The SC card and the whole reward block disappear for good — even if nothing was claimed. The reward burns and cannot be restored.",
                  "What always stays on screen: the $OA balance, the rewards history, the FAQ and the squirrel club block.",
                  "On phones there is no footer, the rules window slides up from the bottom, and the store buttons go straight to the App Store or Google Play — no QR code.",
                ]
            ).map((line) => (
              <li key={line}>{line}</li>
            ))}
          </ol>
        </section>

          </div>

          {/* Правая колонка: клуб белок + FAQ */}
          <aside className="w-full lg:w-[340px] flex-shrink-0 flex flex-col gap-5 lg:sticky lg:top-2">
            {/* Клуб: на десктопе в правой колонке */}
            <div className="hidden md:block">{clubWidget}</div>

            {/* FAQ */}
            <div className="rounded-2xl bg-muted p-5 md:p-6">
              <h2 className="text-[18px] md:text-[20px] font-medium leading-none text-foreground mb-2">
                {ru ? "FAQ по токену" : "Token FAQ"}
              </h2>
              <Accordion type="single" collapsible className="w-full">
                {faq.map((item) => (
                  <AccordionItem key={item.id} value={item.id} className="border-border">
                    <AccordionTrigger className="text-[15px] font-normal text-foreground text-left hover:no-underline">
                      {ru ? item.qRu : item.qEn}
                    </AccordionTrigger>
                    <AccordionContent className="text-[15px] text-muted-foreground leading-snug">
                      {ru ? item.aRu : item.aEn}
                    </AccordionContent>
                  </AccordionItem>
                ))}
              </Accordion>
            </div>
          </aside>
        </div>
      </div>

      {/* Правила награды */}
      <AlertDialog open={confirmOpen} onOpenChange={setConfirmOpen}>
        <AlertDialogContent className="max-w-[560px]">
          <AlertDialogHeader>
            <AlertDialogTitle>
              {ru ? "Правила награды второго сезона" : "Season 2 Reward rules"}
            </AlertDialogTitle>
          </AlertDialogHeader>

          <div>
            {sortedRewardRules.map((rule) => (
              <div
                key={rule.id}
                className="flex items-center justify-between gap-4 py-4 border-b border-border"
              >
                <p
                  className={`text-[17px] md:text-[18px] font-medium leading-snug ${
                    rule.oa === 0 ? "text-muted-foreground/60" : "text-foreground"
                  }`}
                >
                  {ru ? rule.titleRu : rule.titleEn}
                </p>
                <p
                  className={`text-[17px] md:text-[18px] whitespace-nowrap flex-shrink-0 tabular-nums ${
                    rule.oa === 0 ? "text-muted-foreground/60" : "text-muted-foreground"
                  }`}
                >
                  {formatNumber(rule.oa)} $OA
                </p>
              </div>
            ))}

            <div className="flex items-center justify-between gap-4 py-4">
              <p className="text-[18px] md:text-[19px] font-medium text-foreground">
                {ru ? "К начислению" : "Total credited"}
              </p>
              <p className="text-[18px] md:text-[19px] font-medium whitespace-nowrap tabular-nums" style={{ color: "#924CFE" }}>
                {formatNumber(oaFromConversion)} $OA
              </p>
            </div>
          </div>

          <AlertDialogFooter>
            <AlertDialogCancel className="hover:bg-muted hover:text-foreground">
              {ru ? "Отмена" : "Cancel"}
            </AlertDialogCancel>
            <AlertDialogAction onClick={handleConvert}>
              {ru ? "Забрать $OA" : "Claim $OA"}
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};

export default MyToken;
