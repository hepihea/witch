
default night05_elysium_AfterSex_legHurt_told = False # Small guys are called.
default night05_elysium_AfterSex_bait_Cond = False # Big Guys are called

default night05_elysium_AfterSex_handBleeding = False
default night05_elysium_AfterSex_armBleeding = False


label night05_elysium_AfterSex:

    scene black
    with fade

    ono "Pum"

    n "El ruido de una puerta te despierta ligeramente de la somnolencia."

    pt "¿Sigo con vida?..."

    with hpunch
    ono "slap"

    with hpunch
    extend " slap"

    n "Recibes unas ligeras cachetadas en la mejilla."

    ne "Despierta."

    ne "Es hora de irnos."

    scene day05

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears

    with fade

    n "Con tus ojos aún acostumbrándose a la luz,"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    n "te descubres completamente vestido,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    n "al igual que Neus,"

    scene bg el_bedroom_b:
        truecenter
        zoom 0.5
    with Dissolve(0.5)

    n "la cual se distancia de ti para acto seguido ponerse de pie y acercarse a la puerta"
    # scene relda_alone_room:
    #     truecenter
    #     zoom 0.2
    scene relda_alone_room:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.01 # Down
        ease_quad 10.0 zoom 2.4 xpos 0.5 ypos 1.02 # Face
    with fade

    n "dónde hallas esa extraña mujer vestida de etiqueta rojiza"

    n "que vino a vuestro encuentro a la entrada de este extraño lugar."

    if night05_elysium_sexMast_Cond:

        pt "¿Qué...?"

        pt "¿Qué demonios ha pasado?"

    scene bg el_bedroom_b:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        #zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_piris right03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows sadx02:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_top_hair:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose


    $ Pedrera_char_Cond = "NeusFarFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyebrows surprisex01
    $ nteye = "left00"
    call n_closefromup_tears_tears
    with fade

    re "Parece que lo has dejado bastante seco."

    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx04

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No es lo que parece."

    show relda_exp_eyes 05
    show relda_exp_piris right05
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth sad_Talkingx004

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "¿Segura?"

    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Bueno,"
    
    extend " al menos sigue con vida."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Silentx02

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    if night05_elysium_sexMast_Cond:

        pt "¡¿Al menos?!"

    else:

        pause 0.2

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx003

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows normal
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "Sí,"

    show relda_exp_eyes 06
    show relda_exp_piris front06
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx05

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "left00"
    call n_closefromup_tears_tears
    with dissolve

    re "me imagino que para ti eso es una novedad."


    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmm..."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Talkingx005

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    re "Es una lástima que tengáis que iros tan pronto."

    show relda_exp_eyes 03
    show relda_exp_piris right03
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx03

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Por mucho que te agradezca la ayuda,"

    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Silentx04

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "sabes que no tenemos mucho tiempo."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx005

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "De todos modos no parece estar mucho por la labor."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows serious
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    

    ne "..."

    show relda_exp_eyes 05
    show relda_exp_piris right05
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx06

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve


    if night05_elysium_sexMast_Cond:
        
        pt "¿Por qué no puedo ni moverme?"

    else:

        pause 0.2

    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Talkingx006

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "Aunque no estoy convencida de que el tiempo o su estado"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx07

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "sean realmente la razón por la cual no quieres que pase un tiempo con él,"

    show relda_exp_eyes 05
    show relda_exp_piris right05
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Talkingx08

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    re "¿me equivoco?"

    show relda_exp_eyes 05
    show relda_exp_piris right05
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx05

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "De corazón Elur,"

    show relda_exp_eyes 03
    show relda_exp_piris right03
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx05

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "me alegro que por fin puedas ser feliz."

    show relda_exp_eyes 04
    show relda_exp_piris right04
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Silentx04

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Aún es demasiado temprano para decir eso."

    show relda_exp_eyes 01
    show relda_exp_piris front01
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx02

    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyebrows surprisex02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    n "Intentas mover tu cuerpo para poder decir o hacer algo,"

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx02

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    n "pero apenas eres capaz de mover tus dedos."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx06

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "Sí,"

    show relda_exp_eyes 07
    show relda_exp_piris front07
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Talkingx09

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    re "efectivamente sigue con vida."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx07

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with fade

    ne "[protname],"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿estás bien?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Euhh..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Debería haber parado antes."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "Pero me imagino que es demasiado adictivo."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    if night05_elysium_sexMast_Cond:

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        if gensex_INotLoveYouNeus:

            p "¡¿Puedo saber qué coño me has hecho?!"

        else:

            p "¿Puedo saber al menos qué me has hecho?"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex01
        $ nteye = "left01"
        call n_closefromup_tears_tears
        with dissolve

        re "¿Mientras estaba inconsciente?"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "left02"
        call n_closefromup_tears_tears
        with dissolve

        re "Suerte que querías dejar de ser una chica mala..."

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyebrows sadx04
        $ nteye = "right04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Yo..."

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        menu:

            "¡¿En serio me has violado?!":
                call p_Help

                $pl.ch_pts("np",-1)

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows surprisex02
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyebrows angryx02
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "Ya te he dicho que necesitaba tu esperma."

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows angryx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                re "Me parece muy bien que tengáis discusiones de pareja,"

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows sadx04
                $ nteye = "right04"
                call n_closefromup_tears_tears
                with dissolve

                re "pero ahora no es el momento."

                if gensex_INotLoveYouNeus:

                    show neus_exp_mouth sad_Silentx02
                    show neus_exp_eyebrows surprisex02
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡¿Te crees que puedo ser pareja de esta después de lo que me ha hecho?!"

                    $ ntlong += 1

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx06
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ ntlong += 1

                    show neus_exp_mouth sadbiting_Silentx07
                    show neus_exp_eyebrows sadx06
                    $ nteye = "right05"
                    call n_closefromup_tears_tears
                    with dissolve

            "...":
                call p_Help
                pass

    scene bg el_bedroom_b:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        #zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_piris right03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows sadx02:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_top_hair:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Talkingx003
    with fade

    re "¿Me harías el favor de apartarlo de la cama?"

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "Es necesario para que podáis salir de aquí."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Silentx04
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with fade_short

    ne "Claro,"

    extend " claro..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade

    n "Sientes las pequeñas pero fuertes manos de Neus que se deslizan por tus piernas y tu espalda,"

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with vpunch

    n "para acto seguido levantarte en brazos."

    if night05_elysium_sexMast_Cond:

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissole

        pt "¡Dios!"

        pt "Estoy realmente jodido..."

        pt "¡Ni siquiera me siento la entrepierna!"

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissole

        if gensex_INotLoveYouNeus:

            pt "¡¿Qué demonios me ha hecho esta bruja?!"

        else:

            pt "¡¿Pero qué demonios me habrá hecho para que esté así?!"

    scene day05
    with fade

    n "Esa extraña dama se acerca a la alcoba y con una fuerza sobrehumana"

    n "levanta el mueble entero con una sola mano."

    n "Se pone de cuclillas y usando sus largas uñas arranca una baldosa del piso"

    n "mostrando bajo este un oscuro túnel que parece no tener fondo."

    scene bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        relda_pos_close
    show relda_exp_eyes 03:
        truecenter
        relda_pos_close
    show relda_exp_piris right03:
        truecenter
        relda_pos_close
    show relda_exp_eyebrows sadx02:
        truecenter
        relda_pos_close
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        relda_pos_close
    show relda_top_hair:
        truecenter
        relda_pos_close

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx06
    with fade

    re "Me temo que tendrás que llevarlo a cuestas por todo el camino,"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth sad_Talkingx006
    with dissolve

    re "no parece que pueda valerse por si mismo."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth sad_Silentx03
    with dissolve

    pause 0.2

    $ ntlong = 0

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    $ nteye = "left02"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade_short

    ne "No te preocupes,"

    $ nteye = "left04"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "me ha dado la suficiente energía para poder cargar con él."

    if night05_elysium_sexMast_Cond:

        $ nteye = "left05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pt "¿Energía?"

        pt "¡¿Se refiere a mi esperma?!"

    else:

        $ nteye = "left04"
        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

    scene bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        relda_pos_close
    show relda_exp_eyes 03:
        truecenter
        relda_pos_close
    show relda_exp_piris right03:
        truecenter
        relda_pos_close
    show relda_exp_eyebrows sadx02:
        truecenter
        relda_pos_close
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        relda_pos_close
    show relda_top_hair:
        truecenter
        relda_pos_close

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows suspiciousx03
    show relda_exp_mouth happy_Talkingx07
    with fade_short

    re "De eso no tengo duda."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx06 ## Not finished... relamer expression?
    with dissolve

    n "Ves que se relame los labios mientras te mira con un rostro entre la lujuria y el hambre."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth happy_Silentx07
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    $ nteye = "left04"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade_short

    ne "Relda,"

    extend " yo..."

    $ nteye = "left05"
    show n_closefromup_mouth sad_Silentx05
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    re "Tranquila,"

    scene bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        relda_pos_close
    show relda_exp_eyes 03:
        truecenter
        relda_pos_close
    show relda_exp_piris right03:
        truecenter
        relda_pos_close
    show relda_exp_eyebrows sadx02:
        truecenter
        relda_pos_close
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        relda_pos_close
    show relda_top_hair:
        truecenter
        relda_pos_close

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Talkingx002
    with fade_short

    re "no voy a dejar que mis impulsos primarios me impidan ayudar a una querida amiga en apuros."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx04
    with dissolve

    re "Pero te recomiendo celeridad,"

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "no queda mucho para que salga el sol."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Talkingx03
    with dissolve

    re "Estoy convencida de que ese \"perro sarnoso\" al que tú llamas,"

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth sad_Talkingx06
    with dissolve

    re "no estará solo buscándote ahí fuera."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Silentx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with fade_short

    ne "Gracias,"

    extend " de verdad."

    show neus_exp_mouth happy_Silentx03
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg el_bedroom_b:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        #zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_piris right03:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows sadx02:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose
    show relda_top_hair:
        truecenter
        zoom 0.4 xpos 0.22 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 03
    show relda_exp_piris right03
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth happy_Talkingx03

    $ Pedrera_char_Cond = "NeusFarFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with fade

    re "La próxima vez que nos veamos"


    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth happy_Talkingx05

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "left00"
    call n_closefromup_tears_tears
    with dissolve

    re "me lo podrías agradecer compartiendo este apuesto caballero que tienes en brazos."

    show relda_exp_eyes 03
    show relda_exp_piris right03
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show relda_exp_eyes 07
    show relda_exp_piris front07
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Talkingx06

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    re "Tranquila,"

    extend " solo bromeo."

    show relda_exp_eyes 06
    show relda_exp_piris front06
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmm..."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    n "Neus se queda quieta unos segundos fijándose en el pequeño agujero que hay en el suelo."

    scene day05
    with fade

    n "Con una increíble fuerza -especialmente por su estatura- te agarra de las caderas y posa tus nalgas sobre su nuca."

    n "Intentas agarrarla de la cabeza para no caerte,"

    n "pero apenas te quedan fuerzas y la extraña dama tiene que sujetarte para que no termines en el suelo."

    ne "[protname]..."

    pt "Estoy hecho mierda..."

    scene bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        relda_pos_close
    show relda_exp_eyes 03:
        truecenter
        relda_pos_close
    show relda_exp_piris right03:
        truecenter
        relda_pos_close
    show relda_exp_eyebrows sadx02:
        truecenter
        relda_pos_close
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        relda_pos_close
    show relda_top_hair:
        truecenter
        relda_pos_close

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx04
    with fade_short

    re "¿Me permites robarle un beso a tu amado?"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx03
    with dissolve

    ne "..."

    show relda_exp_eyes 06
    show relda_exp_piris front06
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Talkingx03
    with dissolve

    re "Tranquila,"

    extend " es para vuestro bien."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx04
    with dissolve

    ne "De acuerdo."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Silentx05
    with dissolve

    pause 0.2

    scene day05
    with fade

    n "Deslizando suavemente una de sus manos por tu barbilla, logra levantarte ligeramente el mentón."

    n "Ves en su rostro ese extraño brillo verdoso en lo profundo de la oscuridad de su pupila"

    n "mientras acerca sus labios a los tuyos."

    n "Su ardiente lengua acaricia juguetonamente la tuya"

    n "en ese proceso, percibes todo tu cuerpo calentarse y entrando en ligeros espasmos."

    n "Separa finalmente sus labios sin dejar de mirarte fijamente a los ojos"

    n "con ese rostro de mujer madura pero no por ello menos pícara."

    scene bg el_bedroom_blur:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        relda_pos_close
    show relda_exp_eyes 03:
        truecenter
        relda_pos_close
    show relda_exp_piris right03:
        truecenter
        relda_pos_close
    show relda_exp_eyebrows sadx02:
        truecenter
        relda_pos_close
    show relda_exp_mouth happy_Talkingx08:
        truecenter
        relda_pos_close
    show relda_top_hair:
        truecenter
        relda_pos_close

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Talkingx001
    with fade_short

    pause 0.2

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx03
    with dissolve

    re "Creo que con esto bastará."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Silentx03
    with dissolve

    n "Tienes la sensación que tienes la fuerza suficiente para mantener tu espalda erguida"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth happy_Silentx04
    with dissolve

    n "y agarrarte con suficiente fuerza a la cabeza de Neus."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth happy_Silentx05
    with dissolve

    pt "Wow..."

    show relda_exp_eyes 01
    show relda_exp_piris front01
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx02
    with dissolve

    ne "¿Segura que era el único modo de ayudarle?"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Talkingx02
    with dissolve

    re "Querida..."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Silentx04
    with dissolve

    ne "Hmm..."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Silentx03
    with dissolve

    ne "Perdona."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Silentx03
    with dissolve

    ne "Nos estás salvando la vida y lo único que hago es gruñir..."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx05
    with dissolve

    re "Para nada."

    show relda_exp_eyes 06
    show relda_exp_piris front06
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx04
    with dissolve

    re "Entiendo perfectamente lo que significa proteger a alguien amado."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Talkingx04
    with dissolve

    re "Aunque eso sí,"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "te recomiendo que no te entretengas demasiado ahí abajo."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Talkingx06
    with dissolve

    re "Cuando los efectos de mi beso desaparezcan,"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "estará incluso más débil que antes."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Silentx04
    with dissolve

    ne "Me lo imagino."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "Os deseo toda la suerte del mundo."

    show relda_exp_eyes 01
    show relda_exp_piris front01
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx02
    with dissolve

    ne "Te prometo que te devolveré el favor."

    show relda_exp_eyes 06
    show relda_exp_piris front06
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Talkingx05
    with dissolve

    re "De eso no me cabe duda."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Silentx05
    with dissolve

