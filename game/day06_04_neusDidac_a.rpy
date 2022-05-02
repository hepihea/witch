

label day06_neusDidac_01:

    $ day06_company = "neusDidac"

    #aj "Aquí es cuando Dídac aparece."

    call endtranslation

    $ nteye = "left02"
    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    d "¿Te vas a pasar mucho rato yendo a este ritmo de tortuga?"

    $ nteye = "left05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    $ n_dress = "naked"

    pause 0.2

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab
    # show neus_arm_l naked
    # show neus_body naked
    # show neus_arm_r naked

    $ df_eye = "front04"
    # show didacf_eyes 04
    # show didacf_pupils front04
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows surprisex01
    
    call dfeye_lab

    # $ nteye = 1
    # show neus_exp_iris left01
    #$ nteye = "left02"
    $ nteye = "left05"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    #call neus_exp_tears_tears
    with fade

    p "¡¿Dídac?!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    d "¡Así no se va a correr ni mañana!"

    $ df_eye = "left03"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "right03"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmm..."

    $ df_eye = "left04"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Seh..."

    $ df_eye = "left05"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "No he podido evitar que entrase en la habitación."

    # CONDITIONAL

    $ df_eye = "left03"
    show didacf_mouth happy_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "Al fin y al cabo está condenado a ser mujer"

    if DidacMCPregnant:

        $ df_eye = "left02"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows normal
        call dfeye_lab

        $ nteye = "front05"
        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "por que lo dejaste embarazado."

    else:

        $ df_eye = "left03"
        show didacf_mouth sadbiting_Silentx06
        show didacf_eyebrows surprisex01
        call dfeye_lab

        $ nteye = "front05"
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "por que no lo vigilaste lo suficiente."

    $ df_eye = "right02"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows sadx03
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pt "Lo dice como si no hubiera sido ella la que lo convirtió en mujer..."

    if DidacMCPregnant:

        $ df_eye = "right04"
        show didacf_mouth happybiting_Silentx05
        show didacf_eyebrows sadx03
        call dfeye_lab

        $ nteye = "left03"
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        pt "Además,"

        $ df_eye = "right05"
        show didacf_mouth happybiting_Silentx06
        show didacf_eyebrows sadx04
        call dfeye_lab

        $ nteye = "left05"
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        pt "¡se suponía que llevaba condón!"

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Por mucho que manipulara su mente,"

    if DidacMCPregnant:

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "right01"
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "sería incapaz de hacerle olvidar que el retoño que tiene gestando en su vientre es hijo tuyo"

        $ df_eye = "left00"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab

        $ nteye = "right02"
        show neus_exp_mouth sad_Talkingx09
        show neus_exp_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "así como tampoco podría hacerle olvidar el placer que siente con tu miembro y tu esperma..."

    else:

        $ df_eye = "left00"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "right01"
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "hacerle olvidar que existes,"

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab

        $ nteye = "right02"
        show neus_exp_mouth sad_Talkingx09
        show neus_exp_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "tampoco sería justo..."

    $ df_eye = "left00"
    show didacf_mouth sad_Talkingx005
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left00"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    d "¡¿Hacerme olvidar?!"

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx03
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    d "¡Ni se te ocurra!"

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Tus ojos se dirigen a la ventana de la habitación dónde os encontráis"
    
    n "y te fijas en que ya está anocheciendo."

    p "¡¿Es que me he pasado el día durmiendo?!"

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "left03"
    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade

    d "¡¿Ahora te das cuenta?!"

    # CONDITIONAL rape?

    if p_ao_started:

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows serious
        call dfeye_lab

        $ nteye = "front08"
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Eso te pasa por no haberme hecho caso ayer por la noche."

        $ nteye = "front04"
        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        $ Pedrera_char_Cond = "NeusWall"
        call Pedrera_char_lab

        $ nteye = "front04"
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade

        ne "Espero que aprendieras la lección."

        $ nteye = "front05"
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        menu:

            "Supongo que aprendí la lección.":
                call p_Help
                $pl.ch_pts("np", 1)

                $ nteye = "front04"
                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "Eso espero..."

                $ nteye = "front05"
                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            "Tampoco estuvo tan mal.":
                call p_Help
                $pl.ch_pts("np", 2)

                $ nteye = "front00"
                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "¡¿Qué?!"

                $ nteye = "right01"
                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyebrows serious
                call n_closefromup_tears_tears
                with dissolve

                ne "No... no hagas bromas con esto."

                $ nteye = "front01"
                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                p "No lo digo en broma."

                $ nteye = "left01"
                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                d "¿De qué estáis hablando?"

                $ nteye = "front08"
                show neus_exp_mouth sad_Talkingx005
                show neus_exp_eyebrows angryx01
                call n_closefromup_tears_tears
                with dissolve

                ne "¡Nada ¡Nada!"

                $ nteye = "right04"
                show neus_exp_mouth happy_Talkingx03
                show neus_exp_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "No importa..."

                $ nteye = "right05"
                show neus_exp_mouth happybiting_Silentx04
                show neus_exp_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

            "¿Fue necesaria tanta rudeza?":
                call p_Help
                $pl.ch_pts("np", -1)

                $ nteye = "front01"
                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "¡Ya te advertí de ello y no quisiste hacerme caso!"

                $ nteye = "front04"
                show neus_exp_mouth sad_Silentx06
                show neus_exp_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "right05"
                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            "...":
                call p_Help

                $ nteye = "front05"
                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

        pause 0.2
                
        $ Pedrera_char_Cond = "NeusDidac_close"
        call Pedrera_char_lab

    else:

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "front08"
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "No es su culpa,"

        $ df_eye = "left03"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab

        $ nteye = "front04"
        show neus_exp_mouth happy_Talkingx03
        show neus_exp_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "realmente estaba muy cansado."

        $ nteye = "front05"
        show neus_exp_mouth happy_Silentx05
        show neus_exp_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

    
    $ df_eye = "front02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "front01"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    p "¿Dónde está Meritxell?"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left02"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    d "¿Desde cuando te preocupa la tetuda?"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "La tetuda..."

        "Es solo curiosidad.":
            call p_Help
            $pl.ch_pts("np", 1)

            $ df_eye = "front05"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "front03"
            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            d "Ya..."

        "¿Es malo que me preocupe por alguien?":
            call p_Help
            $pl.ch_pts("np", 1)

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "front08"
            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            d "..."

            $ df_eye = "left03"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab

            $ nteye = "right03"
            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "No,"

            $ df_eye = "left04"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows serious
            call dfeye_lab

            $ nteye = "right05"
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "no es malo en absoluto."

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Está bien."

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "right01"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Simplemente prefirió esperar en otra habitación."

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "right03"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando terminemos me encargaré de darle su parte."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "front05"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    p "¿Su parte?"

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "A estas horas mis hermanas deben de estar empezando el {a=https://es.wikipedia.org/wiki/Aquelarre}aquelarre{/a}."

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "front01"
    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Es importante que esta noche estemos todas bien alimentadas con tu esperma,"

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows sadx01
    call dfeye_lab

    $ nteye = "front02"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "para que no surja ningún problema."

    $ df_eye = "front04"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ df_eye = "front01"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    d "¡Así que ya sabes lo que te toca!"

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "Dídac..."

    $ df_eye = "front04"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "front05"
    show neus_exp_mouth happybiting_Silentx03
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    menu:

        "No creo que mi polla aguante otro trote como el de ayer.":
            call p_Help
            #$pl.ch_pts("np", 1)

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx01
            show didacf_eyebrows surprisex01
            call dfeye_lab

            $ nteye = "front02"
            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmm..."

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx01
            show didacf_eyebrows serious
            call dfeye_lab

            $ nteye = "front04"
            show neus_exp_mouth happy_Talkingx05
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "No te subestimes [protname],"

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab

            $ nteye = "front03"
            show neus_exp_mouth happy_Talkingx06
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "te aseguro con mis artes,"

            $ df_eye = "left01"
            show didacf_mouth sad_Silentx01
            show didacf_eyebrows surprisex02
            call dfeye_lab

            $ nteye = "front05"
            show neus_exp_mouth happy_Talkingx07
            show neus_exp_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "y con algo de ayuda,"

            $ df_eye = "left04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            $ nteye = "front04"
            show neus_exp_mouth happy_Talkingx06
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "lo lograremos."

            $ df_eye = "left05"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows surprisex02
            call dfeye_lab

            $ nteye = "left01"
            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            d "¿Algo de ayuda?"

            $ df_eye = "left02"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            $ nteye = "left04"
            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            d "¿A qué viene eso?"

            $ df_eye = "left03"
            show didacf_mouth sadbiting_Silentx02
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows angryx01
            call n_closefromup_tears_tears
            with dissolve

            ne "Por mucho que te hayas convertido en mujer,"

            $ df_eye = "left01"
            show didacf_mouth sadbiting_Silentx01
            show didacf_eyebrows normal
            call dfeye_lab

            $ nteye = "left04"
            show neus_exp_mouth sad_Talkingx005
            show neus_exp_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "sigues siendo bastante inexperta,"

            $ df_eye = "left04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "además tampoco tienes mis ojos brillantes"

            $ df_eye = "left01"
            show didacf_mouth sadbiting_Silentx02
            show didacf_eyebrows surprisex01
            call dfeye_lab

            $ nteye = "left04"
            show neus_exp_mouth happy_Talkingx05
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "o mis habilidades..."

            extend " especiales."

            $ df_eye = "right04"
            show didacf_mouth sadbiting_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            $ nteye = "left03"
            show neus_exp_mouth happy_Silentx04
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            d "..."

            $ df_eye = "right02"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "left05"
            show neus_exp_mouth happy_Silentx06
            show neus_exp_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            d "Supongo que no."

            $ df_eye = "right05"
            show didacf_mouth sadbiting_Silentx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab

            $ nteye = "front05"
            show neus_exp_mouth happy_Silentx05
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

        "Preferiría estar a solas con [neusname]." if not gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np", 5)
            $pl.ch_pts("np", -10)

            $ day06_company = "neusAlone"
            $ day06_morning_rejection = "didac"

            ne "..."

            d "Estarás de broma..."

            d "¿Verdad?"

            p "No."

            p "Lo digo en serio."

            p "Preferiría estar a solas con ella."

            d "..."

            ne "Yo..."

            d "¡¿ME ESTÁS TOMANDO EL PUTO PELO?!"

            if DidacMCPregnant: 

                d "¡¿DESPUÉS DE DEJARME PREÑADA AHORA PASAS DE MÍ?!"

                p "Fuiste tú el que cortaste el condón sin que yo lo supiera."

                d "¡PERO BIEN QUE ME FOLLASTE COMO UN PERRO SARNOSO!"

                p "¿Te recuerdo de qué manera me lo suplicaste?"

                d "¡¿ESA ES TU EXCUSA?!"

            p "Simplemente quiero estar a solas con [neusname]."

            if neusname != "Neus":

                d "¿Prefieres estar con alguien que ni siquiera te había dicho su nombre real?"

                d "¡¿Con alguien que me convirtió en mujer para poder hacerte chantaje?!"

            else:

                d "¿Prefieres estar con alguien que me convirtió en mujer para poder hacerte chantaje?"

            ne "Dídac..."

            d "¡¿Estoy diciendo alguna puta mentira?!"

            ne "..."

            d "Tssk..."

            d "¡Que os follen!"

            d "¡A LOS DOS!"

            d "¡Me voy con la rubia que por lo menos no es tan jodidamente hipócrita!"

            p "No la conoces lo suficiente."

            d "¡QUE TE FOLLEN!"

            n "Sale disparado en dirección a la puerta."

            ne "Dídac,"

            extend " vas desnuda..."

            with hpunch
            with hpunch
            ono "PAM"

            ne "..."

            p "Tranquila,"

            extend " ya se le pasará."

            ne "¿Tú crees?"

            pt "Creo que sí."

            ne "Me siento algo mal por ella..."

            ne "Pero debo confesar que al mismo tiempo"

            ne "soy inmensamente feliz de que prefieras estar conmigo a solas."

            if gensex_ILoveYouNeus:

                ne "Mi querido Lancelot..."

            jump day06_neusAlone_02
            # n "Vuelves a sentir el cálido tacto de sus labios,"
            # n "pero esta vez, acariciando tu lengua con la suya,"
            # n "ofreciéndote un beso algo más apasionado."
            # ne "Te amo tanto."
            # n "Dirige sus ojos a tu erecta entrepierna mientras se muerde los labios."
            # n "Observas que te coge de la muñeca,"

        "Preferiría estar a solas con Dídac." if not gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", -10)
            $pl.ch_pts("dp", 5)

            $ day06_morning_rejection = "neus"
            $ day06_company = "didacAlone"

            ne "..."

            d "¿En serio?"

            p "Sí,"

            p "lo digo en serio."

            d "Sabes que yo no te voy a tratar tan bien como ella,"

            d "¿verdad?"

            p "..."

            ne "¿He hecho algo que te molestara?"

            menu:

                pt "Algo que me molestara..."

                # "¿Te parece poco haber digerido a un niño mientras aún vivía?" if p_ao_neusLastSecret: #No necessary.
                #     call p_Help
                #     $pl.ch_pts("np",-5)
                #     ne "..."
                #     d "¿Digerido?"
                #     d "¿De qué estás hablando?"
                #     p "Cuéntaselo."

                "¿Te parece poco haber sacrificado a un niño?":
                    call p_Help
                    $pl.ch_pts("np",-3)

                    ne "..."

                    ne "..."

                "¿Te parece poco todas las monstruosidades que has hecho?":
                    call p_Help
                    $pl.ch_pts("np",-2)

                    ne "..."

                "Tu sola presencia me repugna.":
                    call p_Help
                    ne "..."

                    if not gensex_YoureAMonster:
                        $pl.ch_pts("np",-4)

                        ne "Pensaba que no me odiabas tanto."

                        p "Pues ya ves que te equivocabas."

                    else:
                        $pl.ch_pts("np",-2)

                        ne "..."

                "Simplemente preferiría no tenerte cerca.":
                    call p_Help
                    $pl.ch_pts("np",-3)

                    ne "..."

                    ne "Como quieras..."

                "Simplemente quiero estar a solas con Dídac.":
                    call p_Help
                    $pl.ch_pts("np",-2)

                    ne "..."

                    ne "Ya veo..."

            d "..."

            ne "Lo-"

            extend "lo siento..."

            ne "Os dejaré a solas."

            n "Se levanta y con los pies desnudos se dirige al baño entre lágrimas."

            d "..."

            d "¿Hacía falta que le dijeras eso?"

            p "Es la verdad."

            d "Ya lo sé."

            d "Pero al fin y al cabo nuestra vida depende de ella."

            d "¿Crees que es buena idea provocarla de ese modo?"

            p "¿Te refieres a que tendría que aceptar estar con ella por miedo a lo que nos pueda hacer?"

            d "..."

            d "Tampoco creo que te lo fueras a pasar tan mal..."

            p "Dídac."

            d "Ey..."

            d "A mi ya me está bien."

            d "Más tiempo con tu pollón a solas."

            ono "cloc"

            n "Oís la puerta del baño abriéndose,"

            n "de dónde sale [neusname] con un albornoz blanco que le cubre el cuerpo"

            n "con el rostro cabizbajo y con una voz temblorosa:"

            ne "Dídac,"

            ne "no te tomes a broma lo que te he dicho sobre esta noche."

            d "No lo haré."

            ne "Y recuerda usar lo que te he dado,"

            ne "solo en caso de extrema necesidad."

            d "Que sí mujer,"

            extend" que sí,"

            d "no te preocupes."

            p "¿Lo que te ha dado?"

            n "Se dirige a la puerta de salida."

            ono "clic"

            ne "No espero que olvides lo que he hecho."

            ne "solo deseo que algún día puedas darme la oportunidad de demostrarte lo que puedo llegar a ser a tu lado."

            ono "pum"

            d "..."

            d "Otra cosa no sé,"

            d "pero la niña sabe hacerte sentir mal."

            p "¿Eso es que se te han pasado las ganas de follar?"

            d "Hmm..."

            d "¿Quieres comprobarlo?"

            jump day06_didacAlone_CanYouStandUp
                # n "Levanta sus caderas y te libera de su cálido interior."
                # d "¿Te puedes levantar?"
                # p "No lo sé..."
                # p "Realmente siento que me faltan fuerzas,"


        "Preferiría que estuviera Meritxell aquí también.":
            call p_Help
            $pl.ch_pts("np", -2)

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx01
            show didacf_eyebrows surprisex01
            call dfeye_lab

            $ nteye = "front02"
            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ df_eye = "front05"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows surprisex01
            call dfeye_lab

            $ nteye = "left04"
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            d "Es avaricioso el cabrón..."

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab

            $ nteye = "front03"
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Es que no tienes suficiente con nosotras dos?"

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            $ nteye = "front05"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows angryx01
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "Un trío con Dídac y [neusname]..."

                "Por supuesto que sí, solo digo que no sería una mala idea, ¿no crees?":
                    call p_Help
                    #$pl.ch_pts("np", -1)

                    $ df_eye = "front04"
                    show didacf_mouth sad_Talkingx004
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "right04"
                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    d "El buen samaritano..."

                    $ df_eye = "front05"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ df_eye = "left03"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "right01"
                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque quisiera,"

                    $ df_eye = "left03"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    $ Pedrera_char_Cond = "NeusWall"
                    call Pedrera_char_lab

                    if pl.mp > 30:

                        $ nteye = "front08"
                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with fade

                        ne "Meritxell me ha pedido que te dijera que no es nada personal,"

                        $ nteye = "right02"
                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "que simplemente cree que no sería buena idea que estuviéramos las tres juntas contigo."

                        $ nteye = "front01"
                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        p "¿Por qué?"

                        $ nteye = "left02"
                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        d "Porque quizás le caigo mal."

                        $ nteye = "left03"
                        show neus_exp_mouth sadbiting_Silentx04
                        show neus_exp_eyebrows suspiciousx01
                        call n_closefromup_tears_tears
                        with dissolve

                    elif pl.mp > 10:

                        $ nteye = "front08"
                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with fade

                        ne "Meritxell no se siente especialmente cómoda contigo."

                        $ nteye = "front06"
                        show neus_exp_mouth happy_Talkingx03
                        show neus_exp_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "no creo que sea nada personal,"

                        $ nteye = "front04"
                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "simplemente no es demasiado amante de los hombres."

                        $ nteye = "front05"
                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                    else:

                        $ nteye = "front08"
                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with fade

                        ne "Meritxell no se siente especialmente cómoda contigo."

                        $ nteye = "front06"
                        show neus_exp_mouth happy_Talkingx03
                        show neus_exp_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Por lo que parece no le caes especialmente bien..."

                        $ nteye = "left02"
                        show neus_exp_mouth sad_Silentx02
                        show neus_exp_eyebrows normal
                        call n_closefromup_tears_tears
                        with dissolve

                        d "¿Por qué será...?"

                        $ nteye = "left03"
                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyebrows suspiciousx01
                        call n_closefromup_tears_tears
                        with dissolve

                        d "Quizás es porque te tiene envidia."

                        $ nteye = "left04"
                        show neus_exp_mouth sad_Silentx02
                        show neus_exp_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusDidac_close"
                    call Pedrera_char_lab

                    $ df_eye = "left04"
                    show didacf_mouth happy_Talkingx06
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "left00"
                    show neus_exp_mouth sad_Silentx01
                    show neus_exp_eyebrows surprisex03
                    call n_closefromup_tears_tears
                    with fade

                    d "O quizás es porque prefiere tenerte a ti para ella sola..."

                    $ df_eye = "left05"
                    show didacf_mouth happy_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "right04"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ df_eye = "left02"
                    show didacf_mouth happy_Talkingx06
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "left04"
                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    d "¿Me equivoco?"

                    $ df_eye = "left01"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx004
                    show neus_exp_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Eso no tiene nada que ver,"

                    $ df_eye = "left04"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx02
                    call dfeye_lab

                    $ nteye = "left02"
                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "es simplemente una cuestión de supervivencia."

                    $ df_eye = "front08"
                    show didacf_mouth sad_Talkingx004
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "left04"
                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    d "Claro,"

                    extend " claro..."

                    $ df_eye = "left03"
                    show didacf_mouth happy_Talkingx07
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "left01"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    if p_txell.cumReceived == "oral":

                        d "Por eso la besaste con lengua,"

                    elif p_txell.cumReceived == "vaginal":

                        d "Por eso le comiste el coño,"

                    elif p_txell.cumReceived == "anal":

                        d "Por eso le comiste el trasero,"

                    else:

                        d "Por eso le pasaste la lengua,"

                    $ df_eye = "left04"
                    show didacf_mouth happy_Talkingx05
                    show didacf_eyebrows angryx01
                    call dfeye_lab

                    $ nteye = "left04"
                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    d "sin ningún tipo de pasión..."

                    $ df_eye = "left05"
                    show didacf_mouth happy_Silentx05
                    show didacf_eyebrows suspiciousx02
                    call dfeye_lab

                    $ nteye = "right04"
                    show neus_exp_mouth sadbiting_Silentx07
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right02"
                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Euhh..."

                    $ df_eye = "left04"
                    show didacf_mouth sad_Silentx01
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx004
                    show neus_exp_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Eso lo hice porque soy adicta al esperma de [protname]."

                    $ df_eye = "left05"
                    show didacf_mouth sad_Talkingx003
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "left01"
                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyebrows normal
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿Solo por eso?"

                    $ df_eye = "left05"
                    show didacf_mouth happy_Silentx04
                    show didacf_eyebrows serious
                    call dfeye_lab

                    $ nteye = "right03"
                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ df_eye = "left01"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No quiero responder a esa pregunta."

                    $ df_eye = "left03"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "right05"
                    show neus_exp_mouth sadbiting_Silentx07
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        "¿Por qué no?":
                            call p_Help

                            if gensex_ILoveYouNeus:

                                if pl.np > 150: # NOT FINISHED, NOT SURE ABOUT THE NUMBER HERE.

                                    $ nteye = "front05"
                                    show neus_exp_mouth sad_Talkingx03
                                    show neus_exp_eyebrows sadx05
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    ne "¿Acaso no me crees cuando te digo que te amo?"
                                else:

                                    $ nteye = "right05"
                                    show neus_exp_mouth sad_Talkingx03
                                    show neus_exp_eyebrows sadx05
                                    call n_closefromup_tears_tears
                                    with dissolve

                                    ne "A veces pienso que realmente no me amas."

                                $ df_eye = "front01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "front01"
                                show neus_exp_mouth sadbiting_Silentx04
                                show neus_exp_eyebrows surprisex01
                                call n_closefromup_tears_tears
                                with dissolve

                                p "¿Entonces por qué te cuesta responderme?"

                                $ df_eye = "left02"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows serious
                                call dfeye_lab

                                $ nteye = "front04"
                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                $ df_eye = "left01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows suspiciousx01
                                call dfeye_lab

                                $ nteye = "right02"
                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Porque cuando voy cachonda hago cosas sin pensar..."

                                $ df_eye = "left02"
                                show didacf_mouth sadbiting_Silentx02
                                show didacf_eyebrows sadx01
                                call dfeye_lab

                                $ nteye = "right04"
                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "y más cuando se trata de tu esperma."

                                $ df_eye = "left03"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows sadx01
                                call dfeye_lab

                                $ nteye = "front08"
                                show neus_exp_mouth sad_Talkingx04
                                show neus_exp_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No me pidas más,"

                                $ df_eye = "left04"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows sadx01
                                call dfeye_lab

                                $ nteye = "front04"
                                show neus_exp_mouth sad_Talkingx03
                                show neus_exp_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "por favor..."

                                $ df_eye = "front02"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows normal
                                call dfeye_lab

                                $ nteye = "front05"
                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                p "..."

                            else:

                                $pl.ch_pts("np", -2)

                                $ df_eye = "left01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "front08"
                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows angryx01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "He dicho que no."

                                $ df_eye = "front02"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows normal
                                call dfeye_lab

                                $ nteye = "right05"
                                show neus_exp_mouth sadbiting_Silentx04
                                show neus_exp_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                        "No es necesario, tranquila.":
                            call p_Help
                            $pl.ch_pts("np", 2)

                            $ df_eye = "front01"
                            show didacf_mouth sad_Silentx02
                            show didacf_eyebrows surprisex01
                            call dfeye_lab

                            $ nteye = "front04"
                            show neus_exp_mouth happy_Silentx03
                            show neus_exp_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ df_eye = "left02"
                            show didacf_mouth sad_Silentx03
                            show didacf_eyebrows suspiciousx01
                            call dfeye_lab

                            $ nteye = "front06"
                            show neus_exp_mouth happy_Talkingx03
                            show neus_exp_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Gracias."

                            $ df_eye = "left04"
                            show didacf_mouth sad_Silentx04
                            show didacf_eyebrows suspiciousx01
                            call dfeye_lab

                            $ nteye = "right05"
                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                        "...":
                            call p_Help
                            $pl.ch_pts("np", 1)

                            $ df_eye = "front04"
                            show didacf_mouth sad_Silentx03
                            show didacf_eyebrows suspiciousx01
                            call dfeye_lab

                            $ nteye = "front05"
                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                "Lo digo para que luego no tuvieras que estar a solas con ella.":
                    call p_Help

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx05
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    
                    $ nteye = "front03"
                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Qué...?"

                    $ df_eye = "front05"
                    show didacf_mouth happy_Talkingx04
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "left01"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows normal
                    call n_closefromup_tears_tears
                    with dissolve

                    d "¿Acaso te pondrías celoso?"

                    $ df_eye = "front00"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "front00"
                    show neus_exp_mouth sadbiting_Silentx01
                    show neus_exp_eyebrows surprisex03
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pues sí."

                    if gensex_YoureAMonster:

                        $pl.ch_pts("np", -1)

                        $ df_eye = "left02"
                        show didacf_mouth sad_Silentx03
                        show didacf_eyebrows suspiciousx01
                        call dfeye_lab

                        $ nteye = "front03"
                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyebrows angryx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No sé porque,"

                        $ nteye = "front04"
                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyebrows angryx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "si me consideras un monstruo."

                        $ df_eye = "front04"
                        show didacf_mouth sad_Silentx04
                        show didacf_eyebrows suspiciousx02
                        call dfeye_lab

                        $ nteye = "right05"
                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                    else:

                        $pl.ch_pts("np", 1)

                        $ df_eye = "left02"
                        show didacf_mouth sad_Silentx03
                        show didacf_eyebrows suspiciousx01
                        call dfeye_lab

                        $ nteye = "front05"
                        show neus_exp_mouth happybiting_Silentx04
                        show neus_exp_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ df_eye = "left05"
                        show didacf_mouth sad_Silentx04
                        show didacf_eyebrows suspiciousx02
                        call dfeye_lab

                        $ nteye = "front06"
                        show neus_exp_mouth happybiting_Silentx05
                        show neus_exp_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                    pause 0.2

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Yo..."

                    $ df_eye = "left03"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "front04"
                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Entiéndelo,"

                    $ df_eye = "left02"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "front01"
                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "necesito darle su parte,"

                    $ df_eye = "left01"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "o corremos el riesgo de que pueda poseerla como ocurrió ayer."

                    $ df_eye = "left02"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "front04"
                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Es una cuestión de supervivencia."

                    $ df_eye = "left04"
                    show didacf_mouth happy_Talkingx04
                    show didacf_eyebrows sadx01
                    call dfeye_lab

                    $ nteye = "front01"
                    show neus_exp_mouth sadbiting_Silentx02
                    show neus_exp_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    d "Y si por el camino una puede gozarlo,"

                    $ df_eye = "front04"
                    show didacf_mouth happy_Talkingx05
                    show didacf_eyebrows serious
                    call dfeye_lab

                    $ nteye = "left04"
                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    d "mucho mejor,"

                    extend " ¿no?"

                    $ df_eye = "front0"
                    show didacf_mouth happy_Silentx05
                    show didacf_eyebrows angryx01
                    call dfeye_lab

                    $ nteye = "right02"
                    show neus_exp_mouth sadbiting_Silentx02
                    show neus_exp_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ df_eye = "left04"
                    show didacf_mouth happy_Silentx03
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "right01"
                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Esto..."

                    $ df_eye = "front02"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "front02"
                    show neus_exp_mouth sadbiting_Silentx02
                    show neus_exp_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿No podrías convencerla?"

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex02
                    call dfeye_lab

                    $ nteye = "front04"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ df_eye = "left02"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Créeme que lo he intentado."

                    $ df_eye = "left03"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows serious
                    call dfeye_lab

                    if pl.mp > 30:

                        $ nteye = "right02"
                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero cuando toma una decisión es difícil hacerle cambiar de opinión."

                    elif pl.mp > 10:

                        $ nteye = "right01"
                        show neus_exp_mouth sad_Talkingx004
                        show neus_exp_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero los hombres en general no son de su gusto."

                        $ nteye = "front04"
                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No te lo tomes como algo personal."

                    else:

                        $ nteye = "front04"
                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero aparentemente no le caes muy bien."

                    $ df_eye = "left02"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab

                    $ nteye = "front08"
                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Y no,"

                    $ df_eye = "left01"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows surprisex01
                    call dfeye_lab

                    $ nteye = "front04"
                    show neus_exp_mouth sad_Talkingx004
                    show neus_exp_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "no la voy a obligar a hacer algo que no quiere."

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows normal
                    call dfeye_lab

                    $ nteye = "front05"
                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        pt "Tampoco se lo he pedido..."

                        "Pero no me siento a gusto que luego tengas que estar a solas con ella.":
                            call p_Help

                            $ df_eye = "front01"
                            show didacf_mouth sad_Silentx02
                            show didacf_eyebrows surprisex01
                            call dfeye_lab

                            $ nteye = "front03"
                            show neus_exp_mouth sadbiting_Silentx03
                            show neus_exp_eyebrows sadx02
                            call n_closefromup_tears_tears
                            with dissolve

                            pause 0.2

                            $ df_eye = "front05"
                            show didacf_mouth sad_Talkingx004
                            show didacf_eyebrows surprisex02
                            call dfeye_lab

                            $ nteye = "left01"
                            show neus_exp_mouth sadbiting_Silentx01
                            show neus_exp_eyebrows surprisex01
                            call n_closefromup_tears_tears
                            with dissolve

                            d "Tampoco estaría sola."

                            $ df_eye = "front02"
                            show didacf_mouth sad_Silentx04
                            show didacf_eyebrows surprisex01
                            call dfeye_lab

                            $ nteye = "front04"
                            show neus_exp_mouth sadbiting_Silentx03
                            show neus_exp_eyebrows sadx01
                            call n_closefromup_tears_tears
                            with dissolve

                            p "Ya me entiende."

                            $ df_eye = "left02"
                            show didacf_mouth sad_Silentx03
                            show didacf_eyebrows normal
                            call dfeye_lab

                            if gensex_YoureAMonster:
                                $pl.ch_pts("np", -5)

                                $ nteye = "front05"
                                show neus_exp_mouth sad_Talkingx004
                                show neus_exp_eyebrows surprisex01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Por qué?"

                                $ df_eye = "left01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "front01"
                                show neus_exp_mouth sad_Talkingx06
                                show neus_exp_eyebrows angryx01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "¿Tienes miedo que otra persona juegue con tu monstruo?"

                                $ df_eye = "left01"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows suspiciousx01
                                call dfeye_lab

                                $ nteye = "front03"
                                show neus_exp_mouth sad_Talkingx07
                                show neus_exp_eyebrows angryx02
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No soy tu mascota."

                                $ df_eye = "front01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "right05"
                                show neus_exp_mouth sadbiting_Silentx05
                                show neus_exp_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                            else:
                                $pl.ch_pts("np", -2)

                                $ nteye = "front08"
                                show neus_exp_mouth sad_Talkingx05
                                show neus_exp_eyebrows surprisex01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Hagamos una cosa."

                                $ df_eye = "left01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "front04"
                                show neus_exp_mouth sad_Talkingx004
                                show neus_exp_eyebrows normal
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Si consigues estar en pie después de pasar por nosotras,"

                                $ df_eye = "left02"
                                show didacf_mouth sad_Silentx03
                                show didacf_eyebrows suspiciousx01
                                call dfeye_lab

                                $ nteye = "front05"
                                show neus_exp_mouth happy_Talkingx04
                                show neus_exp_eyebrows serious
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "luego, si quieres,"

                                $ df_eye = "left00"
                                show didacf_mouth sad_Silentx01
                                show didacf_eyebrows surprisex02
                                call dfeye_lab

                                $ nteye = "front02"
                                show neus_exp_mouth happy_Talkingx05
                                show neus_exp_eyebrows normal
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "puedes venir y mirarnos."

                                $ df_eye = "front01"
                                show didacf_mouth sad_Silentx02
                                show didacf_eyebrows surprisex01
                                call dfeye_lab

                                $ nteye = "front04"
                                show neus_exp_mouth happy_Silentx04
                                show neus_exp_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Si apenas no puedo ni moverme."

                                $ df_eye = "left03"
                                show didacf_mouth happy_Silentx02
                                show didacf_eyebrows sadx01
                                call dfeye_lab

                                $ nteye = "front05"
                                show neus_exp_mouth happy_Talkingx06
                                show neus_exp_eyebrows normal
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Precisamente..."

                                $ df_eye = "front04"
                                show didacf_mouth happy_Silentx03
                                show didacf_eyebrows sadx02
                                call dfeye_lab

                                $ nteye = "front06"
                                show neus_exp_mouth happy_Silentx05
                                show neus_exp_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                        "...":
                            call p_Help

                            $ df_eye = "front04"
                            show didacf_mouth sad_Silentx03
                            show didacf_eyebrows suspiciousx01
                            call dfeye_lab

                            $ nteye = "front04"
                            show neus_exp_mouth sadbiting_Silentx05
                            show neus_exp_eyebrows sadx01
                            call n_closefromup_tears_tears
                            with dissolve

        "...":
            call p_Help

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            $ nteye = "front04"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve
            

    pause 0.2

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "front02"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    p "¿Y dónde estamos?"

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    call day06_neusDidac_whereWeAre

    jump day06_neusDidac_HowAreYou

