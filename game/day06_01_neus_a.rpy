
default day06_ending_city = "paris"
default day06_escapeWithDidac = False
default day06_bloodDrink_cond = False
default mc_stat = ""

default pdaytime = "day01"
default pday_day = 1

default p_bg = "" # Background for Oral Sex Parts.

default df_eye = "front04" # Character Eyes (For general purposes)
default df_blush = 0 # Character Blush


default n_dress = ""

default day06_morning_MC_orgasms = 0

default day06_morning_Didac_orgasms = 0
default day06_morning_Txell_orgasms = 0
default day06_morning_Neus_orgasms = 0

default day06_morning_Didac_buttockSlaps = 0

default day06_morning_Neus_lickingUnder = ""
default day06_morning_Didac_lickingUnder = ""
default day06_morning_Txell_lickingUnder = ""

default day06_morning_rejection = ""

default day06_neusAlone_sex = "vaginal"



#########
#########

label day06_night_label:

    if config.version < "00.99.99": #For FUTURE
        call endupdatescript

    $ p_ao_n_hipsImg = "_open"
    $ p_ao_n_hipsTrans = 0.5
    $ p_ao_n_tongue = ""
    $ p_ao_n_horns = ""
    $ p_ao_n_horns_num = 0
    $ p_ao_n_tail = ""
    $ p_ao_n_tail_num = 0
    $ p_ao_n_wings = ""
    $ p_ao_n_wings_num = 0
    $ p_ao_n_fur = ""
    $ p_ao_n_fur_num = 0
    $ p_ao_n_dick = ""
    $ p_ao_n_dick_num = 0
    $ p_ao_n_size = ""
    $ p_ao_n_size_num = 0
    $ p_ao_n_blur = ""
    $ p_ao_n_blur_num = 0
    $ p_ao_mc_dick = "" # How Reddish it is.
    $ p_ao_mc_dick_num = 6 # How Big it is.
    $ p_ao_ground = "ground"

    $ d_bodyType = "_slim" # probably in future I should delete this.

    $ pdaytime = "06morning"
    $ pday_day = 6
    $ nblush = 3
    $ ntlong = 0

    $ p_ao_background = ""
    $ n_withoutGlasses_story = False

    $ ped_neus_whispers_sfx01 = 0
    $ ped_neus_whispers_sfx02 = 0
    $ ped_neus_whispers_sfx03 = 0
    $ ped_neus_whispers_sfx04 = 0

    $ p_neus.closeOrgasm = 0
    $ p_neus.pleasure = 0
    $ p_neus.closeOrgasmTotal = 0

    $ p_didac.closeOrgasm = 0
    $ p_didac.pleasure = 0
    $ p_didac.closeOrgasmTotal = 0

    $ p_txell.closeOrgasm = 0
    $ p_txell.pleasure = 0
    $ p_txell.closeOrgasmTotal = 0


    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ saturation_tint_level = "default"

    $ day06_company = "neusAlone"

    # It's not morning, it's about 21:00 at night.

    $ renpy.notify("[p_diff]")

    if (pl.np < 100 and gensex_YoureAMonster) or p_ao_neusLastSecret:

        if not p_ao_neusLastSecret:
            $ renpy.notify("[p_neg] 100[hn]")

        $ day06_company = "atHome"

        jump day06_night_home

    elif DidacPregnant and (pl.np < 100 and pl.dp > 90):

        # if Didac is not pregnant, he must remain in bed due for the illnes.

        $ day06_company = "didacAlone"

        jump day06_didacAlone_01

    #elif Txell alone, not yet done.

    else:

        $ day06_company = "neusAlone" # For now, later can be different depend on choices and points.

        jump day06_night_neus


label day06_night_neus:

    play music "audio/sfx/birds01.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/rubbingPussy01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    scene black with fade
    
    $ renpy.notify("Day 06")

    n "El cantar de los p??jaros es lo primero que te llama la atenci??n por su agudo silbido."

    n "Pero hay otro sonido extra??o que te llama m??s la atenci??n."

    play sound "audio/characters/neus/moan06.ogg"

    gn "Mfff... mm... ah..." #Strong Feminine Moans

    n "Sientes una c??lida y h??meda sensaci??n en tu entrepierna."

    pt "????Otra vez el mismo jodido sue??o?!"

    play sound "audio/characters/neus/moan04.ogg"

    n "Una suave piel roza tu ombligo,"

    if p_neus.cumReceived == "vaginal":

        n "mientras tu polla se encuentra ahogada en una ardiente y h??meda carne."

    else:

        n "mientras tu polla se encuentra cercada entre una c??lida y h??meda carne y el vac??o."

        n "Como si una mujer estuviera rozando sus empapados labios vaginales"

        n "contra tu erecto y sensible miembro."

    gn "Mmmm... mfh..." #Strong Feminine Moans

    pt "Este sue??o parece mucho m??s real..."

    pt "Un segundo..."

    gn "Aahhmm... Ghmmgh..." #Strong Feminine Moans

    # scene black
    # show light 01:
    #     light01_topside_position
    # with fade

    pt "Estos gemidos suenan a los de [neusname]."

    scene morning04_bg bedroom_neus_a # Bitch
    show morning04_bedroom_Neus_body 01a:
        morning04_bedroom_Neus_body_anim
        
    show morning04_bedroom_Neus_bodyass 01a:
        morning04_bedroom_Neus_bodyass_anim02

    show light 01:
        light01_topside_position
    

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light_01b :
        light01_topside_position

    with fade
    
    window hide dissolve
    pause

    n "Entreabres los ojos y te encuentras un oscuro y borroso cuerpo justo encima de ti."

    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01b
    with dissolve

    if p_neus.cumReceived == "vaginal":

        n "Esa extra??a silueta hace temblar tu cuerpo mientras te cabalga."

    else:

        n "Esa extra??a silueta hace temblar tu cuerpo mientras desliza su entrepierna contra tu miembro."

    p "[neusname]..."

    show morning04_bedroom_Neus_body 01c
    show morning04_bedroom_Neus_bodyass 01b
    with dissolve

    p "??Eres realmente t???"

    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01c
    with dissolve

    n "Con un movimiento sutil y sugerente, se vuelve hacia ti."

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    # Here would start the music, right?
    if music_play != "last_kiss_goodnight":
        play music "audio/music/kevinmacleod/last_kiss_goodnight.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "last_kiss_goodnight"

    window hide dissolve
    pause
    
    play sound "audio/characters/neus/giggle03.ogg"
    
    hide morning04_bedroom_Neus_body 
    hide morning04_bedroom_Neus_bodyass
    hide light
    hide morning04_bedroom_DMast_blinkeye
    hide light_screen_01
    show morning04_bg bedroom_neus_a
    show morning04_bedroom_Neus_body_ass 02a: 
        morning04_bedroom_Neus_bodyass_anim01
    show morning04_bedroom_Neus_body_body 02a
    #show morning04_bedroom_Neus_Prove
    show morning04_bedroom_Neus_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_mouth happy_Talkingx03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyes 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyepupils front_green_03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyebrows normal:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_glasses:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_body_hair 02a

    show light 01:
        light01_topside_position

    with fade

    ne "??Por qu???"

    show morning04_bedroom_Neus_exp_eyebrows sadx01
    show morning04_bedroom_Neus_exp_mouth happy_Talkingx04
    with dissolve 

    ne "??Es que has so??ado conmigo?"

    show morning04_bedroom_Neus_body_ass 02b
    show morning04_bedroom_Neus_body_body 02b
    show morning04_bedroom_Neus_body_hair 02b
    show morning04_bedroom_Neus_exp_eyebrows normal
    show morning04_bedroom_Neus_exp_mouth happy_Silentx03
    with Dissolve (1.0)

    $ day06_neusSex_Dislike = False

    menu:

        pt "Parece que esta vez no se trata de un sue??o..."

        "De hecho, llevo dos d??as so??ando contigo.":
            call p_Help
            $pl.ch_pts("np",2)

            show morning04_bedroom_Neus_exp_eyebrows sadx02
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
            with dissolve 

            ne "No sabes lo feliz que me hace o??r eso."

            show morning04_bedroom_Neus_exp_eyebrows sadx03
            show morning04_bedroom_Neus_exp_mouth happy_Silentx04
            with dissolve 

            menu:

                pt "??Realmente era un sue??o lo de ayer?"

                "Aunque en el sue??o de ayer ten??as los ojos rojos y la voz parec??a distinta...":
                    call p_Help

                    #$pl.ch_pts("np",2)

                    show morning04_bedroom_Neus_exp_eyebrows surprisex01
                    show morning04_bedroom_Neus_exp_mouth sad_Silentx03
                    with dissolve 

                    ne "Hmmm..."

                    if music_play != "wounded":
                        play music "audio/music/kevinmacleod/sad/wounded.ogg" fadein 2.0 fadeout 2.0
                        $ music_play = "wounded"

                    show morning04_bedroom_Neus_exp_eyebrows sadx02
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx03
                    with dissolve 

                    ne "Vaya,"

                    show morning04_bedroom_Neus_exp_eyebrows sadx03
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                    with dissolve 

                    ne "entonces supongo que en ese caso fue Padre..."

                    show morning04_bedroom_Neus_exp_eyebrows surprisex02
                    show morning04_bedroom_Neus_exp_mouth sad_Silentx02
                    with dissolve 

                    p "????Acaso crees que esa cabra inmunda me follar??a en sue??os?!"

                    show morning04_bedroom_Neus_exp_eyebrows sadx02
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve 

                    ne "No sabes de lo que es capaz..."

                    show morning04_bedroom_Neus_exp_eyebrows sadx03
                    show morning04_bedroom_Neus_exp_mouth sad_Silentx04
                    with dissolve 

                "No tanto como a mi.":
                    call p_Help

                    $pl.ch_pts("np",2)

                    show morning04_bedroom_Neus_exp_eyebrows sadx01
                    show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                    with dissolve 

                    ne "jejeje *Risilla inocente*"

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
                    with dissolve 

                    ne "Tont??n."

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth happy_Silentx03
                    with dissolve 


        "??Tanto te sorprender??a?":
            call p_Help

            $pl.ch_pts("np",1)

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth sad_Silentx03
            with dissolve 

            ne "..."

            show morning04_bedroom_Neus_exp_eyebrows sadx01
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
            with dissolve 

            ne "Me gustar??a pensar que no..."

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth happy_Silentx03
            with dissolve 

        "Simplemente me preguntaba si serias capaz de follarte a alguien mientras est?? inconsciente.":
            call p_Help

            $pl.ch_pts("np",-2)
            $ day06_neusSex_Dislike = True

            show morning04_bedroom_Neus_exp_eyebrows surprisex02
            show morning04_bedroom_Neus_exp_mouth sad_Silentx01
            with dissolve 

            ne "..."

            show morning04_bedroom_Neus_exp_eyebrows sadx03
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx03
            with dissolve 

            ne "No pens?? que te molestar??a tanto..."

            show morning04_bedroom_Neus_exp_eyebrows sadx03
            show morning04_bedroom_Neus_exp_mouth sad_Silentx04
            with dissolve 

    p "..."

    show morning04_bedroom_Neus_exp_eyebrows sadx02
    show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
    with dissolve 

    ne "Ya s?? que deber??a haberte dejado descansar un poco m??s,"

    if music_play != "last_kiss_goodnight":
        play music "audio/music/kevinmacleod/last_kiss_goodnight.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "last_kiss_goodnight"

    show morning04_bedroom_Neus_exp_eyebrows sadx01
    show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
    with dissolve 

    ne "pero es que al v??rtela as??,"

    show morning04_bedroom_Neus_exp_eyebrows sadx02
    show morning04_bedroom_Neus_exp_mouth sad_Talkingx001
    with dissolve 

    ne "no he podido resistirlo..."

    if day06_neusSex_Dislike:

        show morning04_bedroom_Neus_exp_eyebrows sadx03
        show morning04_bedroom_Neus_exp_mouth sad_Talkingx04
        with dissolve 

        ne "Pero supongo que ha sido una mala idea..."

        show morning04_bedroom_Neus_exp_eyebrows sadx03
        show morning04_bedroom_Neus_exp_mouth sad_Silentx04
        with dissolve 

        jump day06_afterWakeUp_wrong

    else:

        show morning04_bedroom_Neus_exp_eyebrows normal
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        with dissolve 

        ne "Espero que no te moleste."

        show morning04_bedroom_Neus_exp_eyebrows sadx01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve 

        menu:

            pt "Que no me moleste..."

            "Claro que no me molesta.":
                call p_Help
                $pl.ch_pts("np",2)

                show morning04_bedroom_Neus_exp_eyebrows sadx02
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve 

                if gensex_ILoveYouNeus:
                    ne "Eres un amor."

                else:
                    ne "Gracias."

                show morning04_bedroom_Neus_exp_eyebrows sadx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx04
                with dissolve 

                jump day06_afterWakeUp

            "Preferir??a que no lo hicieras mientras estoy inconsciente.":
                call p_Help
                $pl.ch_pts("np",-1)
                $ day06_neusSex_Dislike = True

                show morning04_bedroom_Neus_exp_eyebrows surprisex02
                show morning04_bedroom_Neus_exp_mouth sad_Silentx04
                with dissolve

                pause 0.2

                show morning04_bedroom_Neus_exp_eyebrows angryx03
                show morning04_bedroom_Neus_exp_mouth sad_Silentx04
                with dissolve 

                jump day06_afterWakeUp_wrong

            "Es de muy mal gusto follarte a alguien mientras est?? durmiendo.":
                call p_Help
                $pl.ch_pts("np",-2)
                $ day06_neusSex_Dislike = True

                show morning04_bedroom_Neus_exp_eyebrows surprisex02
                show morning04_bedroom_Neus_exp_mouth sad_Silentx04
                with dissolve 

                jump day06_afterWakeUp_wrong

            "Tampoco es que me sorprenda que acabes haciendo lo que te da la gana sin mi permiso." if gensex_YoureAMonster:
                call p_Help
                $pl.ch_pts("np",-4)
                $ day06_neusSex_Dislike = True

                show morning04_bedroom_Neus_exp_eyebrows surprisex02
                show morning04_bedroom_Neus_exp_mouth sad_Silentx04
                with dissolve 

                jump day06_afterWakeUp_wrong

label day06_afterWakeUp_wrong:

    pause 0.2

    scene day05
    with fade

    ne "Lo siento..."

    jump day06_neusAlone_noBlowjobWanted


label day06_afterWakeUp:

    pause 0.2

    scene morning04_bg bedroom_neus_a
    show kiss_ f_n_07:
        truecenter
        xzoom -1.0
        zoom 1.5 rotate -30
    show light 01:
        light01_topside_position

    # show light 01:
    #     light01_rightside_position
    # show light_screen_01:
    #     light_screen_01_position
    with fade

    n "Acerca sus labios a los tuyos y con dulzura acaricia tu mejilla"

    show kiss_ f_n_02
    with Dissolve(0.5)

    pause 0.2

    show kiss_ f_n_10
    with Dissolve(0.5)

    pause 0.2

    show kiss_ f_n_12
    with Dissolve(0.5)

    n "mientras os mezcl??is en un dulce beso."

    show kiss_ f_n_09
    with Dissolve(0.5)

    ne "Te prometo que esta vez intentar?? no dejarte tan seco."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears

    # show light 01:
    #     light01_rightside_position
    # show light_screen_01:
    #     light_screen_01_position

    with fade

    ne "Pero a partir de hoy tienes la obligaci??n de darme de comer cada ma??ana,"

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "sin falta."

    $ nteye = "front02"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    n "No percibes ni el m??s m??nimo atisbo de iron??a en su tono de voz."

    $ nteye = "right03"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Y quiz??s tambi??n por la noche..."

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque si quieres hacerlo tambi??n por la tarde,"

    $ nteye = "right04"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "o cualquier otra hora, en realidad,"

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx02
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "no me quejar??."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx05
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "????Es que no ha visto lo roja que tengo la polla despu??s de un solo d??a con ella?!"

        "??Hablas en serio?":
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows angryx01
            call n_closefromup_tears_tears
            with dissolve

            ne "Por supuesto que s??."

            $ nteye = "front02"
            show n_closefromup_mouth happy_Silentx03
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

        "Me quieres matar, ??verdad?":
            call p_Help

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo justo para que sobrevivas."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            pt "????Habla en serio?!"

        "Har?? lo que quiera, no lo que me exijas":
            call p_Help
            #$pl.ch_pts("np", -1)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if gensex_ILoveYouNeus:

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Tampoco hace falta que te lo tomes as??..."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Pens?? que hab??as dicho que me amabas."

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx06
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    pt "??Qu?? entiende esta mujer por amor?"

                    "Har?? lo que me pides, pero solo cuando nos apetezca a los dos.":
                        call p_Help

                        #$pl.ch_pts("np", 2)

                        $ nteye = "front01"
                        show n_closefromup_mouth sadbiting_Silentx02
                        show n_closefromup_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Perdona."

                        $ nteye = "right02"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero es que..."

                    "Y te amo, pero una relaci??n es cosa de dos personas, no solo de una.":
                        call p_Help

                        $pl.ch_pts("np",1)

                        $ nteye = "front01"
                        show n_closefromup_mouth sadbiting_Silentx02
                        show n_closefromup_eyebrows surprisex01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx02
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Tienes raz??n..."

                        $ nteye = "left05"
                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero..."

                    "Y es as?? como me vas a tratar a partir de ahora?":
                        call p_Help
                        $pl.ch_pts("np", -1)

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx002
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No..."

                        $ nteye = "front01"
                        show n_closefromup_mouth sadbiting_Silentx01
                        show n_closefromup_eyebrows surprisex02
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Ah,"

                        extend " ??no?"

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Talkingx06
                        show n_closefromup_eyebrows angryx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "??Te crees que lo hago a prop??sito?"

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows angryx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "??Que lo hago por pura avaricia y codicia?"

                    "...":
                        call p_Help

                        pass



            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "??Te crees que si no lo necesitara,"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_eyebrows angryx01
            call n_closefromup_tears_tears
            with dissolve

            ne "te lo pedir??a?"

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "??Realmente crees que soy as?? de ego??sta por puro capricho?"

            $ nteye = "front04"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "Ego??sta por puro capricho..."

                "Lo siento.":
                    call p_Help

                    $pl.ch_pts("np", 1)

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx001
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No,"

                    $ nteye = "front06"
                    show n_closefromup_mouth happy_Talkingx02
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "tienes raz??n."

                    $ nteye = "right01"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "no deber??a exigirte tanto."

                    $ nteye = "front03"
                    show n_closefromup_mouth happy_Talkingx03
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "El simple hecho de que est??s a mi lado,"

                    $ nteye = "front06"
                    show n_closefromup_mouth happy_Talkingx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "ya es mucho m??s de lo que puedo pedir."

                    $ nteye = "front05"
                    show n_closefromup_mouth happy_Silentx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                "Es la sensaci??n que me est?? dando.":
                    call p_Help

                    $pl.ch_pts("np", -2)

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lamento que pienses as??."

                    $ nteye = "right02"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Pens?? que realmente me entend??as,"

                    $ nteye = "right03"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "pero supongo que me equivoqu??..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                "...":
                    call p_Help

                    $pl.ch_pts("np", -1)

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

            p "..."

        "...":
            call p_Help
            pass

    # CHECKING
