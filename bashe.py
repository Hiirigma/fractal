import pygame
import time
import pygame_menu

"""
Кто заберёт больше котиков из приюта => тот молодец
"""


class Bashe:
    def __init__(self):
        self._N = 15
        self._M = 3

        self._first_name = "Player1"
        self._second_name = "Player2"

        pygame.init()
        self._resX = 1920
        self._resY = 1080

        self._screen = pygame.display.set_mode([self._resX, self._resY])
        self._font = pygame.font.SysFont('Comic Sans MS', 60)
        self._loadPic()

    def _loadPic(self):
        self._catSize = 200, 200
        self._cat = pygame.image.load("pic/cat.png")
        self._cat_take = pygame.image.load("pic/take_cat_left.jpg")
        self._cat_at_home = pygame.image.load("pic/cat_at_home.jpg")
        self._cat_win = pygame.image.load("pic/cat_win.jpg")
        self._grumpy = pygame.image.load("pic/grumpy.jpg")

    def _loadFirstName(self, value):
        if len(value) == 0:
            return

        self._first_name = value

    def _loadSecondName(self, value):
        if len(value) == 0:
            return

        self._second_name = value

    def _loadN(self, value):
        if len(value) <= 0:
            return

        self._N = int(value)

    def _loadM(self, value):
        if len(value) <= 0:
            return

        self._M = int(value)

    def _initMenu(self):
        self._menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_SOLARIZED)

        self._menu.add.text_input('First player:',
                                  default=self._first_name,
                                  onchange=self._loadFirstName,
                                  maxchar=10)

        self._menu.add.text_input('Second player:',
                                  default=self._second_name,
                                  onchange=self._loadSecondName,
                                  maxchar=10)

        self._menu.add.text_input('N parameter:',
                                  default=self._N,
                                  onchange=self._loadN,
                                  maxchar=2)

        self._menu.add.text_input('M parameter:',
                                  default=self._M,
                                  onchange=self._loadM,
                                  maxchar=2)

        self._menu.add.button('Play', self._prepareParmas)
        self._menu.add.button('Quit', pygame_menu.events.EXIT)
        self._menu.mainloop(self._screen)

    def _outScore(self):
        self._screen.fill(self._background_color, (0, 0, 1028, 120))
        text_surface = \
            self._font.render(f"{self._first_name}: {self._total_cnt[False]}",
                              False, (0, 0, 0))

        self._screen.blit(text_surface, (0, 0))

        text_surface = \
            self._font.render(f"{self._second_name}: {self._total_cnt[True]}",
                              False, (0, 0, 0))

        self._screen.blit(text_surface, (0, 60))

    def _outScoreWinning(self):
        self._screen.blit(self._cat_win, (0, 0))

        text_surface = \
            self._font.render(f"{self._first_name}: {self._total_cnt[False]}",
                              False, (0, 0, 0))

        self._screen.blit(text_surface, (0, 0))

        text_surface = \
            self._font.render(f"{self._second_name}: {self._total_cnt[True]}",
                              False, (0, 0, 0))

        self._screen.blit(text_surface, (0, 60))

        name = self._first_name
        if self._curr_player:
            name = self._second_name

        result = f"{name}: {self._total_cnt[self._curr_player]} - Winner"
        if self._total_cnt[True] == self._total_cnt[False]:
            result = "Friendship is magic. Both players win"

        text_surface = \
            self._font.render(result,
                              False, (0, 0, 0))

        self._screen.blit(text_surface, (0, 120))

        pygame.display.update()

    def _outGrumpyCat(self, text):
        text_surface = \
            self._font.render(text,
                              False, (0, 0, 0))

        self._screen.blit(self._grumpy, (0, 0))
        self._screen.blit(text_surface, (0, 0))
        pygame.display.update()
        time.sleep(3)

    def _prepareParmas(self):
        self._background_color = 14, 166, 211

        self._catSize = []
        self._cat_pictures = []
        self._cat_home = []

        self._curr_player = False
        self._curr_cnt = 0
        self._total_score = 0
        self._total_cnt = dict()
        self._total_cnt[False] = 0
        self._total_cnt[True] = 0

        if self._M >= self._N:
            self._outGrumpyCat("Параметр M не может быть больше или равен N")
            return

        if len(self._first_name) == 0:
            self._outGrumpyCat("Имя первого игрока не должно быть пустым")
            return

        if len(self._second_name) == 0:
            self._outGrumpyCat("Имя второго игрока не должно быть пустым")
            return

        if self._N > 30:
            self._outGrumpyCat("Параметр N должен быть меньше 30")
            return

        if self._N <= 0:
            self._outGrumpyCat("Параметр N должен быть положительным числом и больше M")
            return

        if self._M <= 0:
            self._outGrumpyCat("Параметр M должен быть положительным числом и меньше N")
            return

        self._play()

    def _event_handler(self, event):
        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                for cat in self._cat_pictures:
                    if cat.collidepoint(event.pos):  # is mouse over button
                        if cat in self._cat_home:
                            self._curr_cnt = self._M
                            break

                        self._total_score += 1

                        self._cat_home.append(cat)
                        self._curr_cnt += 1
                        self._total_cnt[self._curr_player] += 1

                        self._outScore()

                        self._screen.blit(self._cat_take, cat)
                        pygame.display.update()
                        time.sleep(2)
                        self._screen.blit(self._cat_at_home, cat)

    def _change_pic_size(self):
        self._cat = pygame.transform.scale(self._cat, self._catSize)
        self._cat_take = pygame.transform.scale(self._cat_take, self._catSize)
        self._cat_at_home = pygame.transform.scale(self._cat_at_home, self._catSize)

    def _play(self):
        self._screen.fill(self._background_color)
        self._outScore()

        is_prime = False
        rows = 1
        if self._N % 7 == 0:
            rows = 7
        elif self._N % 5 == 0:
            rows = 5
        elif self._N % 3 == 0:
            rows = 3
        elif self._N % 2 == 0:
            rows = 2
        else:
            is_prime = True

        columns = self._N // rows
        if is_prime:
            columns = (self._N - 1) // rows

        self._catSize = self._resX // rows - 50, self._resY // rows - 50
        self._change_pic_size()

        center = (self._resX // 2) - ((self._catSize[0] * rows) // 2), \
                 (self._resY // 2) - ((self._catSize[1] * columns) // 2)

        for j in range(columns):
            for i in range(rows):
                self._cat_pictures.append(self._screen.blit(self._cat, (i * self._catSize[0] + center[0],
                                                                        j * self._catSize[1] + center[1])))

        if is_prime:
            self._screen.blit(self._cat, (0, (columns + 1) * self._catSize[0]))

        pygame.display.flip()

        running = True

        while running:

            if self._total_score == self._N:
                self._outScoreWinning()
                time.sleep(5)
                break

            if self._curr_cnt >= self._M:
                self._curr_cnt = 0
                self._curr_player = not self._curr_player

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
