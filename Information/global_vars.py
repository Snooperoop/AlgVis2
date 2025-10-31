import random
# ------Pygame related Variables------#
Window_Used = None
window_Width:int = None
window_Height:int = None
clock = None
fps: int = 60

mouseX, mouseY = 0, 0
action_event: list = None
hold: bool = False
# --------List related Variables-------#
Current_bar: int = None
Last_Swapped: int = None
list_length = 100
Interger_List: list[int] = [0] * list_length
for i in range(len(Interger_List)):
    Interger_List[i] = i
random.shuffle(Interger_List)

def remake_list():
    global Interger_List
    new_List: list[int] = [0] * list_length
    for i in range(len(new_List)):
        new_List[i] = i
    Interger_List = new_List
    random.shuffle(Interger_List)
    reset_list()
    return 

def reset_list():
    random.shuffle(Interger_List)
    return 

start_Sorting: bool = False
#--------Sorting Method Selected----------#

Bubble:bool = False
Bogo:bool = False
Insertion:bool = False
Quick: bool = False
Selection:bool = False
Merge: bool = False
Radix: bool = False
Shell: bool = False

def reset_selected_method():
    global Bubble, Bogo, Insertion, Quick, Selection, Merge, Heap, Shell
    Last_Swapped = 0
    Current_bar = 0
    Bubble = False
    Bogo = False
    Insertion = False
    Quick = False
    Selection = False
    Merge = False
    Heap = False
    Shell = False


# --------Screen Objects--------------#
screen_Key: str = "Start"
Bar_Graph = None

# 



