"""Pong — Stage 4: add the right paddle (2-player, ↑/↓ arrows).

Run with:  uv run main.py

Player 1 (left):  W / S
Player 2 (right): ↑ / ↓
"""
import sys

import pygame

# --- Window ---
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)
TARGET_FPS = 60

# --- Paddle ---
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 100
PADDLE_COLOR = (255, 255, 255)
PADDLE_MARGIN = 30
PADDLE_SPEED = 6


def clamp_paddle(paddle: pygame.Rect) -> None:
    """Keep the paddle inside the window. Mutates `paddle` in place."""
    if paddle.top < 0:
        paddle.top = 0
    if paddle.bottom > WINDOW_HEIGHT:
        paddle.bottom = WINDOW_HEIGHT


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    # Both paddles start vertically centered. The left sits PADDLE_MARGIN in
    # from the left edge; the right sits PADDLE_MARGIN in from the right edge.
    paddle_y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
    left_paddle = pygame.Rect(
        PADDLE_MARGIN,
          paddle_y, 
          PADDLE_WIDTH, 
          PADDLE_HEIGHT
    )
    right_paddle = pygame.Rect(
        WINDOW_WIDTH - PADDLE_MARGIN - PADDLE_WIDTH,
        paddle_y,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    running = True
    while running:
        # 1) Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2) Update game state.
        keys = pygame.key.get_pressed()

        # Left paddle: W/S
        if keys[pygame.K_w]:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s]:
            left_paddle.y += PADDLE_SPEED

        # Right paddle: ↑/↓
        if keys[pygame.K_UP]:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            right_paddle.y += PADDLE_SPEED

        clamp_paddle(left_paddle)
        clamp_paddle(right_paddle)

        # 3) Draw the frame.
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, PADDLE_COLOR, left_paddle)
        pygame.draw.rect(screen, PADDLE_COLOR, right_paddle)
        # TODO(stage 5): draw the ball here.
        pygame.display.flip()

        # 4) Cap the frame rate.
        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
