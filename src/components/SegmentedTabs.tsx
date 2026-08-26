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
  <div className={`overflow-x-auto scrollbar-hide rounded-full bg-muted ${className}`}>
    <div className="flex items-center gap-1 w-max min-w-full p-1">
      {tabs.map((tab) => {
        const active = tab.id === value;
        return (
          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={`h-11 px-5 rounded-full text-[17px] font-medium whitespace-nowrap transition-colors ${
              active ? "bg-background text-foreground shadow-sm" : "text-muted-foreground"
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
