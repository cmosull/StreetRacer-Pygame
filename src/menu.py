from game import *

def first_menu(STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH):
    main_menu = pygame_menu.menu.Menu("Street Racer", STILL_SCREEN_WIDTH, STILL_SCREEN_HEIGHT)
    Start_Button = main_menu.add.button('Play', start_game, STILLDISPLAYSURF, STILL_FPS, Still_FramePerSec, STILL_SCREEN_HEIGHT, STILL_SCREEN_WIDTH)
    Quit_Button = main_menu.add.button('Quit', pygame_menu.events.EXIT)

    main_menu.mainloop(STILLDISPLAYSURF)

def last_menu(DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH):
    final_menu = pygame_menu.menu.Menu("Street Racer", SAME_SCREEN_WIDTH, SAME_SCREEN_HEIGHT)
    Restart_Button = final_menu.add.button('Restart', start_game, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Back_To_Main_Button = final_menu.add.button('Back to Main Menu', first_menu, DispSurf, SAME_FPS, Same_FramePerSec, SAME_SCREEN_HEIGHT, SAME_SCREEN_WIDTH)
    Quit_Button = final_menu.add.button('Quit', pygame_menu.events.EXIT)

    final_menu.mainloop(DispSurf)