label night05_elysium_AfterSex_tunnel:

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    stop music fadeout 3.0

    n "Sin darte tiempo a decir una palabra,"

    scene day05
    with fade

    n "Neus avanza hacia el agujero y con un salto os adentráis en él."

    scene black
    with fade

    n "Usando la suela de sus zapatos fricciona por las estrechas paredes del agujero"

    n "para que la caída no sea tan súbita"

    n "hasta que la oscuridad os engulle por completo y notas que finalmente toca el suelo."

    n "Sobre tu cabeza, oyes el eco de esa losa volviendo a su lugar,"

    n "hasta que la única fuente de luz que había desaparece por completo."

    p "No veo una mierda..."

    ne "No te preocupes."

    n "Sus ojos vuelven a brillar en medio de esa oscuridad."

    ne "Yo sí puedo ver."

    n "Un aroma a humedad y cerrado inunda el lugar."

    n "El hecho de que solo oigas vuestras voces y ciertos ruidos extraños a lo lejos"

    n "no te tranquiliza en absoluto."

    n "Avanza dos pasos."

    with vpunch
    p "¡Ouch!"

    ne "¡Lo siento!"

    ne "No había visto que la cueva era tan bajita."

    n "Te desciende de sus hombros y posas tu trasero sobre la fría arena del suelo."

    ne "¿Te he hecho daño?"

    p "No pasa nada,"

    extend " sobreviviré."

    ne "Me refiero si notas que estás sangrando."

    p "¿Euh...?"

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told:

        n "Acercas tu mano a tu nariz y lo único que percibes son los dos trozos secos de papel"

        n "que anteriormente ella te había introducido."

    else:

        n "Acercas tu mano a tu nariz y no percibes ninguna gota."

    p "Diría que no."

    ne "Será mejor no arriesgarnos."

    n "Acerca sus labios a su nariz mientras oyes el ruido de su nariz forzándose a oler con intensidad."

    n "Sientes su cálida lengua por toda tu frente y tus mejillas."

    pt "Parece que me esté lamiendo un perro..."

    n "Te parece escuchar el ruido de sus manos hurgando en su bolso"

    n "para luego oír un ligero gemido de sus labios."

    p "¿Qué...?"

    ne "No te preocupes."

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told:

        n "Percibes sus cálidos dedos sacándote los dos trozos de papel de tu nariz"

        n "y te vuelve a meter los nuevos húmedos y cálidos hasta el fondo."

        p "Ughh..."

        p "¿Otra vez?"

        ne "Es por seguridad."

    else:

        n "Sientes que acerca dos trozos de papel húmedos y calientes cerca de tu nariz"

        n "con la intención de introducirlos en tus fosas nasales."

        p "¿Qué...?"

        ne "Confía en mi."

        n "Decides que lo más sabio es no rechistar."

        n "Sin demasiada compasión llega a introducírtelos hasta el fondo."

        p "Ugh..."

        ne "Lo siento."

        p "Este olor..."

        p "¿Lo has mojado con tu entrepierna?"

        ne "Sí..."

        p "¿Por qué?"

        ne "Por seguridad."

    n "Vuelve a cogerte con fuerza y te acomoda a su espalda posando tus piernas sobre sus caderas."

    n "Retorciendo tu espalda logras posar tus manos en ella agarrándote a su cuello."

    ne "Será mejor que nos demos prisa antes de que te quedes sin fuerzas."

    p "¿No nos encontrará tu padre si usas tanto el brillo de tus ojos?"

    ne "No a menos que los use para algo más serio."

    ne "Ver en la oscuridad no es la gran cosa, tranquilo."

    n "Arranca a correr como si el peso de tu cuerpo fuera más liviano que una pluma."

    #n "Deduces que el suelo es de arena por el ruido que hace sus zapatos recorriendo el suelo."

    n "Eres incapaz de saber a qué velocidad se desplaza,"

    n "pero por la fuerte brisa que impacta contra tu rostro"

    n "y los extraños ruidos que oyes a lo lejos que rápidamente quedan atrás,"

    n "deduces que su rapidez es francamente veloz."

    n "A pesar de que te cuesta respirar,"

    n "agradeces con creces no tener que averiguar qué se esconde en esta profunda oscuridad."

    n "Sientes que aminora el paso."

    p "¿Estamos llegando?"

    ne "Creo que sí."

    p "¿Es el final del túnel?"

    ne "No."

    ne "En realidad esto es más bien un laberinto de túneles."

    p "..."

    ne "Pero es dónde me ha dicho que debía pararme."

    menu:

        pt "No veo un carajo..."

        "¿Estás segura?":
            call p_Help

            ne "Confía en mi, [protname]."

            p "..."

        "<Confiar en ella>":
            call p_Help

            pass

    ne "Agárrate fuerte."

    p "¿Por...?"

    with vpunch

    p "¡Ouch!"

    n "Por el incremento en la fuerza de gravedad que percibes,"

    n "deduces que ha dado un buen salto."

    n "Oyes que intenta mover algo metálico, aparentemente grande y bastante obstruido."

    ono "NEEEC"

    n "Finalmente logra remover esa pieza y una nueva zona se os abre ante vuestras narices."

    p "¿Es agua lo que oigo?"

    ne "Ajá..."

    p "¡Joder!"

    ne "Sí..."

    ne "Es un olor bastante desagradable,"

    ne "pero no hay otro modo si queremos escondernos de esos malditos perros."

    # ne "La alcantarilla es la mejor manera de poder pasar desapercibidos."

    p "Pensé que este papel que llevo en la nariz era para evitar poder oler cosas extrañas..."

    ne "No,"

    ne "en realidad sirve para que otros no te puedan oler a ti."

    p "Si sabías que veníamos a un lugar apestoso, ¿no podías haber aprovechado?"

    ne "A la velocidad a la que voy es más fácil que respires por la nariz que por la boca."

    n "Cierra la la puerta de metal detrás de ella"

    n "y os adentráis en lo que parece algún lugar incierto y hediondo de las alcantarillas de la ciudad,"

    n "aunque sigues sin ver un carajo."

    n "Con la misma celeridad, vuelve a emprender la carrera adentrándose aún más en esa húmeda oscuridad."

    p "Ufff..."

    n "El olor es tan desagradable que te dan ganas de alejar la mano de su cuello para taparte la nariz."

    ne "No."

    ne "No apartes la mano de mi cuello,"

    ne "estás demasiado débil y no tenemos demasiado tiempo."

    ne "Por favor, aguanta un poco más."

    p "Joder..."

    p "pero es que a la velocidad a la que corres"

    p "aún me está entrando más mierda en la nariz."

    ne "No hables,"

    extend " o será peor."

    ne "Solo un poco más,"

    ne "te lo prometo."

    pt "Dios..."

    pt "¿Cómo puede aguantarlo ella?"

    ne "¡[protname]!"

    p "¿Euh...?"

    ne "Necesito que te agarres con fuerza."

    p "Pero si ya..."

    n "Sientes que te va faltando la fuerza en las manos,"

    n "y poco a poco vas perdiendo la consciencia por ese horrible hedor."

    p "Lo siento,"

    extend " pero es que..."

    n "Se detiene súbitamente y con suavidad te baja de sus brazos."

    p "¿Qué...?"

    p "¿Qué estás haciendo?"

    # ne "No quería recurrir a eso porque a la velocidad a la que voy necesitas la nariz para respirar,"

    # ne "pero creo que con este hedor quizás no ha sido tan buena idea."

    ne "Espero que con esto puedas aguantar un poco más."

    ne "Por favor,"

    ne "no pienses que te estoy haciendo algo raro,"

    ne "¿de acuerdo?"

    n "Notas su aliento acercándose a tu rostro y de un lengüetazo te inunda de saliva tus fosas nasales."

    p "¡¿Qué...?!"

    ne "¿Algo mejor?"

    p "¿Euh...?"

    n "Te hallas incapaz de respirar por la nariz."

    n "Aunque sigues percibiendo el nauseabundo olor a través de tu boca,"

    n "por lo menos es algo más soportable."

    ne "Espero que esto no nos traiga problemas..."

    p "¿Qué...?"

    n "Vuelve agarrarte como antes y sin vacilar palabra,"

    n "intenta recuperar el tiempo perdido yendo incluso más rápido que antes."

    n "Te agarras a ella con todas tus fuerzas mientras sigues oyendo insólitos ruidos a lo lejos,"

    n "aunque esta vez te resultan incluso más extraños que antes,"

    n "ya no parecen animales escarbando entre agujeros de tierra."

    n "No."

    n "Esta vez son distintos."

    n "Estruendos metálicos, chirriantes, casi armónicos."

    n "En ocasiones te perece oír algo parecido a voces guturales ininteligibles"

    n "en la profunda oscuridad que os rodea."

    n "Pero lo que te inquieta de verdad es que cada vez los oyes más cerca."

    n "Intentas separar tus párpados para ver si tus ojos han logrado acostumbrarse algo más a la oscuridad,"

    n "pero a esta velocidad y con las pocas fuerzas que te quedan desistes en tu intento."

    ne "¡[protname]!"

    p "¿Euh...?"

    ne "¡Aguanta!"

    n "Sientes que las fuerzas te están abandonando y percibes el pelo de Neus cada vez más lejos."

    n "No tardarás en depender únicamente de su agarrón en tus piernas apegadas a sus caderas"

    n "para impedir una caída mortal con tu peso muerto."

    n "Se detiene de golpe para bajarte al suelo."

    n "En ese corto espacio de tiempo,"

    n "oyes a lo lejos el sonido de unos pies desnudos corriendo sobre mojado"

    n "acercándose hacia vosotros a toda prisa."

    n "Te agarra a modo de damisela en apuros y arranca a correr de nuevo."

    p "¿Son-"

    extend "son los perros...?"

    n "Apenas eres capaz de articular palabra."

    ne "No,"

    extend " no son ellos."

    p "¿Qué-"

    extend "qué son..."

    extend " entonces...?"

    ne "¡Ahora no [protname]!"

    n "Su voz es firme pero con un tinte que no te tranquiliza en absoluto."

    n "Sientes que se detiene."

    with vpunch

    p "¡Auch!"

    n "Te suelta tan abruptamente que caes de bruces contra el húmedo y frío suelo."

    ono "PAM"

    n "Oyes el ruido de sus zapatos saltando hacia un lugar incierto dejándote ahí tirado."

    p "¿Neus?"

    n "Esa manada de pies que oías detrás de ti no solo aumenta en número y en proximidad,"

    n "sino que ahora también percibes algo parecido al otro lado del túnel."

    p "¡¿Neus?!"

    n "Oyes un agudo chirrido metálico sobre tu cabeza."

    n "La luz de la luna es lo primero que logras ver a través del circular agujero que ha logrado abrir."

    n "Pero esa claridad también te permite ver la silueta de un montón de cuerpos a lo lejos"

    n "corriendo salvajemente hacia vosotros por ambos lados."

    p "{size=60}¡¡NEUS!!{/size}"

    n "Sientes su fuerte agarrón en el brazo que te arranca del suelo impulsándote hacia arriba"

    n "cuando una huesuda y blanca mano te agarra bruscamente por la pierna,"

    n "seguidamente de otra, luego otra..."

    n "Rostros pálidos pero completamente deformados con dientes largos y ojos negros"

    n "te acechan con deseo y hambre mientras Neus sigue tirando de ti para liberarte de ellos."

    n "Logran arrancarte el zapato mientras sus afiladas uñas se aferran a tus piernas."

    n "Finalmente logra apartarte de ahí a fuerza bruta proyectándote al aire"

    with vpunch
    n "para luego caer de bruces contra el frío y duro arcén de la calle."

