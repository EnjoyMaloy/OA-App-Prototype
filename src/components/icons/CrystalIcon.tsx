interface CrystalIconProps {
  className?: string;
  style?: React.CSSProperties;
  /** Основной цвет граней */
  color?: string;
  /** Цвет светлых граней — по умолчанию полупрозрачный белый поверх основного */
  highlight?: string;
}

/** Кристалл валюты: огранка сверху, вытянутый низ, светлая грань слева. */
const CrystalIcon = ({ className, style, color = "#924CFE", highlight = "rgba(255,255,255,0.45)" }: CrystalIconProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    className={className}
    style={style}
    fill="none"
  >
    {/* Корона */}
    <path d="M7.2 3h9.6l3.2 5.4H4L7.2 3Z" fill={color} />
    {/* Павильон */}
    <path d="M4 8.4h16L12 21 4 8.4Z" fill={color} />
    {/* Светлые грани */}
    <path d="M7.2 3 4 8.4h4.6L7.2 3Z" fill={highlight} />
    <path d="M4 8.4h4.6L12 21 4 8.4Z" fill={highlight} />
  </svg>
);

export default CrystalIcon;