label day06_neusDidac_HowAreYou:

    ##CONDITIONAL, LOVE OF NEUS? over 150?

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Cómo te encuentras?"

    $ nteye = "down04"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    p "..."

    n "Intentas levantar el brazo, pero a duras penas eres capaz de mover los dedos."

    p "Siento el cuerpo entumecido y creo que no puedo moverme demasiado."

    d "Por lo menos la polla la sigue teniendo bastante dura."

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with fade

    ne "..."

    $ df_eye = "left05"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "left02"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    d "¿En qué estás pensando brujita?"

    $ df_eye = "left04"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "No me llames así."

    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    d "¿No me has hecho beber algo antes?"

    $ df_eye = "front02"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "front01"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "¿Beber algo?"

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "right02"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    p "¿El qué?"

    $ nteye = "right04"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Mi sangre."

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Qué?!"

    $ nteye = "front08"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Tu sangre?!"

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Para qué?!"

    $ nteye = "down04"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Ciertamente tu polla está bastante dura,"

    $ nteye = "right04"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "así que quizás no hará falta que tú también la ingieras."

    $ nteye = "front02"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero no estoy segura si serás capaz de producir más de una sola dosis en tu estado..."

    if p_ao_started: # You need to take the blood without exception, you can't even move.

        $ nteye = "front01"
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Al fin y al cabo ayer..."

        $ nteye = "front00"
        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Ayer me follaste y me re-follaste."

        $ nteye = "front01"
        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¡¿Y de quien narices es la culpa?!"

        $ nteye = "right05"
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    else:

        $ nteye = "right05"
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        pt "¿Llama dosis a una corrida?"

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Existe un modo de conseguir que te corras al menos dos o tres veces"

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "y que tengas energía suficiente para poder moverte y follarnos a las dos."

    $ nteye = "front03"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "¿Tu sangre?"

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Sí."

    $ nteye = "right01"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero conlleva un pequeño problema."

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "¿Cuál?"

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando suelo usar este método,"

    $ nteye = "right03"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "la otra persona suele..."

    $ nteye = "right04"
    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "terminar bastante mal."

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "¿Cómo de mal?"

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "No suele sobrevivir."

    $ nteye = "front02"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Cómo?!"

    $ nteye = "front03"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Pero no has dicho que Dídac se lo ha tomado?!"

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "left00"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with Dissolve(0.2)

    d "¡¿Voy a morir?!"

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx01
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "¡No!"

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows sadx02
    call dfeye_lab

    $ nteye = "left02"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "En Dídac no lo he usado para recobrar sus fuerzas,"

    $ df_eye = "left02"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "así que no le hará ningún daño en ese aspecto."

    $ df_eye = "front02"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab

    $ nteye = "front04"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "¿Entonces para qué?"

    $ df_eye = "left03"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows sadx02
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Para otro motivo."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    ne "Que ahora no voy a discutir."

    $ nteye = "front02"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front02"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "¿Estás diciéndome que si me tomo esto,"

    $ nteye = "front01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    p "recobraré las fuerzas,"

    $ nteye = "front02"
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    p "pero corro el riesgo de morir?"

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "No,"

    $ nteye = "right01"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "no creo que en tu caso ocurra eso."

    $ nteye = "front01"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    p "¿En mi caso?"

    $ nteye = "front03"
    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Si fueras un humano normal,"

    if night04_pedrera_blowjob_DONE:

        $ nteye = "front02"
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows angryx01
        call n_closefromup_tears_tears
        with dissolve

        ne "ya habrías muerto después de la primera mamada que te hice,"

        $ nteye = "front02"
        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows angryx01
        call n_closefromup_tears_tears
        with dissolve

        if p_ao_started:

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx005
            show neus_exp_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "sin mencionar lo que me obligaste hacer ayer..."

            $ nteye = "front05"
            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            pt "Yo no lo llamaría obligarla..."

        else:

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx005
            show neus_exp_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "sin mencionar lo que hicimos ayer..."

    elif p_ao_started:

        $ nteye = "front05"
        show neus_exp_mouth sad_Talkingx005
        show neus_exp_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "ya habrías muerto después de lo que te hice ayer..."

    else:

        $ nteye = "front04"
        show neus_exp_mouth sad_Talkingx005
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "ya habrías muerto después de lo de ayer."

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Así que es obvio que,"

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "a pesar de que aún no has pasado por ningún aquelarre,"

    $ nteye = "front06"
    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "tu capacidad de curación es sobrehumana."

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front01"
    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "¿Eso significa que no me pasará nada?"

    $ nteye = "right01"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Tampoco he dicho eso."

    $ nteye = "front00"
    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Entonces?!"

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Creo que si la ingieres,"

    $ nteye = "front06"
    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "te pasarás por lo menos una semana sin poder levantarte."

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front01"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿UNA SEMANA?!"

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "left00"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with Dissolve(0.2)

    d "¿Estás diciendo que no podrá follarnos en una semana?"

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "right01"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "Seguiré sacándole esperma, obviamente."

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Al menos yo lo voy a necesitar."

    $ df_eye = "left05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero no podrá follarnos."

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab

    $ nteye = "right01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    d "Entonces que no se lo tome,"

    extend " joder."

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "right04"
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "No sé si seré capaz de sacarle más de una corrida en su estado actual,"

    $ df_eye = "left03"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "por mucho que lo intente y yo me esfuerce..."

    $ df_eye = "left05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "front02"
    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero podemos intentarlo."

    $ df_eye = "front02"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "front03"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque prefiero que sea su elección."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "front02"
    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows angryx02
    call n_closefromup_tears_tears
    with Dissolve(0.2)

    ne "Pero hay algo que quiero dejar bien claro."

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "¿El qué?"

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Podrás follarnos a las dos;"

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "pero bajo ningún concepto debo llegar al orgasmo."

    $ nteye = "front05"
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front01"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando te diga que pares,"

    extend " te paras de inmediato."

    $ nteye = "front00"
    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Me has entendido?"

    $ nteye = "front04"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    # QUESTION?

    menu:

        pt "Si me dice que pare, tengo que parar..."

        "Pero, ¿por qué?":
            call p_Help

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Por que si acabo teniendo un orgasmo,"

            $ nteye = "right01"
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Padre sabrá dónde estamos"

            $ nteye = "right02"
            show neus_exp_mouth sad_Talkingx07
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "y no habrá rincón ni cueva en el mundo"

            $ nteye = "right03"
            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "que sea capaz de escondernos de él."

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            ne "Hoy no."

            $ nteye = "front04"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help

            $ nteye = "front04"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

