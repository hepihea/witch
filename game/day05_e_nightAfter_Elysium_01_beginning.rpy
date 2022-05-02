
    # if _preferences.language == "english":
    #     call endtranslation
    # else:
    #     call WIIP

default night05_NeusLastDate_Noria_Visions_SawNothing = False
default night05_NeusLastDate_Noria_Visions_SawBlondOne = False
default night05_NeusLastDate_Noria_Visions_SawDidac = False

default night05_NeusLastDate_Noria_Visions_MeritxellSawConfession = False

default night05_NeusLastDate_ElysiumGoing = False

default night05_elysium_WhatNow_After_BlowjobDisgusting = False # She will not suck your dick.
default night05_elysium_WhatNow_After_BlowjobDisgusting02 = False # You will accept her blowjob even if you dislike it.

####
default night05_elysium_DidacDone_Question_DidacStartSexNo = False # You told her started minigame but without Sex
default night05_elysium_DidacDone_Question_DidacStartSexYes = False  # You told her started minigame with SEX.

default night05_elysium_DidacDone_Question_DidacStartSexYes_ILikeYou = False  # You told her you like her after telling you had sex with Didac.
default night05_elysium_DidacDone_Question_DidacStartSexYes_FallingInLove = False  # You told her you're falling in lov with her after...
default night05_elysium_DidacDone_Question_DidacStartSexYes_InLove = False  # you told her you're in love with her after...

default night05_elysium_DidacDone_Question_DidacStartNO = False  # You told her you did not have sex with Didac.

default night05_elysium_NeusStupid_FittingRoomDidac_FuckherConsent = False # You told her you fucked her in fitting room.
default night05_elysium_NeusStupid_FittingRoomDidac_ButtocksMast = False  # You told her you masturbate with her buttocks.
default night05_elysium_NeusStupid_FittingRoomDidac_MastBoth = False  # You told her you masturbated both of you.
default night05_elysium_NeusStupid_FittingRoomDidac_NothingTold = False  # You told her nothing happened.

default afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told = False

default night05_elysium_pederast_Cond = False # You call Neus Pederast.

default night05_NeusLastDate_ElysiumDontWant_Cond = "" # If you told here you don't want sex. You can go with Father or have sex with her

default night05_elysium_AllWasALie_Cond = False
default night05_elysium_whyAmISoSpecial_Cond = False
### night04_NeusInterview_Incest_Answer_IDoubtIWouldFallInLove
### night04_NeusInterview_Incest_Answer_YesIfReallyInLove

###

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

label night05_NeusLastDate_Noria_SaveDidac_No:

    pt "¡¿CÓMO?!"

    pt "¡¿Es que se me ha ido completamente la pinza?!"

    pt "¡¡Estamos hablando de Dídac!!"

    pt "¡Ya sé que lo que le hizo a Neus es horrible!"

    pt "Pero..."

    pt "¡Jamás abandonaría a Dídac!"

    pt "Le daría de hostias,"

    pt "pero abandonarle,"

    extend " sabiendo que lo van a matar..."

    pt "¡¿Quién diablos está tomando decisiones por mí?!"

    call screen night05_NeusLastDate_Noria_SaveDidac_02_Question()


screen night05_NeusLastDate_Noria_SaveDidac_02_Question():

    on "show":
        action MouseMove(x=400, y=400, duration= 0.5)

    timer 1.5 repeat True action MouseMove(x=400, y=400, duration= 0.75)

    add "gui/button/choice_idle_background.png" xalign .5 yalign .65

    add "gui/button/choice_idle_background.png" xalign .5 yalign .35

    textbutton (_("<Definitivamente, abandonar a Dídac a su suerte>")):
        xalign .5 
        yalign .35 
        action Jump("night05_NeusLastDate_Noria_SaveDidac_No_02")

    textbutton (_("No puedo Neus.")):
        xalign .5 
        yalign .65
        action Jump("night05_NeusLastDate_Noria_SaveDidac_After")


label night05_NeusLastDate_Noria_SaveDidac_No_02:

    call afternight05_Elysium_Sex_previous

    $ night05_NeusLastDate_ElysiumGoing = True

    #########################################################

    if config.version < "00.99.99": #For FUTURE
        call endupdatescript
    
    #######################################################

    #call endillustrations

    # jump night05_NeusLastDate_Noria_SaveDidac_02_Question

    # scene day05
    # with fade

    # stop music fadeout 3.0
    # $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    # $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    # $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    # $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    # $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    # $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ ntlong = 5

    if night05_NeusLastDate_Noria_Not == True:
        $ p_neuspos = "neus_exp_"
    else:
        $ p_neuspos = "n_s_exp_"

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

    p "¿Estás segura que no hay otra opción?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx03
        $ nteye = "front02"
        call gensex_oral_n_frontHead_exp_tears_tears

    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx03
        $ nteye = "front02"
        call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Créeme,"

    extend " si la hubiera,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front02"
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx03
        $ nteye = "front02"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "no te lo pediría."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Talkingx06
        show n_s_exp_eyebrows sadx02
    $ nteye = "right01"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Nunca le he deseado ningún mal a tu amigo."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_eyebrows sadx03
    $ nteye = "right03"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Solo quería darle una pequeña lección,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx04
    $ nteye = "right04"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "solo eso."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx03
        show n_s_exp_eyebrows sadx04
    $ nteye = "right05"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Pero ahora..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sadbiting_Silentx05
        show n_s_exp_eyebrows sadx04
    $ nteye = "front07"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Silentx05
        show n_s_exp_eyebrows sadx06
    $ nteye = "front08"
    call gensex_oral_n_frontHead_exp_tears_tears

    if music_play != "bentAndBroken":
        play music "audio/music/kevinmacleod/creepy/bentAndBroken.ogg" fadein 0.5 fadeout 0.5
        $ music_play = "bentAndBroken"

    show border_darkness:
        truecenter
        subpixel True
        zoom 2.0
        easein_quad 15.0 zoom 0.5
    with dissolve

    dad "¡Le importa una mierda tu amigo!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex01
    else:
        show n_s_exp_mouth sadbiting_Silentx02
        show n_s_exp_eyebrows surprisex01
    $ nteye = "front01"
    call gensex_oral_n_frontHead_exp_tears_tears

    with vpunch
    p "Ugh..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_eyebrows sadx02
    $ nteye = "front02"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    n "Una repentina jaqueca emerge de nuevo en tu cabeza."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows sadx01
    else:
        show n_s_exp_mouth sad_Silentx02
        show n_s_exp_eyebrows sadx01
    $ nteye = "front03"
    call gensex_oral_n_frontHead_exp_tears_tears
    show border_darkness:
        block:
            ease 20.5 zoom 0.7
            ease 15.8 zoom 1.0
            ease 16.9 zoom 0.6
            ease 18.6 zoom 1.1
            repeat
    with dissolve

    dad "¡Que te cuente la verdad!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx02
    else:
        show n_s_exp_mouth sad_Silentx03
        show n_s_exp_eyebrows sadx02
    $ nteye = "front04"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "Maldita sea..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx02
        show n_s_exp_eyebrows sadx05
    $ nteye = "front05"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "[protname]..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyebrows sadx06
    else:
        show n_s_exp_mouth sad_Silentx07
        show n_s_exp_eyebrows sadx06
    $ nteye = "front08"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "..."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Talkingx03
        show n_s_exp_eyebrows sadx04
    $ nteye = "front05"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Es él,"

    extend " ¿Verdad?"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx05
    $ nteye = "front08"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Tendría que haberme dado cuenta antes."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows angryx03
    else:
        show n_s_exp_mouth sad_Talkingx08
        show n_s_exp_eyebrows angryx03
    $ nteye = "front06"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "¡Soy una estúpida!"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx03
    else:
        show n_s_exp_mouth sad_Talkingx06
        show n_s_exp_eyebrows sadx03
    $ nteye = "left01"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Me creía tan perfeccionista;"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sad_Talkingx05
        show n_s_exp_eyebrows sadx04
    $ nteye = "left03"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "lo había intentado hacer todo tan bien,"

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx05
    $ nteye = "left04"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "que pensaba que era imposible que nos hubiera encontrado."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx04
    else:
        show n_s_exp_mouth sadbiting_Silentx05
        show n_s_exp_eyebrows sadx04
    $ nteye = "left05"
    call gensex_oral_n_frontHead_exp_tears_tears
    show border_darkness:
        truecenter
        block:
            ease 18.5 zoom 0.7
            ease 14.8 zoom 1.0
            ease 12.9 zoom 0.6
            ease 11.6 zoom 1.1
            repeat
    with dissolve

    dad "No te la creas."

    if night05_NeusLastDate_Noria_Not == True:
        show neus_exp_mouth sadbiting_Silentx07
        show neus_exp_eyebrows sadx05
    else:
        show n_s_exp_mouth sadbiting_Silentx07
        show n_s_exp_eyebrows sadx05
    $ nteye = "front08"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    dad "Es una mentirosa compulsiva."

##
    if night05_NeusLastDate_Noria_Not == False:

        
        $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
        $ renpy.music.set_volume(0.0, delay=0.01, channel='sfx1')
        pause 0.01
        $ renpy.music.set_volume(0.4, delay=20.0, channel='sfx1')

        scene bg night05_bg_wheel_far:
            subpixel True
            truecenter
            zoom 1.0
            ease_quad 10.0 zoom 0.5
        show border_darkness:
            subpixel True
            truecenter
            zoom 1.0
            block:
                ease 8.5 zoom 0.7
                ease 12.8 zoom 1.0
                ease 11.9 zoom 0.6
                ease 8.6 zoom 1.1
                repeat
        with fade

        n "Termináis saliendo de la atracción"

        n "y a los pocos metros:"

        scene bg night05_bg_tibidabo_park_00:
            truecenter
            zoom 0.6 xpos 0.6 ypos 0.4
        $ Pedrera_char_Cond = "NeusFarRight"
        call Pedrera_char_lab

    $ p_neuspos = "neus_exp_"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front00"
    call gensex_oral_n_frontHead_exp_tears_tears

    show border_darkness:
        truecenter
        subpixel True
        zoom 1.0
        block:
            ease 9.5 zoom 0.7
            ease 8.8 zoom 1.2
            ease 10.9 zoom 0.6
            ease 8.6 zoom 1.1
            repeat

    with vpunch

    p "¡Ugh...!"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    dad "Que te cuente qué pasó realmente en el baño con Dídac."

    scene black
    with fade

    n "Sientes sus manos posándose sobre ambos lados de tu cráneo,"

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show border_darkness:
        subpixel True
        truecenter
        block:
            ease 9.5 zoom 0.7
            ease 10.8 zoom 1.2
            ease 8.9 zoom 0.6
            ease 9.6 zoom 1.1
            repeat
    with fade

    n "forzándote a bajar la cabeza para acariciar su cálida frente con la tuya."

    show n_closefromup_mouth sad_Talkingx001
    show n_closefromup_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Shhh..."

    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Tranquilízate."

    $ renpy.music.set_volume(0.02, delay=10.0, channel='sfx1')

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Es probable que esto no evite que conecte contigo,"

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx06
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero como mínimo hará que su influencia y su voz,"

    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "no sean más que un eco indescifrable."

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al menos hasta que lleguemos,"

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "es lo único que puedo hacer."

    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿A dónde vamos?"

    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "A un lugar que preferiría no haber tenido que ir..."

    if music_play != "dayOfChaos":
        play music "audio/music/kevinmacleod/creepy/dayOfChaos.ogg" fadein 1.0 fadeout 1.0
        $ music_play = "dayOfChaos"

    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears

    show border_darkness:
        truecenter
        block:
            ease 3.2 zoom 1.5
            ease 2.8 zoom 0.7
            ease 3.9 zoom 1.8
            ease 1.6 zoom 0.8
            repeat
    with dissolve

    dad "A dónde..."

    extend " Vas..."

    extend " Sacrificará..."

    show n_closefromup_mouth sad_Silentx08
    show n_closefromup_eyebrows angryx02
    $ nteye = "front08"
    call n_closefromup_tears_tears

    show border_darkness:
        truecenter
        block:
            ease_quad 1.2 zoom 1.0
            ease_quad 1.8 zoom 0.5
            ease_quad 1.9 zoom 1.4
            ease_quad 1.6 zoom 0.5
            repeat
    with dissolve

    ne "Ughh..."
    
    dad "No..."

    show n_closefromup_mouth sad_Silentx09
    show n_closefromup_eyebrows angryx03
    $ nteye = "front06"
    call n_closefromup_tears_tears
    show border_darkness:
        truecenter
        block:
            easein_quad 0.35 zoom 0.5
            easeout 0.5 zoom 0.9
            easein_quad 0.3 zoom 0.5
            easeout 0.5 zoom 0.95
            repeat
    with dissolve

    extend " Morir..."

    show border_darkness:
        truecenter
        block:
            easein_quad 0.1 zoom 0.5
            easeout 0.2 zoom 0.7
            easein_quad 0.1 zoom 0.5
            easeout 0.2 zoom 0.8
            repeat
    with dissolve

    extend " escuches..."

    if music_play != "atlanteanTwilight":
        play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 1.0 fadeout 4.0
        $ music_play = "atlanteanTwilight"

    $ renpy.music.set_volume(0.3, delay=10.0, channel='sfx1')

    show n_closefromup_mouth sad_Silentx05
    show n_closefromup_eyebrows angryx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    show border_darkness:
        truecenter
        easein_quad 60 zoom 2.5
        repeat
    with dissolve

    n "Esa extraña voz se va diluyendo,"

    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_eyebrows serious
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    n "al mismo tiempo que el dolor de cabeza se va apaciguando."

    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    n "Apenas oyes reminiscencias de una voz lejana que son prácticamente imposibles de entender."

    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows normal
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Tranquilo,"

    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx03
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "pronto dejarás de escucharle del todo."

    if music_play != "lostFrontier":
        play music "audio/music/kevinmacleod/sad/lostFrontier.ogg" fadein 1.5 fadeout 1.5
        $ music_play = "lostFrontier"

    $ saturation_tint_level = "reddish"
    call saturation_ting_values_check

    play sound "audio/characters/didac/scream_au03.ogg"

    scene ped_pain_didac:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0 ypos 1.0
        easeout_bounce 5.0 zoom 2.0 xpos 1.8 ypos 1.8 # Closer
    show border_darkness_reddish:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.0 zoom 1.0
            ease 1.8 zoom 0.7
            ease 0.8 zoom 1.0
            ease 1.0 zoom 0.9
            repeat
    with vpunch

    
    d "{size=40}¡Aarrghh!{/size}"

    scene black
    with hpunch

    $ saturation_tint_level = "dark"

    n "Te agarra de la mano y te arrastra de nuevo hasta el {b}funicular del Tibidabo{/b}."

    scene night05_bg_station_funicular:
        subpixel True
        truecenter
        xzoom -1.0
        ####zoom 0.8 xpos 0.2 ypos 0.6
        zoom 0.9 xpos 0.85 ypos 0.3
        easein_quad 10.0 zoom 0.6 xpos 0.6 ypos 0.4
    with fade

    p "Si cogiéramos un taxi,"

    extend " quizás llegaríamos más temprano."

    p "¿No crees?"

    $ ntlong = 1

    $ p_neuspos = "neus_exp_"

    scene bg night05_bg_station_funicular:
        truecenter
        xzoom -1.0
        zoom 0.6 xpos 0.6 ypos 0.4
    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left01"
    call n_closefromup_tears_tears

    with Dissolve(0.5)

    ne "Seguro que sí."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ saturation_tint_level = "reddish"

    play sound "audio/characters/didac/scream_au15.ogg"

    $ Pedrera_char_Cond = "DidacPain"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx09
    show didacf_eyes 07
    show didacf_pupils front07
    show didacf_eyebrows angryx03

    show border_darkness_reddish:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.0 zoom 1.0
            ease 1.8 zoom 0.7
            ease 0.8 zoom 1.0
            ease 1.0 zoom 0.9
            repeat
    with vpunch
    with vpunch

    d "{size=50}¡AARrrghh!{/size}"

    $ saturation_tint_level = "dark"

    scene bg night05_bg_station_funicular:
        truecenter
        xzoom -1.0
        zoom 0.6 xpos 0.6 ypos 0.4
    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with fade

    ne "Pero no me fío de coger un método de transporte que no sea público,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "estando Padre en ciudad,"

    extend " y siendo mañana el solsticio."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Crees que podría poseer a un taxista?"

    $ saturation_tint_level = "reddish"

    if pl.mp > pl.dp:

        play sound "audio/characters/didac/scream03.ogg"

        $ Pedrera_char_Cond = "TxellPain"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx10
        show m_exp_eyes 06
        show m_exp_piris front06
        show m_exp_eyebrows angryx06

    else:

        play sound "audio/characters/didac/scream03.ogg"

        $ Pedrera_char_Cond = "DidacPain"
        call Pedrera_char_lab

        show didacf_mouth sad_Talkingx08
        show didacf_eyes 06
        show didacf_pupils front06
        show didacf_eyebrows angryx03

    show border_bloddy01:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.0 zoom 1.5
            ease 1.8 zoom 1.2
            ease 0.8 zoom 1.5
            ease 1.0 zoom 1.4
            repeat

    show border_darkness_reddish:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.1 zoom 1.0
            ease 1.7 zoom 0.7
            ease 0.6 zoom 1.0
            ease 1.2 zoom 0.9
            repeat
    
    with vpunch
    with vpunch

    if pl.mp > pl.dp:

        tx "{size=65}¡¡AAAAhhh!!{/size}"
    else:

        d "{size=65}¡¡AAAAhhh!!{/size}"

####

    $ saturation_tint_level = "dark"

    scene bg night05_bg_station_funicular:
        truecenter
        xzoom -1.0
        zoom 0.6 xpos 0.6 ypos 0.4
    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with fade

    ne "Cosas peores le he visto hacer cuando está nervioso,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "y créeme,"

    extend " no le suele ocurrir a menudo."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ saturation_tint_level = "reddish"

    play sound "audio/characters/didac/scream_au16.ogg"

    if pl.mp > pl.dp:
        $ Pedrera_char_Cond = "TxellPain"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx12
        show m_exp_eyes 07
        show m_exp_piris front07
        show m_exp_eyebrows angryx06

    else:

        $ Pedrera_char_Cond = "DidacPain"
        call Pedrera_char_lab

        show didacf_mouth sad_Talkingx09
        show didacf_eyes 07
        show didacf_pupils front07
        show didacf_eyebrows angryx03

    show border_bloddy01:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.0/2 zoom 1.5
            ease 1.8/2 zoom 1.2
            ease 0.8/2 zoom 1.5
            ease 1.0/2 zoom 1.4
            repeat

    show border_darkness_reddish:
        subpixel True
        truecenter
        zoom 0.5
        block:
            ease 1.1/2 zoom 1.0
            ease 1.7/2 zoom 0.7
            ease 0.6/2 zoom 1.0
            ease 1.2/2 zoom 0.9
            repeat
    
    with vpunch
    with vpunch
    if pl.mp > pl.dp:

        tx "{size=80}¡¡¡AARRGGGHH!!!{/size}"

    else:

        d "{size=80}¡¡¡AARRGGGHH!!!{/size}"

    ##

    $ saturation_tint_level = "dark"
    scene bg night05_bg_station_funicular:
        truecenter
        xzoom -1.0
        zoom 0.6 xpos 0.6 ypos 0.4
    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with fade

    ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve
    
    ne "Sigue intentando comunicarse contigo,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Verdad?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_NeusLastDate_Noria_Visions_question:

        pt "¿Qué le digo?"

        "Estoy viendo a Meritxell." if (pl.mp > pl.dp) and (afternoon04_MACBA_TxellName_Know == True):

            call p_Help

            $ night05_NeusLastDate_Noria_Visions_MeritxellSawConfession = True

            if night05_Interrogation_TxellName_Cond == False:
                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
            else:
                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
            with dissolve

            ne "¿A Meritxell?"

            if night05_Interrogation_TxellName_Cond == False:

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Sabes su nombre...?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "Sí..."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows sadx01
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                $pl.ch_pts("np",-2)

                menu night05_NeusLastDate_Noria_Visions_Meritxell_question:

                    "Pero tranquila, no hicimos nada, solo quería hablar con ella.":
                        call p_Help

                        show neus_exp_mouth sadbiting_Silentx03
                        show neus_exp_eyebrows sadx02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $pl.ch_pts("np",3)

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Lo siento."

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx02
                        $ nteye = "right01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "A veces me siento una estúpida cuando siento estos celos..."

                        show neus_exp_mouth sadbiting_Silentx04
                        show neus_exp_eyebrows sadx03
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        if FuckM_Start_Cond: # NOT_FINISHED, FUTURE UPDATE, since you can have Start but without intercourse.

                            pt "Por lo menos se lo ha creído..."

                            if FuckH_Start_Cond:

                                pt "Si hasta me follé a la transexual de su ex-novia..."

                        if FuckM_Start_Cond and FuckH_Start_Cond == False:

                            pt "Lo que sí me follé es a la transexual de su novia..."

                            pt "Pero tampoco hace falta entrar en esos detalles..."

                        if afternight04_sexbattle_started == True:

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pt "Aunque mejor no comentarle por ahora lo que sí hice con Dídac..."

                            if afternight04__Pussy_dick_med_Done == 0:

                                show neus_exp_mouth sadbiting_Silentx06
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                pt "Aunque tampoco se la llegué a meter dentro..."

                                pt "No sé si realmente eso contaría como..."

                                extend " ¿Infidelidad?"

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "left05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pt "Tampoco es que estemos saliendo juntos..."

                            pt "¿O sí lo estamos...?"


                    "Sí, hay cosas que pasaron entre ella y yo que debo contarte." if FuckM_Start_Cond == True:
                        call p_Help

                        ne "..."

                        $pl.ch_pts("np",-5)

                        ne "Tú..."

                        # NOT_FINISHED. FUTURE UPDATE

        "Estoy viendo a la rubia de clase." if pl.mp > pl.dp:

            call p_Help

            $ night05_NeusLastDate_Noria_Visions_SawBlondOne = True

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if afternoon04_MACBA_TxellName_Know:

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                pt "Es mejor no decirle que sé su nombre,"

                show neus_exp_mouth sad_Silentx08
                show neus_exp_eyebrows sadx05
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                pt "tendría que darle demasiadas explicaciones..."

            else:

                show neus_exp_mouth sad_Silentx08
                show neus_exp_eyebrows sadx07
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex02
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Por tu reacción,"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "parecería que la conoces mejor,"

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx05
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            p "que como simple compañera de clase."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

        "<Describirle cómo ves a Dídac en tu mente>" if (pl.mp < pl.dp):

            call p_Help

            $ night05_NeusLastDate_Noria_Visions_SawDidac = True

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "Estoy viendo a Dídac con moratones en la cara y..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows sadx04
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo siento mucho..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx03
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "mucho más de lo que te imaginas."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero de verdad..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx03
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "Lo sé,"

            extend " lo sé..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

        "Tranquila, no estoy viendo nada importante.":

            $ night05_NeusLastDate_Noria_Visions_SawNothing = True

            call p_Help


    if night05_NeusLastDate_Noria_Visions_SawNothing == True:

        show neus_exp_mouth sad_Silentx01
        show neus_exp_eyebrows sadx01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "En realidad estas imágenes,"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx03
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        p "me ayudan a comprender mejor que quizás hubiera sido una mala idea ir allí..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Gracias por entenderlo."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx05
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pt "Aún así..."

    else:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyebrows sadx01
        $ nteye = "right02"
        call n_closefromup_tears_tears
        with dissolve

        ne "No..."

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx02
        $ nteye = "right03"
        call n_closefromup_tears_tears
        with dissolve

        ne "No importa..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        ne "Como te he dicho,"

        extend " ya es demasiado..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "right04"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        if afternoon04_MACBA_TxellName_Know == False:

            pt "Está claro que me oculta algo."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx01
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "No hay nada que podamos hacer por Dídac..."

        if night05_NeusLastDate_Noria_Visions_SawDidac == False:

            extend " ni por ella..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "left04"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    jump night05_NeusLastDate_FunicularLeaving

