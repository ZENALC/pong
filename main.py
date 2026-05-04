"""Pong — Stage 2: draw the left paddle.

Run with:  uv run main.py
"""
import sys

import pygame

# --- Window ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # black, as an (R, G, B) tuple (0-255 each)
TARGET_FPS = 60

# --- Paddle ---
# A paddle is just a tall, thin rectangle. We define its size and color here.
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 100
PADDLE_COLOR = (255, 255, 255)  # white

# How far the paddle sits from the edge of the window.
PADDLE_MARGIN = 30


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    # `pygame.Rect(x, y, width, height)` represents a rectangle. We use it
    # for both *drawing* the paddle and (later) collision checks.
    #
    # In pygame, the coordinate origin (0, 0) is the TOP-LEFT corner. X grows
    # to the right, Y grows DOWNWARD. We place the left paddle:
    #   - x: PADDLE_MARGIN pixels in from the left edge
    #   - y: vertically centered → middle of the window minus half the paddle's height
    left_paddle = pygame.Rect(
        PADDLE_MARGIN,
        WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    running = True
    while running:
        # 1) Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) Update game state. (Still nothing — paddle doesn't move yet.)

        # 3) Draw the frame.
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, PADDLE_COLOR, left_paddle)
        # TODO(stage 4): draw the right paddle here.
        pygame.display.flip()

        # 4) Cap the frame rate.
        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