label night05_elysium_AfterSex_street:

    pt "Mi espalda..."

    with sshake_soft
    ono "clonck"

    with sshake_soft
    extend " clonck"

    with sshake_soft
    extend " clonck"

    scene day05
    with fade

    n "Gracias a luz de la luna y la tenue luz de las farolas"

    n "logras vislumbrar a Neus usando la tapa de la cloaca"

    n "para obstaculizar la salida de esos extraños seres."

    ne "¡¿Puedes moverte?!"

    p "Ughh..."

    n "Lo intentas, realmente lo haces,"

    n "pero apenas eres capaz de mover tus dedos."

    ne "¡Mierda!"

    n "Al mirar a tu alrededor, descubres que seguís en una zona urbana,"

    n "aunque aparentemente, lejos del centro de la ciudad."

    with hpunch
    with hpunch

    ne "{size=80}¡¡SOCOROOO!!{/size}"

    pt "¡Joder!"

    n "El atronador grito de Neus te deja completamente helado."

    pt "¡Tenemos que estar pasándolas canutas si se pone a pedir ayuda ahora!"

    h01 "¡Señorita!"

    h01 "¡¿Se encuentra bien?!"

    n "Un grupo de hombres que estaban descargando un camión a lo lejos"

    n "se acercan corriendo para ver lo que ocurre."

    h02 "¡¿Quiere que llamemos a la policía?"

    h03 "¿No ves cómo están?"

    h04 "¡Hay que llamar a una ambulancia!"

    n "De la panadería que hay justo en frente sale una mujer con un delantal manchado de harina."

    m01 "¡Dios santo!"

    m01 "¡¿Qué está pasando aquí?!"

    h01 "Ella no parece herida."

    h02 "¿No has visto como esta la pierna de ese tipo en el suelo?"

    n "Los golpes en la tapa de la alcantarilla van menguando hasta que finalmente cesan por completo."

    n "Ves el tenue brillo en los ojos de Neus dirigido a esa desdichada pieza metálica."

    n "Finalmente se levanta y se acerca corriendo hacia a ti."

    n "Te agarra de la manga para volver a cargarte en brazos saliendo del lugar a toda prisa."

    p "¡¿Qué...?!"

    p "¿Por qué has gritado de ese modo?"

    ne "Era el único modo de que esas criaturas no salieran de la alcantarilla."

    p "¿No pueden salir si hay personas alrededor?"

    ne "No,"

    ne "si no quieren ser ejecutados por el César."

    p "..."

    pt "Este tipo tiene que ser alguien temible..."

    ne "Mierda..."

    ne "No sé dónde diablos estamos."

    p "Creo que estamos en la zona de {a=https://es.wikipedia.org/wiki/La_Trinitat_Vella}la Trinitat{/a}."

    ne "¿La vieja o la nueva?"

    p "Euh..."

    p "Diría que la vieja."

    ne "Entonces no estamos tan lejos."

    p "Neus..."

    ne "Ahora no [protname]."

    menu:

        pt "¿Debería decírselo?"
            
        "<Mejor no molestarla>":
            call p_Help

            $ night05_elysium_AfterSex_legHurt_told = False

            n "Sigue corriendo a toda velocidad evitando -en lo posible- las zonas más iluminadas"

            n "para no ser vista por los pocos transeúntes que recorren por la calle a estas horas."

            jump night05_elysium_AfterSex_parking

        "<Decirle que tienes la pierna ensangrentada>":
            call p_Help

            $ night05_elysium_AfterSex_legHurt_told = True

            jump night05_elysium_AfterSex_legHurt

        
label night05_elysium_AfterSex_legHurt:

    p "Mi pierna."

    ne "¿Euh...?"

    ne "¡Mierda!"

    n "Sin detenerse, sigue corriendo hasta alcanzar un prominente árbol"

    n "en el que -rama a rama- trepa usando solo sus pies"

    n "hasta alcanzar la más alta capaz de sosteneros a los dos."

    n "Cuando finalmente reposas sobre la incómoda madera,"

    n "te fijas en el sangriento estado de tu pierna."

    ne "Mierda,"

    extend " mierda,"

    extend " mierda..."

    p "En realidad creo que parece peor de lo que es."

    with hpunch
    ono "SRRRKKK"

    n "De un tirón arranca la tela inferior de la parte del pantalón que ha quedado manchada"

    n "y haciéndolo bola se la introduce en su boca."

    ono "glup"

    p "..."

    p "¿Qué...?"

    n "Con su cálida lengua empieza a relamerte la piel de tu pierna provocándote cierto cosquilleo."

    p "Hmmm..."

    n "Se detiene de inmediato para mirar rápidamente detrás de ella."

    p "¿Qué ocurre?"

    ne "..."

    p "¿Estamos a salvo?"

    ne "No lo sé."

    ne "Espero que no hayas sangrado demasiado hasta aquí."

    ne "Aguarda un segundo."

    n "Te abandona de un salto y sigue subiendo por la copa del árbol."

    n "Entre tantas hojas -y a pesar de la poderosa luz de la luna-"

    n "eres incapaz de ver lo que hace ahí arriba."

    ####

    n "Oyes el crujir de una rama a tu espalda."

    #n "al girarte ves un rostro famélico y monstruoso con unos dientes afilados apunto de "

    n "Sin tiempo a darte la vuelta..."

    with Shake((0, 0, 0, 0), 0.75, dist=25)
    p "{size=70}¡¡AAAARGHH!!{/size}"

    n "Dientes largos y afilados te dentellan el hombro derecho"

    n "mientras dos fuertes brazos te rodean para inmovilizarte."

    n "Neus se cierne velozmente sobre esa extraña criatura quitándotela de encima."

    n "Ambos se desploman árbol abajo entre tirones y golpes frenéticos que apenas eres capaz de vislumbrar."

    n "Terminan cayendo al suelo."

    n "Mientras Neus intenta reponerse del golpe"

    n "esa extraña criatura salta encima de ella."

    p "{size=55}¡Neus!{/size}"

    n "Tienes la sensación que se ha quedado completamente quieto."

    n "Neus logra apartarlo y en su rostro ves ese intenso brillo en sus ojos."

    n "Sin apenas recuperar el aliento, regresa de nuevo escalando las ramas del árbol hasta dónde estás."

    n "Usa su ardiente y longeva lengua para lamerte el hombro y parte del pecho"

    n "dónde tu sangre había sido derramada."

    menu:

        pt "No creo que vaya a ser el único monstruo que aparezca esta noche..."

        "<No decir nada>":
            call p_Help

            pass

        "<Proponerle la idea de echarle parte de tu sangre encima de esa criatura a modo de cebo>":

            $ night05_elysium_AfterSex_bait_Cond = True

            call p_Help

            p "Si lo que buscan es mi sangre,"

            p "¿por qué no se la tiras encima para que lo busquen a él y no a nosotros?"

            ne "..."

            ne "No es tan mala idea..."

            n "Desciende rápidamente de nuevo -entre rama y rama- hasta alcanzar ese petrificado cuerpo."

            n "Vuelve a usar sus brillantes ojos mientras le da un lametón en la nariz"

            n "y cierne un vomito de sangre sobre su espalda."

            p "Ughh..."

            n "Pocos después vuelve hacia ti."

            p "Espero que funcione."

            ne "En realidad, exponiendo tu sangre así"

            ne "nos arriesgamos a que acudan seres que no tengo ninguna intención de volver a ver,"

            ne "pero francamente,"

            ne "las cosas se han complicado bastante."

    n "Te agarra de nuevo para luego deslizarse entre la arboleda -contigo a cuestas- hasta alcanzar el suelo."


    # n "Sus pasos vuelven a correr a toda velocidad mientras descubres que se aleja de la zona urbana, atravesando incluso la autopista C-33 saltando por encima del cartel azul que te da la bienvenida a la ciudad."

    #pt "¿A dónde demonios me lleva?"

    p "¿Ya sabes a dónde vas?"

    ne "Sí,"

    ne "me ha dado tiempo a mirar cuando estaba ahí arriba."

    ne "Estamos muy cerca."

    scene black
    with fade

    pause

    #####


label night05_elysium_AfterSex_parking:

    scene day05
    with fade

    n "Finalmente llegáis a una explanada de cemento repleta de coches aparcados"

    n "tenuemente iluminada por cuatro farolas mal puestas"

    n "algo apartada y separada de la zona urbana por un muro de árboles"

    n "y limitada por una muralla ondulada que la aísla del bullicio de la autopista."

    p "¿Euh...?"

    n "Se detiene en medio de ese lugar mientras baja los brazos"

    n "y voltea la cabeza por doquier como si estuviera buscando algo."

    n "A lo lejos uno de los coches enciende de forma fugaz sus luces de posición."

    ne "¡Ahí está!"

    if night05_elysium_AfterSex_legHurt_told and night05_elysium_AfterSex_bait_Cond:

        jump night05_elysium_AfterSex_getCar

    else:

        jump night05_elysium_AfterSex_getKilled

