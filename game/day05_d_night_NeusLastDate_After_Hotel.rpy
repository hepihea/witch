default night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_Cond = False
default night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_NotGF_Cond = False
default night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_Cond = False
default night05_NeusLastDate_After_HotelKrueger_Happened_Cond = False
default night05_NeusLastDate_Noria_Not = False
default night05_NeusLastDate_Noria_Angry_ToldYouDidacFate = False # When Neus phone you to tell you Didac is pregnant and you´ll see her not anymore.

default d_bodyType = ""


default night05_NeusLastDate_Noria_Kiss_First_Try = 0

label night05_NeusLastDate_After_HotelKrueger:

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(0.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.5, delay=15.0, channel='sfx1')

    scene black
    hide screen quick_menu
    with fade 

    $ saturation_tint_level = "verydark"

    $ mmouthp = "" # is not "_blue" anymore.

    n "Sientes un ligero dolor de cabeza,"

    n "a la vez que un montón de voces a tu alrededor."

    #########################################################

    if config.version < "00.12.04": # Before Third Door.
        
        call endupdatescript
    
    #######################################################

    pt "¿Euh...?"

    ne "¡[protname]!"

    ne "¡¿Estás bien?!"

    pt "¿Neus...?"

    pt "¿Eres tú realmente...?"

    $ renpy.music.set_volume(0.2, delay=15.0, channel='sfx1')

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    scene bg dark_a_blurry_02
    show night05_tibidabo_medic_body_blurry Silent:
        truecenter
        zoom 0.5
    show night05_tibidabo_medic_hand empty:
        truecenter
        zoom 0.5
    show morning04_bedroom_DMast_blinkeye
    with fade

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()
        with dissolve

    n "Por fin logras separar tus párpados." 

    show night05_tibidabo_medic_body_blurry Talking
    with dissolve

    b01 "Bien,"

    b01 "parece que vuelve en sí..."

    show night05_tibidabo_medic_body_blurry Silent
    with dissolve

    pt "¿Y ese chaleco amarillo?"

    pt "¿Será un paramédico?"

    show night05_tibidabo_medic_body_blurry Talking
    with dissolve

    b01 "¿Cómo te encuentras, chaval?"

    show night05_tibidabo_medic_body_blurry Silent
    with dissolve

    p "Euhh..."

    p "Algo mejor..."

    show night05_tibidabo_medic_hand blurry
    with fade

    # 4 fingers.

    b01 "¿Cuántos dedos ves aquí?"

    hide morning04_bedroom_DMast_blinkeye
    with fade

    p "..."

    show night05_tibidabo_medic_hand
    with Dissolve (1.0)

    p "Cuatro."

    scene bg dark_a_blurry_01
    show night05_tibidabo_medic_body:
        night05_tibidabo_medic_body
    show night05_tibidabo_medic_exp_mouth sad_Talkingx03:
        night05_tibidabo_medic_exp_pos
    show night05_tibidabo_medic_exp_eyes 03:
        night05_tibidabo_medic_exp_pos
    show night05_tibidabo_medic_exp_piris front03:
        night05_tibidabo_medic_exp_pos
    show night05_tibidabo_medic_exp_eyebrows normal:
        night05_tibidabo_medic_exp_pos
    show night05_tibidabo_medic_hair_front:
        night05_tibidabo_medic_body
    with Dissolve (1.0)

    b01 "Bien."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx04
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    b01 "¿En qué día estamos?"

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_eyebrows normal
    with dissolve

    p "Es domingo,"

    extend " veintidós de junio."

    show night05_tibidabo_medic_exp_mouth happy_Talkingx03
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    b01 "Muy bien."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx04
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    b01 "¿Cómo te llamas?"

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    menu night05_NeusLastDate_After_HotelKrueger_Medic_Name_Question:

        pt "Mi nombre..."

        "[protname].":

            call p_Help

            show night05_tibidabo_medic_exp_mouth sad_Silentx02
            show night05_tibidabo_medic_exp_eyebrows surprisex01
            with dissolve

            p "[protname]."

            show night05_tibidabo_medic_exp_mouth sad_Talkingx02
            show night05_tibidabo_medic_exp_piris right03
            show night05_tibidabo_medic_exp_eyebrows surprisex01
            with dissolve

            b01 "¿Es correcto?"

            show night05_tibidabo_medic_exp_mouth happy_Silentx02
            show night05_tibidabo_medic_exp_piris right03
            show night05_tibidabo_medic_exp_eyebrows angryx01
            with dissolve

            ne "Sí."

            jump night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_label

        "Hermenegildo V de Austria.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            jump night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong

        "Pepito el de los palotes.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            jump night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong

        "Vegeta, rey de los Saiyans.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            jump night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong

label night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong:

    show night05_tibidabo_medic_exp_mouth sad_Silentx05
    show night05_tibidabo_medic_exp_eyes 07
    show night05_tibidabo_medic_exp_piris empty
    show night05_tibidabo_medic_exp_eyebrows angryx03
    with dissolve

    b01 "..."

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    ne "¡No es momento para bromas [protname]!"

    show night05_tibidabo_medic_exp_mouth sad_Silentx04
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows angryx03
    with dissolve

    p "..."

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_eyebrows angryx02
    with dissolve

    p "Lo siento..."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx05
    show night05_tibidabo_medic_exp_eyebrows suspiciousx02
    with dissolve

    b01 "Bueno si eres capaz de ser tan gracioso,"

    show night05_tibidabo_medic_exp_mouth sad_Talkingx04
    show night05_tibidabo_medic_exp_eyes 07
    show night05_tibidabo_medic_exp_piris empty
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    b01 "me imagino que el problema tampoco es tan grave."

    jump night05_NeusLastDate_After_HotelKrueger_Medic_Finished

label night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_label:

    show night05_tibidabo_medic_exp_mouth sad_Talkingx03
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    b01 "¿Cómo se llama tu novia?"

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    ne "Euhh..."

    extend " Yo..."

    show night05_tibidabo_medic_exp_mouth sad_Silentx04
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    menu night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_Question:

        pt "¿Mi novia?"

        "Se llama Neus, pero no es mi novia.":

            call p_Help

            #$pl.ch_pts("np",-1)

            $ night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_NotGF_Cond = True

            show night05_tibidabo_medic_exp_mouth sad_Talkingx03
            show night05_tibidabo_medic_exp_eyes 03
            show night05_tibidabo_medic_exp_piris front03
            show night05_tibidabo_medic_exp_eyebrows sadx01
            with dissolve

            b01 "Vaya,"

            show night05_tibidabo_medic_exp_mouth sad_Talkingx02
            show night05_tibidabo_medic_exp_eyes 03
            show night05_tibidabo_medic_exp_piris right03
            show night05_tibidabo_medic_exp_eyebrows sadx02
            with dissolve

            b01 "lamento la confusión."

            show night05_tibidabo_medic_exp_mouth sad_Silentx03
            show night05_tibidabo_medic_exp_eyes 03
            show night05_tibidabo_medic_exp_piris right03
            show night05_tibidabo_medic_exp_eyebrows sadx03
            with dissolve

            ne "..."

            jump night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_After

        "Se llama Baba Yaga.":

            call p_Help

            $pl.ch_pts("np",-2)

            jump night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong

        "Se llama Bruja Pirula.":

            call p_Help

            $pl.ch_pts("np",-3)

            jump night05_NeusLastDate_After_HotelKrueger_Medic_Name_Wrong

        "Neus.":

            call p_Help

            $pl.ch_pts("np",1)

            $ night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_Cond = True

            jump night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_After
 

label night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_After:

    show night05_tibidabo_medic_exp_mouth happy_Talkingx01
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    b01 "Bueno,"

    extend " parece que no es nada grave."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx02
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows sadx01
    with dissolve

    b01 "¿Sueles tener este tipo de desmayos o mareos repentinos?"

    show night05_tibidabo_medic_exp_mouth sad_Silentx01
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows serious
    with dissolve

    p "No..."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx02
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows normal
    with dissolve

    b01 "Neus,"

    extend " ¿verdad?"

    show night05_tibidabo_medic_exp_mouth happy_Silentx02
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows serious
    with dissolve

    ne "Sí..."

label night05_NeusLastDate_After_HotelKrueger_Medic_Finished:

    show night05_tibidabo_medic_exp_mouth sad_Talkingx04
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows serious
    with dissolve

    if night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_Cond == True:

        b01 "Llama a este número si ves que tu chico vuelve a desmayarse"

    else:

        b01 "Llama a este número si ves que tu amigo vuelve a desmayarse"

    show night05_tibidabo_medic_exp_mouth sad_Talkingx02
    show night05_tibidabo_medic_exp_eyebrows angryx01
    with dissolve

    b01 "o le vuelve a suceder algo extraño."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx01
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows serious
    with dissolve

    b01 "Por ahora debería de estar bien,"

    show night05_tibidabo_medic_exp_mouth happy_Talkingx01
    show night05_tibidabo_medic_exp_eyes 07
    show night05_tibidabo_medic_exp_piris empty
    show night05_tibidabo_medic_exp_eyebrows sadx01
    with dissolve

    b01 "pero nunca se sabe."

    show night05_tibidabo_medic_exp_mouth sad_Silentx03
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    ne "Muchas gracias."

    show night05_tibidabo_medic_exp_mouth happy_Talkingx02
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows normal
    with dissolve

    b01 "Para eso estamos."

    show night05_tibidabo_medic_exp_mouth sad_Talkingx04
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris front03
    show night05_tibidabo_medic_exp_eyebrows serious
    with dissolve

    b01 "Recordad que en treinta minutos cierran el parque."

    show night05_tibidabo_medic_exp_mouth happy_Talkingx03
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows normal
    with dissolve

    b01 "Disfrutad lo que os queda de noche."

    show night05_tibidabo_medic_exp_mouth happy_Silentx03
    show night05_tibidabo_medic_exp_eyes 03
    show night05_tibidabo_medic_exp_piris right03
    show night05_tibidabo_medic_exp_eyebrows surprisex01
    with dissolve

    ne "Muchas gracias."

    scene bg dark_a
    with dissolve_05s

    p "Hmm..."

    show bg dark_a:
        subpixel True
        easein_quad 3.0 zoom 1.2

    n "Haces el esfuerzo para intentar ponerte de pie,"

    play sound "audio/sfx/fall04.ogg"

    scene black
    with vpunch

    n "pero tu cuerpo aún no te responde adecuadamente, y el dolor de cabeza no ayuda..."

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "almost_new_kevin"

    scene bg dark_a
    show n_closefromup_body sd:
        n_closefromup_075_position
    show n_closefromup_blush 01:
        n_closefromup_075_position
    show n_closefromup_eyes 01:
        n_closefromup_075_position
    show n_closefromup_iris front01:
        n_closefromup_075_position
    show n_closefromup_eyebrows sadx04:
        n_closefromup_075_position
    show n_closefromup_tears empty:
        n_closefromup_075_position
    show n_closefromup_mouth sad_Talkingx03:
        n_closefromup_075_position
    show n_closefromup_glasses:
        n_closefromup_075_position
    show n_closefromup_hair_front:
        n_closefromup_075_position
    with fade

    if pl.np >= 120: # NOT FINISHED... number?

        ne "No tan deprisa, mi Lancelot..."

    else:

        ne "No tan deprisa..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth happy_Talkingx02
    with dissolve
    
    ne "Descansa un poco."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    p "¿Qué ha pasado?"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "Justo cuando ibas a subir las escaleras movedizas,"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "te has caído en redondo al suelo y has estado inconsciente por unos veinte minutos."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    pt "¿Solo veinte minutos?"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows surprisex01
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    p "¿No he llegado ni a subir las escaleras?"

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx02
    with dissolve

    ne "No..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "¿Has soñado algo extraño?"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    menu night05_NeusLastDate_After_HotelKrueger_Happened_Question:

        pt "¿Podré decirle la verdad?"

        "<Contarle lo sucedido>" if night05_NeusLastDate_After_HotelKrueger_Happened_Cond == False:

            call p_Help

            $ night05_NeusLastDate_After_HotelKrueger_Happened_Cond = True

            p "Euhmm..."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows normal
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            ne "..."

            show n_closefromup_eyes 00
            show n_closefromup_iris front00
            show n_closefromup_eyebrows suspiciousx01
            show n_closefromup_mouth sad_Silentx04
            with dissolve

            p "..."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth sad_Talkingx05
            with dissolve

            ne "¿Seguro que estás bien?"

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows serious
            show n_closefromup_mouth sad_Silentx03
            with dissolve

            p "..."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows suspiciousx01
            show n_closefromup_mouth sad_Silentx05
            with dissolve

            pt "Como era de esperar,"

            extend " no se lo puedo contar..."

            jump night05_NeusLastDate_After_HotelKrueger_Happened_Question

        "Podríamos decir que algo así...":

            call p_Help

            jump night05_NeusLastDate_After_HotelKrueger_Happened_After

