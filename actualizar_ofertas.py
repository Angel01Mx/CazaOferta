import urllib.request
import json

AFILIADO_TAG = "TU_TAG_AQUI" 
URL_API = "https://api.mercadolibre.com/sites/MLM/search?q=ofertas&limit=12"

def obtener_ofertas():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(URL_API, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('results', [])
    except Exception as e:
        print(f"Error al obtener ofertas: {e}")
        return []

def generar_html(productos):
    cards_html = ""
    for prod in productos:
        titulo = prod.get('title', 'Producto sin nombre')
        precio = prod.get('price', 0)
        precio_original = prod.get('original_price', precio)
        imagen = prod.get('thumbnail', '').replace("http://", "https://")
        link_original = prod.get('permalink', '#')
        
        link_afiliado = f"{link_original}?matt_tool=12345678&matt_word={AFILIADO_TAG}" if AFILIADO_TAG != "TU_TAG_AQUI" else link_original
        
        descuento = ""
        if precio_original and precio_original > precio:
            porcentaje = int(((precio_original - precio) / precio_original) * 100)
            descuento = f'<span style="background:red;color:white;padding:2px 6px;border-radius:4px;">-{porcentaje}%</span>'

        cards_html += f'''
        <div style="border:1px solid #ddd; border-radius:8px; padding:15px; margin:10px; width:250px; display:inline-block; vertical-align:top; background:#fff; text-align:center;">
            <img src="{imagen}" alt="{titulo}" style="max-width:100%; height:150px; object-fit:contain;"><br>
            <h4 style="font-size:14px; height:40px; overflow:hidden;">{titulo}</h4>
            <p><s style="color:#888;">${precio_original:,.2f}</s> <b>${precio:,.2f}</b> {descuento}</p>
            <a href="{link_afiliado}" target="_blank" style="background:#00a650; color:white; padding:10px 15px; text-decoration:none; border-radius:5px; display:inline-block;">Ver Oferta</a>
        </div>
        '''

    html_completo = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CazaOferta - Las Mejores Ofertas del Día</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #f5f5f5; margin:0; padding:20px; text-align:center; }}
        header {{ background: #fff159; padding: 20px; border-radius: 8px; margin-bottom: 20px; }}
        .contenedor {{ display: flex; flex-wrap: wrap; justify-content: center; }}
    </style>
</head>
<body>
    <header>
        <h1>🦊 CazaOferta</h1>
        <p>Ofertas automáticas actualizadas de Mercado Libre</p>
    </header>
    <div class="contenedor">
        {cards_html}
    </div>
</body>
</html>'''

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_completo)

if __name__ == "__main__":
    productos = obtener_ofertas()
    generar_html(productos)
