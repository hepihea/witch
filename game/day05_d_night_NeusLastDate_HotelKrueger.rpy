default night05_NeusLastDate_HotelKrueger_Door_Exit_01_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_Exit_02_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_Exit_03_Cond = False

default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond_Temp = False
default night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp = False
default night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp = False

default night05_NeusLastDate_HotelKrueger_Door_Used_Number = 0


##############
##
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number = 0
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_01_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_02_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_03_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_04_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_05_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_06_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_All_Cond = False
default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_family_Cond = False

default night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_family_met_Cond = False # This should be deleted in future.
default room_01_cemetery_mother_met_Cond = False # The same over, but shorter.

##############
##
default room_02_child_hallway_but_toy_ball_Cond = False
default room_02_child_hallway_but_toy_warrior_Cond = False
default room_02_child_hallway_but_toy_console_Cond = False
default room_02_child_hallway_but_toy_slingshot_Cond = False
default room_02_child_hallway_but_toy_robot_Cond = False
default room_02_child_hallway_but_toy_piano_Cond = False
default room_02_child_hallway_but_toy_Number = 0

default room_02_child_hallway_but_photo_01_Cond = False
default room_02_child_hallway_but_photo_02_Cond = False
default room_02_child_hallway_but_photo_03_Cond = False
default room_02_child_hallway_but_photo_04_Cond = False
default room_02_child_hallway_but_photo_05_Cond = False
default room_02_child_hallway_but_photo_Number = 0

default room_02_child_room_but_exit_Cond = False
default room_02_child_room_but_kid_Cond = False

default room_02_child_hallway_but_Completed = False
default room_02_child_hallway_door_bright_Cond = False
##

default room_02_child_room_but_object_blood_Cond = False
default room_02_child_room_but_object_cigarretes_Cond = False
default room_02_child_room_but_object_coctels_Cond = False
default room_02_child_room_but_object_condom_Cond = False
default room_02_child_room_but_object_drugs_Cond = False
default room_02_child_room_but_object_wine_Cond = False
default room_02_child_room_but_object_Number = 0

default room_02_child_room_but_object_Completed = False
default room_02_child_ALLDONE = False

##############
###
default room_03_marriage_far_but_object_bouquet_Cond = False
default room_03_marriage_far_but_object_cake_Cond = False
default room_03_marriage_far_but_object_chocolates_Cond = False
default room_03_marriage_far_but_object_petals_Cond = False
default room_03_marriage_far_but_object_rings_Cond = False
default room_03_marriage_far_but_object_vows_Cond = False
default room_03_marriage_far_but_object_Number = 0

default room_03_marriage_far_door_Cond = False
default room_03_marriage_far_door_before_Cond = False
default room_03_marriage_ALLDONE = False

default room_03_marriage_far_woman_close_old_Yes = False

default room_03_marriage_far_woman_Cond = False



label night05_NeusLastDate_HotelKrueger:

    $ dad = d_dad

    #$ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    scene bg night05_bg_castle_siege_comp_02:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.1
        ease_quad 5.0 zoom 1.0 xpos 0.0 ypos 0.1
    with dissolve

    pause 2.0

    scene black
    with hpunch

    play sound "audio/characters/protagonist/au01.ogg"

    p "??Auh!"

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    n "Justo cuando traspasas el cerco que ha levantado esa extra??a mujer,"

    n "sientes su mano pos??ndose sobre tu nuca,"

    n "al mismo tiempo que un pinchazo."

    # Look back her. She smiling (no eyes.)

    scene m_park_guard_comp serious:
        subpixel True
        truecenter
        xpos 0.75 ypos -1.0 zoom 1.0 # Boobs
        ease_quad 3.0 xpos 0.5 ypos 0.4 zoom 0.75 # Face
    with fade

    n "R??pidamente tuerces el cuello para mirar atr??s,"

    n "y fijarte en esa extra??a mujer que con un rostro impasible y sereno te dice:"

    # She talking

    show m_park_guard_comp happy_Talking
    with dissolve

    gm "Disfrute del espect??culo."

    show m_park_guard_comp happy_Silent
    with dissolve

    pt "Esta voz me suena..."

    # Kid image?

    scene black
    with fade

    n "Mientras sientes los empujones del ni??o de atr??s queri??ndose subir a las escaleras mec??nicas."

    pt "????Qu?? diablos?!..."

    # Stairs.

    stop music fadeout 3.0
    $ music_play = ""

    scene bg night05_bg_castle_siege_stairs_comp:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.8 ypos 0.75 # Top
        pause 1.0
        ease 8.0 zoom 0.5 xpos 0.7 ypos -0.8 # Middle
        #ease_quad 8.0 zoom 0.5 xpos 0.8 ypos -1.5 # Below
    with fade

    window hide dissolve
    pause

    scene bg night05_bg_castle_siege_stairs_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -4.0 # Base stairs
        easein 5.0 zoom 0.75 xpos 0.5 ypos -1.0 # Starting up.
    with fade
        #zoom 1.0 xpos 0.5 ypos 0.8 # Top stairs
    #show draft_metric

    n "Decides seguir los pasos de Neus y subir por estas endiabladas escaleras."

    show bg night05_bg_castle_siege_stairs_comp:
        subpixel True
        easein_bounce 0.4 zoom 1.0 xpos 0.5 ypos -2.0 # Starting up.

    pause 0.01

    play sound "audio/sfx/fall01.ogg"

    show black
    with fade

    if music_play != "happy_boy_end_theme":
        play music "audio/music/kevinmacleod/happy_boy_end_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "happy_boy_end_theme"

    n "Al pisar el primer escal??n tienes la sensaci??n de que te vas a caer,"

    hide black
    show bg night05_bg_castle_siege_stairs_comp:
        ease_quad 3.0 zoom 0.75 xpos 0.5 ypos -1.0 # Starting up.
    with fade

    n "pero r??pidamente te agarras a la barandilla y logras salvarte del golpe."

    show bg night05_bg_castle_siege_stairs_comp:
        ease 10.0 zoom 1.5 xpos 0.5 ypos 0.8 # Top stairs

    n "Dando tumbos y cogi??ndote fuertemente a ambas barras de metal,"

    scene bg night05_bg_castle_siege_stairs_door:
        truecenter
        zoom 0.5
    with fade

    # Top BLack Door.

    n "consigues finalmente llegar a la cima sin encontrarte con nadie;"

    n "tan solo el oscuro agujero que conduce al interior de la atracci??n con la puerta abierta."

    p "????Neus?!"

    window hide dissolve
    pause

    pt "??D??nde se habr?? metido?"

    ne "??Venga!"

    ne "Entra de una vez,"

    n "Oyes su voz, que procede del interior."

    ne "te estoy esperando."

    pt "??Me dijo que me estar??a esperando en la cima!"

    pt "La madre que la..."

    show bg night05_bg_castle_siege_stairs_door:
        ease_quad 8 zoom 1.5 xpos 0.4

    n "Diriges tus pasos hacia esa entrada ennegrecida por la oscuridad."

    scene black
    with fade_long1s

    window hide dissolve
    pause

    #hide screen quick_menu with dissolve
    hide screen Points
    with dissolve

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    stop music fadeout 3.0
    $ music_play = ""

    pt "??Esto es una atracci??n infantil?"

    pt "??No veo una mierda!"

    p "??Neus?"

    ne "Estoy aqu??."

    n "Palpas las estrechas paredes del lugar intentando seguir su voz en medio de la completa oscuridad."

    p "????Neus?!"

    p "{size=35}????Neus?!{/size}"

    p "????Me oyes?!"

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    n "Decides mirar atr??s, por si consigues ver su silueta a contraluz por la puerta por la que has entrado."

    p "????D??nde est?? la entrada?!"

    p "??No he o??do que la cerraran!"

    p "????Y por qu?? no veo a nadie m??s?!"

    p "??Tampoco he caminado tanto como para que no vea absolutamente nada!"

    n "Sigues usando el tacto de tus manos para guiar tus pasos hasta que te topas con algo que no es una pared."

    $ saturation_tint_level = "superdark"


    p "??Euh...?"

    # Botones con un candelabro. (No eyes are visible.) But will be after telling you, only offering the truth with goat eyes.

    #scene white

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"

    play sound "audio/sfx/match_lighting01.ogg"

    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/candle01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.7, delay=30.0, channel='sfx1')
        
    scene bellhop_candle_comp sad_Silent:
        subpixel True
        truecenter
        zoom 2.5 xpos 1.09 ypos -2.3 # Candle
        pause 2.0
        ease_quad 10.0 zoom 0.25 xpos 0.5 ypos 0.15 # Face a bit far.

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        pause 0.5
        ease 2.0 alpha 0.0
    with fade

    window hide dissolve
    pause
    
    n "De pronto el fuego de una tenue vela en frente de ti,"

    n "te permite ver la decr??pita cara de un hombre vestido de botones que lleva un candelabro de mano."

    window hide dissolve
    pause

    scene bellhop_candle_comp sad_Talkingx02:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.1 # Face
    with fade

    bo "Bienvenido al {a=https://www.tibidabo.cat/es/en-el-parque/atracciones/hotel-krueger}Hotel {i}Kr??eger{/i}{/a}."

    show bellhop_candle_comp sad_Silent
    with dissolve

    pt "????Hotel?!"

    pt "????No era esto un castillo?!"

    show bellhop_candle_comp sad_Talkingx03
    with dissolve

    bo "El espect??culo se desarrolla en un espacio muy poco iluminado."

    show bellhop_candle_comp sad_Silent
    with dissolve

    p "Oiga..."

    show bellhop_candle_comp sad_Talkingx04
    with dissolve

    bo "??Guarde silencio, por favor!"

    show bellhop_candle_comp sad_Silent
    with dissolve

    p "..."

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "Est?? prohibido gritar o hablarle a NADIE."

    show bellhop_candle_comp sad_Talkingx03
    with dissolve

    bo "No encender mecheros,"

    extend " cerillas,"

    extend " celulares,"

    extend " o ning??n otro tipo de objeto luminoso."

    show bellhop_candle_comp sad_Talkingx01
    with dissolve

    bo "Vayan siempre todos juntos."

    show bellhop_candle_comp sad_Silent
    with dissolve

    p "??Pero si no hay nadie m??s!"

    bo "..."

    p "..."

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "Sin separarse."

    bo "Sin correr."

    show bellhop_candle_comp sad_Talkingx01
    with dissolve

    bo "Y nunca retrocedan."

    show bellhop_candle_comp sad_Talkingx03
    with dissolve

    bo "No toquen NADA,"

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "ni a NADIE."

    show bellhop_candle_comp sad_Talkingx01
    with dissolve

    bo "Y les aseguro que nadie les tocar??."

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "En todo momento deben alejarse de la oscuridad,"

    show bellhop_candle_comp sad_Talkingx03
    with dissolve

    bo "y buscar el camino hacia la luz."

    show bellhop_candle_comp sad_Silent
    with dissolve

    pt "??El camino hacia la luz?"

    pt "????Es que estoy muerto?!"

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "M??s adelante hay una puerta con un picaporte,"

    show bellhop_candle_comp sad_Talkingx01
    with dissolve

    bo "Llamen tres veces,"

    show bellhop_candle_comp sad_Talkingx03
    with dissolve

    bo "y esperen a que alguien salga a recibirlos."

    show bellhop_candle_comp sad_Talkingx02
    with dissolve

    bo "Suerte."

    show bellhop_candle_comp sad_Silent
    with dissolve

    play sound "audio/sfx/blow01.ogg"
    $ renpy.music.stop(channel='sfx1', fadeout=0.5)

    show black:
        easein_quad 0.5 alpha 1.0
    with fade

    n "De pronto la llama del candelabro se apaga y vuelve a reinar la oscuridad absoluta."

    p "??Eh!"

    p "??Espere!"

    p "????Y los dem??s?!"

    p "????No ha visto a una morena bajita con gafas?!"

    p "??Oiga!"

    n "Alzas las manos para intentar encontrarle con el tacto,"
    
    n "y solo te encuentras con el vac??o."

    pt "????Qu?? demonios?!"

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    show night05_hotel_entrance_door_far_comp:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    with fade_long1s

    n "De repente,"

    extend " un foco de luz aparece en el fondo iluminando una t??trica puerta de madera,"

    n "con un extra??o picaporte."

    p "..."

    pt "Todo esto es muy raro..."

    pt "Ese pinchazo que he notado antes con la mujer de las gafas de sol..."

    n "Alzas tu mano para palparte la nuca,"

    n "pero no encuentras rastro de sangre ni nada parecido."

    pt "Neus nunca me dejar??a tirado de este modo..."

    p "..."

    show black02
    with fade

    n "Miras a tu espalda, a tus lados, a todo tu entorno."

    hide black02
    with fade

    n "A excepci??n de esa puerta y su pared, lo dem??s est?? ba??ado en una oscuridad absoluta."

    pt "No parece que tenga demasiadas opciones..."

    show night05_hotel_entrance_door_far_comp:
        subpixel True
        ease_quad 15.0 zoom 1.5 xpos -0.35 ypos 0.5

    n "Te acercas cautelosamente hasta el ??nico punto iluminado de la estancia,"

    scene black
    show night05_hotel_entrance_door close_down:
        truecenter
        zoom 0.5
        additive 1.0
        lightbulb_animation_01

    with fade

    show night05_hotel_entrance_door close_up
    with dissolve

    n "y obedeciendo a ese extra??o personaje, usas el picaporte dando tres golpes sobre la madera."

    play sound "audio/sfx/knock_wood_01.ogg"

    show night05_hotel_entrance_door close_down
    with vpunch

    ono "Toc"

    show night05_hotel_entrance_door close_up
    with dissolve

    play sound "audio/sfx/knock_wood_02.ogg"

    show night05_hotel_entrance_door close_down
    with vpunch

    extend " Toc"

    show night05_hotel_entrance_door close_up
    with dissolve

    play sound "audio/sfx/knock_wood_01.ogg"

    show night05_hotel_entrance_door close_down
    with vpunch

    extend " Toc"

    p "..."

    pt "??Y ahora qu??...?"

    play sound "audio/sfx/door_old_open03.ogg"

    show night05_hotel_entrance_door open
    with Dissolve (1.0)

    #ono "MEEEEEC"

    n "La puerta se abre sin que aparentemente haya nadie al otro lado."

    scene night05_hotel_hall_comp 00:
        truecenter
        zoom 0.5

    show black:
        easein 25 alpha 0.0
    with fade

    pt "El lugar est?? a oscuras,"

    extend "\npero al menos se ve algo..."

    pt "Esto parece el {a=https://es.wikipedia.org/wiki/Recibidor}{i}hall{/i}{/a} de un hotel..."

    pt "pero como si estuviera abandonado..."

    play sound "audio/sfx/door_slam01.ogg"
    with hpunch
    ono "PUM"

    show black02
    with fade

    pt "Mierda,"

    extend " ya no puedo volver atr??s..."

    hide black02

    #if music_play != "vanishing":
        #play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        #$ music_play = "vanishing"

    scene night05_hotel_hall_comp 01:
        truecenter
        zoom 0.5
    show black:
        subpixel True
        easein 5.0 alpha 0.0
    with fade

    n "Los candelabros se iluminan, dando m??s luz a la estancia."

    pt "Ser?? mejor ir con cuidado..."

    show night05_hotel_hall_comp 02:
        subpixel True
        easein 15.0 zoom 1.0

    with dissolve

    window hide dissolve
    pause 5.0

    show night05_hotel_hall_comp 02:
        easein 0.5 zoom 0.75
    with hpunch

    call saturation_ting_values_check # Delete this in future!

    $ saturation_tint_level = "candle"

    stop music fadeout 3.0
    $ music_play = ""
    
    adn "????SE PUEDE SABER QU?? EST??S HACIENDO AQU???!"

    p "????Euh?!"

    scene night05_hotel_hall_reception_comp far_01:
        truecenter
        zoom 0.5

    show nold_body_hotel:
        nold_body_align
        nold_tablefar_pos

    show nold_exp_eyes 01:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_piris front01:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_eyebrows sadx04:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_mouth sad_Silentx03:
        nold_expression_align
        nold_tablefar_pos

    show nold_nose:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_glasses:
        nold_expression_align
        nold_tablefar_pos

    show nold_overhead:
        nold_body_align
        nold_tablefar_pos

    show night05_hotel_hall_reception_table_comp far_01:
        truecenter
        zoom 0.5

    show nold_hands:
        nold_body_align
        nold_tablefar_pos

    with fade

    n "Justo detr??s de la barra de recepci??n,"

    if music_play != "crimson_waltz":
        play music "audio/music/alcaknight/crimson_waltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "crimson_waltz"

    n "aparece la figura decr??pita de una anciana vestida con harapos,"

    n "de lo que alg??n d??a fue una recepcionista de un hotel de lujo,"

    n "con una expresi??n de terror absoluto."

    p "????Qu??...?!"

    scene night05_hotel_hall_reception_blur:
        truecenter
        zoom 1.0

    show nold_body_hotel:
        nold_body_align
        nold_centerclose_pos

    show nold_exp_eyes 03:
        nold_expression_align
        nold_centerclose_pos

    show nold_exp_piris front03:
        nold_expression_align
        nold_centerclose_pos

    show nold_exp_eyebrows angryx03:
        nold_expression_align
        nold_centerclose_pos

    show nold_exp_mouth sad_Talkingx03:
        nold_expression_align
        nold_centerclose_pos

    show nold_nose:
        nold_expression_align
        nold_centerclose_pos

    show nold_exp_glasses:
        nold_expression_align
        nold_centerclose_pos

    show nold_overhead:
        nold_body_align
        nold_centerclose_pos

    with fade

    adn "????Acaso no eres consciente de d??nde demonios te has metido?!"

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows angryx02
    show nold_exp_mouth sad_Talkingx04
    with dissolve

    adn "??L??rgate de aqu?? antes de que sea demasiado tarde!"

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Silentx03
    with dissolve

    p "Pe..."

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx01
    show nold_exp_mouth sad_Silentx02
    with dissolve

    extend " Pero..."

    show nold_exp_eyes 07
    show nold_exp_piris front07
    show nold_exp_eyebrows sadx01
    show nold_exp_mouth sad_Silentx01
    with dissolve

    p "??Por qu???"

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx02
    show nold_exp_mouth sad_Silentx02
    with dissolve

    p "????No era esto un castillo de fantas??a para ni??os?!"

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx04
    show nold_exp_mouth sad_Talkingx03
    with dissolve

    adn "????Acaso te parece esto un castillo?!"

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx02
    show nold_exp_mouth sad_Silentx02
    with dissolve

    pt "Desde luego que no..."

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx03
    show nold_exp_mouth sad_Silentx02
    with dissolve

    pt "??Y no me ha dicho ese tipo que no ten??a que hablar con nadie?"

    pt "Todo esto debe de tratarse de un sue??o o algo..."

    pt "est?? siendo todo demasiado extra??o..."

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Talkingx01
    with dissolve

    adn "Ser?? mejor que te vayas de aqu??,"

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows sadx03
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn "antes de que te vea la jefa..."

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Silentx02
    with dissolve

    p "??La jefa?"

    show nold_exp_eyes 01
    show nold_exp_piris left01
    show nold_exp_eyebrows sadx03
    show nold_exp_mouth sad_Talkingx01
    with dissolve

    adn "Entre los interminables pasadizos,"

    show nold_exp_eyes 03
    show nold_exp_piris left03
    show nold_exp_eyebrows sadx03
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn "e innumerables puertas que hay en este hotel;"

    show nold_exp_eyes 01
    show nold_exp_piris left01
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Talkingx03
    with dissolve

    adn "se encuentran las pobres e infelices almas"

    show nold_exp_eyes 01
    show nold_exp_piris left01
    show nold_exp_eyebrows angryx01
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn "que cayeron en sus manos o sus encantos,"

    show nold_exp_eyes 01
    show nold_exp_piris left01
    show nold_exp_eyebrows sadx01
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn "junto con sus recuerdos,"

    show nold_exp_eyes 03
    show nold_exp_piris left03
    show nold_exp_eyebrows sadx03
    show nold_exp_mouth sad_Talkingx01
    with dissolve

    adn " sus gritos,"

    show nold_exp_eyes 05
    show nold_exp_piris front05
    show nold_exp_eyebrows sadx04
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn " sus llantos..."

    show nold_exp_eyes 03
    show nold_exp_piris left03
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Talkingx01
    with dissolve

    adn "Repitiendo y reviviendo una y otra vez"

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows serious
    show nold_exp_mouth sad_Talkingx02
    with dissolve

    adn "el error que una vez cometieron,"

    show nold_exp_eyes 03
    show nold_exp_piris left03
    show nold_exp_eyebrows sadx02
    show nold_exp_mouth sad_Talkingx03
    with dissolve

    adn "y que ya nunca m??s podr??n cambiar."

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows normal
    show nold_exp_mouth sad_Silentx02
    with dissolve

    p "??De qu?? est??s hablando?"

    show nold_exp_eyes 03
    show nold_exp_piris front03
    show nold_exp_eyebrows angryx02
    show nold_exp_mouth sad_Talkingx03
    with dissolve

    adn "{size=42}??HUYE!{/size}"

    show nold_exp_eyes 01
    show nold_exp_piris front01
    show nold_exp_eyebrows angryx05
    show nold_exp_mouth sad_Talkingx04
    with dissolve

    adn "??HUYE INSENSATO!"

    scene night05_hotel_hall_reception_comp far_02:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.09 ypos 0.35
        ease_quad 5.0 zoom 1.0 xpos 0.5 ypos 0.5

    n "Su rostro retorcido con esos ojos tan extra??os y ese grito desgarrador te impulsa levemente hacia atr??s,"

    play sound "audio/sfx/hit02.ogg"

    show night05_hotel_hall_reception_comp far_03:
        easein_bounce 0.3 zoom 1.1 xpos 0.5 ypos 0.5
    with vpunch

    n "hasta que en tu espalda, a la altura de tus hombros,"

    show night05_hotel_hall_reception_comp far_04
    with dissolve

    n "sientes el tacto de dos protuberancias esponjosas de un tama??o considerable."

    p "??Euh?"

    if music_play != "Sinfonia":
        play music "audio/music/alcaknight/Sinfonia.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "Sinfonia"

    scene nadult_encounter_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0 ypos -1.4 ## Boobs
        easein 15.0 zoom 1.0 xpos 0.5 ypos 0.2 # Face
        ease 10.0 zoom 0.3 xpos 0.57 ypos 0.225 # General
    with fade

    n "Detr??s de ti se encuentra una enorme mujer,"

    n "de melena lisa y oscura, con unos senos enormes,"

    n "con unas caderas de v??rtigo, unas facciones estilizadas,"

    n "maquillada de negro tanto en ojos como en labios,"

    n "vistiendo un traje largo con escote de infarto."

    n "y con unos ojos verde esmeralda."

    adn "??Jefa!"

    window hide dissolve
    pause
    
    # Her mouth talking.

    scene black
    with fade

    md01 "??Esas son maneras de tratar a un cliente?"

    rec "??Le pido que me perdone!"

    # Here comes how she touches your face with her hand.

    scene black
    with fade

    n "Su mano pasa gr??cilmente cerca de tu mejilla,"

    n "lo que te permite observar las u??as de sus dedos pintadas de color oscuro."

    n "Al mismo tiempo que tienes sus pechos justo enfrente de tu rostro."

    pt "Esta voz,"

    extend " este olor..."

    pt "Es el mismo de Neus..."

    md01 "Espero que disculpe la incompetencia de nuestra recepcionista."

    scene night05_hotel_hall_reception_comp far_01:
        truecenter
        zoom 0.5

    show nold_body_hotel:
        nold_body_align
        nold_tablefar_pos

    show nold_exp_eyes 03:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_piris left03:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_eyebrows sadx02:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_mouth sad_Silentx02:
        nold_expression_align
        nold_tablefar_pos

    show nold_nose:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_glasses:
        nold_expression_align
        nold_tablefar_pos

    show nold_overhead:
        nold_body_align
        nold_tablefar_pos

    show night05_hotel_hall_reception_table_comp far_01:
        truecenter
        zoom 0.5

    show nold_hands:
        nold_body_align
        nold_tablefar_pos

