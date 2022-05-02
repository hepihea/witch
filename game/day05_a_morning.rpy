default morning05_DidacSex_Pussy_Cond = False

default morning05_DidacSex_Anal_Cond = False
default morning05_DidacSex_WasGood = False
default morning05_DidacSex_Anal_Rejected = False # Used to delete a question to avoid a loop.
default morning05_DidacSex_UsingCondom_Cond = False
default morning05_DidacSex_WrapLegs_Cond = False

default morning05_TxellCall_rejected = False

default morning05_DidacSex_Fucking_Kiss_Tongue_Done = False
default morning05_DidacSex_Fucking_Kiss_Mouth_Done = False

default morning05_DidacSex_Fucking_Kick_Cond = False


default morning05_sexwithDidacNotatHome_Cond = False

default morning05_missionary_cond_01 = False # Starting Machine
default morning05_missionary_cond_02 = False # Rubbing
default morning05_missionary_cond_03 = False # Slow Fuck
default morning05_missionary_cond_04 = False # Fast Fuck
default morning05_missionary_cond_05 = False # She Rubbing you
default morning05_missionary_cond_06 = False # She Rubbing you FAST
default morning05_missionary_cond_07 = False # Half Dick
default morning05_missionary_cond_08 = False # Raped
default morning05_missionary_cond_09 = False # Raped Fast

default morning05_missionary_face_cond_empty = False
default morning05_missionary_face_cond_surprise = False
default morning05_missionary_face_cond_malicious = False
default morning05_missionary_face_cond_horny = False



## Dídac corta el condón para quedarse preñada en el final del día 04.

## Neus solo puede enamorarse de una persona en su vida y debe ser alguien que le atraiga.
####o solo podrá procrear con su padre, un espíritu maligno que preñó a su madre que as u vez era hija también de él.

##De hehco a Neus le gusta a [protname], porque físicamente le recuerda batante a su padre inconscientemente.

##Siempre toma cafeína.

## Es una súcubo del mundo espiritual, capaz de alargar partes de su cuerpo y se alimenta básicamente de esperma y del alma de su víctima."

## Madre pacto con un diablo."

    ##############################################################################
    #############################################################################

    #if afternight04_sexbattle_started == True: #Means you accepted to have sex with Didac.

    #if afternoon04_MACBA_TxellTruth_Cond == True # Llegaste al final de la cita con Txell.
    #if afternight04_didac_pregnant == True # She is pregnant.

    #if afternight04_didac_orgasms >= 4: # If she had + than 4 orgasm.
    #elif afternight04_didac_orgasms >= 1: # If she had + than 1 orgasm.
    #elif afternight04_didac_orgasms == 0: #If she had not a single orgasm.

    #if mc_body.orgasm >= 1

    #if afternight04_LeavingSexBattle == True: #You left sex-battle at some point.

    #if afternight04_DidacisNOTatHome == True: #Didac is not in her bed.

    ####

    # If she had + than 4 orgasm.
    # If she had + than 1 orgasm.
    # if she had not a single orgasm. (Here she ignores you and she masturbates.)
    # If she is not in the room.

    ##############################################################################
    #############################################################################

label morning05:

    call night04_ped_LeaveWithoutBlowjob_label

    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx1')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx2')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx3')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx4')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx5')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx6')

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    stop music fadeout 3.0

    $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/birds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    $ saturation_tint_level = "default"

#########################################################
    
    #if config.version < "00.99.99":  ## NOT HERE.
        
        #call endupdatescript
    
#######################################################

    hide screen dummy_screen
    hide screen premium_dashboard
    if PlatinumHelp == True:
        show screen Points()

    ##############################################################################
    ############################################################################# JUST TO TEST.
    #$ night03_PedreraHome = True #Acompañas a Neus en la primera cita.

    #$ night03_MidnightProblem04_GoUp_Boolean = True #Decides subir al piso con ella.

    #$ night03_2ndDateInsidePedreraWithNeus = True #2nd Date with Neus you get inside Pedrera with her.

    #$ afternight04_sexbattle_started = True #Means you accepted to have sex with Didac.

    #$ afternight04_LeavingSexBattle = False #You left sex-battle at some point.

    ##

    #$ afternight04_didac_pregnant = False # She is pregnant.

    #$ afternight04_didac_orgasms = 2

    ##

    #$ afternight04_DidacisNOTatHome = False #Didac is not in her bed.

    #$ afternoon04_MACBA_TxellTruth_Cond = True # Llegaste al final de la cita con Txell.

    #$ mc_body.orgasm == 3

    #$ night04_Neus_Blowjob_Cum_Affirmative = True # Llegaste a correrte en la 2a cita con Neus.
            
    #$ night04_Neus_Blowjob_CumWarning_NOTWarnHer = True # Te corriste sin avisar en su boca.

    #$ night04_Neus_KissFrenchmade = True

    ##############################################################################
    #############################################################################
    
    ##Domingo
    
    scene black with fade

    window hide dissolve
    pause
    
    $ renpy.notify("Day 05")
    
    #aj "Lo que sucede a continuación es lo que ocurre si has tenido un sexo enormemente placentero con Dídac."

    #aj "Debido a que el minijuego aún no está terminado, por ahora es la única versión disponible, disculpa las molestias."

    n "Como el día anterior,"

    n "el cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."
    
    n "Pero hay otro sonido extraño que te llama la atención."

    $ renpy.music.set_volume(0.4, delay=3.0, channel='sfx1')
    
    if afternight04_didac_orgasms >= 1:

        play sound "audio/characters/didac/moanings06.ogg"
    
        #gd "*Gimoteos femeninos* Mfff... mm... ah..." 
        gd "Mfff... mm... ah..." #Strong Feminine Moans

    else:

        play sound "audio/characters/didac/moanings04.ogg"
    
        #gn "*Gimoteos femeninos* Mfff... mm... ah..." 
        gd "Mfff... mm... ah..." #Soft Feminine Moans
    
    pt "¿Otra vez el mismo sueño?"

    play music "audio/music/kevinmacleod/last_kiss_goodnight.ogg" fadein 3.0 fadeout 3.0
    
    play sound "audio/characters/didac/moanings07.ogg" 

    scene morning04_bg bedroom_neus_a
    show morning04_bedroom_Neus_body 01a: 
        morning04_bedroom_Neus_body_anim

    show morning04_bedroom_Neus_bodyass 01a:
        morning04_bedroom_Neus_bodyass_anim02

    show border_dream:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        ease 150.0 xanchor 0.0 yanchor 0.0 zoom 0.5

    show light 01:
        light01_rightside_position

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light_screen_01:
        light_screen_01_position

    with fade
    
    window hide dissolve
    pause

    n "Entreabres los ojos y te encuentras una borrosa silueta oscura justo encima de ti."

    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01b
    with Dissolve (3.0)

    if afternight04_didac_orgasms >= 1:
    
        n "Oyes ahora más claramente esa extraña voz y distingues perfectamente que se tratan de gemidos, pero esta vez no son ahogados."
    
        n "Ves que esa extraña silueta se desplaza y que además hace temblar tu cuerpo,"
    
        n "como si estuviera cabalgándote."

    show morning04_bedroom_Neus_body 01c
    show morning04_bedroom_Neus_bodyass 01b
    with Dissolve (3.0)

    pt "¿Neus otra vez...?"

    show morning04_bedroom_Neus_body 01b
    show morning04_bedroom_Neus_bodyass 01c
    with Dissolve (3.0)

    n "Con un movimiento sutil y sugerente, se vuelve hacia ti."

    play sound "audio/characters/neus/giggle03.ogg"
    
## NEUS

    hide morning04_bedroom_Neus_body 
    hide morning04_bedroom_Neus_bodyass #HIDE!!
    hide border_dream
    hide light 01
    hide white
    hide morning04_bedroom_DMast_blinkeye
    hide light_screen_01

    show border_dream:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        ease 150.0 xanchor 0.0 yanchor 0.0 zoom 0.5

    show morning04_bg bedroom_neus_a
    show morning04_bedroom_Neus_body_ass 02a:
        subpixel True
        zoom .89
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.50
        linear 1.0 xpos .52 ypos .54 zoom 1.08
        linear 3.0 xpos 0.49 ypos 0.5 zoom .89
        linear 1.0 xpos .55 ypos .54 zoom 1.05
        linear 3.0 xpos .50 ypos .50 zoom .89
        repeat
    show morning04_bedroom_Neus_body_body 02a
    show morning04_bedroom_Neus_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_mouth happy_Silentx02:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyes 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyepupils front_red_03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_eyebrows surprisex01:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_exp_glasses:
        morning04_bedroom_exp_position
    show morning04_bedroom_Neus_body_hair 02a

## DIDAC

    show morning04_bedroom_Didac_body_ass empty:
        zoom .89
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.50
        linear 1.0 xpos .52 ypos .54 zoom 1.08
        linear 3.0 xpos 0.49 ypos 0.5 zoom .89
        linear 1.0 xpos .55 ypos .54 zoom 1.05
        linear 3.0 xpos .50 ypos .50 zoom .89
        repeat
    show morning04_bedroom_Didac_body_body empty
    show morning04_bedroom_Didac_exp_mouth empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair empty

