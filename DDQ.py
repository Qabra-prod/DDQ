import pygame                                           
import random                                           

pygame.init() 

ancho = 400
altura = 1000
ventana = pygame.display.set_mode((ancho, altura))

pygame.display.set_caption('Dance Dance Qabralution (BETA)')
fps = pygame.time.Clock()
fps.tick(240)                                            
negro = (0,0,0)
blanco = (255,255,255)
gris = (200,200,200)

impacto = 100                                  
velocidad = 5                                           
imagenFlecha = {
    "arriba": pygame.image.load("flechaarriba.png"),
    "abajo": pygame.image.load("flechaabajo.png"),
    "izquierda": pygame.image.load("flechaizquierda.png"),
    "derecha": pygame.image.load("flechaderecha.png")
}
#lista vacia para las flechas
flechas = []                                            
def flechaAparece ():                                   #variable para hacer aparecer las flechas
    direccion = random.choice(["arriba","abajo","izquierda","derecha","dobleUpLeft","quadruple"]) 
    posicionX = {"arriba" :125,"abajo":225,"izquierda":25,"derecha":325,"dobleUpLeft":125,"quadruple":25}[direccion]
    if (direccion == "dobleUpLeft"):
        flechas.append({"dir": "arriba", "x" : posicionX, "y" : altura}) 
        flechas.append({"dir": "izquierda", "x" : posicionX - 100, "y" : altura})
    elif (direccion == "quadruple"):
        flechas.append({"dir": "izquierda", "x" : posicionX, "y" : altura}) 
        flechas.append({"dir": "arriba", "x" : posicionX + 100, "y" : altura})
        flechas.append({"dir": "abajo", "x" : posicionX + 200, "y" : altura})
        flechas.append({"dir": "derecha", "x" : posicionX + 300, "y" : altura})
    else: 
        flechas.append({"dir": direccion, "x" : posicionX, "y" : altura}) 

jugando = True
puntaje = 0
tiempoDeSpawn = 0
fuente = pygame.font.SysFont(None, 36)
#main
while jugando:
    ventana.fill(negro)
#quit game
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
#intervalo entre flechas
    tiempoDeSpawn += fps.get_time()
    if tiempoDeSpawn > 300:
        flechaAparece()
        tiempoDeSpawn = 0

    apretar = pygame.key.get_pressed()
#movimiento
    for flecha in flechas[:]:
        flecha["y"] -= velocidad
        ventana.blit(imagenFlecha[flecha["dir"]], (flecha["x"], flecha["y"]))

        # verifica zona de impacto
        if impacto - 10 < flecha["y"] < impacto + 10:
            if (flecha["dir"] == "arriba" and (apretar[pygame.K_UP]) or apretar[pygame.K_w]) or \
               (flecha["dir"] == "abajo" and (apretar[pygame.K_DOWN]) or apretar[pygame.K_s]) or \
               (flecha["dir"] == "izquierda" and (apretar[pygame.K_LEFT]) or apretar[pygame.K_a]) or \
               (flecha["dir"] == "derecha" and (apretar[pygame.K_RIGHT] or apretar[pygame.K_d])):
                flechas.remove(flecha)
                puntaje += 1

        # eliminar flechas que pasaron
        elif flecha["y"] < 0:
            flechas.remove(flecha)

    # dibuja zona de impacto
    pygame.draw.line(ventana, gris, (0, impacto), (altura, impacto), 2)
    pygame.draw.line(ventana, gris, (0, impacto+64), (altura, impacto+64), 2)
    #puntaje
    textoPuntaje = fuente.render(f"Puntaje: {puntaje}", True, blanco)
    ventana.blit(textoPuntaje, (10, 10))

    pygame.display.flip()
    fps.tick(60)

pygame.quit()