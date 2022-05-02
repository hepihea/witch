

default afternight05_Pedrera_LetsGetOut_COND = False
default afternight05_Pedrera_StillTalkToMe_COND = False

label afternight05_Pedrera_MotherDisappear:

    stop music fadeout 3.0

    scene black
    with fade

    n "Cómo si de arena se tratara,"

    n "se deshace encima del cuerpo desnudo de Meritxell."

    with vpunch

    $ meyesc = ""

    tx "¡COF-COF-COF!"

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "meritxell_theme"

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_bodynew naked_down_dirt

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows suspiciousx01
    with fade

    tx "¡¿Pero qué demonios?!"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 00
    show m_exp_piris down00
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "¡¿Por qué estoy llena de arena?!"

    if MShooter_Present_Necklace_Ankh == False:

        show m_exp_mouth sadbiting_Silentx04
        show m_exp_eyes 02
        show m_exp_piris down02
        show m_exp_eyebrows suspiciousx02
        with dissolve

        pt "¿Vuelve a ser ella misma?"

    show m_exp_mouth sad_Talkingx01
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows serious
    with dissolve

    tx "Euh..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "¿Neus...?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx04
    with dissolve

    tx "¿Te encuentras bien...?"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx05
    with dissolve

    pause 0.2

    scene black # NOT FINISHED, A neus image crying on ther corner?
    with fade

    n "Fuerzas el cuello un poco más para poder verla mejor."

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with fade

    n "Apoyando la espalda en la pared,"

    n "se encuentra sentada en el suelo en un mar de lágrimas."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris front07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Mamá..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_iris front05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "¿Por qué...?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "No debiste hacer eso..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_iris front07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx07
    with dissolve

    tx "Neus..."

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_bodynew naked_down_dirt

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with fade

    tx "[protname],"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "¿Se puede saber qué ha pasado con su padre?"

    if MShooter_Present_Necklace_Ankh:

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows serious
        with dissolve

        p "Nuestra madre se ha sacrificado para salvarnos."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows surprisex01
        with dissolve

        tx "¿¡Vuestra madre?!"

        show m_exp_mouth sad_Silentx01
        show m_exp_eyes 00
        show m_exp_piris front00
        show m_exp_eyebrows surprisex02
        with dissolve

        p "Es el polvo que tienes por encima."

    else:

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve

        p "Eso también me gustaría saber a mi."

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows normal
        with dissolve

        ne "Nuestra madre se ha sacrificado para salvarnos."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 01
        show m_exp_piris left01
        show m_exp_eyebrows surprisex01
        with dissolve

        tx "¡Vuestra madre?!"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx02
        with dissolve

        p "¿De qué estás hablando?"

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows normal
        with dissolve

        ne "Es el polvo que tiene por encima."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 00
    show m_exp_piris down00
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "¡¿Euh?!"

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "didac_theme"

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx06
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    with fade

    d "¡¿Qué cojones está pasando aquí?!"

    show didacf_mouth sad_Talkingx004
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils right02
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "¡Pensaba que todo esto era un sueño!"

    $ deyesp = "_rim" # NOT FINISHED, TEST

    show didacf_mouth sad_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils right01
    show didacf_eyebrows suspiciousx02
    with dissolve

    pt "El que faltaba..."

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows normal
    with dissolve

    ne "[protname]..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx05
    with fade

    p "..."

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx07
    with dissolve

    ne "¿Por qué no me has matado?..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx06
    with dissolve

    if music_play != "wounded":
        play music "audio/music/kevinmacleod/sad/wounded.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "wounded"

    p "..."

label afternight05_Pedrera_WhyNotKillMe:

    menu:

        pt "¿Por qué no la he matado?"

        "Porque no soy un asesino.":
            call p_Help

            $ afternight05_Pedrera_WhyNotKillMe_ImNotAKiller = True

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with dissolve

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx07
            with Dissolve (0.75)

        "Porque a pesar de lo que has hecho, nadie merece la muerte.":
            call p_Help

            $ afternight05_Pedrera_WhyNotKillMe_NoneDeserveDeath = True

            if night05_Interrogation_GrowYouADick_EternalLove_Cond:

                $pl.ch_pts("np",-4)

                show neus_exp_mouth sad_Talkingx02
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "Pensé que habías dicho que me amabas..."

                show neus_exp_mouth sad_Silentx03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                p "Le dije que te sería fiel toda mi eternidad."

                show neus_exp_mouth sad_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows serious
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Silentx01
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows surprisex01
                with dissolve

                p "Y obviamente era una mentira."

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris left05
                show neus_exp_eyebrows sadx05
                with dissolve

            else:

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx02
                with dissolve

                pause 0.2

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris left05
                show neus_exp_eyebrows sadx07
                with Dissolve(0.75)

                $pl.ch_pts("np",-2)


        "Porque me negaba a seguir las órdenes de ese psicópata.":
            call p_Help

            $ afternight05_Pedrera_WhyNotKillMe_FollowOrders = True

            $pl.ch_pts("np",-1)

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with dissolve

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx07
            with Dissolve(0.75)

        "Porque no puedo matar a la persona que amo.":
            call p_Help

            $ afternight05_Pedrera_WhyNotKillMe_WhoILove = True
            $ gensex_ILoveYouNeus = True

            if afternight05_Pedrera_Guarantee_DirtyHeartlessKiller_Cond:

                show neus_exp_mouth sad_Talkingx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Por eso me has dicho que soy una asesina sucia y sin corazón..."

                show neus_exp_mouth sad_Talkingx09
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows angryx04
                with dissolve

                p "¡¿Acaso no ves que estaba intentando seguirle el juego?"

                $pl.ch_pts("np",5)

            elif night05_Interrogation_WhatDoYouFeelAboutMe_WhatIFeel_QuestionsDone_Cond:

                if night05_Interrogation_WhatDoYouFeelAboutMe_WhatIFeel_Yes_Cond:

                    $pl.ch_pts("np",3)

                    show neus_exp_mouth sadbiting_Silentx04
                    $ nteye = 0
                    call neus_exp_tears_tears
                    show neus_exp_iris front00
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx02
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris front02
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "Entonces,"

                    extend " esta noche hablabas en serio,"

                    show neus_exp_mouth sad_Talkingx03
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "cuando me dijiste que empezabas a sentir algo por mi..."

                    if night05_Interrogation_GrowYouADick_EternalLove_Cond:

                        show neus_exp_mouth sadbiting_Silentx02
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris front01
                        show neus_exp_eyebrows surprisex02
                        with dissolve

                        p "¿Acaso no se lo he dejado claro también a Padre?"

                        show neus_exp_mouth sad_Talkingx03
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_iris front05
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "¿De verdad crees que podrías amarme toda la eternidad?"

                        show neus_exp_mouth sad_Silentx02
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris front02
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "¿Tienes dudas?"

                        show neus_exp_mouth sadbiting_Silentx04
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris right04
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx03
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris left04
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "¿No te cansarás de mí?"

                        show neus_exp_mouth sad_Silentx03
                        $ nteye = 3
                        call neus_exp_tears_tears
                        show neus_exp_iris front03
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        p "¿Y tú de mí?"

                        show neus_exp_mouth sadbiting_Silentx03
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_iris down05
                        show neus_exp_eyebrows sadx04
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx03
                        $ nteye = 8
                        call neus_exp_tears_tears
                        show neus_exp_iris front08
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "Ahora sabes que más allá de lo que siento por ti,"

                        show neus_exp_mouth sad_Talkingx05
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx05
                        with dissolve

                        ne "también tengo la necesidad de alimentarme de tu esperma para sobrevivir."

                        show neus_exp_mouth sad_Silentx02
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris front01
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "¿Eso significa que no?"

                        show neus_exp_mouth sad_Talkingx03
                        $ nteye = 8
                        call neus_exp_tears_tears
                        show neus_exp_iris front08
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        ne "Eso significa,"

                        show neus_exp_mouth happy_Talkingx05
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "que me alegra saber que no eres como Padre."

                        show neus_exp_mouth happy_Silentx02
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_iris front05
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Silentx03
                        $ nteye = 6
                        call neus_exp_tears_tears
                        show neus_exp_iris front06
                        show neus_exp_eyebrows sadx02
                        with dissolve

                    else:

                        jump afternight05_Pedrera_WhyNotKillMe_Doubts

                elif night05_Interrogation_GrowYouADick_EternalLove_Cond:

                    show neus_exp_mouth sad_Talkingx03
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "¿Lo decías en serio cuando has dicho que me amabas?"

                    jump afternight05_Pedrera_WhyNotKillMe_Doubts

            elif night05_Interrogation_GrowYouADick_EternalLove_Cond:

                show neus_exp_mouth sad_Talkingx03
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "¿Lo decías en serio cuando has dicho que me amas?"

                show neus_exp_mouth sad_Silentx02
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx01
                with dissolve

                p "¿Te crees que estaba la cosa para hacer bromas sobre el tema?"

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "..."

                jump afternight05_Pedrera_WhyNotKillMe_Doubts

                # You said here you loved here, but you didn't ask or talked about that in the interrogation part.

        # NOT FINISHED # No hay otras cosas que le hayas llamado?

    ne "..."

    jump afternight05_Pedrera_WhyNotKillMe_After


label afternight05_Pedrera_WhyNotKillMe_Doubts:

    show neus_exp_mouth sad_Silentx05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx04
    with dissolve

    p "¿Acaso lo dudas?"

    if afternight05_Pedrera_OtherOption_NeusAppear_Assasin or afternight05_Pedrera_Vegan_TellMeIsALie:

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows serious
        with dissolve

        ne "Hombre,"

    if afternight05_Pedrera_OtherOption_NeusAppear_Assasin:

        show neus_exp_mouth sad_Talkingx05
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris front03
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "después de llamarme \"asesina de las narices\","

        show neus_exp_mouth sad_Talkingx004
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows angryx02
        with dissolve

        ne "pues un poco,"

        extend " sinceramente."

        show neus_exp_mouth sad_Silentx06
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris front05
        show neus_exp_eyebrows angryx01
        with dissolve

        p "¿Qué querías que le dijera?"

        show neus_exp_mouth sad_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows serious
        with dissolve

        p "¿La verdad?"

        show neus_exp_mouth sadbiting_Silentx03
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx01
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "No..."

        show neus_exp_mouth sad_Talkingx002
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris left05
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Supongo que no."

        show neus_exp_mouth sadbiting_Silentx06
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx06
        with dissolve

    elif afternight05_Pedrera_Vegan_TellMeIsALie:

        show neus_exp_mouth sad_Talkingx07
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "después de decirme que me importan más las personas,"

        extend " que los animales..."

        show neus_exp_mouth sad_Silentx06
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris front05
        show neus_exp_eyebrows angryx01
        with dissolve

        menu:

            "¿Acaso no es verdad?":
                call p_Help

                $pl.ch_pts("np",-2)

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx08
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx02
                with dissolve

                ne "Por supuesto que no."

                show neus_exp_mouth sad_Silentx06
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows angryx01
                with dissolve

                p "..."

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Yo,"

                extend " sólo..."

                show neus_exp_mouth sad_Talkingx05
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "No quiero que haya más muertes."

                show neus_exp_mouth sad_Talkingx06
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows sadx04
                with dissolve

                p "Ya..."

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 6
                call neus_exp_tears_tears
                show neus_exp_iris front06
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "..."

            "Tenía que interpretar un papel con tu padre, no lo ves?":
                call p_Help

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with dissolve

                ne "..."

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows suspiciousx01
                with dissolve

                ne "Hmm..."

                show neus_exp_mouth sad_Talkingx002
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows suspiciousx02
                with dissolve

                ne "Supongo;"

                show neus_exp_mouth sad_Talkingx02
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "aún así dolió escucharlo de tu voz."

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx03
                with dissolve

                p "..."

                menu:

                    "Lo siento. No era mi intención hacerte daño.":
                        call p_Help

                        $pl.ch_pts("np",2)

                        show neus_exp_mouth sadbiting_Silentx01
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris front02
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        ne "..."

                        show neus_exp_mouth happy_Talkingx04
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        ne "Esas palabras ya suenan mejor."

                        show neus_exp_mouth happy_Silentx03
                        $ nteye = 6
                        call neus_exp_tears_tears
                        show neus_exp_iris front06
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "..."

                    "...":
                        call p_Help

            "Lo lamento.":
                call p_Help

                $pl.ch_pts("np",-1)

                show neus_exp_mouth sad_Talkingx05
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx01
                with dissolve

                ne "Pero no soy así realmente."

                show neus_exp_mouth sad_Talkingx06
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "No prefiero a las personas que a los animales."

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "Simplemente no deseo más muertes..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx03
                with dissolve

                menu:

                    "¿Tanto te costaba pedírmelo sin tener que matar a un niño?":
                        call p_Help

                        $pl.ch_pts("np",-2)

                        show neus_exp_mouth sadbiting_Silentx02
                        $ nteye = 0
                        call neus_exp_tears_tears
                        show neus_exp_iris front00
                        show neus_exp_eyebrows surprisex02
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx08
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx05
                        with dissolve

                        ne "¿Te crees que me fue fácil?"

                        show neus_exp_mouth sad_Talkingx09
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris front02
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "¿Te crees que lo hice porque quise?"

                        show neus_exp_mouth sad_Silentx01
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris front01
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "Nadie te obligó a sacrificar a a ese niño."

                        show neus_exp_mouth sad_Silentx04
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_iris front05
                        show neus_exp_eyebrows angryx01
                        with dissolve

                        ne "..."

                        show neus_exp_mouth sad_Talkingx05
                        $ nteye = 5
                        call neus_exp_tears_tears
                        show neus_exp_iris front05
                        show neus_exp_eyebrows angryx02
                        with dissolve

                        ne "Tu indiferencia es lo que me empujó a hacerlo."

                        show neus_exp_mouth sad_Silentx02
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris front01
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        p "¡¿Cómo iba a saber que estabas interesada en mí,"

                        show neus_exp_mouth sadbiting_Silentx04
                        $ nteye = 0
                        call neus_exp_tears_tears
                        show neus_exp_iris front00
                        show neus_exp_eyebrows surprisex02
                        with dissolve

                        p "si ni siquiera me lo mencionaste en ningún momento?!"

                        show neus_exp_mouth sadbiting_Silentx02
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris right01
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        tx "No había que ser muy listo para notar las miraditas,"

                        $ Pedrera_char_Cond =  "TxellClose_b"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx02
                        with fade

                        tx "y las indirectas que te lanzaba constantemente."

                        show m_exp_mouth sad_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows angryx03
                        with dissolve

                        tx "¡Por el amor de Dios!"

                        show m_exp_mouth sad_Talkingx11
                        show m_exp_eyes 01
                        show m_exp_piris front01
                        show m_exp_eyebrows angryx04
                        with dissolve

                        tx "¡Si no te sacaba los ojos de encima!"

                        show m_exp_mouth sad_Silentx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx03
                        with dissolve

                        p "..."

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 01
                        show m_exp_piris right01
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        d "¿La morena está enamorada de ti?"

                        $ Pedrera_char_Cond =  "TxellDidac"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Silentx04
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        show m_exp_eyebrows serious

                        show didacf_mouth sad_Talkingx003
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows normal
                        with fade

                        d "¿Y dices que mató a un niño?"

                        show m_exp_mouth sad_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris right05
                        show m_exp_eyebrows angryx01

                        show didacf_mouth sad_Talkingx04
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows suspiciousx01
                        with dissolve

                        d "¿Es alguna clase de postura sexual que desconozco?"

                        show m_exp_mouth sad_Talkingx004
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows angryx02

                        show didacf_mouth sad_Silentx03
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils left02
                        show didacf_eyebrows surprisex01
                        with dissolve

                        tx "Dídac..."

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        show m_exp_eyebrows angryx02

                        show didacf_mouth sad_Silentx02
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils left03
                        show didacf_eyebrows suspiciousx01
                        with dissolve

                        tx "Cállate un rato."

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris right05
                        show m_exp_eyebrows surprisex001

                        show didacf_mouth happy_Talkingx05
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils left04
                        show didacf_eyebrows suspiciousx02
                        with dissolve

                        d "Te gustaría amordazarme,"

                        extend " ¿verdad?"

                        $ Pedrera_char_Cond =  "DidacClose"
                        call Pedrera_char_lab

                        show didacf_mouth sad_Silentx03
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows surprisex02
                        with hpunch

                        p "¡Dídac!"

                        show didacf_mouth sad_Talkingx003
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils front05
                        show didacf_eyebrows suspiciousx01
                        with dissolve

                        d "Vale,"

                        extend " vale..."

                        show didacf_mouth sad_Talkingx06
                        $ dteye = 8
                        call didac_exp_tears_tears
                        show didacf_pupils front08
                        show didacf_eyebrows sadx01
                        with dissolve

                        d "No digo nada más..."

                    "...":
                        call p_Help


            "Te quiero, a pesar de ello.":
                call p_Help

                if night05_Interrogation_GrowYouADick_EternalLove_Cond:

                    $pl.ch_pts("np",3)

                else:

                    $pl.ch_pts("np",1)

                ne "..."

    else:

        # NOT FINISHED not add anything here?

        ne "..."

    jump afternight05_Pedrera_WhyNotKillMe_After

