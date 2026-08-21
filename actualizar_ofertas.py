import urllib.request
import json

AFILIADO_TAG = "TU_TAG_AQUI" 
URL_API = "https://api.mercadolibre.com/sites/MLM/search?q=ofertas&limit=10"

# Plantilla idéntica a tu Versión 4
HTML_PLANTILLA = '''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CazaOferta V4</title>
<style>
:root{{--bg:#f6f7fb;--ink:#18202d;--muted:#697386;--line:#e5e8ef;--accent:#f6aa00;--dark:#111827}}*{{box-sizing:border-box}}body{{margin:0;font-family:Arial,sans-serif;background:var(--bg);color:var(--ink)}}header{{position:sticky;top:0;background:#fff;border-bottom:1px solid var(--line);z-index:5}}.nav{{max-width:1200px;margin:auto;padding:15px 22px;display:flex;justify-content:space-between}}.logo{{font-size:26px;font-weight:900}}.logo b{{color:#d88b00}}.hero{{background:linear-gradient(135deg,#101827,#26354d);color:white}}.heroIn{{max-width:1200px;margin:auto;padding:65px 22px;text-align:center}}h1{{font-size:clamp(38px,6vw,64px);margin:18px auto;max-width:850px}}.hero p{{max-width:680px;margin:auto;color:#cbd5e1;font-size:18px;line-height:1.5}}.pill{{display:inline-block;padding:8px 13px;border-radius:999px;background:#ffffff18;color:#ffe3a0;font-size:12px;font-weight:bold}}.search{{max-width:760px;margin:30px auto 0;background:white;padding:7px;border-radius:17px;display:flex}}.search input{{flex:1;border:0;outline:0;padding:14px;font-size:16px}}.search button{{border:0;background:var(--accent);border-radius:12px;padding:0 24px;font-weight:bold}}main{{max-width:1200px;margin:auto;padding:42px 22px 60px}}.head{{display:flex;justify-content:space-between;align-items:end}}h2{{font-size:30px;margin:6px 0}}.eyebrow{{font-size:12px;color:#b66d00;font-weight:bold;text-transform:uppercase}}#count{{color:var(--muted)}}.filters{{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0}}.filter{{background:white;border:1px solid var(--line);border-radius:999px;padding:9px 14px;font-weight:bold;cursor:pointer}}.filter.active{{background:var(--dark);color:white}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(245px,1fr));gap:18px}}.card{{background:white;border:1px solid var(--line);border-radius:22px;overflow:hidden;display:flex;flex-direction:column}}.visual{{height:155px;display:grid;place-items:center;font-size:70px;background:linear-gradient(135deg,#edf1ff,#fff)}}.body{{padding:17px;display:flex;flex-direction:column;flex:1}}.meta{{display:flex;justify-content:space-between;font-size:11px;text-transform:uppercase;color:#7b8492}}.meta b{{background:#fff4d7;color:#865300;padding:6px 8px;border-radius:999px;text-transform:none}}h3{{font-size:18px;margin:13px 0 7px}}.body p{{font-size:13px;color:var(--muted);line-height:1.45;min-height:38px}}.signals{{display:flex;gap:7px;flex-wrap:wrap;margin:12px 0}}.signals span{{background:#f3f5f7;padding:7px 8px;border-radius:8px;font-size:12px;font-weight:bold}}.signals .hot{{background:#eaf8f0;color:#087443}}.body a{{margin-top:auto;text-align:center;background:var(--dark);color:white;text-decoration:none;padding:13px;border-radius:12px;font-weight:bold}}small{{font-size:10px;color:#929baa;margin-top:9px}}.how{{margin-top:55px;background:white;border:1px solid var(--line);border-radius:25px;padding:30px}}.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}.step{{background:#f8fafc;padding:18px;border-radius:16px}}.num{{width:31px;height:31px;border-radius:50%;background:var(--accent);display:grid;place-items:center;font-weight:bold;margin-bottom:10px}}footer{{background:var(--dark);color:#9ca7b8;padding:38px 22px;font-size:12px}}.foot{{max-width:1200px;margin:auto;line-height:1.6}}.foot strong{{color:white;font-size:15px}}@media(max-width:700px){{.steps{{grid-template-columns:1fr 1fr}}.head{{flex-direction:column;align-items:start;gap:5px}}}}@media(max-width:430px){{.steps{{grid-template-columns:1fr}}}}
</style></head><body>
<header><div class="nav"><div class="logo">🦊 Caza<b>Oferta</b></div><div>{total_items} productos</div></div></header>
<section class="hero"><div class="heroIn"><div class="pill">CAZAOFERTA V4 · SELECCIÓN INICIAL</div><h1>Encuentra algo que valga la pena revisar.</h1><p>Productos seleccionados por señales de demanda y potencial de oportunidad. Tú verificas los detalles y decides.</p><div class="search"><input id="q" placeholder="Busca audífonos, cámara, tablet, gaming..." oninput="apply()"><button onclick="apply()">Buscar</button></div></div></section>
<main><div class="head"><div><div class="eyebrow">{total_items} enlaces reales integrados</div><h2>🔥 Productos seleccionados</h2></div><div id="count">{total_items} productos</div></div>
<div class="filters" id="filters"><button class="filter active" data-f="todos">Todos</button><button class="filter" data-f="audio">🎧 Audio</button><button class="filter" data-f="wearables">⌚ Wearables</button><button class="filter" data-f="seguridad">📷 Seguridad</button><button class="filter" data-f="energía">🔋 Energía</button><button class="filter" data-f="accesorios">📱 Accesorios</button><button class="filter" data-f="tablets">📲 Tablets</button><button class="filter" data-f="gaming">🎮 Gaming</button></div>
<div class="grid" id="grid">
{cards_content}
</div>
<section class="how"><h2>¿Cómo funciona CazaOferta?</h2><div class="steps"><div class="step"><div class="num">1</div><b>Seleccionamos</b><p>Buscamos señales de interés y demanda.</p></div><div class="step"><div class="num">2</div><b>Organizamos</b><p>Facilitamos explorar categorías y productos.</p></div><div class="step"><div class="num">3</div><b>Puntuamos</b><p>El índice es una referencia interna, no una garantía.</p></div><div class="step"><div class="num">4</div><b>Tú decides</b><p>Verificas precio y condiciones en la publicación.</p></div></div></section></main>
<footer><div class="foot"><strong>🦊 CazaOferta</strong><br>Proyecto independiente. Algunos enlaces pueden generar una comisión para CazaOferta sin costo adicional para el usuario. Los precios, promociones y disponibilidad pueden cambiar; verifica siempre la información final antes de comprar.</div></footer>
<script>
let cat='todos';const fs=document.querySelectorAll('.filter');fs.forEach(b=>b.onclick=()=>{fs.forEach(x=>x.classList.remove('active'));b.classList.add('active');cat=b.dataset.f;apply();});
function apply(){{let q=document.getElementById('q').value.toLowerCase().trim(),n=0;document.querySelectorAll('.card').forEach(c=>{{let ok=(cat==='todos'||c.dataset.cat===cat)&&(!q||c.dataset.search.includes(q));c.style.display=ok?'flex':'none';if(ok)n++;}});document.getElementById('count').textContent=n+' producto'+(n===1?'':'s');}}
</script></body></html>'''

