import { Lock, Smartphone, Check, ArrowRight, Gift } from "lucide-react";
import { AppleIcon, GooglePlayIcon } from "@/components/StoreIcons";

/* Текст во всех вариантах одинаковый */
const T = {
  title: "Airdrop 2 сезона",
  task: "Установи мобильное приложение Open Academy и авторизуйся в нём",
  sub: "Обязательное условие для получения аирдропа",
  cta: "Забрать 3,399 $OA",
  hint: "Выполни задание выше, чтобы разблокировать кнопку",
};

/* --- общие кусочки ------------------------------------------------- */

const Stores = ({
  outline = false,
  size = "md",
  onDark = false,
}: {
  outline?: boolean;
  size?: "sm" | "md";
  onDark?: boolean;
}) => {
  const h = size === "sm" ? "h-10 px-3.5 text-[14px]" : "h-11 px-4 text-[15px]";
  const cls = onDark
    ? `flex items-center gap-2 ${h} rounded-[10px] bg-white text-[#232323] font-medium whitespace-nowrap hover:opacity-90 transition-opacity`
    : outline
      ? `flex items-center gap-2 ${h} rounded-[10px] border border-border bg-background text-foreground font-medium whitespace-nowrap hover:bg-muted transition-colors`
      : `flex items-center gap-2 ${h} rounded-[10px] bg-foreground text-background font-medium whitespace-nowrap hover:opacity-90 transition-opacity`;
  return (
    <div className="flex items-center gap-2 flex-shrink-0">
      <a href="#" className={cls}>
        <AppleIcon className="w-[18px] h-[18px]" />
        App Store
      </a>
      <a href="#" className={cls}>
        <GooglePlayIcon className="w-[18px] h-[18px]" />
        Google Play
      </a>
    </div>
  );
};

const Cta = ({ full = false, onDark = false }: { full?: boolean; onDark?: boolean }) => (
  <button
    type="button"
    disabled
    className={`flex items-center justify-center gap-2 h-12 px-6 rounded-[10px] text-[16px] font-medium whitespace-nowrap cursor-not-allowed ${
      onDark ? "bg-white/25 text-white/70" : "bg-muted-foreground/20 text-muted-foreground"
    } ${full ? "w-full" : "flex-shrink-0"}`}
  >
    <Lock className="w-4 h-4" />
    {T.cta}
  </button>
);

const Hint = ({ onDark = false }: { onDark?: boolean }) => (
  <p
    className={`text-[14px] md:text-[15px] flex-1 min-w-[180px] ${
      onDark ? "text-white/70" : "text-muted-foreground"
    }`}
  >
    {T.hint}
  </p>
);

const TaskText = ({ compact = false, onDark = false }: { compact?: boolean; onDark?: boolean }) => (
  <div className="flex-1 min-w-[220px]">
    <p
      className={`${compact ? "text-[16px]" : "text-[16px] md:text-[18px]"} leading-snug ${
        onDark ? "text-white" : "text-foreground"
      }`}
    >
      {T.task}
    </p>
    <p className={`text-[14px] md:text-[15px] mt-1 ${onDark ? "text-white/70" : "text-muted-foreground"}`}>
      {T.sub}
    </p>
  </div>
);

const PhoneIcon = ({ tone = "primary" }: { tone?: "primary" | "muted" | "onDark" }) => (
  <div
    className={`w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0 ${
      tone === "primary" ? "bg-primary/10" : tone === "onDark" ? "bg-white/20" : "bg-muted"
    }`}
  >
    <Smartphone
      className={`w-5 h-5 ${
        tone === "primary" ? "text-primary" : tone === "onDark" ? "text-white" : "text-muted-foreground"
      }`}
    />
  </div>
);

const Title = ({ className = "", onDark = false }: { className?: string; onDark?: boolean }) => (
  <h2
    className={`text-[20px] md:text-[22px] font-medium leading-none ${
      onDark ? "text-white" : "text-foreground"
    } ${className}`}
  >
    {T.title}
  </h2>
);

/* --- 20 вариантов --------------------------------------------------- */

