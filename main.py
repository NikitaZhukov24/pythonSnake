# Импортировать библиотеку Pygame.
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
SCREEN = (800, 600)
BLACK = (0, 0, 0)


def main():
    # Инициализировать библиотеку Pygame.
    pygame.init()

    # Создать окно размером 800x600 точек (или пикселей).
    screen = pygame.display.set_mode(SCREEN)
    # Задать окну заголовок.
    pygame.display.set_caption('Snake')

    running = True
    snake = [80, 140]

    # Описание главного цикла игры.
    # Этот цикл работает до тех пор, пока пользователь не закроет окно.
    while running:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, pygame.Rect(snake[0], snake[1], 20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.K_DOWN == pygame.KEYDOWN:
                    snake[1] += 20



        pygame.display.update()
    # Деинициализирует все модули pygame, которые были инициализированы ранее.
    pygame.quit()


if __name__ == '__main__':
    main()