############################################################################################
##############################################
##############################################

    if not p_prot_NotJustMasturbate_with_p_neus:
        progcheck "In theory you only masturbated with Neus."

    if p_prot_NotJustMasturbate_with_p_any:
        if p_prot_NotJustMasturbate_with_p_didac:
                progcheck "In theory you did something with Didac."
        if p_prot_NotJustMasturbate_with_p_txell:
            progcheck "In theory you did something with Txell."

    if DidacPregnant:
        if DidacMCPregnant:
            progcheck "Didac is pregnant by you."
        elif DidacOKUPregnant:
            progcheck "Didac is pregnant by Okupa."
        else:
            progcheck "Didac is pregnant by someone else."

    if gensex_YoureAMonster:
        progcheck "Is possible you can be here if you called her MONSTER?"
    if pl.np < 100:
        progcheck "Is possible to be here with less than 100 points with Neus?"

    progcheck "Didac Points: [pl.dp]\nTxell Points: [pl.mp]\nNeus Points: [pl.np]"

############################################################################################
##############################################
##############################################

    if DidacPregnant and p_prot_NotJustMasturbate_with_p_any and pl.dp>70 and pl.mp > 150:

        aj "??En serio?"

        aj "Subiendo los puntos con Meritxell no te va a dar a??n el final har??n que buscas."

        aj "Su ruta a??n no est?? terminada."

        call WIP

    elif p_prot_NotJustMasturbate_with_p_txell and pl.mp > 150:

        aj "Ya s?? que quieres un final con Meritxell,"

        aj "pero esa ruta a??n no est?? hecha, lo siento."

        call WIP

    if DidacPregnant and p_prot_NotJustMasturbate_with_p_didac and pl.dp>70:

        $ day06_company = "neusDidac"

        jump day06_neusDidac_01 

    else:

        if gensex_YoureAMonster:

            progcheck "Is possible you can be here if you called her MONSTER?"

        if pl.np < 100:

            progcheck "Is possible to be here with less than 100 points with Neus?"

        $ day06_neusAlone_whereAreThey_cond = False
        $ day06_neusAlone_whereAreWe_cond = False
        $ day06_neusDidac_whereWeAre_trust_Cond = "trust"

        scene day06
        with fade

        n "A trav??s de la ventana de la habitaci??n d??nde os encontr??is,"

        n "observas que ya est?? anocheciendo."

        p "????Es que me he pasado el d??a durmiendo?!"

        ne "B??sicamente."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears

        # show light 01:
        #     light01_rightside_position
        # show light_screen_01:
        #     light_screen_01_position

        with fade

        ne "Estabas muy cansado."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx03
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        jump day06_neusAlone_01

label day06_neusAlone_01:

    if not day06_neusAlone_whereAreThey_cond or not day06_neusAlone_whereAreWe_cond:
        menu:
            "??D??nde est??n D??dac y Meritxell?" if not day06_neusAlone_whereAreThey_cond:
                call p_Help
                $ day06_neusAlone_whereAreThey_cond = True
                jump day06_neusAlone_whereAreThey

            "??D??nde estamos?" if not day06_neusAlone_whereAreWe_cond:
                call p_Help
                $ day06_neusAlone_whereAreWe_cond = True
                jump day06_neusAlone_whereAreWe

            "...":
                call p_Help

                jump day06_neusAlone_02
    else:
        jump day06_neusAlone_02

label day06_neusAlone_whereAreThey:

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Est??n en otra habitaci??n."

    if not DidacPregnant:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        p "??D??dac est?? bien?"

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "S??."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero est?? pasando por el mismo calvario que sufri?? cuando se convirti?? en mujer."

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Aunque esta vez la transformaci??n est?? siendo a la inversa."

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Ya ver??s como ma??ana se encuentra mejor"

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "y vuelve a ser el de siempre."

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        p "??Y...?"

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Le ped?? a Meritxell si se pod??a mantener a su lado,"

        $ nteye = "right03"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        ne "por si lo necesitaba."

        $ nteye = "front00"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        p "Me sorprende que esa mujer quiera ayudar a D??dac."

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "Cuando se quita su m??scara de mujer dura y distante,"

        $ nteye = "front08"
        show n_closefromup_mouth happy_Talkingx004
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        ne "estoy segura de que te sorprender??a descubrir"

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "lo cari??osa y atenta que puede llegar a ser."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx04
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        pt "Quiz??s,"

        extend " si eres mujer..."

    else:

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        ne "Aparentemente,"

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "cuando ayer por la noche las dejamos a solas,"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "se hicieron bastante amigas,"

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "por decirlo de alg??n modo."

        $ nteye = "front01"
        show n_closefromup_mouth sadbiting_Silentx02
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        p "Quieres decir que..."

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Es lo m??s probable."

        # if p_prot_NotJustMasturbate_with_p_neus:
        #     progcheck "In theory you did something with Neus."

        # if p_prot_NotJustMasturbate_with_p_any:
        #     if p_prot_NotJustMasturbate_with_p_didac:
        #             progcheck "In theory you did something with Didac."
        #     if p_prot_NotJustMasturbate_with_p_txell:
        #         progcheck "In theory you did something with Txell."

        if gensex_YoureAMonster:

            if not p_prot_NotJustMasturbate_with_p_neus:

                call day06_neusAlone_whereAreThey_preference
                # YOU DID SOMETHING WITH OTHERS.

            else:

                ne "Teniendo en cuenta que a??n me consideras un monstruo,"

                ne "me sorprendi?? bastante que ayer solo usaras la mano con ellas..."

                ne "As?? que pens?? que quiz??s a??n prefer??as tenerme a solas..."

        else:

            if not p_prot_NotJustMasturbate_with_p_neus:

                call day06_neusAlone_whereAreThey_preference
                # YOU DID SOMETHING WITH OTHERS.

            elif p_prot_NotJustMasturbate_with_p_any:

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                if p_prot_NotJustMasturbate_with_p_didac and p_prot_NotJustMasturbate_with_p_txell:

                    ne "Aunque viendo que ayer tambi??n hiciste cosas con ellas..."

                elif p_prot_NotJustMasturbate_with_p_didac:

                    ne "Aunque viendo que ayer tambi??n hiciste cosas con D??dac..."

                elif p_prot_NotJustMasturbate_with_p_txell:

                    ne "Aunque viendo que ayer tambi??n hiciste cosas con Meritxell..."

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Pens?? que quiz??s no te gustar??a estar a solas conmigo..."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx04
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

            else:

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Aunque viendo que ayer no les prestaste mucha atenci??n,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "pens?? que quiz??s prefer??as tenerme a solas."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

        if gensex_ILoveYouNeus:

            pt "??Cu??ntas veces tengo que decirle que la amo para que lo entienda?"

        else:
            p "..."

        if p_prot_NotJustMasturbate_with_p_neus:

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "??Me he equivocado?"

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

        else:

            $ nteye = "right03"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Est?? claro que me he equivocado al pensar que te gustar??a estar a solas conmigo..."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        $ day06_neusAlone_neusWrong_silence_cond = False

        menu day06_neusAlone_neusWrong_question:

            pt "A solas conmigo..."

            "No, no te has equivocado.":
                call p_Help
                $pl.ch_pts("np", 2)

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx03
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Me alegro."

                $ nteye = "front08"
                show n_closefromup_mouth happy_Silentx03
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            "En realidad, no quer??a hacer nada con ninguna de vosotras." if gensex_YoureAMonster:
                call p_Help
                $pl.ch_pts("np", -3)

                if p_prot_NotJustMasturbate_with_p_neus:

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Entonces por qu?? hiciste algo conmigo?"

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows suspiciousx01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Porque si no lo hubiera hecho,"

                    $ nteye = "front00"
                    show n_closefromup_mouth sad_Silentx01
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "te hubieras enfadado conmigo."

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Por qu?? no me dejaste hacerte nada?"

                    $ nteye = "front00"
                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "??A??n me lo preguntas?"

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                ne "??Tan horrible crees que soy?"

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                p "??Acaso me has demostrado lo contrario?"

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Supongo que suplicarte una oportunidad es pedirte demasiado..."

                $ nteye = "right04"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "right05"
                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

            "Un poco m??s de compa????a, no estar??a mal.":
                call p_Help

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "??Acaso no te parezco suficiente?"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                pt "Es obvio que no..."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx03
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                p "Solo digo que cuantos m??s seamos,"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows suspiciousx01
                call n_closefromup_tears_tears
                with dissolve

                p "m??s entretenida y agradable puede ser la situaci??n."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Supongo que el sue??o de tener un har??n para ti solo,"

                $ ntlong += 1

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "es algo con lo que mi peque??o cuerpo no puede competir."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx002
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Dime tonta,"

                $ ntlong += 1

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "pero pens?? que conmigo tendr??as suficiente."

                $ nteye = "front08"
                show n_closefromup_mouth sadbiting_Silentx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    pt "Con ella tendr??a suficiente..."

                    "Quiz??s tengas raz??n.":
                        call p_Help

                        $pl.ch_pts("np", 1)

                        $ nteye = "front05"
                        show n_closefromup_mouth sadbiting_Silentx04
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx02
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me alegra o??rte decir eso."

                        $ nteye = "right05"
                        show n_closefromup_mouth sadbiting_Silentx03
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                    "Me dir??s que cu??ndo pasaste tu lengua por ellas, no lo disfrutaste...":
                        call p_Help
                        #$pl.ch_pts("np", -1)

                        $ nteye = "front00"
                        show n_closefromup_mouth sadbiting_Silentx02
                        show n_closefromup_eyebrows surprisex02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Talkingx02
                        show n_closefromup_eyebrows suspiciousx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Euh..."

                        $ nteye = "right02"
                        show n_closefromup_mouth sad_Talkingx004
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Eso no tiene nada que ver."

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Lo hice para poder salvarles la vida."

                        $ nteye = "front00"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows surprisex03
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Tambi??n era necesario hacerlo con tanta pasi??n?"

                        $ nteye = "right01"
                        show n_closefromup_mouth sadbiting_Silentx03
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "right03"
                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No es algo que pueda controlar,"

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "y menos cuando se trataba de compartir tu esperma."

                        $ nteye = "front01"
                        show n_closefromup_mouth sadbiting_Silentx03
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        p "Suena a excusa barata."

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Es la verdad."

                        $ ntlong = 0

                        $ nteye = "front08"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows sadx02
                        call n_closefromup_tears_tears
                        with dissolve

                    "Pues te equivocaste." if not gensex_ILoveYouNeus:
                        call p_Help
                        $pl.ch_pts("np", -5)

                        $ nteye = "front00"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows surprisex02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ ntlong += 1

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx02
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Me entristece que digas eso."

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows angryx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Pero D??dac ha preferido estar con ella que contigo,"

                        $ nteye = "right02"
                        show n_closefromup_mouth sad_Talkingx06
                        show n_closefromup_eyebrows angryx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "y obviamente Meritxell no tiene ning??n inter??s en ti."

                        $ ntlong += 1

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx005
                        show n_closefromup_eyebrows angryx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "As?? que lament??ndolo mucho tendr??s que conformarte conmigo."

                        $ nteye = "right03"
                        show n_closefromup_mouth sadbiting_Silentx08
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                        $ ntlong == 0

                        $ nteye = "front08"
                        show n_closefromup_mouth sadbiting_Silentx07
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                    "...":

                        call p_Help
                        $pl.ch_pts("np", -4)

                        $ nteye = "front085"
                        show n_closefromup_mouth sad_Silentx05
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ ntlong += 1

                        $ nteye = "right05"
                        show n_closefromup_mouth sad_Silentx09
                        show n_closefromup_eyebrows sadx08
                        call n_closefromup_tears_tears
                        with dissolve

                        pause 0.2

                        $ ntlong = 0

                        $ nteye = "front06"
                        show n_closefromup_mouth sad_Silentx07
                        show n_closefromup_eyebrows angryx03
                        call n_closefromup_tears_tears
                        with dissolve

                        pause 0.2

                        $ nteye = "left05"
                        show n_closefromup_mouth sad_Silentx05
                        show n_closefromup_eyebrows sadx09
                        call n_closefromup_tears_tears
                        with dissolve

            "El sexo no tiene nada que ver con el amor." if not gensex_YoureAMonster:
                call p_Help
                $pl.ch_pts("np", 1)

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Quiz??s no."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero me gustar??a pensar que te atraigo f??sicamente,"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "aunque fuera solo un poco."

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    "Por supuesto que me atraes.":
                        call p_Help

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        if not p_prot_NotJustMasturbate_with_p_neus:
                            $pl.ch_pts("np", -3)

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx07
                            show n_closefromup_eyebrows angryx02
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Desde luego,"

                            $ nteye = "right03"
                            show n_closefromup_mouth sad_Talkingx09
                            show n_closefromup_eyebrows angryx03
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "ayer me lo demostraste con creces..."

                            $ nteye = "right05"
                            show n_closefromup_mouth sadbiting_Silentx05
                            show n_closefromup_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                        else:
                            $pl.ch_pts("np", 1)

                            $ nteye = "front06"
                            show n_closefromup_mouth happy_Talkingx02
                            show n_closefromup_eyebrows sadx02
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Me alegra o??rte decir eso."

                            $ nteye = "right05"
                            show n_closefromup_mouth sadbiting_Silentx04
                            show n_closefromup_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve


                    "No solo me atraes, te amo." if gensex_ILoveYouNeus:
                        call p_Help

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows surprisex02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        if not p_prot_NotJustMasturbate_with_p_neus:
                            $pl.ch_pts("np", -2)

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx02
                            show n_closefromup_eyebrows sadx02
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Ya vi lo mucho que te atraigo ayer..."

                            $ nteye = "right05"
                            show n_closefromup_mouth sadbiting_Silentx03
                            show n_closefromup_eyebrows sadx02
                            call n_closefromup_tears_tears
                            with dissolve


                        else:
                            $pl.ch_pts("np", 2)

                            $ nteye = "front02"
                            show n_closefromup_mouth sadbiting_Silentx03
                            show n_closefromup_eyebrows serious
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            $ nteye = "front06"
                            show n_closefromup_mouth happy_Silentx04
                            show n_closefromup_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                            n "Una dulce sonrisa se dibuja en sus labios."

                            $ nteye = "front05"
                            show n_closefromup_mouth happy_Silentx03
                            show n_closefromup_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                    "...":
                        call p_Help

                        if gensex_ILoveYouNeus:
                            $pl.ch_pts("np", -5)

                            $ nteye = "right05"
                            show n_closefromup_mouth sad_Silentx06
                            show n_closefromup_eyebrows sadx05
                            call n_closefromup_tears_tears
                            with dissolve

                        else:
                            $pl.ch_pts("np", -1)

                            $ nteye = "right05"
                            show n_closefromup_mouth sad_Silentx03
                            show n_closefromup_eyebrows sadx01
                            call n_closefromup_tears_tears
                            with dissolve

                        ne "..."

            "..." if day06_neusAlone_neusWrong_silence_cond == False:

                $ day06_neusAlone_neusWrong_silence_cond = True

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows serious
                call n_closefromup_tears_tears
                with dissolve

                ne "Por favor,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "resp??ndeme."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                jump day06_neusAlone_neusWrong_question


    jump day06_neusAlone_01

label day06_neusAlone_whereAreWe:

    call day06_neusDidac_whereWeAre

    jump day06_neusAlone_01

###########

