import sys
import pygame
import time
import pygame_menu
import math

"""
Кто заберёт больше котиков из приюта => тот молодец
"""

class Bashe:
    def __init__(self):
        pygame.init()
        # game parameters
        self.resX = 1920
        self.resY = 1080
        self.speed = [1, 1]
        self.background_color = 14, 166, 211
        self.screen = pygame.display.set_mode([self.resX, self.resY])
        self.N = 15
        self.M = 3

        self.first_name = "Player1"
        self.second_name = "Player2"
        self.catSize = []
        self.cat_pictures = []
        self.cat_home = []

        self.curr_player = False
        self.curr_cnt = 0
        self.total_cnt = dict()
        self.total_cnt[False] = 0
        self.total_cnt[True] = 0

        self._loadPic()

    def _loadPic(self):
        self.catSize = 200, 200
        self.cat = pygame.image.load("pic/cat.png")
        self.cat_take = pygame.image.load("pic/take_cat_left.jpg")
        self.cat_at_home = pygame.image.load("pic/cat_at_home.jpg")

    def _loadFirstName(self, value):
        if len(value) == 0:
            # print bad cat
            return
        self.first_name = value

    def _loadSecondName(self, value):
        if len(value) == 0:
            # print bad cat
            return
        self.second_name = value

    def _loadN(self, value):
        if len(value) <= 0:
            # print bad cat
            return
        self.N = int(value)

    def _loadM(self, value):
        if len(value) <= 0:
            # print bad cat
            return
        self.M = int(value)

    def _initMenu(self):
        self.menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)

        self.menu.add.text_input('First player:', default=self.first_name, onchange=self._loadFirstName)
        self.menu.add.text_input('Second player:', default=self.second_name, onchange=self._loadSecondName)
        self.menu.add.text_input('N parameter:', default=self.N, onchange=self._loadN)
        self.menu.add.text_input('M parameter:', default=self.M, onchange=self._loadM)
        self.menu.add.button('Play', self._prepareParmas)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)

    def _prepareParmas(self):
        if self.M >= self.N:
            # pic unhappy cat
            exit(-1)

        if self.N == 0:
            # pic unhappy cat
            exit(-1)

        if self.M == 0:
            # pic unhappy cat
            exit(-1)

        self._play()

    def _event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                for cat in self.cat_pictures:
                    if cat.collidepoint(event.pos) and cat not in self.cat_home:  # is mouse over button
                        self.cat_home.append(cat)
                        self.screen.blit(self.cat_take, cat)
                        pygame.display.update()
                        time.sleep(2)
                        self.screen.blit(self.cat_at_home, cat)
                        self.curr_cnt += 1

    def _change_pic_size(self):
        self.cat = pygame.transform.scale(self.cat, self.catSize)
        self.cat_take = pygame.transform.scale(self.cat_take, self.catSize)
        self.cat_at_home = pygame.transform.scale(self.cat_at_home, self.catSize)

    def _play(self):
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        self.screen.fill(self.background_color)
        is_prime = False
        rows = 1
        if self.N % 7 == 0:
            rows = 7
        elif self.N % 5 == 0:
            rows = 5
        elif self.N % 3 == 0:
            rows = 3
        elif self.N % 2 == 0:
            rows = 2
        else:
            is_prime = True

        columns = self.N // rows
        if is_prime:
            columns = (self.N - 1) // rows

        self.catSize = self.resX // rows - 50, self.resY // rows - 50
        self._change_pic_size()

        center = (self.resX // 2) - ((self.catSize[0] * rows) // 2), \
                 (self.resY // 2) - ((self.catSize[1] * columns) // 2)

        for j in range(columns):
            for i in range(rows):
                self.cat_pictures.append(self.screen.blit(self.cat, (i * self.catSize[0] + center[0],
                                            j * self.catSize[1] + center[1])))

        if is_prime:
            self.screen.blit(self.cat, (0, (columns+1)*self.catSize[0]))

        pygame.display.flip()

        running = True

        while running:
            if self.curr_cnt > self.M:
                self.total_cnt[self.curr_player] += self.curr_cnt
                self.curr_cnt = 0
                self.curr_player = not self.curr_player

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                self._event_handler(event)

            pygame.display.update()


    def runGame(self):
        self._initMenu()

def main():
    b = Bashe()
    b.runGame()


if __name__ == "__main__":
    main()