const V1 = () => (
  <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 rounded-xl bg-background p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V2 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 rounded-xl bg-muted p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V3 = () => (
  <section className="rounded-2xl bg-background border border-primary/40 px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 pt-5 border-t border-border flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V4 = () => (
  <section className="rounded-2xl bg-background border border-border border-l-4 border-l-primary px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V5 = () => (
  <section className="rounded-2xl bg-muted overflow-hidden">
    <div className="px-5 md:px-6 py-5 md:py-6">
      <Title />
    </div>
    <div className="bg-background rounded-t-2xl border-x border-b border-border px-5 md:px-6 py-5 md:py-6">
      <div className="flex flex-wrap items-center gap-x-4 gap-y-3">
        <PhoneIcon />
        <TaskText />
        <Stores />
      </div>
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </div>
  </section>
);

const V6 = () => (
  <section className="rounded-2xl bg-background border border-border overflow-hidden">
    <div className="h-1 w-full bg-primary" />
    <div className="px-5 md:px-6 py-5 md:py-6">
      <Title />
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <PhoneIcon />
        <TaskText />
        <Stores />
      </div>
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </div>
  </section>
);

const V7 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <div className="flex items-center justify-between gap-4 flex-wrap">
      <Title />
      <span className="text-[20px] md:text-[22px] font-medium text-primary">3,399 $OA</span>
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V8 = () => (
  <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 pt-5 border-t border-border">
      <Cta full />
    </div>
  </section>
);

const V9 = () => (
  <section className="rounded-2xl bg-background border border-border p-5 md:p-6 flex flex-col lg:flex-row gap-5 lg:gap-8">
    <div className="lg:w-[240px] flex-shrink-0">
      <Title />
      <p className="text-[14px] md:text-[15px] text-muted-foreground mt-2">{T.hint}</p>
      <div className="mt-4">
        <Cta full />
      </div>
    </div>
    <div className="flex-1 rounded-xl bg-muted p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores size="sm" />
    </div>
  </section>
);

const V10 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-start gap-x-4 gap-y-3">
      <span className="w-7 h-7 rounded-full bg-primary/10 text-primary text-[14px] font-medium flex items-center justify-center flex-shrink-0">
        1
      </span>
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-start gap-x-4 gap-y-3">
      <span className="w-7 h-7 rounded-full bg-muted text-muted-foreground text-[14px] font-medium flex items-center justify-center flex-shrink-0">
        2
      </span>
      <div className="flex-1 min-w-[220px] flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </div>
  </section>
);

