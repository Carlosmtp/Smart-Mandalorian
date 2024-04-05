import pygame
import os
import time

class SearchGUI:
    def __init__(self, path, mandalorian_moves):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.empty = pygame.transform.scale(pygame.image.load('../images/empty.png'), (40, 40))
        self.wall = pygame.transform.scale(pygame.image.load('../images/wall.png'), (40, 40))
        self.grogu = pygame.transform.scale(pygame.image.load('../images/grogu.png'), (40, 40))
        self.mandalorian = pygame.transform.scale(pygame.image.load('../images/mandalorian.png'), (40, 40))
        self.ship = pygame.transform.scale(pygame.image.load('../images/ship.png'), (40, 40))
        self.enemy = pygame.transform.scale(pygame.image.load('../images/enemy.png'), (40, 40))
        self.screen = pygame.display.set_mode((800,400))
        self.screen.fill((255,255,255))
        self.tablero = [[0 for _ in range(10)] for _ in range(10)]
        self.mandalorian_moves = mandalorian_moves

        with open(path, 'r') as file:
            testfile = file.read().replace(" ", "").replace("\n", "") 
        for i in range(10):
            for j in range(10):
                self.tablero[i][j] = int(testfile[i*10+j])

    def draw_tablero(self):
        pygame.display.set_caption("Búsqueda")
        move_index = 0  # Indice para recorrer la lista de movimientos del mandaloriano
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()       
            for i in range(10):
                for j in range(10):
                    if self.tablero[i][j] == 0 or self.tablero[i][j] == 2:
                        self.screen.blit(self.empty, (j*40, i*40)) 
                    elif self.tablero[i][j] == 1:
                        self.screen.blit(self.wall, (j*40, i*40))   
                    elif self.tablero[i][j] == 3:
                        self.screen.blit(self.ship, (j*40, i*40))
                    elif self.tablero[i][j] == 4:
                        self.screen.blit(self.enemy, (j*40, i*40))
                    elif self.tablero[i][j] == 5:
                        self.screen.blit(self.grogu, (j*40, i*40))

            # Verificamos si hay movimientos del mandaloriano y lo dibujamos
            if move_index < len(self.mandalorian_moves):
                move = self.mandalorian_moves[move_index]
                self.screen.blit(self.mandalorian, (move.column*40, move.row*40))
                move_index += 1
                self.tablero[move.row][move.column] = self.tablero[move.row][move.column]
                pygame.display.flip()
            time.sleep(0.5)  # Esperamos un momento antes de realizar el próximo movimiento