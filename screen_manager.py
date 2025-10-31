import Screens.Start_Screen as strt
import Screens.Sort_Selection as selc
import Screens.Sort_Display as disp

import Information.global_vars as gv

Selection = {
    "Start":strt.display,
    "Selection": selc.display,
    "Visualize": disp.display
}

def select_screen():
    Selection[gv.screen_Key]()
