import pygame
import sys

# Initialize Pygame
pygame.init()
black=(0,0,0)
# Set up the second window
width, height = 700, 300
second_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("RULES")

t=pygame.font.SysFont('calibri',48)
t2=pygame.font.SysFont('calibri',28)
second_window.fill((144,238,144))
r1=t.render("RULES",True,black)
r11=r1.get_rect()
r11.center=(340,50)

r2=t2.render("1.  For Changing direction use arrow keys in keyboard",True,black)
r22=r2.get_rect()
r22.topleft=((0,100))
r3=t2.render("2.  For Moving in direction select direction and press Y",True,black)
r33=r3.get_rect()
r33.topleft=((0,150))
r4=t2.render("3.  Press Enter to collect gold, To win you need to collect gold ",True,black)
r44=r4.get_rect()
r44.topleft=((0,200))
r5=t2.render("4.  Press Space to shoot arrow, Arrow will kill zombies",True,black)
r55=r5.get_rect()
r55.topleft=((0,250))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    second_window.blit(r1,r11)
    second_window.blit(r2,r22)
    second_window.blit(r3,r33)
    second_window.blit(r4,r44)
    second_window.blit(r5,r55)
    pygame.display.update()

