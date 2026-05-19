import json
import os
import subprocess
from collections import Counter

def main():
    workspace_dir = r"c:\Users\user\Desktop\web"
    json_path = os.path.join(workspace_dir, "scraped_dramas.json")
    output_dir = os.path.join(workspace_dir, "drama_analysis")
    
    # Ensure output dir exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read dramas
    with open(json_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
        dramas = json.loads(content.strip())
        
    # Analyze genres & platforms
    all_genres = []
    all_platforms = []
    for d in dramas:
        gs = [g.strip() for g in d.get("genre", "").replace("/", "、").replace(",", "、").split("、") if g.strip()]
        ps = [p.strip() for p in d.get("platform", "").replace("/", "、").replace(",", "、").split("、") if p.strip()]
        all_genres.extend(gs)
        all_platforms.extend(ps)
        
    genre_counts = dict(Counter(all_genres))
    platform_counts = dict(Counter(all_platforms))
    
    sorted_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)
    sorted_platforms = sorted(platform_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="zh-Hant-TW">
<head>
    <meta charset="UTF-8">
    <title>2026 台灣熱門電視劇推薦與數據分析報告</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;500;700;900&display=swap');
        
        body {{
            font-family: 'Noto Sans TC', "Segoe UI", sans-serif;
            color: #334155;
            line-height: 1.6;
            margin: 40px;
            background: #fff;
        }}
        
        .header-container {{
            text-align: center;
            border-bottom: 3px double #cbd5e1;
            padding-bottom: 25px;
            margin-bottom: 40px;
        }}
        
        h1 {{
            font-size: 2.2rem;
            color: #0f172a;
            margin-bottom: 5px;
            font-weight: 900;
        }}
        
        .subtitle {{
            font-size: 1.1rem;
            color: #64748b;
            margin-bottom: 15px;
        }}
        
        .meta-info {{
            font-size: 0.9rem;
            color: #94a3b8;
        }}
        
        .section {{
            margin-bottom: 45px;
            page-break-inside: avoid;
        }}
        
        h2 {{
            font-size: 1.5rem;
            color: #1e293b;
            border-left: 5px solid #4f46e5;
            padding-left: 12px;
            margin-bottom: 20px;
            font-weight: 700;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 25px;
        }}
        
        th {{
            background-color: #f1f5f9;
            color: #1e293b;
            text-align: left;
            padding: 12px;
            font-weight: 600;
            border-bottom: 2px solid #e2e8f0;
        }}
        
        td {{
            padding: 12px;
            border-bottom: 1px solid #e2e8f0;
            font-size: 0.95rem;
        }}
        
        .rank-badge {{
            display: inline-block;
            background: #e0e7ff;
            color: #4338ca;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 0.85rem;
        }}
        
        .drama-card {{
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 25px;
            background: #fafafa;
            page-break-inside: avoid;
        }}
        
        .drama-title-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 10px;
            margin-bottom: 12px;
        }}
        
        .drama-title {{
            font-size: 1.3rem;
            color: #0f172a;
            font-weight: 700;
            margin: 0;
        }}
        
        .drama-meta {{
            font-size: 0.9rem;
            color: #64748b;
            margin-bottom: 8px;
        }}
        
        .drama-meta strong {{
            color: #334155;
        }}
        
        .drama-summary {{
            font-size: 0.95rem;
            color: #475569;
            text-align: justify;
        }}
        
        .tag-badge {{
            display: inline-block;
            background: #f1f5f9;
            color: #475569;
            padding: 1px 6px;
            border-radius: 4px;
            font-size: 0.8rem;
            margin-right: 4px;
            border: 1px solid #e2e8f0;
        }}
        
        @media print {{
            body {{
                margin: 20px;
            }}
            .drama-card {{
                background: #fff;
                border: 1px solid #cbd5e1;
            }}
        }}
    </style>
</head>
<body>

    <div class="header-container">
        <h1>2026 年台灣熱門電視劇推薦與數據分析報告</h1>
        <div class="subtitle">根據 Google 最新搜尋與各大娛樂媒體推薦之高人氣台劇整合報告</div>
        <div class="meta-info">
            報告產出時間：2026年5月 &nbsp;|&nbsp; 
            分析樣本數：{len(dramas)} 部熱門劇集 &nbsp;|&nbsp; 
            數據擷取技術：Firecrawl Web Crawler
        </div>
    </div>

    <!-- Stats Section -->
    <div class="section">
        <h2>一、 劇集類型統計排行 (Genre Frequencies)</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">排名</th>
                    <th style="width: 40%;">類型標籤</th>
                    <th style="width: 25%;">推薦劇集數量</th>
                    <th style="width: 25%;">市場佔比</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for rank, (genre, count) in enumerate(sorted_genres, 1):
        pct = (count / len(dramas)) * 100
        html_content += f"""
                <tr>
                    <td><span class="rank-badge">{rank}</span></td>
                    <td><strong>{genre}</strong></td>
                    <td>{count} 部</td>
                    <td>{pct:.1f}%</td>
                </tr>
        """
        
    html_content += """
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>二、 播出平台比重分佈 (Streaming Platforms)</h2>
        <table>
            <thead>
                <tr>
                    <th style="width: 10%;">排名</th>
                    <th style="width: 40%;">播放平台</th>
                    <th style="width: 50%;">上架劇集數量</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for rank, (platform, count) in enumerate(sorted_platforms, 1):
        html_content += f"""
                <tr>
                    <td><span class="rank-badge">{rank}</span></td>
                    <td><strong>{platform}</strong></td>
                    <td>{count} 部</td>
                </tr>
        """
        
    html_content += f"""
            </tbody>
        </table>
    </div>

    <div style="page-break-after: always;"></div>

    <!-- Drama list details -->
    <div class="section">
        <h2>三、 推薦劇集詳細清單 (Recommended Dramas Index)</h2>
    """
    
    for d in dramas:
        genres = [g.strip() for g in d.get("genre", "").split("、")]
        genres_html = "".join([f'<span class="tag-badge">{g}</span>' for g in genres])
        
        html_content += f"""
        <div class="drama-card">
            <div class="drama-title-row">
                <div class="drama-title">《{d.get("title", "")}》</div>
                <div>{genres_html}</div>
            </div>
            <div class="drama-meta"><strong>主演卡司：</strong>{d.get("cast", "")}</div>
            <div class="drama-meta"><strong>播放平台：</strong>{d.get("platform", "")} &nbsp;|&nbsp; <strong>預計播出：</strong>{d.get("release_date", "2026")} 年</div>
            <div class="drama-summary" style="margin-top: 10px;">
                <strong>故事簡介：</strong>{d.get("summary", "")}
            </div>
        </div>
        """
        
    html_content += """
    </div>

</body>
</html>
    """
    
    # Save template HTML
    template_path = os.path.join(output_dir, "pdf_template.html")
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    # PDF Output Path
    pdf_path = os.path.join(output_dir, "2026_taiwan_dramas_report.pdf")
    
    # Execute MS Edge to print to PDF
    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    command = [
        edge_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        template_path
    ]
    
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True)
    if result.returncode == 0 and os.path.exists(pdf_path):
        print(f"PDF generated successfully at: {pdf_path}")
    else:
        print("Failed to generate PDF.")
        print(f"Stderr: {result.stderr.decode('utf-8', errors='ignore')}")

if __name__ == "__main__":
    main()
