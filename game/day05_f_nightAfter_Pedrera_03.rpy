default afternight05_Pedrera_Sex_SaidJustWithNeus = False
default afternight05_Pedrera_Sex_SaidJustWithNeusx02 = False


default p_active = ""
default p_activen = "didac" # didac, txell, neus
default p_activeno = "_d" # d, m, n

label afternight05_Pedrera_SexPrevious:

    #$ p_on = False
    $ p_prot_sameAction = False

    if programming_check == True:

        $ afternight04__Anal_dick_low_Done = 5
        $ afternight04__Anal_dick_med_Done = 5
        $ afternight04__Anal_Tongue_Done = 5 # Anilingus/ Rim Job

        $ afternight04__Anal_dick_low_Success = 5
        $ afternight04__Anal_dick_med_Success = 5
        $ afternight04__Anal_Tongue_Success = 5 # Anilingus/ Rim Job

        $ afternight04__Anal_dick_deep_Done = 5 # Anal
        $ afternight04__Anal_dick_deep_Success = 5 # Anal


        $ afternight04_Anal_dick_low_Speed_1_Success = 5
        $ afternight04_Anal_dick_med_Speed_1_Success = 5
        $ afternight04_Anal_dick_deep_Speed_1_Success = 5

        $ afternight04_Anal_dick_low_Speed_2_Success = 5
        $ afternight04_Anal_dick_med_Speed_2_Success = 5
        $ afternight04_Anal_dick_deep_Speed_2_Success = 5

        $ afternight04__MMouth_dick_Done = 5
        $ afternight04__MMouth_dick_Success = 5

        $ afternight04__MMouth_dick_Deep_Done = 5
        $ afternight04__MMouth_dick_Deep_Success = 5

        $ afternight04__MMouth_dick_Deep_Done = 5
        $ afternight04__MMouth_dick_Deep_Success = 5
        $ afternight04__MMouth_dick_Deep_Success_Cond = True

    
    $ ntlong = 4

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "bittersweet"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with fade

    n "Neus se acerca cautelosamente a escasos centímetros de ti."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "Dime,"

    extend " ¿Cómo te imaginabas el final de nuestra cita?"

    #########################################################

    if config.version < "00.14.04": # How did you imagine the end of our date?
        call endupdatescript
    
    #######################################################

    if night04_Neus_Blowjob_Cum_Affirmative:

        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_iris front04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        p "Bueno,"

        show n_closefromup_mouth sad_Silentx01
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex01
        with dissolve

        p "digamos que después de lo que me hiciste con tu \"lengua\" ayer por la noche,"

        show n_closefromup_mouth sadbiting_Silentx04
        $ nblush = 5
        show n_closefromup_iris left05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        p "no sé muy bien cómo irá la cosa..."

        show n_closefromup_mouth sad_Talkingx03
        $ nblush = 3
        show n_closefromup_iris left05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "¿Tanto te disgustó?"

        show n_closefromup_mouth sadbiting_Silentx04
        $ nblush = 2
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows surprisex02
        with dissolve

        d "¿Es que te metió la lengua por el culo?"

        $ Pedrera_char_Cond = "TxellDidac"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx01

        show didacf_mouth sad_Talkingx004
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils front02
        show didacf_eyebrows angryx02
        with fade

        d "¡Y luego el marica soy yo!"

        extend " ¡¿no?!"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx03

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows suspiciousx01
        with dissolve

        tx "¿Qué tiene de malo ser marica?"

        extend " Imbécil."

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx03

        show didacf_mouth sad_Silentx04
        $ dteye = 5
        call didac_exp_tears_tears
        show didacf_pupils left05
        show didacf_eyebrows surprisex01
        with dissolve

        d "..."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx04
        with fade

        ne "Tengamos la fiesta en paz,"

        extend " por favor."

        show n_closefromup_mouth sad_Silentx05
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx04
        with dissolve

        pause 0.2

    else:

        show n_closefromup_mouth sadbiting_Silentx03
        show n_closefromup_iris front01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows serious
        with dissolve

        p "Quizás un poco más a solas..."

        show n_closefromup_mouth sadbiting_Silentx02
        show n_closefromup_iris left04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "Humm..."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Sí..."

        show n_closefromup_mouth happy_Talkingx02
        show n_closefromup_iris front05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Yo también,"

        extend " sinceramente."

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with fade

    tx "Neus,"

    extend " ¿quieres que este idiota y yo salgamos para dejaros a solas?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx02

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils left00
    show didacf_eyebrows surprisex02
    with dissolve

    $ ntlong = 3

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_iris right01
    $ nteye = 1
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows surprisex01
    with fade

    ne "..."

    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_iris front02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    menu:

        pt "¿Txell se ofrece a dejarnos a solas?"

        "Quizás no sería tan mala idea.":
            call p_Help

            $pl.ch_pts("np",1)
            $pl.ch_pts("dp",-1)

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_mouth sad_Silentx01
            show n_closefromup_iris front01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with dissolve

            ne "..."

            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            ne "Sí,"

            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_iris front06
            $ nteye = 6
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx04
            with dissolve

            ne "digo no..."

            extend " no."

            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_iris down05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx03
            with dissolve

            tx "¿No?"


        "La idea de tener a tres chicas para mi solo no me disgusta tanto.":
            call p_Help

            $pl.ch_pts("np",-1)
            $pl.ch_pts("dp",1)

            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_iris front05
            $ nteye = 5
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            ne "..."

            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_iris front08
            $ nteye = 8
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            tx "Desde luego..."

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            tx "¡¿Acaso no entiendes lo que Neus siente por ti?!"

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows serious
            with dissolve

            p "¡No estoy hablando de amor!"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03
            with dissolve

            tx "¡Precisamente!"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    ne "Txell,"

    extend " sé que debe ser difícil verme con un hombre,"

    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_iris down05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "pero..."

    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_iris down05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with fade_short

    tx "No es por eso,"

    extend  " entiendo que estoy fuera de tu liga."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    tx "No me importa,"

    extend " de verdad."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Mientras seas feliz."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx01
    with dissolve

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_iris down04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with fade

    ne "No es eso."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris down05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "Es que..."

    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "No puedo ser la primera."

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "didac_theme"

    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    d "A mi no me importaría serlo."

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx03

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with fade

    tx "¡¿Tú eres imbécil, o qué te pasa?!"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    with dissolve

    d "..."

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with fade

    tx "¿Por qué no puedes ser la primera?"

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "meritxell_theme"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Si lo que te molesta es que toque a [protname],"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "a mi no me importaría recibir el esperma directamente de tu boca."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "didac_theme"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows surprisex02

    show didacf_mouth sad_Talkingx005
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows suspiciousx02
    with fade

    d "Y luego el marrano soy yo..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02

    show didacf_mouth sad_Silentx03
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    with dissolve

    p "Dídac..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01

    show didacf_mouth sad_Talkingx08
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    with dissolve

    d "¡¿Es que no puedo decir nada?!"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    with dissolve

    tx "Si al menos dijeras algo inteligente..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02

    show didacf_mouth sad_Silentx06
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    with dissolve

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "bittersweet"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with fade

    ne "..."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "Por que si empiezo,"

    extend " no voy a poder parar."

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "Y luego no habrá esperma para vosotras."

    if DidacMCPregnant:

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        tx "¿Pero no ha sido él quien lo ha dejado embarazada?"

        show n_closefromup_mouth sad_Talkingx002
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Sí..."

        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_iris down05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Pero a pesar de ello,"

    else:

        $ Pedrera_char_Cond = "TxellDidac"
        call Pedrera_char_lab

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows suspiciousx02

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 0
        call didac_exp_tears_tears
        show didacf_pupils left00
        show didacf_eyebrows surprisex02
        with fade

        tx "¿Seguramente Dídac ya habrá tenido su ración de esperma..."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx01

        show didacf_mouth sad_Talkingx07
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows angryx02
        with dissolve

        d "¡Oye!"

        show m_exp_mouth sadbiting_Silentx04
        show m_exp_eyes 00
        show m_exp_piris right00
        show m_exp_eyebrows surprisex002

        show didacf_mouth sad_Talkingx005
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx03
        with dissolve

        d "¡Habla por ti zorra!"

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx02

        show didacf_mouth sad_Silentx06
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Silentx04
        show n_closefromup_iris front08
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with fade

        ne "..."

        ne "Independientemente de que alguna de las dos tuviera su semilla en su interior,"

    if music_play != "atlanteanTwilight":
        play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "atlanteanTwilight"

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_iris front04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "el esperma tiene que ser reciente para poder hacer el sello en condiciones."

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve


    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx003
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with fade

    d "¿El sello?"

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows surprisex02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_iris right02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows serious
    with dissolve

    ne "Cuando [protname] termine,"

    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows normal
    with dissolve

    ne "tendré que pasar mi lengua por ahí dónde se haya corrido"

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02

    with dissolve
    ne "para sellar el esperma en vuestro interior."

    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with fade

    tx "También podríamos hacerlo a la vez."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    ne "No..."

    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "no sé si podré controlarme una vez empiece."

    show n_closefromup_mouth sad_Silentx04
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02

    show didacf_mouth sad_Talkingx06
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows angryx03
    with dissolve

    d "¡Y luego la ninfómana soy yo!"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02

    show didacf_mouth sad_Silentx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    with vpunch

    p "¡DÍDAC!"

    show didacf_mouth sad_Talkingx04
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    with dissolve

    d "Vale,"

    extend " vale..."

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose_b"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with fade

    tx "Podrías intentarlo."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    ne "No es tan fácil..."

    if night04_Neus_Blowjob_Cum_Affirmative:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx04
        with dissolve

        pt "Desde luego,"

        extend " con lo que pasó con la mamada de ayer,"

        pt "no está exagerando..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "¿Y qué propones entonces?"

    if FuckH_Start_Cond:

        # FOR FUTURE

        ne "Tengo entendido que [protname] ya lo ha hecho contigo."

        if FuckH_Start_Cond: # It lacks another conditional Here, if you had been active or passive. # NOT FINISHED

            tx "Más bien,"

            extend " se lo he hecho a él."

            tx "¿Verdad que sí?"

            extend " mi perrito."

            p "..."

            ne "..."

        ne "Así que tampoco te resultará tan raro volverlo a hacer."

    else:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx03
        with dissolve

        ne "Ya te imaginas de lo que estoy hablando..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Neus..."

    if FuckH_Start_Cond:

        # FOR FUTURE

        ne "No,"

        extend " no importa..."

        ne "Lo entiendo."

        ne "Te conozco Txell,"

        ne "eres una persona curiosa,"

        extend " y más cuando se trata de alguien tan especial como [protname]."

        ne "Aunque no seas del todo consciente,"

        ne "sabes que su esperma tiene un sabor..."

        extend " especial,"

        extend " casi adictivo."

    else:

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows sadx01
        with dissolve

        ne "Es normal que no entiendas el comportamiento de Dídac,"

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with fade

        ne "si no has probado su semen."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows suspiciousx01
        with dissolve

        ne "No niego que me ponga de los nervios verlo así,"

        extend " y más sabiendo que es por mi culpa."

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris down05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "Los efectos de su esperma son..."

        extend " complicados de describir."

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "producen una sensación agradable,"

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "seguidamente de un placer extraño y al mismo tiempo familiar,"

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris left02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "pero a largo plazo,"

        extend " se vuelve enfermizamente adictivos."

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Por suerte,"

        extend " vosotras solo necesitaréis una dosis esta noche y quizás mañana,"

        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        ne "pero después de que las sinergias del solsticio se desvanezcan,"

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris left05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "Padre ya tendrá mayores dificultades para encontraros,"

        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_iris front08
        $ nteye = 8
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "a pesar de que no tengáis su esperma para ocultaros de él."

    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_iris left04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "Pero conmigo,"

    extend " su efecto se intensifica hasta un nivel que no puedes llegar a imaginar."

    if DidacMCPregnant:

        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02
        with dissolve

        ne "Quizás Dídac es el único que puede llegar a comprender mínimamente de lo que estoy hablando."

        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_iris right05
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx03
        with dissolve

        d "..."

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "Una vez las dos recibáis vuestra dosis,"

    extend " luego será mi turno."

    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious

    show didacf_mouth sad_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows surprisex01
    with fade

    tx "Entonces lo que falta por saber es quien empieza."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01

    show didacf_mouth sad_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils front02
    show didacf_eyebrows normal
    with dissolve

    pt "Dídac,"

    extend " o Txell."

    # Both can refuse.

    ###

    show m_exp_mouth sadbiting_Silentx01
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    with dissolve

    p "¿Y por qué no las dos a la vez?"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "..."

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "meritxell_theme"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001

    show didacf_mouth sad_Silentx02
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    with dissolve

    tx "¿Y qué tal si dejo que Dídac haga todo el trabajo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001

    show didacf_mouth sad_Silentx04
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx02
    with dissolve

    tx "y luego le como la boca para así tragarme tu semen directamente de su lengua."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows normal

    show didacf_mouth sad_Talkingx05
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    with dissolve

    d "O sea,"

    extend " te pasas todo el tiempo criticándome,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex002

    show didacf_mouth sad_Talkingx08
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows angryx02
    with dissolve

    d "¿y ahora me quieres comer la boca?"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with dissolve

    tx "Es que calladita estás más guapa."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex01

    show didacf_mouth sad_Silentx02
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    with dissolve

    ne "Es peligroso hacer eso,"

    extend " si no consigues tragarte suficiente cantidad."

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "didac_theme"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows normal

    show didacf_mouth sad_Talkingx07
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows angryx03
    with dissolve

    d "¿Y quien te ha dicho que quiera comerme su polla?"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows normal

    show didacf_mouth sad_Talkingx08
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils front01
    show didacf_eyebrows angryx02
    with dissolve

    d "Lo que quiero es que me folle,"

    extend " no hacerle mamadas."

    if DidacPregnant:

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex002

        show didacf_mouth sadbiting_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex01
        with dissolve

        tx "También podría limpiarte la entrepierna,"

        extend " así no tendría que mirarte a la cara."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx01
        with dissolve

        tx "Al fin y al cabo,"

        extend " ya te ha dejado preñada,"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows suspiciousx01

        show didacf_mouth sadbiting_Silentx05
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows suspiciousx01
        with dissolve

        tx "así que no hay necesidad de que te la meta por detrás."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows surprisex001

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils right04
        show didacf_eyebrows suspiciousx02
        with dissolve

        d "..."

    else:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx01

        show didacf_mouth sad_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows serious
        with dissolve

        tx "¿Quieres te folle sin condón y se corra dentro?"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows normal

        show didacf_mouth sadbiting_Silentx02
        $ dteye = 0
        call didac_exp_tears_tears
        show didacf_pupils left00
        show didacf_eyebrows surprisex02
        with dissolve

        tx "¿Tantas ganas tienes de ser mujer?"

        show m_exp_mouth sadbiting_Silentx02
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex001

        show didacf_mouth sad_Talkingx07
        $ dteye = 8
        call didac_exp_tears_tears
        show didacf_pupils front08
        show didacf_eyebrows angryx03
        with dissolve

        d "Es tan fácil, como que haga marcha atrás cuando esté a punto de correrse."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows surprisex002

        show didacf_mouth sadbiting_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex02
        with dissolve

        tx "¿Es lo que sueles hacer con las chicas que embaucas para llevarte a la cama?"

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex002

        show didacf_mouth sad_Silentx05
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows suspiciousx02
        with dissolve

        d "..."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows surprisex02

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils right04
        show didacf_eyebrows suspiciousx02
        with dissolve

        tx "¿De verdad te arriesgarías a no poder volver a ser el que eras por un orgasmo?"

        show m_exp_mouth sadbiting_Silentx01
        show m_exp_eyes 01
        show m_exp_piris right01
        show m_exp_eyebrows surprisex02

        show didacf_mouth sad_Talkingx08
        $ dteye = 8
        call didac_exp_tears_tears
        show didacf_pupils front08
        show didacf_eyebrows angryx03
        with dissolve

        d "Espero tener más de uno..."

        show m_exp_mouth sadbiting_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx01

        show didacf_mouth sad_Talkingx08
        $ dteye = 4
        call didac_exp_tears_tears
        show didacf_pupils left04
        show didacf_eyebrows angryx03
        with dissolve

        tx "Pff..."

        show m_exp_mouth sadbiting_Silentx03
        show m_exp_eyes 02
        show m_exp_piris left02
        show m_exp_eyebrows normal

        show didacf_mouth sad_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows serious
        with dissolve

        ne "Dídac,"

        extend " no digas eso ni en broma."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_iris right02
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows angryx02
        with fade

        ne "Mañana pasado volverás a ser el hombre que eras,"

        extend " es solo cuestión de tiempo."

        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_iris right01
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx01
        with dissolve

        ne "Así que ten un poco de paciencia,"

        extend " por favor."

        show n_closefromup_mouth sadbiting_Silentx03
        show n_closefromup_iris right04
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_eyebrows sadx02

        d "..."

        $ Pedrera_char_Cond = "TxellDidac"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx01
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex001

        show didacf_mouth sad_Silentx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils right03
        show didacf_eyebrows angryx02
        with fade

        d "Tssk..."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01

        show didacf_mouth sad_Silentx05
        $ dteye = 3
        call didac_exp_tears_tears
        show didacf_pupils right03
        show didacf_eyebrows angryx02
        with dissolve

        tx "Bueno,"

        extend " sino te la mete por detrás,"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows suspiciousx01

        show didacf_mouth sad_Silentx02
        $ dteye = 1
        call didac_exp_tears_tears
        show didacf_pupils left01
        show didacf_eyebrows surprisex01
        with dissolve

        tx "quizás pueda probar a que sabe tu entrepierna."

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx01

        show didacf_mouth sadbiting_Silentx04
        $ dteye = 0
        call didac_exp_tears_tears
        show didacf_pupils left00
        show didacf_eyebrows surprisex02
        with dissolve

        tx "No suelo recibir quejas de mis compañeras femeninas,"

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex001

        show didacf_mouth sad_Silentx03
        $ dteye = 2
        call didac_exp_tears_tears
        show didacf_pupils left02
        show didacf_eyebrows suspiciousx01
        with dissolve

        tx "cuando paso mi lengua por esa parte."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02

    show didacf_mouth sad_Talkingx003
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows surprisex01
    with dissolve

    d "¿Tanto te molestaría comerme el trasero?"

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "meritxell_theme"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex001

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows serious
    with dissolve

    tx "¿El tuyo?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002

    show didacf_mouth sad_Silentx05
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    with dissolve

    tx "Desde luego."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01

    show didacf_mouth sad_Silentx04
    $ dteye = 0
    call didac_exp_tears_tears
    show didacf_pupils left00
    show didacf_eyebrows surprisex02
    with dissolve

    tx "A saber qué comes."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01

    show didacf_mouth sad_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows suspiciousx02
    with dissolve

    d "Tssk..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal

    show didacf_mouth sad_Talkingx03
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows serious
    with dissolve

    d "Tampoco suena tan mal..."

    show m_exp_mouth happybiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01

    show didacf_mouth sad_Talkingx004
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows surprisex02
    with dissolve

    d "Seguro que se te da bien comer \"mejillones\"."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx02

    show didacf_mouth sad_Silentx02
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows normal
    with dissolve

    tx "Hmm..." # mischeivous smile

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex001

    show didacf_mouth sadbiting_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows surprisex01
    with dissolve

    tx "Te sorprenderías..."

    show m_exp_mouth happybiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01

    show didacf_mouth happybiting_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    with dissolve

    pause 0.2

    if music_play != "are_you_still_dreaming":
        play music "audio/music/alcaknight/are_you_still_dreaming.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "are_you_still_dreaming"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Silentx06
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with fade

    n "El rostro de Neus está entre la ira, el calor y la confusión."

    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx02
    with dissolve

    ne "Os recuerdo que tenemos hasta que salga el sol,"

    show n_closefromup_mouth sad_Talkingx08
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    ne "tampoco hay tiempo para hacer el {a=https://es.wikipedia.org/wiki/Kama-sutra}{i}kamasutra{/i}{/a} entero."

    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_iris right00
    $ nteye = 0
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows surprisex01
    with dissolve

    d "Lo que pasa es que lo quieres para ti solo;"

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx05
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    with fade

    d "cuanto más rápido vayamos nosotras,"

    show didacf_mouth sad_Talkingx06
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    with dissolve

    d "más tiempo te quedará para tenerlo tú sola."

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    with dissolve

    pause 0.2

    if music_play != "sadTrio":
        play music "audio/music/kevinmacleod/sad/sadTrio.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "sadTrio"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with fade

    ne "..."

    show n_closefromup_mouth sad_Talkingx001
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx02
    with dissolve

    ne "Yo..."

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris right02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows normal
    with dissolve

    tx "Neus,"

    extend " quizás me extralimite pidiéndote esto,"

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with fade

    tx "pero una vez te toque a ti,"

    extend " aunque en mi interior tenga ya su dosis de esperma,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03

    show didacf_mouth sadbiting_Silentx03
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "me gustaría poder complacerte."

    show m_exp_mouth happybiting_Silentx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx03

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows surprisex02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with fade

    ne "No..."

    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    ne "No creo que te vaya a gustar lo que veas cuando..."

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris right02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with dissolve

    tx "Puedes estar tranquila que a él no lo voy a tocar,"

    extend " solo a ti."

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    ne "No me refería a eso..."

    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx04
    with dissolve

    pause 0.2

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "didac_theme"

    if FuckM_Start_Cond:

        $ Pedrera_char_Cond = "TxellClose_b"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex01
        with dissolve

        p "Si ya te he tocado antes,"

        extend " que más te daría hacerlo ahora?"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Pues mi respeto hacia ella,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris left03
        show m_exp_eyebrows sadx01
        with dissolve

        tx "es la primera vez que está contigo."

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx01
        with dissolve

        tx "Pero..."

        extend " también sería la primera vez que estoy con ella."

        show m_exp_mouth sadbiting_Silentx05
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx02
        with dissolve

    ##

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_mouth sad_Talkingx004
    $ dteye = 2
    call didac_exp_tears_tears
    show didacf_pupils left02
    show didacf_eyebrows suspiciousx01
    with fade

    d "Si está ella,"

    extend " ¿por qué no voy a estar yo?"

    show didacf_mouth sadbiting_Silentx02
    $ dteye = 3
    call didac_exp_tears_tears
    show didacf_pupils left03
    show didacf_eyebrows suspiciousx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx04
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows surprisex01
    with fade

    tx "Porque tú quieres su pollón,"

    extend " no a Neus;"

    extend " idiota."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03

    show didacf_mouth sad_Silentx05
    $ dteye = 4
    call didac_exp_tears_tears
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx01
    with dissolve

    d "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx02

    show didacf_mouth sadbiting_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils right05
    show didacf_eyebrows suspiciousx02
    with dissolve

    d "Hmm..." # Doubtful mischiveous smile

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01

    show didacf_mouth sad_Talkingx03
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows surprisex02
    with dissolve

    d "¿Y si lo que quiero es comerte a ti?"

    show m_exp_mouth sadbiting_Silentx01
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows surprisex02

    show didacf_mouth happybiting_Silentx05
    $ dteye = 5
    call didac_exp_tears_tears
    show didacf_pupils left05
    show didacf_eyebrows suspiciousx01
    with dissolve

    tx "..."

    if music_play != "memories_of_the_east":
        play music "audio/music/alcaknight/memories_of_the_east.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "memories_of_the_east"

    $ ntlong = 1

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx10
    show n_closefromup_iris right01
    $ nteye = 1
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with vpunch

    ne "¡Ya basta!"

    show n_closefromup_mouth sad_Talkingx08
    show n_closefromup_iris right04
    $ nteye = 4
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx02
    with dissolve

    ne "¡Eso ya lo veremos en su momento!"

    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_iris right05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx02
    with dissolve

    ne "Ahora que empiece una de las dos,"

    extend " ¡o las dos a la vez!"

    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_iris front08
    $ nteye = 8
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    ne "me da igual."

    show n_closefromup_mouth sad_Talkingx09
    show n_closefromup_iris right01
    $ nteye = 1
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx03
    with dissolve

    ne "¡Pero empezad!"

    show n_closefromup_mouth sad_Silentx06
    show n_closefromup_iris right02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows angryx04
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellDidac"
    call Pedrera_char_lab

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02

    show didacf_mouth sad_Silentx01
    $ dteye = 1
    call didac_exp_tears_tears
    show didacf_pupils left01
    show didacf_eyebrows surprisex02
    with fade

    tx "..."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_iris front02
    $ nteye = 2
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx01
    with fade

    ne "Será mejor que elijas tú,"

    extend " [protname]."

    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_iris front05
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_eyebrows sadx03
    with dissolve

    menu:

        pt "[neusname] tiene que ser la última..."

        "La verdad es que preferiría hacerlo solamente contigo." if afternight05_Pedrera_LetsGetOut_COND == False:

            call p_Help

            $pl.ch_pts("np", 5)
            $pl.ch_pts("dp", -1)

            if music_play != "clearWaters":
                play music "audio/music/kevinmacleod/happy/clearWaters.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "clearWaters"

            $ afternight05_Pedrera_Sex_SaidJustWithNeus = True

            $ nblush = 4
            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_iris front00
            $ nteye = 0
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex04
            with dissolve

            ne "..."

            $ nblush = 6
            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_iris left01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex05
            with dissolve

            ne "Yo..."

            $ nblush = 7
            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_iris right02
            $ nteye = 2
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            ne "Tanto Dídac como Txell necesitan de tu esperma si queremos sobrevivir mañana..."

            show n_closefromup_mouth sad_Talkingx01
            show n_closefromup_iris front02
            $ nteye = 2
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            ne "Yo,"

            extend " no..."

            $ nblush = 5
            show n_closefromup_mouth sadbiting_Silentx09
            show n_closefromup_iris right01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex02
            with dissolve

            d "¡A ver si vamos a estar mirando como folláis y nosotros nada!..."

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx03

            show didacf_mouth sad_Silentx06
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils front02
            show didacf_eyebrows angryx02
            with fade_short

            tx "¿Por qué eres tan imbécil?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx02

            show didacf_mouth sad_Silentx07
            $ dteye = 4
            call didac_exp_tears_tears
            show didacf_pupils left04
            show didacf_eyebrows angryx03
            with dissolve

            d "..."

            show didacf_mouth sad_Silentx05
            $ dteye = 5
            call didac_exp_tears_tears
            show didacf_pupils right05
            show didacf_eyebrows angryx04
            with dissolve

            pause 0.2

            if music_play != "meritxell_theme":
                play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "meritxell_theme"

            $ Pedrera_char_Cond = "TxellClose_b"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious
            with fade

            tx "[protname],"

            extend " si lo que intentas es evitar que Neus se sienta mal al ver como follas con nosotras,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            tx "hay otras maneras de correrse sin necesidad de que haya sexo de ningún tipo."

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious

            show didacf_mouth sad_Silentx02
            $ dteye = 0
            call didac_exp_tears_tears
            show didacf_pupils left00
            show didacf_eyebrows surprisex02
            with dissolve

            tx "Podrías simplemente masturbarte ante nosotras hasta que consiguieras correrte."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx01

            show didacf_mouth sad_Talkingx08
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows angryx04
            with dissolve

            d "¡Tú ve dándole ideas!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01

            show didacf_mouth sad_Silentx06
            $ dteye = 3
            call didac_exp_tears_tears
            show didacf_pupils left03
            show didacf_eyebrows angryx04
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows angryx01

            show didacf_mouth sad_Silentx05
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils left02
            show didacf_eyebrows angryx01
            with dissolve

            tx "Supongo que así,"

            extend " no se lo tomaría tan mal..."

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 04
            show m_exp_piris left04
            show m_exp_eyebrows sadx01

            show didacf_mouth sad_Silentx07
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows angryx02
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            $ nblush = 4
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_iris right01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex03
            with dissolve

            ne "..."

            $ nblush = 5
            show n_closefromup_mouth sad_Talkingx01
            show n_closefromup_iris front01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows surprisex01
            with dissolve

            ne "Euh..."

            $ nblush = 6
            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_iris left01
            $ nteye = 1
            call n_closefromup_tears_tears
            show n_closefromup_eyebrows sadx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex01

            show didacf_mouth sad_Talkingx08
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils left02
            show didacf_eyebrows angryx03
            with dissolve

            d "¡Habla por ti!"

            show m_exp_mouth sadbiting_Silentx01
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows surprisex001

            show didacf_mouth sad_Talkingx09
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows angryx04
            with dissolve

            d "¡Yo no pienso abrir la boca para que me tire lefa en la boca!"

            show m_exp_mouth sadbiting_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01

            show didacf_mouth sad_Silentx07
            $ dteye = 2
            call didac_exp_tears_tears
            show didacf_pupils left02
            show didacf_eyebrows angryx03
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious

            show didacf_mouth sad_Silentx05
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils left01
            show didacf_eyebrows angryx01
            with dissolve

            tx "Ahora es cosa tuya."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious

            show didacf_mouth sad_Silentx03
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows serious
            with dissolve

        "<No decir nada>":

            call p_Help

            $ Pedrera_char_Cond = "TxellDidac"
            call Pedrera_char_lab

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious

            show didacf_mouth sad_Silentx03
            $ dteye = 1
            call didac_exp_tears_tears
            show didacf_pupils front01
            show didacf_eyebrows serious
            with fade

            pass

