import pygame

pygame.init()

screen = pygame.display.set_mode((450,650)) #create screen/screen size

clock = pygame.time.Clock()
logo = pygame.image.load("logo.png") #logo

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # Do logical updates here.
    # ...

    screen.fill("white")  # Fill the display with a solid color
    screen.blit(logo,(0,0)) #place logo
    # Render the graphics here.
    # ...

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)