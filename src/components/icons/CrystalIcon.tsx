interface CrystalIconProps {
  className?: string;
  style?: React.CSSProperties;
  /** Основной цвет кристалла */
  color?: string;
}

/**
 * Кристалл валюты. Форма плотная и заливная — под пару к огоньку стрика:
 * широкая корона, скруглённые углы, одна светлая грань вместо мелкой огранки.
 */
const CrystalIcon = ({ className, style, color = "#924CFE" }: CrystalIconProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 24 24"
    className={className}
    style={style}
    fill="none"
  >
    <path
      d="M6.4 3h11.2c.6 0 1.16.29 1.5.78l2.5 3.54c.42.6.38 1.4-.1 1.95l-8.1 9.3a1.86 1.86 0 0 1-2.8 0l-8.1-9.3a1.63 1.63 0 0 1-.1-1.95l2.5-3.54c.34-.49.9-.78 1.5-.78Z"
      fill={color}
    />
    <path d="M6.4 3h5.6L9.4 9.9 2.4 8.3 4.9 3.78c.34-.49.9-.78 1.5-.78Z" fill="#FFFFFF" fillOpacity="0.28" />
    <path d="m9.4 9.9 2.6 8.9-8.1-9.3a1.7 1.7 0 0 1-.4-.7l5.9 1.1Z" fill="#FFFFFF" fillOpacity="0.16" />
  </svg>
);

export default CrystalIcon;