########################

    show nadult_body_hotel:
        nadult_body_align
        nadult_center_pos

    show nadult_body_hotel_bright:
        nadult_body_align
        nadult_center_pos
        additive 1.0

    show nadult_exp_eyebrows normal:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_eyes 03:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_piris front03:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_mouth happy_Talkingx03:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_hair_front:
        nadult_expressions_align
        nadult_center_pos

    with fade

    md01 "Soy la gerente de este hotel,"

    show nadult_exp_eyebrows surprisex02
    show nadult_exp_eyes 02
    show nadult_exp_piris front02
    show nadult_exp_mouth happy_Talkingx04
    with dissolve

    ghm "y le doy la bienvenida."

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth happy_Silentx03
    with dissolve

    p "Euh..."

    show nadult_exp_eyebrows normal
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth happy_Silentx04
    with dissolve

    p "Yo..."

    scene black
    with fade

    n "Con un chasquido de sus dedos,"

    scene night05_hotel_hall_reception_comp far_01:
        truecenter
        zoom 0.5

    # nold

    show nold_body_hotel:
        nold_body_align
        nold_tablefar_pos

    show nold_exp_eyes 03:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_piris left03:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_eyebrows sadx03:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_mouth sad_Silentx02:
        nold_expression_align
        nold_tablefar_pos

    show nold_nose:
        nold_expression_align
        nold_tablefar_pos

    show nold_exp_glasses:
        nold_expression_align
        nold_tablefar_pos

    show nold_overhead:
        nold_body_align
        nold_tablefar_pos

    show night05_hotel_hall_reception_table_comp far_01:
        truecenter
        zoom 0.5

    show nold_hands:
        nold_body_align
        nold_tablefar_pos

    ## bellhop

    show bellhop_arm_r_back relax:
        bellhop_body_align
        bellhop_atleft_pos

    show bellhop_arm_l_back relax:
        bellhop_body_align
        bellhop_atleft_pos

    show bellhop_body:
        bellhop_body_align
        bellhop_atleft_pos

    show bellhop_exp_mouth sad_Silentx02:
        bellhop_expressions_align
        bellhop_atleft_pos

    show bellhop_exp_hat down:
        bellhop_expressions_align
        bellhop_atleft_pos

########################
    
    ## nadult

    show nadult_body_hotel:
        nadult_body_align
        nadult_center_pos

    show nadult_body_hotel_bright:
        nadult_body_align
        nadult_center_pos
        additive 1.0

    show nadult_exp_eyebrows angryx02:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_eyes 03:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_piris front03:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_mouth happy_Silentx05:
        nadult_expressions_align
        nadult_center_pos

    show nadult_exp_hair_front:
        nadult_expressions_align
        nadult_center_pos
    with dissolve

    n "aparece el mismo botones que te hab??a recibido al llegar a este lugar tan oscuro,"

    n "justo detr??s de ella."

    show nadult_exp_eyebrows surprisex02
    show nadult_exp_eyes 07
    show nadult_exp_piris front07
    show nadult_exp_mouth happy_Talkingx04
    with dissolve

    ghm "Por favor,"

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth happy_Talkingx03
    with dissolve

    ghm "llame al ascensor para llevar a este caballero tan apuesto"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 02
    show nadult_exp_piris front02
    show nadult_exp_mouth happy_Talkingx05
    with dissolve

    ghm "a los aposentos a los que debe dirigirse."

    hide bellhop_arm_r_back
    hide bellhop_arm_l_back
    hide bellhop_body
    hide bellhop_exp_mouth
    hide bellhop_exp_hat
    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Silentx04 
    with dissolve

    p "Pero..."

    extend " yo..."

    show nadult_exp_eyebrows normal
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth sad_Silentx03 
    with dissolve

    p "??No deseo hospedarme en este hotel!"

    # Close shot to nadult

    scene night05_hotel_hall_reception_blur:
        truecenter
        zoom 1.5 rotate 90 ypos 0.5