label night05_elysium_AfterSex_getKilled:

    ## if night05_elysium_AfterSex_legHurt_told: What happen if you didn't used the bait?

    ## If it's just the leg, you should be probably attacked only by Nosferatus.

    ## If you didn't used the bait, you should be attacked by the Tzimisces. What you think about that?

    ne "¿Euh...?"

    n "Neus retuerce el cuerpo para mirar detrás de ella."

    p "¿Qué ocurre?"

    ne "Me ha parecido..."

    if not night05_elysium_AfterSex_legHurt_told:

        n "Sus ojos descienden hacia tu pierna."

        ne "¡¿Estás sangrando?!"

        ne "¡¿Cuando...?!"

        ne "¡¿Por qué diablos no me lo has dicho antes?!"

        menu:

            pt "No sé si ha sido una buena idea no decírselo..."

            "Me dijiste \"Ahora no\".":
                call p_Help

                ne "¡Porque no sabía que estabas herido!"

            "Creí que si nos parábamos sería peor.":
                call p_Help

                ne "¡¿Peor?!"

            "Tampoco me duele tanto.":
                call p_Help

                ne "¡No tiene nada que ver con el dolor!"

            "No quería molestarte.":
                call p_Help

                ne "¡¿Molestarme?!"

        ne "¡¿Acaso no entiendes...?!"

    else:

        n "Las luces del coche a lo lejos vuelven a encenderse."

        p "Nos está haciendo señal a nosotros, ¿no?"

    n "Vuelve a girarse repentinamente en dirección a la arboleda"

    if not night05_elysium_AfterSex_legHurt_told:

        n "donde -de entre sus hojas- oyes un montón de gruñidos extraños"

        n "y observas ojos brillando en esa oscuridad."

        n "A pie de calle aparece una figura pálida y grotesca vestida con harapos"

        n "con la cabeza torcida, el rostro deformado, los ojos negros y dos colmillos pronunciados."

        p "¡¿Es uno de los que vimos en las alcantarillas?!"

        n "Detrás de este aparecen tres más, cada cual más feo y deformado que el otro."

        n "A vuestra espalda oyes el eco de un montón de risas,"

        n "como si una manada de hienas estuviera escondiéndose tras el muro que os separa de la autopista."

    else:

        n "de donde aparece un tipo con los brazos en alto,"

        n "el pelo semi largo -y tan rojizo como la larga túnica-"

        n "que le cubre medio rostro donde le observas una perturbadora sonrisa de oreja a oreja."

        p "¿Quien es ese tipo?"

        $ p01_name = "Tipo con sonrisa extraña"

        p01 "He-he..."

        n "Sientes como Neus da dos pasos en dirección opuesta a la arboleda"

        n "cuando justo detrás, cerca del muro rojizo que os separa de la autopista"

        with hpunch
        with hpunch
        ono "CRAASH"

        n "un tipo enorme -más parecido a un gorila que a un hombre- destroza un coche al colocarse encima."

        n "Detrás del tipo de la perturbadora sonrisa aparecen dos individuos más,"

        n "a cada cual más extraño que el anterior."

        n "Una mujer vestida de látex negro con un notable escote donde muestra un montón de tatuajes"

        n "y con una melena tan larga que le toca el suelo,"

        n "pero que te parece que se mueve como si tuviera vida propia."

        n "Y el otro individuo -por llamarlo de algún modo-"

        n "quizás no es tan pálido, pero parece de todo menos humano."

        n "Una enorme capa oscura que le cubre la mayor parte del cuerpo,"

        n "pero eso no te impide ver el resto."

        n "Sus ojos parecen estar ocultos tras un cascarón de molusco en su frente,"

        n "cuatro brazos extremadamente delgados pero con dos codos alzándose en el aire."

        n "Sin embargo, detrás de ellos aparecen decenas de otras siluetas acercándose al lugar."

    n "Los dedos de Neus te agarran con más fuerza."

    if not night05_elysium_AfterSex_legHurt_told:

        ono "PLOCK"

        n "Detrás vuestro, sobre el muro, aparece otra figura oscura de piel pálida"

        n "pero vestida toda de negro, llevando lo que parece una katana a su espalda"

        n "y una máscara rojiza tribal cubriéndole el rostro."

        n "El tipo más parecido a un gorila se lo que da mirando con una expresión confusa."

    n "A lo lejos y entre los coches te parece ver la figura de un lobo gigante de pelaje oscuro."

    ne "Mierda..."

    n "Al mirar hacia el coche de antes, descubres que está completamente apagado."

    p "Neus..."

    if not night05_elysium_AfterSex_legHurt_told:
        jump night05_elysium_AfterSex_paleGuysScene
    else:
        jump night05_elysium_AfterSex_highwayScene


label night05_elysium_AfterSex_paleGuysScene:

    n "Se mueve tan abruptamente que tienes la sensación de que te va a soltar."

    n "Pero te agarra sólidamente de nuevo."

    n "Al mirar abajo, descubres que uno de esos seres albinos y deformados"

    n "está agarrándole los pies mientras parte de su cuerpo está fundido con el cemento del suelo."

    with vpunch
    ono "PAM"

    n "Logra darle una enérgica patada que lo noquea el tiempo suficiente para librarse de él."

    n "Los tres insólitos tipos arrancan a correr hacia vosotros"

    n "mientras de los árboles descienden en manada un montón de criaturas a cada cual más extraña."

    n "Neus corre en dirección a la entrada de la autopista"

    n "mientras por detrás del muro aparecen otros seres albinos"

    n "correteando por encima de la rojiza y ondulada muralla sin quitarte el ojo de encima."

    n "Detrás de uno de los coches aparece uno de ellos que se os lanza encima."

    n "Debido al impacto, Neus termina por soltarte y te precipitas en el duro cemento."

    n "En tu intento por levantarte, lo único que consigues es perder las fuerzas y caer de nuevo."

    n "Cuando Neus logra liberarse de esa criatura otra se lanza sobre ella."

    with hpunch
    p "¡AAARGH!"

    n "Sientes unos dientes afilados clavándose en tu pierna."

    n "Neus consigue deshacerse de los dos tipos que estaban encima de ella"

    n "y con un rápido movimiento se acerca a dónde estás y de una patada te quita esa criatura de encima."

    n "Un nuevo ser alvino se lanza sobre ella y le muerde el brazo, mientras por detrás otra le dentella la pierna."

    n "Intentado deshacerse de ellos, otra criatura le aparece por detrás y le muerde el hombro."

    with hpunch
    p "¡Aargh!"

    n "Por el lado en que no mirabas aparece otra criatura que te muerde el brazo,"

    n "luego otra haciendo lo mismo en tu pierna."

    n "Al fijarte en Neus, ves que tiene a tres de esas criaturas abordándola con crueldad"

    n "mientras se derrama sangre por su cuerpo semi-desnudo."

    n "Sus ojos brillan con intensidad de nuevo."

    ne "{size=80}¡¡AAAAAAAARRGHHHH!!{/size}"

    n "Después de ese ensordecedor chillido, sientes un fuerte pitido en tu oído y eres incapaz de escuchar nada."

    n "Al abrir los ojos, ves que los tres monstruos que la estaban agarrando por la espalda"

    n "han quedado completamente congelados por un duro y sólido hielo que aparentemente ha aparecido de la nada."

    pt "¿Qué demonios?"

    n "El resto se detiene mientras usa sus manos para taparse sus enormes y escalofriantes orejas."

    n "Neus aprovecha para agarrarte de nuevo y con una fuerte patada"

    n "se libra del hielo que los unía con esos chupocteros,"

    n "no sin antes dejar un rastro de sangre por el suelo."

    n "Cuando apenas quedan unos metros para llegar a la entrada de la autopista:"

    with Shake((0, 0, 0, 0), 0.5, dist=10)
    ono "PAM"

    n "Neus recibe un golpe en plena cara y tan duro"

    n "que sales disparado al aire mientras ella se aleja por el impacto recibido."

    n "Cuando estás a punto de caer al suelo de bruces"

    n "una enorme y peluda mano lo impide agarrándote del pie."

    ww01 "Sabía que no eras humano,"

    n "Al separar tus párpados, descubres que el monstruo que te agarra"

    $ ww01_name = (_("Licántropo blanco"))

    ww01 "pero no me imaginaba que serías tan especial..."

    n "es aquel hombre-lobo albino de más de dos metros que os encontrasteis en el pasillo."

    n "Al dirigir tu mirada a dónde ha ido parar Neus,"

    n "la descubres peleando con tres criaturas albinas de las alcantarillas."

    with vpunch
    p "¡Ugh!"

    n "Agarrándote esta vez por ambas piernas -como si fueras un jamón-"

    n "se aleja de un salto hasta la cima de uno de esos árboles"

    n "para luego saltar sobre un tejado cercano."

    ne "{size=80}¡¡[protname]!!{/size}"

    n "Oyes la voz de Neus desgañitándose mientras sigue luchando desesperadamente por su vida"

    n "acorralada por un creciente número de esas asquerosas criaturas."

    n "Intentas darle un puñetazo a tu raptor, mover tu cuerpo para librarte de él, gritar..."

    n "Pero tienes tan pocas fuerzas que a duras penas logras mantener los ojos abiertos."

    n "Entre tejado y tejado ese monstruo albino te lleva como si fueras un trozo de carne por las piernas."

    n "A los lados te parece ver la silueta de otros dos monstruos peludos parecidos a él,"

    n "pero parecen mucho más oscuros."

    with hpunch
    ono "PAM"

    n "Sientes el impacto en tu espalda,"

    n "como si hubieras chocado contra un muro invisible,"

    n "al igual que tu raptor que se da de cruces deteniendo en seco su huida hacia delante."

    ww01 "¡¿Qué demonios?!"

    n "Al fijarte en la lejanía ves a uno de sus compañeros luchando contra \"algo\""

    n "que no eres capaz de vislumbrar demasiado bien."

    n "Un fuerte pitido vuelve a inundarte el oído al mismo tiempo que todos los sonidos de la ciudad se apagan."

    n "Apenas eres capaz de escuchar tu propia respiración y al monstruo que tienes al lado,"

    n "el cual cada vez parece más nervioso."

    with hpunch
    ono "PAM"

    with hpunch
    extend " PAM"

    with hpunch
    extend " PAM"

    n "Con su mano libre, el lobo albino empieza a propinar fuertes golpes contra ese muro invisible."

    ww01 "¡Maldita sea!"

    n "Al mirar hacia el otro lado, ves al otro licántropo en otro tejado"

    n "siendo ensartado por una enorme lanza y vomitando sangre."

    with vpunch
    p "¡AUCH!"

    n "Caes de bruces contra las tejas del tejado al ser liberado"

    n "para luego ver a ese albino licántropo usando ambas manos para golpear con más fuerza"

    n "esa dura pared invisible."

    n "El cielo se vuelve rojizo."

    pt "¡¿Qué demonios?!"

    n "Cada vez que intentas moverte,"

    n "lo único que consigues es desangrarte aún más por las heridas de tus brazos."

    n "Una delgada y huesuda mano surge del final del tejado,"

    n "luego otra, después otra y luego una cuarta."

    n "De ellas emergen unos extraordinariamente longevos y delgados brazos"

    n "de los cuales se asoma una criatura..."

    call night05_elysium_AfterSex_aracnidDescription

        # n "Quizás no es tan pálida, pero parece de todo menos humana."
        # n "Una enorme capa oscura que le cubre la mayor parte del cuerpo,"
        # n "pero eso no te impide ver el resto."
        # n "Sus ojos parecen estar ocultos tras un cascarón de molusco en su frente,"
        # n "con orejas enormes de murciélago,"
        # n "decenas de dientes afilados más parecidos a los de un tiburón y rojos como la sangre,"
        # n "cuatro brazos extremadamente delgados pero con dos codos alzándose en el aire."
        # n "Oyes el crepitar de sus dientes mientras su cabeza se contornea y parece dirigirte una vacía mirada."

    with hpunch
    with hpunch
    ono "CRASH"

    n "Como si de un cristal grueso se tratara,"

    n "el licántropo albino logra atravesar ese muro invisible con un último puñetazo."

    n "Una de los longevos brazos de ese monstruo horripilante se lanza como un proyectil hacia el licántropo albino"

    n "pero apenas logra arañarle superficialmente la piel bajo el pelaje de su pierna antes de que este logre escapar."

    pt "¿Qué...?"






    n "Haciendo desagradables ruidos y retorciendo su cuello en extraños espasmos"

    n "se te aproxima a paso lento."

    n "Como si se tratara de la la pata de una araña,"

    n "acerca uno de sus longevos dedos al charco de sangre que estás dejando sobre las tejas"

    n "para luego arrimársela a sus puntiagudos dientes."

    n "De ahí una larga, violácea y desagradable lengua aparece para relamer su dedo."

    ono "tac-tac-tac-tac"

    n "Su mandíbula hace un ruido extraño,"

    n "como si fuera un animal carroñero excitándose por su comida."

    ono "PLOCK"

    n "Oyes el ruido de alguien cayendo sobre las tejas que hay detrás de ti."

    n "Retuerces los ojos para intentar mirar en esa dirección."

    n "Ves a alguien que lleva la misma túnica oscura y rojiza que ese monstruo de los brazos largos,"

    n "pero sus pies..."

    n "Grotescos y azulados; en lugar de uñas tiene cuernos"

    n "y alrededor de su piel tiene hierros de metal clavados en su piel."

    n "Oyes un ruido gutural como si fuera un dinosaurio comunicándose con otro."

    with vpunch
    with vpunch
    p "{size=80}¡UGH!{/size}"

    n "La mano de ese perturbador monstruo te atraviesa el pecho sin piedad."

    n "Te falta el aire y el dolor es tan intenso que te hierve todo el cuerpo."

    n "Hasta que finalmente"

    scene black
    with fade

    n "cierras los párpados."

    ## Final Alternativo

    ## El hombre lobo albino le da un puñetazo a Neus en toda la cara, esta sale despedida mientras el lobo te agarra, ves a lo lejos otros dos licántropos peleándose con esos seres de las alcantarillas, El lobo que te lleva en brazos le dice unas palabras a Neus y justo cuando se gira es ensartado por una especie de lanza que le atraviesa el cuerpo soltándote contra el suelo de nuevo.

    ## Cuando abres los ojos, ves a una criatura de ultra tumba delante tuyo -Eltipo de la cara concha y orejas grandes- El cielo se enrojece etc etc... Sigues sin oir una mierda y a lo lejos ves a Neus siendo ensartada por otras criaturas de ultra tumba. El lobo sale corriendo de ahí mal herido mientras esa otra criatura te clava su lanza ahora a ti y poco a poco vas perdiendo las fuerzas.

    jump gameover