label afternight05_Pedrera_WhyNotKillMe_After:

    #tx "¿Se puede saber de qué estáis hablando?"

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx004
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils right02
    show didacf_eyebrows surprisex01
    with fade

    d "Realmente parece un sueño..."

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows surprisex02
    with dissolve

    pause 0.2

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "didac_theme"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious

    show didacf_mouth sad_Talkingx05
    show didacf_pupils front02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_eyebrows suspiciousx01
    with fade

    d "¿Estas dos no están en nuestra clase de arte?"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show didacf_mouth happy_Talkingx05
    show didacf_pupils left05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_eyebrows surprisex01
    with dissolve

    d "A esta es difícil olvidarla..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth sad_Silentx01
    show didacf_pupils left05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "Ni siquiera siendo mujer cambias lo más mínimo."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex01

    show didacf_mouth happy_Talkingx06
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows surprisex01
    with dissolve

    d "Pero si a ti te gustan con melones..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth happy_Talkingx07
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx02
    with dissolve

    d "¿Qué excusa tienes ahora preciosa?"

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01

    show didacf_mouth sad_Silentx03
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows normal
    with dissolve

    tx "Dios..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious

    show didacf_mouth happybiting_Silentx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Silentx03
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows normal

    if DidacPregnant:

        if afternight04_Park_HelpDidacPolice_Cond: #Después de quedarse preñado, ayudas a Dídac a salir de ahí, 
                    #sin que este se lo tome demasiado bien el hecho de que hubieras estado observándole sin haber hecho nada.

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            show didacf_mouth sad_Silentx03
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex02
            with dissolve

            p "Serás todo lo cachondo que quieras Dídac,"

            show didacf_mouth sad_Silentx04
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows serious
            with dissolve

            p "pero nunca más volverás a tener rabo."

            show didacf_mouth sad_Silentx06
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils right05
            show didacf_eyebrows angryx03
            with dissolve

            d "..."

            #tx "¿De qué estás hablando?..." Both know that, isn't it?

            show didacf_mouth sad_Talkingx09
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            with dissolve

            d "¡¿Y de quién es la culpa?!"

            show didacf_mouth sadbiting_Silentx02
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils front00
            show didacf_eyebrows surprisex01
            with dissolve

            p "¡¿De quien va a ser?!"

            show didacf_mouth sad_Talkingx08
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows angryx03
            with dissolve

            d "¡Sabías que ese yonqui de mierda no llevaba condón,"

            show didacf_mouth sad_Talkingx09
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            with dissolve

            d "y aún así dejaste que se me corriera dentro!"

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex01
            with dissolve

            p "¡Como si te hubiera obligado a follar con ellos!"

            show didacf_mouth sadbiting_Silentx05
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows angryx01
            with dissolve

            p "¡La madre que te parió!"

            show didacf_mouth sad_Silentx06
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils front05
            show didacf_eyebrows serious
            with dissolve

            p "¡Fuiste tú el que se fue del piso insultándome!"

            show didacf_mouth sad_Silentx05
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils right05
            show didacf_eyebrows sadx01
            with dissolve

            d "..."

            jump afternight05_Pedrera_OkupDoneNothing

        else:

            if afternight04_Park_AbandonDidacPolice_Cond:

                menu:

                    pt "¿Debería admitir que le estuve espiando y que no hice nada para detener a ese yonqui?"

                    "<Admitir que lo sabías y dejaste que le atrapara la policía>":

                        call p_Help

                        $pl.ch_pts("np",-6)
                        $pl.ch_pts("dp",-12)
                        $pl.ch_pts("mp",-4)

                        show didacf_mouth sad_Silentx04
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows surprisex01
                        with dissolve

                        p "Espero que valiera la pena el polvo que te metió ese yonqui de mierda,"

                        show didacf_mouth sad_Silentx03
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows normal
                        with dissolve

                        p "porque por su culpa nunca más volverás a ser un hombre."

                        show didacf_mouth sad_Silentx02
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows surprisex02
                        with dissolve

                        d "..."

                        $ Pedrera_char_Cond = "TxellClose_b"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with fade

                        tx "¿Ese yonqui?"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "¿De quien...?"

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows normal
                        with dissolve

                        d "¿Cómo sabes lo del...?"

                        $ Pedrera_char_Cond = "TxellDidac"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 00
                        show m_exp_piris front00
                        show m_exp_eyebrows surprisex002

                        show didacf_mouth sadbiting_Silentx02
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows surprisex02
                        with fade

                        p "Pues porque te seguí."

                        show m_exp_mouth sad_Silentx01
                        show m_exp_eyes 01
                        show m_exp_piris front01
                        show m_exp_eyebrows surprisex01

                        show didacf_mouth sadbiting_Silentx01
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows surprisex02
                        with dissolve

                        d "..."

                        show m_exp_mouth sad_Talkingx02
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows sadx01

                        show didacf_mouth sadbiting_Silentx01
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows surprisex01
                        with dissolve

                        tx "¿Lo seguiste?"

                        $ dtlong = 1

                        show m_exp_mouth sadbiting_Silentx04
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows sadx02

                        show didacf_mouth sad_Talkingx02
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows serious
                        with dissolve

                        d "¿Co-"

                        extend "como que me seguiste?"

                        show m_exp_mouth sadbiting_Silentx05
                        show m_exp_eyes 03
                        show m_exp_piris right03
                        show m_exp_eyebrows sadx03

                        show didacf_mouth sad_Silentx03
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows serious
                        with dissolve

                        p "Pues lo que oyes."

                        $ Pedrera_char_Cond = "DidacClose"
                        call Pedrera_char_lab

                        show didacf_mouth sad_Silentx01
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows surprisex02
                        with fade

                        p "Te estuve espiando escondido tras un arbusto en el parque."

                        show didacf_mouth sad_Silentx04
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows suspiciousx02
                        with dissolve

                        d "..."

                        show didacf_mouth sad_Talkingx04
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils front04
                        show didacf_eyebrows angryx01
                        with dissolve

                        d "¡¿Y dejaste que me llevaran preso?!"

                        $ dtlong = 2

                        show didacf_mouth sad_Talkingx07
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡HE PASADO LA NOCHE EN LA PUTA COMISARÍA!"

                        show didacf_mouth sad_Talkingx08
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡SIN MENCIONAR QUE VISTE COMO ESE PUTO YONQUI"

                        show didacf_mouth sad_Talkingx09
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "ME ESTABA FOLLANDO SIN EL PUTO CONDÓN!"

                        show didacf_mouth sad_Silentx02
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows angryx01
                        with dissolve

                        p "¿Y de quién es la culpa de que eso sucediera?"

                        show didacf_mouth sad_Silentx03
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows serious
                        with dissolve

                        d "..."

                        show didacf_mouth sad_Silentx02
                        $ dteye = 1
                        call didac_exp_tears_tears
                        show didacf_pupils front01
                        show didacf_eyebrows suspiciousx01
                        with dissolve

                        p "¿Quién te dijo por activa y por pasiva que no salieras del piso,"

                        show didacf_mouth sad_Silentx01
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows angryx01
                        with dissolve

                        p "que no hicieras el gilipollas."

                        show didacf_mouth sad_Silentx01
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows serious
                        with dissolve

                        d "..."

                        show didacf_mouth sad_Talkingx03
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows serious
                        with dissolve

                        tx "¿Por qué no interviniste cuando viste que se podía correr dentro?"

                        show didacf_mouth sad_Silentx01
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows serious
                        with dissolve

                        p "Porque ya eres mayorcito para tomar sus propias decisiones."

                        show didacf_mouth sadbiting_Silentx02
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils front05
                        show didacf_eyebrows angryx01
                        with dissolve

                        p "¿O no es lo que me dijiste?"

                        show didacf_mouth sadbiting_Silentx05
                        $ dteye = 6
                        call didac_exp_tears_tears
                        show didacf_pupils front06
                        show didacf_eyebrows sadx04
                        with dissolve

                        d "..."

                        show didacf_mouth sadbiting_Silentx06
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils right05
                        show didacf_eyebrows sadx03
                        with dissolve

                        tx "¡¿Qué clase de mierda de amigo eres?!"

                        $ Pedrera_char_Cond = "TxellClose_b"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Silentx06
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx03
                        with fade

                        p "De los que..."

                        $ dtlong = 3

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 01
                        show m_exp_piris right01
                        show m_exp_eyebrows sadx01
                        with fade

                        d "¿Por qué coño me seguiste?..."

                        $ Pedrera_char_Cond = "DidacClose"
                        call Pedrera_char_lab

                        show didacf_mouth sad_Silentx02
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows serious
                        with fade

                        p "..."

                        show didacf_mouth sad_Talkingx09
                        $ dteye = 0
                        call didac_exp_tears_tears
                        show didacf_pupils front00
                        show didacf_eyebrows angryx04
                        with fade

                        d "¡¿PARA QUÉ COÑO ME SEGUISTE SI LUEGO NO HICISTE NADA?!"

                        show didacf_mouth sad_Silentx09
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils front05
                        show didacf_eyebrows angryx04
                        with dissolve

                        menu:

                            "Por curiosidad.":

                                call p_Help

                                d "..."

                                tx "¿Qué clase de respuesta ese esta?"

                                ne "¿Para qué acudiste a las tres citas entonces?"

                                p "..."

                                p "No negaré que al principio lo hice para ayudarle,"

                                p "pero no soy su niñera,"

                                extend " él es dueño de sus propias decisiones,"

                                p "y si estas le han llevado a esto,"

                                extend " entonces él es el único responsable."

                                p "Además, no he acudido a las tres citas únicamente para ayudarle."

                                p "También quería disfrutar de tu compañía."

                                # NOT FINISHED

                                jump endupdate

                            "Para que no te mataran.":

                                call p_Help

                                # NOT FINISHED

                                jump endupdate


                    "<No admitirlo>":

                        call p_Help

                        pass

            show didacf_mouth sad_Silentx01
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex02
            with dissolve

            p "¡Maldita seas Dídac!"
        
            if DidacMCPregnant:

                jump afternight05_Pedrera_AfM_DidacPregnantMc

            else: # You don't know who is the father. (Okupa is the only one?)

                # if DidacOKUPregnant: If is the only one... makes no sense.
                # elif afternight04_Park_HelpDidacPolice_Cond: # Después de quedarse preñado, lo ayudas a salir de ahí.
                # DidacOKUPregnant_YouKnowIt == False: # YOU DON'T WAITED FOR HER TO GET PREGNANT WATCHING HER.

                show didacf_mouth sad_Silentx01
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils front02
                show didacf_eyebrows surprisex01
                with dissolve

                p "¡¿Qué coño hiciste ayer por la noche?!"

                # NOT FINISHED, what about if you don't find her in the flat.

                if afternight04_DidacisNOTatHome: # She is not at home at night.

                    if aftermorning04_calmdidac_Failed:

                        show didacf_mouth sad_Talkingx08
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils front04
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡¿Te refieres a lo que hice después de que me dejaras tirado en esa celda,"

                        d "después del incidente en el gran almacén?!"

                    #elif morning04_Shopping_NotTogether

                    elif morning04_Shopping_Alone_Cond or morning04_Shopping_Alone_Angry_Cond:

                        d "¡¿Te refieres a lo que ocurrió después de que me dejaras tirado yendo solo de tiendas?!"

                    else:

                        d "¡¿Te refieres cuando no te vi en todo el jodido día?!"


                    # NOT FINISHED

                    jump endudpate

                elif afternight04_sexbattle_started == False:

                    d "¡¿Te refieres a qué hice cuando te negaste ayudarme ayer por la noche?!"

                    p "¡A follar!"

                    extend " ¡Me negué a follarte!"

                    d "¡Llámalo como quieras!"

                    p "¡Joder!"

                    extend " ¡Hay una jodida diferencia!"

                #elif # she's not at the Morning (probably, DIdac didn't have too many orgasms)

                    # NOT FINISHED

                else:

                    d "¡¿Te refieres a qué hice después de que te negaras a ayudarme?!"

                d "¡Pues hice lo que te prometí que haría!"

                d "¡Por tu culpa un puto yonqui de mierda me dejó preñada!"

                menu:

                    "<Usar el sarcasmo para tirarle en cara lo irresponsable que ha sido.":
                        call p_Help

                        $pl.ch_pts("np", -1)
                        $pl.ch_pts("dp", -2)
                        $pl.ch_pts("mp", 1)

                        p "¡Ah!"

                        extend " ¡Lo siento!"

                        p "¡Siento que tu puta ninfomanía te empujara a follarte al primero que pillaras!"

                        d "¡Imbécil!"

                        d "¡No tienes ni la más puta jodida idea de lo que estoy pasando!"

                        p "Sí,"

                        extend " que sufres un calentón de mil narices;"

                        p "pero por lo menos pensaba que tendrías un poco más de cabeza."

                        p "¡¿Pero qué va a saber un tío que se va follando a la primera que se pilla sin condón?!"

                        p "pues mira,"

                        extend " ahora has experimentado la otra cara de la moneda."

                        p "Por imbécil,"

                        extend " te lo mereces."

                        d "¡SERÁS CAPULLO!"

                    "¡¿Y qué se supone que tenía que hacer?!":
                        call p_Help

                        # NOT FINISHED

                    "Lo siento Dídac.":
                        call p_Help

                        # NOT FINISHED

                tx "No negaré que un tipo como Dídac se merezca un escarmiento."

                tx "Pero parte de lo que dice es verdad."

                tx "Lo que se siente con esta transformación,"

                tx "haría enloquecer al más casto de los budistas del Tíbet."

                d "¿Có-"

                extend "cómo lo sa...?"

                p "No intentes excusarlo."

                p "¡¿Qué diablos te pasaba por la cabeza para hacer semejante estupidez?!"

                jump afternight05_Pedrera_AfM_DidacPregnantExplanation

                    # d "¡Joder!"
                    # d "¡Ya sé que va a sonar raro!"
                    # d "pero..."
                    # tx "Sueñas con su polla a cada instante que cierras los ojos."
                    # d "..."
                    # d "¿Te pasa lo mismo?"
        ##

        p "¡¿Por qué coño lo hiciste Dídac?!"

        jump afternight05_Pedrera_AfM_DidacPregnantExplanation

            # d "¡Joder!"
            # d "¡Ya sé que va a sonar raro!"
            # d "pero..."
            # tx "Sueñas con su polla a cada instante que cierras los ojos."


    else: # "Didac not pregnant"

        tx "Al menos no te has quedado preñada."

        d "¿Tanto echas de menos mi cuerpo masculino?"

        tx "Mas bien tengo ganas de que dejes de ser mujer."

        tx "Me da cosa verte así..."

        p "Por eso no dejas de fijarte en sus pechos."

        tx "..."

        p "Creo que más bien tienes miedo de sentir demasiada atracción por un cuerpo,"

        p "del que detestas su personalidad."

        tx "Hmpph..." # Showing rebellious disaprove.

        d "Bah..."

        d "Estoy seguro que con mi polla,"

        d "disfrutarías mucho más que haciendo eso que hacéis vosotras,"

        extend " con las tijeritas..."

        tx "Y ahí tienes la razón por la que ni siquiera el mejor físico,"

        tx "sería capaz de convencerme de acostarme con este idiota."

        jump afternight05_Pedrera_NeusSorrow

            # ne "Soy tan estúpida..."
            # tx "Neus..."
            # tx "No eres estúpida."


label afternight05_Pedrera_OkupDoneNothing:

    $ Pedrera_char_Cond =  "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with fade

    tx "¡¿Pudiste evitarlo y no hiciste nada?!"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "Hice todo lo que pude para que no se largara del piso."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Si no me hizo ni puto caso,"

    extend " es su problema."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    d "¡Me hubiera gustado verte en mi lugar!"

    $ Pedrera_char_Cond =  "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    with fade

    p "Desde luego,"

    show didacf_mouth sad_Silentx06
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    with dissolve

    p "no me hubiera puesto a follar con tres yonquis completamente borrachos,"

    show didacf_mouth sad_Silentx08
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    with dissolve

    p "en medio de un parque en plena noche."

    show didacf_mouth sad_Silentx07
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    with dissolve

    p "Eso te lo garantizo."

    show didacf_mouth sad_Silentx06
    $ dteye = 6
    call didac_exp_tears_tears
    show didacf_pupils front06
    show didacf_eyebrows sadx01
    with dissolve

    d "..."

    show didacf_mouth sad_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    with dissolve

    tx "¿Por qué no lo detuviste?"

    # $ Pedrera_char_Cond =  "TxellClose_b"
    # call Pedrera_char_lab

    show didacf_mouth sad_Silentx03
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows serious
    with fade

    p "Por que según sus palabras;"

    show didacf_mouth sad_Silentx04
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    with dissolve

    p "{i}Ya soy suficientemente mayorcito para tomar mis decisiones.{/i}"

    show didacf_mouth sad_Silentx05
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils right03
    show didacf_eyebrows sadx01
    with dissolve

    p "¿No es así?"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02

    show didacf_mouth sad_Silentx07
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils right04
    show didacf_eyebrows angryx04
    with fade

    d "Tssk..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    with dissolve

    tx "¿Acaso no entiendes que nunca podrá volver a ser el de antes?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01

    show didacf_mouth sad_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows angryx04
    with dissolve

    p "Era plenamente consciente de ello."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 6
    call didac_exp_tears_tears
    show didacf_pupils front06
    show didacf_eyebrows angryx01
    with dissolve

    p "¿No es así?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03

    show didacf_mouth sadbiting_Silentx06
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows sadx02
    with dissolve

    tx "¡No estoy hablando con él!"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows sadx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond =  "TxellClose_b"
    call Pedrera_char_lab

    show didacf_mouth sad_Silentx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    with fade

    p "..."

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    with dissolve

    p "Sí,"

    extend " era consciente de ello."

    show didacf_mouth sad_Talkingx08
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "¡¿Y por qué diablos no hiciste nada?!"

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    with dissolve

    p "Fue ella quien lo convirtió en mujer."

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows sadx01
    with dissolve

    tx "..."

    show didacf_mouth sad_Talkingx004
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    with dissolve

    tx "Lo que ha hecho Neus es horrible,"

    extend " eso no tiene discusión."

    show didacf_mouth sad_Talkingx06
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    with dissolve

    tx "Pero lo que has hecho tú,"

    extend " es simplemente monstruoso."

    show didacf_mouth sad_Talkingx07
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows normal
    with dissolve

    tx "Por lo menos con Neus tenía la oportunidad de volver a ser el que era."

    show didacf_mouth sad_Talkingx08
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    with dissolve

    tx "Por tu culpa ya no lo volverá a ser nunca más."

    show didacf_mouth sad_Silentx04
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows serious
    with dissolve

    p "¿Por mi culpa?!"

    show didacf_mouth sad_Silentx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    with dissolve

    p "¿¡Acaso no me has escuchando cuando he dicho que fue él quien se largó del piso insultándome?!"

    show didacf_mouth sad_Talkingx005
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "Pero podrías haberlo convencido..."

    show didacf_mouth sad_Silentx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx02
    with dissolve

    p "¡¿Cómo?!"

    show didacf_mouth sad_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    with dissolve

    p "¡¿Follando con él?!"

    show didacf_mouth sad_Talkingx004
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows suspiciousx02
    with dissolve

    tx "No necesariamente..."

    show didacf_mouth sad_Talkingx04
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx02
    with dissolve

    tx "pero por lo menos convencerlo de otro modo,"

    show didacf_mouth sad_Talkingx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    with dissolve

    tx "para impedir que fuera por la calle del modo en el que estaba."

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows serious
    with dissolve

    p "..."

    show didacf_mouth sad_Talkingx005
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows surprisex01
    with dissolve

    tx "y de no poder evitarlo,"

    extend " al menos intentar ayudarlo cuando vieras que iba a hacer algo de lo que luego se lamentaría."

    show didacf_mouth sad_Silentx03
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils right03
    show didacf_eyebrows serious
    with dissolve

    d "¿Y cómo sabes tú sobre todo esto?"

    jump afternight05_Pedrera_AfM_TxellExplaining


