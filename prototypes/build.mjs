/*
 * Собирает черновик экрана в самодостаточный HTML для публикации артефактом.
 *
 *   node prototypes/build.mjs prototypes/<файл>.html [выходной-файл]
 *
 * Черновик пишется как фрагмент: <title>, потом разметка. Без <!doctype>, <html>,
 * <head> и <body> — их добавляет хостинг артефактов. Сборщик подставляет:
 *   - шрифты TT Commons в data URI (внешняя сеть в артефактах закрыта);
 *   - токены :root/.dark и типографику прямо из src/index.css, чтобы черновик
 *     не разъезжался с приложением;
 *   - prototypes/kit.css.
 */
import { readFileSync, writeFileSync } from "node:fs";
import { basename, dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const WEIGHTS = [
  ["TT_Commons_Regular.otf", 400],
  ["TT_Commons_Medium.otf", 500],
  ["TT_Commons_DemiBold.otf", 600],
  ["TT_Commons_Bold.otf", 700],
  ["TT_Commons_Black.otf", 900],
];

const src = process.argv[2];
if (!src) {
  console.error("Укажи черновик: node prototypes/build.mjs prototypes/<файл>.html");
  process.exit(1);
}
const out = process.argv[3] ?? resolve(ROOT, "dist-prototypes", basename(src));

const fonts = WEIGHTS.map(([file, weight]) => {
  const data = readFileSync(resolve(ROOT, "public/fonts", file)).toString("base64");
  return `@font-face{font-family:'TT Commons';src:url(data:font/otf;base64,${data}) format('opentype');font-weight:${weight};font-style:normal;font-display:block}`;
}).join("\n");

// Токены и типографика — из приложения, а не копией
const appCss = readFileSync(resolve(ROOT, "src/index.css"), "utf8");
const grab = (re, what) => {
  const m = appCss.match(re);
  if (!m) throw new Error(`Не нашёл ${what} в src/index.css — поменялась структура файла?`);
  return m[0];
};
const tokens = [
  grab(/:root\s*\{[\s\S]*?\n {2}\}/, "блок :root"),
  grab(/\.dark\s*\{[\s\S]*?\n {2}\}/, "блок .dark"),
  appCss.match(/^\s*\.text-[\w-]+\s*\{[^}]*\}$/gm)?.join("\n") ?? "",
].join("\n");

const kit = readFileSync(resolve(ROOT, "prototypes/kit.css"), "utf8");
const draft = readFileSync(resolve(src), "utf8");

for (const tag of ["<!doctype", "<html", "<head", "<body"]) {
  if (draft.toLowerCase().includes(tag)) {
    console.error(`В черновике есть ${tag}> — фрагмент должен быть без обёртки документа.`);
    process.exit(1);
  }
}

const title = draft.match(/<title>[\s\S]*?<\/title>/)?.[0] ?? "";
const body = title ? draft.replace(title, "") : draft;

// charset идёт первым: без него кириллица во фрагменте читается как latin-1
writeFileSync(
  out,
  `<meta charset="utf-8">\n${title}\n<style>\n${fonts}\n${tokens}\n${kit}\n</style>\n${body.trim()}\n`
);
console.log(`${out} — ${(readFileSync(out).length / 1024 / 1024).toFixed(2)} МБ`);