label night05_elysium_AfterSex_aracnidDescription:

    n "Quizás no es tan pálida, pero parece de todo menos humana."

    n "Una enorme capa oscura que le cubre la mayor parte del cuerpo,"

    n "pero eso no te impide ver el resto."

    n "Sus ojos parecen estar ocultos tras una nariz aplastada y deformada,"

    n "con enormes orejas de murciélago,"

    n "decenas de dientes afilados más parecidos a los de un tiburón y rojos como la sangre,"

    n "cuatro brazos extremadamente delgados pero con dos codos alzándose en el aire."

    n "Oyes el crepitar de sus dientes mientras su cabeza se contornea y parece dirigirte una vacía mirada."

    pt "¡Es el monstruo que vi en aquel horrendo lugar!"

    return


    # n "Uno en particular te llama poderosamente la atención, pues a pesar de que aparentemente carece de ojos,"

    # n "tienes la sensación que no te quita vista de encima."

    # n "Sus orejas, longevas y puntiagudas, se alzan por encima de su cráneo -parecidas a las de un murciélago-;"

    # n "sus ojos parecen estar ocultos tras una {a=https://i.natgeofe.com/n/6d16f213-60da-4528-b3f6-e1546d0ebf50/49228.jpg}enorme y deformada nariz{/a}"

    # n "con pieles sueltas que vibran de forma perturbadora,"

    # n "casi como si hubiera acercado su rostro ante una trituradora"

    # n "y aún no le hubieran sanado las heridas;"

    # n "bajo este manto de arrugas deformes y palpitantes pellejos colgantes"

    # n "se esconden un sinfín de rojizos dientes afilados que chocan entre ellos,"

    # n "como si su mandíbula padeciera un tembleque incontrolable."

    # n "Aparte de su escalofriante rostro,"

    # n "hay algo que consigue inquietarte aún más si cabe."

    # n "Carece de brazos y hombros, pero detrás de su espalda"

    # n "goza de lo que parecen cuatro extremadamente longevos y delgados brazos"

    # n "con dos codos cada uno, terminando en manos con cinco largos, delgados y afilados dedos,"

    # n "casi como si fueran las patas de una araña humanoide."

label night05_elysium_AfterSex_highwayScene:

    n "Neus -con sobrehumana celeridad- se dirige hacia el tipo de la máscara tribal"

    n "que aún está sobre el rojizo muro que lleva a la autopista."

    n "Te lanza hacia él y este te agarra al vuelo."

    p "¡¿Pero qué?!"

    ne "¡Corre!"

    n "El de la máscara se queda unos segundos en silencio"

    n "mientras el individuo que parece un gorila da un salto para atacarlo."

    n "Este consigue esquivarlo de un salto sujetándote en brazos"

    n "alcanzando el techo de uno de los coches aparcados."

    n "Neus se quita de encima uno de los monstruos albinos que está más adelantado con un codazo"

    n "y lo lanza hacia los otros dos que iban en cabeza."

    ne "¡HE DICHO QUE TE LARGUES!"

    n "Se lanza a la desesperada hacia uno de ellos dándole un fuerte puñetazo."

    n "Tu cuerpo se tambalea al sentir el rápido trote que emprende por encima del muro el que te lleva en brazos."

    p "¡Neus!"

    n "Sientes que da un pronto y poderoso salto en dirección a la autopista."

    ono "PAM"

    n "Oyes el hueco ruido de un duro plástico."

    n "Cuando separas los párpados descubres que os encontráis encima de un camión en marcha"

    n "directo a la rotonda de la Trinidad."

    menu:

        pt "¡¿Y Neus?!"

        "¡No podemos dejarla ahí!":
            call p_Help

            n "El tipo ni siquiera se inmuta."

        "<No decir nada>":
            call p_Help

            pass

    ##Debajo de los pies o algo aparece otro bicho raro que le agarra las patas al tipo enmascarado. Pero este saca su espada y le corta la mano o algo pero luego aparece el tipo de las patas de araña reencarndo como si fuera Matrix al tipo albino.

    n "Justo cuando iba a saltar por delante de la cabina del conductor..."

    with hpunch
    ono "CRASH"

    n "Se aparta velozmente hacia atrás esquivando un escuálido brazo de una longitud inhumana"

    n "que ha atravesado el capó del vehículo con unas uñas largas y afiladas untadas de un espeso líquido violáceo."

    p "¡¿Qué diablos?!"

    ono "TOC"

    extend " TOC"

    n "Dos monstruos inhumanos de piel pálida y dientes largos"

    n "aterrizan en los laterales de la parte trasera del camión"

    n "quedando vosotros en medio."

    n "Del agujero hecho por ese brazo surge una criatura monstruosa"

    n "cuya mitad de su cuerpo parece la de una persona obesa aparentemente normal,"

    n "pero la otra es de una criatura sin ojos,"

    n "una nariz deforme, -parecida a la de un murciélago-"

    n "y una enorme oreja que le sobresale del cráneo"

    n "además de dos largos y arácnidos brazos en esa porción de su espalda."

    pt "¡Es la criatura que vi en ese antro!"

    n "Tienes la sensación que usa sus dos otros brazos para mantener el coche en marcha."

    n "Tu portador elige saltar por el costado derecho del camión cuando..."

    with hpunch
    ono "PAM"

    n "Chocáis contra lo que parece un muro invisible."

    n "Una de las criaturas que aguardaba detrás, se lanza hacia vosotros."

    n "Agarrándote con una sola mano, toma su katana con la otra"

    n "y consigue rebanarle un brazo antes de que este os alcance."

    with hpunch
    ono "ZAS"

    n "Como si fuera una lanza,"

    n "uno de los longevos y esqueléticos brazos de esa criatura que tenéis en frente"

    n "es proyectada hacia vosotros."

    n "Tu portador logra -por escasos centímetros- evadirla."

    with hpunch
    mas "¡Ugh!" #enmascarado

    n "La otra criatura aprovecha ese lapso de tiempo para agarrarse a su pierna derecha"

    n "y atravesarle la dura tela de su ropa hundiendo sus largos colmillos en su carne."

    n "Con una rápida estocada, le atraviesa el cráneo con la katana,"

    n "pero ni así logra quitárselo de encima."

    n "Ese monstruo de largos brazos le lanza otro ataque con su otra extremidad"

    n "y cuando tu portador se prepara para hacer otra maniobra de evasión..."

    with hpunch
    ono "ZAS"

    n "Debido a que la otra criatura -la que le había cercenado un brazo-"

    n "le agarra -con la extremidad que le queda- su otra pierna"

    n "justo en el momento en que iba a saltar,"

    n "esa lanza humana consigue arañarle el hombro con el que te sujeta"

    n "hiriéndole por debajo de la oscura y resistente tela que lleva encima."

    n "Oyes el perturbador ruido que emiten sus afilados y rojizos dientes chocando entre sí,"

    n "como si fuera un animal carroñero excitándose por su comida."

    n "Tu portador usa su espada a modo de palanca en la mandíbula de ese bicho que permanece en su pierna"

    n "mientras usa el muro invisible con un volteo de cadera para quitarse a la otra criatura de encima."

    n "Otra lanza humana se proyecta hacia vosotros."

    n "Trepa por ese mismo muro y logra saltar por encima del mismo"

    n "aterrizando sobre el arcén de la autopista."

    n "Sin darte tiempo a tomar el aire,"

    n "te vuelve agarrar con una mano y usa la otra para tomar su katana..."

    ono "PAAAM"

    n "Con un veloz salto corta las cinco ruedas laterales."

    n "Mientras el enorme vehículo suelta enormes chispas en fricción con el asfalto,"

    n "el enmascarado vuelve agarrarte con ambas manos y arranca a correr a una inhumana velocidad"

    n "dejando atrás ese camión que termina cayendo al vacío en el tramo de la rotonda en el que os encontráis."


    ## call night05_elysium_AfterSex_aracnidDescription
        # n "Quizás no es tan pálida, pero parece de todo menos humana."
        # n "Una enorme capa oscura que le cubre la mayor parte del cuerpo,"
        # n "pero eso no te impide ver el resto."
        # n "Sus ojos parecen estar ocultos tras un cascarón de molusco en su frente,"
        # n "con orejas enormes de murciélago,"
        # n "decenas de dientes afilados más parecidos a los de un tiburón y rojos como la sangre,"
        # n "cuatro brazos extremadamente delgados pero con dos codos alzándose en el aire."
        # n "Oyes el crepitar de sus dientes mientras su cabeza se contornea y parece dirigirte una vacía mirada."

    # with hpunch
    # ono "PPPFFFF"

    # n "Oyes el particular ruido de las ruedas del camión reventar."

    # n "Mientras tu salvador intenta mantener el equilibrio,"

    # n "en un vehículo que da tumbos en lo que parece un intento por no salirse de la vía,"

    # n "ese extraño monstruo se precipita hacia vosotros."

    # n "De ambos lados del camión aparecen dos criaturas a cada cual más extraña"

    # n "pero con la misma túnica rojiza y oscura y la mirada desquiciada dirigida a ti."

    # n "Mientras te agarra en brazos se dirige hacia el único lugar dónde no ha aparecido nadie,"

    # n "pero al dar tres pasos hacia atrás:"

    # with vpunch
    # ono "PAM"

    # n "Lo que parece un muro invisible os impide el paso."

    # n "Sientes una mano huesuda agarrándote por la pierna izquierda"

    # n "mientras otra más gruesa y robusta te agarra por el brazo opuesto."

    # n "Tu salvador se deshace del tipo de la mano delgada con una vigorosa patada"

    # n "mientras le da un rodillazo al otro intentando hacer que te suelte."

    # n "Con un rápido movimiento logra zafarse de lo que por un momento te parece una lanza"

    # n "proyectada por el tipo de los brazos largos que tenéis en frente,"

    # n "hasta que te descubres que en realidad, se trata de uno de sus longevos brazos"

    # n "y la punta son sus uñas afiladas que sueltan un líquido viscoso y violáceo."

    # n "En cuestión de milésimas de segundo, el tipo de los brazos largos lanza un segundo ataque."

    # mas "¡Ugh...!"

    # n "Oyes el agudo gemido del tipo enmascarado al sentir esas uñas hiriéndole en el hombro superficialmente."

    # n "Al fijarte en su pie descubres que no ha sido capaz de esquivar el ataque"

    # n "debido a que el tipo flacucho le ha vuelto a inmovilizar la pierna."

    # n "Con una rápida maniobra, levanta la pierna agarrada y le lanza ese cuerpo flacucho al otro agresor"

    # n "mientras le da un cabezazo consiguiendo deshacerse de ambos."

    # n "El tipo arácnido vuelve a lanzarle un veloz ataque."

    # n "Aún y llevándote a cuestas, logra esquivarlo girando su cuerpo"

    # n "y con un rápido salto logra pasar por encima del arácnido agresor"

    # n "para terminar cayendo finalmente sobre el asfalto y -sin darte tiempo a tomar el aire-"

    # n "correr como alma que lleva el diablo."

    n "En la distancia empiezas a ver la luces rojas de los coches"

    n "que no han atestiguado el descalabro que ha habido detrás de ellos."

    n "A excepción de uno, el resto te parece verlos cada vez más lejos."

    n "La velocidad del enmascarado que te lleva en brazos disminuye a cada segundo que pasa."

    n "Percibes su respiración más agitada."

    p "¿Qué te ocurre?"

    n "Ese solitario coche no solo ya no avanza,"

    n "sino que está dando marcha atrás."

    with vpunch
    p "¡Ouch!"

    n "Chocas contra el arcén al cuando sus brazos no logran sostenerte."

    p "¡¿Qué?!"

    n "Cae de rodillas en el suelo sin mover ningún otro músculo."

    n "De ese vehículo sale un joven con el rostro cabizbajo,"

    n "vistiendo una ropa mundana y sin anormalidad aparente"

    n "acercándose a vosotros a paso lento pero constante."

    n "Al fijarte a tu alrededor descubres que el cielo se vuelve rojizo"

    n "y dejas de oír el murmullo de la carretera."

    pt "¡¿Qué está pasando?!"

    n "De la espalda de ese joven surge ese -inquietante y familiar- longevo y esquelético brazo"

    n "mientras la carne de su rostro se va derritiendo"

    n "surgiendo detrás de este esa enorme oreja y esa nariz monstruosa."

    p "¡¿No lo habíamos dejado atrás?!"

    n "Detrás de esa horripilante visión oyes una serie de pies acercándose a lo lejos."

    n "Al fijarte en esa dirección ves a varios tipos vistiendo ese mismo largo, rojizo y oscuro ropaje;"

    n "cada uno de ellos con un rostro abominable y nauseabundo."

    pt "Un momento..."

    pt "¡¿No son los mismos que vi en ese antro bajo el metro?!"

    n "El tipo de la máscara intenta balbucear alguna palabra"

    n "pero eres incapaz de entender lo que dice."

    n "Intentas ponerte en pie,"

    n "pero lo único que consigues es caerte de nuevo al no soportar tu propio peso."

    n "Ese grupo de extraños individuos está cada vez más cerca"

    n "y lo único que puedes hacer..."

    p "{size=80}¡SOCORRO!{/size}"

    n "Con tu vista nublada lo único que ves son los escalofriantes pies de esos seres de ultratumba,"

    n "te parece contar hasta siete pares de ellos, pero parecen de todo menos humanos."

    with vpunch
    with vpunch
    p "¡Ugh!"

    n "Sientes un pinchazo clavándose en tu espalda."

    n "El dolor se vuelve en mareo, el mareo en náuseas."

    n "Sientes que te arde el estómago y eres incapaz de respirar."

    n "Los dedos de las manos se te agarrotan."

    n "Tus ojos te arden."

    n "Finalmente..."

    scene black
    with fade

    n "Oscuridad."

    aj "final alternavio xx"

    jump gameover



