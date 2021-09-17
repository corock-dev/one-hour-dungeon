import sys

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()
    pygame.display.set_caption('첫 번째 Pygame: 키 입력 ')
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 리스트 key에 모든 키 상태 입력


        # 방향키 상/하 리스트 값을 표시할 Surface




        # 방향키 좌/우 리스트 값을 표시할 Surface



        # 스페이스/엔터 리스트 값을 표시할 Surface



        screen.fill(BLACK)

        # 문자열을 표시한 Surface 를 스크린에 전송




        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