########################
    
    ## nadult

    show nadult_body_hotel:
        nadult_body_align
        nold_centerclose_pos
    show nadult_body_hotel_bright:
        nadult_body_align
        nold_centerclose_pos
        additive 1.0

    show nadult_exp_eyebrows angryx02:
        nadult_expressions_align
        nold_centerclose_pos

    show nadult_exp_eyes 07:
        nadult_expressions_align
        nold_centerclose_pos

    show nadult_exp_piris front07:
        nadult_expressions_align
        nold_centerclose_pos

    show nadult_exp_mouth sad_Silentx05 :
        nadult_expressions_align
        nold_centerclose_pos

    show nadult_exp_hair_front:
        nadult_expressions_align
        nold_centerclose_pos

    with fade

    ghm "..."

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Talkingx03
    with dissolve

    ghm "Desde luego que no."

    show nadult_exp_eyebrows normal
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth sad_Talkingx02
    with dissolve

    ghm "Nadie en su sano juicio lo desear??a."

    show nadult_exp_eyebrows surprisex02
    show nadult_exp_eyes 06
    show nadult_exp_piris front06
    show nadult_exp_mouth happy_Talkingx05
    with dissolve

    ghm "Pero t?? no est??s aqu?? para hospedarte,"

    extend "\nquerido."

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth happy_Silentx05
    with dissolve

    p "..."

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Talkingx05
    with dissolve

    ghm "Cuando subas al ascensor,"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Talkingx06
    with dissolve

    ghm "este te llevar?? a un piso en el que encontrar??s tres puertas."

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 02
    show nadult_exp_piris front02
    show nadult_exp_mouth sad_Talkingx04
    with dissolve

    ghm "Puedes empezar por la que desees..."

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Talkingx05
    with dissolve

    ghm "O tambi??n puedes optar por elegir la salida de emergencia y abandonar de este lugar."

    show nadult_exp_eyebrows normal
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth sad_Silentx04
    with dissolve

    p "??Realmente tengo esa opci??n?"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 07
    show nadult_exp_piris front07
    show nadult_exp_mouth sad_Talkingx06
    with dissolve

    ghm "Por supuesto."

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 05
    show nadult_exp_piris front05
    show nadult_exp_mouth sad_Talkingx05
    with dissolve

    ghm "Lo que hay detr??s de esas puertas"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth happy_Talkingx05
    with dissolve

    ghm "es algo que te permitir?? entender mejor a esa chica que parece tan inocente,"

    show nadult_exp_eyebrows normal
    show nadult_exp_eyes 02
    show nadult_exp_piris front02
    show nadult_exp_mouth happy_Talkingx06
    with dissolve

    ghm "pero si prefieres vivir en la ignorancia,"

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 03
    show nadult_exp_piris front03
    show nadult_exp_mouth sad_Talkingx06
    with dissolve

    ghm "o tienes demasiado miedo para afrontar la verdad;"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth sad_Talkingx04
    with dissolve

    ghm "es tu elecci??n."

    show nadult_exp_eyebrows serious
    show nadult_exp_eyes 04
    show nadult_exp_piris front04
    show nadult_exp_mouth sad_Silentx05
    with dissolve

    p "..."

    show nadult_exp_eyebrows surprisex02
    show nadult_exp_eyes 05
    show nadult_exp_piris front05
    show nadult_exp_mouth happy_Talkingx06
    with dissolve

    ghm "Suerte."

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"

    show nadult_exp_eyebrows angryx02
    show nadult_exp_eyes 01
    show nadult_exp_piris front01
    show nadult_exp_mouth happy_Silentx06
    with dissolve

    scene night05_hotel_hall_reception_blur:
        truecenter
        zoom 1.5 rotate 90 ypos 0.5

    with Dissolve (2.0)

    p "????Euh?!"

    n "Como si de un espectro se tratara,"

    n "desaparece de tu vista."

    scene night05_hotel_hall_reception_comp far_01:
        truecenter
        zoom 0.5
    with fade

    n "Al observar tu entorno, te percatas de que la recepcionista tampoco est?? en su lugar."

    scene night05_hotel_hall_comp 03:
        truecenter
        zoom 0.5
    with fade

    n "Las velas se apagan y el lugar empieza a oscurecerse."

    scene night05_hotel_hall_comp 04:
        truecenter
        zoom 0.5
    with dissolve

    n "a excepci??n de la luz que procede del interior del elevador."

    bo "Cuando lo desee el caballero."

    n "Donde se encuentra el botones esper??ndote."

    pt "Parece que tampoco tengo demasiadas opciones..."

    show night05_hotel_hall_comp 05:
        subpixel True
        zoom 0.5 xpos 0.5 ypos 0.5 # far
        ease 10.0 zoom 1.5 xpos 0.55 ypos 0.25 # Close
    with dissolve

    n "Lo acompa??as en el interior del reducido habit??culo,"

    n "y a los pocos segundos de haber entrado,"

    stop music fadeout 3.0
    $ music_play = ""

    scene bg black
    show night05_hotel_hall_elevator_door_l:
        subpixel True
        truecenter
        zoom 0.5 xpos -0.02 ypos 0.5
        ease_quad 10.0 xpos 0.5
    show night05_hotel_hall_elevator_door_r:
        subpixel True
        truecenter
        zoom 0.5
        zoom 0.5 xpos 1.02 ypos 0.5
        ease_quad 10.0 xpos 0.5

    show  white:
        additive 1.0 alpha 1.0
        pause 0.5
        easein_quad 5.0 alpha 0.0
    with fade

    n "cierra sus puertas,"

    n "para luego presionar el bot??n que eleva el ascensor a un piso superior."

    $ saturation_tint_level = "default"

    n "Durante unos segundos reina un silencio inc??modo,"

    if music_play != "elevator_music":
        play music "audio/music/others/elevator_music.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "elevator_music"

    n "hasta que empieza a sonar una m??sica disonante con la situaci??n..."

    n "que no ayuda en absoluto a relajar el ambiente."

    n "Por suerte,"

    with vpunch

    n "al poco tiempo, este se detiene y sus puertas vuelven a abrirse de nuevo."

    scene night05_hotel_bg_doors3_a_far:
        truecenter
        zoom 0.5
    show night05_hotel_hall_elevator_door_l:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease_quad 10.0 xpos 0.0

    show night05_hotel_hall_elevator_door_r:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease_quad 10.0 xpos 1.0
    with dissolve

    n "En frente, como bien dijo la mujer despampanante,"

    n "se encuentra de nuevo un lugar reinado completamente por la oscuridad,"

    n "a excepci??n de una pared con tres puertas en ella."

    bo "Esta es su parada,"

    extend " caballero."

    p "..."

    stop music fadeout 6.0
    $ music_play = ""

    scene black:
        zoom 2.0
    show night05_hotel_bg_doors3_a_far:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -0.8
        easein_quad 15.0 zoom 0.75 xpos 0.5 ypos 0.5
    with fade

    n "Cautelosamente sales del ascensor, pisando un suelo que eres incapaz de vislumbrar,"

    n "como si la luz no pudiera reverberar en ninguna otra parte que no fuera en ese rinc??n,"

    n "y en el resto solo existiera el vac??o."

    $ saturation_tint_level = "default"

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    bo "Recuerda."

    scene bellhop_afterelevator_comp sad_Silent:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos -0.2 # Down
        easein_quad 10.0 zoom 0.7 xpos 0.5 ypos 0.3 # Face Talk

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        pause 0.5
        ease 2.0 alpha 0.0
    with fade

    p "??Euh?"

    show bellhop_afterelevator_comp sad_Talkingx03
    with dissolve

    bo "Lo ??nico que te ofrezco es {a=https://es.wikipedia.org/wiki/The_Matrix}la verdad{/a},"

    show bellhop_afterelevator_comp sad_Talkingx02
    with dissolve

    bo "nada m??s."

    show bellhop_afterelevator_comp happy_Silentx02
    with dissolve

    pause 1.0

    show bellhop_afterelevator_comp happy_Silentx02_eyes
    with dissolve

    window hide dissolve
    pause 1.0

    show night05_hotel_hall_elevator_door_d_l:
        subpixel True
        truecenter
        zoom 0.5 xpos -0.05 ypos 0.5
        easein_quad 5.0 xpos 0.5

    show night05_hotel_hall_elevator_door_d_r:
        subpixel True
        truecenter
        zoom 0.5 xpos 1.05 ypos 0.5
        easein_quad 5.0 xpos 0.5

    n "Las puertas del elevador se van cerrando,"

    show black02:
        truecenter
        alpha 0.0
        ease_quad 5.0 alpha 1.0

    n  "hasta que se funde en la oscuridad."

    p "Esos ojos rojos,"

    extend " eran algo distintos..."

    stop music fadeout 3.0
    $ music_play = ""

    scene night05_hotel_bg_doors3_a_far:
        truecenter
        zoom 0.75
    with fade

    n "Diriges de nuevo tu vista hacia esa extra??a pared con tres puertas."

    n "Te percatas de que en estas hay unos n??meros,"

    n "que de forma inexplicable,"

    n "van cambiando de cifra."

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"

    show night05_hotel_bg_doors3_a_far:
        subpixel True
        ease_quad 15.0 zoom 1.25
    with dissolve

    pt "??Qu?? diablos...?"

    n "A medida que te vas acercando,"

    n "observas tambi??n, que en la parte superior derecha,"

    n "se encuentra el s??mbolo de salida de emergencia."

    p "..."

    p "Ser??a mejor no optar por esa opci??n a??n..."

    if night05_Interrogation_WhatIsYourFather_Cond == True:

        pt "??Ser?? realmente el padre de Neus el que me est?? haciendo ver todo esto...?"

        pt "Pero..."

        pt"??Por qu??...?"

        pt "????Por qu?? no me mata y se ahorra toda esta estupidez?!"

        pt "????Qu?? es lo que quiere que vea?!"

        pt "??Y c??mo sabr?? que lo que me ense??a en realidad no es m??s que una burda mentira?"

        p "Tampoco estoy muy seguro de que sea tan f??cil salir de aqu??..."

        p "y en cualquier caso,"

        p "debo confesar que realmente tengo curiosidad de saber qu?? hay detr??s de estas puertas."

        p "Al fin y al cabo,"

        p "si realmente me quisiera muerto,"

        extend " o loco,"

        p "no necesitar??a pedirme permiso..."

        p "est?? claro que tiene un control absoluto de este lugar,"

        p "y yo no soy m??s que un t??tere en su juego..."

    #########################################################
    
    if config.version < "00.12.01": # Beginning of Hotel.
        
        call endupdatescript
    
    #######################################################

label night05_NeusLastDate_HotelKrueger_Door_General:



    #if ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond == True) and
        #(night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == True) and
        #(night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == True)):

        #scene black
        #with fade

        #n "He visitado todas las puertas!"

        #jump night05_NeusLastDate_After_HotelKrueger

    scene night05_hotel_bg_doors3_a_close_original:
        truecenter
        zoom 0.5

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond == True:
        show night05_hotel_bg_doors3_a_close_01:
            truecenter
            zoom 0.5
    if night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == True:
        show night05_hotel_bg_doors3_a_close_02:
            truecenter
            zoom 0.5
    if night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == True:
        show night05_hotel_bg_doors3_a_close_03:
            truecenter
            zoom 0.5
    with dissolve

    if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 0:

        $ renpy.music.stop(channel='sfx1', fadeout=3.0)
        $ renpy.music.stop(channel='sfx2', fadeout=3.0)
        $ renpy.music.stop(channel='sfx3', fadeout=3.0)
        $ renpy.music.stop(channel='sfx4', fadeout=3.0)
        $ renpy.music.stop(channel='sfx5', fadeout=3.0)
        stop music fadeout 3.0
        $ music_play = ""

    if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 1:

        if music_play != "vanishing":
            play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "vanishing"

        p "..."

        pt "??Qu?? diablos...?"

        pt "No solo la puerta ya no se abre,"

        pt "sino que adem??s,"

        extend " esa sangre..."

    elif night05_NeusLastDate_HotelKrueger_Door_Used_Number == 2:

        if music_play != "ossuary_6_air":
            play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "ossuary_6_air"

        pt "Otra vez aqu??,"

        pt "con la puerta cerrada,"

        extend " y de nuevo manchada de sangre..."

    elif night05_NeusLastDate_HotelKrueger_Door_Used_Number == 3:

        if music_play != "welcome_to_horror_land":
            play music "audio/music/kevinmacleod/welcome_to_horror_land.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "welcome_to_horror_land"

        p "..."

        show black:
            alpha 0.0
            ease 10.0 alpha 1.0

        pt "Las tres puestas est??n cubiertas de sangre..."

        pt "????Y ahora qu???!"

        pt "????Tengo que ver alguna chorrada m??s?!"

        pt "??Esto es absurdo!"

        pt "??Qu?? diablos ha sido todo esto?"

        pt "????C??mo s?? que todo esto no es m??s que una est??pida fantas??a tuya?!"

        pt "????Por qu?? deber??a creer nada de lo que he visto?!"

        dad "No lo hagas."

        p "..."

        dad "Simplemente,"

        extend " recuerda."

        p "..."

        dad "Disfruta de tu cita,"

        dad "al menos lo que queda de ella..."

        show black
        with dissolve

        p "..."

        jump night05_NeusLastDate_After_HotelKrueger



    p "..."

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond_Temp == True:

        $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond_Temp = False

        if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_family_met_Cond == True:

            pt "Si lo de esa mujer es cierto,"

            pt "qu?? modo m??s horrible de perder a un hijo..."

        else:

            pt "Ese cementerio me ha dado escalofr??os..."

    if night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp == True:

        $ night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp = False

        if room_02_child_room_but_kid_Cond == True:

            pt "El padre de ese ni??o deb??a de ser el de las fotos del pasillo..."

            pt "y esa mujer tan tetuda de los dibujos..."

        else:

            pt "Me pregunto si realmente hab??a un ni??o bajo esa s??bana..."

    if night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp == True:

        $ night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp = False

        pt "Espero que si alg??n d??a me caso,"

        extend "\nno acabe igual la cosa..."

    hide screen quick_menu 
    with dissolve
    call screen night05_hotel_doors3_screen()


####################################################################################################
################################################################################################## BABY

####################################################################################################
##################################################################################################

####################################################################################################
##################################################################################################

label night05_NeusLastDate_HotelKrueger_Door_Baby:

    menu night05_NeusLastDate_HotelKrueger_Door_Baby_Quesiton:
            
        pt "??Seguro que quiero tomar esta puerta?"

        "S??.":

            #########################################################
    
            if config.version < "00.12.02": # Before First Door.
                
                call endupdatescript
            
            #######################################################
            
            call p_Help

            $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond = True
            $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond_Temp = True
            $ night05_NeusLastDate_HotelKrueger_Door_Used_Number += 1

            jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Gate

        "No":

            call p_Help

            hide screen quick_menu 
            with dissolve
            call screen night05_hotel_doors3_screen()
            with fade_long1s

label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Gate:

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/ambient_cemetery.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    scene black
    with fade_long1s

    if ((night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False) and 
        (night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == False)):

        pt "Esto est?? completamente a oscuras."

        pt "Pens?? que ten??a que seguir la luz..."

    else:

        pt "Como era de esperar,"

        pt "tambi??n est?? a oscuras."

    $ saturation_tint_level = "verydark"

    scene bg room_01_cemetery_gate_bg
    show night05_Cemetery_smoke_comp
    with fade_long1s # Make a conditional for this LONG fade, if you already had one of the tombs visited.

    pt "????Estoy en un cementerio?!"

    $ renpy.music.set_volume(0.2, delay=20.0, channel='sfx1')

    show black
    with fade

    n "Retuerces el cuello para mirar atr??s."

    if ((night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False) and
        (night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == False)):

        pt "La puerta ha desaparecido y solo queda la oscuridad..."

    else:

        pt "Tampoco puedo volver..."

    hide night05_Cemetery_smoke_comp
    hide bg

    pt "Supongo que no tengo otra opci??n que entrar..."

    #$ quick_menu = False ## JUST TO TAKE IN MIND THE OPTION.
    hide screen quick_menu
    with dissolve
    call screen night05_hotel_doors3_Cemetery_Gate_screen()
    

label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far_Beginning: #Only the beginning

    $ renpy.music.set_volume(0.1, delay=1.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/crying_woman01_far.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.03, delay=6.0, channel='sfx2')

    scene bg room_01_cemetery_far_bg
    show night05_Cemetery_smoke_comp
    with fade_long1s

    window hide dissolve
    pause

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    #$ saturation_tint_level = "verydark"

    pt "??Qu?? demonios...?"

    n "El triste llanto de una mujer a lo lejos,"

    n "al lado de una diminuta cripta,"

    n "donde ves una puerta sospechosamente semiabierta emanando una potente luz de su interior,"

    n "rompe el silencio y la tranquilidad del lugar."

    n "Te encuentras rodeado de sepulcros de un tama??o aparentemente reducido,"

    n "en lo que parece un {a=https://es.wikipedia.org/wiki/Cementerio}camposanto{/a} bastante f??nebre y envuelto en una espesa niebla."

    pt "Parece que el lugar est?? bastante descuidado..."

    pt "??Y qu?? son todas estas cosas al lado de las tumbas?"

    p "Hmm..."

    pt "Quiz??s podr??a echarles un ojo antes de ir hasta all?? al fondo..."

    pt "Mucho me temo que luego no podr?? volver atr??s."

    pt "Aunque desde luego,"

    extend " esto no tiene buena pinta..."

    hide screen quick_menu
    with dissolve
    call screen night05_hotel_doors3_Cemetery_Far_screen()

label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far:

    if (night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_01_Cond == True and 
        night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_02_Cond == True and 
        night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_03_Cond == True and 
        night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_04_Cond == True and 
        night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_05_Cond == True and 
        night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_06_Cond == True):

            $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_All_Cond = True

    scene bg room_01_cemetery_far_bg
    show night05_Cemetery_smoke_comp
    with fade

    hide screen quick_menu
    with dissolve
    call screen night05_hotel_doors3_Cemetery_Far_screen()
    
label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close:

    $ renpy.music.set_volume(0.4, delay=20.0, channel='sfx2')

    scene bg room_01_cemetery_close_open_comp:
        truecenter
    with fade_long1s

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    pt "Estoy bastante cerca."

    pt "No parece que me est??n haciendo caso..."

    pt "Podr??a usar la puerta y salir de este lugar,"

    pt "o acercarme a ellos y averiguar qu?? diablos est?? pasando."

label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Choose:

    hide screen quick_menu
    with dissolve
    call screen night05_hotel_room01_cemetery_close_doorout_screen()

label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Out:

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    menu night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Question:

        pt "Si salgo, seguramente no podr?? volver..."

        "??He dicho que me largo de aqu??!":
            jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Out_GettingOut

        "Quiz??s a??n no...":
            jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Choose


label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Out_GettingOut:

    pt "??Al carajo!"

    show bg:
        easein_quad 5.0 zoom 2.0 xpos 0.2 ypos 0.8

    pt "??Me largo de aqu??!"

    show white:
        additive 1.0
        alpha 0.0
        easein_quad 1.0 alpha 1.0

    show black:
        alpha 0.0
        pause 1.0
        easein_quad 1.0 alpha 1.0

    pause

    jump night05_NeusLastDate_HotelKrueger_Door_General