label afternight05_Pedrera_AfM_DidacPregnantMc:

    show didacf_mouth sad_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    with dissolve

    p "¡¿Qué demonios hiciste ayer por la noche con el último condón que me diste?!"

    show didacf_mouth sad_Talkingx02
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils right03
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "¿Euh...?"

    show didacf_mouth happy_Talkingx02
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils down04
    show didacf_eyebrows sadx01
    with dissolve

    d "Ahh..."

    show didacf_mouth happy_Talkingx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils right04
    show didacf_eyebrows sadx02
    with dissolve

    d "¿A qué te...?"

    show didacf_mouth sadbiting_Silentx06
    $ dteye = 7
    call didac_exp_tears_tears
    show didacf_pupils front07
    show didacf_eyebrows angryx03
    with vpunch

    p "¡NO TE HAGAS EL IMBÉCIL!"

    show didacf_mouth sad_Silentx03
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows sadx02
    with dissolve

    p "¡¿Te das cuenta que ahora ya no podrás volver a ser hombre nunca más?!"

    show didacf_mouth sad_Talkingx02
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows sadx01
    with dissolve

    d "Euh..."

    show didacf_mouth sad_Talkingx04
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    with dissolve

    d "Ya..."

    show didacf_mouth sad_Talkingx06
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    with dissolve

    d "Ya lo sé..."

    show didacf_mouth sad_Silentx02
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows normal
    with dissolve

    p "¡¿Es que te han lavado el cerebro?!"

    show didacf_mouth sad_Talkingx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    with dissolve

    d "No..."

    show didacf_mouth sad_Talkingx002
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils right02
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "No lo creo..."

    show didacf_mouth sad_Talkingx004
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils right01
    show didacf_eyebrows surprisex01
    with dissolve

    d "Me sigo sintiendo el mismo de siempre."

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    with dissolve

    p "¡Y un cuerno!"

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows serious
    with dissolve

    p "¡El Dídac que yo conozco,"

    extend " nunca hubiera deseado ser mujer!"

    show didacf_mouth sad_Silentx02
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "Me pregunto por qué será..."

    show didacf_mouth sad_Silentx04
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    with dissolve

    d "..."

    show didacf_mouth sad_Talkingx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    with dissolve

    d "¡Mira!"

    show didacf_mouth sad_Talkingx07
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows sadx01
    with dissolve

    d "¡Francamente,"

    extend " no sé cómo explicártelo!"

    show didacf_mouth sad_Talkingx05
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    with dissolve

    d "Pero en pocas palabras,"

    show didacf_mouth happy_Talkingx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows sadx02
    with dissolve

    d "te puedo asegurar que nunca había sentido tanto placer en mi vida,"

    show didacf_mouth happy_Talkingx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils down04
    show didacf_eyebrows sadx01
    with dissolve

    d "como lo que sentí ayer con tu polla."

    show didacf_mouth sad_Talkingx07
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    with dissolve

    d "¡Corté la punta del último condón antes de ponértelo!"

    show didacf_mouth sad_Talkingx08
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    with dissolve

    d "¡Sí!"

    show didacf_mouth sad_Talkingx06
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    with dissolve

    d "¡Fui yo!"

    show didacf_mouth sad_Talkingx07
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows serious
    with dissolve

    d "¡Y no me arrepiento de ello!"

    show didacf_mouth sadbiting_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows sadx01
    with dissolve

    p "Pero..."

label afternight05_Pedrera_AfM_DidacPregnantExplanation:

    show didacf_mouth sad_Talkingx08
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    with dissolve

    d "¡Joder!"

    show didacf_mouth sad_Talkingx06
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils right01
    show didacf_eyebrows angryx02
    with dissolve

    d "¡Ya sé que va a sonar raro!"

    show didacf_mouth sad_Talkingx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils right04
    show didacf_eyebrows sadx01
    with dissolve

    d "pero..."

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows serious
    with dissolve

    tx "Sueñas con su polla a cada instante que cierras los ojos."

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with fade

    d "..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth sad_Talkingx004
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with dissolve

    d "¿Te pasa lo mismo?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001

    show didacf_mouth sad_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with dissolve

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    if afternoon04_MACBA_TxellTruth_Cond:

        if FuckM_Start_Cond:

            # FOR FUTURE

            tx "Bueno..."

            tx "No lo describiría así,"

            tx "pues a mi me ha convencido más con sus palabras,"

            tx "que con sus atributos,"

        else:

            show m_exp_mouth sad_Talkingx002
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with fade

            tx "No exactamente,"

        show m_exp_mouth sad_Talkingx002
        show m_exp_eyes 05
        show m_exp_piris down05
        show m_exp_eyebrows normal
        with dissolve

        tx "aunque el chico se defiende bien ahí debajo,"

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        tx "eso no se puede negar..."

        show m_exp_mouth sad_Talkingx02
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows normal
        with dissolve

        tx "Pero no."

    else:

        show m_exp_mouth sad_Talkingx001
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows normal
        with dissolve

        tx "No."

label afternight05_Pedrera_AfM_TxellExplaining:

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    tx "Leí que alguien padeció tu misma transformación en un libro."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show didacf_mouth sad_Talkingx08
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with fade

    d "¿Mi transformación?"

    show m_exp_mouth sad_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show didacf_mouth sad_Talkingx07
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx02
    with dissolve

    d "¡¿En un libro?!"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show didacf_mouth sad_Talkingx09
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils left00
    show didacf_eyebrows surprisex01
    with dissolve

    d "¿Acaso sabes...?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    with dissolve

    tx "Lo sé todo,"

    extend " no te preocupes."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal

    show didacf_mouth sadbiting_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows normal
    with dissolve

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    if afternoon04_MACBA_TxellTruth_Cond:

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows normal
        with fade

        p "¿En el libro explica uno de estos casos?"

        show m_exp_mouth sad_Talkingx01
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        tx "Sí."

    else:

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows normal
        with fade

        p "¿Todo...?"

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        tx "..."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01
        with dissolve

        tx "Era algo que me hubiera podido contarte," # NOT FINISHED, NECESITA REVISIÓN.

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve

        tx "pero por desgracia no estuviste a la altura."

##

label afternight05_Pedrera_AfM_MeritxellAcussation: # NOT FINISHED where this part go?!

    if DidacSex_Vaginal:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Puedo llegar entender por qué lo hizo él."

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx02
        with dissolve

        tx "Pero tú,"

        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx02
        with dissolve

        tx "¿Qué excusa tienes?"

        if (FuckM_Start_Cond and FuckH_Start_Cond) == False:

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx03
            with dissolve

            tx "¡¿No se supone que estabas con Neus?!"

        show m_exp_mouth sad_Talkingx09
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx04
        with dissolve

        tx "¿Te parece que follártelo con condón es una excusa?!"

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

        p "..."

label afternight05_Pedrera_NeusSorrow:

    stop music fadeout 3.0

    if music_play != "heartbreaking":
        play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "heartbreaking"

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex01
    with dissolve

    ne "Soy tan estúpida..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Neus..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx03
    with dissolve

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with fade

    tx "No eres estúpida."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx05
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Me dejó escapar..."

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Creía que durante estos últimos veinte años me había ganado su confianza,"

    show neus_exp_mouth sad_Talkingx07
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "que si me dejaba más libertad,"

    show neus_exp_mouth sad_Talkingx09
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "es porque le había convencido de mi lealtad y amor hacia él..."

    show neus_exp_mouth sad_Talkingx08
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Todo lo que he sacrificado para conseguir que creyera en mi,"
    show neus_exp_mouth sad_Talkingx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "todo lo que he tenido que hacer con él,"

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "todos a los que he perdido,"

    show neus_exp_mouth sad_Talkingx05
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx07
    with dissolve

    ne "todos a los que he sacrificado..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx07
    with dissolve

    tx "..."

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Recuperar a Madre ha sido siempre su verdadero objetivo."

    show neus_exp_mouth sad_Talkingx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris down05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Solo he sido una herramienta para encontrarla..."

    show neus_exp_mouth sad_Talkingx08
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Sabía que tarde o temprano acabaría escapándome,"

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "y entonces..."

    show neus_exp_mouth sad_Talkingx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris down04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Madre acabaría por hallarme y ayudarme."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris down05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "y yo..."

    show neus_exp_mouth sad_Talkingx10
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows angryx02
    with dissolve

    ne "¡Él sabía que la cagaría en algún momento!"

    show neus_exp_mouth sad_Talkingx09
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris down01
    show neus_exp_eyebrows angryx03
    with dissolve

    ne "y que entonces Madre se expondría para salvarme."

    show neus_exp_mouth sad_Talkingx10
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "¡Soy una imbécil!"

    show neus_exp_mouth sad_Talkingx07
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Debiste matarme [protname]..."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Sabía que después del beso de Txell..."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris down05
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "¡Tenía que haber abandonado Barcelona antes!"

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx05
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    if afternoon05_NeusMeeting_Told == False:

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx05
        with fade

        pt "¿El beso de Txell?"

        pt "¿La rubia y [neusname] se besaron?"

        show m_exp_mouth sad_Talkingx02
        show m_exp_eyes 05
        show m_exp_piris left05
        show m_exp_eyebrows sadx06
        with dissolve

    else:

        show m_exp_mouth sad_Talkingx02
        show m_exp_eyes 05
        show m_exp_piris left05
        show m_exp_eyebrows sadx06
        with fade

    tx "Neus..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx07
    with dissolve

    pause 0.1

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx01
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx06
    with fade

    ne "Lo siento Mamá..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx07
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx04
    with dissolve

    p "Si ese era su objetivo desde el principio,"

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx03
    with dissolve

    p "¿porqué me ha estado empujando en la dirección contraria?"

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with dissolve

    p "¿Porqué quería que me uniera a él y te matara?"

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with dissolve

    tx "Porque si hay algo que deseaba más que recuperarla,"

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with fade

    tx "era destrozar lo único por lo que ha estado sufriendo en vida todos estos años."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "La esperanza de que pudiera alejar a su hijo de su influencia."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx02
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with fade

    ne "¿Cómo sabes...?"

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris right03
    show neus_exp_eyebrows sadx03
    with dissolve

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with fade

    tx "Porque el libro que me entregó,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "sin duda,"

    extend " sabía que estaba escrito por ella."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx03
    with dissolve

    ne "..."

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "didac_theme"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows surprisex02
    with dissolve

    d "¿Por qué está llorando...?"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with fade

    tx "¡¿Podrías callarte por unos segundos?!"

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Talkingx08
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows angryx03

    with dissolve

    d "¡Pero si solo he hecho una pregunta!"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows angryx02

    with dissolve

label afternight05_Pedrera_NowWhat: 

    menu:

        pt "¿Y ahora qué?"

        "Dídac, larguémonos de aquí." if afternight05_Pedrera_WhyNotKillMe_WhoILove == False:
            call p_Help
            $pl.ch_pts("np",-5)

            $ afternight05_Pedrera_LetsGetOut_COND = True

            jump afternight05_Pedrera_LetsGetOut

        "¿Y qué se supone que debemos hacer ahora?":
            call p_Help

            $ Pedrera_char_Cond = "NeusWall"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with fade

            ne "..."

            jump afternight05_Pedrera_WeAreSafeHere

            
label afternight05_Pedrera_LetsGetOut:

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02

    show didacf_mouth sad_Silentx02
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows sadx01

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows surprisex01
    with dissolve

    ne "No..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with fade

    p "No,"

    extend " ¿Qué?"

    show neus_exp_mouth sad_Silentx05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx05
    with dissolve

    menu:

        "¡¿Aún tienes las narices de dirigirme la palabra?!":
            call p_Help

            $ afternight05_Pedrera_StillTalkToMe_COND = True

            $pl.ch_pts("np",-3)

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx05
            with vpunch

            ne "..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with dissolve

            tx "[protname]..."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with fade

            tx "No seas tan duro con ella..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx02
            with dissolve

            menu:

                "Txell, esto no va contigo.":
                    call p_Help

                    $pl.ch_pts("np",-1)
                    $pl.ch_pts("mp",-1)

                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx03
                    with dissolve

                    tx "..."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 02
                    show m_exp_piris left02
                    show m_exp_eyebrows serious
                    with dissolve

                    ne "En realidad sí."

                    $ Pedrera_char_Cond = "NeusWall"
                    call Pedrera_char_lab

                    show neus_exp_mouth sadbiting_Silentx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris left05
                    show neus_exp_eyebrows sadx04
                    with fade

                    p "..."

                "Quizás tienes razón.":
                    call p_Help
                    $pl.ch_pts("np",1)

                    $pl.ch_pts("mp",1)

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 02
                    show m_exp_piris left02
                    show m_exp_eyebrows serious
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusWall"
                    call Pedrera_char_lab

                    show neus_exp_mouth sadbiting_Silentx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris left05
                    show neus_exp_eyebrows sadx04
                    with fade

                    tx "..."

                "...":
                    call p_Help

                    $ Pedrera_char_Cond = "NeusWall"
                    call Pedrera_char_lab

                    show neus_exp_mouth sadbiting_Silentx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris left05
                    show neus_exp_eyebrows sadx04
                    with fade

                    ne "..."

                    

        "...":
            call p_Help

 
label afternight05_Pedrera_WeAreSafeHere:

    if music_play != "despairAndTriunph":
        play music "audio/music/kevinmacleod/sad/despairAndTriunph.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "despairAndTriunph"

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Mientras sigamos en este edificio,"

    extend " por el momento estamos seguros."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Al menos hasta que salga el sol."

    show neus_exp_mouth sad_Silentx03
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx02
    with dissolve

    tx "¿Y después?"

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Mañana por la noche será el solsticio."

    show neus_exp_mouth sad_Talkingx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Cuando se haga de noche,"

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "no importa en qué lugar sagrado,"

    extend " o energético nos encontremos,"

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "nos va a encontrar y matar."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "A menos que..."

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx04
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx04
    with dissolve

    tx "¡¿A menos que qué?!"

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_iris front08
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Lo único que podría escondernos de su radar,"

    show neus_exp_mouth sad_Talkingx05
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris down03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "es que en nuestro interior,"

    extend " haya su propia semilla."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Tu esperma."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx06
    with dissolve

    p "..."

    menu:

        pt "Correrme dentro de Dídac, Meritxell y [neusname]..."

        "<Negarte a hacerlo>" if afternight05_Pedrera_WhyNotKillMe_WhoILove == False:

            call p_Help

            $pl.ch_pts("np",-2)
            $pl.ch_pts("mp",-3)

            jump afternight05_Pedrera_NeusRejection

        "<Aceptarlo, pero mencionar que hubieras preferido hacerlo a solas con [neusname]>" if afternight05_Pedrera_LetsGetOut_COND == False:

            $pl.ch_pts("np",2)
            $pl.ch_pts("dp",-1)

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx04
            with dissolve

            p "Desde luego,"

            extend " no es el modo en que me imaginaba el final de esta cita."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx06
            with dissolve

            ne "Lo siento..."

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Yo tampoco me la imaginaba así,"

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne " te lo aseguro."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx04
            with dissolve

            jump afternight05_Pedrera_NeusAcceptance

        "<Aceptar a ayudarlas>" if afternight05_Pedrera_LetsGetOut_COND == True:

            $pl.ch_pts("np",1)
            $pl.ch_pts("dp",1)
            #$pl.ch_pts("mp",1)

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            p "Hmmm..."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx05
            with dissolve

            p "Supongo que no hay otro remedio."

            show neus_exp_mouth happy_Talkingx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Gracias [protname]..."

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx04
            with dissolve

            jump afternight05_Pedrera_NeusAcceptance

        "<Aceptar ayudarlas gratamente>" if afternight05_Pedrera_LetsGetOut_COND == False:

            $pl.ch_pts("np",1)
            $pl.ch_pts("dp",1)
            $pl.ch_pts("mp",1)

            show neus_exp_mouth sad_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx02
            with dissolve

            p "Bueno,"

            extend " si hay que sacrificarse por el bien común;"

            show neus_exp_mouth sad_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx01
            with dissolve

            p "creo que hay peores maneras de hacerlo que disfrutando de la compañía de tres hermosas mujeres."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx05
            with dissolve

            tx "Desde luego,"

            extend " que sensibilidad tienes con Neus..."

            show neus_exp_mouth sad_Talkingx001
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "No-"

            extend "no me importa..."

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Tiene razón."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris down04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "Al fin y al cabo,"

            extend " todo esto es por mi culpa..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx04
            with dissolve

            menu:

                pt "Su culpa..."

                "Hay que mirar hacia delante y no lamentarse por lo que ya no se puede cambiar.":

                    call p_Help

                    $pl.ch_pts("np",1)
                    $pl.ch_pts("mp",1)

                    show neus_exp_mouth sad_Silentx01
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth happy_Talkingx02
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    ne "Gracias [protname]."

                    show neus_exp_mouth happy_Silentx01
                    $ nteye = 6
                    call neus_exp_tears_tears
                    show neus_exp_iris front06
                    show neus_exp_eyebrows sadx02
                    with dissolve

                "<No decir nada>":

                    call p_Help

                    pass

            jump afternight05_Pedrera_NeusAcceptance




