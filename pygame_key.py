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
        key = pygame.key.get_pressed()

        # 방향키 상/하 리스트 값을 표시할 Surface
        txt1 = font.render(
            'UP' + str(key[pygame.K_UP]) + ' DOWN' + str(key[pygame.K_DOWN]),
            True, WHITE, GREEN)

        # 방향키 좌/우 리스트 값을 표시할 Surface
        txt2 = font.render('LEFT' + str(key[pygame.K_LEFT]) + ' RIGHT' + str(
            key[pygame.K_RIGHT]), True, WHITE, BLUE)

        # 스페이스/엔터 리스트 값을 표시할 Surface
        txt3 = font.render('SPACE' + str(key[pygame.K_SPACE]) + ' ENTER' + str(
            key[pygame.K_RETURN]), True, WHITE, RED)

        screen.fill(BLACK)

        # 문자열을 표시한 Surface 를 스크린에 전송
        screen.blit(txt1, [100, 100])
        screen.blit(txt2, [100, 200])
        screen.blit(txt3, [100, 300])

        pygame.display.update()
        clock.tick(10)


if __name__ == '__main__':
    main()
