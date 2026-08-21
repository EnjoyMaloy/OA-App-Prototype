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
    return lang === "ru" ? `${w} ${pluralRu(w, ["неделю", "недели", "недель"])} назад` : `${w} week${w > 1 ? "s" : ""} ago`;
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

import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
