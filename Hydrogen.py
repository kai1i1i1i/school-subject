import pygame

pygame.init()

background = pygame.display.set_mode((1300, 720))
pygame.display.set_caption("1")

font = pygame.font.Font(None, 70)
text_surface = font.render("여기에 글자가 출력됩니다!", True, black)
text_rect = text_surface.get_rect()
text_rect.center = (1300 // 2, 720 // 2)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()