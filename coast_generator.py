import numpy as np
import turtle

def generate_coast(size, n_particles, max_iter):
    coast = np.zeros((size, size), dtype=bool)
    
    # Posición inicial aleatoria
    x = np.random.randint(0, size)
    y = np.random.randint(0, size)
    
    for _ in range(n_particles):
        for _ in range(max_iter):
            # Movimiento aleatorio
            dx, dy = np.random.randint(-1, 2, size=2)
            x_new, y_new = x + dx, y + dy
            
            # Verifica que la nueva posición esté dentro del rango
            if 0 <= x_new < size and 0 <= y_new < size:
                # Si hay agua, se adhiere a la costa
                if not coast[x_new, y_new]:
                    coast[x_new, y_new] = True
                    break
            # Actualiza la posición
            x, y = x_new, y_new
            
    return coast

def draw_coast(coast, scale, num_turtles):
    turtle.speed(0)  # Establecer la velocidad al máximo
    # turtle.tracer(False)  # Desactivar actualizaciones de la pantalla
    
    turtles = [turtle.Turtle() for _ in range(num_turtles)]
    for t in turtles:
        t.screen.bgcolor('#0E87CC')
        t.color("#C2B280")
        t.speed(0)
        t.penup()
    
    for i in range(len(coast)):
        for j in range(len(coast[0])):
            if coast[i, j]:
                t = turtles[(i + j) % num_turtles]
                # t.begin_fill()
                t.goto(i * scale - len(coast) * scale / 2, j * scale - len(coast[0]) * scale / 2)
                # for _ in range(4):
                #     t.forward(scale)
                #     t.left(90)
                # t.end_fill()
                t.pendown()
                t.dot(scale)
                t.penup()
    
    turtle.hideturtle()
    turtle.tracer(True)  # Activar actualizaciones de la pantalla
    turtle.done()

size = 200  # Tamaño del mapa
n_particles = 10000  # Número de partículas
max_iter = 500  # Máximo de iteraciones para cada partícula
scale = 4  # Escala para dibujar la costa
num_turtles = 4  # Número de tortugas para dibujar

coast = generate_coast(size, n_particles, max_iter)
draw_coast(coast, scale, num_turtles)