label afternight05_Pedrera_NeusAcceptance:

    menu:

        "Aunque sigo sin aprobar de ninguna forma lo que le hiciste a ese pobre niño.":

            call p_Help

            show neus_exp_mouth sad_Silentx03
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx02
            with dissolve

            p "Prométeme que nunca más lo volverás a hacer."

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Te prometo que nunca más lo volveré a hacer para salvar mi vida."

            show neus_exp_mouth sad_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            p "¿Tu vida?"

            show neus_exp_mouth sad_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx04
            with dissolve

            p "Te he dicho que no hay razón alguna que justifique..."

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Ya sé lo que has dicho."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx05
            with dissolve

            p "Pero..."

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Sinceramente,"

            extend " no sé de lo que sería capaz de hacer para salvar la tuya."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "No quiero volver a mentirte de nuevo,"

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "así que no me hagas prometer algo que no sé si podré cumplir."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

            p "..."

            if music_play != "didac_theme":
                play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "didac_theme"

            show neus_exp_mouth sad_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows sadx01
            with dissolve

            d "Que cursi ha sonado eso,"

            extend " ¿no?"

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows angryx03

            show didacf_mouth sad_Silentx02
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows surprisex02
            with fade

            tx "¿Por qué eres tan bocazas?"

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03

            show didacf_mouth sad_Silentx01
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            with dissolve

            p "Porque es así de idiota."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx02

            show didacf_mouth sad_Silentx05
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils right05
            show didacf_eyebrows suspiciousx02
            with dissolve

            d "Tssk..."

            $ Pedrera_char_Cond = "NeusWall"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx01
            with fade

            pause 0.2

        "<No decir nada>":

            show neus_exp_mouth sad_Silentx01
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "..."

            call p_Help


    ##

    jump afternight05_Pedrera_SexPrevious
    

label afternight05_Pedrera_NeusRejection:

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Si crees que después de todo lo que ha ocurrido aquí,"

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx03
    with dissolve

    p "después de lo que sé de ti,"

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx04
    with dissolve

    p "después de saber todo lo que has hecho..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with dissolve

    p "Me van a quedar ganas de follar contigo;"

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¡Es que estás más enferma de lo que me imaginaba!"

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx05
    with dissolve

    tx "¡¿Es que no lo entiendes [protname]?!"

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx03
    with fade

    tx "Todo lo que ha hecho,"

    extend " es para poder escapar de su padre!"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex002
    with dissolve

    p "¡¿Incluso lo de matar a ese niño?!"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "¿Qué...?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "¿Que niño?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Para transformar a Dídac en mujer,"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex002
    with dissolve

    p "tuvo que sacrificar a un niño inocente."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex002
    with dissolve

    p "Y todo ello,"

    extend " porque no fue capaz de hablar conmigo en primer lugar."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Me hizo creer durante todo este tiempo,"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "que Dídac intentó violarla,"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    
    show didacf_mouth sad_Silentx02
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    with fade

    p "cuando en realidad,"

    extend " fue ella misma quien provocó esa situación."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01

    show didacf_mouth sad_Silentx03
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with dissolve

    tx "Neus..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02

    show didacf_mouth sad_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx02
    with dissolve

    tx "¿Es eso verdad?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx03

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows normal
    with dissolve

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with fade

    ne "..."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_iris down05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Sí..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    d "..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_iris right05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    d "Un momento..."

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    
    show didacf_mouth sad_Talkingx08
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils left00
    show didacf_eyebrows surprisex02
    with fade

    d "¿La culpa de que sea mujer,"

    extend " es de la gafotas de clase?"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx05
    
    show didacf_mouth sadbiting_Silentx04
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex01
    with dissolve

    tx "..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    
    show didacf_mouth sad_Talkingx08
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows angryx01
    with dissolve

    d "¡¿Por que la intenté violar?!"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx03
    
    show didacf_mouth sadbiting_Silentx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    with dissolve

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Silentx01
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    with fade

    p "Sí."

    show didacf_mouth sad_Talkingx09
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "¡¿Cuando?!"

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with dissolve

    ne "Dídac..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris down05
    show neus_exp_eyebrows sadx05
    with fade

    ne "Lo lamento,"

    extend " lo lamento tanto..."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Esto..."

    extend " no tenía que haber terminado así..."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx04
    with dissolve

    d "Pero..."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx05
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows surprisex02
    with fade

    d "¡¿Yo la violé?!"

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows suspiciousx01
    with dissolve

    p "Eso me hizo creer."

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows surprisex01
    with dissolve

    ne "Lo siento..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx06
    with fade

    menu:

        pt "¡¿Qué es lo que siente?!"

        "¡No te hagas la víctima ahora!":
            call p_Help

            $pl.ch_pts("np",-5)

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows sadx01
            with dissolve

            p "Todo esto ha pasado por tu culpa."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx04
            with dissolve

            tx "No seas tan dura con ella..."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx02
            with fade

            p "¡¿Que no lo sea?!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            p "¡¿Acaso no te das cuenta de todo el mal que ha hecho?!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris left04
            show m_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusWall"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx07
            with fade

            ne "..."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows sadx01
            with fade

            tx "Estoy segura que nunca se hubiera imaginado este escenario."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 04
            show m_exp_piris left04
            show m_exp_eyebrows sadx03
            with dissolve

            ne "No así..."

            $ Pedrera_char_Cond = "NeusWall"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx06
            with fade

            p "¿Y se supone que tengo que disculparla?"

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx07
            with dissolve

            p "¡¿y tan amigos?!"

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            # show m_exp_mouth sadbiting_Silentx04
            # show m_exp_eyes 05
            # show m_exp_piris left05
            # show m_exp_eyebrows sadx04
            
            show didacf_mouth sad_Silentx03
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils left03
            show didacf_eyebrows normal
            with fade

            tx "..."

        "...":
            call p_Help

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 05
            show m_exp_piris left05
            show m_exp_eyebrows sadx05
            
            show didacf_mouth sad_Silentx04
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils left04
            show didacf_eyebrows sadx01
            with fade

            d "..."

            pass

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    
    show didacf_mouth sad_Talkingx05
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows sadx01
    with fade

    d "¿Existe alguna manera de volver a ser hombre?"

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx03
    with dissolve

    p "..."

    if DidacPregnant:

        show neus_exp_mouth sad_Talkingx001
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "No..."

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "No si te quedaste embarazada."

        show neus_exp_mouth sad_Silentx04
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx04
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab
        
        show didacf_mouth sadbiting_Silentx03
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows sadx01
        with fade

        d "..."

        if DidacSex_Vaginal:

            show didacf_mouth sad_Talkingx02
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils left04
            show didacf_eyebrows sadx03
            with dissolve

            d "Pero..."

            show didacf_mouth sad_Talkingx04
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils left02
            show didacf_eyebrows sadx02
            with dissolve

            d "seguiré teniendo los orgasmos que he tenido hasta ahora..."

            show didacf_mouth sad_Talkingx03
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils left05
            show didacf_eyebrows sadx03
            with dissolve

            d "¿Verdad?"

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils left05
            show didacf_eyebrows sadx04
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusWall"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx03
            with fade

            ne "..."

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "Sí..."

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris right03
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Pero únicamente si te los proporciona [protname]."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "De otro modo difícilmente consigas alcanzar el orgasmo."

            show neus_exp_mouth sad_Talkingx06
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Solo su semilla puede complacerte,"

            show neus_exp_mouth sad_Talkingx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris down04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "pues así fue cómo pactó este conjuro mi padre con sus criaturas,"

            show neus_exp_mouth sad_Talkingx07
            $ nteye = 8
            call neus_exp_tears_tears
            show neus_exp_iris front08
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "para que solo él pudiera complacernos de verdad."

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx07
            with dissolve

            pause 0.2

            if not DidacMCPregnant:

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx01
                with dissolve

                p "Pero no fui yo quien se corrió dentro."

                show neus_exp_mouth sad_Talkingx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "Eso no cambia nada."

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx04
                with dissolve

                p "..."

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab
            
            show didacf_mouth sadbiting_Silentx03
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils left00
            show didacf_eyebrows surprisex02
            with fade

            d "..."

            show didacf_mouth sad_Talkingx07
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows surprisex01
            with dissolve

            d "¿Te has follado a tu padre?"

            show didacf_mouth sadbiting_Silentx02
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            with dissolve

            p "Dídac,"

            extend " sé que tienes preguntas,"

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows suspiciousx01
            with dissolve

            p "pero ya te las contaré en otro momento."

            show didacf_mouth sadbiting_Silentx03
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils left03
            show didacf_eyebrows suspiciousx02
            with dissolve

            d "..." 

    else:

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Sí."

        show neus_exp_mouth sad_Talkingx04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris right04
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "Mañana empezarás a transformarte de nuevo poco a poco en el hombre que eras."

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab

        show didacf_mouth sadbiting_Silentx01
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows normal
        with dissolve

        d "..."

        show didacf_mouth happy_Talkingx05
        $ dteye = 0
        call didac_exp_tears_tears
        show didacf_pupils left00
        show didacf_eyebrows surprisex01
        with dissolve

        d "¡Bueno!"

        show didacf_mouth happy_Talkingx06
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils front01
        show didacf_eyebrows normal
        with dissolve

        d "¡Eso son buenas noticias!"

        show didacf_mouth sad_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows serious
        with dissolve

        p "Algo que ni debería haber ocurrido nunca."

    ##

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01

    show didacf_mouth sadbiting_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows normal
    with fade

    tx "¿Y ahora qué?"

    extend " entonces."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "¿Tiene que follarnos a todas?"

    if not DidacPregnant:

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 01
        show m_exp_piris right01
        show m_exp_eyebrows suspiciousx02

        show didacf_mouth sadbiting_Silentx01
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils front01
        show didacf_eyebrows suspiciousx02
        with dissolve

        tx "¿Incluso a Dídac?"

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx02
    with fade

    ne "No necesariamente."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_iris right04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Con que cada una de nosotras tenga un poco de esperma en su interior,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_iris right05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "aunque sea por vía oral,"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "debería bastar."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris left05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Al menos durante mañana..."

    ###

label afternight05_Pedrera_PregnancyInterrogation:

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_iris front00
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Y a qué venía entonces lo que dijo tu padre,"

    extend " sobre dejarte embarazada?"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris front01
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx01
    with dissolve

    tx "¡¿Embarazada?!"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris left04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Si me quedara preñada de ti,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_iris down04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Padre no podría encontrarme ni manipularme;"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris left05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "al menos durante nueve meses..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_iris left05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    menu:

        pt "Quedarse embarazada para no ser encontrada..."

        "Y además, pensaste que de este modo me sentiría responsable del niño.":
            call p_Help

            $pl.ch_pts("np",-1)

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_iris front00
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_eyebrows surprisex01
            with dissolve

            p "y no me alejaría de ti."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_iris front01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx01
            with dissolve

            p "¡¿No es así?!"

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_iris front04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_iris left05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx05
            with dissolve

            tx "Neus..."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_iris left02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "¡Era una opción!"

            show neus_exp_mouth sad_Talkingx01
            show neus_exp_iris down05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "No..."

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_iris right04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "Madre dijo que era el único modo,"

            extend " que..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_iris left02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "sería la manera más segura..."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_iris left05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_eyebrows sadx04
            with dissolve

            menu:

                pt "Madre le dijo..."

                "Si no tenías suficiente con que tu padre te manipulara, luego te dejaste manipular por tu madre.":
                    call p_Help

                    $pl.ch_pts("np",-3)

                    show neus_exp_mouth sadbiting_Silentx02
                    show neus_exp_iris front00
                    $ nteye = 0
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    p "¿Es que no tienes criterio propio?!"

                    show neus_exp_mouth sad_Talkingx09
                    show neus_exp_iris front01
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "¡Claro que sí!"

                    show neus_exp_mouth sad_Talkingx11
                    show neus_exp_iris front02
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    ne "¡Si hubiera querido quedarme embarazada de ti"

                    show neus_exp_mouth sad_Talkingx10
                    show neus_exp_iris front03
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "solo tendría que haber sacrificado a más gente,"

                    show neus_exp_mouth sad_Talkingx09
                    show neus_exp_iris front04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "y manipularte hasta tenerte bajo mi control!"

                    show neus_exp_mouth sad_Silentx10
                    show neus_exp_iris front04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    p "..."

                    show neus_exp_mouth sad_Talkingx09
                    show neus_exp_iris left04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "¡O dejarte en un almacén inmóvil,"

                    show neus_exp_mouth sad_Talkingx10
                    show neus_exp_iris front02
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "y luego ordeñarte como si fueras una vaca de granja cuando me diera la gana!"

                    show neus_exp_mouth sad_Silentx09
                    show neus_exp_iris front04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    p "..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_iris front05
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Pero eso..."

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_iris front08
                    $ nteye = 8
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "Eso me hubiera convertido en Padre..."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_iris left05
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    p "..."

                "...":
                    call p_Help

                    pass

        "...":
            call p_Help

            pass

