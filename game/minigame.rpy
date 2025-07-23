
default is_game_over = False

init python:
    class GameField(renpy.Displayable):

        def __init__(self):
            super(GameField, self).__init__()
            self.bara = Solid("#000")
            self.safe_zone = Solid("#1d8c44")
            self.indicator = Solid("#b20a0a")

            self.width = 1920
            self.height = 1080

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)
            bara_element = renpy.render(self.bara, 1600, 200, st, at)
            r.blit(bara_element, (200, 400))
            renpy.redraw(r, 0)
            return r


screen bar_minigame:
    add "village landscape"
    default field = GameField()
    add field


label minigame:
    window hide 
    $ quick_menu = False

    call screen bar_minigame

    $ quick_menu = True
    window show
    if _return:
        "Ai castigat"
    else:
        "Ai pierdut"

