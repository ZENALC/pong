"""Pong — Stage 6: ball bounces off the top and bottom walls.

Run with:  uv run main.py

Player 1 (left):  W / S
Player 2 (right): ↑ / ↓

The ball still flies off the LEFT and RIGHT — those are scoring zones we'll
handle in stage 8. Only top/bottom are walls.
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

# --- Ball ---
# A square Rect — easy to draw and easy to do collision with later.
BALL_SIZE = 14
BALL_COLOR = (255, 255, 255)

# Velocity (pixels per frame). Positive vx → moving right, positive vy → down.
# Starting both positive sends the ball toward the bottom-right.
BALL_INITIAL_VX = 5
BALL_INITIAL_VY = 4


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

    # Spawn the ball at the exact center of the window. We pass the top-left
    # corner to Rect, so we subtract half the ball's size to center it.
    ball = pygame.Rect(
        WINDOW_WIDTH // 2 - BALL_SIZE // 2,
        WINDOW_HEIGHT // 2 - BALL_SIZE // 2,
        BALL_SIZE,
        BALL_SIZE,
    )
    # Velocity lives outside the Rect because Rect only stores position/size,
    # not motion. We track (vx, vy) as plain ints and update the rect each frame.
    ball_vx = BALL_INITIAL_VX
    ball_vy = BALL_INITIAL_VY

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

        # Move the ball. The position+velocity update pattern — `pos += vel`
        # every frame — is the foundation of all motion in games.
        ball.x += ball_vx
        ball.y += ball_vy

        # Bounce off the top and bottom walls. The trick: when the ball
        # crosses an edge, flip the y-velocity so it heads the other way,
        # AND clamp the position back inside the wall. Without the clamp,
        # at high speeds the ball can land *past* the wall and the next
        # frame it'll still be past the wall — sign flips again — and it
        # gets stuck vibrating on the edge.
        if ball.top <= 0:
            ball.top = 0
            ball_vy = -ball_vy
        elif ball.bottom >= WINDOW_HEIGHT:
            ball.bottom = WINDOW_HEIGHT
            ball_vy = -ball_vy

        # 3) Draw the frame.
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, PADDLE_COLOR, left_paddle)
        pygame.draw.rect(screen, PADDLE_COLOR, right_paddle)
        pygame.draw.rect(screen, BALL_COLOR, ball)
        pygame.display.flip()

        # 4) Cap the frame rate.
        clock.tick(TARGET_FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
