import sys

import pygame


def main():
    pygame.init()
    pygame.display.set_caption('첫 번째 Pygame: 이미지 표시')
    screen = pygame.display.set_mode((640, 360))
    clock = pygame.time.Clock()

    # 배경 이미지 로딩


    # 캐릭터 이미지 로딩


    tmr = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 키를 누르는 이벤트 발생 처리

                # F1 키라면 풀 스크린 모드로 전환




                # F2 키 또는 ESC 키라면 일반 스크린 모드로 전환



        # tmr 값을 배경 스크롤 값으로부터 계산


        # 반복해서 옆으로 5장만큼

            # 배경 이미지 표시


        # 캐릭터를 애니메이션해서 표시


        pygame.display.update()
        clock.tick(5)


if __name__ == '__main__':
    main()