## TXELL

    show morning04_bedroom_Txell_body_ass empty:
        zoom .89
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.50
        linear 1.0 xpos .52 ypos .54 zoom 1.08
        linear 3.0 xpos 0.49 ypos 0.5 zoom .89
        linear 1.0 xpos .55 ypos .54 zoom 1.05
        linear 3.0 xpos .50 ypos .50 zoom .89
        repeat
    show morning04_bedroom_Txell_body_body empty
    show morning04_bedroom_Txell_exp_mouth empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Txell_exp_eyes empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Txell_exp_eyepupils empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Txell_exp_eyebrows empty:
        morning04_bedroom_exp_position
    show morning04_bedroom_Txell_body_hair empty

    show light 01:
        light01_rightside_position

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    #show morning04_bedroom_DMast_blinkeye

    show light_screen_01:
        light_screen_01_position

    with fade

    window hide dissolve
    pause

    pt "¿Por qué tiene los ojos rojos?"

    ##

    show morning04_bedroom_Neus_body_ass 02b
    show morning04_bedroom_Neus_body_body 02b
    show morning04_bedroom_Neus_body_hair 02b
    show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
    show morning04_bedroom_Neus_exp_eyebrows surprisex01
    with Dissolve (1.0)

    if night03_PedreraHome == True: #Acompañas a Neus en la primera cita.

        ne "Fuiste todo un caballero al acompañarme a casa con la cogorza que llevaba..."

        show morning04_bedroom_Neus_exp_eyebrows normal
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        pt "¿Cogorza?"

        extend " Se me hace raro oír esa expresión en Neus..."

        if night03_MidnightProblem04_GoUp_Boolean == True: #Decides subir al piso con ella.

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "Me acompañaste hasta entrar en el piso..."

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
            with dissolve

            ne "¿Qué intenciones llevabas?"

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "¿Acaso pretendías abusar de una chica con un pedo como un piano?"

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            p "Neus,"

            extend " eres tú la que..."

    if night03_2ndDateInsidePedreraWithNeus == True: #2nd Date with Neus in Pedrera.

        if night04_Neus_KissFrenchmade == True:

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "Y en la segunda cita no solo me acompañaste..."

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
            with dissolve

            ne "Sino que vaya beso de torniquete diste..."

        else:

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "Y en la segunda cita me volviste a acompañar..."

        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        p "Ahí no estabas borracha..."

        show morning04_bedroom_Neus_exp_eyebrows normal
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        with dissolve

        ne "Eso quizás es verdad..."

        if night04_Neus_Blowjob_Cum_Affirmative == True:

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
            with dissolve

            ne "Aunque luego no desaprovechaste la oportunidad de llevar la noche un poco más lejos..."

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            with dissolve

            ne "pero seguro que te habría gustado algo más que una simple limpieza de sable..."

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            pt "Me pareció de todo menos simple..."

            pt "¿Y desde cuándo Neus habla de este modo?"
                
            if night04_Neus_Blowjob_CumWarning_NOTWarnHer == True:

                show morning04_bedroom_Neus_exp_eyebrows surprisex01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "Al final te corriste en la boca sin avisar..."

                show morning04_bedroom_Neus_exp_eyebrows angryx02
                show morning04_bedroom_Neus_exp_mouth happy_Silentx02
                with dissolve

                p "..."

                show morning04_bedroom_Neus_exp_eyebrows surprisex01
                with dissolve

                p "No pareció que te disgustara el resultado..."

                show morning04_bedroom_Neus_exp_eyebrows angryx02
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                ne "No te haces una idea..."

            else:

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "Al final avisaste antes de correrte en la boca..."

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx02
                with dissolve

                p "..."

                show morning04_bedroom_Neus_exp_eyebrows normal
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                ne "Todo un caballero..."

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            p "¿Qué diablos ocurrió esa noche?"

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
            with dissolve

            ne "¿Me lo preguntas a mí?"

            ne "¿O a ti mismo?"

            show morning04_bedroom_Neus_exp_eyebrows angryx02
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            pt "Si esto es un sueño,"

            pt "realmente no hallaré una respuesta..."

        else: #Acompañaste a Neus 2a cita, pero no disfrutaste de su mamada.



            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "Y después de toda esa parafernalia para mojar el churro,"

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "resulta que al final te vas perdiendo la oportunidad de haber conseguido algo más con ella..."

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            pt "¿Con ella?"

            pt "¿Ahora me habla como si no fuera Neus quien habla?"

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve

            p "¡Fuiste tú quien me insistió en que no era el momento ni el lugar!"

            if night04_Neus_DoILeave_AngryFail == True:

                show morning04_bedroom_Neus_exp_eyebrows normal
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "Deberías saber mejor cómo funciona la psique de las mujeres, [protname]."

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "A veces lo más sabio,"

                extend " es usar la psicología inversa..."

                show morning04_bedroom_Neus_exp_eyebrows surprisex01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "Si te hubieras largado mostrando enfado,"

                ne "¿crees que Neus te hubiera dejado marchar sin más?"

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx02
                with dissolve

            else:

                show morning04_bedroom_Neus_exp_eyebrows sadx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                with dissolve

                ne "Aunque ayer te fueras mostrando enfado,"

                extend " parece que aún no se ha rendido a tus encantos..."

                show morning04_bedroom_Neus_exp_eyebrows sadx02
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx03
                with dissolve

                ne "¿Por qué será...?"

                show morning04_bedroom_Neus_exp_eyebrows suspiciousx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx02
                with dissolve

            p "..."

            show morning04_bedroom_Neus_exp_eyebrows angryx02
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
            with dissolve

            ne "Te tomaba por alguien algo más inteligente..."

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth happy_Silentx02
            with dissolve



    else:

        ## $ night03_2ndDateInsidePedreraWithNeus = True # If you get inside Pedrera. NOT_FINISHED
        ## n "Si el exterior del edificio ya es de por sí realmente hermoso."
        # There should be another conditional for if you acompanied her to there, but not get into the Pedrera.

        if not night03_PedreraHome: 

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
            with dissolve

            ne "En la primera cita,"

            show morning04_bedroom_Neus_exp_eyebrows surprisex01
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
            with dissolve

            ne "no acompañaste a Neus a su casa."

        show morning04_bedroom_Neus_exp_eyebrows angryx01
        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        with dissolve

        ne "¿No te preguntas cómo hubieran ido las cosas si las hubieras hecho de forma distinta?"

        show morning04_bedroom_Neus_exp_eyebrows angryx02
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        p "..."

        pt "¿Por qué habla de ella en tercera persona...?"

        p "Si me tuviera que arrepentir de algo,"

        extend " me arrepentiría de todo."

        p "De todas mis malas notas,"

        extend " de todos mis malos polvos,"

        extend " de todos mis malos rollos,"

        extend " de todos mis fracasos."

        p "Pero si tuviera que vivir del pasado,"

        extend " jamás miraría el presente,"

        p "que es donde estoy ahora."

        show morning04_bedroom_Neus_exp_eyebrows angryx02
        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        with dissolve

        ne "No me vengas con gilipolleces de poeta fracasado."

        show morning04_bedroom_Neus_exp_eyebrows angryx01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        p "..."

        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        with dissolve

        ne "Aun así esta noche tendrás una tercera cita con ella..."

        show morning04_bedroom_Neus_exp_eyebrows angryx01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        p "Sí..."

        show morning04_bedroom_Neus_exp_eyebrows normal
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        pt "¿Ella...?"

    if ((afternight04_DidacisNOTatHome == False
        and afternight04_didac_pregnantRapeOkupa == False)
        or  afternoon04_MACBA_TxellTruth_Cond == True):

        show morning04_bedroom_Neus_exp_eyebrows normal
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        with dissolve

        ne "Picarón..."

        extend " picarón..."

        show morning04_bedroom_Neus_exp_eyebrows angryx01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx03
        with dissolve

        pt "Su voz..."

        extend " es extraña..."

        if (afternight04_sexbattle_started == True
            and afternoon04_MACBA_TxellTruth_Cond == True):

            show morning04_bedroom_Neus_exp_eyebrows angryx02
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
            with dissolve

            ne "Jugando a tres bandas..."
        else:

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
            with dissolve

            ne "Jugando a dos bandas..."

        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        show morning04_bedroom_Neus_exp_mouth happy_Silentx02
        with dissolve

        p "¿Qué?"

        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        p "¿A qué te refieres?"

        show morning04_bedroom_Neus_exp_eyebrows sadx01
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        with dissolve

        ne "Oh,"

        extend " venga,"

        ne "no te hagas el inocente..."

        show morning04_bedroom_Neus_exp_eyebrows sadx02
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        with dissolve

        ne "¿Para qué conformarse con una insípida morena de pechos planos,"

        if afternight04_sexbattle_started == True and afternoon04_MACBA_TxellTruth_Cond == True:

            show morning04_bedroom_Neus_exp_eyebrows angryx02
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx04
            with dissolve

            ne "cuando puedes tener a dos más por el mismo precio..."

        else:

            show morning04_bedroom_Neus_exp_eyebrows angryx01
            show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
            with dissolve

            ne "cuando podrías tener a dos más por el mismo precio..."

            show morning04_bedroom_Neus_exp_eyebrows angryx02
            show morning04_bedroom_Neus_exp_mouth happy_Silentx03
            with dissolve

            p "¿Dos?"

            if afternoon04_TxellMacbaDate == False: #You didn´t have date with Txell.

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                with dissolve

                ne "Te ofrecí el número de esa rubia despampanante y ni siquiera te dignaste a llamarla."

                show morning04_bedroom_Neus_exp_eyebrows sadx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx02
                with dissolve

                p "¡¿Qué?!"

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                with dissolve

                ne "Me avergüenzas..."

                show morning04_bedroom_Neus_exp_eyebrows normal
                show morning04_bedroom_Neus_exp_mouth sad_Silentx02
                with dissolve

                p "¡¿Me ofreciste?!"

            else:

                show morning04_bedroom_Neus_exp_eyebrows surprisex01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                with dissolve

                ne "Por lo visto esa rubia despampanante es demasiado mujer para ti."

                show morning04_bedroom_Neus_exp_eyebrows normal
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "Reconozco que es una mujer de armas tomar y algo pesada con las preguntitas..."

                show morning04_bedroom_Neus_exp_eyebrows angryx02
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                ne "¿Pero acaso no es más satisfactorio cuando la dificultad de conquistar y someter es mayor?"

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx03
                with dissolve

                p "..."

                p "¿Sigo hablando con Neus?"

                show morning04_bedroom_Neus_exp_eyebrows normal
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "¿Me lo preguntas a mí?"

                show morning04_bedroom_Neus_exp_eyebrows angryx02
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                ne "¿O te lo preguntas a ti mismo?"

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Silentx03
                with dissolve

                p "..."

            if afternight04_sexbattle_started == False: #You did not have sex with DIDAC.

                if morning04_DidacHotforyou_Cond == True:

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "Te meneas la polla cuando la oyes gemir al masturbarse,"

                if aftermorning04_FittingRoom_ButtocksDickOver == True:

                    show morning04_bedroom_Neus_exp_eyebrows surprisex01
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                    with dissolve

                    ne "le bajas los pantalones para meter tu polla desnuda sobre sus nalgas,"

                if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True:

                    show morning04_bedroom_Neus_exp_eyebrows angryx01
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "le bajas los pantalones y usas sus nalgas para masturbarte con ellas,"

                if aftermorning04_FittingRoom_FuckherConsent == True: #Penetración sin lubricación

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "si no llega a ser por la dependienta y su grito,"

                    ne "te la hubieras follado sin condón,"

                if morning04_Shopping_didaccum_Cond == True: #Didac Cum with your fingers.

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "le metiste el dedo hasta el fondo hasta que se corrió en tu mano,"

                if morning04_Shopping_didaccumANAL_Cond == True: #Didac cum, but only for anal.

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "le metiste el dedo en el culo hasta el fondo hasta que se corrió,"

                if morning04_Shopping_youcum_Cond == True: # You cum on ground.

                    show morning04_bedroom_Neus_exp_eyebrows normal
                    show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
                    with dissolve

                    ne "te me corriste en su mano mientras le estabas metiendo el dedo,"

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
                with dissolve

                ne "y encima tuviste las narices de decirle que, como eres su amigo,"

                ne "jamás te lo follarías..."

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth sad_Silentx01
                with dissolve

                p "..."

        if afternight04_sexbattle_started == True or afternoon04_MACBA_TxellTruth_Cond == True:

            show morning04_bedroom_Neus_exp_eyebrows normal
            show morning04_bedroom_Neus_exp_mouth sad_Talkingx002
            with dissolve

            ne "Me decepcionas, [protname]..."

        if afternight04_sexbattle_started == True:

            if afternoon04_MACBA_TxellTruth_Cond == True:

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                d "Tu compañero de piso,"

                extend " por ejemplo..."

            else:

                show morning04_bedroom_Neus_exp_eyebrows angryx01
                show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
                with dissolve

                d "Tu amigo de la infancia y compañero de piso..."

            play sound "audio/characters/neus/giggle03.ogg"

            play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
            
        ## NEUS

            show morning04_bedroom_Neus_body_ass empty
            show morning04_bedroom_Neus_body_body empty
            show morning04_bedroom_Neus_exp_blush empty
            show morning04_bedroom_Neus_exp_mouth empty
            show morning04_bedroom_Neus_exp_eyes empty
            show morning04_bedroom_Neus_exp_eyepupils empty
            show morning04_bedroom_Neus_exp_eyebrows empty
            show morning04_bedroom_Neus_exp_glasses empty
            show morning04_bedroom_Neus_body_hair empty

        ## DIDAC

            show morning04_bedroom_Didac_body_ass 02c
            show morning04_bedroom_Didac_body_body 02c
            show morning04_bedroom_Didac_exp_mouth happy_Silentx02
            show morning04_bedroom_Didac_exp_eyes 04
            show morning04_bedroom_Didac_exp_eyepupils front_red_04
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            show morning04_bedroom_Didac_body_hair 02c

        ## TXELL

            show morning04_bedroom_Txell_body_ass empty
            show morning04_bedroom_Txell_body_body empty
            show morning04_bedroom_Txell_exp_mouth empty
            show morning04_bedroom_Txell_exp_eyes empty
            show morning04_bedroom_Txell_exp_eyepupils empty
            show morning04_bedroom_Txell_exp_eyebrows empty
            show morning04_bedroom_Txell_body_hair empty

            with Dissolve (3.0)

            pt "¡Coño!"

            n "Como si de una aparición se tratara, el cuerpo delicado de Neus se transforma en el atlético y musculoso cuerpo de Dídac, así como su rostro."

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
            show morning04_bedroom_Didac_exp_eyebrows surprisex01
            with dissolve

            d "No todo el mundo puede disfrutar de semejante compañía femenina en su propio hogar..."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
            show morning04_bedroom_Didac_exp_eyebrows serious
            with dissolve

            d "Después de tantos años compartiendo clases,"

            d "amistades,"

            extend " piso,"

            extend " recuerdos,"

            extend " noches de farra,"

            extend " ligoteos..."

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
            show morning04_bedroom_Didac_exp_eyebrows sadx01
            with dissolve

            d "¿No se te hace extraño meterle la polla en su recién estrenado coño a tu mejor camarada?"

            show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx02
            show morning04_bedroom_Didac_exp_eyebrows normal
            with dissolve

            p "..."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx01
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "¿Demasiada tentación?"

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
            show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
            with dissolve

            d "O quizás es que realmente te importa bien poco lo que le pase..."

            if afternight04_Pussy_dick_deep_Speed_1_Done > 0:

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows normal
                with dissolve

                d "Al fin y al cabo, ayer se la metiste hasta el fondo,"

                if afternight04_Pussy_dick_deep_Speed_1_Failed > afternight04_Pussy_dick_deep_Speed_1_Success:

                    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
                    show morning04_bedroom_Didac_exp_eyebrows angryx01
                    with dissolve

                    d "aunque no parece que le encantara demasiado..."

            if afternight04_Anal_dick_deep_Speed_0_Done > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
                show morning04_bedroom_Didac_exp_eyebrows surprisex02
                with dissolve

                d "hasta le reventaste el ano metiéndole el pollón que gastas enterito..."

            elif afternight04_Anal_dick_med_Speed_1_Done > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
                show morning04_bedroom_Didac_exp_eyebrows normal
                with dissolve


                d "hasta le reventaste el ano con el pedazo de pollón que gastas,"

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "y eso que no se lo metiste entero..."

            if afternight04_Anal_dick_med_Speed_1_Done > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows surprisex01
                with dissolve

                d "Eso también se lo podías haber hecho antes de que se convirtiera en mujer..."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows sadx01
                with dissolve

                d "Pero quizás no apetecía tanto,"

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "¿verdad?"

            if afternight04__MMouth_Tongue_Success > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
                with dissolve

                d "Lo que no me esperaba es que le convencieras para morrearos,"

                if afternight04__MMouth_Tongue_Deep_Success > 0:

                    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
                    show morning04_bedroom_Didac_exp_eyebrows normal
                    with dissolve

                    d "mucho menos que te dejara meterle la lengua..."


                show morning04_bedroom_Didac_exp_mouth sad_Talkingx001
                show morning04_bedroom_Didac_exp_eyebrows surprisex01
                with dissolve

                d "Gaaaaay..."

                show morning04_bedroom_Didac_exp_mouth happy_Silentx05
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                p "..."
            
            if afternight04__MMouth_dick_Deep_Success > 0:

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "Sin mencionar que se la has metido casi entera en la garganta..."

            elif afternight04__MMouth_dick_Success > 0:

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "Sin mencionar que has conseguido que aceptara tenerla en su boca..."

            if afternight04_CumInThroat > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "Aunque lo de correrte ahí con la posibilidad de ahogarla..."

            elif afternight04_CumInMouth > 0:

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "Aunque lo de correrte en su boca..."

            if ((afternight04_CumInThroat) or (afternight04_CumInMouth)) > 0 :

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
                show morning04_bedroom_Didac_exp_eyebrows surprisex02
                with dissolve

                d "Hasta me siento orgulloso de ti y todo."

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "Estás hecho todo un {b}cabronazo{/b}..."

            show morning04_bedroom_Didac_exp_mouth happy_Silentx04
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            pt "Si esto es mi subconsciente,"

            pt "realmente soy muy retorcido..."

        if afternoon04_MACBA_TxellTruth_Cond == True:

            play sound "audio/characters/neus/giggle03.ogg"
            play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
            
        ## NEUS

            show morning04_bedroom_Neus_body_ass empty
            show morning04_bedroom_Neus_body_body empty
            show morning04_bedroom_Neus_exp_blush empty
            show morning04_bedroom_Neus_exp_mouth empty
            show morning04_bedroom_Neus_exp_eyes empty
            show morning04_bedroom_Neus_exp_eyepupils empty
            show morning04_bedroom_Neus_exp_eyebrows empty
            show morning04_bedroom_Neus_exp_glasses empty
            show morning04_bedroom_Neus_body_hair empty

        ## DIDAC

            show morning04_bedroom_Didac_body_ass empty
            show morning04_bedroom_Didac_body_body empty
            show morning04_bedroom_Didac_exp_mouth empty
            show morning04_bedroom_Didac_exp_eyes empty
            show morning04_bedroom_Didac_exp_eyepupils empty
            show morning04_bedroom_Didac_exp_eyebrows empty
            show morning04_bedroom_Didac_body_hair empty

        ## TXELL

            show morning04_bedroom_Txell_body_ass 02c
            show morning04_bedroom_Txell_body_body 02c
            show morning04_bedroom_Txell_exp_mouth happy_Talkingx02
            show morning04_bedroom_Txell_exp_eyes 04
            show morning04_bedroom_Txell_exp_eyepupils front_red_04
            show morning04_bedroom_Txell_exp_eyebrows surprisex01
            show morning04_bedroom_Txell_body_hair 02c

            with Dissolve (3.0)

            tx "Por no hablar de la rubia tetuda..."


            show morning04_bedroom_Txell_exp_mouth happy_Silentx02
            show morning04_bedroom_Txell_exp_eyebrows serious
            with dissolve

            pt "¡¿Otra vez cambia?!"


            show morning04_bedroom_Txell_exp_mouth happy_Silentx03
            show morning04_bedroom_Txell_exp_eyebrows normal
            with dissolve

            n "Sus pechos aumentan de tamaño, su pelo se aclara hasta volverse rubio claro, pero sus ojos permanecen rojos."

            show morning04_bedroom_Txell_exp_mouth happy_Talkingx01
            show morning04_bedroom_Txell_exp_eyebrows surprisex02
            with dissolve

            tx "¿Cómo dejar pasar semejante oportunidad...?"

            show morning04_bedroom_Txell_exp_mouth happy_Talkingx02
            show morning04_bedroom_Txell_exp_eyebrows angryx01
            with dissolve

            tx "Aunque parece que esta no te lo está poniendo tan fácil..."

            show morning04_bedroom_Txell_exp_mouth happy_Talkingx03
            show morning04_bedroom_Txell_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Verdad?"

            show morning04_bedroom_Txell_exp_mouth happy_Silentx04
            show morning04_bedroom_Txell_exp_eyebrows serious
            with dissolve

            pt "Tiene el mismo color de ojos que cuando la conocí..."

            show morning04_bedroom_Txell_exp_mouth happy_Silentx05
            show morning04_bedroom_Txell_exp_eyebrows angryx01
            with dissolve

            pt "¡¿Qué diablos estoy soñando?!"

            show morning04_bedroom_Txell_exp_mouth happy_Talkingx02
            show morning04_bedroom_Txell_exp_eyebrows angryx02
            with dissolve

            tx "Puedes mentir a los demás,"

            extend " pero no a mí..."

            show morning04_bedroom_Txell_exp_mouth sad_Talkingx002
            show morning04_bedroom_Txell_exp_eyebrows normal
            with dissolve

            tx "Es normal que la lujuria te corroiga,"

            extend " por tus venas corre mi sangre."

            show morning04_bedroom_Txell_exp_mouth happy_Silentx04
            show morning04_bedroom_Txell_exp_eyebrows angryx02
            with dissolve

            p "¿Qué?"

    ## NEUS

        show morning04_bedroom_Neus_body_ass 02c
        show morning04_bedroom_Neus_body_body 02c
        show morning04_bedroom_Neus_exp_blush empty
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        show morning04_bedroom_Neus_exp_eyes 03
        show morning04_bedroom_Neus_exp_eyepupils front_red_03
        show morning04_bedroom_Neus_exp_eyebrows serious
        show morning04_bedroom_Neus_exp_glasses
        show morning04_bedroom_Neus_body_hair 02c

    ## DIDAC

        show morning04_bedroom_Didac_body_ass empty
        show morning04_bedroom_Didac_body_body empty
        show morning04_bedroom_Didac_exp_mouth empty
        show morning04_bedroom_Didac_exp_eyes empty
        show morning04_bedroom_Didac_exp_eyepupils empty
        show morning04_bedroom_Didac_exp_eyebrows empty
        show morning04_bedroom_Didac_body_hair empty

    ## TXELL

        show morning04_bedroom_Txell_body_ass empty
        show morning04_bedroom_Txell_body_body empty
        show morning04_bedroom_Txell_exp_mouth empty
        show morning04_bedroom_Txell_exp_eyes empty
        show morning04_bedroom_Txell_exp_eyepupils empty
        show morning04_bedroom_Txell_exp_eyebrows empty
        show morning04_bedroom_Txell_body_hair empty

        with Dissolve (3.0)

        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0

        dad "Dime..."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        dad "¿Le contarás todo esto a la preciosa e inocente Neus?"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx04
        show morning04_bedroom_Neus_exp_eyepupils front_goat_03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        show morning04_bedroom_Neus_exp_eyepupils front_red_03
        with Dissolve (0.75)

        p "¿Y esta voz?"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx003
        show morning04_bedroom_Neus_exp_eyebrows suspiciousx01
        with dissolve

        dad "¿Estás seguro de hacerlo?"

        dad "Quizás no se lo tome demasiado bien..."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        with dissolve

        dad "Al fin y al cabo,"

        dad "ojos que no ven..."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows serious
        with dissolve

        dad "¿Para qué conformarse con alguien que te pide amor eterno?"

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        dad "Especialmente después de usar el chantaje para llegar hasta ti."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx04
        show morning04_bedroom_Neus_exp_eyebrows angryx03
        with dissolve

        dad "Y más cuando puedes tener el mundo a tus pies..."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx04
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        dad "No seas otra hormiga en esta sociedad."

        show morning04_bedroom_Neus_exp_mouth happy_Silentx03
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve
        
        pt "¿Hormiga?"

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        dad "Abraza la libertad que tienes delante,"

        extend " y juzga tus acciones por ti mismo."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        dad "Y para que luego no me digas que no te lo advertí,"

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx04
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        dad "de inocente,"

        extend " Neus tiene bien poco..."

        show morning04_bedroom_Neus_exp_mouth happy_Silentx04
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        pt "¡¿Qué?!"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx05
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        pt "¿De qué está hablando?"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx06
        show morning04_bedroom_Neus_exp_eyepupils front_goat_03
        show morning04_bedroom_Neus_exp_eyebrows angryx03
        with dissolve

        show morning04_bedroom_Neus_exp_eyepupils front_red_03
        with Dissolve (0.75)

        pt "¿Realmente estoy hablando con mi subconsciente?"

        show morning04_bedroom_Neus_exp_eyepupils front_goat_03
        with Dissolve(0.75)

        stop music fadeout 3.0

        pause 0.25

        scene black
        with fade

        p "..."

    else: #if afternight04_DidacisNOTatHome == False or afternoon04_MACBA_TxellTruth_Cond == True:

        show morning04_bedroom_Neus_exp_blush 03
        show morning04_bedroom_Neus_exp_mouth sad_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows normal
        with dissolve

        ne "¿Te conformas con una insípida morena de pechos planos?"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        with dissolve

        ne "Pudiendo haber tenido al bellezón en que se ha convertido tu compañero de piso,"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows surprisex02
        with dissolve


        ne "y a la despampanante rubia que te ofrecí en bandeja..."

        show morning04_bedroom_Neus_exp_mouth sad_Silentx01
        show morning04_bedroom_Neus_exp_eyebrows normal
        with dissolve

        p "¿Que me ofreciste en bandeja?"

        p "¡¿De qué estás hablando?!"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows surprisex02
        with dissolve

        ne "Bueno,"

        extend " reconozco que quizás hubiera sido una presa algo más complicada de conseguir"

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows serious
        with dissolve

        ne "que la ninfómana en que se ha convertido tu compañero de piso..."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows sadx01
        with dissolve

        ne "Pero aun así..."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows sadx02
        with dissolve

        ne "Qué desperdicio..."

        ###

        show morning04_bedroom_Neus_exp_blush empty
        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with Dissolve (2.0)

        dad "Manteniéndote fiel a la preciosa e inocente Neus,"

        extend " ¿verdad?"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        p "¿Y esta voz?"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows normal
        with dissolve

        dad "¿Estás seguro de hacerlo?"

        dad "Quizás no es lo que realmente crees..."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx001
        show morning04_bedroom_Neus_exp_eyebrows surprisex01
        with dissolve

        dad "Al fin y al cabo,"
        
        extend " ojos que no ven..."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        dad "¿Para qué conformarse con alguien que te pide amor eterno?"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx02
        show morning04_bedroom_Neus_exp_eyebrows serious
        with dissolve

        dad "Especialmente después de usar el chantaje para llegar hasta ti."

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        dad "Y más cuando puedes tener el mundo a tus pies..."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        dad "No seas hormiga en esta sociedad."

        show morning04_bedroom_Neus_exp_mouth happy_Silentx03
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve
        
        pt "¿Hormiga?"

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx04
        show morning04_bedroom_Neus_exp_eyebrows serious
        with dissolve

        dad "Abraza la libertad que tienes delante y juzga tus acciones por ti mismo."

        show morning04_bedroom_Neus_exp_mouth sad_Talkingx01
        show morning04_bedroom_Neus_exp_eyebrows normal
        with dissolve

        dad "Y para que luego me digas que no te lo advertí,"

        show morning04_bedroom_Neus_exp_mouth happy_Talkingx03
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        dad "de inocente,"

        extend " Neus tiene bien poco..."

        show morning04_bedroom_Neus_exp_mouth happy_Silentx03
        show morning04_bedroom_Neus_exp_eyebrows angryx01
        with dissolve

        pt "¡¿Qué?!"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx04
        show morning04_bedroom_Neus_exp_eyebrows angryx02
        with dissolve

        pt "¿De qué está hablando?"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx05
        show morning04_bedroom_Neus_exp_eyebrows angryx03
        with dissolve

        pt "¿Realmente estoy hablando con mi subconsciente?"

        show morning04_bedroom_Neus_exp_mouth happy_Silentx06
        show morning04_bedroom_Neus_exp_eyebrows angryx03
        with dissolve

        p "..."

        stop music fadeout 3.0

        scene black
        with fade

#####


    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == True:

        $ debug ("#Impides que Fumetas le folle el culo sin condón.")

    if afternight04_Park_DidacFuckAnal_Cond == True: 

        $ debug ("# Fumetas Follando a Dídac sin condón en el culo.")

    if afternight04_Park_DidacFuckWithoutCondom_Aborted_Cond == True: 

        $ debug ("#Has impedido que se quede preñada por el Okupa, cosa que te agradece.")

    if afternight04_Park_DidacFuckWithoutCondom_Pregnant == True:

        $ debug ("No impides que se quede preñada por el Okupa.")

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant == True:

        $ debug ("#Te largas de la escena sin pelear, Dídac queda preñada. Dídac queda preñada sin que lo veas.")

    if DidacMCPregnant == True:

        $ debug ("Didac is pregnant by you")

    if afternight04_Park_HelpDidacPolice_Cond == True: 

        $ debug ("Después de quedarse preñado, ayudas a Dídac a salir de ahí, sin que este se lo tome demasiado bien el hecho de que hubieras estado observándole sin haber hecho nada.")

    if afternight04_Park_Battle_Punch_GetBackHomewithDidac_Cond == True: 

        $ debug ("#You get back home with Didac after a fight.")

    if afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True: 

        $ debug ("#You don´t get back home with Didac, They changed place. You were punched on the face.")

#####


    if (afternight04_DidacisNOTatHome or 
        afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or 
        afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond or 
        afternight04_Park_DidacFuckWithoutCondom_Pregnant or 
        afternight04_didac_pregnantRapeOkupa or 
        afternight04_Park_HelpDidacPolice_Cond):

            $ morning05_sexwithDidacNotatHome_Cond = True

            jump morning05_sexwithDidacNotatHome

    #elif afternight04_didac_orgasms >= 1:
    elif (girl_1.orgasm or afternight04_didac_orgasms) >= 1 :
        jump morning05_sexwithDidacYES

    else:
        jump morning05_sexwithDidacNO

##
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
## ##########################################################################################
##