label night05_NeusLastDate_FunicularLeaving:

    # Ya sentados en el Funicular.

    $ renpy.music.set_volume(0.01, delay=8.0, channel='sfx1')

    if music_play != "darkTimes":
            play music "audio/music/kevinmacleod/sad/darkTimes.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "darkTimes"

    scene night05_bg_station_funicular_out:
        subpixel True
        truecenter
        zoom 0.9 xpos 0.1 ypos 0.1 # Door Station
        #zoom 0.8 xpos 0.2 ypos 0.6
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    p "¿A dónde vamos, Neus?"

    $ saturation_tint_level = "verydark"

    scene bg night05_bg_station_funicular_out:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab
    # show neus_arm_r sd:
    #     neus_body_atright_position
    # show neus_body sd_default:
    #     neus_body_atright_position
    # show neus_head:
    #     neus_body_atright_position
    # show neus_arm_l sd:
    #     neus_body_atright_position

    # show neus_exp_blush 01:
    #     neus_exp_atright_position
    # show neus_exp_mouth sad_Talkingx03:
    #     neus_exp_atright_position
    # show neus_exp_eyes 01:
    #     neus_exp_atright_position
    # show neus_exp_iris left01:
    #     neus_exp_atright_position
    # show neus_exp_tears empty:
    #     neus_exp_atright_position
    # show neus_exp_eyebrows surprisex01:
    #     neus_exp_atright_position
    # show neus_exp_glasses:
    #     neus_exp_atright_position
    # show neus_exp_hairfront:
    #     neus_exp_atright_position


    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears

    with Dissolve(0.5)

    ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si te lo cuento,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "es probable que él lo descubra antes de que lleguemos."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque te haya bloqueado parcialmente el contacto con él,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "aún es posible que oiga y vea lo mismo que tú."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    # pause 0.2

    # show day05
    # with hpunch

    # # Imagen de Dídac o Txell siendo violado. # im_01e
 
    # pause

    # hide day05

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque de todos modos,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "me imagino que ya sabrá a dónde tengo pensado ir..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "No tengo demasiadas opciones,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "por desgracia..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Por lo que dices,"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "no suena un sitio muy seguro."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Desde luego que no."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Dime,"

    extend " ¿estás herido?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "No,"

    extend " tranquila."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "Estoy bien."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "No te pregunto eso."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Quiero saber si tienes alguna herida abierta,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "alguna parte de tu cuerpo dónde te hayas puesto recientemente alguna tirita,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "o en la que hayas sangrado, aunque sea superficialmente, estas últimas veinticuatro horas."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond:

        menu:

            "<Contarle que recibiste un puñetazo y sangraste por la nariz>":
                call p_Help

                $ afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told = True

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Bueno,"

                extend " ayer tuve una pelea con alguien y me sangró un poco la nariz."

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyebrows surprisex01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿En la nariz?"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows serious
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "Déjame ver."

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyebrows sadx01
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusSuperSuperClose"
                call Pedrera_char_lab

                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows sadx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with fade

                n "Levantas la cabeza para que pueda mirar con más atención tus fosas nasales."

                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx02
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "No parece que sangres,"

                extend " pero aún así es mejor ir con precaución."

                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows sadx01
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with dissolve

                n "De su bolso saca un pañuelo de papel."

                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "Por favor,"

                extend " no te tomes esto como algo desagradable,"

                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx04
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "créeme que es necesario."

                show n_closefromup_mouth sadbiting_Silentx09
                show n_closefromup_eyebrows sadx03
                $ nteye = "down05"
                call n_closefromup_tears_tears
                with dissolve

                n "Observas cómo se introduce ese objeto entre sus piernas bajo la falda,"

                show n_closefromup_mouth sadbiting_Silentx07
                show n_closefromup_eyebrows sadx01
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                n "y lo vuelve a sacar empapado en abundancia."

                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx01
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "Te prometo que me he duchado recientemente."

                if night05_Park_WC_Lawyer_Cunnilingus:

                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows normal
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "He pasado mi lengua por ahí,"

                    extend " sé lo limpio que está."

                    show n_closefromup_mouth happybiting_Silentx05
                    show n_closefromup_eyebrows suspiciousx01
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show n_closefromup_mouth happy_Talkingx06
                    show n_closefromup_eyebrows sadx01
                    $ nteye = "front06"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Tonto..."

                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows normal
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pero..."

                else:

                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows sadx01
                    $ nteye = "down05"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿Qué...?"

                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows sadx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                extend " ¿Qué pretendes hacer con eso?"

                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows sadx01
                $ nteye = "down05"
                call n_closefromup_tears_tears
                with dissolve

                n "Neus rompe el pañuelo y hace dos pequeñas bolitas con él."

                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows serious
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "Póntelos en la nariz."

                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows angryx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Intenta introducírtelos lo más profundamente que puedas,"

                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows serious
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "para que no sobresalga ni se vea."

                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¿Es algún truco erótico para que no deje de pensar en tu aroma vaginal?"

                show n_closefromup_mouth sadbiting_Silentx06
                show n_closefromup_eyebrows suspiciousx01
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                scene bg night05_bg_station_funicular_out:
                    truecenter
                    zoom 0.5 xpos 0.5 ypos 0.5

                $ Pedrera_char_Cond = "NeusFarRight"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows serious
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with fade

                ne "Es un truco para que no te maten, [protname]."

            "Que yo sepa no.":
                call p_Help

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows serious
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "Espero que estés seguro de ello."

    else:

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "No,"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        p "que yo sepa no."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows angryx01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        ne "Pues asegúrate de ello."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "Me estás asustando Neus..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Es de vital importancia que no tengas ninguna herida,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "hasta que lleguemos a la habitación del lugar a dónde te llevo."

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows serious
        $ nteye = "front03"
        call n_closefromup_tears_tears

        show coffeedrinking_front:
            truecenter
        with dissolve

        n "Obedeciendo tus palabras, metes esas dos bolitas en tu nariz."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows angryx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "Más adentro."

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows normal
        $ nteye = "front01"
        call n_closefromup_tears_tears
        hide coffeedrinking_front
        with dissolve

        p "Si me lo meto más adentro al final no me los podré sacar."

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows angryx01
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        ne "No te preocupes por eso."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx01
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows serious
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        p "De acuerdo."

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx01
        $ nteye = "front03"
        call n_closefromup_tears_tears
        show coffeedrinking_front:
            truecenter
        with dissolve

        n "Haces lo que te dice, pero por su expresión no parece muy convencida."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "NeusSuperSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows serious
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with fade

        ne "Déjame a mí."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_eyebrows sadx04
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "¿Qué...?"

        show n_closefromup_mouth sad_Silentx04
        show n_closefromup_eyebrows sadx02
        $ nteye = "front02"
        call n_closefromup_tears_tears

        show coffeedrinking_front:
            truecenter

        with vpunch
        p "¡UGHH...!"

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears

        hide coffeedrinking_front
        with dissolve

        ne "Lo siento."

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero de verdad,"

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx02
        $ nteye = "right02"
        call n_closefromup_tears_tears
        with dissolve

        ne "es una cuestión de vida o muerte."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_eyebrows sadx03
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        scene bg night05_bg_station_funicular_out:
            truecenter
            zoom 0.5 xpos 0.5 ypos 0.5

        $ Pedrera_char_Cond = "NeusFarRight"
        call Pedrera_char_lab

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "front0´8"
        call n_closefromup_tears_tears
        with fade

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Pero a dónde me llevas?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si en algún momento te cortaras con algo,"

    extend " o te hicieras una herida al caer,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "iríamos a una muerte segura."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "Neus..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Por favor,"

    extend " confía en mi."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Mientras no sangres por ninguna parte,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "al menos en este lugar,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "aún tenemos alguna esperanza de sobrevivir."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "A dónde vamos,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "es el único sitio dónde sé que mi Padre no tendrá narices de entrar."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left5"
    call n_closefromup_tears_tears
    with dissolve

    pt "Desde luego,"

    extend " eso no me reconforta..."

    if music_play != "nightOfChaos":
            play music "audio/music/kevinmacleod/creepy/nightOfChaos.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "nightOfChaos"

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx1')
    $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=2.0, channel='sfx1')

    scene night05_bg_station_tranvia:
        subpixel True
        truecenter
        zoom 0.8
        easein_quad 10.0 zoom 0.5
    with fade

    n "Después del funicular, volvéis a coger el bus"

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_hospital.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=4.0, channel='sfx1')

    scene night05_bg_station_sign:
        subpixel True
        truecenter
        zoom 1.2 xpos 0.5 ypos 0.5
        ease_quad 10.0 zoom 0.5
    with fade

    n "hasta la estación de la {i}avenida Tibidabo{/i},"

    scene bg el_plazaMet:
        subpixel True
        truecenter
        zoom 1.2 xpos 0.5 ypos 0.5
        ease_quad 10.0 zoom 0.5
    with fade

    n "y de ahí os dirigís en metro de nuevo a {i}Plaça Catalunya{/i}."

    n "Sin soltarte la mano, te arrastra por todo el andén repleto de gente,"

    n "hasta el final de este, dónde no hay nadie."

    scene bg el_plazaCam:
        subpixel True
        truecenter
        zoom 1.2 xpos 0.5 ypos 0.5
        ease_quad 10.0 zoom 0.5
    with fade

    n "Ahí te pide que mires a la cámara de seguridad que se encuentra encima de vosotros."

    n "Obedeces sin rechistar, hasta que te vuelve a empujar en dirección a la pared."

    p "Pero Neus..."

    ne "Confía en mi,"

    extend " por favor."

    scene bg el_plazaMet:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease_quad 10.0 zoom 1.0
    with fade

    n "Al volver la mirada atrás, te percatas de que toda la gente ahí presente,"

    n "ni si quiera se ha fijado en vosotros en ningún momento,"

    n "como si no existierais."

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    scene bg el_plazaWall:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease_quad 6.0 zoom 1.8
    with fade

    n "Sin miedo alguno, camina y te arrastra decidida hasta el muro."

    scene black
    with fade_short

    n "Cierras los ojos por inercia al ver en tu mente como os vais a meter una leche."

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    window hide dissolve
    pause

    n "Sientes que os detenéis abruptamente."

    p "..."

    p "¿Qué...?"

    $ ntlong = 0

    ne "Ya puedes abrir los ojos, [protname]."

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    scene bg el_cath_cave:
        truecenter
        zoom 2.0 xpos 0.9 ypos -0.3
        #ase_quad 20.0 zoom 0.5 xpos 0.5 ypos 0.5 # General
    with fade_long1s

    n "Al separar tus párpados, descubres que ya no estáis en el andén,"

    show bg el_cath_cave:
        subpixel True
        ease_quad 15.0 zoom 0.5 xpos 0.5 ypos 0.5 # General

    n "sino en un lugar oscuro, húmedo;"

    n "más parecido a una cueva,"

    n "iluminado tenuemente por unas antorchas con un fuego azulado,"

    n "y con unas escaleras rudimentarias que conducen hacia abajo."

    p "¿Qué-"

    extend "qué demonios...?"

    window hide dissolve
    pause

    $ saturation_tint_level = "veryDarkBlue"

    scene bg el_cath_cave:
        truecenter
        zoom 0.5

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    ne "Ahora bajaremos estas escaleras,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al llegar abajo,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "verás que al fondo de un largo pasillo habrá un portón enorme,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows serious
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "y seguramente habrá un o dos seguratas."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Una vez hayamos pasado esa enorme puerta,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "es muy importante que actúes de la forma más casual y normal posible."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Intenta no mantener la mirada a nadie durante demasiado tiempo,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "por muy curioso o extraño que te parezca lo que vayas a encontrar ahí dentro."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Y sobretodo,"

    extend " te repito,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "intenta no cortarte ni herirte con nada."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Neus..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya sé que tienes muchas preguntas,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero por favor,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "por ahora,"

    extend " confía en mi."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    pt "Tampoco es que tenga muchas más opciones..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg el_cath_hall:
        subpixel True
        truecenter
        #zoom 1.0 xpos 0.0 ypos 0.7
        zoom 0.34 xpos 0.5 ypos 0.5 # General view
    with fade

    n "Cuando llegáis al último escalón, os encontráis ese largo pasadizo que te ha mencionado,"

    show bg el_cath_hall:
        ease 20.0 zoom 2.0 xpos -1.37 ypos -0.38 # Door characters.

    n "repleto de decoración clásica y con un doble portón gigantesco de metal al fondo,"

    $ saturation_tint_level = "darkBlue"

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"

    n "custodiado por dos individuos realmente extraños."

    window hide dissolve
    pause

    # scene guard_alone:
    #     truecenter
    #     zoom 0.2 ypos 0.5

    scene guard_alone:
        subpixel True
        truecenter
        #zoom 2.0 ypos -0.338 # Down
        zoom 1.5 ypos 0.0 # Down
        ease_quad 10.0 zoom 2.0 ypos 1.3 # Head
    with fade

    n "Uno parece un gorila de casi dos metros,"

    window hide dissolve
    pause

    # scene butler_alone:
    #     truecenter
    #     zoom 0.2 ypos 0.5

    scene butler_alone:
        subpixel True
        truecenter
        zoom 2.0 ypos -0.332 # Down
        ease_quad 10.0 zoom 2.5 ypos 0.8 # Face
    with fade

    n "y el otro, algo bajito y mucho más raquítico,"

    n "con un cierto parecido a lo que te podrías esperar de alguien que no tiene pasión alguna por el deporte."

    window hide dissolve
    pause

    # show relda_body:
    #     transform_anchor True
    #     xalign 0.5 yalign 0.218 # Relda Eyes.
    #     alpha 0.5
    #     zoom 0.4 xpos 0.5 ypos 0.252 # Perfect ypose

    scene bg_el_cath_doorFront:
        truecenter
        zoom 0.5
        xpos 0.4 ypos 0.3

    show butler_body:
        transform_anchor True
        xalign 0.5 yalign 0.16 # Butler Eyes.
        zoom 0.4 xpos 0.2 ypos 0.31 # Perfect ypose

    show butler_exp_eyes 04:
        truecenter
        zoom 0.4 xpos 0.2 ypos 0.31 # Perfect ypose
    show butler_exp_piris front04:
        truecenter
        zoom 0.4 xpos 0.2 ypos 0.31 # Perfect ypose
    show butler_exp_eyebrows serious:
        truecenter
        zoom 0.4 xpos 0.2 ypos 0.31 # Perfect ypose
    show butler_exp_mouth sad_Silentx04:
        truecenter
        zoom 0.4 xpos 0.2 ypos 0.31 # Perfect ypose


    show guard_body:
        transform_anchor True
        xalign 0.5 yalign 0.111 # Guard Eyes.
        zoom 0.4 xpos 0.7 ypos -0.02

    show guard_exp_mouth sad_Silentx03:
        truecenter
        zoom 0.4 xpos 0.7 ypos -0.02

    with fade

    n "Os detenéis en frente de ellos,"

    show butler_exp_eyes 03
    show butler_exp_piris front03
    show butler_exp_eyebrows suspiciousx02
    show butler_exp_mouth sad_Silentx03
    with dissolve

    n "Neus le dedica una mirada intensa con sus ojos brillantes al tipo delgado."

    show butler_exp_eyes 04
    show butler_exp_piris front04
    show butler_exp_eyebrows normal
    show butler_exp_mouth sad_Talkingx04
    with dissolve

    sdel "La señorita puede entrar."

    show butler_exp_eyes 05
    show butler_exp_piris front05
    show butler_exp_eyebrows serious
    show butler_exp_mouth sad_Talkingx03
    with dissolve

    sdel "Pero el humano debe permanecer aquí fuera."

    show butler_exp_eyes 08
    show butler_exp_piris front08
    show butler_exp_eyebrows normal
    show butler_exp_mouth sad_Silentx03

    show guard_exp_mouth sad_Silentx04
    with dissolve

    sgor "Hmgrr..."

    n "El tipo más corpulento hace un gruñido más parecido al de un animal que al de una persona."

    show butler_exp_eyes 01
    show butler_exp_piris front01
    show butler_exp_eyebrows normal
    show butler_exp_mouth sad_Silentx02

    show guard_exp_mouth sad_Silentx03
    with dissolve

    ne "Dile a {b}Relda Eneri{/b},"

    extend " que {b}Elur{/b} quiere hablar con ella."

    show butler_exp_eyes 04
    show butler_exp_piris front04
    show butler_exp_eyebrows angryx01
    show butler_exp_mouth sad_Silentx04
    with dissolve

    n "El tipo enclenque se queda unos segundos en silencio,"

    show butler_exp_eyes 08
    show butler_exp_piris front08
    show butler_exp_eyebrows angryx02
    show butler_exp_mouth sad_Silentx03
    with dissolve

    n "para luego cerrar los ojos."

    show butler_exp_eyes 08
    show butler_exp_piris front08
    show butler_exp_eyebrows angryx01
    show butler_exp_mouth sad_Silentx05
    with dissolve

    n "Poco después:"

    show butler_exp_eyes 03
    show butler_exp_piris front03
    show butler_exp_eyebrows serious
    show butler_exp_mouth sad_Talkingx03
    with dissolve

    sdel "Por favor,"

    extend " espere unos minutos."

    show butler_exp_eyes 04
    show butler_exp_piris front04
    show butler_exp_eyebrows suspiciousx02
    show butler_exp_mouth sad_Silentx04
    with dissolve

    pause 0.2

    hide butler_body
    hide butler_exp_eyes
    hide butler_exp_piris
    hide butler_exp_eyebrows
    hide butler_exp_mouth
    with dissolve

    pause 0.2
    
    scene bg_el_cath_doorSide:
        truecenter
        zoom 0.5

    $ Pedrera_char_Cond = "NeusFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with fade

    p "¿Elur?"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Ese es tu verdadero nombre?"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Es el nombre con el que más gente me conoce."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Significa nieve en {a=https://es.wikipedia.org/wiki/Euskera}Euskera{/a}."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Naciste en el {a=https://es.wikipedia.org/wiki/País_Vasco}País Vasco{/a}?"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Más bien es dónde me crié..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    pt "Ahora que caigo,"

    pt "Neus es nieve en {a=https://es.wikipedia.org/wiki/Idioma_catalán}catalán{/a}..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    n "Poco tiempo después, oyes unos ligeros golpes huecos sobre ese enorme portón de metal."

    scene black
    with fade

    n "El tipo grandote, se agarra de una de las enormes manillas de la puerta,"

    n "y haciendo una fuerza sobrehumana, consigue abrir ligeramente ese enorme portón."

    if music_play != "waltz_in_f_minor":
        play music "audio/music/alcaknight/waltz_in_f_minor.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "waltz_in_f_minor"

    scene relda_alone:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.01 # Down
        ease_quad 10.0 zoom 2.4 xpos 0.5 ypos 1.02 # Face
    with fade

    n "De ahí aparece una mujer con el pelo corto y oscuro, con un vestido azul-rojizo de etiqueta."

    window hide dissolve
    pause

    scene bg_el_cath_doorSide:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 05:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_piris left05:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows sadx03:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_mouth happy_Talkingx05:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    # show relda_top_hair
    #     truecenter
    #     zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_top_hat:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose


    $ Pedrera_char_Cond = "NeusFarFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears


    # show relda_test:
    #     truecenter
    #     zoom 0.4
    #     alpha 0.5

    with fade

    re "Querida,"

    extend " que sorpresa."

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth happy_Talkingx08

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    re "Pensé que tardaría alguna que otra década en volver a verte."

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx03

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí,"

    extend " lo siento..."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Silentx04

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    ne "He tenido que hacer un pequeño reajuste de planes."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Talkingx05

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    re "¿Y este galán tan apuesto?"

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Euh..."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth sad_Talkingx003

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "¿Es él...?"

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows serious
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth happy_Silentx06

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Si soy él?"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows suspiciousx01
    show relda_exp_mouth happy_Silentx05

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿De qué estáis hablando?"

    scene bg_el_cath_doorSide:
        truecenter
        zoom 1.0 ypos 1.0

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda

    show relda_exp_eyes 05:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_piris front05:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_eyebrows angryx01:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_mouth happy_Silentx05:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    # show relda_top_hair
    #     truecenter
    #     zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_top_hat:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda

    with fade

    n "Sugerentemente, esa desconocida mujer se acerca a ti."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx003
    with dissolve

    re "¿Cómo te llamas?"

    extend " cariño."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Silentx03
    with dissolve

    p "Euh..."

    show relda_exp_eyes 03
    show relda_exp_piris front03
    show relda_exp_eyebrows serious
    show relda_exp_mouth happy_Silentx03
    with dissolve

    p "[protname]."

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth happy_Silentx04
    with dissolve

    re "Hmmm..."

    if protname.lower() == ("jordi"):

        show relda_exp_eyes 05
        show relda_exp_piris front05
        show relda_exp_eyebrows sadx01
        show relda_exp_mouth happy_Talkingx04
        with dissolve

        re "Interesante..."

    elif protname.lower() in joan_names:

        show relda_exp_eyes 03
        show relda_exp_piris front03
        show relda_exp_eyebrows surprisex01x01
        show relda_exp_mouth sad_Talkingx004
        with dissolve

        re "Vaya,"

        show relda_exp_eyes 06
        show relda_exp_piris front06
        show relda_exp_eyebrows sadx01
        show relda_exp_mouth happy_Talkingx05
        with dissolve

        re "felices vísperas."

    else:

        show relda_exp_eyes 05
        show relda_exp_piris front05
        show relda_exp_eyebrows suspiciousx01
        show relda_exp_mouth happy_Talkingx05
        with dissolve

        re "Un nombre,"

        extend " curioso..."

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "Pero querida,"

    extend " sabes muy bien a qué te arriesgas si entras aquí con él."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Talkingx04
    with dissolve

    re "¿Estás segura que no quieres intentar antes alguna otra opción?"

    show relda_exp_eyes 05
    show relda_exp_piris left05
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Silentx05
    with dissolve

    pause 0.2

    scene bg_el_cath_doorSide:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 01:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_piris left01:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows normal:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_mouth sad_Silentx03:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    # show relda_top_hair
    #     truecenter
    #     zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_top_hat:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose

## Neus

    $ Pedrera_char_Cond = "NeusFarFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with fade

    ne "¿Qué otra opción?"

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx005

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    re "Tanto el {a=https://es.wikipedia.org/wiki/Gran_Teatro_del_Liceo}Liceo{/a},"

    extend " como la parte neutral en las alcantarillas,"

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Talkingx05

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    re "están amparados por el {b}César{/b}."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Silentx04
    with dissolve

    pt "¿{a=https://es.wikipedia.org/wiki/César_(nombre)}César{/a}?"

    extend " ¿de {a=https://es.wikipedia.org/wiki/Julio_César}Julio César{/a}?"

    pt "¿o de qué demonios están hablando?"

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Silentx04

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero ahí no estás tú,"

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Silentx05

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "y sabes cómo de violento se está poniendo Barcelona últimamente por la noche."

    show relda_exp_eyes 05
    show relda_exp_piris left05
    show relda_exp_eyebrows sadx03
    show relda_exp_mouth sad_Silentx04

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows serious
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Y no tengo la fuerza,"

    extend " ni el tiempo,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "para arriesgarme a que se pudiera cortar o dañar con algo."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Silentx06

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    re "..."

    show relda_exp_eyes 01
    show relda_exp_piris left01
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Silentx02

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sé que te estoy exigiendo mucho al pedirte entrar con él..."

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Silentx03

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero no hubiera venido aquí si tuviera otra opción."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Silentx02

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "..."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth sad_Silentx06

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    re "Humm..."

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Talkingx005

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    re "Espero que sepas lo que te haces, querida."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Silentx06
    with dissolve

    pause 0.2

    scene bg_el_cath_doorSide:
        truecenter
        zoom 1.0 ypos 1.0

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 1.0 xpos 0.5 ypos 0.252 # Close
    show relda_exp_eyes 05:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_piris front05:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_eyebrows angryx01:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_exp_mouth sad_Talkingx004:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    # show relda_top_hair
    #     truecenter
    #     zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    show relda_top_hat:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 1.0 xpos 0.5 ypos 0.252 # Close Relda
    with fade

    re "Y tú,"

    extend " cariño,"

    show relda_exp_eyes 04
    show relda_exp_piris front04
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "intenta no tropezar con nada,"

    extend " ni con nadie..."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows suspiciousx02
    show relda_exp_mouth sad_Talkingx005
    with dissolve

    re "Preferiría que no se derramara más sangre de la necesaria en mi local."

    show relda_exp_eyes 05
    show relda_exp_piris front05
    show relda_exp_eyebrows normal
    show relda_exp_mouth sad_Silentx05
    with dissolve

    pt "¿Más de la necesaria...?"

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Talkingx004
    with dissolve

    re "Aquí tienes la tarjeta querida,"

    show relda_exp_eyes 03
    show relda_exp_piris left03
    show relda_exp_eyebrows serious
    show relda_exp_mouth sad_Talkingx05
    with dissolve

    re "es la puerta noventa y tres,"

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx01
    show relda_exp_mouth sad_Silentx04
    with dissolve

    pause 0.2

    scene bg_el_cath_doorSide:
        truecenter
        zoom 0.5

    show relda_body:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose

    show relda_exp_eyes 01:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_piris left01:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_eyebrows normal:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_exp_mouth sad_Silentx03:
        truecenter
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    # show relda_top_hair
    #     truecenter
    #     zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose
    show relda_top_hat:
        transform_anchor True
        xalign 0.5 yalign 0.218 # Relda Eyes.
        zoom 0.4 xpos 0.78 ypos 0.252 # Perfect ypose


    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows sadx02
    show relda_exp_mouth sad_Talkingx04

    $ Pedrera_char_Cond = "NeusFarFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with fade

    re "espero que sea lo suficientemente hermética,"

    show relda_exp_eyes 04
    show relda_exp_piris left04
    show relda_exp_eyebrows surprisex01
    show relda_exp_mouth sad_Talkingx004

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    re "pero yo de ti no abusaría del tiempo,"

    show relda_exp_eyes 05
    show relda_exp_piris left05
    show relda_exp_eyebrows angryx01
    show relda_exp_mouth sad_Talkingx03

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    re "ni de la suerte."

    show relda_exp_eyes 08
    show relda_exp_piris front08
    show relda_exp_eyebrows angryx02
    show relda_exp_mouth sad_Silentx03
    with dissolve

    pause 0.2

    scene guard_alone:
        subpixel True
        truecenter
        #zoom 2.0 ypos -0.338 # Down
        zoom 1.5 ypos 0.0 # Down
        ease_quad 10.0 zoom 2.0 ypos 1.3 # Head
    with fade

    n "Acto seguido ordena a ese tipo tan corpulento que vuelva a abrir el portón,"

    n "dándoos paso al misterioso lugar."

    if music_play != "serenade":
        play music "audio/music/others/serenade.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "serenade"

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_cathedral01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=5.0, channel='sfx1')

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond and afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_told:

        jump night05_NeusLastDate_ElysiumBloodDeath

    scene bg el_cath_main:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.38 ypos 1.6 # Window Up
        ease 15.0 zoom 0.31 xpos 0.5 ypos 0.5 # Center Far Image
    with fade
    # scene bg el_cath_main:
    #     truecenter
    #     zoom 1.0 xpos 0.38 ypos 1.6 # Window Up
    #     zoom 0.31 xpos 0.5 ypos 0.5 # Center Far Image
    #     zoom 0.5 xpos 1.25 ypos 0.19 # Table Left
    #     zoom 0.5 xpos -0.25 ypos 0.19 # Table Right
    # with fade

    n "Una melodía clásica a piano sumamente tranquila, inunda el enorme espacio repleto de columnas,"

    $ renpy.music.set_volume(0.1, delay=30.0, channel='sfx1')

    # $ saturation_tint_level = "verydark"

    n "resonando en las enormes bóvedas del techo, más propias de una catedral."

    n "Mayormente en una oscuridad profunda, que apenas permite ver con claridad el lugar,"

    n "con la excepción de una barra circular en medio del enorme espacio,"

    n "con una iluminación azulada y más típica de bares de ambiente."

    window hide dissolve
    pause

    scene bg el_cath_main:
        subpixel True
        truecenter
        zoom 0.5 xpos -0.25 ypos 0.19 # Table Right
        ease 20.0 zoom 0.5 xpos 1.25 ypos 0.19 # Table Left
    with fade

    n "A lo largo y ancho de esa enorme estancia,"

    n "se encuentran varias mesas a cada cual más separada de la otra"

    n "con pequeñas velas que permiten vislumbrar a duras penas sus ocupantes."

    n "Ni en tus peores pesadillas podrías imaginarte semejante repertorio de personajes y criaturas,"

    n "a cada cual más extraño y escalofriante."

    n "Un montón de ojos que brillan en la oscuridad como si fueran felinos acechando a su presa."

    window hide dissolve
    pause

    # Warriors
    scene el_tab_war:
        subpixel True
        truecenter
        zoom 2.0 xpos -0.2 ypos 0.1 # Head on table
        ease 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "Murmullos de fiesta y celebración con varones corpulentos"

    n "con apenas ropajes que les cubren sus cuerpos peludos y musculados,"

    n "así como mujeres ligeras de ropa y no mucho menos musculosas alzando sus copas al aire."

    window hide dissolve
    pause

    scene el_tab_nos:
        subpixel True
        truecenter
        zoom 1.3 xpos 1.3 ypos 0.65 #Face Left
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "En otro rincón, lo que parecen gentes que ocultan sus cuerpos con gruesos y tupidos ropajes,"

    n "pero no sus rostros, los cuales en su mayor parte están deformados tanto en mandíbulas y cráneo,"

    n "con largos y aislados pelos gruesos,"

    n "globos oculares completamente negros"

    n "y sus dientes a cada cual más asqueroso y extravagante."

    pt "Y yo que pensaba que el amigo barman de Neus tenía cara de rata..."

    pt "Dios..."

    window hide dissolve
    pause

    # Tsimizce
    scene el_tab_tsi:
        subpixel True
        truecenter
        zoom 1.6 xpos 1.5 ypos 0.85 # Left #Only faces
        ease 60.0 zoom 1.0 xpos 0.3 ypos 0.75 # Righ Only faces
    with fade

    n "Al apartar tu mirada de ahí,"

    n "tus ojos no pueden evitar fijarse en otra mesa, algo más iluminada."

    n "La única manera de describirlo sería monstruos humanoides,"

    n "vestidos rojizos y negros con un acabado elegante que podría vestir una persona con gusto arcaico,"

    n "pero ahí es dónde termina cualquier parecido con algo humano,"

    n "pues no solamente sus manos son garras enormes con afiladas uñas cubiertas de sangre,"

    n "sino que sus cuellos, mandíbulas, cráneos, ojos..."

    n "Deformaciones {a=https://es.wikipedia.org/wiki/H._P._Lovecraft}Lovercraftianas{/a},"

    n "como si algún ceramista hubiera tenido parkinson al moldear sus cabezas."

    n "Cubiertos de huesos que sobresalen de sus cráneos,"

    n "como si fueran estacas preparadas para clavarse a cualquiera que ose acercase a ellos."

    n "Cejas ausentes de pelo pero con cuernos,"

    n "frentes alargadas y extravagantes,"

    n "una de ellas se asemeja más al caparazón de un insecto"

    n "otro con lo que la única manera de describirlo, es que parece una caja torácica."

