
default is_game_over = False

init python:
    import pygame 

    class GameField(renpy.Displayable):
        def __init__(self):
            super(GameField, self).__init__()
            self.bara = Solid("#000")
            self.safe_zone = Solid("#1d8c44")
            self.indicator = Solid("#b20a0a")
            self.indicator_position = 300

            self.width = 1920
            self.height = 1080

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)

            text_location = Text(f"st={st} at={at}")
            text_element = renpy.render(text_location, 200, 200, st + 1, at + 1)
            r.blit(text_element, (100, 100))

            bara_element = renpy.render(self.bara, 1600, 200, st, at)
            r.blit(bara_element, (200, 400))
            safe_zone_element = renpy.render(self.safe_zone, 400, 200, st, at)
            r.blit(safe_zone_element, (400, 400))
            indicator_element = renpy.render(self.indicator, 50, 250, st, at)
            r.blit(indicator_element, (self.indicator_position, 380))

            renpy.redraw(self, 0)
            return r

        def event(self, ev, x, y, st):
            if (ev.type == pygame.KEYDOWN):
                if ev.key == pygame.locals.K_LEFT:
                    self.indicator_position -= 10
                elif ev.key == pygame.locals.K_RIGHT:
                    self.indicator_position += 10


screen bar_minigame:
    add "village landscape"
    default field = GameField()
    add field


label minigame:
    call screen bar_minigame
    if _return:
        "Ai castigat"
    else:
        "Ai pierdut"

