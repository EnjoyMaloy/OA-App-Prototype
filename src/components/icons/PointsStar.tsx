import { useId } from "react";

/** Восьмиконечная «звезда» баллов: фиолетовый градиент и светлый внутренний кант — как объёмный значок */
const PointsStar = ({ className = "" }: { className?: string }) => {
  const gradientId = useId();

  return (
    <svg viewBox="0 0 24 24" className={className} aria-hidden>
      <path
        d="M12.0 0.4 L14.91 4.98 L20.2 3.8 L19.02 9.09 L23.6 12.0 L19.02 14.91 L20.2 20.2 L14.91 19.02 L12.0 23.6 L9.09 19.02 L3.8 20.2 L4.98 14.91 L0.4 12.0 L4.98 9.09 L3.8 3.8 L9.09 4.98 Z"
        fill={`url(#${gradientId})`}
        stroke="#7B3EF0"
        strokeWidth="0.8"
        strokeLinejoin="round"
      />
      {/* Внутренний светлый контур даёт блик по фаске */}
      <path
        d="M12.0 3.1 L14.2 6.6 L18.2 5.7 L17.3 9.7 L20.8 12.0 L17.3 14.3 L18.2 18.3 L14.2 17.4 L12.0 20.9 L9.8 17.4 L5.8 18.3 L6.7 14.3 L3.2 12.0 L6.7 9.7 L5.8 5.7 L9.8 6.6 Z"
        fill="none"
        stroke="rgba(255,255,255,0.5)"
        strokeWidth="0.9"
        strokeLinejoin="round"
      />
      <defs>
        <linearGradient id={gradientId} x1="4" y1="2" x2="20" y2="22" gradientUnits="userSpaceOnUse">
          <stop stopColor="#A78BFA" />
          <stop offset="0.55" stopColor="#8B5CF6" />
          <stop offset="1" stopColor="#7C3AED" />
        </linearGradient>
      </defs>
    </svg>
  );
};

export default PointsStar;
