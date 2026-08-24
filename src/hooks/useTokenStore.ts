import { useState, useEffect } from "react";

export interface TokenStore {
  /** Мобильное приложение установлено и вход выполнен */
  appTaskDone: boolean;
  /** SC уже сконвертированы в $OA */
  converted: boolean;
  convertedAt: string | null;
  /** Сколько SC было списано и сколько $OA начислено */
  burnedSc: number;
  receivedOa: number;
}

const STORAGE_KEY = "demo_token_store";
const EVENT_NAME = "token_store_update";

const emptyStore: TokenStore = {
  appTaskDone: false,
  converted: false,
  convertedAt: null,
  burnedSc: 0,
  receivedOa: 0,
};

function getStore(): TokenStore {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    if (raw) return { ...emptyStore, ...JSON.parse(raw) };
  } catch {}
  return { ...emptyStore };
}

function saveStore(store: TokenStore) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(store));
  window.dispatchEvent(new Event(EVENT_NAME));
}

export function completeAppTask() {
  saveStore({ ...getStore(), appTaskDone: true });
}

export function convertScToOa(burnedSc: number, receivedOa: number) {
  saveStore({
    ...getStore(),
    converted: true,
    convertedAt: new Date().toISOString(),
    burnedSc,
    receivedOa,
  });
}

export function resetTokenStore() {
  localStorage.removeItem(STORAGE_KEY);
  window.dispatchEvent(new Event(EVENT_NAME));
}

export function useTokenStore(): TokenStore {
  const [store, setStore] = useState<TokenStore>(getStore);

  useEffect(() => {
    const handler = () => setStore(getStore());
    // "Сбросить всё" в сайдбаре чистит и состояние токенов
    const resetHandler = () => {
      localStorage.removeItem(STORAGE_KEY);
      setStore(getStore());
    };
    window.addEventListener(EVENT_NAME, handler);
    window.addEventListener("demo_reset", resetHandler);
    return () => {
      window.removeEventListener(EVENT_NAME, handler);
      window.removeEventListener("demo_reset", resetHandler);
    };
  }, []);

  return store;
}
