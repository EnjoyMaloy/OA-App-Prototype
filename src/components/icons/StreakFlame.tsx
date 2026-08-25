import { useId } from "react";

/**
 * Стрик: пламя с градиентом и число внутри — цифра набрана с белой обводкой
 * (paint-order: stroke), поэтому читается поверх огня.
 */
const StreakFlame = ({ value, className = "" }: { value: number; className?: string }) => {
  // Идентификатор градиента уникален на экземпляр: иначе вторая копия иконки
  // ссылается на градиент внутри скрытой первой и остаётся незакрашенной
  const gradientId = useId();

  return (
    <span className={`relative inline-flex items-center justify-center ${className}`}>
      <svg width="25" height="30" viewBox="0 0 84 102" fill="none" aria-hidden>
        <path
          d="M64.8944 23.6509C64.3017 22.908 63.4033 22.4755 62.4534 22.4755C62.4484 22.4755 62.443 22.4755 62.4378 22.4755C61.4822 22.4803 60.5815 22.9223 59.9932 23.6756L56.4198 28.2486L44.8594 1.86949C44.3673 0.746095 43.263 0.0151618 42.0364 0.000419644C40.8063 -0.016514 39.689 0.690513 39.1701 1.80176L21.0914 40.5227L17.1829 33.6046C16.6524 32.6649 15.674 32.0661 14.5959 32.0209C13.5175 31.975 12.4927 32.4896 11.8847 33.3811C4.41219 44.3384 0.623047 53.504 0.623047 60.6235C0.623246 83.4386 19.1845 102 41.9994 102C64.8149 102 83.3765 83.4386 83.3765 60.6231C83.3767 51.4658 77.1583 39.0264 64.8944 23.6509ZM41.9994 82.8491C34.9978 82.8491 29.3016 77.1531 29.3016 70.1515C29.3016 68.4006 29.8351 65.0617 34.45 56.3186C36.8655 51.7425 39.2428 47.8876 39.343 47.7257C39.9118 46.8051 40.917 46.2447 41.9992 46.2447C43.0813 46.2447 44.0864 46.8051 44.6554 47.7257C44.7554 47.8874 47.1329 51.7425 49.5484 56.3184C54.1637 65.0617 54.6974 68.4006 54.6974 70.1515C54.6976 77.1531 49.0013 82.8491 41.9994 82.8491Z"
          fill={`url(#${gradientId})`}
        />
        <defs>
          <linearGradient id={gradientId} x1="42" y1="0" x2="42" y2="102" gradientUnits="userSpaceOnUse">
            <stop stopColor="#EB4620" />
            <stop offset="1" stopColor="#FE7B5D" />
          </linearGradient>
        </defs>
      </svg>

      {/* Число сидит в нижней части пламени */}
      <svg width="34" height="14" className="absolute left-1/2 -translate-x-1/2 bottom-[2px]" aria-hidden>
        <text
          x="50%"
          y="70%"
          textAnchor="middle"
          dominantBaseline="middle"
          stroke="#FBF9FF"
          strokeWidth="4"
          fill="#111111"
          paintOrder="stroke"
          fontSize="14"
          fontWeight="600"
          strokeLinejoin="round"
          strokeLinecap="round"
        >
          {value}
        </text>
      </svg>
    </span>
    );
};

export default StreakFlame;