label day06_neusDidac_TellMeYouUnderstand:

### 
    
    pause 0.2

    $ nteye = "front03"
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Dime que lo entiendes;"

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "o solo podrás follarte a Dídac."

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ##

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with fade

    $ day06_neusDidac_TellMeYouUnderstand_NoAnswer = False

    menu day06_neusDidac_TellMeYouUnderstand_Question:

        pt "¿Me tengo que beber su sangre?"

        "Lo siento, pero prefiero no beber tu sangre.":
            call p_Help

            jump day06_neusDidac_noBlood_begin

        "Lo entiendo.":

            jump day06_neusDidac_IUnderstand

        "Me beberé tu sangre, pero no puedo prometerte que me detenga cuando vea que estás al borde del orgasmo.":
            call p_Help

            # NOT FIIIIIIINISHED
            # does it need to be writen before getting there?
            # Here Neus tell him you can't have any other option but doing without drinking blood, so you decide.
            jump day06_neusDidac_noBlood_begin

        "..." if day06_neusDidac_TellMeYouUnderstand_NoAnswer == False:
            call p_Help

            $ day06_neusDidac_TellMeYouUnderstand_NoAnswer = True

            $ df_eye = "left02"
            show didacf_mouth sadbiting_Silentx03
            show didacf_eyebrows sadx01
            call dfeye_lab

            $ nteye = "front02"
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Hablo en serio [protname]."

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Dame una respuesta."

            $ df_eye = "front03"
            show didacf_mouth sadbiting_Silentx05
            show didacf_eyebrows sadx03
            call dfeye_lab

            $ nteye = "front04"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusDidac_TellMeYouUnderstand_Question

label day06_neusDidac_IUnderstand:

    $ df_eye = "left04"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Me alegra escuchar eso."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx005
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex03
    call n_closefromup_tears_tears
    with dissolve

    d "Tampoco me hubiera quejado si solo me hubiera follado a mi."

    $ df_eye = "left04"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Mira que eres golfa..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    d "Simplemente estoy cachonda,"

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows serious
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    d "y además,"

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex03
    call n_closefromup_tears_tears
    with dissolve

    d "tú ya llevas rato follándotelo."

    # CONDITIONAL?

    if p_neus.cumReceived == "vaginal":

        $ df_eye = "left05"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "front01"
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        $ nblush += 1

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex02
        call dfeye_lab

        $ nteye = "right01"
        show neus_exp_mouth sad_Talkingx001
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Tampoco hace tanto rato..."

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx03
        call dfeye_lab

        $ nteye = "right00"
        show neus_exp_mouth sadbiting_Silentx01
        show neus_exp_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        d "¡Por lo menos media hora!"

        $ nblush += 1

        $ df_eye = "left04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows suspiciousx02
        call dfeye_lab

        $ nteye = "right04"
        show neus_exp_mouth happybiting_Silentx04
        show neus_exp_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

    else:

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex02
        call dfeye_lab

        $ nteye = "front08"
        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows angryx01
        call n_closefromup_tears_tears
        with dissolve

        ne "¡Solo he estado frotándome con su polla,"

        $ df_eye = "left04"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "left02"
        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "aún no me la he llegado a meter dentro!"

        $ df_eye = "left03"
        show didacf_mouth sad_Silentx002
        show didacf_eyebrows surprisex01
        call dfeye_lab

        $ nteye = "left00"
        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        d "Por que no has querido..."

        $ df_eye = "left05"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab

        $ nteye = "right01"
        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

    call day06_bloodDrink

    jump day06_neusDidac_afterDrink

####

label day06_neusDidac_afterDrink:

    # Neus alone

    $ nteye = "left02"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    d "¡¿Y bien?!"

    $ nteye = "left00"
    show n_closefromup_mouth sadbiting_Silentx01
    show n_closefromup_eyebrows surprisex03
    call n_closefromup_tears_tears
    with dissolve

    d "¡¿Cuando empiezas?!"

    $ d06_threesomeNeus = False
    $ d06_threesomeBigNeus = False
    $ d06_threesomeDidac = True
    $ d06_threesomeTxell = False


    scene d06_backThreesome_comp:
        truecenter
        zoom 2.0 xpos 1.35 ypos -1.0 # dFeet.
        easein_quad 10.0 zoom 1.9 xpos 1.92 ypos 0.78 # Pussy
        #zoom 2.0 xpos 1.35 ypos -1.0 # dFeet.
        #zoom 1.9 xpos 1.92 ypos 0.78 # Pussy
        #zoom 1.5 xpos 1.45 ypos 1.15 # Face
        #zoom 0.8 xpos 1.06 ypos 0.62 # dGeneralNoFeet
        #zoom 0.4 xpos 0.5 ypos 0.5 # Complete Image
    with fade

    n "Apartas la vista para fijarte en Dídac."

    n "El cual se encuentra a cuatro patas sobre la cama agitando sus caderas con su culo apuntando hacia ti."

    p "..."

    ne "La sutileza no es tu punto fuerte,"

    ne "¿verdad?"

    show d06_backThreesome_comp:
        easein_quad 5.0 zoom 1.5 xpos 1.45 ypos 1.15 # Face

    d "¡Que sutileza ni que hostias!"

    d "¡Llevo cachonda todo el puto día!"

    d "Fóllame de una vez."

    show d06_backThreesome_comp:
        ease_quad 5.0 zoom 0.58 xpos 0.9 ypos 0.47 # dCOMPLETE

    window hide dissolve
    pause

    scene day06
    with fade

    n "Te miras la polla y no la ves tan rojiza como antes,"

    n "pero sigue estando venosa y dura como una piedra."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "down04"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade

    n "Tu mirada se fija entonces en [neusname],"

    $ nteye = "down05"
    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    n "la cual está también mirándote la parte inferior mientras se muerde los labios."

    $ nteye = "front00"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "Parece que Dídac no es la única persona poco sutil..."

    $ nteye = "right02"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Que no lo diga tan alegremente como ella,"

    $ nteye = "front05"
    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "no significa que no me esté muriendo de ganas también."

    $ nteye = "down05"
    show neus_exp_mouth happybiting_Silentx07
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ d06_threesomeNeus = True

    scene d06_backThreesome_comp:
        truecenter
        zoom 2.0 xpos 0.88 ypos -1.0 # nLeftFeet
        ease 7.0 zoom 1.75 xpos 0.5 ypos 0.55 # Ass
    with fade

    # progcheck "General"
    # show d06_backThreesome_comp:
    #     zoom 2.0 xpos 0.88 ypos -1.0 # nLeftFeet
    # progcheck "Feet"
    # show d06_backThreesome_comp:
    #     zoom 1.75 xpos 0.5 ypos 0.55 # Ass
    # progcheck "AssFace"
    # show d06_backThreesome_comp:
    #     zoom 1.4 xpos 0.5 ypos 0.8 # Face-Ass
    # progcheck "AssFace"
    # show d06_backThreesome_comp:
    #     zoom 0.64 xpos 0.5 ypos 0.37 # Neus Complete
    # progcheck "NeusComplete"
    # show d06_backThreesome_comp:
    #     zoom 0.55 xpos 0.7 ypos 0.45 # Neus+Didac
    # progcheck "NeusDidac"


    n "Se desliza a gatas por la cama y se pone a su lado a cuatro patas"

    n "mostrándote su trasero del mismo modo que ella."

    ne "¿Y bien?"

    show d06_backThreesome_comp:
        ease 5.0 zoom 1.4 xpos 0.5 ypos 0.8 # Face-Ass

    ne "¿Por quien vas a empezar?"

    show d06_backThreesome_comp:
        zoom 1.5 xpos 1.45 ypos 1.15 # DFace
    with dissolve

    d "Mucho criticarme,"

    d "pero tampoco es que estés haciendo algo distinto."

    show d06_backThreesome_comp:
        zoom 1.4 xpos 0.5 ypos 0.8 # NFace-Ass
    with dissolve

    ne "Es obvio que le estás poniendo cachondo."

    ne "Yo no voy a ser menos."

    show d06_backThreesome_comp:
        zoom 1.5 xpos 1.45 ypos 1.15 # DFace
    with dissolve

    d "Te faltan tetas y culo para hacerme competencia."

    show d06_backThreesome_comp:
        zoom 1.4 xpos 0.5 ypos 0.8 # NFace-Ass
        ease 5.0 zoom 0.55 xpos 0.7 ypos 0.45 # Neus+Didac
    with dissolve

    ne "..."

    ne "Con que esas tenemos, ¿verdad?"

    show d06_backThreesome_comp:
        ease 5.0 zoom 1.75 xpos 0.5 ypos 0.55 # Ass
        
    ne "Ghnn..."

    show d06_backThreesome_comp:
        zoom 1.75 xpos 0.5 ypos 0.55
    with vpunch

    d "¿Euh?"

    # Didac and Neus at doggystyle. (Neus Big)

    $ d06_threesomeNeus = False
    $ d06_threesomeBigNeus = True
    # $ d06_threesomeDidac = True
    # $ d06_threesomeTxell = False

    show d06_backThreesome_comp:
        ease_quad 8.0 zoom 1.4 xpos 0.5 ypos 1.05 # NBIGFace-Ass
    with Dissolve(5.0)

    n "De su piel emana un vapor denso al mismo tiempo que su piel empieza a agitarse y vibrar."

    d "¿Qué-"

    extend "qué estás haciendo?"

    n "Tienes la sensación de que su cuerpo aumenta de tamaño."

    d "¡¿Qué diablos?!"

    show d06_backThreesome_comp:
        easein_quad 10.0 zoom 0.55 xpos 0.7 ypos 0.45 # Neus+Didac

    n "Su cuerpo es ahora mayor que el de Dídac,"

    n "con un trasero más voluminoso, unas piernas más largas,"

    n "unos pechos ligeramente más grandes"

    n "y un rostro bastante más adulto."

    scene p_ao_n_behindLook_comp:
        truecenter
        zoom 1.0 xpos 1.0 ypos 0.5 #Her eye Close
        easein 8.0 zoom 0.5 xpos 0.75 ypos 0.5 #Her eye Far
    with fade_long1s

    ne "¿Así estoy mejor?"

    if p_ao_started:

        pt "Es la misma transformación que hizo ayer."

    else:

        pt "Se parece a la mujer que vi en ese hotel tan extraño..."


    scene d06_backThreesome_comp:
        truecenter
        zoom 1.4 xpos 0.5 ypos 1.05 # NBIGFace-Ass
    with hpunch
    ne "¡Ughh...!"

    #scene day06 # Didac and Neus at doggystyle. (Neus small)

    show d06_backThreesome_comp:
        ease 8.0 zoom 0.55 xpos 0.7 ypos 0.45 # Neus+Didac

    pause 2.0

    $ d06_threesomeNeus = True
    $ d06_threesomeBigNeus = False

    show d06_backThreesome_comp
    with Dissolve(5.0)

    n "Su cuerpo vuelve a desprender humo mientras su piel se agita y vibra de igual modo que antes."

    n "A medida que el vapor se disipa, descubres su cuerpo otra vez del mismo tamaño y forma en el que estaba."

    d "¡¿Qué coño ha sido esto?!"

    d "¡¿Soy yo,"

    d "o antes parecía otra mujer?!"

    if p_ao_started:

        p "Sí Dídac, antes lucía distinta,"

        p "no te lo has imaginado."

    else:

        p "Eso parece."

    ne "..."

    show d06_backThreesome_comp:
        zoom 1.4 xpos 0.5 ypos 0.8 # NFace-Ass
    with dissolve

    ne "Lo siento..."

    ne "Pensaba que podría aguantar más tiempo en ese estado."

    ne "Pero con la poca energía que absorbo de tu esperma,"

    ne "no tengo la suficiente para este tipo de transformaciones."

    ne "Me temo que tendrás que conformarte con mi cuerpo actual." 

    show d06_backThreesome_comp:
        ease 8.0 zoom 0.55 xpos 0.7 ypos 0.45 # Neus+Didac

    # Choice Start with Neus.

    $ day06_neusDidac_startWithNeus_Cond = False

    menu:

        pt "Conformarme con su cuerpo actual..."

        "<Empezar con [neusname]>":
            call p_Help
            $pl.ch_pts("np",2)
            $pl.ch_pts("dp",-2)

            $ day06_neusDidac_startWithNeus_Cond = True

            jump day06_neusDidac_startSex

        "<Empezar con Dídac>":
            call p_Help
            $pl.ch_pts("np",-2)
            $pl.ch_pts("dp",2)

            $ day06_neusDidac_startWithNeus_Cond = False

            jump day06_neusDidac_startSex


