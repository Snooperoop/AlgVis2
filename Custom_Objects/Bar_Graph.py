import pygame
import Information.global_vars as gv

class Bar_Graph:
    def __init__(self, x=0, y=0, width=100, height=100):
        self.X = x
        self.Y = y
        self.Width = width
        self.Height = height
        pass

    def change_pos(self,X,Y,Width,Height):
        self.X = X
        self.Y = Y
        self.Width = Width
        self.Height = Height

    def Draw(self, surface, List: list[int]):
        box_width = self.Width
        box_height = self.Height

        box_surface = pygame.Surface((box_width, box_height))
        box_area = pygame.draw.rect(box_surface, 'black', (0, 0,  box_width, box_height)) 
        box_border = pygame.draw.rect(surface, 'gray', (self.X - 10, self.Y - 10, self.Width + 20, self.Height + 20), 10)

        # Draw the bars of the graph!
        number_of_bars: int = len(List)
        for i in range(number_of_bars):
            if  gv.Last_Swapped == i: lastColor = 'red'
            elif gv.Current_bar == i: lastColor = 'green'
            else: lastColor = 'white'
            pygame.draw.rect(box_surface,
                            lastColor, #BAR COLOR
                            (i*box_width/number_of_bars, 0, box_width/number_of_bars, List[i]*box_height/number_of_bars))

        # Transform and rotate the box_surface to 
        box_surface = pygame.transform.rotate(box_surface, 180)
        box_surface = pygame.transform.flip(box_surface,True,False)

        # Display it!
        surface.blit(box_surface,(self.X, self.Y))
        return box_surface
    
