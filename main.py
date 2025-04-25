import pygame
import sys
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import AsteroidField
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.shots_group = shots
    
    
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2, shots_group=shots)
    asteroid_field = AsteroidField()
    
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid) == True:
                sys.exit("Game Over")
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid) == True:
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

    
    
if __name__ == "__main__":
    main()
