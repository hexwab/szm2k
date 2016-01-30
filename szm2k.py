import random, pygame, pygame.gfxdraw
from pygame.locals import *

class game:
    width = 1280
    height = 720
    running = True
    lanes = 5
    columns = 10
    scale = 1280 / 32
    top_border = 5
    left_border = 2
    plantsize = 1
    spacing = 2
    money = 50
    money_spawn_rate = 200
    money_spawn_amount = 10
    plantcost = 20
    frame = 0

def init_plants():
    game.plants = []
    for y in xrange(0,game.lanes):
        lane = []
        for x in xrange(0,game.columns):
            lane.append(False)
        game.plants.append (lane)
        
def spawn(x,y):
    if game.plants[y][x] or game.money < game.plantcost:
        return False
    
    game.plants[y][x] = True
    game.money -= game.plantcost
    return True

def init_zombies():
    game.zombies = []
    
        
def loop():
    ZOMBIE = (40,120,70)
    PLANT = (255,0,0)
    EMPTY = (40,0,0)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    game.clock.tick(60)
    game.frame = game.frame + 1

    if not game.frame % game.money_spawn_rate:
        game.money = game.money + game.money_spawn_amount
    
    pygame.draw.rect(game.screen, BLACK, (0,0,game.width,game.height))

    game.screen.blit(game.font.render("$"+str(game.money), True, WHITE), (2*game.scale, 2*game.scale))

    
    for y in xrange(0,game.lanes):
        for x in xrange(0,game.columns):
            if (game.plants[y][x]):
                pygame.draw.rect(game.screen, PLANT, ((game.left_border + x*game.spacing) * game.scale,
                                                    (game.top_border + y*game.spacing) * game.scale,
                                                    game.plantsize * game.scale, game.plantsize * game.scale))
            else:
                pygame.draw.rect(game.screen, EMPTY, ((game.left_border + x*game.spacing) * game.scale,
                                                    (game.top_border + y*game.spacing) * game.scale,
                                                    game.plantsize * game.scale, game.plantsize * game.scale))

                
    # Controls
    for event in pygame.event.get():
        if event.type == QUIT:
            game.running = False
            return
        elif event.type == KEYDOWN:
            if event.key == ord('q'):
                game.running = False # Quit
            elif event.key == ord('f'):
                pygame.display.toggle_fullscreen()
                print 43

        elif event.type == MOUSEBUTTONDOWN:
            pos = (event.pos[0] / game.scale, event.pos[1] / game.scale)
            if (pos[0] >= game.left_border and
                pos[1] >= game.top_border):
                gamepos = (pos[0] - game.left_border,
                           pos[1] - game.top_border)

                if (gamepos[0] % game.spacing < game.plantsize and
                    gamepos[1] % game.spacing < game.plantsize):
                    x = gamepos[0] / game.spacing
                    y = gamepos[1] / game.spacing
                    if (x < game.columns and y < game.lanes):
                        print spawn (x,y)

def main():
    pygame.init()
    pygame.display.set_caption('Super Zombie Massacre 2000!!')
    pygame.key.set_repeat(20, 20)
    game.screen = pygame.display.set_mode((game.width,game.height))
    game.clock = pygame.time.Clock()
    game.font = pygame.font.Font(None, game.scale)

    init_plants()
    
    while game.running:
        loop()
        pygame.display.flip()

    pygame.quit()

#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()