label afternight05_Pedrera_SufferedEnough:

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with fade

    tx "[protname]."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "¿No crees que ya ha sufrido bastante?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        "¡¿Tú crees?!...":
            call p_Help

            $pl.ch_pts("np",-1)
            $pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03
            with dissolve

            tx "¡Sí!"

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            tx "¡Lo creo!"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx03
            with dissolve

            pause 0.2

            if DidacPregnant:

                $ Pedrera_char_Cond = "TxellDidac"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows angryx03
                
                show didacf_mouth sadbiting_Silentx01
                $ dteye = 1
                call didac_exp_tears_tears
                show didacf_pupils left01
                show didacf_eyebrows surprisex01
                with fade

                tx "¡Al fin y al cabo Dídac ha tomado su propia decisión!"

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx04

                show didacf_mouth sadbiting_Silentx03
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows sadx01
                with dissolve

                tx "¡Y tampoco es que tú estés libre de culpa!"

                if DidacMCPregnant:

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx04

                    show didacf_mouth sadbiting_Silentx04
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils right04
                    show didacf_eyebrows sadx02
                    with dissolve

                    menu:

                        pt "¡En teoría estaba usando preservativo!"

                        "¡No sabía que había roto el condón!":
                            call p_Help

                            $pl.ch_pts("dp",-1)

                            show m_exp_mouth sad_Talkingx004
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows angryx01
                            
                            show didacf_mouth sadbiting_Silentx02
                            $ dteye = 1
                            call didac_exp_tears_tears
                            show didacf_pupils front01
                            show didacf_eyebrows surprisex01
                            with dissolve

                            tx "¿Y eso te exculpa de habértelo follado?"

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows suspiciousx01
                            
                            show didacf_mouth sadbiting_Silentx03
                            $ dteye = 2
                            call didac_exp_tears_tears
                            show didacf_pupils front02
                            show didacf_eyebrows angryx02
                            with dissolve

                            p "¡Fue él quien me lo pidió!"

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows surprisex001
                            
                            show didacf_mouth sad_Silentx05
                            $ dteye = 3
                            call didac_exp_tears_tears
                            show didacf_pupils front03
                            show didacf_eyebrows angryx03
                            with dissolve

                            p "¡De hecho, casi me lo exigió a gritos!"

                            show m_exp_mouth sad_Silentx05
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows angryx01
                            
                            show didacf_mouth sad_Silentx06
                            $ dteye = 8
                            call didac_exp_tears_tears
                            show didacf_pupils front08
                            show didacf_eyebrows angryx03
                            with dissolve

                            p "Y tampoco iba a pasar nada grave si lo hacíamos con preservativo,"

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris right05
                            show m_exp_eyebrows suspiciousx01
                            
                            show didacf_mouth sadbiting_Silentx06
                            $ dteye = 4
                            call didac_exp_tears_tears
                            show didacf_pupils right04
                            show didacf_eyebrows angryx03
                            with dissolve

                            p "más allá de lo incómodo que pudiéramos sentirnos al recordar lo sucedido una vez hubiera pasado todo..."

                            # $ Pedrera_char_Cond = "TxellClose_b"
                            # call Pedrera_char_lab

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows suspiciousx01
                            
                            show didacf_mouth sad_Silentx05
                            $ dteye = 5
                            call didac_exp_tears_tears
                            show didacf_pupils right05
                            show didacf_eyebrows angryx03
                            with dissolve

                            p "¡Yo he sido la victima de vuestras mentiras todo este tiempo!"

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows surprisex01
                            
                            show didacf_mouth sadbiting_Silentx05
                            $ dteye = 8
                            call didac_exp_tears_tears
                            show didacf_pupils front08
                            show didacf_eyebrows angryx04
                            with dissolve

                            p "Creo que no es comparable."

                            show m_exp_mouth sad_Silentx05
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows suspiciousx02
                            
                            show didacf_mouth sad_Silentx06
                            $ dteye = 5
                            call didac_exp_tears_tears
                            show didacf_pupils right05
                            show didacf_eyebrows angryx03
                            with dissolve

                            tx "..."

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 03
                            show m_exp_piris left03
                            show m_exp_eyebrows surprisex01
                            
                            show didacf_mouth sad_Silentx03
                            $ dteye = 3
                            call didac_exp_tears_tears
                            show didacf_pupils left03
                            show didacf_eyebrows angryx01
                            with dissolve

                            ne "Tiene razón."

                            show m_exp_mouth sad_Talkingx04
                            show m_exp_eyes 04
                            show m_exp_piris left04
                            show m_exp_eyebrows sadx02
                            
                            show didacf_mouth sad_Silentx05
                            $ dteye = 5
                            call didac_exp_tears_tears
                            show didacf_pupils left05
                            show didacf_eyebrows suspiciousx02
                            with dissolve

                            tx "Neus..."

                        "...":

                            call p_Help
                            pass

                else: # Pregnant by someone else.

                    show m_exp_mouth sad_Silentx01
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows angryx01

                    show didacf_mouth sadbiting_Silentx04
                    $ dteye = 3
                    call didac_exp_tears_tears
                    show didacf_pupils front03
                    show didacf_eyebrows surprisex01
                    with dissolve

                    p "¡¿Yo?!"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows serious

                    show didacf_mouth sadbiting_Silentx02
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils front04
                    show didacf_eyebrows serious
                    with dissolve

                    p "¿Culpa?"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris right02
                    show m_exp_eyebrows sadx01

                    show didacf_mouth sad_Silentx04
                    $ dteye = 5
                    call didac_exp_tears_tears
                    show didacf_pupils front05
                    show didacf_eyebrows sadx01
                    with dissolve

                    p "¡Yo no he sido el que se ha corrido dentro!"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx02

                    show didacf_mouth sad_Silentx04
                    $ dteye = 5
                    call didac_exp_tears_tears
                    show didacf_pupils front05
                    show didacf_eyebrows serious
                    with dissolve

                    tx "Pero podrías haberlo detenido."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows normal

                    show didacf_mouth sad_Silentx05
                    $ dteye = 4
                    call didac_exp_tears_tears
                    show didacf_pupils right04
                    show didacf_eyebrows angryx01
                    with dissolve

                    p "No soy su niñera."

                    # if not minigame or not sex at all.

                    if DidacSex_Vaginal == False:

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows surprisex01

                        show didacf_mouth sad_Silentx05
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils front04
                        show didacf_eyebrows angryx01
                        with dissolve

                        p "Además,"

                        extend " lo más seguro es que hubiera acabado violándome a mi también."

                    # If DIdac saw you at the park.

                    if afternight04_Park_HelpDidacPolice_Cond:

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows sadx01

                        show didacf_mouth sad_Talkingx08
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils front05
                        show didacf_eyebrows angryx03
                        with dissolve

                        d "¡De hecho podrías haberme detenido en el parque,"

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows sadx01

                        show didacf_mouth sad_Talkingx09
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows angryx02
                        with dissolve

                        d "antes de que ese \"yonki\" de mierda se corriera dentro de mi!"

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 03
                        show m_exp_piris right03
                        show m_exp_eyebrows sadx01

                        show didacf_mouth sad_Talkingx09
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils front04
                        show didacf_eyebrows angryx04
                        with dissolve

                        d "¡Me ayudaste a salir de ahí justo cuando se había corrido dentro de mi!"

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows serious

                        show didacf_mouth sad_Talkingx06
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows angryx01
                        with dissolve

                        d "¡¿Por qué esperaste hasta entonces?!"

                        show m_exp_mouth sad_Silentx02
                        show m_exp_eyes 01
                        show m_exp_piris right01
                        show m_exp_eyebrows surprisex01

                        show didacf_mouth sad_Talkingx06
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils front03
                        show didacf_eyebrows serious
                        with dissolve

                        p "..."

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 01
                        show m_exp_piris front01
                        show m_exp_eyebrows surprisex001

                        show didacf_mouth sad_Silentx06
                        $ dteye = 3
                        call didac_exp_tears_tears
                        show didacf_pupils right03
                        show didacf_eyebrows angryx03
                        with dissolve

                        tx "¡¿Es eso verdad?!"

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 00
                        show m_exp_piris front00
                        show m_exp_eyebrows surprisex01

                        show didacf_mouth sad_Silentx04
                        $ dteye = 2
                        call didac_exp_tears_tears
                        show didacf_pupils front02
                        show didacf_eyebrows angryx01
                        with dissolve

                        p "No lo voy a negar."

                        $pl.ch_pts("np",-3)
                        $pl.ch_pts("mp",-3)

                        show m_exp_mouth sad_Talkingx08
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx04

                        show didacf_mouth sad_Silentx08
                        $ dteye = 4
                        call didac_exp_tears_tears
                        show didacf_pupils right04
                        show didacf_eyebrows angryx02
                        with dissolve

                        tx "¿Y aún tienes las narices de decir que no tienes ninguna culpa?"

                        show m_exp_mouth sad_Silentx04
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows angryx01

                        show didacf_mouth sad_Silentx09
                        $ dteye = 5
                        call didac_exp_tears_tears
                        show didacf_pupils front05
                        show didacf_eyebrows angryx03
                        with dissolve

                        p "Fui como espectador,"

                        extend " no hice nada más que mirar."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows sadx01

                show didacf_mouth sad_Silentx07
                $ dteye = 4
                call didac_exp_tears_tears
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                with dissolve

                p "Ya es mayorcito para aceptar las consecuencias de sus decisiones."

                show m_exp_mouth sad_Silentx01
                show m_exp_eyes 01
                show m_exp_piris left01
                show m_exp_eyebrows surprisex01

                show didacf_mouth sad_Silentx03
                $ dteye = 2
                call didac_exp_tears_tears
                show didacf_pupils left02
                show didacf_eyebrows serious
                with dissolve

                ne "No..."

                $ Pedrera_char_Cond = "NeusWall"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with fade

                ne "no si sentía la necesidad carnal de satisfacer sus deseos,"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "no es tan fácil evitar esa tentación."

                show neus_exp_mouth sad_Silentx02
                show neus_exp_iris front01
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with dissolve

                p "Tú lo has dicho."

                show neus_exp_mouth sad_Silentx03
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                p "Tentación."

                show neus_exp_mouth sad_Silentx02
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                p "Se trata de tener mantener la cabeza fría,"

                extend " y ser un poco más responsable."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris left02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Es normal que pienses así,"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "si no has sufrido este apetito insaciable y enfermizo en tus carnes."

                show neus_exp_mouth sad_Silentx03
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                p "..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "Se requiere de una mente admirable,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "y una fuerza de voluntad inquebrantable,"

                extend " casi inhumana,"

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "para evitar la tentación."

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_iris front08
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Es un deseo,"

                extend " una voracidad,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "que es prácticamente imposible huir de ella sin un poco de ayuda."

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris front03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Especialmente cuando te pasa por primera vez y no sabes lo que te está ocurriendo."

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows serious
                with dissolve

                p "Bueno,"

                extend " pues entonces es culpa tuya."

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_iris front00
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with dissolve

                ne "¡¿Cómo?!"

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_iris front01
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_eyebrows normal
                with dissolve

                p "¿No crees que hubiera sido mejor que me hubieras contado esto antes?"

                show neus_exp_mouth sad_Talkingx001
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Yo..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris left03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "No sabía que Padre estaría detrás de todo tan pronto..."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                p "Pero sospechabas que podría haber la posibilidad;"

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                p "¿no crees que un poco más de información hubiera ayudado?"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris front06
                $ nteye = 6
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Si te hubiera contado esto antes,"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris left05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "lo más probable es que no me hubieras creído,"

                extend " o algo peor."

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_iris front05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                p "Ya..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_iris down05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Al fin y al cabo,"

                extend " conociendo a mi padre,"

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_iris left04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "lo que realmente hubiera hecho es zanjar el asunto sin más,"

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_iris left05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "así que tampoco tenía mucho sentido contarte nada."

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                p "Pero sin embargo no ha sido así."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_iris left04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "No..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris left05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Porque en realidad no era a mi quien buscaba..."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_iris left05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx06
                with dissolve

                ne "..."

                $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx03
                with fade

                tx "[protname]"

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx04
                with dissolve

                tx "Ya basta,"

                extend " ¿no crees?"

                    # p "¿Y qué me dices del niño sacrificado?"

            else: # If she is not pregnant

                show m_exp_mouth sad_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx03
                with dissolve

                tx "¡Al fin y al cabo mañana Dídac volverá a ser el hombre que era!"

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 02
                show m_exp_piris left02
                show m_exp_eyebrows serious
                with dissolve

                ne "Bueno,"

                extend " mañana empezará la transformación,"

                $ Pedrera_char_Cond = "NeusWall"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_iris right04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with fade

                ne "quizás tarde dos o tres días..."

                $ Pedrera_char_Cond = "TxellClose_b"
                call Pedrera_char_lab

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 01
                show m_exp_piris left01
                show m_exp_eyebrows suspiciousx02
                with fade

                tx "..."

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows angryx01
                with dissolve

                tx "¡El caso es que volverá a ser el de siempre!"

                show m_exp_mouth sadbiting_Silentx03
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows serious
                with dissolve

                p "Y como si nada hubiera ocurrido,"

                extend " ¿Verdad?"

                show m_exp_mouth sadbiting_Silentx02
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx01
                with dissolve

                p "Olvidemos que me hizo creer que mi amigo era un violador en potencia,"

                show m_exp_mouth sadbiting_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows serious
                with dissolve

                p "que tiene un padre psicótico que lo más probable es que me quiera muerto,"

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 02
                show m_exp_piris left02
                show m_exp_eyebrows sadx01
                with dissolve

                p "que me chantajeó para tener tres citas con ella sin contarme ni la mitad de la historia..."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris left04
                show m_exp_eyebrows sadx02
                with dissolve

                ne "He intentado contante tanto como he podido..."

                $ Pedrera_char_Cond = "NeusWall"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Silentx03
                show neus_exp_iris front00
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_eyebrows surprisex01
                with fade

                p "¿Lo de que era tu hermano también tenías planeado contármelo?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_iris front01
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_eyebrows normal
                with dissolve

                p "¿Cuándo?"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_iris front02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx01
                with dissolve

                p "¿Hoy?"

                extend " ¿Mañana?"

                extend " ¿Después de que te dejara embarazada?"

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_iris left04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx03
                with dissolve

                p "¿O quizás dentro de unos años mejor?"

                show neus_exp_mouth sad_Silentx05
                show neus_exp_iris left05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx04
                with dissolve

                p "¿O eso si de caso tampoco hacía falta?"

                show neus_exp_mouth sadbiting_Slientx05
                show neus_exp_iris front07
                $ nteye = 7
                call neus_exp_tears_tears
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "..."

        "...":

            jump afternight05_Pedrera_WhatAboutKid

label afternight05_Pedrera_WhatAboutKid:

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with vpunch

    p "¡¿Y qué me dices del niño sacrificado?!"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx03
    with dissolve

    tx "¿Y qué me dices de las decenas o centenares de niños que hubiera tenido que matar,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "de no haber hecho este sacrificio?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        pt "¡Aún se le tendrá que dar las gracias y todo por haber matado a un niño inocente!"

        "¡¿Esa es la excusa?! ¡¿Por un mal menor?!":
            call p_Help

            $pl.ch_pts("mp",-1)

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows serious
            with dissolve

            p "¿Qué clase de justificación es esta?"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx04
            with dissolve

            tx "¡La que puede salvar vidas!"

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "¿Sacrificarías al amor de tu vida,"

            extend " o a tu propio hijo,"

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows normal
            with dissolve

            p "para salvar un autobús lleno de niños?"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            p "¿O quizás para salvar a dos niños?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            p "¿Cuál es el número exacto que se requiere en tu opinión para justificar el sacrificio de un niño inocente?"

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            tx "..."

        "...":

            call p_Help

            pass

    ###

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris front04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with fade

    ne "Sino lo haces por mi,"

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_iris front05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "Al menos,"

    extend " hazlo por ellas..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx07
    with dissolve

    ne "No dejes que mueran por mi culpa."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris front08
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    p "..."

    menu:

        pt "{i}Hazlo por ellas{/i}, dice..."

        "<Largarte con Dídac a casa e intentar dejar atrás todo esto>":
            call p_Help

            jump afternight05_Pedrera_DecideToLeave

        "NOT FINISHED":

            call p_Help

            # NOT FINISHED

            jump endupdate

label afternight05_Pedrera_DecideToLeave:

    $pl.ch_pts("np",-10)
    $pl.ch_pts("mp",-10)

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Silentx01
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows normal
    with fade

    p "Dídac."

    show didacf_mouth sad_Talkingx01
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    with dissolve

    d "¿Euh?..."

    show didacf_mouth sad_Silentx01
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    with dissolve

    p "Nos largamos."

    show didacf_mouth sad_Talkingx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "¿E-"

    extend "estás seguro?"

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows sadx01
    with dissolve

    menu:

        "¡¿Es que te quieres quedar aquí con ellas?!":

            call p_Help

            $pl.ch_pts("dp",-2)

            show didacf_mouth sad_Silentx04
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            with dissolve

            p "Por mi haz lo que quieras."

            show didacf_mouth sad_Talkingx002
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils front04
            show didacf_eyebrows sadx01
            with dissolve

            d "No-"

            extend "no..."

            show didacf_mouth sad_Talkingx004
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex01
            with dissolve

            d "¡Espera!"

            jump afternight05_Pedrera_Leaving

        "No hagas que te lo repita.":

            call p_Help

            $pl.ch_pts("dp",-1)

            jump afternight05_DidacAcceptingLeave

        "Sí, estoy seguro.":

            call p_Help

            jump afternight05_DidacAcceptingLeave


label afternight05_DidacAcceptingLeave:

    show didacf_mouth sad_Silentx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils front04
    show didacf_eyebrows sadx02
    with dissolve

    d "..."

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows sadx04
    with dissolve

    n "Dídac les dedica un rostro de confusión y pésame a ambas chicas."

    show didacf_mouth sad_Talkingx02
    $ dteye = 8
    call didac_exp_tears_tears
    show didacf_pupils front08
    show didacf_eyebrows sadx03
    with dissolve

    d "Como quieras..."

    jump afternight05_Pedrera_Leaving


label afternight05_Pedrera_Leaving:

    scene night04_pedrera_baba01_background:
        subpixel True
        zoom 0.6
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4 xanchor -0.1
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4
        # xanchor 0.0 yanchor 0.0
    with fade

    play sound "audio/sfx/door_old_open02.ogg"

    n "Te dispones a salir por la puerta."

    ne "Por favor..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_iris front05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with fade

    ne "No dejes que Meritxell muera por mi culpa..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_iris front03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx02
    with dissolve

    p "Tú eres la única responsable de lo que le ocurra."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx07
    with dissolve

    ne "..."

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx04
    with fade

    tx "¡¿Qué te hace pensar que después de Neus,"

    extend " no irá a por ti después?!"

    if DidacPregnant:

        show m_exp_mouth sad_Talkingx09
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows angryx04
        with dissolve

        tx "¿Y qué me dices de Dídac?"

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx03
        with dissolve

        tx "¿Cómo justificarás su existencia?"

        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx03
        with dissolve

        tx "¿No tienes miedo de que acabe muerta a manos de esas criaturas oscuras,"

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx03
        with dissolve

        tx "si revela el origen de su transformación?"

        show m_exp_mouth sad_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx04
        with dissolve

        p "..."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Sigues siendo una amenaza para él."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx04
    with dissolve

    p "..."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    p "Es posible."

    if DidacPregnant:

        show m_exp_mouth sadbiting_Silentx02
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows serious
        with dissolve

        p "Si reclama mi vida o la de Dídac,"

        show m_exp_mouth sadbiting_Silentx04
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows suspiciousx01
        with dissolve

        p "es algo de lo que no puedo estar seguro,"

        show m_exp_mouth sadbiting_Silentx01
        show m_exp_eyes 00
        show m_exp_piris front00
        show m_exp_eyebrows surprisex01
        with dissolve

        p "pero al menos tendré la conciencia tranquila."

    else:

        show m_exp_mouth sadbiting_Silentx02
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows serious
        with dissolve

        p "Pero si eso ocurre,"

        show m_exp_mouth sadbiting_Silentx04
        show m_exp_eyes 00
        show m_exp_piris front00
        show m_exp_eyebrows surprisex01
        with dissolve

        p "al menos tendré la conciencia tranquila."

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx07
    with dissolve

    tx "¡¿Tranquila?!"

    show m_exp_mouth sad_Silentx14
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx06
    with dissolve

    p "No he sido responsable de ninguna muerte."

    if DidacPregnant:

        show m_exp_mouth sad_Talkingx11
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows angryx07
        with dissolve

        tx "¡¿No serás responsable de la muerte de tu amigo?!"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx05
    with dissolve

    tx "¡¿Tampoco de la mía?!"

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows serious
    with dissolve

    p "Tú misma te metiste en la boca del lobo cuando decidiste seguir tratándola,"

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx05
    with dissolve

    p "cuando viste que había algo extraño en ella."

    show m_exp_mouth sad_Silentx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx04
    with dissolve

    p "Ya eres mayorcita para ser responsable de tus propios errores."

    if DidacPregnant:

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows angryx03
        with dissolve

        p "Y en cuanto a Dídac,"

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows angryx02
        with dissolve

        p "confieso que no estoy seguro de cómo acabará la cosa,"

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx01
        with dissolve

        p "pero aún así,"

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows serious
        with dissolve

        p "es mejor que vivir con una arpía mentirosa,"

        extend " manipuladora"

        extend " y asesina."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows sadx01
        with dissolve

        p "Tampoco es que tenga muchas opciones."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx05
    with dissolve

    tx "¡¿De verdad te crees lo que estás diciendo?!"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx04
    with dissolve

    tx "¡Sí!"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx03
    with dissolve

    tx "¡Es verdad que intuía que había algo extraño!"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx05
    with dissolve

    tx "¡Pero aún así decidí tratarla,"

    extend " porque necesitaba ayuda!"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows serious
    with dissolve

    p "¿También necesitaba que la besaras?"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "Se sincera,"

    extend " no la trataste porque creíste que necesitara tu ayuda."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    p "Simplemente te acabaste enamorando de ella."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "Aunque realmente nunca sabrás si se trató de amor puro y sincero,"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    p "o del deseo influido por la oscura magia de su sangriento padre."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx01
    with dissolve

    tx "..."

