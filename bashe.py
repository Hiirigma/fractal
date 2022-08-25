import sys
import pygame
import time
import pygame_menu
import math

class Bashe:
    def __init__(self):
        pygame.init()
        # game parameters
        self.resX = 1920
        self.resY = 1080
        self.speed = [1, 1]
        self.black = 0, 0, 0
        self.screen = pygame.display.set_mode([self.resX, self.resY])
        self.N = 15
        self.M = 3

        self.first_name = "Player1"
        self.second_name = "Player2"
        self.catSize = []

        self._loadPic()
        # # cats picture
        # self.cat = pygame.image.load("pic/cat.png")
        # self.takeLeft = pygame.image.load("pic/take_cat_left.jpg")
        # self.takeRigth = pygame.image.load("pic/take_cat_right.jpg")

    def _loadPic(self):
        self.cat = pygame.image.load("pic/cat.png")
        self.catSize = self.cat.get_size()
        self.take_left = pygame.image.load("pic/take_cat_left.jpg")
        self.take_right = pygame.image.load("pic/take_cat_right.jpg")

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
        self.menu = pygame_menu.Menu('Welcome', 400, 300,
                                     theme=pygame_menu.themes.THEME_BLUE)

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

    def _play(self):
        # ballrect = self.cat.get_rect()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        self.screen.fill(self.black)
        is_prime = False
        delimit = 1
        if self.N % 7 == 0:
            delimit = 7
        elif self.N % 5 == 0:
            delimit = 5
        elif self.N % 3 == 0:
            delimit = 3
        elif self.N % 2 == 0:
            delimit = 2
        else:
            is_prime = True

        size = self.N // delimit
        if is_prime:
            size = (self.N - 1) // delimit

        self.catSize = 1920//delimit - 50, 1280//delimit - 50
        self.cat = pygame.transform.scale(self.cat, self.catSize)

        for j in range(size):
            for i in range(delimit):
                self.screen.blit(self.cat, (i * self.catSize[0], j*self.catSize[0]))

        if is_prime:
            self.screen.blit(self.cat, (0, (size+1)*self.catSize[0]))

        pygame.display.flip()

        while 1:
            time.sleep(1)

    def runGame(self):
        self._initMenu()

def main():
    b = Bashe()
    b.runGame()


if __name__ == "__main__":
    main()