label night05_NeusLastDate_After_HotelKrueger_Happened_After:

    show bg_night05_bg_castle_siege:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.25 ypos -0.25
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.11
    with fade

    n "Observas atentamente a tu alrededor."

    ne "¿Has perdido algo?"

    pt "Como me imaginaba,"

    pt "la mujer alta y pechugona que nos bloqueaba el paso en la atracción,"

    extend " no está..."

    hide bg_night05_bg_castle_siege
    show n_closefromup_eyes 00
    show n_closefromup_iris front00
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Silentx04
    with fade

    pt "Y, qué sorpresa..."

    extend " tampoco se lo puedo preguntar."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    pt "Me imagino que se habrá ido."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Silentx06
    with dissolve

    pt "Sería absurdo buscarla ahora..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "¿Te encuentras con fuerzas para levantarte?"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    p "Creo que sí..."

    scene bg night05_bg_castle_queue_out:
        truecenter
        zoom 0.5
    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 02:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris front01:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx05:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with fade

    ne "Bueno..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx04
    with dissolve

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    ne "Supongo que deberíamos dar por finalizada la noche..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "tampoco es que nos quede mucho tiempo."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx06
    with dissolve

    menu night05_NeusLastDate_After_HotelKrueger_EndDate_Question:

        pt "Parece que la última cita que acordamos se ha terminado."

        "Bueno, me alegro de que ya se haya terminado...":
            call p_Help

            $pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 00
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex01
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            p "¿Qué?"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "¿Tan mal lo has pasado?"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx06
            with dissolve

            menu night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_Question:

                pt "¿Qué le digo ahora...?"

                "Si sigo aquí, es por Dídac; no por ti.":
                    call p_Help

                    $pl.ch_pts("np",-1)

                    show neus_exp_mouth sad_Silentx08
                    show neus_exp_eyes 08
                    show neus_exp_iris front08
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx08
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    ne "Ya te he dicho que pasara lo que pasara,"

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Dídac volvería a ser hombre..."

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_tears 02_01
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "Solo esperaba que pudieras disfrutar un poco más de mi compañía."

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 01
                    show neus_exp_iris right01
                    show neus_exp_tears 01_01
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Al menos por una noche más..."

                    jump night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_After

                "Se me ha hecho eterno.":
                    call p_Help

                    $pl.ch_pts("np",-1)

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 03
                    show neus_exp_iris right03
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Siento que te hayas aburrido tanto..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 04_01
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Esperaba que pudieras disfrutar mejor de mi compañía..."

                    jump night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_After

                "No me he divertido en absoluto.":
                    call p_Help

                    $pl.ch_pts("np",-3)

                    show neus_exp_mouth sad_Talkingx005
                    show neus_exp_eyes 00
                    show neus_exp_iris front00
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    ne "¿En absoluto?"

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "¿Tanto te has aburrido conmigo...?"

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_tears 01_01
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    p "..."

                    jump night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_After

                "La idea de venir a un parque como cita, ha sido una elección horrible.":
                    call p_Help

                    $pl.ch_pts("np",-2)

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyes 00
                    show neus_exp_iris front00
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 04_01
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "Pensé que en un parque podríamos pasárnoslo bien..."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_tears 02_01
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    p "Te recuerdo que me pediste sinceridad."

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_tears 04_02
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    ne "A veces no hace falta ser tan sincero..."

                    jump night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_After

                "En absoluto, pero por lo menos a partir de ahora podremos quedar sin la sombra del chantaje.":
                    call p_Help

                    $pl.ch_pts("np",3)

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 00
                    show neus_exp_iris front00
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    ne "Euhh..."

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows serious
                    with dissolve

                    ne "¿A qué te refieres?"

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    p "He disfrutado de tu compañía."

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows normal
                    with dissolve

                    p "Pero tengo la sensación de que has estado completamente tensa e incómoda durante estas tres citas,"

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows serious
                    with dissolve

                    p "forzándote a ser agradable y amable conmigo,"

                    extend " sin ser completamente tú misma."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyes 08
                    show neus_exp_iris front08
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 03
                    show neus_exp_iris right03
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "Reconozco que he estado muy nerviosa..."

                    show neus_exp_mouth sad_Talkingx08
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "Pero no es verdad que me haya comportado de manera tan distinta a cómo soy,"

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyes 01
                    show neus_exp_iris right01
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    ne "en realidad nunca había sido tan sincera y clara con alguien"

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyes 03
                    show neus_exp_iris right03
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "como lo he sido contigo."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    p "..."

                    show neus_exp_mouth happy_Silentx03
                    show neus_exp_eyes 08
                    show neus_exp_iris front08
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    ne "..."

                    jump night05_NeusLastDate_After_HotelKrueger_EndDate_After

                    # ne "En realidad lo he disfrutado mucho más de lo que me imaginaba;"

        "Lo lamento.":

            call p_Help

            $pl.ch_pts("np",1)

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyes 00
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "En absoluto,"

            jump night05_NeusLastDate_After_HotelKrueger_EndDate_After

        "<No decir nada>":

            call p_Help

            show neus_exp_mouth happy_Silentx02
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Hmm..."

            jump night05_NeusLastDate_After_HotelKrueger_EndDate_After

label night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_After:

    $ night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_Cond = True

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_tears 08_02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_tears 03_03
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Tranquilo..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_tears 06_04
    show neus_exp_eyebrows sadx05
    with dissolve

    n "Una lágrima empieza a desprenderse de su mejilla."

    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Ya nos vamos..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx07
    with dissolve

    jump night05_NeusLastDate_After_HotelKrueger_Leaving

label night05_NeusLastDate_After_HotelKrueger_EndDate_After:

    if (night05_Park_RollerCoaster_Used == True or
        night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == True or 
        night05_Park_MinigameShooter_Played == True):

        show neus_exp_mouth happy_Talkingx05
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
        with dissolve

        ne "En realidad lo he disfrutado mucho más de lo que me imaginaba;"

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "es solo que se me ha pasado muy rápido..."

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_eyebrows sadx01
        with dissolve

    else:

        show neus_exp_mouth sad_Talkingx005
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_eyebrows surprisex02
        with dissolve

        ne "Admito que podría haber ido mejor con un poco más de tu colaboración..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_eyebrows serious
        with dissolve

        ne "Pero siendo sincera,"

        extend " he disfrutado de tu compañía."

        show neus_exp_mouth happy_Talkingx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "En realidad el tiempo se me ha pasado muy rápido..."

        show neus_exp_mouth happybiting_Silentx03
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_eyebrows sadx01
        with dissolve

    menu night05_NeusLastDate_After_HotelKrueger_DateDuration_Question:

        pt "El tiempo..."

        "A mí también se me ha hecho bastante corta la noche a tu lado, Neus.":

            call p_Help

            show neus_exp_blush 03
            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            $pl.ch_pts("np",1)

            ne "..."

            play sound "audio/characters/neus/giggle02.ogg"

            show neus_exp_blush 04
            show neus_exp_mouth happy_Silentx05
            show neus_exp_eyes 07
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx01
            with dissolve

            n "Una dulce sonrisa se dibuja en su rostro."

        "<No decir nada>":

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 08
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Bueno..."

            call p_Help

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "¿Nos vamos?"

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    p "Sí."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx01
    with dissolve

    window hide dissolve
    pause

    ##

label night05_NeusLastDate_After_HotelKrueger_Leaving:

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(1.0, delay=1.5, channel='sfx1')


    scene bg night05_bg_tibidabo_park_00:
        subpixel True
        truecenter
        zoom 0.6 xpos -0.35 ypos 0.4
        ease 20.0 zoom 0.6 xpos 0.6 ypos 0.4 #Pose for Neus Speak
    with fade

    n "Volvéis por vuestros pasos alrededor del parque,"

    $ renpy.music.set_volume(0.1, delay=30.0, channel='sfx1')

    n "hasta llegar a la puerta cerca del funicular en el que habíais llegado."

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "almost_new_kevin"

    scene bg night05_bg_tibidabo_park_00:
        truecenter
        zoom 0.6 xpos 0.6 ypos 0.4
    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position
    
    show neus_exp_blush 02:
        neus_exp_atright_position
    show neus_exp_mouth sadbiting_Silentx04:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx04:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    n "La observas mirando con pesar la enorme atracción cerca del acantilado de la montaña."

    show night05_bg_tibidabo_park_00:
        subpixel True
        truecenter
        zoom 0.6 xpos 0.6 ypos 0.4
        easein_quad 10.0 zoom 0.75 xpos 1.65 ypos 0.4 # Noria
    with fade

    menu night05_NeusLastDate_Noria_Question:

        pt "Es verdad..."

        "<Recordarle que quería subirse a la noria antes de irse del parque>":
            call p_Help

            if ((night05_Park_RollerCoaster_Used == False and
                night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False and 
                night05_Park_MinigameShooter_Played == False) and 
                pl.np < 100) or pl.np < 15: # puntuation # not_finished.

                hide night05_bg_tibidabo_park_00
                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with fade

                p "Me dijiste que antes de irnos del parque,"

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyes 04
                show neus_exp_iris left04
                show neus_exp_eyebrows surprisex02
                with dissolve

                p "te querías subir a la noria para observar desde lo más alto las vistas de Barcelona de noche."

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyes 08
                show neus_exp_iris front08
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Tranquilo."

                if night05_NeusLastDate_After_HotelKrueger_EndDate_Bad_Cond == True:

                    $pl.ch_pts("np",-2)

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_tears 03_01
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Después de que me hayas dicho lo mucho que te has aburrido en esta cita,"

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyes 02
                    show neus_exp_iris right02
                    show neus_exp_tears 02_01
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    ne "se me han pasado las ganas de subirme."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 04_02
                    show neus_exp_eyebrows angryx03
                    with dissolve

                else:

                    $pl.ch_pts("np",-1)

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 04_01
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Ya no me apetece subirme ahí."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_tears 01_01
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    p "¿Por qué?"

                    show neus_exp_mouth sad_Talkingx08
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_tears 03_01
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Creo que es bastante evidente."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 04_02
                    show neus_exp_eyebrows angryx05
                    with dissolve

                jump night05_NeusLastDate_Noria_Angry

            else:

                $pl.ch_pts("np",1)

                jump night05_NeusLastDate_Noria_Beginning

        "<No decir nada>":
            call p_Help

            if ((night05_Park_RollerCoaster_Used == False and
                night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False and 
                night05_Park_MinigameShooter_Played == False) and
                pl.np < 100):

                hide night05_bg_tibidabo_park_00
                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyes 02
                show neus_exp_iris right02
                show neus_exp_eyebrows angryx03
                with fade

                ne "Lo mejor es que cada uno se vaya por su lado."

                jump night05_NeusLastDate_Noria_Angry

            else:

                jump night05_NeusLastDate_Noria_Not


label night05_NeusLastDate_Noria_Not:

    $ night05_NeusLastDate_Noria_Not = True

    pt "Es mejor no perder más tiempo..."

    jump night05_NeusLastDate_Noria_Message

#label night05_NeusLastDate_Noria_Message:

    #ono "*BEEP*"

    #p "Hmm..."

    #ne "¿Qué ocurre?"

    #p "Es mi móvil,"

    #ne "¿Un mensaje?"