label morning05_sexwithDidacNotatHome: #Didac is not at home.

    n "En la absoluta oscuridad a causa de tus párpados, el leve canto de los pájaros es lo primero que vuelves a escuchar."

    pt "¿Sigo soñando?"

    pt "Por lo menos ya no se oye ningún gemido..."

    scene morning04_bg bedroom_neus_a

    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position

    n "Entreabres los ojos para deleitarte con la misma visión rutinaria de tu habitación de buena mañana."

    show morning04_bg bedroom_neus_b
    with dissolve

    n "Volteas la cabeza para ver si -como de costumbre-, tu compañero de piso sigue en cama durmiendo."

    scene beds_morning_lightOff_blindUp_DemptyMCbusy
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with fade

    p "¡Maldita seas Dídac!"

    p "¡¿Dónde cojones has pasado la noche?!"

    scene morning04_bg bedroom_neus_a
    show morning04_bg_livingroom_mc_resting_phone home_message:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Instintivamente coges el móvil que hay encima de la mesita de noche para revisar si tienes alguna llamada perdida o mensaje."

    show morning04_bg_livingroom_mc_resting_phone add_01
    with dissolve

    n "Lo único que encuentras ahí es un {i}SMS{/i} de tu compañía telefónica promocionando una oferta \"irrechazable\"."

    scene morning04_bg bedroom_neus_c
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with dissolve

    p "..."

    if afternight04_didac_pregnantRapeOkupa  == True:

        p "Después de que lo rescatara de la policía,"

        extend " parece ser que no volvió a casa."

        p "Supongo que quedarse preñada de un {b}yonki{/b},"

        p "con la posibilidad de que no vuelva a ser nunca más un hombre,"

        p "debe de ser algo difícil de digerir..."

        p "me imagino que yo hubiera reaccionado igual..."

        p "..."

        p "Mierda..."

        extend " quizás me pasé de la raya..."

        p "Si Neus me dijo la verdad,"

        extend " nunca volveré a ver a mi antiguo compañero de piso..."


    scene morning04_bg bedroom_neus_a
    show morning04_bg_livingroom_mc_resting_phone didac:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with dissolve
    p "¡¿Qué narices se supone que tengo que hacer ahora?!"

    menu morning05_sexwithDidacNotatHome_CallPhone_question:
        
        pt "¿Debería llamarle?"
        
        "<Llamarle o enviarle un mensaje>":
            
            call p_Help

            $pl.ch_pts("dp",1)

            show morning04_bg_livingroom_mc_resting_phone didac_calling
            with dissolve

            p "Mierda..."

            p "Como era de imaginar,"

            extend " no responde."

            show morning04_bg_livingroom_mc_resting_phone whatsapp_01
            with dissolve

            p "Le he enviado varios mensajes por {i}WhatsApp{/i},"

            p "pero tampoco parece que reciba el mensaje..."

            show morning04_bg_livingroom_mc_resting_phone home
            with dissolve

            p "¿Debería ir a buscarlo?"

            scene morning04_bg bedroom_neus_c
            show light 01:
                light01_rightside_position
            show light_screen_01:
                light_screen_01_position
            with dissolve

            p "..."

            p "Pero ¡¿dónde?!"

            if afternight04_Park_LookingForDidac_yes_Cond == False:

                p "¡No puedo ir a la policía y preguntar por él!"

                p "{i}Oiga,"

                extend " señor policía,{/i}"

                p "{i}¿ha visto usted a mi compañero de piso?{/i}"

                p "{i}Sí,"

                extend " verá,{/i}"

                p "{i}resulta que ahora es más bajito,"

                extend " tiene cara afeminada,"

                extend " y dos tetas.{/i}"

                p "Tampoco puedo buscarlo por su nombre."

                p "No será tan inútil de dar su nombre real siendo ahora una mujer..."

                p "De hecho, si acabó en una oficina de policía e hizo eso,"

                p "por lo que me comentó Neus ahora estará..."

                p "..."

            p "¡Mierda!"

            p "Ir a buscarle por la ciudad sería una completa pérdida de tiempo..."

            p "¡Al fin y al cabo él se lo ha buscado, maldita sea!"

            p "Solo espero que siga vivo..."

            p "..."

            p "Lo mejor que puedo hacer ahora es tomarme una ducha y esperar que me responda en algún momento..."

            $ renpy.music.stop(channel='sfx1', fadeout=3.0)

            scene afternight03_bg shower
            with fade

            pause

            jump morning05_AfterDidac

        "<Sudar de él>":
            
            call p_Help
            $pl.ch_pts("dp",-3)

            p "Que le den."

            p "Al fin y al cabo él se lo ha buscado,"

            p "no será porque no ha tenido oportunidades..."

            jump morning05_AfterDidac


    aj "This text should not be visible... :P 9238"



label morning05_sexwithDidacNO: #She is masturbating.

    pt "Vaya sueño más raro..."

#########################################################
    
    if config.version < "00.10.02": # Waking up on 5th day Morning.
        
        call endupdatescript
    
#######################################################

    play sound "audio/characters/didac/moanings06.ogg"

    #gd "*Gimoteos femeninos* Mfff... mm... ah..."
    gd "Mfff-mm... ah..." # Feminine Moans

    pt "¡¿Otra vez lo mismo?!"

    play sound "audio/characters/didac/moanings06.ogg"

    scene morning04_bg bedroom_neus_a
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0
    with fade

    #gd "*Gimoteos femeninos* MMMmff..."
    gd "MMMmff..." # Feminine Moans

    show morning04_bg bedroom_neus_c
    with dissolve

    pt "Es el mismo gimoteo que escuché ayer y proviene del mismo lugar..."

    scene morning04_bedroom_DMast_move_02: # When Didac Is Facing you.
        subpixel True
        #xpos -0.0 ypos -3.25 zoom 1.3 #inicio
        xanchor 0.0 yanchor 2.0 zoom 1.3 # Inicio?
        easein_quad 30.0 xanchor 0.7 yanchor 1.6 zoom 0.7 #Middle image
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Con suma sutileza, tuerces la cabeza para comprobar si tu sospecha es acertada."

    n "Exactamente la misma situación que el día anterior."

    n "Desnuda y retorcida, acariciándose el clítoris con sus dedos mientras gime con un placer incontrolable."

    show morning04_bedroom_DMast_move_02:
        subpixel True
        easein_quad 15.0 xanchor 1.8 yanchor 1.6 zoom 1.0 #Face?

    n "Su cuerpo sigue siendo el de una hermosa y tonificada mujer con unos pechos voluptuosos."

    pt "¡¿Me está mirando?!"

    n "Su rostro no muestra ningún tipo de simpatía."

    scene morning04_bg_bedroom_youleaving 01
    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_naked_wet 02:
        dfbody_atright_closex2
    show didacfbodytop naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandx2 empty: #both hands
        dfbody_atright_closex2
    show didacf_blush 04:
        dfexpressions_atright_closex2
    show didacf_eyes 04:
        dfexpressions_atright_closex2
    show didacf_pupils front04:
        dfexpressions_atright_closex2
    show didacf_eyebrows angryx03:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth sad_Talkingx03:
        dfexpressions_atright_closex2
    show light_screen_01:
        light_screen_01_position
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position

    with hpunch

    d "Siento haberte interrumpido el sueño, pero una tiene sus necesidades cuando no la ayudan."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx04
    with dissolve

    n "Su tono es gélido y distante."

    menu morning05_sexwithDidacNO_question:
        
        pt "Supongo que se siente rechazada por las veces que me insistió y le dije que no..."
        
        "Pues podrías haberlo hecho en otro sitio, si tanto lo lamentas.":
            
            call p_Help

            $pl.ch_pts("dp",-3)

            show didacf_blush 00
            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx09
            with dissolve

            pause

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx09
            with dissolve

            d "¡TRANQUILO!"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            show morning04_bg_bedroom_youleaving 02
            with dissolve

            d "¡Ya te dejo en paz!"

            scene morning04_bg_bedroom_youleaving 01
            show light 01:
                light01_rightside_position
            show light_screen_01:
                light_screen_01_position

            play sound "audio/sfx/door_slam01.ogg"
            with hpunch

            n "Rápidamente sale de la habitación dando con un portazo."

            pt "Un día de estos va a romper una puerta de verdad,"

            pt "y luego me va a tocar a mí pagar la reparación..."

            n "Con cierta pereza terminas levantándote también de la cama y te diriges al baño."

            pt "Necesito una ducha fría..."

            jump morning05_DidacIsGone

        "La verdad es que tampoco es que me disguste.":
            
            call p_Help

            $pl.ch_pts("dp",1)

            show didacf_blush 03
            show didacf_eyes 03
            show didacf_pupils down03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx002
            with dissolve

            d "Ya lo veo, ya..."

            show didacf_blush 03
            show didacf_eyes 04
            show didacf_pupils down04
            show didacf_eyebrows angryx01
            show didacf_mouth sadbiting_Silentx05
            with dissolve

            n "Sus ojos se apartan de tu mirada y se fijan en una parte concreta inferior de tu anatomía"

            show didacf_blush 04
            show didacf_eyes 05
            show didacf_pupils down05
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Talkingx000
            with dissolve

            n "que sobresale notablemente de la sábana que cubre tu cuerpo."

            show didacf_blush 04
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Bue-"

            extend "bueno,"

            p "ya sabes que esto es bastante normal por las mañanas..."

            show didacf_blush 03
            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "Sí,"

            extend " lo sé."

            show didacf_blush 03
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows normal
            show didacf_mouth sad_Talkingx002
            with dissolve

            d "Pero lo que no es tan normal es que te la estuvieras tocando en sueños mientras me oías gemir."

            show didacf_blush 03
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx01
            with dissolve

            pt "¡¿Eso hacía?!"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "Tranquilo,"

            extend " ya me voy..."

            play sound "audio/sfx/door_open01.ogg"
    
            show morning04_bg_bedroom_youleaving 02
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx05
            with dissolve

            n "Con cierta rudeza, abre la puerta de la habitación."

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx05
            with dissolve

            d "No tengo ningún interés en ser la causa de tus puñeteras erecciones."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡Mátate a pajas si quieres,"

            extend " pero a mí déjame en paz!"

            play sound "audio/sfx/door_slam01.ogg"

            scene morning04_bg_bedroom_youleaving 01
            show light 01:
                light01_rightside_position
            show light_screen_01:
                light_screen_01_position
            with hpunch

            n "Y con un portazo sale de la habitación."

            pt "No ahorraremos en puertas en esta casa..."

            pt "Está claro que no está de muy buen humor,"

            pt "lo mejor será ducharme y vestirme cuanto antes para ver qué diablos trama hoy..."

            scene afternight03_bg shower
            with fade

            n "Ni corto ni perezoso decides tomarte una ducha fría antes de volver a tener contacto con él."

            jump morning05_DidacIsGone

label morning05_DidacIsGone: #After shower you discover Didac is not at home.

    scene morning04_bg_livingroom_others_morning
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #ight_screen_01_position
    with fade

    p "Pero ¡¿dónde coño se ha metido ahora el muy imbécil?!"

    n "Después de una reconfortante y revitalizante ducha, vuelves a la sala más grande del piso,"

    n "pero no localizas a Dídac en ninguna parte."

    n "Lo que sí logras encontrar es un trozo de papel imantado en la nevera que dice,"

    n "{i}He ido a la playa. No intentes buscarme, prefiero no tenerte cerca por ahora.{/i}"

    p "..."

    p "Maldito idiota..."

    p "¿A qué playa ha ido?"

    p "Es absurdo que lo vaya a buscar..."

    p "Y si lo encuentro, ¿qué hago?"

    p "¿Lo arrastro hasta casa?"

    p "Con todo el montón de gente que estará mirando,"

    extend " especialmente los chulitos de playa,"

    p "..."

    p "Solo espero que no haga ninguna estupidez..."

    jump morning05_AfterDidac

label morning05_sexwithDidacYES:
#####
    ###if afternight04_didac_orgasms >= 1: #Didac is really fucking you.

    pt "Vaya sueño más raro..."

    play sound "audio/characters/didac/moanings06.ogg"

    #gd "*Gimoteos femeninos* Mfff... mm... ah..."
    gd "Mfff... mm... ah..." # Feminine Moans

    pt "¡¿Otra vez lo mismo?!"

    play sound "audio/characters/didac/moanings06.ogg"

    scene morning04_bg bedroom_neus_a
    show morning04_bedroom_Didac_body 01a:
        morning04_bedroom_Neus_body_anim

    show morning04_bedroom_Didac_bodyass 01a:
        morning04_bedroom_Neus_bodyass_anim02

    show light 01:
        light01_rightside_position
    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light 01:
        light01_rightside_position
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position

    with fade
    
    window hide dissolve
    pause

    show morning04_bedroom_Didac_body 01b
    show morning04_bedroom_Didac_bodyass 01b
    with dissolve

    #gd "*Gimoteos femeninos* MMMmff..."
    gd "MMmfff..." # Feminine Moan

    show morning04_bedroom_Didac_body 01b
    show morning04_bedroom_Didac_bodyass 01c
    with Dissolve (1.0)

    pt "La sensación es mucho más placentera que ayer..."

    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0

    play sound "audio/characters/didac/moanings06.ogg"

    p "¡¿Dídac?!"

    show morning04_bedroom_Didac_body 01c
    show morning04_bedroom_Didac_bodyass 01b
    with Dissolve (1.0)

    d "Mmm..."

    play sound "audio/characters/didac/moanings05.ogg"

    ## DIDAC
    scene morning04_bg bedroom_neus_a
    show morning04_bedroom_Didac_body_ass 02c:
        zoom .89
        xanchor 0.5
        xpos 0.5
        yanchor 0.5
        ypos 0.50
        linear 1.0 xpos .52 ypos .54 zoom 1.08
        linear 3.0 xpos 0.49 ypos 0.5 zoom .89
        linear 1.0 xpos .55 ypos .54 zoom 1.05
        linear 3.0 xpos .50 ypos .50 zoom .89
        repeat
    show morning04_bedroom_Didac_body_body 02c
    show morning04_bedroom_Didac_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows serious:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c

    show light 01:
        light01_rightside_position
    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0
    show light_screen_01:
        light_screen_01_position
    with fade

    d "Tu polla es realmente enorme, [protname]..."

    show morning04_bedroom_Didac_exp_blush 03
    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

#########################################################
    
    if config.version < "00.10.03": # Start Morning Sex with Didac.
        
        call endupdatescript
    
#######################################################

    menu morning05_DidacSex_Question:
        
        pt "¿Qué diablos se supone que tengo que decirle ahora...?"
        
        "¡¿Qué coño estás haciendo?!":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)

            jump morning05_DidacSex_No

        "<Después de lo de anoche, ¿por qué no?>":

            call p_Help
            
            $pl.ch_pts("dp",1)

            jump morning05_DidacSex_Yes

label morning05_DidacSex_No:

    show morning04_bedroom_Didac_exp_blush 03
    show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
    show morning04_bedroom_Didac_exp_eyebrows normal
    with dissolve

    d "¿No es evidente?"

    show morning04_bedroom_Didac_exp_blush 03
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "Te estoy violando de buena mañana."

    show morning04_bedroom_Didac_exp_blush 04
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx01
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
    with dissolve

    d "No podía desperdiciar semejante \"trampera mañanera\"..."

    show morning04_bedroom_Didac_exp_blush 04
    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx05
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    menu morning05_DidacAskPermission_Question:
        
        pt "La verdad es que la tengo bastante dura..."
        
        "Podrías haberme pedido permiso primero...":
            
            call p_Help
            
            $pl.ch_pts("dp",1)

            jump morning05_DidacAskPermission_Answer

        "<Después de lo de anoche, ¿por qué no?>":

            call p_Help
            
            $pl.ch_pts("dp",1)

            jump morning05_DidacSex_Yes

label morning05_DidacAskPermission_Answer:

    show morning04_bedroom_Didac_exp_blush 04
    show morning04_bedroom_Didac_exp_mouth sad_Talkingx001
    show morning04_bedroom_Didac_exp_eyebrows sadx02
    with dissolve

    d "¿Y despertarte con la carita de angelito que tenías?"

    show morning04_bedroom_Didac_exp_blush 04
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx02
    with dissolve

    d "Me dirás que hay mejores formas de desvelarse por la mañana que con un buen polvo..."

    show morning04_bedroom_Didac_exp_blush 03
    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx02
    show morning04_bedroom_Didac_exp_eyebrows normal
    with dissolve

    p "Dídac..."

    show morning04_bedroom_Didac_exp_blush 02
    show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "¡¿Qué?!"

    if afternight04_didac_orgasms >= 4:

        show morning04_bedroom_Didac_exp_blush 02
        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx03
        with dissolve

        d "¡¿Me vendrás ahora con tu estúpida moralidad hipócrita?!"

        if afternight04_Pussy_dick_med_Speed_1_Success > 0:

            show morning04_bedroom_Didac_exp_blush 03
            show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "¡¿Después de que me follaras como un toro semental desbocado hace apenas ocho horas?!"

        else:

            show morning04_bedroom_Didac_exp_blush 03
            show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows angryx03
            with dissolve

            d "Aunque ni siquiera te dignaras a meterme tu jodida polla como te pedí."

    if afternight04_didac_orgasms >= 4:

        show morning04_bedroom_Didac_exp_blush 04
        show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
        show morning04_bedroom_Didac_exp_eyebrows sadx03
        with dissolve

        d "Me corrí bastantes veces..."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx03
        show morning04_bedroom_Didac_exp_eyebrows sadx02
        with dissolve


    elif afternight04_didac_orgasms == 3:

        show morning04_bedroom_Didac_exp_blush 03
        show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
        show morning04_bedroom_Didac_exp_eyebrows serious
        with dissolve

        d "Me diste solo tres orgasmos,"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        d "pero es mejor que nada..."

        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

    elif afternight04_didac_orgasms == 2:

        show morning04_bedroom_Didac_exp_blush 02
        show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "Aunque solo me corrí dos veces..."

        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve


    elif afternight04_didac_orgasms == 1:

        show morning04_bedroom_Didac_exp_blush 01
        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        d "Aunque solo tuve un mísero orgasmo..."

        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows angryx03
        with dissolve


    elif afternight04_didac_orgasms == 0:

        if mc_body.orgasm == 3:

            show morning04_bedroom_Didac_exp_blush 01
            show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
            show morning04_bedroom_Didac_exp_eyebrows angryx03
            with dissolve

            d "¡Después de que me dejaras sin un jodido orgasmo cuando tú te corriste tres putas veces!"

        else:

            show morning04_bedroom_Didac_exp_blush 01
            show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
            show morning04_bedroom_Didac_exp_eyebrows angryx03
            with dissolve

            d "¡Después de que me dejaras tirada sin tener ni un puto orgasmo!"

        show morning04_bedroom_Didac_exp_blush 01
        show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
        show morning04_bedroom_Didac_exp_eyebrows angryx04
        with dissolve

        d "¡¿Encima quieres que pare ahora?!"

        show morning04_bedroom_Didac_exp_blush 01
        show morning04_bedroom_Didac_exp_mouth sad_Silentx06
        show morning04_bedroom_Didac_exp_eyebrows angryx04
        with dissolve

    if mc_body.orgasm == 3 and afternight04_didac_orgasms > 0:

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        d "Además,"

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "te corriste bien a gusto ayer,"

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        d "hasta que ya no pudiste más..."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

    p "..."

    if afternight04_didac_orgasms >= 4:

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows sadx01
        with dissolve

        d "Tantas, que perdí la cuenta..."

        if mc_body.orgasm >= 2:

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
            with dissolve

            d "¡y tú tampoco te quedaste corto!"

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx05
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        p "..."

    pt "Desde luego,"

    extend " razón no le falta..."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx02
    with dissolve

    d "¿Acaso quieres que la saque?"

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
    show morning04_bedroom_Didac_exp_eyebrows serious
    with dissolve

    pt "Definitivamente, esto es un {a=https://es.wikipedia.org/wiki/Déjà_vu}{i}déjà vu{/i}{/a}..."

    menu morning05_AbortSex_Question:
        
        pt "pero en lugar de Neus, es el {a=https://es.wikipedia.org/wiki/Hipersexualidad}nimfómano{/a} de mi compañero de piso convertido en chica..."
        
        "Lo siento, pero ahora mismo no tengo ganas.":
            
            call p_Help
            
            $pl.ch_pts("dp",-3)

            jump morning05_AbortSex_Yes

        "<Después de lo de anoche, ¿por qué no?>":

            call p_Help
            
            $pl.ch_pts("dp",3)

            jump morning05_DidacSex_Yes

label morning05_AbortSex_Yes:

    #Dídac con cara de pocos amigos.

    show morning04_bedroom_Didac_exp_blush 00
    show morning04_bedroom_Didac_exp_mouth sad_Silentx05
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "..."

    play music "audio/music/alcaknight/bury_it.ogg" fadein 3.0 fadeout 3.0

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "Puto [protname] de los cojones..."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx03
    with dissolve

    d "¡Eres un puto hipócrita de mierda!"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
    show morning04_bedroom_Didac_exp_eyebrows angryx04
    with dissolve

    d "Vete y que te folle un pez..."

    scene morning04_bg bedroom_neus_c
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with hpunch

    n "De forma agresiva se aparta de ti y recogiendo su ropa encima de la estantería de noche,"

    play sound "audio/sfx/door_open01.ogg"

    scene morning04_bg_bedroom_youleaving 02
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with fade

    n "se dirige fuera de la habitación cerrando la puerta con un portazo."

    play sound "audio/sfx/door_slam01.ogg"

    show morning04_bg_bedroom_youleaving 01
    with hpunch

    pt "Maldita sea..."

    pt "Esto se me está yendo de las manos..."

    pt "Lo mejor será que me vaya a tomar una ducha fría..."

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    play music "audio/sfx/shower01.ogg" fadein 3.0 fadeout 3.0

    scene afternight03_bg shower
    with fade

    window hide dissolve
    pause

    jump morning05_AfterShower

