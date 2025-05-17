import json

# Abrir el archivo original
with open("plantillas_problemas.json", encoding="utf-8") as f:
    plantillas = json.load(f)

# Diccionario de equivalencias tipo -> figura
tipo_a_figura = {
    "área_rectángulo": "rectángulo",
    "perímetro_cuadrado": "cuadrado",
    "área_círculo": "círculo",
    "área_trapecio": "trapecio",
    "área_rombo": "rombo",
    "perimetro_rectangulo": "rectángulo",
    "perimetro_triangulo_equilatero": "triángulo equilátero",
    "area_triangulo": "triángulo",
    "area_pentagono": "pentágono",
    "perimetro_hexagono": "hexágono",
    "area_cuadrado": "cuadrado",
    "area_trapecio_recto": "trapecio recto",
    "area_romboide": "romboide",
    "area_circulo_medio": "semicírculo",
    "area_triangulo_escaleno": "triángulo escaleno",
    "area_hexagono": "hexágono",
    "area_rectangulo_alfombra": "rectángulo",
    "area_cuadrado_pizarra": "cuadrado",
    "perimetro_rombo": "rombo",
    "area_triangulo_cesped": "triángulo",
    "perimetro_pentagono_escudo": "pentágono",
    "area_trapecio_publicidad": "trapecio",
    "area_paralelogramo_toldo": "paralelogramo",
    "area_circulo_marcaje": "círculo",
    "area_rombo_cesped": "rombo",
    "area_rectangulo_fijo": "rectángulo",
    "area_cuadrado_fijo": "cuadrado",
    "area_circulo_fijo": "círculo",
    "perimetro_triangulo_equilatero_fijo": "triángulo equilátero",
    "area_triangulo_isosceles_fijo": "triángulo isósceles"
}

# Reorganizar pistas y generar nueva pista1
for p in plantillas:
    tipo = p.get("tipo", "")
    figura = tipo_a_figura.get(tipo, "figura geométrica")

    p["pista3"] = p.get("pista2", "")
    p["pista2"] = p.get("pista1", "")
    p["pista1"] = f"La figura es un {figura}."

# Guardar el archivo resultante
with open("plantillas_modificadas.json", "w", encoding="utf-8") as f:
    json.dump(plantillas, f, ensure_ascii=False, indent=2)

print("✅ Archivo guardado como plantillas_modificadas.json con las pistas reorganizadas.")