label night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close_Couple:

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/crying_woman01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.8, delay=6.0, channel='sfx2')

    scene bg room_01_cemetery_closer_bg
    show room_01_cemetery_closer_body
    show room_01_cemetery_closer_head down
    show night05_Cemetery_smoke_comp:
        truecenter
        ypos 0.85
    show room_01_cemetery_closer_light:
        additive 1.0
        light_flame_animation
    
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_family_met_Cond = True

    $ room_01_cemetery_mother_met_Cond = True # This one should be the one used in the future, previous one is too long.

    n "Te acercas con precauci??n a apenas unos cent??metros de ellos."

    window hide dissolve
    pause 0.5

    show room_01_cemetery_closer_head camera
    with Dissolve(2.0)

    h01 "Disculpe joven,"

    show room_01_cemetery_closer_head down
    with dissolve_05s

    h01 "lamento mucho las molestias por el ruido."

    show room_01_cemetery_closer_head camera
    with dissolve

    h01 "Pero debe entender que no es nada f??cil perder a un hijo,"

    show room_01_cemetery_closer_head down
    with dissolve

    h01 "cuando apenas quedaba una semana para cumplir los nueve meses de embarazo..."

    show room_01_cemetery_closer_head camera
    with dissolve

    h01 "especialmente,"

    show room_01_cemetery_closer_head down
    with dissolve

    h01 "despu??s hallar a mi mujer completamente ensangrentada en la cama,"

    h01 "sin ning??n rastro de nuestro..."

    n "Sus palabras -entrecortadas por el estremecimiento y el sollozo-, apenas le permiten hablar."

    h01 "Llorar la tumba vac??a de un hijo no nato..."

    h01 "no poder darle un entierro digno,"

    extend " es..."

    h01 "algo que no le deseo ni a mi peor enemigo..."

    h01 "??Qu?? clase de monstruo es capaz de hacer semejante cosa?"

    p "..."

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    play sound "audio/sfx/hit02.ogg"

    scene bg dark_a_blurry_01

    show room_01_cemetery_mother_body:
        truecenter_05
    show room_01_cemetery_mother_exp_eyes 02:
        truecenter_05
    show room_01_cemetery_mother_exp_tears 02_05:
        truecenter_05
    show room_01_cemetery_mother_exp_mouth sad_Talkingx04:
        truecenter_05
    show room_01_cemetery_mother_exp_eyebrows sadx01:
        truecenter_05
    show room_01_cemetery_mother_veil:
        truecenter_05
    show room_01_cemetery_husband_hand empty:
        truecenter_05
    show room_01_cemetery_mother_hands:
        truecenter_05
        shake_hands
    #show night05_Cemetery_smoke_comp:
        #truecenter
        #ypos 1.2
        #alpha 0.5
    with vpunch

    m01 "????Sabes qui??n ha sido?!"

    show room_01_cemetery_mother_exp_eyes 04
    show room_01_cemetery_mother_exp_tears 04_05
    show room_01_cemetery_mother_exp_mouth sad_Talkingx05
    show room_01_cemetery_mother_exp_eyebrows sadx03
    with dissolve_05s

    m01 "????D??nde est?? mi hijo?!"

    show room_01_cemetery_mother_exp_eyes 06
    show room_01_cemetery_mother_exp_tears 06_05
    show room_01_cemetery_mother_exp_mouth sad_Silentx07
    show room_01_cemetery_mother_exp_eyebrows sadx04
    with dissolve

    h01 "Querida..."

    if (room_02_child_room_but_kid_Cond and room_03_marriage_far_woman_Cond) == True:

        pt "Tiene los mismos ojos que en los dos casos anteriores..."

    elif room_02_child_room_but_kid_Cond == True:

        pt "Tiene los mismos ojos que ese ni??o..."

    elif room_03_marriage_far_woman_Cond == True:

        pt "Tiene los mismos ojos que la viuda llorosa..."

    else:

        pt "??Qu?? le pasa en los ojos?"

    show room_01_cemetery_mother_exp_eyes 04
    show room_01_cemetery_mother_exp_tears 04_05
    show room_01_cemetery_mother_exp_mouth sad_Talkingx03
    show room_01_cemetery_mother_exp_eyebrows sadx05
    with dissolve

    m01 "??Por favor!"

    show room_01_cemetery_mother_exp_eyes 06
    show room_01_cemetery_mother_exp_tears 06_05
    show room_01_cemetery_mother_exp_mouth sad_Talkingx04
    show room_01_cemetery_mother_exp_eyebrows sadx03
    with dissolve

    m01 "??Al menos d??jame poder enterrarlo!"

    show room_01_cemetery_mother_exp_eyes 07
    show room_01_cemetery_mother_exp_tears 07_05
    show room_01_cemetery_mother_exp_mouth sad_Silentx05
    show room_01_cemetery_mother_exp_eyebrows sadx04
    show room_01_cemetery_husband_hand
    with dissolve_05s

    h01 "Tranquil??zate..."

    show room_01_cemetery_mother_exp_eyes 06
    show room_01_cemetery_mother_exp_tears 06_05
    show room_01_cemetery_mother_exp_mouth sad_Talkingx03
    show room_01_cemetery_mother_exp_eyebrows sadx02
    with dissolve

    m01 "Por favor..."

    show room_01_cemetery_mother_exp_eyes 05
    show room_01_cemetery_mother_exp_tears 05_05
    show room_01_cemetery_mother_exp_mouth sad_Silentx05
    show room_01_cemetery_mother_exp_eyebrows sadx05
    with dissolve

    h02 "??Hijo...?"

    show room_01_cemetery_mother_exp_eyes 02
    show room_01_cemetery_mother_exp_tears 02_05
    show room_01_cemetery_mother_exp_mouth sad_Silentx03
    show room_01_cemetery_mother_exp_eyebrows normal
    show room_01_cemetery_mother_hands:
        truecenter_05
    with dissolve_1s

    h02 "??Eres t??...?"

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(0.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/whispers_creepy01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.2, delay=15.0, channel='sfx2')

    scene black
    show night05_Cemetery_smoke_comp:
        truecenter
        ypos 1.2
    with fade

    n "R??pidamente levantas la cabeza para mirar de d??nde viene esa voz."

    m02 "??Cari??o!"

    m02 "????Est??s ah???!"

    $ renpy.music.set_volume(0.4, delay=15.0, channel='sfx2')

    n "Poco a poco el lugar se va oscureciendo."

    scene bg dark_a_blurry_01
    show night05_Cemetery_smoke_comp:
        truecenter
        ypos 1.2
    with fade

    n "Y la pareja que sollozaba ante la tumba del no nacido ha desaparecido por completo."

    h02 "Tu madre est?? muy preocupada."

    scene black
    show night05_Cemetery_smoke_comp:
        truecenter
        ypos 1.2
    with fade

    $ renpy.music.set_volume(0.8, delay=15.0, channel='sfx2')

    h02 "Vuelve a casa..."

    h03 "??Te dije que no te alejaras!"

    pt "??Qu?? diablos es todo esto...?"

    m03 "??Cari??o!"

    h04 "??Solo te perd?? de vista un segundo!"

    m04 "Regresa a casa..."

    h05 "????Por qu?? no me hiciste caso?!"

    m05 "Te echo de menos..."

    n "Decenas de voces quebrantadas por el dolor y la p??rdida,"

    n "rompen el silencio que hab??a hasta el momento."

    n "Cada vez los oyes m??s, y m??s cerca,"

    play sound "audio/sfx/heartbeat_01.ogg"

    n "y tu coraz??n empieza a acelerarse."

    play sound "audio/sfx/heartbeat_01.ogg"

    n "Oyes sus gritos de desesperaci??n, sus llantos, sus s??plicas..."

    play sound "audio/sfx/heartbeat_01.ogg"

    $ renpy.music.stop(channel='sfx1', fadeout=10.0)
    $ renpy.music.stop(channel='sfx2', fadeout=8.0)

    scene black
    with fade_long1s

    window hide dissolve
    pause

    pt "??Qu?? demonios ha sido todo esto...?"
    

    # Continue Story here.

    #m01 "mujer desconocida"

    jump night05_NeusLastDate_HotelKrueger_Door_General

#####################################################
#####################################################

label room_01_cemetery_far_tomb_Visits_01:

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 1:

        pt "La tumba de un beb??..."

    elif night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 2:

        pt "Parece una tumba similar a la anterior..."

    return

    ##

label room_01_cemetery_far_tomb_Visits_02:

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 1:

        pt "En ella parece haber algo escrito..."

    elif night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 2:

        pt "Tambi??n hay una inscripci??n en ella..."

    else:

        pt "En la inscripci??n pone..."

    return


label room_01_cemetery_far_tomb_Visits_03:

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 1:

        pt "??Qu?? demonios...?"

    elif night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 2:

        pt "No parecen epitafios,"

        pt "son como los pensamientos de una madre cuando a??n ten??a el beb?? entre sus brazos..."

    elif night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number == 3:

        pt "Maldita sea..."

        pt "??Por qu?? me est?? ense??ando esto?"

    return