label day06_neusDidac_startSex:

    scene day06
    with fade

    if day06_neusDidac_startWithNeus_Cond:

        p "No tienes ninguna necesidad de hacer nada para complacerme."

        p "Me gustas tal y como eres."

    n "Acercas tus labios a su pequeño trasero."

    n "Mientras le acaricias las piernas,"

    n "le besas suavemente la suave piel de uno de sus glúteos."

    if day06_neusDidac_startWithNeus_Cond:

        d "¡Oye!"

        d "¡Eso de usar la pena como recurso para que empiece contigo es muy rastrero!"
        
    else:

        d "¡Así me gusta!"

        ne "..."

    n "Aproximas tu rostro a su húmeda entrepierna para acariciar el borde de su vagina con tus labios,"

    n "mientras acercas tu mano derecha a la parte superior de su pubis"

    n "y empiezas a acariciarle suavemente el clítoris."

    if day06_neusDidac_startWithNeus_Cond:

        ne "Hmm..."

        ne "No-"

        extend "no es por eso..."

        ne "que lo he hecho..."

    else:

        d "Hmmm..."

        ne "De todos modos acabaremos compartiendo su corrida."

        d "Dirás lo que quieras,"

        d "pero ha preferido empezar conmigo."

        ne "..."

        d "No te lo tomes a mal mujer."

    n "Sumerges tu rostro en sus labios vaginales y penetras su vagina con tu lengua."

    if day06_neusDidac_startWithNeus_Cond:

        ne "¡Hhmm...!"

        d "Ya..."

        d "No te lo crees ni tú."

    else:

        d "Fóllame de una vez."

    $ day06_neusDidac_DidacCare = False
    $ day06_neusDidac_NeusCare = False

    menu:

        pt "¿Debería hacer algo con ella?"

        "<Darle también cariño a Dídac con tu mano>" if day06_neusDidac_startWithNeus_Cond:
            call p_Help
            #$pl.ch_pts("np",1)
            $pl.ch_pts("dp",2)

            $ day06_neusDidac_DidacCare = True

        "<Ignorar a Dídac>" if day06_neusDidac_startWithNeus_Cond:
            call p_Help

            $ day06_neusDidac_DidacCare = False

        "<Darle también cariño a [neusname] con tu mano>" if not day06_neusDidac_startWithNeus_Cond:
            call p_Help
            #$pl.ch_pts("np",1)
            $pl.ch_pts("np",2)

            $ day06_neusDidac_NeusCare = True

        "<Ignorar a [neusname]>" if not day06_neusDidac_startWithNeus_Cond:
            call p_Help

            $ day06_neusDidac_NeusCare = False

    if day06_neusDidac_DidacCare or day06_neusDidac_NeusCare:

        n "Con tu mano libre,"

    if day06_neusDidac_DidacCare:

        d "¡Ghmm!"

        n "Metes sin misericordia tus dedos en el húmedo y caliente coño de Dídac."

        d "Ahhmm..."

    elif day06_neusDidac_NeusCare:

        ne "¡Hhmmm...!"

        n "Metes sin misericordia tus dedos en el empapado y ardiente coño de [neusname]."

        ne "Ahmmm..."

    ne "[protname],"

    ne "deberías estar follándonos y no estar usando tu lengua."

    if day06_neusDidac_startWithNeus_Cond:

        if not day06_neusDidac_DidacCare:

            d "Secundo la opinión de la morenita."

            ne "..."

    else:

        d "Eso lo dices porque no la está usando contigo..."

        ne "¡No es por eso!"

    ne "Esta energía no te va a durar toda la noche."

    if day06_neusDidac_startWithNeus_Cond:

        ne "¡Hhhmmm...!"

        n "Remueves tu lengua en su carnoso, viscoso, y ardiente interior."

    else:

        d "¡Hhmmm...!"

        n "Remueves tu lengua en su carnoso y húmedo interior."

    if day06_neusDidac_startWithNeus_Cond:

        if day06_neusDidac_DidacCare:

            d "HHmmfghm..."

            n "Al mismo tiempo que introduces tus cuatro dedos hasta los nudillos en el coño de Dídac."

            d "Aunque confieso que me estás poniendo cachonda,"

            d "prefiero tu polla, cabrón."

        else:

            d "Me siento un tanto ignorada..."

    else:

        if day06_neusDidac_NeusCare:

            ne "Hmm..."

            n "Al mismo tiempo que introduces tus cuatro dedos hasta los nudillos en el estrecho coño de [neusname]."

            d "Aunque confieso que sabes usar esa jodida lengua tuya,"

            d "prefiero tu polla, cabrón."

        else:

            ne "..."

    n "Apartas tu lengua y acercas tu polla a su encharcada entrepierna."

    $ day06_neusDidac_NeusSexVag = False
    $ day06_neusDidac_DidacSexVag = False

    menu:

        pt "¿Por dónde?"

        "<Sexo vaginal>":
            call p_Help
            $pl.ch_pts("np",2)

            if day06_neusDidac_NeusCare:

                $ day06_neusDidac_NeusSexVag = True

            else:

                $ day06_neusDidac_DidacSexVag = True


        "<Sexo anal>":
            call p_Help
            $pl.ch_pts("np",2)

            if day06_neusDidac_NeusCare:

                $ day06_neusDidac_NeusSexVag = False

            else:

                $ day06_neusDidac_DidacSexVag = False


    ne "[protname]..."

    n "Agarrándola por una de sus nalgas,"

    if day06_neusDidac_startWithNeus_Cond:

        n "empiezas a introducir tu terso y duro miembro en su estrecho y ardiente interior."

    else:

        n "empiezas a introducir tu terso y duro miembro en su estrecho y caliente interior."

    n "Casi sin dificultad logras hundir casi la mitad de tu miembro"

    if day06_neusDidac_NeusSexVag or day06_neusDidac_DidacSexVag:

        n "en su ceñida y pequeña vagina."

    else:

        n "en su ceñido y estrecho agujero anal."

    if day06_neusDidac_startWithNeus_Cond:

        ne "Hhmffhmm..."

        n "[neusname] se agarra a la sábana mientras ahoga sus gemidos bajo la tela."

    else:

        d "Hhhfmm..."

        n "Dídac se agarra a la sábana mientras ahoga sus gemidos bajo la tela."

    if day06_neusDidac_DidacCare or day06_neusDidac_NeusCare:

        n "A medida que vas deslizando tu polla erecta como una piedra en su interior,"

        if day06_neusDidac_NeusCare:

            n "sigues agitando tus dedos en la vagina de tu ex-compañero de piso."

        else:

            n "sigues agitando tus dedos en la vagina de la morenita."

    if day06_neusDidac_startWithNeus_Cond:

        d "Hmm..."

        d "Es increíble que te llegue a caber un pollón como el suyo con lo diminuta que eres."

        ne "Ahhmm..."

        ne "¿Por-"

        extend "por qué "

        extend "no te callas...?"

    else:

        d "Hmm..."

        if day06_neusDidac_DidacSexVag:

            ne "Parece que te gusta..."

            d "Me encanta..."

        else:

            ne "Pensaba que habías dicho que por detrás no te gustaba."

            d "¿Por qué no te callas?"

            ne "..."

            ne "¿Tanto te gusta?"

            d "Hhhhmmfmm..."

        d "¿Acaso no te gustaría estar ahora en mi lugar?"

        ne "..."

    d "¿Es que he dicho alguna mentira?"

    d "Aparentas ser cándida e ingenua,"

    d "pero en el fondo eres más zorra que la rubia y yo juntas."

    n "Los ojos de [neusname] se fijan con brillo e intensidad en el rostro de Dídac."

    d "Oye..."

    d "Tampoco hace falta tomárselo..."

    n "Con una mano le agarra su longevo pelo y arrastra su rostro al suyo."

    with hpunch
    with hpunch
    d "¡Ghmmm!"

    n "Con lascivia y desenfreno, entremezclan sus lenguas."

    if day06_neusDidac_NeusSexVag or day06_neusDidac_DidacSexVag:

        if day06_neusDidac_NeusSexVag:

            n "A medida que profundizas más en su ardiente vagina,"

            n "sientes su carne palpitar y estrujarte la polla casi como si lo hiciera expresamente."

        else:

            n "A medida que profundizas más en su cálida vagina,"

            n "sientes que se va dilatando y humedeciendo cada vez más."

    else:

        if day06_neusDidac_startWithNeus_Cond:

            n "A medida que profundizas más en su estrecho y ardiente trasero,"

            n "sientes su carne vibrar y estrujarte la polla casi como si lo hiciera expresamente."

        else:

            n "A medida que profundizas más en su estrecho y cálido trasero,"

            n "sientes que se va volviendo cada vez menos hostil."

    if day06_neusDidac_startWithNeus_Cond:
        ne "¡Ghmm...!"

    else:

        d "¡Ghhmm...!"

    n "Entre sus gemidos y el sonido de su lengua mezclándose con otra,"

    if ay06_neusDidac_NeusSexVag or day06_neusDidac_DidacSexVag:

        n "tu polla topa en lo que parece su cuello uterino, impidiéndote penetrar más profundamente."

    else:

        n "tu polla topa con lo que parece la pared de su intestino grueso."

    n "Así que decides deslizar tranquilamente tu miembro de modo horizontal."

    pt "Quizás dentro de un rato esté algo más dilatada..."

    if day06_neusDidac_startWithNeus_Cond:

        ne "*Aahhmm...*"

        n "Suelta ese gemido, permitiendo a Dídac finalmente respirar después de semejante beso con lengua."

    else:

        d "*Ahhhmm...*"

        n "Finalmente suelta a Dídac permitiéndole respirar."

    d "*Aaahh-Ahhh...*"

    d "¿A qué ha venido esto?"

    d "¿Es que te ha puesto cachonda que te llamara zorra?"

    ne "Sí."

    ne "Me ha puesto muy cachonda."

    d "..."

    d "No me esperaba tanta sinceridad..."

    $ day06_neusDidac_KissAllowed = False

    if not gensex_YoureAMonster:

        ne "[protname]..."

        ne "Lo siento,"

        ne "quizás debería haberte pedido permiso,"

        ne "pero..."

        d "¿Qué eres?"

        d "¿Su mascota?"

        ne "¡Por supuesto que no!"

        d "¿Entonces por qué coño le pides permiso?"

        ne "..."

        if gensex_ILoveYouNeus:

            ne "Por que le amo."

        else:

            ne "¡Se trata de respeto y confianza por la otra persona!"

        d "Tsskk..."

        d "Lo que tú digas."

        ne "Tampoco pretendo que tú lo entiendas..."

        d "¡¿Qué insinúas?!"

        ne "¿Te molesta que la haya besado?"

        menu:

            pt "¿Me molesta que se besen?"

            "Por supuesto que no.":
                call p_Help
                $pl.ch_pts("np",1)
                $pl.ch_pts("dp",1)

                $ day06_neusDidac_KissAllowed = True

                ne "Me alegra que te lo tomes así."

            "Todo lo contrario, me ha encantado.":
                call p_Help
                $pl.ch_pts("np",2)
                $pl.ch_pts("dp",1)

                $ day06_neusDidac_KissAllowed = True

                ne "..."

                d "Y luego la única pervertida soy yo..."

                ne "Como si no lo hubieras disfrutado."

                d "Por eso he dicho \"la única\"..."

                ne "Hmmm..."

            "La verdad es que preferiría que no lo hicieras.":
                call p_Help
                #$pl.ch_pts("np",1)
                $pl.ch_pts("dp",-4)

                $ day06_neusDidac_KissAllowed = False

                ne "..."

                d "¡Aguafiestas!"

                p "¿Desde cuándo te gusta [neusname]?"

                d "..."

                d "No es que me encante..."

                d "Pero la zorra sabe dar besos."

                ne "..."

                ne "¿Se supone que eso es un cumplido?"

                d "Tómatelo cómo prefieras."

                ne "Hmmm..."

                ne "Te prometo que intentaré controlarme."

                p "Gracias."

    else:

        $ day06_neusDidac_KissAllowed = True

    jump day06_neusDidac_afterKiss

label day06_neusDidac_afterKiss:

    if day06_neusDidac_KissAllowed:

        n "Vuelve agarrarla de la cabeza y sigue besándola con fervor."

    pt "Empieza a hacer frío,"

    if day06_neusDidac_startWithNeus_Cond:

        pt "y ella cada vez está más caliente..."

    else:

        if day06_neusDidac_NeusCare:

            pt "Y su coño está tan caliente que me está quemando los dedos..."

        else:

            pt "Y parece que [neusname] se está calentando cada vez más..."

    if day06_neusDidac_DidacCare:

        n "Tu mano está completamente empapada en los jugos de Dídac."

    d "Hmmm..."

    n "Aceleras el ritmo de tus caderas"

    if day06_neusDidac_startWithNeus_Cond:

        ne "¡Ghhmm...!"

    else:

        d "¡Ghhmmm...!"

    n "al sentir su interior cada vez menos hostil."

    $ day06_neusDidac_CumInDidac_Cond = False

    if day06_neusDidac_startWithNeus_Cond or day06_neusDidac_NeusCare:

        jump day06_neusDidac_NeusAskStop

    else:

        jump day06_neusDidac_CumInDidac

label day06_neusDidac_NeusAskStop:

    ne "Para..."

    n "Empiezas a oír a lo lejos el sonido de unos familiares susurros."

    if day06_neusDidac_KissAllowed:

        d "¡Pero si has sido tú quien ha empezado a morrearme!"

    $ day06_neusDidac_Stopped = False

    menu:

        pt "¿Debería pararme?"

        "<Detenerte>":
            call p_Help

            $pl.ch_pts("np",1)
            $pl.ch_pts("dp",-1)

            $ day06_neusDidac_Stopped = True

            if day06_neusDidac_startWithNeus_Cond:

                n "Detienes en seco tu movimiento de caderas."

            else:

                # day06_neusDidac_DidacCare Should be False.

                n "Detienes la mano dónde tenías tus cuatro dedos ardiendo por su infernal interior."

                ne "*Aahhmm...*"

                d "Hmmm..."

                ne "Gracias."

                jump day06_neusDidac_CumInDidac

            # day06_neusDidac_DidacCare Should be True.

            d "..."

            d "¡¿Euh?!"

            d "Que pares de follártela a ella lo entiendo,"

            $ Pedrera_char_Cond = "DidacClose"
            call Pedrera_char_lab

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows suspiciousx03
            call dfeye_lab

            # $ nteye = "front05"
            # show neus_exp_mouth sadbiting_Silentx05
            # show neus_exp_eyebrows sadx04
            # call n_closefromup_tears_tears
            with vpunch

            d "¡¿pero por qué cojones no siento nada en mi coño?!"

            $ Pedrera_char_Cond = "NeusDidac_close"
            call Pedrera_char_lab

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx03
            call dfeye_lab

            $ nteye = "left05"
            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx04
            call n_closefromup_tears_tears
            with Dissolve(2.0)

            jump day06_neusDidac_afterStop
                # d "¡¿Qué cojones es esto?!"
                # n "Un montón de orbes rojos os rodean en la semi-oscuridad de la habitación."
                # p "¿Dídac también puede verlos?"

        "<Continuar>":
            call p_Help
            $pl.ch_pts("np",-1)
            $pl.ch_pts("dp",1)

            jump day06_neusDidac_ignoreNeus


label day06_neusDidac_CumInDidac:

    $ day06_neusDidac_CumInDidac_Cond = True

    d "Aaahhmm..."

    p "¿Qué...?"

    $ day06_morning_Didac_orgasms += 1
    with vpunch
    # Conditional, Vaginal

    if day06_neusDidac_DidacSexVag:

        n "Un enorme chorro te empapa la barriga y las piernas."

    else:

        n "Un enorme chorro te empapa las piernas."

    d "¡Joder!"

    p "..."

    ne "Parece que no mentías cuando decías que ibas tan cachonda."

    d "Yo no miento tanto como otras personas..."

    ne "..."

    ne "Hmm..."

    ne "[protname],"

    ne "¿por qué te has parado?"

    ne "Síguele dando duro a esta perra."

    if day06_neusDidac_DidacSexVag:

        d "Por una vez estoy de acuerdo con la enanita."

        ne "Hmm..."

    else:

        d "Aunque sea por el culo..."

        ne "El orgasmo lo has tenido igual,"

        ne "así que tampoco creo que te disguste tanto."

        d "Tssk..."

    d "¡AGhhmm...!"

    d "Dios..."

    n "Agarrándola rudamente de las nalgas con ambas manos,"

    n "embistes sin piedad contra sus nalgas."

    d "Seehh..."

    menu:

        "<Azotarle las nalgas>":
            call p_Help

            $ day06_morning_Didac_buttockSlaps += 1

        "...":
            call p_Help

            pass

    if day06_morning_Didac_buttockSlaps > 0:

        d "¡Auch!"

        d "¡¿Por qué coño me azotas?!"

        if p_didac.buttockSlaps_received > 1:

            p "Ayer no pareció que te disgustara tanto."

            ne "Eso es verdad."

        else:

            ne "Tampoco parece que te hay disgustado tanto del modo en que has gemido.."

        d "Tssk..."

        d "Iros a tomar por el culo."

        ne "Eso es lo que te está haciendo."

        d "¡Niña!"

        d "Estás más bonita cuando te callas."

        ne "Te sorprendería saber cuantos años tengo realmente."

        d "Eso no quita que pareces una..."

        $ day06_morning_Didac_buttockSlaps += 1

        d "¡AUCH!"

        d "Puto [protname]."

        p "Tú también estás mejor calladita."

        d "Tsskk..."

        d "Aahhmm..."

        pt "No es posible..."

        ne "¿Tanto te gusta que te azoten?"

        d "Ca-"

        extend "calla..."

    else:

        ne "Parece que te está gustando bastante..."

        d "Te encantaría estar en mi lugar, ¿verdad?"

        ne "..."

        d "Vaya pollón tienes cabrón..."

        ne "Hmm..."

        ne "Eso es verdad."

        d "¿Y lo otro no?"

        ne "¡Obviamente que también!"

        d "AaAHhhmm..."

        ne "¿Seguro que no le puedes dar más duro?"

        p "¡No soy una máquina!"

        ne "Quizás necesites algo de ayuda..."

        p "¿Cómo...?"

        n "Sientes el los pequeños pero tersos pechos desnudo de [neusname] en tu espalda,"

        n "para luego sentir su ardiente entrepierna acariciando tus nalgas."

        ne "Déjame follar un poco a esta perra."

        p "¿A qué te...?"

        n "Alarga sus brazos para agarrarse cómo puede a las caderas de Dídac."

        ne "A ver si te gusta esto..."

        if p_ao_started:

            p "No estás pensando en usar lo mismo de ayer, verdad?"

            ne "No!"

        else:

            p "No estarás pensando hacer lo que creo que estás pensando hacer, ¿verdad?"

            ne "Hmm..."

            ne "No sé..."

            ne "¿En qué estás pensando...?"

            ne "Quieres que te folle también el trasero con una sorpresa que me sauqe de las piernas?"

        ne "Desgraciadamente,"

        ne "aunque me lo pidieras,"

        ne "eso me requiere demasiada energía."

        ne "Lo que quiero es ver como reacciona la perra esta a una embestida de las mías..."

        pt "¿De las suyas?"

        n "Empieza a empujarte suavemente las nalgas con sus caderas forzándote a penetrar de nuevo a Dídac."

        n "Sin embargo, lo que empieza como algo juguetón y casi inocente,"

        n "va volviéndose en cada nueva embestida en algo más rudo y acelerado."

        p "Euh..."

        n "Hasta el punto en que ejerce una fuerza tan brusca"

        n "que empiezas a sentir el huesos de sus caderas clavándose en tus nalgas."

        p "[neusname]..."

        n "Su movimiento se vuelve tan brusco y acelerado que apenas eres capaz de seguirle el ritmo"

        n "siendo finalmente ella quien está dominando la situación"

        n "y quien realmente está follándose -de forma indirecta- a Dídac."

        d "Jodeeer..."

        n "Su celeridad y brusquedad aumenta de tal modo,"

        n "que tienes la sensación que tus caderas acabarán por aplastarse del todo en medio de esas dos."

        n "Dídac a duras penas es capaz de mantenerse a cuatro patas"

        n "mientras la ves agarrándose dónde puede mientras muerde la sábana. "

        d "¡COÑOOOOO!"

    $ day06_morning_Didac_orgasms += 1
    with vpunch
    d "¡Uuughhmmm....!"

    n "Otro enorme y cálido chorro vuelve a empaparte las piernas."

    d "Jodeeeer..."

    if day06_morning_Didac_buttockSlaps == 0:

        n "[neusname] finalmente se detiene."

    ne "Hmm..."

    if day06_morning_Didac_buttockSlaps == 0:

        p "[neusname]..."

        p "Me has dejado el culo hecho mierda..."

        ne "No te quejes tanto..."

        if p_neus.anal_received > 3:

            if p_neus.analDeep_received > 2:

                ne "Tú ayer me la metiste entera por detrás."

            else:

                ne "Tú ayer me dejaste el culo peor."

            p "No es exactamente lo mismo..."

            ne "¿Prefieres que te haga lo otro?"

            if p_ao_started:

                p "Me acabas de decir que te toma demasiada energía."

                ne "Hmm..."

                ne "Eso es verdad..."

        p "..."

        pt "¡Si hubiera seguido así me hubiera quedado inválido!"

    n "La ves mordiéndose el labio sin quitar sus ojos de tu polla aún en el interior de Dídac."

    ne "[protname]..."

    ne "¿Te molestaría si me pongo debajo de ella y paso mi lengua por su entrepierna?"

    ne "Así de paso quizás te ayude a correrte más pronto..."

    menu:

        "Por supuesto que no me molestaría.":
            call p_Help

            $ day06_morning_Neus_lickingUnder = "Didac"

        "Preferiría que no.":
            call p_Help

            $ day06_morning_Neus_lickingUnder = ""