label day06_neusAlone_02:

    if day06_neusDidac_whereWeAre_trust_Cond == "trust":

        pause 0.2

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        scene morning04_bg bedroom_neus_a
        show kiss_ f_n_07:
            truecenter
            xzoom -1.0
            zoom 1.5 rotate -30
        with fade_short

        n "Vuelves a sentir el c??lido tacto de sus labios,"

        show kiss_ f_n_10
        with Dissolve(0.5)

        n "pero esta vez, acariciando tu lengua con la suya,"

        show kiss_ f_n_12
        with Dissolve(0.5)

        n "ofreci??ndote un beso algo m??s apasionado."

        show kiss_ f_n_09
        with Dissolve(0.5)

        pause 0.2

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx01
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with fade

        if gensex_ILoveYouNeus:

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "Te amo tanto."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

        elif gensex_YoureAMonster:

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve
            
            ne "A pesar de lo que pienses de mi,"

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "me alegro de poder estar a tu lado."

            $ nteye = "front08"
            show n_closefromup_mouth happy_Silentx03
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve
            

        else:

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve
            
            ne "No sabes cuantas noches he so??ado con este momento."

            $ nteye = "down05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve
            

    else:

        # $ Pedrera_char_Cond = "NeusSuperClose"
        # call Pedrera_char_lab

        # show n_closefromup_body naked

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve
        
        ne "A pesar de que desconf??es de mi,"

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "me alegra poder estar a tu lado."

        $ nteye = "down04"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        n "Dirige sus ojos a tu erecta entrepierna mientras se muerde los labios."

    menu:

        pt "Se nota que est?? bastante caliente..."

        "Yo tambi??n te amo, [neusname]." if gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", 4)

            $ nblush += 1

            $ nteye = "front03"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nblush += 1

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx07
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmm... *risilla inocente*"

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

        "Yo tambi??n me alegro de estar contigo." if not gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np", 1)

            $ nblush += 1

            $ nteye = "front06"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

        "Me hubiera gustado conocerte en otras circunstancias.":
            call p_Help
            #$pl.ch_pts("np", -1)

            $ nteye = "front02"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Cr??eme,"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "a mi tambi??n me hubiera gustado."

            $ nteye = "down04"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

        "Desear??a que todas las ma??anas del resto de mi vida fueran despert??ndome a tu lado." if not gensex_YoureAMonster:
            call p_Help
            if gensex_ILoveYouNeus:
                $pl.ch_pts("np", 4)
            else:
                $pl.ch_pts("np", 2)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx01
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if gensex_ILoveYouNeus:

                $ nteye = "front07"
                show n_closefromup_mouth happy_Talkingx03
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Que cursi eres cuando quieres..."

                $ nteye = "down05"
                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            else:

                $ nteye = "front02"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Cuidado con lo que dices [protname],"

                $ nteye = "front06"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "o al final pensar?? que te est??s enamorando de mi."

                $ nteye = "down04"
                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

        "...":

            $ nteye = "down04"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            call p_Help

    pause 0.2

    $ ntlong = 0
    $ mc_stat = "_cuffed"

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = ""
    $ mc_cuff_right = True

    scene d06_cuffHand_mc_hand_comp:
        subpixel True
        truecenter
        zoom 1.2 xpos -0.0 ypos -0.2 # Beginning?
        ease 5.0 zoom 1.0 xpos 0.9 ypos 0.6 # Center Hand
    with fade

    n "Observas que te coge de la mu??eca,"

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "morgana_rides"

    $ mc_cuff_cuffed = "open"
    show d06_cuffHand_mc_hand_comp:
        ease 10.0 zoom 0.5 xpos 0.5 ypos 0.5 # Complete
    with Dissolve(0.5)

    n "y estir??ndote de ella te lo extiende hasta el extremo superior de la cama"

    n "d??nde percibes un objeto fr??o y met??lico."

    p "??Qu??...?"

    $ mc_cuff_cuffed = "closed"
    show d06_cuffHand_mc_hand_comp
    with Dissolve(0.5)

    ono "clic" # 1rst Click

    p "??Me est??s esposando en la cama?"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade

    ne "No te lo tomes a mal,"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "es por seguridad."

    $ nteye = "front05"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "????Por seguridad?!"

        "????Pero por qu???!":
            call p_Help

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "No lo har??a si no fuera necesario."

        "No te har?? ning??n da??o.":
            call p_Help
            $pl.ch_pts("np", 1)

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Eso ya lo s??."

        "??No podemos pasar una noche tranquila?":
            call p_Help
            $pl.ch_pts("np", 1)

            $ nteye = "right03"
            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Lamentablemente no."

        "??Por qu?? no me sorprende?" if not gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", -3)

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "??Por qu?? eres as?? conmigo?"

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            p "??A??n me lo preguntas?"

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front06"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo hago por el bien de los dos."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    p "??A qu?? te refieres?"

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Necesito volver alimentarme de ti"

    if p_ao_started:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

    ne "y es muy importante que esta noche no tenga ni un solo orgasmo."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo m??s probable es que mis hermanas ya est??n empezando el {a=https://es.wikipedia.org/wiki/Aquelarre}aquelarre{/a}."

    $ nteye = "right02"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Si Padre me descubre esta noche,"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "en un momento de debilidad,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "aunque estuvi??ramos en una cueva,"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx08
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "en el otro rinc??n del mundo,"

    $ nteye = "front00"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "ser??a capaz de poseer mi cuerpo"

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "y ya no habr??a nada que pudi??ramos hacer para detenerlo."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    $ day06_neusAlone_02_anotherChance_cond = False

    menu:

        pt "En un momento de debilidad..."

        "??No me crees capaz de resistir la tentaci??n?":
            call p_Help

            $ day06_neusAlone_02_anotherChance_cond = True

            if p_ao_started or p_neus.cumReceived in ["stomach", "buttocks"]:

                if p_ao_started:
                    $pl.ch_pts("np", -5)

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows surprisex05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Como ayer,"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx006
                    show n_closefromup_eyebrows suspiciousx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??verdad?"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Desde luego..."

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx08
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Para fiarme de ti."

                    $ nteye = "left05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                elif p_neus.cumReceived in ["stomach", "buttocks"]:
                    $pl.ch_pts("np", -3)

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows surprisex04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Del mismo modo que te ped?? que te corrieras dentro de mi"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx008
                    show n_closefromup_eyebrows angryx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "y no me hiciste ni el menor caso,"

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx10
                    show n_closefromup_eyebrows angryx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??verdad?"

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows angryx05
                    call n_closefromup_tears_tears
                    with dissolve

            elif pl.np > 200:

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Es posible..."

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero a??n as??..."

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx02
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Es demasiado arriesgado."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                if gensex_ILoveYouNeus:

                    ne "Cari??o,"

                    extend " por favor,"

                else:

                    ne "Por favor,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "cr??eme."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            elif gensex_YoureAMonster:
                $pl.ch_pts("np", -2)

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Perdona que no te tenga demasiada confianza,"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows angryx04
                call n_closefromup_tears_tears
                with dissolve

                ne "pero cuando me llaman monstruo tan abiertamente,"

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows angryx05
                call n_closefromup_tears_tears
                with dissolve

                ne "suelo tener mis dudas."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                jump day06_neusAlone_secondHand

            else:

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Es posible,"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "pero a??n as?? es demasiado arriesgado."

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "por favor,"

                if gensex_ILoveYouNeus:
                    extend " cari??o,"
                else:
                    extend " [protname]"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "conf??a en mi."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

            jump day06_neusAlone_02_anotherChance

        "??Por qu?? intentas justificarte? Siempre terminas haciendo lo que te da la gana." if not gensex_ILoveYouNeus:
            call p_Help

            $pl.ch_pts("np", -5)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Piensa lo que quieras."

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            p "Por suerte es lo ??nico que me permites hacer."

            $ nteye = "right04"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_secondHand

        "Conf??o en ti." if not gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np", 2)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            if gensex_ILoveYouNeus:
                ne "Gracias cari??o."
            else:
                ne "Gracias [protname]."

            $ nteye = "front06"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_secondHand

        "...":
            call p_Help
            jump day06_neusAlone_secondHand


label day06_neusAlone_02_anotherChance:

    menu:

        pt "Quiz??s no sea buena idea insistir..."

        "Pero esta vez, te prometo que te obedecer??.":
            call p_Help

            if p_ao_started or p_neus.cumReceived in ["stomach", "buttocks"]:
                $pl.ch_pts("np", -1)

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Como te he dicho,"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows angryx04
                call n_closefromup_tears_tears
                with dissolve

                ne "despu??s de lo de ayer,"

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows angryx04
                call n_closefromup_tears_tears
                with dissolve

                ne "no me puedo fiar de ti."

                $ nteye = "right05"
                show n_closefromup_mouth sad_Silentx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

            elif pl.np > 230:

                jump day06_neusAlone_uncuff

                    #$ renpy.notify("[p_pos] 230[hn]")
                    #ne "..."
                    #ne "??Est??s seguro?"
                    #aj "Aqu?? te quitar?? las esposas, pero no est?? terminado."

            else:

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Lo siento,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "pero como ya te he dicho,"

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "es demasiado arriesgado."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

            $ renpy.notify("[p_diff]")

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "por favor,"

            extend " enti??ndelo."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "No solo nos ponemos los dos en peligro,"

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "tambi??n lo estar??an D??dac y Meritxell."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Es demasiado arriesgado."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_secondHand

        "...":
            call p_Help

            jump day06_neusAlone_secondHand


label day06_neusAlone_secondHand:

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = ""
    $ mc_cuff_right = False

    scene d06_cuffHand_mc_hand_comp:
        subpixel True
        truecenter
        xzoom -1.0
        zoom 1.2 xpos 1.0 ypos -0.2 #Beginning?
        ease 5.0 zoom 1.0 xpos 0.1 ypos 0.6 # Center Hand
    with fade

    n "Sientes que te coge la otra mu??eca."

    $ mc_cuff_cuffed = "open"
    show d06_cuffHand_mc_hand_comp:
        ease 10.0 zoom 0.5 xpos 0.5 ypos 0.5 # Complete
    with Dissolve(0.5)

    menu:

        pt "??Y va a follarme estando esposado?"

        "<Apartar bruscamente la mano>":
            call p_Help

            $pl.ch_pts("np", -3)

            $ mc_cuff_handTensed = True
            show d06_cuffHand_mc_hand_comp:
                easein_bounce 1.0 zoom 0.53 xpos 0.5 ypos 0.5 # Complete
            with hpunch
            with hpunch
            ne "??Oye!"

            p "Te he dicho que no quiero que me esposes."

            $ nleye = "full"

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_body naked

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            show white:
                additive 1.0
                alpha 1.0
                easein_quad 2.0 alpha 0.0
            with vpunch

            n "Ves sus ojos brillar de nuevo."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx06
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            p "??Ugh...!"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "??Por qu?? me obligas a recurrir a esto?"

            $ nleye = "horny"

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Por favor,"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "enti??ndelo..."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ mc_cuff_handTensed = False
            $ mc_cuff_cuffed = "open"
            #$ mc_cuff_right = False

            scene d06_cuffHand_mc_hand_comp:
                subpixel True
                truecenter
                xzoom -1.0
                zoom 1.0 xpos 0.1 ypos 0.6 # Center Hand
                ease 5.0 zoom 0.5 xpos 0.5 ypos 0.5 # Center Hand
            with fade

            n "Vuelves a sentir su mano en tu mu??eca,"

            n "sin que seas capaz de hacer nada para evitarlo."

            jump day06_neusAlone_secondClick

        "<No hacer nada>":
            call p_Help
            
            jump day06_neusAlone_secondClick

label day06_neusAlone_secondClick:

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = "closed"
    $ mc_cuff_right = False

    show d06_cuffHand_mc_hand_comp:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    with Dissolve(0.5)

    ono "clic" # 2th click

####

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = ""
    $ mc_cuff_right = True

    scene d06_cuffHand_mc_leg_comp:
        subpixel True
        truecenter
        zoom 1.2 xpos 1.2 ypos 1.2 # TopLeft
        ease 5.0 zoom 1.0 xpos 0.4 ypos 0.45 # Foot
        #zoom 0.5 xpos 0.5 ypos 0.5 # Complete
    with fade_long1s

    n "Se aparta de ti y se dirige hasta uno de tus pies."

    $ mc_cuff_handTensed = True
    $ mc_cuff_cuffed = "open"
    show d06_cuffHand_mc_leg_comp:
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5 # Complete
    with Dissolve(1.0)

    p "????Tambi??n me vas a inmovilizar los pies?!"

    ne "Hoy s??."

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = "closed"
    show d06_cuffHand_mc_leg_comp:
        easein_quad 1.0 zoom 0.52 xpos 0.5 ypos 0.5 # Complete
    with Dissolve(1.0)

    ono "clic" # 3th click

    if gensex_ILoveYouNeus:
        ne "Sabes que te amo,"

    elif gensex_YoureAMonster:

        ne "En el fondo sabes que me fiar??a de ti,"

    else:

        ne "Sabes que me f??o de ti,"

    extend " [protname]."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade

    ne "Pero incluso sin que hagas nada que pueda hacerme da??o,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "esta noche necesito que sea de este modo."

    if day06_neusAlone_02_anotherChance_cond:

        if gensex_YoureAMonster:

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            p "Lo dices como si no te fiaras ni de ti misma."

            $ nteye = "front04"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            p "??Y puedo saber quien me proteger?? de ti?"

            $ nteye = "front04"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        else:

            $ nteye = "front08"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            p "Te he dicho que no te har?? nada."

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx04
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Aunque te creyera,"

            $ nteye = "right04"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "el problema es que tampoco conf??o en mi misma."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            p "..."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

        ne "Por favor,"

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "conf??a en mi."

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Al menos hoy."

        if gensex_YoureAMonster:

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            p "Confiar en alguien que no conf??a ni en si misma,"

            $ nteye = "front04"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            p "todo muy l??gico."

            $ nteye = "right04"
            show n_closefromup_mouth sad_Silentx05
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

        else:

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            pt "??Debo fiarme de alguien que no conf??a ni en si misma?"

            $ nteye = "down05"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve


    else:

        $ nteye = "down05"
        show n_closefromup_mouth sad_Silentx03
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve



#####

    pause 0.2

    $ mc_cuff_handTensed = True
    $ mc_cuff_cuffed = "open"
    $ mc_cuff_right = False

    scene d06_cuffHand_mc_leg_comp:
        subpixel True
        truecenter
        xzoom -1.0
        zoom 1.2 xpos -0.2 ypos 1.2 # TopLeft
        ease 5.0 zoom 1.0 xpos 0.6 ypos 0.45 # Foot
    with fade_long1s

    pause 5.0

    # $ mc_cuff_handTensed = True
    # $ mc_cuff_cuffed = "open"

    # show d06_cuffHand_mc_leg_comp
    # with Dissolve(1.0)

    # pause 0.2

    $ mc_cuff_handTensed = False
    $ mc_cuff_cuffed = "closed"

    show d06_cuffHand_mc_leg_comp:
        easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
    with Dissolve(1.0)

    ono "clic" # 4th click  Second leg.


    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "loopster"

    $ p_ao_action_Cond = "legs"

    scene p_ao_ground_comp:
        zoom 2.0 xpos -1.65 ypos -1.3 # Legs Camera
    with fade

    n "Sientes su respiraci??n ascendiendo por tus piernas."

    $ p_ao_action_Cond = "crotch"

    show p_ao_ground_comp:
        zoom 2.0 xpos -0.5 ypos -1.3
    with Dissolve(0.5)

    ne "Me encanta cuando est?? as?? de dura."

    $ p_ao_action_Cond = "sigh"

    show p_ao_ground_comp:
        subpixel True
        zoom 2.0 xpos -0.5 ypos -1.5
        ease 10.0 xpos -0.5 ypos -1.2
    with Dissolve(0.5)

    ne "Aunque sigue estando bastante rojiza."

    if p_prot_NotJustMasturbate_with_p_neus:

        p "No s?? de quien es la culpa..."

        #$ nleye = "horny"

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        if p_ao_started:

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            ne "??Eso digo yo!"

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx09
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            ne "??Te dije que no era buena idea que me llevaras al orgasmo,"

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx10
            show n_closefromup_eyebrows angryx05
            call n_closefromup_tears_tears
            with dissolve

            ne "y a??n as?? no me hiciste ni pu??etero caso!"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx07
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            pt "Desde luego,"

            $ nteye = "down05"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows normal
            call n_closefromup_tears_tears
            with dissolve

            pt "no bromeaba..."

        else:

            if p_neus.vaginal_received < 3 or p_neus.anal_received < 3 or p_neus.blowjob_done:

                if p_neus.vaginal_received < 3 and p_neus.anal_received < 3 and p_neus.blowjob_done:

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No s?? de que me hablas..."

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    if p_neus.vaginal_received < 3:

                        ne "Si pr??cticamente no llegu?? ni a sentirla dentro de mi..."

                    elif p_neus.anal_received < 3:

                        ne "Si apenas me la llegaste a meter por detr??s..."

                    elif p_neus.blowjob_done < 3:

                        ne "Si pr??cticamente no me diste ni la oportunidad de saborearla..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Silentx06
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Silentx02
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Hmmm..."

                    $ nteye = "right02"
                    show n_closefromup_mouth sad_Talkingx004
                    show n_closefromup_eyebrows surprisex03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Es posible,"

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "pero..."

                    if p_neus.vaginal_received < 3:

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx003
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "apenas la sent?? dentro de mi..."

                    elif p_neus.anal_received < 3:

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx004
                        show n_closefromup_eyebrows suspiciousx02
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "apenas la sent?? por detr??s..."

                    elif p_neus.blowjob_done < 3:

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "pr??cticamente no me diste ni la oportunidad de saborearla..."

                if p_neus.vaginalDeep_received > 1 or p_neus.analDeep_received > 1:

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows suspiciousx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No obstante,"

                    if p_neus.vaginalDeep_received > 1:

                        $ nteye = "front03"
                        show n_closefromup_mouth happy_Talkingx05
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "me alegro de que te gustara tanto tenerla dentro de mi."

                    elif p_neus.analDeep_received > 1:

                        $ nteye = "front04"
                        show n_closefromup_mouth happy_Talkingx04
                        show n_closefromup_eyebrows suspiciousx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "me alegro de que te gustara tanto mi trasero."

                if p_neus_orgasmHurry:

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows suspiciousx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Aunque es verdad que casi logras que tenga un orgasmo..."

                $ nteye = "down05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

            else:

                if p_neus_orgasmHurry:

                    $ nteye = "front02"
                    show n_closefromup_mouth happy_Talkingx06
                    show n_closefromup_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Oye..."

                    $ nteye = "front08"
                    show n_closefromup_mouth happy_Talkingx005
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Tampoco me lo pusiste nada f??cil,"

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows normal
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??sabes?"

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

            if p_neus_orgasmHurry:

                pause 0.2

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                p "??No creo que hubiera sido tan horrible si realmente hubieras tenido un orgasmo."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx04
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx07
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

        ne "..."

        jump day06_neusAlone_startLicking

    else:

        $pl.ch_pts("np", -1)

        p "Un poco..."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        p "??Qu?? pasa?"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Me entristece que no me hayas dado la oportunidad de poder complacerte..."

        $ nteye = "down05"
        show n_closefromup_mouth sad_Silentx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        jump day06_neusAlone_startLicking

###

label day06_neusAlone_startLicking:

    # Lick Dick -Blowjob, but tongue.
    pause 0.2

    scene day06
    with fade

    ##
    # $ p_ao_n_vel = 1

    # $ ped_sex_general_expression_Cond = "closed"
    # $ ped_sex_general_expressionJaw_Cond = "blow_below_04"

    # show pedrera_sex_neus_oral softLicking:
    #     ypos 0.55 # Up
    #     block:
    #         ease 10.0/p_ao_n_vel ypos 0.45 # Down
    #         ease 10.0/p_ao_n_vel ypos 0.55 # Up
    #         repeat
    # with Dissolve(1.0)

    ##

    p "Ughh..."

    n "Sientes su c??lida lengua acariciando tu erecto pero sensible miembro."

    $ p_prot.pos = "oral"
    $ p_prot.action = "rest"
    $ p_neus.action = "rest"
    #$ ped_sex_general_zoom_Cond = "faceCentered"
    $ ped_sex_general_zoom_Cond = ""

    call p_neus_boobjob_stop_label

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with Dissolve(0.5)

    ne "Me encanta su sabor..."

    $ nteye = "down04"
    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    menu:

        pt "??Su sabor?"

        "??Es que sabe distinta a cualquier otra polla?":

                $ nteye = "front01"
                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_n_frontHead_exp_eyebrows surprisex01
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front08"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
                show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "Aunque te cueste de creerlo,"

                extend " s??."

                $ nteye = "front05"
                show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_n_frontHead_exp_eyebrows normal
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "??Acaso todos los co??os saben igual?"

                $ nteye = "front03"
                show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                p "..."

                $ nteye = "front04"
                show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_n_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                pt "M??s o menos..."

                $ nteye = "front08"
                show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx03
                show gensex_oral_n_frontHead_exp_eyebrows sadx01
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                pt "Si est??n limpios..."

                $ nteye = "down04"
                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx04
                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "Pero adem??s,"

                $ nteye = "down05"
                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "la tuya tiene algo que..."

                $ nteye = "front06"
                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx07
                show gensex_oral_n_frontHead_exp_eyebrows sadx03
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "No es solo el gusto y el tacto,"

                $ nteye = "down03"
                show gensex_oral_n_frontHead_exp_mouth happy_Talkingx06
                show gensex_oral_n_frontHead_exp_eyebrows sadx04
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "es algo m??s."

                $ nteye = "down05"
                show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx06
                show gensex_oral_n_frontHead_exp_eyebrows sadx07
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                menu:

                    pt "Algo m??s..."

                    "Quiz??s, el hecho de que sea tu hermano sea la causa.":
                        call p_Help

                        $pl.ch_pts("np", 2)

                        $ nteye = "front01"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                        show gensex_oral_n_frontHead_exp_eyebrows surprisex03
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        p "Al fin y al cabo,"

                        $ nteye = "front02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx02
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        p "por lo visto formamos parte de una familia de brujas y bichos raros..."

                        $ nteye = "right02"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
                        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sad_Silentx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        p "No s??,"

                        extend " digo yo..."

                        $ nteye = "front05"
                        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
                        show gensex_oral_n_frontHead_exp_eyebrows sadx07
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        ne "Es mejor que no hablemos de eso."

                        $ nteye = "right04"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_n_frontHead_exp_eyebrows sadx08
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        pt "S??..."

                        $ nteye = "front08"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
                        show gensex_oral_n_frontHead_exp_eyebrows sadx05
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        pt "quiz??s sea mejor..."

                        $ nteye = "down05"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx07
                        show gensex_oral_n_frontHead_exp_eyebrows sadx03
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        jump day06_neusAlone_continueLicking

                    "...":
                        call p_Help

                        $ nteye = "down04"
                        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                        show gensex_oral_n_frontHead_exp_eyebrows sadx06
                        call gensex_oral_n_frontHead_exp_tears_tears
                        with dissolve

                        jump day06_neusAlone_continueLicking

        "Me alegra de que te guste." if not gensex_YoureAMonster:
            call p_Help

            $pl.ch_pts("np", 1)

            $ nteye = "front04"
            show gensex_oral_n_frontHead_exp_mouth happy_Talkingx06
            show gensex_oral_n_frontHead_exp_eyebrows sadx04
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "No te haces una idea..."

            $ nteye = "down05"
            show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx07
            show gensex_oral_n_frontHead_exp_eyebrows sadx07
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            jump day06_neusAlone_continueLicking

        "...":
            call p_Help

            $ nteye = "down05"
            show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx07
            show gensex_oral_n_frontHead_exp_eyebrows sadx07
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            jump day06_neusAlone_continueLicking

label day06_neusAlone_continueLicking:

    pause 0.2

    scene day06
    with fade

    n "Su lengua sigue recorriendo tu miembro hasta alcanzar tu glande d??nde le dedica m??s tiempo y cari??o."

    p "Ugh..."

    $ p_prot.pos = "oral"
    $ p_prot.action = "rest"
    $ p_neus.action = "rest"

    call p_neus_boobjob_stop_label

    $ nteye = "front01"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with Dissolve(0.5)

    ne "??Te duele?"

    if gensex_YoureAMonster:

        $ nteye = "front05"
        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx06
        show gensex_oral_n_frontHead_exp_eyebrows sadx04
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "??A ti que te parece?"

        $ nteye = "right05"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
        show gensex_oral_n_frontHead_exp_eyebrows sadx06
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve


    else:

        $ nteye = "front03"
        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
        show gensex_oral_n_frontHead_exp_eyebrows sadx02
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "Solo un poco,"

        $ nteye = "front05"
        show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx05
        show gensex_oral_n_frontHead_exp_eyebrows sadx03
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "realmente la tengo muy sensible."

        $ nteye = "front08"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
        show gensex_oral_n_frontHead_exp_eyebrows sadx04
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    ne "Lo lamento..."

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx02
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "??Quieres que pare?"

    $ nteye = "front05"
    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    menu:

        pt "??Es una pregunta ret??rica?"

        "??Quieres parar?" if not gensex_YoureAMonster:
            call p_Help

            $pl.ch_pts("np", 1)

            $ nteye = "front05"
            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
            show gensex_oral_n_frontHead_exp_eyebrows sadx07
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "No..."

            $ nteye = "front03"
            show gensex_oral_n_frontHead_exp_mouth happy_Silentx02
            show gensex_oral_n_frontHead_exp_eyebrows serious
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            p "Entonces sigue."

            $ nteye = "front04"
            show gensex_oral_n_frontHead_exp_mouth happy_Talkingx04
            show gensex_oral_n_frontHead_exp_eyebrows sadx04
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "Gracias."

            $ nteye = "down05"
            show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx06
            show gensex_oral_n_frontHead_exp_eyebrows sadx05
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            jump day06_neusAlone_startDeepthroat

        "??Acaso tengo elecci??n?":
            call p_Help

            $pl.ch_pts("np", -2)

            $ nteye = "front02"
            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx15
            show gensex_oral_n_frontHead_exp_eyebrows angryx03
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "??Por supuesto que tienes elecci??n!"

            $ nteye = "right01"
            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx007
            show gensex_oral_n_frontHead_exp_eyebrows angryx02
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "Es verdad que necesito alimentarme de ti,"

            $ nteye = "right03"
            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
            show gensex_oral_n_frontHead_exp_eyebrows sadx03
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "pero me gustar??a que fuera con tu consentimiento."

            $ nteye = "right04"
            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
            show gensex_oral_n_frontHead_exp_eyebrows sadx05
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            menu:

                pt "Con mi consentimiento..."

                "Entonces preferir??a que parases.":
                    call p_Help
                    $pl.ch_pts("np", -5)

                    $ nteye = "front00"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
                    show gensex_oral_n_frontHead_exp_eyebrows surprisex002
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right04"
                    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    ne "Co-"

                    extend "como quieras..."

                    $ nteye = "right05"
                    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx04
                    show gensex_oral_n_frontHead_exp_eyebrows sadx07
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    jump day06_neusAlone_noBlowjobWanted

                "Puedes seguir.":
                    call p_Help
                    $pl.ch_pts("np", 2)

                    $ nteye = "front02"
                    show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                    show gensex_oral_n_frontHead_exp_eyebrows serious
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    pause 0.2

                    $ nteye = "front04"
                    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx02
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    ne "Gracias..."

                    $ nteye = "down05"
                    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx05
                    show gensex_oral_n_frontHead_exp_eyebrows sadx03
                    call gensex_oral_n_frontHead_exp_tears_tears
                    with dissolve

                    jump day06_neusAlone_startDeepthroat

        "...":
            call p_Help

            $ nteye = "front04"
            show gensex_oral_n_frontHead_exp_mouth sad_Silentx04
            show gensex_oral_n_frontHead_exp_eyebrows suspiciousx01
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front08"
            show gensex_oral_n_frontHead_exp_mouth sad_Talkingx003
            show gensex_oral_n_frontHead_exp_eyebrows normal
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            ne "Me tomar?? eso como un no..."

            $ nteye = "down05"
            show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
            show gensex_oral_n_frontHead_exp_eyebrows sadx02
            call gensex_oral_n_frontHead_exp_tears_tears
            with dissolve

            jump day06_neusAlone_startDeepthroat

label day06_neusAlone_startDeepthroat:

    pause 0.2

    scene day06
    with fade

    $ day06_neusAlone_sex = "vaginal"

    n "Ves c??mo engulle tu miembro sin dificultad"

    n "sintiendo el h??medo y c??lido interior de su boca."

    n "Usando su lengua de modo juguet??n,"

    n "relame la parte inferior del glande mientras sus labios te succionan."

    n "Sin prisas, sigue hundiendo su rostro, hasta alcanzar la mitad de tu miembro."

    p "[neusname]..."

    n "Finalmente, logra sumergirse hasta tener todo tu miembro atrapado en su garganta,"

    n "sintiendo sus labios y su respiraci??n a flor de piel con tu ombligo."

    pt "??Joder!"

    n "Sientes que tu polla empieza a palpitar violentamente."

    $ p_prot.pos = "oral"
    $ p_prot.action = "rest"
    $ p_neus.action = "rest"

    call p_neus_boobjob_stop_label

    $ nteye = "down00"
    show gensex_oral_n_frontHead_exp_mouth sad_Silentx05
    show gensex_oral_n_frontHead_exp_eyebrows surprisex002
    call gensex_oral_n_frontHead_exp_tears_tears
    with vpunch
    with vpunch

    n "Con celeridad, se aparta de tu polla."

    $ nteye = "down01"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx008
    show gensex_oral_n_frontHead_exp_eyebrows angryx01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "??No!"

    $ nteye = "front02"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx004
    show gensex_oral_n_frontHead_exp_eyebrows sadx05
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "No..."

    $ nteye = "front03"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx03
    show gensex_oral_n_frontHead_exp_eyebrows sadx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "No te corras a??n..."

    $ nteye = "front02"
    show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
    show gensex_oral_n_frontHead_exp_eyebrows normal
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "Si sigues haci??ndome esta mamada,"

    $ nteye = "down03"
    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "no creo que pueda aguantar mucho m??s..."

    $ nteye = "front05"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "S?? que tienes poco aguante."

    $ nteye = "front01"
    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx02
    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "??Puedo saber cu??nto hac??a que me estabas cabalgando antes de despertarme?"

    $ nteye = "right01"
    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx06
    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "..."

    $ nteye = "front07"
    show gensex_oral_n_frontHead_exp_mouth happy_Silentx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pause 0.2

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx03
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    if gensex_ILoveYouNeus:

        ne "Quiero sentirte dentro de mi."

    else:

        ne "Quiero sentirla dentro de mi."

    $ nteye = "front05"
    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx06
    show gensex_oral_n_frontHead_exp_eyebrows sadx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pt "Y no me responde..."

    $ nteye = "front08"
    show gensex_oral_n_frontHead_exp_mouth happy_Silentx03
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Se pone de pie sobre la cama posando sus pies cerca de tus caderas."

    $ day06_neusAlone_notEvenBecause_cond = "tongue"

    if p_neus.vaginal_received > 1 or p_neus.anal_received > 1:

        ne "Me gustar??a volver a sentirla dentro de mi..."

    else:

        ne "Me gustar??a poderla sentir dentro de mi..."

        if p_neus.blowjob_done > 1:

            ne "no solo en mi boca."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked
    #show n_closefromup_body naked_FULL

    if p_neus.cumReceived in ["stomach", "buttocks"]:

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with fade

        ne "Y esta vez,"

        ne "si no es mucho pedir,"

        ne "que puedas terminar dentro de mi."

    elif p_neus.cumReceived in ["vaginal", "anal"]:

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with fade

        ne "Volver a sentir tu esperma..."

    else:

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with fade

    if p_neus.cumReceived in ["vaginal", "anal"]:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero si lo prefieres,"

        if p_neus.cumReceived == "anal":

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "hoy podr??as probar de terminar por delante."

            if p_neus.vaginal_dilatation < 3:

                $ nteye = "front06"
                show n_closefromup_mouth happy_Talkingx03
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Ayer no es que me dieras demasiado cari??o en esta parte..."

            # if gensex_YoureAMonster:
                ## Not necessary
            #     p "Para que te deje pre??ada como la zorra que eres,"
            #     extend " ??verdad?"
            #     ne "..."
            #     p "??Te crees que soy imb??cil?"
            #     ne "Nunca he dicho tal cosa."
            #     p "Ya..."

        if p_neus.cumReceived == "vaginal":

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx02
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "hoy podemos probar por detr??s."

            if p_neus.anal_dilatation < 3:

                $ nteye = "front06"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Aunque no entrar?? f??cilmente,"

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "ayer apenas le prestaste demasiada atenci??n..."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx04
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "Creo que est?? claro lo que prefiere..."

        "??Y no podr??as volver a usar lo que te hiciste crecer en la entrepierna?..." if p_prot_aoNight_analReceived == "True":

            jump day06_neusAlone_pasSex

        "Lo que quieres es que te deje embarazada, ??Me equivoco?" if p_neus.cumReceived != "vaginal":
            call p_Help

            $pl.ch_pts("np",-1)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "????Qu???!"

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx009
            show n_closefromup_eyebrows angryx06
            call n_closefromup_tears_tears
            with dissolve

            ne "??No!"

            $ nteye = "right01"
            show n_closefromup_mouth sad_Talkingx006
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            ne "No..."

            $ nteye = "right03"
            show n_closefromup_mouth sadbiting_Silentx09
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "right05"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx08
            call n_closefromup_tears_tears
            with dissolve

            ne "Quiz??s..."

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero tampoco es como si te estuviera obligando,"

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "??no crees?"

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "No s?? yo..."

                "No obligas, pero insistes.":
                    call p_Help
                    $pl.ch_pts("np", -1)

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right04"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo siento."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                "Apenas hace tres d??as que nos conocemos.":
                    call p_Help
                    $pl.ch_pts("np", -2)

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows suspiciousx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right01"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    pause 0.2

                    $ nteye = "right04"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo s??..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    p "??Entonces?"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Har??a las cosas m??s f??ciles..."

                    $ nteye = "front04"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    p "??Traer un ni??o al mundo har??a las cosas m??s f??ciles?"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Para ocultarnos mejor de Padre,"

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "s??."

                    $ nteye = "right03"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Al menos hasta que diera a luz..."

                    $ nteye = "right04"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    p "??Y luego?"

                    $ nteye = "front03"
                    show n_closefromup_mouth happy_Talkingx03
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Tendr??amos un precioso hijo."

                    $ nteye = "right05"
                    show n_closefromup_mouth happybiting_Silentx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    pt "O hija..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    if gensex_YoureAMonster:

                        menu:

                            pt "Precioso hijo..."

                            "??Y luego tambi??n lo sacrificar??as?":
                                call p_Help

                                $pl.ch_pts("np", -4)

                                $ nteye = "front00"
                                show n_closefromup_mouth sadbiting_Silentx02
                                show n_closefromup_eyebrows surprisex02
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "????Por quien diablos me tomas?!"

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Silentx08
                                show n_closefromup_eyebrows angryx05
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Responde."

                                $ ntlong += 1

                                $ nteye = "front08"
                                show n_closefromup_mouth sad_Silentx12
                                show n_closefromup_eyebrows angryx07
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Talkingx15
                                show n_closefromup_eyebrows angryx06
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "??Por supuesto que no!"

                                $ ntlong += 1

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Talkingx17
                                show n_closefromup_eyebrows angryx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "??No tienes ni idea de lo que he pasado durante todos estos a??os!"

                                $ nteye = "front04"
                                show n_closefromup_mouth sad_Talkingx14
                                show n_closefromup_eyebrows angryx06
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No te atrevas a juzgarme tan a la ligera."

                                $ ntlong += 1

                                $ nteye = "front05"
                                show n_closefromup_mouth sad_Silentx10
                                show n_closefromup_eyebrows angryx04
                                call n_closefromup_tears_tears
                                with dissolve

                                p "..."

                                $ nteye = "front08"
                                show n_closefromup_mouth sad_Silentx12
                                show n_closefromup_eyebrows angryx06
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.2

                                $ ntlong == 0

                                $ nteye = "right05"
                                show n_closefromup_mouth sad_Silentx08
                                show n_closefromup_eyebrows sadx06
                                call n_closefromup_tears_tears
                                with dissolve
                                

                            "...":
                                call p_Help

                "??De verdad quieres traer a un reci??n nacido al horrible mundo en el que vives?" if not gensex_YoureAMonster:
                    call p_Help

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "El mundo siempre ha sido as??,"

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "solo que lo desconoc??as."

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "[neusname]..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Las oscuras criaturas de ojos rojos,"

                    $ nteye = "left02"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "no atacan,"

                    extend " y apenas se acercan,"

                    $ nteye = "left01"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "a las mujeres embarazadas."

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Podr??amos ocultarnos mejor de Padre y mis hermanas."

                    $ nteye = "right01"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Quiz??s,"

                    extend " incluso ser??amos capaces de vivir tranquilos y felices."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx02
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "??Y una vez dieras a luz?"

                    $ nteye = "front00"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Con nueve meses tendremos tiempo para encontrar otra soluci??n a largo plazo,"

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx08
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "te lo prometo."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Pero tiene que ser tu elecci??n."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                "??Eres capaz de traer a un pobre inocente al mundo con tal de poder salvarte t?? misma, aunque sea tu propio hijo?" if gensex_YoureAMonster:
                    $pl.ch_pts("np", -4)

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??De verdad crees eso de mi?"

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Es lo que me est??s demostrando."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Silentx08
                    show n_closefromup_eyebrows sadx09
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right01"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lamento que pienses as??."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_eyebrows sadx08
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_analSex

            menu day06_neusAlone_sexChoice_question:

                pt "??Por d??nde?"

                "<Por delante>":
                    call p_Help

                    $ nteye = "front05"
                    show n_closefromup_mouth happy_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    n "Una ligera sonrisa se dibuja en sus labios."

                    $ nteye = "down05"
                    show n_closefromup_mouth happybiting_Silentx07
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_vaginalSex

                "<Por detr??s>":
                    call p_Help

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx001
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    n "Exhala un ligero suspiro de sus labios."

                    $ nteye = "down05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_analSex

        "Esta vez, preferir??a poderla sentir dentro de tu otro agujero." if p_neus.vaginal_received > 2 and p_neus.anal_received < 2:

            $ nteye = "front03"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Si no me diste cari??o por esa parte ayer,"

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "es por que no quisiste."

            $ nteye = "front04"
            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero si es lo que quieres..."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx03
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_analSex

        "Preferir??a volverla a sentir dentro de tu trasero."if p_neus.anal_received >= 2:

            $ nteye = "front02"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "right02"
            show n_closefromup_mouth sad_Talkingx005
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "Si te dijera que me disgust??,"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "te estar??a mintiendo..."

            if p_neus.analDeep_received > 1:

                $ nteye = "front03"
                show n_closefromup_mouth happy_Talkingx06
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Especialmente cuando fui capaz de retenerla entera dentro..."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_analSex

        "Esta vez, me gustar??a poder terminar en tu trasero." if p_neus.cumReceived != "anal":

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            if p_neus.cumReceived in ["stomach", "buttocks"]:

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Si por lo menos ayer,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows serious
                call n_closefromup_tears_tears
                with dissolve

                if p_neus.cumReceived == "stomach":

                    ne "no te hubieras corrido sobre mi barriga..."
                else:

                    ne "no te hubieras corrido sobre mis nalgas..."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero bueno,"

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "si es lo que prefieres..."

                $ nteye = "down05"
                show n_closefromup_mouth happybiting_Silentx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

            else:

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Como prefieras."

                $ nteye = "down05"
                show n_closefromup_mouth happybiting_Silentx04
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

            jump day06_neusAlone_analSex

        "Yo tambi??n quiero volver a sentirla dentro de ti, [neusname]." if p_neus.vaginal_received > 1:
            call p_Help

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Gracias..."

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            menu:
                pt "Otra vez d??ndome las gracias..."

                "No me des las gracias por todo, mujer.":
                    call p_Help

                    $ nteye = "front07"
                    show n_closefromup_mouth extra_burlesque
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Gnnnn!"

                    $ nteye = "front04"
                    show n_closefromup_mouth happy_Talkingx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Tonto."

                "...":
                    call p_Help

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx04
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_vaginalSex

        "Yo tambi??n quiero sentirla dentro de tu vagina, [neusname]." if p_neus.vaginal_received < 1:
            call p_Help

            if gensex_ILoveYouNeus:

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "??Y ayer por qu?? no quisiste hacerme el amor por ah???"

            else:

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "??Y ayer por qu?? no quisiste hacerlo por ah???"

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "Por qu?? no quise ayer..."

                "Por que no quer??a dejarte embarazada.":
                    call p_Help

                    $pl.ch_pts("np", -2)

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Y ahora s???"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Silentx02
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "No."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Si est??s a punto de correrte"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "y ahora me la meto dentro,"

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx004
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??no te vas a correr?"

                    $ nteye = "front04"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front02"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows normal
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Es posible."

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Entonces, por d??nde quieres hacerlo?"

                    $ nteye = "sadbiting_Silentx05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_sexChoice_question

                "Porque quer??a que fuera un momento especial y sin prisas.":
                    call p_Help
                    $pl.ch_pts("np", 1)

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx007
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Y es ahora un momento suficientemente especial?"

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Estoy atado..."

                    $ nteye = "down02"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo s??..."

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Talkingx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Pero por favor,"

                    extend " enti??ndelo..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Entonces, por d??nde quieres hacerlo?"

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_sexChoice_question


                "Porque ten??a ganas de probar ese trasero tuyo." if p_neus.anal_received > 5:
                    call p_Help

                    $ day06_neusAlone_notEvenBecause_cond = "anal"

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows suspiciousx01
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_notEvenVaginal

                "Porque me encant?? esa garganta profunda tuya." if p_neus.blowjobDeep_done > 5:
                    call p_Help

                    $ day06_neusAlone_notEvenBecause_cond = "throat"

                    $ nteye = "front03"
                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_notEvenVaginal

                "Porque me encanta la forma en que usas la lengua con mi polla." if p_neus.blowjob_done > 5:
                    call p_Help

                    $ day06_neusAlone_notEvenBecause_cond = "tongue"

                    $ nteye = "front02"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    jump day06_neusAlone_notEvenVaginal

            jump day06_neusAlone_vaginalSex

        "...":
            call p_Help

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx005
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya que no eliges,"

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "lo har?? yo por ti."

            $ nteye = "down05"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_vaginalSex


label day06_neusAlone_notEvenVaginal:

    ne "..."

    if day06_neusAlone_notEvenBecause_cond == "tongue":

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Me alegra saber que te gusta tanto mi lengua..."

    elif day06_neusAlone_notEvenBecause_cond == "throat":

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Me alegra comprobar que mis esfuerzos para tenerla entera en mi garganta no fueron en vano..."

    elif day06_neusAlone_notEvenBecause_cond == "anal":

        if p_neus.analDeep_received > 2:

            $ nteye = "front08"
            show n_closefromup_mouth happy_Talkingx07
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "No pens?? que llegar??a a entrar toda,"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "aunque me alegro de que as?? fuera."

        else:

            $ nteye = "right01"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Me alegra saber que te gust?? tanto mi agujero trasero."

    if day06_neusAlone_notEvenBecause_cond == "anal":

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "pero tambi??n me hubiera gustado sentirte en el otro lado..."

    else:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "pero tambi??n me hubiera gustado sentirte dentro de mi..."

    $ nteye = "front00"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    p "????Acaso no me dijiste que era mejor que no tuvieras ning??n orgasmo?!"

    if p_neus.vaginal_received < 5:

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "??Pero si apenas me la llegaste a meter!"

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

    elif p_neus.vaginal_received < 1:

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx007
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        ne "??Pero es que si ni siquiera llegaste a met??rmela!"

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

    elif p_neus_orgasmHurry == False:

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Tampoco hab??a tanta prisa..."

        $ nteye = "right03"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "right02"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "En eso tienes raz??n..."

        $ nteye = "front07"
        show n_closefromup_mouth extra_burlesque
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        n "La ves haci??ndote una mueca con la lengua."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx06
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

    pause 0.2

    $ nteye = "down04"
    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Realmente est?? rojita..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Silentx04
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    n "jejeje *risilla inocente*"

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    jump day06_neusAlone_vaginalSex

label day06_neusAlone_analSex:

    $ day06_neusAlone_sex = "anal"

    jump day06_neusAlone_sexLabel

label day06_neusAlone_vaginalSex:

    $ day06_neusAlone_sex = "vaginal"

    jump day06_neusAlone_sexLabel

label day06_neusAlone_sexLabel:

    scene day06
    with fade

    n "Sin prisas, desciende su cuerpo,"

    if day06_neusAlone_sex == "vaginal":

        n "hasta que sientes sus labios vaginales acariciando tu rojizo miembro."

    elif day06_neusAlone_sex == "anal":

        n "hasta que sientes la carne de su orificio anal acariciando tu rojizo miembro."

    ne "No te haces una idea de cuan adictiva puede llegar a ser tu polla..."

    if day06_neusAlone_sex == "vaginal":

        ne "Especialmente aqu?? dentro."

    elif day06_neusAlone_sex == "anal":

        ne "Aunque sea por aqu?? detr??s..."

    n "Paulatinamente, se lo va introduciendo en su interior."

    n "Su ardiente carne rodea por completo la punta de tu miembro."

    p "Ugh..."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "down02"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with fade_short

    ne "Lo siento,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "no puedo evitar estar tan caliente."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    $ day06_neusAlone_sexLabel_fast = True

    menu:

        pt "No lo puede evitar dice..."

        "??Vas a seguir disculp??ndote todo el d??a?":
            call p_Help

            $pl.ch_pts("np", 2)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx005
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            ne "Con que esas tenemos..."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows suspiciousx04
            call n_closefromup_tears_tears
            with dissolve

        "Podr??amos ir m??s despacio.":
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "No quiero ir m??s despacio..."

            $ nteye = "down05"
            show n_closefromup_mouth sadbiting_Silentx08
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        "Por favor, ve m??s despacio.":

            $ day06_neusAlone_sexLabel_fast = False

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "Como quieras..."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        "No pasa nada, ve a tu ritmo." if not gensex_YoureAMonster:
            call p_Help

            $pl.ch_pts("np", 1)

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "??Quieres que vaya a mi ritmo?"

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx10
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        "...":

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows suspiciousx04
            call n_closefromup_tears_tears
            with dissolve

            call p_Help

    pause 0.2
    scene day06

    if day06_neusAlone_sexLabel_fast:

        with vpunch
        with vpunch

        p "??Ugh!"

        n "Sus caderas se desplazan a mayor velocidad,"

    else:

        with fade

        n "Desplaza sus caderas hacia abajo,"

    n "logrando engullir m??s de la mitad de tu  miembro en su interior."

    if not day06_neusAlone_sexLabel_fast:

        p "Hmmm..."

        ne "S?? que estoy caliente y tu polla est?? bastante da??ada,"

        ne "pero parece que a??n as?? lo est??s disfrutando."

        p "No puedo negarlo."

        ne "Me alegro."

        ne "Realmente la tienes enorme..."

        n "Cada vez que desciende,"

        ne "HMmmm... *gemido*"

        n "sientes que lo hace a m??s velocidad."

        p "[neusname]..."

    p "Te he dicho que..."

    if not day06_neusAlone_sexLabel_fast:

        ne "Lo lamento,"

        ne "pero es que voy demasiado caliente."

        p "Uhgn..."

    jump day06_neusAlone_orgasm

label day06_neusAlone_orgasm:

    ne "No lo retengas..."

    ne "D??melo todo."

    p "??Ughhh!"

    n "Tu polla palpita con fuerza a pesar de estar ahogada por su ardiente carne"

    if day06_neusAlone_sex == "vaginal":

        n "al mismo tiempo que algo en esa profundidad empieza a lamer la punta de tu miembro."

    elif day06_neusAlone_sex == "anal":

        n "al mismo tiempo que en esa profundidad empiezas a notar una tenue vibraci??n"

    pt "????Qu?? diablos?!"

    n "El cosquilleo particular te recorre por la entrepierna."

    p "No voy a poder..."

    n "Su caderas descienden a??n con m??s energ??a y dureza."

    ne "??C??rrete!"

    n "Sus ojos brillan con intensidad."

    ne "??Hazlo ya!"

    n "Oyes un mont??n de susurros rode??ndote."

    p "??Ughh...!"

    n "Tu miembro explosiona en ese ardiente interior"

    if day06_neusAlone_sex == "vaginal":

        n "mientras esa extra??a lengua recorre tu miembro sin compasi??n."

    elif day06_neusAlone_sex == "anal":

        n "mientras esa extra??a vibraci??n, que ha aumentado de intensidad,"

        n "alcanza tu polla al completo."

    ne "??Dios!"

    n "Sin cesar en su movimiento de caderas,"

    n "desciende su cuerpo y sientes su pecho desnudo sobre tus pectorales."

    if day06_neusAlone_sex == "vaginal":

        n "Mientras el resto de su carne vaginal succiona tu miembro,"

        n "esa extra??a lengua sigue recorriendo y exprimiendo tu miembro"

        n "como si fuera una aspiradora a m??xima potencia."

    elif day06_neusAlone_sex == "anal":

        n "Mientras el resto de su cavidad anal succiona tu miembro,"

        n "esa extra??a vibraci??n sigue recorriendo tu miembro,"

        n "como si quisiera tragarse hasta la ??ltima gota."

    pt "La madre que la..."

    play sound "audio/sfx/meme_surprise02.ogg"
    stop music fadeout 0.5

    n "Repentinamente detiene sus caderas."

    ne "Ughhnnn..."

    p "??Qu??-"

    extend "qu?? pasa?"

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "bittersweet"

    $ ped_neus_whispers_sfx04 = 0.8

    $ nblush += 2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front06"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with fade_short

    ne "He tenido que parar..."

    $ nteye = "down02"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Estaba a punto de..."

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    if gensex_YoureAMonster:

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    else:

        menu:

            pt "Ni siquiera se atreve a terminar la frase..."

            "Me alegra ver que no eres de piedra." if not p_ao_started:
                call p_Help
                #$pl.ch_pts("np", -1)

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx008
                show n_closefromup_eyebrows angryx04
                call n_closefromup_tears_tears
                with dissolve

                ne "??Por supuesto que no soy de piedra!"

                $ nteye = "front04"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "front08"
                show n_closefromup_mouth sadbiting_Silentx07
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

            "Seguro que tampoco ser??a tan horrible..." if not p_ao_started:
                call p_Help
                #$pl.ch_pts("np", -1)

                $ nteye = "front01"
                show n_closefromup_mouth sadbiting_Silentx03
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ nteye = "right01"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Prefiero no responderte a eso..."

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx07
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            # "Tampoco fue tan horrible." if p_ao_started: # NOPE.

            "Es una l??stima que no pueda darte un orgasmo..." if not gensex_YoureAMonster:
                call p_Help
                #$pl.ch_pts("np", -1)

                if p_ao_started:

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows suspiciousx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo dices como si hubieras disfrutado lo de ayer..."

                    $ nteye = "front04"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        "Fue intenso, pero tampoco lo describir??a como algo horrible.":
                            call p_Help
                            $pl.ch_pts("np", 1)

                            $ nteye = "front01"
                            show n_closefromup_mouth sadbiting_Silentx02
                            show n_closefromup_eyebrows surprisex01
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            if p_prot_aoNight_analReceived == "True":

                                $ nteye = "front04"
                                show n_closefromup_mouth sad_Talkingx003
                                show n_closefromup_eyebrows surprisex02
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "??De verdad...?"

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Talkingx05
                                show n_closefromup_eyebrows suspiciousx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "??Acaso prefieres mi oscura polla"

                                $ nteye = "front02"
                                show n_closefromup_mouth sad_Talkingx005
                                show n_closefromup_eyebrows suspiciousx04
                                call n_closefromup_tears_tears
                                with dissolve
                                
                                ne "antes que mi ardiente y h??meda entrepierna?"

                                $ nteye = "front03"
                                show n_closefromup_mouth sadbiting_Silentx04
                                show n_closefromup_eyebrows suspiciousx04
                                call n_closefromup_tears_tears
                                with dissolve

                                menu:

                                    "Es posible.":
                                        call p_Help
                                        $pl.ch_pts("np", 1)

                                        $ nteye = "front00"
                                        show n_closefromup_mouth sad_Silentx02
                                        show n_closefromup_eyebrows surprisex02
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "Hmm..."

                                        $ nteye = "right02"
                                        show n_closefromup_mouth sad_Talkingx003
                                        show n_closefromup_eyebrows suspiciousx02
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "Es bueno saberlo."

                                        $ nteye = "right05"
                                        show n_closefromup_mouth sadbiting_Silentx04
                                        show n_closefromup_eyebrows suspiciousx04
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        pause 0.2

                                        $ nteye = "front08"
                                        show n_closefromup_mouth sadbiting_Silentx07
                                        show n_closefromup_eyebrows sadx03
                                        call n_closefromup_tears_tears
                                        with dissolve


                                    "No, prefiero tu ardiente co??o.":
                                        call p_Help
                                        $pl.ch_pts("np", 2)

                                        $ nteye = "front02"
                                        show n_closefromup_mouth happy_Silentx03
                                        show n_closefromup_eyebrows sadx01
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        pause 0.2

                                        $ nteye = "front06"
                                        show n_closefromup_mouth happy_Talkingx04
                                        show n_closefromup_eyebrows sadx03
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "Me alegro."

                                        $ nteye = "front05"
                                        show n_closefromup_mouth happy_Talkingx09
                                        show n_closefromup_eyebrows surprisex02
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "Pero tambi??n podemos cambiar roles de tanto en cuando si te apetece..."

                                        $ nteye = "front03"
                                        show n_closefromup_mouth happybiting_Silentx07
                                        show n_closefromup_eyebrows suspiciousx04
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        p "..."

                                        $ nteye = "front06"
                                        show n_closefromup_mouth happy_Silentx08
                                        show n_closefromup_eyebrows normal
                                        call n_closefromup_tears_tears
                                        with dissolve

                                        ne "jejeje *Risilla no demasiado inocente*"

                                        $ nteye = "down05"
                                        show n_closefromup_mouth happybiting_Silentx06
                                        show n_closefromup_eyebrows sadx06
                                        call n_closefromup_tears_tears
                                        with dissolve

                            else:

                                $ nteye = "right02"
                                show n_closefromup_mouth sad_Talkingx002
                                show n_closefromup_eyebrows suspiciousx02
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Es bueno saberlo."

                                $ nteye = "right08"
                                show n_closefromup_mouth sadbiting_Silentx04
                                show n_closefromup_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                        "Fue algo intenso y doloroso, pero viendo c??mo lo disfrutaste, vali?? la pena.":
                            call p_Help

                            $ nteye = "front01"
                            show n_closefromup_mouth sad_Silentx02
                            show n_closefromup_eyebrows suspiciousx02
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "..."

                            if gensex_ILoveYouNeus:

                                $pl.ch_pts("np", 3)

                                $ nteye = "front05"
                                show n_closefromup_mouth happy_Talkingx05
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No me de ideas..."

                                $ nteye = "front06"
                                show n_closefromup_mouth happy_Talkingx07
                                show n_closefromup_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Mi querido Lancelot."

                                $ nteye = "front05"
                                show n_closefromup_mouth happybiting_Silentx05
                                show n_closefromup_eyebrows sadx04
                                call n_closefromup_tears_tears
                                with dissolve

                            else:
                                $pl.ch_pts("np", 2)

                                $ nteye = "front04"
                                show n_closefromup_mouth sad_Talkingx05
                                show n_closefromup_eyebrows surprisex01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "No me des ideas,"

                                extend " [protname]."

                                $ nteye = "front05"
                                show n_closefromup_mouth sadbiting_Silentx05
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                else:
                    $pl.ch_pts("np", 1)

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Es mejor que no sepas c??mo me pongo cuando logro un orgasmo..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    pt "Tampoco creo que sea tan horrible como dice..."

            "Y luego soy yo el que tiene que estar atado.":
                call p_Help

                if gensex_YoureAMonster:
                    $pl.ch_pts("np", -1)

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                else:
                    $pl.ch_pts("np", 1)

                    $ nteye = "front06"
                    show n_closefromup_mouth extra_burlesque
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "*Gnnn...*"

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                ne "Al menos he parado."

                if gensex_YoureAMonster:

                    $ nteye = "down05"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    $ nteye = "down05"
                    show n_closefromup_mouth happybiting_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                pt "Menos mal..."

            "...":
                call p_Help

    pause 0.2

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "??Por qu?? eres tan adictivo?"

    if not gensex_YoureAMonster:

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx05
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        scene morning04_bg bedroom_neus_a
        show kiss_ f_n_07:
            truecenter
            xzoom -1.0
            zoom 1.5 rotate -30
        with fade_short

        show kiss_ f_n_10
        with Dissolve(0.5)

        show kiss_ f_n_12
        with Dissolve(0.5)

        n "Acerca su rostro al tuyo y os mezcl??is en una apasionado beso."

        show kiss_ f_n_09
        with Dissolve(0.5)

        n "Sugerentemente se aparta de ti"

        $ ped_neus_whispers_sfx04 = 0.75
        $ ntlong = 3

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with fade_short

        n "mientras te mira con sus brillantes y h??medos ojos."

        $ ntlong = 4

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        n "De sus mejillas ves desprenderse una l??grima."

    else:

        n "Ves que te observa durante unos segundos en silencio."

####

label day06_neusAlone_happy:

    $ nteye = "front03"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    p "??Qu?? pasa?"

    if not gensex_YoureAMonster:

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

    ne "Nada."

    if not gensex_YoureAMonster:

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Simplemente,"

        extend " soy feliz."

        $ nteye = "front07"
        show n_closefromup_mouth happy_Silentx07
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx07
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "down05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

    pause 0.2

    scene day06
    with fade

    #$ ped_neus_whispers_sfx04 = 0.3
    $ ntlong = 2
    $ nblush = 4

    n "Desciende su cabeza hasta tu cuello"

    n "y percibes su tierno abrazo mientras sientes la humedad de sus l??grimas en tu piel."

    menu:

        pt "Est?? llorando..."

        "????Y ahora por qu?? te pones a llorar?!" if not gensex_ILoveYouNeus:
            call p_Help

            $pl.ch_pts("np", -1)

            ne "??Podr??as estarte unos segundos en silencio?"

            ne "te lo pido por favor..."

            p "..."

        "??Te pasa algo?":
            call p_Help

            ne "??No puedo simplemente estar feliz mientras te abrazo?"

            p "..."

        "Es una l??stima que est?? atado, me encantar??a poder abrazarte." if not gensex_YoureAMonster:
            call p_Help

            $pl.ch_pts("np", 2)

            if gensex_ILoveYouNeus:

                ne "Por favor,"

                ne "no sigas..."

                p "??El qu???"

                ne "Si sigues dici??ndome estas cosas,"

                ne "no podr?? aguantarlo..."

            else:

                ne "Me alegra saber que puedes llegar a ser cari??oso conmigo."

            n "Sientes que abandona su abrazo y se vuelve a acercarse a tu rostro."

            n "Para fundirse contigo en un nuevo beso."

            menu:

                "Desear??a poder tener este despertar por el resto de mis d??as.":
                    call p_Help

                    $pl.ch_pts("np", 2)

                    ne "Tonto..."

                    p "Es la verdad."

                    if not gensex_ILoveYouNeus:

                        ne "Al final pensar?? que me amas de verdad..."

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
                    with Dissolve(0.5)

                    pause 0.2

                    show kiss_ f_n_10
                    with Dissolve(0.5)

                    pause 0.2

                    show kiss_ f_n_07
                    with Dissolve(0.5)

                    n "Sientes sus labios de nuevo."

                    scene day06
                    with fade

                    n "Y vuelves a experimentar sus brazos agarr??ndote con una c??lida firmeza."

                "...":
                    call p_Help

        "...":
            call p_Help


    jump day06_neusAlone_whatYouWant


label day06_neusAlone_LookBracellet:

    # She looks at her bracelet while asking where is your collar.

    $ n_exp_shine = -0.01

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "down05"
    show n_closefromup_mouth happy_Silentx02
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with fade_short

    n "Ves que sus ojos est??n como ausentes."

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "almost_new_kevin"

    show day06
    with fade

    n "Cuando te fijas en qu?? direcci??n,"

    n "descubres que est?? observando esa pulsera de la feria que tiene en la mu??eca."

    menu:

        "Me hubiera gustado poder regalarte algo mejor." if MShooter_Bracelet == "GOLD":

            call day06_neusAlone_LookBracellet_kindAnswer

        "Me hubiera gustado poder entregarte la dorada." if not MShooter_Bracelet == "GOLD":

            call day06_neusAlone_LookBracellet_kindAnswer

        "...":
            call p_Help

    hide day06

    return

label day06_neusAlone_LookBracellet_kindAnswer:

    $pl.ch_pts("np",2)

    ne "Tonter??as..."

    hide day06

    $ nteye = "front02"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade_short

    ne "Prefiero mil veces esta pulsera de feria,"

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "que cualquier sortija o gema de joyer??a que me hubieras podido comprar."

    $ nteye = "down02"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    ne "Por mucho que te parezca una baratija,"

    $ nteye = "down04"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "para mi..."

    $ nteye = "front02"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "para mi no hay oro en el mundo que pueda comprar un recuerdo as??..."

    $ nteye = "down05"
    show n_closefromup_mouth happy_Silentx04
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front08"
    show n_closefromup_mouth happy_Silentx05
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pt "Si a mi tambi??n me lloviera el dinero del cielo..."

    return

label day06_neusAlone_whatYouWant:

    if MShooter_Bracelet in MShooter_Bracelet_var:
        call day06_neusAlone_LookBracellet

####
    # ped_neus_whispers_sfx04
    $ n_exp_shine = -0.01

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with fade_short

    ne "[protname]..."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    menu:

        "Dime.":
            call p_Help

            $ nteye = "front08"
            show n_closefromup_mouth happy_Silentx02
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_areYouSure

        "??Qu?? diablos quieres ahora?" if gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np",-2)

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx02
            show n_closefromup_eyebrows sadx07
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_areYouSure

        "??Qu?? deseas, mi princesa?" if gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np",2)

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_areYouSure

        "...":
            call p_Help
            $pl.ch_pts("np",-2)

            $ nteye = "front05"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows sadx07
            call n_closefromup_tears_tears
            with dissolve


            jump day06_neusAlone_areYouSure

####


label day06_neusAlone_areYouSure:

    pause 0.2

    if gensex_YoureAMonster:

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "??Tanto lamentas haberme conocido?"

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx04
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front02"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "??Lamentas haberme conocido?"

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

    menu:

        pt "??Lamento haberla conocido?"

        "??A qu?? viene esto ahora?":
            call p_Help
            $pl.ch_pts("np",1)

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_eyebrows sadx08
            call n_closefromup_tears_tears
            with dissolve

        "??Acaso lo dudas?" if gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np",-50)

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_eyebrows sadx08
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "right02"
            show n_closefromup_mouth sad_Talkingx02
            show n_closefromup_eyebrows sadx07
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo entiendo..."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx09
            show n_closefromup_eyebrows sadx09
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_farFromNeus_question

        "Cuando te digo que te amo, lo digo en serio." if gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np",4)

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx07
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Me alegra tanto escuchar eso."

            $ nteye = "down05"
            show n_closefromup_mouth sad_Talkingx03
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Aunque..."

            $ nteye = "front02"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            p "??Qu?? pasa?"

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_eyebrows sadx06
            call n_closefromup_tears_tears
            with dissolve

        "Por supuesto que no." if not gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np",3)

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help
            $pl.ch_pts("np",-1)

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx08
            show n_closefromup_eyebrows sadx08
            call n_closefromup_tears_tears
            with dissolve

    pause 0.2

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Al fin y al cabo,"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "si no me hubiera acercado a ti,"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx09
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "nada de esto hubiera ocurrido."

    $ nteye = "right03"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Podr??a culpar a mam?? de haberme convencido para ir en tu b??squeda,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "pero en realidad,"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "ten??a ganas de conocerte [protname]."

    $ nteye = "left02"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque lo ??nico que he logrado es poner tu vida en peligro"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx09
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    ne "y sacarte de una vida a la que jam??s podr??s volver."

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Tus amistades,"

    extend " tu trabajo,"

    extend " tus padres adoptivos..."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Deseo pensar que est??s a mi lado porque es lo que quieres;"

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "y no porque tengas miedo de morir,"

    $ nteye = "right04"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "o porque crees que no existe otra opci??n."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "A fin de cuentas,"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    ne "Padre me est?? buscando a mi."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx09
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "??l ya sab??a de tu existencia cuando mam?? escap??,"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "y a??n as?? jam??s te encontr??."

    $ nteye = "right04"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "Nunca has acudido a un {a=https://es.wikipedia.org/wiki/Aquelarre}aquelarre{/a},"

    $ nteye = "right03"
    show n_closefromup_mouth sad_Talkingx08
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "por lo que sus oscuras criaturas no ser??n capaces de localizarte si te alejas de mi."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "No puedes volver a tu antigua vida"

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "ni hablar de lo que te ha ocurrido estos d??as con nadie,"

    if DidacPregnant:

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "y deber??as abandonar a D??dac..."

        $ nteye = "front03"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        menu:

            "??De qu?? diablos est??s hablando?":
                call p_Help
                $pl.ch_pts("np",1)

                if DidacMCPregnant:

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Debido a que lo dejaste embarazado,"

                else:

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Debido a que qued?? embarazada,"

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "ya nunca m??s podr?? volver a ser un hombre."

                $ nteye = "front04"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                p "??Y por ser una mujer deber??a abandonarlo?"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Aunque se quemara regularmente las yemas de los dedos,"

                # huellas dactilares

                $ nteye = "right05"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

                ne "se cambiara de nombre,"

                $ nteye = "left04"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "se pintara el pelo de otro color,"

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

                ne "y lograra falsificar convincentemente sus documentos de identidad."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "Siempre cabe la posibilidad de que sufra un accidente,"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "o simplemente necesite una transfusi??n de sangre."

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    "??Qu?? tiene de malo su sangre?":
                        call p_Help

                        $ nteye = "front02"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Ya no es enteramente humana,"

                        $ nteye = "front03"
                        show n_closefromup_mouth sad_Talkingx08
                        show n_closefromup_eyebrows serious
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "y es mejor que eso no lo sepa nadie."

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Silentx05
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        p "..."

                    "...":
                        call p_Help

                $ nteye = "left02"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Si alguien investigara su pasado,"

                $ nteye = "left04"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "descubriera quien fue,"

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx09
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "y c??mo se convirti?? en mujer,"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "su vida correr??a un grave peligro."

                $ nteye = "front01"
                show n_closefromup_mouth sadbiting_Silentx02
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                p "Antes has dicho que estas criaturas no atacan a mujeres embarazadas."

                $ nteye = "front03"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "No atacan sin raz??n."

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Pero en general, las entes que moran en las sombras del conocimiento humano,"

                $ nteye = "right01"
                show n_closefromup_mouth sad_Talkingx09
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "son muy recelosas de su anonimato."

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "Si existe la posibilidad de que los humanos puedan sospechar"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx008
                show n_closefromup_eyebrows serious
                call n_closefromup_tears_tears
                with dissolve

                ne "aunque sea m??nimamente,"

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx10
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "de la existencia de estos sujetos m??s all?? del velo del umbral."

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "No solo deber??s preocuparte de las criaturas oscuras de Padre."

                $ nteye = "front04"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                p "????Te refieres a que hay cosas peores que esos ojos rojos?!"

                $ nteye = "right03"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "No te haces una idea..."

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Despu??s de lo que te he dicho,"

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "??A??n crees que estar??a segura contigo?"

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    pt "??D??dac estar??a segura conmigo?"

                    "Lo ??nico que s??, es que nunca dejar??a abandonado a un amigo.":
                        call p_Help
                        $pl.ch_pts("np",2)

                        $ day06_escapeWithDidac = True

                        $ nteye = "front05"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        pause 0.2

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Aunque no tengas ni idea de los riesgos a lo que realmente te expondr??as,"

                        $ nteye = "front06"
                        show n_closefromup_mouth happy_Talkingx03
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "en el fondo,"

                        $ nteye = "front04"
                        show n_closefromup_mouth happy_Talkingx06
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "me alegra o??rte decir eso."

                        $ nteye = "down05"
                        show n_closefromup_mouth sadbiting_Silentx05
                        show n_closefromup_eyebrows sadx03
                        call n_closefromup_tears_tears
                        with dissolve

                    "Quiz??s tengas raz??n...":
                        call p_Help
                        $pl.ch_pts("np",1)

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx06
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Aunque te cueste creerlo,"

                        $ nteye = "front03"
                        show n_closefromup_mouth sad_Talkingx003
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "hay muchas cosas que a??n desconoces de este mundo."

                        $ nteye = "front08"
                        show n_closefromup_mouth sadbiting_Silentx08
                        show n_closefromup_eyebrows sadx07
                        call n_closefromup_tears_tears
                        with dissolve

                    "Conf??o en ti, [neusname]." if not gensex_YoureAMonster:
                        call p_Help
                        $pl.ch_pts("np",2)

                        $ nteye = "front05"
                        show n_closefromup_mouth happy_Silentx03
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Hmmm... *sonrisa tierna*"

                        $ nteye = "front07"
                        show n_closefromup_mouth happy_Talkingx07
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Gracias [protname]."

                        $ nteye = "front08"
                        show n_closefromup_mouth happybiting_Silentx05
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                    "??Acaso contigo estar?? m??s segura?" if not gensex_ILoveYouNeus:
                        call p_Help
                        $pl.ch_pts("np",-1)

                        $ day06_escapeWithDidac = True

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Talkingx07
                        show n_closefromup_eyebrows serious
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Gracias a tu esperma,"

                        $ nteye = "front04"
                        show n_closefromup_mouth sad_Talkingx08
                        show n_closefromup_eyebrows angryx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "puedo realizar peque??as intervenciones en el velo de la realidad,"

                        $ nteye = "front03"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "pero sin ti..."

                        $ nteye = "right04"
                        show n_closefromup_mouth sad_Silentx05
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        menu:

                            pt "Sin ella..."

                            "Usar a D??dac para hacerme chantaje emocional, ??por qu?? no me sorprende?":
                                call p_Help
                                $pl.ch_pts("np",-1)

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Silentx02
                                show n_closefromup_eyebrows surprisex02
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.2

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Talkingx10
                                show n_closefromup_eyebrows angryx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "??Eso no es verdad!"

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Silentx04
                                show n_closefromup_eyebrows angryx01
                                call n_closefromup_tears_tears
                                with dissolve

                                p "??En serio?"

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Silentx02
                                show n_closefromup_eyebrows surprisex02
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Es lo que has est??s haciendo desde el principio."

                                $ nteye = "front02"
                                show n_closefromup_mouth sadbiting_Silentx05
                                show n_closefromup_eyebrows sadx02
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                $ nteye = "right04"
                                show n_closefromup_mouth sad_Talkingx003
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Yo..."

                                $ nteye = "front08"
                                show n_closefromup_mouth sad_Talkingx06
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve
                                
                                ne "Te prometo que ahora no te estoy mintiendo."

                                $ nteye = "front00"
                                show n_closefromup_mouth sadbiting_Silentx04
                                show n_closefromup_eyebrows surprisex03
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Y se supone que antes tampoco."

                                $ nteye = "down05"
                                show n_closefromup_mouth sad_Silentx05
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "..."

                                $ nteye = "right05"
                                show n_closefromup_mouth sadbiting_Silentx07
                                show n_closefromup_eyebrows sadx07
                                call n_closefromup_tears_tears
                                with dissolve

                            "...":
                                call p_Help
                                #$pl.ch_pts("np",-1)

                                $ nteye = "front08"
                                show n_closefromup_mouth sadbiting_Silentx02
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                    "...":
                        call p_Help

                        $ nteye = "front08"
                        show n_closefromup_mouth sadbiting_Silentx02
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                ###
            

            "Aunque mi vida estuviera en peligro, jam??s har??a tal cosa.":
                call p_Help
                $pl.ch_pts("np",1)

                $ day06_escapeWithDidac = True

                ne "..."

                if DidacPregnant:

                    ne "Aunque lo hayas dejado embarazado,"

                else:

                    ne "Aunque no estuvieras ah?? para protegerlo de sus impulsos,"

                ne "D??dac tiene suerte de tenerte."


            "...":
                call p_Help
                $pl.ch_pts("np",-1)

        ##

        pause 0.2

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Si lo deseas..."

    else:

        $ day06_escapeWithDidac = True

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "ni siquiera con D??dac,"

        $ nteye = "right04"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "pero si lo deseas..."

###

    if day06_escapeWithDidac:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Podr??a daros dinero y medios para que pod??is ir a un lugar seguro"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne " para que ni siquiera yo pudiera volver a encontraros."

    else:

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Podr??a darte dinero y medios para irte a un lugar seguro"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "para que ni siquiera yo pudiera volverte a encontrar."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        if DidacPregnant:

            menu:

                "??Y qu?? pasar??a con D??dac?":
                    call p_Help

                    $ nteye = "right03"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Es mejor que no lo sepas."

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    menu:

                        "??Lo matar??as?":
                            call p_Help

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx04
                            show n_closefromup_eyebrows sadx05
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Te aseguro que matarla ser??a lo m??s recomendable en su situaci??n."

                            $ nteye = "left04"
                            show n_closefromup_mouth sad_Talkingx03
                            show n_closefromup_eyebrows sadx06
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "No te imaginas los horrores que se esconden tras el velo."

                        "...":
                            call p_Help

                            $ nteye = "front08"
                            show n_closefromup_mouth sadbiting_Silentx08
                            show n_closefromup_eyebrows sadx07
                            call n_closefromup_tears_tears
                            with dissolve

                "Ya te he dicho que no lo har??.":

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front07"
                    show n_closefromup_mouth happybiting_Silentx07
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    #n "Una ligera sonrisa aparece en sus labios."

                "...":
                    call p_Help

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve
                    

    pause 0.2

    $ nteye = "left04"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Quiz??s as?? seas capaz de ser feliz y tener tu propia vida."

    $ ntlong += 1

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "Al fin y al cabo,"

    $ nteye = "front08"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "has acudido a las tres citas como te ped??."

    $ ntlong += 1

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx02
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Has cumplido el {a=https://es.wikipedia.org/wiki/Pacto}pacto{/a} que hicimos."

    $ ntlong += 1

    $ nteye = "front06"
    show n_closefromup_mouth happybiting_Silentx04
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "El pacto con la bruja..."

        "[neusname], no te voy a abandonar." if not gensex_YoureAMonster and not gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", 5)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            ne "Gracias [protname]."

            $ nteye = "front07"
            show n_closefromup_mouth happybiting_Silentx08
            show n_closefromup_eyebrows sadx07
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            scene day06
            with fade

            n "Acerca dulcemente su rostro a tu pecho y reposa su cuerpo desnudo sobre el tuyo"

            n "mientras sientes sus l??grimas derram??ndose sobre tu piel."

        "<Aceptar su oferta de tener una vida lejos de ella>":
            call p_Help
            #$pl.ch_pts("np", -50)

            jump day06_neusAlone_letLeave
                # p "Si no eres el monstruo que dices ser,"
                # p "nos dejar??s marchar a D??dac y a mi,"

        "<Abrazarla y decirle que nunca la abandonar??s>" if gensex_ILoveYouNeus:
            call p_Help
            $pl.ch_pts("np", 5)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            scene day06
            with fade

            ne "??Uh?"

            if gensex_ILoveYouNeus:

                p "[neusname]."

                ne "??S???..."

                p "Te amo."

                $pl.ch_pts("np", 3)

            n "Alarga sus brazos para rodearte entrelazando vuestros cuerpos desnudos en un dulce abrazo."

        "??Seguro que no es un truco para ver qu?? clase de perro fiel soy?" if not gensex_ILoveYouNeus:
            $pl.ch_pts("np", -3)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx06
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx08
            show n_closefromup_eyebrows angryx05
            call n_closefromup_tears_tears
            with dissolve

            ne "La fidelidad no es una cuesti??n de sumisi??n,"

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "sino de confianza."

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx03
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            p "??Y se supone que debo confiar en ti?"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx06
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            jump day06_neusAlone_DidacCondition
                # ne "..."
                # ne "No s?? qu?? m??s quieres que haga"
                # ne "para demostrarte que deseo con toda mi alma"
                # ne "ser una mejor persona."
                # p "Me has enga??ado,"
                # p "manipulado,"
                # p "y has asesinado a un ni??o inocente."

    jump day06_ending_NeusLove

#######

########
# CREDITS

label day06_ending_NeusLove:

    call day06_ending_window

    p "Oye..."

    p "??Qu?? est??s haciendo?"

    ne "Se te est?? volviendo a poner dura..."

    if day06_bloodDrink_cond:

        p "??Es que se me ha bajado en alg??n momento?"

        ne "..."

        ne "S??,"

        ne "al final se te ha terminado bajando."

        p "Lo dices algo decepcionada."

        ne "..."

        ne "Quiz??s."

    p "??No puedes estarte quietecita unos minutos?"

    ne "Ya hace rato que no te he hecho nada..."

    p "Un poquito m??s."

    ne "??Es que no te gusta lo que te hago?"

    if gensex_YoureAMonster:

        p "..."

    else:

        p "Sabes que no es eso."

    ne "??Te duele?"

    if day06_bloodDrink_cond:

        p "Sinceramente,"

        p "bastante."

    else:

        p "Un poco..."

    ne "??Y esto?"

    if day06_bloodDrink_cond:

        p "Quiz??s no tanto..."

    else:

        p "No tanto..."

    ne "??Y esto?"

    p "Por dios..."

    ne "Me alegro de que te guste."

    ne "Me podr??a pasar la eternidad haci??ndotelo..."

    p "Dudo que fuera posible..."

    ne "??Me est??s retando?"

    p "Me refiero a que no creo que mi polla pudiera aguantarlo.."

    if day06_bloodDrink_cond:

        p "??No has visto c??mo est???"

    ne "..."

    ne "Te sorprender??as de lo que tu cuerpo es capaz de aguantar."

    p "??Y eso c??mo lo sabes?"

    ne "Simplemente lo s??."

    p "??Por qu?? todo tu cuerpo y especialmente tu interior,"

    p "es tan caliente?"

    ne "Por tu culpa."

    p "Te lo pregunto en serio."

    ne "..."

    ne "Cuando me pongo caliente,"

    ne "mi cuerpo reacciona de este modo,"

    ne "es algo que no puedo controlar,"

    ne "bueno,"

    ne "al menos no del todo,"

    ne "cuando estoy contigo intento controlarlo."

    p "Ayer no pareciste haberlo controlado demasiado."

    if p_ao_started:

        ne "Ayer no hiciste lo que te ped??."

    else:

        ne "Y eso que no me llevaste al orgasmo."

        p "Porque fue lo que me pediste."

        ne "Precisamente..."

    p "??Podemos tomarnos un descanso?"

    ne "..."

    if day06_neusAlone_uncuff_cond:

        ne "Gracias [protname]."

        p "??Por qu???"

        if gensex_ILoveYouNeus:

            ne "Por haberme hecho el amor"

        else:

            ne "Por haberme follado"

        ne "sin necesidad de estar esposado."

        p "Te dije que pod??as confiar en mi."

        ne "No sabes lo feliz que me haces."

    p "[neusname]..."

    ne "Tu polla est?? dura..."

    if day06_bloodDrink_cond:

        p "Y hecha una mierda."

        ne "Las he visto peores."

    p "Solo te pido unos minutos..."

    ne "..."

    p "????[neusname]?!"

    ne "??Es que est?? muy dura!"

    p "??No tienes suficiente fuerza de voluntad?"

    ne "No seas malo..."

    if not gensex_YoureAMonster:

        p "Abr??zame."

        ne "Esto tambi??n me gusta."

    else:

        p "Ap??rtate de mi polla."

        ne "Vale..."

        p "Tampoco te he dicho que me abraces."

        ne "Eres un quejica."

    p "[neusname]..."

    ne "??Qu???"

    p "Tu pierna sigue roz??ndome la entrepierna..."

    ne "Pero no estoy usando mi lengua."

    if day06_bloodDrink_cond:

        p "????No ves lo jodida que est???!"

        ne "..."

        ne "Supongo que haberte hecho beber mi sangre"

        ne "no ha sido la mejor de las ideas..."

        ne "Pero..."

        p "..."

    else:

        p "??No ves lo roja que est???"

        ne "Ayer la ten??as peor y te corriste."

    p "Me temo que no puedo hacer nada para convencerte,"

    p "??verdad?"

    if gensex_ILoveYouNeus:

        ne "Dime cuanto me amas y parar??."

    elif gensex_YoureAMonster:

        ne "Te prometo que lo intentar??..."

    else:

        ne "Dime cuanto me deseas y parar??."

    p "[neusname]."

    ne "??S???"

    if gensex_ILoveYouNeus:

        p "Te amo."

        ne "Yo tambi??n te amo."

    elif not gensex_YoureAMonster:

        p "Te deseo."

    if not gensex_YoureAMonster:

        p "..."

    p "Has dicho que parar??as..."

    ne "S??..."

    ne "Pero no tengo fuerza de voluntad."

    p "Al final me vas a matar."

    ne "No te preocupes,"

    ne "si eso ocurre ya te resucitar??."

    p "??C??mo?"

    ne "Es una broma,"

    extend " tont??n."

    ne "O quiz??s no..."

    p "??[neusname]!"

    if gensex_YoureAMonster:

        ne "Lo lamento..."

        ne "pero es como soy."

    else:

        ne "B??same."

    window hide dissolve
    pause

    call false_gameover

    jump textless_gameover

    #jump pre_gamover


# label pre_gamover:

#     hide screen c_creditos
#     scene black
#     with fade_long1s

#     h01 "[protname]."

#     h01 "Pero en realidad,"

#     h01 "este no es tu verdadero nombre,"

#     h01 "??verdad?"

#     h01 "Hmmm..."

#     h01 "Interesante."

#     h01 "No puedes ni responderme."

#     h01 "Seguramente debes estar pregunt??ndote..."

#     h01 "??Quien diablos soy?"

#     h01 "Pero en realidad,"

#     h01 "la pregunta correcta ser??a..."

#     scene day06
#     with dissolve

#     m01 "????QU?? COJONES HACES AQU?? CON LA LUZ APAGADA?!"

#     h01 "??Akuma!"

#     h01 "Pens?? que te hab??as ido a..."

#     m01 "NO PUEDES ENTRAR EN UNA ZONA RESTRINGIDA!"

#     m01 "??ESTO ES ARKHAM!"

#     m01 "??NO TU ZONA DE PATIO PARTICULAR!"

#     h01 "??No te han dicho nunca que eres muy sexy cuando gritas?"

#     m01 "??SAL DE AQU?? ANTES DE QUE TE ROMPA LAS PIERNAS!"

#     h01 "No creo que tu padre estuviera muy contento si..."

#     h01 "..."

#     h01 "Vale,"

#     extend " vale..."

#     h01 "ya salgo,"

#     h01 "no es necesaria tanta violencia..."

#     h01 "Supongo que ya nos volveremos a ver."

#     m01 "??Con quien diablos est??s hablando?"

#     h01 "??Te parece que estoy hablando con alguien?"

#     m01 "Hmm..."

#     h01 "Aunque estar??a encantado de saludar a estas dos bellezas cada ma??ana..."

#     m01 "??QUE SALGAS DE AQU?? NARICES!"

#     h01 "??OUCH!"

#     m01 "..."

#     m01 "??Realmente hablaba solo?"

#     h01 "Oye bonita,"

#     h01 "??C??mo te llamas?"
 
#     h01 "??Podr??a tener tu n??mero de tel??fono?"

#     m01 "??NO TE PUEDO DEJARTE SUELTO NI UN SEGUNDO!"

#     ono "PUM"

#     scene black
#     with fade

#     jump textless_gameover



#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
## blood drink

label day06_bloodDrink:

    $ day06_bloodDrink_cond = True

    if day06_company == "neusDidac":

        $ nteye = "front01"
        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "??Y qu?? es lo que me tengo que beber?"

        $ Pedrera_char_Cond = "NeusWall"
        call Pedrera_char_lab

        $ nteye = "front08"
        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with Dissolve(0.5)

    else:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

    ne "Hubiera sido mejor preparar un frasco para esto,"

    if day06_company == "neusDidac":
        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab
        #show n_closefromup_body naked

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears

    if day06_company == "neusDidac":
        with Dissolve(0.5)
    else:
        with dissolve

    ne "pero supongo que no pasar?? nada."

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    pt "??Qu?? deber??a pasar?"

    $ nteye = "down04"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Acerca el dedo ??ndice de su mano izquierda a la mu??eca de su otro brazo,"

    n "y con su u??a, presiona con fuerza su suave piel hasta hacer una herida."

    if day06_company == "neusDidac":

        p "??Qu??...?"

    n "Sientes una gota caliente cayendo sobre tu rostro."

    n "Acerca su sangrienta mu??eca hasta tus labios."

    ne "Bebe."

    menu:

        "????En serio no eres un vampiro?!":
            call p_Help

            ne "No hagas preguntas est??pidas."

            pt "No me parece tan est??pida la pregunta..."

            ne "Bebe."

        "<Obedecer>":
            call p_Help


    n "Abres tu boca para empezar a lamer su herida."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with fade_short

    ne "No basta con lamer,"

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "tienes que succionarla."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Atrapas su mu??eca con tus labios y sorbes su c??lido l??quido vital."

    n "Lo que al principio te parec??a el t??pico sabor salado y met??lico de una c??lida sangre,"

    n "es ahora algo distinto,"

    n "su gusto salado se va volviendo algo m??s dulce, envolvente y extra??amente afrutado."

    n "A medida que lo ingieres,"

    n "un calor en la punta de los dedos de tus manos y de tus pies empieza aflorar."

    n "El calor se va extendiendo por tus nudillos y poco a poco a lo largo de tu cuerpo."

    n "Tus m??sculos vibran levemente."

    ne "Creo que ya tienes suficiente."

    n "No sabr??as definir si su sabor es ??spero, ??cido, salado o dulce,"

    n "es casi es una combinaci??n de ellos,"

    n "y al mismo tiempo no es ninguno en particular."

    n "Sin apenas darte cuenta, te agarras a su brazo y succionas con m??s ??mpetu."

    ne "[protname]..."

    n "El gusto se va volviendo m??s carnoso y elegante,"

    n "un sabor que nunca antes hab??as catado."

    ne "??He dicho que ya basta!"

    n "Intenta apartar su mano de tu boca,"

    n "pero instintivamente la sigues con los labios para poder seguir bebiendo de ese elixir."

    n "Te agarra la cara con su otra mano intentando apartarte de ella."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx10
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with hpunch
    with hpunch

    ne "??[protname]!"

    $ nteye = "front04"
    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    p "??Euh?"

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    p "Yo..."

    $ nteye = "down05"
    show n_closefromup_mouth sadbiting_Silentx09
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Pasa su sangrienta mu??eca por sus labios,"

    n "usando su lengua para relamerse la herida."

    n "Cuando aparta el brazo ves que lo ??nico que queda es una cicatriz que empieza a desaparecer."

    p "??Qu??...?"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with fade

    ne "Tranquilo, no pasa nada."

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "La primera vez que beb?? de una de mis hermanas,"

    $ nteye = "right04"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "actu?? de un modo mucho peor."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Cuando nuestra sangre es ingerida por un ser no humano,"

    $ nteye = "left02"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "tiene un sabor,"

    extend " adictivo..."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "No es algo f??cil de evitar..."

    $ nteye = "right05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    n "Tu cuerpo empieza a sudar."

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Especialmente si nunca has pasado por el proceso de iniciaci??n."

    $ nteye = "front02"
    show n_closefromup_mouth sadbiting_Silentx01
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "??Proceso de iniciaci??n?"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "El primer {a=https://es.wikipedia.org/wiki/Aquelarre}aquelarre{/a}."

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Por eso te dije que era mejor usar un frasco."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "De este modo, cuando se termina el bote,"

    extend " ya no bebes m??s."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "??Est?? haciendo calor o soy yo?"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Es la reacci??n normal."

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Bueno,"

    extend " quiz??s has bebido m??s de lo que de la cuenta..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Deber??a haberte detenido antes."

    $ nteye = "front04"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    n "Tus m??sculos empiezan a palpitar con arrebato."

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx01
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    pt "????Qu?? cojones?!"

    $ nteye = "down02"
    show n_closefromup_mouth happybiting_Silentx03
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Sientes que recobras el control sobre tu cuerpo"

    n "y que tienes ganas de levantarte, saltar, derribar un muro, gritar..."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    p "??Joder!"

    $ nteye = "front02"
    show n_closefromup_mouth happy_Silentx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "??Est??s segura que voy a estar bien?"

    $ nteye = "front08"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "S??,"

    extend " deber??as estar bien."

    $ nteye = "front00"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    p "Hasta que se me termine esta euforia,"

    extend " supongo."

    $ nteye = "front07"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "S??..."

    $ nteye = "front03"
    show n_closefromup_mouth happybiting_Silentx06
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    p "Ya..."

    return

#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################

label day06_neusAlone_DidacCondition:

    pause 0.2

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "No s?? qu?? m??s quieres que haga"

    $ ntlong += 1

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "para demostrarte que deseo con toda mi alma"

    $ nteye = "front06"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    ne "ser una mejor persona."

    $ ntlong += 1

    $ nteye = "front04"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    p "Me has enga??ado,"

    $ nteye = "front03"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    p "manipulado,"

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "y has asesinado a un ni??o inocente."

    $ nteye = "right02"
    show n_closefromup_mouth sadbiting_Silentx06
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    p "Eso sin contar con las atrocidades que hiciste antes de llegar a Barcelona."

    $ nteye = "right05"
    show n_closefromup_mouth sadbiting_Silentx08
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ nteye = "front06"
    show n_closefromup_mouth sadbiting_Silentx09
    show n_closefromup_eyebrows sadx09
    call n_closefromup_tears_tears
    with dissolve

    p "??Qu?? clase de enfermo mental crees que soy?"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "Te ruego que me des la oportunidad de conocerme mejor,"

    $ nteye = "left04"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "no te pido m??s."

    $ nteye = "front08"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    jump day06_neusAlone_letLeave

#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################

label day06_neusAlone_letLeave:

    pause 0.2

    $ nteye = "front02"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    p "Si no eres el monstruo que dices ser,"

    $ nteye = "front01"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "nos dejar??s marchar a D??dac y a mi,"

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx10
    show n_closefromup_eyebrows sadx10
    call n_closefromup_tears_tears
    with dissolve

    p "??verdad?"

    if DidacPregnant:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "D??dac no volver?? a ser el hombre que fue."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        p "Eso ya lo s??."

        # huella dactilar yema de los dedos

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "No existe como persona f??sica,"

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx10
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        ne "nunca podr??s demostrar d??nde naci??"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows angryx05
        call n_closefromup_tears_tears
        with dissolve

        ne "y si alg??n d??a alguien descubre que en su d??a fue un hombre,"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "no solo es posible que ??l muera de la peor manera,"

        $ nteye = "front01"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "sino que adem??s Padre sabr?? d??nde est??s."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        menu:

            "Eso ser?? mi problema.":
                call p_Help

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx11
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "??Acaso no ser?? tambi??n su problema?"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx09
                show n_closefromup_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx09
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "??Le contar??s toda la verdad?"

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx10
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

            "Es cuesti??n de pregunt??rselo.":
                call p_Help

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx13
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "??Pero le contar??s toda la verdad?"

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx10
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

        menu:

            "??Qu?? verdad?":
                call p_Help
                $pl.ch_pts("np",1)

                $ nteye = "right05"
                show n_closefromup_mouth sadbiting_Silentx10
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Sin ti,"

                $ nteye = "right01"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "lo m??s probable es que vuelva con Padre."

                $ nteye = "right02"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "No creo que tenga el suficiente coraje"

                $ nteye = "right05"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "como para experimentar lo que sufri?? mam?? por ti..."

                if gensex_YoureAMonster:

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Tampoco me sorprende."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Silentx10
                    show n_closefromup_eyebrows angryx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx13
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                else:

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx06
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    pt "No puedo culparla de eso..."

                    $ nteye = "front06"
                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_eyebrows sadx08
                    call n_closefromup_tears_tears
                    with dissolve

                pause 0.2

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "A Meritxell le borrar?? sus recuerdos como anta??o"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "e intentar?? que viva lejos de Barcelona,"

                $ nteye = "left02"
                show n_closefromup_mouth sad_Talkingx006
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "pero con D??dac..."

                $ nteye = "left05"
                show n_closefromup_mouth sadbiting_Silentx06
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                p "..."

                $ nteye = "front02"
                show n_closefromup_mouth sadbiting_Silentx07
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

                ne "Por mucho que le borre la memoria,"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "seguir?? habiendo un vac??o en su historial,"

                $ nteye = "front04"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                ne "una persona sin patria,"

                extend " sin origen,"

                extend " sin padres..."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Tendr?? que pasarse la vida en un perfil bajo para no levantar ning??n tipo de sospecha."

                $ nteye = "left05"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Nunca podr?? saber que fue un hombre,"

                $ nteye = "left01"
                show n_closefromup_mouth sad_Talkingx10
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "jam??s podr?? pedir un cr??dito al banco,"

                $ nteye = "left02"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

                ne "nunca podr?? acudir a un hospital p??blico,"

                $ nteye = "left03"
                show n_closefromup_mouth sad_Talkingx09
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "tendr?? que quemarse las yemas de sus dedos cada cierto tiempo..."

                $ nteye = "left05"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx08
                call n_closefromup_tears_tears
                with dissolve

                ne "y esto solo son algunos ejemplos..."

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx005
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "??Realmente deseas esta vida para tu amigo?"

                $ nteye = "front00"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                p "????Y acaso contigo vivir??a mucho mejor?!"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "Gracias a tu esperma,"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx06
                call n_closefromup_tears_tears
                with dissolve

                ne "ser??a capaz de hacer peque??as manipulaciones"

                $ nteye = "right04"
                show n_closefromup_mouth sad_Talkingx05
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                ne "en las mentes de las personas que se hicieran demasiadas preguntas,"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx06
                show n_closefromup_eyebrows sadx04
                call n_closefromup_tears_tears
                with dissolve

                ne "evitando ciertos problemas."

                $ nteye = "front01"
                show n_closefromup_mouth sad_Talkingx005
                show n_closefromup_eyebrows serious
                call n_closefromup_tears_tears
                with dissolve

                ne "As?? que s??,"

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx07
                show n_closefromup_eyebrows sadx05
                call n_closefromup_tears_tears
                with dissolve

                ne "har??a la vida de D??dac mucho m??s sencilla."

                $ nteye = "front05"
                show n_closefromup_mouth sadbiting_Silentx08
                show n_closefromup_eyebrows sadx07
                call n_closefromup_tears_tears
                with dissolve

                menu:

                    "????Acaso no ves que est??s haci??ndome chantaje emocional?!":
                        call p_Help
                        $pl.ch_pts("np",-2)

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx003
                        show n_closefromup_eyebrows sadx04
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "No."

                        $ nteye = "front08"
                        show n_closefromup_mouth sad_Talkingx05
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Te estoy mostrando la situaci??n."

                        $ nteye = "right01"
                        show n_closefromup_mouth sad_Talkingx07
                        show n_closefromup_eyebrows sadx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "De un modo u otro,"

                        $ nteye = "right02"
                        show n_closefromup_mouth sad_Talkingx06
                        show n_closefromup_eyebrows sadx07
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "ser?? tu decisi??n."

                        $ nteye = "front01"
                        show n_closefromup_mouth sad_Talkingx04
                        show n_closefromup_eyebrows sadx01
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "Solo quiero que sepas las consecuencias de tu elecci??n."

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Silentx05
                        show n_closefromup_eyebrows sadx06
                        call n_closefromup_tears_tears
                        with dissolve

                    "Me importa un r??bano la vida de D??dac." if not day06_escapeWithDidac:
                        call p_Help
                        $pl.ch_pts("np",-6)

                        $ nteye = "front00"
                        show n_closefromup_mouth sad_Silentx02
                        show n_closefromup_eyebrows surprisex03
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "..."

                        $ nteye = "front05"
                        show n_closefromup_mouth sad_Talkingx09
                        show n_closefromup_eyebrows angryx05
                        call n_closefromup_tears_tears
                        with dissolve

                        ne "??Y el monstruo soy yo?"

                        $ nteye = "right05"
                        show n_closefromup_mouth sadbiting_Silentx08
                        show n_closefromup_eyebrows sadx07
                        call n_closefromup_tears_tears
                        with dissolve

                    "Estaremos mucho mejor sin ti, no tengas la menor duda.":
                        call p_Help

                        $pl.ch_pts("np",-1)

                        $ nteye = "front00"
                        show n_closefromup_mouth sadbiting_Silentx06
                        show n_closefromup_eyebrows surprisex04
                        call n_closefromup_tears_tears
                        with dissolve

                        pause 0.3

                        $ nteye = "right04"
                        show n_closefromup_mouth sad_Talkingx03
                        show n_closefromup_eyebrows sadx08
                        call n_closefromup_tears_tears
                        with Dissolve(1.0)

                        ne "Siento que pienses as??..."

                        $ nteye = "left05"
                        show n_closefromup_mouth sadbiting_Silentx08
                        show n_closefromup_eyebrows sadx10
                        call n_closefromup_tears_tears
                        with dissolve

                p "..."

            "Le contar?? lo que quiera." if not gensex_ILoveYouNeus:
                call p_Help

                $pl.ch_pts("np",-2)

                $ nteye = "front00"
                show gensex_oral_n_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_n_frontHead_exp_eyebrows surprisex04
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                p "No hagas como si ahora te interesaras por D??dac,"

                $ nteye = "front04"
                show gensex_oral_n_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_n_frontHead_exp_eyebrows sadx05
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                p "cuando todo esto ha empezado por tu culpa."

                $ nteye = "right04"
                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
                show gensex_oral_n_frontHead_exp_eyebrows sadx06
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

                ne "..."

                $ nteye = "right05"
                show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx08
                show gensex_oral_n_frontHead_exp_eyebrows sadx07
                call gensex_oral_n_frontHead_exp_tears_tears
                with dissolve

            "...":
                call p_Help

        pause 0.2

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve
    
        ne "Solo te pido que si decides irte,"

        $ nteye = "front02"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "te escondas lo mejor que puedas."

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo m??s probable,"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

        ne "es que cuando nos volvamos a ver,"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "tenga que matarte."

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx09
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        $ nteye = "front04"
        show n_closefromup_mouth sadbiting_Silentx05
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        p "??Matarme?"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "S??."

        if not gensex_ILoveYouNeus:

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx03
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            p "????Y a??n tienes los huevos de decirme que no eres un monstruo?!"

        else:

            $ nteye = "front00"
            show n_closefromup_mouth sadbiting_Silentx02
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            p "Y dices que me amas..."

        $ nteye = "front02"
        show n_closefromup_mouth sad_Talkingx13
        show n_closefromup_eyebrows angryx06
        call n_closefromup_tears_tears
        with dissolve

        ne "????Acaso sigues sin entender por qu?? he huido de Padre?!"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx15
        show n_closefromup_eyebrows angryx07
        call n_closefromup_tears_tears
        with dissolve

        ne "??Precisamente para no volver a ser quien era!"

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero sin ti,"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows sadx09
        call n_closefromup_tears_tears
        with dissolve

        ne "no..."

        $ nteye = "right04"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "No hay otro modo."

        $ nteye = "front06"
        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_eyebrows sadx09
        call n_closefromup_tears_tears
        with dissolve

        ne "Aunque me quitase la vida,"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "en el siguiente aquelarre volver??a a renacer."

        $ nteye = "front08"
        show n_closefromup_mouth sadbiting_Silentx09
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "La elecci??n es tuya."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx06
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "S??."

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "Tienes mi palabra."

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx08
        call n_closefromup_tears_tears
        with dissolve

    $ ped_neus_whispers_sfx04 = 0
    $ n_exp_shine = 0.0

    menu day06_neusAlone_farFromNeus_question:

        "<Quedarte>" if not gensex_YoureAMonster:

            $ nteye = "front01"
            show n_closefromup_mouth happy_Silentx02
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front07"
            show n_closefromup_mouth happy_Silentx05
            show n_closefromup_eyebrows sadx10
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx08
            call n_closefromup_tears_tears
            with dissolve

            ne "Gracias por entenderlo [protname]."

            $ nteye = "front06"
            show n_closefromup_mouth happy_Silentx06
            show n_closefromup_eyebrows sadx09
            call n_closefromup_tears_tears
            with dissolve

            jump day06_ending_NeusLove

        "<Marcharte sin D??dac lejos de [neusname]." if not day06_escapeWithDidac:
            call p_Help

            $ day06_escapeWithDidac = False

            jump day06_neusAlone_farFromNeus

        "<Marcharte con D??dac lejos de [neusname].":
            call p_Help

            $ day06_escapeWithDidac = True

            jump day06_neusAlone_farFromNeus

#####


################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################


################################################################################################
################################################################################################
################################################################################################

label day06_neusDidac_whereWeAre:

    if day06_company == "neusDidac":

        $ Pedrera_char_Cond = "NeusWall"
        call Pedrera_char_lab

        $ nteye = "front08"
        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx01
        call n_closefromup_tears_tears
        with fade

    else: # "neusAlone"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

    ne "En un lugar seguro."

    if day06_company == "neusDidac":
        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        #show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears

    if day06_company == "neusDidac":
        with Dissolve(0.5)
    else:
        with dissolve

    p "Por favor,"

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    p "no me abrumes con tantos detalles..."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "??Acaso importa?"

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx03
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    $ day06_neusDidac_whereWeAre_trustSilence_Cond = False

    $ day06_neusDidac_whereWeAre_trust_Cond = "trust"

    menu:

        "Es algo que me gustar??a saber.":
            call p_Help
            $pl.ch_pts("np", -1)

            $ day06_neusDidac_whereWeAre_trust_Cond = "doubts"

            $ nteye = "front04"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            jump day06_neusDidac_whereWeAre_city


        "S??, importa.":
            call p_Help
            #$pl.ch_pts("np", -3)

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx06
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "??Acaso no te f??as de mi?"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx04
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            menu:

                pt "Usando chantaje emocional..."

                "No demasiado." if not gensex_ILoveYouNeus:
                    call p_Help
                    $pl.ch_pts("np", -3)

                    $ day06_neusDidac_whereWeAre_trust_Cond = "distrust"

                    $ nteye = "front00"
                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows surprisex03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right04"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lamento que pienses as??."

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                "Claro que s??.":
                    call p_Help
                    $pl.ch_pts("np", 1)

                    $ day06_neusDidac_whereWeAre_trust_Cond = "trust"

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx08
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Pues entonces qu?? m??s da d??nde estemos?"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Silentx02
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front04"
                    show n_closefromup_mouth sadbiting_Silentx02
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx01
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    n "Suelta un suspiro."

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                "Prefiero no responder a esa pregunta.":
                    call p_Help

                    $ nteye = "front00"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Talkingx10
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Pues yo s?? que quiero que me respondas!"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx04
                    call n_closefromup_tears_tears
                    with dissolve

                    menu day06_neusDidac_whereWeAre_trustSilence_question:

                        "S??, conf??o en ti.":
                            call p_Help
                            $pl.ch_pts("np", 1)

                            $ day06_neusDidac_whereWeAre_trust_Cond = "trust"

                            $ nteye = "front04"
                            show n_closefromup_mouth sad_Talkingx06
                            show n_closefromup_eyebrows sadx05
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "??Entonces por qu?? no te basta con que te diga que est??s en un lugar seguro?"

                            $ nteye = "front05"
                            show n_closefromup_mouth sadbiting_Silentx05
                            show n_closefromup_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            $ ntlong += 1

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx02
                            show n_closefromup_eyebrows sadx04
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Agradezco que intentes creer en mi,"

                            $ nteye = "right04"
                            show n_closefromup_mouth sad_Talkingx05
                            show n_closefromup_eyebrows sadx06
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "pero me duele que realmente no lo hagas."

                            $ ntlong += 1

                            $ nteye = "right05"
                            show n_closefromup_mouth sadbiting_Silentx04
                            show n_closefromup_eyebrows sadx05
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            $ nteye = "front08"
                            show n_closefromup_mouth sad_Talkingx001
                            show n_closefromup_eyebrows sadx07
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "Aaahhhhh.... *Largo suspiro*"

                            $ ntlong = 0

                            $ nteye = "front06"
                            show n_closefromup_mouth sad_Silentx04
                            show n_closefromup_eyebrows sadx02
                            call n_closefromup_tears_tears
                            with dissolve

                        "No, no conf??o en ti.":
                            call p_Help
                            
                            $ day06_neusDidac_whereWeAre_trust_Cond = "distrust"

                            if gensex_ILoveYouNeus:

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Silentx03
                                show n_closefromup_eyebrows surprisex04
                                call n_closefromup_tears_tears
                                with dissolve

                            else:

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Silentx05
                                show n_closefromup_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                            ne "..."

                            if gensex_ILoveYouNeus:
                                $pl.ch_pts("np", -6)

                                $ gensex_ILoveYouNeus = False

                                $ nteye = "front01"
                                show n_closefromup_mouth sad_Talkingx03
                                show n_closefromup_eyebrows sadx01
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Pensaba que me amabas."

                                $ nteye = "front00"
                                show n_closefromup_mouth sad_Silentx02
                                show n_closefromup_eyebrows surprisex03
                                call n_closefromup_tears_tears
                                with dissolve

                                p "Eso no tiene nada que ver."

                                $ ntlong += 1

                                $ nteye = "front02"
                                show n_closefromup_mouth sad_Talkingx11
                                show n_closefromup_eyebrows angryx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "????C??mo no va a tener nada que ver?!"

                                $ nteye = "front03"
                                show n_closefromup_mouth sad_Talkingx14
                                show n_closefromup_eyebrows angryx07
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "????Qu?? entiendes t?? por amor?!"

                                $ ntlong += 1

                                $ nteye = "front04"
                                show n_closefromup_mouth sad_Silentx09
                                show n_closefromup_eyebrows angryx05
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.2

                                $ nteye = "front05"
                                show n_closefromup_mouth sad_Silentx05
                                show n_closefromup_eyebrows angryx04
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.4

                                $ ntlong = 0

                                $ nteye = "front06"
                                show n_closefromup_mouth sadbiting_Silentx06
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                pause 0.4

                                $ nteye = "front08"
                                show n_closefromup_mouth sadbiting_Silentx04
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                            elif gensex_YoureAMonster:
                                $pl.ch_pts("np", -1)

                                $ nteye = "front02"
                                show n_closefromup_mouth sad_Talkingx04
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Me apena que pienses as??,"

                                $ nteye = "right04"
                                show n_closefromup_mouth sad_Talkingx03
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "pero supongo que no deber??a de sorprenderme..."

                                $ nteye = "right05"
                                show n_closefromup_mouth sadbiting_Silentx08
                                show n_closefromup_eyebrows sadx07
                                call n_closefromup_tears_tears
                                with dissolve

                            else:
                                $pl.ch_pts("np", -2)

                                $ nteye = "front05"
                                show n_closefromup_mouth sad_Talkingx04
                                show n_closefromup_eyebrows sadx03
                                call n_closefromup_tears_tears
                                with dissolve

                                ne "Me duele escuchar eso."

                                $ nteye = "front08"
                                show n_closefromup_mouth sadbiting_Silentx05
                                show n_closefromup_eyebrows sadx05
                                call n_closefromup_tears_tears
                                with dissolve

                            p "..."

                        "..." if day06_neusDidac_whereWeAre_trustSilence_Cond == False:

                            $ day06_neusDidac_whereWeAre_trustSilence_Cond = True

                            $ nteye = "front03"
                            show n_closefromup_mouth sad_Talkingx005
                            show n_closefromup_eyebrows angryx03
                            call n_closefromup_tears_tears
                            with dissolve

                            ne "He dicho que me respondas."

                            $ ntlong += 1

                            $ nteye = "front04"
                            show n_closefromup_mouth sad_Silentx05
                            show n_closefromup_eyebrows suspiciousx02
                            call n_closefromup_tears_tears
                            with dissolve

                            p "..."

                            $ nteye = "front05"
                            show n_closefromup_mouth sadbiting_Silentx05
                            show n_closefromup_eyebrows sadx03
                            call n_closefromup_tears_tears
                            with dissolve

                            jump day06_neusDidac_whereWeAre_trustSilence_question

                "??Por qu?? te cuesta tanto responder a una simple pregunta?":
                    call p_Help
                    $pl.ch_pts("np", -2)

                    $ day06_neusDidac_whereWeAre_trust_Cond = "doubts"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "??Por qu?? te cuesta tanto confiar en mi?"

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx03
                    show n_closefromup_eyebrows serious
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Simplemente quiero saber d??nde estamos."

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Silentx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx001
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "*Aaahhhhh....*-Largo suspiro-"

                    $ nteye = "front06"
                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

            jump day06_neusDidac_whereWeAre_city

        "Mientras estemos juntos, realmente no." if not gensex_YoureAMonster:
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nblush += 1

            if gensex_ILoveYouNeus:

                $pl.ch_pts("np", 2)

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Que cursi eres cuando quieres."

                $ nteye = "front07"
                show n_closefromup_mouth happy_Silentx05
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                p "??Oye!"

                $ nteye = "front02"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Te amo tanto."

                $ nteye = "front06"
                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            else:

                $pl.ch_pts("np", 4)

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx06
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Me alegra tanto que digas esto."

                $ nteye = "front06"
                show n_closefromup_mouth happy_Silentx05
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

            # Now comes the kisss.

        "...":
            call p_Help

            # $ nteye = "front05"
            # show n_closefromup_mouth sad_Silentx04
            # show n_closefromup_eyebrows suspiciousx02
            # call n_closefromup_tears_tears
            # with dissolve

    return
    #jump day06_neusDidac_HowAreYou

label day06_neusDidac_whereWeAre_city:

    $ ntlong = 0

    pause 0.2

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Estamos en Par??s."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "??Por qu?? aqu???"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Porque es una ciudad grande"

    $ nteye = "right04"
    show n_closefromup_mouth happy_Talkingx02
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "y tengo algunos contactos en esta ciudad."

    $ nteye = "front08"
    show n_closefromup_mouth happy_Silentx02
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "down05"
    show n_closefromup_mouth sad_Talkingx02
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Por favor,"

    if day06_neusDidac_whereWeAre_trust_Cond == "distrust":

        $ nteye = "front01"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "ya s?? que has dicho que no te f??as de mi,"

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "pero cr??eme;"

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front04"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "conf??a en mi;"

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx02
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

    ne "aqu?? estaremos a salvo."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx04
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    return
    #jump day06_neusDidac_HowAreYou