const V11 = () => (
  <section className="rounded-2xl bg-primary/5 border border-primary/20 px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 rounded-xl bg-background p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V12 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <div className="flex items-center gap-3">
      <Gift className="w-5 h-5 text-primary flex-shrink-0" />
      <Title />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <TaskText />
      <Stores outline />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V13 = () => (
  <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon tone="muted" />
      <TaskText />
      <Stores outline />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V14 = () => (
  <section className="rounded-2xl bg-background border border-border divide-y divide-border">
    <div className="px-5 md:px-6 py-4 md:py-5">
      <Title />
    </div>
    <div className="px-5 md:px-6 py-4 md:py-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <TaskText />
      <Stores />
    </div>
    <div className="px-5 md:px-6 py-4 md:py-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V15 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <span className="w-6 h-6 rounded-full border-2 border-border flex items-center justify-center flex-shrink-0">
        <Check className="w-3.5 h-3.5 text-muted-foreground/40" />
      </span>
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V16 = () => (
  <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6">
    <div className="flex flex-wrap items-center justify-between gap-4">
      <Title />
      <Stores size="sm" />
    </div>
    <p className="text-[16px] md:text-[18px] text-foreground leading-snug mt-4">{T.task}</p>
    <p className="text-[14px] md:text-[15px] text-muted-foreground mt-1">{T.sub}</p>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V17 = () => (
  <section className="rounded-2xl bg-background border border-border p-5 md:p-6">
    <div className="flex flex-col lg:flex-row lg:items-center gap-5">
      <div className="flex-1 min-w-0">
        <Title className="mb-3" />
        <div className="flex flex-wrap items-center gap-x-4 gap-y-3">
          <PhoneIcon />
          <TaskText />
        </div>
      </div>
      <div className="flex flex-col gap-3 lg:w-[240px] flex-shrink-0">
        <Stores size="sm" />
        <Cta full />
      </div>
    </div>
  </section>
);

const V18 = () => (
  <section className="rounded-2xl bg-muted overflow-hidden">
    <div className="px-5 md:px-6 py-4 md:py-5 flex flex-wrap items-center justify-between gap-3">
      <Title />
      <span className="text-[14px] text-muted-foreground">{T.hint}</span>
    </div>
    <div className="bg-background border-t border-border px-5 md:px-6 py-5 md:py-6 flex flex-wrap items-center gap-x-4 gap-y-3">
      <TaskText />
      <Stores />
      <Cta />
    </div>
  </section>
);

const V19 = () => (
  <section className="rounded-2xl bg-background border border-border px-5 md:px-6 py-5 md:py-6">
    <Title />
    <div className="mt-5 rounded-xl border border-border p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V20 = () => (
  <section className="rounded-2xl bg-muted px-5 md:px-6 py-5 md:py-6">
    <div className="flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <div className="flex-1 min-w-[220px]">
        <Title className="mb-1.5" />
        <p className="text-[16px] text-foreground leading-snug">{T.task}</p>
        <p className="text-[14px] md:text-[15px] text-muted-foreground mt-1">{T.sub}</p>
      </div>
      <div className="flex flex-col items-stretch gap-3 flex-shrink-0">
        <Stores size="sm" />
        <Cta full />
      </div>
    </div>
  </section>
);


/* --- градиентные варианты ------------------------------------------- */

const G = {
  purple: "linear-gradient(105deg, #A66CFF 0%, #924CFE 55%, #7B37E8 100%)",
  purpleLight: "linear-gradient(105deg, #F6F0FF 0%, #E2D2FF 55%, #C9AEFF 100%)",
  purpleToOrange: "linear-gradient(105deg, #924CFE 0%, #A66CFF 42%, #FF8256 100%)",
  orange: "linear-gradient(105deg, #FF8256 0%, #F65C39 60%, #E04A28 100%)",
  orangeLight: "linear-gradient(105deg, #FFF4EE 0%, #FFDECD 55%, #FFC0A5 100%)",
  orangeToPurple: "linear-gradient(105deg, #F65C39 0%, #FF8256 40%, #A66CFF 100%)",
};

/** Насыщенная заливка: белый текст, белые кнопки, стеклянная вложенная карточка */
const Solid = ({ bg, nested = true }: { bg: string; nested?: boolean }) => (
  <section className="rounded-2xl px-5 md:px-6 py-5 md:py-6" style={{ background: bg }}>
    <Title onDark />
    <div
      className={`mt-5 flex flex-wrap items-center gap-x-4 gap-y-3 ${
        nested ? "rounded-xl bg-white/15 p-4 md:p-5" : ""
      }`}
    >
      <PhoneIcon tone="onDark" />
      <TaskText onDark />
      <Stores onDark />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta onDark />
      <Hint onDark />
    </div>
  </section>
);

/** Светлая заливка: тёмный текст, белая вложенная карточка */
const Pale = ({ bg }: { bg: string }) => (
  <section className="rounded-2xl px-5 md:px-6 py-5 md:py-6" style={{ background: bg }}>
    <Title />
    <div className="mt-5 rounded-xl bg-background p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <PhoneIcon />
      <TaskText />
      <Stores />
    </div>
    <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
      <Cta />
      <Hint />
    </div>
  </section>
);

const V21 = () => <Solid bg={G.purple} />;
const V22 = () => <Solid bg={G.purple} nested={false} />;
const V23 = () => <Pale bg={G.purpleLight} />;
const V24 = () => <Solid bg={G.purpleToOrange} />;
const V25 = () => <Solid bg={G.orange} />;
const V26 = () => <Pale bg={G.orangeLight} />;
const V27 = () => <Solid bg={G.orangeToPurple} nested={false} />;

/** Градиентная шапка, белое тело */
const V28 = () => (
  <section className="rounded-2xl bg-background border border-border overflow-hidden">
    <div className="px-5 md:px-6 py-4 md:py-5 flex flex-wrap items-center justify-between gap-3" style={{ background: G.purple }}>
      <Title onDark />
      <span className="text-[20px] md:text-[22px] font-medium text-white">3,399 $OA</span>
    </div>
    <div className="px-5 md:px-6 py-5 md:py-6">
      <div className="flex flex-wrap items-center gap-x-4 gap-y-3">
        <PhoneIcon />
        <TaskText />
        <Stores />
      </div>
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </div>
  </section>
);

/** Белый блок с градиентной полосой сверху */
const V29 = () => (
  <section className="rounded-2xl bg-background border border-border overflow-hidden">
    <div className="h-1.5 w-full" style={{ background: G.purpleToOrange }} />
    <div className="px-5 md:px-6 py-5 md:py-6">
      <Title />
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <PhoneIcon />
        <TaskText />
        <Stores />
      </div>
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </div>
  </section>
);

/** Градиентная рамка, светлая фиолетовая заливка внутри */
const V30 = () => (
  <div className="rounded-2xl p-[2px]" style={{ background: G.purpleToOrange }}>
    <section className="rounded-[14px] px-5 md:px-6 py-5 md:py-6" style={{ background: G.purpleLight }}>
      <Title />
      <div className="mt-5 rounded-xl bg-background p-4 md:p-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <PhoneIcon />
        <TaskText />
        <Stores />
      </div>
      <div className="mt-5 flex flex-wrap items-center gap-x-4 gap-y-3">
        <Cta />
        <Hint />
      </div>
    </section>
  </div>
);

const variants: { n: number; name: string; C: () => JSX.Element }[] = [
  { n: 1, name: "Текущий — серый блок, задача в белой карточке", C: V1 },
  { n: 2, name: "Белый блок с бордером, задача на сером", C: V2 },
  { n: 3, name: "Фиолетовый бордер, разделитель перед кнопкой", C: V3 },
  { n: 4, name: "Акцентная полоса слева", C: V4 },
  { n: 5, name: "Серая шапка + белая панель со скруглением", C: V5 },
  { n: 6, name: "Акцентная полоска сверху", C: V6 },
  { n: 7, name: "Сумма в шапке справа", C: V7 },
  { n: 8, name: "Кнопка во всю ширину", C: V8 },
  { n: 9, name: "Две колонки: слева CTA, справа задача", C: V9 },
  { n: 10, name: "Нумерованные шаги 1–2", C: V10 },
  { n: 11, name: "Мягкий фиолетовый фон", C: V11 },
  { n: 12, name: "Иконка у заголовка, аутлайн-кнопки сторов", C: V12 },
  { n: 13, name: "Серый блок, нейтральные иконки и аутлайн-кнопки", C: V13 },
  { n: 14, name: "Строки через разделители", C: V14 },
  { n: 15, name: "Чекбокс-кружок вместо иконки", C: V15 },
  { n: 16, name: "Кнопки сторов в шапке", C: V16 },
  { n: 17, name: "Действия колонкой справа", C: V17 },
  { n: 18, name: "Шапка с подсказкой, всё в одну строку", C: V18 },
  { n: 19, name: "Вложенная карточка на бордере, без заливки", C: V19 },
  { n: 20, name: "Компактный: заголовок внутри строки задачи", C: V20 },
  { n: 21, name: "Фиолетовый градиент, задача в стеклянной карточке", C: V21 },
  { n: 22, name: "Фиолетовый градиент, всё без вложенной карточки", C: V22 },
  { n: 23, name: "Светлый фиолетовый градиент + белая карточка", C: V23 },
  { n: 24, name: "Градиент фиолетовый → оранжевый", C: V24 },
  { n: 25, name: "Оранжевый градиент (цвет SC)", C: V25 },
  { n: 26, name: "Светлый оранжевый градиент + белая карточка", C: V26 },
  { n: 27, name: "Градиент оранжевый → фиолетовый, без карточки", C: V27 },
  { n: 28, name: "Градиентная шапка с суммой, белое тело", C: V28 },
  { n: 29, name: "Белый блок, градиентная полоса сверху", C: V29 },
  { n: 30, name: "Градиентная рамка + светлая фиолетовая заливка", C: V30 },
];

const AirdropVariants = () => (
  <div className="w-full px-4 md:px-9 py-6 md:py-10">
    <div className="max-w-[900px]">
      <h1 className="text-[24px] md:text-[28px] font-medium leading-none text-foreground">
        Airdrop-блок: 30 вариантов
      </h1>
      <p className="text-[15px] text-muted-foreground mt-2 mb-8">
        Текст во всех вариантах одинаковый. Назови номер — поставлю его на страницу «Мой токен».
      </p>

      <div className="flex flex-col gap-10">
        {variants.map(({ n, name, C }) => (
          <div key={n}>
            <div className="flex items-baseline gap-3 mb-3">
              <span className="text-[16px] font-medium text-primary">{n}</span>
              <span className="text-[14px] text-muted-foreground">{name}</span>
            </div>
            <C />
          </div>
        ))}
      </div>
    </div>
  </div>
);

export default AirdropVariants;
