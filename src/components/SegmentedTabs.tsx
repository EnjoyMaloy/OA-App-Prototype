export interface SegmentedTab {
  id: string;
  label: string;
}

interface SegmentedTabsProps {
  tabs: SegmentedTab[];
  value: string;
  onChange: (id: string) => void;
  className?: string;
}

/**
 * Переключатель-сегменты: лоток-«пилюля», внутри пункты по ширине текста.
 * Активный — залитая пилюля; если пунктов много, ряд листается вбок.
 */
const SegmentedTabs = ({ tabs, value, onChange, className = "" }: SegmentedTabsProps) => (
  <div
    className={`overflow-x-auto scrollbar-hide rounded-full ${className}`}
    // Лоток чуть темнее любой подложки, поэтому виден и на белом, и на карточке автора
    style={{ background: "hsl(var(--foreground) / 0.06)" }}
  >
    {/* Колонки одной ширины: делят лоток поровну, пустоты справа не остаётся */}
    <div className="grid grid-flow-col auto-cols-fr w-full gap-1 p-1">
      {tabs.map((tab) => {
        const active = tab.id === value;
        return (
          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={`h-[50px] px-2 rounded-full text-[17px] font-medium whitespace-nowrap overflow-hidden transition-colors ${
              active
                ? "bg-background dark:bg-[hsl(var(--foreground)/0.14)] text-foreground shadow-sm"
                : "text-muted-foreground"
            }`}
          >
            {tab.label}
          </button>
        );
      })}
    </div>
  </div>
);

export default SegmentedTabs;
