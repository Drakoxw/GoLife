import pygame
import numpy as np 
import time

pygame.init()

#se crea las dimensiones de a pantalla 
height = 700
width=700
screen = pygame.display.set_mode((height,width))

#se pinta el fondo 
bg = 25,25,25
screen.fill(bg)


nxC = 55# número de celdas
nyC = 55
dimCW = width / nxC#se le da la dimensión
dimCh = height / nyC


# estado de las celdas viva=1, muerta=0.
gameState = np.zeros((nxC, nyC))

gameState[15,3] = 1
gameState[15,4] = 1
gameState[15,5] = 1
gameState[15,6] = 1
#automatas palo
gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1
gameState[5,6] = 1
#automate movil
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1
 
#control de pausa del juego
pauseExect = False
rodar= True

     
while rodar == True:#recorer los dos ejes

    NewgameState = np.copy(gameState)

    #limpiar pantalla en cada iteración
    screen.fill(bg)#pintandola como al principio

    #diley
    time.sleep(0.1)

    #registra eventos de raton y teclado
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            print('s impt')
            rodar = False


        #if event.type == pygame.KEYDOWN:
         #   pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCh))
            NewgameState[celX, celY] = not mouseClick[2]

    

    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:

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