label morning05_DidacSex_Yes:

    $ morning05_DidacSex_Anal_Cond = False
    $ morning05_DidacSex_Pussy_Cond = True

    $ morning05_DidacSex_WrapLegs_Cond = False

    #$ DidacMCPregnant = False #Condom Yes or not.

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = True
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False


    $ morning05_missionary_cond_01 = True # Starting Machine
    $ morning05_missionary_cond_02 = False # Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She rubbing you.
    $ morning05_missionary_cond_06 = False
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    # Dídac se está debajo de ti, peor de cara a ti mientras se la metes. (Te agarrará la cadera con sus piernas.)

    play music "audio/music/kevinmacleod/fearless_first.ogg" fadein 3.0 fadeout 3.0

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 4.0 xpos -0.4 ypos 1.3 # Hand
        easein_quad 0.5 zoom 5.0 xpos -0.6 ypos 1.5  # Hand Closer

    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with hpunch

    n "La tomas por las muñecas a la fuerza y consigues invertir la situación."

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos -0.4 #From your dick
        ease_quad 10.0 zoom 3.0 ypos 1.25 # Face Good
        #zoom 5.0 ypos 1.2 # Close Shot Boobs
        #easeout_quad 10.0 zoom 5.0 ypos 1.85 # Close Shot Face
    #show light 01:
        #light01_rightside_position #wrong direction
    show light_screen_01:
        light_screen_01_position
    
    pause

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 03:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth happy_Talkingx04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 05:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front05:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows angryx03:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    #show light 01:
        #light01_rightside_position
    show light_screen_01:
        light_screen_01_position

    with dissolve

    d "Qué bruto eres cuando quieres..."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    p "Te quejaste mucho anoche..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth happy_Talkingx11
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "Fóllame y calla."

    #show gensex_missionary_d_head_exp_blush 04
    #show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
    #show gensex_missionary_d_head_exp_eyes 05
    #show gensex_missionary_d_head_exp_pupils front05
    #show gensex_missionary_d_head_exp_eyebrows angryx04
    #with dissolve

    if DidacMCPregnant == True:
        jump morning05_DidacSex_Yes_CondomNO
    else:
        jump morning05_DidacSex_Yes_CondomYES

label morning05_DidacSex_Yes_CondomYES:

    $ morning05_DidacSex_UsingCondom_Cond = True

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = True
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = True # Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False
    $ morning05_missionary_cond_06 = False
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good
        ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
    show light_screen_01:
        light_screen_01_position
    with dissolve

    n "Justo en el momento en que decides empezar a moverte te detienes al dirigir tu mirada a vuestra unida entrepierna."

    p "¿De dónde has sacado este condón?"

    d "Llevo horas despierta..."

    d "Me ha dado tiempo a ir a la farmacia y volver."

    d "Y aun así seguías durmiendo del tirón..."

    p "..."

    d "¿Qué?"

    p "¿Has sido capaz de salir de buena mañana a la calle solo para ir a comprar condones?"

    d "La farmacia tampoco está tan lejos..."

    pt "Siendo domingo habrá ido a una farmacia de guardia..."

    p "Pero nunca te había visto levantarte pronto y mucho menos para ir a buscar algo y volver..."

    d "¡¿Quieres hacer el puñetero favor de callarte y follarme?!"

    pt "Realmente desconozco a este Dídac..."

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = True # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good
        easein_quad 10.0 zoom 1.5 ypos 0.26 # Pussy
    show light_screen_01:
        light_screen_01_position
    with dissolve

    n "Sin demasiada dificultad, logras introducir más de la mitad de tu miembro en su cavidad vaginal."

    pt "Realmente está bien mojada..."

    #d "*Gemido femenino* Ahhmm..."
    d "Ahhmm..." # Feminine Moan

    pt "Coño,"

    extend " ¿cuánto rato lleva follándome?"

    pt "La tengo súper sensible..."

    jump morning05_DidacSex_Fucking

label morning05_DidacSex_Yes_CondomNO:

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = True
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = True # Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False
    $ morning05_missionary_cond_06 = False
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good
        ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
    show light_screen_01:
        light_screen_01_position

    with dissolve

    n "Justo en el momento en que decides empezar a moverte,"

    n "te detienes al dirigir tu mirada a vuestra unida entrepierna."

    p "..."

    p "Dídac..."

    d "¿Sí...?"

    p "No llevo condón..."

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils right00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows surprisex02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position

    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "¡¿Te me has montado encima sin que llevara condón?!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx004
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "No seas melodramático..."

    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
    with dissolve

    d "Sé cómo reaccionas cuando estás a punto de correrte..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx05
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    p "¡¿Es que se te ha ido completamente la pinza?!"

    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows angryx03
    with dissolve

    p "¡¿Acaso no has oído hablar del {a=https://es.wikipedia.org/wiki/Líquido_preseminal}preseminal{/a}?!"

    p "¡Por poner solo un ejemplo!"

    show gensex_missionary_d_head_exp_blush 03
    show gensex_missionary_d_head_exp_mouth sad_Talkingx17
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    d "Deja de mirar tantas películas,"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
    with dissolve

    d "se te atrofia el cerebro, que de por sí ya lo tienes bastante jodido..."

    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "Ninguna tía se queda preñada por el preseminal..."

    show gensex_missionary_d_head_exp_mouth sad_Talkingx004
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    d "he follado muchas veces sin condón y nunca he dejado preñada a ninguna."

    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    p "Tampoco sueles quedar muy a menudo una segunda vez con las chicas que sueles follarte..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx11
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx13
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    pt "Por no hablar de a saber qué {a=https://es.wikipedia.org/wiki/Infecciones_de_transmisión_sexual}enfermedades de transmisión sexual{/a} habrá pillado el idiota este..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx03
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    p "¡Joder Dídac!"

    show gensex_missionary_d_head_exp_mouth sad_Silentx05
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    p "¡Esto va en serio!"

    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx03
    with dissolve

    p "¡¿No oíste lo que me dijo quien te convirtió en mujer sobre si te quedabas preñada?!"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx05
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "¿No has pensado que quizás te estaba tomando el pelo?"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
    with dissolve

    d "O quizás solo quiere que te fijes en ella y no tengas tentaciones conmigo..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
    with dissolve

    p "¡¿Para qué te habría convertido en mujer entonces?!"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx13
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "¡Y yo qué sé!"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "Para empezar, ni siquiera la conozco;"

    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx03
    with dissolve

    d "¡y en segundo lugar no tengo ni idea de por qué me convirtió en mujer!"

    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    pt "No recuerda absolutamente nada..."

    p "..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx03
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    p "¡¿Y qué me dices si no es mentira?!"

    show gensex_missionary_d_head_exp_mouth sad_Silentx01
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows surprisex04
    with dissolve

    p "¡¿Acaso quieres quedarte de por vida como mujer?!"

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils right00
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx01
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    d "Tampoco sería el fin del mundo..."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx06
    with dissolve

    pt "¡¡¿PERO QUÉ COÑO?!!"

    d "..."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "¿Dónde están los condones?"

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    p "Ya los cojo yo..."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "tampoco cuesta tanto ponerse el chubasquero,"

    extend " leches..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sad_Talkingx001
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    d "Ayer te di el último que tenía..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx03
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    p "..."

    show gensex_missionary_d_head_exp_mouth sad_Talkingx003
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    d "Tú tienes..."

    show gensex_missionary_d_head_exp_mouth sad_Talkingx001
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    d "¿No?"

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "..."

    show gensex_missionary_d_head_exp_mouth happybiting_Silentx02
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    pt "Mierda."

    show gensex_missionary_d_head_exp_mouth sad_Silentx03
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows normal
    with dissolve

    p "Euh..."

    show gensex_missionary_d_head_exp_mouth sad_Silentx05
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows surprisex02
    with dissolve

    p "No..."

    extend " no tengo ninguno..."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows angryx03
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "..."

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = True # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5

        zoom 3.0 ypos 0.5 # Face Good
        ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
        #zoom 0.75
        #zoom 3.0 ypos 1.25 # Face Good
        #ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
    show light_screen_01:
        light_screen_01_position
    with dissolve

    n "Sutilmente,"

    n "sus caderas empiezan a moverse frotando sus -ardientes y húmedos- labios vaginales con la punta de tu glande,"

    n "completamente erecto"

    p "Dídac..."

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sad_Talkingx004:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows angryx03:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position

    with dissolve

    d "Voy cachonda."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    p "Espera aquí,"

    extend " voy a la farmacia."

    # Wrapped crossed legs on your back

    play music "audio/music/kevinmacleod/happy/coolRock.ogg" fadein 3.0 fadeout 3.0

    $ morning05_DidacSex_WrapLegs_Cond = True

    scene morning04_bg bedroom_neus_a
    show morning05_crossedlegs:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 0.75
        easein_quad 1.0 zoom 1.0

    show border_lines 04:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5 xpos 0.45 ypos 0.5
        zoom 0.3
        easein_elastic 1.5 zoom 0.5
    show light_screen_01:
        light_screen_01_position
    with hpunch

    n "Rápidamente abre sus piernas y las cierra envolviéndolas en tu espalda sin darte opción a poder escapar."

    d "No."

    d "De aquí no te vas hasta que yo no pueda ni moverme..."

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = True # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5

        zoom 2.0 ypos 0.5 # Half Body
        easein_quad 10.0 zoom 2.0 ypos 0.25 # Body Perspective
        #ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
        #zoom 0.75
        #zoom 3.0 ypos 1.25 # Face Good
        #ease_quad 10.0 zoom 3.0 ypos 0.0 # Pussy View
    show light_screen_01:
        light_screen_01_position
    with dissolve

    pause 1.5 

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = True # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    show morning05_missionary_anim 01
    with dissolve

    n "Con su cadera se acerca aún más a tu erecto miembro con la clara intención de metérselo de nuevo dentro."

    p "Dídac..."

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = True # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows angryx03:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position

    with dissolve

    pt "Lo que más me jode es que no tardaré mucho en correrme,"

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    pt "no sé cuanto tiempo llevaba cabalgándome,"

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    pt "pero la tengo a escasos segundos..."

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    pt "Y me jode confesarlo,"

    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    pt "pero sabe cómo ponerme a tono el muy hijo de puta..."

    show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
    show gensex_missionary_d_head_exp_eyebrows sadx06
    with dissolve

    pt "y sus desarrollados músculos vaginales no ayudan..."

    menu morning05_DidacSex_WithoutCondom_Question:
        
        pt "Si me corro dentro, es muy probable que no vuelva a ver a Dídac tal y como era nunca más..."
        
        "No sin condón Dídac, me niego a correr el riesgo.":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)

            jump morning05_DidacSex_WithoutCondom_No

        "<Follar su coño sin condón>":

            call p_Help
            
            $pl.ch_pts("dp",3)

            $ morning05_DidacSex_Pussy_Cond = True
            $ morning05_DidacSex_Anal_Cond = False
            $ morning05_DidacSex_Pussy_Unsafe_Cond = True

            jump morning05_DidacSex_WithoutCondom_Yes

        "<Follar su cavidad anal sin condón>" if morning05_DidacSex_Anal_Rejected == False:

            call p_Help
            
            if afternight04_Anal_dick_med_Speed_1_Success == 0:

                $pl.ch_pts("dp",-1)

                $ morning05_DidacSex_Anal_Rejected = True

                d "¿Qué haces?"

                p "Bueno,"

                extend " ya que no tenemos condones,"

                p "creo que lo más sensato sería hacerlo por el otro agujero..."

                d "Estás de coña,"

                extend " ¿no?"

                p "No..."

                if afternight04_Anal_dick_med_Speed_0_Success > 0:

                    p "Pero si conseguí metértela por el culo sin que te quejaras..."

                    if afternight04_Anal_dick_med_Speed_0_Failed > afternight04_Anal_dick_med_Speed_0_Success:

                        d "¡¿Sin quejarme?!"

                        d "¡Te lo dije como mínimo [afternight04_Anal_dick_med_Speed_0_Failed] veces!"

                    else:

                        d "Que no me quejara no significa que me encantara..."

                        d "además... me gustó cuando estaba quieta..."

                        d "así que no te flipes tú ahora."

                d "¡¿Te crees que soy marica o qué?!"

                p "¿Debo responder a esa pregunta...?"

                d "Ni de puta broma."

                d "¡¿Queda claro?!"

                p "..."

                pt "Quizás,"

                extend " si ayer por la noche hubiera probado esa opción con éxito,"

                pt "ahora tendría más posibilidades de convencerlo..."

                jump morning05_DidacSex_WithoutCondom_Question

            else:

                $pl.ch_pts("dp",2)

                $ morning05_DidacSex_Pussy_Cond = False
                $ morning05_DidacSex_Anal_Cond = True

                jump morning05_DidacSex_WithoutCondom_Yes

label morning05_DidacSex_WithoutCondom_No:

    #Dídac con cara de pocos amigos.

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = True # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sad_Silentx05:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows surprisex02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position

    with dissolve
    
    d "..."

    show gensex_missionary_d_head_exp_blush 03
    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    p "..."

    show gensex_missionary_d_head_exp_blush 03
    show gensex_missionary_d_head_exp_mouth sad_Silentx11
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx12
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    pt "¿Es que no me ha oído...?"

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = True # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 2.0 ypos 0.5 # Half Body
        easein_quad 10.0 zoom 2.0 ypos 0.25 # Body Perspective
    show light_screen_01:
        light_screen_01_position

    with dissolve

    n "Sientes el leve movimiento de sus caderas acercándose a tu entrepierna de nuevo."

    p "¡Dídac!"

    p "¡Te he dicho que sin condón ni de coña!"

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = True # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 06:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sad_Talkingx16:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front00:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows angryx08:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position

    with vpunch

    d "¡Joder!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx13
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx08
    with dissolve

    d "¡Ya te he oído la primera vez!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx17
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    d "¡no hace falta que me lo repitas!"

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sad_Silentx13
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows angryx08
    with dissolve

    p "¡¿Entonces para qué diablos me sigues buscando la polla?!"

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows angryx08
    with dissolve

    d "¡Porque voy jodidamente cachonda!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx13
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows angryx08
    with dissolve

    d "¡¿Vale?!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Silentx20
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows angryx08
    with dissolve

    p "Joder..."

    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0

    $ morning05_DidacSex_WrapLegs_Cond = False

    show morning05_missionary_anim 01

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Talkingx03
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils front00
    show gensex_missionary_d_head_exp_eyebrows surprisex04
    with vpunch

    n "Con cierta resistencia consigues apartarte de la presión de sus piernas."

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sad_Silentx05
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils front02
    show gensex_missionary_d_head_exp_eyebrows surprisex02
    with dissolve

    p "Necesito una ducha."

    show gensex_missionary_d_head_exp_blush 03
    show gensex_missionary_d_head_exp_mouth sad_Silentx07
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows angryx04
    with dissolve

    d "..."

    show gensex_missionary_d_head_exp_blush 02
    show gensex_missionary_d_head_exp_mouth sad_Silentx11
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows angryx07
    with dissolve

    p "Tú haz lo que tengas que hacer."

    show gensex_missionary_d_head_exp_blush 02
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
    show gensex_missionary_d_head_exp_eyes 00
    show gensex_missionary_d_head_exp_pupils right00
    show gensex_missionary_d_head_exp_eyebrows serious
    with dissolve

    p "Pero ten claro que no voy a follarte sin condón."

    show gensex_missionary_d_head_exp_blush 03
    show gensex_missionary_d_head_exp_mouth sad_Silentx03
    show gensex_missionary_d_head_exp_eyes 02
    show gensex_missionary_d_head_exp_pupils right02
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    p "¡¿Me explico?!"

    show gensex_missionary_d_head_exp_blush 04
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils right05
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    d "..."

    #n "Una extraña combinación de sentimientos, culpa, arrepentimiento y deseo se dibuja en su rostro."

    if DidacMCPregnant == True: #Condom Yes or not.

        show gensex_missionary_d_head_exp_blush 04
        show gensex_missionary_d_head_exp_mouth sad_Silentx03
        show gensex_missionary_d_head_exp_eyes 08
        show gensex_missionary_d_head_exp_pupils front07
        show gensex_missionary_d_head_exp_eyebrows sadx06
        with dissolve

    else:

        show gensex_missionary_d_head_exp_blush 02
        show gensex_missionary_d_head_exp_mouth sad_Silentx07
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils front05
        show gensex_missionary_d_head_exp_eyebrows angryx03
        with dissolve

    n "Decides que lo más sensato es salir de esa habitación,"

    scene morning04_bg_bedroom_youleaving 01
    show light_screen_01:
        light_screen_01_position
    with fade

    play sound "audio/sfx/door_open01.ogg"

    show morning04_bg_bedroom_youleaving 02
    with dissolve

    n "y diriges tus pasos hacia el cuarto de baño,"

    play sound "audio/sfx/door_close01.ogg"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    play music "audio/sfx/shower01.ogg" fadein 3.0 fadeout 3.0

    scene afternight03_bg shower
    with fade

    n "donde te tomas una ducha fría para templar tu mente y tus decisiones."

    stop music fadeout 3.0 

    jump morning05_AfterShower

label morning05_DidacSex_WithoutCondom_Yes:

    pt "¡A tomar viento!"

    pt "¡Es él, que me está provocando!"

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = True # Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 2.0 ypos 0.5 # Half Body
        easein_quad 10.0 zoom 2.0 ypos 0.25 # Body Perspective
        #zoom 3.0 ypos 1.25 # Face Good
    show light_screen_01:
        light_screen_01_position

    with dissolve

    if morning05_DidacSex_Pussy_Cond == True:

        n "Decides agarrar tu polla y se la introduces de nuevo casi completamente."

        $ morning05_missionary_cond_01 = False # Starting Machine
        $ morning05_missionary_cond_02 = False # Rubbing
        $ morning05_missionary_cond_03 = False # Slow Fuck
        $ morning05_missionary_cond_04 = False # Fast Fuck
        $ morning05_missionary_cond_05 = False # She Rubbing you
        $ morning05_missionary_cond_06 = False # She Rubbing you FAST
        $ morning05_missionary_cond_07 = True # Slow Half Fuck
        $ morning05_missionary_cond_08 = False # Raped
        $ morning05_missionary_cond_09 = False # Raped Fast

        show morning05_missionary_anim 01
            #transform_anchor True
            #xalign 0.5 yalign 0.5
            #zoom 1.0
        with dissolve

        #d "*gemido* Aaaahhh..."
        d "Aaaahh..." # Feminine Moan

        d "Sí,"

        extend " esto ya me gusta más..."

    elif morning05_DidacSex_Anal_Cond == True:

        n "Decides agarrar tu polla y empiezas a hacer presión en su cavidad anal."

        d "¡¿Qué cojones estás haciendo?!"

        $ morning05_missionary_cond_01 = False # Starting Machine
        $ morning05_missionary_cond_02 = False # Rubbing
        $ morning05_missionary_cond_03 = False # Slow Fuck
        $ morning05_missionary_cond_04 = False # Fast Fuck
        $ morning05_missionary_cond_05 = False # She Rubbing you
        $ morning05_missionary_cond_06 = False # She Rubbing you FAST
        $ morning05_missionary_cond_07 = True # Slow Half Fuck
        $ morning05_missionary_cond_08 = False # Raped
        $ morning05_missionary_cond_09 = False # Raped Fast

        show morning05_missionary_anim 01
        with dissolve

        n "Con cierta dificultad por la presión que hace con sus piernas,"

        n "consigues meter casi la mitad de tu polla en su ano."

        $ morning05_missionary_face_cond_empty = True
        $ morning05_missionary_face_cond_surprise = False
        $ morning05_missionary_face_cond_malicious = False
        $ morning05_missionary_face_cond_horny = False

        $ morning05_missionary_cond_01 = False # Starting Machine
        $ morning05_missionary_cond_02 = False# Rubbing
        $ morning05_missionary_cond_03 = False # Slow Fuck
        $ morning05_missionary_cond_04 = False # Fast Fuck
        $ morning05_missionary_cond_05 = False # She Rubbing you
        $ morning05_missionary_cond_06 = False # She Rubbing you FAST
        $ morning05_missionary_cond_07 = True
        $ morning05_missionary_cond_08 = False # Raped
        $ morning05_missionary_cond_09 = False # Raped Fast

        scene morning05_missionary_anim 01:
            transform_anchor True
            xalign 0.5 yalign 0.5
            zoom 3.0 ypos 1.25 # Face Good

        show gensex_missionary_d_head_face:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_exp_blush 03:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_exp_mouth sad_Talkingx26:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_exp_eyes 00:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_exp_pupils front00:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_exp_eyebrows angryx07:
            gensex_missionary_d_head_FaceZoom03_pos
        show gensex_missionary_d_head_hairfront:
            gensex_missionary_d_head_FaceZoom03_pos
        show light_screen_01:
            light_screen_01_position

        with vpunch

        d "¡Te he dicho que me folles!"

        #show gensex_missionary_d_head_exp_blush 02
        show gensex_missionary_d_head_exp_mouth sad_Talkingx16
        show gensex_missionary_d_head_exp_eyes 02
        show gensex_missionary_d_head_exp_pupils front02
        show gensex_missionary_d_head_exp_eyebrows angryx07
        with dissolve

        d "¡No que me hagas mariconadas!"

        show gensex_missionary_d_head_exp_mouth sad_Silentx20
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils front05
        show gensex_missionary_d_head_exp_eyebrows angryx08
        with dissolve

        p "¿Tú te oyes lo que dices?"

        show gensex_missionary_d_head_exp_mouth sad_Silentx13
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils right05
        show gensex_missionary_d_head_exp_eyebrows angryx08
        with dissolve

        d "..."

        show gensex_missionary_d_head_exp_mouth sad_Silentx11
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils front05
        show gensex_missionary_d_head_exp_eyebrows angryx07
        with dissolve

        p "Además,"

        extend " ayer te di por el culo hasta el fondo y no oí que te quejaras mucho al final..."


        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils right05
        show gensex_missionary_d_head_exp_eyebrows angryx04
        with dissolve

        d "..."

        show gensex_missionary_d_head_exp_blush 04
        show gensex_missionary_d_head_exp_mouth sad_Silentx05
        show gensex_missionary_d_head_exp_eyes 02
        show gensex_missionary_d_head_exp_pupils front02
        show gensex_missionary_d_head_exp_eyebrows angryx03
        with dissolve

        p "Por lo menos por aquí no te voy a dejar preñado,"

        extend " imbécil."

        #Rostro de Dídac que te aparta la mirada totalmente sonrojada.

        show gensex_missionary_d_head_exp_blush 06
        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils right05
        show gensex_missionary_d_head_exp_eyebrows angryx04
        with dissolve

        d "..."

        show gensex_missionary_d_head_exp_blush 06
        show gensex_missionary_d_head_exp_mouth sad_Talkingx003
        show gensex_missionary_d_head_exp_eyes 02
        show gensex_missionary_d_head_exp_pupils right02
        show gensex_missionary_d_head_exp_eyebrows suspiciousx02
        with dissolve

        d "Haz lo que te salga de los huevos..."

        show gensex_missionary_d_head_exp_blush 06
        show gensex_missionary_d_head_exp_mouth sadbiting_Silentx10
        show gensex_missionary_d_head_exp_eyes 05
        show gensex_missionary_d_head_exp_pupils right05
        show gensex_missionary_d_head_exp_eyebrows angryx03
        with dissolve

        pt "Realmente el problema es que no sé si tiene más estrecho el coño o el ano..."