label night05_NeusLastDate_Noria_Beginning:

    p "Me dijiste que antes de irnos del parque,"

    p "te querías subir a la noria para observar desde lo más alto las vistas de Barcelona de noche."

    hide night05_bg_tibidabo_park_00
    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with fade

    ne "¿Euh...?"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 00
    show neus_exp_iris left00
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Sí..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows serious
    with dissolve

    ne "es verdad."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 03
    show neus_exp_iris down03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Pero,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "¿seguro que te encuentras bien?"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "Es una noria Neus,"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "no una montaña rusa;"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    p "creo que sería capaz de sobrevivir si por una extraña razón me volviera a caer."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "Hmm..."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with dissolve

    n "Una tímida sonrisa aparece en su rostro."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "De acuerdo."

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx01
    with dissolve

    window hide dissolve
    pause

    scene bg night05_bg_wheel_queue:
        subpixel True
        truecenter
        xpos 0.5 ypos 0.5 zoom 0.5 
        ease_quad 10.0 xpos 0.8 ypos 0.8 zoom 1.0
    with fade

    n "Por suerte la cola de esta atracción resulta ser bastante corta,"

    scene bg night05_bg_wheel_far:
        subpixel True
        truecenter
        zoom 0.5
        ease_quad 10.0 zoom 1.0
    with fade

    $ saturation_tint_level = "dark"

    n "y rápidamente accedéis a una de las cabinas los dos solos."

    $ renpy.music.set_volume(0.01, delay=30.0, channel='sfx1')
    
    scene black
    show bg night05_bg_wheel_city:
        subpixel True
        truecenter
        zoom 0.6 xpos 2.0 ypos 0.4 # On the left
        ease 50.0 zoom 0.6 xpos -1.0 ypos 0.4 # On the Right
    with fade_long1s
        
    ne "Me encanta ver las luces de la ciudad durante la noche."

    n "A medida que os eleváis del suelo, observas la metrópolis catalana,"

    n "bañada de colores luminiscentes anaranjados y amarillentos arropada por la oscuridad y el techo estrellado."

    show bg night05_bg_wheel_city:
        subpixel True
        easein_quad 10.0 zoom 0.3 xpos 0.5 ypos 0.4 # Full View

    p "Hay que reconocer que las vistas desde aquí son espectaculares."

    window hide dissolve
    pause

    ##

    scene black
    show bg night05_bg_wheel_city:
        subpixel True
        truecenter 
        zoom 0.5 
        xpos 0.5 ypos 0.0
        easein_quad 200 ypos 0.9
    show night05_bg_wheel_seat_structure_comp:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        easein_quad 100.0 xpos 1.5 ypos 1.0
    show night05_bg_wheel_seat_structure_comp02:
        subpixel True
        truecenter
        yzoom -1.0 zoom 0.5
        xpos 1.5 ypos 0.0
        pause 100.0
        easein_quad 100.0 xpos 0.5 ypos 0.5
    show night05_bg_wheel_seat_cabin:
        truecenter
        zoom 0.5
        
    show n_s_b_sd_hair_back:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_body:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_face:
        n_s_b_sd_cup_close_position

    # Neus Expressions:

    show n_s_exp_blush 03:
        n_s_exp_sd_cup_close_position
    show n_s_exp_mouth happy_Talkingx08:
        n_s_exp_sd_cup_close_position
    show n_s_exp_eyes 04:
        n_s_exp_sd_cup_close_position
    show n_s_exp_iris front04:
        n_s_exp_sd_cup_close_position
    show n_s_exp_tears empty:
        n_s_exp_sd_cup_close_position
    show n_s_exp_eyebrows sadx02:
        n_s_exp_sd_cup_close_position
    show n_s_exp_glasses:
        n_s_exp_sd_cup_close_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_cup_close_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_leg_l down_closed:
        n_s_b_sd_cup_close_position

    show n_s_b_sd_arm_l empty:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_arm_r empty:
        n_s_b_sd_cup_close_position
    with fade

    ne "Es una lástima que el parque suela estar cerrado de noche."

    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 07
    show n_s_exp_iris front07
    with dissolve

    pt "No puedo quitarle la razón."

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Al menos es un buen modo de terminar nuestra última cita."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_blush 02
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    pt "Hasta demasiado cursi se podría decir..."

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    with dissolve

    ne "Euh..."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "Es verdad..."

    show n_s_exp_mouth sad_Silentx06
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    menu night05_NeusLastDate_Noria_CloseDate_Question:

        pt "Parece que no se ha tomado demasiado bien esa última frase..."

        "Terminar la cita en el lugar más alto de la ciudad durante la noche, es un buen punto y final.":
            call p_Help

            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_eyebrows sadx02
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            ne "..."

            show n_s_exp_mouth sad_Talkingx003
            show n_s_exp_eyebrows normal
            show n_s_exp_eyes 04
            show n_s_exp_iris left04
            with dissolve

            ne "Es cierto..."

            show n_s_exp_mouth sad_Talkingx05
            show n_s_exp_eyebrows sadx04
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

            ne "Aunque me gustaría más si fuera un punto y aparte..."

            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_eyebrows sadx05
            show n_s_exp_eyes 04
            show n_s_exp_iris left04
            with dissolve

            p "..."

            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_eyebrows suspiciousx01
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

        "<Decirle que aún tienes la esperanza de que te invite de nuevo a un café>" if night03_PedreraHome == True:
            call p_Help

            $pl.ch_pts("np",2)

            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_eyebrows normal
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            p "Me refería a la cita como tal en el parque..."

            show n_s_exp_mouth sad_Silentx02
            show n_s_exp_eyebrows surprisex01
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            p "Aún tengo la esperanza de que me invites a ese café con el sabor tan raro sin leche de vaca."

            show n_s_exp_mouth happy_Silentx04
            show n_s_exp_blush 03
            show n_s_exp_eyebrows normal
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            with dissolve

            ne "..."

            show n_s_exp_mouth happy_Talkingx04
            show n_s_exp_blush 04
            show n_s_exp_eyebrows sadx03
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "Tonto..."

            show n_s_exp_mouth happybiting_Silentx05
            show n_s_exp_eyebrows sadx03
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

        "<No decir nada>":
            call p_Help

            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_blush 03
            show n_s_exp_eyebrows sadx03
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

    ne "Hmm..."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    p "¿Qué pasa?"

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_blush 03
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Hay algo que le falta a esta cita para poder terminarla en condiciones,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    ne "¿no crees?"

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_blush 04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    menu night05_NeusLastDate_Noria_Joke_Question:

        pt "¿En condiciones?"

        "<Admitir que estabas esperando el mejor momento para besarla>":
            call p_Help

            $pl.ch_pts("np",1)

            show n_s_exp_mouth sad_Talkingx05
            show n_s_exp_blush 03
            show n_s_exp_eyebrows angryx02
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "¿Y tenía que ser justamente al final de la cita?"

            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_eyebrows angryx04
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            with dissolve

            jump night05_NeusLastDate_Noria_Kiss_Label

        "<Usar la tradición catalana a modo de broma para destensar la situación>":
            call p_Help

            $pl.ch_pts("np",2)

            show n_s_exp_mouth sad_Silentx03
            show n_s_exp_blush 03
            show n_s_exp_eyebrows surprisex01
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            p "Ya sé que existe la tradición milenaria del {a=https://es.wikipedia.org/wiki/Trovador}Trovador{/a} catalán de cantarle a su amante en el balcón,"

            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_eyebrows surprisex02
            show n_s_exp_eyes 00
            show n_s_exp_iris front00
            with dissolve

            p "pero tendría que bajarme primero de esta atracción"

            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_eyebrows suspiciousx01
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            p "haciendo el ridículo rodeado de mucha gente."

            show n_s_exp_mouth sadbiting_Silentx03
            show n_s_exp_eyebrows suspiciousx02
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            p "Y si me pongo a cantar es probable que mañana nos caiga el diluvio universal de nuevo..."

            play sound "audio/characters/neus/giggle03.ogg"

            show n_s_exp_mouth happy_Talkingx04
            show n_s_exp_eyebrows sadx02
            show n_s_exp_eyes 07
            show n_s_exp_iris front07
            with dissolve

            ne "Mira que eres tonto cuando quieres..."

            show n_s_exp_mouth happybiting_Silentx03
            show n_s_exp_eyebrows suspiciousx02
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            p "Y lo que te gusta."

            play sound "audio/characters/neus/giggle02.ogg"

            show n_s_exp_mouth happy_Silentx06
            show n_s_exp_blush 04
            show n_s_exp_eyebrows sadx03
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "..."

            show n_s_exp_mouth happy_Talkingx06
            show n_s_exp_blush 04
            show n_s_exp_eyebrows sadx02
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            with dissolve

            ne "Idiota..."

            show n_s_exp_mouth sadbiting_Silentx06
            show n_s_exp_blush 05
            show n_s_exp_eyebrows sadx05
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

            ne "..."

            show n_s_exp_mouth sadbiting_Silentx03
            show n_s_exp_eyebrows sadx01
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            p "Lo sé..."

            show n_s_exp_mouth sadbiting_Silentx02
            show n_s_exp_eyebrows normal
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            p "No te he besado en toda la noche,"

            show n_s_exp_mouth sadbiting_Silentx04
            show n_s_exp_eyebrows sadx03
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            p "¿verdad?"

            show n_s_exp_mouth sadbiting_Silentx05
            show n_s_exp_eyebrows sadx05
            show n_s_exp_eyes 04
            show n_s_exp_iris right04
            with dissolve

            ne "..."

            show n_s_exp_mouth sad_Talkingx03
            show n_s_exp_eyebrows sadx04
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "Y ¿por qué no?"

            show n_s_exp_mouth sadbiting_Silentx04
            show n_s_exp_eyebrows surprisex01
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            # p "Estaba esperando que me lo pidieras."

            jump night05_NeusLastDate_Noria_Kiss_Label

        "Pues la verdad es que echo de menos tus labios en contacto a los míos.":
            call p_Help

            $pl.ch_pts("np",2)

            show n_s_exp_mouth sadbiting_Silentx03
            show n_s_exp_blush 05
            show n_s_exp_eyebrows surprisex01
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            ne "..."

            show n_s_exp_mouth sad_Talkingx07
            show n_s_exp_blush 04
            show n_s_exp_eyebrows angryx03
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "¿Entonces por qué no me has besado aún?"

            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_eyebrows suspiciousx02
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            with dissolve

            if PlatinumHelp:

                n "¡Porque el maldito desarrollador del juego no me ha dado esa opción hasta ahora!"

                show n_s_exp_mouth sadbiting_Silentx03
                show n_s_exp_eyebrows surprisex02
                show n_s_exp_eyes 05
                show n_s_exp_iris right05
                with dissolve

                aj "¡Ejem!"

                extend " ¡Ejem...!"

                show n_s_exp_mouth sad_Silentx04
                show n_s_exp_eyebrows serious
                show n_s_exp_eyes 02
                show n_s_exp_iris front02
                with dissolve

            jump night05_NeusLastDate_Noria_Kiss_Label

        
label night05_NeusLastDate_Noria_Kiss_Label:

    p "Estaba esperando que me lo pidieras."

    show n_s_exp_mouth sad_Talkingx07
    show n_s_exp_eyebrows angryx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¡Como si no supieras a estas alturas lo que quiero!"

    show n_s_exp_mouth sad_Talkingx06
    show n_s_exp_eyebrows angryx03
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Si tienes que sentirte obligado,"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows angryx02
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    ne "no me lo des..."

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "¿Eso es que no lo quieres?"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows angryx03
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    ne "Tonto..."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    scene bg dark_a
    show n_closefromup_body sd:
        n_closefromup_05_position
    show n_closefromup_blush 03:
        n_closefromup_05_position
    show n_closefromup_eyes 01:
        n_closefromup_05_position
    show n_closefromup_iris front01:
        n_closefromup_05_position
    show n_closefromup_eyebrows sadx04:
        n_closefromup_05_position
    show n_closefromup_tears empty:
        n_closefromup_05_position
    show n_closefromup_mouth sadbiting_Silentx02:
        n_closefromup_05_position
    show n_closefromup_glasses:
        n_closefromup_05_position
    show n_closefromup_hair_front:
        n_closefromup_05_position
    with fade

    ne "..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sadbiting_Silentx03
    with dissolve

    menu night05_NeusLastDate_Noria_Kiss_First_Question:

        pt "¿Espero a que lo haga ella, o tomo la iniciativa?"

        "<Besarla>":
            call p_Help

            $pl.ch_pts("np",1)

            scene bg_dark_a
            show n_closefromup_comp sd_kisssurprise:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 10.0 zoom 0.75
            with dissolve

            n "Con decisión, acercas los labios a los suyos,"

            if music_play != "forever_dreaming":
                play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "forever_dreaming"

            # if music_play != "last_kiss_goodnight":
            #     play music "audio/music/kevingmacleod/last_kiss_goodnight.ogg" fadein 3.0 fadeout 3.0
            #     $ music_play = "last_kiss_goodnight"

            show n_closefromup_comp sd_receivekiss:
                subpixel True
                easein_quad 10.0 zoom 1.5 xpos 0.4 ypos 0.4 rotate -30
            with dissolve_1s

            n "mientras ella cierra sus ojos,"

        "Bésame.":
            call p_Help

            if ((pl.np > 130) or
                (night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_NotGF_Cond == False or
                night05_Park_MinigameShooter_Played == True or
                night05_Park_RollerCoaster_Used == True)):

                $pl.ch_pts("np",2)

                show n_closefromup_eyes 05
                show n_closefromup_blush 04
                show n_closefromup_iris front05
                show n_closefromup_eyebrows sadx02
                show n_closefromup_mouth happybiting_Silentx05
                with dissolve

                ne "..."

                scene bg_dark_a
                show n_closefromup_comp sd_kisssurprise:
                    subpixel True
                    truecenter
                    zoom 0.5
                    easein_quad 10.0 zoom 0.75
                with dissolve

                n "Con ternura,"

                if music_play != "forever_dreaming":
                    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "forever_dreaming"

                # if music_play != "last_kiss_goodnight":
                #     play music "audio/music/kevingmacleod/last_kiss_goodnight.ogg" fadein 3.0 fadeout 3.0
                #     $ music_play = "last_kiss_goodnight"

                show n_closefromup_comp sd_receivekiss:
                    subpixel True
                    easein_quad 10.0 zoom 1.5 xpos 0.4 ypos 0.4 rotate -30
                with dissolve_1s

                n "acerca sus labios a los tuyos,"

                jump night05_NeusLastDate_Noria_Kiss_After

            else:

                $ night05_NeusLastDate_Noria_Kiss_First_Try += 1

                if night05_NeusLastDate_Noria_Kiss_First_Try == 1:

                    if music_play != "torn_apart":
                        play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "torn_apart"

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_eyebrows sadx04
                    show n_closefromup_mouth sadbiting_Silentx05
                    with dissolve

                    ne "..."

                    show n_closefromup_eyes 04
                    show n_closefromup_iris right04
                    show n_closefromup_eyebrows sadx02
                    show n_closefromup_mouth sadbiting_Silentx10
                    with dissolve

                    p "¿Qué ocurre?"

                    show n_closefromup_eyes 02
                    show n_closefromup_iris left02
                    show n_closefromup_eyebrows sadx03
                    show n_closefromup_mouth sad_Talkingx04
                    with dissolve

                    ne "Estoy nerviosa..."

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_eyebrows sadx04
                    show n_closefromup_mouth sadbiting_Silentx09
                    with dissolve

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 2:

                    if music_play != "aura":
                        play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "aura"

                    if night05_NeusLastDate_After_HotelKrueger_Medic_NeusName_NotGF_Cond == True:

                        show n_closefromup_eyes 05
                        show n_closefromup_iris right05
                        show n_closefromup_tears 04_01
                        show n_closefromup_eyebrows sadx04
                        show n_closefromup_mouth sadbiting_Silentx09
                        with dissolve

                        ne "..."

                        show n_closefromup_eyes 02
                        show n_closefromup_iris right02
                        show n_closefromup_tears 02_01
                        show n_closefromup_eyebrows sadx05
                        show n_closefromup_mouth sad_Talkingx04
                        with dissolve

                        ne "¿Por qué le has dicho al paramédico que no era tu novia?"

                        show n_closefromup_eyes 02
                        show n_closefromup_iris front02
                        show n_closefromup_tears 02_01
                        show n_closefromup_eyebrows sadx02
                        show n_closefromup_mouth sad_Silentx05
                        with dissolve

                        p "Porque aún nos estamos conociendo."

                        show n_closefromup_eyes 05
                        show n_closefromup_iris right05
                        show n_closefromup_tears 04_01
                        show n_closefromup_eyebrows sadx05
                        show n_closefromup_mouth sadbiting_Silentx05
                        with dissolve

                        p "¿O no es así?"

                        show n_closefromup_eyes 05
                        show n_closefromup_iris down05
                        show n_closefromup_tears 04_01
                        show n_closefromup_eyebrows sadx06
                        show n_closefromup_mouth sad_Talkingx01
                        with dissolve

                        ne "Ya..."

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_tears 04_01
                    show n_closefromup_eyebrows sadx05
                    show n_closefromup_mouth sad_Silentx06
                    with dissolve

                    ne "..."

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 3:

                    if music_play != "colorless_aura":
                        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "colorless_aura"

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_tears 04_02
                    show n_closefromup_eyebrows sadx05
                    show n_closefromup_mouth sadbiting_Silentx04
                    with dissolve

                    ne "..."

                    if night05_Park_MinigameShooter_Played == False:

                        show n_closefromup_eyes 04
                        show n_closefromup_iris front04
                        show n_closefromup_tears 04_02
                        show n_closefromup_eyebrows sadx03
                        show n_closefromup_mouth sad_Talkingx02
                        with dissolve

                        ne "¿Por qué no has querido probar suerte conmigo en la zona de disparar?"

                        show n_closefromup_eyes 01
                        show n_closefromup_iris front01
                        show n_closefromup_tears 01_02
                        show n_closefromup_eyebrows sadx01
                        show n_closefromup_mouth sad_Silentx04
                        with dissolve

                        p "Ya sabes que ese gordo seboso me cae como el culo."

                        show n_closefromup_eyes 02
                        show n_closefromup_iris right02
                        show n_closefromup_tears 02_02
                        show n_closefromup_eyebrows sadx03
                        show n_closefromup_mouth sadbiting_Silentx09
                        with dissolve

                        ne "..."

                        show n_closefromup_eyes 04
                        show n_closefromup_iris right04
                        show n_closefromup_tears 04_02
                        show n_closefromup_eyebrows sadx04
                        show n_closefromup_mouth sad_Talkingx01
                        with dissolve

                        ne "Ya..."

                        show n_closefromup_eyes 01
                        show n_closefromup_iris front01
                        show n_closefromup_tears 01_02
                        show n_closefromup_eyebrows sadx03
                        show n_closefromup_mouth sadbiting_Silentx04
                        with dissolve

                        p "¿Por qué me sacas ahora el tema?"

                        show n_closefromup_eyes 04
                        show n_closefromup_iris right04
                        show n_closefromup_tears 04_02
                        show n_closefromup_eyebrows sadx05
                        show n_closefromup_mouth sad_Talkingx001
                        with dissolve

                        ne "Lo siento..."

                        show n_closefromup_eyes 05
                        show n_closefromup_iris right05
                        show n_closefromup_tears 04_02
                        show n_closefromup_eyebrows sadx06
                        show n_closefromup_mouth sad_Silentx06
                        with dissolve

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 4:

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_tears 04_03
                    show n_closefromup_eyebrows sadx03
                    show n_closefromup_mouth sad_Silentx06
                    with dissolve

                    ne "..."

                    if night05_Park_RollerCoaster_Used == False:

                        show n_closefromup_eyes 02
                        show n_closefromup_iris front02
                        show n_closefromup_tears 02_03
                        show n_closefromup_eyebrows sadx03
                        show n_closefromup_mouth sad_Talkingx03
                        with dissolve

                        ne "¿Por qué no te has querido subir a la montaña rusa conmigo...?"

                        show n_closefromup_eyes 01
                        show n_closefromup_iris front01
                        show n_closefromup_tears 01_03
                        show n_closefromup_eyebrows surprisex01
                        show n_closefromup_mouth sadbiting_Silentx04
                        with dissolve

                        p "¿Y qué tiene esto que ver ahora?"

                        show n_closefromup_eyes 04
                        show n_closefromup_iris right04
                        show n_closefromup_tears 04_03
                        show n_closefromup_eyebrows sadx05
                        show n_closefromup_mouth sad_Talkingx01
                        with dissolve

                        ne "Perdona..."

                        show n_closefromup_eyes 04
                        show n_closefromup_iris right04
                        show n_closefromup_tears 04_03
                        show n_closefromup_eyebrows sadx06
                        show n_closefromup_mouth sad_Silentx06
                        with dissolve

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 5:

                    show n_closefromup_eyes 05
                    show n_closefromup_iris right05
                    show n_closefromup_tears 04_04
                    show n_closefromup_eyebrows sadx04
                    show n_closefromup_mouth sadbiting_Silentx09
                    with dissolve

                    ne "..."

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 6:

                    show n_closefromup_eyes 05
                    show n_closefromup_iris left05
                    show n_closefromup_tears 04_04
                    show n_closefromup_eyebrows sadx05
                    show n_closefromup_mouth sadbiting_Silentx10
                    with dissolve

                    ne "..."

                elif night05_NeusLastDate_Noria_Kiss_First_Try == 7:

                    show n_closefromup_eyes 06
                    show n_closefromup_iris front06
                    show n_closefromup_tears 06_05
                    show n_closefromup_eyebrows sadx06
                    show n_closefromup_mouth sadbiting_Silentx11
                    with dissolve

                    ne "..."

                elif night05_NeusLastDate_Noria_Kiss_First_Try >= 8:

                    show n_closefromup_eyes 07
                    show n_closefromup_iris front06
                    show n_closefromup_tears 07_05
                    show n_closefromup_eyebrows sadx07
                    show n_closefromup_mouth sadbiting_Silentx12
                    with dissolve

                    ne "..."

                jump night05_NeusLastDate_Noria_Kiss_First_Question