# Lista V4 con tus 10 enlaces reales
PRODUCTOS_V4 = [
    {"cat": "audio", "icon": "🎧", "title": "Xiaomi Redmi Buds 6 Play", "score": "92/100", "tag": "🔥 Alta demanda", "search": "xiaomi redmi buds 6 play audio alta demanda", "link": "https://meli.la/2dxgimX"},
    {"cat": "audio", "icon": "🎧", "title": "1Hora AUT205", "score": "89/100", "tag": "🔥 Alta demanda", "search": "1hora aut205 audio alta demanda", "link": "https://meli.la/2FtFhvh"},
    {"cat": "audio", "icon": "🎶", "title": "Sony WH-CH520", "score": "87/100", "tag": "🔥 Alta demanda", "search": "sony wh-ch520 audio alta demanda", "link": "https://meli.la/2XQV37A"},
    {"cat": "wearables", "icon": "⌚", "title": "Xiaomi Redmi Watch 5 Active", "score": "90/100", "tag": "🔥 Alta demanda", "search": "xiaomi redmi watch 5 active wearables alta demanda", "link": "https://meli.la/2VsM6PP"},
    {"cat": "seguridad", "icon": "📷", "title": "Cámara WiFi 360°", "score": "91/100", "tag": "🔥 Muy buscado", "search": "cámara wifi 360° seguridad muy buscado", "link": "https://meli.la/1pbjott"},
    {"cat": "energía", "icon": "🔋", "title": "Power Bank 1HORA 10,000 mAh", "score": "94/100", "tag": "🔥 Alta demanda", "search": "power bank 1hora 10,000 mah energía alta demanda", "link": "https://meli.la/2wP2VJL"},
    {"cat": "accesorios", "icon": "🔌", "title": "Cargador rápido 35W", "score": "91/100", "tag": "🔥 Compra impulsiva", "search": "cargador rápido 35w accesorios compra impulsiva", "link": "https://meli.la/1cvPPRF"},
    {"cat": "accesorios", "icon": "📱", "title": "Kit funda MagSafe + micas", "score": "88/100", "tag": "🔥 Precio accesible", "search": "kit funda magsafe + micas accesorios precio accesible", "link": "https://meli.la/1CaCvxN"},
    {"cat": "tablets", "icon": "📲", "title": "Samsung Galaxy Tab A11 128 GB", "score": "86/100", "tag": "🔥 Ticket alto", "search": "samsung galaxy tab a11 128 gb tablets ticket alto", "link": "https://meli.la/2iGHmkR"},
    {"cat": "gaming", "icon": "🎮", "title": "Soporte PS5 + base para control", "score": "82/100", "tag": "🔥 Nicho gaming", "search": "soporte ps5 + base para control gaming nicho gaming", "link": "https://meli.la/2dULAfw"}
]

def generar_sitio():
    cards_html = ""
    for item in PRODUCTOS_V4:
        cat_capitalizada = item['cat'].capitalize()
        cards_html += f'''<article class="card" data-cat="{item['cat']}" data-search="{item['search']}">
<div class="visual">{item['icon']}</div><div class="body"><div class="meta"><span>{cat_capitalizada}</span><b>🦊 {item['score']}</b></div>
<h3>{item['title']}</h3><p>Producto seleccionado para nuestra primera colección de oportunidades.</p>
<div class="signals"><span class="hot">{item['tag']}</span><span>⭐ Seleccionado</span></div>
<a href="{item['link']}" target="_blank" rel="nofollow sponsored noopener">🛒 Ver oferta</a>
<small>Precio y disponibilidad pueden cambiar. Verifica la publicación antes de comprar.</small></div></article>\n'''

    html_final = HTML_PLANTILLA.format(
        total_items=len(PRODUCTOS_V4),
        cards_content=cards_html
    )

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_final)

if __name__ == "__main__":
    generar_sitio()
