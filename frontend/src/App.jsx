import { useState, useEffect } from "react";
import axios from "axios";
import ArticleCard from "./components/ArticleCard";
import CategoryFilter from "./components/CategoryFilter";

const categoryThemes = {
  business: "from-slate-900 via-blue-950 to-slate-800",
  technology: "from-blue-950 via-cyan-900 to-blue-900",
  sports: "from-orange-900 via-red-800 to-yellow-900",
  health: "from-teal-900 via-green-800 to-teal-950",
  science: "from-purple-950 via-indigo-900 to-purple-900",
  entertainment: "from-gray-900 via-zinc-800 to-slate-900",
};

export default function App() {
  const [articles, setArticles] = useState([]);
  const [category, setCategory] = useState("technology");
  const [loading, setLoading] = useState(false);
  const [enrich, setEnrich] = useState(false);

  const fetchArticles = async (cat, enriched) => {
    setLoading(true);
    try {
      const response = await axios.get(`https://news-aggregator-4d5n.onrender.com/articles`, {
        params: { category: cat, page_size: 6, enrich: enriched }
      });
      setArticles(response.data.articles);
    } catch (error) {
      console.error("Error fetching articles:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchArticles(category, enrich);
  }, [category]);

  const handleEnrichToggle = () => {
    const newEnrich = !enrich;
    setEnrich(newEnrich);
    fetchArticles(category, newEnrich);
  };

  const theme = categoryThemes[category];

  return (
    <div className={`min-h-screen bg-gradient-to-br ${theme} transition-all duration-700`}>
      <header className="bg-white/10 backdrop-blur-sm sticky top-0 z-10 border-b border-white/10">
        <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-white">📰 News Aggregator</h1>
          <button
            onClick={handleEnrichToggle}
            className={`px-4 py-1.5 rounded-full text-sm font-semibold transition-colors
              ${enrich ? "bg-white text-blue-600" : "bg-white/10 text-white border border-white/20 hover:bg-white/20"}`}
          >
            {enrich ? "✨ AI On" : "✨ AI Off"}
          </button>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-8 flex flex-col gap-6">
        <CategoryFilter selected={category} onSelect={setCategory} />

        {loading ? (
          <div className="text-center text-white/60 py-20 text-lg">Loading articles...</div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {articles.map((article, index) => (
              <ArticleCard key={index} article={article} />
            ))}
          </div>
        )}
      </main>
    </div>
  );
}