label night05_NeusLastDate_Noria_Kiss_After:

    scene bg dark_a
    show kiss_ n_n_01:
        truecenter
    with fade

    show kiss_ n_n_02
    with dissolve_1s

    show kiss_ n_n_05
    with dissolve_1s

    show kiss_ n_n_04
    with dissolve_1s

    n "y os fundís en un dulce y suave beso."

    if night05_NeusLastDate_Noria_Kiss_First_Try >= 3:

        extend "\nA pesar de tener sus mejillas aún empapadas por sus lágrimas..."


    show kiss_ n_n_01:
        truecenter
    show light_01_red:
        subpixel True
        light01_leftside_position
        pause 1.2
        easein_quad 1.0 alpha 0.0
        pause 3.0
        easein_quad 1.0 alpha 1.0
        repeat
    show light_01_green:
        subpixel True
        alpha 0.0
        pause 1.2
        light01_leftside_position
        pause 2.2
        easein_quad 1.0 alpha 0.0
        repeat
    show light_01_blue:
        subpixel True
        alpha 0.0
        pause 1.8
        light01_leftside_position
        pause 1.6
        easein_quad 1.0 alpha 0.0
        repeat
    show white:
        subpixel True
        additive 1.0
        easein_bounce 1.0 alpha 0.0
    with dissolve_05s

    n "Un potente foco de luz os alumbra y sorprende."

    scene night05_bg_wheel_city_fireworks:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 1.5 # First firework
        ease 25.0 zoom 0.4 xpos 0.5 ypos 0.5 # Final vision
    with fade

    n "Vislumbráis en el cielo unos enormes fuegos de artificio que se están lanzando por la ciudad."

    p "¿Es que jugaba el {a=https://es.wikipedia.org/wiki/Fútbol_Club_Barcelona}Barça hoy{/a}?"

    ne "No lo creo,"

    ne "me parece que es más bien porque mañana es la {a=https://es.wikipedia.org/wiki/Verbena_(fiesta)}verbena{/a}."

    if protname.lower() in joan_names:

        ne "Por cierto,"

        extend " felices vísperas."

        p "¿Qué?"

        ne "Mañana es tu santo,"

        extend " ¿verdad?"

        p "..."

        ne "Tendré que darte un regalo especial entonces esta medianoche,"

        ne "¿no crees?"

    window hide dissolve
    pause

    scene bg dark_a

    if night05_NeusLastDate_Noria_Kiss_First_Try >= 1:

        show kiss_ f_n_04:
            truecenter
        show light_01_red:
            subpixel True
            light01_leftside_position
            pause 1.2
            easein_quad 1.0 alpha 0.0
            pause 3.0
            easein_quad 1.0 alpha 1.0
            repeat
        show light_01_green:
            subpixel True
            alpha 0.0
            pause 1.2
            light01_leftside_position
            pause 2.2
            easein_quad 1.0 alpha 0.0
            repeat
        show light_01_blue:
            subpixel True
            alpha 0.0
            pause 1.8
            light01_leftside_position
            pause 1.6
            easein_quad 1.0 alpha 0.0
            repeat
        show white:
            subpixel True
            additive 1.0
            easein_bounce 1.0 alpha 0.0

        show kiss_ f_n_11:
            truecenter
        with fade

        show kiss_ f_n_05
        with dissolve_1s

        show kiss_ f_n_07
        with dissolve_1s

        n "Con cierta duda, regresa a tus labios."

    else:

        show kiss_ f_n_12:
            truecenter
        show light_01_red:
            subpixel True
            light01_leftside_position
            pause 1.2
            easein_quad 1.0 alpha 0.0
            pause 3.0
            easein_quad 1.0 alpha 1.0
            repeat
        show light_01_green:
            subpixel True
            alpha 0.0
            pause 1.2
            light01_leftside_position
            pause 2.2
            easein_quad 1.0 alpha 0.0
            repeat
        show light_01_blue:
            subpixel True
            alpha 0.0
            pause 1.8
            light01_leftside_position
            pause 1.6
            easein_quad 1.0 alpha 0.0
            repeat
        show white:
            subpixel True
            additive 1.0
            easein_bounce 1.0 alpha 0.0
        with hpunch

        show kiss_ f_n_11:
            truecenter
        with dissolve_1s

        show kiss_ f_n_08
        with dissolve_1s

        show kiss_ f_n_10
        with dissolve_1s

        n "Sin pensarlo dos veces regresa a ti con mayor pasión."

    show kiss_ f_n_09:
        truecenter
    with dissolve_1s

    show kiss_ f_n_07
    with dissolve_1s

    show kiss_ f_n_06
    with dissolve_1s

    if night04_Neus_KissFrenchmade == True:

        n "Mezclando vuestras lenguas como la noche anterior,"

    show kiss_ f_n_08
    with dissolve_1s

    show kiss_ f_n_05
    with dissolve_1s

    show kiss_ f_n_04
    with dissolve_1s

    n "pero esta vez,"

    show kiss_ f_n_10
    with dissolve_1s

    show kiss_ f_n_11
    with dissolve_1s

    show kiss_ f_n_12
    with dissolve_1s

    n "con la luz coloreada de las explosiones pirotécnicas."