####

    show el_tab_tsi:
        ease 40.0 zoom 2.0 xpos -1.0 ypos 0.95 # Face of that monster

    n "Uno en particular te llama poderosamente la atención, pues a pesar de que aparentemente carece de ojos,"

    n "tienes la sensación que no te quita vista de encima."

    n "Sus orejas, longevas y puntiagudas, se alzan por encima de su cráneo -parecidas a las de un murciélago-;"

    n "sus ojos parecen estar ocultos tras una {a=https://i.natgeofe.com/n/6d16f213-60da-4528-b3f6-e1546d0ebf50/49228.jpg}enorme y deformada nariz{/a}"

    n "con pieles sueltas que vibran de forma perturbadora,"

    n "casi como si se hubiera caído de morros ante una trituradora"

    n "y aún no le hubieran sanado las heridas;"

    n "bajo este manto de arrugas deformes y palpitantes pellejos colgantes"

    n "se esconden un sinfín de rojizos dientes afilados que chocan entre ellos,"

    n "como si su mandíbula padeciera un tembleque incontrolable."

    n "Aparte de su escalofriante rostro,"

    n "hay algo que consigue inquietarte aún más si cabe."

    n "Carece de brazos y hombros, pero detrás de su espalda"

    n "goza de lo que parecen cuatro extremadamente longevos y delgados brazos"

    n "con dos codos cada uno, terminando en manos con cinco largos, delgados y afilados dedos,"

    n "casi como si fueran las patas de una araña humanoide."

#####

    # n "Quizás no es tan pálida, pero parece de todo menos humana."

    # n "Una enorme capa oscura que le cubre la mayor parte del cuerpo,"

    # n "pero eso no te impide ver el resto."

    # n "Sus ojos parecen estar ocultos tras un cascarón de molusco en su frente,"

    # n "con orejas enormes de murciélago,"

    # n "decenas de dientes afilados más parecidos a los de un tiburón y rojos como la sangre,"

    # n "cuatro brazos extremadamente delgados pero con dos codos alzándose en el aire."

    # n "Oyes el crepitar de sus dientes mientras su cabeza se contornea y parece dirigirte una vacía mirada."

#####
    
    show el_tab_tsi:
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5 # Whole Scene

    n "Al mismo tiempo, te fijas en lo que tienen sobre la mesa,"

    n "y desde luego no te tranquiliza en absoluto."

    n "Lo que parece un hombre con el vientre abierto,"

    n "con sus tripas entre los largos y sangrientos dedos de esos extraños y escalofriantes huéspedes"

    n "y el corazón aún latiendo en la mano de uno de ellos,"

    n "mientras su cuerpo sigue teniendo un tembleque perturbador."

    window hide dissolve
    pause

    scene el_tab_cth:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 ypos -0.6 #Fish
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5 # Whole Scene
    with fade

    n "Por no mencionar, esas criaturas más alejadas,"

    n "que solo pueden aparecer en los peores sueños nocturnos,"

    n "monstruos de enorme tamaño, más parecidos a un anfibio o criatura de las profundidades del mar,"

    n "que de la propia existencia terrenal."

    window hide dissolve
    pause

    $ saturation_tint_level = "reallydark"

    # play sound "audio/sfx/rewind01.ogg"

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_cath_main:
        truecenter
        zoom 0.31 xpos 0.5 ypos 0.5 # Center Far Image

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with hpunch

    ne "Te he dicho que no les fijes la mirada."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows angryx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿No podríamos correr?"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No te harán nada,"

    extend " si no llamamos la atención"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg el_cath_main:
        subpixel True
        truecenter
        zoom 0.31 xpos 0.5 ypos 0.5 # Center Far Image
        ease 20.0 zoom 1.0 xpos 2.5 ypos 0.6 # Discotquete Door
    with fade

    n "A medida que os acercáis a la barra,"

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx2')
    $ renpy.music.play("audio/sfx/discoteque01.ogg", channel="sfx2",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=5.0, channel='sfx2')

    n "observas al fondo una doble puerta hermética semi-cerrada,"

    n "dónde te parece ver gente bailando con poderosos focos, una iluminación intermitente, y luces de colores."

    pt "¿Eso de ahí es una discoteca?"

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)

    $ saturation_tint_level = "darkBlue"

    window hide dissolve
    pause

    # show bg el_cath_main:
    #     truecenter
    #     zoom 2.0 xpos 0.35 ypos 0.0 # Bar Close

    scene bg el_cath_bar:
        truecenter
        zoom 0.5

    $ Pedrera_char_Cond = "NeusFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows serious
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with fade

    ne "Ponme un ruso negro,"

    extend " por favor."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿No decías que teníamos pri...?"

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows angryx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    n "Neus te lanza una mirada, que no necesita de palabra alguna para darse a entender."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows angryx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    pt "Supongo que tomar una consumición,"

    extend " es un trámite obligatorio en este lugar..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows serious
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg el_cath_main:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.35 ypos 0.0 # Bar Close
        ease 30.0 zoom 1.0 xpos -1.0 ypos 0.0 # On the right part
    with fade

    n "Poco después de habérsela bebido de un solo trago, te vuelve a arrastrar hacia otro rincón del local,"

    stop music fadeout 10.0
    $ renpy.music.stop(channel='sfx1', fadeout=10.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ saturation_tint_level = "darkBlue"
    scene bg_el_cath_dunHall_01_comp:
        subpixel True
        truecenter
        #zoom 0.2 xpos 0.5 ypos 0.5
        zoom 1.0 xpos 2.4 ypos 1.4 # Torch LeFT?
        pause 2.0
        ease 25.0 zoom 1.0 xpos 1.0 ypos 0.6 # Test
    with fade

    n "algo más oscuro, en lo que parece un largo pasillo iluminado por antorchas azuladas"

    n "y repleto de puertas de madera a ambos lados."

    play sound "audio/sfx/piip01.ogg"

    n "Al atravesar el arco que da paso al pasillo, sientes un pitido y una presión en tus oídos."

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_hell01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.6, delay=4.0, channel='sfx1')


    show morning04_bedroom_DMast_blinkeye
    with hpunch
    p "Ughh..."

    n "De pronto, empiezas a oír llantos, gritos, réplicas de súplica y hasta algún que otro gemido."

    p "¿Qué demonios es este lugar Neus?"

    if music_play != "theDread":
        play music "audio/music/kevinmacleod/creepy/theDread.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theDread"
    
    scene bg_el_cath_dunHall_01_comp:
        truecenter
        zoom 0.2

    $ Pedrera_char_Cond = "NeusFarLeft"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyebrows angryx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with fade

    ne "Shhh..."

    $ renpy.music.set_volume(0.3, delay=30.0, channel='sfx1')

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows angryx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No digas nada hasta que te lo diga."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "En este local hay orejas hasta en las paredes."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg_el_cath_dunHall_01_comp:
        subpixel True
        truecenter
        zoom 0.2
        ease 40.0 zoom 1.0
    with Dissolve(0.25)

    n "Puertas de madera putrefacta, más parecidas a las de un calabozo,"

    n "manchadas de sangre reseca, vómito y con un hedor nauseabundo."

    n "A medida que os adentráis en ese oscuro pasadizo, los gritos se vuelven insoportables,"

    n "algunos incluso suenan de un modo muy extraño,"

    n "deformándose repentinamente para cesar por completo al instante."

    n "Voces de hombres adultos quebrados por el dolor y la desesperación,"

    n "algunos incluso pidiendo clemencia, no por su vida,"

    n "sino por la de alguien amado que está ahí presente con ellos."

    n "Voces de mujeres suplicando piedad, de ancianos que apenas les quedan fuerzas,"

    n "otros de una edad más prematura de los que prefieres no entrar en detalles en tu imaginación."

    pt "Dios..."

    $ renpy.music.set_volume(0.1, delay=10.0, channel='sfx1')

    window hide dissolve
    pause

    scene bg_el_cath_dunHall_02_comp:
        subpixel True
        truecenter
        zoom 0.2
        pause 1.0
        ease 40.0 zoom 1.0
    with fade

    n "Cuando cruzáis esa lejana puerta al final del pasillo"

    n "descubres otro habitáculo parecido al anterior,"

    n "solo que quizás con un olor no tan fuerte a podredumbre y sangre reseca."

    n "Las puertas laterales se ven algo más sólidas, limpias y herméticas."

    n "El murmullo y el ruido va cesando."

    $ renpy.music.stop(channel='sfx1', fadeout=10.0)

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    window hide dissolve
    pause

    scene bg_el_cath_dunHall_03_comp:
        subpixel True
        truecenter
        zoom 0.2
        pause 1.0
        ease 40.0 zoom 1.0
    with fade

    n "El lugar va pareciendo cada vez más decente y tranquilo."

    ne "Ya casi hemos llegado."

    p "..."

    pt "No estoy seguro si no se oye nada,"

    pt "porque esta zona es realmente más tranquila,"

    pt "o porque al estar las puertas completamente selladas,"

    pt "nadie puede saber lo que ocurre realmente ahí dentro..."

    play sound "audio/sfx/fall07.ogg"

    scene black
    with vpunch

    ## TEMPORAL
    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    n "Neus se detiene de golpe."

    p "¿Qué...?"

    extend " ¿Qué pasa?"

    scene bg_el_cath_dunHall_04_comp:
        truecenter
        zoom 0.2

    show wwW__whole_darkness:
        transform_anchor True
        xalign 0.5 yalign 0.1364 #-13Down +14Up
        zoom 0.5 xpos 0.5 ypos -0.1 # Pose?
    with fade

    n "Una enorme figura monstruosa y peluda se cierne justo en frente de vosotros"

    scene wwW__whole_darkness_comp:
        subpixel True
        truecenter
        zoom 1.0 ypos -1.0
        easein_quad 20.0 zoom 2.0 ypos 0.35
    with fade

    n "con los ojos brillando en medio de la oscuridad."

    n "Por su silueta a contraluz descubres que su pelaje es blanco como la nieve"

    n "y que su tamaño debe ser superior a los dos metros de altura."

    n "Instintivamente te tapas la nariz al sentir ese hedor tan pestilente a animal muerto."

    scene bg_el_cath_dunHall_04_comp:
        truecenter
        zoom 0.2

    show wwW__whole_darkness:
        wwW_pos_body_center
    show wwW_exp_mouth happy_Silentx01:
        wwW_pos_exp_center
    with fade

    ono "Snif-Snif"

    show wwW_exp_mouth happy_Talkingx01:
    with dissolve

    ww01 "Elur..."

    ww01 "El aroma a sangre ha desaparecido,"

    ww01 "pero tu fragancia es inconfundible,"

    extend " pequeña."

    show wwW_exp_mouth happy_Silentx01:
    with dissolve

    ne "..."

    show wwW_exp_mouth happy_Talkingx01:
    with dissolve

    ww01 "Y por lo visto eres incluso más bajita que la última vez."

    ww01 "¿Se debe eso a la basura humana que te acompaña?"

    show wwW_exp_mouth happy_Silentx01:
    with dissolve

    p "..."

    show wwW_exp_mouth happy_Talkingx01:
    with dissolve

    ww01 "Si tienes pensado pasar un buen rato en una de estas habitaciones,"

    ww01 "podría hacerte mejor compañía que la que pueda ofrecerte un mísero mortal."

    ww01 "Aprovecha que hoy es luna llena,"

    extend " pequeña..."

    show wwW_exp_mouth sad_Silentx01:
    with dissolve

    ne "Tenía entendido que no dejaban entrar a perros en este lugar."

    ww01 "Hmgrr..."

    n "Un extraño e inquietante gruñido surge de sus fauces."

    show wwW_exp_mouth happy_Talkingx01:
    with dissolve

    ww01 "Por lo visto,"

    extend " no has perdido tu sentido del \"mal\" humor."

    ww01 "Aunque sé que echas de menos mi bestia dentro de ti,"

    extend " pequeña..."

    ww01 "Quizás al principio estabas obligada a complacerme,"

    ww01 "pero tienes que admitir que tus gemidos del final,"

    ww01 "no eran fingidos."

    show wwW_exp_mouth happy_Silentx01:
    with dissolve

    p "..."

    show wwW_exp_mouth happy_Talkingx01:
    with dissolve

    ww01 "¿Por qué no dejas al excremento humano,"

    ww01 "y pasamos un buen rato juntos?"

    ww01 "recordando viejos tiempos."

    ww01 "Si quieres,"

    extend " puede entrar a mirar,"

    ww01 "a ver si aprende un poco de un macho alfa de verdad."

    show wwW_exp_mouth happy_Silentx01:
    with dissolve

    ne "Te crees muy superior a alguien que ni siquiera conoces."

    show wwW_exp_mouth sad_Silentx01:
    with dissolve

    ww01 "..."

    p "..."

    scene bg_el_cath_dunHall_04_comp:
        truecenter
        zoom 0.2

    show wwW_body:
        transform_anchor True
        xalign 0.5 yalign 0.1364 #-13Down +14Up
        zoom 4.5 ypos -0.15 # Nose
    show wwW_exp_mouth sad_Silentx01:
        truecenter
        zoom 4.5 ypos -0.15 # Nose
    show wwW_exp_eyes 03:
        truecenter
        zoom 4.5 ypos -0.15 # Nose

    with fade

    n "Sientes el ruido y la humedad de su nariz cerca de tu rostro."

    ono "SNIF-SNIF"

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond:

        ww01 "El interior de su nariz huele igual que tu mojada entrepierna..."

    show wwW_body:
        subpixel True
        ease_quad 6.0 zoom 3.0 ypos 2.0 # Down
    show wwW_exp_mouth sad_Silentx01:
        subpixel True
        ease_quad 6.0 zoom 3.0 ypos 2.0 # Down
    show wwW_exp_eyes 03:
        subpixel True
        ease_quad 6.0 zoom 3.0 ypos 2.0 # Down

    n "Poco después se desplaza hacia abajo."

    scene black
    with hpunch
    p "¡Ey!"

    scene bg_el_cath_dunHall_04_comp:
        truecenter
        zoom 0.2

    show wwW__whole_darkness:
        wwW_pos_body_center
    show wwW_exp_mouth sad_Silentx01:
        wwW_pos_exp_center
    with fade

    ww01 "..."

    show wwW_exp_mouth sad_Talkingx01
    with dissolve

    ww01 "Este tamaño no suele ser habitual en los humanos..."

    ww01 "y este olor..."

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond:

        show wwW_exp_mouth happy_Talkingx01

        ww01 "Le has puesto papel empapado en tu jugo,"

        show wwW_exp_mouth sad_Talkingx01
        with dissolve

        extend " me imagino que para ocultar el olor de su sangre nasal..."

    show wwW_exp_mouth happy_Talkingx01
    with dissolve

    ww01 "¿Qué tienes aquí?"

    extend " pequeña..."

    show wwW_exp_mouth sad_Silentx01
    with dissolve

    ne "No es de tu incumbencia."

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_night05_park:
        subpixel True
        truecenter
        zoom 0.4
        easein_quad 1.0 zoom 1.0
        easein_quad 5.0 xpos 1.3
    with hpunch

    n "Con un fuerte agarrón, te coge de la muñeca y te arrastra más allá de ese enorme monstruo,"

    n "dirigiéndoos a una puerta cercana, en la que introduce la llave"

    ww01 "Grrr..."

    n "Sin mirar atrás,"

    scene black
    with hpunch

    p "¡Ouch!"

    n "te lanza dentro y luego cierra la puerta."

    scene bg el_bedroom_a:
        subpixel True
        truecenter
        zoom 1.5
        ease_quad 15.0 zoom 0.5
    with fade

    n "Una habitación enorme y lujosa, con una cama de matrimonio,"

    n "cubierta por manteles rojizos y blancos, con bombones en la mesa."

    window hide dissolve
    pause

    $ saturation_tint_level = "default"

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg el_bedroom_a:
        truecenter
        zoom 0.5

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx04
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    ne "Yo..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "No debería haberle dicho eso."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows angryx04
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "No hacía falta..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero cuando he visto cómo te trataba,"

    extend " yo..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo siento..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al final has sabido respetar mejor el silencio,"

    extend " de lo que yo he sido capaz..."

    if night05_Interrogation_VampireExistence_Cond == True:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        p "En la pregunta sobre los vampiros que te he hecho esta noche,"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "me has respondido que hacía años que no veías a ninguno."

        show neus_exp_mouth sad_Silentx01
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Me puedes explicar qué demonios son entonces esas criaturas de ahí?!"

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx01
        $ nteye = "left01"
        call n_closefromup_tears_tears
        with dissolve

        p "¡Por no hablar del jodido hombre-lobo albino este!"

        show neus_exp_mouth sadbiting_Silentx07
        show neus_exp_eyebrows sadx04
        $ nteye = "left04"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx04
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "No quería darte más información de la que pudieras digerir en tan poco tiempo..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Para que no salieras corriendo sin que pudiera explicarme como es debido."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    else:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "Ok..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "Neus,"

    extend " tengo un montón de preguntas..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo sé,"

    extend " pero no hay mucho tiempo."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pt "¡Nunca hay tiempo!"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Significa eso que va a reventar la puerta y entrar?"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows normal
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No creo que sea capaz de romper el sacramento de este lugar..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Sacramento?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero desde luego nos estará esperando a la salida"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "y lo más probable es que no lo haga solo."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Entonces lo mejor sería esperar aquí dentro."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Este lugar cierra una hora antes de salir el sol."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y no sería más seguro esperar hasta entonces?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque de día no tiene esa transformación,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows serious
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "sigue siendo alguien muy corpulento y poderoso en su forma humana."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Y mis poderes no funcionan demasiado bien a la luz del sol..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Así que lo mejor sería que pudiéramos salir de aquí antes de que amaneciera,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "e intentar escapar por una salida alternativa."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Y la mujer con la que has hablado antes,"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿no podría escondernos en este local?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "una vez sale el sol,"

    extend " este lugar pierde la protección del César,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "por lo que podrían entrar a la fuerza y la cosa se pondría muy fea..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pt "Otra vez lo del César."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Hay otra salida?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows serious
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Seguro,"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "este tipo de lugares bajo tierra suelen estar preparados para casos de emergencia."

    show neus_exp_mouth happy_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Podríamos salir por alguna de esas salidas entonces."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Y es lo que pienso hacer,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero aún así será peligroso."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Tienen muy buen olfato,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "incluso en su forma humana."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y cuanto tiempo falta para que salga el sol?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Menos de lo que desearía..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Hmm..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve
    
    p "¿Puedo saber al menos,"

    extend " qué demonios hacemos aquí?"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "right00"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Euhh..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Supongo que lo habrás notado,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero este lugar es como un zona neutral,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "dónde se reúnen gran parte de los seres que habitan en las sombras de esta ciudad,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "seres tan,"

    extend " o más temibles incluso,"

    extend " que Padre."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si tan solo,"

    extend " una gota de tu sangre se hubiera derramado antes de llegar aquí,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "no habríamos salido vivos de este lugar."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero esto parece una habitación,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "No hay ninguna salida..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Verdad?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx01
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No,"

    extend " ninguna."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Que yo sepa..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_afterAll_Question:

        pt "¿Una sola gota?"

        "<Aceptar hacerlo con Neus sin hacer más preguntas>":
            call p_Help

            jump night05_elysium_acceptNeus

        "¿En serio? ¡¿Aquí?! ¡¿Después de lo que hemos oído por el pasadizo?!":
            call p_Help

            jump night05_elysium_afterAll_label

        "<Hacerle más preguntas sobre toda esta situación>":
            call p_Help

            $ night05_elysium_whySoSpecial_Cond = True

            jump night05_elysium_whySoSpecial_Answer

