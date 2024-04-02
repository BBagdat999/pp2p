import pygame
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect , ball_rect)
dx, dy = 1, -1

game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('lab8_catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

block_list = [(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), False) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(10) for j in range(4)]

bonus_blocks = [(pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50), True) for i in range(5) for j in range(1)]
color_list += [(0, 255, 0) for _ in range(5)] 

unbreak = random.sample(range(len(block_list)), 5)  
for i in unbreak:
    block_list[i] = (block_list[i][0], True)  

print(block_list)

losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

time_passed = 0  
time_to_shrink = 5  

time_to_increase_speed = 5 

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    for i, (block, is_unbreakable) in enumerate(block_list):
        pygame.draw.rect(screen, color_list[i], block)
    
    for block, _ in bonus_blocks:
        pygame.draw.rect(screen, (0, 255, 0), block)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)


    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy
 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy 
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    for i, (block, is_unbreakable) in enumerate(block_list):
        if ball.colliderect(block):
            if is_unbreakable:
                dx, dy = detect_collision(dx, dy, ball, block)
            else:
                block_list.pop(i)
                color_list.pop(i)
                dx, dy = detect_collision(dx, dy, ball, block)
                game_score += 1
                collision_sound.play()
                break 
    
    for i, (block, _) in enumerate(bonus_blocks):
        if ball.colliderect(block):
            ballSpeed += 2 
            bonus_blocks.pop(i)
            color_list.pop(i + len(block_list)) 

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not any(not is_unbreakable for _, is_unbreakable in block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
    else:
        time_passed += clock.get_rawtime() / 1000  
        if time_passed >= time_to_shrink:
            time_passed -= time_to_shrink  

            paddleW -= 10  
            paddle.width = paddleW  
            paddle.x += 3 

        time_to_increase_speed -= clock.get_rawtime() / 1000
        if time_to_increase_speed <= 0:
            time_to_increase_speed = 5
            ballSpeed += 1  

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)