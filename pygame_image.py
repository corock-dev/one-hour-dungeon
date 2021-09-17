import sys

import pygame


def main():
    pygame.init()
    pygame.display.set_caption('첫 번째 Pygame: 이미지 표시')
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()

    # 배경 이미지 로딩
    img_bg = pygame.image.load('pg_bg.png')

    # 캐릭터 이미지 로딩
    img_chara = [pygame.image.load('pg_chara0.png'),
                 pygame.image.load('pg_chara1.png')]
    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 키를 누르는 이벤트 발생 처리
            if event.type == pygame.KEYDOWN:
                # F1 키라면 풀 스크린 모드로 전환
                if event.key == pygame.K_F1:
                    screen = pygame.display.set_mode((640, 360),
                                                     pygame.FULLSCREEN)

                # F2 키 또는 ESC 키라면 일반 스크린 모드로 전환
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screen = pygame.display.set_mode((640, 360))

        # tmr 값을 배경 스크롤 값으로부터 계산
        x = tmr % 160

        # 반복해서 옆으로 5장만큼
        for i in range(5):
            # 배경 이미지 표시
            screen.blit(img_bg, [i * 160 - x, 0])

        # 캐릭터를 애니메이션해서 표시
        screen.blit(img_chara[tmr % 2], [224, 160])

        pygame.display.update()
        clock.tick(5)


if __name__ == '__main__':
    main()
