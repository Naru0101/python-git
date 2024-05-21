import pygame
import random

pygame.init()
width, height = 1367, 678
window_start = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer game")

player_width, player_height = 50, 40
player_color = (128, 0, 128)
player_jump = 10
player_speed = 10

barrier_color = (0, 255, 0)
barrier_speed = 6
barrier_width, barrier_height = 50, 40

score = 0

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.is_jump = False

    def draw(self, win):
        pygame.draw.rect(win, player_color, (self.x, self.y, player_width, player_height))

class Barrier:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, barrier_color, (self.x, self.y, self.width, self.height))

def draw_window(player, barriers):
    window_start.fill((0, 0, 0))
    player.draw(window_start)
    for barrier in barriers:
        barrier.draw(window_start)
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    window_start.blit(text, (10, 10))
    pygame.display.update()

def main():
    global score, barrier_speed
    player = Player(50, height - player_height)
    barriers = []
    clock = pygame.time.Clock()
    run = True
    barrier_speed_default = barrier_speed
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not player.is_jump:
            player.is_jump = True
            player.vel = -player_jump
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if keys[pygame.K_LSHIFT]:
            barrier_speed = barrier_speed_default * 2
        else:
            barrier_speed = barrier_speed_default

        if player.is_jump:
            player.y += player.vel
            player.vel += 0.5
            if player.y >= height - player_height:
                player.y = height - player_height
                player.is_jump = False

        if random.randrange(0, 100) == 0:
            barrier_width_rand = random.randint(30, 70)
            barrier_height_rand = random.randint(30, 70)
            barriers.append(Barrier(width, height - barrier_height_rand, barrier_width_rand, barrier_height_rand))

        for barrier in barriers:
            barrier.x -= barrier_speed
            if barrier.x < -barrier.width:
                barriers.remove(barrier)
                score += 1

            if (barrier.x < player.x + player_width and barrier.x + barrier.width > player.x
                    and barrier.y < player.y + player_height and barrier.y + barrier.height > player.y):
                run = False

        draw_window(player, barriers)

    pygame.quit()

if __name__ == "__main__":
    main()            