label night05_elysium_AfterSex_getCar:

    n "Rápidamente se dirige hacia allí llevándote en brazos."

    pt "No parece un coche barato..."

    n "Del asiento del conductor sale una mujer de piel pálida,"

    n "vestida con un traje de etiqueta de color negro, con gafas de sol,"

    n "y con un sombreo típico de chófer."

    dri "Espera, ya te abro la puerta."

    ne "Gracias."

    n "Neus logra introducirte en el asiento trasero,"

    n "para luego sentarse a tu lado."

    dri "¿Ha ido todo bien?"

    ne "Ya hablaremos después,"

    ne "ahora conduce."

    dri "Me imagino que no del todo entonces..."

    ne "¡Rápido!"

    dri "¡Sí señora!"

    ono "POM"

    n "Oyes la puerta del conductor cerrándose de nuevo mientras arranca el motor."

    ono "BRrrrmm"

    p "¿Quien es?"

    ne "Una amiga,"

    extend " no te preocupes."

    p "¿Cómo sabía que estaríamos aquí?"

    ne "La he llamado mientras estabas inconsciente en la habitación."

    p "¿Segura que no han registrado la llamada?"

    ne "Sé lo que me hago,"

    extend " tran-"

    with hpunch
    ono "RAAAAASSS"

    n "Oyes las ruedas traseras del coche quemando goma sin que el vehículo avance lo más mínimo."

    p "¿Qué...?"

    ono "{size=60}AAAAUUUUUUUUUUU{/size}"

    ne "No..."

    n "El agudo aullido de un lobo suena justo detrás de vosotros."

    #ww02 "Grrr...."

    n "Al girar el rostro para mirar a través del cristal trasero,"

    n "ves la silueta oscura de una figura enorme y peluda."

    ww02 "Puedes correr rápido,"

    extend " pequeña."

    ww02 "Pero no más que yo."

    pt "No parece el mismo que el del pasillo..."

    n "Gracias a la tenue luz anaranjada de las farolas descubres que su pelo no es blanco,"

    n "sino completamente negro."

    n "A pesar del enorme tamaño y ferocidad que demuestra,"

    n "hay algo que te resulta curioso."

    pt "¿Tiene los ojos cerrados?"

    ne "Tss..."

    ww02 "Reconozco que eres una chica lista."

    ww02 "Unos minutos más"

    ww02 "y no hubiera podido saber qué salida habríais tomado en el {a=https://es.wikipedia.org/wiki/Nudo_de_la_Trinidad}Nudo de la Trinidad{/a}."

    ww02 "Pero para tu desgracia,"

    ww02 "la sangre de tu de tu chico tiene..."

    with hpunch
    ono "CRASH"

    n "Rompiendo el cristal trasero del coche, Neus salta encima de ese enorme bicho de pelaje oscuro"

    n "dándole un puñetazo tan fuerte que lo proyecta contra el muro rojizo de atrás."

    ne "{size=50}¡Arranca de una vez!{/size}"

    n "Obedeciendo sus palabras, la mujer que está al volante pone en marcha el vehículo de nuevo."

    p "¡No podemos dejarla aquí!"

    dri "¡Sale valerse por si misma,"

    dri "no te preocupes por ella!"

    n "Volviendo la mirada atrás, ves -a la par que os alejáis-"

    n "a ese bicho intentando agarrarla con los ojos cerrados mientras ella sigue esquivándolo."

    with vpunch
    with vpunch
    ono "RAAAAAASSSS"

    n "El frenazo del coche es tan abrupto que sales lanzado hacia delante."

    dri "¡Joder!"

    n "Otro enorme hombre-lobo -de pelo blanco como la nieve- se encuentra justo delante bloqueando el paso."

    n "Ves que se pone de cuclillas y lo siguiente que oyes es el fuerte pinchazo de las dos ruedas de delante."

    ww01 "¡Maldito inútil!"

    pt "Era este..."

    ww01 "¡¿Cuantas veces te he dicho que lo primero es agujerar las ruedas para que no puedan escapar?!"

    n "La conductora abre la puerta y sale corriendo,"

    n "pero apenas ha conseguido recorrer unos míseros metros"

    n "cuando otra enorme criatura de pelaje rojizo,"

    n "uñas oscuras, y con un parche en el ojo derecho,"

    n "emerge de la copa de uno de los árboles bloqueándole el paso."

    dri "¡Por favor!"

    ww03 "Vaya..."

    ww03 "Así que puedes dirigirme la palabra y todo..."

    dri "¡No me hagas daño!"

    ww03 "¿Esta es VIP?"

    ww01 "No,"

    extend " no lo és."

    ww01 "Pero por ahora no la mates."

    ww03 "¿Puedo hacer otras cosas?"

    ww01 "No hagas nada que yo no haría."

    n "Un gruñido de satisfacción emerge de sus fauces."

    n "A lo lejos ves a Neus siendo lanzada al aire por esa enorme y oscura criatura,"

    n "mientras su vestido va quedando hecho pedazos."

    with vpunch
    ono "CRAC"

    n "De una puntada de pie el monstruo albino levanta el morro del coche en el que estás"

    n "y sin poder evitarlo sales lanzado al asiento de delante."

    ww01 "Sí..."

    with hpunch
    ono "CRASH"

    n "Con su enorme zarpa atraviesa el cristal de en frente"

    n "para agarrarte por el cuello, sacarte del vehículo, y finalmente acercarte a su hocico."

    p "Ughh..."

    ono "-snif-"

    extend " -snif-"

    ww01 "Desde luego,"

    extend " ese olor a sangre tan peculiar viene de ti."

    ww01 "Me pregunto qué serán capaces de ofrecerme los chupatintas de esta ciudad por alguien como tú."

    ww01 "O quizás debería hablar con el retorcido chupa-cabras de su padre..."

    dri "{size=45}¡¡AAAAHHH!!{/size}"

    n "Al voltear la mirada ves a esa rojiza criatura peluda desgarrando salvajemente el negro vestido de esa pobre mujer."

    ww03 "Si gritas más,"

    n "De entre las piernas de ese monstruo emerge un enorme falo,"

    ww03 "al final te cortaré la lengua."

    n "más parecido al de un canino que al de un humano."

    dri "¡Por favor!"

    n "Vuelves a sentir la humedad del morro de ese monstruo en tu rostro."

    ww01 "Dime,"

    ww01 "¿Qué demonios eres?"

    ## If you Didn't use a trap, here is where more vampires appear and you're basically fucked up.

    ww01 "¡¿Euh?!"

    n "Ves que frunce su ceño mientras su mirada se dirige a un punto incierto a tus espaldas."

    ww01 "¡Maldito inútil!"

    n "Al volver la vista atrás descubres que Neus ha logrado inmovilizar al enorme monstruo de pelaje oscuro."

    ww01 "¡Te dije que no abrieras los ojos!"

    n "Con un pecho fuera, rastros de sangre por su cuerpo y su vestido hecho trizas se acerca corriendo hacia vosotros."

    ww01 "¡Maldita sea!"

    n "Te lanza de nuevo sobre el coche."

    ww01 "¡Rojo!"

    ww01 "¡Ni se te ocurra abrir los ojos!"

    ww03 "¿Acaso me tomas por ese inútil?"

    n "El enorme monstruo rojizo le da una patada al pie derecho de la conductora."

    dri "{size=50}¡¡¡AAARGHHH!!!{/size}"

    n "Rompiéndole visiblemente los huesos del pie."

    n "Para luego abandonarla y obstaculizar el paso de Neus.."

    n "Esta salta por encima de él para propinarle un golpe de puño al líder albino."

    n "Pero este consigue bloquearlo y ambos caen al suelo."

    n "Neus le lanza una serie de puñetazos mientras el albino se protege de ellos"

    n "hasta que el rojizo consigue agarrarla por sorpresa."

    n "Cuando ella intenta desprenderse de este,"

    n "el albino le muerde bruscamente la pierna."

    n "Con una patada y una rápida maniobra logra zafarse alejándose de los dos."

    n "Ambos licántropos miran con rabia contenida a la pequeña Neus"

    n "que ahora cojea de una pierna, su respiración es cada vez más agitada,"

    n "y apenas consigue mantenerse en pie."

    pt "¡Mierda!"

    pt "¡¿Es que no puedo hacer absolutamente nada?!"

    n "Estando encima del capó del coche miras a tu alrededor para ver si puedes usar algo a tu favor."

    n "Pero lo único que ves son trozos de cristal roto por todas partes."

    pt "Un momento..."

    $ night05_elysium_AfterSex_armBleeding = False

    # CHOICE
    # menu:

    menu:

        pt "Mi sangre..."

        "<Coger un trozo de cristal y hacerte un corte en el brazo con él>":
            call p_Help

            $ night05_elysium_AfterSex_handBleeding = True

            jump night05_elysium_AfterSex_blackGettingUp


        "<No hacer nada>":
            call p_Help

            $ night05_elysium_AfterSex_handBleeding = False

            # Neus and drive are gonna get raped...

            jump night05_elysium_AfterSex_blackGettingUp


label night05_elysium_AfterSex_blackGettingUp:

    if night05_elysium_AfterSex_handBleeding:

        n "Levantas tu mano para acercarte al cristal más robusto que encuentras."

        ne "¡AAargh!"

        n "Usando toda la fuerza que te es posible lo agarras con tanta fuerza que terminas cortándote la mano."

        p "Ughh..."

        n "A lo lejos, ves la conductora semidesnuda que sigue arrastrándose por el suelo intentando salir de ahí."

        n "Intentas acercar ese cristal roto a tu brazo pero a medio trayecto se te cae."

        pt "¡Mierda!"

        pt "¿Debería seguir?"

        pt "¿O con la sangre de mi mano ya basta?"

        pt "Al fin y al cabo Neus dijo que con una sola gota era suficiente para que todo se fuera al garete..."

        menu:

            pt "Con lo débil que estoy si pierdo más sangre puedo acabar muriendo..."

            "<Abrirte una profunda herida en el brazo>":
                call p_Help

                $ night05_elysium_AfterSex_armBleeding = True

                n "Usando toda la fuerza que te queda, agarras de nuevo ese cristal roto"

                n "y te lo clavas en la piel del brazo haciéndote un tajo largo y pronunciado."

                pt "¡JODER!"

                pt "¡Esto duele un cojón!"

                pt "¡En las películas parece algo más fácil!"

            "<No hacer nada más.":
                call p_Help

                pt "Ojalá haya suficiente..."

    n "A lo lejos ves al oscuro y petrificado monstruo que empieza a levantarse."

    n "Los otros dos se arrojan encima de Neus mientras esta intenta defenderse como puede"

    if night05_elysium_AfterSex_armBleeding:

        n "Tu sangre empieza a derramarse por el arrugado chasis en el que reposas."

    n "La conductora semi-desnuda se levanta medio cojeando con intención de salir de ahí."

    if night05_elysium_AfterSex_handBleeding:

        n "Tu dolor de cabeza aumenta por momentos."

    if night05_elysium_AfterSex_armBleeding:

        pt "Mierda..."

        n "Te miras el brazo ensangrentado y apenas eres capaz de ver tu piel entre tanta sangre."

        pt "No creo que haya sido una buena idea..."

    else:

        pt "Estoy hecho una mierda..."


    if night05_elysium_AfterSex_armBleeding:

        jump night05_elysium_AfterSex_CaesarDog

    else:

        jump night05_elysium_AfterSex_noEscape

