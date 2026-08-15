// Lesson data shared between the course map (/my-courses) and the home screen.

// ============ Article-style content types ============
export type Inline = string | { text: string; bold?: boolean; highlight?: boolean };
export type Section =
  | { type: "h2"; text: string }
  | { type: "h3"; text: string }
  | { type: "p"; runs: Inline[] }
  | { type: "list"; items: Inline[][] };

export interface LessonContent {
  heading: string;
  author: string;
  views: number;
  readMin: number;
  date: string;
  sections: Section[];
}

export interface Lesson {
  number: number;
  title: string;
  description: string;
  reward: number;
  progress: number;
  hasInstruction?: boolean;
  content: LessonContent;
}

export const lessonsData: Lesson[] = [
  {
    number: 1,
    title: "Введение в Telegram Gifts",
    description: "Узнаем, что такое Telegram Gifts, как они работают и почему это интересно.",
    reward: 500,
    progress: 100,
    hasInstruction: true,
    content: {
      heading: "Что такое Telegram Gifts и почему это новый класс цифровых активов?",
      author: "pablo1337.base.eth",
      views: 124,
      readMin: 3,
      date: "12 мая 2026 г.",
      sections: [
        { type: "p", runs: [
          { text: "Telegram Gifts", bold: true }, " — это новая функция в мессенджере, которая превращает обычные подарки в ",
          { text: "уникальные цифровые активы", highlight: true }, " на блокчейне TON. Их можно дарить, коллекционировать и продавать на вторичном рынке.",
        ]},
        { type: "p", runs: [
          "Каждый подарок имеет ограниченный тираж, поэтому редкие экземпляры быстро становятся ",
          { text: "объектом коллекционирования", highlight: true }, " и заметно растут в цене.",
        ]},
        { type: "h2", text: "Разберём на пальцах" },
        { type: "h3", text: "Покупка подарка" },
        { type: "p", runs: [
          "Вы выбираете подарок в Telegram, оплачиваете его звёздами и сразу получаете в свой инвентарь. Подарок можно подарить другу или оставить себе.",
        ]},
        { type: "h3", text: "Вторичный рынок" },
        { type: "p", runs: [
          "Полученный подарок можно перепродать. Цена формируется ",
          { text: "спросом и редкостью", bold: true }, ": чем меньше тираж и выше интерес сообщества — тем дороже актив.",
        ]},
        { type: "h2", text: "Почему это интересно?" },
        { type: "p", runs: [
          "Telegram Gifts открывают ",
          { text: "новый способ заработка", highlight: true },
          " внутри привычного мессенджера — без сложных кошельков и бирж. Достаточно интуиции и понимания трендов.",
        ]},
      ],
    },
  },
  {
    number: 4,
    title: "Как зарабатывают на подарках?",
    description: "Узнаем, как идёт торговля сейчас и какие навыки помогут выйти в плюс.",
    reward: 1300,
    progress: 100,
    content: {
      heading: "Как зарабатывают на Telegram Gifts: критерии выбора прибыльных подарков",
      author: "pablo1337.base.eth",
      views: 89,
      readMin: 4,
      date: "15 мая 2026 г.",
      sections: [
        { type: "p", runs: [
          { text: "Выбор подарков для инвестиций", bold: true }, " — ключевой навык, который отделяет случайную прибыль от стабильного дохода. Разберём, на что смотреть в первую очередь.",
        ]},
        { type: "h2", text: "Критерии оценки" },
        { type: "h3", text: "Редкость" },
        { type: "p", runs: [
          "Чем ниже тираж — тем выше потенциал роста. Ищите подарки с пометкой ",
          { text: "Limited Edition", highlight: true }, " и небольшим количеством выпущенных экземпляров.",
        ]},
        { type: "h3", text: "Дизайн и эстетика" },
        { type: "p", runs: [
          "Визуально привлекательные подарки пользуются большим спросом. Сообщество ценит ",
          { text: "сильную айдентику", highlight: true }, " и узнаваемый стиль.",
        ]},
        { type: "h3", text: "Тренды сообщества" },
        { type: "p", runs: [
          "Следите за активностью в каналах коллекционеров — резкий рост обсуждений часто опережает рост цены на ",
          { text: "несколько часов", bold: true }, ".",
        ]},
      ],
    },
  },
  {
    number: 6,
    title: "Стратегии торговли на вторичном рынке",
    description: "Разберём основные стратегии покупки и продажи подарков.",
    reward: 800,
    progress: 45,
    hasInstruction: true,
    content: {
      heading: "Стратегии торговли на вторичном рынке Telegram Gifts",
      author: "pablo1337.base.eth",
      views: 57,
      readMin: 5,
      date: "20 мая 2026 г.",
      sections: [
        { type: "p", runs: [
          { text: "Вторичный рынок", bold: true }, " — это место, где формируется реальная цена подарка. Здесь работают сразу несколько ",
          { text: "проверенных стратегий", highlight: true }, ", каждая со своим горизонтом и риском.",
        ]},
        { type: "h2", text: "Разберём на пальцах" },
        { type: "h3", text: "Скальпинг" },
        { type: "p", runs: [
          "Быстрая покупка на просадке и продажа на отскоке. Подходит активным трейдерам, готовым ",
          { text: "следить за рынком в режиме онлайн", highlight: true }, ".",
        ]},
        { type: "h3", text: "Долгосрочное удержание" },
        { type: "p", runs: [
          "Покупаете редкий подарок и держите месяцами. Главное — ",
          { text: "выбрать действительно дефицитный актив", bold: true }, " с растущим интересом.",
        ]},
        { type: "h2", text: "Пример" },
        { type: "p", runs: [
          "Подарок с тиражом 500 шт. куплен за 200 звёзд. Через месяц на фоне новой коллекции его цена выросла до 850 звёзд — ",
          { text: "+325% за 30 дней", highlight: true }, ".",
        ]},
      ],
    },
  },
  {
    number: 7,
    title: "Анализ трендов и популярных подарков",
    description: "Научимся отслеживать тренды и предсказывать популярность подарков.",
    reward: 1000,
    progress: 0,
    content: {
      heading: "Анализ трендов: как предсказывать рост популярных подарков",
      author: "pablo1337.base.eth",
      views: 12,
      readMin: 3,
      date: "25 мая 2026 г.",
      sections: [
        { type: "p", runs: [
          "Умение читать тренды — это ",
          { text: "ключевой навык успешного трейдера", highlight: true }, ". Цена редко растёт случайно: за каждым движением стоят понятные сигналы.",
        ]},
        { type: "h2", text: "Инструменты анализа" },
        { type: "h3", text: "Мониторинг цен" },
        { type: "p", runs: [
          "Регулярно сверяйтесь с маркетплейсами и трекерами. Резкий рост объёмов почти всегда предшествует ",
          { text: "ценовому импульсу", bold: true }, ".",
        ]},
        { type: "h3", text: "Активность сообщества" },
        { type: "p", runs: [
          "Каналы и чаты коллекционеров — лучший опережающий индикатор. Если о подарке начали говорить — у вас есть ",
          { text: "пара часов", highlight: true }, " на покупку.",
        ]},
      ],
    },
  },
];

// Lesson states derived from progress: completed / current / locked.
export const lessonState = (idx: number): "completed" | "current" | "locked" => {
  const l = lessonsData[idx];
  if (!l) return "locked";
  if (l.progress >= 100) return "completed";
  if (l.progress > 0) return "current";
  const prev = lessonsData[idx - 1];
  if (!prev || prev.progress >= 100) return "current";
  return "locked";
};

// Overall course completion in percent.
export const courseProgress = Math.round(
  lessonsData.reduce((s, l) => s + l.progress, 0) / lessonsData.length
);

// Index of the lesson the user should continue with.
export const currentLessonIndex = Math.max(
  0,
  lessonsData.findIndex((_, i) => lessonState(i) === "current")
);
