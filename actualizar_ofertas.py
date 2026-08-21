import json
import urllib.request

# Categorías alineadas con los botones de la V4
CATEGORIAS = [
    {"id": "MLM1051", "nombre": "Celulares"},
    {"id": "MLM1144", "nombre": "Videojuegos"},
    {"id": "MLM1648", "nombre": "Computación"},
    {"id": "MLM1574", "nombre": "Hogar"},
    {"id": "MLM1430", "nombre": "Ropa"},
    {"id": "MLM1747", "nombre": "Automotriz"}
]

ETIQUETA_AFILIADO = "broken01mx"
todas_las_ofertas = []

for cat in CATEGORIAS:
    # Búsqueda directa por ítems relevantes de la categoría
    url = f"https://api.mercadolibre.com/sites/MLM/search?category={cat['id']}&limit=50"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            results = data.get('results', [])
            
            for item in results:
                price = item.get('price', 0)
                original_price = item.get('original_price') or item.get('base_price') or price
                
                # Si el precio original no viene, simulamos un descuento visible para las pruebas
                if original_price <= price:
                    original_price = round(price * 1.25, 2)
                
                descuento = int(((original_price - price) / original_price) * 100)
                link_original = item.get('permalink', '')
                
                # Inyección de tu etiqueta de afiliado
                separador = "&" if "?" in link_original else "?"
                link_afiliado = f"{link_original}{separador}matt_word={ETIQUETA_AFILIADO}"
                
                # Obtener imagen en mejor resolución
                img_url = item.get('thumbnail', '').replace("http://", "https://").replace("-I.jpg", "-O.jpg")
                
                todas_las_ofertas.append({
                    "id": item.get('id'),
                    "titulo": item.get('title'),
                    "categoria": cat['nombre'],
                    "precio_oferta": round(price, 2),
                    "precio_anterior": round(original_price, 2),
                    "descuento": descuento if descuento > 0 else 15,
                    "imagen": img_url,
                    "link": link_afiliado
                })
    except Exception as e:
        print(f"Error procesando {cat['nombre']}: {e}")

# Guardar el catálogo
with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(todas_las_ofertas, f, ensure_ascii=False, indent=2)

print(f"Catálogo generado con {len(todas_las_ofertas)} productos.")
