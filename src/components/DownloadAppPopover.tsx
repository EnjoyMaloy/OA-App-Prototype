import { ReactNode } from "react";
import { QRCodeSVG } from "qrcode.react";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";
import { AppleIcon, GooglePlayIcon } from "@/components/StoreIcons";
import { STORE_LINKS, DOWNLOAD_LINK } from "@/lib/storeLinks";

const BTN =
  "flex items-center justify-center gap-2.5 h-11 px-5 rounded-[10px] bg-primary text-primary-foreground text-[16px] font-medium hover:brightness-110 transition-all whitespace-nowrap";

/** QR всегда на белом — иначе камера не считает в тёмной теме */
const Qr = ({ value, size }: { value: string; size: number }) => (
  <div className="rounded-xl bg-white p-2 flex-shrink-0 flex items-center justify-center">
    <QRCodeSVG value={value} size={size} level="M" bgColor="#ffffff" fgColor="#232323" />
  </div>
);

/**
 * Оборачивает любой триггер и по клику показывает QR-код.
 * store задан  — один QR на ссылку этого стора и одна кнопка под ним.
 * store не задан — общий QR и обе кнопки (для нейтрального триггера, например в сайдбаре).
 * onStoreClick вызывается при переходе в стор.
 */
const DownloadAppPopover = ({
  children,
  store,
  onStoreClick,
  align = "start",
  side = "bottom",
}: {
  children: ReactNode;
  store?: "appStore" | "googlePlay";
  onStoreClick?: () => void;
  align?: "start" | "center" | "end";
  side?: "top" | "right" | "bottom" | "left";
}) => (
  <Popover>
    <PopoverTrigger asChild>{children}</PopoverTrigger>
    <PopoverContent align={align} side={side} className="w-auto p-5 rounded-2xl">
      {store ? (
        <div className="flex flex-col gap-3">
          <Qr value={STORE_LINKS[store]} size={140} />
          <a
            href={STORE_LINKS[store]}
            target="_blank"
            rel="noopener noreferrer"
            onClick={onStoreClick}
            className={`${BTN} w-full`}
          >
            {store === "appStore" ? (
              <AppleIcon className="w-[18px] h-[18px]" />
            ) : (
              <GooglePlayIcon className="w-[18px] h-[18px]" />
            )}
            {store === "appStore" ? "App Store" : "Google Play"}
          </a>
        </div>
      ) : (
        <div className="flex items-stretch gap-5">
          <Qr value={DOWNLOAD_LINK} size={82} />
          <div className="flex flex-col gap-2.5">
            <a
              href={STORE_LINKS.appStore}
              target="_blank"
              rel="noopener noreferrer"
              onClick={onStoreClick}
              className={BTN}
            >
              <AppleIcon className="w-[18px] h-[18px]" />
              App Store
            </a>
            <a
              href={STORE_LINKS.googlePlay}
              target="_blank"
              rel="noopener noreferrer"
              onClick={onStoreClick}
              className={BTN}
            >
              <GooglePlayIcon className="w-[18px] h-[18px]" />
              Google Play
            </a>
          </div>
        </div>
      )}
    </PopoverContent>
  </Popover>
);

export default DownloadAppPopover;
