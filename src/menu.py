import high_score
from game import *


def first_menu(STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH):
    main_menu = pygame_menu.menu.Menu("Street Racer", STILL_SCREEN_WIDTH, STILL_SCREEN_HEIGHT)
    Start_Button = main_menu.add.button('Play', start_game, STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH)
    Quit_Button = main_menu.add.button('Quit', pygame_menu.events.EXIT)

    main_menu.mainloop(STILLDISPLAYSURF)

##################################################################################################################################################################################

def last_menu(DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH):
    final_menu = pygame_menu.menu.Menu("Street Racer", SAME_SCREEN_WIDTH, SAME_SCREEN_HEIGHT)
    Restart_Button = final_menu.add.button('Restart', start_game, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Back_To_Main_Button = final_menu.add.button('Back to Main Menu', first_menu, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Quit_Button = final_menu.add.button('Quit', pygame_menu.events.EXIT)

    final_menu.mainloop(DispSurf)

##################################################################################################################################################################################

def high_score_menu(TopDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH, final_score):
    hs_menu = pygame_menu.menu.Menu("Street Racer", TOTAL_SCREEN_WIDTH, TOTAL_SCREEN_HEIGHT)
    high_score.high_score_add(final_score)

    hs_menu.text_input("Enter three initials: ", maxchar=3, onreturn=high_score.add_name, *final_score)

    data = high_score.read_data()

    table = hs_menu.add.table(table_id='my_table', font_size=20)
    table.default_cell_padding = 5
    table.default_row_background_color = 'white'
    for row in data:
        table.add_row(row, cell_font=pygame_menu.font.FONT_OPEN_SANS_BOLD)
    
    Back_To_Main = hs_menu.add.button("Back to Main Menu", first_menu, TopDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH)
    
    hs_menu.mainloop(TopDispSurf)

