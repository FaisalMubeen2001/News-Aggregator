export default function ArticleCard({ article }) {
  const sentimentColor = {
    Positive: "bg-green-100 text-green-700",
    Negative: "bg-red-100 text-red-700",
    Neutral: "bg-gray-100 text-gray-700",
  };

  return (
    <div className="bg-white rounded-2xl shadow-md p-5 flex flex-col gap-3 hover:shadow-lg transition-shadow">
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold uppercase tracking-wide text-blue-500">{article.source}</span>
        {article.sentiment && (
          <span className={`text-xs font-semibold px-2 py-1 rounded-full ${sentimentColor[article.sentiment] || "bg-gray-100 text-gray-700"}`}>{article.sentiment}</span>
        )}
      </div>
      <h2 className="text-base font-bold text-gray-800 leading-snug">{article.title}</h2>
      {article.summary ? (
        <p className="text-sm text-gray-600">{article.summary}</p>
      ) : (
        <p className="text-sm text-gray-400 italic">{article.description}</p>
      )}
      <div className="flex items-center justify-between mt-auto pt-2 border-t border-gray-100">
        <span className="text-xs text-gray-400">{new Date(article.published_at).toLocaleDateString()}</span>
        <a href={article.url} target="_blank" rel="noopener noreferrer" className="text-xs font-semibold text-blue-500 hover:underline">Read more</a>
      </div>
    </div>
  );
}