label morning05_DidacSex_Fucking:

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = True # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows surprisex02:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position
    with dissolve

    p "Dídac,"

    extend " te aviso;"

    p "No tardaré mucho en correrme,"

    extend " la tengo bastante..."

    show gensex_missionary_d_head_exp_blush 06
    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    n "Empieza a mover sus caderas, mientras su mirada parece haberse arrojado completamente al placer."

    show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
    with dissolve

    pt "Como si le hablara a la pared..."

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = True # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good
        easein_quad 10.0 zoom 1.5 ypos 0.26 # Pussy
    show light_screen_01:
        light_screen_01_position

    if morning05_DidacSex_WrapLegs_Cond == True: #If it´s anal she didn´t made that move.

        n "Poco a poco, ayudada por sus piernas, sujetas a tu espalda,"

    else:

        n "Poco a poco, desplazando sin vergüenza tus caderas,"

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = True # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    show morning05_missionary_anim 01
    with dissolve

    n "percibes cómo consigues llegar hasta el fondo,"

    if morning05_DidacSex_Pussy_Cond == True or morning05_DidacSex_UsingCondom_Cond == True:

        n "penetrando completamente de nuevo su cuello uterino."

    elif morning05_DidacSex_Anal_Cond == True:

        n "penetrando completamente su intestino grueso."

        d "¡Cabrón!"

        pt "Espero que haya ido al baño antes de violarme de buena mañana..."

    $ morning05_missionary_face_cond_empty = True
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = False

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = True # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good

    show gensex_missionary_d_head_face:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_blush 06:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_mouth sad_Talkingx07:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyes 06:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_pupils front06:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_exp_eyebrows sadx07:
        gensex_missionary_d_head_FaceZoom03_pos
    show gensex_missionary_d_head_hairfront:
        gensex_missionary_d_head_FaceZoom03_pos
    show light_screen_01:
        light_screen_01_position
    with dissolve

    #d "*gemido* AAAHhh..."
    d "AAAaahh..." # Feminine Moan

    if morning05_DidacSex_Pussy_Cond == True or morning05_DidacSex_UsingCondom_Cond == True:

        if afternight04_Pussy_dick_deep_Speed_0_Done == 0 and afternight04_Pussy_dick_deep_Speed_0_Rape_Done == 0:

            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
            show gensex_missionary_d_head_exp_eyes 05
            show gensex_missionary_d_head_exp_pupils front05
            show gensex_missionary_d_head_exp_eyebrows sadx04
            with dissolve

            d "Por fin ha entrado toda..."

            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
            show gensex_missionary_d_head_exp_eyes 05
            show gensex_missionary_d_head_exp_pupils front05
            show gensex_missionary_d_head_exp_eyebrows angryx03
            with dissolve

            d "Debiste haberme follado así ayer..."

        else:

            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
            show gensex_missionary_d_head_exp_eyes 02
            show gensex_missionary_d_head_exp_pupils front02
            show gensex_missionary_d_head_exp_eyebrows angryx03
            with dissolve
            
            d "Toda dentro..."

            show gensex_missionary_d_head_exp_mouth happy_Talkingx06
            show gensex_missionary_d_head_exp_eyes 05
            show gensex_missionary_d_head_exp_pupils front05
            show gensex_missionary_d_head_exp_eyebrows sadx04
            with dissolve

            d "como ayer..."

    elif morning05_DidacSex_Anal_Cond == True:

        show gensex_missionary_d_head_exp_mouth sad_Talkingx05
        show gensex_missionary_d_head_exp_eyes 02
        show gensex_missionary_d_head_exp_pupils front02
        show gensex_missionary_d_head_exp_eyebrows angryx03
        with dissolve

        d "Me la has metido entera..."

        if afternight04_Anal_dick_deep_Speed_0_Done == 0:

            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
            show gensex_missionary_d_head_exp_eyes 05
            show gensex_missionary_d_head_exp_pupils front05
            show gensex_missionary_d_head_exp_eyebrows angryx04
            with dissolve

            d "¡Hay que joderse!"

        else:

            show gensex_missionary_d_head_exp_mouth happy_Talkingx04
            show gensex_missionary_d_head_exp_eyes 05
            show gensex_missionary_d_head_exp_pupils front05
            show gensex_missionary_d_head_exp_eyebrows suspiciousx02
            with dissolve

            d "Por lo visto lo de ayer no fue simple suerte..."


    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
    show gensex_missionary_d_head_exp_eyes 05
    show gensex_missionary_d_head_exp_pupils front05
    show gensex_missionary_d_head_exp_eyebrows sadx04
    with dissolve

    n "Su rostro muestra una satisfacción fuera de este mundo." 

    show gensex_missionary_d_head_exp_mouth happybiting_Silentx10
    show gensex_missionary_d_head_exp_eyes 06
    show gensex_missionary_d_head_exp_pupils front06
    show gensex_missionary_d_head_exp_eyebrows sadx07
    with dissolve

    n "La presión que sientes en tu polla empieza a preocuparte por el placer indescriptible que ofrece."

    if morning05_DidacSex_Pussy_Cond == True or morning05_DidacSex_UsingCondom_Cond == True:

        pt "Es como si su coño quisiera ahogarme la polla..."

    elif morning05_DidacSex_Anal_Cond == True:

        pt "Es como si su ano me succionara la polla..."

    pt "¡Joder...!"

    pt "Así no voy a durar mucho más..."

    # Besarla?

    menu morning05_DidacSex_Fucking_Kiss_Question:

        pt "¿Sería demasiado gay si le beso ahora?"
        
        "<Hacerlo>":
            
            call p_Help

            if afternight04__MMouth_Tongue_Success > 1:

                $pl.ch_pts("dp",1)

                $ morning05_DidacSex_Fucking_Kiss_Mouth_Done = True

                scene morning04_bg bedroom_neus_a
                show kiss_ n_d_01:
                    transform_anchor True
                    xalign 0.5 yalign 0.5
                    zoom 1.4 xpos 0.5 ypos 0.35 rotate -90
                show light_screen_01:
                    light_screen_01_position
                with fade
            
                d "¡¿Hmmm?!"

                show kiss_ n_d_04
                with dissolve

                pause 0.25

                show kiss_ n_d_02
                with dissolve

                pause 0.25

                show kiss_ n_d_03
                with dissolve

                pause 0.25

                show kiss_ n_d_05
                with dissolve

                d "Hhhmm..."


                menu morning05_DidacSex_Fucking_Kiss_Tongue_Question:

                    pt "¿Me arriesgo a hacerlo con lengua?"

                    "<Sí>":
                        call p_Help

                        if afternight04__MMouth_Tongue_Deep_Success > 1:

                            $pl.ch_pts("dp",1)

                            $ morning05_DidacSex_Fucking_Kiss_Tongue_Done = True

                            scene morning04_bg bedroom_neus_a
                            show kiss_ f_d_07:
                                transform_anchor True
                                xalign 0.5 yalign 0.5
                                zoom 1.2 xpos 0.5 ypos 0.35 rotate -90
                            show light_screen_01:
                                light_screen_01_position
                            with fade

                            d "¡¿Hmm..."

                            extend " Qué?!"

                            show kiss_ f_d_11
                            with Dissolve (0.5)

                            show kiss_ f_d_12
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_11
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_12
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_10
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_09
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_01
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_02
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_05
                            with Dissolve (0.5)

                            pause 0.5

                            show kiss_ f_d_07
                            with Dissolve (0.5)

                            d "Hmm..."

                            $ morning05_missionary_face_cond_empty = True
                            $ morning05_missionary_face_cond_surprise = False
                            $ morning05_missionary_face_cond_malicious = False
                            $ morning05_missionary_face_cond_horny = False

                            $ morning05_missionary_cond_01 = False # Starting Machine
                            $ morning05_missionary_cond_02 = False# Rubbing
                            $ morning05_missionary_cond_03 = False # Slow Fuck
                            $ morning05_missionary_cond_04 = False # Fast Fuck
                            $ morning05_missionary_cond_05 = False # She Rubbing you
                            $ morning05_missionary_cond_06 = False # She Rubbing you FAST
                            $ morning05_missionary_cond_07 = True # Half Dick
                            $ morning05_missionary_cond_08 = False # Raped
                            $ morning05_missionary_cond_09 = False # Raped Fast

                            scene morning05_missionary_anim 01:
                                transform_anchor True
                                xalign 0.5 yalign 0.5
                                zoom 3.0 ypos 1.25 # Face Good

                            show gensex_missionary_d_head_face:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_blush 06:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx003:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_eyes 06:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_pupils front06:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_eyebrows sadx07:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_hairfront:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show light_screen_01:
                                light_screen_01_position
                            with dissolve

                        else:

                            $pl.ch_pts("dp",-1)

                            $ morning05_missionary_face_cond_empty = True
                            $ morning05_missionary_face_cond_surprise = False
                            $ morning05_missionary_face_cond_malicious = False
                            $ morning05_missionary_face_cond_horny = False

                            $ morning05_missionary_cond_01 = False # Starting Machine
                            $ morning05_missionary_cond_02 = False# Rubbing
                            $ morning05_missionary_cond_03 = False # Slow Fuck
                            $ morning05_missionary_cond_04 = False # Fast Fuck
                            $ morning05_missionary_cond_05 = False # She Rubbing you
                            $ morning05_missionary_cond_06 = False # She Rubbing you FAST
                            $ morning05_missionary_cond_07 = True # Half Dick
                            $ morning05_missionary_cond_08 = False # Raped
                            $ morning05_missionary_cond_09 = False # Raped Fast

                            scene morning05_missionary_anim 01:
                                transform_anchor True
                                xalign 0.5 yalign 0.5
                                zoom 3.0 ypos 1.25 # Face Good

                            show gensex_missionary_d_head_face:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_blush 03:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_mouth sad_Talkingx003:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_eyes 05:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_pupils front05:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_exp_eyebrows angryx07:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show gensex_missionary_d_head_hairfront:
                                gensex_missionary_d_head_FaceZoom03_pos
                            show light_screen_01:
                                light_screen_01_position
                            with vpunch

                            d "¡QUITA COÑO!"

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx04
                            with dissolve

                            d "¡Que me estés dando un jodido morreo"

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            with dissolve

                            d "ya es de por sí una soplapollez mayúscula!"

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx03
                            with dissolve

                            d "Que te permito porque sé que se te pone más dura..."

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx17
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            with dissolve

                            d "¡Pero que me metas la jodida lengua!"

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                            show gensex_missionary_d_head_exp_eyes 00
                            show gensex_missionary_d_head_exp_pupils front00
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            with dissolve

                            d "¡Por ahí no paso joder!"

                            show gensex_missionary_d_head_exp_mouth sad_Silentx20
                            show gensex_missionary_d_head_exp_eyes 02
                            show gensex_missionary_d_head_exp_pupils front02
                            show gensex_missionary_d_head_exp_eyebrows angryx08
                            with dissolve

                            p "..."

                            show gensex_missionary_d_head_exp_mouth sad_Talkingx13
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            with dissolve

                            d "¡Deja de hacerme mariconadas y fóllame como es debido!"

                            show gensex_missionary_d_head_exp_mouth sad_Silentx11
                            show gensex_missionary_d_head_exp_eyes 05
                            show gensex_missionary_d_head_exp_pupils front05
                            show gensex_missionary_d_head_exp_eyebrows angryx07
                            with dissolve

                            pt "Si hubiera tenido más suerte ayer,"

                            pt "quizás ahora la habría convencido mejor..."

                            jump morning05_DidacSex_Fucking_Kiss_After

                    "<No>":

                        call p_Help

                        pt "Mejor no tentar a la suerte..."

                        $ morning05_missionary_face_cond_empty = True
                        $ morning05_missionary_face_cond_surprise = False
                        $ morning05_missionary_face_cond_malicious = False
                        $ morning05_missionary_face_cond_horny = False

                        $ morning05_missionary_cond_01 = False # Starting Machine
                        $ morning05_missionary_cond_02 = False# Rubbing
                        $ morning05_missionary_cond_03 = False # Slow Fuck
                        $ morning05_missionary_cond_04 = False # Fast Fuck
                        $ morning05_missionary_cond_05 = False # She Rubbing you
                        $ morning05_missionary_cond_06 = False # She Rubbing you FAST
                        $ morning05_missionary_cond_07 = True # Half Dick
                        $ morning05_missionary_cond_08 = False # Raped
                        $ morning05_missionary_cond_09 = False # Raped Fast

                        scene morning05_missionary_anim 01:
                            transform_anchor True
                            xalign 0.5 yalign 0.5
                            zoom 3.0 ypos 1.25 # Face Good

                        show gensex_missionary_d_head_face:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_exp_blush 04:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_exp_mouth sad_Talkingx003:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_exp_eyes 06:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_exp_pupils front06:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_exp_eyebrows sadx07:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show gensex_missionary_d_head_hairfront:
                            gensex_missionary_d_head_FaceZoom03_pos
                        show light_screen_01:
                            light_screen_01_position
                        with dissolve

                d "..."

                if morning05_DidacSex_Fucking_Kiss_Tongue_Done == True:

                    show gensex_missionary_d_head_exp_mouth sad_Talkingx003
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows surprisex04
                    with dissolve

                elif morning05_DidacSex_Fucking_Kiss_Mouth_Done == True:

                    show gensex_missionary_d_head_exp_mouth sad_Talkingx001
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows normal
                    with dissolve

                else:

                    show gensex_missionary_d_head_exp_mouth sad_Silentx05
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                    with dissolve               

                d "Se..."

                if morning05_DidacSex_Fucking_Kiss_Tongue_Done == True:

                    show gensex_missionary_d_head_exp_mouth sad_Talkingx07
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    with dissolve

                elif morning05_DidacSex_Fucking_Kiss_Mouth_Done == True:

                    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    with dissolve

                else:

                    show gensex_missionary_d_head_exp_mouth sad_Talkingx10
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    with dissolve

                d "¡¿Se puede saber a qué ha venido esta mariconez?!"


                if morning05_DidacSex_Fucking_Kiss_Tongue_Done == True:

                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils right02
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    with dissolve

                else:

                    show gensex_missionary_d_head_exp_mouth sad_Silentx07
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    with dissolve

                p "Ayer me dijiste que, si vas cachonda, y estamos follando,"

                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx04
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils right05
                show gensex_missionary_d_head_exp_eyebrows serious
                with dissolve

                p "es algo que en el fondo no te molesta tanto..."

                d "..."

                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils right02
                show gensex_missionary_d_head_exp_eyebrows normal
                with dissolve

                p "Además,"

                show gensex_missionary_d_head_exp_mouth sad_Talkingx03
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows suspiciousx02
                with dissolve

                d "¿Qué?"

                if morning05_DidacSex_Fucking_Kiss_Tongue_Done == True:
                    show gensex_missionary_d_head_exp_blush 06

                else:
                    show gensex_missionary_d_head_exp_blush 04
                show gensex_missionary_d_head_exp_mouth sad_Silentx05
                show gensex_missionary_d_head_exp_eyes 00
                show gensex_missionary_d_head_exp_pupils front00
                show gensex_missionary_d_head_exp_eyebrows surprisex02
                with dissolve

                p "tienes unos labios muy tentadores."

                show gensex_missionary_d_head_exp_blush 06
                show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils right05
                show gensex_missionary_d_head_exp_eyebrows sadx04
                with dissolve

                d "..."

                if morning05_DidacSex_Fucking_Kiss_Tongue_Done == True:

                    show gensex_missionary_d_head_exp_blush 06
                    show gensex_missionary_d_head_exp_mouth sad_Talkingx05
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows suspiciousx03
                    with dissolve

                    d "¿¿Mi lengua también es muy tentadora??"

                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx02
                    show gensex_missionary_d_head_exp_eyes 02
                    show gensex_missionary_d_head_exp_pupils front02
                    show gensex_missionary_d_head_exp_eyebrows normal
                    with dissolve

                    p "Desde luego,"

                    show gensex_missionary_d_head_exp_mouth sadbiting_Silentx06
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows sadx07
                    with dissolve

                    p "me dio la sensación que ayer lo disfrutaste incluso más que yo..."

                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx04
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils right05
                    show gensex_missionary_d_head_exp_eyebrows sadx04
                    with dissolve

                    d "..."

                    show gensex_missionary_d_head_exp_mouth happybiting_Silentx07
                    show gensex_missionary_d_head_exp_eyes 08
                    show gensex_missionary_d_head_exp_pupils front07
                    show gensex_missionary_d_head_exp_eyebrows angryx04
                    with dissolve

                    d "Tssk..."

                    show gensex_missionary_d_head_exp_mouth happy_Talkingx04
                    show gensex_missionary_d_head_exp_eyes 05
                    show gensex_missionary_d_head_exp_pupils front05
                    show gensex_missionary_d_head_exp_eyebrows angryx03
                    with dissolve

                    d "Lo de que te follen por la mañana no te va muy bien para el riego sanguíneo..."

            else:

                $pl.ch_pts("dp",-1)

                show morning04_bg bedroom_neus_a
                show kiss_ n_d_01:
                    transform_anchor True
                    xalign 0.5 yalign 0.5
                    zoom 1.4 xpos 0.5 ypos 0.35 rotate -90
                with fade

                d "¡¿HHMMM?!"

                hide morning04_bg
                hide kiss_

                show gensex_missionary_d_head_exp_mouth sad_Talkingx16
                show gensex_missionary_d_head_exp_eyes 00
                show gensex_missionary_d_head_exp_pupils front00
                show gensex_missionary_d_head_exp_eyebrows angryx08
                with hpunch

                d "¡¿QUÉ COÑO HACES IMBÉCIL?!"

                show gensex_missionary_d_head_exp_mouth sad_Silentx11
                show gensex_missionary_d_head_exp_eyes 02
                show gensex_missionary_d_head_exp_pupils front02
                show gensex_missionary_d_head_exp_eyebrows angryx08
                with dissolve

                p "..."

                show gensex_missionary_d_head_exp_mouth sad_Silentx13
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx07
                with dissolve

                pt "Quizás ha sido una mala idea..."

                show gensex_missionary_d_head_exp_mouth sad_Silentx07
                show gensex_missionary_d_head_exp_eyes 05
                show gensex_missionary_d_head_exp_pupils front05
                show gensex_missionary_d_head_exp_eyebrows angryx07
                with dissolve

                if afternight04__MMouth_Tongue_Deep_Failed > 0:

                    pt "teniendo en cuenta que ayer fue un fracaso absoluto."

                else:

                    pt "teniendo en cuenta que ayer ni siquiera lo intenté..."

            jump morning05_DidacSex_Fucking_Kiss_After

        "Mejor no...":

            call p_Help

            jump morning05_DidacSex_Fucking_Kiss_After

