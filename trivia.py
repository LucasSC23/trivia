"""
# trivia
# es juego de triviaaa!
# Challenge: Mini Trivia en Python

## Debes crear:
Un archivo llamado `trivia.py`

## Tu programa debe:
- pedir el nombre del jugador
- mostrar una bienvenida
- hacer 4 preguntas
- sumar 1 punto por cada respuesta correcta
- mostrar el nombre y el puntaje final

## Resultado final
- si `puntaje == 4` → **Excelente**
- si `puntaje >= 2` → **Muy bien**
- si no → **Puedes mejorar**

## Recuerda
- trabaja paso a paso
- no hace falta terminar perfecto
- usa Git durante el proceso
- haz varios commits pequeños
"""
nombre_usuario=input("Ingrese su nombre: \n")
pregunta1=""
pregunta2=""
pregunta3=""
pregunta4=""
respuestas=["blanco","negro","rojo","rosa"]
contador=0

def preguntas(nombre):
    print(f"Bienvenido {nombre}")

    pregunta1=input("De que color es el caballo blanco del Mcal. Lopez?")
    pregunta2=input("De que color es el caballo negro del Mcal. Lopez?")
    pregunta3=input("De que color es el caballo rojo del Mcal. Lopez?")
    pregunta4=input("De que color es el caballo rosa del Mcal. Lopez?")
    for i in respuestas:
        if pregunta1 == respuestas[i]:
            contador+=1
        elif pregunta2== respuestas[i]:
            contador+=1
        elif pregunta3== respuestas[i]:
            contador+=1
        elif pregunta4==respuestas[i]:
            contador+=1    
        else:
            print("Fallo")


preguntas(nombre_usuario)