label night05_elysium_afterAll_label:

    #p "¿Después de todo lo que ha pasado?"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Después de haber abandonado a Dídac?!"

    if night05_NeusLastDate_Noria_Visions_MeritxellSawConfession:

        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Después de haber abandonado a Meritxell?!"

        if night05_Interrogation_MeritxellLove_Cond:

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex03
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡¿No me dijiste que sentías algo por ella?!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "¡¿Es así como te importan los seres queridos?!"

            show neus_exp_mouth sad_Talkingx11
            show neus_exp_eyebrows angryx05
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡No te atrevas a juzgarme de esa manera!"

            if gensex_YoureAMonster:

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows surprisex02
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "Ahora me dirás que tienes sentimientos y todo."

                show neus_exp_mouth sad_Silentx09
                show neus_exp_eyebrows angryx04
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

            else:

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¡¿Entonces?!"

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

            pause 0.3

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows angryx01
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡No te haces ni la más mínima idea de lo que he sufrido para llegar hasta aquí!"

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx02
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡Los sacrificios que he hecho!"

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            ne "La cantidad de sangre que se ha vertido por mi culpa;"

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx05
            $ nteye = "left02"
            call n_closefromup_tears_tears
            with dissolve

            ne "No..."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx06
            $ nteye = "left03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Tú no..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx05
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "No me juzgues sin saber toda la verdad,"

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx07
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "por favor."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "Pero antes has dicho que no tenemos mucho tiempo."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Y así es."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ ntlong = 0

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with fade

            pause 0.2

    else:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Te dije que confiaras en mí."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx06
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Verás..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sé que no es fácil de entender,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero el único modo de escapar de Padre,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "es que..."

    extend " pudieras..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Euhmm..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Necesitas mi esperma?"

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx06
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_whySoSpecial_Question:

        pt "¿Qué tiene mi esperma que no tenga otra persona?"

        "<Aceptar hacerlo con Neus sin hacer más preguntas>":

            jump night05_elysium_acceptNeus

        "¿Por qué es tan especial?":

            call p_Help

            $ night05_elysium_whySoSpecial_Cond = True

            jump night05_elysium_whySoSpecial_Answer



label night05_elysium_whySoSpecial_Answer:

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Por qué dicen que no soy humano?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Eres humano."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Que no te digan lo contrario!"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y tú también no?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿A quien quieres engañar?"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Es solo que tu sangre,"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx03
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "por lo tanto tu esperma,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Son un tanto especial..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Cómo de especial?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo suficiente,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "para que todos los presentes en este local"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "se mataran unos a otros para conseguir aunque fuera una sola gota,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "arriesgándose a sufrir la condena a muerte permanente,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "y por lo tanto a ser perseguidos de por vida a lo largo y ancho del continente,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "al causar un acto violento en un lugar protegido por el César de Barcelona."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pt "Otra vez lo de César..."

    pt "Debe de ser alguna clase de rey o dictador de estos monstruos..."

    ## SALIVA MATTER

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero no lo entiendo..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Me estás diciendo que cada vez que he sangrado en mi vida he estado en peligro de muerte?"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ha sido mi saliva la que ha activado eso en tu sangre."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Y por qué diablos lo has hecho?!"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Porque quería besarte."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    if night03_SaySomething_KissSucces_Cond:

        p "¡Pero ya me besaste en la primera cita y de eso hace dos días!"

    else:

        p "¡Pero ya me besaste en la cita de ayer!" # I mean, I'm sure a single kiss must be done... or you woldn't be here.

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿He estado en peligro todo este tiempo?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al usar solo mi saliva el efecto no es tan potente."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "La mayoría de seres oscuros de esta ciudad no lo notarían ni aunque estuvieras en frente de ellos."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero en este lugar..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Solo su saliva?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya sé que es mucha información de golpe,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero por favor..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_whyAmISoSpecial_Question:

        pt "Hay algo que no me está contando."

        "<Aceptar hacerlo con Neus sin hacer más preguntas>":

            jump night05_elysium_acceptNeus

        "<Insistir en por qué eres tan especial>":

            call p_Help

            $ night05_elysium_whyAmISoSpecial_Cond = True # knows about your mother and you´re both brothers.

            jump night05_elysium_whyAmISoSpecial_Answer


label night05_elysium_whyAmISoSpecial_Answer:

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Por qué soy tan especial?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Neus,"

    extend " responde a la pregunta."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "No..."

    extend " no sé si es un buen momento..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¡Neus!"

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Porque no deberías estar vivo."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "¿A qué te refieres?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Deberías haberla conocido..."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "Era la mujer más hermosa que haya visto nunca."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    p "¿De quien estás hablando?"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "De Baba."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿La anciana que vive contigo?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Realmente existe?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y qué tiene que ver con todo esto?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Hasta ese momento,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "siempre había tenido hembras,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "yo fui una de sus últimas hijas."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Mis hermanas siempre sospecharon que usaba algún tipo de truco para que nunca tuviera varones."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "La anciana Baba que vive en tu piso,"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿es tu madre?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Así es..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y por qué no la he visto nunca?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Por que prefiere no ser vista."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Su aspecto no es..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "lo que una vez fue."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Pero por qué me estás contando esto ahora?"

    if night05_Interrogation_HowManyBrothers_Cond == True:

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Como ya te dije mientras estabas comiendo..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando nace un hijo varón en nuestra familia,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "debe ser sacrificado en el siguiente {b}aquelarre{/b} que se celebre."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Solo que en tu caso..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿En mi caso?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿En mi caso qué?!"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Baba no pudo matarte."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Baba es mi madre...?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Tu verdadera madre."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Baba es tu madre."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    p "Mi padre es..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Tú eres..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    p "Dios..."

    pt "¿Qué coño...?"

    #scene day05

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show bg el_bedroom_b:
        truecenter
        zoom 0.5

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with Dissolve(0.75)

    n "Logras sentarte sobre la cama."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "O sea..."

    if night04_NeusInterview_Incest_Cond == True:

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "Las preguntas que me hiciste mientras me toqueteabas la polla con tu pie..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve


        if night04_NeusInterview_Incest_Answer_YesIfReallyInLove:

            p "No eran preguntas teóricas."

        else:

            p "¡No eran preguntas teóricas!"

        if night04_NeusInterview_killerlover_Cond == True:

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Lo de que si te perdonaría o no"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "si fueras una asesina,"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "tampoco era una pregunta teórica..."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "¡¿Verdad?!"

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    if not night04_NeusInterview_Incest_Answer_YesIfReallyInLove:

        p "¡Por Dios Neus!"

    else:

        p "Neus..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    if not night04_NeusInterview_Incest_Answer_YesIfReallyInLove:

        if night04_pedrera_blowjob_DONE == True:

            p "¡Que has tenido mi polla en tu boca!"

        elif night04_Neus_KissFrenchmade == True:

            p "¡Que te he besado con lengua!"

        else:

            p "¡Que hemos hecho cosas!"

        p "¡No sabía que eras mi hermana!"

    else:

        p "Yo..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "[protname]..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Por favor,"

    extend " tranquilízate..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    if not night04_NeusInterview_Incest_Answer_YesIfReallyInLove:

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx06
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        pt "¡¿Por qué no podía ser simplemente una bruja normal que se sintiera atraída por mi?!"

        p "..."

        pt "¿A quien quiero engañar...?"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "¿Y qué coño tenías pensado hacer en esta habitación?"

        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyebrows sadx07
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

    else:

        p "..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        ne "Durante la cena de ayer,"

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        ne "me dijiste que si realmente estuvieras enamorada de tu hermana,"

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx06
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "no te importaría..."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx05
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Acaso me mentiste?"

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx06
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿O es que no me amas?"

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "¿Mentí?"

            "Por supuesto que te amo.":
                call p_Help
                $pl.ch_pts("np",2)

                $ gensex_ILoveYouNeus = True

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows surprisex02
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "El hecho de que seas mi hermana,"

                show neus_exp_mouth sad_Silentx01
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "no va a cambiar lo que siento por ti."

                $ ntlong += 1

                show neus_exp_mouth happybiting_Silentx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ ntlong += 1

                show neus_exp_mouth happy_Talkingx06
                show neus_exp_eyebrows sadx05
                $ nteye = "front07"
                call n_closefromup_tears_tears
                with dissolve

                ne "No sabes lo feliz que me hace oírte decir eso."

                $ ntlong += 1

                show neus_exp_mouth happy_Silentx06
                show neus_exp_eyebrows sadx05
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                show neus_exp_mouth happybiting_Silentx06
                show neus_exp_eyebrows sadx06
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with Dissolve(0.5)

                pause 0.4

                $ ntlong = 0

                show neus_exp_mouth happy_Silentx05
                show neus_exp_eyebrows sadx04
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with fade

                pause 0.2

            "El hecho de que seas mi hermana cambia bastante las cosas.":
                call p_Help
                #$pl.ch_pts("np",-1)
                $ gensex_INotLoveYouNeus = True
                $ gensex_NotLoveSister = True

                $ ntlong += 1

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_eyebrows sadx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ ntlong += 1

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx04
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with Dissolve(0.5)

                pause 0.4

                $ ntlong += 1

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx05
                $ nteye = "right04"
                call n_closefromup_tears_tears
                with Dissolve(0.5)

                pause 0.4

                $ ntlong += 1

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_eyebrows sadx06
                $ nteye = "right03"
                call n_closefromup_tears_tears
                with Dissolve(0.5)

                ne "Me lo temía..."

                $ ntlong += 1

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows sadx06
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ ntlong = 0

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows angryx02
                $ nteye = "front06"
                call n_closefromup_tears_tears
                with fade

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx06
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with Dissolve(0.5)

                pause 0.4

            # "Nunca he dicho que te amase.":
            #     call p_Help
            #     $pl.ch_pts("np",-3)
            #     $ gensex_INotLoveYouNeus = True

            #     ne "..."



    if not night04_NeusInterview_Incest_Answer_YesIfReallyInLove or gensex_INotLoveYouNeus == True:

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows sadx06
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx07
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "Por eso no te lo quería contar aún..."

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        p "Por Dios Neus."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "¿En serio...?"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        p "Bueno,"

        extend " digo Neus,"

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows surprisex01
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "por llamarte de algún modo,"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "porque por lo visto tampoco es tu verdadero nombre."

        $ ntlong += 1

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx04
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "[protname]..."

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx05
        $ nteye = "front06"
        call n_closefromup_tears_tears
        with dissolve

        ne "Por favor..."

        $ ntlong += 1

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx06
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "Vale,"

        extend " vale..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "Quizás estoy asumiendo las cosas demasiado rápido,"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx06
        $ nteye = "right04"
        call n_closefromup_tears_tears
        with dissolve

        p "y aún no sé realmente por qué hemos venido aquí..."

        ne "..."

    else:

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows sadx03
        $ nteye = "right01"
        call n_closefromup_tears_tears
        with dissolve

        ne "Aún así..."

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows sadx02
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "¿Qué ocurre?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "El único modo de salir de la ciudad con vida,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "sin que Padre pueda encontrarnos,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "sin que llamemos exageradamente la atención al salir de aquí,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "es si me dejas embarazada."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "[protname]..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Me has oído?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Sí..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Y bien...?"

    if gensex_ILoveYouNeus:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "¿No me has oído cuando te he dicho que te amo?"

        $ ntlong += 1

        show neus_exp_mouth happy_Silentx05
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        $ ntlong += 1

        show neus_exp_mouth happy_Talkingx05
        show neus_exp_eyebrows sadx04
        $ nteye = "front06"
        call n_closefromup_tears_tears
        with dissolve

        ne "Tonto."

        $ ntlong += 1

        show neus_exp_mouth happybiting_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ ntlong += 1

        if gensex_INotLoveYouNeus or gensex_YoureAMonster:

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡¿Pero qué cojones quieres que te responda?!"
            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

        else:

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows normal
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "¿Qué quieres que te responda?"
            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

        ne "..."

        $ ntlong += 1

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx05
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo siento..."

        $ ntlong += 1

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx06
        $ nteye = "front06"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Mi madre..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Ella..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No te preocupes por ella."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sabe esconderse bien,"

    extend " incluso de Padre."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Especialmente en la Pedrera."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero Dídac..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "No..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya te he dicho en el Tibidabo que era demasiado tarde para él..."

    if ntlong > 0:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx04
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx05
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ ntlong = 0

        show neus_exp_mouth sadbiting_Silentx07
        show neus_exp_eyebrows sadx06
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with fade

    else:

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

    if night05_NeusLastDate_Noria_Visions_MeritxellSawConfession:

        pt "Me imagino que lo mismo para Meritxell..."

    else:

        p "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "No quería que las cosas terminaran así..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo pensaba..."

    extend " que podríamos tener tiempo después del parque,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "que podríamos hablar..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "No tenías pensando contarme nada de esto hoy,"

    extend " ¿verdad?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No..."

    if not gensex_ILoveYouNeus:

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Querías que te dejara preñada antes de saber que eras mi hermana?!"

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx04
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx06
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo hubiera intentado,"

        extend " pero nunca te hubiera forzado a ello..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Para poder ocultarnos,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve


    if night04_pedrera_blowjob_DONE:

        ne "quizás con que simplemente te corrieras en mi boca como ayer,"

    else:

        ne "quizás con que simplemente te corrieras en mi boca,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "hubiera bastado;"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero después de haber provocado al perro sarnoso este,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "y sabiendo que Padre está en Barcelona buscándonos intensamente..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Le llama perro a un hombre-lobo que mide más de dos metros?!"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "No creo que sea suficiente."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_AllWasALie_Question:

        pt "¡¿De verdad me estoy planteando hacerlo con mi hermana?!"

        "<Aceptar hacerlo con Neus sin hacer más preguntas>":

            jump night05_elysium_acceptNeus
                # $pl.ch_pts("np",2)
                # p "De acuerdo Neus,"
                # extend " como quieras."

        "<Cuestionarle si realmente está contigo por sentimientos o por otra razón>":

            call p_Help

            $ night05_elysium_AllWasALie_Cond = True

            #$pl.ch_pts("np",-1)

            jump night05_elysium_AllWasALie_Answer

