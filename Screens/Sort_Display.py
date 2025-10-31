import Custom_Objects.Text_Box as txt
import Custom_Objects.Bar_Graph as grph
import Algorithms as alg

import Information.global_vars as gv
import pygame


def display():

    back_button = txt.Text_Box("BACK", 32, 'white', 'black')
    bb_collision = back_button.draw(gv.Window_Used, gv.window_Width/5,
                                    gv.window_Height*0.75,
                                    gv.window_Width*0.15,
                                     gv.window_Height*0.1)
    if back_button.clickable(back_button, bb_collision):
        gv.reset_list()
        gv.reset_selected_method()
        gv.screen_Key = "Selection"

    visualize = txt.Text_Box("START", 32, 'white', 'black')
    v_collision = visualize.draw(gv.Window_Used, 3*gv.window_Width/5,gv.window_Height*0.75,gv.window_Width*0.15, gv.window_Height*0.1)
    if visualize.clickable(visualize, v_collision):
        gv.start_Sorting = True

    gv.Bar_Graph.Draw(gv.Window_Used,gv.Interger_List)
    
    if gv.start_Sorting is True:
    
        if gv.Bubble:
            alg.bubbleSort(gv.Interger_List)

        if gv.Selection:
            alg.selectionSort(gv.Interger_List)
    
        if gv.Insertion:
            alg.insertionSort(gv.Interger_List)

        if gv.Merge:
            alg.mergeSort(gv.Interger_List)

        if gv.Quick:
            alg.quickSort(gv.Interger_List)

        if gv.Bogo:
            alg.bogoSort(gv.Interger_List)

        if gv.Radix:
            alg.radixSort(gv.Interger_List)


pass




