import json
import os
import jieba
from snownlp import SnowNLP
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def main():
    workspace = r"c:\Users\user\Desktop\web"
    input_file = os.path.join(workspace, "dcard_parsed.json")
    output_json = os.path.join(workspace, "dcard_sentiment.json")
    assets_dir = os.path.join(workspace, "assets")
    output_wc = os.path.join(assets_dir, "wordcloud.png")
    
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
        
    with open(input_file, "r", encoding="utf-8") as f:
        posts = json.load(f)
        
    all_text = ""
    sentiment_results = []
    
    pos_count = 0
    neu_count = 0
    neg_count = 0
    
    for post in posts:
        title = post.get("title", "")
        snippet = post.get("snippet", "")
        text = f"{title} {snippet}"
        all_text += text + " "
        
        # Calculate Sentiment
        try:
            s = SnowNLP(text)
            score = s.sentiments
        except:
            score = 0.5
            
        if score > 0.6:
            label = "Positive"
            pos_count += 1
        elif score < 0.4:
            label = "Negative"
            neg_count += 1
        else:
            label = "Neutral"
            neu_count += 1
            
        sentiment_results.append({
            "title": title,
            "author": post.get("author", "Unknown"),
            "time": post.get("time", "Unknown"),
            "snippet": snippet,
            "sentiment_score": round(score, 3),
            "label": label
        })
        
    # Sort by sentiment score (descending)
    sentiment_results.sort(key=lambda x: x["sentiment_score"], reverse=True)
    
    analysis_data = {
        "stats": {
            "positive": pos_count,
            "neutral": neu_count,
            "negative": neg_count,
            "total": len(posts)
        },
        "posts": sentiment_results
    }
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(analysis_data, f, ensure_ascii=False, indent=2)
        
    print("Sentiment analysis completed and saved.")
    
    # Generate Word Cloud
    print("Generating Word Cloud...")
    jieba.setLogLevel(20) # Hide warnings
    
    # Custom stopwords
    stopwords = set(["的", "了", "和", "是", "就", "都", "而", "及", "與", "著", "這", "那", "有", "我", "你", "他", "在", "也", "不", "人", "什麼", "這個", "可以", "覺得", "大家", "因為", "不過", "很多", "一直", "自己", "最近", "真的", "然後"])
    
    words = jieba.cut(all_text)
    filtered_words = [w for w in words if w not in stopwords and len(w) > 1]
    text_for_wc = " ".join(filtered_words)
    
    font_path = r"C:\Windows\Fonts\msjh.ttc"
    if not os.path.exists(font_path):
        font_path = None # Fallback to default
        
    wc = WordCloud(
        font_path=font_path,
        background_color="#020617", # Match website background
        width=800,
        height=400,
        max_words=100,
        colormap="Pastel1", # Nice aesthetic pastel colors
        contour_width=0
    )
    
    wc.generate(text_for_wc)
    wc.to_file(output_wc)
    print("Word Cloud generated and saved to assets/wordcloud.png")

if __name__ == "__main__":
    main()