label night05_elysium_AllWasALie_Answer:

    if not gensex_ILoveYouNeus:

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "Todo ha sido mentira."

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Qué...?"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "Desde el principio."

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "Nunca te has interesado por mi,"

        extend " por cómo soy."

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows suspiciousx02
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "Solo..."

        extend " me has usado."

        show neus_exp_mouth sad_Talkingx11
        show neus_exp_eyebrows angryx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "¡Eso no es verdad!"

        show neus_exp_mouth sad_Silentx09
        show neus_exp_eyebrows sadx03
        $ nteye = "front05"
        call n_closefromup_tears_tears
        with dissolve

    else:

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

    p "Necesitas mi esperma para escapar de tu..."

    extend " de nuestro padre."

    if not gensex_ILoveYouNeus:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "No soy más que una herramienta para ti."

        show neus_exp_mouth sad_Talkingx10
        show neus_exp_eyebrows angryx05
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "¡No digas tonterías!"

        show neus_exp_mouth sad_Silentx10
        show neus_exp_eyebrows angryx04
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows angryx02
        $ nteye = "right"
        call n_closefromup_tears_tears
        with dissolve

    else:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        p "¿No es así?"

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx01
        $ nteye = "right04"
        call n_closefromup_tears_tears
        with dissolve

    ne "Después de escapar de Padre,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "pasé varios meses en Barcelona deambulando por las calles de la ciudad,"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "el hambre,"

    extend " la necesidad,"

    extend " me corroían,"

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "no te imaginas lo que es intentar huir de una vida de placeres indescriptibles,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "de tu familia,"

    extend " de tus hermanas,"

    extend " del amor de tu pequeña compañía felina,"

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "de tus recuerdos,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx05
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "de todo aquello por lo que has vivido tanto,"

    extend " pero tanto tiempo,"

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx06
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "que apenas eres capaz de recordar cuando empezó a torcerse todo en tu mente."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    if night05_NeusLastDate_Noria_Visions_MeritxellSawConfession or night05_Interrogation_TxellName_Cond:

        ne "Gracias a Meritxell,"

    else:

        ne "Gracias a la rubia que conoces de clase,"

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx04
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pt "La tetuda..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    ne "conseguí calmar un poco esa necesidad."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero luego..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "ella me besó,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "y todo se fue al garete."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx05
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pensé que estaba perdida,"

    extend " que no tendría otro remedio que volver con Padre."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx06
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Quise hacer un tour turístico por la ciudad antes de irme finalmente"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "y entonces fue cuando descubrí que en la Pedrera estaba Madre."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ahí entendí porque me había sentido tan atraída a venir a esta ciudad."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    if ntlong > 0:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ ntlong = 0

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with fade

        pause 0.2

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Confieso que cuando Madre me contó que seguías con vida"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "me interesé en buscarte y encontrarte!"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows angryx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "es verdad que al principio me tentaba la idea de saber"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "que se experimentaba el tener sexo con alguien"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "que no fuera un monstruo espiritual,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "y no muriese después del coito."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows sadx04
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Monstruo espiritual?"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Pero eso solo fue al principio!"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Mucho antes de poder conocerte."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo..."

    extend " quería saber más cosas de ti..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "cómo eras,"

    extend " hasta que punto te parecías a Padre,"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "cómo tratabas a las mujeres..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Poco a poco fui viendo lo cariñoso y bondadoso que eres,"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "lo realmente distinto que eres de Padre,"

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "eso me hizo muy feliz."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Hasta el punto que sin darme cuenta"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "empezaba a tener celos de las mujeres que se te acercaban..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Y luego..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Quise que me conocieras."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero no pude."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "No podía."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Cada vez que te tenía cerca,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "mi cuerpo se paralizaba,"

    extend " mi labios no se movían,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx04
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "no era capaz de gesticular ninguna palabra,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "solo podía darte los buenos días"

    extend " y algunas veces hasta despedirme."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Me sentía una idiota,"

    extend " pero no podía."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Nunca me había pasado con nadie,"

    extend " ni con nada..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows angryx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Siempre he atacado de frente,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "prácticamente ningún hombre o mujer había sido capaz de escapar de mis encantos."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al-"

    extend "al no tener ningún poder,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx03
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "al no ser más que una estúpida,"

    extend " gafotas,"

    extend " enana,"

    extend " más plana que un tablón de madera..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "down05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows angryx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Por qué se empeña en insistir que es tan plana?"

    pt "Bueno,"

    extend " si la comparamos con la rubia..."

    pt "¡Pero es que eso es una exageración!"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "No podía entrar en tu cabeza y hacer que me olvidaras,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "como suelo hacer cuando mi primer intento de seducción ha sido un fracaso,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    ne "para probar otra estrategia,"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Entrar en mi cabeza?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "no..."

    extend " contigo eso no funcionaría,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "ni aunque hubiera tenido el poder y la capacidad para hacerlo..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Madre me dijo que tu mente no puede olvidar."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Así que solo tenía una oportunidad,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Una única y simple oportunidad."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Y si lo estropeaba?"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "right00"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿y si te daba asco?"

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿y si me considerabas simplemente una amiga?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Podría escapar a otra ciudad,"

    extend " a otro país..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero..."

    extend " no te podía sacar de mi cabeza."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "El solsticio se acercaba,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "sabía que corría un enorme riesgo estando tanto tiempo en una misma ciudad,"

    if night05_Interrogation_Solstice_Cond == False:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx03
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        pt "¿El solsticio?"

        pt "¿De qué está hablando?"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Padre acabaría por encontrarme,"

    extend " tenía que irme de Barcelona,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero no era capaz de decirte nada..."

    extend " y el tiempo se me acababa..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero siendo tú tan alto,"

    extend " corpulento,"

    extend " atractivo..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "y yo..."

    extend " siendo..."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx03
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡esto!"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "down05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo..."

    extend " No podía..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "No sabía qué más hacer."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Neus..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya..."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya sé que lo de ser hermanos,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "no es lo más..."

    extend " correcto..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero yo no te considero mi hermano."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No al menos del modo en cómo los humanos normalmente lo consideran."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿De qué estás hablando?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Tengo más años que la mujer humana más anciana que haya vivido en este mundo."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡¿Cómo podría considerarte mi hermanito?!"

    show neus_exp_mouth sad_Talkingx10
    show neus_exp_eyebrows angryx04
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Si podría ser tu tatarabuela!"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Có-"

    extend "cómo?!"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "No debería haber dicho eso..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿De qué demonios estás hablando?"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Como te he dicho,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "fui criada en el {a=https://es.wikipedia.org/wiki/País_Vasco}País Vasco{/a}."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero no te he dicho en qué año."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "¿En qué año fuiste criada Neus?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    if not gensex_ILoveYouNeus:

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿En qué año?!"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "A mediados del siglo dieciséis..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Di algo..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Tienes más de cuatrocientos años?!"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "Me imaginaba que tendrías una longeva edad,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¡pero no que fueras más vieja que Matusalén!"

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "No soy tan vieja."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx06
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_pederast_Question:

        pt "¡¿Nació en el mismo siglo que {a=https://es.wikipedia.org/wiki/William_Shakespeare}Shakespeare{/a}, {a=https://es.wikipedia.org/wiki/Galileo_Galilei}Galileo{/a}, {a=https://es.wikipedia.org/wiki/Nostradamus}Nostradamus{/a} y {a=https://es.wikipedia.org/wiki/Miguel_de_Cervantes}Cervantes{/a}?!"

        # "<Aceptar hacerlo con Neus sin hacer más preguntas>":

        #     jump night05_elysium_acceptNeus
        #         # $pl.ch_pts("np",2)
        #         # p "De acuerdo Neus,"
        #         # extend " como quieras."

        "<Tratarla de pederasta contigo por lo anciana que es en comparación>":

            call p_Help

            $ night05_elysium_pederast_Cond = True

            if gensex_ILoveYouNeus:
                $pl.ch_pts("np",-4)
            else:
                $pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "No..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "Si es que encima de incestuosa,"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "¡eres una pederasta!"

            if gensex_ILoveYouNeus:

                $ gensex_ILoveYouNeus = False
                $ gensex_INotLoveYouNeus = True

                show neus_exp_mouth sad_Silentx08
                show neus_exp_eyebrows angryx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "Pensaba que habías dicho que me amabas..."

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows serious
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Esto cambia las cosas!"

                show neus_exp_mouth sad_Talkingx09
                show neus_exp_eyebrows angryx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¡¿En qué exactamente?!"

            else:

                show neus_exp_mouth sad_Talkingx09
                show neus_exp_eyebrows angryx04
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "¡Oye!"

            show neus_exp_mouth sad_Talkingx10
            show neus_exp_eyebrows angryx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡Que yo sepa eres mayor de edad!"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows angryx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Coño!"

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Eso ya lo sé!"

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx02
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows serious
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Pero tienes veinte veces mi edad!"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            p "por lo menos..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows angryx01
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

        "<No decirle nada al respecto>":

            call p_Help

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "Ya veo..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "De verdad..."

    jump night05_elysium_pederast_After

label night05_elysium_pederast_After:


    ne "No es la cantidad de años lo que define la madurez de alguien."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Además,"

    if gensex_INotLoveYouNeus:

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx02
        $ nteye = "right01"
        call n_closefromup_tears_tears
        with dissolve

        ne "aunque ahora digas que no me amas,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "sé cómo eres,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "lo fiel que eres a tu palabra,"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "cómo te has preocupado por Dídac todo este tiempo..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "A pesar de mi edad,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "tengo la sensación que sin poderes,"

    show neus_exp_mouth sad_Talkingx005
    show neus_exp_eyebrows sadx03
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "eres mucho más responsable y maduro que yo."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Quizás también es porque nunca había estado tanto tiempo siendo tan vulnerable..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_aboutDidac_Question:

        pt "¿Debería serle sincero yo también?"

        "<Aceptar hacerlo con Neus sin contarle lo de Dídac>":

            jump night05_elysium_acceptNeus
                # $pl.ch_pts("np",2)
                # p "De acuerdo Neus,"
                # extend " como quieras."

        "<Contarle lo sucedido con Dídac>":

            call p_Help

            $ night05_elysium_aboutDidac_Cond = True

            jump night05_elysium_aboutDidac_After

