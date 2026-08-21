import urllib.request
import json

AFILIADO_TAG = "TU_TAG_AQUI" 
URL_API = "https://api.mercadolibre.com/sites/MLM/search?q=gadgets&limit=12"

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
    
    # Lista de respaldo con imágenes reales y estables de Unsplash (sin bloqueos de servidor)
    return [
        {"title": "Audífonos Inalámbricos Bluetooth Pro", "price": 499, "original_price": 899, "thumbnail": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300", "permalink": "https://www.mercadolibre.com.mx"},
        {"title": "Smartwatch Deportivo Full Touch", "price": 649, "original_price": 1199, "thumbnail": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300", "permalink": "https://www.mercadolibre.com.mx"},
        {"title": "Bocina Portátil Bluetooth Bass", "price": 380, "original_price": 599, "thumbnail": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=300", "permalink": "https://www.mercadolibre.com.mx"},
        {"title": "Camara de Seguridad WiFi 1080p", "price": 420, "original_price": 750, "thumbnail": "https://images.unsplash.com/photo-1557324232-b8917d3c3dcb?w=300", "permalink": "https://www.mercadolibre.com.mx"}
    ]

def generar_html(productos):
    cards_html = ""
    for prod in productos:
        titulo = prod.get('title', 'Producto en Oferta')
        precio = prod.get('price', 0)
        precio_original = prod.get('original_price') or precio
        imagen = prod.get('thumbnail', '').replace("http://", "https://")
        
        # Ajuste de resolución para imágenes que provienen directamente de Mercado Libre
        if "mlstatic.com" in imagen:
            imagen = imagen.replace("-I.jpg", "-O.jpg")

        link_original = prod.get('permalink', 'https://www.mercadolibre.com.mx')
        link_afiliado = f"{link_original}?matt_tool=12345678&matt_word={AFILIADO_TAG}" if AFILIADO_TAG != "TU_TAG_AQUI" else link_original
        
        descuento = ""
        if precio_original and precio_original > precio:
            porcentaje = int(((precio_original - precio) / precio_original) * 100)
            descuento = f'<span style="background:#ff3b30; color:white; padding:4px 8px; border-radius:6px; font-weight:bold; font-size:12px; position:absolute; top:10px; right:10px;">-{porcentaje}%</span>'

        cards_html += f'''
        <div style="border: 1px solid #eef2f5; border-radius: 12px; padding: 16px; margin: 12px; width: 250px; display: inline-block; vertical-align: top; background: #ffffff; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.06); position: relative; transition: transform 0.2s;">
            {descuento}
            <div style="height: 160px; display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
                <img src="{imagen}" alt="{titulo}" style="max-width: 100%; max-height: 100%; object-fit: contain;">
            </div>
            <h4 style="font-size: 14px; height: 40px; overflow: hidden; color: #2c3e50; margin: 8px 0; line-height: 1.3;">{titulo}</h4>
            <p style="margin: 10px 0;">
                <s style="color: #a0aec0; font-size: 13px;">${precio_original:,.2f}</s> 
                <b style="color: #2b6cb0; font-size: 20px; display: block; margin-top: 2px;">${precio:,.2f}</b>
            </p>
            <a href="{link_afiliado}" target="_blank" style="background: linear-gradient(135deg, #3182ce, #2b6cb0); color: white; padding: 10px 20px; text-decoration: none; border-radius: 8px; display: block; font-weight: bold; font-size: 14px; margin-top: 10px;">Ver Oferta</a>
        </div>
        '''

    html_completo = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CazaOferta - Las Mejores Ofertas del Día</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f7fafc; margin: 0; padding: 20px; text-align: center; }}
        header {{ background: linear-gradient(135deg, #fff159, #ffe600); padding: 30px 20px; border-radius: 16px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        h1 {{ margin: 0; color: #1a202c; font-size: 32px; font-weight: 800; }}
        p {{ color: #4a5568; margin-top: 8px; font-size: 16px; }}
        .contenedor {{ display: flex; flex-wrap: wrap; justify-content: center; max-width: 1200px; margin: 0 auto; gap: 10px; }}
    </style>
</head>
<body>
    <header>
        <h1>🦊 CazaOferta</h1>
        <p>Las mejores promociones y descuentos actualizados automáticamente</p>
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