label room_01_cemetery_far_tomb_01_label:

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_01_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    #"01"

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry01.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    pt "Una silla de beb?? de madera..."

    pt "??Qu?? hace en un sitio como este?"

    call room_01_cemetery_far_tomb_Visits_01 # Description Tomb
    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}Por mucho que crezcas,"

    extend "\nsiempre ser??s mi beb??.{/i}"

    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_02_label:

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry02.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_02_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    #"02"

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    pt "Sin ninguna duda,"

    pt "es la cuna de un beb??."

    if night04_pedrera_blowjob_DONE == True:

        pt "Es parecida a la que vi en la habitaci??n de la Pedrera..."

    call room_01_cemetery_far_tomb_Visits_01 # Description Tomb
    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}Es incre??ble c??mo alguien tan peque??ito,"

    extend "\npuede hacerme sentir algo tan gigantesco.{/i}"

    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_03_label:

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry03.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_03_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    #"03"

    pt "Un osito de peluche,"

    pt "da un poco de grima."

    call room_01_cemetery_far_tomb_Visits_01 # Description Tomb
    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}Sin ti,"

    extend "\ntal vez mi casa estar??a limpia y mi billetera llena,{/i}"

    let "{i}pero mi coraz??n se encontrar??a totalmente vac??o.{/i}"

    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_04_label:

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry02.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_04_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    #"04"

    call room_01_cemetery_far_tomb_Visits_01 # Description Tomb

    pt "Esto parecen los adornos que se suelen usar para entretener al reci??n nacido en su cuna."

    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}Es probable que te lleve nueve meses en el vientre,"

    extend " quiz??s tres a??os en los brazos,{/i}"

    let "{i}pero de lo que estoy convencida,"

    extend "\nes que te llevar?? toda la vida en el coraz??n.{/i}"

    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_05_label:

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry03.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_05_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    #"05"

    #call room_01_cemetery_far_tomb_Visits_01 # Description Tomb

    pt "Dos tumbas tan juntas..."

    pt "Es probable que fueran mellizos reci??n nacidos..."

    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}No s?? si llegar?? a conocer el para??so,"

    extend "\npero si existe;{/i}"

    let "{i}seguro que no es tan bonito como ser la madre de este par de maravillas.{/i}"

    let "{i}Gracias.{/i}"

    let "{i}Gracias por todos estos momentos que me regal??is cada d??a.{/i}"
    
    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_06_label:

    $ renpy.music.set_volume(0.3, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/baby_ghost_cry01.ogg", channel="sfx3",loop=False, fadeout=0.5, synchro_start=True, fadein=0.5)

    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_06_Cond = True
    $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_Number += 1

    scene black
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    #"06"

    pt "Aparentemente es un carrito de beb??,"

    pt "pero parece como el que usaban a principios del siglo pasado..."

    call room_01_cemetery_far_tomb_Visits_01 # Description Tomb

    call room_01_cemetery_far_tomb_Visits_02 # Description Epitafio

    let "{i}No importa si estoy durmiendo,"

    extend "\nsi tengo problemas propios,"

    extend "\no si estoy enojada contigo.{/i}"

    let "{i}Si me necesitas,"

    extend " y necesitas hablar conmigo,"

    extend " siempre voy a estar ah?? para ti.{/i}"

    let "{i}no importa lo grande o peque??o que sea tu problema,{/i}"

    let "{i}ah?? estar?? para ti.{/i}"

    call room_01_cemetery_far_tomb_Visits_03 # After reading

    jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

label room_01_cemetery_far_tomb_family_label:

    if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_All_Cond == False:

        menu room_01_cemetery_far_tomb_family_Question:

            pt "Si voy all??, seguramente ya no podr?? volver."

            "Ir.":
                call p_Help

                $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_family_Cond = True

                jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close

            "A??n no.":
                call p_Help

                jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Far

    else:

        if PlatinumHelp == True:
            show screen quick_menu()
            with dissolve

        pt "Ahora solo me queda acercarme a los llantos que se oyen al fondo..."

        $ night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_far_tomb_family_Cond = True

        jump night05_NeusLastDate_HotelKrueger_Door_Baby_Cemetery_Close


####################################################################################################
################################################################################################## CHILDHOOD

####################################################################################################
##################################################################################################

####################################################################################################
##################################################################################################

label night05_NeusLastDate_HotelKrueger_Door_Childhood:

    menu night05_NeusLastDate_HotelKrueger_Door_Childhood_Quesiton:
        
        pt "??Seguro que quiero tomar esta puerta?"

        "S??.":

            #########################################################
    
            if config.version < "00.12.03": # Before Second Door.
                
                call endupdatescript
            
            #######################################################
            
            call p_Help

            $ night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond = True
            $ night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp = True
            $ night05_NeusLastDate_HotelKrueger_Door_Used_Number += 1

            jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Beginning

        "No":

            call p_Help

            hide screen quick_menu
            with dissolve
            call screen night05_hotel_doors3_screen()

label night05_NeusLastDate_HotelKrueger_Door_Childhood_Beginning:

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(0.8, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/rain_onCar.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.1, delay=30.0, channel='sfx1')

    $ renpy.music.set_volume(0.2, delay=0, channel='sfx2')
    $ renpy.music.play("audio/sfx/crying_boy01_far.ogg", channel="sfx2",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.05, delay=10.0, channel='sfx2')

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx3')
    $ renpy.music.play("audio/sfx/thunders01.ogg", channel="sfx3",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=30.0, channel='sfx3')

    scene black
    with fade_long1s

    $ saturation_tint_level = "superdark"

    pause 1.0

    pt "No veo nada..."

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx4')
    $ renpy.music.play("audio/sfx/thunders01.ogg", channel="sfx4",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=30.0, channel='sfx4')

    show room_02_child_hallway_bg_dark_lighting_comp:
        truecenter
        zoom 0.2
        alpha 0.0
        ease_quad 2.0 alpha 1.0

    window hide dissolve
    pause 2.0

    p "..."

    pt "Una noche de tormenta,"

    pt "un tanto clich??..."

    pt "pero,"

    extend " ??y estos juguetes por el suelo?"

    pt "aunque estos cuadros..."

    extend "\ntampoco se quedan muy atr??s..."

    pt "Me imagino que la salida es la puerta del fondo,"

    pt "pero antes podr??a echar un ojo a lo que hay por aqu??."

label night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons:

    if (room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) > 0:

        scene room_02_child_hallway_bg_dark_lighting_comp:
            truecenter
            zoom 0.2
        with fade

    if ((room_02_child_hallway_but_toy_Number == 6) and (room_02_child_hallway_but_photo_Number == 5)):

        $ room_02_child_hallway_but_Completed = True

        pt "Creo que solo me queda la puerta del fondo..."

    elif ((room_02_child_hallway_but_toy_Number == 0) and (room_02_child_hallway_but_photo_Number == 5)):

        pt "Quiz??s deber??a echarles un ojo a estos juguetes que hay por el suelo..."

    elif ((room_02_child_hallway_but_toy_Number == 6) and (room_02_child_hallway_but_photo_Number == 0)):

        pt "Quiz??s deber??a ver qu?? hay en los cuadros."

    hide screen quick_menu
    with dissolve
    call screen room_02_child_hallway_buttons_screen()

label HotelKrueger_rooms_voice_check:

    if (((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) + (room_03_marriage_far_but_object_Number)) == 1):

        pt "????Y esta voz?!"

        pt "????De d??nde viene?!"

    elif (((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) + (room_03_marriage_far_but_object_Number)) == 2):

        pt "Otra vez esta voz..."

    if (((((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) == 1) and (room_03_marriage_far_but_object_Number > 0))
        and (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp == True))
        or
        (((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) > 0) and (room_03_marriage_far_but_object_Number == 1))
        and (night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp == True)):
            pt "Esta voz no es la misma de antes,"

    if ((((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) == 1) and (room_03_marriage_far_but_object_Number > 0))
        and (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond_Temp == True)):

        pt "esta parece la de un ni??o..."

    if ((((room_02_child_hallway_but_toy_Number + room_02_child_hallway_but_photo_Number) > 0) and (room_03_marriage_far_but_object_Number == 1))
        and (night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp == True)):

        pt "esta parece la de un hombre adulto..."

    window hide dissolve
    pause

    return

label room_02_child_hallway_but_toy_ball_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_ball_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos 1.5 ypos -2.7 # Down
        easein_quad 10.0 xpos 1.5 ypos -2.5 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Es solo una amiga."

    call HotelKrueger_rooms_voice_check

    #"ball"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons


label room_02_child_hallway_but_toy_warrior_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_warrior_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos 0.06 ypos -1.3 # Down
        easein_quad 10.0 ypos -1.05 # End
        #xpos -0.05 ypos -1.2 # Down
        #easein_quad 10.0 xpos -0.05 ypos -0.95 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Te lo prometo."

    let "Pase lo que pase,"

    extend " te mantendr?? a salvo."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons


label room_02_child_hallway_but_toy_console_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_console_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos 0.0 ypos -1.9 # Down
        easein_quad 10.0 xpos 0.0 ypos -1.6 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Eres la personita m??s valiente que conozco;"

    extend "\n??no es as?? hombret??n?"

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_toy_slingshot_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_slingshot_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos -0.16 ypos -2.7 # Down
        easein_quad 10.0 xpos -0.16 ypos -2.3 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Tranquilo,"

    extend " ya me he encargado del monstruo del armario."

    let "Nunca m??s te va a molestar."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_toy_robot_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_robot_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos 1.3 ypos -2.1 #
        easein_quad 10.0 xpos 1.3 ypos -1.95 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "??Qu?? puedo hacer para que te sientas m??s seguro?"

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_toy_piano_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_toy_piano_Cond = True
    $ room_02_child_hallway_but_toy_Number += 1

    show room_02_child_hallway_bg_dark_lighting_comp_close:
        truecenter
        zoom 1.5
        xpos 1.0 ypos -1.7 #
        easein_quad 10.0 xpos 1.0 ypos -1.4 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Nunca te voy a abandonar, tont??n."

    let "A pesar de lo que ocurra esta noche,"

    extend " o cualquier otra,"

    let "siempre voy a ser tu padre,"

    extend " y eso no cambiar?? nunca,"

    let "por mucho que te empe??es en hacerme enfadar."

    call HotelKrueger_rooms_voice_check

    #"piano"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

####################


label room_02_child_hallway_but_photo_01_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_photo_01_Cond = True
    $ room_02_child_hallway_but_photo_Number += 1

    show room_02_child_hallway_but_photo_01_image_comp:
        truecenter
        zoom 1.0
        easein_quad 5.0 zoom 0.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "??Estudias o trabajas?"

    call HotelKrueger_rooms_voice_check

    #"Photo 01"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_photo_02_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_photo_02_Cond = True
    $ room_02_child_hallway_but_photo_Number += 1

    show room_02_child_hallway_but_photo_02_image_comp:
        truecenter
        zoom 1.0
        easein_quad 5.0 zoom 0.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "??D??nde est??n tus alas?"

    call HotelKrueger_rooms_voice_check

    #"Photo 02"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_photo_03_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_photo_03_Cond = True
    $ room_02_child_hallway_but_photo_Number += 1

    show room_02_child_hallway_but_photo_03_image_comp:
        truecenter
        zoom 1.0
        easein_quad 5.0 zoom 0.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Por tentaciones como t??,"

    extend "\nhay tantos pecadores como yo."

    call HotelKrueger_rooms_voice_check

    #"Photo 03"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_photo_04_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_photo_04_Cond = True
    $ room_02_child_hallway_but_photo_Number += 1

    show room_02_child_hallway_but_photo_04_image_comp:
        truecenter
        zoom 1.0
        easein_quad 5.0 zoom 0.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "??Crees en el amor a primera vista?,"

    extend " ??o deber??a volver a pasar?"

    call HotelKrueger_rooms_voice_check

    #"Photo 04"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

label room_02_child_hallway_but_photo_05_label:

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    $ room_02_child_hallway_but_photo_05_Cond = True
    $ room_02_child_hallway_but_photo_Number += 1

    show room_02_child_hallway_but_photo_05_image_comp:
        truecenter
        zoom 1.0
        easein_quad 5.0 zoom 0.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Disculpa,"

    extend " eh..."

    let "es que eres tan bella que se me olvid?? lo que te iba a decir."

    call HotelKrueger_rooms_voice_check

    #"Photo 05"

    jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

####################

label room_02_child_hallway_door_bright_label:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    if room_02_child_hallway_but_Completed == False:

        pt "Parece que a??n puedo investigar un poco m??s este pasadizo..."

        menu room_02_child_hallway_door_bright_Question:
        
            pt "Si entro, es muy probable que no pueda volver atr??s."

            "<Entrar>":
                
                call p_Help

                jump room_02_child_room_beginning

            "<A??n no>":

                call p_Help

                jump night05_NeusLastDate_HotelKrueger_Door_Childhood_Buttons

    else:

        pt "Veamos qu?? hay en la habitaci??n..."

        jump room_02_child_room_beginning



label room_02_child_room_beginning:

    $ renpy.music.set_volume(0.6, delay=5.0, channel='sfx2')
    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"


    show room_02_child_hallway_bg_dark_lighting_comp_open:
        truecenter
        zoom 0.2 xpos 0.5 ypos 0.5
        easeout_quad 5.0 zoom 1.0 xpos 0.65 ypos 0.5
    
    pause 4.0
    show white:
        additive 1.0
        alpha 0.0
        easein_quad 1.0 alpha 1.0

    pause 1.5

    scene black
    with fade_long1s

    pause 1.5

    show room_02_child_room_bg_comp:
        truecenter
        zoom 0.2
        alpha 0.0
        ease_quad 2.0 alpha 1.0

    window hide dissolve

    pause 1.5

    p "..."

    ## Zoom to the kid

    pt "Esa manta se est?? moviendo..."

    pt "Parece el sollozo de un cr??o."

    # Zoom to armario.

    pt "Ah?? a la derecha hay un armario,"

    pt "??quiz??s sea la salida?"

    # Zoom back.

    pt "Pero..."

    pt "si dejamos de lado qu?? demonios puede haber realmente bajo esa manta,"

    pt "hay cosas por el suelo que no deber??an de estar en la habitaci??n de un ni??o..."

    jump room_02_child_room_Buttons

label room_02_child_room_Buttons:

    if room_02_child_room_but_object_Number > 0:

        scene room_02_child_room_bg_comp:
            truecenter
            zoom 0.2
        with fade

    if room_02_child_room_but_object_Number == 6:

        $ room_02_child_room_but_object_Completed = True

        if PlatinumHelp == True:
            show screen quick_menu()
            with dissolve

        pt "Creo que me queda solo comprobar qu?? hay bajo esa s??bana..."

    #window hide dissolve

    hide screen quick_menu
    with dissolve
    call screen room_02_child_room_buttons_screen()

########

label room_02_child_room_but_object_blood_label:

    $ room_02_child_room_but_object_blood_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.5 ypos -0.55 # Beginning
        easein_quad 10.0 zoom 0.9 xpos -0.1 ypos -0.65 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Pap??,"

    extend "\nesta mujer me da miedo..."

    call HotelKrueger_rooms_voice_check

    jump room_02_child_room_Buttons

label room_02_child_room_but_object_cigarretes_label:

    $ room_02_child_room_but_object_cigarretes_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        truecenter
        subpixel True
        zoom 1.5
        xpos 2.8 ypos -2.4 # Beginning
        easein_quad 5.0 xpos 3.3 ypos -2.75 # end
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Hay alguien en el armario..."

    call HotelKrueger_rooms_voice_check

    #"Cigarretes"

    jump room_02_child_room_Buttons


label room_02_child_room_but_object_coctels_label:

    $ room_02_child_room_but_object_coctels_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        subpixel True
        truecenter
        zoom 1.5
        xpos 0.75 ypos -1.4 # UpLeft Beginning
        easein_quad 8.0 xpos 0.4 ypos -2.0 # Cotails Close
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Sus ojos se han vuelto de otro color, pap??..."

    call HotelKrueger_rooms_voice_check

    jump room_02_child_room_Buttons


label room_02_child_room_but_object_condom_label:

    $ room_02_child_room_but_object_condom_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        truecenter
        zoom 1.5
        subpixel True
        zoom 1.0 xpos 2.0 ypos 0.0 #Beginning
        easein 10.0 zoom 2.5 xpos 5.0 ypos -1.25 # End
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Cada vez que viene esta mujer a casa,"

    let "oigo voces en mi habitaci??n..."

    call HotelKrueger_rooms_voice_check

    jump room_02_child_room_Buttons

label room_02_child_room_but_object_drugs_label:

    $ room_02_child_room_but_object_drugs_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        truecenter
        zoom 1.5
        xpos 1.65 ypos -1.8 # end
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Hay algo bajo la cama..."

    call HotelKrueger_rooms_voice_check

    jump room_02_child_room_Buttons

label room_02_child_room_but_object_wine_label:

    $ room_02_child_room_but_object_wine_Cond = True
    $ room_02_child_room_but_object_Number += 1
    
    show black02
    show room_02_child_room_bg_comp_close:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.2 ypos -2.5 # beginning BEGINNING BOTTLE LEFT
        easein_quad 10.0 zoom 0.8 xpos -0.36 ypos -1.0 # end
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Por favor,"

    extend "\nno te vayas con ella,"

    let "no me dejes solo..."

    call HotelKrueger_rooms_voice_check

    jump room_02_child_room_Buttons

######

label room_02_child_room_but_kid_label:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    if room_02_child_room_but_object_Number <6:

        pt "Creo que a??n quedan cosas extra??as por revisar..."

        menu room_02_child_room_but_kid_Question:

            pt "??Seguro que quiero acercarme a este ni??o...?"

            "S??.":
                
                call p_Help

                $ saturation_tint_level = "verydark"

                jump room_02_child_room_but_kid_close

            "A??n no.":

                call p_Help

                jump room_02_child_room_Buttons

    else:

        jump room_02_child_room_but_kid_close


label room_02_child_room_but_kid_close:

    $ renpy.music.set_volume(1.0, delay=5.0, channel='sfx2')

    $ room_02_child_room_but_kid_Cond = True

    scene room_02_child_bed_kid_covered:
        truecenter

    show light 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 2.0
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_01

    show light_01b:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 1.5
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_02

    with fade

    n "Cautelosamente, te acercas hasta la cama en la que est?? ese tembloroso bulto bajo la s??bana."

    p "..."

    n01 "????Eres un monstruo?!"

    p "??Euh...?"

    p "??Yo?"

    p "No."

    p "No soy ning??n monstruo."

    n01 "..."

    n01 "??Tienes los ojos rojos?"

    p "..."

    p "No."

    n01 "??Me vas a comer?"

    p "No..."

    n01 "??Le has hecho algo a mi padre...?"

    p "..."

    p "No."

    n01 "..."

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"
    $ renpy.music.stop(channel='sfx2', fadeout=5.0)

    scene bg_dark_a_blurry_01:
        truecenter
    show room_02_child_bed_bg:
        truecenter
        zoom 0.5
    show room_02_child_bed_kid_exp_mouth sad_Talkingx04:
        room_02_child_bed_kid_exp_pos
    show room_02_child_bed_kid_exp_eyes 03:
        room_02_child_bed_kid_exp_pos
    show room_02_child_bed_kid_exp_tears 03:
        room_02_child_bed_kid_exp_pos
    show room_02_child_bed_kid_exp_eyebrows sadx01:
        room_02_child_bed_kid_exp_pos
    show room_02_child_bed_sheet 02:
        truecenter
        zoom 0.5
    show light 01:
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 2.0
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_01

    show light_01b:
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 1.5
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_02
    with Dissolve (1.0)

    n "Lentamente destapa su rostro de la s??bana que lo cubre."

    show room_02_child_bed_kid_exp_eyebrows surprisex01
    with dissolve

    pt "Pero si es un cr??o..."

    show room_02_child_bed_kid_exp_eyebrows sadx02
    with dissolve

    n01 "??Y qu?? haces en mi habitaci??n entonces?"

    show room_02_child_bed_kid_exp_eyebrows sadx01
    with dissolve

    pt "Esa es una buena pregunta..."

    show room_02_child_bed_kid_exp_eyebrows serious
    show room_02_child_bed_kid_exp_eyes 02
    show room_02_child_bed_kid_exp_tears 02
    with dissolve

    n01 "??Qui??n eres?"

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    menu room_02_child_room_but_kid_close_Question:
        
        pt "??Qu?? le digo?"

        "Me llamo [protname].":
            
            call p_Help

            show room_02_child_bed_kid_exp_eyebrows sadx03
            show room_02_child_bed_kid_exp_eyes 02
            show room_02_child_bed_kid_exp_tears 02
            with dissolve

            n01 "??Y qu?? haces en mi habitaci??n...?"

            show room_02_child_bed_kid_exp_eyebrows serious
            show room_02_child_bed_kid_exp_eyes 02
            show room_02_child_bed_kid_exp_tears 02
            with dissolve

            p "Hmm..."

            show room_02_child_bed_kid_exp_eyebrows sadx02
            show room_02_child_bed_kid_exp_eyes 03
            show room_02_child_bed_kid_exp_tears 03
            with dissolve

            pt "Eso me gustar??a saber tambi??n a m??..."

            jump room_02_child_room_but_kid_close_02

        "Soy un polic??a.":

            call p_Help

            show room_02_child_bed_kid_exp_eyebrows sadx02
            show room_02_child_bed_kid_exp_eyes 02
            show room_02_child_bed_kid_exp_tears 02
            with dissolve

            n01 "No..."

            show room_02_child_bed_kid_exp_eyebrows sadx03
            show room_02_child_bed_kid_exp_eyes 04
            show room_02_child_bed_kid_exp_tears 04
            with dissolve

            n01 "no me digas que..."

            jump room_02_child_room_but_kid_close_03

        "??Te encuentras bien?":

            call p_Help

            show room_02_child_bed_kid_exp_eyebrows surprisex02
            show room_02_child_bed_kid_exp_eyes 01
            show room_02_child_bed_kid_exp_tears 01
            with dissolve

            n01 "Euh..."

            show room_02_child_bed_kid_exp_eyebrows normal
            show room_02_child_bed_kid_exp_eyes 03
            show room_02_child_bed_kid_exp_tears 03
            with dissolve

            n01 "S??..."

            show room_02_child_bed_kid_exp_eyebrows serious
            show room_02_child_bed_kid_exp_eyes 02
            show room_02_child_bed_kid_exp_tears 02
            with dissolve

            n01 "Me encuentro bien."

            jump room_02_child_room_but_kid_close_02

label room_02_child_room_but_kid_close_02:

    show room_02_child_bed_kid_exp_eyebrows surprisex01
    show room_02_child_bed_kid_exp_eyes 02
    show room_02_child_bed_kid_exp_tears 02
    with dissolve

    p "??Por qu?? est??s llorando?"

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    n01 "??Sabes d??nde est?? mi pap???"

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 02
    show room_02_child_bed_kid_exp_tears 02
    with dissolve

    p "..."

    show room_02_child_bed_kid_exp_eyebrows sadx05
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    p "No,"

    extend " lo siento..."

    show room_02_child_bed_kid_exp_eyebrows sadx06
    show room_02_child_bed_kid_exp_eyes 02
    show room_02_child_bed_kid_exp_tears 02
    with dissolve

    n01 "Me dijo que volver??a antes de las diez para seguir ley??ndome el libro de cuentos,"

    show room_02_child_bed_kid_exp_eyebrows sadx04
    show room_02_child_bed_kid_exp_eyes 07
    show room_02_child_bed_kid_exp_tears 07
    with dissolve

    n01 "pero la aguja peque??a del reloj est?? cerca del n??mero dos,"

    extend " y sigue sin haber vuelto..."

    show room_02_child_bed_kid_exp_eyebrows sadx05
    show room_02_child_bed_kid_exp_eyes 05
    show room_02_child_bed_kid_exp_tears 05
    with dissolve

    n01 "????Por qu?? no ha vuelto?!"

    show room_02_child_bed_kid_exp_eyebrows sadx06
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    p "..."

label room_02_child_room_but_kid_close_03:

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    show room_02_child_bed_kid_exp_mouth sad_Talkingx02
    show room_02_child_bed_sheet 03
    with dissolve

    n01 "??Le ha pasado algo?"

    show room_02_child_bed_kid_exp_eyebrows serious
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Silentx02
    with dissolve

    p "No..."

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Silentx03
    with dissolve

    p "No lo s??..."

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Talkingx02
    with dissolve

    n01 "Le dije que no se fuera,"

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 05
    show room_02_child_bed_kid_exp_tears 05
    show room_02_child_bed_kid_exp_mouth sad_Talkingx01
    with dissolve

    n01 "que esa mujer me daba miedo."

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Talkingx03
    with dissolve

    n01 "Pero ??l me dijo que fuera fuerte,"

    show room_02_child_bed_kid_exp_eyebrows serious
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    show room_02_child_bed_kid_exp_mouth sad_Talkingx03
    show room_02_child_bed_sheet 02
    with dissolve

    n01 "que fuera valiente,"

    show room_02_child_bed_kid_exp_eyebrows angryx01
    show room_02_child_bed_kid_exp_eyes 04
    show room_02_child_bed_kid_exp_tears 04
    show room_02_child_bed_kid_exp_mouth sad_Talkingx03
    show room_02_child_bed_sheet 02
    with dissolve

    n01 "que ya soy mayorcito..."

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Talkingx01
    show room_02_child_bed_sheet 03
    with dissolve

    n01 "Pero..."

    show room_02_child_bed_kid_exp_eyebrows surprisex01
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    show room_02_child_bed_kid_exp_mouth sad_Silentx01
    with dissolve

    p "??A qu?? mujer te refieres?"

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    show room_02_child_bed_kid_exp_mouth sad_Talkingx02
    with dissolve

    n01 "A la mujer de los ojos rojos."

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Silentx04
    with dissolve

    p "..."

    show room_02_child_bed_kid_exp_eyebrows sadx03
    show room_02_child_bed_kid_exp_eyes 06
    show room_02_child_bed_kid_exp_tears 06
    show room_02_child_bed_kid_exp_mouth sad_Talkingx02
    show room_02_child_bed_sheet 02
    with dissolve

    n01 "Me da mucho miedo..."

    show room_02_child_bed_kid_exp_eyebrows sadx01
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    n01 "Siempre est?? rodeada de cosas extra??as,"

    show room_02_child_bed_kid_exp_eyebrows surprisex01
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    with dissolve

    n01 "y a menudo,"

    extend " cuando viene..."

    show room_02_child_bed_kid_exp_eyebrows sadx03
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    with dissolve

    n01 " veo cosas..."

    show room_02_child_bed_kid_exp_eyebrows sadx02
    show room_02_child_bed_kid_exp_eyes 06
    show room_02_child_bed_kid_exp_tears 06
    with dissolve

    n01 "Y muchas veces aqu??,"

    extend " en mi habitaci??n..."

    show room_02_child_bed_kid_exp_eyebrows sadx04
    show room_02_child_bed_kid_exp_eyes 04
    show room_02_child_bed_kid_exp_tears 04
    with dissolve

    n01 "Me susurran cosas al o??do,"

    show room_02_child_bed_kid_exp_eyebrows sadx05
    show room_02_child_bed_kid_exp_eyes 05
    show room_02_child_bed_kid_exp_tears 05
    with dissolve

    n01 "me dicen que no volver?? a ver a mi pap??..."

    show room_02_child_bed_kid_exp_eyebrows sadx06
    show room_02_child_bed_kid_exp_eyes 06
    show room_02_child_bed_kid_exp_tears 06
    with dissolve

    p "..."

    show room_02_child_bed_kid_exp_eyebrows angryx03
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Talkingx04
    show room_02_child_bed_sheet 03
    with dissolve

    n01 "??Pero ??l no me cree!"

    show room_02_child_bed_kid_exp_eyebrows angryx02
    show room_02_child_bed_kid_exp_eyes 04
    show room_02_child_bed_kid_exp_tears 04
    show room_02_child_bed_kid_exp_mouth sad_Talkingx03
    with dissolve

    n01 "Dice que ya soy mayor para estas cosas..."

    show room_02_child_bed_kid_exp_eyebrows angryx01
    show room_02_child_bed_kid_exp_eyes 06
    show room_02_child_bed_kid_exp_tears 06
    show room_02_child_bed_kid_exp_mouth sad_Silentx04
    with dissolve

    p "..."

    show room_02_child_bed_kid_exp_eyebrows sadx06
    show room_02_child_bed_kid_exp_eyes 04
    show room_02_child_bed_kid_exp_tears 04
    show room_02_child_bed_kid_exp_mouth sad_Talkingx02
    with dissolve

    n01 "??D??nde est?? mi pap??...?"

    show room_02_child_bed_kid_exp_eyebrows sadx05
    show room_02_child_bed_kid_exp_eyes 03
    show room_02_child_bed_kid_exp_tears 03
    show room_02_child_bed_kid_exp_mouth sad_Talkingx01
    with dissolve

    n01 "Tengo miedo..."

    show room_02_child_bed_kid_exp_eyebrows sadx06
    show room_02_child_bed_kid_exp_eyes 04
    show room_02_child_bed_kid_exp_tears 04
    show room_02_child_bed_kid_exp_mouth sad_Silentx04
    with dissolve

    p "..."

    stop music fadeout 2.0
    $ music_play = ""

    $ renpy.music.set_volume(0.0, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/whispers_child01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.1, delay=2.0, channel='sfx2')

    show room_02_child_bed_kid_exp_eyebrows surprisex02
    show room_02_child_bed_kid_exp_eyes 01
    show room_02_child_bed_kid_exp_tears 01
    show room_02_child_bed_kid_exp_mouth sad_Silentx01
    with dissolve

    ng01 "Pap??..."

    play sound "audio/sfx/fall02.ogg"

    scene room_02_child_bed_kid_covered:
        truecenter

    show light 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 2.0
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_01

    show light_01b:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.0
        zoom 1.5
        xpos -0.1 ypos 0.3
        rotate -80
        parallel:
            storm_lighting_anim_02
    with vpunch

    ng01 " ??Eres t??...?"

    n01 "??Otra vez las voces!"

    $ renpy.music.set_volume(0.4, delay=2.0, channel='sfx2')

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    scene black
    with fade

    n "R??pidamente giras la cabeza para mirar de d??nde proced??a esa voz."

    pt "Vuelvo a estar completamente a oscuras..."

    ng01 "Me dijiste que volver??as pronto..."

    $ renpy.music.set_volume(0.4, delay=2.0, channel='sfx2')

    n "La voz dulce y temblorosa de una ni??a muy, muy peque??a."

    n02 "Tengo fr??o..."

    pt "??Ahora un ni??o?"

    ng02 "??D??nde te fuiste pap??...?"

    pt "??Qu?? diablos...?"

    n03 "Hay alguien bajo la cama..."

    n04 "??Por qu?? no volviste a casa...?"

    ng03 "Esa mujer me da miedo..."

    $ renpy.music.set_volume(0.01, delay=2.0, channel='sfx1')
    $ renpy.music.set_volume(1.0, delay=2.0, channel='sfx2')
    $ renpy.music.set_volume(0.2, delay=2.0, channel='sfx3')
    $ renpy.music.set_volume(0.2, delay=2.0, channel='sfx4')

    n "Sus voces son cada vez m??s cercanas..."

    play sound "audio/sfx/heartbeat_01.ogg"

    ng04 "No me dejes sola..."

    play sound "audio/sfx/heartbeat_01.ogg"

    n05 "??Por qu?? no vuelves...?"

    play sound "audio/sfx/heartbeat_01.ogg"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)

    window hide dissolve
    pause

    p "..."

    pt "Ya no les oigo..."

    jump night05_NeusLastDate_HotelKrueger_Door_General