label afternight05_Pedrera_IHadEnough:

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Ya he tenido suficiente con toda esta historia."

    scene night04_pedrera_baba01_background:
        subpixel True
        zoom 0.4
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.4 xanchor -0.1
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.4
    with fade

    p "Lo único que quería era ayudar a mi estúpido amigo;"

    p "y en realidad durante todo este tiempo,"

    p "el único que ha sido realmente un idiota,"

    extend " he sido yo,"

    p "al creerme a esta bruja."

    p "Nada de lo que ha dicho puede tomarse en serio."

    ne "Eso no es verdad..."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris front07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx07
    with vpunch

    p "¡Basta!"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_iris front05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    p "Apañaos como queráis,"

    extend " pero sin mi."

    if DidacPregnant:

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_iris front08
        $ nteye = 8
        call neus_exp_tears_tears
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "[protname],"

        extend " si quieres que Dídac sobreviva,"

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_iris front04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_eyebrows sadx06
        with dissolve

        ne "evita que caiga en problemas."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_iris front02
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Que nunca tengan que tomarle las huellas,"

        extend " o no vivirá para contarlo."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_iris front05
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_eyebrows sadx05
        with dissolve

        p "..."

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab

        show didacf_mouth sad_Talkingx03
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows sadx02
        with fade

        d "[protname],"

        extend " ¿Estás seguro de...?"

        show didacf_mouth sad_Silentx04
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows sadx01
        with dissolve

        p "Dídac,"

        extend " tú haz lo que quieras."

        show didacf_mouth sad_Silentx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows sadx04
        with dissolve

        p "Yo me largo."

    scene night04_pedrera_baba01_background:
        subpixel True
        zoom 0.6
        easein_quad 6.0 zoom 0.4
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.5
        easein_quad 12.0 zoom 0.4 xanchor -0.5
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.5
        easein_quad 6.0 zoom 0.4
        # xanchor 0.0 yanchor 0.0
    with fade

    play sound "audio/sfx/door_old_open03.ogg"

    p "Buenas noches."

    scene night03_bg street_pedrera_corridorclosed
    with fade

    n "Sin mirar atrás, atraviesas el portal del piso"

    scene night03_bg street_pedrera_elevator
    with fade

    n "y sin esperar ese extraño y antiguo ascensor,"

    scene night03_bg street_pedrera_entrance
    with fade

    n "decides bajar por la escalinata espiral hasta llegar a la calle."

    scene night03_bg street_pedrera_door
    with fade
    pause 0.2
    scene night03_bg street_pedrera_close
    with Dissolve(0.5)
    pause 0.2

    scene night03_bg street_pedrera_far
    with fade

    n "Mientras estás esperando el taxi,"

    show didacfbodycloth_whole new_naked:
        dfbody_atright
    # show didacfbodybelow naked:
    #     dfbody_atright
    show didacfbodycloth_below_pants:
        dfbody_atright
    # show didacfbodytop naked:
    #     dfbody_atright
    show didacfbodycloth_top_maleshirt:
        dfbody_atright
    show didacfhandl hip_naked:
        dfbody_atright
    show didacfhandr leg_maleshirt:
        dfbody_atright
    show didacf_blush 00:
        dfexpressions_atright
    show didacf_eyes 02:
        dfexpressions_atright
    show didacf_pupils front02:
        dfexpressions_atright
    show didacf_eyebrows surprisex01:
        dfexpressions_atright
    show didacfbodytop_hair_new:
        dfbody_atright
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows sadx03
    with dissolve

    n "aparece Dídac por detrás con la misma ropa masculina del primer día."

    show didacf_mouth sadbiting_Silentx03
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    with dissolve

    n "Os cruzáis por un instante la mirada, tienes la sensación que quiere decir algo,"

    show didacf_mouth sad_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows sadx03
    with dissolve

    n "pero al ver tu expresión, prefiere optar por el silencio."

    ###

label afternight05_DidacEnd_AtHome:

    scene afternight03_bg entrance_lightoff
    with fade

    pause 0.2

    scene afternight03_bg entrance_lighton
    with dissolve

    #ono "Clink"

    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with dissolve

    n "Eres el primero en entrar al piso y dejar las llaves en su lugar."

    p "Voy a tomarme una ducha."

    show didacfbodycloth_whole new_naked:
        dfbody_atright_closex2
    show didacfbodycloth_below_pants:
        dfbody_atright_closex2
    show didacfbodycloth_top_maleshirt:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandr leg_maleshirt:
        dfbody_atright_closex2
    show didacf_blush 00:
        dfexpressions_atright_closex2
    show didacf_eyes 02:
        dfexpressions_atright_closex2
    show didacf_pupils front02:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair_new:
        dfbody_atright_closex2
    show didacf_mouth sad_Silentx04:
        dfexpressions_atright_closex2

    show didacf_mouth sad_Talkingx01
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows sadx01
    with dissolve

    d "Euh..."

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils front05
    show didacf_eyebrows sadx03
    with dissolve

    menu:

        pt "Joder... ¿En serio? ¡¿Ahora tiene ganas de follar?!"

        "No. No pienso hacer nada contigo.":
            call p_Help

            $pl.ch_pts("dp",-1)

            show didacf_mouth sadbiting_Silentx01
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows surprisex01
            with dissolve

            p "Ni ahora en la ducha,"

            extend " ni después."

        "Ahora no Dídac." if DidacPregnant:
            call p_Help

            #$pl.ch_pts("dp",-1)

            show didacf_mouth sadbiting_Silentx03
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows normal
            with dissolve

            p "No estoy de humor."

            show didacf_mouth sad_Silentx04
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils front05
            show didacf_eyebrows sadx02
            with dissolve

            d "..."

            show didacf_mouth sad_Talkingx02
            $ dteye = 8
            call didac_exp_tears_tears
            show didacf_pupils front08
            show didacf_eyebrows sadx01
            with dissolve

            d "Lo-"

            extend "lo entiendo..."

        "No hagamos tonterías Dídac, es demasiado arriesgado." if DidacPregnant == False:
            call p_Help

            show didacf_mouth sadbiting_Silentx04
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils front03
            show didacf_eyebrows sadx01
            with dissolve

            d "..."

    if DidacPregnant:

        show didacf_mouth sadbiting_Silentx03
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils front05
        show didacf_eyebrows sadx02
        with dissolve

        p "Teniendo en cuenta que a partir de ahora vas a ser una mujer,"

        show didacf_mouth sad_Silentx04
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx01
        with dissolve

        p "tendrás que acostumbrarte a tu nueva vida."

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 8
        call didac_exp_tears_tears
        show didacf_pupils front08
        show didacf_eyebrows sadx01
        with dissolve

        d "..."

        show didacf_mouth sad_Talkingx06
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows sadx02
        with dissolve

        d "¿Estás seguro que es buena idea que sigamos viviendo aquí?"

        show didacf_mouth sad_Talkingx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows sadx01
        with dissolve

        d "¿No deberíamos ir a vivir a otro sitio?"

        show didacf_mouth sad_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows sadx02
        with dissolve

        p "..."

        show didacf_mouth sad_Silentx03
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils front01
        show didacf_eyebrows normal
        with dissolve

        p "Tengo la extraña sensación de que por mucho que intentemos escondernos,"

        show didacf_mouth sad_Silentx04
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows suspiciousx01
        with dissolve

        p "nos acabaría encontrando igualmente."

        show didacf_mouth sad_Talkingx003
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows suspiciousx01
        with dissolve

        d "¿Te refieres a...?"

        show didacf_mouth sad_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows serious
        with dissolve

        p "Sí."

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows serious
        with dissolve

        p "Si quiere dar con nosotros,"

        extend " ya sabe dónde estamos."

        show didacf_mouth sad_Silentx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows sadx01
        with dissolve

        p "Si nos largamos e intentamos escondernos,"

        show didacf_mouth sad_Silentx06
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows sadx02
        with dissolve

        p "solo sería cuestión de tiempo que nos acabara encontrando de nuevo."

        show didacf_mouth sad_Silentx03
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils right03
        show didacf_eyebrows sadx03
        with dissolve

        p "Si [neusname] no ha sido capaz de esconderse,"

        show didacf_mouth sadbiting_Silentx03
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils front04
        show didacf_eyebrows sadx03
        with dissolve

        p "mucho menos lo vamos a lograr nosotros."

        if neusname == "Elur":

            show didacf_mouth sad_Talkingx06
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils front03
            show didacf_eyebrows serious
            with dissolve

            d "[neusname] es la morenita con gafas,"

            extend " ¿no?"

            show didacf_mouth sad_Silentx05
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils front04
            show didacf_eyebrows sadx01
            with dissolve

            p "Así es."

            show didacf_mouth sad_Silentx04
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils front04
            show didacf_eyebrows sadx01
            with dissolve

            d "Hmm..."

        else:

            show didacf_mouth sad_Silentx04
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils front04
            show didacf_eyebrows sadx01
            with dissolve

            d "..."

    else:

        show didacf_mouth sad_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils front01
        show didacf_eyebrows surprisex01
        with dissolve

        p "Lo más probable es que mañana vuelvas a tu forma original,"

        show didacf_mouth sad_Silentx04
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows serious
        with dissolve

        p "así que sería estúpido hacer alguna gilipollez ahora."

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils front03
        show didacf_eyebrows sadx01
        with dissolve

        p "¿Me explico?"

        show didacf_mouth sad_Talkingx02
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils right04
        show didacf_eyebrows sadx02
        with dissolve

        d "Sí-"

        extend "sí..."

        show didacf_mouth sadbiting_Silentx05
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils right05
        show didacf_eyebrows sadx03
        with dissolve

        p "Bien."

    show didacf_mouth sad_Talkingx04
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    with dissolve

    d "¿No tienes hambre?"

    show didacf_mouth sad_Silentx04
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows sadx02
    with dissolve

    p "He perdido el apetito."

    show didacf_mouth sad_Talkingx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows normal
    with dissolve

    scene afternight03_bg hallway_dark
    with fade

    pause 0.2

    scene afternight03_bg hallway_dooropen
    with dissolve

    pause 0.2

    scene afternight03_bg shower
    with fade

    n "Sin esperar su dubitativa respuesta, te diriges al baño y cierras la puerta con baldosa."

    ##

    if DidacPregnant:

        scene beds_night_lightOff_blindUp_DemptyMCempty
        show beds_D03b_night_lightOff_blindUp
        with fade

    else:

        scene beds_night_lightOff_blindUp_Dbusy02MCempty
        show beds_D02_night_lightOff_blindUp
        with fade

    n "Al salir del baño y volver a la habitación,"

    if DidacPregnant:

        n "te encuentras a Dídac desnuda sobre la cama."

    else:

        n "te encuentras a Dídac en la cama cubierto por sus sábanas."

    pt "Lo más probable es que la ducha la necesitara más él que yo."

    pt "Pero bueno,"

    extend " supongo que también estará algo cansado."

    scene black
    with fade

    n "Decides ponerte en la cama y reunirte con el sueño."


    ###

    # DAY 06

    ##Lunes

    window hide dissolve
    pause
    
    $ renpy.notify("Day 06")
    $ pdaytime = "06morning"
    $ pday_day = 6

    n "Igual que los días anteriores,"

    scene morning04_bg bedroom_neus_a # Bitch
    show light 01:
        light01_rightside_position

    show white:
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light_screen_01:
        light_screen_01_position

    n "el cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."

    show morning04_bg bedroom_neus_b
    with dissolve

    show morning04_bg bedroom_neus_c
    with Dissolve(1.0)
    
    n "Pero hay otro sonido familiar que también te llama la atención."

    if DidacPregnant:

        jump morning06_DidacBeingWoman

        scene day05
        with fade

    else:

        jump morning06_DidacBecomingMan

label morning06_DidacBeingWoman:

    d "Mmmfhhmm..."

    # scene morning04_bedroom_DMast_move_02: # When Didac Is Facing you.
    #     #xpos -0.0 ypos -3.25 zoom 1.3 #inicio
    #     xanchor 0.0 yanchor 2.0 zoom 1.3 # Inicio?
    #     easein_quad 30.0 xanchor 0.7 yanchor 1.6 zoom 0.7 #Middle image
    # show light 01:
    #     light01_rightside_position
    # show light_screen_01:
    #     light_screen_01_position
    # with fade

    pt "Puto Dídac..."

    pt "¿Tienes que masturbarte cada jodida mañana?"

    if pl.dp > 50: # NOT FINISHED # acutally it should be if she's happy or horny, not if you just impregnated her.

        jump morning06_DidacBeingWoman_Horny

    else:

        pass

        call WIP

        # NOT FINISHED

        jump endupdate

label morning06_DidacBeingWoman_Horny:

    d "¿Vas a tardar mucho en apuntarte?"

    p "..."

    d "Venga va,"

    extend " no te hagas el digno."

    d "Si tienes la polla más dura que ayer y todo."

    pt "Puto Dídac..."

    d "Ya oíste lo que dijo ayer la bajita gafotas,"

    d "solo tu esperma puede calmarme."

    if DidacMCPregnant:

        d "Y en el fondo es por tu esperma que no puedo volver a ser el que era."

        p "Tendrás morro."

        p "Fuiste tú quien..."

        d "*Bla-bla-bla...*"

    elif DidacOKUPregnant:

        p "Si no te hubieras dejado follar por ese Yonki de..."

    else:

        aj "Error 126484"

    d "Voy cachonda [protname]."

    d "¿Me vas a follar,"

    extend " o me vas a dejar con las ganas?"

    p "..."

    # Te recuerdo que esta semana antes de las clases tengo entreno con los muchachos. ## Something to take in mind!! # Not finished

    #########################################################

    if config.version < "00.99.99": # For Future.
        call endupdatescript
    
    #######################################################

    menu:

        pt "Se acabaron las mañanas tranquilas..."

        "Estás hecha una jodida ninfómana.":

            call p_Help

            $pl.ch_pts("np", 2)

            jump morning06_DidacBeingWoman_HavingSex

        "Ahora no tengo ganas.":

            call p_Help

            $pl.ch_pts("np", 2)

            # NOT FINISHED

            jump endupdate

        "Tendríamos que hablar.":

            call p_Help

            $pl.ch_pts("np", 2)

            # NOT FINISHED

            jump endupdate

label morning06_DidacBeingWoman_HavingSex:

    d "Empiezas a entenderlo."

    d "¿Estás seguro que no quieres que me ponga encima?"

    d "¿O prefieres tenerme a cuatro patas?"

    p "..."

    # NOT FINISHED... should I change anything else?

    menu:

        "Ponerla a cuatro patas.":

            call p_Help

        "Ponerte encima de ella.":

            call p_Help

    d "Ahora fóllame y calla."

    d "Hmmm..."

    d "¿Esto es lo más rápido que puedes ir?"

    p "Como me provoques así,"

    extend " al final te voy a destrozar."

    d "¿Y quien te lo impide?"

    extend " Nenaza."

    menu:

        "<Meterle caña>":

            call p_Help

            d "¡¡DIOS!!"

            d "¡La madre que te parió!"

            d "Duele..."

            p "Pues ahora te jodes."

            d "¡Joder!"

            d "¡Pero como me pone!"

            pt "Definitivamente es sadomasoquista..."

        "<No caer en sus provocaciones>":

            call p_Help

            p "Siempre te me estás quejando de que la tengo tan grande,"

            p "¿No crees que provocarme es una mala idea?"

            d "..."

            d "Nenaza..."

            p "A veces pareces un niño."

            d "Que me hubiera quejado un poco antes,"

            d "no quita que me enloquezca tenerla bien dentro..."

            p "Ah..."

            p "y no te importa una mierda que te parta en dos"

            p "y que sufras un dolor de mil narices."

            d "..."

            d "Bueno..."

            p "Que no Dídac,"

            p "que no pienso volver a ser tan bruto..."

            d "Gallina."

            p "..."

            p "Vete al..."


    p "Ughh..."

    d "Te vas a correr pronto,"

    extend " ¿verdad?"

    pt "Una cosa es que me conozca desde hace años,"

    pt "la otra es que sepa tan bien cuando estoy a punto de correrme..."

    pt "¿Será que ya me observaba de esta manera antes de que se convirtiera en mujer?"

    d "¡Córrete dentro capullo!"

    d "Al fin y al cabo,"

    extend " ahora ya da igual."

    p "No hace falta que me lo repitas."

    p "¡Ugh...!"

    d "¡AAAHHHhgg!"

    d "Mmmhffhmm..."

    d "¡Dios!..."

    d "Me-"

    extend "me encanta..."

    p "Dídac,"

    extend " ¿Estás bien?"

    d "Seehh..."

    p "..."

    pt "Será mejor dejarlo descansar un poco."

label morning06_DidacBeingWoman_AfterSex:

    $ DidacStillMemory = True

    n "Te diriges al baño para tomarte una ducha antes de ir a clase."

    ##

    p "¿Se puede saber que haces vestida así?"

    d "Me alegra ver que por fin me tratas como a una dama."

    p "Siempre he tratado a las mujeres con respeto,"

    extend " incluso las que son como tú."

    d "¿Es algún tipo de indirecta?"

    p "Creo que es bastante directa."

    d "Pfft..."

    call morning06_TVKid

        # ptv "Después de cuatro días sin haber ninguna noticia de la desaparición del pequeño Edward,"
        # ptv "los padres han decidido aumentar la recompensa por..."
        # p "Apaga el televisor."
        # d "¿Este es el niño que...?"
        # p "Dídac."
        # d "Vale, vale..."
        # p "Prefiero no volver a hablar nunca más sobre este tema."
        # p "¿De acuerdo?"
        # d "Como quieras..."

    d "Bueno..."

    d "¿Estás listo para irnos?"

    p "¿A dónde tienes pensado ir?"

    d "¡Coño!"

    d "¡A clase!"

    d "¡¿A dónde quieres que vaya?!"

    p "¿Y qué le vas a decir exactamente al profesor,"

    p "cuando este te pregunte?:"

    p "¿Quien coño eres?"

    d "..."

    d "Euhh..."

    d "Que me llamo {b}Daphne{/b}?"

    p "¡¿Dafne?!"

    d "¿No te gusta?"

    p "..."

    p "Dídac,"

    extend " el nombre es lo de menos."

    p "La pregunta es qué coño hace una alumna a prácticamente una semana o dos de terminar el curso,"

    p "¡en una clase dónde nunca ha asistido!"

    p "Eso sin hablar de que no podrás entrar ahí por la buenas sin que sepan quien eres."

    p "Tendrías que inscribirte de nuevo."

    d "¡Pero si vamos por el tercer curso!"

    p "También podrías empezarlo de nuevo,"

    extend " tampoco es que las clases de dibujo y anatomía te fueran tan bien."

    d "Serás capullo."

    p "Venga va,"

    extend " no te lo tomes así."

    p "Piensa en que es una nueva oportunidad."

    p "Aunque tampoco sé lo fácil o difícil que te resultará inscribirte en un curso,"

    p "sin poder justificar tu nacionalidad..."

    d "Como si no hubiera suficientes inmigrantes ilegales en este país,"

    d "tampoco creo que sea tan complicado."

    p "No creo que tengas ni la más remota idea de lo jodida que tiene que ser su situación..."

    p "Pero aparte,"

    extend " todos tienen al menos un país de origen,"

    p "¿de dónde demonios les dirás que vienes?"

    d "Pues les diré que una bruja enana y gafotas me transformó en mujer por acusarme de intentar violarla,"

    d "y que luego mi compañero de piso me folló sin condón dejándome una sorpresa por el camino,"

    d "así que ahora me toca ser mujer de por vida."

    p "¡No hagas bromas con esto!"

    d "Oh,"

    extend " vamos..."

    d "Un poco de humor no te haría ningún daño."

    p "Te estoy hablando en serio Dídac."

    d "Ya lo sé,"

    extend " ya lo sé..."

    d "No puedo decírselo a nadie,"

    extend " o mi vida correría peligro."

    p "..."

    d "Pero bien que la rubia sabía sobre todo este tema,"

    extend " ¿No?"

    p "Sí..."

    d "Entonces tampoco sería imposible que alguien más lo pudiera saber."

    p "¿Pondrías tu vida en riesgo para averiguarlo?"

    d "..."

    d "Supongo que no."

    d "Pero al menos mis padres podrían saber que no he muerto o desaparecido..."

    extend " ¿No?"

    p "..."

    p "Supongo que ellos serían capaces de guardar el secreto,"

    p "si saben lo que hay en juego."

    d "Entonces sí podría contárselo a alguien..."

    p "¡Se trata de usar un poco la cabeza y ser un poco responsable!"

    p "Aunque sea por una vez en tu jodida vida."

    d "..."

    d "Que de tanto en cuanto haga broma,"

    d "no significa que no sea alguien responsable."

    pt "Ya..."

    p "Por lo menos has pensando en un nombre."

    p "Un tanto raro,"

    extend " pero algo es algo."

    d "Tampoco es que Dídac fuera un nombre muy común."

    p "Al menos era Catalán."

    p "¿No lo echarás de menos?"

    d "No si me lo susurras al oído mientras me penetras hasta el fondo."

    p "..."

    d "Mira que es fácil ponértela dura."

    p "Como si a ti te resultara difícil mojarte las bragas..."

    d "..."

    p "Bueno,"

    extend " en cualquier caso,"

    p "tengo que largarme,"

    extend " o realmente llegaré tarde."

    d "¿Y yo qué hago?"

    p "Pues yo que sé."

    p "Mírate cursos gratis por {i}youtube{/i} o internet,"

    p "qué es lo que te gustaría hacer,"

    p "intenta buscar trabajo online,"

    p "quizás algo en negro para que no tengas que declarar quien eres,"

    p "o vuelve a las clases de arte,"

    p "a ver si volviendo a empezar de cero aprendes a hacerlo mejor que hasta ahora."

    d "Serás capullo."

    p "Yo tengo que largarme."

    n "Te alejas del comedor hasta llegar a la entrada dónde recoges las llaves."

    p "¡Se responsable!"

    d "¡Que te follen!"

    n "Te responde gritando desde la sala de estar."

    p "¡Ya lo harás tú cuando vuelva!"

    d "¡Quizás me vaya a comprar un polla de goma para follarte de verdad!"

    p "¡Entonces te follara tu madre!"

    d "¡Capullo!"

    p "¡Cachonda mental!"

    n "Finalmente cierras la puerta de la entrada al piso,"

    n "porque tampoco es plan de que el vecindario entero se entere de lo idiotas que sois de buena mañana."

    call morning06_AtSchool

        # p "..."
        # n "Un Lunes normal como cualquier otro, a escasos días de las vacaciones de verano."
        # n "Por mucho que rebuscaras entre los pasillos y en ambos baños,"
        # (...)
        # n "Como si jamás hubieran existido."
        # n "Como si su existencia no fuera más que un extraño y largo sueño que solo tú eres capaz de recordar."

    jump aftermorning06_DidacWoman