label morning05_DidacSex_Fucking_Kiss_After:

    $ morning05_missionary_face_cond_empty = False
    $ morning05_missionary_face_cond_surprise = False
    $ morning05_missionary_face_cond_malicious = False
    $ morning05_missionary_face_cond_horny = True

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = True # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 3.0 ypos 1.25 # Face Good
        easein_quad 5.0 zoom 1.5 ypos 0.26 # Pussy
    show light_screen_01:
        light_screen_01_position
    with fade

    pause

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = True # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        #zoom 3.0 ypos 1.25 # Face Good
        zoom 1.5 ypos 0.26 # Pussy
        block:
            easein_quad 0.25 ypos 0.3
            easeout_quad 0.25 ypos 0.26
            repeat
    show light_screen_01:
        light_screen_01_position
    with dissolve

    d "¡Por tu puta madre!"

    d "¡Ni se te ocurra parar!"

#########################################################
    
    if config.version < "00.10.04": # Climax Sex With Didac in the morning.
        
        call endupdatescript
    
#######################################################

    if morning05_DidacSex_Pussy_Cond == True and DidacMCPregnant == True:

        p "Dídac,"

        extend " quita tus piernas de mí o no podré apartarme cuando me corra..."

        d "¡He dicho que no pares!"

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = True # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        #zoom 3.0 ypos 1.25 # Face Good
        zoom 1.5 ypos 0.26 # Pussy
        block:
            easein_quad 1.0 ypos 0.3
            easeout_quad 1.0 ypos 0.26
            repeat
    show light_screen_01:
        light_screen_01_position
    with dissolve

    n "Inconscientemente disminuyes ligeramente el ritmo debido a que sientes el flujo seminal a punto de estallar,"

    #$ morning05_DidacSex_Anal_Cond = False # TEST

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = True # Raped
    $ morning05_missionary_cond_09 = False # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 1.5 ypos 0.3
        block:
            easein_quad 1.0 ypos 0.5
            easeout_quad 1.0 ypos 0.3
            repeat
    show light_screen_01:
        light_screen_01_position
    with dissolve

    n "Pero Dídac decide ocupar tu lugar y seguir con el mismo ritmo,"

    n "impidiéndote así poder recuperarte lo más mínimo."

    p "¡No puedo más!"

    p "Me voy a correr..."

    #d "*gemido* AAAHhh..."
    d "Aaaahh..." # Feminine Moan

    if morning05_DidacSex_Pussy_Cond == True and DidacMCPregnant == True:

        p "¡Que no llevo condón gilipollas!"

    pt "¡¿Me está ignorando?!"

    $ morning05_missionary_cond_01 = False # Starting Machine
    $ morning05_missionary_cond_02 = False# Rubbing
    $ morning05_missionary_cond_03 = False # Slow Fuck
    $ morning05_missionary_cond_04 = False # Fast Fuck
    $ morning05_missionary_cond_05 = False # She Rubbing you
    $ morning05_missionary_cond_06 = False # She Rubbing you FAST
    $ morning05_missionary_cond_07 = False # Half Dick
    $ morning05_missionary_cond_08 = False # Raped
    $ morning05_missionary_cond_09 = True # Raped Fast

    scene morning05_missionary_anim 01:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 1.5 ypos 0.3
        block:
            easein_quad 0.25 ypos 0.5
            easeout_quad 0.25 ypos 0.3
            repeat
    show light_screen_01:
        light_screen_01_position
    with dissolve

    pt "¡DIOS!"

    if morning05_DidacSex_Pussy_Cond == True and DidacMCPregnant == True:

        p "¡Aparta tus putas piernas o me voy a correr dentro de ti!"

        p "¡VA EN SERIO!"

    show white:
        subpixel True
        additive 1.0
        easein_bounce 0.25 alpha 0.8
        easeout_bounce 1.0 alpha 0.0
        repeat
    with dissolve

    #Corrida

    show white:
        subpixel True
        additive 1.0
        alpha 0.0
        easein_quad 5.0 alpha 1.0

    pause 5.0

    if morning05_DidacSex_Pussy_Cond == True and DidacMCPregnant == True:

        $ morning05_DidacSex_Fucking_Kick_Cond = True

        scene black
        with hpunch

        play sound "audio/sfx/fall05.ogg"

        d "{size=32}¡AAAU!{/size}"

    scene black 
    with fade

    p "Joder..."

    if morning05_DidacSex_Pussy_Cond == True and morning05_DidacSex_UsingCondom_Cond == False: #Didac está en el suelo, te has corrido en la cama.

        p "ha ido por los pelos..."

        n "Tus sábanas han quedado completamente empapadas por tu semilla,"

        n "que paulatinamente se va enfriando."

    elif morning05_DidacSex_Pussy_Cond == True and morning05_DidacSex_UsingCondom_Cond == True: # El condón está lleno de semen, su coño empapado y abierto.

        p "Suerte que llevaba el condón puesto..."

    elif morning05_DidacSex_Anal_Cond == True or morning05_DidacSex_UsingCondom_Cond == False: # Su agujero anal está lleno de semen.

        p "Vaya corrida..."

    elif morning05_DidacSex_Anal_Cond == True or morning05_DidacSex_UsingCondom_Cond == True: # El condón lleno, su ano emapapado y abierto.

        p "Le he dejado el culo bonito..."

    else:

        pass # NOT FINISHED?

        $ debug ("Here goes a text, but it´s not written... Need more conditionals!")

    n "A medida que pasan los segundos vas recuperando el aliento."

    scene morning05_missionary_anim after:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 1.5 xpos 0.4 ypos -0.1
        easein_quad 30.0 zoom 0.5 xpos 0.5 ypos 0.5 #Whole image?
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade

    pause

    if morning05_DidacSex_UsingCondom_Cond == True:

        n "En convulsiones, Dídac se encuentra temblando mientras gime de forma descontrolada encima de la cama con los ojos en blanco."

        n "Poco después de descargar toda tu leche en el preservativo, perdió su fuerza, y con extraños espasmos,"

        n "se desplomó encima de la cama moviéndose incontroladamente,"

        n "mientras tu polla sigue bañándose entre tu semilla rodeada de plástico."

    elif morning05_DidacSex_Pussy_Cond == True: # Not necessary the condom, is already top.

        n "Pero no puedes evitar mirar al suelo donde has propulsado con una fuerte patada a Dídac en el último instante."

        p "Será posible..."

        n "En convulsiones, Dídac se encuentra temblando mientras gime de forma descontrolada con los ojos en blanco."

    elif morning05_DidacSex_Anal_Cond == True:

        n "En convulsiones, Dídac se encuentra temblando mientras gime de forma descontrolada encima de la cama con los ojos en blanco."

        n "Poco después de descargar toda tu leche dentro de su cavidad anal, perdió su fuerza y con extraños espasmos,"

        n "se desplomó encima de la cama moviéndose incontroladamente,"

        n "mientras tu semilla sigue brotando de entre sus nalgas empapándote las sábanas."

    hide morning04_bedroom_DMast_blinkeye
    show eyeopen01
    with dissolve

    #d "*gemido exasperante* AA-Ahh-AHhh..."
    d "AA-Ahh-AHhh..." # Maddening Moan (Having an orgasm)

    pt "¿Está teniendo un orgasmo?"

    pt "¿O tengo que llamar a un exorcista?"

    p "Dídac,"

    extend " ¿te encuentras bien?"

    if morning05_DidacSex_Anal_Cond == True:

        d "Ca-"

        extend "ca-"

        extend "bró-"

        extend "óoon"

        d "me-"

        extend "me due-"

        extend "ee-"

        extend"leee..."

        p "Hombre,"

        p "claro que te duele;"

        p "meterla así de golpe sin lubricante ni nada con el tamaño que tengo es lo que tiene."

        p "Pero no te la iba a meter de nuevo en el coño."

        p "¡Idiota de las narices!"

        p "Aunque por lo que veo tampoco es que te haya disgustado tanto,"

        p "viendo el orgasmo que estás teniendo..."

    d "Hi-"

    extend "hijo..."

    extend " de..."

    extend " puuu-"

    extend "uu..."

    if morning05_DidacSex_Pussy_Cond == True:

        p "¡Estás jodidamente enfermo maldito majara!"

        p "¡Debería haberme corrido dentro de ti!"

    #d "*gemido exasperante* AA-Ahh-AHhh..."
    d "AA-Ahh-AHhh..." # Maddening Moan (Having an orgasm)

    if morning05_DidacSex_UsingCondom_Cond == True:

        pt "En realidad el haber usado condón no es que me convierta en el mejor ejemplo de amigo posible,"

        pt "teniendo en cuenta que la forma en la que actúa no tiene nada que ver con el Dídac que yo conozco..."

        pt "Pero es mejor correrme con la seguridad de un chubasquero,"

        pt "que dejarlo preñado y condenarlo a ser una puta ninfómana de por vida..."

    elif morning05_DidacSex_Pussy_Cond == True:

        pt "En realidad no sé por qué me he apartado,"

        pt "mi cuerpo se ha movido solo..."

        pt "Supongo que en el fondo del fondo,"

        pt "sigo pensando que Dídac no es realmente así"

        pt "y no se merece que lo condene a una vida perpetua como algo que no es..."

        n "Sigue en el suelo, pero sus espasmos son cada vez más sutiles y espaciados en el tiempo."

        pt "Esta situación se me ha ido completamente de las manos..."

        pt "Tengo que arreglarlo lo antes posible con Neus,"

        pt "o realmente acabaré dejando preñado a Dídac..."

        p "..."

        pt "¡No!"

        extend " ¡No puedo dejar que Dídac se mantenga como una puta ninfómana...!"

        pt "Aunque vaya polvos me montaría cada día..."

        p "..."

        pt "¿De verdad me estoy planteando esto en serio?"

        pt "¡¿Acaso alguien está tomando decisiones por mí?!"

        p "..."

        pt "Pero vaya puto orgasmo..."

        p "..."

        pt "Estoy fatal..."

    elif morning05_DidacSex_Anal_Cond == True:

        pt "En realidad correrme dentro de su culo mientras tenía toda mi polla dentro,"

        pt "no es que me convierta en el mejor ejemplo de amigo posible,"

        pt "teniendo en cuenta que la forma en la que actúa no tiene nada que ver con el Dídac que yo conozco..."

        pt "Pero es mejor correrme en su culo que dejarlo preñado y condenarlo a ser una puta ninfómana de por vida..."

    pt "Lo mejor será desayunar algo y recuperar las fuerzas antes de que se me vaya completamente la cabeza..."

    window hide dissolve
    pause

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    play music "audio/sfx/shower01.ogg" fadein 3.0 fadeout 3.0

    scene afternight03_bg shower
    with fade

    n "Decides dejar reposar a Dídac, que -poco a poco- se va recuperando del reciente y escalofriante orgasmo."

    $ morning05_DidacSex_WasGood = True

    jump morning05_AfterShower

label morning05_AfterShower:

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0

    scene morning04_bg_livingroom_dbreakfast_bikini
    #show morning04_bg_livingroom_dbreakfast_bikini_PROVE
    show morning04_bg_livingroom_dbreakfast_eyes closed:
        truecenter
        alpha 0.8
        xpos 0.748 ypos 0.299
    show light 01:
        light01_rightside_position
    #show light_screen_01:
        #light_screen_01_position
    with fade

    n "Después de una reconfortante y revitalizante ducha vuelves a la sala más grande del piso,"

    n "donde te encuentras a Dídac tomando el desayuno con lo que parece un bikini de playa."

#########################################################
    
    if config.version < "00.10.05": # Talking about going to the beach or not.
        
        call endupdatescript
    
