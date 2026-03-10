const CATEGORIES = ["business", "technology", "sports", "health", "science", "entertainment"];

export default function CategoryFilter({ selected, onSelect }) {
  return (
    <div className="flex flex-wrap gap-2 justify-center">
      {CATEGORIES.map((category) => (
        <button
          key={category}
          onClick={() => onSelect(category)}
          className={`px-4 py-1.5 rounded-full text-sm font-semibold capitalize transition-colors
            ${selected === category
              ? "bg-white text-gray-800"
              : "bg-white/10 text-white border border-white/20 hover:bg-white/20"}`}
        >
          {category}
        </button>
      ))}
    </div>
  );
}