label aftermorning06_DidacWoman:

    n "Después de las clases y de entrenar a uno de los equipos fútbol juveniles del barrio en que vives,"

    n "te diriges al piso lo más pronto que te es posible."

    p "¡Joder Dídac!"

    p "¡¿Otra vez has ido de compras?!"

    n "Observas el comedor completamente desordenado y lleno de piezas de ropa por todos lados."

    p "Al menos podrías ser un poco más ordenado."

    d "¿No te gusta lo que ves?"

    p "..."

    p "No me cambies de tema."

    d "Respóndeme la pregunta."

    p "..."

    menu:

        "No negaré que estás provocativa.":
            call p_Help

            $pl.ch_pts("dp",1)

            d "Así me gusta..."

        "Mehh, tampoco te queda tan bien.":
            call p_Help

            $pl.ch_pts("dp",-3)

            d "..."

            d "¡¿Y por qué coño se te está poniendo dura?!"

            p "Porque soy humano."

            d "¡¿Qué clase de respuesta es esa?!"

            p "Pues que mi polla a veces se pone tiesa cuando veo a dos perros follar,"

            p "pero eso no significa que me vaya a unir a ellos."

            p "La polla va a su bola."

            p "Como si no lo supieras..."

            d "¡Serás imbécil!"

            d "¡¿Tanto te cuesta admitir que te pongo cachondo?!"

            p "Soy sincero."

            p "¿O acaso prefieres que mienta?"

            d "Podrías decir que prefieres otro tipo de lencería,"

            d "o ser algo más delicado."

            p "¿Más delicado?"

            p "¿En qué demonios te has convertido?"

            p "¿Te pones así porque alguien te dice que no le gusta lo que llevas?"

            p "¿Acaso te has vuelto una \"ofendidita\" de manual?"

            d "¡Los demás me importan un carajo!"

            p "¿Entonces te importa mi opinión?"

            d "¡Cállate imbécil!"

        "Me gustas más con otro tipo de lencería.":
            call p_Help

            $pl.ch_pts("dp",-1)

            d "..."

            d "Es tan fácil como decir..."

            d "{i}Sí,"

            extend " Dídac...{/i}"

            d "{i}me pone muy caliente la lencería que llevas.{/i}"

            d "¡Joder!"

            d "Si hasta el rabo se te está poniendo tieso de solo verme."

            p "..."

            p "eso no quita que me gustes más con otro tipo de lencería."

            d "Tssk..."

            d "Mira que eres capullo..."

        "La verdad es que se me está poniendo bastante dura con solo verte...":
            call p_Help

            $pl.ch_pts("dp",3)

            d "Hmmm..."

            d "Así me gusta..."


    d "Ahora quítate la ropa que ya no aguanto más."

    p "¡Coño!"

    p "¡Que acabo de llegar!"

    d "¡Ya descansarás después!"

    p "¡Déjame tomarme una ducha primero al menos!"

    d "Tampoco apestas tanto..."

    p "¡Vengo de estar entrenando a los chavales!"

    p "¡Dame un jodido respiro!"

    d "Me gusta cuando hueles a sudor..."

    p "..."

    d "¡Vale!"

    d "Vete a duchar,"

    d "¡pero luego no te me escapas!"

    n "Con la mirada atravesada de tu nueva compañera de piso,"

    n "te diriges al baño para tomarte una relajante ducha."

    pt "Dios..."

    pt "¿Va a ser así todos los días?"

    pt "No sé yo si podré aguantar el ritmo..."

    n "Los días se suceden uno tras otro,"

    n "a pesar del cambio sufrido por Dídac,"

    n "su personalidad apenas ha cambiado lo más mínimo,"

    n "lo que sí ha cambiado es la irritabilidad que sufre ahora tu pollón,"

    n "teniendo que satisfacer los deseos insaciables de la ninfómana que vive contigo."

    jump EndingDidac

        # n "Aún así, no puedes evitar imaginar lo qué debió ocurrirle al final a Meritxell;"
        # n "Tampoco te tranquiliza lo más mínimo que el \"Papa-cabra\" sepa dónde vives,"
        # n "con la incertidumbre de si algún día vendrá a reclamarte algo, o por algo peor."
        # n "Sin olvidar esa extraña criatura que proclamó ser tu madre en la {i}Pedrera{/i},"
        # n "cuya parte de la ciudad evitas transitar a toda costa, incluso cuando te llevan en taxi."
        # n "Y esa aparentemente inocente morenita de ojos verdes con gafas,"
        # n "a pesar de todo lo ocurrido, de los secretos sangrientos confesados,"
        # n "de haber sacrificado a sangre fría por beneficio propio a un menor completamente inocente;"
        # n "tienes la sensación de que quizás,"
        # extend " podrías haber hecho las cosas distintas con ella."
        # n "Quizas..."
        # aj "FIN DEL JUEGO z001"


label morning06_TVKid:

    ptv "Después de varios días sin haber ninguna noticia de la desaparición del pequeño Edward,"

    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0

    scene bg tv_kid_comp:
        subpixel True
        truecenter
        zoom 1.5 xpos 1.5 ypos 1.1
        easein_quad 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    ptv "los padres han decidido aumentar la recompensa por..."

    p "Apaga el televisor."

    if DidacStillMemory:

        d "¿Este es el niño que...?"

        p "Dídac."

    else:

        d "¿Es que conocías al niño este?"

        p "Simplemente te pido que apagues el televisor,"

        p "por favor."


    show bg tv_background_off
    with dissolve

    d "Vale,"

    extend " vale..."

    scene morning04_bg_livingroom_others_morning

    if DidacPregnant:

        # NOT FINISHED

        call WIP

        pass

    else:

        show D_damagedIndifferent_body at right
        show D_damagedIndifferent_eyes front01 at right
        show D_damagedIndifferent_mouth sad_Silent at right
        with fade

    if DidacStillMemory:

        p "Prefiero no volver a hablar nunca más sobre este tema."

        p "¿De acuerdo?"

        show D_damagedIndifferent_eyes left01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve

        d "Como quieras..."

        show D_damagedIndifferent_eyes left01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve


    else:

        show D_damagedIndifferent_eyes front01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve

        d "No sabía que te afectaran tanto este tipo de noticias."

        show D_damagedIndifferent_eyes front01
        show D_damagedIndifferent_mouth sad_Silent
        with dissolve

        p "Quizás no me conoces tan bien como crees."

        show D_damagedIndifferent_eyes left01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve

        d "Joder..."

        show D_damagedIndifferent_eyes front01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve

        d "Tranquilo,"

        show D_damagedIndifferent_eyes left01
        show D_damagedIndifferent_mouth sad_Talking
        with dissolve

        d "tampoco hace falta ponerse así."

        show D_damagedIndifferent_eyes left01
        show D_damagedIndifferent_mouth sad_Silent
        with dissolve

        pt "Está claro que no se acuerda de nada."

    show D_damagedIndifferent_mouth sad_Silent
    with dissolve

    return

label morning06_DidacBecomingMan:

    scene didac_bed_bed over
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    d "¡Uggh...!"

    n "Al acercarte a Dídac, observas como vuelve a sudar del mismo modo que lo hizo hace dos días."

    pt "Supongo que eso significa que pronto volverá a ser el de antes."

    p "Dídac,"

    show didac_bed_d_eyes 06
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "¿Te encuentras bien?"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿A ti te parece que me encuentre bien?!"

    show didac_bed_d_mouth sad_Silentx04
    with dissolve

    pt "Supongo que ha sido una pregunta estúpida."

    scene night01_bg dinner
    with fade

    n "Regresas de la cocina con la caja de aspirinas y le das un vaso de agua para que se lo pueda tomar."

    scene 01_aspiring_bg
    show 01_aspirin:
        truecenter
        zoom 0.6
        ease 2.0 zoom 0.5
    with fade

    p "Espero que esto te ayude."

    scene didac_bed_bed over
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    d "Yo también lo espero."

    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_mouth sad_Silentx04
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Es el mismo dolor que sentí antes de transformarme en una mujer,"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¿significa eso que voy a volver a ser el de antes?"

    show didac_bed_d_eyes 06
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_mouth sad_Silentx04
    with dissolve

    p "Es posible."

    show didac_bed_d_eyes 07
    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_mouth sad_Silentx05
    with hpunch

    d "¡Ughh...!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Bueno..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "supongo que entonces este dolor vale la pena entonces..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "Eso espero."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¿Se puede saber qué estás haciendo aquí?"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "¿Euh...?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Vas a llegar tarde a clase imbécil!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Pe-"

    extend "pero..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Ni peros ni hostias!"

    show didac_bed_d_mouth sad_Talkingx02
    with dissolve

    d "¡No pienso tener un búho observándome a todas horas mientras estoy así!"

    show didac_bed_d_mouth sad_Talkingx04
    with dissolve

    d "¡Lárgate!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Si me pasa algo o necesito tu ayuda,"

    d "ya te llamaré al móvil."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "¿Estás seguro?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Que te largues coño!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Hmm..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Está bien."

    scene beds_morning_lightOff_blindUp_Dbusy02MCmessy
    show beds_D02b
    with fade

    n "Te diriges al armario dónde te vistes y te preparas para asistir a la clase de primera hora de la mañana."

    pt "No negaré que prefería quedarme para vigilar la evolución de Dídac,"

    pt "pero confieso,"

    extend " que también tengo cierto nerviosismo de ir a clase"

    pt "y encontrarme con la rubia y la bruja..."

    pt "Pero supongo que..."

    d "[protname]..."

    scene didac_bed_bed over
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    p "¿Hmm...?"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Gracias por todo."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with hpunch

    d "¡Ugghh...!"

    p "¡Dí-"

    extend "dídac!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Que te largues imbécil!"

    d "¡O al final me levantaré y te echare a patadas!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    pt "Su cuerpo se habrá transformado,"

    pt "pero desde luego su personalidad no ha cambiado en lo más mínimo en todo este tiempo."

    call morning06_AtSchool

    jump aftermorning06_DidacMan

label morning06_AtSchool:

    scene morning02_bg schoolwall
    with fade

    p "..."

    if pday_day == 8:

        n "Un Miércoles normal, como cualquier otro,"

    elif pday_day == 7:

        n "Un Martes normal, como cualquier otro,"

    else:

        n "Un Lunes normal como cualquier otro,"

    n "a escasos días de las vacaciones de verano."

    n "Por mucho que rebuscaras entre los pasillos y en ambos baños,"

    n "no había ningún rastro de [neusname] o Meritxell."

    n "Pero lo más curioso, fue que no quedó vestigio alguno de su paso por la escuela."

    n "Ni sus nombres, ni la personalidad, ni el aspecto,"

    n "ni tan siquiera los enormes pechos de la rubia de Meritxell,"

    n "eran recordados lo más mínimo por ningún alumno, ni tan siquiera por el equipo docente."

    n "Las piezas artísticas de los alumnos que decoran las paredes de los pasillos realizados por ellas,"

    n "habían sido sustituidas por la de otros estudiantes,"

    n "las anotaciones privadas en los diarios personales,"

    n "los escritos de amor eterno grabados en la madera de los pupitres,"

    n "las fotografías realizadas con las cámaras del móvil,"

    n "incluso las que aparecían por detrás por casualidad,"

    n "sin mencionar las conversaciones privadas de {i}WhatsApp{/i},"

    n "hablando de lo \"buenorra\" y otras lindezas que ofrece el vocabulario español,"

    n "sobre el atractivo físico de la rubia de clase,"

    n "Todo ello había sido borrado, tachado o sustituido."

    n "Como si jamás hubieran existido."

    n "Como si su existencia no fuera más que un extraño y largo sueño que solo tú eres capaz de recordar."

    return

    ##

label aftermorning06_DidacMan:

    scene bg an04_flat_outside
    with fade

    n "Después de las clases y de entrenar a uno de los equipos fútbol juveniles del barrio en que vives,"

    scene afternight03_bg entrance_lighton
    with fade

    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with dissolve

    n "te diriges al piso lo más pronto que te es posible."

    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 03
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_hair 03
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    p "Dídac..."

    p "¿Estás bien?"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Ughh..."

    n "Observas su cuerpo cubierto de sudor."

    n "Sus voluptuosidades mamarias se han reducido bastante,"

    n "así como su musculatura ha aumentado considerablemente de volumen."

    pt "Parece que está recuperando su forma física anterior."

    menu:

        pt "¿Debería insistirle en que debe tomarse una ducha?"

        "<Decirle que lo mejor es que se tome una ducha>":
            call p_Help

            $pl.ch_pts("dp",1)

            jump aftermorning06_DidacMan_Shower

        "<Quizás no es una buena idea>":
            call p_Help

            n "Decides que lo más sensato es no tentar a la suerte,"

            n "cuando apenas quedan unas horas para que vuelva a ser el de siempre."

            n "Lo que sí haces, es pedirle que se levante un poco de la cama para poderle cambiar las sábanas."

            jump aftermorning06_DidacMan_Routine
                # n "Regresas a tu rutina diaria,"
                # n "comer, ir al gimnasio y más al atardecer, entrenar al otro equipo de juveniles."
                # n "Por la noche vuelves a ver cómo está tu compañero de piso."
                # pt "Parece que finalmente está recuperando su forma masculina."
                # n "Al día siguiente por la mañana, revisas de nuevo su estado físico."
                # pt "Parece que vuelve a ser el de siempre."