label day06_neusDidac_CumInDidac_AfterDidacOrgasm:

    if day06_morning_Neus_lickingUnder == "Didac":

        p "Por supuesto que no me molestaría."

        ne "Así me gusta."

    else:

        ne "..."

        ne "Como prefieras..."

    d "Oye..."

    d "¿Y mi opinión no cuenta para nada?"

    if day06_morning_Neus_lickingUnder == "Didac":
        pass
    else:
        jump day06_neusDidac_CumInDidac_noCunnilingus

    n "Ves como escurre su cabeza entre sus piernas"

    n "y acerca su lengua por su empapada entrepierna deslizándola por esos viscosos jugos."

    d "Hmmm..."

    menu:

        "¿Por qué no la ayudas tú también?":
            $pl.ch_pts("np",1)

            $ day06_morning_Didac_lickingUnder = "Neus"

        "...":
            call p_Help

            $ day06_morning_Didac_lickingUnder = ""

    if day06_morning_Didac_lickingUnder == "Neus":

        p "¿O es que ya no te va eso?"

        d "Tssk..."

        d "Que no te quepa la menor duda de que le encantaría,"

        d "pero es tan bajita que ni siquiera..."

        with hpunch
        d "*¡AAAhhmm...!*"

    # IF pussy sex

    n "Su longeva lengua juguetea con su clítoris"

    n "al mismo tiempo que intenta acariciar la superficie inferior de tu polla"

    n "cuando esta no se encuentra en su interior."

    d "¡Joder!"

    d "¡¿Por qué coño tienes la lengua tan caliente?!"

    ne "Lo dices como si tú no estuvieras también caliente..."

    d "¡Pero es que tú estás literalmente quemando!"

    ne "Eso es porque voy muy cachonda..."

    pt "La verdad es que con apenas habérmela rozado,"

    pt "ya siento lo ardiente que tiene la lengua..."

    if day06_morning_Didac_lickingUnder == "Neus":

        n "Ves que Dídac hace un esfuerzo para intentar arquear su espalda"

        n "y acercar su rostro a la entrepierna de [neusname]."

    d "AAAhhmmm..."

    if day06_morning_Didac_lickingUnder == "Neus":

        n "Pero esta acelera el ritmo de sus lengüetazos"

    else:

        n "[neusname] acelera el ritmo de sus lengüetazos"

    n "al mismo tiempo que acaricia el clítoris con sus habilidosos dedos"

    n "haciendo que Dídac vuelva a caer mordiendo la almohada."

    ne "Sí..."

    ne "¡[protname]!"

    ne "¡No pares!"

    ne "La muy zorra volverá a correrse en nada."

    pt "A decir verdad,"

    pt "tampoco creo que a mí me quede demasiado..."

    p "Ughh..."

    d "*AAAhhhh...*"

    d "Jodeeer..."

    $ day06_morning_Didac_orgasms += 1

    n "Un enorme chorro inunda el rostro de [neusname]"

    n "pero a pesar de ello, no se detiene en lo absoluto en su labor por complacerla."

    n "Intentas mantener el ritmo de tus embestidas"

    n "mientras sigues percibiendo la ardiente lengua de [neusname]"

    if ay06_neusDidac_DidacSexVag:

        n "que sigue relamiendo su sensible clítoris"

    else:

        n "que sigue indagando en el interior de su vagina"

    n "hasta que empiezas a sentir el familiar cosquilleo en tu entrepierna."

    n "Uughh..."

    ne "¡No te detengas!"

    ne "¡Y ni se te ocurra sacarla hasta que no te quede ni una gota!"

    n "Percibes que su ardiente lengua te presta algo más de atención"

    n "mientras sigues embistiendo a Dídac sin compasión."

    n "Justo en el momento en el que sientes que tu esperma está atravesando la parte del tronco,"

    n "su longeva lengua se envuelve en tu miembro, cerca de la bolsa escrotal,"

    n "y ejerciendo una fuerza dolorosa impide el paso de tus soldaditos blancos."

    p "¡¿Pero qué coño?!"

    ne "¡SIGUE!"

    p "Pero..."

    extend " Joder..."

    p "¡¿Por qué?"

    ne "¡NO PARES!"

    p "¡Ugh!"

    n "Te aprieta con tanta fuerza que el dolor ya no proviene de lo ardiente que la tiene."

    ne "Confía en mi."

    n "Tienes la sensación de que tu esperma se está acumulando en tu entrepierna."

    p "Ughh..."

    p "[neusname]..."

    $ day06_morning_MC_orgasms += 1

    with hpunch
    with hpunch
    p "Aaaaghh..."


    n "Hasta que finalmente te libera de su presión"

    n "y descargas toda tu leche en el estrecho interior de tu ex-compañero de piso"

    n "mientras la ardiente lengua de [neusname] sigue lamiéndote los testículos"

    n "como si intentara vaciártelos aún más."

    if day06_neusDidac_DidacSexVag:

        n "Percibes que el coño de Dídac vuelve a ponerse hostil"

        n "hasta el punto que sientes que está a punto de echarte de su interior."

    else:

        n "Tienes la sensación de que Dídac está temblando más de lo habitual."

    $ day06_morning_Didac_orgasms += 1

    d "¡¡DIOOS!!"



    n "Vuelve a expulsar otro enorme chorro por su glándula de Skene."

    n "Esta vez, [neusname] se aparta de tus testículos"

    n "para acercar su boca a sus labios menores,"

    if day06_neusDidac_DidacSexVag:

        n "en contacto con la base de tu polla que sigue en movimiento,"

    else:

        n "metiendo su lengua en su vagina mientras con sus labios succiona sus labios menores"

    n "tragándose por completo el líquido que expulsa."

    d "JOOOdeeer..."

    n "Ves que las caderas de Dídac descienden"

    n "pero [neusname] las agarra para que tu polla no salga de su interior."

    ne "Sigue dándole duro [protname]."

    p "No creo que pueda sacar mucho más..."

    ne "..."

    n "Te agarra fuertemente de las pelotas con una mano"

    n "y con un movimiento brusco te aparta de su interior"

    p "¡Joder!"

    n "para luego acercarla a su rostro y metérsela en la boca."

    p "Un poco más de delicadeza,"

    extend " no estaría..."

    n "Sientes su lengua deslizarse a lo largo de tu miembro,"

    n "en el interior de su boca, que es tan o más ardiente que su lengua."

    n "La revisa con esmero, buscando bajo el glande, por los lados,"

    n "limpiando cualquier rastro de esperma que hubiera podido quedar olvidado a lo largo del miembro,"

    n "al mismo tiempo que succiona con rudeza el sensible orificio de tu polla."

    n "Cuando finalmente llega cerca de los testículos,"

    n "te envuelve la polla formando un estrecho nudo, que usa para ahogártela de nuevo."

    p "Ughh..."

    pt "¡¿Otra vez?!"

    n "Sin prisas, desliza ese nudo por tu miembro como si este se tratara de un tubo de pasta de dientes,"

    n "exprimiéndote con rudeza,"

    n "mientras con sus dedos acaricia suavemente tus testículos"

    n "hasta llegar a la punta"

    n "dónde logra sacar unas últimas gotas que se escondían en lo más profundo."

    p "Dios..."

    n "Finalmente se aparta."

    n "Mientras se relame los dedos:"

    ne "Siempre quedan algunas gotas..."

    n "Y con una mirada lasciva y de placer con sus ojos brillantes:"

    ne "Y no hay que desperdiciar ni una sola de ellas."

    n "Una singular gota de esperma cae en la mejilla derecha de [neusname]."

    ne "Hmm..."

    ne "Vaya..."

    ne "Parece que te has corrido tanto,"

    ne "que empieza a desprenderse..."

    n "Ignorando tu presencia, se agarra a sus nalgas"

    if day06_neusDidac_DidacSexVag:

        n "y abalanza sus labios contra su empapada vagina"

    else:

        n "y abalanza sus labios contra su empapado ano"

    n "como si fuera un pulpo devorando a su presa."

    d "¡Jodeeeer...!"

    

    n "Vira su cabeza ligeramente hacia los lados"

    n "dándote la sensación de que su lengua debe estar limpiándola profunda y rigurosamente."

    d "¡¡Diooos!!!"

    n "Las piernas de Dídac tiemblan de nuevo en lo que te parece que es otro orgasmo,"

    n "pero ni siquiera una sola gota logra escapar de los labios de [neusname]"

    n "que sigue succionando con ímpetu."

    n "Cuando su movimiento bucal disminuyes, ves que Dídac logra relajarse."

    n "Finalmente aparta sus labios de su entrepierna y Dídac cae rendida sobre la cama."

    ne "Hmmm..."

    ne "Me gusta recibirlo directamente de la fuente,"

    ne "pero reconozco que cuando está bien caliente y recién exprimido,"

    ne "limpiarlo de un coño tan rico es algo que también me encanta."

    n "Mirándote con esos ojos brillantes y mirada de gata felina."

    if gensex_ILoveYouNeus:

        ne "¿Necesitas que te limpie un poco más, cariño?"

    else:

        ne "¿Necesitas que te limpie un poco más?"

    p "[neusname]..."

    ne "Euhmm.."

    ne "Vaya..."

    ne "parece que me he sobreexcitado un poco..."

    ne "hehe..."

    p "Quizás deberíamos tomar un descanso."

    ne "No,"

    extend " no podemos."

    ne "Primero porque has ingerido mi sangre"

    ne "y sus efectos no tardarán en desvanecerse."

    ne "Especialmente cuando ya te has corrido,"

    ne "y segundo,"

    ne "esta noche es de vital importancia que tengamos las dosis necesarias de tu esperma,"

    ne "así que no hay tiempo que perder."

    n "[neusname] fija su mirada a su compañera que sigue rendida sobre la cama."

    ne "Dídac,"

    ne "¿te encuentras con fuerzas para continuar?"

    d "Cla-"

    extend "claro que sí..."

    d "Da-"

    extend "dame un minuto..."

    ne "Ya te he dicho antes que no tendríamos mucho tiempo."

    n "Ejerciendo un sobre-esfuerzo,"

    ne "se reincorpora de nuevo."

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab

    $ nteye = "left03"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with fade

    d "Dios..."

    $ df_eye = "front01"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    d "que putos orgasmos..."

    $ df_eye = "let02"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    ne "Ese lenguaje..."

    $ df_eye = "let03"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    d "Y tú que jodida lengua tienes,"

    $ df_eye = "let03"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ nteye = "left04"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    d "jodida..."

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx01
    show didacf_eyebrows surprisex01
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    d "¿Euh...?"

    jump day06_neusDidac_afterStop
        # d "¡¿Qué cojones es esto?!"
        # n "Un montón de orbes rojos os rodean en la semi-oscuridad de la habitación."
        # p "¿Dídac también puede verlos?"


label day06_neusDidac_ignoreNeus:

    if day06_neusDidac_startWithNeus_Cond:

        n "Con tu mano derecha, agarras con más fuerza su suave nalga"

        n "y embistes su trasero con rudeza logrando ahondar más tu miembro en su interior."

    else:

        n "A pesar de estar follando a Dídac sin compasión"

        n "y del dolor que sufres en tus dedos por su ardiente interior,"

        n "sigues perforando su vagina hasta incluso más allá de tus nudillos."

    ne "¡Aaahhmm...!"

    n "Esos extraños susurros aumentan de número y cada vez están más cerca."

    ne "Por favor..."

    if day06_neusDidac_startWithNeus_Cond:

        d "¿Soy yo,"

        d "o estoy oyendo voces?"

        n "Desplazas tus caderas a mayor celeridad."

    else:

        d "Ahhhhmm..."

        d "¿Soy yo...?"

        d "Ohhh..."

        d "¿Estoy oyendo voces...?"

        n "Desplazas tu mano a mayor celeridad."

    ne "Para..."

    n "Su cuerpo se arquea aún más y hunde su rostro en la sábana gimiendo sin cesar."

    ne "¡Para!"

    if day06_neusDidac_startWithNeus_Cond:

        n "A cada nueva embestida, tus caderas se acercan más a sus posaderas"

        n "y apenas quedan unos centímetros para poder chocar tu ombligo contra sus nalgas,"

        n "enterrando así por completo tu polla en su interior."

    else:

        n "A cada nueva embestida, intentas hundir más tu puño."

    n "El rostro de [neusname] se voltea mirándote con una cara de rabia contenida con sus ojos brillantes."

    with vpunch
    ne "{size=50}¡HE DICHO QUE PARES!{/size}"

    n "Sientes tu cuerpo completamente paralizado."

    if day06_neusDidac_startWithNeus_Cond:

        n "Ni siquiera eres capaz de mover la mano que tienes en el coño de Dídac."

    else:

        n "Ni siquiera eres capaz de mover tus caderas."

    if day06_neusDidac_DidacCare:

        p "¡¿Qué?!"

        d "¿Qué coño haces?"

        d "Que pares de follártela a ella lo entiendo,"

        d "¡¿pero por qué cojones no siento nada en mi coño?!"

    else:

        d "¿Qué...?"

    p "No puedo moverme..."

    n "Dídac mira con curiosidad y cierto temor a la morenita que tiene al lado."

    $ ped_neus_whispers_sfx04 = 0.95
    $ n_exp_shine = -0.01

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx008
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade_short

    ne "Cuando te digo que pares,"

    $ nteye = "front00"
    show n_closefromup_mouth sad_Talkingx18
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    ne "¡TE PARAS!"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx13
    show n_closefromup_eyebrows angryx06
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Esto no es una broma, [protname]!"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx15
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "¡He estado a punto de correrme!"

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx010
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "¡¿Es que acaso no entiendes lo que eso significaría?!"

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx08
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "front05"
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with Dissolve(0.2)

    pause 0.2

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    d "¿Que tendrías un orgasmo de mil narices?"

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "left05"
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    jump day06_neusDidac_afterStop

label day06_neusDidac_afterStop:

    pause 0.2

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx01
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    $ nteye = "left03"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    d "¿Euh...?"

    $ df_eye = "right00"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    d "¡¿Qué cojones es esto?!"

    $ df_eye = "right00"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows sadx01
    call dfeye_lab

    $ nteye = "left02"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Un montón de orbes rojos os rodean en la semi-oscuridad de la habitación."

    p "¿Dídac también puede verlos?"

    #n "[neusname] sigue exhalando un vapor denso y cálido."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade

    ne "Sí..."

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando un humano recibe nuestra saliva,"

    extend " sangre,"

    extend " o fluidos corporales,"

    $ nteye = "right02"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "es capaz de escucharlos y verlos cuando cruzan el umbral."

    $ nteye = "front01"
    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    p "Pero hasta que te conocí nunca los había visto."

    $ nteye = "front02"
    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Eso es porque nunca has asistido a ningún aquelarre;"

    $ nteye = "front03"
    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Aún no has sido iniciado."

    $ Pedrera_char_Cond = "NeusDidac_close"
    call Pedrera_char_lab

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows surprisex02
    call dfeye_lab

    $ nteye = "left01"
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    $ df_eye = "left02"
    show didacf_mouth sadbiting_Silentx07
    show didacf_eyebrows suspiciousx02
    call dfeye_lab

    d "¡¿Los susurros vienen de estas cosas raras?!"

    

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo siento..."

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    $ nteye = "front04"
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    if day06_neusDidac_startWithNeus_Cond:

        ne "No debería haberte pedido que me follaras."

    else:

        ne "No debería ni de haberme puesto a cuatro patas."

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab

    $ nteye = "right01"
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Ha sido estúpido por mi parte."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "right04"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    menu:

        "Es mi culpa por no haberme detenido cuando me lo has pedido." if not day06_neusDidac_Stopped:
            call p_Help
            $pl.ch_pts("np",1)

            $ nteye = "front01"
            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "En parte..."

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero por otra parte soy yo la que te he dado de beber de mi sangre,"

            $ nteye = "right02"
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "es normal que te cueste controlarte."

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Así que tampoco te puedo echar toda la culpa,"

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "pues soy yo la que tiene que ser responsable aquí."

            if day06_neusDidac_startWithNeus_Cond:

                $ nteye = "right04"
                show neus_exp_mouth sad_Talkingx004
                show neus_exp_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero..."

                $ nteye = "front05"
                show neus_exp_mouth happy_Talkingx04
                show neus_exp_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "no te haces una idea de lo mucho adoro tu polla, [protname]."

            $ nteye = "down05"
            show neus_exp_mouth happybiting_Silentx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            jump day06_neusDidac_neusCalming

        "Me hubiera gustado continuar, pero me has pedido que parase." if day06_neusDidac_Stopped:
            call p_Help
            $pl.ch_pts("np",1)

            $ nteye = "front02"
            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front04"
            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Te aseguro que a mi también me hubiera encantado."

            $ nteye = "front08"
            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero es demasiado arriesgado."

            $ nteye = "right05"
            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusDidac_neusCalming

        "...":
            call p_Help

            jump day06_neusDidac_neusCalming

    jump day06_neusDidac_neusCalming

