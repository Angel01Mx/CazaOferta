import json
import urllib.request

ETIQUETA_AFILIADO = "broken01mx"

# Búsquedas clave por categoría para garantizar variedad y productos activos
BUSQUEDAS = [
    {"query": "celulares", "cat": "Celulares"},
    {"query": "videojuegos", "cat": "Videojuegos"},
    {"query": "laptop", "cat": "Computación"},
    {"query": "hogar", "cat": "Hogar"},
    {"query": "ropa", "cat": "Ropa"},
    {"query": "accesorios auto", "cat": "Automotriz"}
]

todas_las_ofertas = []

for item in BUSQUEDAS:
    url = f"https://api.mercadolibre.com/sites/MLM/search?q={item['query']}&limit=15"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            results = data.get('results', [])
            
            for producto in results:
                price = producto.get('price', 0)
                original_price = producto.get('original_price') or price
                
                # Calcular descuento o generar margen visible de oferta
                if original_price <= price:
                    original_price = round(price * 1.20, 2)
                
                descuento = int(((original_price - price) / original_price) * 100)
                
                # Enlace directo de la publicación activa
                link_real = producto.get('permalink', '')
                separador = "&" if "?" in link_real else "?"
                link_afiliado = f"{link_real}{separador}matt_word={ETIQUETA_AFILIADO}"
                
                # Imagen oficial accesible desde la CDN de Mercado Libre
                img_id = producto.get('thumbnail_id') or producto.get('id')
                imagen_url = f"https://http2.mlstatic.com/D_NQ_NP_{producto.get('thumbnail_id')}-O.webp" if producto.get('thumbnail_id') else producto.get('thumbnail')
                
                todas_las_ofertas.append({
                    "id": producto.get('id'),
                    "titulo": producto.get('title'),
                    "categoria": item['cat'],
                    "precio_oferta": round(price, 2),
                    "precio_anterior": round(original_price, 2),
                    "descuento": descuento if descuento > 0 else 15,
                    "imagen": imagen_url,
                    "link": link_afiliado
                })
    except Exception as e:
        print(f"Error extrayendo {item['query']}: {e}")

# Guardar catálogo en el repositorio
with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(todas_las_ofertas, f, ensure_ascii=False, indent=2)

print(f"Proceso finalizado. Total de productos recopilados: {len(todas_las_ofertas)}")
