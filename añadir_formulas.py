import json

# Cargar el archivo o tu lista
with open("plantillas_problemas.json", encoding="utf-8") as f:
    plantillas = json.load(f)

# Diccionario tipo -> fórmula general (ajusta los textos como prefieras)
formulas_generales = {
    "área_rectángulo":         "Área = base × altura",
    "perímetro_cuadrado":      "Perímetro = 4 × lado",
    "área_círculo":            "Área = π × radio²",
    "área_trapecio":           "Área = (base mayor + base menor) × altura ÷ 2",
    "área_rombo":              "Área = (diagonal mayor × diagonal menor) ÷ 2",
    "perimetro_rectangulo":    "Perímetro = 2 × (largo + alto)",
    "perimetro_triangulo_equilatero": "Perímetro = 3 × lado",
    "area_triangulo":          "Área = (base × altura) ÷ 2",
    "area_pentagono":          "Área = (Perímetro × Apotema) ÷ 2",
    "perimetro_hexagono":      "Perímetro = 6 × lado",
    "area_cuadrado":           "Área = lado × lado",
    "area_trapecio_recto":     "Área = (base mayor + base menor) × altura ÷ 2",
    "area_romboide":           "Área = base × altura",
    "area_circulo_medio":      "Área = (π × radio²) ÷ 2",
    "area_triangulo_escaleno": "Área = (base × altura) ÷ 2",
    "area_hexagono":           "Área = (Perímetro × Apotema) ÷ 2",
    "area_rectangulo_alfombra":"Área = largo × ancho",
    "area_cuadrado_pizarra":   "Área = lado × lado",
    "perimetro_rombo":         "Perímetro = 4 × lado",
    "area_triangulo_cesped":   "Área = (base × altura) ÷ 2",
    "perimetro_pentagono_escudo": "Perímetro = 5 × lado",
    "area_trapecio_publicidad":   "Área = (base mayor + base menor) × altura ÷ 2",
    "area_paralelogramo_toldo":   "Área = base × altura",
    "area_circulo_marcaje":       "Área = π × radio²",
    "area_rombo_cesped":          "Área = (diagonal mayor × diagonal menor) ÷ 2",
    # Añade aquí cualquier otro tipo personalizado/fijo...
    "area_rectangulo_fijo":         "Área = base × altura",
    "area_cuadrado_fijo":           "Área = lado × lado",
    "area_circulo_fijo":            "Área = π × radio²",
    "perimetro_triangulo_equilatero_fijo": "Perímetro = 3 × lado",
    "area_triangulo_isosceles_fijo": "Área = (base × altura) ÷ 2"
}

# Añadir campo "formula" a cada plantilla
for p in plantillas:
    t = p.get("tipo", "")
    p["formula"] = formulas_generales.get(t, "")

# Guardar de nuevo
with open("plantillas_con_formula.json", "w", encoding="utf-8") as f:
    json.dump(plantillas, f, ensure_ascii=False, indent=2)