label day06_neusDidac_neusCalming:

    pause 0.2

    $ nteye = "down05"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    n "[neusname] inspira profundamente para luego exhalar un vaho amplio y denso."

    $ ped_neus_whispers_sfx04 = 0.0
    $ n_exp_shine = 0.0

    $ nteye = "front08"
    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    scene day05
    with fade

    n "Esos susurros y orbes rojos empiezan a disiparse entre la oscuridad."

    $ Pedrera_char_Cond = "NeusWall"
    call Pedrera_char_lab

    $ nteye = "left02"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade

    d "¿Siempre que te acercas al orgasmo aparecen estas cosas?"

    $ nteye = "left02"
    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ nteye = "left05"
    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    d "Que putada."

    $ nteye = "front08"
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    jump day06_neusDidac_neusChangingPosition

###

label day06_neusDidac_neusChangingPosition:

    pause 0.2

    scene day06
    with fade

    n "Con agilidad y celeridad, [neusname] se levanta"

    n "y se pone debajo de las piernas de Dídac."

    if day06_neusDidac_CumInDidac_Cond:

        d "¿Otra vez?"

    else:

        d "¡¿Qué estás hacien...?!"

    n "Alarga su cuello hasta acercar sus labios a su zona púbica"

    n "dónde empieza a lamer su sensible parte."

    d "Hmmm..."

    n "Apartando ligeramente su boca de la entrepierna de Dídac."

    ne "¿A qué estás esperando?"

    if day06_neusDidac_CumInDidac_Cond:

        p "¿No sería tu turno ahora?"

        ne "Desgraciadamente no es buena idea."

        ne "Me he acercado demasiado al orgasmo"

        ne "y solo te la estaba lamiendo superficialmente."

        p "..."

        ne "Pero estoy segura de que Dídac no se quejará de que se la metas de nuevo,"

        ne "¿verdad?"

    else:

        ne "Aún no te has corrido"

        ne "y estoy segura que Dídac está desando que se la metas."

    d "..."

    d "No diré que no."

    d "Hnmmm..."

    n "Vuelve a posar su lengua por sus labios vaginales"

    n "mientras con sus manos separa sus nalgas para mostrarte el camino."

    p "La sutileza no es tu punto fuerte."

    ne "¿Quién ha dicho que yo sea sutil?"

    n "Dídac hace lo mismo y hace un esfuerzo arqueando su espalda"

    n "para acercar su rostro a la entrepierna de la morenita."

    ne "¡Dídac!"

    d "¿Qué?"

    d "¿Es que no quieres que te lo haga yo también?"

    ne "¿Acaso te apetece volver a ver esos ojos rojos observándote?"

    d "Aparte de susurrar,"

    d "¿hacen algo más?"

    ne "..."

    ne "A menos que tenga un orgasmo,"

    ne "no..."

    d "Entonces no hay problema."

    ne "Pero si te digo que pares,"

    ne "paras."

    if day06_neusDidac_Stopped:

        d "¿Acaso me tomas por el idiota de [protname]?"

    else:

        d "Si el idiota de [protname] ha sido capaz de parar,"

        d "yo no voy a ser menos."

    ne "¡¿Me has oído?!"

    d "Que sí,"

    extend " que sí..."

    d "me detendré cuando me lo pidas."

    ne "..."

    n "Acercas tus caderas al trasero de Dídac posando tu polla sobre sus nalgas."

    n "[neusname] se detiene observándote desde abajo con una mirada de deseo y cierta frustración."

    d "¡Fóllame de una vez!"

    # OPTIONAL?

    menu:

        pt "¿Por dónde?"

        "<Follarle el trasero>":
            call p_Help
            $pl.ch_pts("dp",-1)

            $ day06_neusDidac_dF_01_Vag = False

        "<Follarle la vagina>":
            call p_Help
            $pl.ch_pts("dp",1)

            $ day06_neusDidac_dF_01_Vag = True

    jump day06_neusDidac_second_fuckingDidac

label day06_neusDidac_second_fuckingDidac:

    if day06_neusDidac_dF_01_Vag:

        n "Acercas tu polla a su cálida y empapada concha"

        n "jugando con sus labios vaginales con la punta de tu glande."

    else:

        n "Acercas tu polla a su cálida y suave piel trasera"

        n "jugando con su arrugado y estrecho anillo con la punta de tu glande."

        if not day06_neusDidac_startWithNeus_Cond and not day06_neusDidac_DidacSexVag:

            d "¡¿Otra vez por aquí?!"

            d "¿Es que antes no has tenido suficiente?"

        else:

            d "¡Ey!"

            d "¡¿Por qué coño tienes que follarme el culo?!"

        p "Mi polla,"

        extend " mi decisión."

        p "Si no te gusta,"

        p "simplemente me masturbo y ya está."

        d "..."

        d "Que simpático eres cuando quieres..."

        if p_didac.anal_received > 2 or afternight04__Anal_dick_med_Success > 2:

            p "Si en el fondo te gusta más de lo que quieres confesar."

            d "..."

        if p_didac.vaginal_received > 2 or afternight04_Pussy_dick_med_Speed_0_Success > 2:

            d "¡Pero me gusta más por mi jodida concha joder!"

    d "Hmmm..."

    n "[neusname] prosigue con su juguetona lengua."

    d "¡Joder!"

    n "Las piernas de Dídac empiezan a temblar."

    ne "¡UGhhmm...!"

    $ day06_morning_Didac_orgasms += 1
    n "Un chorro de líquido se precipita encima del rostro de [neusname]."

    ne "Vaya..."

    if day06_morning_Didac_orgasms == 1:

        ne "Hacía rato que te estabas aguantando."

    elif day06_morning_Didac_orgasms == 2:

        ne "Ya es la segunda vez que te corres..."

    else:

        ne "Ya llevas unos cuantos..."

    d "..."

    d "No te voy a pedir disculpas,"

    d "has sido tú la que se ha puesto debajo."

    ne "¿Acaso crees que me ha disgustado?"

    if day06_neusDidac_dF_01_Vag:

        n "Prosigue con su juego oral, pero esta vez hundiendo su rostro en su entrepierna."

        n "Tienes la sensación de que esta vez usa de nuevo su longeva lengua."

        d "Ughhmm..."

    else:

        n "Su lengua se extiende y logra penetrar en el interior del agujero anal de Dídac."

        d "Ughhmm..."

        n "Del modo en que la mueve y la desliza por su interior,"

        n "tienes la sensación de que está profundizando bastante."

        d "Dios..."

        d "¡¿Pero cuanto le mide la lengua a esta tía?!"

    p "Así no me vas a dejar espacio para meterla."

    n "Apartando su rostro de su entrepierna."

    ne "Ahora está lista para tu pollón."

    pt "Creo que ya estaba suficientemente lista..."

    n "Deslizando su lengua se dirige a su clítoris"

    if day06_neusDidac_dF_01_Vag:

        n "mientras con sus manos te abre de nuevo sus labios vaginales a modo de invitación."

    else:

        n "mientras con sus manos te abre de nuevo sus nalgas a modo de invitación."

    d "Será jodía la enana..."

    ne "¡No me llames así!"

    n "Con un grácil movimiento de cadera,"

    if day06_neusDidac_dF_01_Vag:

        n "introduces tu miembro en su cavidad vaginal,"

    else:

        n "introduces tu miembro en su cavidad anal,"

    n "sintiendo tu polla arropada por su caliente carne."

    d "¡Hhmm...!"

    if day06_neusDidac_dF_01_Vag:

        p "A pesar de lo caliente,"

        if afternight04__Pussy_dick_deep_Success > 1 or p_didac.vaginalDeep_received > 1:

            extend " húmeda,"

        if afternight04__Pussy_dick_deep_Success > 1 and p_didac.vaginalDeep_received > 1:

            p "y de que haya llegado a metértela entera dos días seguidos..."

        elif p_didac.vaginalDeep_received > 1:

            p "y de que ayer llegara a metértela entera,"

        elif afternight04__Pussy_dick_deep_Success > 1:

            p "y de que antes de ayer llegara a metértela entera,"

        else:

            p "y húmeda que estás,"

        p "sigue estando bastante estrecha..."

    else:

        if afternight04__Anal_dick_deep_Success > 1 and p_didac.analDeep_received > 1:

            p "A pesar de que he llegado a metértela entera dos días seguidos..."

        elif p_didac.analDeep_received > 1:

            p "A pesar de que llegué a metértela entera,"

        elif afternight04__Anal_dick_deep_Success > 1:

            p "A pesar de que antes de ayer llegara a metértela entera,"

        if afternight04__Anal_dick_deep_Success > 1 or p_didac.analDeep_received > 1:

            p "tu trasero sigue estando bastante estrecho..."

        else:

            p "Parece que tu trasero está bien estrecho..."

    d "Vete a la mierda."

    d "¡¡HHMmmm...!"

    n "A medida que la lengua de [neusname] juguetea con sus labios exteriores,"

    n "sientes casi como por accidente que también acaricia la parte inferior de tu sensible polla."

    n "A medida que penetras en su interior,"

    if day06_neusDidac_dF_01_Vag and p_didac.vaginalDeep_received > 1:

        n "sientes que su cavidad vaginal no te ofrece demasiada hostilidad"

    elif not day06_neusDidac_dF_01_Vag and p_didac.analDeep_received > 1:

        n "sientes que su cavidad anal no te ofrece tanta hostilidad"

    else:

        n "sientes que a pesar de la hostilidad inicial,"

        n "consigues profundizar cada vez más."

    n "y logras introducir casi la mitad de tu miembro en su cálido interior."

    d "¡Joder...!"

    n "De pronto su carne te aprisiona el miembro con más ímpetu,"

    n "casi como si quisiera echarte de su interior."

    d "¡¿Otra vez?!"

    $ day06_morning_Didac_orgasms += 1
    n "Otro chorro sale disparado empapando tu polla y el rostro de [neusname],"

    n "la cual, permanece con la boca completamente abierta"

    n "deslizando su lengua por debajo de tu polla para relamer las gotas que descienden de ella."

    n "Una vez eliminada toda prueba del crimen,"

    n "desliza su lengua hacia el interior de su coño."

    d "¡Joder con esta lengua!"

    n "A medida que va penetrando en su interior,"

    if day06_neusDidac_dF_01_Vag:

        n "la percibes deslizándose por la base de tu sensible miembro"

        n "como si fuera una serpiente en ascuas."

    else:

        n "la percibes a través de la pared anal de Dídac,"

        n "jugueteando con su interior y chocando contra tu palpitante polla."

    if day06_neusDidac_dF_01_Vag:

        n "Sientes que el coño de Dídac vuelve a relajarse ligeramente"

    else:

        n "Sientes que su cavidad anal vuelve a relajarse ligeramente"

    n "y consigues penetrar más profundamente."

    pt "Joder..."

    n "Tu polla ahogada por su carne"

    if day06_neusDidac_dF_01_Vag:

        n "y esa calcinante lengua"

    else:

        n "y esa lengua en constante movimiento a través de su carne"

    n "producen que tu polla empiece a palpitar con ímpetu."

    menu:

        pt "¿Debería decir algo?"

        "No creo que pueda aguantar mucho más...":
            call p_Help
            $pl.ch_pts("np",1)

            pass

        "...":
            call p_Help

            ne "[protname]..."

            ne "Estás a punto de correrte,"

            ne "¿verdad?"

            p "..."

            ne "Es obvio que sí."

    ne "Córrete [protname]."

    ne "Saca toda la cantidad que puedas..."

    d "¡Pero dame más duro joder!"

    n "Agarrándola con fuerza en ambas nalgas,"

    n "la embistes con fuerza logrando en cada nueva embestida hundir más tu polla en ella."

    d "¡SEEEH!"

    n "Dídac se detiene en su movimiento bucal"

    n "debido a que sus gemidos le impiden seguir usando su lengua con normalidad,"

    n "y reposa su cabeza sobre su entrepierna mientras jadea, gime, y se agarra a sus piernas."

    n "Pero [neusname] no se detiene en ningún momento"

    if day06_neusDidac_dF_01_Vag:

        n "y sigue deslizando su longeva lengua por su interior"

        n "y alrededor de tu sensible polla."

    else:

        n "y sigues sintiendo su lengua moviéndose a través de la pared carnal que os separa."

    d "¡DIOS!"

    d "¡¿Pero cuantas putas lengua tiene esta?!"

    n "Al fijarte, descubres una segunda lengua,"

    n "que surge de su infernal boca,"

    n "acariciando minuciosamente su clítoris."

    n "Sus labios se acercan a la altura de tus testículos"

    n "a la par que estos chocan contra la entrepierna de Dídac,"

    n "intentando besarte en ellos cada vez que la embistes de nuevo."

    p "¡Ugh!"

    n "El cosquilleo de una intensidad mayor a la que estás acostumbrado recorre tu entrepierna"

    n "mientras tu polla palpita exageradamente en su interior."

    n "Un enorme flujo de esperma recorre tu erecto miembro"

    n "a medida que sientes que tu polla va explotar,"

    n "desparramándose en su estrecha y cálida carne."

    d "¡AAAaahhmm!"

    if day06_neusDidac_dF_01_Vag:

        n "Su cavidad vaginal vuelve a ceñirse rápidamente,"

    else :

        n "Sientes que su carne anal vuelve a ceñirse rápidamente,"

    n "como si quisiera expulsar tu polla,"

    n "pero sigues embistiéndola con rudeza evitando que eso ocurra."

    n "La lengua de [neusname] sigue lamiendo tu polla desde tus testículos"

    n "hasta casi el glande que sigue derramando esperma en su interior."

    $ day06_morning_Didac_orgasms += 1
    if day06_neusDidac_dF_01_Vag:

        n "Un chorro energético de líquido vaginal surca toda tu polla"

    else:

        n "Un chorro energético de líquido vaginal surge del estrecho coño de Dídac."
    
    n "hasta explosionar como un {a=https://es.wikipedia.org/wiki/Aspersor}aspersor{/a} por toda tu barriga, piernas,"

    n "y cayendo por ende sobre el rostro de [neusname]."

    d "¡Jodeeer...!"

    n "A pesar del intenso orgasmo, sientes que tu polla está incluso más dura que antes."

    pt "¡¿Pero qué mierdas?!"

    n "Sientes los tendones de tus piernas y tus brazos en plena tensión,"

    n "tus músculos palpitando con viveza,"

    n "y apenas eres capaz de detener tus caderas que siguen embistiendo con rudeza las nalgas de Dídac,"

    n "como si estuvieran a modo automático."

    n "El esperma empieza a derramarse por sus piernas,"

    n "aunque no llegan muy lejos antes de que [neusname] pase la lengua por ellas."

    with hpunch
    p "¡Ouch!"

    d "¡¿Qué cojones?!"

    n "Con un fuerte empujón, [neusname] te aparta de Dídac"

    n "y la empuja boca-arriba sobre la cama."

    d "¡¿Pero qué coño haces?!"

    d "¡¡GHHmmm!!"

    n "Abriéndola de piernas, hunde su rostro en la entrepierna de Dídac"

    n "como si hiciera semanas que no hubiera probado bocado"

    n "y estuviera apurando los restos de comida en su interior."

    d "¡¡JOOODEEER!!"

    n "Te la quedas mirando sin saber muy bien cómo reaccionar,"

    n "su expresión y actitud es como la de un animal salvaje."

    p "[neusname]..."

    p "¿Estás bien?"

    ne "*Ahh....-ah...*"

    n "Ves que voltea y te mira ansiosa, famélica,"

    n "y perturbadoramente alegre con sus brillantes ojos"

    n "y su barbilla empapada en los jugos de Dídac."

    ne "Quiero verte la cara mientras la follas."

    d "¡¿De qué...?!"

    d "¡GHHMmmgh!"

    n "Posa su coño sobre su cara impidiéndole decir nada más."

    n "Sin dejar de mirarte a los ojos:"

    ne "Fóllala [protname]."

    ne "Quiero que te corras de nuevo."

    pt "Cuando va cachonda, se pone algo mandona..."

    n "Separa sus piernas mientras desciende su rostro."

    n "Con una mirada lasciva y juguetona alarga su lengua para relamer su clítoris"

    n "mientras te mira desde ahí abajo."

    ne "Mira lo cachonda que está,"

    ne "y lo dura que la tienes..."

    menu:

        pt "Sus ojos..."

        "[neusname]...":
            call p_Help
            $pl.ch_pts("np",1)

            ne "Ya lo sé, tranquilo."

            ne "No me voy a correr."

            ne "Pero no te voy a negar que estoy realmente muy cachonda."

            ne "Quiero saborear de nuevo tu delicioso esperma."

            p "..."

        "...":
            call p_Help

            pass

    jump day06_neusDidac_third_fuckingDidac