######
label room_02_child_room_but_exit_label:

    show room_02_child_room_bg_comp_doorlight:
        truecenter
        zoom 0.2

    if PlatinumHelp == True:
        show screen quick_menu()
    with dissolve

    pt "Eso tiene pinta de ser un armario,"

    pt "pero no veo otra salida."

    pt "??Y si me encuentro con el monstruo del armario ah?? dentro?"
    
    menu room_02_child_room_but_exit_Question:
        
        pt "Si voy por ah?? seguramente no podr?? volver..."

        "S??.":
            
            call p_Help

            jump room_02_child_room_but_exit02_label

        "No.":

            call p_Help

            jump room_02_child_room_Buttons

label room_02_child_room_but_exit02_label:

    $ room_02_child_room_but_exit_Cond = True

    pt "Aunque probablemente sea un ni??o,"

    pt "prefiero no destapar lo que hay debajo de esa manta..."

    show room_02_child_room_bg_comp_doorlight:
        ###truecenter
        ###zoom 0.2 xpos 0.5 ypos 0.5
        subpixel True
        ease 3.0 zoom 1.0 xpos -1.5 ypos 0.9

    show white:
        additive 1.0
        alpha 0.0
        pause 1.0
        easein_quad 1.0 alpha 1.0

    window hide dissolve
    pause 2.5

    scene black
    with fade

    p "..."

    pt "??Hola...?"

    p "..."

    pt "No s?? si ha sido buena idea..."

    jump night05_NeusLastDate_HotelKrueger_Door_General



####################################################################################################
################################################################################################## MARRIAGE

####################################################################################################
##################################################################################################

####################################################################################################
##################################################################################################

label night05_NeusLastDate_HotelKrueger_Door_Marriage:

    menu night05_NeusLastDate_HotelKrueger_Door_Marriage_Quesiton:
        
        pt "??Seguro que quiero tomar esta puerta?"

        "S??.":

            #########################################################
    
            if config.version < "00.12.04": # Before Third Door.
                
                call endupdatescript
            
            #######################################################
            
            call p_Help

            $ night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond = True
            $ night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond_Temp = True
            $ night05_NeusLastDate_HotelKrueger_Door_Used_Number += 1

            jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Beginning

        "No":

            call p_Help

            hide screen quick_menu
            with dissolve
            call screen night05_hotel_doors3_screen()

label night05_NeusLastDate_HotelKrueger_Door_Marriage_Beginning:

    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/birds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.1, delay=30.0, channel='sfx1')

    $ renpy.music.set_volume(0.1, delay=0.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/crying_woman02_far.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.06, delay=30.0, channel='sfx2')

    stop music fadeout 3.0
    $ music_play = ""

    scene black
    with fade_long1s

    if ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond) or (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond)) == True:

        pt "Vuelvo a no ver nada..."

    else:

        pt "No veo un carajo..."

label night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons:

    if ((room_03_marriage_far_but_object_Number == 0) and (room_03_marriage_far_door_before_Cond == False)):

        scene room_03_marriage_far_HD:
            truecenter
            zoom 0.2
        show white:
            subpixel True
            additive 1.0 alpha 1.0
            ease_quad 3.0 alpha 0.0
        with fade

        pause 3.0

        if PlatinumHelp == True:
            show screen quick_menu() 
            with dissolve

        p "..."

        pt "??A pleno d??a?"

        if ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond) and (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond)) == True:

            pt "Las otras dos habitaciones me llevaron a un lugar de noche,"

            pt "pero este..."

        elif ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond) or (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond)) == True:

            pt "Pens?? que ver??a un lugar t??trico y oscuro como la otra habitaci??n..."

        else:

            pt "Me esperaba algo m??s oscuro y t??trico..."

        pt "Aunque viendo lo que hay por el suelo,"

        pt "tampoco parece un lugar de ensue??o,"

        extend "\nprecisamente..."

        pt "Al fondo veo lo que podr??a ser la puerta de salida;"

        pt " y esa mujer,"

        extend " llorando..."

        if ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond) and (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond)) == True:

            pt "??Por qu?? hay alguien llorando en todas las habitaciones?"

        elif ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond) or (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond)) == True:

            pt "Como en la otra habitaci??n."

        pt "Quiz??s ser??a buena idea mirar lo que hay por el suelo antes de acercarme ah??."

        hide screen quick_menu 
        with dissolve

        call screen room_03_marriage_far_buttons_screen()

    else:

        scene room_03_marriage_far_HD:
            truecenter
            zoom 0.2
        with fade

        if room_03_marriage_far_but_object_Number == 6:

            if PlatinumHelp == True:
                show screen quick_menu() 
                with dissolve

            pt "Parece que solo me queda ir a ver a esa extra??a mujer..."

            pt "o largarme de aqu?? por esa puerta..."

        hide screen quick_menu 
        with dissolve

        call screen room_03_marriage_far_buttons_screen()


label room_03_marriage_far_but_object_bouquet_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_bouquet_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        zoom 1.5 xpos -0.35 ypos -2.2
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Te quiero,"

    extend " no por quien eres,"

    let "sino por quien soy cuando estoy contigo."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_but_object_cake_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_cake_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        #zoom 1.5 xpos 1.2 ypos -2.5
        zoom 1.0 xpos 1.0 ypos -1.6
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Si volviera a nacer,"

    extend " te volver??a a elegir."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons


label room_03_marriage_far_but_object_chocolates_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_chocolates_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        zoom 1.5 xpos 1.1 ypos -1.5
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Amor es solo una palabra;"

    let "hasta que llegaste para darle sentido."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_but_object_petals_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_petals_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        zoom 1.5 xpos 0.5 ypos -2.7 # Bottom
        easein_quad 15.0 zoom 1.0 xpos 0.5 ypos -0.4 # Top
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Tantos siglos,"

    extend "\ntantos mundos,"

    extend "\ntanto espacio,"

    let "y coincidir."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_but_object_rings_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_rings_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        zoom 2.0 xpos -1.1 ypos -4.2
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "Si yo pudiera darte una cosa en la vida,"

    let "me gustar??a darte la capacidad de verte a ti mismo a trav??s de mis ojos."

    let "Solo entonces te dar??s cuenta,"

    extend "\nde lo especial que eres para m??."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_but_object_vows_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_but_object_vows_Cond = True
    $ room_03_marriage_far_but_object_Number += 1
    
    scene black
    show room_03_marriage_far_HD_close:
        truecenter
        zoom 2.0 xpos -0.5 ypos -1.7
    with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    let "No seas est??pida, cari??o,"

    let "S??,"

    extend " me conquistaste con tus virtudes,"

    let "pero me temo que te amo tanto,"

    let "que ya ser??a incapaz de vivir sin ti y tus vicios."

    call HotelKrueger_rooms_voice_check

    jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_but_woman_label:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    #scene black
    #show room_03_marriage_far_HD_close:
        #truecenter
        #zoom 1.5 xpos 0.4 ypos 0.4
    #with fade

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    if room_03_marriage_far_but_object_Number < 6:

        pt "Antes de ir hasta all??,"

        pt "a??n podr??a echarles un ojo a estos objetos que hay por el suelo..."

        menu room_03_marriage_far_but_woman_Question:
        
            pt "??Seguro que quiero ir hasta esa mujer?"

            "S??.":
                
                call p_Help

                jump room_03_marriage_far_woman_close

            "A??n no.":

                call p_Help

                jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

    else:

        jump room_03_marriage_far_woman_close

