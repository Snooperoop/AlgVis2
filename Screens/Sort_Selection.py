import Custom_Objects.Text_Box as txt
import Information.global_vars as gv
import pygame

def display():

    back_button = txt.Text_Box("BACK", 48, 'white', 'black')
    bb_collision = back_button.draw(gv.Window_Used, gv.window_Width/50, gv.window_Height/100 ,gv.window_Width*0.25 *0.9, gv.window_Height*0.15 * 0.9)
    if back_button.clickable(back_button, bb_collision):
        gv.screen_Key = "Start"

    butt_wid: float = gv.window_Width*0.20
    butt_het: float =  gv.window_Height*0.10

    row1Y = 5*gv.window_Height/14
    row2Y = 7*gv.window_Height/14
    row3Y = 9*gv.window_Height/14
    row4Y = 11*gv.window_Height/14
    row5Y = 11*gv.window_Height/14


    # Column 1
    col1X = 2*gv.window_Width/12 - butt_wid/2

    Selection_Sort = txt.Text_Box("Selection Sort", 32, "white", "black")
    ssRect = Selection_Sort.draw(gv.Window_Used, col1X, row1Y, butt_wid, butt_het)
    if Selection_Sort.clickable(Selection_Sort, ssRect):
        gv.Selection = True
        gv.screen_Key = "Visualize"

    Bubble_Sort = txt.Text_Box("Bubble Sort", 32, "white", "black")
    bubRect = Bubble_Sort.draw(gv.Window_Used, col1X, row2Y, butt_wid, butt_het)
    if Bubble_Sort.clickable(Bubble_Sort, bubRect):
        gv.Bubble = True
        gv.screen_Key = "Visualize"

    Insertion_Sort = txt.Text_Box("Insertion Sort", 32, "white", "black")
    insRect = Insertion_Sort.draw(gv.Window_Used, col1X, row3Y, butt_wid, butt_het)
    if Insertion_Sort.clickable(Insertion_Sort,insRect):
        gv.Insertion = True
        gv.screen_Key = "Visualize"

    # Column 2

    col2X = 5*gv.window_Width/12 - butt_wid/2

    Quick_Sort = txt.Text_Box("Quick Sort", 32, "white", "black")
    qsRECT = Quick_Sort.draw(gv.Window_Used, col2X, row2Y, butt_wid, butt_het)
    if Quick_Sort.clickable(Quick_Sort, qsRECT):
        gv.Quick = True
        gv.screen_Key = "Visualize"

    merge_Sort = txt.Text_Box("Merge Sort", 32, "white", "black")
    mgsRECT = merge_Sort.draw(gv.Window_Used, col2X, row1Y, butt_wid, butt_het)
    if merge_Sort .clickable(merge_Sort, mgsRECT):
        gv.Merge = True
        gv.screen_Key = "Visualize"


    BOGO_Sort = txt.Text_Box("BOGO Sort", 32, "white", "black")
    bogoRect = BOGO_Sort.draw(gv.Window_Used, col2X, row3Y, butt_wid, butt_het)
    if BOGO_Sort.clickable(BOGO_Sort,bogoRect):
        gv.Bogo = True
        gv.screen_Key = "Visualize"

    # shell_Sort = txt.Text_Box("Shell Sort", 32, "white", "black")
    # shellRECT = shell_Sort.draw(gv.Window_Used, col2X, row4Y, butt_wid, butt_het)
    # if shell_Sort.clickable(shell_Sort, shellRECT):
    #     gv.Shell = True
    #     gv.screen_Key = "Visualize"

    # radix_Sort = txt.Text_Box("Radix Sort", 32, "white", "black")
    # radRECT = radix_Sort.draw(gv.Window_Used, col2X, row3Y, butt_wid, butt_het)
    # if radix_Sort.clickable(radix_Sort,radRECT):
    #     gv.Radix= True
    #     gv.screen_Key = "Visualize"


    content_name = txt.Text_Box("Algorithms", 48)
    content_name.draw(gv.Window_Used, (col1X + col2X)/2,  row1Y - row1Y*0.3333, 300, 70 )


    # Second half of the screen -------------------

    col3X = gv.window_Width/15


    content_name2A = txt.Text_Box("Number of Elements:", 36, 'white').draw(gv.Window_Used, (9.5+14.75)/2 * col3X - butt_wid*0.75 , row3Y - row3Y*0.15 , butt_wid, butt_het )
    content_name2B = txt.Text_Box( str(gv.list_length), 38, 'white').draw(gv.Window_Used, (9.5+14.75)/2 * col3X - butt_wid*0.75, row3Y - row3Y*0.05, butt_wid, butt_het*0.65 )
    

    element_decider1 = txt.Text_Box("10 Item Sort", 24, 'white', 'black')
    ed1rect = element_decider1.draw(gv.Window_Used, 9.5*col3X - butt_wid/2, row4Y - row4Y*0.1 , butt_wid*0.5, butt_het*0.8  )
    if element_decider1.clickable(element_decider1, ed1rect):
        gv.list_length = 10
        gv.remake_list()

    element_decider2 =  txt.Text_Box("100 Item Sort", 24, 'white', 'black')
    ed2rect = element_decider2.draw(gv.Window_Used, 11.25*col3X - butt_wid/2, row4Y - row4Y*0.1 , butt_wid*0.5, butt_het*0.8 )
    if element_decider2.clickable(element_decider2, ed2rect):
        gv.list_length = 100
        gv.remake_list()

    element_decider3 =  txt.Text_Box("500 Item Sort", 24, 'white', 'black')
    ed3rect = element_decider3.draw(gv.Window_Used, 13*col3X - butt_wid/2, row4Y - row4Y*0.1 , butt_wid*0.5, butt_het*0.8 )
    if element_decider3.clickable(element_decider3, ed3rect):
        gv.list_length = 500
        gv.remake_list()
    
    element_decider4 =  txt.Text_Box("1000 Item Sort", 24, 'white', 'black')
    ed4rect = element_decider4.draw(gv.Window_Used, 14.75*col3X - butt_wid/2, row4Y - row4Y*0.1 , butt_wid*0.5, butt_het*0.8 )
    if element_decider4.clickable(element_decider4, ed4rect):
        gv.list_length = 1000
        gv.remake_list()


    pass