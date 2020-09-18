import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 960
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# create game objects
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 -70, 10, 140)

# set game variables
background = pygame.Color('grey12')
grey = pygame.Color(200,200,200)
vel = 6
vel_x = vel * random.choice((1,-1))
vel_y = vel * random.choice((1,-1))
player_speed = 0
opponent_speed = 6 #change to increase or decrease difficulty

# set text variables
player_score = 0
opponent_score = 0
font = pygame.font.Font("freesansbold.ttf", 32)

# timer
time_score = None

def reset_ball(vel_x, vel_y, ball):
    ball.center = (screen_width/2, screen_height/2)
    vel_y *= random.choice((1, -1))
    vel_x *= random.choice((1, -1))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += vel
            if event.key == pygame.K_UP:
                player_speed -= vel

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= vel
            if event.key == pygame.K_UP:
                player_speed += vel

    ball.x += vel_x
    ball.y += vel_y

    # ball animation
    if ball.top <= 0 or ball.bottom >= screen_height:
        vel_y *= -1

    if ball.left <= 0:  
        reset_ball(vel_x, vel_y, ball)
        player_score += 1

    if ball.right >= screen_width:
        reset_ball(vel_x, vel_y, ball)
        opponent_score += 1

    if ball.colliderect(player) or ball.colliderect(opponent):
        vel_x *= -1
    
    # player animation
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

    # opponent animation
    if opponent.top < ball.y:
        opponent.top += opponent_speed
        
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
         
    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
    # draw objects
    window.fill(background)
    pygame.draw.rect(window, grey, player)
    pygame.draw.rect(window, grey, opponent)
    pygame.draw.ellipse(window, grey, ball)
    pygame.draw.aaline(window, grey, (screen_width/2, 0), (screen_width/2, screen_height))

    # display score
    player_text = font.render(f"{player_score}", False, grey)
    window.blit(player_text, (screen_width/2 + 10, 10))
    opponent_text = font.render(f"{opponent_score}", False, grey)
    window.blit(opponent_text, (screen_width/2 - 25, 10))

    # announce winner
    if player_score == 5:
        win_text = font.render("Player Wins", False, grey)
        window.blit(win_text, (700, 450))
        pygame.time.delay(1000)
        run = False

    if opponent_score == 5:
        win_text = font.render("Opponent Wins", False, grey)
        window.blit(win_text, (250, 450))
        pygame.time.delay(1000)
        run = False

    pygame.display.flip()
    clock.tick(60)