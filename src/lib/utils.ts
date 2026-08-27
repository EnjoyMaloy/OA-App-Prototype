import { clsx, type ClassValue } from "clsx"

/** Русские окончания по числу: 1 урок, 2 урока, 5 уроков */
export function pluralRu(n: number, forms: [string, string, string]) {
  const mod10 = n % 10;
  const mod100 = n % 100;
  if (mod10 === 1 && mod100 !== 11) return forms[0];
  if (mod10 >= 2 && mod10 <= 4 && (mod100 < 10 || mod100 >= 20)) return forms[1];
  return forms[2];
};
/** «2 дня назад», «месяц назад» — как счётчик обновления на YouTube */
export function agoLabel(days: number, lang: "ru" | "en") {
  if (days <= 0) return lang === "ru" ? "сегодня" : "today";
  if (days === 1) return lang === "ru" ? "день назад" : "1 day ago";
  if (days < 7) return lang === "ru" ? `${days} ${pluralRu(days, ["день", "дня", "дней"])} назад` : `${days} days ago`;
  if (days < 31) {
    const w = Math.round(days / 7);
    return lang === "ru"
      ? w === 1 ? "неделю назад" : `${w} ${pluralRu(w, ["неделю", "недели", "недель"])} назад`
      : `${w} week${w > 1 ? "s" : ""} ago`;
  }
  if (days < 365) {
    const m = Math.round(days / 30);
    return lang === "ru"
      ? m === 1 ? "месяц назад" : `${m} ${pluralRu(m, ["месяц", "месяца", "месяцев"])} назад`
      : `${m} month${m > 1 ? "s" : ""} ago`;
  }
  const y = Math.round(days / 365);
  return lang === "ru"
    ? y === 1 ? "год назад" : `${y} ${pluralRu(y, ["год", "года", "лет"])} назад`
    : `${y} year${y > 1 ? "s" : ""} ago`;
}

/** Рейтинг всегда с одним знаком: 4.95 → 4.9 */
export function formatRating(r: number) {
  return (Math.floor(r * 10) / 10).toFixed(1);
}

/** Компактное число для карточек: 1 024 → 1К, 35 419 → 35К */
export function compactNumber(n: number, lang: "ru" | "en") {
  const k = lang === "ru" ? "К" : "K";
  if (n < 1000) return String(n);
  const v = n / 1000;
  const digits = v < 10 ? 1 : 0;
  const num = v.toFixed(digits).replace(/\.0$/, "");
  return (lang === "ru" ? num.replace(".", ",") : num) + k;
}

/** Короткая дата обновления, когда полная не помещается: «2 дня», «3 нед», «5 мес» */
export function agoLabelShort(days: number, lang: "ru" | "en") {
  if (days <= 0) return lang === "ru" ? "сегодня" : "today";
  if (days < 7) return lang === "ru" ? `${days} ${pluralRu(days, ["день", "дня", "дней"])}` : `${days}d`;
  if (days < 31) {
    const w = Math.round(days / 7);
    return lang === "ru" ? `${w} нед` : `${w}w`;
  }
  if (days < 365) {
    const m = Math.round(days / 30);
    return lang === "ru" ? `${m} мес` : `${m}mo`;
  }
  const y = Math.round(days / 365);
  return lang === "ru" ? `${y} ${pluralRu(y, ["год", "года", "лет"])}` : `${y}y`;
}

import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