label aftermorning06_DidacMan_Shower:

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    n "Aún y a regañadientes,"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    n "consigues convencerlo de tomarse una ducha mientras le limpias la cama."

    scene beds_midday_lightOff_blindUp_DmessyMCmessy
    with fade

    n "Aunque sorprendentemente, esta vez no te reclama la ayuda que te solicitó la última vez."

    pt "Es extraño,"

    extend " solamente oigo el ruido del agua de la ducha..."

    scene beds_midday_lightOff_blindUp_DemptyMCempty
    with Dissolve(1.0)

    pt "¿Le habrá ocurrido algo?"

    scene afternoon02_beforeshower_bg
    with fade

    p "¿Dídac?"

    p "¿Estás bien?"

    scene d_showerin_compilation:
        subpixel True
        zoom 5.0
        xanchor 0.25 yanchor 0.6
        ease_quad 5.0 xanchor 0.4 yanchor 0.2
    with fade

    p "Hace rato que no oigo..."

    scene d_showerin_bg:
        d_showerin_base_close_pos
    show d_showerin_body:
        d_showerin_base_close_pos
    #show d_showerin_bg_prove:
        #d_showerin_base_close_pos
    show d_showerin_blush 01:
        d_showerin_expressions_close_pos
    show d_showerin_mouth sadx2_Talking:
        d_showerin_expressions_close_pos
    show d_showerin_eyes 03:
        d_showerin_expressions_close_pos
    show d_showerin_pupils front03:
        d_showerin_expressions_close_pos
    show d_showerin_eyebrows angryx2:
        d_showerin_expressions_close_pos
    show d_showerin_hair:
        d_showerin_expressions_close_pos
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    show night05_Cemetery_smoke_comp
    #show fog_01:
        ##additive 1.0
        #afternoon02_bg_showering_smoke_move
    show d_showerin_doors:
        d_showerin_base_close_pos
    with dissolve

    d "¡Tío!"

    d "¡Que estoy en pelotas!"

    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve

    p "¡¿Qué cojones haces sentado en el plato de ducha?!"

    show d_showerin_eyes 03
    show d_showerin_pupils right03
    show d_showerin_eyebrows sad
    show d_showerin_mouth sad_Talking
    with dissolve

    d "¡Ey!"

    d "¡Me las apaño!"

    d "¡¿Vale?!"

    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve

    scene d_showerin_compilation:
        subpixel True
        truecenter
        zoom 5.0
        xpos 0.5 ypos 1.5 #face
        ease 7.0 xpos 0.3 ypos -0.63 # penis
    with fade

    n "Al dirigir tu mirada hacia abajo, te percatas de que,"

    n "aunque de forma diminuta, ha vuelto a recuperar su antiguo miembro viril."

    p "¿Estás seguro que no quieres mi ayuda?"

    d "¿Para que me toquetees como hiciste la última vez?"

    scene d_showerin_bg:
        d_showerin_base_close_pos
    show d_showerin_body:
        d_showerin_base_close_pos
    #show d_showerin_bg_prove:
        #d_showerin_base_close_pos
    show d_showerin_blush 01:
        d_showerin_expressions_close_pos
    show d_showerin_mouth sadx2_Talking:
        d_showerin_expressions_close_pos
    show d_showerin_eyes 03:
        d_showerin_expressions_close_pos
    show d_showerin_pupils front03:
        d_showerin_expressions_close_pos
    show d_showerin_eyebrows angryx2:
        d_showerin_expressions_close_pos
    show d_showerin_hair:
        d_showerin_expressions_close_pos
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    show night05_Cemetery_smoke_comp
    #show fog_01:
        ##additive 1.0
        #afternoon02_bg_showering_smoke_move
    show d_showerin_doors:
        d_showerin_base_close_pos
    with dissolve

    d "¡Que no!"

    d "¡Que paso!"

    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve

    p "Como si te hubieras quejado mucho la última vez..."

    show d_showerin_eyes 02
    show d_showerin_pupils right02
    show d_showerin_eyebrows angryx2
    show d_showerin_mouth sad_Silent
    with dissolve

    d "..."

    show d_showerin_eyes 03
    show d_showerin_pupils front03
    show d_showerin_eyebrows angryx2
    show d_showerin_mouth sad_Talking
    with dissolve

    d "¡Va!"

    d "¡Lárgate de una vez!"

    extend " ¡o llegarás tarde!"

    show d_showerin_eyes 03
    show d_showerin_pupils front03
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve

    p "Vale,"

    extend " vale..."

    scene afternoon02_beforeshower_bg
    with fade

    pt "Quizás está perdiendo la libido que le empujaba a provocarme estos últimos días."

    pt "Supongo que es buena señal."

    ##

label aftermorning06_DidacMan_Routine:

    scene morning02_bg schoolwall
    with fade

    n "Regresas a tu rutina diaria,"

    n "comer, ir al gimnasio, y más al atardecer, entrenar al otro equipo de juveniles."

    scene afternight03_bg entrance_lighton
    with fade

    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with dissolve

    n "Por la noche vuelves a ver cómo está tu compañero de piso."

    scene didac_bed_bed over
    show didac_bed_d_body 02
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_hair 02
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    pt "Parece que finalmente está recuperando su forma masculina."

    scene morning04_bg bedroom_neus_a # Bitch
    show light 01:
        light01_rightside_position
    show white:
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade_long1s

    pause 0.2

label aftermorning06_DidacMan_Routine02:

    
    $ pday_day += 1

    if pday_day == 7:
        $ pdaytime = "07morning"
    else:
        $ pdaytime = "06morning"

    show morning04_bg bedroom_neus_c
    show light 01:
        light01_rightside_position
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade

    $ saturation_tint_level = "default"

    n "Al día siguiente por la mañana,"

    scene didac_bed_bed over
    show didac_bed_d_body 01
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_hair 01
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    show light_screen_01:
        light_screen_01_position
    with fade

    n "revisas de nuevo su estado físico."

    pt "Parece que vuelve a ser el de siempre."

    scene morning04_bg_livingroom_others_morning
    with fade

    n "Esta mañana es capaz de levantarse."

    n "Se toma una ducha rápida,"

    show D_damagedIndifferent_body at right
    show D_damagedIndifferent_eyes front01 at right
    show D_damagedIndifferent_mouth sad_Silent at right
    with dissolve

    n "y aunque apenas tiene fuerzas para mantenerse en pie,"

    n "eres incapaz de convencerle de que se quede en casa reposando un poco más."

    show D_damagedIndifferent_eyes left01
    with dissolve

    call morning06_TVKid

            # ptv "Después de cuatro días sin haber ninguna noticia de la desaparición del pequeño Edward,"
            # ptv "los padres han decidido aumentar la recompensa por..."
            # p "Apaga el televisor."
            # d "¿Este es el niño que...?"
            # p "Dídac."
            # d "Vale, vale..."
            # p "Prefiero no volver a hablar nunca más sobre este tema."
            # p "¿De acuerdo?"
            # d "Como quieras..."
    
    if day06_night_homeDidacMale:
        return

    else:

        jump aftermorning06_DidacMan_Routine03


label aftermorning06_DidacMan_Routine03:

    if not day06_night_homeDidacMale:

        scene morning02_bg schoolwall
        with fade

        show black:
            alpha 0.0
            linear 60.0 alpha 1.0

        n "Al regresar a la escuela, descubres sin demasiada sorpresa,"

        n "que sigue sin haber ninguna señal de ellas."

    scene morning04_bg_livingroom_others_morning # It must be changed for the room, morning, day, night... ?
    show light_screen_01:
        light_screen_01_position
    with fade
    
    n "Pasan los días, luego las semanas, ninguna noticia."

    hide light_screen_01
    with Dissolve(1.0)


    n "En general regresas a tu rutina,"

    show morning04_bg_livingroom_others_night_lightOn:
        alpha 0.0
        easein_quad 5.0 alpha 1.0

    n "Dídac vuelve a ser el de siempre y actúa como si nada de esto hubiera ocurrido,"

    n "de hecho cuando se te ocurre sacar el tema,"

    n "vuelve darte ese rostro de confusión;"

    n "como si no supiera de lo que estás hablando."

    show morning04_bg_livingroom_others_night:
        alpha 0.0
        easein_quad 5.0 alpha 1.0

    n "Decides no indagar demasiado en el tema, para evitar despertar ciertos \"fantasmas\" del pasado."

    n "Aunque esa duda permanece ahí, como una herida que no termina de cicatrizar."

    show black:
        alpha 0.0
        linear 5.0 alpha 1.0
    
    n "Al menos sientes que lo peor ha pasado, con la sensación de que,"

    n "siempre y cuando no vuelvas a meter las narices en estos extraños asuntos,"

    n "nada malo debería ocurrir."

    n "No debería, al menos..."

    scene black
    with fade

    jump EndingDidac

label EndingDidac:

    $ day06_ending_city = "barcelona"

    call day06_ending_window

    n "Aún así, no puedes evitar imaginar lo qué debió ocurrirle al final a Meritxell;"

    n "Tampoco te tranquiliza lo más mínimo que el \"Papa-cabra\" sepa dónde vives,"

    n "con la incertidumbre de si algún día vendrá a reclamarte algo,"

    n "o por algo peor."

    n "Sin olvidar esa extraña criatura que proclamó ser tu madre en la {i}Pedrera{/i},"

    n "cuya parte de la ciudad evitas transitar a toda costa, incluso cuando te llevan en taxi."

    n "Y esa aparentemente inocente morenita de ojos verdes con gafas,"

    n "a pesar de todo lo ocurrido, de los secretos sangrientos confesados,"

    if p_ao_neusLastSecret:

        n "de haberse tragado vivo a un menor completamente inocente;"

    else:

        n "de haber sacrificado a sangre fría por beneficio propio a un menor completamente inocente;"

    n "tienes la sensación de que quizás,"

    n "podrías haber hecho las cosas distintas con ella."

    # scene black
    # with fade_long1s

    if p_ao_neusLastSecret or pl.np < 100:

        n "O quizás no..."

    else:

        n "Quizás..."

    pause

    if day06_night_homeDidacMale:

        aj "FIN DEL JUEGO z003"

    elif DidacPregnant:

        aj "FIN DEL JUEGO z002"

    else:

        aj "FIN DEL JUEGO z001"

    #jump endupdate

    jump gameover

    # Wich one do you sperm? all of them, just Didac, Didac an Txell, the three of them?






    # Sino lo haces por mi, al menos hazlo por ellas.

    # Puedes irte sin ayudar a Txell ni a Neus, si Dídac se puede volver hombre, ya le darás el semen de algún modo por via oral.



    # Neus le tira en cara porque no la ha matado. Madre estaba escondida durante años para protegerle y ahora...

    # Neus se lamente de haber sido usada por su padre para encontrar a su madre, por eos le resultó tan fácil escapar.

    # Dices que es hora de largarse de aquí, pero Neus te detiene. Puesto que en la Pedrera, almenos durante esta noche estáis seguros. Pero una vez fuera, tanto Dídac como Meritxell son balizas y sufrirán la muerte a menos que tengan el esperma de MC en su interior, A Neus también le vendría bien para conseguir más poderes para poder escapar con más comodidad.

    # La fricción de las conversaciones dependerán de los puntos que se tenga con cada una de ellas.

    # Quieres echarle la bronca  Didac por romper el condón y Txell te tira encara que decidieras follartelo incluso usando condón.

    #Neus se mantiene en silencio durante la conversación.

    











    



#     - En la habitación entrará Nana, que MC podrá vislumbrar a duras penas. Esta se acerca a Txell poseída por Padre, mientras Padre sonríe.

#     - Aquí es dónde se revela el verdadero plan de Padre. Hacer salir a madre para volverla a su harén. Si MC lleva el colgar, Madre podrá hablar con él. Le revela que fue ella quien indujo a su hija a sacrificar a ese niño, fue ella quien la condujo hasta ti, fue ella quien deseaba que ambos pudieráis tener una vida feliz y sigue deseándolo, te pide que perdones a Neus, quien desea de corazón cambiar y ser feliz contigo.

#     - Padre desde el suelo sigue riéndose y diciéndole que es un esfuerzo en vano, que del mismo modo que ha recuperado a Madre, tarde o temprano recuperará a su hija y matará al protagonista, es solo cuestión de tiempo, algo de lo que él dispone en abundancia.

#     - Poco después Nana se vuelve cenizas encima de Txell. Hasta que esta recupera el color de sus ojos. Preguntándose dónde está y qué está ocurriendo.

#     - Neus se encuentra desolada llorando la pérdida de su amada madre.

#     -- Después del drama viene el sexo! Vivan los juegos porno que sudan de todo xD.

#     - Neus te implora perdón, copmprende la situación y no te pide que la ames en estas circunstancias, pero al mismo tiempo te pide comprensión, ya que necesita tu semén, no sólo ella, sino también Txell y Dídac para poder sobrevivir y salir con vida de ahí. Tienen de tiempo hasta salir el sol, pues en la Pedrera por el momento están seguros, pero cuando anochezca el día siguiente deben de estar muy lejos de ahí y es el único modo de sobrevivir, incluso de día es si las tres tienen tu esperma en su interior, pues eso las hará casi invisibles a ojo de Padre.

#     - Dependiendo de puntos y acciones, aquí las escenas de sexo pueden tener un aire u otro, Neus puede estas más o menos segura de que la amas si no te has follado a Dídac ni Txell, Txell puede estar en contra de follar contigo, con lo que te correrías en la boca de Neus y estas dos se besarían, puedes dejar o no embarazadas a las tres dependiendo de los puntos, etc.

#     - Una vez hayas tenido tus tres orgasmos, terminas perdiendo el sentido, pues Neus tiene un modo de tener sexo que te deja completamente inútil.

#     - Cuando recuepras los sentidos te encuentras en otro lugar, dependiendo de las acciones previas pueden estar las tres, sólo dos, o sólo Neus. Dídac si estaba embarazada estará sí o sí, pero sino dependerá de si la dejas o no preyñada (a Neus no le gustará demasiado la idea.)

#     - Lejos de padre, fuera de su radar, pero hasta cuando?

    # NIÑO SACRIFICIO.

    # VEGANA


# - Qué sacrificio ha hecho para poder convertir a Dídac en Mujer.

#     - Le cuenta lo del hotel y las 3 puertas, todas las víctimas de Neus, en cómo se convirtió en una de las asesinas más letales de su harén.

#     - Lo que ocurrió en la sagrada familia con el NIÑO.

#     - Porque es VEGANA si luego es una asesina en série.




# Durante el transcuro del viaje en el taxi, la observas mirar en el bolso con el colgate dorado de Ankhj si no te lo ha dado.

# Una vez llegáis a la pedrera, nerviosamente abre el portal y subís rápidamente por las escaleras sin esperar al ascensor.

# Una vez os acercáis al piso, empezáis a escuchar unos gemidos, identificas que es la voz de Dídac.

# Al abrir la puerta oís con más intensidad esos gemidos y los localizáis en la habitación dónde Neus te hizo esa extraña mamada dónde también está la cuna.

# Al entrar en la habitación con las luces encendidas, Observas a Dídac desnuda y con su nuevo cuerpo encima de la cama abierta de piernas, mientras Txell le está practicando un cunnilingus con los ojos rojos.

# El personaje se sorprende a ver a Txell.

# Txell: Por fin habéis llegado, os estábamos esperando.

# - Cosas a revelar, no sé en qué orden.

    
#     - El padre revela si Dídac está o no embarazada por MC o por un extraño.

#     - Neus le hace preguntas a MC sobre este tema (Antes de revelar que es su hermana).

#     - Le comenta si quiere volver a follarse a su compañero o a Txell misma, pues tampoco sería la primera vez. Después de lo que pasó después de la librería.

#     - La infidelidad con Txell si es que ha habido sexo. Como no iba a preferir este par de melones en lugar de ese pecho plano, le pregunta su padre.

#     - Neus ha estado utilizando a MC, es su hermana, necesita su esperma para poder esconderse definitivamente de su padre, Txell está poseída por Padre. Este puede ir saltando de cuerpo, excepto en el MC.

#     - El hecho de que Dídac se convirtiera en Mujer fue un plan de Neus cómo último recurso para romper el hielo con MC.

#     - Qué sacrificio ha hecho para poder convertir a Dídac en Mujer.

#     - Le cuenta lo del hotel y las 3 puertas, todas las víctimas de Neus, en cómo se convirtió en una de las asesinas más letales de su harén.

#     - Lo que ocurrió en la sagrada familia con el NIÑO.

#     - Porque es VEGANA si luego es una asesina en série.

#     - Porqué tuvo que matar a un niño, si lo único que tenía que hacer es pedirle una cita. (plan de la madre) [Si te has follado a otras, te lo tira en cara diciendo que ni así podías sentirte interesada con ella, cómo iba a sentirse segura pidiéndotelo.]

#     - El padre le cuenta los planes de Neus, que este la deje embarazada, pues así ya casi ni necesitaria su semen tan a menudo y lo tendría un poco más atrapado.

#     - El padre le da sus opciones, Unirse a él bajo sus condiciones a sangre, o la muerte.

#     - Si MC decide unirse, tendrá que matar a Neus y violar a a una de las dos chicas.

#     - Si MC decide no unirse, el Padre forzará a MC a asfixiar hasta la muerte a Neus, poseyéndolo, luego el jugador pulsando irá asfixiando a Neus, si cesa en su empeño de asfixiar a Neus, el latido del corazón de MC irá disminuyendo hasta alcanzar -la muerte-.

#     - Si MC decide detenerse y sacrificarse, poco antes de morir oirá los pasos desnudos de alguien en el pasillo acercándose a la habitación.

#     - Al mismo tiempo que Neus gritando de desesperación que se detenga (Quien? La madre.)

#     - En la habitación entrará Nana, que MC podrá vislumbrar a duras penas. Esta se acerca a Txell poseída por Padre, mientras Padre sonríe.

#     - Aquí es dónde se revela el verdadero plan de Padre. Hacer salir a madre para volverla a su harén. Si MC lleva el colgar, Madre podrá hablar con él. Le revela que fue ella quien indujo a su hija a sacrificar a ese niño, fue ella quien la condujo hasta ti, fue ella quien deseaba que ambos pudieráis tener una vida feliz y sigue deseándolo, te pide que perdones a Neus, quien desea de corazón cambiar y ser feliz contigo.

#     - Padre desde el suelo sigue riéndose y diciéndole que es un esfuerzo en vano, que del mismo modo que ha recuperado a Madre, tarde o temprano recuperará a su hija y matará al protagonista, es solo cuestión de tiempo, algo de lo que él dispone en abundancia.

#     - Poco después Nana se vuelve cenizas encima de Txell. Hasta que esta recupera el color de sus ojos. Preguntándose dónde está y qué está ocurriendo.

#     - Neus se encuentra desolada llorando la pérdida de su amada madre.

#     -- Después del drama viene el sexo! Vivan los juegos porno que sudan de todo xD.

#     - Neus te implora perdón, copmprende la situación y no te pide que la ames en estas circunstancias, pero al mismo tiempo te pide comprensión, ya que necesita tu semén, no sólo ella, sino también Txell y Dídac para poder sobrevivir y salir con vida de ahí. Tienen de tiempo hasta salir el sol, pues en la Pedrera por el momento están seguros, pero cuando anochezca el día siguiente deben de estar muy lejos de ahí y es el único modo de sobrevivir, incluso de día es si las tres tienen tu esperma en su interior, pues eso las hará casi invisibles a ojo de Padre.

#     - Dependiendo de puntos y acciones, aquí las escenas de sexo pueden tener un aire u otro, Neus puede estas más o menos segura de que la amas si no te has follado a Dídac ni Txell, Txell puede estar en contra de follar contigo, con lo que te correrías en la boca de Neus y estas dos se besarían, puedes dejar o no embarazadas a las tres dependiendo de los puntos, etc.

#     - Una vez hayas tenido tus tres orgasmos, terminas perdiendo el sentido, pues Neus tiene un modo de tener sexo que te deja completamente inútil.

#     - Cuando recuepras los sentidos te encuentras en otro lugar, dependiendo de las acciones previas pueden estar las tres, sólo dos, o sólo Neus. Dídac si estaba embarazada estará sí o sí, pero sino dependerá de si la dejas o no preyñada (a Neus no le gustará demasiado la idea.)

#     - Lejos de padre, fuera de su radar, pero hasta cuando?