label night05_elysium_aboutDidac_After:

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Sobre lo de Dídac..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Sí...?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    if afternight04__Pussy_dick_med_Done > 0 or aftermorning04_FittingRoom_FuckherConsent == True:

        p "No soy tan responsable como realmente crees."

    else:

        p "Hay algo que debería contarte..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows suspiciousx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿A qué te refieres...?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Bueno..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Supongo que eres consciente de que se convirtió en mujer."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Lo que no sé si sabías,"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "es que además se volvió una jodida ninfómana enfermiza."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿De qué estás hablando?"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Solo la convertí en mujer,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "su carácter y personalidad las dejé intactas."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Incluso le bajé la libido para prevenir que..."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_eyebrows surprisex01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows angryx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows angryx04
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Padre..."

    show neus_exp_mouth sad_Talkingx10
    show neus_exp_eyebrows angryx05
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Seré estúpida!"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "No fue cosa tuya entonces."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx04
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Claro que no!"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No negaré que tenía mis reservas en convertir a Dídac en mujer,"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "por si os daba por curiosear,"

    extend " viviendo juntos,"

    extend " estando tanto tiempo solos..."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero en solo tres días y después de que le bajara la lujuria,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "lo veía bastante improbable..."

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows angryx02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero si Padre..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Qué habéis hecho [protname]?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Bueno,"

    extend " digamos que..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "Nunca había conocido a nadie tan desesperadamente necesitado para el sexo"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "como Dídac en estos dos últimos días..."

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows angryx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx05
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "Maldito seas Papá..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows serious
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Qué..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Qué hiciste con él...?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Acaso importa?"

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "Tampoco es que podamos hacer nada por él a estas alturas ya."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo siento."

    $ ntlong += 1

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "Soy una estúpida."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx06
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pensé que quizás conmigo te bastaría,"

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "y que no necesitarías nunca a nadie más..."

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyebrows sadx06
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "Supongo que ni con la edad aprendo de mis errores."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    menu night05_elysium_NeusStupid_Question:

        pt "Con ella me bastaría..."

        "Lo dices como si me importara lo que piensas de mí." if gensex_INotLoveYouNeus:
            $pl.ch_pts("np",-6)

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows surprisex02
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Por qué eres así...?"

            $ ntlong += 1

            show neus_exp_mouth sasdbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows sadx07
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.5

            $ ntlong = 0

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows sadx07
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with fade

            pause 0.2

            jump night05_elysium_WhatNow_After
                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"

        "<Contarle que cuando llegaste a casa Dídac no estaba en casa>" if afternight04_DidacisNOTatHome:
            call p_Help

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows serious
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Después de la cena en el restaurante vegano,"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows normal
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "cuando volví a casa,"

            extend " Dídac no estaba."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Qué quieres decir que no estaba?"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Que se había ido."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Probablemente porque durante estos días he intentado evitarlo tanto como he podido."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "Me imagino que no se lo tomó muy bien,"

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows sadx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            p "o su desesperación lo llevó a buscar la solución a otro lugar..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Y por la mañana hablaste con él?"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "No."

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            p "No durmió en casa."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "No lo he vuelto a ver hasta que me ha enviado el mensaje que tú misma has visto."

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx05
            $ nteye = "left02"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Yo..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx02
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo siento mucho [protname]..."

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows sadx03
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Esto..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "esto no era lo que yo..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Como has dicho,"

            extend " ya es demasiado tarde para lamentarse de ello."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

                # p "Neus..."

                # ne "..."

                # jump night05_elysium_WhatNow_After

                #         # p "¿Qué es lo que quieres hacer?"
                #         # ne "..."
                #         # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"

        "<Contarle el porqué tenías que ayudar a Dídac>" if afternight04_sexbattle_started:

            call p_Help

            $ night05_elysium_NeusStupid_Cond = True

            jump night05_elysium_NeusStupid_After


        "<Contarle cómo se fue de casa a buscar a alguien para follar>"if ((afternight04_sexbattle_started == False) and (afternight04_DidacisNOTatHome == False) or afternight04_Didac_Leaving_Cond):
            call p_Help

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows normal
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Ayer por la noche rechacé su más que insistente petición de follar."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Me dijo que si no le complacía yo,"

            show neus_exp_mouth sad_Silentx01
            show neus_exp_eyebrows surprisex02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "encontraría a alguien que estuviera más dispuesto a ello."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Así que se fue de casa a buscar a alguien para follar."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Dejaste que se fuera?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows normal
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows serious
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡¿No lo seguiste?!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            if afternight04_Didac_FollowHim_Yes_Cond == False:

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¡¿Te crees que no intenté detenerle?!"

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Era eso,"

                extend " o follar con él!"

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows sadx04
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Podrías haber hecho algo..."

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡¿Te refieres a que me follara a mi compañero de piso?!"

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows angryx02
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "¡No!"

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyebrows angryx01
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "No hace falta follar para calmar esa sed,"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows sadx03
                $ nteye = "right04"
                call n_closefromup_tears_tears
                with dissolve

                ne "al menos durante los primeros días."

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows sadx03
                $ nteye = "left01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Quizás si hubieras logrado llevarlo al orgasmo de otro modo..."

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Quería mi polla,"

                extend " solo mi polla."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "Sí,"

                extend " ya sé lo que se siente,"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyebrows sadx06
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with dissolve

                ne "pero aún así..."

                extend " dejarlo en la calle de esa manera,"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows sadx04
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "es realmente muy peligroso."

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows surprisex03
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡¿Desde cuando te importa la integridad de Dídac?!"

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyebrows angryx03
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Nunca te he dicho que le odie tanto."

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows serious
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Intento violarte!"

                show neus_exp_mouth sadbiting_Silentx07
                show neus_exp_eyebrows sadx06
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows sadx05
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Solo quería darle una lección..."

                $ ntlong += 1

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows sadx04
                $ nteye = "right02"
                call n_closefromup_tears_tears
                with dissolve

                ne "Solo eso..."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "right01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Nunca le he deseado ningún daño a tu amigo."

                $ ntlong += 1

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows sadx06
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx07
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                p "Como ya he dicho,"

                extend " hablar de esto ya no tiene mucho sentido..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows sadx02
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "tú misma dijiste que es demasiado tarde."

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx05
                $ nteye = "left05"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows sadx05
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Lo siento..."

                show neus_exp_mouth sadbiting_Silentx08
                show neus_exp_eyebrows sadx06
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ ntlong = 0

                show neus_exp_mouth sadbiting_Silentx08
                show neus_exp_eyebrows sadx06
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with fade

                pause 0.2

            else:

                $pl.ch_pts("np",1)

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Por supuesto que le seguí!"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows sadx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Y qué pasó?"

                if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond: # Paliza que te han dado.

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿No te he dicho que ayer me golpearon la nariz?"

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Intenté ayudarle,"

                    extend " intentaba follar con tres yonkis de mierda."

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyebrows sadx02
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Como si estuviera enloquecido..."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Y lo único que recibí es una paliza."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Y Dídac...?"

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Cuando desperté ya no estaba."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx06
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows sadx07
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo siento..."

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows surprisex02
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Se lo merece,"

                    extend" por gilipollas."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No..."

                    extend " no digas eso..."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡Ni siquiera intentó defenderme cuando lo único que intentaba era ayudarle!"

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Es difícil de explicar lo que se siente cuando tienes esa hambre,"

                    extend " [protname]."

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx01
                    $ nteye = "right01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Las amistades,"

                    extend " el amor,"

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "pasan casi a un segundo plano,"

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "lo que se padece en ese estado,"

                    extend " es algo mucho peor que la adicción a la peor droga."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows normal
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pff..."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿Acaso importa a estas alturas?"

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx05
                    $ nteye = "down04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No,"

                    extend " supongo que no..."

                else: # No recibes una paliza.

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Intentó buscar un lugar alejado de las calles,"

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows surprisex02
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "hasta que llegó a un parque dónde encontró a tres yonkis de mierda."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx02
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Lo sacaste de ahí?"

                    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant: # Te vas sin Dídac.

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Intenté razonar con él,"

                        extend " pero era como hablarle a una piedra."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Qué hiciste?"

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Fue él quien no quería irse."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx02
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Le dije que lo que pretendía era una locura,"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx03
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "pero me insistió en que era mi culpa por no haber querido follar con él."

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows surprisex01
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¡¿Te puedes creer que me chantajeó con eso?!"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx05
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Es un capullo."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx02
                        $ nteye = "right01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx03
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "[protname]..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Tienes que entender que si Padre influyó en su libido;"

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "no importa la razón,"

                        extend " solo el deseo."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx03
                        $ nteye = "left02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Probablemente hubiera hecho cualquier cosa por saciar esa sed."

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No puedes culparle realmente por ello."

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Cuando esos tipejos me amenazaron con una jodida navaja,"

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¡hubiera podido defenderme,"

                        extend " o decir algo en mi favor!"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¡Se quedó ahí quieto sin hacer ni decir nada!"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx05
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx06
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¿Qué querías que hiciera?"

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows surprisex01
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¡¿Follarme a mi compañero de piso?!"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx05
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx06
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Podrías haber intentado hacer algo con él cuando estabais en casa..."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx05
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¿Hablas en serio?"

                        show neus_exp_mouth sad_Talkingx08
                        show neus_exp_eyebrows sadx01
                        $ nteye = "left01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¡No hablo de follar!"

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyebrows sadx03
                        $ nteye = "right02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx04
                        $ nteye = "right03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "quizás con tus manos"

                        extend " o tu lengua,"

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx05
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "hubiera podido..."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx06
                        $ nteye = "right05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Estamos hablando de Dídac,"

                        extend " no solo es un tío,"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "sino que lo conozco desde que tengo uso de razón."

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¿Estás de coña?"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ ntlong += 1

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Lo siento [protname]."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx01
                        $ nteye = "right01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Nunca había sido mi intención que la cosa acabara así."

                        $ ntlong += 1

                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows sadx05
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "De todos modos ya es un poco tarde para eso..."

                        $ ntlong += 1

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows sadx06
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows sadx05
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        pause 0.2

                        $ ntlong = 0

                        show neus_exp_mouth sadbiting_Silentx04
                        show neus_exp_eyebrows sadx04
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with fade

                        pause 0.2

                    else:

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows sadx02
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "No."

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Al menos no al principio."

                        if afternight04_Park_HelpDidacPolice_Cond or afternight04_Park_AbandonDidacPolice_Cond: # Didac se queda preñado con Okupa.

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Estuve observándole desde lejos para ver si en algún momento"

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "se daba cuenta de lo que realmente estaba haciendo."

                            show neus_exp_mouth sad_Silentx07
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Pero supongo que esperé demasiado."

                            show neus_exp_mouth sad_Talkingx003
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿A qué te refieres?"

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Los dos tipos hicieron lo que quisieron con él,"

                            extend " pero al menos intentaron usar condón,"

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "quizás al final y por falta de cooperación de Dídac,"

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "uno de ellos se la metió por detrás sin él."

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Pero el último individuo,"

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "directamente arrojó el condón poco antes de metérsela,"

                            extend " y..."

                            show neus_exp_mouth sad_Silentx07
                            show neus_exp_eyebrows sadx05
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx06
                            show neus_exp_eyebrows serious
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Pero ahí saliste a su rescate,"

                            show neus_exp_mouth sad_Talkingx005
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¡¿no?!"

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows suspiciousx01
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows serious
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Tenías que haberlo visto,"

                            extend " no me hubiera hecho ni el más mínimo caso!"

                            show neus_exp_mouth sad_Silentx07
                            show neus_exp_eyebrows sadx05
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "¡Estaba como poseído!"

                            show neus_exp_mouth sad_Silentx08
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "No hubiera servido de nada."

                            show neus_exp_mouth sad_Talkingx09
                            show neus_exp_eyebrows angryx02
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¡[protname]!"

                            show neus_exp_mouth sad_Talkingx10
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¡¿Por qué no detuviste esa locura cuando viste que podía quedar embarazada?!"

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            show neus_exp_mouth sad_Talkingx07
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¡Sabes que Dídac nunca hubiera hecho algo así sino hubiera...!"

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows surprisex02
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Si tú no le hubieras mordido."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx05
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Neus,"

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "no te culpo."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "En tu situación,"

                            extend " yo habría hecho lo mismo."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx06
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "El muy capullo se merecía eso y más."

                            $ ntlong += 1

                            show neus_exp_mouth sadbiting_Silentx07
                            show neus_exp_eyebrows sadx05
                            $ nteye = "right04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx003
                            show neus_exp_eyebrows sadx06
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "No..."

                            $ ntlong += 1

                            show neus_exp_mouth sad_Talkingx03
                            show neus_exp_eyebrows sadx04
                            $ nteye = "right02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "No seas tan duro con él..."

                            show neus_exp_mouth sad_Silentx02
                            show neus_exp_eyebrows surprisex02
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "¡Intentó violarte!"

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx05
                            $ nteye = "right04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            $ ntlong += 1

                            show neus_exp_mouth sad_Talkingx003
                            show neus_exp_eyebrows sadx06
                            $ nteye = "left05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Yo..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Al final llegó la policía,"

                            if afternight04_Park_HelpDidacPolice_Cond:

                                extend " y tuve que sacarlo a rastras del lugar."

                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿No te dijo nada al darse cuenta que estuviste espiando la situación y...?"

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¡Claro que me dijo algo!"

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows suspiciousx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Pero yo también le respondí."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows surprisex01
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¡Fue él quien quiso irse de casa para hacer esa locura!"

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¡Él fue quien tuvo la brillante idea de buscar a varios yonkis de mierda para follar!"

                                show neus_exp_mouth sad_Silentx06
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Por lo menos evité que fuera detenido."

                                show neus_exp_mouth sad_Silentx07
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No hacía falta que fueras tan duro con él..."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¿A qué viene ese cambio de opinión respecto a Dídac?"

                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Nunca quise que fuera algo permanente [protname]..."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows sadx02
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Yo no puedo convertirlo en una mujer por lo que te hizo."

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows surprisex01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Pero puedo elegir no ayudarle si creo que se merece eso y más."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows suspiciousx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Además,"

                                extend " es lo que dijiste,"

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "ser mujer tampoco es un castigo,"

                                show neus_exp_mouth sad_Silentx06
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "es una lección."

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Y en el fondo ha sido su decisión."

                                $ ntlong += 1

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx02
                                $ nteye = "right04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx002
                                show neus_exp_eyebrows sadx05
                                $ nteye = "right05"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No,"

                                extend " no lo ha sido..."

                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No si Padre influyó en aumentar su libido..."

                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Hubiera hecho cualquier cosa para saciar esa sed."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¿Y qué importancia tiene ahora todo esto...?"

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx06
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Lo siento [protname]."

                                $ ntlong += 1

                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Nunca desee que esto terminara así,"

                                show neus_exp_mouth sad_Talkingx04
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "de verdad..."

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Ya..."

                                show neus_exp_mouth sadbiting_Silentx06
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.2

                                $ ntlong = 0

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with fade

                            else:

                                extend " y era demasiado arriesgado sacarlo de ahí."

                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows suspiciousx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Lo dejaste ahí?"

                                show neus_exp_mouth sad_Talkingx08
                                show neus_exp_eyebrows suspiciousx02
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿¡Dejaste que lo detuvieran!?"

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows surprisex01
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Si me hubiera puesto en medio y me hubieran detenido,"

                                extend " no habría podido acudir a nuestra última cita."

                                show neus_exp_mouth sadbiting_Silentx06
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Pero él ya no puede volver a ser hombre si ha quedado..."

                                show neus_exp_mouth sadbiting_Silentx03
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "No acudí a nuestra última cita por él."

                                $pl.ch_pts("np",3)

                                $ ntlong += 1

                                show neus_exp_mouth sadbiting_Silentx04
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx03
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "[protname]..."

                                show neus_exp_mouth sad_Talkingx003
                                show neus_exp_eyebrows sadx06
                                $ nteye = "right02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Yo..."

                                show neus_exp_mouth sadbiting_Silentx07
                                show neus_exp_eyebrows sadx06
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.2

                                $ ntlong = 0

                                show neus_exp_mouth sadbiting_Silentx06
                                show neus_exp_eyebrows sadx05
                                $ nteye = "right05"
                                call n_closefromup_tears_tears
                                with fade

                            ne "..."

                        elif afternight04_Park_DidacFuckWithoutCondom_Aborted_Cond: # Vuelves a casa con Dídac sin estar preñada.

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Sabía que si intentaba razonar con él antes de tiempo,"

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "del modo en que estaba no me haría ningún caso."

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Así que decidí esperar el momento adecuado para sacarlo de ahí."

                            show neus_exp_mouth sad_Talkingx05
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿A qué te refieres con el momento adecuado?"

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows normal
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "A que se diera cuenta por él mismo,"

                            extend " que lo que estaba haciendo era una jodida locura."

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Justo cuando el que estaba peor de los tres,"

                            extend " iba a follarle el coño sin condón,"

                            show neus_exp_mouth sad_Silentx02
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "es cuando salí de mi escondite para apartarlos"

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "y demostrarle lo jodidamente imbécil e inconsciente que estaba siendo."

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            $pl.ch_pts("np",5)

                            show neus_exp_mouth sad_Talkingx03
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "No solo fuiste un buen amigo, [protname],"

                            show neus_exp_mouth sad_Talkingx02
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "sino que además actuaste con paciencia e inteligencia."

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx05
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.5

                            $ ntlong = 0

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with fade

                        else : # Fumetas se lo folla sin condón por el culo.

                            aj "This shouldn't be readable... In theory... 032547"


            pause 0.2

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Neus..."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx03
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            jump night05_elysium_WhatNow_After

                    # p "¿Qué es lo que quieres hacer?"
                    # ne "..."
                    # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"


        "<Decirle que no hiciste absolutamente nada con él>" :

            call p_Help

            $ night05_elysium_NeusStupidDidacNothingDone_Cond = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows serious
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            p "De verdad Neus,"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "No hice nada con él."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿En serio...?"

            if  (aftermorning04_FittingRoom_FuckherConsent or
                aftermorning04_FittingRoom_ButtocksDickOverMasturbate or
                aftermorning04_Mast001_Pussy_insert or
                aftermorning04_Mast001_Anal_insert):

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows serious
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Bueno..."

                extend " quizás tonteé un poco con él en los vestuarios de los almacenes..."

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿En los almacenes?"

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Fuisteis a comprar ropa?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Insistió en que quería comprarse unos sujetadores!"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "o algo por el estilo..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows normal
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "en realidad tampoco le culpo,"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "toda la ropa que tenemos en el piso no es que sea muy femenina que digamos..."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows suspiciousx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿A qué te refieres con tontear?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows serious
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "Mientras estaba en los vestuarios probándose la ropa,"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "me agarró y me arrastró dentro con él."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front3"
                call n_closefromup_tears_tears
                with dissolve

                p "Pero en cierto momento,"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p  "creo que una de las dependientas que estaba ahí cerca sospechó algo"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "y Dídac se puso a hablar con ella."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "En aquel momento y debido al reducido tamaño del habitáculo,"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "empezó a mover sus nalgas sobre mi entrepierna."

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_eyebrows normal
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Y qué hiciste?"

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                menu night05_elysium_NeusStupid_FittingRoomDidac_Question:

                    pt "¿Qué pasó en los probadores con Dídac?"

                    "Acabé bajándome los pantalones y metiéndosela dentro" if aftermorning04_FittingRoom_FuckherConsent:

                        call p_Help

                        $ night05_elysium_NeusStupid_FittingRoomDidac_FuckherConsent = True

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows surprisex03
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Qué...?"

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyebrows suspiciousx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Por qué?"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        menu night05_elysium_NeusStupid_FittingRoomDidac_Penetration_Question:

                            "Porque me puso cachondo y se lo merecía.":
                                call p_Help

                                $pl.ch_pts("np",-3)

                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows surprisex03
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¡¿Entera?!"

                                show neus_exp_mouth sad_Silentx07
                                show neus_exp_eyebrows suspiciousx03
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "No..."

                                extend " entera no..."

                                show neus_exp_mouth sad_Silentx07
                                show neus_exp_eyebrows angryx03
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                pt "No porque no lo hubiera intentado..."

                                show neus_exp_mouth sad_Talkingx08
                                show neus_exp_eyebrows angryx02
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Le debiste hacer un daño terrible..."

                                show neus_exp_mouth sad_Silentx08
                                show neus_exp_eyebrows angryx02
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¡por no hablar de que es tu compañero de piso!"

                                show neus_exp_mouth sad_Talkingx04
                                show neus_exp_eyebrows sadx01
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Pensé..."

                                extend " pensé que Dídac te importaba algo más..."

                                show neus_exp_mouth sadbiting_Silentx04
                                show neus_exp_eyebrows sadx03
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                menu:

                                    pt "Dídac me importaba más..."

                                    "No después de lo que te hizo.":
                                        call p_Help
                                        $pl.ch_pts("np",1)

                                        show neus_exp_mouth sad_Talkingx08
                                        show neus_exp_eyebrows angryx03
                                        $ nteye = "front08"
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "Por terribles que hubieran podido ser sus intenciones,"

                                    "...":
                                        call p_Help

                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "por favor,"

                                extend " no actúes así..."

                                show neus_exp_mouth sadbiting_Silentx06
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                            "Porque si veía que iba en serio, y no me lo tomaba a broma, quizás me dejaría en paz.":

                                call p_Help

                                $pl.ch_pts("np",-2)

                                show neus_exp_mouth sad_Talkingx004
                                show neus_exp_eyebrows suspiciousx01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Le debiste hacer un daño terrible..."

                                show neus_exp_mouth sad_Silentx02
                                show neus_exp_eyebrows surprisex02
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Como si él se hubiera preocupado mucho por ti cuando intentó violarte."

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx06
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx03
                                $ nteye = "right02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Esa es tu manera de resolver las cosas?"

                                show neus_exp_mouth sad_Talkingx08
                                show neus_exp_eyebrows angryx03
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Sin consentimiento y con violencia?"

                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows sadx05
                                $ nteye = "left04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No demuestras ser muy diferente actuando de esta manera."

                                show neus_exp_mouth sad_Silentx07
                                show neus_exp_eyebrows sadx06
                                $ nteye = "left05"
                                call n_closefromup_tears_tears
                                with dissolve

                        p "..."

                    "Acabé bajándome los pantalones y masturbándome con sus nalgas." if aftermorning04_FittingRoom_ButtocksDickOverMasturbate:

                        call p_Help

                        $pl.ch_pts("np",-1)

                        $ night05_elysium_NeusStupid_FittingRoomDidac_ButtocksMast = True

                        show neus_exp_mouth sad_Talkingx004
                        show neus_exp_eyebrows surprisex01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¡¿Por qué?!"

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows surprisex02
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Porque me puso tan cachondo que era eso o metérsela dentro."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Además,"

                        extend " si hacía algo así,"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows angryx03
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "quizás me dejaría en paz."

                        show neus_exp_mouth sad_Talkingx08
                        show neus_exp_eyebrows angryx04
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Qué clase de lógica es esa?"

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyebrows angryx03
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx03
                        $ nteye = "front03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¡Pensé que era tu amigo!"

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows surprisex00
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "No desde que intentó violarte en el baño."

                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "right01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sadbiting_Silentx07
                        show neus_exp_eyebrows sadx05
                        $ nteye = "right05"
                        call n_closefromup_tears_tears
                        with dissolve

                    "Después de que se fuera la dependienta, acabamos masturbándonos mutuamente en el vestuario." if (aftermorning04_Mast001_Pussy_insert or aftermorning04_Mast001_Pussy_insert):

                        call p_Help

                        $ night05_elysium_NeusStupid_FittingRoomDidac_MastBoth = True

                        $pl.ch_pts("np",-1)

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows suspiciousx2
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Tú también lo masturbaste...?"

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows serious
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Si no hubiera hecho eso,"

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "la cosa hubiera podido acabar en algo más que una simple masturbación."

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyebrows sadx01
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx02
                        show neus_exp_eyebrows sadx03
                        $ nteye = "left04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "ya..."

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyebrows sadx03
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                    "No pasó nada más allá de alguna insinuación.":

                        call p_Help

                        $ night05_elysium_NeusStupid_FittingRoomDidac_NothingTold = True

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿En serio...?"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        if aftermorning04_FittingRoom_FuckherConsent:

                            pt "Mejor no le digo que le metí la polla mientras nos hablaba la dependienta..."

                        elif aftermorning04_FittingRoom_ButtocksDickOverMasturbate:

                            pt "Mejor no le comento como me corrí masturbándome con sus nalgas..."

                        elif (aftermorning04_Mast001_Pussy_insert or aftermorning04_Mast001_Pussy_insert):

                            pt "Mejor no comentarle cómo nos masturbamos mutuamente..."

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyebrows suspiciousx01
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "En serio Neus."

                pause 0.2

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿No ha ocurrido nada más?"

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows suspiciousx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                p "No."

            else: # Not gone to Fitting room with Didac.

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                p "Te lo prometo."

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows suspiciousx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Realmente te crees que soy tan ingenua?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "No sé si eres estúpida,"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows serious
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "¡pero te estoy diciendo la verdad!"

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows suspiciousx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if afternight04_sexbattle_started:

                pt "Espero que me crea..."

                if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                        pt "Por que realmente se la metí hasta el fondo..."

                    else:

                        pt "Por que realmente se la metí..."

                        if afternight04_Pussy_dick_med_Speed_1_Done > 3:

                            pt "y no pocas veces,"

                            extend " precisamente..."

                    pt "Aunque fuera con condón,"

                    extend " no creo que eso sirva de excusa para ella..."

                elif afternight04_Pussy_dick_med_Speed_0_Rape_Done > 0:

                    pt "¡Aunque en realidad yo no hice realmente nada..."

                    pt "fue él quien me violó!"

                elif afternight04_Anal_dick_med_Speed_0_Done > 0:

                    pt "Aunque en realidad solo se la metí por detrás..."

                else:

                    pt "Aunque en realidad no llegué a penetrarla en ningún momento..."

                if afternight04_LeavingSexBattle:

                    pt "De hecho lo dejé antes de tiempo."

                    if mc_body.orgasm == 2:

                        pt "Y eso que me corrí hasta dos veces..."

                    elif mc_body.orgasm == 1:

                        pt "Y eso que hasta me corrí una vez..."

                    elif mc_body.orgasm == 0:

                        pt "Aunque realmente no me corrí ni una sola vez..."

                if girl_1.orgasm > 3:

                    pt "Aunque él tampoco se quedó corto con sus [girl_1.orgasm] corridas..."

                elif girl_1.orgasm == 2:

                    pt "Y él tuvo hasta dos orgasmos..."

                elif girl_1.orgasm == 1:

                    pt "Y él tuvo hasta un orgasmo."

                elif girl_1.orgasm == 0:

                    pt "Pero sí es verdad que no tuvo ningún orgasmo."

            else: # No minigame

                if  (aftermorning04_FittingRoom_FuckherConsent or
                    aftermorning04_FittingRoom_ButtocksDickOverMasturbate or
                    aftermorning04_Mast001_Pussy_insert or
                    aftermorning04_Mast001_Anal_insert):

                    pt "Si no tenemos en cuenta lo que pasó en los vestuarios,"

                    extend " claro..."

                if      (aftermorning05_Deepsea_Fuck_PussyCOND_Cond or
                        aftermorning05_Deepsea_Fuck_PussyRAW_Cond or
                        aftermorning05_Deepsea_Fuck_AnalRAW_Cond or
                        aftermorning05_AfterDeepsea_WakeUp_Sex):

                    pt "Sin mencionar lo que ocurrió en el mar..."

                    if aftermorning05_AfterDeepsea_WakeUp_Sex:

                        pt "Y mejor no hablar de lo ocurrido en la playa..."

                else:

                    pt "¿Por qué le cuesta tanto creerme?"

            jump night05_elysium_WhatNow_After
                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"

