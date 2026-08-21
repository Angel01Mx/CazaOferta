import urllib.request
import json

AFILIADO_TAG = "TU_TAG_AQUI" 
# Búsqueda directa de productos populares en México
URL_API = "https://api.mercadolibre.com/sites/MLM/search?q=laptops%20celulares%20audifonos&limit=12"

def obtener_ofertas():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(URL_API, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            resultados = data.get('results', [])
            if resultados:
                return resultados
    except Exception as e:
        print(f"Error al conectar con la API: {e}")
    
    # Productos de respaldo por si la API no devuelve respuesta inmediata
    return [
        {"title": "Audífonos Inalámbricos Bluetooth", "price": 399, "original_price": 699, "thumbnail": "https://http2.mlstatic.com/D_658325-MLA46516512345_062021-I.jpg", "permalink": "https://www.mercadolibre.com.mx"},
        {"title": "Smartwatch Reloj Inteligente", "price": 549, "original_price": 899, "thumbnail": "https://http2.mlstatic.com/D_658325-MLA46516512345_062021-I.jpg", "permalink": "https://www.mercadolibre.com.mx"},
        {"title": "Laptop 14 Pulgadas SSD 256GB", "price": 4999, "original_price": 7200, "thumbnail": "https://http2.mlstatic.com/D_658325-MLA46516512345_062021-I.jpg", "permalink": "https://www.mercadolibre.com.mx"}
    ]

def generar_html(productos):
    cards_html = ""
    for prod in productos:
        titulo = prod.get('title', 'Producto en Oferta')
        precio = prod.get('price', 0)
        precio_original = prod.get('original_price') or precio
        imagen = prod.get('thumbnail', '').replace("http://", "https://")
        link_original = prod.get('permalink', 'https://www.mercadolibre.com.mx')
        
        link_afiliado = f"{link_original}?matt_tool=12345678&matt_word={AFILIADO_TAG}" if AFILIADO_TAG != "TU_TAG_AQUI" else link_original
        
        descuento = ""
        if precio_original and precio_original > precio:
            porcentaje = int(((precio_original - precio) / precio_original) * 100)
            descuento = f'<span style="background:#e60000;color:white;padding:3px 7px;border-radius:4px;font-weight:bold;font-size:12px;">-{porcentaje}%</span>'

        cards_html += f'''
        <div style="border:1px solid #e0e0e0; border-radius:10px; padding:15px; margin:12px; width:240px; display:inline-block; vertical-align:top; background:#fff; text-align:center; box-shadow:0 2px 5px rgba(0,0,0,0.05);">
            <img src="{imagen}" alt="{titulo}" style="max-width:100%; height:140px; object-fit:contain; margin-bottom:10px;"><br>
            <h4 style="font-size:14px; height:38px; overflow:hidden; color:#333; margin:10px 0;">{titulo}</h4>
            <p style="margin:8px 0;"><s style="color:#999; font-size:13px;">${precio_original:,.2f}</s> <b style="color:#222; font-size:18px;">${precio:,.2f}</b> {descuento}</p>
            <a href="{link_afiliado}" target="_blank" style="background:#2968c8; color:white; padding:10px 18px; text-decoration:none; border-radius:6px; display:inline-block; font-weight:bold; font-size:13px; margin-top:5px;">Ver Oferta</a>
        </div>
        '''

    html_completo = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CazaOferta - Las Mejores Ofertas del Día</title>
    <style>
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #f8f9fa; margin:0; padding:20px; text-align:center; }}
        header {{ background: #fff159; padding: 25px; border-radius: 12px; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ margin:0; color:#333; font-size:28px; }}
        p {{ color:#555; margin-top:5px; }}
        .contenedor {{ display: flex; flex-wrap: wrap; justify-content: center; max-width: 1200px; margin: 0 auto; }}
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