label room_03_marriage_far_woman_close:

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ room_03_marriage_far_woman_Cond = True

    show room_03_marriage_far_HD_close:
        truecenter
        zoom 0.2 xpos 0.5 ypos 0.5
        easein 15.0 zoom 1.5 xpos 0.4 ypos 0.15

    # Here you get closer to the crying woman.

    $ renpy.music.set_volume(0.8, delay=15.0, channel='sfx2')

    pt "Ah?? vamos..."

    pt "Espero que no sea una {a=https://witcher.fandom.com/wiki/Noonwraith}dama del mediod??a{/a},"

    extend " como en \"{a=https://es.wikipedia.org/wiki/Saga_de_Geralt_de_Rivia}The Witcher{/a}\"..."

    $ renpy.music.play("audio/sfx/crying_woman02.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx2')

    scene room_03_church_close_headdown_comp:
        subpixel True
        truecenter
        zoom 2.5
        xpos 0.5 ypos 0.1
        ease 20.0 zoom 1.0 xpos 0.5 ypos 0.5 # End
    with fade 

    $ renpy.music.set_volume(0.8, delay=15.0, channel='sfx2')

    m02 "??Por qu??...?"

    n "Ves con mejor claridad a esa mujer sentada,"

    n "en el suelo,"

    extend " apoyando su espalda contra el sagrado altar,"

    m02 "??Por qu?? hoy...?"

    n "con el rostro escondido entre sus rodillas,"

    n " ahog??ndose entre l??grimas."

    p "..."

    with vpunch

    m02 "??He dicho que os fuerais!"

    m02 "Necesito estar sola..."

    pt "??No ser??a m??s razonable que fuera ella la que se fuera a llorar a otra parte?"

    p "??Ejem...!"

    $ renpy.music.stop(channel='sfx2', fadeout=3.0)

    scene room_03_church_close_bg:
        room_03_church_close_rest_pos
    show room_03_church_close_head camera:
        room_03_church_close_rest_pos
    show room_03_church_close_bride_exp_mouth sad_Talkingx01:
        room_03_church_close_exp_pos
    show room_03_church_close_bride_exp_eyes 02:
        room_03_church_close_exp_pos
    show room_03_church_close_bride_exp_tears 02:
        room_03_church_close_exp_pos
    show room_03_church_close_bride_exp_eyebrows surprisex01:
        room_03_church_close_exp_pos
    show room_03_church_close_hair_front:
        room_03_church_close_rest_pos
    with Dissolve (1.0)

    m02 "??Euh...?"

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    m02 "??Qui??n eres?"

    show room_03_church_close_bride_exp_mouth sad_Silentx01
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows sadx01
    with dissolve

    p "Yo..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx06
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows surprisex01
    with dissolve

    m02 "????Sabes algo de mi marido?!"

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    m02 "????Est?? bien?!"

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "????Le ha pasado algo?!"

    show room_03_church_close_bride_exp_mouth sadbiting_Silentx02
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    p "..."

    show room_03_church_close_bride_exp_mouth sad_Silentx02
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows sadx01
    with dissolve

    p "No,"

    extend " no lo s??,"

    show room_03_church_close_bride_exp_mouth sad_Silentx05
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    p "lo lamento."

    show room_03_church_close_bride_exp_mouth sad_Silentx06
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    m02 "..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows angryx01
    with dissolve

    m02 "Dime,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx01
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "??te parezco vieja,"

    extend " o fea?"

    show room_03_church_close_bride_exp_mouth sad_Silentx06
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    p "??Qu??...?"

    show room_03_church_close_bride_exp_mouth sad_Silentx05
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    menu room_03_marriage_far_woman_close_old_Question:
        
            pt "??Vieja o fea?"

            "No, por supuesto que no.":
                
                call p_Help

                jump room_03_marriage_far_woman_close_old_No

            "Quiz??s un poco...":

                call p_Help

                $ room_03_marriage_far_woman_close_old_Yes = True

                show room_03_church_close_bride_exp_mouth sad_Silentx06
                show room_03_church_close_bride_exp_eyes 02
                show room_03_church_close_bride_exp_tears 02
                show room_03_church_close_bride_exp_eyebrows surprisex02
                with dissolve

                m02 "..."

                show room_03_church_close_bride_exp_mouth sad_Talkingx02
                show room_03_church_close_bride_exp_eyes 07
                show room_03_church_close_bride_exp_tears 07
                show room_03_church_close_bride_exp_eyebrows sadx05
                with dissolve

                m02 "S??..."

                show room_03_church_close_bride_exp_mouth sad_Talkingx003
                show room_03_church_close_bride_exp_eyes 05
                show room_03_church_close_bride_exp_tears 05
                show room_03_church_close_bride_exp_eyebrows sadx04
                with dissolve

                m02 "Quiz??s tengas raz??n..."

                show room_03_church_close_bride_exp_mouth sadbiting_Silentx02
                show room_03_church_close_bride_exp_eyes 06
                show room_03_church_close_bride_exp_tears 06
                show room_03_church_close_bride_exp_eyebrows sadx05
                with dissolve

                dad "Decirle eso a una mujer con el coraz??n hecho a??icos,"

                show room_03_church_close_bride_exp_mouth sadbiting_Silentx03
                show room_03_church_close_bride_exp_eyes 07
                show room_03_church_close_bride_exp_tears 07
                show room_03_church_close_bride_exp_eyebrows sadx04
                with dissolve

                dad "despu??s de ser abandonada en frente de toda su familia y sus amigos,"

                show room_03_church_close_bride_exp_mouth sadbiting_Silentx04
                show room_03_church_close_bride_exp_eyes 06
                show room_03_church_close_bride_exp_tears 06
                show room_03_church_close_bride_exp_eyebrows sadx05
                with dissolve

                dad "el d??a de su boda..."

                show room_03_church_close_bride_exp_mouth sadbiting_Silentx05
                show room_03_church_close_bride_exp_eyes 05
                show room_03_church_close_bride_exp_tears 05
                show room_03_church_close_bride_exp_eyebrows sadx05
                with dissolve

                dad "Me siento orgulloso de ti."

                show room_03_church_close_bride_exp_mouth sad_Talkingx03
                show room_03_church_close_bride_exp_eyes 04
                show room_03_church_close_bride_exp_tears 04
                show room_03_church_close_bride_exp_eyebrows sadx04
                with dissolve

                m02 "??Pero por qu?? no me lo ha dicho...?"

                show room_03_church_close_bride_exp_mouth sadbiting_Silentx01
                show room_03_church_close_bride_exp_eyes 03
                show room_03_church_close_bride_exp_tears 03
                show room_03_church_close_bride_exp_eyebrows sadx01
                with dissolve

                p "No es algo f??cil de decir cara a cara."

                jump room_03_marriage_far_woman_close_old_After

    # Choice.

label room_03_marriage_far_woman_close_old_No:

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    m02 "??Entonces, por qu?? me ha abandonado?"

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx04
    with dissolve

    m02 "??Por qu?? justo el d??a de nuestra boda...?"

    show room_03_church_close_bride_exp_mouth sadbiting_Silentx04
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    p "Si opinara que eres vieja o fea,"

    show room_03_church_close_bride_exp_mouth sadbiting_Silentx03
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    p "no habr??a llegado tan lejos como para llevarte al altar."

    show room_03_church_close_bride_exp_mouth sad_Talkingx003
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx01
    with dissolve

    m02 "Entonces..."

    show room_03_church_close_bride_exp_mouth sad_Silentx01
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows surprisex02
    with dissolve

    p "A veces pueden ser los nervios..."

label room_03_marriage_far_woman_close_old_After:

    show room_03_church_close_bride_exp_mouth sad_Talkingx06
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "????Y por qu?? no me ha dejado una nota...?!"

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    m02 "Algo,"

    if room_03_marriage_far_woman_close_old_Yes == True:

        show room_03_church_close_bride_exp_mouth sad_Talkingx03
        show room_03_church_close_bride_exp_eyes 06
        show room_03_church_close_bride_exp_tears 06
        show room_03_church_close_bride_exp_eyebrows sadx05
        with dissolve

        m02 "que me hubiera hecho saber que ya no le gusto;"

        show room_03_church_close_bride_exp_mouth sad_Talkingx05
        show room_03_church_close_bride_exp_eyes 02
        show room_03_church_close_bride_exp_tears 02
        show room_03_church_close_bride_exp_eyebrows angryx02
        with dissolve

        m02 "??Que ha encontrado a otra furcia est??pida que se cree que lo amar?? m??s que yo!"

        show room_03_church_close_bride_exp_mouth sad_Talkingx06
        show room_03_church_close_bride_exp_eyes 07
        show room_03_church_close_bride_exp_tears 07
        show room_03_church_close_bride_exp_eyebrows angryx03
        with dissolve


    else:

        show room_03_church_close_bride_exp_mouth sad_Talkingx03
        show room_03_church_close_bride_exp_eyes 03
        show room_03_church_close_bride_exp_tears 03
        show room_03_church_close_bride_exp_eyebrows sadx01
        with dissolve

        m02 "que me hubiera hecho saber que a??n no estaba preparado..."

        show room_03_church_close_bride_exp_mouth sad_Talkingx04
        show room_03_church_close_bride_exp_eyes 02
        show room_03_church_close_bride_exp_tears 02
        show room_03_church_close_bride_exp_eyebrows sadx02
        with dissolve

        m02 "Lo hubiera hecho..."

        show room_03_church_close_bride_exp_mouth sad_Talkingx06
        show room_03_church_close_bride_exp_eyes 04
        show room_03_church_close_bride_exp_tears 04
        show room_03_church_close_bride_exp_eyebrows sadx05
        with dissolve

    m02 "habr??a hecho cualquier cosa por ??l..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    m02 "Pero ahora..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx04
    with dissolve

    m02 "no s?? d??nde est??..."

    show room_03_church_close_bride_exp_mouth sadbiting_Silentx06
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    p "..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows angryx01
    with dissolve

    m02 "Hace ya unas noches que lo noto algo extra??o..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx01
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "Huele distinto,"

    extend " \nparece m??s cansado de lo habitual,"

    extend "\nregresa tarde del trabajo..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx03
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    m02 "Al principio pens?? que eran imaginaciones m??as..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "pero ahora..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "No quer??a aceptarlo,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows angryx02
    with dissolve

    m02 "no quiero..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx03
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows angryx01
    with dissolve

    m02 "Pero..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows serious
    with dissolve

    m02 "??Y si se ha fugado con ella?"

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows normal
    with dissolve

    m02 "??Y si es m??s joven que yo?"

    show room_03_church_close_bride_exp_mouth sad_Talkingx06
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "Soy una est??pida..."

    show room_03_church_close_bride_exp_mouth sadbiting_Silentx08
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    p "..."

    if room_03_marriage_far_woman_close_old_Yes == True:

        show room_03_church_close_bride_exp_mouth sadbiting_Silentx07
        show room_03_church_close_bride_exp_eyes 06
        show room_03_church_close_bride_exp_tears 06
        show room_03_church_close_bride_exp_eyebrows sadx04
        with dissolve

        p "No eres est??pida por querer a alguien que no te corresponde."

    else:

        show room_03_church_close_bride_exp_mouth sadbiting_Silentx08
        show room_03_church_close_bride_exp_eyes 06
        show room_03_church_close_bride_exp_tears 06
        show room_03_church_close_bride_exp_eyebrows sadx05
        with dissolve

        p "No creo que sea eso..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx05
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "??S??!"

    show room_03_church_close_bride_exp_mouth sad_Talkingx06
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "??Lo soy!"

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows angryx01
    with dissolve

    m02 "Porque aun as??,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx04
    with dissolve

    m02 "lo sigo amando con locura..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx03
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows angryx02
    with dissolve

    m02 "Si no quiere casarse hoy,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "no me importa esperar un a??o,"

    extend " dos,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx03
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows angryx03
    with dissolve

    m02 "o incluso nunca..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 05
    show room_03_church_close_bride_exp_tears 05
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    m02 "Solo quiero que vuelva,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx06
    show room_03_church_close_bride_exp_eyes 07
    show room_03_church_close_bride_exp_tears 07
    show room_03_church_close_bride_exp_eyebrows sadx04
    with dissolve

    m02 "quiero escuchar su voz,"

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 06
    show room_03_church_close_bride_exp_tears 06
    show room_03_church_close_bride_exp_eyebrows sadx05
    with dissolve

    m02 "quiero..."

    show room_03_church_close_bride_exp_mouth sad_Talkingx04
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows sadx02
    with dissolve

    m02 "quiero que sepa cu??nto le amo."

    show room_03_church_close_bride_exp_mouth sad_Talkingx02
    show room_03_church_close_bride_exp_eyes 04
    show room_03_church_close_bride_exp_tears 04
    show room_03_church_close_bride_exp_eyebrows sadx03
    with dissolve

    m02 "Solo eso..."

    show room_03_church_close_bride_exp_mouth sad_Silentx03
    show room_03_church_close_bride_exp_eyes 03
    show room_03_church_close_bride_exp_tears 03
    show room_03_church_close_bride_exp_eyebrows serious
    with dissolve

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(0.0, delay=0, channel='sfx3')
    $ renpy.music.play("audio/sfx/whispers_creepy01.ogg", channel="sfx3",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.05, delay=5.0, channel='sfx3')

    m03 "??Cari??o!"

    show room_03_church_close_bride_exp_mouth sad_Silentx06
    show room_03_church_close_bride_exp_eyes 02
    show room_03_church_close_bride_exp_tears 02
    show room_03_church_close_bride_exp_eyebrows surprisex02
    with Dissolve (1.0)

    p "..."

    $ renpy.music.set_volume(0.2, delay=3.0, channel='sfx3')

    scene black
    with fade

    n "Vuelves la mirada atr??s para ver de d??nde procede esa extra??a voz."

    m03 "????Eres t???!"

    m04 "Mi amor..."

    extend " ??D??nde est??s?"

    m05 "??Qu?? hice mal?"

    m01 "??Esa ramera tetuda no te ama!"

    m01 "??Solo te est?? usando!"

    $ renpy.music.set_volume(0.7, delay=3.0, channel='sfx3')

    n "Aparecen voces de mujeres quebrantadas por el dolor y la p??rdida, por todos lados."

    m03 "Vuelve,"

    extend " por favor..."

    $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx3')

    n "Cada vez las oyes m??s,"

    play sound "audio/sfx/heartbeat_01.ogg"

    m04 "Te amo..."

    play sound "audio/sfx/heartbeat_01.ogg"

    n "y m??s cerca..."

    play sound "audio/sfx/heartbeat_01.ogg"

    m05 "??NO ME ABANDONES!"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)

    scene black
    with fade_long1s

    p "..."

    pt "Da un poco de {a=https://es.wikipedia.org/wiki/Miedo}{i}yuyu{/i}{/a} o??r a tantas mujeres gritarte eso,"

    pt "sin saber de d??nde vienen."

    pt "Aunque lo de ramera tetuda..."

    pt "??A qui??n se referir???"

    jump night05_NeusLastDate_HotelKrueger_Door_General

label room_03_marriage_far_but_door_label:

    $ room_03_marriage_far_door_before_Cond = True

    show room_03_marriage_far_but_door

    pt "Si tomo esa puerta,"

    extend "\nseguramente ya no podr?? volver..."

    menu room_03_marriage_far_but_object_door_Question:
        
        pt "??Seguro que me quiero largar?"

        "??Ya estoy tardando!":
            
            call p_Help

            jump room_03_marriage_far_door_exit

        "A??n no.":

            call p_Help

            jump night05_NeusLastDate_HotelKrueger_Door_Marriage_Buttons

label room_03_marriage_far_door_exit:

    $ room_03_marriage_far_door_Cond = True

    pt "??Yo me largo de aqu??!"
    
    show room_03_marriage_far_HD_door_bright:
        truecenter
        zoom 0.2 xpos 0.5 ypos 0.5
        ease_quad 3.0 zoom 1.5 xpos -0.3 ypos 0.8
    

    window hide dissolve
    pause 1.5

    show white:
        additive 1.0
        alpha 0.0
        easein_quad 1.5 alpha 1.0

    pause 2.0

    scene black
    with fade_long1s

    pause

    jump night05_NeusLastDate_HotelKrueger_Door_General



    #call screen night05_hotel_doors3_screen()
    #with dissolve


####################################################################################################
##################################################################################################
        ## EXIT
####################################################################################################
##################################################################################################

label night05_NeusLastDate_HotelKrueger_Door_Exit_00:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    if night05_NeusLastDate_HotelKrueger_Door_Exit_01_Cond == False:
        jump night05_NeusLastDate_HotelKrueger_Door_Exit_01
    else:
        jump night05_NeusLastDate_HotelKrueger_Door_Exit_02_Question

label night05_NeusLastDate_HotelKrueger_Door_Exit_01:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    $ night05_NeusLastDate_HotelKrueger_Door_Exit_01_Cond = True

    pt "Este es el cartel de salida."

    pt "Si tomo esta direcci??n,"

    pt "??podr?? salir de este lugar?"

    pt "??O ser?? otra manipulaci??n m??s?"

    pt "Pero..."

    pt "??y si no lo fuera?"

    pt "??y si realmente salgo de aqu??...?"

    pt "Si hubiera querido hacerme da??o,"
    
    pt "ya me lo habr??a hecho..."

    pt "Est?? claro que hay algo tras estas puertas que quiere ense??arme."

    menu night05_NeusLastDate_HotelKrueger_Door_Exit_01_Question:

        pt "Si me voy de aqu?? ya no tendr?? oportunidad de verlo..."

        "Largarse de aqu??.":

            jump night05_NeusLastDate_HotelKrueger_Door_Exit_02

        "Mejor no.":

            jump night05_NeusLastDate_HotelKrueger_Door_General

label night05_NeusLastDate_HotelKrueger_Door_Exit_02:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    $ night05_NeusLastDate_HotelKrueger_Door_Exit_02_Cond = True

    pt "??Al carajo!"

    pt "??No pienso pasar ni un solo segundo m??s en este lugar!"

    dad "??Est??s seguro?"

    p "..."

    dad "??No quieres saber la verdad sobre Neus?"

    dad "??Tanto miedo tienes de saber la verdad?"

    dad "??O es que te da miedo la oscuridad...?"

    p "..."

    dad "Te ten??a por alguien m??s valiente..."

    menu night05_NeusLastDate_HotelKrueger_Door_Exit_02_Question:

        pt "??Y si realmente me estoy perdiendo algo al irme...?"

        "??He dicho que me largo de aqu??!":
            jump night05_NeusLastDate_HotelKrueger_Door_Exit_03

        "Quiz??s podr??a echarle un ojo...":

            jump night05_NeusLastDate_HotelKrueger_Door_General

