import sys

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def main():
    # pygame 모듈 초기화
    pygame.init()

    # 윈도우에 표시할 타이틀 지정
    pygame.display.set_caption('첫 번째 Pygame')

    # 그릴 화면(스크린) 초기화
    screen = pygame.display.set_mode((800, 600))

    # clock 오브젝트 초기화
    clock = pygame.time.Clock()

    # font 오브젝트 초기화
    font = pygame.font.Font(None, 80)

    # 시간 관리 변수 tmr 선언
    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Surface 에 문자열 표시
        txt = font.render(str(tmr), True, WHITE)

        # 지정한 색으로 스크린 전체 채움
        screen.fill(BLACK)

        # 문자열 표시한 Surface 를 스크린으로 전송
        screen.blit(txt, [300, 200])

        # 화면 업데이트
        pygame.display.update()

        # Framerate 지정
        clock.tick(10)


if __name__ == '__main__':
    main()
