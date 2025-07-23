
default is_game_over = False

init python:
    class GameField(renpy.Displayable):

        def __init__(self):
            pass

        def render(self, width, height, st, at):
            pass


screen bar_minigame:
    add "village landscape"
    default field = GameField()
    add field
    if is_game_over:
        Return(True)


label minigame:
    call screen bar_minigame

    if _return:
        "Ai castigat"
    else:
        "Ai pierdut"

