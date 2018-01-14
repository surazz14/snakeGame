import pygame
pygame.init()
red=(255,0,0)
black=(255,255,255)
fps=30
display_width=800
display_height=600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("snake game")
gameExit = False
lead_x=display_width/2
lead_y=display_height/2
lead_x_change=0
lead_y_change=0
block_size=10
clock=pygame.time.Clock()
while not gameExit:
        for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                        gameExit = True
                if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_LEFT:
                                lead_x_change=-block_size
                                lead_y_change=0
                        elif event.key==pygame.K_RIGHT:
                                lead_x_change=block_size
                                lead_y_change=0
                        elif event.key==pygame.K_UP:
                                lead_y_change=-block_size
                                lead_x_change=0
                        elif event.key==pygame.K_DOWN:
                                lead_y_change=block_size
                                lead_x_change=0
        if lead_x>=display_width or lead_x<=0 or lead_y>=display_height or lead_y<=0:
                gameExit = True

        lead_x+=lead_x_change
        lead_y+=lead_y_change

                #print(event)
        screen.fill(red)
        pygame.draw.rect(screen,black,[lead_x,lead_y,15,15])
        pygame.display.update()
        clock.tick(fps)

pygame.quit()
quit()