label night05_elysium_NeusStupid_After:

    if not gensex_INotLoveYouNeus:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "Un poco estúpida eres."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows suspiciousx02
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "Si complací a Dídac,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows serious
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "no fue porque necesitara hacerlo con él,"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "sino porque de no haberlo hecho,"

    extend " las consecuencias hubieran sido peores."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿A qué te refieres?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex03
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "Iba a salir a la calle a follarse al primero que encontrara."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Eso hubiera sido inútil y completamente imprudente."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Inútil?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si Papá lo convirtió en la ninfómana que mencionas,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "solo su semilla,"

    extend " y por lo tanto tu esperma,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "es lo único que podría calmar su sed y darle los orgasmos que necesita."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    pt "De ahí a que no hubiera manera de sacar mi polla de su cabeza..."

    ##

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Hasta dónde llegasteis?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Otra vez con eso Neus?"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "¿No decías que no teníamos tiempo?"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Oh vamos!"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No vendrá de esto ahora..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    $ night05_elysium_DidacDone_Question_itMatters = False

    menu night05_elysium_DidacDone_Question:

        pt "¿Debería decirle la verdad?"

        "Lo dices como si me importara lo que piensas de mí." if gensex_INotLoveYouNeus:
            $pl.ch_pts("np",-6)

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex03
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Por qué eres así...?"

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx06
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows sadx07
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx09
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ ntlong = 0

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx07
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with fade

            jump night05_elysium_WhatNow_After
                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"

        "<Contarle que ayer se te puso encima, pero que no follaste con él>" if afternight04_sexbattle_started == True:

            call p_Help

            $ night05_elysium_DidacDone_Question_DidacStartSexNo = True

            call night05_elysium_DidacDone_Explanation

                # p "Era eso o dejar que algún yonki o mal nacido de mierda lo dejara preñado."
                # p "Y eso no me lo hubiera perdonado nunca."
                # p "No tuve más remedio que aceptar sus condiciones."
                # ne "..."
                # ne "Pero..."
                # ne "¿Follaste con tu compañero de piso...?"
                # return

            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve
            
            p "¡Por supuesto que no!"

            if (afternight04__MClitoris_Massage_Done or afternight04__Pussy_Fingers_Done) > 0:

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Ya me resultó raro tener que masturbarlo!"

            if (afternight04__MClitoris_Tongue_Done or afternight04__Pussy_Tongue_Done) > 0:

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows suspiciousx01
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "¡Hasta meterle la lengua ahí dónde antes tenía su polla!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Pero lo que no iba a hacer es follarme a mi compañero de piso."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                pt "Espero que se lo crea..."

            $pl.ch_pts("np",5)

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Me alegra que fueras capaz de resistir la tentación."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "Me imagino que no te lo puso nada fácil."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Bueno,"

            extend " no negaré que tuve cierta discusión con mi polla al respecto..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Pero era Dídac!"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Una cosa es hacerle cosas con los dedos,"

            extend " o hasta con la lengua."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "Otra muy distinta es \"hacerlo\"."

            show neus_exp_mouth happy_Silentx02
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmm..."

            show neus_exp_mouth happy_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Hiciste lo correcto."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx02
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Sé que puede sonar raro,"

            extend " pero haberlo dejado deambular por la calle hubiera sido un peligro mayor."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Es lo que me imaginé..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Entonces..."

            extend " ¿no estás decepcionada porque hubiéramos hecho..."

            extend " cosas?"

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "No."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx04
            $ nteye = "left04"
            call n_closefromup_tears_tears
            with dissolve

            ne "No puedo estarlo si Padre influyó en su libido."

            show neus_exp_mouth happy_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "left05"
            call n_closefromup_tears_tears
            with dissolve

            ne "De hecho estoy feliz,"

            show neus_exp_mouth happy_Talkingx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front06"
            call n_closefromup_tears_tears
            with dissolve

            ne "por que pudiste ayudar a tu amigo"

            show neus_exp_mouth happy_Talkingx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "y al mismo tiempo fuiste capaz de resistir la tentación hasta ese punto."

            show neus_exp_mouth happy_Silentx04
            show neus_exp_eyebrows sadx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            if afternight04_Pussy_dick_med_Speed_0_Done > 0:

                pt "Parece que se lo ha creído..."

            else:

                p "..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Aunque espero que conmigo no te resistas tanto..."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            jump night05_elysium_WhatNow_After

                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"
                # ne "pero realmente el tiempo no va a nuestro favor."

        "<Contarle que ayer se te puso encima, y no tuviste otra opción>" if afternight04_sexbattle_started == True and afternight04_Pussy_dick_med_Speed_0_Done > 0:

            call p_Help

            $ night05_elysium_DidacDone_Question_DidacStartSexYes = True

            $pl.ch_pts("np",-5)

            call night05_elysium_DidacDone_Explanation

                # p "Era eso o dejar que algún yonki o mal nacido de mierda lo dejara preñado."
                # p "Y eso no me lo hubiera perdonado nunca."
                # p "No tuve más remedio que aceptar sus condiciones."
                # ne "..."
                # ne "Pero..."
                # ne "¿Follaste con tu compañero de piso...?"
                # return

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Sí."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "Con condón,"

            extend " por supuesto."

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows angryx04
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx10
            show neus_exp_eyebrows angryx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡Menos mal!"

            show neus_exp_mouth sad_Talkingx09
            show neus_exp_eyebrows angryx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¡Eso me tranquiliza un montonazo!"

            extend " ¡Vamos!"

            show neus_exp_mouth sad_Silentx09
            show neus_exp_eyebrows angryx03
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            pt "La ironía no es su punto fuerte..."

            show neus_exp_mouth sad_Silentx10
            show neus_exp_eyebrows angryx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "Neus,"

            extend " tienes que entender que no tenía muchas más opciones..."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx04
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "No creo que te apuntara con una pistola, [protname]..."

            show neus_exp_mouth sad_Silentx08
            show neus_exp_eyebrows suspiciousx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "No,"

            extend " pero te aseguro que su forma de insistir era enfermiza."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows angryx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya..."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "Si no hubiera hecho lo que me pedía,"

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            p "se habría largado a la calle a hacerlo con el primero que se encontrara."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx07
            $ nteye = "left05"
            call n_closefromup_tears_tears
            with dissolve

            p "Nunca me perdonaría que Dídac se quedara embarazado con algún desconocido"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows serious
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "simplemente porque no quise ayudarle."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows serious
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo sé..."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows serious
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Sé lo que se siente en ese estado"

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows sadx03
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "y lo difícil que es controlar esas ansias..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx04
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            ne "Podrías haberlo hecho sin necesidad de penetrarla."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Al fin y al cabo lo único que realmente te pedía era calmar esa ansia,"

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "y para eso no hace falta realmente penetración."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "left04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Al menos a corto plazo..."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo siento,"

            $ ntlong += 1

            show neus_exp_mouth happy_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "front06"
            call n_closefromup_tears_tears
            with dissolve

            ne "Soy así..."

            show neus_exp_mouth happy_Talkingx05
            show neus_exp_eyebrows sadx06
            $ nteye = "left01"
            call n_closefromup_tears_tears
            with dissolve

            $ ntlong += 1

            ne "Aún tenía la vaga esperanza de que solo conmigo te bastara..."

            if not gensex_INotLoveYouNeus:

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                p "Neus,"

                extend " no tiene nada que ver."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyebrows angryx02
                $ nteye = "right02"
                call n_closefromup_tears_tears
                with dissolve

                ne "Ya..."

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx07
            $ nteye = "left05"
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "No parece muy feliz..."

                "Eres mi hermana, ¿Cómo diablos quieres que sienta algo por ti?" if night05_elysium_whyAmISoSpecial_Cond and gensex_INotLoveYouNeus:
                    call p_Help
                    $pl.ch_pts("np",-4)

                    $ gensex_NotLoveSister = True

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx03
                    $ nteye = "right04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque sea tu hermana de sangre,"

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "yo nunca te podría considerar un hermano."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows serious
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Te amo demasiado para eso."

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx04
                    $ nteye = "left02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque por lo visto,"

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows sadx05
                    $ nteye = "left04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "tú no sientes lo mismo..."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx06
                    $ nteye = "left05"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    pause 0.2

                    $ ntlong = 0

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyebrows sadx07
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with fade

                        # jump night05_elysium_WhatNow_After
                            # p "¿Qué es lo que quieres hacer?"
                            # ne "..."
                            # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"
                            # ne "pero realmente el tiempo no va a nuestro favor."

                "De verdad que me gustas mucho." if not gensex_INotLoveYouNeus:
                    call p_Help

                    $ night05_elysium_DidacDone_Question_DidacStartSexYes_ILikeYou = True

                    $pl.ch_pts("np",1)

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows surprisex01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows serious
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "A mi también me gusta mucho mi gato,"

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyebrows angryx02
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "pero no por eso tengo ganas de tener sexo con él."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows suspiciousx02
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "No te considero un gato."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows angryx02
                    $ nteye = "right02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx06
                    $ nteye = "right05"
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        pt "¿Sexo con su gato? ¿Por qué diablos me ha metido esa imagen en la cabeza?"

                        "Te lo digo en serio.":
                            call p_Help

                            $pl.ch_pts("np",1)

                            $ gensex_ILoveYouNeus = True

                            show neus_exp_mouth sadbiting_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            show neus_exp_mouth sad_Talkingx02
                            show neus_exp_eyebrows sadx03
                            $ nteye = "left04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Ya..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx04
                            $ nteye = "left05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pt "Desde luego,"

                            pt "vaya poca confianza tiene la chica."

                        "En cualquier caso serías más bien una gata en celo.":
                            call p_Help

                            $pl.ch_pts("np",2)

                            $ gensex_ILoveYouNeus = True

                            show neus_exp_mouth sad_Silentx02
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Vale,"

                            extend " eso quizás ha sonado mal..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Pero te lo digo de verdad,"

                            extend " me gustas mucho."

                            $ ntlong += 1

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx003
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Serás tonto..."

                            $ ntlong += 1

                            show neus_exp_mouth happy_Silentx04
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Hmm..."

                            show neus_exp_mouth happy_Talkingx04
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front06"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Gra-"

                            extend "gracias,"

                            $ ntlong += 1

                            show neus_exp_mouth happy_Talkingx03
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "[protname]..."

                            show neus_exp_mouth happy_Silentx04
                            show neus_exp_eyebrows sadx05
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ ntlong = 0

                            show neus_exp_mouth happy_Silentx03
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                        "...":
                            call p_Help
                            $pl.ch_pts("np",-1)

                            show neus_exp_mouth happy_Silentx06
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                "Creo que me estoy enamorando de ti, Neus." if not gensex_YoureAMonster:
                    call p_Help

                    $ night05_elysium_DidacDone_Question_DidacStartSexYes_FallingInLove = True

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows surprisex03
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    if gensex_INotLoveYouNeus:

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pensaba que habías dicho que no me amabas."

                        if night05_elysium_whyAmISoSpecial_Cond:

                            show neus_exp_mouth sad_Talkingx07
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Que no podías amar a tu hermana."

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows surprisex02
                        $ nteye = "front00"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Puedo cambiar de opinión."

                        show neus_exp_mouth sad_Talkingx004
                        show neus_exp_eyebrows suspiciousx01
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Ya veo que tu opinión es bastante voluble."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Cree lo que quieras,"

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows sadx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "pero te estoy siendo sincero."

                    else:

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "¿Solo lo crees?"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        menu:

                            pt "¡¿Es que quiere un certificado oficial avalado por el notario?!"

                            "¿Por qué te cuesta tanto creerme?":
                                call p_Help
                                $pl.ch_pts("np",1)

                                $ gensex_ILoveYouNeus = True

                                show neus_exp_mouth sad_Talkingx004
                                show neus_exp_eyebrows angryx02
                                $ nteye = "front03"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Realmente crees que no tengo motivos?"

                                show neus_exp_mouth sad_Silentx03
                                show neus_exp_eyebrows surprisex01
                                $ nteye = "front01"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Estoy siendo sincero."

                                show neus_exp_mouth sad_Silentx04
                                show neus_exp_eyebrows serious
                                $ nteye = "right02"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sad_Talkingx002
                                show neus_exp_eyebrows sadx02
                                $ nteye = "right04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Supongo..."

                                show neus_exp_mouth sad_Silentx05
                                show neus_exp_eyebrows sadx04
                                $ nteye = "right05"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¿Solo supones?"

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                            "Te lo digo en serio.":
                                call p_Help
                                $pl.ch_pts("np",1)

                                $ gensex_ILoveYouNeus = True

                                show neus_exp_mouth sad_Talkingx003
                                show neus_exp_eyebrows suspiciousx02
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Ya..."

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx05
                                $ nteye = "right04"
                                call n_closefromup_tears_tears
                                with dissolve

                                pt "No parece muy convencida."

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx05
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                            "Han pasado solamente tres días, dame algo más de tiempo.":
                                call p_Help

                                $pl.ch_pts("np",2)

                                show neus_exp_mouth sadbiting_Silentx02
                                show neus_exp_eyebrows surprisex01
                                $ nteye = "front00"
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¿O prefieres que te mienta?"

                                show neus_exp_mouth sad_Talkingx03
                                show neus_exp_eyebrows sadx04
                                $ nteye = "front04"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No,"

                                extend " de hecho agradezco mucho más tu sinceridad."

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx03
                                $ nteye = "right05"
                                call n_closefromup_tears_tears
                                with dissolve

                            "...":
                                $pl.ch_pts("np",-1)

                                show neus_exp_mouth sad_Silentx06
                                show neus_exp_eyebrows sadx06
                                $ nteye = "front05"
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx07
                                $ nteye = "front08"
                                call n_closefromup_tears_tears
                                with dissolve

                    pause 0.2

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Entonces por qué hiciste eso con Dídac?"

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Ya te he dicho por qué."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows serious
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Si mi explicación no te ha resultado suficiente,"

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyebrows angryx01
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "nada de lo que te diga te servirá."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque no te lo creas,"

                    extend " hace tiempo que siento algo por ti."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Y me alegro de que al menos haya alguna esperanza"

                    show neus_exp_mouth happy_Talkingx03
                    show neus_exp_eyebrows sadx02
                    $ nteye = "front06"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "de que tú puedas sentir algo parecido."

                    if night05_elysium_whyAmISoSpecial_Cond:

                        show neus_exp_mouth happy_Talkingx04
                        show neus_exp_eyebrows sadx05
                        $ nteye = "front07"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "A pesar de lo que opines sobre nuestro lazo de sangre."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ gensex_ILoveYouNeus = True

                "Estoy enamorado de ti, Neus." if not gensex_INotLoveYouNeus:
                    call p_Help

                    $pl.ch_pts("np",1)

                    $ gensex_ILoveYouNeus = True

                    $ night05_elysium_DidacDone_Question_DidacStartSexYes_InLove = True

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows surprisex03
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows serious
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Me resultaría más fácil creerte,"

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows angryx01
                    $ nteye = "right03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "si no fuera cierto lo que me acabas de contar."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Ya te he dicho el por qué lo he hecho."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Sí."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx04
                    $ nteye = "left01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Pero si tus sentimientos fueran sinceros,"

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx03
                    $ nteye = "left02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "no hubieras podido hacer nada con él,"

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "o habrías buscado otro modo de hacerlo."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Entiendo los motivos,"

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx05
                    $ nteye = "left05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "pero eso no quita que me hace daño."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Neus..."

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx06
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Habría preferido que me hubieras dicho \"eso\""

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "cuando realmente lo sintieras,"

                    $ ntlong += 1

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx05
                    $ nteye = "left02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "no porque simplemente creas que me voy a sentir mejor por escuchar una mentira."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx06
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        pt "Una mentira..."

                        "Lo he dicho de corazón.":
                            call p_Help
                            $pl.ch_pts("np",1)

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx03
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Bueno,"

                            show neus_exp_mouth sad_Talkingx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "right04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "perdona,"

                            extend " pero me cuesta creerlo."

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx05
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                        "Lo siento.":
                            call p_Help
                            $pl.ch_pts("np",-2)

                            show neus_exp_mouth sad_Talkingx03
                            show neus_exp_eyebrows angryx01
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Disculpándote no me haces sentir mejor..."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx06
                            $ nteye = "left05"
                            call n_closefromup_tears_tears
                            with dissolve

                        "...":
                            call p_Help
                            $pl.ch_pts("np",-1)

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows sadx05
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx06
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                    p "..."

                "<No decir nada al respecto>":
                    call p_Help
                    $pl.ch_pts("np",-2)

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx06
                    $ nteye = "right05"
                    call n_closefromup_tears_tears
                    with dissolve

            jump night05_elysium_WhatNow_After

                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"
                # ne "pero realmente el tiempo no va a nuestro favor."

        "De verdad, no hicimos nada.":
            call p_Help

            $ night05_elysium_DidacDone_Question_DidacStartNO = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if afternight04_sexbattle_started:

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows suspiciousx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                pt "Espero que cuele..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx04
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Me cuesta de creerlo..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¿Y luego soy yo el desconfiado?"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "left04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx02
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "De acuerdo."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx01
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Si dices que no hiciste nada,"

            extend " supongo que..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx03
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Tengo que creerte."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            if not afternight04_sexbattle_started:

                pt "Es desconfiada de narices..."

            else:

                pt "No parece muy convencida..."

            jump night05_elysium_WhatNow_After

                # p "¿Qué es lo que quieres hacer?"
                # ne "..."
                # ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"
                # ne "pero realmente el tiempo no va a nuestro favor."

        "¿Acaso importa?" if night05_elysium_DidacDone_Question_itMatters == False:
            call p_Help

            #$pl.ch_pts("np",-1)

            $ night05_elysium_DidacDone_Question_itMatters = True

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows angryx02
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Sí,"

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows angryx03
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "a mi me importa."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows angryx02
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx06
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            jump night05_elysium_DidacDone_Question

label night05_elysium_DidacDone_Explanation:

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Era eso o dejar que algún yonki o mal nacido de mierda lo dejara preñado."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "Y eso no me lo hubiera perdonado nunca."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    p "No tuve más remedio que aceptar sus condiciones."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Follaste con tu compañero de piso...?"

    return

#######
#######

# label night05_elysium_DidacDone_After:

    # p "Tampoco me dejó muchas más opciones..."

    # ne "No creo que te apuntara con una pistola."

    # ne "Siempre tuviste opción."

    # p "..."

    # p "¿Realmente importa?"

    # ne "..."

    # ne "No..."

    # ne "Supongo que no..."

    # pt "Que situación más incomoda..."

    # jump night05_elysium_WhatNow_After

label night05_elysium_WhatNow_After:

    if ntlong > 0:

        $ ntlong = 0

        show neus_exp_mouth sadbiting_Silentx07
        show neus_exp_eyebrows sadx06
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with fade

        pause 0.2

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué es lo que quieres hacer?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Hubiera preferido que nuestra primera vez fuera en mejores condiciones,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx06
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "pero realmente el tiempo no va a nuestro favor."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Podrías apagar la luz?"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Por qué?"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Prefiero hacerlo a oscuras..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Puedo saber por qué?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando me excito..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "suelo perder el control de mi propio cuerpo,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    ne "y es posible que veas cosas que quizás no te gusten..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "A oscuras quizás verás mis ojos brillar,"

    extend " pero poco más..."

    if night04_pedrera_blowjob_DONE == True:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows surprisex02
        $ nteye = "front00"
        call n_closefromup_tears_tears
        with dissolve

        p "¿Como tu extraordinariamente longeva lengua?"

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows sadx04
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows sadx01
        $ nteye = "front03"
        call n_closefromup_tears_tears
        with dissolve

        p "Quizás no la vi con detalle,"

        show neus_exp_mouth sad_Silentx07
        show neus_exp_eyebrows sadx03
        $ nteye = "right02"
        call n_closefromup_tears_tears
        with dissolve

        p "pero desde luego la sentí."

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows sadx01
        $ nteye = "right01"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Tanto te disgustó?"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx06
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "¿Si me disgustó sentir una ardiente lengua que se alargaba por lo menos un metro y pico...?"

            "Fue una sensación extraña, pero agradable.":

                call p_Help

                $pl.ch_pts("np",2)

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿De verdad?"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows sadx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "Sinceramente,"

                extend " fue una experiencia bastante curiosa."

                show neus_exp_mouth happy_Silentx03
                show neus_exp_eyebrows sadx02
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth happy_Talkingx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front07"
                call n_closefromup_tears_tears
                with dissolve

                ne "Me alegra oír eso..."

                show neus_exp_mouth happybiting_Silentx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

            "En realidad me encantó.":

                call p_Help

                $pl.ch_pts("np",3)

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿No lo dices para quedar bien?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex02
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¿Por qué te cuesta tanto creerme?"

                if night05_elysium_pederast_Cond:

                    show neus_exp_mouth sad_Talkingx09
                    show neus_exp_eyebrows angryx03
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¡¿Quizás porque me has dicho que soy una jodida pederasta?!"

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows surprisex01
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Eso no tiene nada que ver."

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyebrows suspiciousx03
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                elif not gensex_ILoveYouNeus:

                    show neus_exp_mouth sad_Talkingx004
                    show neus_exp_eyebrows sadx01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Realmente crees que no tengo motivos?"

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx03
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right05"
                    call n_closefromup_tears_tears
                    with dissolve

                pause 0.2

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyebrows sadx03
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Porque siempre que he llegado a mostrar ese aspecto de mi,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows sadx01
                $ nteye = "left03"
                call n_closefromup_tears_tears
                with dissolve

                ne "generalmente la gente ya no me suele ser sincera..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows sadx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Quizás porque saben que no saldrán de ahí con vida."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                p "Pero yo te lo digo con sinceridad."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx02
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                p "Y al menos que yo sepa,"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows surprisex01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "con la idea de que voy a salir de aquí con vida."

                show neus_exp_mouth happy_Silentx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "Hmm..."

                show neus_exp_mouth happy_Talkingx05
                show neus_exp_eyebrows sadx02
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "Con lo que te voy a hacer,"

                show neus_exp_mouth happy_Talkingx06
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "probablemente no quieras ni salir de esta habitación."

                show neus_exp_mouth happy_Silentx05
                show neus_exp_eyebrows sadx03
                $ nteye = "front07"
                call n_closefromup_tears_tears
                with dissolve

                pt "No estoy muy seguro de cómo tomarme esa frase..."

                show neus_exp_mouth happybiting_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with dissolve

            "Sinceramente, fue bastante desagradable.":

                call p_Help

                $pl.ch_pts("np",-4)

                $ night05_elysium_WhatNow_After_BlowjobDisgusting = True

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows surprisex03
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyebrows angryx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyebrows angryx04
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Si te llegaste a correr,"

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyebrows angryx03
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "tan desagradable no sería."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows serious
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "Me corrí porque hiciste otras cosas"

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows suspiciousx03
                $ nteye = "front00"
                call n_closefromup_tears_tears
                with dissolve

                p "aparte de usar esa lengua tan monstruosa..."

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyebrows angryx04
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Hace falta que la describas de esta manera?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyebrows surprisex03
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                p "¿No me has pedido sinceridad?"

                $ ntlong += 1

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyebrows angryx04
                $ nteye = "right03"
                call n_closefromup_tears_tears
                with dissolve

                ne "Tampoco hace falta que lo seas tanto."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx04
                $ nteye = "right04"
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ ntlong += 1

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows angryx02
                $ nteye = "left04"
                call n_closefromup_tears_tears
                with dissolve

                ne "Tranquilo,"

                extend " que no te la volveré a chupar más."

                $ ntlong += 1

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows angryx02
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

        #jump night05_elysium_NeusPushesToBed

    menu:

        pt "La habitación es bonita, pero lo que hay fuera de ella..."

        "¿Es realmente necesario que lo hagamos aquí?":

            call p_Help

            #$pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex02
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows suspiciousx03
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿El problema lo tienes con el lugar,"

            extend " o conmigo?"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Hay sangre reseca en las puertas"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "left02"
            call n_closefromup_tears_tears
            with dissolve

            p "y gente gritando de dolor por el pasillo que hay ahí fuera."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows normal
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Perdona si te ofendo,"

            extend " pero no me resulta el panorama más sensual imaginable."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex03
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Quizás soy raro!"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero tienes que entender que no había otro lugar al que pudiéramos ir..."

            if (night05_Park_RollerCoaster_Used or
                night05_Park_RollerCoaster_Queuing_Enjoyed_Cond or 
                night05_Park_MinigameShooter_Played):

                if pl.np >= 120: # NOT_FINISHED... number?

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Te aseguro que no es así como me había imaginado"

                    show neus_exp_mouth happy_Talkingx03
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "el final de esta maravillosa noche que he pasado contigo."

                else:

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx04
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Te aseguro que no es así como me había imaginado el final de esta noche."

                if night05_Park_MinigameShooter_Played == False:

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque me hubiera gustado que hubieras probado suerte disparando con la escopeta..."

                elif night05_Park_RollerCoaster_Used == False:

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx05
                    $ nteye = "left03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque me hubiera gustado que hubieras subido a la montaña rusa conmigo..."

                elif night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False:

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyebrows sadx05
                    $ nteye = "left03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque me hubiera gustado no tener la sensación"

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows suspiciousx01
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "de que te obligué a subirte a la montaña rusa conmigo..."

            else:

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_eyebrows sadx03
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Te aseguro que no es así como me había imaginado el final de nuestra cita,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows suspiciousx02
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "a pesar de lo poco participativo que has estado,"

                show neus_exp_mouth happy_Talkingx02
                show neus_exp_eyebrows sadx05
                $ nteye = "front06"
                call n_closefromup_tears_tears
                with dissolve

                ne "realmente he disfrutado estando a tu lado esta noche."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx04
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Por desgracia,"

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx05
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "no tenemos muchas más opciones."

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows sadx04
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Si no lo haces por mí,"

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "al menos hazlo para que puedas salir de aquí con vida."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx06
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            if not gensex_INotLoveYouNeus:

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyebrows sadx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "Tampoco hace falta tomárselo así..."

                show neus_exp_mouth sad_Talkingx002
                show neus_exp_eyebrows sadx05
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero es la verdad."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx05
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                p "Hmm..."

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows sadx04
                $ nteye = "front08"
                call n_closefromup_tears_tears
                with dissolve

            else:

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows sadx01
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "Supongo que si no hay más remedio..."

                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows sadx05
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows sadx07
                $ nteye = "right05"
                call n_closefromup_tears_tears
                with dissolve

        "<Aceptar hacerlo con ella>":
            call p_Help

            #$pl.ch_pts("np",1)

        "Me estoy muriendo de ganas de hacerlo contigo." if not gensex_INotLoveYouNeus:
            call p_Help

            $pl.ch_pts("np",2)

            $ gensex_ILoveYouNeus = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows sadx01
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Lo dices de verdad?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex03
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Pues claro!"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "Aunque te cueste creerlo,"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "me gustas Neus,"

            extend " mucho."

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero..."

            ne "pensaba,"

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx04
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            extend " que lo de ser hermanos,"

            extend " te iba..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "A ver..."

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows sadx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "No te voy a negar que eso da,"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            p "como un rollo extraño a toda esta situación..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows normal
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡Pero demonios!"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx03
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "te he conocido sin saber que teníamos lazos de sangre,"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "así que en el fondo no es algo que debiera importarme."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            pt "Sin mencionar lo retorcida que es la herencia sanguínea de..."

            extend " ¿nuestra familia?"

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows normal
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Eres una mujer encantadora,"

            extend " con un corazón de oro."

            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_eyebrows sadx03
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Y para que negarlo,"

            if night04_pedrera_blowjob_DONE:

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                p "dejando de lado la mamada de ayer..."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex03
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            p "llevo dos días con los huevos azules por tu culpa."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows suspiciousx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Que otra cosa no sé,"

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            p "pero sabes ponerme caliente."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if (night05_elysium_DidacDone_Question_DidacStartSexYes or
                night05_elysium_NeusStupid_FittingRoomDidac_FuckherConsent or
                night05_elysium_NeusStupid_FittingRoomDidac_ButtocksMast or
                night05_elysium_NeusStupid_FittingRoomDidac_MastBoth):

                show neus_exp_mouth sad_Talkingx005
                show neus_exp_eyebrows surprisex01
                $ nteye = "front05"
                call n_closefromup_tears_tears
                with dissolve

                ne "Tampoco habrás sufrido mucho por lo que me has contado..."

                if night05_elysium_DidacDone_Question_DidacStartSexYes:

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows suspiciousx02
                    $ nteye = "front03"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Especialmente si llegaste a follarte a tu compañero de piso,"

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows suspiciousx03
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "me imagino que te habrás corrido alguna que otra vez."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyebrows serious
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    if night05_elysium_NeusStupid_FittingRoomDidac_FuckherConsent:

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows suspiciousx01
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Le metiste la polla a Dídac antes que a mí."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Pero fue solo un momento,"

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "y ya te dije que fue con la intención de asustarle"

                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows angryx02
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "que supiera que iba en serio y se acojonara."

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Muy original no eres,"

                        extend " si no se te ocurrió otra manera..."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows angryx01
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                    elif night05_elysium_NeusStupid_FittingRoomDidac_ButtocksMast:

                        show neus_exp_mouth sad_Talkingx004
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Especialmente después de masturbarte con sus nalgas, me imagino que te corriste a gusto con ellas."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front05"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows angryx02
                        $ nteye = "left02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Mis nalgas no son tan voluminosas..."

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows surprisex01
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¡Neus!"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyebrows serious
                        $ nteye = "front02"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Ya sabes por qué hice eso con Dídac!"

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows angryx02
                        $ nteye = "left03"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Lo que sé,"

                        extend " es porque la tenías tan dura con él..."

                        show neus_exp_mouth sad_Silentx06
                        show neus_exp_eyebrows suspiciousx03
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Lo dices como si no la tuviera dura contigo."

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyebrows angryx03
                        $ nteye = "front08"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Quizás ese es el problema,"

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows angryx02
                        $ nteye = "right01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "no importa con quien,"

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyebrows angryx03
                        $ nteye = "right02"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "se te pone igualmente dura."

                        $ ntlong += 1

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx05
                        $ nteye = "right04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No tengo nada de especial."

                        $ ntlong += 1

                        show neus_exp_mouth sadbiting_Silentx06
                        show neus_exp_eyebrows sadx07
                        $ nteye = "right05"
                        call n_closefromup_tears_tears
                        with dissolve

                    elif night05_elysium_NeusStupid_FittingRoomDidac_MastBoth:

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows suspiciousx02
                        $ nteye = "front01"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Especialmente después de que os masturbarais mutuamente en los probadores."

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyebrows surprisex02
                        $ nteye = "front04"
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me imagino que te corriste a gusto..."

                        if morning04_Shopping_didaccum_Cond:

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "En realidad no llegué a correrme."

                            show neus_exp_mouth sad_Talkingx002
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿No...?"

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows surprisex02
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Fui más rápido que él y terminó corriéndose tan fuerte que cayó al suelo sin poder terminar lo que hacía."

                            show neus_exp_mouth sadbiting_Silentx04
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            $pl.ch_pts("np",3)

                            show neus_exp_mouth sad_Talkingx003
                            show neus_exp_eyebrows sadx03
                            $ nteye = "right02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Lo-"

                            extend "lo siento..."

                            show neus_exp_mouth sad_Talkingx04
                            show neus_exp_eyebrows sadx04
                            $ nteye = "right03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Te he juzgado demasiado rápido..."

                            show neus_exp_mouth sad_Talkingx05
                            show neus_exp_eyebrows sadx05
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Pensé que el cuerpo de Dídac te habría hipnotizado de tal manera,"

                            show neus_exp_mouth sad_Talkingx04
                            show neus_exp_eyebrows sadx02
                            $ nteye = "left04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "que lo de ayudar a Dídac,"

                            extend " era tan solo una excusa."

                            show neus_exp_mouth sad_Talkingx05
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Cuando en realidad,"

                            extend " lo único que intentabas era ayudarle..."

                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx06
                            $ nteye = "down05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pt "Bueno si fuera sincero,"

                            extend " lo que intentaba era ganarle a su juego,"

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows sadx07
                            $ nteye = "right05"
                            call n_closefromup_tears_tears
                            with dissolve

                            pt "como solemos hacer,"

                            pt " pero mejor,"

                            extend " no discuto con ella sobre esto..."

                            show neus_exp_mouth happy_Talkingx03
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Eres un buen amigo [protname]."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows serious
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "No estoy convencido de que sea la mejor manera de mantener"

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows normal
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "una sana relación de pura amistad"

                            show neus_exp_mouth sad_Silentx02
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front00"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "eso de ir masturbándose mutuamente,"

                            show neus_exp_mouth happy_Silentx03
                            show neus_exp_eyebrows suspiciousx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "pero tampoco es que sea yo un experto en el tema..."

                            show neus_exp_mouth happy_Talkingx05
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front06"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "No seas tonto."

                            show neus_exp_mouth sad_Talkingx004
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Sabes que Dídac no estaba bien,"

                            show neus_exp_mouth happy_Talkingx07
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "y aún así hiciste lo posible para ayudarle."

                            show neus_exp_mouth happy_Talkingx06
                            show neus_exp_eyebrows sadx02
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Eres más buena persona de lo que eres capaz de admitir."

                            show neus_exp_mouth happy_Talkingx05
                            show neus_exp_eyebrows sadx03
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Y ese es uno de los encantos que más me gustan de ti."

                            show neus_exp_mouth happy_Silentx05
                            show neus_exp_eyebrows sadx01
                            $ nteye = "front06"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            show neus_exp_mouth happybiting_Silentx06
                            show neus_exp_eyebrows sadx04
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                        else:

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows normal
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Bueno..."

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows suspiciousx03
                            $ nteye = "front0."
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Debo reconocer que tiene algo de práctica en masturbar una polla..."

                            show neus_exp_mouth sad_Talkingx08
                            show neus_exp_eyebrows angryx02
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿Esa es tu excusa?"

                            show neus_exp_mouth sad_Silentx06
                            show neus_exp_eyebrows angryx01
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Es la verdad."

                            show neus_exp_mouth sad_Talkingx004
                            show neus_exp_eyebrows angryx02
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Creí que intentabas ayudar a tu amigo."

                            show neus_exp_mouth sad_Silentx03
                            show neus_exp_eyebrows surprisex01
                            $ nteye = "front01"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Es un juego que tenemos desde siempre..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows suspiciousx01
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "ver quien es el mejor,"

                            extend " en lo que sea."

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows angryx01
                            $ nteye = "front04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx06
                            show neus_exp_eyebrows suspiciousx03
                            $ nteye = "front03"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¿Os habíais masturbado antes mutuamente?"

                            show neus_exp_mouth sad_Silentx05
                            show neus_exp_eyebrows suspiciousx02
                            $ nteye = "front05"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            show neus_exp_mouth sad_Silentx04
                            show neus_exp_eyebrows angryx01
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                            p "No..."

                            $pl.ch_pts("np",-3)

                            show neus_exp_mouth sad_Talkingx06
                            show neus_exp_eyebrows angryx03
                            $ nteye = "front02"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Entonces no es un juego entre amigos."

                            show neus_exp_mouth sad_Talkingx04
                            show neus_exp_eyebrows sadx03
                            $ nteye = "right04"
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Es algo más."

                            show neus_exp_mouth sadbiting_Silentx06
                            show neus_exp_eyebrows sadx06
                            $ nteye = "front08"
                            call n_closefromup_tears_tears
                            with dissolve

                    #ne "me imagino que al menos te habrás corrido una vez con él..."

                p "..."

                if night05_elysium_DidacDone_Question_DidacStartSexYes:

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyebrows angryx02
                    $ nteye = "front06"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Euh..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows angryx03
                    $ nteye = "front08"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Bahh..."

                    show neus_exp_mouth sad_Talkingx004
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿A quien quiero engañar?"

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front04"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Realmente no puedo más..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx05
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    show neus_exp_mouth sad_Silentx02
                    show neus_exp_eyebrows surprisex02
                    $ nteye = "front00"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡Pero solo me he corrido una vez!"

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyebrows surprisex01
                    $ nteye = "front01"
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡En tres días!"

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows suspiciousx01
                    $ nteye = "front02"
                    call n_closefromup_tears_tears
                    with dissolve

                    if FuckM_Start_Cond or FuckH_Start_Cond:

                        pt "Si no contamos lo que he hecho con Meritxell,"

                        if FuckH_Start_Cond:

                            extend " y Hiromi,"

                        extend "claro..."

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx04
                    $ nteye = "right02"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Hmmm..."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows surprisex01
                    $ nteye = "front05"
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Bueno,"

                    extend " me imagino que algo cargadito aún estarás entonces..."

                    if night05_Park_Bathroom_Sweet_Cond:

                        ne "Al fin y al cabo en el baño la tenías bien dura..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx04
                    $ nteye = "down05"
                    call n_closefromup_tears_tears
                    with dissolve

            else:

                show neus_exp_mouth sad_Talkingx01
                show neus_exp_eyebrows surprisex02
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "Euhh..."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows sadx01
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with dissolve

                ne "Ya..."

                show neus_exp_mouth happy_Talkingx03
                show neus_exp_eyebrows sadx03
                $ nteye = "down05"
                call n_closefromup_tears_tears
                with dissolve

                ne "Es que me gusta imaginármelo relleno de comi..."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows angryx02
                $ nteye = "front06"
                call n_closefromup_tears_tears
                with dissolve

                ne "digo,"

                extend " de esperma..."

                show neus_exp_mouth happybiting_Silentx06
                show neus_exp_eyebrows sadx05
                $ nteye = "down04"
                call n_closefromup_tears_tears
                with dissolve

            jump night05_elysium_NeusPushesToBed

                # p "¡Ugh!"
                # n "De pronto te tira encima de la cama."
                # p "¡Neus!"
                # ne "Por favor,"
                # extend " simplemente relájate..."
                # 
        "Lo siento, pero el hecho de que seas mi hermana me impide tener ganas de tener sexo contigo, Neus." if gensex_INotLoveYouNeus and gensex_NotLoveSister:
            call p_Help

            jump night05_NeusLastDate_ElysiumDontWant


        "No me gustas lo suficiente aún como para tener sexo contigo, Neus." if not gensex_ILoveYouNeus:
            call p_Help

            jump night05_NeusLastDate_ElysiumDontWant

    jump night05_elysium_acceptNeus

