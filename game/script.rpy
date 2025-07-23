# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define preot = Character(name="Boris", color="#cc1111")
image preot = "Priest.png"
image house = im.Scale("house.png", 1920, 1080)

default butelii_de_vin = 0


# The game starts here.

label start:
    jump awakening

    scene house
    show preot at Position(xpos=900, ypos=1500) with fade

    preot "Maria, Ion, veniti la masa! Au mai ramas doar [butelii_de_vin] butelii de vin"

    hide preot with Dissolve(10.0)

    menu:
        "Mai cauta prin casa":
            $ butelii_de_vin = 2
        "Iese afara":
            "Boris iesi pe usa, fara sa mai astepte o clipa"

    "Boris nu auzi nimic ca raspuns"

    jump looking_for_siblings

    "Unde ar putea sa fie?"

    return


label looking_for_siblings:

    scene village landscape

    show preot at Position(xpos=900, ypos=1500) with fade

    while butelii_de_vin < 10:
        preot "Ion! Maria! Am mai gasit [butelii_de_vin]! Hai veniti!"
        $ butelii_de_vin += 2

    $ mancaruri = ["placinte", "cartofi", "croissante"]
    $ mancare = 0

    while mancare <  len(mancaruri):
        preot "Hai veniti ca am gatit [mancaruri[mancare]]"
        $ mancare += 1
    
    preot "Unde sunteti?"
    
    jump looking_for_siblings

    return
