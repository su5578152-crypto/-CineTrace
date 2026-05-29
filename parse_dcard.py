import re
import json

def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    posts = []
    current_post = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Match post titles like "## \#情報 主題講座｜..." or "## JJ悄悄刪掉..."
        if line.startswith("## "):
            title = line[3:].strip()
            
            # The author and time usually appear in the previous few lines, e.g., "國立臺中科技大學 企業管理學系[Just now](...)"
            # Let's search upwards up to 5 lines for the author and time info
            author_info = "Unknown"
            time_info = "Unknown"
            for j in range(1, 6):
                if i - j >= 0:
                    prev_line = lines[i - j].strip()
                    # e.g., "淡江大學[7h](https://...)" or "Securities Broker[12h](https://...)"
                    match = re.search(r'^(.*?)\[(.*?)\]\(https://www\.dcard\.tw/f/entertainer/p/\d+\)', prev_line)
                    if match:
                        author_info = match.group(1).strip()
                        time_info = match.group(2).strip()
                        break
                        
            # The snippet is usually the lines immediately following the title that are not empty and not images
            snippet = ""
            for j in range(1, 10):
                if i + j < len(lines):
                    next_line = lines[i + j].strip()
                    if next_line and not next_line.startswith("!") and not next_line.startswith("## ") and not next_line.startswith("["):
                        snippet = next_line
                        break
                        
            current_post = {
                "title": title,
                "author": author_info,
                "time": time_info,
                "snippet": snippet[:100] + "..." if len(snippet) > 100 else snippet
            }
            posts.append(current_post)
            
            if len(posts) >= 30:
                break
                
    return posts

posts = parse_markdown(r"c:\Users\user\Desktop\web\dcard_raw.md")

with open(r"c:\Users\user\Desktop\web\dcard_parsed.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, ensure_ascii=False, indent=2)

print(f"Parsed {len(posts)} posts successfully.")
