import Custom_Objects.Text_Box as txt
import Information.global_vars as gv
import Custom_Objects.Bar_Graph as grph
import pygame

def display():

    # Title 
    Title = txt.Text_Box("Algorithm Visualizer 2", 48, 'White', 'black ')
    Title.draw(gv.Window_Used,
            gv.window_Width/2 - (2*gv.window_Width/3)/2,
            gv.window_Height/6,
            2* gv.window_Width/3,
            gv.window_Height/6)
    
    # !variables! ------
    colX = 2.5*gv.window_Width/12
    butt_width = gv.window_Width/5
    butt_height = gv.window_Height/10
    #  -------

    # Draws a graph
    grph.Bar_Graph(4*gv.window_Width/10,
                3*gv.window_Height/8, 
                gv.window_Width/2,
                3*gv.window_Height/8
                ).Draw(gv.Window_Used, gv.Interger_List)

    # Start button
    start_button = txt.Text_Box("View Algorithms", 32, 'white', 'black')
    sb_collision = start_button.draw(gv.Window_Used,
                    colX - butt_width/2,
                    gv.window_Height*0.40,
                    butt_width,
                    butt_height)
    start_button.hovering(start_button, sb_collision)
    if start_button.clickable(start_button, sb_collision) is True:
        gv.Bar_Graph = grph.Bar_Graph( gv.window_Width/2 - gv.window_Width*(8/9)/2, gv.window_Height/10 ,gv.window_Width*(8/9),gv.window_Height/2)
        gv.screen_Key = "Selection"

# Credits section
    txt.Text_Box("Application by Grayson Gnassounou,", 24, 'white'
                 ).draw(gv.Window_Used, gv.window_Width*0.05, gv.window_Height*0.55, gv.window_Width/3, gv.window_Height/15)
    txt.Text_Box("made in python with pygame", 24, 'white'
                 ).draw(gv.Window_Used, gv.window_Width*0.05, gv.window_Height*0.6, gv.window_Width/3, gv.window_Height/15)


    
    return