label day06_neusDidac_third_fuckingDidac:

    ne "Fóllala y córrete pronto,"

    ne "antes de que los efectos se disipen del todo."

    p "¿Los efectos?"

    ne "Alza tu mano y fíjate en ella."

    n "Cuando lo haces, apenas eres capaz de mantenerla en el aire y la descubres temblorosa,"

    n "como si estuvieras en una etapa preliminar de la {a=https://es.wikipedia.org/wiki/Enfermedad_de_Parkinson}enfermedad de Parkinson{/a}."

    ne "Ya te he dicho que mi sangre podría ayudarte,"

    ne "pero no tardarás mucho en perder tu energía."

    ne "Para entonces quedarás completamente paralítico durante unos días."

    p "..."

    ne "Fóllatela."

    if not day06_neusDidac_dF_01_Vag:

        ne "Pero esta vez métesela por su empapado coño,"

        ne "quiero saborear tu polla junto a sus jugos..."

    n "Mientras se muerde el labio, presiona con más fuerza sus caderas sobre el rostro de Dídac."

    d "¡Hghmmghhmkm!"

    # CHOICE? I don't really think is necessary here.
    menu:

        pt "¿Por dónde?"

        "<Follártela vaginalmente>":
            call p_Help

            $ day06_neusDidac_dF_02_Vag = True

        "<Follártela analmente>":
            call p_Help

            if day06_neusDidac_dF_01_Vag == False:
                $pl.ch_pts("np",-2)

            else:
                $pl.ch_pts("np",-1)

            $ day06_neusDidac_dF_02_Vag = False

    if day06_neusDidac_dF_02_Vag:

        pt "Con la cara que pone,"

        pt "no creo que sea buena idea llevarle la contraria..."

        n "Obedeces sus palabras y acercas tu erecta polla,"

    else:

        n "Acercas tu erecta polla a su no tan estrecho agujero anal."

    n "esta vez mucho más rojiza y venosa que antes,"

    if day06_neusDidac_dF_02_Vag:

        n "en la empapada entrepierna de Dídac."

    else:

        if not day06_neusDidac_dF_01_Vag:

            n "en el no tan estrecho agujero anal de Dídac."

        else:

            n "en el estrecho agujero anal de Dídac."

    if not day06_neusDidac_dF_02_Vag:

        ne "Hmm..."

        ne "Si es lo que prefieres..."

        if not day06_neusDidac_dF_01_Vag:

            d "¡¿Otra vez por aquí?!"

        else:

            d "¡¿Ahora por aquí?!"

        if DidacMCPregnant:

            d "¡Que ya me has dejado preñada joder!"

        else:

            d "¡Que ya me han dejado preñada joder!"

    n "Sin demasiado esfuerzo, logras penetrar su cálida carne,"

    n "al mismo tiempo, sientes los suaves labios de [neusname]"

    n "besando la sudorosa piel de la parte superior de tu erecto miembro."

    n "De modo cariñoso y apasionado, sube por tu ombligo,"

    n "luego por tu pecho,"

    n "teniéndose unos segundos para lamer tu pezón de modo juguetón,"

    n "para luego seguir subiendo por tu cuello,"

    n "hasta alcanzar tu barbilla dónde se acerca tiernamente a tus labios"

    # NOT FINISHED... ¿More choices? Hate Love? dOES SHE kisses you if you hate her? Can you be here if she hates you?

    n "y entremezcla vuestras lenguas en un apasionado beso."

    $ ped_neus_whispers_sfx04 = 0.95 # NOT FINISHED... how should be the number here?
    #$ n_exp_shine = -0.01
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx001
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade_short

    pause 0.2

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx03
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "Su lengua..."

        "Tiene un sabor distinto...":
            call p_Help

            $ nteye = "front02"
            show n_closefromup_mouth sad_Silentx01
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Cállate tonto."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx04
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

        "Me encanta cómo besas.":
            call p_Help

            $ nteye = "front02"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "Y a mi me encantan tus labios y tu lengua."

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve
            

label day06_neusDidac_third_keepMoving:

    pause 0.2

    $ nteye = "down01"
    show n_closefromup_mouth sad_Silentx01
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    d "¡Pero mueve esa polla!"

    $ nteye = "down04"
    show n_closefromup_mouth happybiting_Silentx06
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Sin apenas darte cuenta, habías aminorado el ritmo de tus caderas."

    if day06_neusDidac_dF_02_Vag:

        d "¡Aunque me esté follando el puto trasero,"

        d "al menos haz que valga la jodida pena!"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade_short

    ne "Fóllate a esta perra."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Vuelves a mover tus caderas logrando hundir tu miembro en su interior casi en su totalidad."

    d "¡Hmmmmghhh...!"

    n "Un gemido agudo, satisfactorio, y ligeramente libre de la entrepierna de [neusname],"

    n "surge de los labios de Dídac mientras se agarra fuertemente a la sábana."

    with vpunch
    p "¡Auch!"

    n "Sientes un fuerte mordisco en tu oreja,"

    n "para luego percibir cálido aliento mientras te susurra:"

    ne "¿Te ha dolido?"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx09
    show n_closefromup_eyebrows suspiciousx04
    call n_closefromup_tears_tears
    with fade_short

    menu:

        pt "No es que haya sido delicada, precisamente..."

        "Eres un poco bruta...":
            call p_Help

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "No te quejes tanto."

            $ nteye = "down04"
            show n_closefromup_mouth sadbiting_Silentx08
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            pt "¿Entonces para qué pregunta?"

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

        "¿A ti qué te parece?":
            call p_Help

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            ne "Que eres un poco quejica."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            p "¿Quieres que te muerda yo y compruebas lo que duele?"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Y por qué no?"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Silentx06
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

        "No, es que me suelo comunicar con monosílabos.":
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Tu sarcasmo es tan adorable..."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx01
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            p "Mira quien habla."

            $ nteye = "front06"
            show n_closefromup_mouth happybiting_Silentx08
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

        "Solo un poco...":
            call p_Help

            $ nteye = "front04"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx005
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Eso es que tengo que morder más fuerte?"

            $ nteye = "front02"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            p "No era una invitación."

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "Pues lo ha parecido..."

            $ nteye = "front01"
            show n_closefromup_mouth happy_Silentx10
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ nteye = "front07"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "*hehehe...*"

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Solo estoy bromeando,"

            if gensex_ILoveYouNeus:

                extend " cariño."

            else:

                extend " tontín."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            pt "Desde luego,"

            $ nteye = "down04"
            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            pt "va cachonda..."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

label day06_neusDidac_third_DidacHorny:

    pause 0.2

    scene day06
    with fade

    n "Dídac mueve sus caderas al percibir que vuelves a menguar la marcha."

    ne "Parece que está bastante cachonda,"

    ne "¿no crees?"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with fade_short

    p "¿Te traigo un espejo?"

    $ nteye = "front04"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # CONDITONAL?

    if not gensex_YoureAMonster:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Bésame."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx01
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        scene morning04_bg bedroom_neus_a
        show kiss_ f_n_01:
            truecenter
            xzoom -1.0
            zoom 1.5 rotate -30
        show light 01:
            light01_topside_position
        with fade_short

        pause 0.2

        show kiss_ f_n_10
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_n_12
        with Dissolve(0.5)

        n "Vuelve a mezclar vuestras lenguas con fervor mientras prosigues la marcha con tus caderas"

        show kiss_ f_n_11
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_n_02
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_n_10
        with Dissolve(0.5)

        n "sintiendo la estrecha carne de Dídac ahogando tu palpitante polla."

    scene day06
    with vpunch

    d "¡Ahhhmm...!"

    n "Sientes las piernas de Dídac temblar y todo su cuerpo se convulsiona."

    d "¡No pares joder!"

    if day06_neusDidac_dF_02_Vag:

        n "Repentinamente sientes otra vez su carne vaginal estrujarte la polla"

        n "como si su coño quisiera echarte a patadas"

    else:

        n "Repentinamente sientes otra vez su pared carnal estrujándote la polla"

        n "como si su ano quisiera echarte a patadas"

    $ day06_morning_Didac_orgasms += 1
    n "mientras un chorro de líquido vaginal vuelve a empaparte la barriga."

    d "¡COÑOOO!"

    n "Percibes cómo las piernas de Dídac se van relajando paulatinamente."

    d "Seehhh..."

    n "Su voz es femenina y temblorosa."

    $ ped_neus_whispers_sfx04 = 0.95 # NOT FINISHED... how should be the number here?
    #$ n_exp_shine = -0.01
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade_short

    n "[neusname] te mira con un rostro de gata en celo, y con una erótica voz:"

    
    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Parece que le gusta tu polla."

    $ nteye = "down04"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque debo confesar que también estoy enamorada de ella."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx09
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    # CHOICE

    $ day06_neusDidac_third_neusChoose_Cond = ""

    menu:

        pt "Me pregunto si me ama a mí, o a mi polla..."

        "Yo también estoy enamorado de tu coño y tu lengua." if not gensex_YoureAMonster:
            call p_Help

            $pl.ch_pts("np",1)

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            if not gensex_ILoveYouNeus:

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "Al menos me alegro de que te guste tanto algo de mí..."

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Y cual de los dos te gusta más?"

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            menu day06_neusDidac_third_neusChoose_Question:

                pt "¿Cuál de los dos?"

                "Tu coño.":
                    call p_Help

                    $ day06_neusDidac_third_neusChoose_Cond = "pussy"

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Hmm..."

                    if p_neus.vaginal_received < 5:

                        $pl.ch_pts("np",-1)

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx005
                        show n_closefromup_eyebrows angryx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pues a ver si me lo follas más a menudo,"

                        $ nteye = "right04"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "que ayer le hiciste pasar hambre."

                        $ nteye = "right05"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve


                    elif p_neus.vaginalDeep_received < 1:
                        #$pl.ch_pts("np",2)

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx005
                        show n_closefromup_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me hubiera gustado poder sentirla entera dentro..."

                        if p_neus.vaginal_pain_received > 0:

                            $ nteye = "front01"
                            show n_closefromup_mouth sadbiting_Silentx02
                            show n_closefromup_eyebrows surprisex02
                            call n_closefromup_tears_tears
                            with dissolve

                            p "¡Pero si cuando lo intentaba me echabas a patadas!"

                            $ nteye = "front04"
                            show n_closefromup_mouth sad_Talkingx06
                            show n_closefromup_eyebrows angryx02
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "¡Por que no estaba lo suficientemente dilatada!"

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx005
                            show n_closefromup_eyebrows suspiciousx01
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Un poco más de paciencia y estoy segura que hubiera entrado mejor..."

                            $ nteye = "right05"
                            show n_closefromup_mouth sadbiting_Silentx06
                            show n_closefromup_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                        else:

                            $ nteye = "front08"
                            show n_closefromup_mouth sadbiting_Silentx07
                            show n_closefromup_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                    else:
                        $pl.ch_pts("np",1)

                        $ nteye = "front04"
                        show n_closefromup_mouth happy_Talkingx04
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me alegra saber eso..."

                        $ nteye = "front05"
                        show n_closefromup_mouth happybiting_Silentx06
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                    if p_neus_orgasmHurry and p_neus.vaginal_received<5 or p_neus.vaginalDeep_received<1:

                        pause 0.2

                        $ nteye = "front01"
                        show n_closefromup_mouth sadbiting_Silentx01
                        show n_closefromup_eyebrows suspiciousx01
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Me dijiste que parase porque estabas a punto de tener un orgasmo."

                        $ nteye = "front04"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front06"
                        show n_closefromup_mouth extra_burlesque
                        show n_closefromup_eyebrows angryx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "*Gnnn...*"

                        $ nteye = "right01"
                        show n_closefromup_mouth sad_Talkingx004
                        show n_closefromup_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Le podrías haber dado un poco más de cariño antes de que eso pasara."

                        $ nteye = "front05"
                        show n_closefromup_mouth happybiting_Silentx07
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                    pause 0.2

                    if gensex_ILoveYouNeus:

                        pause 0.2

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Te amo tanto..."

                        $ nteye = "front05"
                        show n_closefromup_mouth happybiting_Silentx07
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                "Tu lengua.":
                    call p_Help

                    $ day06_neusDidac_third_neusChoose_Cond = "tongue"

                    if p_neus.blowjob_done < 5:
                        $pl.ch_pts("np",-1)

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx004
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pues ayer no me la dejaste chupar demasiado..."

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows normal
                        call n_closefromup_tears_tears
                        with dissolve

                        p "No quería correrme tan pronto."

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows suspiciousx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "right05"
                        show n_closefromup_mouth sad_Talkingx007
                        show n_closefromup_eyebrows suspiciousx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "He oído excusas peores..."

                        $ nteye = "front08"
                        show n_closefromup_mouth sadbiting_Silentx06
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                    else:

                        $pl.ch_pts("np",1)

                        $ nteye = "front03"
                        show n_closefromup_mouth happy_Talkingx05
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me alegra saber eso..."

                        $ nteye = "front05"
                        show n_closefromup_mouth happybiting_Silentx05
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                "Ambos por igual." if day06_neusDidac_third_neusChoose_Cond != "both":
                    call p_Help

                    $ day06_neusDidac_third_neusChoose_Cond = "both"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Esa respuesta no me sirve."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Se valiente y elige solo una."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusDidac_third_neusChoose_Question

        "¿Es que acaso soy una polla con patas?":
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx01
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "down01"
            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "down03"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Es bastante grande."

            $ nteye = "front01"
            show n_closefromup_mouth happybiting_Silentx10
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Tonto."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            if gensex_ILoveYouNeus:

                ne "Ya sabes que te amo con locura."

            else:

                ne "Ya sabes lo mucho que me gustas."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            p "No sé yo..."

            if gensex_YoureAMonster:

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Aunque sigas pensando que soy un monstruo..."

                $ nteye = "down05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

            else:

                $ nteye = "down05"
                show n_closefromup_mouth happybiting_Silentx06
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

        "...":
            call p_Help

    pause 0.2

    if not gensex_YoureAMonster:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Bésame."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx01
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        scene morning04_bg bedroom_neus_a
        show kiss_ f_n_01:
            truecenter
            xzoom -1.0
            zoom 1.5 rotate -30
        show light 01:
            light01_topside_position
        with fade_short

        pause 0.2

        show kiss_ f_n_10
        with Dissolve(0.5)

        

        n "Te agarra suavemente por la nuca y acerca sus labios a los tuyos"

        show kiss_ f_n_05
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_n_08
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_n_12
        with Dissolve(0.5)

        n "para mezclaros en un suave y apasionado beso,"

        scene day06
        with fade

        if day06_neusDidac_dF_02_Vag:

            n "mientras tus caderas siguen penetrando el cada vez más estrecho coño de Dídac"

        else:

            n "mientras tus caderas siguen penetrando el cada vez más estrecho ano de Dídac"

    else:

        scene day06
        with fade

        n "Sigues moviendo tus caderas en su interior"

    n "a la par que sientes tu polla palpitar con más intensidad en cada nueva embestida."   

    n "Con picardía,"

    n "desliza su lengua por tu cuello mientras te da pequeños y aleatorios besos por tu piel,"

    n "bajando hasta tu pecho,"

    p "Auch..."

    n "donde vuelve a morderte el pezón."

    ne "Ya te quejas por vicio..."

    if day06_neusDidac_dF_02_Vag:

        n "Las paredes vaginales de Dídac te arropan con tanta intensidad"

    else:

        n "Las paredes carnes de Dídac te arropan con tanta intensidad"

    n "que vuelves a tener la sensación de que intentan expulsar tu polla de su interior."

    n "mientras vuelve intentar echarte de su interior,"

    $ day06_morning_Didac_orgasms += 1
    n "cuando sientes un nuevo chorro que te vuelve a dejar empapada la barriga."

    p "¿Pero cuantas veces se va a correr esta mujer?"

    # CONDITIONAL

    if p_didac.orgasm < 3:

        ne "Creo que ya ha tenido más orgasmos que ayer..."

    else:

        ne "Creo que ayer tuvo más orgasmos..."

    n "Los labios de [neusname] bajan por tus abdominales lamiendo ese líquido vaginal empapado en tu piel."

    d "¡¿Otra vez?!"

    d "¡Ghhmmmgh!"

    n "Vuelve a silenciar a Dídac con su entrepierna"

    n "mientras baja su lengua por tu ombligo hasta alcanzar la base de tu polla"

    n "siguiendo el ritmo de tus embestidas."

    p "Hmmm..."

    n "A pesar de que sigues chocando con su rostro,"

    n "ella sigue moviendo su lengua hasta que alcanza de nuevo el clítoris de Dídac"

    n "en el cual se detiene y relame con cariño"

    n "mientras sigues aumentando el ritmo de tus caderas"

    if day06_neusDidac_dF_02_Vag:

        n "al sentir que el sexo de Dídac se va dilatando."

    else:

        n "al sentir que la cavidad anal de Dídac se va dilatando."

    d "¡AAhhhmm...!"

    with hpunch
    p "¡Ouch!"

    n "Caes de culo sobre la almohada al ser empujado por [neusname]."

    n "Cuando te fijas en ella ves que ha hundido su rostro en su entrepierna."

    d "¡¡DIOS!!"

    pt "Aparentemente no solo es adicta a mi corrida..."

    n "Ves que sigue succionando a pesar de que estás seguro que se lo ha tragado todo."

    n "Las piernas de Dídac siguen temblando"

    n "mientras [neusname] mueve su cabeza como si estuviera hurgando con su lengua en su interior."

    d "¡Jodeeer....!"

    p "[neusname]..."

    n "Sin prisas, separa sus labios de su entrepierna."

    ne "¿Sí...?"

    p "Pensaba que solo te gustaba mi esperma."

    ne "Me encanta todo en el sexo,"

    ne "pero tu polla simplemente es mi mayor perdición."

    ne "Lamento haberte empujado así."

    ne "Por favor, vuelve a metérsela y asegúrate de correrte pronto,"

    ne "del modo en que tiemblan tus piernas, no creo que aguantes mucho más."

    n "Te fijas en ellas y descubres cuánta razón tiene."

    n "Al observar tu mano, descubres que apenas eres capaz de mantener el pulso,"

    n "casi como si estuviera dentro de una batidora."

    n "Tu cuerpo entero está ardiendo y tus músculos están palpitando sin cesar."

    n "Sientes su aliento acercarse a tu polla."

    n "Su lengua juguetea con tu sensible e hinchado glande,"

    n "para finalmente introducírsela entre sus labios."

    p "Hmm..."

    n "Tu polla está calcinándose en su ardiente boca,"

    n "y su lengua juguetea con la parte inferior de tu miembro."

    n "Hasta que finalmente ves tu polla desparecer en su interior"

    n "mientras sientes su ardiente garganta ahogar tu palpitante miembro."

    pt "Dioos..."

    n "Finalmente te libera."

    n "Te mira con esos ojos brillantes mientras exhala un vapor cálido y denso."

    ne "¿Dónde quieres correrte?"

    if DidacMCPregnant or p_didac.cumReceived == "oral":

        ne "Al fin y al cabo ya te has corrido en su coño..."

    else:

        ne "Al fin y al cabo ya está embarazada."

    p "¿Cómo puedes estar tan segura de que ya está embarazada?"

    ne "Por que si no lo estuviera,"

    ne "a estas horas ya se estaría transformando."

    p "..."

    ne "Voy a succionar todo tu esperma sea dónde sea,"

    ne "pero tienes que elegir."

    # CHOICE

    menu:

        pt "¿Dónde me corro...?"

        "<En su coño>":
            call p_Help
            $pl.ch_pts("dp",1)

            $ day06_neusDidac_dF_03_Vag = True

        "<En su trasero>":
            call p_Help
            #$pl.ch_pts("dp",-1)

            $ day06_neusDidac_dF_03_Vag = False

    if day06_neusDidac_dF_03_Vag:

        p "Me gustaría correrme en su coño y cuando termine,"

    else:

        p "Me gustaría correrme en su trasero y cuando termine"

    p "que me limpies con tu boca."

    ne "Hmmm..."

    if day06_neusDidac_dF_03_Vag:

        ne "No hubiera podido elegir mejor."

    else:

        ne "Como desees..."

    n "Se aparta y vuelve a posar su lengua cerca del clítoris de Dídac."

    n "Te reincorporas poniéndote de rodillas ante sus piernas abiertas"

    n "mientras [neusname] te observa con una mirada lasciva y hambrienta."

    n "Acercas tu polla a su entrepierna y la deslizas en su interior."

    if day06_neusDidac_dF_03_Vag:

        n "Percibes su sexo estrecho y hostil."

    else:

        n "Percibes su cavidad anal estrecha y hostil."

    if day06_neusDidac_dF_03_Vag:

        pt "Lo que me sorprende es que siga entrando después de los orgasmos que ha llegado a tener."

    n "A pesar de que intentas desplazarte lentamente,"

    if day06_neusDidac_dF_03_Vag:

        n "sientes que tu polla palpita descontroladamente en su sexo."

    else:

        n "sientes que tu polla palpita descontroladamente en su interior."

    p "Hmm..."

    # CHOICE say it or she will notice it.

    menu:

        pt "¿Debería avisarla?"

        "No creo que tarde mucho.":
            call p_Help

            $pl.ch_pts("np",1)

        "...":
            call p_Help

            ne "..."

            ne "Sabes que noto cuando estás a punto de correrte,"

            ne "¿verdad?"

            p "..."

            ne "Hmmm..."


    ne "Dale duro."

    n "Sus manos vuelven a separar sus piernas"

    if day06_neusDidac_dF_03_Vag:

        n "y con sus dedos te abre aún más sus labios vaginales"

    else:

        n "y con sus dedos te separa aún más sus nalgas"

    n "mientras sigue jugueteando con su lengua."

    ne "No tengas compasión."

    n "Con cierto esfuerzo, logras penetrar hasta sentir una muralla en su interior."

    d "¡GGGhhhmm...!"

    n "Dídac sigue gimiendo ahogadamente debido a la entrepierna de [neusname],"

    n "mientras esta sigue lamiendo juguetonamente la parte libre de su coño"

    n "y te mira con esos ojos brillantes, obscenos, y famélicos."

    n "Mueves tus caderas sin compasión en su interior"

    if day06_neusDidac_dF_03_Vag:

        n "mientras te deja la entrepierna completamente empapada por sus jugos."

    else:

        n "mientras padeces lo estrecha y caliente que tiene la cavidad anal."

    d "¡¡Ghhhmm...!!"

    n "La lengua de [neusname] se alarga"

    if day06_neusDidac_dF_03_Vag:

        n "y acaricia la base de tu polla que entra y sale de su sexo."

    else:

        n "y acaricia la base de tu polla que entra y sale de su trasero."

    pt "Joder..."

    n "A medida que vas chocando contra el muro del sexo de Dídac,"

    if day06_neusDidac_dF_03_Vag:

        n "Una segunda lengua fisgonea para entrar en su vagina"

    else:

        n "Una segunda lengua fisgonea para entrar en su cavidad anal"

    n "a lo largo de tu herramienta en movimiento."

    n "Pero esta vez, por la parte superior."

    ne "¡No pares!"

    n "Sientes que se arropa a ella para luego moverse como si te masturbara"

    n "sin que hayas detenido en absoluto tus embestidas."

    pt "¡JODER!"

    ne "¡Dale más duro!"

    n "En tu intento de aumentar el ritmo,"

    n "sientes los músculos de todo tu cuerpo vibrar con tanta intensidad"

    n "que el dolor se vuelve casi insoportable,"

    n "tus piernas tiemblan tanto que apenas eres capaz de mantenerte en pie,"

    n "tus manos tambalean de tal modo que apenas logras agarrarte a sus nalgas,"

    n "tu polla palpita con tanta violencia,"

    n "que te da la sensación de que pronto explotará en mil pedazos."

    n "Entre tanto dolor, sientes el familiar cosquilleo en tu entrepierna."

    d "¡¡Ghhhmmm!!"

    n "La lengua de [neusname] se vuelve incluso más caliente"

    n "y se desplaza a mayor velocidad en su interior"

    n "comprimiendo aún más tu palpitante polla."

    pt "¡Dios!"

    n "Justo cuando sientes tu esperma fluir por tu entrepierna hasta tu latente polla,"

    n "la ardiente lengua de [neusname] estruja tan fuertemente tu polla,"

    n "que no le permite su salida."

    p "¡[neusname]...!"

    n "El dolor apenas te permite articular palabra alguna."

    ne "¡No te detengas!"

    p "No-"

    extend "no puedo..."

    ne "{size=30}¡HE DICHO QUE NO TE DETENGAS!{/size}"

    n "Tus manos vuelven a agarrarse con firmeza en esas nalgas."

    pt "¿Qué...?"

    n "Tus caderas recuperan el ritmo, embistiendo las caderas de Dídac,"

    n "como si fueras una bestia desenfrenada."

    pt "Yo no..."

    n "Chocando incluso contra el rostro de [neusname] sin piedad."

    pt "¡¿Mi cuerpo se está moviendo por si solo?!"

    n "Percibes incluso más esperma que antes removiéndose en tu polla palpitante con voluntad de salir,"

    n "pero su lengua sigue presionándote con firmeza."

    with hpunch
    p "¡UGHHH...!"

    n "Hasta que finalmente te libera de su presión y explotas descontroladamente en su interior."

    d "¡¡AGHHHMMMmmm...!!"

    n "Al mismo tiempo,"

    if day06_neusDidac_dF_03_Vag:

        n "el sexo de Dídac te ahoga la polla con sus convulsiones y contorsiones."

    else:

        n "el trasero de Dídac te ahoga la polla con sus convulsiones y contorsiones."

    p "¡Jodeer!"

    n "Las manos de [neusname] te agarran por las nalgas impidiéndote apartar tu polla de su interior."

    n "Cuando te fijas en ella, está de rodillas sobre la cama mirándote fijamente a la cara,"

    n "a la par que Dídac arquea su espalda entre convulsiones por semejante orgasmo desmedido"

    n "mientras tu polla sigue vaciándose en su interior."

    scene morning04_bg bedroom_neus_a
    show kiss_ f_n_01:
        truecenter
        xzoom -1.0
        zoom 1.5 rotate -30
    show light 01:
        light01_topside_position
    with fade_short

    pause 0.2

    show kiss_ f_n_12
    with hpunch

    n "Sientes la lengua de [neusname] entremezclándose con la tuya."

    show kiss_ f_n_08
    with Dissolve (0.2)

    pause 0.2

    show kiss_ f_n_11
    with Dissolve (0.2)

    pause 0.2

    show kiss_ f_n_10
    with Dissolve (0.2)


    n "Tus caderas se mueven casi por voluntad propia y tus piernas siguen temblando sin cesar."

    $ ped_neus_whispers_sfx04 = 0.95
    $ n_exp_shine = -0.01

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front02"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with fade_short

    ne "Me encanta verte así..."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx09
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    scene day06
    with fade_short

    n "Rápidamente desciende hasta tu entrepierna para agarrarte la polla,"

    n "y sacándotela como si quitara el corcho de una botella de champán,"

    n "se traga tu polla entera en su garganta."

    d "¡¡GHHMMM...!"

    n "Sin piedad alguna,"

    n "succiona tu polla como si quisiera tragarse el vacío,"

    n "a pesar de eso, sientes su garganta más ardiente que antes."

    n "succionado sin piedad tu rojiza y sensible polla"

    n "mientras su lengua sigue estrujándote aún más tu sensible y dolorida polla."

    n "Recorre tu miembro con ella hasta llegar a la base de tus testículos,"

    n "dónde te envuelve con su versión longeva y te ahoga esa parte con rudeza."

    pt "¡Jodeer...!"

    n "A pesar del dolor y de tus muecas,"

    n "desplaza el estrecho nudo formado por su lengua en la base de tu polla a lo largo y ancho del miembro"

    n "hasta llegar a tu glande."

    n "Percibes que esas últimas gotas llegan al fondo de su garganta,"

    n "donde su segunda lengua las relame."

    n "Finalmente te libera de su infernal garganta"

    n "mientras sigue relamiendo la base de tu glande"

    n "y te mira con ese rostro de niña traviesa."

    d "Ghhhmm..."

    n "Sus ojos se fijan en las -ya no tan temblorosas- piernas de Dídac"

    if day06_neusDidac_dF_03_Vag:

        n "de dónde se escurren algunas gotas de esperma que brotan de su sexo."

    else:

        n "de dónde se escurren algunas gotas de esperma que brotan de su ano."

    n "Con un movimiento brusco,"

    n "abandona tu polla y se agarra a las piernas de Dídac relamiéndolas como si fuera un animal salvaje."

    pt "¿Aún no ha tenido suficiente?"

    with hpunch
    d "¡Ouch!"

    n "Con un fuerte y rudo movimiento,"

    n "gira el cuerpo de Dídac y se pone debajo de ella"

    n "acercando su cara a las partes de la pierna que aún no había limpiado."

    d "Hmmm..."

    d "No hace falta que seas tan..."

    n "Cuando no queda más esperma por sus piernas,"

    d "¡COÑOOO!"

    if day06_neusDidac_dF_03_Vag:

        n "hunde su rostro en el sexo de Dídac."

    else:

        n "hunde su rostro el agujero anal de Dídac."

    pt "Por su expresión, diría que está disfrutando de su longeva lengua."

    p "Ughh..."

    n "Un dolor punzante en tus temblorosas piernas te hace perder el equilibrio."

    ono "PUM"
    with vpunch

    # you were fucking her with your feet on ground?
    n "Sin poder evitarlo, caes de rodillas en el suelo"

    n "y la parte superior de tu cuerpo se desploma rendido sobre la cama."

    n "Con un ojo entre-abierto sigues viendo a [neusname] devorando con afán su entrepierna"

    n "mientras esta sigue retorciéndose en un dolor-placer particular."

    n "Tus ojos ceden y todo se vuelve oscuro."

    jump day06_ending_NeusDidac


