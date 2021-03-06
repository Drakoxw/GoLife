import pygame
import numpy as np 
import time

pygame.init()

#se crea las dimensiones de a pantalla 
height = 1000
width=1000
screen = pygame.display.set_mode((height,width))

#se pinta el fondo 
bg = 25,25,25
screen.fill(bg)


nxC = 50# número de celdas
nyC = 50
dimCW = width / nxC#se le da la dimensión
dimCh = height / nyC


# estado de las celdas viva=1, muerta=0.
gameState = np.zeros((nxC, nyC))


#automatas palo
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1
#automate movil
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1



while True:#recorer los dos ejes

    NewgameState = np.copy(gameState)

    #limpiar pantalla en cada iteración
    screen.fill(bg)

    #diley
    time.sleep(0.1)

    for y in range(0, nxC):
        for x in range(0, nyC):

            #calcular el numero de vecinos cercanos
            n_neigh = gameState[(x - 1)% nxC, (y-1) % nyC]+ \
                      gameState[(x)    % nxC, (y-1) % nyC]+ \
                      gameState[(x + 1)% nxC, (y-1) % nyC]+ \
                      gameState[(x - 1)% nxC, (y) % nyC]+ \
                      gameState[(x + 1)% nxC, (y) % nyC]+ \
                      gameState[(x - 1)% nxC, (y+1) % nyC]+ \
                      gameState[(x)    % nxC, (y+1) % nyC]+ \
                      gameState[(x + 1)% nxC, (y+1) % nyC]

            # Regla 1: una celular con 3 celulas viva,revive
            if gameState[y, x] == 0 and n_neigh == 3:
                NewgameState[x, y] = 1

            #Regla2: una celula viva con menos d 2, o mas de 3 muere
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                NewgameState[x, y] = 0

            poly =[((x) * dimCW, y * dimCh),
            ((x+1) * dimCW, y * dimCh),
            ((x+1) * dimCW, (y+1) * dimCh),
            ((x) * dimCW, (y+1) * dimCh)]

            if NewgameState[x, y] == 0:
                pygame.draw.polygon(screen, (128,128,128), poly,1)

            else:
                pygame.draw.polygon(screen, (255,255,255), poly,0)


    #Actualiza el estado del juego
    gameState = np.copy(NewgameState)

    # actualiza la pantalla
    pygame.display.flip()