#######################################################

    

    if morning05_DidacSex_WasGood == True:

        scene morning04_bg_livingroom_others_morning

        show didacfbodybelow naked:
            dfbody_atright_little
        show didacfbodybelow_panties bikini:
            dfbody_atright_little
        show didacfbodybelow_naked_drops 00:
            dfbody_atright_little
        show didacfbodycloth_below empty:
            dfbody_atright_little
        show didacfhandrb spoon:
            dfbody_atright_little
        show didacfbodytop brabikini:
            dfbody_atright_little
        show didacfbodytop_naked_drops 00:
            dfbody_atright_little
        show didacfbodycloth_top empty:
            dfbody_atright_little
        show didacfhandl hip_naked:
            dfbody_atright_little
        show didacfhandr empty:
            dfbody_atright_little
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_little
        show didacf_blush 03:
            dfexpressions_atright_little
        show didacf_eyes 03:
            dfexpressions_atright_little
        show didacf_pupils front03:
            dfexpressions_atright_little
        show didacf_eyebrows angryx01:
            dfexpressions_atright_little
        show didacfbodytop_hair:
            dfbody_atright_little
        show didacf_mouth happy_Talkingx04:
            dfexpressions_atright_little
        show didacfbodycloth_whole empty:
            dfbody_atright_little

        show light 01:
            light01_rightside_position
        #show light_screen_01:
            #light_screen_01_position
        with fade

        d "Buenos días, semental."

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows angryx03
        show didacf_mouth happybiting_Silentx05
        with dissolve

        n "Una sonrisa pícara y algo escalofriante se dibuja en su rostro sin demasiado disimulo."

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows normal
        show didacf_mouth sad_Silentx03
        with dissolve

        p "..."

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows surprisex02
        show didacf_mouth sad_Silentx04
        with dissolve

        p "¿Por qué te has puesto un bañador?"

        show didacf_eyes 02
        show didacf_pupils down02
        show didacf_eyebrows normal
        show didacf_mouth sad_Talkingx002
        with dissolve

    else:

        show morning04_bg_livingroom_dbreakfast_eyes opened
        with dissolve

        n "Su mirada se cruza por un instante con la tuya,"

        show morning04_bg_livingroom_dbreakfast_eyes closed
        with dissolve

        n "como si de una mosca se hubiera tratado vuelve sus ojos al plato que estaba ya a punto de terminar."

        p "..."

        p "¿Por qué te has puesto un bañador?"

        scene morning04_bg_livingroom_others_morning

        show didacfbodybelow naked:
            dfbody_atright_little
        show didacfbodybelow_panties bikini:
            dfbody_atright_little
        show didacfbodybelow_naked_drops 00:
            dfbody_atright_little
        show didacfbodycloth_below empty:
            dfbody_atright_little
        show didacfhandrb spoon:
            dfbody_atright_little
        show didacfbodytop brabikini:
            dfbody_atright_little
        show didacfbodytop_naked_drops 00:
            dfbody_atright_little
        show didacfbodycloth_top empty:
            dfbody_atright_little
        show didacfhandl hip_naked:
            dfbody_atright_little
        show didacfhandr empty:
            dfbody_atright_little
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_little
        show didacf_blush 00:
            dfexpressions_atright_little
        show didacf_eyes 02:
            dfexpressions_atright_little
        show didacf_pupils down02:
            dfexpressions_atright_little
        show didacf_eyebrows angryx01:
            dfexpressions_atright_little
        show didacfbodytop_hair:
            dfbody_atright_little
        show didacf_mouth sad_Talkingx002:
            dfexpressions_atright_little
        show didacfbodycloth_whole empty:
            dfbody_atright_little

        show light 01:
            light01_rightside_position
        #show light_screen_01:
            #light_screen_01_position
        with fade


    d "Es evidente."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¿No has notado el calor que hace?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "El verano ya está aquí y sería de ser un completo deficiente mental no aprovechar un día de playa como hoy."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "A muchas ciudades ya les gustaría tener una playa como la {a=https://es.wikipedia.org/wiki/Playa_de_la_Barceloneta}{i}Barceloneta{/i}{/a}..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Dídac,"

    extend " ¿de verdad te estás planteando ir...?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡¿Y si no qué?!"

    if morning05_DidacSex_WasGood == True:
        show didacf_blush 02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡¿Quieres que me vuelva a pasar el día entero encerrado en casa?!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Ayer no te quedaste el día entero encerrado..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "Uy no,"

    extend " es verdad,"

    d "pude salir de compras porque el señorito me dio permiso..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve

    p "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "No tengo que pedirte permiso para nada,"

    d "¡estoy totalmente asfixiada aquí dentro!"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡Necesito salir!"

    if morning05_DidacSex_WasGood == True:
        show didacf_blush 01
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve

    p "Pero..."

    extend " ¿En bikini?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¿De qué tienes miedo?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡¿De que me violen en la playa?!"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡¿Pero tú dónde te crees que vives?!"

    d "¡¿En un videojuego porno?!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx07
    with dissolve

    p "..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Solo digo,"

    extend " que es arriesgado..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "Tú estás enfermo [protname]..."

    if morning05_DidacSex_WasGood == True:
        show didacf_blush 00
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Hay tantas probabilidades de que me violen a pleno día en una playa pública de Barcelona"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "como de que me caiga un meteorito ahora mismo."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve

    p "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "No me preocupa tanto lo que puedan hacerte los demás,"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "me preocupa más lo que tú puedas hacerles."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Lo dices como si fuera una enferma mental..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve

    menu morning05_mentallyill_question:
        
        pt "¿Se supone que ve normal todo lo que está haciendo?"
        
        "¿Y no es así?":
            
            call p_Help

            $pl.ch_pts("dp",-3)

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¿Por qué no te vas un poco a la mierda gilipollas?!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx08
            with dissolve

        "Eso lo has dicho tú, no yo.":
            
            call p_Help

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx05
            with dissolve

            d "Eres bastante gilipollas cuando quieres."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx05
            with dissolve

        "¿Realmente crees que actúas como siempre?":
            
            call p_Help

            $pl.ch_pts("dp",-1)

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx04
            with dissolve

            d "Vete un poco a la mierda..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx05
            with dissolve

    scene afternight03_bg entrance_lighton
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys

    show didacfbodybelow naked:
        dfbody_close_
    show didacfbodybelow_panties bikini:
        dfbody_close_
    show didacfbodybelow_naked_drops 00:
        dfbody_close_
    show didacfbodycloth_below empty:
        dfbody_close_
    show didacfhandrb empty:
        dfbody_close_
    show didacfbodytop brabikini:
        dfbody_close_
    show didacfbodytop_naked_drops 00:
        dfbody_close_
    show didacfbodycloth_top empty:
        dfbody_close_
    show didacfhandl hip_naked:
        dfbody_close_
    show didacfhandr empty:
        dfbody_close_
    show didacfhandl_hip_naked_drops 00:
        dfbody_close_
    show didacf_blush 00:
        dexpressions_close_
    show didacf_eyes 02:
        dexpressions_close_
    show didacf_pupils front02:
        dexpressions_close_
    show didacf_eyebrows angryx02:
        dexpressions_close_
    show didacfbodycloth_whole pareo_bagtowel:
        dfbody_close_
    show didacfbodytop_hair:
        dfbody_close_
    show didacf_mouth sad_Silentx04:
        dexpressions_close_

    with dissolve

    n "Rápidamente se pone el pareo encima, coge la toalla y su mochila dispuesta a salir por la puerta."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "Yo me voy,"

    d "tú haz lo que te dé la puta gana."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx03
    with dissolve

    menu morning05_gotobeachwithDidac_question:
        
        pt "¿Es buena idea dejar que vaya solo a la playa?"
        
        "<Ir con Dídac a la playa>":
            
            call p_Help

            $pl.ch_pts("dp",+1)

            p "No te pongas así..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows suspiciousx02
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Estoy de acuerdo contigo en que ir a la playa con el día que hace tampoco es una mala idea."

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx01
            with dissolve

            d "..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "¿Y ese cambio de humor?"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "No eres el único al que le gusta el mar."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "No me vayas de hipócrita,"

            d "nunca has venido conmigo a la playa,"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "¿y ahora mágicamente has cambiado de opinión?"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx04
            with dissolve

            p "Prefería ir solo a la playa que contigo."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "¡¿Por?!"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Porque no dejabas de molestar,"

            p "mostrar musculito y lucirte como un completo idiota,"

            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows sadx01
            show didacf_mouth sadbiting_Silentx02
            with dissolve

            p "ante la primera tía que te encontrabas;"

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows serious
            show didacf_mouth sadbiting_Silentx05
            with dissolve

            p "y si eran guiris,"

            extend " aún te volvías más insoportable."

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx03
            with dissolve

            d "..."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx05
            with dissolve

            d "Txxt..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx07
            with dissolve

            d "¿Y qué te hace pensar que ahora actuaré distinto...?"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx000
            with dissolve

            pt "Eso es precisamente lo que más me temo..."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx05
            with dissolve

            p "Tengo ganas de acompañarte,"

            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Silentx04
            with dissolve


            p "¿no quieres que venga?"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows suspiciousx02
            show didacf_mouth sad_Silentx03
            with dissolve

            d "..."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows surprisex02
            show didacf_mouth sad_Talkingx004
            with dissolve

            d "Bah..."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "Haz lo que te dé la gana..."

            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_eyebrows normal
            show didacf_mouth sad_Talkingx002
            with dissolve

            d "Al fin y al cabo,"

            extend " es un lugar público..."

            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx02
            with dissolve

            menu morning05_gotobeachwithDidac_swimsuit_question:
                
                pt "Ya, pero dudo que eso te impida hacer cosas de ámbito más privado..."
                
                "Además, ese traje de baño te queda muy bien.":
                    
                    call p_Help

                    $pl.ch_pts("dp",+2)

                    #Roja como un tomate.

                    show didacf_blush 03
                    show didacf_eyes 00
                    show didacf_pupils front00
                    show didacf_eyebrows surprisex02
                    show didacf_mouth sad_Silentx01
                    with dissolve

                    d "..."

                    show didacf_blush 04
                    show didacf_eyes 01
                    show didacf_pupils right01
                    show didacf_eyebrows suspiciousx02
                    show didacf_mouth sad_Talkingx002
                    with dissolve

                    d "Euhh..."

                "Además, siempre hay buenas vistas en la {i}Barceloneta{/i}...":
                    
                    call p_Help

                    $pl.ch_pts("dp",+1)

                    show didacf_eyes 03
                    show didacf_pupils front03
                    show didacf_eyebrows suspiciousx02
                    show didacf_mouth sad_Talkingx02
                    with dissolve

                    d "Eso no puedo negártelo..."

                    show didacf_eyes 02
                    show didacf_pupils front02
                    show didacf_eyebrows normal
                    show didacf_mouth sad_Silentx01
                    with dissolve

                    p "Por lo general,"

                    extend " en la playa sueles flirtear y mirar sin demasiado disimulo,"

                    p "las mujeres que deciden hacer {a=https://es.wikipedia.org/wiki/Toples}toples{/a}..."

                    show didacf_eyes 04
                    show didacf_pupils right04
                    show didacf_eyebrows suspiciousx01
                    show didacf_mouth sadbiting_Silentx02
                    with dissolve

                    d "..."

                    menu morning05_gotobeachwithDidac_swimsuit_question02:
                        
                        pt "Especialmente Dídac, la persona más insoportable y plasta que he conocido con las tías..."
                        
                        "Estoy convencido de que seguirás haciendo exactamente lo mismo con ellas...":
                            
                            call p_Help

                            show didacf_eyes 05
                            show didacf_pupils front05
                            show didacf_eyebrows serious
                            show didacf_mouth sadbiting_Silentx02
                            with dissolve

                            d "..."

                            show didacf_eyes 04
                            show didacf_pupils front04
                            show didacf_eyebrows angryx01
                            show didacf_mouth happy_Talkingx02
                            with dissolve

                            d "Que no te quepa duda,"

                            extend " imbécil."

                            jump morning05_gotobeachwithDidac

                        "Me pregunto si ahora tus ojos se fijarán en otra cosa...":
                            
                            call p_Help

                            #Roja como un tomate.

                            show didacf_blush 03
                            show didacf_eyes 01
                            show didacf_pupils front01
                            show didacf_eyebrows surprisex02
                            show didacf_mouth sad_Talkingx02
                            with dissolve

                            d "¿Qué...?"

                            show didacf_eyes 03
                            show didacf_pupils front03
                            show didacf_eyebrows suspiciousx02
                            show didacf_mouth sad_Talkingx004
                            with dissolve

                            d "¡¿Qué insinúas?!"

                            show didacf_eyes 04
                            show didacf_pupils front04
                            show didacf_eyebrows suspiciousx01
                            show didacf_mouth sad_Silentx01
                            with dissolve

                            if mc_body.orgasm >= 1:

                                $pl.ch_pts("dp",+2)

                                p "Hombre..."

                                p "después de lo de ayer,"

                                if morning05_DidacSex_WasGood == True:

                                    p "y lo de esta mañana,"

                                p "no vas a hacerte el mojigato ahora..."

                                show didacf_blush 04
                                show didacf_eyes 04
                                show didacf_pupils right04
                                show didacf_eyebrows sadx01
                                show didacf_mouth happybiting_Silentx03
                                with dissolve

                                d "..."

                                jump morning05_gotobeachwithDidac

                            elif afternight04_sexbattle_started == True:

                                $pl.ch_pts("dp",-2)

                                p "Hombre..."

                                p "después de lo de ayer..."

                                if morning05_DidacSex_WasGood == True:

                                    p "y lo de esta mañana,"

                                show didacf_eyes 05
                                show didacf_pupils front05
                                show didacf_eyebrows angryx02
                                show didacf_mouth sad_Talkingx05
                                with dissolve

                                d "¡si por lo menos hubieras hecho algo!"

                                show didacf_eyes 03
                                show didacf_pupils front03
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Silentx06
                                with dissolve

                                p "..."

                                if afternight04_didac_orgasms == 0:

                                    show didacf_eyes 05
                                    show didacf_pupils front05
                                    show didacf_eyebrows angryx04
                                    show didacf_mouth sad_Talkingx07
                                    with dissolve

                                    d "¡Tanta cháchara y estupidez,"

                                    d "para que luego no tuviera ni un puto mísero orgasmo de mierda!"

                                elif afternight04_didac_orgasms == 1:

                                    show didacf_eyes 01
                                    show didacf_pupils front01
                                    show didacf_eyebrows angryx01
                                    show didacf_mouth sad_Silentx04
                                    with dissolve

                                    p "Por lo menos tuviste un orgasmo."

                                    show didacf_eyes 03
                                    show didacf_pupils front03
                                    show didacf_eyebrows angryx03
                                    show didacf_mouth sad_Talkingx07
                                    with dissolve

                                    d "¡Tú lo has dicho!"

                                    show didacf_eyes 05
                                    show didacf_pupils front05
                                    show didacf_eyebrows angryx04
                                    show didacf_mouth sad_Talkingx07
                                    with dissolve

                                    d "¡Un puto orgasmo de mierda!"

                                elif afternight04_didac_orgasms == 2:

                                    show didacf_eyes 01
                                    show didacf_pupils front01
                                    show didacf_eyebrows angryx01
                                    show didacf_mouth sad_Silentx03
                                    with dissolve

                                    p "Por lo menos tuviste dos orgasmos."

                                    show didacf_eyes 02
                                    show didacf_pupils front02
                                    show didacf_eyebrows angryx03
                                    show didacf_mouth sad_Talkingx07
                                    with dissolve

                                    d "¡¿Y te parecen muchos?!"

                                elif afternight04_didac_orgasms == 1:

                                    show didacf_eyes 02
                                    show didacf_pupils front02
                                    show didacf_eyebrows angryx01
                                    show didacf_mouth sad_Silentx03
                                    with dissolve

                                    p "Por lo menos tuviste tres orgasmos."

                                    show didacf_eyes 04
                                    show didacf_pupils front04
                                    show didacf_eyebrows angryx02
                                    show didacf_mouth sad_Talkingx04
                                    with dissolve

                                    d "¿Y crees que con tres tuve suficiente?"

                                elif afternight04_didac_orgasms >= 4:

                                    show didacf_eyes 01
                                    show didacf_pupils front01
                                    show didacf_eyebrows surprisex01
                                    show didacf_mouth sadbiting_Silentx02
                                    with dissolve

                                    p "Por lo menos tuviste [afternight04_didac_orgasms] orgasmos."

                                    show didacf_eyes 05
                                    show didacf_pupils right05
                                    show didacf_eyebrows angryx02
                                    show didacf_mouth sadbiting_Silentx05
                                    with dissolve

                                    d "..."

                                show didacf_eyes 05
                                show didacf_pupils front05
                                show didacf_eyebrows angryx02
                                show didacf_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                jump morning05_gotobeachwithDidac

                            else:

                                $pl.ch_pts("dp",-1)

                                p "Hombre,"

                                extend " después de cómo te pusiste ayer para que..."

                                show didacf_eyes 02
                                show didacf_pupils front02
                                show didacf_eyebrows angryx02
                                show didacf_mouth sad_Talkingx004
                                with dissolve

                                d "Sí [protname],"

                                extend " sí."

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Talkingx004
                                with dissolve

                                d "Lo sé..."

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx04
                                show didacf_mouth sad_Talkingx05
                                with dissolve

                                d "Me quedó clarísimo ayer."

                                show didacf_eyes 05
                                show didacf_pupils front05
                                show didacf_eyebrows angryx04
                                show didacf_mouth sad_Talkingx06
                                with dissolve

                                d "¡¿Podemos dejar ese tema de una vez?!"

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Silentx07
                                with dissolve

                                p "..."

                                jump morning05_gotobeachwithDidac

                        "¿Vas a fijarte ahora en los paquetes de los tíos con el mismo disimulo?":
                            
                            call p_Help

                            #Roja como un tomate.

                            show didacf_blush 02
                            show didacf_eyes 00
                            show didacf_pupils front00
                            show didacf_eyebrows surprisex02
                            show didacf_mouth sad_Talkingx002
                            with dissolve

                            d "¡¿Qué?!"

                            show didacf_eyes 03
                            show didacf_pupils front03
                            show didacf_eyebrows angryx02
                            show didacf_mouth sad_Talkingx07
                            with dissolve

                            d "¡¿Tú eres imbécil o qué?!"

                            show didacf_eyes 04
                            show didacf_pupils front04
                            show didacf_eyebrows angryx01
                            show didacf_mouth sad_Silentx04
                            with dissolve

                            if mc_body.orgasm >= 1:

                                $pl.ch_pts("dp",+3)

                                p "Después de lo de ayer,"

                                if morning05_DidacSex_WasGood == True:

                                    p "y lo de esta mañana,"

                                p "no vas a hacerte ahora el mojigato..."

                                show didacf_blush 04
                                show didacf_eyes 01
                                show didacf_pupils front01
                                show didacf_eyebrows surprisex01
                                show didacf_mouth sadbiting_Silentx02
                                with dissolve

                                p "Con lo que disfrutaste de mi polla,"

                                show didacf_eyes 03
                                show didacf_pupils right03
                                show didacf_eyebrows angryx02
                                show didacf_mouth sadbiting_Silentx05
                                with dissolve

                                p "estoy convencido de que poco o nada,"

                                p "vas a fijarte ahora en lo que solías,"

                                show didacf_eyes 04
                                show didacf_pupils right04
                                show didacf_eyebrows sadx01
                                show didacf_mouth sad_Talkingx000
                                with dissolve

                                p "y que ahora vas a dirigir tu objetivo en otros sujetos,"

                                show didacf_eyes 05
                                show didacf_pupils right05
                                show didacf_eyebrows sadx01
                                show didacf_mouth sad_Silentx03
                                with dissolve

                                p "y especialmente en otra parte de la anatomía masculina..."

                                show didacf_eyes 05
                                show didacf_pupils front05
                                show didacf_eyebrows angryx01
                                show didacf_mouth sad_Talkingx002
                                with dissolve

                                d "Imbécil."

                                show didacf_eyes 01
                                show didacf_pupils front01
                                show didacf_eyebrows surprisex01
                                show didacf_mouth sad_Silentx03
                                with dissolve

                                p "Perra en celo."


                                show didacf_eyes 05
                                show didacf_pupils right05
                                show didacf_eyebrows angryx02
                                show didacf_mouth sad_Silentx05
                                with dissolve

                                d "..."

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx01
                                show didacf_mouth sad_Talkingx001
                                with dissolve

                                d "Eres un gilipollas de campeonato."

                                show didacf_eyes 04
                                show didacf_pupils left04
                                show didacf_eyebrows suspiciousx01
                                show didacf_mouth sad_Silentx02
                                with dissolve

                                p "Y aun así, no puedes disimular lo cachonda que te pones"

                                p "al imaginar tantas pollas cerca de ti..."

                                show didacf_eyes 05
                                show didacf_pupils front05
                                show didacf_eyebrows angryx01
                                show didacf_mouth sad_Silentx03
                                with dissolve

                                d "..."

                                show didacf_eyes 08
                                show didacf_pupils front08
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Silentx04
                                with dissolve

                                p "¿O es que realmente solo disfrutas exclusivamente con la mía?"

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Talkingx06
                                with dissolve

                                d "¡Cállate ya joder!"

                                show didacf_eyes 03
                                show didacf_pupils front03
                                show didacf_eyebrows angryx02
                                show didacf_mouth sadbiting_Silentx02
                                with dissolve

                                p "Sabes que tengo razón..."

                                show didacf_eyes 05
                                show didacf_pupils right05
                                show didacf_eyebrows angryx01
                                show didacf_mouth sadbiting_Silentx05
                                with dissolve

                                d "..."

                                pt "Siempre me ha resultado fácil provocarlo,"

                                pt "pero ahora no solo se cabrea..."

                                jump morning05_gotobeachwithDidac

                            elif afternight04_sexbattle_started == True:

                                $pl.ch_pts("dp",-2)

                                p "Después de lo de ayer,"

                                if morning05_DidacSex_WasGood == True:

                                    p "y lo de esta mañana,"

                                p "no vas a hacerte ahora el mojigato..."

                                show didacf_eyes 03
                                show didacf_pupils front03
                                show didacf_eyebrows angryx02
                                show didacf_mouth sad_Talkingx04
                                with dissolve

                                d "¡¿Después de qué?!"

                                if afternight04_LeavingSexBattle == True:

                                    show didacf_eyes 04
                                    show didacf_pupils front04
                                    show didacf_eyebrows angryx04
                                    show didacf_mouth sad_Talkingx06
                                    with dissolve


                                    d "¡¿De que me dejaras a medias por la puta cara?!"

                                else:

                                    show didacf_eyes 04
                                    show didacf_pupils front04
                                    show didacf_eyebrows angryx03
                                    show didacf_mouth sad_Talkingx05
                                    with dissolve

                                    d "¡¿De que te corrieras tres jodidas veces sin que yo tuviera un solo puto orgasmo?!"

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                jump morning05_gotobeachwithDidac

                            else: #Not even Sex Battle.

                                $pl.ch_pts("dp",-1)

                                p "Después de cómo insististe ayer..."

                                show didacf_eyes 04
                                show didacf_pupils front04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Talkingx004
                                with dissolve

                                d "Sí,"

                                extend " insistí mucho,"

                                d "y tú eres el jodido amigo del puto año..."

                                show didacf_eyes 03
                                show didacf_pupils front03
                                show didacf_eyebrows angryx04
                                show didacf_mouth sad_Talkingx05
                                with dissolve

                                d "¡¿Podemos dejar el tema de ayer de una puta vez?!"

                                show didacf_eyes 04
                                show didacf_pupils right04
                                show didacf_eyebrows angryx03
                                show didacf_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                jump morning05_gotobeachwithDidac



        "<Decirle que tienes otros planes>":
            
            call p_Help

            $pl.ch_pts("dp",-2)

            #n "Rápidamente se pone pone el pareo encima y coge su mochila dispuesta a salir por la puerta."

            #d "Yo me voy, tú haz lo que te de la puta gana."

            p "Tú sabrás..."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx05
            with dissolve

            d "¿Qué insinúas con eso?"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Después de lo desesperada por follar que estuviste ayer..."

            if afternight04_didac_orgasms >= 1:

                # idac sonrojada.

                show didacf_blush 03
                show didacf_eyes 04
                show didacf_pupils right04
                show didacf_eyebrows suspiciousx01
                show didacf_mouth sadbiting_Silentx05
                with dissolve

                d "..."

            elif afternight04_sexbattle_started == True:

                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                show didacf_mouth sad_Talkingx04
                with dissolve

                d "Y para lo que me sirvió..."

            else: #Not even Sex Battle.

                show didacf_eyes 03
                show didacf_pupils front03
                show didacf_eyebrows angryx03
                show didacf_mouth sad_Talkingx06
                with dissolve

                d "No me lo recuerdes..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "¿Crees que es buena idea ir a un lugar rodeado por tus antiguos semejantes luciendo poca ropa?"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows suspiciousx02
            show didacf_mouth sad_Talkingx04
            with dissolve

            d "¡¿Por antiguos semejantes?!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "¡¿A qué coño te refieres?!"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx01
            with dissolve

            p "Cierrabares,"

            extend " cantamañanas,"

            extend " picaflores,"

            extend " asaltacunas,"

            extend " caza-chochos..."

            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows angryx02
            show didacf_mouth sadbiting_Silentx02
            with dissolve

            d "..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Oh..."

            extend " perdona,"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx04
            with dissolve

            p "¿cómo llamas entonces a lo que hacías cuando te follabas a la primera borracha que convencías"

            p "prometiéndole amor eterno"

            show didacf_eyes 02
            show didacf_pupils left02
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx05
            with dissolve

            p "y luego la dejabas tirada antes de que saliera el sol?"

            show didacf_eyes 04
            show didacf_pupils left04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx06
            with dissolve

            d "..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx04
            with dissolve

            d "Nunca prometí amor eterno..."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx06
            with dissolve

            p "{i}Eres la única persona con dos corazones,"

            extend " el tuyo y el mío.{/i}"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx07
            with dissolve

            p "{i}¿Acaba de salir el sol?,"

            extend " ¿o me has sonreído?{/i}"

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx08
            with dissolve

            p "{i}Casi temo tanto a la muerte,"

            extend " como a la posibilidad de no volver a verte.{/i}"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¡BUENO YA BASTA!!"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx004
            with dissolve

            d "¡¿NO?!"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "Con un ejemplo ya te entendí."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx08
            with dissolve

            p "Aparte de ser tremendamente cutres,"

            p "son más trilladas que la polla de {a=https://es.wikipedia.org/wiki/Julio_Iglesias}{i}Julio Iglesias{/i}{/a}..."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx06
            with dissolve

            d "..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx05
            with dissolve

            p "Una cosa sí te concedo."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx06
            with dissolve

            p "Si conseguías conquistarlas con semejantes flirteos,"

            p "se merecían el trato que les dabas."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx09
            with dissolve

            d "..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "Mira..."

            extend " ¿Por qué no te vas un poco...?"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx09
            with dissolve

            d "¡¡A LA PUTA MIERDA!!"
            play sound "audio/sfx/metal_keys_deposit.ogg"
            pause 0.2
            play sound "audio/sfx/door_slam01.ogg"

            scene afternight03_bg entrance_lighton
            show afternight03_bg_entrance_keysd empty
            with hpunch

            n "Rápidamente sale del piso dando un portazo."

            p "Si seguimos dándole ese trato a las puertas,"

            p "no ahorraremos demasiado en carpintería..."

            jump morning05_AfterDidac

        "<Insistir en que no es una buena idea que vaya>":
            
            call p_Help

            $pl.ch_pts("dp",-1)

            #n "Rápidamente se pone pone el pareo encima y coge su mochila dispuesta a salir por la puerta."

            #d "Yo me voy, tú haz lo que te de la puta gana."

            p "Dídac,"

            extend " insisto en que no es una buena idea."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "Y yo insisto en que me paso tu opinión por el forro de los cojones."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx01
            with dissolve

            p "..."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx03
            with dissolve

            p "Piénsalo fríamente."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows suspiciousx02
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Ayer me comentaste lo mal que lo pasaste durante todo el día,"

            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx04
            with dissolve

            p "lo caliente que estuviste yendo de un lado para otro."

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows sadx01
            show didacf_mouth sad_Silentx06
            with dissolve

            p "¡Hasta fuiste a una sex-shop para comprarte juguetes de todo tipo y ni eso te resultó útil!"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "No dije que no me fueran útiles..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx04
            with dissolve

            p "..."

            show didacf_blush 03
            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows sadx02
            show didacf_mouth sad_Silentx03
            with dissolve

            d "..."

            show didacf_blush 02
            show didacf_eyes 02
            show didacf_pupils right02
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "¡Me da igual!"

            show didacf_blush 02
            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx07
            with dissolve

            d "¡El caso es que quiero salir de aquí!"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Silentx01
            with dissolve

            p "¿Y crees que la playa es la mejor idea?"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx07
            with dissolve

            d "¡¿Prefieres que vaya a un puticlub?!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¿O qué?!"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Por la mañana no abren..."

            show didacf_eyes 03
            show didacf_pupils right03
            show didacf_eyebrows suspiciousx02
            show didacf_mouth sad_Talkingx003
            with dissolve

            d "Se nota que conoces poco Barcelona..."

            show didacf_blush 04
            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Silentx03
            with dissolve

            p "..."

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows sadx01
            show didacf_mouth sad_Talkingx000
            with dissolve

            d "..."

            show didacf_blush 03
            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx05
            with dissolve

            p "Dídac,"

            extend " sé razonable."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx04
            with dissolve

            p "Desde que te has convertido en chica,"

            p "¡actúas completamente distinto al Dídac que yo conozco!"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx07
            with dissolve

            d "¡Es evidente que he cambiado!"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¿Acaso no me ves?!"

            show didacf_blush 02
            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx03
            with dissolve

            p "Me refiero a tu forma de actuar..."

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx01
            with dissolve

            d "Me apetece ir a la playa,"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "y voy a ir."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "¡Te guste o no!"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx05
            with dissolve

            p "..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx01
            show didacf_mouth sad_Talkingx004
            with dissolve

            d "¡¿Acaso me lo vas a prohibir amordazándome y atándome a la cama o qué?!"

            show didacf_blush 04
            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            show didacf_mouth sad_Silentx01
            with dissolve

            p "Tengo unas esposas..."

            show didacf_blush 03
            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Talkingx07
            with dissolve

            d "¿Te estás cachondeando de mí?"

            show didacf_blush 02
            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx05
            with dissolve

            pt "No sé si es muy buena idea que se vaya ahí,"

            pt "quizás debería impedírselo a la fuerza"

            pt "para evitar que haga alguna tontería de la que luego se arrepienta..."

            menu morning05_TieAndGagDidac_question:
                
                pt "Aun así, no creo que vaya a ser fácil, sigue teniendo bastante fuerza..."
                
                "<Reducirla hasta llevarla a la habitación, esposarla y amordazarla>":
                    
                    call p_Help

                    $pl.ch_pts("dp",-5)

                    play sound "audio/sfx/fall01.ogg"
                    play music "audio/music/alcaknight/bury_it.ogg" fadein 3.0 fadeout 3.0

                    scene morning05_Against_bg:
                        transform_anchor True
                        xalign 0.5 yalign 0.5
                        zoom 0.5
                    #show morning05_Against_prove:
                        #transform_anchor True
                        #xalign 0.5 yalign 0.5
                        #zoom 0.5
                    show morning05_Against_D_body pareotowel_tensed_shadow:
                        transform_anchor True
                        xalign 0.5 yalign 0.5
                        zoom 0.5
                    show morning05_Against_D_exp_blush 03:
                        morning05_Against_D_exp_pos
                    show morning05_Against_D_exp_mouth sad_Silentx06:
                        morning05_Against_D_exp_pos
                    show morning05_Against_D_exp_eyes 06:
                        morning05_Against_D_exp_pos  
                    show morning05_Against_D_exp_pupils empty:
                        morning05_Against_D_exp_pos
                    show morning05_Against_D_exp_eyebrows angryx03:
                        morning05_Against_D_exp_pos
                    show morning05_Against_D_exp_hair_front:
                        morning05_Against_D_exp_pos

                    show N_Against_P_Arm:
                        transform_anchor True
                        xalign 0.5 yalign 0.5
                    show N_Against_P_Body:
                        transform_anchor True
                        xalign 0.5 yalign 0.5
                    with hpunch

                    pause 1.0

                    show morning05_Against_D_exp_blush 02
                    show morning05_Against_D_exp_mouth sad_Silentx07
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils prot_00
                    show morning05_Against_D_exp_eyebrows surprisex01
                    with dissolve

                    pause 1.0

                    show morning05_Against_D_exp_blush 01
                    show morning05_Against_D_exp_mouth sad_Talkingx03
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils prot_00
                    show morning05_Against_D_exp_eyebrows angryx02
                    with dissolve

                    d "¡¿Qué coño haces gilipollas?!"

                    show morning05_Against_D_exp_mouth sad_Silentx03
                    with dissolve

                    n "Del mismo modo que agarraste a Neus en clase,"

                    show morning05_Against_D_exp_mouth sad_Silentx04
                    with dissolve

                    n "esta vez es Dídac quien está sujeta por las muñecas contra la pared."

                    show morning05_Against_D_exp_mouth sad_Silentx05
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils prot_00
                    show morning05_Against_D_exp_eyebrows angryx02

                    show N_Against_P_Body Talking
                    with dissolve

                    p "Entiéndelo Dídac."

                    show morning05_Against_D_exp_mouth sad_Silentx04
                    show morning05_Against_D_exp_eyes 03
                    show morning05_Against_D_exp_pupils prot_03
                    show morning05_Against_D_exp_eyebrows angryx01
                    with dissolve

                    p "No estás bien,"

                    extend " no eres tú,"

                    show morning05_Against_D_exp_mouth sad_Silentx07
                    show morning05_Against_D_exp_eyes 03
                    show morning05_Against_D_exp_pupils prot_03
                    show morning05_Against_D_exp_eyebrows angryx02
                    with dissolve

                    p "si te dejo ir,"

                    p "harás cualquier tontería de la que luego te arrepentirás toda tu vida."

                    show morning05_Against_D_exp_mouth sad_Silentx08
                    show morning05_Against_D_exp_eyes 06
                    show morning05_Against_D_exp_pupils empty
                    show morning05_Against_D_exp_eyebrows angryx03
                    with dissolve

                    p "Es absurdo arriesgarse"

                    p "cuando esta noche tengo la última cita con la que hará que todo esto termine."

                    show morning05_Against_D_exp_mouth sad_Talkingx09
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils prot_00
                    show morning05_Against_D_exp_eyebrows angryx01
                    with dissolve

                    show N_Against_P_Body
                    with dissolve

                    d "¡¿No crees que eso es elección mía?!"

                    show morning05_Against_D_exp_mouth sad_Silentx07
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils prot_00
                    show morning05_Against_D_exp_eyebrows sadx01
                    with dissolve

                    show N_Against_P_Body Talking
                    with dissolve

                    p "¡Ni de coña!"

                    show morning05_Against_D_exp_mouth sad_Silentx08
                    show morning05_Against_D_exp_eyes 03
                    show morning05_Against_D_exp_pupils prot_03
                    show morning05_Against_D_exp_eyebrows serious
                    with dissolve

                    p "Después del comportamiento que he estado viendo estos últimos dos días,"

                    show morning05_Against_D_exp_mouth sad_Silentx09
                    show morning05_Against_D_exp_eyes 06
                    show morning05_Against_D_exp_pupils empty
                    show morning05_Against_D_exp_eyebrows angryx04
                    with dissolve

                    p "no puedo dejarte ir."

                    play sound "audio/sfx/hit02.ogg"

                    show morning05_Against_D_exp_mouth sad_Silentx08
                    show morning05_Against_D_exp_eyes 00
                    show morning05_Against_D_exp_pupils down_00
                    show morning05_Against_D_exp_eyebrows angryx04

                    hide N_Against_P_Body
                    hide N_Against_P_Arm
                    with vpunch

                    play sound "audio/sfx/fall11.ogg"

                    p "Ooooouuhhh..."

                    show morning04_bedroom_DMast_blinkeye

                    show morning05_Against_D_exp_mouth sad_Silentx07
                    show morning05_Against_D_exp_eyes 03
                    show morning05_Against_D_exp_pupils down_03
                    show morning05_Against_D_exp_eyebrows angryx04
                    with dissolve

                    n "Sientes el frío suelo en tus rodillas"

                    n "después de haber recibido uno de los peores golpes que puede recibir un hombre."

                    scene black
                    with fade

                    p "Una..."

                    extend " patada..."

                    extend " en los huevos..."

                    p "Eso es..."

                    extend " un golpe bajo..."

                    d "¡Lo tuyo sí ha sido un golpe bajo!"

                    scene afternight03_bg entrance_lighton
                    show afternight03_bg_entrance_keysd lighton:
                        afternight03_bg_entrance_keys
                    show afternight03_bg_entrance_keysmc lighton:
                        afternight03_bg_entrance_keys

                    show didacfbodybelow naked:
                        dfbody_close_
                    show didacfbodybelow_panties bikini:
                        dfbody_close_
                    show didacfbodybelow_naked_drops 00:
                        dfbody_close_
                    show didacfbodycloth_below empty:
                        dfbody_close_
                    show didacfhandrb empty:
                        dfbody_close_
                    show didacfbodytop brabikini:
                        dfbody_close_
                    show didacfbodytop_naked_drops 00:
                        dfbody_close_
                    show didacfbodycloth_top empty:
                        dfbody_close_
                    show didacfhandl hip_naked:
                        dfbody_close_
                    show didacfhandr empty:
                        dfbody_close_
                    show didacfhandl_hip_naked_drops 00:
                        dfbody_close_
                    show didacf_blush 00:
                        dexpressions_close_
                    show didacf_eyes 02:
                        dexpressions_close_
                    show didacf_pupils front02:
                        dexpressions_close_
                    show didacf_eyebrows angryx03:
                        dexpressions_close_
                    show didacfbodycloth_whole pareo_bagtowel:
                        dfbody_close_
                    show didacfbodytop_hair:
                        dfbody_close_
                    show didacf_mouth sad_Talkingx08:
                        dexpressions_close_

                    show morning04_bedroom_DMast_blinkeye

                    with dissolve

                    d "No me esperaba esto de tu parte..."

                    show didacf_blush 00
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx04
                    show didacf_mouth sad_Silentx08
                    with dissolve

                    p "Lo-"

                    extend "lo..."

                    extend " hago..."

                    extend " por tu bien..."

                    play sound "audio/sfx/metal_keys_deposit.ogg"

                    hide afternight03_bg_entrance_keysd

                    show didacf_blush 00
                    show didacf_eyes 03
                    show didacf_pupils front03
                    show didacf_eyebrows angryx04
                    show didacf_mouth sad_Silentx09
                    with dissolve

                    n "Rápidamente recoge sus cosas y se dirige a la puerta de entrada."

                    show didacf_eyes 02
                    show didacf_pupils front02
                    show didacf_eyebrows angryx04
                    show didacf_mouth sad_Talkingx09
                    with dissolve

                    d "Deja que decida yo lo que es o no por mi bien."

                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx04
                    show didacf_mouth sad_Talkingx05
                    #hide morning04_bedroom_DMast_blinkeye
                    with dissolve

                    d "Imbécil."

                    play sound "audio/sfx/door_slam01.ogg"

                    scene afternight03_bg entrance_lighton
                    show afternight03_bg_entrance_keysmc lighton:
                        afternight03_bg_entrance_keys
                    show morning04_bedroom_DMast_blinkeye
                    with hpunch

                    n "Con un portazo cierra la puerta que da a la escalera comunitaria."

                    n "Intentas con todas tus fuerzas ponerte de pie,"

                    play sound "audio/sfx/fall09.ogg"

                    n "pero el dolor es tan intenso que vuelves a perder las fuerzas y caer al suelo."

                    p "¡Me cago en todo!"

                    p "¡Debería haberle dado un golpe en la cabeza con una sartén o algo contundente para dejarlo inconsciente!"

                    p "..."

                    pt "¿A quién quiero engañar?"

                    pt "Nunca le he hecho esto a nadie y mucho menos soy capaz de hacérselo a Dídac..."

                    pt "por muy gilipollas que sea..."

                    pt "Dios..."

                    extend " mis huevos..."

                    n "Sigues retorciéndote por el suelo durante un tiempo hasta que recuperas la compostura,"

                    hide morning04_bedroom_DMast_blinkeye
                    with dissolve

                    n "para entonces, crees que es absurdo perseguirlo, mucho más ir en su búsqueda a la playa,"

                    pt "siendo temporada alta..."

                    pt "y a saber si habrá ido concretamente a la {i}Barceloneta{/i} o habrá elegido otro destino..."

                    jump morning05_AfterDidac

                "<Dejar que se vaya a la playa>":
                    
                    call p_Help

                    $pl.ch_pts("dp",1)

                    show didacf_blush 01
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx03
                    show didacf_mouth sad_Silentx03
                    with dissolve

                    p "Claro que es una broma..."

                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx01
                    show didacf_mouth sad_Silentx03
                    with dissolve

                    p "¿Quién soy yo para impedirte ir a cualquier parte,"

                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx01
                    show didacf_mouth sad_Silentx03
                    with dissolve

                    p "Ya eres mayorcito,"

                    extend " ¿O debería decir \"mayorcita\"?"

                    show didacf_blush 00
                    show didacf_eyes 08
                    show didacf_pupils front08
                    show didacf_eyebrows angryx01
                    show didacf_mouth sad_Silentx05
                    with dissolve

                    play sound "audio/characters/didac/pff01.ogg"

                    d "Pff..."

                    show didacf_eyes 04
                    show didacf_pupils front04
                    show didacf_eyebrows angryx02
                    show didacf_mouth sad_Talkingx06
                    with dissolve

                    d "Imbécil..."

                    show afternight03_bg_entrance_keysd empty
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows suspiciousx02
                    show didacf_mouth sad_Talkingx002
                    with dissolve

                    d "No te aburras demasiado sin mí."

                    scene afternight03_bg entrance_lighton
                    show afternight03_bg_entrance_keysmc lighton:
                        afternight03_bg_entrance_keys
                    with dissolve

                    n "Acto seguido cierra la puerta dejándote solo en el piso."

                    pt "¿Soy demasiado paranoico?"

                    pt "No creo que le vaya a pasar nada por ir a la playa en pleno día..."

                    pt "Además, al fin y al cabo ha sido su elección,"

                    pt "así que es cosa suya..."

                    jump morning05_AfterDidac

                "<Usar el maletín que te dio la rubia en el museo>" if p_prot_analgesic == "accepted":
                    call p_Help

                    jump afternight04_Didac_FuckMe_NCloro
  