################################################################################################
################################
################################################################################################
################################################################################################
################################
################################################################################################
################################################################################################
################################
################################################################################################
################################################################################################
################################
################################################################################################

label night05_NeusLastDate_ElysiumBloodDeath:

    scene day05

    ono "snif-snif"

    n "El tipo delgaducho voltea su cabeza y te mira con unos ojos inyectados en sangre."

    sdel "¡Cierra la puerta!"

    n "El tipo fortachón se queda unos segundos sin reaccionar y su mirada se dirige hacia su jefa."

    re "¡¿A qué estás esperando?!"

    re "¡Ciérrala!"

    n "Sujetándola con ambas manos -y con cierto esfuerzo- desplaza ese enorme portón."

    ono "CLONCK"

    sdel "¡Mantenla cerrada!"

    re "¿Qué ocurre?"

    sdel "Su sangre."

    re "¿El chico?"

    #re "¿Está sangrando?"

    n "Observas que el tipo flacucho está empezando a salivar"

    n "sin quitarte esos perturbadores ojos de encima."

    ne "¡Me habías dicho que no tenías ninguna herida!"

    p "No es una herida abierta."

    re "¡No discutas con él y lar...!"

    with hpunch
    with hpunch
    ono "{size=80}PAAM{/size}"

    n "El estruendo metal de la puerta resuena a lo largo de esa cueva,"

    n "como si alguien le hubiera dado un monstruoso golpe."

    
    with vpunch
    ono "{size=90}PAM{w=0.1}{nw}"
    with hpunch
    extend " PAM{w=0.1}{nw}"
    with vpunch
    extend " PAM{w=0.1}{nw}"
    with hpunch
    extend " PAM{w=0.1}{nw}"
    with vpunch
    extend " PAM{/size}"

    n "Una serie de golpes se amontonan a lo largo y ancho del gigante de hierro."

    with hpunch
    p "¡Ugh!"

    n "Neus te agarra del brazo y te arranca de ahí saliendo con una increíble celeridad."

    n "En esa oscuridad y a esa velocidad eres incapaz de ver nada."

    # RUIDO DEL portón cayéndose?

    n "Cuando a penas estáis por la mitad de la escalinata,"

    n "Neus salta abruptamente."

    n "Sientes que choca contra algo"

    n "y en un forcejeo rápido termina cayendo de bruces contra el suelo"

    n "mientras te agarra con fuerza para que no sientes el impacto."

    #p01_name = (_("Tipo Extraño"))

    p01 "¿Qué llevas ahí, muñeca?"

    ne "..."

    $ p02_name = (_("Otro tipo extraño"))

    p01 "Has tenido la mala suerte de que llegásemos nosotros ahora mismo."

    n "Al fijarte de dónde viene la voz, ves a dos tipos vestidos con ropajes oscuros y con el pelo estilo punk,"

    n "pero lo que más te llama la atención es que sus miran en dirección al suelo."

    p02 "¿No nos ha dicho el jefe que la inmovilicemos?"

    n "Mientras estáis en el suelo, percibes las manos de Neus aferrándose a ti con más garra."

    p01 "¿Tú la has visto?"

    p01 "Si parece una niña."

    p02 "¡El jefe nos ha dicho que no la miremos a los ojos!"

    p01 "¡Y no la estoy mirando a los ojos!"

    with hpunch
    ono "{size=80}PAAAMMM{/size}"

    n "El atronador ruido del enorme portón de metal que habéis dejado atrás te hiela la sangre."

    p01 "Tiene pinta de que ya..."

    with vpunch
    p01 "¡OUCH!"

    n "Neus se lanza sobre el tipo que está obstaculizando el paso."

    n "Cuando el otro intenta agarrarla,"

    n "esta consigue darle una veloz patada saltando encima de él"

    n "para -con suma celeridad- seguir subiendo las escaleras."

    n "Justo cuando llegáis a la cima de esa escalinata,"

    with vpunch
    p "{size=60}¡AAUhch!{/size}"

    n "Neus cae al suelo lanzándote al piso abruptamente."

    ne "{size=80}¡AAAARGH!{/size}"

    n "Ves su cuerpo siendo aplastado por un grupo de seres monstruosos"

    n "mientras estos te fijan una mirada que te deja sin aliento."

    n "Uno de ellos se lanza hacia ti"

    p "¡Augh...!"

    n "clavando sus longevos colmillos en tu cuello."

    n "Con la vista nublada, percibes que otro hace lo mismo, pero en tu pierna."

    p "¡Ugh...!"

    n "Alguien te agarra del brazo."

    n "El que te está mordiendo el cuello lo empuja con tanta fuerza que termina alejándolo,"

    with hpunch
    with hpunch
    p "{size=80}¡¡AAAARGHHH!!{/size}"

    n "no sin que este se lleve tu brazo arrancándolo en el proceso."

    n "Vorazmente otros cuerpos se van amontonando encima de ti mientras pelean con uñas y dientes"

    n "por cada gota de tu sangre."

    n "Apenas eres capaz de respirar,"

    n "y el martirio es tan extremo"

    n "que todo se vuelve borroso."

    n "Tus párpados se cierran."

    scene black
    with fade

    n "Y todo se vuelve negro."

    aj "Final alternativo zz (not sure about number yet)"

    jump gameover

    # You didn't tell her about your nose thing, and your blood is exposed.

label night05_NeusLastDate_ElysiumDontWant:

    #$pl.ch_pts("np",1)

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ ntlong += 1

    if gensex_NotLoveSister:

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx03
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Por que soy tu hermana..."

    else:

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyebrows sadx04
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "No..."

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyebrows sadx04
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿No te gusto lo suficiente...?"

        if night05_elysium_whyAmISoSpecial_Cond:

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Es por que sabes que soy tu hermana?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "Tener sexo con mi hermana..."

        "No tiene nada que ver." if night05_elysium_whyAmISoSpecial_Cond and not gensex_NotLoveSister:
            call p_Help

            $pl.ch_pts("np",-10)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows suspiciousx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyebrows sadx05
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya..."

        "En parte." if night05_elysium_whyAmISoSpecial_Cond:
            call p_Help

        "Así es." if night05_elysium_whyAmISoSpecial_Cond:
            call p_Help

        "Realmente no." if not night05_elysium_whyAmISoSpecial_Cond:
            call p_Help

        "Lo siento.":
            call p_Help

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Acaso no lo entiendes?"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Es el único modo de sobrevivir."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Me estás pidiendo que te folle para no morir?"

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows sadx05
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx06
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Podría volver con Padre e intentar suplicarle que te perdone la vida."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx07
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Eso es una opción?"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si te resulta imposible hacerlo conmigo,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx06
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "no veo otra alternativa."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero francamente,"

    extend " conociéndole,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "dudo mucho que te permita vivir."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows angryx01
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ntlong = 0

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2


    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Qué quieres hacer?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    $ night05_NeusLastDate_ElysiumDontWant_Cond = ""

    menu night05_NeusLastDate_ElysiumDontWant_question:

        pt "No es que me de demasiadas opciones..."

        "¿Qué castigo te caerá a ti?" if night05_NeusLastDate_ElysiumDontWant_Cond == "":
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_NeusLastDate_ElysiumDontWant_Cond = "whatAboutNeus"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx07
            $ nteye = "left01"
            call n_closefromup_tears_tears
            with dissolve

            n "Su cuerpo tiembla ligeramente."

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyebrows sadx04
            $ nteye = "left00"
            call n_closefromup_tears_tears
            with dissolve

            ne "No..."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "left02"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "No te preocupes por mí."

            $ ntlong += 1

            show neus_exp_mouth happy_Talkingx04
            show neus_exp_eyebrows sadx06
            $ nteye = "front07"
            call n_closefromup_tears_tears
            with dissolve

            ne "No será la primera vez que recibo su castigo."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx07
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            ne "Eres tú quien realmente me preocupa."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx05
            $ nteye = "left01"
            call n_closefromup_tears_tears
            with dissolve

            ne "No sabes de lo que es capaz de hacer cuando no está contento."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx06
            $ nteye = "left03"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Al menos yo, algún lejano día,"

            show neus_exp_mouth happy_Talkingx03
            show neus_exp_eyebrows sadx05
            $ nteye = "front06"
            call n_closefromup_tears_tears
            with dissolve

            ne "podré volver a ver un amanecer."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            jump night05_NeusLastDate_ElysiumDontWant_question

        "Si no hay otro modo...":
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_NeusLastDate_ElysiumDontWant_Cond = "accept"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "De verdad que no."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx04
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lamento que tengamos que hacerlo en este antro y de este modo."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            pt "Bueno, la habitación tampoco es que sea un cuchitril..."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx06
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Te amo tanto que me duele."

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx05
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero eso soy yo,"

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows angryx02
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "que soy así de estúpida,"

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "así que no te preocupes por ello."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Nunca he querido hacerte daño ni obligarte a hacer nada en contra de tu voluntad."

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows sadx03
            $ nteye = "right01"
            call n_closefromup_tears_tears
            with dissolve

            ne "Sí es verdad que no te quería contar que era tu hermana"

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx02
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "porque sinceramente pensaba que no era algo tan importante,"

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "al menos yo no te considero mi hermano,"

            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows sadx02
            $ nteye = "left03"
            call n_closefromup_tears_tears
            with dissolve

            ne "no del modo en que los humanos suelen entenderlo,"

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows sadx01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            ne "quizás más bien algo parecido a mi alma gemela."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "Aunque si no soy correspondida,"

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "no estoy segura si debería llamarlo de este modo."

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx04
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Hubiera preferido hacerlo cuando tú me amases del mismo modo,"

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            $ nteye = "right02"
            call n_closefromup_tears_tears
            with dissolve

            ne "pero..."

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx04
            $ nteye = "right03"
            call n_closefromup_tears_tears
            with dissolve

            ne "supongo que es demasiado tarde."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "right05"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx03
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "Lamento que no tengas otra opción."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx06
            $ nteye = "front06"
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx07
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            pt "¿Lo está diciendo de corazón o me está intentando manipular?"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx06
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero hay algo que tienes que saber antes de empezar."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "¿El qué?"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

            jump night05_elysium_NeusInfoOrgasm
                # ne "No puedo tener ningún orgasmo."
                # p "¿Cómo?"
                # p "¡¿Por qué?!"
                # ne "Si llegara al clímax,"

        "Prefiero probar suerte con tu Padre.":
            $pl.ch_pts("np",-50)

            $ night05_NeusLastDate_ElysiumDontWant_Cond = "refuse"

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows surprisex03
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx04
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Tan-"

    extend "tanto asco te doy...?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    if gensex_NotLoveSister:

        p "Ya te he dicho que el hecho de que seas mi hermana cambia las cosas."

    else:

        aj "Is this even possible? ERROR 189641"

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows angryx02
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows angryx05
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    n "Una combinación de dolor, frustración, rabia y tristeza se dibuja en su rostro."

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿O acaso me obligarás?"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "No."

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx06
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    ne "No soy mi padre."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx03
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Realmente pensé que podríamos llegar a ser felices."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "No debería habértelo dicho."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex03
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "Preferirías tener el poder de hacerme olvidar,"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows angryx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿verdad?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Yo..."

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx03
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "No te amo porque seas mi hermano,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "te amo por quien y cómo eres."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "Pero no estarías interesado en mí si no tuviera la sangre y el esperma que tengo."

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx04
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Eso no tiene nada que ver."

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows angryx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    pt "No se lo cree ni ella."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx06
    $ nteye = "left05"
    call n_closefromup_tears_tears
    with dissolve

    ne "No es la primera vez que cometo el error de enamorarme de alguien"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx03
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "para luego tener que presenciar o incluso ejecutar su horrible muerte."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx06
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Ejecutar?!"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero sí es la primera vez que tenía la esperanza de poder tener un feliz futuro con esa persona."

    $ ntlong += 1

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyebrows sadx07
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque supongo que eso solo existía en mis sueños."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx06
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx05
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "De acuerdo."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows angryx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Si es lo que quieres..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows angryx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Espera aquí."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg el_bedroom_b:
        truecenter
        zoom 0.5
    with fade

    n "Sin mediar otra palabra se dirige a la puerta entre lágrimas cerrando la puerta justo al salir."

    p "..."

    pt "Después de ver todo lo que hay en este horrible lugar,"

    pt "de ver el estado de Dídac en mi mente,"

    pt "de haberme dicho lo terrible que ese tal \"Padre\"..."

    pt "¿Seguro que he tomado la mejor decisión?"

    call WIP

    ## NOT_FINISHED

    # If he doesn't fuck you or don't love you, she can't die anyway, whenever she dies, gets back with her father, there's no escape.


    jump endupdate