label night05_NeusLastDate_Noria_Message:

    if night05_NeusLastDate_Noria_Not == True:
        hide night05_bg_tibidabo_park_00
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_01
        show neus_exp_eyebrows surprisex01
        with fade

    else:

        show kiss_ f_n_01:
            truecenter
        with hpunch
        scene bg dark_a
        show kiss_ f_n_01:
            truecenter
        with Dissolve (1.0)

    play sound "audio/sfx/ring_phone_message01.ogg"

    ono "*BEEP*"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears 02_01
        show neus_exp_eyebrows surprisex02
        with dissolve

    else:

        scene bg dark_a
        show n_closefromup_body sd:
            n_closefromup_1_position
        show n_closefromup_blush 04:
            n_closefromup_1_position
        show n_closefromup_eyes 00:
            n_closefromup_1_position
        show n_closefromup_iris front00:
            n_closefromup_1_position
        show n_closefromup_eyebrows normal:
            n_closefromup_1_position
        show n_closefromup_tears empty:
            n_closefromup_1_position
        show n_closefromup_mouth sad_Silentx03:
            n_closefromup_1_position
        show n_closefromup_glasses:
            n_closefromup_1_position
        show n_closefromup_hair_front:
            n_closefromup_1_position
        with fade

    p "Hmm..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears empty
        show neus_exp_eyebrows suspiciousx01
    else:
        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows sadx02
        show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "¿Qué ocurre?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyes 02
        show neus_exp_iris down02
        show neus_exp_eyebrows serious
    else:
        show n_closefromup_eyes 01
        show n_closefromup_iris down01
        show n_closefromup_eyebrows serious
        show n_closefromup_mouth sad_Silentx01
    with dissolve

    p "Es mi móvil."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows sadx01
    else:
        show n_closefromup_eyes 01
        show n_closefromup_iris front01
        show n_closefromup_eyebrows surprisex01
        show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "¿Un mensaje?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx02
    else:
        show n_closefromup_eyes 04
        show n_closefromup_iris front04
        show n_closefromup_eyebrows normal
        show n_closefromup_mouth happy_Silentx02
    with dissolve

    pt "Generalmente no me envía mensajes ni mi madre..."

    stop music fadeout 3.0
    $ music_play = ""

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_eyebrows sadx04
        with dissolve
    else:
            ##
        scene black
        show bg night05_bg_wheel_city:
            subpixel True
            truecenter 
            zoom 0.5 
            xpos 0.5 ypos 0.9
            easein_quad 200 ypos 0.0
        show night05_bg_wheel_seat_structure_comp:
            subpixel True
            truecenter
            zoom 0.5 xzoom -1.0
            xpos -1.0 ypos 1.0
            pause 100.0
            easein_quad 100.0 xpos 0.5 ypos 0.5
        show night05_bg_wheel_seat_structure_comp02:
            subpixel True
            truecenter
            zoom 0.5 yzoom -1.0 xzoom -1.0 
            xpos 0.5 ypos 0.5
            easein_quad 100.0 xpos -1.0 ypos 0.0
        show night05_bg_wheel_seat_cabin:
            truecenter
            zoom 0.5
              
        show n_s_b_sd_hair_back:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_body:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_face:
            n_s_b_sd_cup_close_position

        # Neus Expressions:

        show n_s_exp_blush 03:
            n_s_exp_sd_cup_close_position
        show n_s_exp_mouth sadbiting_Silentx06:
            n_s_exp_sd_cup_close_position
        show n_s_exp_eyes 00:
            n_s_exp_sd_cup_close_position
        show n_s_exp_iris right00:
            n_s_exp_sd_cup_close_position
        show n_s_exp_tears empty:
            n_s_exp_sd_cup_close_position
        show n_s_exp_eyebrows surprisex01:
            n_s_exp_sd_cup_close_position
        show n_s_exp_glasses:
            n_s_exp_sd_cup_close_position

        show n_s_b_sd_arm_l_b bank_rest:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_arm_r_b bank_rest:
            n_s_b_sd_cup_close_position

        show n_s_b_sd_hair_front:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_leg_r down_closed:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_leg_l down_closed:
            n_s_b_sd_cup_close_position

        show n_s_b_sd_arm_l empty:
            n_s_b_sd_cup_close_position
        show n_s_b_sd_arm_r empty:
            n_s_b_sd_cup_close_position
        with fade

    pt "¿Quién diablos será...?"

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    show morning04_bg_livingroom_mc_resting_phone pedreradidac:
        zoom 0.5 xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with dissolve

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
    with dissolve

    p "¡¿Qué demonios?!"

    #########################################################

    if config.version < "00.12.05": # Receiving a message in Noria.
        
        call endupdatescript
    
    #######################################################

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx04
    with dissolve

    ne "¿Qué pasa?"

    $ d_bodyType = "_slim"

    show black02
    show morning04_bg_livingroom_mc_resting_phone_pedreradidacHD:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.35 ypos -0.5
        easein_quad 20.0 zoom 1.0 xpos 0.35 ypos 1.1
    with fade

    n "Al abrir el móvil y mirar el {i}WhatsApp{/i},"

    n "observas un mensaje de Dídac adjuntando una foto,"

    n "en la que aparece una chica, vista de lejos, con el pelo del mismo color que Dídac,"

    n "pero muchísimo más largo, con un cuerpo nada musculado y completamente desnudo,"

    n "en una habitación oscura que te resulta familiar;"

    n "y con un mensaje debajo en el que pone:"

    show morning04_bg_livingroom_mc_resting_phone_pedreradidacHD:
        subpixel True
        ease_quad 10.0 zoom 0.35 xpos 0.5 ypos 0.5
    with dissolve

    n "{i}Os estamos esperando.{/i}"

    n "{i}P.D.{/i}"

    extend " {i}Espero que no te disguste el nuevo look que le he dado.{/i}"

    window hide dissolve
    pause

    hide black02
    hide morning04_bg_livingroom_mc_resting_phone_pedreradidacHD

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx08
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx06
    with dissolve

    p "Pero qué..."

    pt "¿Cómo le ha crecido el pelo tan rápidamente?"

    pt "¡¿Y ese cuerpo tan distinto?!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx05
    with dissolve

    ne "¿Qué ocurre [protname]?"

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone

    if night05_NeusLastDate_Noria_Not == True:

        show neus_arm_r sd:
            neus_body_atright_close_position
        show neus_body sd_default:
            neus_body_atright_close_position
        show neus_head:
            neus_body_atright_close_position
        show neus_arm_l sd:
            neus_body_atright_close_position
        
        show neus_exp_blush 02:
            neus_exp_atright_close_position
        show neus_exp_mouth sad_Silentx04:
            neus_exp_atright_close_position
        show neus_exp_eyes 01:
            neus_exp_atright_close_position
        show neus_exp_iris front01:
            neus_exp_atright_close_position
        show neus_exp_tears empty:
            neus_exp_atright_close_position
        show neus_exp_eyebrows sadx01:
            neus_exp_atright_close_position
        show neus_exp_glasses:
            neus_exp_atright_close_position
        show neus_exp_hairfront:
            neus_exp_atright_close_position
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_eyebrows serious
        show n_s_exp_eyes 04
        show n_s_exp_iris down04
    with dissolve

    n "Le das el móvil para que lo vea con sus propios ojos."

    if music_play != "aura":
        play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "aura"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 01
        show neus_exp_iris down01
        show neus_exp_tears 01_01
        show neus_exp_eyebrows serious
    else:
        show n_s_exp_mouth sad_Silentx03
        show n_s_exp_blush 01
        show n_s_exp_eyebrows serious
        show n_s_exp_eyes 01
        show n_s_exp_iris down01
    with dissolve

    n "Su cuerpo empieza temblar."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_tears 04_02
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sadbiting_Silentx05
        show n_s_exp_tears 05_01
        show n_s_exp_blush 00
        show n_s_exp_eyebrows sadx06
        show n_s_exp_eyes 05
        show n_s_exp_iris down05
    with dissolve

    ne "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_tears 06_03
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sadbiting_Silentx07
        show n_s_exp_blush 00
        show n_s_exp_tears 06_02
        show n_s_exp_eyes 06
        show n_s_exp_iris front06
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "Neus..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_tears 04_04
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx02
        show n_s_exp_tears 05_03
        show n_s_exp_eyebrows sadx06
        show n_s_exp_eyes 05
        show n_s_exp_iris down05
    with dissolve

    ne "Me ha encontrado."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_tears 06_05
        show neus_exp_eyebrows angryx02
    else:
        show n_s_exp_mouth sadbiting_Silentx07
        show n_s_exp_tears 07_03
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx07
    with dissolve

    p "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_tears 07_05
        show neus_exp_eyebrows angryx03
    else:
        show n_s_exp_mouth sadbiting_Silentx08
        show n_s_exp_tears 06_04
        show n_s_exp_eyes 06
        show n_s_exp_iris front06
        show n_s_exp_eyebrows sadx05
    with dissolve

    n "Era evidente por la distancia en la que estaba hecha la foto,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sadbiting_Silentx09
        show n_s_exp_tears 04_04
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        show n_s_exp_eyebrows sadx06
    with dissolve

    n "que Dídac no se había podido tomar un {i}selfie{/i}."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_tears 06_05
        show neus_exp_eyebrows sadx05
        with dissolve
    else:
        show n_s_exp_mouth sad_Silentx07
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx07
    with dissolve

    n "Había alguien más con él."

    n "Y esa habitación oscura;"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx08
        show n_s_exp_tears 08_05
        show n_s_exp_eyes 08
        show n_s_exp_iris front08
        show n_s_exp_eyebrows sadx06
    with dissolve

    n "sin ninguna duda, era la Pedrera;"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx06
        with dissolve
    else:
        show n_s_exp_mouth sad_Silentx09
        show n_s_exp_tears 07_05
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx07
    with dissolve

    n "el refugio de Neus."

    if night05_Interrogation_WhatIsYourFather_Cond == True:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_tears 01_05
            show neus_exp_eyebrows sadx01
        else:
            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_tears 02_05
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            show n_s_exp_eyebrows sadx04
        with dissolve

        p "Te refieres a tu padre,"

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_tears 03_05
            show neus_exp_eyebrows sadx04
        else:
            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_tears 04_05
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            show n_s_exp_eyebrows sadx05
        with dissolve

        p "¿verdad?"

    else:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_tears 01_05
            show neus_exp_eyebrows sadx02
        else:
            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_tears 02_05
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            show n_s_exp_eyebrows sadx04
        with dissolve

        p "¿Qué está pasando?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 01
        show neus_exp_iris down01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris down01
        show n_s_exp_eyebrows sadx06
    with dissolve

    n "Sus ojos están abandonados en un punto incierto, como si estuviera perdida en sus pensamientos,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx07
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx07
    with dissolve

    n "mientras sus lágrimas brotan en abundancia y su temblor es más que evidente."

    if night05_Interrogation_WhatIsYourFather_Cond == True:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 02
            show neus_exp_iris right02
            show neus_exp_tears 02_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sad_Talkingx03
            show n_s_exp_tears 02_05
            show n_s_exp_eyes 02
            show n_s_exp_iris right02
            show n_s_exp_eyebrows sadx05
        with dissolve

        ne "Sí..."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 00
            show neus_exp_iris front00
            show neus_exp_tears 00_05
            show neus_exp_eyebrows sadx02
        else:
            show n_s_exp_mouth sad_Silentx03
            show n_s_exp_tears 00_05
            show n_s_exp_eyes 00
            show n_s_exp_iris front00
            show n_s_exp_eyebrows sadx02
        with dissolve

        p "Entonces Dídac está en peligro."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 04
            show neus_exp_iris right04
            show neus_exp_tears 04_05
            show neus_exp_eyebrows sadx07
        else:
            show n_s_exp_mouth sad_Talkingx02
            show n_s_exp_tears 05_05
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            show n_s_exp_eyebrows sadx07
        with dissolve

        ne "Sí..."

    else:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris right02
            show neus_exp_tears 02_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_tears 02_05
            show n_s_exp_eyes 02
            show n_s_exp_iris right02
            show n_s_exp_eyebrows sadx05
        with dissolve

        p "Dídac está en peligro..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx05
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "Tenemos que ir a ayudarle."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx01
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx07
    else:
        show n_s_exp_mouth sad_Talkingx01
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx07
    with dissolve

    ne "Es lo que él quiere..."

    if night05_Interrogation_WhatIsYourFather_Cond == True:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_tears 04_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sad_Silentx03
            show n_s_exp_tears 05_05
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            show n_s_exp_eyebrows sadx05
        with dissolve

        p "Sí..."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 08
            show neus_exp_iris front08
            show neus_exp_tears 08_05
            show neus_exp_eyebrows sadx04
        else:
            show n_s_exp_mouth sad_Silentx05
            show n_s_exp_tears 08_05
            show n_s_exp_eyes 08
            show n_s_exp_iris front08
            show n_s_exp_eyebrows sadx04
        with dissolve

        p "no hay que ser un genio para darse cuenta que es una trampa."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris right03
            show neus_exp_tears 03_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_tears 04_05
            show n_s_exp_eyes 04
            show n_s_exp_iris right04
            show n_s_exp_eyebrows sadx05
        with dissolve

        ne "..."

    else:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_tears 03_05
            show neus_exp_eyebrows sadx04
        else:
            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_tears 04_05
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            show n_s_exp_eyebrows sadx04
        with dissolve

        p "¿Él?"

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 02
            show neus_exp_iris right02
            show neus_exp_tears 02_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sadbiting_Silentx05
            show n_s_exp_tears 02_05
            show n_s_exp_eyes 02
            show n_s_exp_iris right02
            show n_s_exp_eyebrows sadx05
        with dissolve

        p "¡¿De quién estás hablando?!"

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 04
            show neus_exp_iris right04
            show neus_exp_tears 04_05
            show neus_exp_eyebrows sadx06
        else:
            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_tears 05_05
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            show n_s_exp_eyebrows sadx06
        with dissolve

        ne "..."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 08
            show neus_exp_iris front08
            show neus_exp_tears 08_05
            show neus_exp_eyebrows sadx04
        else:
            show n_s_exp_mouth sad_Talkingx02
            show n_s_exp_tears 08_05
            show n_s_exp_eyes 08
            show n_s_exp_iris front08
            show n_s_exp_eyebrows sadx04
        with dissolve

        ne "De mi padre."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyes 06
            show neus_exp_iris front06
            show neus_exp_tears 06_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sadbiting_Silentx05
            show n_s_exp_tears 06_05
            show n_s_exp_eyes 06
            show n_s_exp_iris front06
            show n_s_exp_eyebrows sadx05
        with dissolve

        p "..."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_tears 03_05
            show neus_exp_eyebrows sadx04
        else:
            show n_s_exp_mouth sad_Silentx04
            show n_s_exp_tears 04_05
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            show n_s_exp_eyebrows sadx04
        with dissolve

        p "¿Qué...?"

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 01
            show neus_exp_iris right01
            show neus_exp_tears 01_05
            show neus_exp_eyebrows sadx05
        else:
            show n_s_exp_mouth sad_Talkingx06
            show n_s_exp_tears 01_05
            show n_s_exp_eyes 01
            show n_s_exp_iris right01
            show n_s_exp_eyebrows sadx05
        with dissolve

        ne "Te quería hablar de ello mientras estabas comiendo..."

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyes 03
            show neus_exp_iris right03
            show neus_exp_tears 03_05
            show neus_exp_eyebrows sadx06
        else:
            show n_s_exp_mouth sad_Talkingx04
            show n_s_exp_tears 04_05
            show n_s_exp_eyes 04
            show n_s_exp_iris right04
            show n_s_exp_eyebrows sadx06
        with dissolve

        ne "pero..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Silentx03
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        show n_s_exp_eyebrows sadx02
    with dissolve

    p "Neus,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_eyebrows sadx03
    with dissolve

    p "por muy capullo que sea,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Silentx05
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "por terrible que fuera lo que te iba a hacer en el baño..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sadbiting_Silentx04
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        show n_s_exp_eyebrows sadx02
    with dissolve

    p "no se merece esto."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sadbiting_Silentx05
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx03
    with dissolve

    p "Es mi amigo."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_tears 07_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sadbiting_Silentx06
        show n_s_exp_tears 07_05
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx06
    with dissolve

    p "Tengo que ayudarlo."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx03
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx05
    with dissolve

    ne "Ya está muerto."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sadbiting_Silentx04
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "¿Qué?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "¡En la foto no parecía que estuviera muerto!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Talkingx002
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        show n_s_exp_eyebrows sadx06
    with dissolve

    ne "No,"

    extend " aún no lo está..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx03
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "pero técnicamente ya está muerto..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx06
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "Si vamos allí no conseguiremos nada,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx01
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx01
    with dissolve

    ne "y él acabará muerto de todos modos."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "[protname]..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx08
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "No conoces a mi padre,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx07
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "es normal que no lo entiendas."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx09
        show neus_exp_eyes 00
        show neus_exp_iris right00
        show neus_exp_tears 00_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx09
        show n_s_exp_tears 00_05
        show n_s_exp_eyes 00
        show n_s_exp_iris right00
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "Y sé que soy la menos indicada para decirte esto,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Talkingx06
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx04
    with dissolve

    ne "pero ya no podemos hacer nada por él..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx07
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "Entiéndelo,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "si vamos allí..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx06
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "Tú también acabarás muerto."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        show n_s_exp_eyebrows sadx05
    with dissolve

    ne "Y yo..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_tears 07_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sadbiting_Silentx05
        show n_s_exp_tears 07_05
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx06
    with dissolve

    p "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx01
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        show n_s_exp_eyebrows sadx01
    with dissolve

    p "¿Entonces qué diablos propones?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "¿Que escapemos juntos abandonando a Dídac a su suerte?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sadbiting_Silentx03
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "¡¿Para qué?!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "¡¿Para escondernos en algún rincón del mundo hasta que nos vuelva a encontrar de nuevo?!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows angryx01
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_tears 08_05
        show n_s_exp_eyes 08
        show n_s_exp_iris front08
        show n_s_exp_eyebrows sadx07
    with dissolve

    ne "[protname]..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx07
        show n_s_exp_tears 02_05
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "Contigo a mi lado todo será distinto..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx03
    with dissolve

    ne "Créeme..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx08
        show n_s_exp_tears 01_05
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "Ya no podrá encontrarnos tan fácilmente."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "¿Me estás diciendo en serio,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sadbiting_Silentx06
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "que lo abandone en manos de un psicópata malnacido?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Silentx07
        show n_s_exp_tears 08_05
        show n_s_exp_eyes 08
        show n_s_exp_iris front08
        show n_s_exp_eyebrows sadx06
    with dissolve

    ne "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx02
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx05
    with dissolve

    ne "Sí..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx04
    with dissolve

    ne "Es demasiado tarde para él..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_tears 07_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sadbiting_Silentx06
        show n_s_exp_tears 07_05
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx06
    with dissolve

    call screen night05_NeusLastDate_Noria_SaveDidac_Question()

