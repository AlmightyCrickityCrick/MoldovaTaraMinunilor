image preot_lumanare = "Priest holding candle.png"
image butoi_vin =im.Scale("barrel.png", 100, 200)

default butoaie = 0

init python:
    import random
    def afiseaza_random_nr_butoaie():
        return random.randint(0, 4)

    def colecteaza_butoi():
        globals()['butoaie'] += 1
        renpy.hide_screen("butoi")
        return

screen butoi(x, y):
    imagebutton:
        xalign 0.5
        yalign 0.5
        idle "butoi_vin"
        action Function(colecteaza_butoi)

screen numarator_butoaie():
    frame:
        xalign 0.5
        yalign 0.1
        vbox:
            text "butoaie: [butoaie] "



label awakening:
    scene house
    show preot at Position(xpos=900, ypos=1500) with fade
    show screen butoi(540, 960)
    show screen numarator_butoaie
    preot "Maria, Ion, veniti la masa! Avem doar [butoaie] butoaie ramase"

    hide preot

    "Boris se incrunta cand auzi drept raspuns liniste"

    "Geminii nu aveau obiceiul de a ramane tacuti pe mult timp"

    "Ceva se intamplase"

    menu:
        "Verifica ce fac gemenii":
            "Linistea la ora aceasta nu este un semn bun"
            "Boris isi lua o lumanare si pleca sa verifice"
            jump check_the_corridor
        "Vede-ti de treaba":
            "Boris stia ca nu putea sa se intample nimic celor doi in propria casa, asa ca decise sa nu isi faca prea multe griji"
            jump bad_end
        
    return


label check_the_corridor:
    scene house:
        matrixcolor SaturationMatrix(0)
    
    show preot_lumanare at Position(xpos=900, ypos=1500, zorder=2) with fade

    preot "Maria! Ion! [butoaie] BUTOAIE"

    "Cu cat Boris se adancea in casa, cu atat devenea mai intunecata privelistea"

    "La un moment dat simti cum cineva ii sufla in ceafa"

    menu:
        "Intoarce-te sa vezi ce se afla in spate":
            "Boris se opri in loc"
            "Incetul cu incetul, el isi intoarse corpul"
            "Insa cand urma sa dea cu ochii peste intrus"
            "Intuneric"
            jump bad_end
        "Continua drumul":
            "Boris stia ca orice ar fi fost in spatele sau zacea in asteptare de a fi observat"
            "Pastrandu-si privirea inainte, Boris isi urma drumul"
            jump twins_dissapearing
    return

label bad_end:
    scene house:
        matrixcolor BrightnessMatrix(1)
    "Si lumina"
    "Boris isi deschide ochii in locul din care a plecat, fara amintiri de cum ajunse aici"

    hide preot_lumanare

    jump awakening

label twins_dissapearing:
    "Cand Boris aproape ajunse de usa camerei, vazu niste siluete in fata acesteea"

    show silouettes at Position(zorder=0)

    preot "Cine sunteti? Ce cautati aici?"

    "Boris nu apuca sa primeasca raspunsul la intrebare, ca ele disparusera, impreuna cu ochii ce il priveau in ceafa"

    "Boris alerga spre usa si trase de aceasta"

    scene village landscape
    
    "Dar se trezi in mijlocul satului, fara gemeni, ca din vis"

    return