label night05_elysium_AfterSex_CaesarDog:

    with hpunch
    dri "¡AAAhhhh!"

    n "Al fijar tu mirada en dirección al grito de la conductora"

    n "ves a un hombre barrigudo de mediana edad, con barba larga y densa, gafas de sol"

    n "y vistiendo los típicos ropajes que suelen llevar los motoristas de carretera con una chupa negra de cuero."

    ww02 "¡Y luego el inútil soy yo!" # Black Fur 

    ww02 "¡Ni siquiera has sabido hacer bien la burbuja!"

    n "Ambas criaturas han logrado inmovilizar a Neus,"

    n "la cual se encuentra en el suelo ahogada por el peso y las garras de ambos monstruos."

    ww03 "¡Es solo un humano!" # Red Fur

    ww02 "No huele a humano."

    ww03 "¡Entonces eres incluso más inútil haciendo la maldita burbuja!"

    ww02 "¡Cállate!"

    ww03 "¡Aunque sea un chupatintas,"

    ww03 "nosotros somos tres!"

    ww03 "Encargarte de él y asegúrate que no escape esa conductora."

    ww03 "¡Tengo planes con ella!"

    n "A paso lento pero seguro, el oscuro monstruo se acerca hacia el nuevo individuo."

    ww02 "Hmmm..."

    ww02 "Aunque seas un chupatintas,"

    ww02 "Si crees que puedes hacer frente a tres licántropos en luna llena,"

    ww02 "estás más bebido de lo que pareces."

    ww02 "Has tenido mala suerte de pasar por aquí a estas horas."

    n "Este se prepara para propinarle un puñetazo con sus garras cuando..."

    ww02 "¡¿Euh...?!"

    n "El motorista barrigudo le detiene el puño con una sola mano."

    ono "{size=40}PAM{/size}"

    n "El oscuro monstruo sale disparado a lo largo del parking"

    n "hasta colisionar con un coche y finalmente contra el muro"

    n "después de haberle propinado un fuerte puñetazo con la otra mano."

    n "Los otros dos se quedan boquiabiertos con la escena."

    ww01 "¡¿Pero qué...?!"

    ww03 "¡Eso es porque no te habías recuperado del todo, imbécil!"

    n "El licántropo rojizo abandona los brazos de Neus y sale disparado hacia el motorista."

    ww01 "¡Espera idiota!"

    n "Ese extraño individuo, sin demasiado esfuerzo, detiene el ataque del monstruo rojizo con ambas manos."

    n "Dando un ligero salto, le propina una fuerte patada doble"

    n "que lo envía justo encima de su otro compañero al otro lado del parking."

    pt "¡¿Pero qué narices...?!"

    n "La mujer conductora se queda completamente petrificada ante esa imponente figura."

    bog "Humana."

    bog "Si sales de aquí,"

    extend " estás muerta."

    n "Sin decir otra palabra, avanza -dejándola atrás- en dirección al monstruo albino."

    ww01 "..."

    n "Este sigue agarrando a Neus de los pies, pero cada vez con menos autoridad"

    n "sin saber muy bien cómo reaccionar ante esta situación."

    ww02 "¡Nos ha pillado de improvisto pero si luchamos los tres podremos contra él!"

    ww01 "¡Idiota!"

    ww01 "¡¿Acaso no reconoces quién es?!"

    n "El motorista barrigudo se detiene a escasos metros del monstruo albino."

    n "A pesar de que lleva gafas de sol,"

    n "ves que tuerce ligeramente la cabeza para mirar en tu dirección"

    n "mientras te parece que balbucea unas palabras en una voz que no logras escuchar."

    n "Después dirige su mirada al monstruo albino de nuevo."

    bog "Estáis violando el tratado del Liceo."

    bog "Ningún licántropo transformado puede pisar suelo urbano en la ciudad de Barcelona"

    bog "y menos usando artilugios o artes de ocultación."

    bog "Cesad inmediatamente vuestra actividad o ateneos a las consecuencias."

    ww01 "Grrr..."

    # ww02 "¡¿Es el perro?!"

    # ww02 "¡¿No decían que nunca abandonaba al César?!"

    n "Con un gesto poco amistoso se aparta del cuerpo de Neus."

    bog "Ahora dime,"

    bog "¿qué está pasando aquí?"

    ww01 "Es solo una antigua amiga."

    bog "Tienes cinco segundos para darme una mejor explicación."

    ww01 "..."

    ww01 "En realidad el que nos interesaba es el chico de ahí."

    bog "..."

    ono "POM"

    n "De un salto, el motorista barrigudo se acerca hasta ti."

    n "Al verlo de cerca, descubres que su rostro está marcado por una palidez casi absoluta,"

    n "rodeado de arrugas y cicatrices, su cabello es oscuro, largo y grasiento, al igual que su tupida barba."

    n "Sus oscuras gafas de sol te impiden ver sus ojos,"

    n "pero aún así tienes la sensación de que te observa con un ansia y apetito que te hiela la sangre,"

    n "al menos la escasa que sigue en tu cuerpo."

    bog "No le queda mucho tiempo de vida."

    pt "¿Me está hablando a mi?"

    bog "No."

    bog "No puedo lamerle la herida."

    bog "Si empiezo, no pararé hasta matarlo."

    bog "No."

    bog "Que vengas no es una buena idea."

    pt "¿Con quién está hablando?"

    bog "No,"

    extend " el mariposón no puede venir."

    bog "Está reforzando la burbuja para alejarlos,"

    bog "pero no creo que vaya a aguantar mucho más."

    pt "¿Mariposón?"

    bog "Podría meterlo dentro de una bolsa de basura."

    bog "Comérmelo entero también es una opción."

    pt "¡¿Cómo?!"

    bog "No me matarán si logro escapar."

    bog "El mariposón..."

    bog "Sí..."

    bog "De acuerdo."

    bog "¿Y entonces qué coño quieres que haga?"

    ne "Yo puedo cerrarle la herida."

    n "Dejando un rastro de sangre y yendo coja de un pie,"

    n "Neus logra llegar hasta el coche -apoyándose en él-"

    n "mirando al barrigudo con un rostro que aparenta serenidad."

    bog "..."

    bog "Entonces hazlo."

    ne "Solo si el César me promete que nos dejará escapar,"

    ne "y que no nos seguirá ni usará ninguna artimaña para rastrearnos."

    bog "..."

    bog "¿Quieres que muera?"

    bog "Porque no le queda mucho."

    p "..."

    ne "Si le salvo y luego os lo lleváis,"

    ne "tendrá un destino peor que la muerte,"

    ne "así que no."

    bog "¿Cómo sabes que luego no cambiaré de opinión?"

    ne "Por eso he mencionado al César,"

    ne "sé que estás hablando con él"

    ne "y lo conozco lo suficiente como para saber lo importante que es para él no romper su palabra."

    bog "..."

    bog "Elur..."

    bog "Eres una de esas ninfómanas hermanas incestuosas del país Vasco,"

    extend " ¿verdad?"

    ne "Lo dices como si vosotros hicierais cosas mejores."

    bog "Por lo menos no me follo a mi hermano."

    ne "Quizás es porque hace décadas que..."

    n "Tus sentidos están prácticamente nublados y obstruidos,"

    n "pero te parece ver y escuchar el puño del barrigudo estremeciéndose con fuerza."

    bog "Puede que haya aceptado el hecho de que me llamen el perro del César."

    bog "Pero te recomiendo que elijas bien tus siguientes palabras, niñata."

    ne "..."

    ne "Por mucho que tengas a alguien fuera reforzando la barrera"

    ne "para impedir que la mitad de los vampiros de esta ciudad entren aquí,"

    ne "este chico morirá en los próximos minutos."

    ne "Si no hago nada para impedirlo,"

    ne "tendrás una batalla campal,"

    ne "a pocas horas de salir el sol,"

    ne "y en medio de la ciudad"

    ne "que no podrás evitar."

    bog "..."

    ne "No creo que al César le interese semejante escándalo en su ciudad,"

    ne "y menos cuando mañana es el solsticio de verano."

    bog "¿Te atreves a chantajearle?"

    ne "Es lo que parece."

    bog "..."

    bog "No."

    bog "¡No!"

    bog "¡Puedo llevármelo de aquí!"

    bog "¡No necesito a la niñata esta!"

    bog "¡Y yo que sé si se morirá por el camino!"

    bog "¡Pues claro que hay muchas posibilidades!"

    bog "¡Si se largan de aquí no los volverás a ver!"

    bog "..."

    n "Sientes un ligero temblor que hace vibrar todos y cada uno de los cristales"

    n "que hay por por el coche y por el suelo."

    n "El ambiente se siente frío y algo más oscuro."

    n "Los licántropos os miran como si fueran tres aterrados perros en la lejanía"

    n "mientras Neus intenta mantener la compostura"

    n "y tú te estás muriendo por momentos."

    ne "Quiero su palabra de que también dejará escapar a la conductora."

    bog "..."

    bog "Estás moviéndote por hielo quebradizo..."

    bog "Grhh..."

    bog "De acuerdo."

    bog "Tienes la palabra del César."

    ne "..."

    bog "¿Es que no me has oído niñata?"

    ne "Sí..."

    extend " sí..."

    bog "¡Pues date prisa!"

    n "Neus se sube a gatas encima del chasis dónde estás"

    n "y con su larga y ardiente lengua empieza a lamerte la longeva herida del brazo."

    bog "No olvides limpiar el resto de la sangre que hay por el capó y el suelo."

    ne "Primero necesito darle un poco de mi sangre."

    bog "No juegues con mi paciencia."

    n "Ves que se muerde la muñeca de su mano y te la acerca a tus labios."

    ne "Bebe."

    n "Sin rechistar, obedeces sus palabras."

    bog "Mariposón,"

    bog "necesito que aguantes un poco más."

    bog "Sí,"

    bog "ha habido cambio de planes."

    ne "Estás muy débil,"

    extend " así que supongo que no te afectará de inmediato."

    bog "¡No!"

    bog "¡No voy a tener una cita contigo si lo logras!"

    ne "Pero al menos permitirá que tus órganos y cerebro trabajen con más normalidad."

    bog "Niña."

    bog "No tenemos toda la noche."

    n "Neus aparta su muñeca, se aleja de ti y se pone a lamer lo que hay alrededor de tu brazo."

    n "Sientes su cálido aliento alejarse a medida que tus ojos se van cerrando."

    scene black
    with fade

        ## If you have the ankh colar, it will burn on your chest if you're in danger, and if there's time, your mother will appear to protect you both, but not 100% it will work.


        ###


        # El ruido de metal te despierta de nuevo y agradeces la brisa que respiras una vez lograis salir al exterior, descubres que estás a las afueras de la ciudad, una luz brillante de unos foco de coche te dejan sin vista durante unos segundos. ¡¿Nos han descubierto?!

        # Ella se acerca al coche, saludo al conductor, y te pone en la parte de atrás y se acomoda contigo al otro lado del coche. Ordenado al conductor que arranque.

        # Te pregutna si estás bien, le respondes que sí... que adónde vais, ella te dice que no te preocupes, que descanses, le dices que no importa, que estás bien, que puedes aguantar, pero lo comodo que es el asiento y lo cansado que estás hace que cierres los ojos por uninstante y la oscuridad se cierne sobre ti.

    ###

    ## Now in the car.

    pause

