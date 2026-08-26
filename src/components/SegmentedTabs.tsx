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
    {/* Пункты не уже своего текста, но растягиваются, если в лотке остаётся место */}
    <div className="flex items-center gap-1 w-full min-w-max p-1">
      {tabs.map((tab) => {
        const active = tab.id === value;
        return (
          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={`grow shrink-0 h-[56px] px-6 rounded-full text-[22px] font-medium whitespace-nowrap transition-colors ${
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
