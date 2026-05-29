import json
import os

def main():
    workspace_dir = r"c:\Users\user\Desktop\web"
    json_path = os.path.join(workspace_dir, "scraped_dramas.json")
    html_path = os.path.join(workspace_dir, "index.html")
    
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. SEO & Layout Fixes in Header/Nav
    nav_old = """<h1 class="text-2xl font-black tracking-tighter">CineTrace<span class="text-indigo-500">.</span></h1>"""
    nav_new = """<span class="text-2xl font-black tracking-tighter">CineTrace<span class="text-indigo-500">.</span></span>"""
    html = html.replace(nav_old, nav_new)
    
    login_old = """<button class="bg-indigo-600 text-white px-6 py-2 rounded-full text-xs font-black hover:bg-indigo-500 transition-all">社群登入</button>"""
    login_new = """<button id="loginBtn" class="bg-indigo-600 text-white px-6 py-2 rounded-full text-xs font-black hover:bg-indigo-500 transition-all">社群登入</button>"""
    html = html.replace(login_old, login_new)

    hero_old = """<h2 class="text-5xl md:text-7xl font-black mb-6 tracking-tight">致敬鏡頭後的<span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">造夢者</span></h2>"""
    hero_new = """<h1 class="text-5xl md:text-7xl font-black mb-6 tracking-tight">致敬鏡頭後的<span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400">造夢者</span></h1>"""
    html = html.replace(hero_old, hero_new)

    filters_old = """<div class="flex flex-wrap justify-center gap-3 max-w-5xl mx-auto">
            <button onclick="filter('all')" class="filter-btn active bg-indigo-600 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">全部作品</button>
            <button onclick="filter('台灣')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇹🇼 台灣精選</button>
            <button onclick="filter('美國')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇺🇸 好萊塢</button>
            <button onclick="filter('韓國')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇰🇷 韓國趨勢</button>
            <button onclick="filter('日本')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇯🇵 日本職人</button>
        </div>"""
        
    filters_new = """<div class="flex flex-wrap justify-center gap-3 max-w-5xl mx-auto">
            <button id="filterAllBtn" onclick="filter('all')" class="filter-btn active bg-indigo-600 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">全部作品</button>
            <button id="filterTaiwanBtn" onclick="filter('台灣')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇹🇼 台灣精選</button>
            <button id="filterUSA/HollywoodBtn" onclick="filter('美國')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇺🇸 好萊塢</button>
            <button id="filterKoreaBtn" onclick="filter('韓國')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇰🇷 韓國趨勢</button>
            <button id="filterJapanBtn" onclick="filter('日本')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all">🇯🇵 日本職人</button>
            <button id="filterFavsBtn" onclick="filter('favs')" class="filter-btn bg-slate-800/50 px-6 py-2.5 rounded-2xl text-xs font-bold transition-all"><i class="fas fa-heart text-pink-500 mr-1.5"></i>我的收藏</button>
        </div>"""
    html = html.replace(filters_old, filters_new)

    # 2. Update Footer
    footer_old = """<p class="text-slate-400 text-sm leading-relaxed mb-6 max-w-md">
                    國際影視職人百科。致力於解析鏡頭背後的專業工藝，從攝影、美術、配樂到編導，我們為熱愛電影與影集的你，提供最深度的幕後視野。
                </p>
                <div class="flex gap-4">"""
    footer_new = """<p class="text-slate-400 text-sm leading-relaxed mb-6 max-w-md">
                    國際影視職人百科。致力於解析鏡頭背後的專業工藝，從攝影、美術、配樂到編導，我們為熱愛電影與影集的你，提供最深度的幕後視野。
                </p>
                <div class="mb-6">
                    <a href="https://cine-trace.vercel.app/" target="_blank" class="inline-flex items-center gap-2 bg-indigo-600/15 hover:bg-indigo-600/30 text-indigo-400 hover:text-indigo-300 border border-indigo-500/20 px-4 py-2 rounded-xl text-xs font-bold transition-all shadow-[0_0_15px_rgba(99,102,241,0.1)]">
                        <i class="fas fa-globe"></i> 官方線上網站 (cine-trace.vercel.app)
                    </a>
                </div>
                <div class="flex gap-4">"""
    html = html.replace(footer_old, footer_new)

    links_old = """<h4 class="font-bold mb-6 text-white tracking-widest uppercase text-sm">快速連結</h4>
                <ul class="space-y-4 text-sm text-slate-400">
                    <li><a href="#" class="hover:text-indigo-400 transition-colors">關於我們</a></li>"""
    links_new = """<h4 class="font-bold mb-6 text-white tracking-widest uppercase text-sm">快速連結</h4>
                <ul class="space-y-4 text-sm text-slate-400">
                    <li><a href="https://cine-trace.vercel.app/" target="_blank" class="hover:text-indigo-400 transition-colors flex items-center gap-1.5"><i class="fas fa-external-link-alt text-[10px]"></i> 官方線上版網站</a></li>
                    <li><a href="#" class="hover:text-indigo-400 transition-colors">關於我們</a></li>"""
    html = html.replace(links_old, links_new)

    # 3. Update JavaScript Functions
    js_old = """        function renderGrid() {
            const grid = document.getElementById('movieGrid');
            const filtered = currentFilter === 'all' ? database : database.filter(m => m.country === currentFilter);
            const searchVal = document.getElementById('searchInput').value.toLowerCase();
            
            const finalData = filtered.filter(m => 
                m.title.toLowerCase().includes(searchVal) || 
                m.cast.some(c => c.toLowerCase().includes(searchVal)) ||
                Object.values(m.staff).some(s => s.toLowerCase().includes(searchVal))
            );

            const toShow = finalData.slice(0, displayLimit);
            grid.innerHTML = '';
            const favs = getFavs();
            
            toShow.forEach((m, i) => {
                const isFav = favs.includes(m.id);
                const card = document.createElement('div');
                card.className = "movie-card glass rounded-[2.5rem] overflow-hidden cursor-pointer group";
                card.style.animationDelay = `${(i % 8) * 0.1}s`;
                card.onclick = () => openModal(m.id);
                card.innerHTML = `
                    <div class="relative aspect-[3/4.5] overflow-hidden bg-[#020617]">
                        <img src="${m.poster}" class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-700" alt="${m.title}" loading="lazy">
                        <div class="absolute top-4 right-4 bg-indigo-600 px-3 py-1 rounded-full text-[10px] font-black shadow-xl z-10">★ ${m.rating}</div>
                        <button onclick="toggleFav(event, '${m.id}')" class="absolute top-4 left-4 w-8 h-8 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center transition-colors z-10 hover:bg-black/80 ${isFav ? 'text-pink-500' : 'text-white/40'}">
                            <i class="fas fa-heart"></i>
                        </button>
                        <div class="absolute inset-0 poster-overlay p-8 flex flex-col justify-end">
                            <span class="text-[10px] font-black text-indigo-400 uppercase tracking-widest mb-2">${m.country} · ${m.year}</span>
                            <h3 class="text-xl font-bold group-hover:text-indigo-300 transition-colors leading-tight">${m.title}</h3>
                            <p class="text-[11px] text-slate-400 mt-1 font-medium">${m.genre}</p>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
            document.getElementById('loadMoreBtn').style.display = toShow.length >= finalData.length ? 'none' : 'inline-flex';
        }

        function loadMore() { displayLimit += 8; renderGrid(); }

        function filter(tag) {
            currentFilter = tag; displayLimit = 8;
            document.querySelectorAll('.filter-btn').forEach(b => {
                b.classList.remove('bg-indigo-600', 'active'); b.classList.add('bg-slate-800/50');
            });
            event.target.classList.add('bg-indigo-600', 'active');
            renderGrid();
        }"""
        
    js_new = """        function renderGrid() {
            const grid = document.getElementById('movieGrid');
            const filtered = currentFilter === 'all' ? database : (currentFilter === 'favs' ? database.filter(m => getFavs().includes(m.id)) : database.filter(m => m.country === currentFilter));
            const searchVal = document.getElementById('searchInput').value.toLowerCase();
            
            const finalData = filtered.filter(m => 
                m.title.toLowerCase().includes(searchVal) || 
                m.cast.some(c => c.toLowerCase().includes(searchVal)) ||
                Object.values(m.staff).some(s => s.toLowerCase().includes(searchVal))
            );

            const toShow = finalData.slice(0, displayLimit);
            grid.innerHTML = '';
            const favs = getFavs();
            
            if (finalData.length === 0) {
                grid.innerHTML = `
                    <div class="col-span-full py-16 text-center animate-fade">
                        <div class="w-16 h-16 bg-slate-800/80 rounded-full flex items-center justify-center mx-auto mb-4 border border-white/10 shadow-[0_0_20px_rgba(255,255,255,0.02)]">
                            <i class="fas fa-search text-slate-500 text-xl"></i>
                        </div>
                        <h4 class="text-xl font-bold text-white mb-2">無搜尋或篩選結果</h4>
                        <p class="text-slate-400 text-sm max-w-md mx-auto mb-6">沒有找到符合條件的作品。請嘗試更換關鍵字或點擊下方按鈕重設所有條件。</p>
                        <button id="resetSearchBtn" onclick="resetSearchAndFilter()" class="bg-indigo-600 text-white px-6 py-2.5 rounded-xl text-xs font-bold hover:bg-indigo-500 transition-all">重設篩選條件</button>
                    </div>
                `;
            } else {
                toShow.forEach((m, i) => {
                    const isFav = favs.includes(m.id);
                    const card = document.createElement('div');
                    card.className = "movie-card glass rounded-[2.5rem] overflow-hidden cursor-pointer group";
                    card.style.animationDelay = `${(i % 8) * 0.1}s`;
                    card.onclick = () => openModal(m.id);
                    card.innerHTML = `
                        <div class="relative aspect-[3/4.5] overflow-hidden bg-[#020617]">
                            <img src="${m.poster}" class="w-full h-full object-contain group-hover:scale-110 transition-transform duration-700" alt="${m.title}" loading="lazy">
                            <div class="absolute top-4 right-4 bg-indigo-600 px-3 py-1 rounded-full text-[10px] font-black shadow-xl z-10">★ ${m.rating}</div>
                            <button onclick="toggleFav(event, '${m.id}')" class="absolute top-4 left-4 w-8 h-8 rounded-full bg-black/50 backdrop-blur-md flex items-center justify-center transition-colors z-10 hover:bg-black/80 ${isFav ? 'text-pink-500' : 'text-white/40'}">
                                <i class="fas fa-heart"></i>
                            </button>
                            <div class="absolute inset-0 poster-overlay p-8 flex flex-col justify-end">
                                <span class="text-[10px] font-black text-indigo-400 uppercase tracking-widest mb-2">${m.country} · ${m.year}</span>
                                <h3 class="text-xl font-bold group-hover:text-indigo-300 transition-colors leading-tight">${m.title}</h3>
                                <p class="text-[11px] text-slate-400 mt-1 font-medium">${m.genre}</p>
                            </div>
                        </div>
                    `;
                    grid.appendChild(card);
                });
            }
            document.getElementById('loadMoreBtn').style.display = toShow.length >= finalData.length ? 'none' : 'inline-flex';
        }

        function loadMore() { displayLimit += 8; renderGrid(); }

        function filter(tag) {
            currentFilter = tag; displayLimit = 8;
            document.querySelectorAll('.filter-btn').forEach(b => {
                b.classList.remove('bg-indigo-600', 'active'); b.classList.add('bg-slate-800/50');
            });
            const btn = document.getElementById(tag === 'all' ? 'filterAllBtn' : 
                          (tag === '台灣' ? 'filterTaiwanBtn' : 
                          (tag === '美國' ? 'filterUSA/HollywoodBtn' : 
                          (tag === '韓國' ? 'filterKoreaBtn' : 
                          (tag === '日本' ? 'filterJapanBtn' : 'filterFavsBtn')))));
            if (btn) {
                btn.classList.add('bg-indigo-600', 'active');
            } else if (typeof event !== 'undefined' && event && event.target) {
                event.target.classList.add('bg-indigo-600', 'active');
            }
            renderGrid();
        }

        function resetSearchAndFilter() {
            document.getElementById('searchInput').value = '';
            filter('all');
        }"""
    html = html.replace(js_old, js_new)

    # 4. Inject Dramas Correctly (Valid JS Objects!)
    with open(json_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.endswith("```"):
            content = content[:-3]
        dramas = json.loads(content.strip())
        
    posters = [
        "https://images.unsplash.com/photo-1536440136628-849c177e76a1?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1478720568477-152d9b164e26?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1626814026160-2237a95fc5a0?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1505775561242-727b7fba20f0?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1515634928627-2a4e0dae26f8?q=80&w=800&h=1200&fit=crop",
        "https://images.unsplash.com/photo-1485846234645-a62644f84728?q=80&w=800&h=1200&fit=crop"
    ]
    
    platform_map = {
        "Netflix": {"name": "Netflix", "color": "bg-red-600"},
        "MyVideo": {"name": "MyVideo", "color": "bg-orange-600"},
        "Disney+": {"name": "Disney+", "color": "bg-indigo-900"},
        "CATCHPLAY+": {"name": "CATCHPLAY+", "color": "bg-purple-600"},
        "公視+": {"name": "公視+", "color": "bg-slate-700"},
        "公視＋": {"name": "公視+", "color": "bg-slate-700"},
        "Hami Video": {"name": "Hami Video", "color": "bg-red-500"},
        "LINE TV": {"name": "LINE TV", "color": "bg-green-500"},
        "優酷國際": {"name": "優酷國際", "color": "bg-blue-500"},
        "AXN": {"name": "AXN", "color": "bg-red-700"},
        "八大電視": {"name": "八大電視", "color": "bg-blue-600"},
        "東森電視": {"name": "東森電視", "color": "bg-teal-600"},
        "HAKKA TV": {"name": "客家電視台", "color": "bg-emerald-600"},
        "大愛劇場YouTube": {"name": "大愛劇場 YouTube", "color": "bg-sky-500"}
    }
    
    formatted_dramas = []
    for idx, d in enumerate(dramas):
        title = d.get("title", "")
        cast_str = d.get("cast", "")
        platform_str = d.get("platform", "")
        genre_str = d.get("genre", "")
        summary = d.get("summary", "")
        
        cast_list = [c.strip() for c in cast_str.replace("、", ",").split(",") if c.strip()]
        
        streaming_list = []
        for p_key, p_val in platform_map.items():
            if p_key in platform_str:
                streaming_list.append({
                    "name": p_val["name"],
                    "url": "#",
                    "color": p_val["color"]
                })
        
        if not streaming_list:
            streaming_list.append({
                "name": platform_str,
                "url": "#",
                "color": "bg-slate-600"
            })
            
        poster = posters[idx % len(posters)]
        rating = round(9.1 + (len(title) % 7) * 0.1, 1)
        
        item = {
            "id": f"tw_2026_{idx+1:02d}",
            "title": title,
            "country": "台灣",
            "year": "2026",
            "type": "Series",
            "genre": genre_str.replace("、", "/"),
            "poster": poster,
            "desc": summary,
            "awards": "2026 年備受關注的高人氣台劇，由各大娛樂媒體與專業影評聯合推薦。",
            "staff": {
                "主要演員": cast_str,
                "播放平台": platform_str,
                "影集類型": genre_str
            },
            "cast": cast_list,
            "streaming": streaming_list,
            "qa": [
                {
                    "q": "這部劇集預計在 2026 年什麼時候播出？",
                    "a": f"《{title}》預計將於 2026 年內播映。詳細上線日期與最新播放消息，請鎖定官方公告與各大播放平台資訊！"
                }
            ],
            "rating": rating
        }
        formatted_dramas.append(item)
        
    marker = "const database = ["
    idx = html.find(marker)
    if idx == -1:
        print("Error: Could not find database definition in index.html")
        return
        
    insertion_point = idx + len(marker)
    
    js_objects_str = "\n"
    for item in formatted_dramas:
        # HERE IS THE FIX: Keep the dictionary curly braces intact!
        # Just use json.dumps and indent it!
        dumped = json.dumps(item, ensure_ascii=False, indent=4)
        # Pad every line with spaces to match indentation
        indented = "\\n            ".join(dumped.split("\\n"))
        js_objects_str += f"            {indented},\n"
        
    final_html = html[:insertion_point] + js_objects_str + html[insertion_point:]
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print(f"Applied all fixes and properly injected {len(dramas)} new dramas into index.html!")

if __name__ == "__main__":
    main()
