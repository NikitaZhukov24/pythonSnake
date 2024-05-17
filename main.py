# Импортировать библиотеку Pygame.
import pygame
import random

# colors
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SCREEN = (640, 480)
BLOCK_SIZE = 20


def spam_apple(snake):
    """Function generate coords for apple"""
    a = random.randrange(0, SCREEN[0]-BLOCK_SIZE, BLOCK_SIZE)
    b = random.randrange(0, SCREEN[1]-BLOCK_SIZE, BLOCK_SIZE)
    # a, b mod BLOCK_SIZE == 0
    # a, b < size[0], size[1]
    if (a, b) in snake:
        a, b = spam_apple(snake)
    # generate a, b again
    return a, b


def main():
    # Инициализировать библиотеку Pygame.
    pygame.init()
    x, y = SCREEN[0]//2, SCREEN[1]//2
    snake = [(x, y)]
    snakesize = len(snake)
    apple_x, apple_y = spam_apple(snake)
    # Создать окно размером 640x480 точек (или пикселей).
    screen = pygame.display.set_mode(SCREEN)
    # Задать окну заголовок.
    pygame.display.set_caption('Snake')

    # for moving logic
    direction_moving = {'W': True, 'A': True, 'S': True, 'D': True}
    dx, dy = 0, 0

    running = True

    # Описание главного цикла игры.
    # Этот цикл работает до тех пор, пока пользователь не закроет окно.
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Analysing pressed button on keyboard
        if keys[pygame.K_d] and direction_moving['D']:
            direction_moving = {'W': True, 'A': False, 'S': True, 'D': True}
            dx = BLOCK_SIZE
            dy = 0

        if keys[pygame.K_a] and direction_moving['A']:
            direction_moving = {'W': True, 'A': True, 'S': True, 'D': False}
            dx = -BLOCK_SIZE
            dy = 0
        if keys[pygame.K_s] and direction_moving['S']:
            direction_moving = {'W': False, 'A': True, 'S': True, 'D': True}
            dy = BLOCK_SIZE
            dx = 0
        if keys[pygame.K_w] and direction_moving['W']:
            direction_moving = {'W': True, 'A': True, 'S': False, 'D': True}
            dy = -BLOCK_SIZE
            dx = 0

            # add new block in snake
        x += dx
        y += dy
        # check x y teleport
        snake.append((x, y))

        print(snake)
        # delete last block in snake
        snake = snake[-snakesize:]
        print(snake)

        # snake teleporting cycle
        for i in range(len(snake)):
            if snake[i][0] > SCREEN[0] - BLOCK_SIZE:
                snake[i] = (0, snake[i][1])
                x = 0

            if snake[i][0] < 0:
                snake[i] = (SCREEN[0] - BLOCK_SIZE, snake[i][1])
                x = SCREEN[0] - BLOCK_SIZE

            if snake[i][1] > SCREEN[1] - BLOCK_SIZE:
                snake[i] = (snake[i][0], 0)
                y = 0

            if snake[i][1] < 0:
                snake[i] = (snake[i][0], SCREEN[1] - BLOCK_SIZE)
                y = SCREEN[1] - BLOCK_SIZE

        # snake ate apple
        if snake[-1][0] == apple_x and snake[-1][1] == apple_y:
            snakesize += 1
            apple_x, apple_y = spam_apple(snake)

        # game over
        if len(snake) != len(set(snake)):
            print("Game over")
            return
        for i, j in snake:
            pygame.draw.rect(screen, GREEN, (i, j, BLOCK_SIZE, BLOCK_SIZE))
        # pygame.draw.rect(screen, WHITE, (snake[-1][0], snake[-1][1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE))

        pygame.time.delay(100)
        # refresh display
        pygame.display.flip()
    # Деинициализирует все модули pygame, которые были инициализированы ранее.
    pygame.quit()


if __name__ == '__main__':
    main()
