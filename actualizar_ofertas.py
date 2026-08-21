import json
import urllib.request

# Categorías con más demanda en México
CATEGORIAS = [
    {"id": "MLM1051", "nombre": "Celulares y Telefonía"},
    {"id": "MLM1144", "nombre": "Consolas y Videojuegos"},
    {"id": "MLM1648", "nombre": "Computación"},
    {"id": "MLM1574", "nombre": "Hogar, Muebles y Jardín"},
    {"id": "MLM1430", "nombre": "Ropa y Calzado"},
    {"id": "MLM1747", "nombre": "Accesorios para Vehículos"}
]

ETIQUETA_AFILIADO = "broken01mx"
todas_las_ofertas = []

for cat in CATEGORIAS:
    url = f"https://api.mercadolibre.com/sites/MLM/search?category={cat['id']}&sort=relevance&limit=30"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            
            for item in data.get('results', []):
                price = item.get('price', 0)
                original_price = item.get('original_price') or price
                
                # Solo tomamos productos con descuento real
                if original_price > price:
                    descuento = int(((original_price - price) / original_price) * 100)
                    link_original = item.get('permalink')
                    
                    # Construcción con tu etiqueta de afiliado
                    separador = "&" if "?" in link_original else "?"
                    link_afiliado = f"{link_original}{separador}matt_word={ETIQUETA_AFILIADO}"
                    
                    todas_las_ofertas.append({
                        "id": item.get('id'),
                        "titulo": item.get('title'),
                        "categoria": cat['nombre'],
                        "precio_oferta": round(price, 2),
                        "precio_anterior": round(original_price, 2),
                        "descuento": descuento,
                        "imagen": item.get('thumbnail').replace("I.jpg", "O.jpg"),
                        "link": link_afiliado
                    })
    except Exception as e:
        print(f"Error en {cat['nombre']}: {e}")

# Guardar catálogo masivo
with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(todas_las_ofertas, f, ensure_ascii=False, indent=2)

print(f"¡Catálogo generado con {len(todas_las_ofertas)} ofertas!")