################################################################################################
################################################################################################

################################################################################################
################################################################################################

#  CREDITS SCENE:

label day06_ending_NeusDidac:

    call day06_ending_window

    p "Ughh..."

    ne "¿Te duele?"

    p "Un poco..."

    p "¿Cómo es posible que siga estando dura?"

    ne "Euhhmm..."

    ne "Es que tienes mucha libido..."

    p "..."

    p "[neusname]..."

    ne "¿Sí?"

    p "¿Estás usando dos lenguas?"

    ne "No."

    ne "Hay alguien más que está chupándote la polla,"

    ne "¿verdad?"

    d "Tssk..."

    p "Pensaba que ..."

    # CONDITIONAL, how much love?

    if pl.dp > 90:

        d "¡Me gusta chuparte la polla!"

        d "¡¿Algún problema?!"

        p "No..."

        p "Simplemente me sorprende tu sinceridad."

        ne "La verdad es que sí..."

        d "Tssk..."

    else:

        d "No pienses cosas raras,"

        d "te la  estamos chupando para que se te ponga dura,"

        d "nada más."

        ne "Ya te he dicho que podía hacerlo sola,"

        ne "y aún así has insistido en ayudarme."

        ne "Tan desagradable no te resultará."

        d "..."

        d "¿Nunca te han llamado {i}bocachancla{/i}?"

        ne "¿Por qué te cuesta tanto admitir que te gusta chuparle la polla?"

        d "..."

        ne "¿Es por tu orgullo masculino?"

        ne "Te refieres a ti misma de forma femenina constantemente,"

        ne "has aceptado que vas a ser mujer el resto de tu vida"

        ne "y aún así mantienes la postura de rebelde sin causa."

        ne "¿Por qué?"

        d "..."

        ne "¿Acaso no te gusta su sabor salado y espeso,"

        ne "como se te pega en la lengua,"

        ne "la suavidad y el calor de su glande,"

        ne "o cuando sientes que palpita dentro de tu boca?"

        d "¡Bueno!"

        extend " ¡Vale!"

        d "¡Ya lo he pillado!"

        ne "..."

    d "¿Puedo follármela o no?!"

    p "¿Follarme?"

    ne "Eumm..."

    extend " sí."

    ne "Le he dicho que podría montarte,"

    ne "espero que no te moleste."

    ne "Necesitamos otra corrida tuya para Meritxell."

    p "[neusname],"

    extend " mi polla está..."

    ne "Sí,"

    extend " está un poco jodida."

    ne "Pero solo una corrida más"

    ne "y te dejaré descansar toda la noche."

    p "¿Solo la noche?"

    ne "Por la mañana necesitaré otra dosis."

    p "¿Me quieres matar?"

    ne "No..."

    p "¿Y cómo es posible que mi polla siga estando dura?"

    ne "Euhmm..."

    p "¡Ugh!"

    d "HHMMmm..."

    d "No te flipes,"

    d "que no está tan dura como antes."

    d "Pero sí que es verdad que está bastante más caliente"

    d "y está palpitando todo el tiempo..."

    d "Sinceramente,"

    extend " no tiene muy buen aspecto."

    # CONDITIONAL

    if day06_bloodDrink_cond:

        p "¡¿Es que acaso me he vuelto a tragar su sangre?!"

    else:

        p "¡¿Es que acaso me has hecho beber tu sangre?!"

    ne "Haces demasiadas preguntas."

    p "¡Me vais a matar!"

    d "[neusname] ha dicho que sobrevivirás,"

    d "así que no seas tan llorona."

    ne "Lo siento,"

    ne "pero es que no se te estaba poniendo dura."

    p "¡¿Cuanto tiempo me voy a pasar sin poder moverme?!"

    ne "Euhmmm..."

    ne "No lo sé..."

    d "¿Por qué te disculpas?"

    d "Si seguro que lo está disfrutando como un perro."

    ne "En realidad,"

    ne "creo que a estas alturas debe de sentir bastante dolor..."

    d "No te callarás,"

    extend " ¿verdad?"

    p "Y luego el egoísta soy yo..."

    $ day06_morning_Didac_buttockSlaps += 1

    ono "SPLASH"

    p "Auch!"

    d "No te quejes tanto,"

    d "que la que tiene que montarte soy yo."

    d "Ufff..."

    d "Me encanta.."

    p "Ughh..."

    d "¡¿Tan pronto?!"

    d "¡No aguantas una mierda!"

    ne "Bueno,"

    ne "técnicamente hace media hora que se la estamos chupando,"

    ne "bastante ha aguantado en realidad..."

    d "¿Nunca te han dicho que hablas demasiado?"

    ne "..."

    d "Al menos usa tu lengua en sus pelotas para hacer su corrida más intensa."

    ne "Cuando se vaya a correr,"

    extend " te apartas."

    d "..."

    # CONDITIONAL where did you cum?

    if day06_neusDidac_dF_03_Vag:

        ne "Ya te he dicho que esta vez no se puede correr dentro de ti."

    else:

        ne "Ya te he dicho que ahora no se puede correr dentro de ti."

        d "¡Ni ahora ni antes!"

    ne "Necesito todo su esperma para Meritxell."

    if day06_neusDidac_dF_03_Vag:

        d "Y no podrías meter luego tu lengua para sacarme todo su esperma como hiciste antes?"

        ne "¿Quieres que me enfade?"

        d "Vale,"

        extend " vale..."

    p "¡Ugh!"

    d "¡Auch!"

    ne "¡Te había dicho que te apartaras!"

    p "[neusname]..."

    p "Ufffhh..."

    ne "Hmm..."

    ne "Parece que tu polla ya no da más de si..."

    p "Me vais a matar..."

    ne "Es lo último que desearía."

    ne "Tranquilo,"

    ne "ahora ya puedes tomarte tu merecido descanso,"

    if gensex_ILoveYouNeus:

        extend " mi apuesto Lancelot."

    else:

        extend "nuestro querido semental."

    if gensex_ILoveYouNeus:

        ne "Te amo."

    else:

        ne "Me encanta tu polla,"

        ne "aunque no esté del todo dura..."

    d "¡Iros a un hotel!"

    ne "¿Tú eres tonta?"

    d "Tanta ñoñería me resulta insoportable."

    ne "Pues acostúmbrate,"

    ne "o vete buscando otra polla que te satisfaga."

    d "Pero,"

    extend " ¿no es la única que puede...?"

    ne "Precisamente."

    d "Tsskk..."

    window hide dissolve
    pause

    call false_gameover

    jump textless_gameover

    # Te despiertas estirado en la cama, mientras sientes dos lengus juguetear con tu entrepierna.
    # Neus... por qué usas tus dos lenguas?
    # Solo estoy usando una.
    # Dídac?
    # Solo hago esto para ponertela dura.
    # Ya hace rato que está dura...
    # Tú cállate!
    # Por qué no admites de una vez que disfrutas de su polla en todos sus aspectos?
    # Mentirte a ti misma no te ayudará en nada.
    # Disfrutas de su polla, aunque sea chupándosela, no es cierto?
    # ...
    # Actuas de forma masculina, pero en la cama te gusta ser domada y follada como la que más.
    # ...
    # No tiene nada de malo, pero cuanto antes lo aceptes, antes lo disfrutarás de esta manera.
    # Tssk...
    # ¿Por qué no te callas?



    # Ugh...
    # Quizás emipeza a dolerte.
    # Me has dicho que podía follármelo si se ponía dura.
    # Ya...


    # They are sucking your dick, while blubering about it. Didac admits that loves to suck your dick. and she wants to fuck you, but Neus remind her, this time is important she receives the cum so she could share it better to Meritxell.