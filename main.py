import pygame
import screen_manager as mgmt
import Information.global_vars as gv

def main():
    pygame.init()
    gv.Window_Used = pygame.display.set_mode((1280, 720))
    gv.clock = pygame.time.Clock()
    running = True
    gv.window_Width = gv.Window_Used.get_width()
    gv.window_Height = gv.Window_Used.get_height()

    while running:
        gv.mouseX, gv.mouseY = pygame.mouse.get_pos()
        gv.action_events = pygame.event.get()
        for event in gv.action_events:
            if event.type == pygame.QUIT:
                running = False

        gv.Window_Used.fill("white")

        #------ ------ -----RENDER YOUR GAME HERE------ ------ ------

        mgmt.select_screen()
        
        #----^^^---- ------ ------ ------ ------ ------ ------ ------
        
        pygame.display.flip()
        gv.clock.tick(gv.fps)  # limits FPS to 60
    pygame.quit()

if __name__ == "__main__":
    main()
    

