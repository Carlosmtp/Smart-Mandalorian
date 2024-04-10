import pygame
import os
import time

class SearchGUI:
    def __init__(self, path, search_results, algorithm):
        """
        Inicializa la interfaz gráfica de búsqueda.

        Args:
            path (str): La ruta del archivo de prueba.
            search_results (tuple): Una tupla que contiene los resultados de la búsqueda.
                Los resultados deben estar en el siguiente orden:
                - mandalorian_moves (list): Lista de movimientos del Mandalorian.
                - tree_nodes (int): Número de nodos del arbol de búsqueda.
                - expanded_nodes (int): Número de nodos expandidos durante la búsqueda.
                - depth (int): Profundidad de la solución encontrada.
                - computation_time (float): Tiempo de cómputo de la búsqueda.
                - cost (int): Costo de la solución encontrada.
            algorithm (str): El algoritmo de búsqueda utilizado.
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        self.empty = pygame.transform.scale(pygame.image.load('../images/empty.png'), (40, 40))
        self.wall = pygame.transform.scale(pygame.image.load('../images/wall.png'), (40, 40))
        self.grogu = pygame.transform.scale(pygame.image.load('../images/grogu.png'), (40, 40))
        self.mandalorian = pygame.transform.scale(pygame.image.load('../images/mandalorian.png'), (40, 40))
        self.ship = pygame.transform.scale(pygame.image.load('../images/ship.png'), (40, 40))
        self.boarded_ship = pygame.transform.scale(pygame.image.load('../images/boarded_ship.png'), (40, 40))
        self.enemy = pygame.transform.scale(pygame.image.load('../images/enemy.png'), (40, 40))
        self.background = pygame.image.load('../images/search_background.png')
        self.screen = pygame.display.set_mode((800,400))
        self.screen.fill((255,255,255))
        self.tablero = [[0 for _ in range(10)] for _ in range(10)]
        self.algo = algorithm
        self.mandalorian_moves, self.tree_nodes, self.expanded_nodes, self.depth, self.computation_time, self.cost = search_results

        with open(path, 'r') as file:
            testfile = file.read().replace(" ", "").replace("\n", "") 
        for i in range(10):
            for j in range(10):
                self.tablero[i][j] = int(testfile[i*10+j])

    def draw_tablero(self):
        """
        Dibuja el tablero y muestra los resultados de la búsqueda en la interfaz gráfica.
        """
        pygame.display.set_caption(self.algo.upper())
        move_index = 0
        ship_trip = 0
        title = pygame.font.Font(None, 36)
        font = pygame.font.Font(None, 30)
        title = font.render(self.algo.upper(), True, (255, 255, 255))  
        tree = font.render("Nodos del Arbol: " + str(self.tree_nodes), True, (255, 255, 255))
        expanded = font.render("Nodos Expandidos: " + str(self.expanded_nodes), True, (255, 255, 255))  
        depth_title = font.render("Profundidad Meta: " + str(self.depth), True, (255, 255, 255))
        compute_time_title = font.render("Tiempo de Computo: " + str(round(self.computation_time, 7)), True, (255, 255, 255))
        cost = font.render("Costo: " + str(self.cost), True, (255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return    
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
            for i in range(10):
                for j in range(10, 20):
                    self.screen.blit(self.background, (j*40, i*40))
                    
            if move_index < len(self.mandalorian_moves):
                move = self.mandalorian_moves[move_index]
                if self.tablero[move.row][move.column] == 3:
                    self.mandalorian = self.boarded_ship
                    self.ship = self.empty
                if self.ship == self.empty:
                    ship_trip += 1
                if ship_trip == 10:
                    self.mandalorian = pygame.transform.scale(pygame.image.load('../images/mandalorian.png'), (40, 40))
                self.screen.blit(self.mandalorian, (move.column*40, move.row*40))
                move_index += 1
                self.tablero[move.row][move.column] = self.tablero[move.row][move.column]
            else:
                self.screen.blit(self.mandalorian, (self.mandalorian_moves[-1].column*40, self.mandalorian_moves[-1].row*40))
            self.screen.blit(title, (450, 40))
            self.screen.blit(tree, (450, 100))
            self.screen.blit(expanded, (450, 140))
            self.screen.blit(depth_title, (450, 180))
            self.screen.blit(compute_time_title, (450, 220))
            self.screen.blit(cost, (450, 260))
            pygame.display.flip()
            time.sleep(1)