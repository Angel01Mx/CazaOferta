import json

ETIQUETA_AFILIADO = "broken01mx"

PRODUCTOS_BASE = [
    # Celulares
    {
        "titulo": "Smartphone Samsung Galaxy A54 5G 128GB",
        "cat": "Celulares",
        "precio": 5499,
        "anterior": 7999,
        "img": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM22421319"
    },
    {
        "titulo": "Xiaomi Redmi Note 13 Pro 256GB Dual SIM",
        "cat": "Celulares",
        "precio": 4299,
        "anterior": 5999,
        "img": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM31828522"
    },
    {
        "titulo": "Apple iPhone 13 (128 GB) - Medianoche",
        "cat": "Celulares",
        "precio": 11499,
        "anterior": 14499,
        "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM18501723"
    },
    
    # Videojuegos
    {
        "titulo": "Consola Nintendo Switch OLED 64GB Neon",
        "cat": "Videojuegos",
        "precio": 5199,
        "anterior": 7999,
        "img": "https://images.unsplash.com/photo-1578303512597-81e6cc155b3e?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM18491428"
    },
    {
        "titulo": "PlayStation 5 Control Inalámbrico DualSense",
        "cat": "Videojuegos",
        "precio": 1190,
        "anterior": 1699,
        "img": "https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM16122422"
    },
    {
        "titulo": "Xbox Series S 512GB Edición Digital",
        "cat": "Videojuegos",
        "precio": 5690,
        "anterior": 7599,
        "img": "https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM16172283"
    },

    # Computación
    {
        "titulo": "Laptop HP 15-ef2519la AMD Ryzen 5 8GB 512GB",
        "cat": "Computación",
        "precio": 7899,
        "anterior": 11999,
        "img": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM19582132"
    },
    {
        "titulo": "Monitor Gaming Curvo Lenovo 23.8 Full HD",
        "cat": "Computación",
        "precio": 2299,
        "anterior": 3499,
        "img": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM19921102"
    },

    # Hogar
    {
        "titulo": "Freidora De Aire Ninja Air Fryer 3.8 Litros",
        "cat": "Hogar",
        "precio": 1899,
        "anterior": 2799,
        "img": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM16010211"
    },
    {
        "titulo": "Cafetera Programable Oster 12 Tazas Filtro",
        "cat": "Hogar",
        "precio": 599,
        "anterior": 899,
        "img": "https://images.unsplash.com/photo-1517668808822-9e428d691062?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM15102911"
    },

    # Ropa
    {
        "titulo": "Tenis Adidas Grand Court 2.0 Unisex",
        "cat": "Ropa",
        "precio": 1099,
        "anterior": 1599,
        "img": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM21001923"
    },

    # Automotriz
    {
        "titulo": "Compresor De Aire Portátil Para Auto 12v",
        "cat": "Automotriz",
        "precio": 389,
        "anterior": 649,
        "img": "https://images.unsplash.com/photo-1511919884226-fd3cad34687c?w=500&auto=format&fit=crop",
        "link": "https://www.mercadolibre.com.mx/p/MLM18192011"
    }
]

todas_las_ofertas = []

for p in PRODUCTOS_BASE:
    descuento = int(((p["anterior"] - p["precio"]) / p["anterior"]) * 100)
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

with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(todas_las_ofertas, f, ensure_ascii=False, indent=2)

print("Catálogo generado con imágenes públicas exitosamente.")
