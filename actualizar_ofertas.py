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

    with open('plantilla.html', 'r', encoding='utf-8') as f:
        contenido_base = f.read()

    html_final = contenido_base.replace('<!--PRODUCTOS_AQUI-->', cards_html)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_final)

if __name__ == "__main__":
    generar_sitio()
