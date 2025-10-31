import pygame
import Information.global_vars as gv


class Text_Box:
    def __init__(self, text:str, text_size=12, Area_Color=(255,255,255), Border_Color=None):
        self.Border_Color = Border_Color
        self.Area_Color = Area_Color
        self.Text_Size = text_size
        self.Text = text

    def draw(self, screen, X: int, Y: int, Width: float, Height: float):
        """
        returns the rectangle, can be used for collision!
        """
        # Box
        box_surface = pygame.Surface((Width, Height))
        Box_Area = pygame.draw.rect(box_surface, self.Area_Color, ( 0, 0, Width, Height))
        if self.Border_Color != None:
            border = pygame.draw.rect(box_surface, self.Border_Color, (0, 0, Width, Height), 4)

        # Text
        font_object = pygame.font.Font(None, self.Text_Size)
        text_Surface = font_object.render(self.Text, False, (0,0,0))
        text_Box = text_Surface.get_rect(center=Box_Area.center)

        # Blitters
        box_surface.blit(text_Surface, text_Box.topleft)
        screen.blit(box_surface, (X, Y))
        return pygame.Rect(X, Y, Width, Height)

    def change_color(self, area=(200,200,200), border='black'):
        self.Area_Color = area
        self.Border_Color = border
        return 

    def clickable(self,object, rectangle: pygame.Rect):
        self.hovering( object, rectangle)
        if rectangle.collidepoint(gv.mouseX, gv.mouseY) and pygame.mouse.get_pressed()[0] == True:
            object.change_color()
            object.draw(gv.Window_Used,
                rectangle.left,
                rectangle.top,
                rectangle.width,
                rectangle.height)
            gv.hold = True
        if gv.hold is True and pygame.mouse.get_pressed()[0] == False and rectangle.collidepoint(gv.mouseX, gv.mouseY):
            gv.hold = False
            return True
        
    def hovering(self, object, rectangle: pygame.Rect, color=(240,240,240)):
        if rectangle.collidepoint(gv.mouseX, gv.mouseY):
            object.change_color(color)
            object.draw(gv.Window_Used,
                rectangle.left,
                rectangle.top,
                rectangle.width,
                rectangle.height)
