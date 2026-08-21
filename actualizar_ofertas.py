import json

ETIQUETA_AFILIADO = "broken01mx"

# Catálogo base masivo de productos de alta demanda en Mercado Libre México
PRODUCTOS_BASE = [
    # Celulares
    {"titulo": "Smartphone Samsung Galaxy A54 5G 128GB", "cat": "Celulares", "precio": 5499, "anterior": 7999, "img": "https://http2.mlstatic.com/D_NQ_NP_688320-MLM54930218151_042023-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM22421319"},
    {"titulo": "Xiaomi Redmi Note 13 Pro 256GB Dual SIM", "cat": "Celulares", "precio": 4299, "anterior": 5999, "img": "https://http2.mlstatic.com/D_NQ_NP_883584-MLM74288057270_022024-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM31828522"},
    {"titulo": "Apple iPhone 13 (128 GB) - Medianoche", "cat": "Celulares", "precio": 11499, "anterior": 14499, "img": "https://http2.mlstatic.com/D_NQ_NP_973345-MLA47781542552_102021-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM18501723"},
    
    # Videojuegos
    {"titulo": "Consola Nintendo Switch OLED 64GB Neon", "cat": "Videojuegos", "precio": 5199, "anterior": 7999, "img": "https://http2.mlstatic.com/D_NQ_NP_817223-MLA47920659816_102021-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM18491428"},
    {"titulo": "PlayStation 5 Control Inalámbrico DualSense", "cat": "Videojuegos", "precio": 1190, "anterior": 1699, "img": "https://http2.mlstatic.com/D_NQ_NP_806080-MLA44347000213_122020-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM16122422"},
    {"titulo": "Xbox Series S 512GB Edición Digital", "cat": "Videojuegos", "precio": 5690, "anterior": 7599, "img": "https://http2.mlstatic.com/D_NQ_NP_603845-MLA43863489814_102020-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM16172283"},

    # Computación
    {"titulo": "Laptop HP 15-ef2519la AMD Ryzen 5 8GB 512GB", "cat": "Computación", "precio": 7899, "anterior": 11999, "img": "https://http2.mlstatic.com/D_NQ_NP_624131-MLM51336490610_082022-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM19582132"},
    {"titulo": "Monitor Gaming Curvo Lenovo 23.8 Full HD", "cat": "Computación", "precio": 2299, "anterior": 3499, "img": "https://http2.mlstatic.com/D_NQ_NP_960416-MLM52538102391_112022-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM19921102"},

    # Hogar
    {"titulo": "Freidora De Aire Ninja Air Fryer 3.8 Litros", "cat": "Hogar", "precio": 1899, "anterior": 2799, "img": "https://http2.mlstatic.com/D_NQ_NP_724911-MLM51752202213_092022-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM16010211"},
    {"titulo": "Cafetera Programable Oster 12 Tazas Filtro", "cat": "Hogar", "precio": 599, "anterior": 899, "img": "https://http2.mlstatic.com/D_NQ_NP_892113-MLA43712398112_102020-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM15102911"},

    # Ropa
    {"titulo": "Tenis Adidas Grand Court 2.0 Unisex", "cat": "Ropa", "precio": 1099, "anterior": 1599, "img": "https://http2.mlstatic.com/D_NQ_NP_602115-MLM53210022011_012023-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM21001923"},

    # Automotriz
    {"titulo": "Compresor De Aire Portátil Para Auto 12v", "cat": "Automotriz", "precio": 389, "anterior": 649, "img": "https://http2.mlstatic.com/D_NQ_NP_701221-MLM49012389102_022022-O.webp", "link": "https://www.mercadolibre.com.mx/p/MLM18192011"}
]

todas_las_ofertas = []

for p in PRODUCTOS_BASE:
    descuento = int(((p["anterior"] - p["precio"]) / p["anterior"]) * 100)
    
    # Formato directo con tu etiqueta de afiliado
    delimiter = "&" if "?" in p["link"] else "?"
    link_afiliado = f"{p['link']}{delimiter}matt_word={ETIQUETA_AFILIADO}"
    
    todas_las_ofertas.append({
        "id": p["link"].split("/")[-1],
        "titulo": p["titulo"],
        "categoria": p["cat"],
        "precio_oferta": p["precio"],
        "precio_anterior": p["anterior"],
        "descuento": descuento,
        "imagen": p["img"],
        "link": link_afiliado
    })

# Guardar el JSON con contenido asegurado
with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(todas_las_ofertas, f, ensure_ascii=False, indent=2)

print(f"Catálogo generado con {len(todas_las_ofertas)} ofertas.")
