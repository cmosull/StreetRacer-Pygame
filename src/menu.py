import game
import csv

def player_add_name(value):
    if (game.first_time_check == 0):
        game.high_score.add_name(value.upper())

###################################################################################################################################################################################

def first_menu(STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH):
    game.first_time_check = 0
    main_menu = game.pygame_menu.menu.Menu("Street Racer", STILL_SCREEN_WIDTH, STILL_SCREEN_HEIGHT)

    Start_Button = main_menu.add.button('Play', game.start_game, STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH, game.TotalScore)
    main_menu.add.label("",font_size=12)
    Quit_Button = main_menu.add.button('Quit', game.pygame_menu.events.EXIT)

    main_menu.mainloop(STILLDISPLAYSURF)

##################################################################################################################################################################################

def last_menu(DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH):
    final_menu = game.pygame_menu.menu.Menu("Street Racer", SAME_SCREEN_WIDTH, SAME_SCREEN_HEIGHT)
    Restart_Button = final_menu.add.button('Restart', game.start_game, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH, game.TotalScore)
    HighScore_Button = final_menu.add.button('View High Scores', high_score_view_menu, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Back_To_Main_Button = final_menu.add.button('Back to Main Menu', first_menu, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Quit_Button = final_menu.add.button('Quit', game.pygame_menu.events.EXIT)

    final_menu.mainloop(DispSurf)

##################################################################################################################################################################################

def high_score_menu(TopDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH, final_score, check):
    hs_menu = game.pygame_menu.menu.Menu("Street Racer", TOTAL_SCREEN_WIDTH, TOTAL_SCREEN_HEIGHT)
    
    if (check == 0):
        game.TotalScore = final_score
        game.high_score.high_score_add(final_score)


    hs_menu.add.label("Enter 3 initials and press Return",font_size=24)
    hs_menu.add.text_input("", maxchar=3, onreturn=player_add_name)
    hs_menu.add.label("",font_size=12)

    table = hs_menu.add.table(table_id='my_table', font_size=20)
    table.default_cell_padding = 5
    #table.default_row_background_color = 'white'
    for row in list(csv.reader(open('scores.csv', newline=''))):
        table.add_row(row, cell_font = game.pygame_menu.font.FONT_OPEN_SANS_BOLD)
    
    hs_menu.add.label("",font_size=12)
    hs_menu.add.button("Update High Scores", high_score_menu, TopDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH, final_score, 1, font_size=24)
    hs_menu.add.label("",font_size=12)
    Back_To_Main = hs_menu.add.button("Back to Main Menu", first_menu, TopDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH, font_size=24)

    hs_menu.mainloop(TopDispSurf)

###################################################################################################################################################################################

def high_score_view_menu(AnotherDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH):
    hs_view_menu = game.pygame_menu.menu.Menu("Street Racer", TOTAL_SCREEN_WIDTH, TOTAL_SCREEN_HEIGHT)

    table = hs_view_menu.add.table(table_id='my_table', font_size=20)
    table.default_cell_padding = 5
    table.default_row_background_color = 'white'
    for row in list(csv.reader(open('scores.csv', newline=''))):
        table.add_row(row, cell_font = game.pygame_menu.font.FONT_OPEN_SANS_BOLD)
    
    Back_To_Main = hs_view_menu.add.button("Back to Main Menu", first_menu, AnotherDispSurf, TOTAL_FPS, Total_FramePerSec, TOTAL_SCREEN_HEIGHT, TOTAL_SCREEN_WIDTH)
    
    hs_view_menu.mainloop(AnotherDispSurf)