label afternight05_Pedrera_Sex_DTChoose_previous:

    stop music fadeout 3.0

    #########################################################

    if config.version < "00.14.08": # How did you imagine the end of our date?
        call endupdatescript
    
    #######################################################



    # And what if you don't want to fuck them? then she tells you, you can always just masturbate in front of them and cum.

    $ p_prot = Pedrera_Body()
    $ p_neus = Pedrera_Girl()
    $ p_txell = Pedrera_Girl()
    $ p_didac = Pedrera_Girl()


    $ ntlong = 0

    $ p_prot.id = "p_prot"
    $ p_neus.id = "p_neus"
    $ p_txell.id = "p_txell"
    $ p_didac.id = "p_didac"

    $ p_active = ""
    $ p_activen = "" # didac, txell, neus
    $ p_activeno = "" # d, m, n

    $ p_girl_active = p_didac # I need a default here.

    $ p_deyespCond = False # Is it has to be changed?

    $ p_deyesp = deyesp
    #$ p_prot.posit = ""
    
    call afternight05_Pedrera_Sex_After

    hide screen Points
    if PlatinumHelp == True:
        show screen Points_PedreraSex()

    #########################################################

    if config.version < "00.15.00": # DidacSex: Blowjob/Boobjob/69
        call endupdatescript
    
    jump afternight05_Pedrera_Sex_DTChoose



label afternight05_Elysium_Sex_previous:

    $ p_prot = Pedrera_Body()
    $ p_neus = Pedrera_Girl()


    #$ ntlong = 0

    $ p_prot.id = "p_prot"
    $ p_neus.id = "p_neus"

    $ p_active = "neus"
    $ p_activen = "neus" # didac, txell, neus
    $ p_activeno = "n" # d, m, n

    $ p_girl_active = p_neus # I need a default here.

    #$ p_deyespCond = False # Is it has to be changed?

    return