label morning05_gotobeachwithDidac:

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "Bahh..."

    extend " da igual."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "Vayámonos antes de que se nos haga de noche..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happybiting_Silentx03
    with dissolve

    jump aftermorning05

label morning05_AfterDidac: #After a shower and Didac is not home.

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "bittersweet"

    scene morning04_livingroom_mc_resting_bg feet01
    with fade

    n "Decides tomar reposo donde sueles hacerlo en tu hogar,"

    n "en el cómodo sofá frente al televisor apagado."

    pt "Este panorama me recuerda al de ayer..."

label morning05_AfterDidac_02: #After a shower and Didac is not home.

    if afternoon04_TxellMacbaDate == True:

        if afternoon04_MACBA_TxellTruth_Cond == True:

            pt "La cita con Txell fue rara de narices..."

            if TxellSlave >= 1:

                pt "Aunque confieso que la idea de someterme a alguien con su experiencia y su figura,"

                if TxellSlave >= 1:

                    pt "no es una idea que me desagrade demasiado..."

                elif TxellSlave >= 3:

                    pt "es algo con lo que mi mente está fantaseando... "

                    pt "¡¿De verdad soy alguien tan sumiso?!"

                    pt "¡¿O es que alguien está tomando decisiones por mí?!"

            else:

                pt "¿Quién diablos se cree que es?"

                pt "Como si fuera a aceptar que una loca del coño me tratara como a un juguete..."

                pt "Pero no puedo negar que tiene un buen par de razones para ver dónde puede acabar todo esto..."

            pt "Especialmente después de lo que me comentó sobre lo de Neus..."

            pt "¿Por qué siempre me dejan a medias con sus explicaciones?"

            show morning04_bg_livingroom_mc_resting_phone 01:
                xpos 0.485 ypos 0.125
            show morning04_livingroom_mc_resting_handphone
            with dissolve

            n "Diestramente sacas el móvil de tu bolsillo y vuelves a tener en frente su número de teléfono a un clic de aceptar su oferta."

            pt "Me pregunto si en esta cita se comportará mejor o seguirá siendo..."

            call screen phonebuttons02()
            with dissolve

        else: #La cita fue un fracaso.

            pt "Maldita loca del coño..."

            if afternoon04_MACBA_Agent01Talk_Cond == True: #Habla con el agente 01 en el MACBA.

                pt "La muy zorra usó a un agente de seguridad del museo para que me echara del lugar..."

            else:

                pt "Ya no aguantaba más a esa tiparraca engreída."

            pt "¡¿Quién se ha creído que es?!"

            pt "{i}No me interesan los hombres,"

            extend " abajo el patriarcado...{/i}"
            
            if afternoon04_Q_ModernArt == True or afternoon04_Q_ClassicArt == True:

                pt "Tanta preguntita de arte de las narices..."

                if afternoon04_Q_ModernArt == True:

                    pt "{i}¿No sabes quién es el artista con {a=https://es.wikipedia.org/wiki/Enfermedad_de_Parkinson}enfermedad de Parkinson{/a} que vendía cuadros?...{/i}"

                    pt "¡Bendiciendo el PUTO cuadro con el pincel!"

                elif afternoon04_Q_ClassicArt == True:

                    pt "{i}Mira que no saber que el cuadro de un coño...{/i}"

                    pt "¡es el PUTO ORIGEN DEL MUNDO!"

                pt "{i}oooh..."

                extend " cuánta ignorancia...{/i}"

                p "¡A pollazos te tapaba la puta boca!"

                p "¡Gilipollas!"

            else:

                pt "Tiene narices,"

                extend " con lo simpática que parecía en clase..."

                pt "Y lo gilipollas que resultó ser en persona..."

                pt "¡A tomar por culo sus preguntitas de las narices!"

            p "..."

            pt "No puedo evitarlo..."

            pt "Me sacan de quicio la gente con estas ínfulas de sabelotodo..."

            $ morning05_TxellCall_rejected = True

            jump morning05_NeusFinalDate

    else: #You did not even had the date.

        pt "Desde luego,"

        pt "si no llamé ayer a la rubia tetona de clase,"

        pt "que fue cuando concertamos quedar..."

        pt "No voy a ser tan impresentable como para llamarla ahora..."

        $ morning05_TxellCall_rejected = True

        jump night05_NeusLastDate

label morning05_TxellCall_question_Accepted:

    $pl.ch_pts("mp",1)

    # No text is necessary here.

    jump afternoon05_TxellWorkPlace

label morning05_TxellCall_question_Refused:

    $pl.ch_pts("mp",-5)

    p "¿Para qué?"

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone
    with dissolve

    p "¿Para que me siga insultando y poniéndome a prueba como si fuera un mono de feria?"

    p "Además..."

    extend " ¿Qué puto problema tiene la tiparraca esta con los hombres?"

    $ morning05_TxellCall_rejected = True

    if aftermorning05_beachafter_Stay_GoTxellDate_Cond:

        jump aftermorning05_beachafter_Stay_SexNo_Leaving
        
    else:

        jump morning05_NeusFinalDate

label morning05_NeusFinalDate:

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    scene morning04_livingroom_mc_resting_bg feet01
    with fade

    if morning05_TxellCall_rejected == True:

        pt "Estaré mucho más tranquilo y a gusto en casa esperando que se haga de noche,"

        pt "para acudir a la última cita con Neus."

        n "Decides apartar de tu vista del teléfono y agarras el mando a distancia,"

        n "que se encuentra escondido entre los cojines."

    pt "Con más de sesenta canales a elegir y solo hacen basura,"

    pt "repiten lo mismo hasta la saciedad o cada veinte minutos hay un cuarto de hora de anuncios..."

    pt "¿Quién narices puede ver esta escoria hoy en día?"

    pt "Mejor me pongo {a=https://es.wikipedia.org/wiki/YouTube}{i}YouTube{/i}{/a} a ver si {a=https://www.youtube.com/channel/UCNYW2vfGrUE6R5mIJYzkRyQ}{i}Dross Rotzank{/i}{/a} o {a=https://www.youtube.com/channel/UCmaEoq1zaakpdudbzgll-zw}{i}Alva Majo{/i}{/a} han hecho algo nuevo,"

    pt "como mínimo me entretendrá algo más..."

    pt "Cuando se haga de noche tendré la última cita con Neus."

    if night04_Neus_Blowjob_Cum_Affirmative == True:

        pt "Y la verdad,"

        pt "después de lo que ocurrió anoche,"

        pt "tengo bastantes preguntas que hacerle..."

        pt "aunque no estoy seguro de si quiero saber la respuesta..."

    pt "Pero antes de salir..."

    pt "Voy a coger un juguete de los que se ha comprado Dídac."

    pt "De entre tantos,"

    pt "supongo que no echará en falta este."

    jump night05_NeusLastDate

    # Aquí es cuando decides acudir a la cita con Neus.

    





