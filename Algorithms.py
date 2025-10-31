import Information.global_vars as gv
import Custom_Objects.Bar_Graph as grph
import Custom_Objects.Text_Box as txt
import random

import pygame


def update_visuals(speed:int=60):
    """
    Mimics the initial game loop to have the game update under special conditions
    """
    gv.action_events = pygame.event.get()
    gv.mouseX, gv.mouseY = pygame.mouse.get_pos()
    for event in gv.action_events:
        if event.type == pygame.QUIT:
            pygame.quit()

    #------ RENDER HERE -----
    gv.Window_Used.fill('white')

    # Pause Button
    pause_button = txt.Text_Box("Restart", 32, 'white', 'black')
    pb_collision = pause_button.draw(gv.Window_Used, gv.window_Width/2 - gv.window_Width*0.2/2,gv.window_Height*0.75,gv.window_Width*0.2, gv.window_Height*0.1)
    if pause_button.clickable(pause_button, pb_collision):
        gv.Last_Swapped = 0
        gv.Current_bar = 0
        gv.reset_list()
        gv.start_Sorting = False
    
    # Graph
    graph = gv.Bar_Graph
    graph.Draw(gv.Window_Used, gv.Interger_List)

    # ------^^^--------

    pygame.display.flip()
    gv.clock.tick(speed)
    return

def check(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

#--------Simple Algorithms-------

def insertionSort(list: list[int]):
    if check(list): 
        gv.start_Sorting = False
        return True
    for index in range(1, len(list)):
        if gv.start_Sorting is False: break
        update_visuals()
        current = list[index]
        gv.Current_bar = index
        insert_Index = index - 1

        while insert_Index > -1 and current < list[insert_Index]:
            if gv.start_Sorting is False: break
            update_visuals()
            gv.Last_Swapped = insert_Index
            list[insert_Index + 1] = list[insert_Index]
            insert_Index-=1

        list[insert_Index + 1] = current
    return list

def bubbleSort(list: list[int]):
    if check(list) is True:
        gv.start_Sorting = False
        return list
    for whatsLeft in range(len(list)):
        for index in range(len(list)-whatsLeft-1):
            if gv.start_Sorting is False: break
            update_visuals()
            if list[index] > list[index+1]:
                swap = list[index+1]
                list[index+1] = list[index]
                list[index] = swap
                gv.Last_Swapped = index+1
            gv.Current_bar = index
        if gv.start_Sorting is False: break
    gv.start_Sorting = False
    return list

def selectionSort(list: list[int]):    
    if check(list): 
        gv.start_Sorting = False
        return list
    for start in range(len(list)):
        currMin = list[start]
        minIndex = start
        for currInd in range(start,len(list)):
            if gv.start_Sorting is False: break
            update_visuals()
            if currMin < list[currInd]:
                update_visuals()
                gv.Last_Swapped = currInd
                minIndex = currInd
                currMin = list[minIndex]
            gv.Current_bar = currInd
        if gv.start_Sorting is False: break
        gv.Current_bar = currInd
        swap = list[start]
        list[start] = currMin
        list[minIndex] = swap

    return list

def bogoSort(list: list[int]):
    if check(list):
        gv.start_Sorting = False
        return True
    while check(list) is False:
        n = len(list)
        for A in range(0, n):
            if gv.start_Sorting is False: break
            update_visuals()
            B = random.randint(0, n-1)
            tempA = list[A]
            tempB = list[B]
            list[A] = tempB
            list[B] = tempA
            gv.Last_Swapped = A
            gv.Current_bar = B
        if gv.start_Sorting is False: break

#----------^^^^^^---------------


#----------Recursive Algorithms-------------

def mergeSort(list: list[int], left:int=0, right:int=None):
    if check(list) is True:
        return list
    
    if gv.start_Sorting is False:
        gv.start_Sorting = False
        update_visuals()
        return list

    if right is None:
        right = len(list)
    update_visuals()
    if right - left > 1:  # more than one element
        middle: int = (left + right) // 2
        mergeSort(list, left, middle)
        mergeSort(list, middle, right)
        merge(list, left, middle, right)
    return list

def merge(list:list[int], left:int, middle:int, right:int):
    # copy halves into temporary lists
    left_half = list[left:middle]
    right_half = list[middle:right]

    A = 0
    B = 0

    now_left = left
    gv.Current_bar = right
    while A < len(left_half) and B < len(right_half):
        if gv.start_Sorting is False: break
        if left_half[A] <= right_half[B]:
            list[now_left] = left_half[A]
            # gv.Current_bar = A
            A += 1
        else:
            list[now_left] = right_half[B]
            # gv.Current_bar = B
            B += 1
        gv.Last_Swapped = now_left
        now_left += 1
        update_visuals()

    while A < len(left_half):
        if gv.start_Sorting is False: break
        list[now_left] = left_half[A]
        # gv.Current_bar = A
        update_visuals()
        A += 1
        gv.Last_Swapped = now_left
        now_left += 1
    while B < len(right_half):
        list[now_left] = right_half[B]
        # gv.Current_bar = B
        update_visuals()
        B += 1
        gv.Last_Swapped = now_left
        now_left += 1

def quickSort(arr, low=0, high=None):
    if check(arr):
        
        gv.start_Sorting = False
        return arr

    if high is None:
        high = len(arr) - 1

    if low < high:
        update_visuals()
        # Partition the array and get pivot index
        p = partition(arr, low, high)
        # Recurse on subarrays
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot
    i = low - 1
    
    for j in range(low, high):
        gv.Last_Swapped = i
        gv.Current_bar = j
        if gv.start_Sorting is False: break

        update_visuals()
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap in place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1