label night05_elysium_AfterSex_carLeaving:

    ono "slurp"

    p "Ughh..."

    ono "slurp"

    n "Algo cálido y húmedo se mueve alrededor de tu erección matinal diaria,"

    n "aunque lo percibes como si llevaras un condón de varios centímetros de grosor."

    scene day06
    with fade

    n "A través de tus párpados -aún cerrados- descubres que ya es de día."

    pt "¿Estoy en un coche...?"

    n "Al separarlos, lo primero que ves es un frondoso bosque"

    n "a través del cristal de la puerta del coche en el que estás"

    n "que rápidamente queda atrás por la velocidad a la que os desplazáis,"

    n "mientras percibes la gruesa tela del asiento"

    n "a través de tu culo desnudo."

    n "Pensaba que había perdido solo medio pantalón..."

    ono "slurp"

    n "Cuando bajas la mirada descubres la melena oscura de Neus subiendo y bajando."

    pt "¿Me la está chupando?"

    n "Tienes el cuerpo tan agotado y entumecido"

    n "que todo él lo sientes como si llevaras una segunda piel"

    n "y tu polla no es una excepción."

    n "Es como si te la estuviera lamiendo a través de un grueso y rígido plástico,"

    n "pero aún así notas la humedad y calidez de su lengua."

    p "¿Qué haces?..."

    n "Lentamente se detiene y levanta la cabeza para mirarte a los ojos."

    ne "[protname],"

    ne "¿te encuentras bien?"

    p "Euhm..."

    p "Estoy un poco grogui..."

    n "A pesar de haber apartado sus labios, su mano sigue masajeándola."

    ne "Me alegro que te hayas despertado,"

    ne "después de la cantidad de sangre que perdiste,"

    ne "no estaba segura si te despertarías tan pronto."

    pt"Mi brazo..."

    n "Al fijarte en él no encuentras ni siquiera un rasguño."

    ne "Eres más fuerte de lo que pareces."

    n "Baja la cabeza de nuevo retomando su labor."

    p "Neus..."

    n "Sin detenerse en su movimiento bucal:"

    ne "Dime..."

    p "No me siento demasiado la entrepierna."

    ne "¿Solo la entrepierna?"

    p "Bueno..."

    ne "Tranquilo,"

    extend " es normal."

    p "..."

    ne "Lo siento,"

    ne "es que he visto que se te iba poniendo dura y no he podido resistir la tentación."

    n "Retuerce su longeva lengua a lo largo de tu miembro"

    n "mientras sus labios succionan la punta juguetonamente."

    ne "No sé si te acuerdas de lo que pasó ayer,"

    ne "pero tuve que gastar mucha energía y..."

    extend " sinceramente,"

    ne "estoy muerta de hambre..."

    p "Euh..."

    n "Rápidamente hunde su rostro hundiendo tu miembro casi hasta la mitad en el interior de su garganta."

    p "Ghhmm..."

    n "Hasta que se aparta de nuevo sin dejar de acariciártela con la mano."

    ne "Cuando llegó el gordinflón de las gafas de sol estaba en las últimas..."

    ne "Si no te hubieras cortado con ese cristal,"

    ne "sinceramente,"

    ne "no sé qué hubiera pasado."

    p "¿El que conduce es un hombre?"

    ne "Sí."

    ne "Veo que vas recuperando la vista."

    p "¿No era una mujer?..."

    n "Tienes los labios tan entumecidos que tu voz suena ronca y apenas inteligible."

    ne "Era."

    ne "Hemos cambiado de vehículo y de conductor varias veces."

    p "..."

    p "Creo que nos está mirando..."

    ne "¿Hmm...?"

    n "Mira en esa dirección de modo vago y casi sin interés."

    ne "No te preocupes por él."

    n "Vuelve a meterse el miembro en su interior."

    p "Hmm..."

    n "A pesar de lo aletargado y entumecido,"

    n "tienes la sensación que hace ya un buen rato que está jugueteando con él."

    n "Percibes el ardor de su lengua,"

    n "su forma de juguetear con tu miembro,"

    n "su garganta desplazándose y acariciando tu miembro de un modo inhumano,"

    n "-como si tuviera vida propia-"

    n "mientras te parece lo que son pequeñas lenguas"

    n "acariciando el contorno de tu glande en el fondo de su garganta."

    p "Neus..."

    ne "¿Hmmm...?"

    p "Yo..."

    with vpunch
    p "Ughh.."

    n "Todo tu cuerpo tiembla hasta que finalmente descargas en su boca."

    n "Velozmente, desciende su rostro hasta tragarse tu miembro hasta casi la mitad."

    ono "glup"

    n "Como si fuera una bomba de succión automática,"

    ono "glup"

    n "sigue tragando,"

    ono "glup"

    n "y succionando,"

    ono "slurp"

    n "hasta que tienes la impresión que está aspirando el aire de tus pulmones a través de tu polla."

    n "Finalmente se aparta."

    n "No sin antes darle un beso a la punta de tu -aún más adormecido- miembro"

    n "para luego ascender hasta tu rostro hasta mirarte con sus felinos -y ligeramente brillantes- ojos."

    ne "¿Va todo bien?"

    p "Seehh..."

    ne "Me alegra oír eso."

    p "Hmm..."

    ne "¿Qué pasa?"

    p "Hay un problema..."

    n "Notas una nueva presión en tu entrepierna."

    ne "¿Qué ocurre?"

    p "Estando tan relajado..."

    p "y haciendo tanto tiempo que no voy al baño..."

    ne "Hmmm..."

    n "Sus ojos se dirigen de nuevo a tu entrepierna."

    p "La erección evitaba que..."

    ne "No te preocupes."

    n "Vuelve a dirigirte esa mirada felina y juguetona."

    ne "Si necesitas descargar,"

    ne "simplemente hazlo."

    p "¿Tienes alguna botella o pote?"

    ne "No lo necesitamos."

    n "Agarrándote por el pecho desciende su rostro de nuevo."

    p "No voy a aguantar mucho más..."

    n "Sientes su aliento rozando tu adormecida piel."

    p "Neus..."

    n "Sus labios acariciando la parte superficial."

    p "No voy a..."

    p "Aaah-aahh...."

    n "Te relajas tanto,"

    scene black
    with fade

    n "que terminas cerrando los ojos de nuevo."


label night05_elysium_AfterSex_hotelParking:

    pause

    ono "PAM"

    p "¿Euh...?"

    n "El ruido del portazo de una puerta de coche te despierta de tu somnolencia."

    scene day05
    with fade

    n "Sigues sentado en el vehículo,"

    n "pero te da la sensación de que estás reposando tu cabeza en la puerta opuesta,"

    n "hasta descubres que ni siquiera estás en el mismo vehículo que antes."

    n "Al mirar por la ventana ves que el lugar está a oscuras."

    pt "¿Es de noche?"

    pt "No..."

    pt "Parece un parking subterráneo..."

    ono "Click"

    n "Ves a Neus abriéndote la puerta mientras te sujeta por el hombro para que no caigas al suelo."

    n "Percibes sus brazos por tu espalda mientras te coge en brazos."

    h01 "¿Necesita ayuda?"

    ne "No, tranquilo,"

    ne "ya me las apaño."

    n "con su trasero logra cerrar el coche."

    ne "Recuerda lo que te he dicho."

    h02 "Por supuesto."

    n "Sin darte cuenta,"

    scene black
    with fade

    n "vuelves a cerrar los párpados."

    pause

label night05_elysium_AfterSex_hotelHall:

    h01 "{i}Bonsoir Miss Elur{/i}."

    n "Oyes la voz de lo que parece un hombre adulto en tono educado dirigiéndose a Neus que sigue cargando contigo."

    h01 "{i}Avez-vous besoin d'aide pour déplacer votre dîner ?{/i}"

    scene day06
    with fade

    n "Al entreabrir los ojos,"

    n "descubres que estáis en lo que parece la recepción de un hotel de lujo"

    n "y el hombre que os está hablando lleva un vestido de etiqueta con corbata."

    ne "{i}Non,"

    extend " merci{/i}."

    ne "{i}J'ai juste besoin des clés des chambres{/i}."

    pt "¿Están hablando en francés?"

    h01 "{i}Bien sûr,"

    extend " les voici{/i}."

    n "Ves a ese hombre que se acerca,"

    n "le pone una tarjeta en la mano,"

    n "la cual sigue sujetándote como si fueras una esposa en brazos de su recién esposo."

    n "Cuando este se retira:"

    p "Neus..."

    ne "Shh..."

    ne "Ahora no."

    if gensex_ILoveYouNeus:

        ne "Relájate mi amor,"

    else:

        ne "Relájate,"

    extend " ya casi llegamos."

    ne "Descansa un poco más."

    n "Vuelve a mirarte con sus brillantes ojos"

    scene black
    with fade

    n "y caes de nuevo en la oscuridad."

    pause

    jump endupdate

    # jump day06_night_label


# Neus...

## Shhh... No digas nada, relájate mi amor, ya casi llegamos. Descansa un poco más.

# Hace algo con sus ojos y vuelves a caer en un sueño profundo.


##Jump 6th DAY.

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
#


# '''


#     Images of Didac Dying or being rape by Fater, or even the Blonde one if Didac points are really low.

#     ¿Quien era ese hombre-lobo enorme?


#     ------

#     Primero empieza con una mamada para ir calentando la situación, Lengua larga y ojos brillantes como la noche anterior. Te hace correr te guste o no.

#     Luego tú tomas el control, más transformaciones, dientes afilado, pechos algo más grandes. Después de correrte,

#     Ella se pone encima y toma el control, más transformaciones, mucho más terrorífica, con alas, cola, pezuñas...

#     Después del tercer orgasmo pierdes la conciencia, ella te dice que no te preocupes de nada, que ella se encargará de todo.

#     Luego te la encuentras chupándoltea en un coche en pleno día. Vuelves a perder la conciencia.

#     Finalmente despiertas acomodado en una cama, mientras oyes y sientes algo en tu entrepierna. Es Neus que te está cabalgando, pero esta vez no es un sueño.


# '''


label night05_elysium_AfterSex_noEscape:

    n "Debido al dolor que sufre por el pie roto,"

    n "la conductora se desplaza a gatas para intentar escapar del lugar,"

    n "pero antes de que logre llegar demasiado lejos el licántropo de pelaje oscuro,"

    n "que a duras puede andar -pero que desde luego se desplaza a mayor velocidad que alguien que va a gatas-,"

    n "logra alcanzarla."

    ww03 "¿A dónde crees que ibas?" # Red Fur

    dri "¡Por favor...!"

    n "Mientras tiene a Neus agarrada por ambos brazos:"

    ww02 "¡Un poco más y se te escapa la conductora!" # Black Fur 

    ww03 "¡Por si no lo has notado, estoy ocupado!" # Red Fur

    ww01 "¡Céntrate y no la sueltes!"

    ww03 "¡Ya lo hago!"

    n "El licántropo albino la sujeta por los pies."

    n "Entre ambos la tienen completamente inmovilizada en el suelo."

    ww03 "De todos modos parece que ya no tiene tanta fuerza como antes."

    ww01 "Yo no me fiaría de esta bruja."

    ww01 "Estoy seguro que aún se guarda algo de fuerza bajo la manga"

    ww01 "y no dudes que la usara para morderte cuando menos te lo esperes."

    ww03 "Hmmmm..."

    ww03 "¿Entonces la inmovilizamos en condiciones?"

    ww01 "No veo por qué no."

    # BROKING LEGS




    ## NOT_FINISHED - STORY
    call WIP


    # The three wolfes fuck those women. 

    ## They broke arms and legs of Neus, even her teeth.

    ## White fucks Neus Ass, Red her mouth and the black fucks the driver.

    # Neus bites the dick of the Red with her sharp teeth and starts screaming, white tells him, I warned you.

    # Neus Screams very loud. El lobo albino no le gusta cómo ha sonado eso. Le ordena a rojo que agarra a Neus, al negro que coja a la Conductura y él te agarra a ti  para salir cagando leches del lugar atravesando la autopista para alejar se de la zona urbana.

    # When Neus has an Orgasm. She's possesed by her Father. Which then enters in the Werewolf.

    # He walks upon to you, and You can see in the wolfs eyes, the eyes of the Red Goat eyes of your Father.

    ## I told you. It was just a matter of time. Sooner or later I'd end up finding you both. ## Tarde o temprano acabaría encontrandoos.

    

    jump gameover