import json
import os
from collections import Counter

def main():
    # Paths
    workspace_dir = r"c:\Users\user\Desktop\web"
    json_path = os.path.join(workspace_dir, "scraped_dramas.json")
    output_dir = os.path.join(workspace_dir, "drama_analysis")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the scraped dramas
    with open(json_path, "r", encoding="utf-8") as f:
        # Check if file has ```json and ``` wrapping it (sometimes firecrawl outputs markdown wrapper)
        content = f.read().strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
        dramas = json.loads(content.strip())
    
    # Extract genres and build statistics
    all_genres = []
    genre_to_dramas = {}
    
    for drama in dramas:
        title = drama.get("title", "")
        genre_str = drama.get("genre", "")
        # Split by various delimiters
        genres = [g.strip() for g in genre_str.replace("/", "、").replace(",", "、").split("、") if g.strip()]
        
        for g in genres:
            all_genres.append(g)
            if g not in genre_to_dramas:
                genre_to_dramas[g] = []
            genre_to_dramas[g].append({
                "title": title,
                "cast": drama.get("cast", ""),
                "platform": drama.get("platform", "")
            })
            
    # Calculate statistics
    genre_counts = dict(Counter(all_genres))
    # Sort by count descending
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Write stats to JSON
    stats_output = {
        "total_dramas": len(dramas),
        "unique_genres_count": len(genre_counts),
        "genre_frequencies": dict(sorted_genres)
    }
    
    with open(os.path.join(output_dir, "genre_statistics.json"), "w", encoding="utf-8") as f:
        json.dump(stats_output, f, ensure_ascii=False, indent=2)
        
    # Write categorized dramas to JSON
    with open(os.path.join(output_dir, "categorized_dramas.json"), "w", encoding="utf-8") as f:
        json.dump(genre_to_dramas, f, ensure_ascii=False, indent=2)
        
    # Generate a beautiful Markdown Report
    report_lines = []
    report_lines.append("# 2026年台劇推薦數據分析與分類報告\n")
    report_lines.append(f"- **分析劇集總數**：{len(dramas)} 部")
    report_lines.append(f"- **分類標籤總數**：{len(genre_counts)} 種\n")
    
    report_lines.append("## 📊 劇集類型統計排名 (Genre Statistics)")
    report_lines.append("| 排名 | 類型標籤 | 出現次數 | 佔比 | 直方圖示意 |")
    report_lines.append("| :--- | :--- | :--- | :--- | :--- |")
    
    for rank, (genre, count) in enumerate(sorted_genres, 1):
        percentage = (count / len(dramas)) * 100
        bar = "█" * count
        report_lines.append(f"| {rank} | {genre} | {count} | {percentage:.1f}% | {bar} |")
        
    report_lines.append("\n## 🗂️ 類型分類詳細劇單 (Categorized Dramas)")
    
    # Sort category names to display beautifully
    for genre, count in sorted_genres:
        report_lines.append(f"### 🏷️ {genre} ({count} 部)")
        for item in genre_to_dramas[genre]:
            report_lines.append(f"- **《{item['title']}》** (主要演員：{item['cast']} | 平台：{item['platform']})")
        report_lines.append("")
        
    with open(os.path.join(output_dir, "analysis_report.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
        
    print("Analysis completed and files saved successfully!")

if __name__ == "__main__":
    main()
