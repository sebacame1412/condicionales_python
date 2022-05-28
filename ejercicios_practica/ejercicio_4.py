# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

if texto_1[0] > texto_2[0]:
    print(f"{texto_1} es mayor alfabéticamente a {texto_2}")
else:
    print(f"{texto_2} es mayor alfabéticamente a {texto_1}")


# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

numero_1 = int(texto_1)
numero_2 = int(texto_2)

if numero_1 > numero_2:
    print(f"La variable {numero_1} es mayor a la variable {numero_2}")
elif numero_1 < numero_2:
    print(f"La variable {numero_2} es mayor a la variable {numero_1}")
else:
    print(f"Las variables {numero_1} y {numero_2} son iguales")

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

# Respuesta:
# Según el orden alfabetico de los numeros, 7(siete) es mayor a 5(cinco)