screen night05_NeusLastDate_Noria_SaveDidac_Question():

    on "show":
        action MouseMove(x=400, y=400, duration= 0.5)

    timer 2.0 repeat True action MouseMove(x=400, y=400, duration= 1.0)

    add "gui/button/choice_idle_background.png" xalign .5 yalign .65

    add "gui/button/choice_idle_background.png" xalign .5 yalign .35

    textbutton (_("Quizás tengas razón.")):
        xalign .5 
        yalign .35 
        action Jump("night05_NeusLastDate_Noria_SaveDidac_No")

    textbutton (_("No puedo, Neus.")):
        xalign .5 
        yalign .65
        action Jump("night05_NeusLastDate_Noria_SaveDidac_After")


label night05_NeusLastDate_Noria_SaveDidac_After:

    if night05_NeusLastDate_ElysiumGoing:

        if night05_NeusLastDate_Noria_Not == True:
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyes 04
            show neus_exp_iris down04
            show neus_exp_eyebrows sadx04
            with dissolve
        else:
                ##
            scene black
            show bg night05_bg_wheel_city:
                subpixel True
                truecenter 
                zoom 0.5 
                xpos 0.5 ypos 0.9
                easein_quad 200 ypos 0.0
            show night05_bg_wheel_seat_structure_comp:
                subpixel True
                truecenter
                zoom 0.5 xzoom -1.0
                xpos -1.0 ypos 1.0
                pause 100.0
                easein_quad 100.0 xpos 0.5 ypos 0.5
            show night05_bg_wheel_seat_structure_comp02:
                subpixel True
                truecenter
                zoom 0.5 yzoom -1.0 xzoom -1.0 
                xpos 0.5 ypos 0.5
                easein_quad 100.0 xpos -1.0 ypos 0.0
            show night05_bg_wheel_seat_cabin:
                truecenter
                zoom 0.5
                  
            show n_s_b_sd_hair_back:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_body:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_face:
                n_s_b_sd_cup_close_position

            # Neus Expressions:

            show n_s_exp_blush 03:
                n_s_exp_sd_cup_close_position
            show n_s_exp_mouth sadbiting_Silentx06:
                n_s_exp_sd_cup_close_position
            show n_s_exp_eyes 00:
                n_s_exp_sd_cup_close_position
            show n_s_exp_iris right00:
                n_s_exp_sd_cup_close_position
            show n_s_exp_tears empty:
                n_s_exp_sd_cup_close_position
            show n_s_exp_eyebrows surprisex01:
                n_s_exp_sd_cup_close_position
            show n_s_exp_glasses:
                n_s_exp_sd_cup_close_position

            show n_s_b_sd_arm_l_b bank_rest:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_arm_r_b bank_rest:
                n_s_b_sd_cup_close_position

            show n_s_b_sd_hair_front:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_leg_r down_closed:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_leg_l down_closed:
                n_s_b_sd_cup_close_position

            show n_s_b_sd_arm_l empty:
                n_s_b_sd_cup_close_position
            show n_s_b_sd_arm_r empty:
                n_s_b_sd_cup_close_position

            if night05_NeusLastDate_Noria_Not == True:
                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_tears 03_05
                show neus_exp_eyebrows sadx02
            else:
                show n_s_exp_mouth sadbiting_Silentx03
                show n_s_exp_tears 04_05
                show n_s_exp_eyes 04
                show n_s_exp_iris front04
                show n_s_exp_eyebrows sadx02
            with dissolve

    ne "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sadbiting_Silentx03
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx02
    with dissolve

    p "Sé que es un gilipollas y un capullo en potencia."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sadbiting_Silentx04
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx04
    with dissolve

    p "Pero es Dídac."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sadbiting_Silentx03
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        show n_s_exp_eyebrows sadx03
    with dissolve

    p "Tenga tetas o no,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_tears 08_05
        show n_s_exp_eyes 08
        show n_s_exp_iris front08
        show n_s_exp_eyebrows sadx05
    with dissolve

    p "sigue siendo el capullo con el me he criado desde que tengo uso de razón."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_tears 06_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Silentx07
        show n_s_exp_tears 06_05
        show n_s_exp_eyes 06
        show n_s_exp_iris front06
        show n_s_exp_eyebrows sadx06
    with dissolve

    p "Es como un hermano para mí."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx09
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_tears 07_05
        show neus_exp_eyebrows sadx07
    else:
        show n_s_exp_mouth sad_Silentx09
        show n_s_exp_tears 07_05
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        show n_s_exp_eyebrows sadx07
    with dissolve

    p "No puedo..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx08
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Silentx08
        show n_s_exp_tears 08_05
        show n_s_exp_eyes 08
        show n_s_exp_iris front08
        show n_s_exp_eyebrows sadx02
    with dissolve

    ne "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Talkingx01
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        show n_s_exp_eyebrows sadx06
    with dissolve

    ne "Lo entiendo..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Silentx07
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        show n_s_exp_eyebrows sadx05
    with dissolve

    if night05_NeusLastDate_Noria_Not == False:

        n "Su voz es entrecortada y apenas es capaz de mantener la respiración."

        show bg night05_bg_wheel_city:
            truecenter 
            zoom 0.5 
            xpos 0.5 ypos 0.0
        show night05_bg_wheel_seat_structure_comp:
            truecenter
            xpos 0.5 ypos 0.5
        show night05_bg_wheel_seat_structure_comp02:
            truecenter
            yzoom -1.0 zoom 0.5
            xpos -1.0 ypos 0.0
        show n_s_exp_mouth sad_Silentx05
        show n_s_exp_tears 04_05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_eyebrows sadx05
        with dissolve

        n "Oís cómo la atracción se detiene llegando al suelo,"

        show n_s_exp_mouth sadbiting_Silentx06
        show n_s_exp_tears 05_05
        show n_s_exp_eyes 05
        show n_s_exp_iris left05
        show n_s_exp_eyebrows sadx06
        with dissolve

        n "mientras un encargado os abre la puerta para salir."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows sadx03
        with dissolve
    else:
        scene bg night05_bg_tibidabo_park_00:
            truecenter
            zoom 0.6 xpos 0.6 ypos 0.4
        show neus_arm_r sd:
            neus_body_atright_close_position
        show neus_body sd_default:
            neus_body_atright_close_position
        show neus_head:
            neus_body_atright_close_position
        show neus_arm_l sd:
            neus_body_atright_close_position
        
        show neus_exp_blush 00:
            neus_exp_atright_close_position
        show neus_exp_mouth sad_Talkingx06:
            neus_exp_atright_close_position
        show neus_exp_eyes 01:
            neus_exp_atright_close_position
        show neus_exp_iris right01:
            neus_exp_atright_close_position
        show neus_exp_tears 01_05:
            neus_exp_atright_close_position
        show neus_exp_eyebrows sadx03:
            neus_exp_atright_close_position
        show neus_exp_glasses:
            neus_exp_atright_close_position
        show neus_exp_hairfront:
            neus_exp_atright_close_position
        with fade

    ne "Hay..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_tears 02_05
    show neus_exp_eyebrows sadx04
    with dissolve

    extend " muchas cosas que aún no te he contado..."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Pensaba..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_tears 03_05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Pensaba que tendría tiempo..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_tears 02_05
    show neus_exp_eyebrows sadx03
    with dissolve

    p "Neus..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_tears 01_05
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Dídac corre peligro."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx04
    with dissolve

    p "Tenemos que irnos ya."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Yo..."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_tears 07_05
    show neus_exp_eyebrows sadx07
    with dissolve

    p "Lo mejor será coger un taxi."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_tears 06_05
    show neus_exp_eyebrows sadx05
    with dissolve

label night05_NeusLastDate_Noria_After:

    play sound "audio/sfx/grabarm01.ogg"

    scene bg dark_a_blurry_01
    show night04_pedrera_Ngrabhand_hold_night05:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0
        ease 2.0 xpos 0.0
        ease 2.0 zoom 0.5 xpos 0.5 ypos 0.5
    with hpunch

    n "Agarras de la mano a tu compañera,"

    n "como si fuera una niña pequeña, sigue tus pasos con la mirada perdida y el rostro en un mar de lágrimas."

    scene black
    with fade

    n "Conseguís coger un taxi justo en la salida y durante el transcurso del viaje,"

    n "Neus sigue manteniendo esa mirada perdida en la nada,"

    n "encogida de hombros y temblando de miedo."

    if MShooter_Present_Necklace_Ankh == False:

        n "De tanto en cuando, ves como mira en su bolso,"

        n "y te parece ver entre sus dedos"

        n "un collar dorado con la misma cruz que lleva tatuada en su pecho."

    pt "¿Qué diablos será lo que aún no me ha contado...?"

    #call WIP

    #call endupdate

    #jump gameover

    #scene day05
    with fade

    jump afternight05_Pedrera_arrive