label night05_NeusLastDate_HotelKrueger_Door_Exit_03:

    if PlatinumHelp == True:
        show screen quick_menu()
        with dissolve

    $ night05_NeusLastDate_HotelKrueger_Door_Exit_03_Cond = True

    pt "??Que te follen!"

    pt "??No tengo ninguna intenci??n de ser tu juguete!"

    dad "No soy yo quien est?? jugando contigo..."

    dad "Que disfrutes de tu cita,"

    dad "al menos lo que queda de ella..."

    pt "??Qu??...?"

    jump night05_NeusLastDate_After_HotelKrueger

# Solo el botones es un hombre. La gerente es Neus adulta y la Recepcionista es Neus(?) de joven.

# Una vez dentro te encuentras a una anciana recepcionista clamando que diablos haces aqu?? dentro, este lugar est?? repleto de almas perdidas que vagan por la eternidad condenadas por culpa de la maldici??n de una terrible mujer.

# Detr??s de ti aparece una morena despanpanante con un traje a lo morticia Addams, unas facciones adultas, unas curvas de infarto, que te dice que no le hagas ning??n caso a la loca esa. Que si est??s buscando a tu amiga morena, ya est??s llegando tarde, que debes de subir en el ascensor/escalera.

# la mujer te recuerda que nunca puedes volver atr??s, siempre tienes que avanzar. y me recuerda que no me aparte de la luz y que busque siempre la puerta de salida que estar?? iluminada. ??C??mo es que est??s solo? ??D??nde est??n los dem??s?

# Una vez arriba te encuentras con 3 Puertas, (y una salida de emergencias). El juego no te recomienda salir por la puerta de emergencias.




## PUERTA 1 # CEMENTERIO # Ni??os Muertos. // Padres desconsolados buscando a sus hijos (?). Aparecen padres buscando a sus ni??os.

# Frases cuando ves las tumbas repletas de objetos de recuerdos: // Seguro que de mayor ser?? astronauta. // Tiene los mismos ojos que su madre. // Es la cosa m??s bointa que he visto nunca. // Jam??s dejar?? que te ocurra nada malo. // Te amo m??s que a mi propia vida. // Hijo, no dejes que nadie te diga que no puedes hacer algo. Ni siquiera yo, ??De acuerdo? Si tienes un sue??o, tienes que protegerlo. // Por mucho que crezcas, siempre ser??s mi beb??. // Es incre??ble c??mo alguien tan peque??ito... puede hacerme sentir algo tan gigantesco. // Eres mi futuro y lo mejor que me ha pasado nunca // Sin ti, tal vez mi casa estar??a limpia y mi billetera llena, pero mi coraz??n se encontrar??a totalmente vac??o. // Te amo desde el mismo instante que supe que ven??as en camino, te am?? m??s cuando escuch?? latir tu coraz??n por primera vez, te am?? desde el primer minuto que naciste. Cuando vi tu carita y tomaste mi mano, entonces supe que desde ese mismo instante, que dar??a mi vida entera por ti. // Te llev?? 9 meses en el vientre, tres a??os en los brazos y te llevar?? toda la vida en el coraz??n. // Cari??o, sino crees en los milagros, es porque has olvidado que eres uno. // Soy tu madre, te cansar??, me enfadar?? contigo, gritar?? como una loca, te llamar?? la atenci??n, te repetir?? mil veces las cosas... ??Y sabes por qu??? Por que te amo... nunca encontrar??s a nadie que te ame m??s que yo, sin ning??n inter??s, solo por el amor maternal, porque tu triunfo ser?? el mio. // Soy tu madre, y eso es para siempre, com el amor que siento por ti. // Tengo un cofre que contiene un tesoro, uno que no se puede comparar con ning??n otro. Este tesoro eres t??, que con gran amor creciste en mis brazos, me diste tu primera sonrisa, me llamaste mam?? y me entregaste amor sin esperar nada a cambio. // Si me necesitas, ll??mame. No importa si estoy durmiendo, si tengo problemas propios o si estoy enojada contigo. Si me necesitas y necesitas hablar conmigo, siempre voy a estar ah?? para ti, no importa lo grande o peque??o que sea tu problema. Ah?? estar?? para ti. // No s?? si llegar?? a conocer el para??so, pero si existe, seguro que no es tan bonito como lo es ser la madre de un hijo tan maravilloso como t??. Gracias, por todos estos momentos que me regalas cada d??a. // 

# Por el suelo (o en las pr??pias tumbas) te vas encontrando sonajeros, cunas abandonadas, chupetes, biberones, pa??ales, etc.

# En una de las puertas te encuentras ante las enormes y oxidadas puertas de un cementerio de noche, cuando miras hacia atr??s solo ves oscuridad, el sonido de viento envuelve el lugar, al mirar atr??s solo ves oscuridad y un sonido escalofriante que proviene de negrura absoluta.

# Cuando entras en el cementerio te das cuenta que pr??citcamente lo ??nico iluminado del lugar es el camino que recorres y apenas las l??pidas que se encuentran cerca de este sendero, te percatas que las tumbas son diminutas y que en muchas de ellas son pocos a??os, meses o incluso d??as los que hay de diferencia entre el nacimiento y el fallecimiento, a lo que deduces que se tratan todos de ni??os.

# A lo lejos oyes el llanto desconsolado de unos padres, te percatas que al final del sendero que sigues se encuentra la cripta en la que ambos est??n arrodillados. Tambi??n descubres que esa cripta tiene una puerta iluminada, la puerta por la que tienes que volver. Cuando te acercas tienes la opci??n de preguntar que les pasa, o directamente ir a la puerta. Si les preguntas te miran con los ojos llorosos pregunt??ndote d??nde est?? su hijo. El esto del lugar se hace oscuro, y empiezan a aparecer padres desconsolados pregunt??ndote por sus hijos. Era un buen chico, no deb?? gritarle, deber??a haberle dicho que no hablara con desconocidos,...





## PUERTA 2 # HABITACI??N NI??O # Padres Muertos. // Ni??os desconsolados buscando a sus padres de la oscuridad.

# Una noche de tormenta, en una habitaci??n infantil, juguetes por el suelo, sangre, condones, botellas de vino. The kid is crying on the bed.

### // ??Qu?? hace una mujer tan hermosa sola en este lugar? // ??Estudias o trabajas? // ??D??nde est??n tus alas? // Disculpa... eh... es que eres tan bella que se me olvid?? lo que iba a decir. // Por tentaciones como t??, hay tantos pecadores como yo. // ??Crees en el amor a primera vista? ??O deber??a volver a pasar? // 



# Frases de Padres con sus hijos: // Eres la personita m??s valiente que conozco ??No es as??? hombret??n. // Dame un abrazo. // Es solo una amiga. // Vamos a investigar lo que te da miedo. // Te lo prometo, pase lo que pase, te mantendr?? a salvo. // ??Qu?? puedo hacer para que te sientas seguro? // Nunca te voy a abandonar tont??n, a pesar de lo que ocurra esta noche o cualquier otra, siempre voy a ser tu padre y te amar?? y te proteger?? hasta el fin de mis dias. // Recuerda que ya eres un chico grandote. comp??rtate, y saluda a la dama. //



# Una noche de tormenta, en un callej??n oscuro, te encuentras un hombre sin rostro que te dice, "Necesito tu ayuda", elijas lo que elijas, ves como gira su rostro y este est?? completamente destrozado con el pulm??n perforado. "Habla con mi hijo". Y desaprece al cruzar el callej??n.

#Sin poder elegir otra cosa, sigues adelante y cruzas el callej??n, al final de este, encuentras un ni??o llorando desconsoladamente en una escalinata en medio de la lluvia sujetando un trozo de papel. Detr??s de ??l se encuentra la puerta semiabierta con luz, la puerta por la que debes regresar. Cuando te acercas al ni??o tienes la opci??n de preguntar que le ocurre. Con  ojos llorosos te pregunta d??nde est?? su padre... porqu?? se ha ido? por qu?? lo ha abandonado? Promete ser un ni??o bueno si regresa.

# Frases mientras vas encontrado objetos por el suelo: // Pap??, hay algo bajo la cama... // Pap??... Esta mujer me da miedo... // Pap??, cada vez que viene esta mujer a casa oigo voces en mi habitaci??n... // Sus ojos se han vuelto de otro color pap??. // Por favor, no te vayas con ella, no me dejes solo... //


# Hallway: Ground (Toys)
    # Pelota de f??tbol: "Es solo una amiga"
    # Guerrero de peluche: "Te lo prometo, pase lo que pase, te mantendr?? a salvo."
    # Consola port??til: "Eres la personita m??s valiente que conozco, ??No es as?? hombret??n?"
    # Tira-chinas: "Tranquilo, ya me he encargado del monstruo del armario, nunca m??s te va a molestar."
    # Piano de juguete: Recuerda que ya eres un chico grandote; comp??rtate, y saluda a la dama.
    # Robot Juguete: ??Qu?? puedo hacer para que te sientas seguro?

# Hallway: Wall Photos
    # ??Estudias o trabajas?
    # Disculpa, eh... es que eres tan bell que se me olvid?? que te iba a decir.
    # Por tentaciones como t??, hay tantos pecadores como yo.
    # ??Crees en el amor a primera vista? ??O deber??a volver a pasar?
    # ??D??nde est??n tus alas?

# Kid Room:
    # Condom: Cada vez que viene esta mujer a casa, oigo voces en mi habitaci??n...
    # Wine Bottle: Por favor, no te vayas con ella, no me dejes solo...
    # Tobacoo: Hay alguien en el armario...
    # Drugs: Hay algo bajo la cama...
    # Blood on ground: Pap??, Esta mujer me da miedo...
    # C??ctel: Sus ojos se han vuelto de otro color pap??.

# Kid on the bed crying
    # ??Quien eres? ??Qu?? haces en mi habitaci??n? ??Sabes d??nde est?? mi padre?



## PUERTA 3 # CAPILLA # Maridos (Infieles) Muertos. // Esposas buscando a sus maridos (Grito Bruja Dross) de la oscuridad.

# Ramos de flores, bombones, pastel por el suelo, (anillos de boda). La esposa lleva el velo.

# Frases mientras miras los objetos: // Amor es solo una palabra, hasta que llegaste para darle sentido. // Te quiero, no por quien eres, sino por quien soy cuando estoy contigo. // Si volviera a nacer, te volver??a a elegir. // Quiero envejecer contigo. // De nadie ser??, s??lo de ti, hasta que mis huesos se vuelvan cenizas y mi coraz??n deje de latir. // Qui??reme cuando no lo merezca, porque ser?? cuando realmente te necesite. // Hoy, entrelazo mi vida con la tuya, no solo como tu esposo, sino como tu amigo, amante y confidente. D??jame ser el hombro en el que te apoyas, la roca sobre la que descansas, el compa??ero de tu vida. Desde este d??a caminar?? junto a ti. // 

# Al entrar te encuentras dentro de una peque??a capilla iluminada por un sol radiante. A lo lejos se encuentra el altar, d??nde hay una nuvia llorando desconsoladamente. A medida que avanzas ves hombres desnudos encima de tu cabeza, completamente p??lidos, como si fueran cad??veres sin rostro. Detr??s del altar, descubres que hay una puerta iluminada. Al pasar por el altar te encuentras a la novia, si te acercas y le preguntas que le ocurre, Te pregunta d??nde est?? su esposo... D??nde est?? el hombre al que ama, porque lo ha abandonado en el d??a m??s importante de su vida, que ha hecho para que deje de amarla. AL mirar atr??s descubres como la iglesia entera se va oscureciendo y cada vez hay m??s hombres cadav??ricos. La nuvia ya no est??, y solo queda la puerta iluminada. El ruido en la oscuridad vuelve a ce??irse cerca.


    # Ramo de flores: Te quiero, no por quien eres, sino por quien soy cuando estoy contigo.
    # Bombones: Amor es s??lo una palabra, hasta que llegaste para darle sentido.
    # Pastel de bodas por el suelo: Si volviera a nacer, te volver??a a elegir.
    # Arras de boda: Qui??reme cuando no lo merezca, por que ser?? cuando realmente te necesite.
    # Anillo de boda: Hoy entrelazo mi vida con la tuya, no s??lo como tu esposo, sino como tu amigo, amante y confidente. D??jame ser el hombro en el que te apoyas, la roca sobre la que descansas, el compa??ero de tu vida. Desde este d??a caminar?? junto a ti.
    # No s??: Quiero envejecer contigo.
    




## TERMINAR PUERTAS.

# Cuando todas las puertas han terminado, vuelves al mismo sitio, con las tres puertas oscuras y completamente podridas. Ves como la luz se va apagando y empiezas a oir el ruido de la oscuridad acerc??ndose a ti (Voz gritos bruja loca), hasta que despiertas de golpe y tienes delante de ti un fuerte luz procedente de una peque??a linterna, y una voz masculina pregunt??ndote, ??C??mo te llamas? ??Cuantos dedos ves? Parece que ha sido un simple desmayo... No te levantes a??n. Luego ves a Neus. ??Te encuentras bien Jordi? Me has dado un susto de muerte cuando te has caido desmayado justo antes de subir las escaleras. Los doctores te recomiendan que no vuelvas a subir a ning??na atracci??n que pueda ser peligrosa. te hacen tomar una pstilla y te dan un n??mero de tel??fono por si vuelve a ocurrir algo parecido, para que luego peudan llamar a la ambulancia si vuelve a ocurrir.

# Una vez alejados el cuerpo de sanidad, Neus vuelve a preguntarte si te encuentras bien. Intentas buscar a esa enorme mujer pechugona y no la encuentras por ning??n lado. Le preguntas a Neus si la has visto irse. Ella te dice que s?? que es verdad que no est??, pero que en su momento no se ha fijado a d??nde se hab??a ido, s??lo se preocupaba por que te ocurr??a a ti. Has estado como 8 minutos inconsciente.

# neus te comenta que ya se ha hecho tarde y que lo mejor ser??a dar por finalizada la cita. Cuando os dirig??s hacia la entrada te fijas en la noria que se encuentra cerca de la salida del parque. Recuerdas que ella te hab??a dicho que no os pod??ais ir de ah?? sin que os subi??rais al menos una vez en esa atracci??n. Decides decirle que pod??is subir a esa atracci??n, que tampoco es tan peligrosa. Cuando os sub??s y est??is en la cima, te pide disculpas por todo lo currido y te agradece que hayas venido hasta ah??. Luego te insinua que durante toda la cita, no has sido capaz de hacerle ni siquiera un beso... Cuando est??is cerca de besaros un foco de luz os ilumina la cara con un enorme estruendo, enormes fuegos de artificio se est??n lanzando en la ciudad al estar tan cerca de Sant Joan, en ese instante decides besarla bajo los fuegos de artificio en uno de los lugares m??s altos de la ciudad.

# Poco despu??s de besarla, recibes un mensaje en el m??vil. Al abrir la aplicaci??n descubres que es una foto de D??dac desnuda sonriente en el piso de la pedrera donde vive Neus. Con el siguiente mensaje. "Os estamos esperando".

# Os?! Neus te pregunta qu?? ocurre y decides mostrarle el m??vil. Su rostro cambia completamente. Su cuerpo empieza a temblar. Unas l??grimas empiezan a dearramarse por sus mejillas.

#Le preguntas si se encuentra bien.

# Neus dice... Nos ha encontrado.

# Dices que tienes que ir al piso a rescatar a D??dac. Ella te agarra del brazo. Si vamos all??, todos vamos a morir. No puedo dejar a D??dac. NO! NO PUEDO ABANDONAR A MI AMIGO POR MUY GILIPOLLAS QUE SEA! QUE CLASE DE PERSONA SOY?! Neus te dice... tienes raz??n... Su cuerpo sigue temblando. Al fin y al cabo si sabe d??nde vivo, tambi??n sabr?? d??nde estoy ahora... ser??a absurdo intentar huir... al final me ha encontrado... Intentas inutilmente animarla, pero tus esfuerzos son en vano, apenas te oye, apenas escucha nada... su mirada est?? como perdida, como un animal bloqueado en un rinc??n por el miedo, incapaz de reaccionar. La agarras por la mano y sal??s de la atracci??n, decides tomar un taxi que os lleve directamente hasta la Pedrera. ## FINAL DEMO

#Durante todo el transcurso del viaje, Neus sigue en modo shock sin saber qu?? decir ni d??nde mirar... Por un instante te mira a los ojos, para luego aparatarlos de golpe. Si intentas hablar con ella, te aparta la mirada. ??He dicho algo malo...?