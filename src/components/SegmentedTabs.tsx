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
 * Переключатель-сегменты: светлый лоток, активный пункт — белая «пилюля».
 * Один компонент на все разделы, чтобы переключатели выглядели одинаково.
 */
const SegmentedTabs = ({ tabs, value, onChange, className = "" }: SegmentedTabsProps) => (
  <div className={`flex items-center gap-1 p-1 rounded-full bg-muted ${className}`}>
    {tabs.map((tab) => {
      const active = tab.id === value;
      return (
        <button
          key={tab.id}
          onClick={() => onChange(tab.id)}
          className={`flex-1 basis-0 min-w-0 h-11 px-3 rounded-full text-[15px] font-medium whitespace-nowrap transition-colors ${
            active ? "bg-background text-foreground shadow-sm" : "text-muted-foreground"
          }`}
        >
          {tab.label}
        </button>
      );
    })}
  </div>
);

export default SegmentedTabs;