label night05_NeusLastDate_Noria_Angry:

    $ night05_NeusLastDate_Noria_Angry_Cond = True

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_03
    show neus_exp_eyebrows angryx05
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_tears 03_03
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "Sinceramente esperaba que pudieras disfrutar mejor de mi compañía,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_tears 02_03
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "pero supongo que te estaba pidiendo demasiado."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_03
    show neus_exp_eyebrows sadx02
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_tears 08_04
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "No voy a insistir más,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_tears 04_04
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "has cumplido con las tres citas tal y como te pedí,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_tears 02_04
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "quizás con menos ganas de las que me hubiera gustado,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_05
    show neus_exp_eyebrows angryx03
    with dissolve

    ne "pero tampoco te obligué a ello."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_tears 07_05
    show neus_exp_eyebrows sadx04
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Podemos dar la cita por finalizada."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_tears 02_05
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "Así que eres libre de irte si quieres."

    show neus_arm_r sd:
        neus_body_atright_close_position
    show neus_body sd_default:
        neus_body_atright_close_position
    show neus_head:
        neus_body_atright_close_position
    show neus_arm_l sd:
        neus_body_atright_close_position
    
    show neus_exp_blush 03:
        neus_exp_atright_close_position
    show neus_exp_mouth sad_Talkingx08:
        neus_exp_atright_close_position
    show neus_exp_eyes 01:
        neus_exp_atright_close_position
    show neus_exp_iris front01:
        neus_exp_atright_close_position
    show neus_exp_tears 01_05:
        neus_exp_atright_close_position
    show neus_exp_eyebrows angryx04:
        neus_exp_atright_close_position
    show neus_exp_glasses:
        neus_exp_atright_close_position
    show neus_exp_hairfront:
        neus_exp_atright_close_position
    with dissolve

    ne "Toma."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows angryx03
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx11
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_tears 08_05
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "Aquí tienes el tique para el funicular,"

    show neus_exp_mouth sad_Talkingx10
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "y el billete de una zona para que vuelvas a casa."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_tears 02_05
    show neus_exp_eyebrows angryx03
    with dissolve

    ne "Es una {i}T-10{/i} a la que le sobran como siete viajes,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "pero tampoco lo voy a necesitar más."

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position
    
    show neus_exp_blush 03:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx04:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris right04:
        neus_exp_atright_position
    show neus_exp_tears 04_05:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx07:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    p "Pero..."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows angryx03
    with dissolve

    p "¿Cómo vas a volver tú?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_tears 02_05
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "Voy a coger un taxi."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "No quiero aburrirte más con mi compañía."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_05
    show neus_exp_eyebrows sadx07
    with dissolve

    p "..."

    if night05_Interrogation_DidacAgainBeingMan_Cond == False:

        show neus_exp_mouth sad_Silentx08
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows angryx04
        with dissolve

        p "Pero..."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_05
        show neus_exp_eyebrows angryx02
        with dissolve

        p "¿Y Dídac...?"

        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_tears 02_05
        show neus_exp_eyebrows angryx04
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx09
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_tears 08_05
        show neus_exp_eyebrows angryx05
        with dissolve

        ne "No te preocupes por él."

        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_tears 03_05
        show neus_exp_eyebrows angryx04
        with dissolve

        ne "En pocos días volverá a ser el de siempre."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_tears 04_05
        show neus_exp_eyebrows sadx06
        with dissolve

        p "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_tears 08_05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "De corazón te lo digo [protname]."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_tears 03_05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Espero que seas feliz."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_tears 07_05
    show neus_exp_eyebrows sadx07
    with dissolve

    pause 0.5

    scene bg night05_bg_tibidabo_park_00:
        truecenter
        zoom 0.6 xpos 0.6 ypos 0.4
    with dissolve

    n "Dicho esto se dirige hasta la entrada del parque,"

    n "donde desaparece de tu vista al cruzar el enorme mural."

    p "..."

    pt "Se le podrán reprochar muchas cosas;"

    pt "mimada,"

    extend " consentida,"

    extend " infantil,"

    extend " egoísta..."

    pt "Pero parece que ha hecho el esfuerzo de intentar ser sincera conmigo."

    p "..."

    pt "¡Tengo que volver a casa para ver cómo está Dídac!"

    #

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    if music_play != "decline":
        play music "audio/music/kevinmacleod/sad/decline.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "decline"

    scene afternight03_bg_entrance_lightoff_night
    if (DidacMCPregnant == False and 
        DidacOKUPregnant == False):
        show afternight03_bg_entrance_keysd lightoff_night:
            afternight03_bg_entrance_keys
    with fade

    $ saturation_tint_level = "verydark"

    n "Después de un largo viaje en el funicular, el tranvía azul, el metro, y finalmente el complicado bus de noche;"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "consigues llegar al piso."

    n "Entras en la habitación."

    if (DidacMCPregnant == True or 
        DidacOKUPregnant == True):

        scene beds_night_lightOff_blindUp_DemptyMCempty
        with fade

        pt "¡Mierda!"

        pt "¡¿Dónde diablos te has metido Dídac?!"

        n "La habitación se encuentra completamente vacía y con las dos camas intactas."

        n "Miras por todo el piso en su búsqueda, sin ningún resultado."

        show go_07_e
        hide go_07_e

        show morning04_bg_livingroom_mc_resting_phone didac:
            xpos 0.485 ypos 0.125
        show morning04_livingroom_mc_resting_handphone
        with dissolve

        n "Usas el móvil para intentar ponerte en contacto con él,"

        n "y lo único que recibes es el silencio."

        hide morning04_bg_livingroom_mc_resting_phone
        hide morning04_livingroom_mc_resting_handphone
        with dissolve

        pt "Joder..."

        if aftermorning05_AfterDeepsea_Mossos_Cond == True:

            $ night05_NeusLastDate_Noria_Angry_ToldYouDidacFate = True

            pt "¿Seguirá aún en comisaría después de lo que pasó en la playa?"

            scene bg an04_flat_gate_composition002:
                subpixel True
                zoom 0.5 xanchor 0.0 yanchor 1.4
                easein_quad 10.0 zoom 1.0 xanchor 0.8 yanchor 1.8
            with fade

            n "Ni corto ni perezoso,"

            scene bg an04_street_01:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 10.0 zoom 1.0
            with fade

            n "sales a la calle en búsqueda de la comisaría más cercana."

            scene bg night05_bg_policestation:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 20.0 zoom 1.0
            with fade

            n "Entonces, a escasos metros de llegar a ella, te suena el teléfono."

            play sound "audio/sfx/ring_phone01.ogg"

            scene bg night05_bg_policestation:
                subpixel True
                truecenter
                zoom 0.8
            with vpunch

            pause 0.2

            show morning04_bg_livingroom_mc_resting_phone unknownmale:
                xpos 0.485 ypos 0.125
            show morning04_livingroom_mc_resting_handphone
            with dissolve

            pt "¿Quién diablos es...?"

            hide morning04_bg_livingroom_mc_resting_phone
            hide morning04_livingroom_mc_resting_handphone
            with dissolve

            p "¿Sí...?"

            if music_play != "classichorror01":
                play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "classichorror01"

            ne "No vayas."

            p "¿Qué...?"

            ne "Si hablas de Dídac a las autoridades,"

            extend " o descubren algo sobre su transformación,"

            ne "levantarás demasiado polvo."

            p "¿Acaso me estás amenazando?"

            ne "No."

            ne "No es una amenaza,"

            ne "es una advertencia."

            ne "Si hablas de Dídac a la policía,"

            extend " acabarás muerto antes de que puedas dar una segunda descripción."

            p "..."

            ne "Lo siento."

            p "Pero..."

            p "¿Por qué?"

            if DidacMCPregnant == True:

                ne "Por que Dídac está embarazada de ti."

            elif DidacOKUPregnant == True:

                ne "Por que Dídac está embarazada."

                # NOT FINISHED, If you wistened how she became pregnant.

                p "¡¿De quien?!"

                ne "¿Acaso importa?"

                p "¡Claro que importa!"

                p "¡Si no lo hubieras transformado en mujer,"

                extend "\nesto no hubiera pasado!"

                ne "..."

                ne "Lo sé,"

                ne "y lo lamento..."

                extend "\nde verdad."

                ne "Pero, como te he dicho,"

                ne "ya no hay nada que ni tú,"

                extend " ni yo,"

                ne "podamos hacer para cambiar eso."

            p "..."

            p "Pero..."

            p "¿Está bien?"

            ne "Sí..."

            ne "Pero no volverás a verlo nunca más."

            ne "Ni a mí tampoco."

            p "Espera..."

            p "¡¿Qué?!"

            ne "Lo siento..."

            ne "Adiós [protname]."

            p "¡Espera!"

            play sound "audio/sfx/click02.ogg"

            ono "bip"

            if music_play != "darkTimes":
                play music "audio/music/kevinmacleod/sad/darkTimes.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "darkTimes"

            p "..."

        if aftermorning05_DidacFar_01_Cond == True: # Not finished, it should be used another one when is ready.

            pt "La última vez que lo vi fue con ese grupo de capullos en la playa..."

            pt "No debería haberlo dejado ahí..."

            pt "Mierda..."

        elif afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

            pt "Después de que esos capullos me dieran una paliza, Dídac se fue con ellos..."

            pt "¡¿Por qué diablos tengo que preocuparme por ti?!"

            pt "¡Joder!"

        elif afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant == True:

            pt "La última vez que lo vi fue con esos tres capullos del parque..."

            pt "Espero sinceramente que no haya hecho ninguna gilipollez."

        elif DidacOKUPregnant == True:

            # NOT FINISHED Conditional in order you wistened this.

            pt "Recuerdo que ese puto {b}yonqui{/b} se terminó corriendo dentro..."

            pt "Mierda..."

        elif DidacMCPregnant == True:

            pt "Recuerdo que ayer por la noche cuando estuvimos follando,"

            pt "Fue él quien me puso el último condón."

            pt "Y se sentía distinto a los otros dos..."

            pt "¿Puede ser que estuviera roto...?"

            pt "Y si..."

            pt "¿Y si acabé corriéndome dentro en realidad?"

            pt "Estaría condenado a quedarse como mujer el resto de su vida,"

            pt "o lo que es peor..."

            pt "Mierda..."
        else:

            pt "¿Se supone que tendría que ir a buscarlo?"

            pt "¿Pero dónde?"

            pt "¡¿Por dónde demonios empiezo a buscarle?!"

            pt "Podría estar en cualquier lado..."

        window hide dissolve
        pause

        if night05_NeusLastDate_Noria_Angry_ToldYouDidacFate == False:

            scene afternight03_bg_entrance_lightoff_night
            with fade

            show afternight03_bg_entrance_keysmc lightoff_night:
                afternight03_bg_entrance_keys
            with dissolve

            scene beds_night_lightOff_blindUp_DemptyMCempty
            with fade

            pt "¡¿Dónde coño te has metido imbécil?!"

            scene beds_morning_lightOff_blindUp_DemptyMCmessy
            with Dissolve (1.0)

            n "Al día siguiente,"

            n "sigues viendo la cama de tu compañero de piso vacía;"

            scene beds_morning_lightOff_blindUp_DemptyMCempty
            with dissolve

            n "te levantas y te vistes para ir a la escuela de Ilustración,"

            n "con la esperanza de encontrar a Neus en busca de respuestas."

    else: #Not Pregnant, He becomes a Man again.

        if music_play != "sovereign":
            play music "audio/music/kevinmacleod/happy/sovereign.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "sovereign"

        $ saturation_tint_level = "verydark"

        scene beds_night_lightOff_blindUp_Dbusy02MCempty
        show beds_D02b
        with fade

        pt "Está durmiendo..."

        n "De tus pulmones emana un largo suspiro de tranquilidad."

        pt "Sigue siendo una mujer."

        pt "Me ha dicho que en unos días volverá a ser el que era..."

        if aftermorning05_AfterDeepsea_Mossos_Cond == True:

            pt "Pensé que aún estaría en comisaría,"

            pt "después de lo que ocurrió en la playa..."

        ## park scene is not necessary, since she get pregnant or you take off of her.

        elif (morning05_sexwithDidacNotatHome_Cond == True or
            aftermorning05_DidacFar_01_Cond == True):

            pt "Me alegro que siga estando de una pieza,"

            if morning05_sexwithDidacNotatHome_Cond == True:

                pt "Después de ver que no estaba aquí por la mañana,"

            elif aftermorning05_DidacFar_01_Cond == True:

                pt "Después de dejarle con esos desalmados en la playa,"

            pt "me temí lo peor..."

        pt "Supongo que solo queda esperar..."

        $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
        $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        show afternight03_bg_shower
        with fade

        n "Te das una ducha rápida,"

        $ renpy.music.stop(channel='sfx1', fadeout=3.0)
        stop music fadeout 0.5
        $ music_play = ""

        hide afternight03_bg_shower
        with fade

        show black:
            subpixel True
            alpha 0.0
            easein_quad 1.0 alpha 1.0

        n "para luego volver a la habitación y reunirte con Morfeo."

        $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
        $ renpy.music.play("audio/sfx/birds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        $ saturation_tint_level = "default"

        scene beds_morning_lightOff_blindUp_Dbusy02MCbusy
        show beds_D02b
        with fade

        n "Al día siguiente al levantarte, oyes los extraños gemidos de tu compañero,"

        n "pero esta vez no son de placer, sino de dolor."

        show go_07_j
        hide go_07_j

        scene didac_bed_bed over_sweaty
        show didac_bed_d_body 04
        show didac_bed_d_sweat 03-04
        show didac_bed_d_blush 04
        show didac_bed_d_mouth sad_Silentx05
        show didac_bed_d_eyes 07
        show didac_bed_d_eyespup empty
        show didac_bed_d_eyebrows angryx04
        show didac_bed_d_hair 04
        show didac_bed_headtowel empty
        show didac_bed_d_blanket 00
        with fade

        n "Al acercarte a él, descubres que su cuerpo y su cama vuelven a estar empapados en sudor,"

        n "y que su masa muscular vuelve a recuperar algo de volumen."

        pt "Parece que la transformación no es un proceso indoloro, ni rápido..."

        pt "Supongo que podré agradecérselo hoy a Neus cuando la vea por la escuela."

        pt "Es lo mínimo que puedo hacer."

    if night05_NeusLastDate_Noria_Angry_ToldYouDidacFate == True: #Neus Phoned you.

        scene afternight03_bg_entrance_lightoff_night
        show afternight03_bg_entrance_keysd lightoff_night:
            afternight03_bg_entrance_keys
        with fade

        play sound "audio/sfx/metal_keys_deposit.ogg"

        show afternight03_bg_entrance_keysmc lightoff_night:
            afternight03_bg_entrance_keys
        with dissolve

        scene beds_night_lightOff_blindUp_DemptyMCempty
        with fade

        stop music fadeout 3.0
        $ music_play = ""

        show black:
            subpixel True
            alpha 0.0
            easein_quad 3.0 alpha 1.0

        window hide dissolve
        pause

        $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
        $ renpy.music.play("audio/sfx/birds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        scene beds_morning_lightOff_blindUp_DemptyMCmessy
        with Dissolve (1.0)

        n "Al día siguiente al levantarte, tan solo oyes el canto de los pájaros."

        n "La cama de Dídac sigue estando vacía."

        $ renpy.music.stop(channel='sfx1', fadeout=3.0)

        if music_play != "decline":
            play music "audio/music/kevinmacleod/sad/decline.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "decline"

        scene morning02_bg_schoolwall
        with fade

        n "Al ser lunes, regresas a la escuela de Ilustración,"

        n "donde, como era de esperar, no encuentras a Neus,"

        n "ni a Dídac;"

        n "pero a la que tampoco encuentras, es a la rubia tetuda."

        n "Algunos días después descubres que dejó el curso,"

        $ mmouthp = "" # is not "_blue" anymore.
        $ saturation_tint_level = "default"

        scene bg 05afternoon_entrance_receptiondoor_closed_bg:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.55 ypos 0.9
            easein 15.0 zoom 0.5 xpos 0.5 ypos 0.5
        with fade

        n "y pudiste descubrir su lugar de trabajo."

        scene bg 05afternoon_entrance_reception_bg:
            truecenter
            zoom 0.3335  xpos 0.5 ypos 0.5

        show m_bodynew hips_04:
            mtxell_body_ontheright_zoom_0_3_pos

        show m_exp_blush 01:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_mouth sad_Silentx03:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_eyes 02:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_piris front02:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_eyebrows surprisex01:
            mtxell_exp_ontheright_zoom_0_3_pos

        show m_exp_hair_front:
            mtxell_exp_ontheright_zoom_0_3_pos
        with fade_short

        n "Ni siquiera se acordaba de tu cara, ni de Neus."

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows suspiciousx03
        with dissolve

        pause 0.2

        scene beds_midday_lightOff_blindUp_DemptyMCmessy
        with fade

        n "Los padres de Dídac habían recibido una carta del puño y letra de su propio hijo,"

        n "en el que este les decía que se marchaba."

        n "Cuando hablaste con ellos en alguna ocasión,"

        n "te dio la sensación de que se lo habían tomado relativamente bien,"

        n "como si fuera una aventura que tuviera que vivir por sí solo,"

        n "alejado del mundo y de la familia."

        show beds_afternoon_lightOn_blindUp_DemptyMCmessy:
            subpixel True
            alpha 0.0
            easein_quad 5.0 alpha 1.0
        with dissolve

        n "Algo así te hizo sospechar que esa actitud no había sido algo natural."

        n "Las horas pasaban de forma lenta, y los días se te hacían interminables."

        show beds_night_lightOn_blindUp_DemptyMCmessy:
            alpha 0.0
            easein_quad 5.0 alpha 1.0
        with dissolve

        if DidacMCPregnant == True:

            n "Quizás, si no hubieras aceptado tener sexo con Dídac,"

            n "o por lo menos te hubieras asegurado de que el último condón estaba en buenas condiciones;"

        elif DidacOKUPregnant == True:

            n "Quizás, si no hubieras permitido que ese {b}yonqui{/b} de mierda se hubiera corrido dentro de Dídac;"

        show beds_night_lightOff_blindUp_DemptyMCmessy:
            alpha 0.0
            easein_quad 3.0 alpha 1.0
        with dissolve

        n "ahora estarías disfrutando de su compañía, de sus tonterías, de sus locuras, de sus risas..."

        show black:
            alpha 0.0
            easein_quad 3.0 alpha 1.0

        n "Quizás..."

        window hide dissolve
        pause

        aj "FINAL ALTERNATIVO 07a" # Noria Date Fail -- Didac is not with you.

        jump gameover 

    else:

        $ renpy.music.stop(channel='sfx1', fadeout=3.0)

        if music_play != "crypticSorrow":
            play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "crypticSorrow"

        scene morning02_bg_schoolwall
        with fade

        n "Pero al llegar al centro docente, a pesar de buscarla en cada rincón del lugar,"

        n "y preguntar por ella hasta al director;"

        n "descubres, no solo que no está por ninguna parte,"

        n "sino que nadie, absolutamente nadie,"

        n "recuerda que hubiera existido una alumna con esa apariencia ni con ese nombre."

        n "Después de las clases,"

        $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
        $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        scene night03_bg street_pedrera_far
        with fade

        n "decides visitar el emblemático edificio de la {i}Pedrera{/i} como un turista más,"

        $ renpy.music.stop(channel='sfx1', fadeout=3.0)

        scene night03_bg_street_pedrera_entrance
        with fade

        n "al preguntar al guía sobre el piso en el que estás interesado,"

        show night03_bg_street_pedrera_entrance_lightson:
            subpixel True
            alpha 0.0
            easein_quad 20.0 alpha 1.0
        with dissolve

        n "te comenta, después de mucho insistir, que ahí no vive nadie desde hace décadas,"

        n "que ese lugar le pertenece a un inversor privado"

        n "y que tampoco te puede dar muchos detalles sobre el tema."

        n "Luego caes en la cuenta de que tampoco habías encontrado por ningún sitio a la rubia tetuda;"

        if afternoon04_MACBA_TxellTruth_Cond == False:

            scene morning02_bg_schoolwall
            with fade

            n "Intentas indagar por la escuela sobre ella y un profesor te comenta que había abandonado el curso."

            n "Insistiendo un poco más descubres dónde puedes encontrarla."

        $ mmouthp = "" # is not "_blue" anymore.
        $ saturation_tint_level = "default"

        scene bg 05afternoon_entrance_receptiondoor_closed_bg:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.55 ypos 0.9
            easein 15.0 zoom 0.5 xpos 0.5 ypos 0.5
        with fade

        n "Así que decides ir a su despacho para hallar alguna respuesta."

        scene bg 05afternoon_entrance_reception_bg:
            truecenter
            zoom 0.3335  xpos 0.5 ypos 0.5

        show m_bodynew hips_04:
            mtxell_body_ontheright_zoom_0_3_pos

        show m_exp_blush 01:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_mouth sad_Silentx03:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_eyes 02:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_piris front02:
            mtxell_exp_ontheright_zoom_0_3_pos
        show m_exp_eyebrows surprisex01:
            mtxell_exp_ontheright_zoom_0_3_pos

        show m_exp_hair_front:
            mtxell_exp_ontheright_zoom_0_3_pos
        with fade_short

        n "Una vez logras llegar y después de discutir con la recepcionista,"

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows surprisex002
        with dissolve

        n "consigues acceder a ella, donde le preguntas por Neus."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx03
        with dissolve

        n "Su cara de asombro y de incertidumbre destruye toda esperanza que hubieras podido sostener."

        ##

        if (DidacMCPregnant == True or 
            DidacOKUPregnant == True):

            scene beds_night_lightOff_blindUp_DemptyMCmessy
            with fade
            show beds_morning_lightOff_blindUp_DemptyMCmessy:
                subpixel True
                alpha 0.0
                easein_quad 10.0 alpha 1.0

        else:

            scene beds_morning_lightOff_blindUp_Dbusy02MCmessy
            show beds_D02b
            with fade

        n "Al día siguiente,"

        if (DidacMCPregnant == True or 
            DidacOKUPregnant == True):

            n "te encuentras con el mismo desolador panorama."

            n "Durmiendo solo en una habitación,"

            n "que no hacía tantos días disfrutabas con esa peculiar -pero entrañable- compañía."

            n "Intentas ponerte en contacto con sus padres para saber si tienen alguna noticia de él."

            n "Te cuentan que recibieron un correo electrónico de su parte diciéndoles que no le buscaran,"

            n "que había decido desaparecer del mapa para tener aventuras por el mundo,"

            n "y que les prometió que, de tanto en cuanto, les iría dando noticias."

            n "Te sorprendió que se lo tomaran tan a la ligera,"

            n "casi como si les hiciera ilusión que su hijo se hubiera independizado a ese nivel."

            n "No te cabía ninguna duda de que esa actitud no tenía nada de natural."

            show beds_midday_lightOff_blindUp_DemptyMCmessy:
                alpha 0.0
                easein_quad 10.0 alpha 1.0

            n "Los días se iban sucediendo, y la rutina volvió a aparecer en tu vida."

            n "Es verdad que Dídac no era un personaje demasiado educado ni cariñoso,"

            n "pero alguien tan extrovertido y risueño se había ganado muchas amistades por la ciudad,"

            show beds_afternoon_lightOn_blindUp_DemptyMCempty:
                alpha 0.0
                easein_quad 10.0 alpha 1.0

            n "sin embargo te daba la sensación de que nadie lo extrañaba,"

            n "como si nunca hubiera tenido amistades o conocidos..."

            n "como si nunca hubiera existido."

            n "Como si hubiera sido un sueño que apenas solo tú recuerdas con cariño y pesar."

            show beds_night_lightOn_blindUp_DemptyMCmessy:
                alpha 0.0
                easein_quad 10.0 alpha 1.0

            n "Las horas pasaban de forma lenta, y los días se te hacían interminables."

            if DidacMCPregnant == True:

                n "Quizás, si no hubieras aceptado tener sexo con Dídac,"

                n "o por lo menos te hubieras asegurado de que el último condón estaba en buenas condiciones;"

            elif DidacOKUPregnant == True:

                n "Quizás, si no hubieras permitido que ese {b}yonqui{/b} de mierda se corriera dentro de Dídac;"

            scene beds_night_lightOn_blindUp_DemptyMCmessy
            show beds_night_lightOff_blindUp_DemptyMCmessy:
                alpha 0.0
                easein_quad 5.0 alpha 1.0

            n "ahora estarías disfrutando de su compañía, de sus tonterías, de sus locuras, de sus risas..."

            show black:
                alpha 0.0
                easein_quad 5.0 alpha 1.0

            n "Quizás..."

            window hide dissolve
            pause

            aj "FINAL ALTERNATIVO 07b" # Noria Date Fail -- Didac is not with you... what's difference with A?

            jump gameover 

        else:

            scene didac_bed_bed over_sweaty
            show didac_bed_d_body 03
            show didac_bed_d_sweat 03-04
            show didac_bed_d_blush 03
            show didac_bed_d_mouth sad_Silentx04
            show didac_bed_d_eyes 06
            show didac_bed_d_eyespup empty
            show didac_bed_d_eyebrows angryx02
            show didac_bed_d_hair 03
            show didac_bed_headtowel wet
            show didac_bed_d_blanket 01
            with fade

            n "Dídac ya se encuentra mucho más recuperado de salud y de forma física,"

            show didac_bed_d_mouth sad_Silentx03
            show didac_bed_d_eyes 03
            show didac_bed_d_eyespup front03
            show didac_bed_d_eyebrows normal
            with dissolve

            n "así que intentas preguntarle si recuerda algo de Neus,"

            show didac_bed_d_mouth sad_Silentx01
            show didac_bed_d_eyes 03
            show didac_bed_d_eyespup upleft03
            show didac_bed_d_eyebrows suspiciousx02
            with dissolve

            n "No solo no se acuerda de ella,"

            show beds_midday_lightOff_blindUp_Dbusy02MCmessy
            show beds_D02b
            with dissolve

            n "sino que ni siquiera recuerda estos últimos cinco días,"

            n "ni que se había convertido en mujer, ni el incidente del baño,"

            n "ni de las cosas que habías llegado a hacer."

            call saturation_ting_values_check # Delte this, is just for refreshing colors.

            $ saturation_tint_level = "afternoon"

            scene beds_afternoon_lightOff_blindUp_Dbusy02MCmessy
            show beds_D02b
            with Dissolve (1.0)

            n "Nada."

            $ saturation_tint_level = "verydark"

            scene beds_night_lightOff_blindUp_Dbusy02MCmessy
            show beds_D02b
            with Dissolve (1.0)

            scene black
            with fade

            $ saturation_tint_level = "default"

            n "Como si todo lo ocurrido hubiera sido un sueño."

            scene beds_morning_lightOff_blindUp_Dbusy01MCmessy
            show beds_D01b
            with fade

            n "Al día siguiente,"

            scene didac_bed_bed over_sweaty
            show didac_bed_d_body 02
            show didac_bed_d_sweat 02
            show didac_bed_d_blush 03
            show didac_bed_d_mouth sad_Silentx01
            show didac_bed_d_eyes 06
            show didac_bed_d_eyespup empty
            show didac_bed_d_eyebrows normal
            show didac_bed_d_hair 02
            show didac_bed_headtowel dry
            show didac_bed_d_blanket 01
            with fade

            n "Dídac había recuperado prácticamente su forma original,"

            n "y su humor particular."

            scene beds_midday_lightOff_blindUp_DemptyMCempty
            with fade

            n "A pesar de todo lo ocurrido, todo volvía a la normalidad,"

            show beds_afternoon_lightOn_blindUp_DemptyMCempty:
                alpha 0.0
                easein_quad 5.0 alpha 1.0

            n "habías logrado tu objetivo, ayudar a tu viejo amigo, y recuperar tu vida."

            n "Pero aún así, en tu mente seguían esos recuerdos,"

            n "de esa chica bajita de ojos verdes,"

            show beds_night_lightOn_blindUp_DemptyMCempty:
                alpha 0.0
                easein_quad 5.0 alpha 1.0

            n "con las mejillas empapadas en lágrimas."

            n "{i}De corazón te lo digo [protname].{/i}"

            show beds_night_lightOff_blindUp_DemptyMCempty:
                alpha 0.0
                easein_quad 5.0 alpha 1.0

            n "{i}Espero que seas feliz.{/i}"

            show black:
                alpha 0.0
                easein_quad 5.0 alpha 1.0
            
            pt "Quizás hubiera podido hacer las cosas de otro modo..."
            
            pt "Quizás..."

            window hide dissolve
            pause

            aj "FINAL ALTERNATIVO 07c" # Noria Date Fail -- Didac is with you.

        jump gameover 


        # NOT FINISHED. Write End of this BAD ENDING.

# Cuando os subís y estáis en la cima, te pide disculpas por todo lo currido y te agradece que hayas venido hasta ahí. Luego te insinua que durante toda la cita, no has sido capaz de hacerle ni siquiera un beso... Cuando estáis cerca de besaros un foco de luz os ilumina la cara con un enorme estruendo, enormes fuegos de artificio se están lanzando en la ciudad al estar tan cerca de Sant Joan, en ese instante decides besarla bajo los fuegos de artificio en uno de los lugares más altos de la ciudad.

# Poco después de besarla, recibes un mensaje en el móvil. Al abrir la aplicación descubres que es una foto de Dídac desnuda sonriente en el piso de la pedrera donde vive Neus. Con el siguiente mensaje. "Os estamos esperando".

# Os?! Neus te pregunta qué ocurre y decides mostrarle el móvil. Su rostro cambia completamente. Su cuerpo empieza a temblar. Unas lágrimas empiezan a dearramarse por sus mejillas.

#Le preguntas si se encuentra bien.

# Neus dice... Nos ha encontrado.

# Dices que tienes que ir al piso a rescatar a Dídac. Ella te agarra del brazo. Si vamos allí, todos vamos a morir. No puedo dejar a Dídac. NO! NO PUEDO ABANDONAR A MI AMIGO POR MUY GILIPOLLAS QUE SEA! QUE CLASE DE PERSONA SOY?! Neus te dice... tienes razón... Su cuerpo sigue temblando. Al fin y al cabo si sabe dónde vivo, también sabrá dónde estoy ahora... sería absurdo intentar huir... al final me ha encontrado... Intentas inutilmente animarla, pero tus esfuerzos son en vano, apenas te oye, apenas escucha nada... su mirada está como perdida, como un animal bloqueado en un rincón por el miedo, incapaz de reaccionar. La agarras por la mano y salís de la atracción, decides tomar un taxi que os lleve directamente hasta la Pedrera. ## FINAL DEMO

#Durante todo el transcurso del viaje, Neus sigue en modo shock sin saber qué decir ni dónde mirar... Por un instante te mira a los ojos, para luego aparatarlos de golpe. Si intentas hablar con ella, te aparta la mirada. ¿He dicho algo malo...?



