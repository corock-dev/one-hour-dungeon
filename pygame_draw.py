import math
import sys

import pygame

WHITE =
BLACK =
RED =
GREEN =
BLUE =
GOLD = (255, 216, 0)
SILVER = (192, 192, 192)
COPPER = (192, 112, 48)


def main():
    pygame.init()
    pygame.display.set_caption('첫 번째 Pygame: 도형')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    tmr = 0

    while True:
        tmr = tmr + 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # 선 표시




        # 사각형 표시



        # 다각형 표시



        # 원 표시


        # 타원 표시



        # 원호 각도 계산






        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
