default night05_Plaza_NeusLooking_BadAnswer_Cond = False # You told her you don´t like it.
default night05_Plaza_NeusLooking_Change_Cond_Yes = False # You asked her to change it.
default night05_Plaza_NeusLooking_EyesCursi_Cond = False # n realidad creo que resalta aún más el color esmeralda de tus ojos.

default neyesp = "" # Neus Eyes Painted
default mmouthp = "" # Meritxell mouth Painted. Empty is Default.

default deyesp = "" # Didac Eyes Painted.
default p_deyesp = "" # Didac Eyes Painted after Pedrera.

default night05_Funicular_Didac_Daddy_Cond = 0
default night05_Plaza_Food_Biscuit = False

default night05_Park_RollerCoaster_Used = False # If you both got in the RollerCoaster.
default night05_Park_Cups_Used = False



default night05_Park_RollerCoaster_Doubt = False # Dudas de que puedas decidir.
default night05_Park_RollerCoaster_Queuing_Enjoyed_Cond = False # Disfrutado haciendo cola de la montaña rusa.
default night05_Park_RollerCoaster_Queuing_Reproach_Cond = False # Reprocharle la cena vegana.
default night05_Park_RollerCoaster_Queuing_ThankHerForHonesty_Cond = False # Agradecerle la honestida de contarle lo de Dídac.

default night05_Park_MinigameShooter_Participate_Cond = False

default night05_Park_MinigameShooter_Participate_GoHome_Cond = False
default night05_Park_MinigameShooter_HowGood_NotGood = False

default night05_Park_MinigameShooter_Participate_RatAgainst_Cond = False
default night05_Park_MinigameShooter_After_RatLife_Cond = False

default MShooter_Present_Necklace_Ankh = False

default night05_Park_Bathroom_Sweet_Cond = False # AssJob in the Bathroom.
default night05_Park_Bathroom_Bad_Cond = False #She didn´t wanted stay in the bathroom.

default night05_Park_WC_NeusCry_BeingRude_Cond = False
default night05_Park_WC_NeusCry_BeingNice_Cond = False

default night05_Park_WC_Lawyer_Cunnilingus = False

default night05_Plaza_NeusLooking_Body_MiniSkirt_loliLike = False

label night05_NeusLastDate:

    if night05_DidacHome_NeusLate_Cond:
        scene bg night04_fnac_02
    else:
        scene bg night04_fnac_01
    with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    #########################################################
    
    if config.version < "00.11.02": # Wake Up by a BALL after massage. ## I put that here, so there´s a block.
        
        call endupdatescript
    
    #######################################################

    $ neyesp = "True" # Neus Eyes Painted
    
    p "Vaya..."
    if night05_DidacHome_NeusLate_Cond:
        $ saturation_tint_level = "verydark"

    else:
        $ saturation_tint_level = "dark"

    ne "¿Qué...?"

    play music "audio/music/alcaknight/are_you_still_dreaming.ogg" fadein 3.0 fadeout 3.0 

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris front01:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx05:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "¿Qué ocurre...?"

    show neus_exp_blush 03
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx04
    with dissolve

    if night05_DidacHome_NeusLate_Cond:

        n "Hace ya bastante rato que la noche caído"

    else:

        n "Apenas hace unos minutos que el sol yace bajo el horizonte,"

    show neus_exp_blush 03
    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx03
    with dissolve

    if night05_DidacHome_NeusLate_Cond:

        n "y a pesar de la hora que es, la calle está abarrotada de gente."

    else:

        n "y las calles cerca del centro comercial están incluso más abarrotadas que ayer."


    show neus_exp_blush 02
    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "¿No te gusta...?"

    if night05_DidacHome_NeusLate_Cond:

        show neus_exp_blush 03
        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with dissolve

        pt "A pesar de que llego como media hora más tarde de la hora acordada,"

        show neus_exp_blush 04
        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 05
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx03
        with dissolve

        pt "parece que le preocupa más lo que opino sobre su nueva vestimenta"

        pt "que otra cosa..."

    show neus_exp_blush 03
    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with dissolve

    pt "No solo lleva otro vestido,"

    show neus_exp_blush 02
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx03
    with dissolve

    pt "mucho más corto que ese traje victoriano de estos últimos dos días,"

    show neus_exp_blush 03
    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with dissolve

    pt "sino que además se ha pintado los ojos de modo cadavérico..."

    menu night05_Plaza_NeusLooking_question:
        
        pt "¿No era suficientemente gótica que tenía que pintarse los ojos?"

        "Pareces un personaje de las películas de Tim Burton.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            show neus_exp_blush 02
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "..."

            show neus_exp_blush 01
            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "¿Se supone que eso debe de hacerme gracia?"

            show neus_exp_blush 01
            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            p "..."

            menu night05_Plaza_NeusLooking_Burton_question:

                pt "Supongo que se imagina que me refiero las películas que hizo antes de los 2000..."

                "Lo decía como un cumplido.":

                    call p_Help

                    $pl.ch_pts("np",3)

                    show neus_exp_blush 03
                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows serious
                    with dissolve

                    ne "¿En serio...?"

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "¿No te estás cachondeando de mí?"

                    show neus_exp_mouth sad_Silentx02
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows serious
                    with dissolve

                    p "Ya sé que no es de ese director,"

                    show neus_exp_mouth sadbiting_Silentx01
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    p "¿pero has visto alguna vez lo sexy que está {a=https://es.wikipedia.org/wiki/Morticia_Addams}Morticia Addams{/a}?"

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "Como si de ella solo te fijaras en su cara..."

                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                    jump night05_Plaza_NeusLooking_GoodAnswer

                "Me gustabas más sin los ojos pintados.":

                    call p_Help

                    $pl.ch_pts("np",-1)

                    

                    jump night05_Plaza_NeusLooking_BadAnswer

        
        "En realidad, creo que resalta aún más el color esmeralda de tus ojos.":
            
            call p_Help

            $pl.ch_pts("np",2)

            $ night05_Plaza_NeusLooking_EyesCursi_Cond = True

            jump night05_Plaza_NeusLooking_GoodAnswer

        "Me gustabas más sin los ojos pintados.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            jump night05_Plaza_NeusLooking_BadAnswer

            # Surprise face

            ne "..."

        "Estás ridícula con los ojos pintados así.":
            
            call p_Help

            $pl.ch_pts("np",-3)

            show neus_exp_blush 01
            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx05
            with dissolve

            ne "¡Tampoco hace falta que seas tan explícito en tu opinión!"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx05
            with dissolve

            p "..."

            jump night05_Plaza_NeusLooking_BadAnswer


label night05_Plaza_NeusLooking_BadAnswer:

    $ night05_Plaza_NeusLooking_BadAnswer_Cond = True

    # Sad Face

    show neus_exp_blush 01

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "¿Preferirías que fuera a quitármelo entonces?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx06
    with dissolve

    menu night05_Plaza_NeusLooking_Change_question:

        pt "¿La prefiero sin la sombra de ojos?"

        "La verdad es que sí.":

            call p_Help

            $pl.ch_pts("np",-1)

            $ night05_Plaza_NeusLooking_Change_Cond_Yes = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx07
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 06
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx07
            with dissolve

            p "..."

            show neus_exp_mouth sad_Talkingx01
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Espérame aquí entonces."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            p "..."

            jump night05_Plaza_NeusLooking_BadAnswer_Change

        "No, prefiero que vistas lo que a ti te apetezca.":

            call p_Help

            $pl.ch_pts("np",3)

            ne "..."

            show neus_exp_blush 01
            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx05
            with dissolve

            p "A pesar de mi opinión,"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx06
            with dissolve

            p "eres tú quien debe sentirse cómoda vistiendo y maquillándote con lo que te apetezca,"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 06
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx05
            with dissolve

            p "o estarías disfrazando tu modo de ser para simplemente complacerme,"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx05
            with dissolve

            p "dejando de ser tú misma por completo."

            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_eyes 04
            show neus_exp_iris down04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx01
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "Ya..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Pero ahora ya sé que no te gusto así..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with dissolve

            p "Como habrá cosas que seguro que no te gustarán de mí."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows suspiciousx01
            with dissolve

            ne "Pero me las callo."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx02
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx03
            with dissolve

            pt "¡¿O sea que en verdad hay cosas que no le gustan de mí?!"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx04
            with dissolve

            pt "Será zorra..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "Espérame aquí."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows angryx01
            with dissolve

            p "¿Dónde vas?"

            jump night05_Plaza_NeusLooking_BadAnswer_Change

label night05_Plaza_NeusLooking_BadAnswer_Change:

    $ neyesp = "" # False Neus Eyes Painted

    if night05_DidacHome_NeusLate_Cond:
        show bg_night04_fnac_02

    else:
        show bg_night04_fnac_01
    with dissolve

    n "Sin mediar palabra,"

    n "se dirige hacia la gran superficie que hay detrás de ella."

    pt "¿Dónde diablos va?"

    if night05_DidacHome_NeusLate_Cond:

        n "Pocos minutos después:"

    else:

        n "Pocos minutos después,"

        show bg_night04_fnac_02
        with Dissolve (3.0)

        n "el tenue brillo solar desaparece del techo azul para volverse oscuro y estrellado."

    ne "¿Y bien?"

    hide bg_night04_fnac_02
    hide bg_night04_fnac_01
    show bg night04_fnac_02
    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Así mejor."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "¿No?"

    if night05_Plaza_NeusLooking_Change_Cond_Yes == True:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx02
        with dissolve

        p "La verdad es que sí."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Por lo menos eres sincero."

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx03
        with dissolve

        p "Es lo que me pediste ayer,"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx03
        with dissolve

        p "¿no es así?"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "..."

        $pl.ch_pts("np",1)

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Sí,"

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "eso es verdad..."

        jump night05_Plaza_WhereToGo

    else:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx04
        with dissolve

        p "Neus..."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx03
        with dissolve

        p "Te he dicho que no hacía falta."

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Lo sé."

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx04
        with dissolve

        ne "Pero preferiría que esta noche"

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "no me estuvieras viendo la cara pensando en todo momento"

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx06
        with dissolve

        ne "lo mal maquillada que estoy para tu gusto."

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "Ya tengo suficiente con que pienses lo bajita,"

        extend " plana,"

        extend " y cuatro ojos que soy."

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows sadx02
        with dissolve

        p "No he dicho nada de eso."

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "Pero lo piensas."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx05
        with dissolve

        p "..."

        jump night05_Plaza_NeusLooking_GoodAnswer

label night05_Plaza_NeusLooking_GoodAnswer:

    # Sad Face

    show neus_exp_blush 02
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "..."

    show neus_exp_blush 01
    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with dissolve


    ne "¿Solo te fijas en mis ojos porque el resto no te interesa?"

    
    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx03
    with dissolve

    p "Neus,"

    show neus_exp_blush 02
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with dissolve

    p "¿Cuándo te he dado razones para que te sientas tan insegura conmigo?"

    if night05_DidacHome_NeusLate_Cond:

        # NOT_FINISHED images

        ne "Hace más de una hora que estoy aquí esperando nuestra última cita,"

        ne "Es verdad que quizás he llegado un poco temprano,"

        ne "no voy a negar que estoy algo nerviosa..."

        ne "Pero a ti te he tenido que llamar"

        ne "para asegurarme de que realmente no te has olvidado de mi."

        ne "Creo que tengo razones para estar insegura,"

        ne "¿no crees?"

        p "..."

        ne "¿Realmente estás aquí por gusto,"

        ne "o por obligación?"

    else:

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx05
        with dissolve

        ne "Quizás es por el hecho de que sigo sin saber,"

        show neus_exp_blush 01
        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx04
        with dissolve


        ne "si estás aquí por gusto o por obligación..."

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx06
        with dissolve

    p "..."

    menu night05_Plaza_NeusLooking_GoodAnswer_Opinion_Question:

        "¿Acaso no es así?":

            call p_Help

            $pl.ch_pts("np",-2)

            jump night05_Plaza_NeusLooking_Body_Sad

        "Si no me quisieras aquí por obligación, le hubieras devuelto su cuerpo original antes de esta cita.":

            call p_Help

            $pl.ch_pts("np",1)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx06
            with dissolve

            ne "Te prometí que le devolvería su cuerpo original después de esta cita..."

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx04
            with dissolve

            p "Y sé que vas a cumplir tu palabra."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "¿Entonces por qué me dices esto?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows serious
            with dissolve

            p "Porque si igualmente lo vas a hacer,"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows normal
            with dissolve

            p "y no me quieres aquí con la duda de si lo hago por gusto o por obligación,"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            p "hubiera sido mejor salir de dudas quitando el chantaje que hay de por medio."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "Solo te he pedido tres citas..."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx01
            with dissolve

            p "Y aquí estaría igualmente."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "No lo creo..."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows angryx02
            with dissolve

            p "Siempre tan negativa..."

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Realista..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx04
            with dissolve

            p "..."

        "Si sigo aquí es por Dídac, no por ti.":

            call p_Help

            $pl.ch_pts("np",-3)

            jump night05_Plaza_NeusLooking_Body_Sad

        "Por favor, intenta pensar que no tengo una opinión tan negativa de ti.":

            call p_Help

            $pl.ch_pts("np",1)

    jump night05_Plaza_NeusLooking_Body


label night05_Plaza_NeusLooking_Body_Sad:

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "Lamento que te haya resultado tan desagradable tener que acudir a las tres citas que te he pedido."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows angryx02
    with dissolve

    p "No me lo has pedido,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx03
    with dissolve

    p "me lo has exigido."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Te dije que le devolvería su cuerpo original ocurriera lo que ocurriera."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with dissolve

    p "Y aun así sigue teniendo su cuerpo de mujer"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx05
    with dissolve

    p "y yo estoy aquí cumpliendo mi palabra."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx06
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Solo te pido que intentes disfrutar un poco de mi compañía..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "¿Tanto te pido?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx06
    with dissolve

    p "No disfruto demasiado las cosas con la sombra de un chantaje."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    jump night05_Plaza_NeusLooking_Body

label night05_Plaza_NeusLooking_Body:

    ne "..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx03
    with dissolve

    p "Aunque si debo serte sincero,"

    if night05_Plaza_NeusLooking_EyesCursi_Cond == True:

        show neus_exp_mouth sad_Silentx01
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx01
        with dissolve

        p "me ha parecido más inteligente ser cursi describiendo tus ojos,"

        show neus_exp_blush 03
        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
        with dissolve

        p "que intentar mantener las formas para describir el resto..."

    else:

        show neus_exp_mouth sadbiting_Silentx01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows serious
        with dissolve
        p "Si te he hablado de tus ojos,"

        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows surprisex01
        with dissolve

        p "era para intentar no perder las formas hablando del resto..."


    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Ah..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "¿Sí...?"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "¿Y cómo sonaría entonces?"

    show neus_exp_mouth happybiting_Silentx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve


    menu night05_Plaza_NeusLooking_Body_Question:

        pt "¿Por qué diablos tengo una erección si ni siquiera me ha tocado?"

        "Me gustabas más con el vestido largo.":

            call p_Help

            $pl.ch_pts("np",1)

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex02
            with dissolve


            ne "..."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows suspiciousx02
            with dissolve

            ne "Porque así parezco una niña..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows suspiciousx01
            with dissolve

            ne "¿No?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows suspiciousx01
            with dissolve

            p "Porque el otro vestido te hacía más elegante y misteriosa."

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "¿Es que así parezco una puta?"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx04
            with dissolve

            p "¿Por qué tienes que ser siempre tan negativa?"

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "¿Por qué no puedes decirme cosas bonitas?"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris left02
            show neus_exp_eyebrows angryx02
            with dissolve

            p "Porque me has pedido sinceridad desde la primera cita."

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx01
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Tienes razón..."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx02
            with dissolve

        "Creo que mi cuerpo responde mejor que mis palabras.":

            call p_Help

            $pl.ch_pts("np",2)

            jump night05_Plaza_NeusLooking_Body_Erection

        "Pareces una colegiala pervertida.":

            call p_Help

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows suspiciousx02
            with dissolve

            p "¿Qué?"

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "Porque parezco una niña,"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "¿verdad?"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx03
            with dissolve

            p "Eso lo has dicho tú."

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows angryx05
            with dissolve

            ne "¡¿Cuándo has visto a una adulta parecer una colegiala?!"

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx04
            with dissolve

            p "..."

            menu night05_Plaza_NeusLooking_Body_MiniSkirt_Question:

                pt "Hombre, esa minifalda..."

                "¿Y qué te hace pensar que eso no me pone?":

                    call p_Help

                    $pl.ch_pts("np",3)

                    $ night05_Plaza_NeusLooking_Body_MiniSkirt_loliLike = True

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows suspiciousx03
                    with dissolve

                    ne "¿Te va el rollo loli?"

                    show neus_exp_blush 02
                    show neus_exp_mouth sadbiting_Silentx01
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows surprisex02
                    with dissolve

                    p "Quizás me gusta eso en ti."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 02
                    show neus_exp_iris left02
                    show neus_exp_eyebrows suspiciousx02
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "Eres bien retorcido..."

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "¿Lo sabías?"

                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    p "¿Tiene algo de malo que me gustes como eres?"

                    show neus_exp_blush 03
                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyes 02
                    show neus_exp_iris left02
                    show neus_exp_eyebrows suspiciousx02
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx003
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    ne "Me cuesta creerte..."

                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    p "Pues si no me crees a mí,"

                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    p "mira al de abajo."

                    jump night05_Plaza_NeusLooking_Body_Erection

                "¿No querías sinceridad?":

                    call p_Help

                    $pl.ch_pts("np",-1)

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyes 02
                    show neus_exp_iris left02
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    ne "Sí..."

                    show neus_exp_mouth sad_Talkingx002
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "Pero esperaba que me tomaras un poco más en serio,"

                    show neus_exp_mouth sad_Talkingx01
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    ne "o por lo menos que mi aspecto físico no te resultara gracioso..."

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    p "..."


    jump night05_Plaza_WhereToGo

label night05_Plaza_NeusLooking_Body_Erection:

    show neus_exp_blush 06
    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris down02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "¿Hmmm...?"

    show neus_exp_mouth happybiting_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris down04
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "..."

    show neus_exp_blush 03
    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "¿Tan pronto...?"

    if night04_pedrera_blowjob_DONE == True:

        show neus_exp_mouth happy_Silentx06
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx03
        with dissolve

        p "Después de lo que ocurrió ayer..."

        show neus_exp_mouth happybiting_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_eyebrows sadx06
        with dissolve

        pt "por raro y bizarro que fuera,"

        show neus_exp_mouth happy_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx03
        with dissolve

        pt "mi imaginación no puede evitar divagar sola..."

    show neus_exp_blush 02
    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows surprisex01
    with dissolve

    n "Una risa tímida y femenina emerge de sus labios."

    jump night05_Plaza_WhereToGo

    ##

label night05_Plaza_WhereToGo:

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    p "¿A qué restaurante tienes pensado ir esta noche?"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    p "No puedo asegurarte nada,"

    show neus_exp_mouth happybiting_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows serious
    with dissolve

    p "pero te prometo que intentaré no ser tan pusilánime con la comida."

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Hoy no iremos a un restaurante."

    show neus_exp_mouth happy_Silentx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    p "¿Euh?"

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    p "¿Y dónde tienes pensado ir?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Ya lo verás."

    show neus_exp_mouth happy_Silentx08
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows surprisex01
    with dissolve

    n "Con una inocencia pueril te dedica una sonrisa."

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex02
    with dissolve

    pt "No sé si me gusta cómo suena esto..."

    play sound "audio/sfx/fall07.ogg"

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_night05_park:
        subpixel True
        truecenter
        zoom 0.4
        easein_quad 1.0 zoom 1.0
        easein_quad 5.0 zoom 0.8
    with hpunch

    n "Rápidamente te agarra de la mano."

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    ne "Sígueme."

    n "Sin demasiada resistencia, y como si fuerais una pareja que pasea cogida de la mano,"

    scene night03_bg street_catalunya_square
    with fade

    #$ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.play("audio/sfx/crowd_hospital.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0

    n "sigues sus pasos que os conducen al subsuelo de la plaza,"

    scene bg night05_bg_station_previous:
        subpixel True
        truecenter
        zoom 0.5
        ease_quad 10.0 zoom 1.2
    with fade

    #########################################################
    
    if config.version < "00.11.03": # Start date with Neus, before taking metro.
        
        call endupdatescript
    
    #######################################################

    n "hasta llegar a la entrada del {a=https://es.wikipedia.org/wiki/Ferrocarriles_de_la_Generalidad_de_Cataluña}ferrocarril{/a},"

    scene bg night05_bg_station_ticket:
        subpixel True
        truecenter
        zoom 1.0
        ease_quad 10.0 zoom 0.5
    with fade

    n "ahí introduce su billete dos veces para que podáis pasar"

    # Background Station

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/train_station01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene bg night05_bg_station_train:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.8
        easein_quad 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "y te conduce hasta el andén de la estación dónde yace vuestro tren parado con las puertas abiertas."

    pt "Siempre había cogido el metro,"

    pt "pero creo que nunca había tomado el ferrocarril."

    # Señal de Av. Tibidabo del Metro.

    scene bg night05_bg_station_train:
        subpixel True
        truecenter
        zoom 2.5 xpos 0.15 ypos 0.7
        #zoom 0.5 xpos 0.5 ypos 0.5
        #ease_quad 15.0 zoom 2.0 xpos 0.25 ypos 0.75
    with dissolve

    n "Ya en la misma estación, no puedes evitar ver que el tren que cogéis,"

    scene bg night05_bg_station_train:
        subpixel True
        truecenter
        zoom 2.5 xpos 0.15 ypos 0.7
        ease_quad 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with dissolve

    n "se dirige a la {a=https://es.wikipedia.org/wiki/Estación_de_Avinguda_Tibidabo}Avenida {i}Tibidabo{/i}{/a}."

    p "Así que vamos al famoso parque de atracciones de la ciudad."

    p "Pensaba que cerraba a las nueve de la noche..."

    $ saturation_tint_level = "default"

    window hide dissolve
    pause

    $ renpy.music.set_volume(0.3, delay= 15.0, channel='sfx1')
    play music "audio/music/alcaknight/memories_of_the_east.ogg" fadein 3.0 fadeout 3.0

    scene bg night05_bg_station_train:
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

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris left01:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with fade

    ne "Por lo visto,"

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    ne "esta semana hacen una excepción."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    pt "Curioso,"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex02
    with dissolve

    pt "uno podría llegar a imaginarse que este tipo de excepciones solo ocurren en las historias por licencias creativas..."

    show neus_exp_mouth happy_Silentx10
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows surprisex02
    with dissolve

    if PlatinumHelp:

        aj ":P"

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    # No sé que puto background # NOT FINISHED

    scene bg night05_bg_station_sign:
        subpixel True
        truecenter
        zoom 1.2 xpos 0.5 ypos 0.5
        ease_quad 10.0 zoom 0.5
    with fade

    n "Pocas paradas después, llegáis a fin de trayecto,"

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/elevator_01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "y allí cogéis el ascensor para salir a la superficie,"

    $ renpy.music.set_volume(0.8, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/bus_01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    # Tranvía

    scene bg night05_bg_station_tranvia:
        subpixel True
        truecenter
        zoom 0.8
        easein_quad 10.0 zoom 0.5
    with fade

    n "de ahí con el tranvía azul, que recorre las calles con sus carriles perforados en el asfalto,"

    # Funicular Outside.

    scene bg night05_bg_station_funicular_out:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.2 ypos 0.6
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "hasta que conseguís llegar al famoso e histórico funicular del {a=https://es.wikipedia.org/wiki/Funicular_del_Tibidabo}{i}Tibidabo{/i}{/a}."

    
    $ renpy.music.play("audio/sfx/train_station01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    $ saturation_tint_level = "verydark"

    scene bg night05_bg_station_funicular:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.6
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    p "¿¡Casi ocho euros solo el funicular!?"

    $ renpy.music.set_volume(0.2, delay = 15.0, channel = 'sfx1')
    play music "audio/music/alcaknight/are_you_still_dreaming.ogg" fadein 3.0 fadeout 3.0

    scene bg night05_bg_station_funicular:
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

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris left01:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "En realidad,"

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "si compras la entrada al parque,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows normal
    with dissolve

    ne "este transporte te sale a mejor precio."

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "Igualmente son más de treinta euros por persona en total..."

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Tranquilo,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    ne "que ya lo pago todo yo."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "No me siento demasiado cómodo con que me vayas pagando las cosas, Neus."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Te he traído aquí sin que supieras a dónde ibas,"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "así que lo mínimo que puedo hacer es invitarte."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "De verdad,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "no es problema."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex01
    with dissolve

    pt "O le sobra el dinero,"

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows surprisex02
    with dissolve

    pt "o quiere impresionarme tanto que al final la arruinaré..."


    ###

    scene bg night05_bg_tranvia_door:
        subpixel True
        truecenter
        zoom 0.5
        easein_quad 10.0 zoom 0.8
    with fade


    n "Justo cuando te dispones a entrar en el primer vagón,"

    play sound "audio/sfx/hit02.ogg"

    scene night05_bg_tranvia_door:
        truecenter
        zoom 0.5
    with vpunch

    n "sientes de nuevo su fuerte agarrón que te empuja a seguir subiendo peldaños para ir más arriba."

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_night05:
        subpixel True
        truecenter
        xzoom -1.0
        zoom 1.0 xpos 2.0
        easein_quad 10.0 xpos -0.25
    with fade

    ne "Aquí hay demasiada gente."

    pt "¿Demasiada gente?"

    pt "¿Para qué?"

    n "Con cierto ímpetu te lleva hasta el último vagón donde prácticamente no hay nadie."

    #scene bg night05_bg_tranvia_seat:
    scene bg n_s_bg_sd_01:
        subpixel True
        truecenter
        zoom 0.8
        easein_quad 15.0 zoom 0.5
    with fade

    n "Ahí te indica que te sientes en frente de ella."

    p "¿No estás a gusto rodeado de gente?"

    $ saturation_tint_level = None # unknown key, so using default = untinted

    # Neus sentada.

    scene bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 01:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth happy_Talkingx08:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 02:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front02:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows surprisex02:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l down_closed:
        n_s_b_sd_funicular_position

    show n_s_b_sd_arm_l empty:
        n_s_b_sd_table_position
    show n_s_b_sd_arm_r empty:
        n_s_b_sd_table_position

    with dissolve

    ne "Esta noche prefiero tenerte para mí sola."

    show n_s_exp_blush 02
    show n_s_exp_mouth happy_Silentx07
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "..."

    # Hacer pareja en la puerta??

    show n_s_exp_blush 01
    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris left00
    with dissolve

    n "Apenas unos segundos después aparece una pareja que pretende entrar en vuestro vagón,"

    show n_s_exp_blush 00
    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    n "hasta que Neus, en escasos segundos,"

    play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0

    # mirada brillante de Neus a la izquierda (por dónde han entrado.)

    show n_s_exp_mouth sad_Silentx08
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 00
    show n_s_exp_iris left00_bright
    with Dissolve (1.0)

    n "les dirige esa mirada gélida con sus ojos brillantes, nada amistosa."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 01
    show n_s_exp_iris left01_bright
    with dissolve

    pt "Otra vez esos ojos..."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with Dissolve (1.0)

    g01 "¿Qué ocurre?"

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    b01 "Nada,"

    extend " nada,"

    show n_s_exp_mouth happy_Silentx02
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    b01 "pero,"

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    b01 "¿qué tal si nos sentamos en el vagón de atrás?"

    show n_s_exp_mouth happy_Silentx04
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    g01 "¿No decías que querías ir delante?"

    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    g01 "Para ver mejor el paisaje por la ventana frontal del tranvía."

    show n_s_exp_mouth happy_Silentx04
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    b01 "Bueno,"

    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    b01 "pero si vamos al de atrás estaremos a solas."

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    g01 "Ohh..."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris left00
    with dissolve

    g01 "No sabía que te hubieras vuelto tan romántico."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    b01 "No..."

    show n_s_exp_mouth happybiting_Silentx02
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    b01 "Yo..."

    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    g01 "Te quiero tanto mi amor..."

    show n_s_exp_mouth happybiting_Silentx01
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    b01 "..."

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    n "Uno con el rostro dubitativo y la otra chica con un resplandor en sus ojos,"

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    n "se dirigen al vagón de atrás mientras Neus te dedica una sonrisa maliciosa."

    show n_s_exp_mouth happy_Silentx07
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    pt "Creo que por ahora es mejor no preguntar qué demonios ha pasado aquí..."

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    n "Apenas logras sentar el trasero sobre el banco,"

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    n "y observas llegar al conductor poniendo en marcha el motor."

    ####################################################### ## # Speaking of Didac in Train.

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Por cierto,"

    $ renpy.music.set_volume(0.1, delay = 15.0, channel = 'sfx1')
    stop music fadeout 3.0
    $ music_play = ""


    # Neus sentada.

    show bg n_s_bg_sd_01:
        truecenter
        zoom 1.0
        ypos 1.0

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_close_position

    # Neus Expressions:

    show n_s_exp_blush 01:
        n_s_exp_sd_funicular_close_position
    show n_s_exp_mouth sad_Talkingx04:
        n_s_exp_sd_funicular_close_position
    show n_s_exp_eyes 01:
        n_s_exp_sd_funicular_close_position
    show n_s_exp_iris left01:
        n_s_exp_sd_funicular_close_position
    show n_s_exp_tears empty:
        n_s_exp_sd_table_position
    show n_s_exp_eyebrows serious:
        n_s_exp_sd_funicular_close_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_close_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_close_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_leg_l down_closed:
        n_s_b_sd_funicular_close_position

    show n_s_b_sd_arm_l empty:
        n_s_b_sd_funicular_close_position
    show n_s_b_sd_arm_r empty:
        n_s_b_sd_funicular_close_position

    with Dissolve (1.0)

    ne "sé que tendría que habértelo preguntado antes,"

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    ne "pero sinceramente estaba tan nerviosa al ser capaz de estar contigo,"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "que hasta ahora no he tenido la claridad para hacerlo."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "Hmm..."

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "¿A qué te refieres?"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Cómo está Dídac?"

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0

    p "Ahh..."

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "¿A qué viene esa pregunta ahora...?"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    ne "Me imagino que no debe de estar pasándolo demasiado bien,"

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    ne "probablemente no entienda muy bien lo que le está ocurriendo."

    show n_s_exp_mouth sad_Talkingx004
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    ne "Espero que no estéis haciendo marranadas,"

    show n_s_exp_mouth sad_Talkingx07
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "que los chicos en esto sois muy brutos..."

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    p "..."

    play sound "audio/characters/neus/giggle05.ogg"

    show n_s_exp_mouth happy_Talkingx06
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 07
    show n_s_exp_iris front07
    with dissolve

    ne "jejeje"

    show n_s_exp_mouth happy_Talkingx07
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "Sería un poco homo,"

    show n_s_exp_mouth happy_Talkingx08
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    ne "¿verdad?"

    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    p "..."

    play sound "audio/characters/neus/giggle04.ogg"

    show bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 03:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth happy_Silentx07:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 05:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front05:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows suspiciousx02:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l down_closed:
        n_s_b_sd_funicular_position
    with dissolve

    n "Una sonrisa pícara y burlona aparece en su rostro,"

    # Levanta una pierna y la al lado de sus nalgas encima del banco. (Piernas aún juntas)

    # Neus sentada.

    show bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 03:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth happybiting_Silentx05:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 05:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front05:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows suspiciousx04:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l up_closed:
        n_s_b_sd_funicular_position
    with Dissolve (1.0)

    n "mientras levanta una pierna y la deposita al lado de sus nalgas encima del banco."

    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    p "..."

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Me alegra ver que al final me hiciste caso y no te lo llevaste al hospital."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "¿Cómo sabes que no lo hice?"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Porque no estaríamos hablando aquí tan tranquilamente si lo hubieras hecho."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "¿Por qué?"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Hay cosas que debo contarte esta noche,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "pero todo a su debido tiempo, [protname]."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    pt "Sus ojos violáceos brillando en la oscuridad,"

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    pt "esa lengua larga como la de una serpiente,"

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    pt "y no olvidemos la transformación en un solo día de Dídac..."

    if afternoon04_MACBA_TxellTruth_Cond == True:

        show n_s_exp_mouth sadbiting_Silentx03
        show n_s_exp_eyebrows sadx03
        show n_s_exp_eyes 04
        show n_s_exp_iris left04
        with dissolve

        pt "Después de lo que me contó Txell en la biblioteca,"

        show n_s_exp_mouth sadbiting_Silentx01
        show n_s_exp_eyebrows sadx01
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        with dissolve

        pt "hay muchas cosas que quiero preguntarle,"

        show n_s_exp_mouth happybiting_Silentx01
        show n_s_exp_eyebrows suspiciousx01
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with dissolve

        pt "pero al mismo tiempo,"

        show n_s_exp_mouth happybiting_Silentx02
        show n_s_exp_eyebrows suspiciousx03
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        with dissolve

        pt "no estoy seguro si realmente quiero saberlo..."

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    window hide dissolve
    pause 0.5

    # Con la pierna encima de la silla, se ABRE de piernas.

    # Neus sentada.

    play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0

    show bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 04:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth happybiting_Silentx05:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 05:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front05:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows suspiciousx04:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l up_open_skirt_over:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r empty
    with Dissolve (1.0)

    n "Observas cómo separa sus piernas de modo poco sutil."

    show n_s_exp_mouth happybiting_Silentx07
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    pt "¿Ahora le da por hacer un {a=https://es.wikipedia.org/wiki/Manspreading}{i}manspreading{/i}{/a}?"

    show n_s_exp_mouth happybiting_Silentx08
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    pt "¿O cuando lo hace una chica se llama de otro modo?"

    show n_s_exp_mouth happybiting_Silentx09
    show n_s_exp_eyebrows suspiciousx05
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    pt "Con esa falda tan corta no sé si es muy buena idea..."

    show n_s_exp_mouth happybiting_Silentx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    pt "Aunque es cierto que en este vagón,"

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    pt "el único que podría verla es el conductor si se gira."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Debe de estar deseando regresar a su cuerpo de hombre musculado,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "¿verdad?"

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Espero no haberle causado demasiados quebraderos de cabeza con todo esto."

    show n_s_exp_mouth sad_Silentx06
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    p "..."

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "Me imagino que no debe de ser agradable que un hombre pierda su pene,"

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "aún más si no recuerda muy bien lo sucedido,"

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    pt "¡¿Sabe que no lo recuerda?!"

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "aunque sea por solo tres días."

    show n_s_exp_mouth happybiting_Silentx03
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    pt "¡¿Acaso no tiene ni la más remota idea de en qué tipo de ninfómana se ha convertido Dídac?!"

    show n_s_exp_mouth happybiting_Silentx05
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    window hide dissolve
    pause 1.0

    # Se sube la falda abierta de piernas sobre el sillón.

    # Neus sentada.

    scene bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 04:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth happybiting_Silentx07:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 05:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front05:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows suspiciousx04:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b empty:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l up_open_skirt_off:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r empty:
        n_s_b_sd_funicular_position

    show n_s_b_sd_arm_r bank_skirthold:
        n_s_b_sd_funicular_position
    
    with Dissolve (1.0)

    n "Sutilmente se sube un poco más la minifalda,"

    show n_s_b_sd_funicular_comp 01:
        subpixel True
        transform_anchor True
        xalign 0.599 yalign 0.205 # Don´t touch it.
        zoom 6.0 xpos 0.55 ypos 0.6 # Eyes.
        pause 1.0
        ease 20.0 zoom 5.0 xpos 0.55 ypos -2.0 # Pussy
        ease 10.0 zoom  1.5 xpos 0.53 ypos 0.0 # Full Body?
    with fade

    n "mostrándote su entrepierna desprovista de ningún tipo de ropa interior."

    if night03_NeusFall_NotPanties == True:

        n "Como ya pudiste comprobar cuando se tropezó en la puerta de la Pedrera."

    p "..."

    if night03_NeusFall_NotPanties == True:

        n "Pero a diferencia del otro día, esta vez lo observas bastante más húmedo."

    window hide dissolve
    pause

    hide n_s_b_sd_funicular_comp

    show n_s_exp_blush 02
    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with fade

    ne "No le habrás espiado mientras se masturba,"

    show n_s_b_sd_leg_l up_open_skirt_up
    show n_s_b_sd_arm_r bank_onleg_rest

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with Dissolve (1.0)

    ne "¿verdad?"

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 00
    show n_s_exp_iris right00
    with dissolve

    ne "En tres días habrá tenido la curiosidad de probarlo me imagino,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "especialmente si no lo dejas salir de casa."

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "Tampoco tendrá mucho que hacer ahí encerrado..."

    show n_s_exp_mouth sad_Talkingx004
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Espero que no le hayas dejado ir a sus anchas por la calle,"

    show n_s_exp_mouth sad_Talkingx06
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    ne "no te lo advertí,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "pero sería igualmente peligroso si alguien descubriera quién es realmente."

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "Aunque me pregunto cómo lo habrás convencido para que no salga de casa."

    show n_s_exp_blush 03
    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "..."

    show n_s_exp_blush 04
    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "Perdona..."

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "Soy curiosa por naturaleza,"

    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "a veces pregunto demasiado."

    play sound "audio/characters/neus/giggle02.ogg"

    show n_s_exp_mouth happybiting_Silentx06
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    n "Su sonrisa es maliciosa y femenina,"

    # Se muerde un Dedo y la otra se la acerca a la entrepierna.

    scene n_s_b_sd_funicular_comp 02:
        subpixel True
        transform_anchor True
        xalign 0.599 yalign 0.205 # Don´t touch it.
        zoom 6.0 xpos 0.55 ypos 0.6 # Eyes.
        pause 1.0
        ease 20.0 zoom 5.0 xpos 0.55 ypos -2.0 # Pussy
        ease 10.0 zoom  1.5 xpos 0.53 ypos 0.0 # Full Body?
    with fade

    n "mientras se muerde un dedo,"

    n "y se acerca la otra mano a su entrepierna como si la usara de apoyo."

    pt "¿Me está tomando el pelo?"

    pt "¿o realmente no tiene ni la más remota idea de lo que le ocurre?"

    play music "audio/music/neus_theme.ogg" fadein 3.0 fadeout 3.0 

    window hide dissolve
    pause

    scene bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 03:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth sad_Silentx04:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 04:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front04:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows serious:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_r_b empty:
        n_s_b_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l up_open_skirt_up:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r empty:
        n_s_b_sd_funicular_position

    show n_s_b_sd_arm_r bank_onleg_rest:
        n_s_b_sd_funicular_position
    
    with fade

    n "Su rostro cambia de expresión, y regresando a la serenidad, te vuelve la mirada con sinceridad."

    show n_s_exp_blush 03
    show n_s_exp_mouth sad_Talkingx06
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Ahora te lo pregunto en serio, [protname],"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "¿cómo está?"

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    $ night05_Funicular_Didac_Daddy_Cond = 0

    ##

    ## Here is when the red doesn´t let you answer her.

    menu night05_Funicular_Didac_question:

        pt "Ya tardaba en hacerme esa pregunta..."

        "Debo contarte algo sobre Dídac..." if night05_Funicular_Didac_Daddy_Cond < 7:

            call p_Help

            $ night05_Funicular_Didac_Daddy_Cond += 1

            jump night05_Funicular_Didac_Daddy_answers


        "He follado con Dídac. " if (afternight04_Pussy_dick_deep_Speed_1_Done > 0 and night05_Funicular_Didac_Daddy_Cond < 7):

            call p_Help

            $ night05_Funicular_Didac_Daddy_Cond += 1

            jump night05_Funicular_Didac_Daddy_answers

        "Preferiría centrar mi atención contigo esta noche.":

            call p_Help

            $pl.ch_pts("np",1)

            jump night05_Funicular_Didac_After


label night05_Funicular_Didac_Daddy_answers:

    if night05_Funicular_Didac_Daddy_Cond == 1:

        jump night05_Funicular_Didac_Daddy_01

    elif night05_Funicular_Didac_Daddy_Cond == 2:

        jump night05_Funicular_Didac_Daddy_02

    elif night05_Funicular_Didac_Daddy_Cond == 3:

        jump night05_Funicular_Didac_Daddy_03

    elif night05_Funicular_Didac_Daddy_Cond == 4:

        jump night05_Funicular_Didac_Daddy_04

    elif night05_Funicular_Didac_Daddy_Cond == 5:

        jump night05_Funicular_Didac_Daddy_05

    elif night05_Funicular_Didac_Daddy_Cond >= 6:

        jump night05_Funicular_Didac_Daddy_06

label night05_Funicular_Didac_Daddy_01:

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "..."

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Hmm..."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Ocurre algo [protname]?"

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Euh..."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "No..."

    p "Yo..."

    jump night05_Funicular_Didac_question

label night05_Funicular_Didac_Daddy_02:

    p "..."

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Va todo bien?"

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Yo..."

    pt "¡¿Por qué diablos no puedo hablar?!"

    jump night05_Funicular_Didac_question

label night05_Funicular_Didac_Daddy_03:

    p "..."

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Hay algo que me quieras contar?"

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Euh..."

    pt "¡Parezco imbécil!"

    pt "¡¿Qué diablos me pasa?!"

    jump night05_Funicular_Didac_question

label night05_Funicular_Didac_Daddy_04:

    p "..."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    dad "Aún no."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    pt "¡¿Y esa voz?!"

    pt "¡Es la misma que oí en mi sueño esta mañana!"

    jump night05_Funicular_Didac_question

label night05_Funicular_Didac_Daddy_05:

    p "..."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    pt "¡¿Es que no me dejas responder otra cosa?!"

    ne "..."

label night05_Funicular_Didac_Daddy_06:

    p "..."

    jump night05_Funicular_Didac_question

label night05_Funicular_Didac_After:

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "No te preocupes por él, Neus."

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Al fin y al cabo, tuvo un comportamiento contigo por el que se merece esto, y más."

    if night05_Funicular_Didac_Daddy_Cond >= 4:

        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_eyebrows suspiciousx05
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with dissolve

        pt "¡Tampoco puedo responderte otra cosa!"

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    ne "Tampoco seas muy duro con él, [protname]..."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "¿Acaso no lo hiciste para castigarlo?"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    ne "La recompensa que he recibido con tu compañía,"

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "es muchísimo más valiosa que el castigo que pudiera darle."

    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "Además me aseguré de que no recordara lo sucedido..."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "¿Qué sentido tiene reprimir a alguien,"

    show n_s_exp_mouth sad_Silentx06
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    p "si luego no recuerda el motivo por el cual ha sido castigado?"

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows sadx07
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    pt "¿Por qué pone esa cara tan triste ahora?"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    with dissolve

    ne "¿A qué viene esa erección mientras estamos hablando de castigos, [protname]?"

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "Soy humano,"

    show n_s_exp_mouth happybiting_Silentx05
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    p "¿sabes?"

    show n_s_exp_mouth happy_Silentx07
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Me imagino que por eso has querido ir al vagón frontal donde no hubiera nadie,"

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with dissolve

    p "excepto el conductor,"

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    p "que pudiera verte."

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Yo..."

    show n_s_exp_blush 03
    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "No eres consciente de cuánto tiempo hace que estoy esperando esta noche."

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    p "¿Hmm...?"

    show n_s_exp_blush 03
    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "A veces me hago un poco la idiota cuando intento ocultar lo nerviosa que estoy..."

    play sound "audio/characters/neus/moan17.ogg"

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    n "Una sonrisa entrecortada se dibuja en sus labios,"

    show n_s_exp_blush 04
    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    n "mientras intenta evitar tu mirada con el rostro completamente rojizo."

    # Neus sentada.

    stop music fadeout 3.0
    $ music_play = ""
    play sound "audio/sfx/bus_stop.ogg"

    scene bg n_s_bg_sd_01:
        truecenter
        zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_funicular_position
    show n_s_b_sd_body:
        n_s_b_sd_funicular_position
    show n_s_b_sd_face:
        n_s_b_sd_funicular_position

    # Neus Expressions:

    show n_s_exp_blush 04:
        n_s_exp_sd_funicular_position
    show n_s_exp_mouth sadbiting_Silentx06:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyes 00:
        n_s_exp_sd_funicular_position
    show n_s_exp_iris front00:
        n_s_exp_sd_funicular_position
    show n_s_exp_tears empty:
        n_s_exp_sd_funicular_position
    show n_s_exp_eyebrows surprisex03:
        n_s_exp_sd_funicular_position
    show n_s_exp_glasses:
        n_s_exp_sd_funicular_position

    show n_s_b_sd_arm_l_b bank_rest:
        n_s_b_sd_funicular_position
    show n_s_b_sd_arm_r_b bank_rest:
        n_s_b_sd_funicular_position

    show n_s_b_sd_hair_front:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_r down_closed:
        n_s_b_sd_funicular_position
    show n_s_b_sd_leg_l down_closed:
        n_s_b_sd_funicular_position
    with vpunch

    n "Sentís cómo el tren detiene súbitamente su marcha."

    play sound "audio/sfx/train_finaldetrajecte.ogg"

    show n_s_exp_blush 04
    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    meg "Fin de trayecto."

    ###################################################

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
 
    scene bg night05_bg_tibidabo_park_00:
        subpixel True
        truecenter
        zoom 0.6 xpos -0.35 ypos 0.4
        ease 20.0 zoom 0.6 xpos 0.6 ypos 0.4 #Pose for Neus Speak
    with fade

    window hide dissolve
    pause

    #########################################################
    
    if config.version < "00.11.04": # Conversation in the tranvia.
        
        call endupdatescript
    
    #######################################################

    ne "Wow."

    ne "La verdad es que de noche el lugar tiene otro tipo de magia."

    p "Y tampoco es que haya poca gente..."

    $ saturation_tint_level = "verydark"

    window hide dissolve
    pause

    $ renpy.music.set_volume(0.2, delay=15.0, channel='sfx1')
    play music "audio/music/kevinmacleod/fireflies_and_stardust.ogg" fadein 3.0 fadeout 3.0

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
    show neus_exp_mouth happy_Talkingx02:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris front02:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    ne "¡La noria es preciosa de noche!"

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 05
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx01
    with dissolve

    pause 0.2

    show night05_bg_tibidabo_park_00:
        subpixel True
        truecenter
        zoom 0.6 xpos 0.6 ypos 0.4
        easein_quad 10.0 zoom 0.75 xpos 1.65 ypos 0.4 # Noria
    with fade

    window hide dissolve
    pause

    ne "Antes de irnos del parque,"

    hide night05_bg_tibidabo_park_00
    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows surprisex01
    with fade

    ne "quiero que nos subamos a ella;"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "para poder ver las vistas,"

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "y las luces de la ciudad desde lo más alto."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "Prométemelo."

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "Eres tú quien decide aquí."

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Jejeje"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Así me gusta."

    show neus_exp_mouth happy_Silentx03
    show neus_exp_eyes 05
    show neus_exp_iris front05
    show neus_exp_eyebrows normal
    with dissolve

    pause 0.2

    scene night05_bg_tibidabo_park_00:
        subpixel True
        truecenter
        zoom 0.6 xpos 0.6 ypos 0.4
        ease 10.0 zoom 1.2 xpos -0.75 ypos 0.3 # Plane
    with fade

    ne "¡Vaya!"

    ne "¡No sabía que el {a=https://ca.wikipedia.org/wiki/Parc_d'Atraccions_Tibidabo#/media/Fitxer:Tibidabo08.jpg}avión del {i}Tibidabo{/i}{/a} había recuperado su diseño original!"

    ne "Luce algo distinto a lo que recuerdo,"

    ne "pero por lo menos es parecido."

    p "..."

    window hide dissolve
    pause

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
    show neus_exp_mouth sad_Talkingx002:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris front02:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex02:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with fade

    ne "¿Qué?"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿De lo que recuerdas?"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "El diseño original es por lo menos de los años veinte del siglo pasado."

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Bueno..."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Ya..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Me refiero a las fotos que he visto."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows suspiciousx02
    with dissolve

    ne "Mm..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "¿Cuántos años tenías la última vez que te subiste a un carrusel?"

    show neus_exp_mouth happybiting_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx02
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "Sinceramente,"

    show neus_exp_mouth happy_Silentx01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    p "no lo recuerdo..."

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "¿Te subirías a él conmigo?"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "Esto,"

    extend " yo..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 01
    show neus_exp_iris down01
    show neus_exp_eyebrows surprisex02
    with vpunch

    play sound "audio/sfx/stomach01.ogg"

    ono "BBBBBRRRRRrrrr..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Lo siento..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Me imagino que no habrás comido nada en horas esperando a la cena de hoy."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Debes de estar hambriento."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    pt "Un poco sí..."

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "En lugar de comer en un restaurante,"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    ne "hoy me gustaría ir al pequeño parque que hay un poco más al fondo de esta montaña."

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿Has traído comida?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve
    
    ne "Así es."

    show neus_exp_mouth happy_Silentx07
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Tranquilo,"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "estoy segura de que esta vez"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "te va a gustar más lo que te voy a dar."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Aunque, si crees que no te va a satisfacer,"

    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "también podemos bajar al {a=https://es.wikipedia.org/wiki/Telepizza}{i}Telepizza{/i}{/a} que hay al lado del castillo más abajo..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Puedo saber al menos qué llevas en el bolso?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows normal
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx01
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "Euh..."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Traigo un bizcocho de naranja,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris down02
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "y otro de chocolate con galletas que simulan un salchichón."

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "..."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "¿Y bien...?"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "Me imagino que ninguno estará hecho con leche o huevos..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Contienen margarina,"

    extend " cacao,"

    extend " leche vegetal,"

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex03
    with dissolve

    ne "y especialmente el de salchichón,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    ne "galletas digestivas."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "Pero,"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "¿los bizcochos y las galletas no son algo más para comer de postre?"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Es más fácil que te gusten los postres,"

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "que los platos principales."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Especialmente en frío."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows serious
    with dissolve

    p "No sé yo..."

    show neus_exp_blush 01
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Por favor,"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    ne "ten un poco de fe en mis artes culinarias."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Los has hecho tú misma?"

    
    show neus_exp_blush 03
    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Así es."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "No sabía que te gustara la cocina."

    show neus_exp_blush 06
    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "En realidad he sido un desastre en ello durante la mayor parte de mi vida,"

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "pero con el paso de los siglos,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "una acaba cogiéndole el truco."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿De los siglos?"

    show neus_exp_blush 03
    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "..."

    show neus_exp_blush 02
    show neus_exp_mouth happy_Talkingx02
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Euh..."

    show neus_exp_mouth happy_Talkingx01
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Je..."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Es un modo de hablar, hombre..."

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with dissolve

    pt "Ya,"

    extend " seguro..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿Y tú vas a comer lo mismo?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "Quizás un poco,"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "pero en realidad,"

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "mi plato principal me lo reservo para más tarde."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿También saltarás directamente a los postres?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows normal
    with dissolve

    ne "Así es."

    show neus_exp_mouth happybiting_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Y qué demonios vas a comer?"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Tú eres mi postre."

    show neus_exp_blush 03
    show neus_exp_mouth happybiting_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx02
    with dissolve

    p "..."

    play sound "audio/characters/neus/giggle01.ogg"

    show neus_exp_blush 06
    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows surprisex02
    with dissolve

    n "Una sonrisa pícara y burlona emerge de sus labios."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    pt "No estoy muy seguro de si el escalofrío que he sentido es de morbo o de miedo..."

    show neus_exp_blush 03
    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "¿Entonces qué vas a comer?"

    show neus_exp_blush 02
    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "¿Pizza o mis bizcochos?"

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "..."

    menu night05_Plaza_Food_Question:
        
        pt "Si quisiera envenenarme lo haría de otro modo me imagino..."

        "Me apetece probar tus bizcochos.":
            
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_Plaza_Food_Biscuit = True

            show neus_exp_mouth happy_Talkingx07
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows surprisex03
            with dissolve

            ne "Así me gusta."

            show neus_exp_mouth happy_Silentx06
            show neus_exp_eyes 06
            show neus_exp_iris front06
            show neus_exp_eyebrows normal
            with dissolve

            pause 0.2

            jump night05_Eating

        "Sinceramente, preferiría comer una pizza.":

            call p_Help

            $pl.ch_pts("np",-3)

            $ night05_Plaza_Food_Biscuit = False

            show neus_exp_blush 01
            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows serious
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 01
            show neus_exp_iris left01
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "Hmm..."

            show neus_exp_mouth sad_Talkingx001
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Como quieras."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx05
            with dissolve

            pt "No parece que se lo haya tomado demasiado bien..."

            jump night05_Eating
    ####

    ############################################################ Decides probar sus bizcochos.

label night05_Eating:

    #$ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.set_volume(0.8, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.02, delay=40.0, channel='sfx1')
    stop music fadeout 3.0
    $ music_play = ""

    call saturation_ting_values_check

    $ saturation_tint_level = "verydark"

    scene bg night05_bg_tibidabo_dinner_bg:
        truecenter
        zoom 0.5

    # Neus sentada.

    show n_s_b_sd_hair_back:
        n_s_b_sd_table_position
    show n_s_b_sd_body:
        n_s_b_sd_table_position
    show n_s_b_sd_face:
        n_s_b_sd_table_position

    # Neus Expressions:

    show n_s_exp_blush 01:
        n_s_exp_sd_table_position
    show n_s_exp_mouth sad_Silentx03:
        n_s_exp_sd_table_position
    show n_s_exp_eyes 02:
        n_s_exp_sd_table_position
    show n_s_exp_iris front02:
        n_s_exp_sd_table_position
    show n_s_exp_tears empty:
        n_s_exp_sd_table_position
    show n_s_exp_eyebrows surprisex02:
        n_s_exp_sd_table_position
    show n_s_exp_glasses:
        n_s_exp_sd_table_position
    show n_s_b_sd_hair_front:
        n_s_b_sd_table_position

    show n_s_b_sd_arm_l_b empty: # Hands behind Table
        n_s_b_sd_table_position
    show n_s_b_sd_arm_r_b empty:
        n_s_b_sd_table_position

    show night05_bg_tibidabo_dinner_table:
        truecenter
        zoom 0.5

    show n_s_b_sd_arm_l table_rest:
        n_s_b_sd_table_position
    show n_s_b_sd_arm_r table_rest:
        n_s_b_sd_table_position
    
    #show n_s_b_sd_leg_r down_closed:
        #n_s_b_sd_table_position
    #show n_s_b_sd_leg_l down_closed:
        #n_s_b_sd_table_position

    if night05_Plaza_Food_Biscuit == True:

        show n_s_exp_blush 03
        show n_s_exp_mouth happy_Talkingx06
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with fade

        ne "¿Qué tal está?"

        show n_s_exp_mouth happy_Silentx04
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        with dissolve

        pause 0.2

        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ renpy.music.set_volume(0.05, delay=10.0, channel='sfx1')

        show night05_bg_park_food orange:
            subpixel True
            truecenter
            zoom 1.0
            easein_quad 20.0 zoom 0.5
        with fade

        p "Debo confesar que sabe mejor de lo que esperaba."

        pt "También podría haber traído algo más que dos rodajas..."

        pt "Me voy a quedar con hambre con esto."

        pt "Aunque me pregunto cómo se lo habrá montado para mantener esta buena presentación,"

        pt "teniendo en cuenta que lo llevaba dentro de un {i}tupper{/i} en su bolso..."

        window hide dissolve
        pause

        hide night05_bg_park_food
        show n_s_exp_mouth happy_Silentx06
        show n_s_exp_eyebrows surprisex01
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        with fade

    else:

        show n_s_exp_blush 01
        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows angryx01
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        with fade

        ne "Al menos espero que hayas elegido una pizza que te guste..."

        play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
        $ renpy.music.set_volume(0.05, delay=10.0, channel='sfx1')

        show night05_bg_park_food pizza:
            subpixel True
            truecenter
            zoom 1.0
            easein_quad 20.0 zoom 0.5
        with fade

        n "Después de haberos pateado medio parque,"

        n "una riquísima pizza barbacoa con su topping a base de mozzarella,"

        n "beicon, carne de vacuno, pollo marinado y su particular salsa;"

        n "se encontraba por fin ante ti, recién horneada y lista para saborear."

        pt "Bizcochos con leche de soja,"

        extend " Bah..."

        pt "¿Cómo me lo vas a comparar con esta maravilla?"

        window hide dissolve
        pause

        hide night05_bg_park_food
        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_eyebrows angryx01
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        with fade

    #$ saturation_tint_level = "superdark"

    n "Apenas una tenue farola amarillenta instalada el siglo pasado,"

    if night05_Plaza_Food_Biscuit == True:

        show n_s_exp_mouth happy_Silentx06
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 06
        show n_s_exp_iris front06
        with dissolve

    else:

        show n_s_exp_mouth sad_Silentx03
        show n_s_exp_eyebrows sadx03
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        with dissolve

    n "ilumina un poco el lugar donde os encontráis."

    n "El parque fue diseñado para ser disfrutado de día, no tanto de noche."

    if night05_Plaza_Food_Biscuit == True:

        show n_s_exp_mouth happy_Silentx05
        show n_s_exp_eyebrows surprisex01
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        with dissolve

    else:

        show n_s_exp_mouth sad_Silentx02
        show n_s_exp_eyebrows sadx02
        show n_s_exp_eyes 04
        show n_s_exp_iris right04
        with dissolve

    n "Algún que otro amante o borracho se encuentra en la cercanía."

    n "La mayor parte del público frecuenta la región lúdica y más activa del parque,"

    if night05_Plaza_Food_Biscuit == True:

        show n_s_exp_mouth happy_Silentx04
        show n_s_exp_eyebrows normal
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        with dissolve

    else:

        show n_s_exp_mouth sad_Silentx01
        show n_s_exp_eyebrows sadx01
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        with dissolve

    n "donde se encuentra la zona de pago y sus atracciones."

    if night05_Plaza_Food_Biscuit == True:

        show n_s_exp_mouth happy_Talkingx07
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        with dissolve

        ne "Y aún no has probado el salchichón con galletas."

        show n_s_exp_mouth happy_Silentx07
        show n_s_exp_eyebrows surprisex03
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        with dissolve

        p "No seas impaciente, mujer..."

        show n_s_exp_mouth happy_Talkingx05
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with dissolve

        ne "Tengo curiosidad por saber qué opinas."

        show n_s_exp_mouth happy_Silentx04
        show n_s_exp_eyebrows surprisex03
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        with dissolve

        p "Tiene un aspecto increíble,"

        show n_s_exp_mouth happy_Silentx05
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with dissolve

        p "y un toque dulzón sutil que le da un sabor delicioso."

        show n_s_exp_mouth happy_Silentx06
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        with dissolve

        p "Además del olor y el gusto natural de la naranja recién exprimida."

        show n_s_exp_mouth happy_Silentx07
        show n_s_exp_eyebrows surprisex03
        show n_s_exp_eyes 07
        show n_s_exp_iris front07
        with dissolve

        p "Se nota que han sido hechos con cariño."

        show n_s_exp_mouth happy_Talkingx04
        show n_s_exp_eyebrows surprisex03
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        with dissolve

        ne "Debo confesarte que con el de salchichón relleno de galletas,"

        show n_s_exp_mouth happy_Talkingx05
        show n_s_exp_eyebrows surprisex02
        show n_s_exp_eyes 02
        show n_s_exp_iris right02
        with dissolve

        ne "me ha ayudado un poco {b}Baba{/b}."

        show n_s_exp_mouth sad_Silentx01
        show n_s_exp_eyebrows surprisex03
        show n_s_exp_eyes 00
        show n_s_exp_iris front00
        with dissolve

        p "¿Realmente existe esta anciana?"

        show n_s_exp_mouth sad_Silentx04
        show n_s_exp_eyebrows suspiciousx02
        show n_s_exp_eyes 05
        show n_s_exp_iris front05
        with dissolve

        p "¿O la usaste ayer como excusa?"

        show n_s_exp_mouth sad_Talkingx04
        show n_s_exp_eyebrows sadx01
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        with dissolve

        ne "¡Por supuesto que existe!"

        show n_s_exp_mouth sad_Talkingx002
        show n_s_exp_eyebrows sadx03
        show n_s_exp_eyes 01
        show n_s_exp_iris right01
        with dissolve

        ne "Solo que es algo tímida..."

        show n_s_exp_mouth sad_Silentx05
        show n_s_exp_eyebrows sadx04
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        with dissolve

        pt "Tímida..."

        show n_s_exp_mouth sad_Silentx06
        show n_s_exp_eyebrows sadx05
        show n_s_exp_eyes 05
        show n_s_exp_iris right05
        with dissolve

        pt "seguro..."

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "Bueno,"

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "mientras comes,"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "podría seguir con el interrogatorio de ayer."

    show n_s_exp_mouth happybiting_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    pt "¿De verdad no va a comer nada?"

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Aún me gustaría saber más cosas sobre tu vida y tus gustos."

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "¿Y qué hay de ti?"

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "¿Euh?"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿A qué te refieres?"

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Ayer me hiciste tú el interrogatorio,"

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "hoy me toca hacértelo a ti."

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows suspiciousx03
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    p "Soy yo quien tiene más preguntas sin responder."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "..."

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    ne "Supongo que tienes razón..."

    show n_s_exp_mouth happybiting_Silentx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    p "..."

    show n_s_exp_mouth happy_Talkingx02
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "Bueno,"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "lo que podemos hacer es jugar a {a=https://es.wikipedia.org/wiki/Quid_pro_quo}{i}Quid Pro Quo{/i}{/a}."

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "Tú respondes una pregunta mía,"

    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "y luego yo una tuya..."

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "De eso nada."

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "¿Euh?"

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Esta vez hago yo las preguntas,"

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "y tú te limitas a responderme."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Así fue el juego ayer."

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows suspiciousx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "..."

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    ne "Me gusta esa parte dominante de ti..."

    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "De acuerdo,"

    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "me parece justo."

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 00
    show n_s_exp_iris left00
    with dissolve

    ne "Pero no te prometo poder responder todas tus preguntas..."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    p "Por lo menos te pido que no me mientas."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "Tampoco te puedo prometer eso..."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    p "¡¿Qué?!"

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    p "¡¿Por qué?!"

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "Pero me comprometo, en la medida de lo posible,"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "que antes de mentir,"

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "preferiré callarme."

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "¿Preferirás?"

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "¿Por qué simplemente no respondes?"

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    p "Así te ahorras tener que engañarme."

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "Porque a veces la ausencia de una réplica"

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    ne "es de por sí una respuesta."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    p "..."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    pt "Algo de razón tiene..."

    show n_s_exp_mouth happy_Talkingx02
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Pero si consigues hacerme preguntas interesantes que pueda responderte,"

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "te iré recompensando con algo que quizás te alegre la vista."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Te gusta controlar la situación en todo momento y hacerme sufrir,"

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    p "¿verdad?"

    show n_s_exp_mouth happy_Talkingx06
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Dame un látigo y unas esposas,"

    show n_s_exp_mouth happy_Talkingx07
    show n_s_exp_eyebrows angryx02
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    ne "y quizás entonces descubras lo que soy capaz de hacerte sufrir."

    play sound "audio/characters/neus/giggle02.ogg"

    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    pt "Y luego dice que es una chica tímida..."

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "No."

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_eyebrows suspiciousx02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "¿No?"

    show n_s_exp_mouth sad_Silentx02
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Esta noche te vas a poner este juguete que he traído."

    
    play music "audio/music/alcaknight/forever_dreaming.ogg" fadein 3.0 fadeout 3.0

    show night05_bg_park_food dildo:
        subpixel True
        truecenter
        zoom 1.0
        easein_quad 15.0 zoom 0.5
    with fade

    n "De tu bolsillo sacas un huevo vibrador a control remoto,"

    n "que puedes activar a distancia con el móvil."

    ne "[protname]..."

    hide night05_bg_park_food
    show n_s_exp_mouth happy_Talkingx04
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with fade

    ne "No te tenía por un chico tan travieso..."

    show n_s_exp_mouth happy_Talkingx06
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "Pero no hace falta que me introduzcas eso para ponerme más caliente de lo que ya estoy..."

    show n_s_exp_mouth sad_Silentx01
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "Póntelo."

    show n_s_exp_mouth happy_Silentx02
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "..."

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "Como quieras."

    show n_s_exp_mouth happybiting_Silentx03
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris down02
    show n_s_b_sd_arm_l_b bank_rest
    show n_s_b_sd_arm_r_b bank_rest
    show n_s_b_sd_arm_l empty
    show n_s_b_sd_arm_r empty
    with dissolve

    p "Cada vez que no respondas mi pregunta,"

    show n_s_exp_mouth happybiting_Silentx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "o no me satisfaga tu respuesta,"

    show n_s_exp_mouth happybiting_Silentx06
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 08
    show n_s_exp_iris front08
    with dissolve

    p "activaré el juguete por tres segundos a máxima intensidad."

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_b_sd_arm_l_b empty
    show n_s_b_sd_arm_r_b empty
    show n_s_b_sd_arm_l table_rest
    show n_s_b_sd_arm_r table_rest
    with dissolve

    ne "[protname]..."

    show n_s_exp_mouth sad_Talkingx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Sabes muy bien lo que ocurre cuando estoy cerca del orgasmo..."

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "No puedo tener uno aquí en medio..."

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Es a ti a la que le gustan los juegos eróticos en público."

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    p "Además estamos a oscuras y prácticamente solos."

    show n_s_exp_mouth sad_Talkingx002
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Me gustan cuando no soy yo la víctima."

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    pt "Por lo menos es sincera..."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Entiéndelo,"

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "no es una cuestión de vergüenza,"

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    ne "sino de..."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Bueno,"

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "lo tienes muy fácil,"

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "simplemente aguántate las ganas,"

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "o mejor aún,"

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    p "responde con sinceridad a mis preguntas."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "..."

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "Al menos prométeme que no me harás preguntas raras expresamente."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "..."

    show n_s_exp_mouth sadbiting_Silentx03
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Intentaré ser justo con ellas."

    show n_s_exp_mouth happybiting_Silentx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    with dissolve

    ne "..."

    menu night05_Eating_CheckingLegs_Question:

        pt "¿Se lo habrá puesto?"

        "Abre esas piernas y déjame ver que te lo has puesto.":
            
            call p_Help

            $pl.ch_pts("np",-1)

            show n_s_exp_mouth sad_Talkingx08
            show n_s_exp_eyebrows angryx04
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            ne "¿Es que no te fías de mí?"

            show n_s_exp_mouth sad_Silentx06
            show n_s_exp_eyebrows angryx03
            show n_s_exp_eyes 05
            show n_s_exp_iris front05
            with dissolve

            menu night05_Eating_CheckingLegs_Trust_Question:

                pt "Existe la posibilidad de que no se lo haya puesto..."

                "Quizás solo quiero verte abierta de piernas.":
                    
                    call p_Help

                    $pl.ch_pts("np",2)

                    show n_s_exp_blush 03
                    show n_s_exp_mouth sadbiting_Silentx02
                    show n_s_exp_eyebrows surprisex01
                    show n_s_exp_eyes 01
                    show n_s_exp_iris front01
                    with dissolve

                    ne "..."

                    show n_s_exp_blush 04
                    show n_s_exp_mouth sad_Talkingx003
                    show n_s_exp_eyebrows surprisex01
                    show n_s_exp_eyes 05
                    show n_s_exp_iris front05
                    with dissolve

                    ne "Pervertido..."

                    show n_s_b_sd_park_undertable_comp 01: # NOT FINISHED yet
                        subpixel True
                        transform_anchor True
                        xalign 0.599 yalign 0.205 # Don´t touch it.
                        zoom 10.0 xpos 0.55 ypos -3.5
                        easein_quad 10.0 zoom 5.0 xpos 0.55 ypos -2.0 # Pussy
                    with fade

                    pt "Mira quién habla..."

                    window hide dissolve
                    pause

                    hide n_s_b_sd_park_undertable_comp
                    show n_s_exp_mouth happybiting_Silentx04
                    show n_s_exp_eyebrows sadx03
                    show n_s_exp_eyes 05
                    show n_s_exp_iris right05
                    with fade

                    ne "..."

                "Prefiero estar seguro.":

                    call p_Help

                    $pl.ch_pts("np",-1)

                    show n_s_exp_mouth sad_Silentx07
                    show n_s_exp_eyebrows angryx05
                    show n_s_exp_eyes 05
                    show n_s_exp_iris front05
                    with dissolve

                    ne "..."

                    show n_s_b_sd_park_undertable_comp 01: # NOT FINISHED yet
                        subpixel True
                        transform_anchor True
                        xalign 0.599 yalign 0.205 # Don´t touch it.
                        zoom 10.0 xpos 0.55 ypos -3.5
                        easein_quad 10.0 zoom 5.0 xpos 0.55 ypos -2.0 # Pussy
                    with fade

                    p "Hmm..."

                    window hide dissolve
                    pause

                    hide n_s_b_sd_park_undertable_comp
                    show n_s_exp_mouth sad_Talkingx06
                    show n_s_exp_eyebrows angryx03
                    show n_s_exp_eyes 02
                    show n_s_exp_iris front02
                    with fade

                    ne "¿Contento?"

                    show n_s_exp_mouth sad_Silentx05
                    show n_s_exp_eyebrows angryx04
                    show n_s_exp_eyes 04
                    show n_s_exp_iris front04
                    with dissolve

                    p "Satisfecho."

                    show n_s_exp_mouth sad_Silentx06
                    show n_s_exp_eyebrows angryx04
                    show n_s_exp_eyes 05
                    show n_s_exp_iris right05
                    with dissolve

                    ne "Hmm..."

                "No importa, ya me fío de tu palabra.":

                    call p_Help

                    $pl.ch_pts("np",1)

                    show n_s_exp_mouth happy_Talkingx05
                    show n_s_exp_eyebrows normal
                    show n_s_exp_eyes 04
                    show n_s_exp_iris front04
                    with dissolve

                    ne "Buen chico."

                    show n_s_exp_mouth happy_Silentx05
                    show n_s_exp_eyebrows serious
                    show n_s_exp_eyes 05
                    show n_s_exp_iris front05
                    with dissolve

        "<Mejor no ser tan desconfiado...>":

            ne "..."

    

    ########################################################################################
    ########################################################################################
    ########################################################################################

    ## INTERROGATION

    jump night05_Interrogation

    ########################################################################################
    ########################################################################################
    ########################################################################################

    # Dividir el interrogatorio en tres partes. O no.

    ########################################################################################
    ########################################################################################
    ########################################################################################

    ## AFTER INTERROGATION

    ########################################################################################
    ########################################################################################
    ########################################################################################

    ########################################################################################
    ########################################################################################
    ########################################################################################

    ########################################################################################
    ########################################################################################
    ########################################################################################

    #ne "Veo que has llegado a terminarte los dos bizcochos que te he preparado."

label night05_Interrogation_After:

    stop music fadeout 3.0
    $ music_play = ""

    play sound "audio/sfx/fall12.ogg"

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    ne "Ahora sígueme."

    n "Vuelve a agarrarte suavemente de la mano hasta salir de la zona de pícnic."

    pt "¿Y el vibrador?"

    pt "¿Sigue teniéndolo entre las piernas?"

    #########################################################
    
    if config.version < "00.11.07": # Interrogation Finished.
        
        call endupdatescript
    
    #######################################################

    $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.8, delay=1.0, channel='sfx1')

    scene bg night05_bg_tibidabo_park_ticketpass:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5 zoom 0.5
        ease_quad 15.0 zoom 1.0 xpos 1.0 ypos 0.5
        #zoom 1.0 xpos 0.0 ypos 1.0
        #easein_quad 15.0 xpos 0.5 ypos 0.5 zoom 0.5
    with fade

    n "Entre columpios, matorrales y caminos con asfalto y sin él,"

    n "a lo largo de la bajada, lográis llegar a un rellano,"

    n "en el que tenéis que mostrar vuestro brazalete para dar prueba de que habéis pagado la entrada."

    n "Sobrepasáis distintas atracciones primerizas aparentemente más destinadas a un público infantil que juvenil,"

    $ saturation_tint_level = "verydark"

    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.8, delay=1.0, channel='sfx1')

    scene bg night05_bg_tibidabo_park_acuatic:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0 ypos 0.5
        easein_quad 15.0 xpos 0.5 ypos 0.5 zoom 0.5
    with fade

    $ renpy.music.set_volume(0.1, delay=25, channel='sfx1')

    n "hasta llegar a la primera y única atracción acuática del parque."

    p "La {a=https://www.tibidabo.cat/es/en-el-parque/atracciones/la-mina-de-oro}Mina de Oro{/a},"

    p "¿Quieres subirte a esta atracción?"

    if music_play != "fireflies_and_stardust":
            play music "audio/music/kevinmacleod/fireflies_and_stardust.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "fireflies_and_stardust"

    scene bg night05_bg_tibidabo_park_acuatic:
        truecenter
        xpos 0.5 ypos 0.5 zoom 0.5

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "Es de noche y la atracción es de agua..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Y qué quieres decir con eso?"

    if night05_Interrogation_Vibrator_AngryNumber > night05_Interrogation_Vibrator_HappyNumber:

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows angryx01
        with dissolve

    else:

        show neus_exp_mouth happy_Talkingx03
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows surprisex01
        show neus_exp_blush 02
        with dissolve

    ne "Que ya estoy suficientemente mojada..."

    if night05_Interrogation_Vibrator_AngryNumber > night05_Interrogation_Vibrator_HappyNumber:

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows serious
        with dissolve

    else:

        show neus_exp_mouth happy_Silentx02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows surprisex02
        with dissolve

    p "..."

    if night05_Interrogation_Vibrator_AngryNumber > night05_Interrogation_Vibrator_HappyNumber:

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows surprisex02
        with dissolve

    else:

        show neus_exp_mouth happy_Talkingx04
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows normal
        with dissolve

    ne "Mejor probemos otra."

    if night05_Interrogation_Vibrator_AngryNumber > night05_Interrogation_Vibrator_HappyNumber:

        show neus_exp_mouth happy_Silentx01
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows normal
        with dissolve

    else:

        show neus_exp_mouth happy_Silentx02
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_eyebrows surprisex01
        with dissolve

    menu night05_Park_WaterCoaster_Question:

        pt "Aparentemente ella tiene la primera y última palabra..."

        "Ok...":
            call p_Help

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "Podrías ponerle algo más de interés..."

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows serious
            with dissolve

            p "Debes admitir que tu lógica para saltarnos esta atracción es algo retorcida..."

            if night05_Interrogation_Vibrator_Number > 1:

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Después de haberme encendido ese trasto más de [night05_Interrogation_Vibrator_Number] veces..."

                if night05_Interrogation_Vibrator_AngryNumber > 1:

                    show neus_exp_mouth sad_Talkingx08
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "¡Y [night05_Interrogation_Vibrator_AngryNumber] de ellas porque te ha salido de las narices!"

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows suspiciousx02
                with dissolve

                ne "¿Aún te atreves a decir que mi lógica de estar mojada es retorcida?"

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx03
                with dissolve

                p "..."

                show neus_exp_mouth sadbiting_Silentx01
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows serious
                with dissolve

                p "Pero ¿qué tiene que ver estar mojada de abajo con mojarte con agua?"

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_eyes 03
                show neus_exp_iris left03
                show neus_exp_eyebrows suspiciousx01
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_eyes 04
                show neus_exp_iris left04
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Yo sé lo que me digo..."

                show neus_exp_mouth sadbiting_Silentx01
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx02
                with dissolve

                p "Vale,"

                extend " vale,"

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyes 04
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx01
                with dissolve

                p "como quieras."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyes 05
                show neus_exp_iris left05
                show neus_exp_eyebrows sadx02
                with dissolve


            else:

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyes 01
                show neus_exp_iris left01
                show neus_exp_eyebrows suspiciousx01
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx002
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows surprisex01
                with dissolve

                ne "Si no has encendido ese trasto de las narices es porque no has querido..."

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows normal
                with dissolve

                p "Pero si no lo he hecho,"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex02
                with dissolve

                p  "¿por qué estás mojada?"

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyes 01
                show neus_exp_iris left01
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx002
                show neus_exp_eyes 02
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "Porque..."

                show neus_exp_mouth sad_Talkingx06
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx01
                with dissolve

                ne "Porque podías encenderlo en cualquier momento..."

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyes 03
                show neus_exp_iris left03
                show neus_exp_eyebrows suspiciousx01
                with dissolve

                ne "¡Y eso pone caliente a cualquiera!"

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyes 04
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx01
                with dissolve

                pt "Si tú lo dices..."

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyes 05
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx02
                with dissolve

        "Eres tú la que manda, ¿no?":
            call p_Help
            $pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "¿Es necesario que seas tan gruñón?"

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with dissolve

            p "¿Qué?"

            show neus_exp_mouth sad_Silentx01
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex03
            with dissolve

            p "¡¿No estás decidiendo tú en todo momento a dónde ir?!"

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "Tampoco hace falta que te lo tomes así..."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx06
            with dissolve

            p "..."

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 05
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with dissolve

        "De acuerdo.":
            call p_Help
            $pl.ch_pts("np",1)

            show neus_exp_mouth happy_Talkingx07
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "Así me gusta."

            show neus_exp_mouth happy_Silentx06
            show neus_exp_eyes 06
            show neus_exp_iris front06
            show neus_exp_eyebrows surprisex01
            with dissolve

    pause 0.2


label night05_Park_RollerCoaster:

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    n "Seguís andando hasta toparos con lo que es sin duda la montaña rusa más emocionante del parque."

    scene bg night05_bg_tibidabo_park_coaster_entrance:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.0 ypos 1.0
        ease 7.0 zoom 0.7 xpos 0.6 ypos 0.3
    with fade

    ne "No se puede comparar al {a=https://es.wikipedia.org/wiki/Dragon_Khan}Dragon Khan{/a} o al {a=https://es.wikipedia.org/wiki/Shambhala_(montaña_rusa)}Shambala{/a} de {a=https://es.wikipedia.org/wiki/PortAventura_Park}Port Aventura{/a},"

    window hide dissolve
    pause

    scene bg night05_bg_tibidabo_park_coaster_entrance:
        truecenter
        zoom 0.7 xpos 0.6 ypos 0.3

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth happy_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows normal:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    

    ne "Pero ¿qué tal si nos subimos a esta?"

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    menu night05_Park_RollerCoaster_Question:

        "Claro, puede ser interesante.":
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_Park_RollerCoaster_Queuing_Enjoyed_Cond = True

            jump night05_Park_RollerCoaster_On

        "Me lo preguntas como si pudiera decidir...":
            call p_Help

            $ night05_Park_RollerCoaster_Doubt = True

            $pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx02
            with dissolve

            ne "..."

            if music_play != "bittersweet":
                play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bittersweet"

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "Te lo pregunto porque me interesa tu opinión."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "Estúpido."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows serious
            with dissolve

            p "¿Entonces realmente me das a elegir?"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx01
            with dissolve

            ne "¡Por supuesto!"

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "Si no, ¿por qué te lo preguntaría?"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows angryx03
            with dissolve

            p "Porque acabas haciendo lo que te da la gana."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Talkingx004
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "Entonces no quieres subir,"

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx03
            with dissolve

            ne "¿verdad?"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows angryx04
            with dissolve

            menu night05_Park_RollerCoaster_CanDecide_Question:

                "Sí, quiero subir.":
                    call p_Help

                    $pl.ch_pts("np",1)

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "Si igualmente querías subir,"

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "¿a qué ha venido eso?"

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows normal
                    with dissolve

                    p "Quería saber si aceptabas un no por respuesta."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx01
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    ne "¿Tan autoritaria me ves?"

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows serious
                    with dissolve

                    p "Un poco..."

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx02
                    show neus_exp_eyes 01
                    show neus_exp_iris left01
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    p "Pero ahora me has dado a elegir,"

                    show neus_exp_mouth sadbiting_Silentx01
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    p "y eso me ha gustado."

                    show neus_exp_mouth sadbiting_Silentx03
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    p "Va,"

                    extend " venga,"

                    show neus_exp_mouth sadbiting_Silentx01
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    p "no pongas esa cara y subamos."

                    jump night05_Park_RollerCoaster_On

                "No, no quiero subir.":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    show neus_exp_mouth sad_Silentx02
                    show neus_exp_eyebrows surprisex01
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyebrows sadx02
                    show neus_exp_eyes 02
                    show neus_exp_iris left02
                    with dissolve

                    p "¿Qué?"

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyebrows sadx03
                    show neus_exp_eyes 03
                    show neus_exp_iris left03
                    show neus_exp_tears 04_01
                    with dissolve

                    ne "Nada."

                    show neus_exp_mouth sad_Talkingx02
                    show neus_exp_eyebrows sadx04
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_tears 06_01
                    with dissolve

                    ne "Como quieras."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyebrows sadx05
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_tears 06_02
                    with dissolve

                    pt "Me dejará decidir,"

                    show neus_exp_mouth sadbiting_Silentx06
                    show neus_exp_eyebrows sadx06
                    show neus_exp_eyes 08
                    show neus_exp_iris front08
                    show neus_exp_tears 08_02
                    with dissolve

                    pt "pero con esa cara de mala leche que me pone,"

                    show neus_exp_mouth sadbiting_Silentx07
                    show neus_exp_eyebrows sadx07
                    show neus_exp_eyes 07
                    show neus_exp_iris front07
                    show neus_exp_tears 07_03
                    with dissolve

                    pt "deja bien claro que no es una opción que acepte de buen grado..."

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyebrows angryx01
                    show neus_exp_eyes 02
                    show neus_exp_iris right02
                    show neus_exp_tears empty
                    with dissolve

                    ne "Vamos."

                    show neus_exp_mouth sadbiting_Silentx04
                    show neus_exp_eyebrows sadx05
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    with dissolve

                    p "..."

                    jump night05_Park_RollerCoaster_After

        "Prefiero no subir a esta atracción.":
            call p_Help

            #$pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 00
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            ne "¿Por qué?"

            if music_play != "bittersweet":
                play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bittersweet"

            show neus_exp_mouth sadbiting_Silentx03
            show neus_exp_eyes 01
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            p "No soy muy fan de las montañas rusas."

            show neus_exp_mouth sadbiting_Silentx04
            show neus_exp_eyes 03
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyes 04
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            p "¿Qué?"

            show neus_exp_mouth sad_Talkingx002
            show neus_exp_eyes 04
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Nada,"

            extend " nada..."

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyes 03
            show neus_exp_iris right03
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "Hay cosas que a mí tampoco me gustan..."

            show neus_exp_mouth sad_Talkingx02
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Así que lo entiendo..."

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyes 03
            show neus_exp_iris front03
            show neus_exp_eyebrows serious
            with dissolve

            p "Gracias por tu comprensión Neus."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyes 04
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            jump night05_Park_RollerCoaster_After

label night05_Park_RollerCoaster_On:

    $ night05_Park_RollerCoaster_Used = True

    if night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == True:

        play sound "audio/characters/neus/giggle02.ogg"

        show neus_exp_mouth happy_Silentx06
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_eyebrows surprisex01
        with dissolve

        n "Una dulce sonrisa se dibuja en su rostro."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "Pero..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "Vamos a hacer por lo menos media hora de cola por lo que estoy viendo."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Sí..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Eso nos va a pasar en cualquier atracción a la que queramos subir."

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿No podrías...?"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "Ya me gustaría..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Pero hay demasiada gente,"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 04
    show neus_exp_iris down04
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "y tampoco puedo hacerlo muy a menudo..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Además,"

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "como ya te he contado,"

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows serious
    with dissolve

    ne "a veces es un riesgo demasiado alto,"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "por lo que es mejor no usarlo a la ligera."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with dissolve

    p "Ya..."

    show neus_exp_mouth sadbiting_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Bueno,"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx03
    with dissolve

    p "tenía que preguntar."

    if night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == True:

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "Siempre puedes pensar que estás disfrutando de mi compañía,"

        show neus_exp_mouth happy_Talkingx03
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows normal
        with dissolve

        ne "a pesar de estar esperando en la cola."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows surprisex02
        with dissolve

        p "Con lo peligrosa que eres"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows serious
        with dissolve

        p "y lo mojada que estás..."

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "¡Oye!"

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows serious
        with dissolve

        ne "También me sé aguantar..."

        show neus_exp_blush 03
        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "Especialmente sabiendo que luego me lo recompensarás."

        show neus_exp_mouth happybiting_Silentx02
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows normal
        with dissolve

        p "No sé,"

        extend " no sé..."

        show neus_exp_mouth happy_Talkingx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows surprisex01
        with dissolve

        ne "Tranquilo,"

        show neus_exp_mouth happy_Talkingx04
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "haré que la espera valga la pena."

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_eyebrows surprisex01
        with dissolve

        ne "Lo de ayer fue simplemente un tentempié."

        show neus_exp_mouth happy_Talkingx02
        show neus_exp_eyes 06
        show neus_exp_iris front06
        show neus_exp_eyebrows surprisex02
        with dissolve

        ne "Jejeje"

        show neus_exp_mouth happybiting_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows surprisex01
        with dissolve

        pt "La madre que la parió..."

    if night05_Interrogation_DidacAgainBeingMan_Cond == True:

        show neus_exp_mouth happy_Silentx04
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_eyebrows normal
        with dissolve

        pt "Sabiendo que Dídac volverá igualmente a la normalidad,"

        show neus_exp_mouth happy_Silentx02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows serious
        with dissolve

        pt "¿qué obligación tengo ahora...?"

        menu night05_Park_RollerCoaster_IfIGetBackToPedrera_Question:

            "<Recordarle que puedes volverte a casa después de la cita>":
                call p_Help

                $pl.ch_pts("np",-1)

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows normal
                with dissolve

                p "Siempre y cuando vaya a tu piso después de la cita."

                show neus_exp_mouth sad_Talkingx02
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with dissolve

                ne "¿Euh...?"

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyes 00
                show neus_exp_iris front00
                show neus_exp_eyebrows serious
                with dissolve

                p "Ahora que sé que Dídac volverá a la normalidad de todos modos,"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows sadx02
                with dissolve

                p "no tengo ninguna obligación."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyes 02
                show neus_exp_iris right02
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "..."

                show neus_exp_mouth sad_Talkingx05
                show neus_exp_eyes 03
                show neus_exp_iris right03
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "A parte de exigirte acudir a las tres citas,"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyes 03
                show neus_exp_iris left03
                show neus_exp_eyebrows sadx06
                with dissolve

                ne "no te he obligado a hacer nada que no quisieras."

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx07
                with dissolve

                pt "Eso de que no me ha obligado a hacer nada,"

                show neus_exp_mouth sadbiting_Silentx05
                show neus_exp_eyes 04
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx06
                with dissolve

                pt "sería discutible..."

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "¿Qué te hace pensar que te forzaré ahora entonces?"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx03
                with dissolve

                menu night05_Park_RollerCoaster_IfIGetBackToPedrera_Obligation_Question:

                    "<Aceptar que tiene razón>":
                        call p_Help

                        show neus_exp_mouth sadbiting_Silentx02
                        show neus_exp_eyes 03
                        show neus_exp_iris front03
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        p "Lo sé,"

                        extend " lo sé..."

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyes 02
                        show neus_exp_iris front02
                        show neus_exp_eyebrows sadx01
                        with dissolve

                        p "Simplemente quería dejarte claro que tengo esa opción."

                        show neus_exp_mouth sad_Talkingx004
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows angryx02
                        with dissolve

                        ne "Siempre has tenido esa opción."

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyes 03
                        show neus_exp_iris front03
                        show neus_exp_eyebrows angryx02
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "¿Tantas ganas tienes de deshacerte de mí...?"

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyes 03
                        show neus_exp_iris right03
                        show neus_exp_eyebrows sadx04
                        with dissolve

                        p "Yo..."

                        show neus_exp_mouth sad_Talkingx002
                        show neus_exp_eyes 03
                        show neus_exp_iris front03
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "Por favor,"

                        show neus_exp_mouth sad_Talkingx03
                        show neus_exp_eyes 02
                        show neus_exp_iris front02
                        show neus_exp_eyebrows sadx05
                        with dissolve

                        ne "solo te pido que intentes disfrutar estas pocas horas que nos quedan juntos..."

                        show neus_exp_mouth sad_Talkingx04
                        show neus_exp_eyes 02
                        show neus_exp_iris left02
                        show neus_exp_eyebrows sadx04
                        with dissolve

                        ne "Si después no quieres volverme a ver,"

                        show neus_exp_mouth sad_Talkingx05
                        show neus_exp_eyes 03
                        show neus_exp_iris right03
                        show neus_exp_eyebrows sadx05
                        with dissolve

                        ne "te prometo que no te volveré a molestar nunca más."

                        show neus_exp_mouth sadbiting_Silentx04
                        show neus_exp_eyes 02
                        show neus_exp_iris right02
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        p "..."

                        show neus_exp_mouth sadbiting_Silentx02
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows serious
                        with dissolve

                        pt "Es difícil decirle que no."

                        jump night05_Park_RollerCoaster_Queuing

                    "<Reprocharle que ayer te hizo comer esos platos veganos>":
                        call p_Help

                        $pl.ch_pts("np",-3)

                        show neus_exp_mouth sad_Silentx03
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        p "¿Cómo llamarías entonces lo de llevarme a un restaurante vegano,"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyes 00
                        show neus_exp_iris front00
                        show neus_exp_eyebrows surprisex03
                        with dissolve

                        p "para obligarme a comerme algo que no quería?"

                        show neus_exp_mouth sad_Talkingx06
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows angryx03
                        with dissolve

                        ne "¡Te dije que si no te gustaba lo que te había pedido,"

                        show neus_exp_mouth sad_Talkingx07
                        show neus_exp_eyes 03
                        show neus_exp_iris front03
                        show neus_exp_eyebrows angryx04
                        with dissolve

                        ne "te invitaría a un {i}McRonald´s{/i} al salir!"

                        show neus_exp_mouth sadbiting_Silentx05
                        show neus_exp_eyes 02
                        show neus_exp_iris front02
                        show neus_exp_eyebrows angryx02
                        with dissolve

                        p "Me obligaste a comerlo."

                        show neus_exp_mouth sad_Talkingx08
                        show neus_exp_eyes 04
                        show neus_exp_iris front04
                        show neus_exp_eyebrows angryx05
                        with dissolve

                        ne "¡Te pedí que lo probaras!"

                        show neus_exp_mouth sad_Silentx07
                        show neus_exp_eyes 04
                        show neus_exp_iris front04
                        show neus_exp_eyebrows angryx05
                        with dissolve

                        p "..."

                        show neus_exp_mouth sad_Talkingx003
                        show neus_exp_eyes 03
                        show neus_exp_iris right03
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "¿Tanto te cuesta entender que simplemente intento conocerte mejor?"

                        show neus_exp_mouth sad_Silentx05
                        show neus_exp_eyes 04
                        show neus_exp_iris right04
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        p "..."

                        $ night05_Park_RollerCoaster_Queuing_Reproach_Cond = True

                        jump night05_Park_RollerCoaster_Queuing

                    "<Agradecerle su sinceridad y tu nueva capacidad de elección>":
                        call p_Help

                        $pl.ch_pts("np",3)

                        show neus_exp_mouth sadbiting_Silentx02
                        show neus_exp_eyes 02
                        show neus_exp_iris front02
                        show neus_exp_eyebrows normal
                        with dissolve

                        p "Lo sé."

                        show neus_exp_mouth sadbiting_Silentx01
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        p "Y te lo agradezco."

                        show neus_exp_mouth sad_Silentx02
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows suspiciousx01
                        with dissolve

                        p "Con esta libertad,"

                        show neus_exp_mouth happybiting_Silentx02
                        show neus_exp_eyes 02
                        show neus_exp_iris front02
                        show neus_exp_eyebrows serious
                        with dissolve

                        p "puedo disfrutar mucho mejor de tu compañía."

                        show neus_exp_mouth happybiting_Silentx03
                        show neus_exp_eyes 02
                        show neus_exp_iris right02
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "..."

                        show neus_exp_mouth happy_Talkingx03
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "Gracias [protname]."

                        show neus_exp_mouth happy_Silentx04
                        show neus_exp_eyes 07
                        show neus_exp_iris front07
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        $ night05_Park_RollerCoaster_Queuing_ThankHerForHonesty_Cond = True

                        $ night05_Park_RollerCoaster_Queuing_Enjoyed_Cond = True

                        jump night05_Park_RollerCoaster_Queuing

            "<No decir nada>":

                call p_Help

                $ night05_Park_RollerCoaster_Queuing_Enjoyed_Cond = True

                jump night05_Park_RollerCoaster_Queuing

    
label night05_Park_RollerCoaster_Queuing:

    scene bg night05_bg_tibidabo_park_coaster_entrance_02:
        truecenter
        zoom 0.5
    $ saturation_tint_level = "default"

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    if night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == True:

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_eyebrows suspiciousx03
        with fade_long305s

        pause 0.5

        play sound "audio/characters/neus/laugh02.ogg"

        show neus_exp_mouth happy_Talkingx08
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_eyebrows normal
        with dissolve

        n "Su peculiar personalidad y su picaresca,"

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 00
        show neus_exp_iris left00
        show neus_exp_eyebrows surprisex01
        with dissolve

        n "desembocan en ciertas carcajadas que distraen la atención de los que os acompañan haciendo la cola,"

        show neus_exp_mouth happy_Silentx06
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows surprisex03
        with dissolve

        n "pero consigue hacer más llevadera la espera de subir a la atracción."

    else:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_eyebrows sadx04
        with dissolve

        n "Debido a la tensa e incómoda situación,"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_eyebrows sadx05
        with dissolve

        n "pasáis la mayor parte de la espera en silencio,"

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx06
        with dissolve

        n "y sin prácticamente cruzaros las miradas."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_eyebrows sadx07
        with dissolve

        pt "Quizás he sido un poco demasiado duro con ella..."

label night05_Park_RollerCoaster_GettingOut:

    stop music fadeout 1.0
    $ music_play = ""
    $ renpy.music.play("audio/sfx/roller_coaster_screams.ogg", channel="sfx1",loop=True, fadeout=0.0, synchro_start=True, fadein=0.0)
    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')

    scene bg night05_bg_tibidabo_park_coaster_riding:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.25 ypos 0.7
        easein_bounce 5.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "Después de disfrutar del paisaje montañoso a más de ochenta kilómetros por hora,"

    play sound "audio/characters/neus/laugh01.ogg"

    $ saturation_tint_level = "verydark"

    n "ambos os dirigís a la salida de la estación entre risas,"

    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.8, delay=1.0, channel='sfx1')
    if music_play != "fireflies_and_stardust":
            play music "audio/music/kevinmacleod/fireflies_and_stardust.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "fireflies_and_stardust"

    play sound "audio/characters/neus/laugh02.ogg"

    scene bg night05_bg_tibidabo_park_coaster_entrance:
        truecenter
        zoom 0.7 xpos 0.35 ypos 0.3

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth happy_Talkingx05:
        neus_exp_atright_position
    show neus_exp_eyes 07:
        neus_exp_atright_position
    show neus_exp_iris front07:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with fade

    n "sin poder evitar los comentarios jocosos del que se sentaba en el vagón de atrás,"

    $ renpy.music.set_volume(0.1, delay=25.0, channel='sfx1')

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows normal
    with dissolve

    n "el cual había aparentado mucha valentía mientras hacía la cola entre las chicas que le rodeaban,"

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with dissolve

    n "y una vez sentado en el carruaje, le empezaron los sudores fríos"

    play sound "audio/characters/neus/giggle06.ogg"

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx06
    with dissolve

    n "terminando entre lloros y súplicas para que terminara su pesadilla."

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    p "A este me hubiera gustado verle en el {a=https://en.wikipedia.org/wiki/Star_Wars_Hyperspace_Mountain}Space Mountain{/a} de {a=https://es.wikipedia.org/wiki/Disneyland_Park_(París)}Disneyland París{/a}." # No Spanish Wiki for Space Mountain.

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 00
    show neus_exp_iris left00
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Ahh..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    ne "¿Pero qué dices?"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows serious
    with dissolve

    ne "¡Si esa atracción es una gozada!"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Una montaña rusa cubierta,"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows serious
    with dissolve

    ne "repleta de luces y estrellas en la oscuridad."

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    ne "Me pareció precioso."

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "Y además por lo visto,"

    show neus_exp_mouth happy_Silentx01
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "ahora está ambientando en el universo de {a=https://es.wikipedia.org/wiki/Star_Wars}Star Wars{/a},"

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    p "en lugar del clásico {a=https://es.wikipedia.org/wiki/De_la_Tierra_a_la_Luna}De la Tierra a la Luna{/a} de {a=https://es.wikipedia.org/wiki/Julio_Verne}Julio Verne{/a}."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Wow..."

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "Debe de ser una pasada estar entre láseres y naves."

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "Por eso lo digo,"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "si este hombre se ha asustado tanto viendo solo árboles,"

    show neus_exp_mouth happybiting_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx01
    with dissolve

    p "ahí dentro le hubiera cogido un ataque."

    play sound "audio/characters/neus/laugh01.ogg"

    show neus_exp_mouth happy_Talkingx09
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Jajaja"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Es posible."

    #$ saturation_tint_level = "dark"

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    n "Vuelves a sentir su cálida mano mientras te dedica una sonrisa."

    if night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False:

        pt "Parece que ha retomado el buen humor."

    ne "Sigamos."

    menu night05_Park_RollerCoaster_After_Question:

        "De acuerdo.":
            call p_Help

            $pl.ch_pts("np",1)

            ne "Así me gusta."

            # show neus_exp_mouth happy_Silentx06
            # show neus_exp_eyes 06
            # show neus_exp_iris front06
            # show neus_exp_eyebrows normal
            # with dissolve

            # pause 0.2

            jump night05_Park_RollerCoaster_After

        "Tú mandas, ¿no?":
            call p_Help

            $pl.ch_pts("np",-1)

            scene bg night05_bg_tibidabo_park_coaster_entrance:
                truecenter
                zoom 0.5

            scene bg_dark_a
            show n_closefromup_body sd:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_blush 01:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_eyes 01:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_iris front01:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_eyebrows angryx01:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_tears empty:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_mouth sad_Silentx03:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_glasses:
                zoom 0.5 xalign 0.5 yalign 0.5
            show n_closefromup_hair_front:
                zoom 0.5 xalign 0.5 yalign 0.5
            with fade

            ne "..."

            if music_play != "bittersweet":
                play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bittersweet"

            show n_closefromup_eyes 01
            show n_closefromup_iris right01
            show n_closefromup_eyebrows sadx05
            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "¿Por qué tienes que ser de esta manera?"

            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows sadx04
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            p "Eres tú quien está decidiéndolo todo."

            show n_closefromup_eyes 04
            show n_closefromup_iris right04
            show n_closefromup_eyebrows sadx06
            show n_closefromup_mouth sad_Silentx03
            with dissolve

            ne "..."

            show n_closefromup_eyes 01
            show n_closefromup_iris right01
            show n_closefromup_eyebrows sadx05
            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "¿De verdad me ves así...?"

            show n_closefromup_eyes 05
            show n_closefromup_iris right05
            show n_closefromup_eyebrows sadx07
            show n_closefromup_mouth sadbiting_Silentx04
            with dissolve

            p "..."

            jump night05_Park_RollerCoaster_After

label night05_Park_RollerCoaster_After:

    scene bg night05_bg_tibidabo_park_around01:
        subpixel True
        truecenter
        zoom 1.2 xpos 1.2 ypos 1.0
        easein_quad 20.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "Os cruzáis por delante de varias atracciones y su multitud,"

    n "algunas más interesantes que otras,"

    n "pero todas ellas peculiares y únicas;"

    scene bg night05_bg_tibidabo_park_shooter_surroundings:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 25.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "hasta llegar a lo que parece ser la zona lúdica,"

    n "que imita las paraditas típicas de las ferias en las fiestas mayores de los barrios."

    p "Pensaba que este tipo de espacios no existían en los parques de atracciones."

    show bg night05_bg_tibidabo_park_shooter_surroundings:
        zoom 0.5 xpos 0.5 ypos 0.5
    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx003:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris left01:
        neus_exp_atright_position
    show neus_exp_eyebrows suspiciousx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "Me imagino que si atrae a público,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "es algo extra que ganan."

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_eyebrows normal
    with dissolve

    pause 0.2


    ## Aquí es donde os encontráis a rata.

    scene bg night05_bg_tibidabo_park_shooter_barra:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    show night03_bar_barra_barman_body_b
    show night03_bar_barra_barman_eyes surprise:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_pupils surprise_left:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_mouth happy_Talkingx02:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_n_body_sd
    show night03_bar_barra_n_eyes 01:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_pupils right01:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_eyebrows surprisex02:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_glasses:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_mouth sad_Silentx03:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_hair_front:
        night03_bar_barra_n_expressions_pos
    with fade

    rat "¡Buenas noches Calavera!"

    if music_play != "happy_boy_end_theme":
        play music "audio/music/kevinmacleod/happy_boy_end_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "happy_boy_end_theme"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "¡¿Rata!?"

    show night03_bar_barra_n_eyebrows suspiciousx02
    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve

    ne "¿Qué haces aquí?" 

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex03
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    pt "¿Pero este tipo no es el barman de hace dos noches?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Talkingx02
    with dissolve

    rat "Estoy sustituyendo a mi primo feriante que está enfermo."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    pt "¿Y es necesario que se ponga también a limpiar la barra sin que esté sirviendo bebidas?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve

    ne "¿Te refieres a Cerdo?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex03
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    p "¿Cerdo?"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "Sí,"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "casi todos en su familia usan motes de animales para hablar entre ellos."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    p "¿Esos motes coinciden con sus facciones faciales también?"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows suspiciousx01
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    ne "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows suspiciousx03
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    p "..."

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows suspiciousx02
    show night03_bar_barra_n_mouth sad_Silentx04
    with dissolve

    pt "Desde luego,"

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows sadx03
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    pt "no me estoy ganando su simpatía..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Talkingx02
    with dissolve

    ne "Euh..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve

    ne "Los que yo he conocido por lo menos tienen un cierto parecido,"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "pero no lo hacen de forma despectiva,"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "es su manera de expresar afecto entre ellos."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    pt "No me quiero imaginar cómo debe de ser una reunión familiar..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "No se ofenden si lo dices con cariño."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex03
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "¿Verdad que no?"

    extend " Rata."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Silentx02
    with dissolve

    rat "Claro que no,"

    extend " preciosa."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    rat "Por ti me dejaría llamar lo que fuera."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex03
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    rat "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    pt "Ese por ti,"

    extend " y con esa mirada,"

    pt "desde luego me excluye a mí..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth sad_Talkingx02
    with dissolve

    ne "¿Y a quién has dejado a cargo del bar?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    rat "No te preocupes cariño,"

    show night03_bar_barra_barman_mouth happy_Talkingx02
    with dissolve

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    rat "está en buenas manos."

    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "Me alegra oír eso."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Talkingx02

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    if night03_barmaninsult_01_AskedWater == True:

        rat "Veo que sigues con el {b}grumete{/b} de agua dulce este a tu lado."

    else:

        rat "Veo que sigues con el {b}ganapán{/b} este a tu lado."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows angryx05
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "¡Rata!"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx03
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "¡No seas así hombre!"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows sadx04
    show night03_bar_barra_n_mouth sad_Silentx04
    with dissolve

    pt "Tienes suerte de que esté Neus a mi lado,"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    pt "si no te llevabas una hostia,"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth sad_Silentx04
    with dissolve

    pt "que tendrían que ir a la Luna para buscar tu dentadura."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth sad_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    rat "Apenas se bebió medio vaso,"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Talkingx02

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    rat "y al final lo tuviste que terminar tú;"

    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx05
    with dissolve

    rat "no me puedes negar que es un poco {b}bebecharcos{/b}..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows suspiciousx03
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    p "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows angryx04
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "Al menos no tiene una ballena entera por barriga como tú."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    rat "..."

    show night03_bar_barra_barman_mouth sad_Talkingx02

    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    rat "No hace falta que seas tan cruel conmigo, Calavera..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows angryx05
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "Eres tú quien ha empezado, Rata."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    p "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows angryx01
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    rat "Arghh..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows angryx02
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    rat "Cómo defiendes al marinero."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_front
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows suspiciousx01
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    rat "Esta bien..."

    
    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    rat "¿Y qué os trae por aquí?"

    extend " Parejita."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    rat "¿Os apetece probar suerte con la escopeta?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "¿Qué me dices [protname]?"

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "¿Quieres ver quién de los dos hace más puntos?"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    p "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve


    p "¿Y qué hacemos luego con el premio?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "Nos intercambiamos los regalos."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    menu night05_Park_MinigameShooter_HowGood_Question:

        "No soy demasiado bueno en esto...":
            call p_Help

            $ night05_Park_MinigameShooter_HowGood_NotGood = True

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "Venga, [protname]."

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth happy_Talkingx04
            with dissolve

            ne "Ya pago yo el precio."

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Talkingx04
            with dissolve

            ne "¿Qué te cuesta intentarlo?"

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            p "Vas a malgastar el dinero,"
   
            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Silentx04
            with dissolve

            p "y quizás solo consiga regalarte un globo."

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth happy_Talkingx02
            with dissolve

            ne "Pero será un globo que me habrás regalado tú."

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows angryx03
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

        "Me imagino que no me dejarás pagar a mí...":
            call p_Help

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth happy_Talkingx04
            with dissolve


            ne "Por supuesto que no."

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            p "¿Aunque fracase miserablemente?"

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth happy_Talkingx04
            with dissolve

            ne "Al menos lo habrás intentado a mi lado."

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows angryx04
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve


    p "Con tu dinero."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows angryx05
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "No seas tan aguafiestas."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    rat "Vas a desperdiciar tu oro con este {b}besugo{/b}."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows angryx05
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "¡Rata!"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows angryx04
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    pt "¿Soy yo?"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    with dissolve

    pt "¿o me está suplicando que le dé una hostia?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "Vamos..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows sadx03
    show night03_bar_barra_n_mouth sad_Silentx04
    with dissolve

    pt "Desde luego,"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx04
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    pt "no acepta un no por respuesta."

    menu night05_Park_MinigameShooter_Participate_Question:

        "Lo siento, pero no pienso hacerlo.":
            call p_Help

            $pl.ch_pts("np",-1)

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows angryx03
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            ne "..."

            play sound "audio/characters/barman/laugh_stupid02.ogg"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Talkingx02

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils right01
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            rat "Jajaja"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Talkingx01

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils right03
            show night03_bar_barra_n_eyebrows angryx05
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            rat "Es tan malo que no lo quiere ni intentar..."

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            with dissolve

            rat "¡Por lo menos es sincero el {b}bocachancla{/b}!"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth happy_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx01
            with dissolve

            ne "[protname]..."

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Talkingx02
            with dissolve

            ne "¿Por qué...?"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_left
            show night03_bar_barra_barman_mouth sad_Talkingx01

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils right01
            show night03_bar_barra_n_eyebrows normal
            show night03_bar_barra_n_mouth sad_Silentx04
            with dissolve

            rat "Será mejor que emplees tu dinero comprando sapos,"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_left
            show night03_bar_barra_barman_mouth happy_Talkingx01

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils right03
            show night03_bar_barra_n_eyebrows serious
            show night03_bar_barra_n_mouth sad_Silentx02
            with dissolve

            rat "seguro que te saldrán menos rana que este {b}cabezabuque{/b}."

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils right01
            show night03_bar_barra_n_eyebrows angryx06
            show night03_bar_barra_n_mouth sad_Talkingx04
            with dissolve

            ne "¡¿TE QUIERES CALLAR RATA?!"

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils right03
            show night03_bar_barra_n_eyebrows angryx05
            show night03_bar_barra_n_mouth sad_Silentx06
            with dissolve

            rat "..."

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx02
            with dissolve

            ne "Cuando te he dicho lo de a ver quién hacía más puntos,"

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "lo decía a modo de juego,"

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Talkingx04
            with dissolve

            ne "no me importa que hagas más,"

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx01
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "o menos puntos que yo,"

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Talkingx02
            with dissolve

            ne "simplemente quiero pasar un rato agradable contigo;"

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "¿tanto te estoy pidiendo?"

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Silentx03
            with dissolve

            p "Quizás el gordo seboso este te caiga bien,"

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Silentx04
            with dissolve

            p "pero a mí no me apetece estar cerca de él."

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils right03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Silentx05
            with dissolve

            rat "..."

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx01
            with dissolve

            ne "Por favor,"

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_left
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "olvídate de él..."

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx03
            show night03_bar_barra_n_mouth sad_Talkingx02
            with dissolve

            ne "solo inténtalo..."

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth sad_Talkingx03
            with dissolve

            ne "No te pido nada más."

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows sadx04
            show night03_bar_barra_n_mouth sad_Silentx04
            with dissolve

            menu night05_Park_MinigameShooter_Participate_02_Question:

                "Como ya te he dicho, no pienso hacerlo.":
                    call p_Help

                    $pl.ch_pts("np",-3)

                    # $ night05_Park_MinigameShooter_Played = False #Not really necessary, actually.

                    if music_play != "bittersweet":
                        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "bittersweet"

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows surprisex02
                    show night03_bar_barra_n_mouth sad_Silentx01
                    with dissolve

                    p "No obligas,"

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Silentx03
                    with dissolve

                    p "pero insistes de mala manera."

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Talkingx01

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils right03
                    show night03_bar_barra_n_eyebrows sadx03
                    show night03_bar_barra_n_mouth sad_Silentx04
                    with dissolve

                    rat "¡Serás desagradecido!"

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_front
                    show night03_bar_barra_barman_mouth sad_Talkingx02

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils right01
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Silentx03
                    with dissolve

                    rat "¡¿Eres consciente de la suerte que tienes de estar al lado de semejante perla de mujer?!"

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Talkingx01

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils right03
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Silentx02
                    with dissolve

                    rat "¡Bah!"

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Talkingx02

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils right03
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Silentx03
                    with dissolve

                    rat "¡¿Que va a saber un {b}pelagambas{/b} como tú de lo que vale una mujer?!"

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Silentx04
                    with dissolve

                    menu night05_Park_MinigameShooter_Participate_RatAgainst_Question:

                        "<Meterte con Rata>":
                            call p_Help

                            $pl.ch_pts("np",-2)

                            $ night05_Park_MinigameShooter_Participate_RatAgainst_Cond = True

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows surprisex01
                            show night03_bar_barra_n_mouth sad_Silentx02
                            with dissolve

                            p "Si tanta envidia me tienes,"

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows surprisex02
                            show night03_bar_barra_n_mouth sad_Silentx03
                            with dissolve

                            p "¿por qué no se lo has pedido tú?"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows sadx01
                            show night03_bar_barra_n_mouth sad_Silentx02
                            with dissolve

                            p "Está claro que hace tiempo que os conocéis,"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx01
                            show night03_bar_barra_n_mouth sad_Silentx03
                            with dissolve

                            p "así que oportunidades has tenido de sobra..."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx02
                            show night03_bar_barra_n_mouth sad_Silentx04
                            with dissolve

                            p "Oh,"

                            extend " espera..."

                            show night03_bar_barra_barman_eyes angry
                            show night03_bar_barra_barman_pupils angry_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx03
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            p "quizás realmente ya lo hayas hecho,"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils right03
                            show night03_bar_barra_n_eyebrows sadx04
                            show night03_bar_barra_n_mouth sad_Silentx06
                            with dissolve

                            p "y te dio calabazas..."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx02
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            p "¿¡Verdad?!"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx03
                            show night03_bar_barra_n_mouth sad_Silentx03
                            with dissolve

                            rat "..."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows surprisex02
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            p "¡Pero si tienes más tetas que ella!"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows angryx06
                            show night03_bar_barra_n_mouth sad_Talkingx04
                            with dissolve

                            ne "¡Ya basta!"

                            show night03_bar_barra_barman_eyes angry
                            show night03_bar_barra_barman_pupils angry_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows angryx05
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            p "..."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Talkingx01

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils right03
                            show night03_bar_barra_n_eyebrows angryx04
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            rat "Pero cariño..."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Talkingx02

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils right03
                            show night03_bar_barra_n_eyebrows suspiciousx03
                            show night03_bar_barra_n_mouth sad_Silentx04
                            with dissolve

                            rat "¿Has oído lo que me ha dicho?"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils right01
                            show night03_bar_barra_n_eyebrows angryx05
                            show night03_bar_barra_n_mouth sad_Talkingx04
                            with dissolve

                            ne "¡Admite que has empezado tú, Rata!"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Talkingx01

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils right03
                            show night03_bar_barra_n_eyebrows angryx03
                            show night03_bar_barra_n_mouth sad_Silentx05
                            with dissolve

                            rat "¿Pero no has escuchado lo que ha mencionado de tus...?"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils right01
                            show night03_bar_barra_n_eyebrows angryx06
                            show night03_bar_barra_n_mouth sad_Talkingx04
                            with dissolve

                            ne "{size=35}¡He dicho que ya basta!{/size}"

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows angryx05
                            show night03_bar_barra_n_mouth sad_Silentx04
                            with dissolve

                            rat "..."

                        "<Mejor no>":
                            call p_Help

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Talkingx02
                    with dissolve

                    ne "Si no quieres,"

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils right03
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Talkingx01
                    with dissolve

                    ne "no quieres."

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx03
                    show night03_bar_barra_n_mouth sad_Talkingx02
                    with dissolve

                    ne "No te voy a obligar a ello."

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Silentx01
                    with dissolve

                    p "Gracias."

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Talkingx02
                    with dissolve

                    ne "¿Podemos continuar?"

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_left
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Talkingx01
                    with dissolve

                    ne "¿O es que también te quieres ir ya a casa?"

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Silentx02
                    with dissolve

                    p "¿Me das la oportunidad de irme?"

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_left
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx03
                    show night03_bar_barra_n_mouth sad_Talkingx02
                    with dissolve

                    ne "Si es lo que quieres,"

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx02
                    show night03_bar_barra_n_mouth sad_Talkingx01
                    with dissolve

                    ne "no te voy a obligar a estar aquí en contra de tu voluntad."

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx01
                    show night03_bar_barra_n_mouth sad_Silentx02
                    with dissolve

                    p "¿Y Dídac volverá a la normalidad?"

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Talkingx01
                    with dissolve

                    ne "Tienes mi palabra."

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx03
                    show night03_bar_barra_n_mouth sad_Silentx04
                    with dissolve

                    menu night05_Park_MinigameShooter_Participate_GoHome_Question:

                        "<Ir a casa>" if night05_Park_MinigameShooter_Participate_GoHome_Cond == False:
                            call p_Help

                            $ night05_Park_MinigameShooter_Participate_GoHome_Cond = True

                            p "..."

                            pt "No..."

                            pt "Aún no es buena idea irse."

                            pt "No me fío un pelo de la palabra de esta chica..."

                            pt "No cuando falta tan poco para terminar la noche."

                            jump night05_Park_MinigameShooter_Participate_GoHome_Question

                        "<Quedarte>":
                            call p_Help

                            $pl.ch_pts("np",1)

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows normal
                            show night03_bar_barra_n_mouth sad_Silentx02
                            with dissolve

                            p "Podemos continuar."

                            show night03_bar_barra_barman_eyes surprise
                            show night03_bar_barra_barman_pupils surprise_left
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx01
                            show night03_bar_barra_n_mouth happy_Silentx02
                            with dissolve

                            ne "..."

                            show night03_bar_barra_n_eyes 01
                            show night03_bar_barra_n_pupils front01
                            show night03_bar_barra_n_eyebrows sadx02
                            show night03_bar_barra_n_mouth happy_Talkingx02
                            with dissolve

                            ne "Gracias [protname]."

                            show night03_bar_barra_barman_eyes angry
                            show night03_bar_barra_barman_pupils angry_front
                            show night03_bar_barra_barman_mouth sad_Silent

                            show night03_bar_barra_n_eyes 03
                            show night03_bar_barra_n_pupils front03
                            show night03_bar_barra_n_eyebrows sadx02
                            show night03_bar_barra_n_mouth happy_Silentx03
                            with dissolve

                            window hide dissolve
                            pause

                            jump night05_Park_MinigameShooter_After

                                #label night05_Park_MinigameShooter_After:

                                    #n "Sientes otra vez su cálida mano."

                                    #ne "Vamos,"

                                    #ne "aún hay tiempo para probar alguna atracción más."

                                    #ne "Volvéis a cruzar gran parte del parque hasta llegar a ese lugar tan repleto de gente."

                                    #ne "¡Uooh!"

                "<De acuerdo...>":
                    call p_Help

                    $pl.ch_pts("np",1)

                    show night03_bar_barra_barman_eyes surprise
                    show night03_bar_barra_barman_pupils surprise_left
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows sadx04
                    show night03_bar_barra_n_mouth sad_Talkingx02
                    with dissolve

                    ne "Gracias [protname]."

                    show night03_bar_barra_barman_eyes angry
                    show night03_bar_barra_barman_pupils angry_front
                    show night03_bar_barra_barman_mouth sad_Silent

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows sadx01
                    show night03_bar_barra_n_mouth sad_Silentx02
                    with dissolve

                    rat "..."

                    jump night05_Park_MinigameShooter_Introduction


        "De acuerdo.":
            call p_Help

            $pl.ch_pts("np",1)

            show night03_bar_barra_barman_eyes surprise
            show night03_bar_barra_barman_pupils surprise_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth happy_Talkingx02
            with dissolve

            ne "Así me gusta."

            show night03_bar_barra_barman_eyes angry
            show night03_bar_barra_barman_pupils angry_front
            show night03_bar_barra_barman_mouth sad_Silent

            show night03_bar_barra_n_eyes 03
            show night03_bar_barra_n_pupils front03
            show night03_bar_barra_n_eyebrows surprisex02
            show night03_bar_barra_n_mouth happy_Silentx05
            with dissolve

            window hide dissolve
            pause

            jump night05_Park_MinigameShooter_Introduction



########################################################################
########################################################################

########################################################################
########################################################################

label night05_Park_MinigameShooter_Finished:

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "almost_new_kevin"

    if MShooter_points == 25: # Golden Bracelet
        $ MShooter_Bracelet = "GOLD"# GOLD
    elif MShooter_points >= 20: # Silver Bracelet
        $ MShooter_Bracelet = "SILVER" # SILVER
    elif MShooter_points >= 15: # Bronze Bracelet
        $ MShooter_Bracelet = "BRONZE" # BRONZE
    elif MShooter_points >= 10: # Pink Bracelet
        $ MShooter_Bracelet = "PLASTIC" # PLASTIC PINK
    else: #Nothing
        $ MShooter_Bracelet = "" # Nothing


    scene bg night05_bg_tibidabo_park_shooter_barra:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    show night03_bar_barra_barman_body_b
    show night03_bar_barra_barman_eyes angry:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_pupils angry_front:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_mouth sad_Silent:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_n_body_sd
    show night03_bar_barra_n_eyes 01:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_pupils front01:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_eyebrows surprisex02:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_glasses:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_mouth happy_Silentx03:
        night03_bar_barra_n_expressions_pos
    show night03_bar_barra_n_hair_front:
        night03_bar_barra_n_expressions_pos
    with fade

    if MShooter_points >= 10:

        show bg_dark_a
        show night05_tibidabo_bracelet_MCShow_comp:
            subpixel True
            truecenter
            zoom 0.6 xpos 0.52 ypos 0.5
            ease 10.0 zoom 0.375 xpos 0.5 ypos 0.5
        with fade

        p "Toma,"

        hide bg_dark_a
        hide night05_tibidabo_bracelet_MCShow_comp
        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth happy_Silentx04
        with fade

        p "el premio que he ganado."

    if MShooter_points == 25: # Golden Bracelet

        #$ MShooter_Bracelet = "GOLD"# GOLD

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows suspiciousx02
        show night03_bar_barra_n_mouth sad_Talkingx03
        with dissolve

        ne "¡Y luego decías que esto no se te daba bien!"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows angryx01
        show night03_bar_barra_n_mouth happy_Talkingx04
        with dissolve

        ne "¡Has conseguido todos los puntos!"

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_front

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows suspiciousx03
        show night03_bar_barra_n_mouth happy_Silentx01
        with dissolve

        p "Quizás solo quería impresionarte."

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "Lo has hecho."

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows serious
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "Pero ya me daba por satisfecha,"

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx02
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "con el simple hecho de que lo hayas intentado a mi lado."

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils right03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Silentx04
        with dissolve


    elif MShooter_points >= 20: # Silver Bracelet

        #$ MShooter_Bracelet = "SILVER" # SILVER

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth sad_Silentx02
        with dissolve

        p "Siento no haberte conseguido la dorada."

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows suspiciousx03
        show night03_bar_barra_n_mouth sad_Talkingx03
        with dissolve

        ne "¿Estás de broma?"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows normal
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "El plateado es un color metálico que me encanta."

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows angryx01
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "Además,"

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth happy_Talkingx01
        with dissolve

        ne "para ser tu primera vez,"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex02
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "has estado realmente increíble,"

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils right03
        show night03_bar_barra_n_eyebrows suspiciousx01
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "de hecho, te ha faltado bien poco para conseguir una puntuación perfecta."

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows suspiciousx01
        show night03_bar_barra_n_mouth happy_Silentx05
        with dissolve

    elif MShooter_points >= 15: # Bronze Bracelet

        #$ MShooter_Bracelet = "BRONZE" # BRONZE

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth sad_Silentx01
        with dissolve

        p "Siento que debas conformarte con el tercer premio..."

    elif MShooter_points >= 10: # Pink Bracelet

        #$ MShooter_Bracelet = "PLASTIC" # PLASTIC PINK

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth sad_Silentx01
        with dissolve

        p "Siento que debas conformarte con el brazalete de plástico..."

    else: #Nothing

        #$ MShooter_Bracelet = "" # Nothing

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth sad_Silentx01
        with dissolve

        

    if MShooter_Bracelet == "PLASTIC" or MShooter_Bracelet == "BRONZE":

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows serious
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "No seas absurdo,"

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "para ser tu primera vez, lo has hecho muy bien."

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows normal
        show night03_bar_barra_n_mouth happy_Silentx03
        with dissolve

    if MShooter_Bracelet == "PLASTIC": # PLASTIC PINK

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Talkingx01

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils right01
        show night03_bar_barra_n_eyebrows surprisex02
        show night03_bar_barra_n_mouth sad_Silentx01
        with dissolve

        rat "¡Ja!"

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_front
        show night03_bar_barra_barman_mouth happy_Talkingx02

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils right03
        show night03_bar_barra_n_eyebrows angryx02
        show night03_bar_barra_n_mouth sad_Silentx02
        with dissolve

        rat "¡Ni en mi primera vez saqué tan mala puntuación!"

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils right01
        show night03_bar_barra_n_eyebrows angryx05
        show night03_bar_barra_n_mouth sad_Talkingx04
        with dissolve

        ne "¡¿Te quieres callar de una vez Rata?!"

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils right03
        show night03_bar_barra_n_eyebrows angryx03
        show night03_bar_barra_n_mouth sad_Silentx04
        with dissolve

        rat "..."

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Silentx03
        with dissolve

    p "..."

    if MShooter_points < 10:

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front
        show night03_bar_barra_barman_mouth happy_Silent

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Silentx01
        with dissolve

        p "Lo siento Neus."

        if night05_Park_MinigameShooter_HowGood_NotGood == True:

            show night03_bar_barra_n_eyes 01
            show night03_bar_barra_n_pupils front01
            show night03_bar_barra_n_eyebrows sadx01
            show night03_bar_barra_n_mouth happy_Silentx02
            with dissolve

            p "Como ya te había advertido,"

            show night03_bar_barra_n_eyebrows sadx02
            show night03_bar_barra_n_mouth happy_Silentx03
            with dissolve

            p "no soy nada bueno en esto."

        else:

            show night03_bar_barra_n_eyebrows sadx01
            show night03_bar_barra_n_mouth happy_Silentx02
            with dissolve

            p "No he ganado nada."

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows normal
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "Y yo te he dicho que no me importa,"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Talkingx01
        with dissolve

        ne "atesoro mucho más el recuerdo el tiempo que hemos pasado juntos,"

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx02
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "que un objeto que se pueda perder o estropear."

    if MShooter_points >= 10:

        show night03_bar_barra_barman_eyes surprise
        show night03_bar_barra_barman_pupils surprise_left
        show night03_bar_barra_barman_mouth sad_Silent

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex02
        show night03_bar_barra_n_mouth happy_Talkingx03
        with dissolve

        ne "Guardaré este regalo por el resto de mi vida."

        show night03_bar_barra_barman_eyes angry
        show night03_bar_barra_barman_pupils angry_front

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Silentx03
        with dissolve

        pt "No sé yo si este tipo de baratijas de feria duran tanto..."

    if MShooter_points >= 15: # GSB Bracelet

        pt "Además,"

    if MShooter_Bracelet == "GOLD": # Golden Bracelet

        pt "esto tiene de oro,"

    elif MShooter_Bracelet == "SILVER": # Silver Bracelet

        pt "esto tiene de plata,"

    elif MShooter_Bracelet == "BRONZE": # Bronze Bracelet

        pt "esto tiene de bronce,"

    if MShooter_points >= 15: # GSB Bracelet

        pt "lo que yo tengo de vidente."

    elif MShooter_Bracelet == "PLASTIC": # PLASTIC PINK

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth sad_Silentx03
        with dissolve

        p "¿Seguro que lo quieres?"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex02
        show night03_bar_barra_n_mouth sad_Silentx02
        with dissolve

        p "No sé muy bien si te gusta el rosa,"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows suspiciousx01
        show night03_bar_barra_n_mouth sad_Silentx01
        with dissolve

        p "siendo tú tan gótica..."

        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "Es cierto que no es de mis colores favoritos,"

        show night03_bar_barra_n_eyes 01
        show night03_bar_barra_n_pupils front01
        show night03_bar_barra_n_eyebrows surprisex01
        show night03_bar_barra_n_mouth happy_Talkingx02
        with dissolve

        ne "pero no creo que me quede tan mal."

    if MShooter_points >= 10: # GSBP Bracelet

        show bg_dark_a
        show night05_tibidabo_bracelet_SheShow_comp:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.4 ypos 0.5
            ease 4.0 zoom 0.375 xpos 0.5 ypos 0.5
        with fade

        ne "¿Qué opinas?"

        window hide dissolve
        pause

        hide bg_dark_a
        hide night05_tibidabo_bracelet_SheShow_comp
        show night03_bar_barra_n_eyes 03
        show night03_bar_barra_n_pupils front03
        show night03_bar_barra_n_eyebrows sadx01
        show night03_bar_barra_n_mouth happy_Silentx03
        with fade

        menu night05_Park_MinigameShooter_BraceletLooking_Question:

            "Creo que te queda bien.":
                call p_Help

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows surprisex01
                show night03_bar_barra_n_mouth happy_Talkingx03
                with dissolve

                ne "¿Verdad que sí?"

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows surprisex02
                show night03_bar_barra_n_mouth happy_Silentx05
                with dissolve

                pt "Al final pensaré realmente que se hubiera contentado con un globo y todo..."

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows sadx01
                show night03_bar_barra_n_mouth happy_Talkingx02
                with dissolve

                ne "Gracias, [protname]."

                jump night05_Park_MinigameShooter_Finished_HerPresent

            "Me hubiera gustado poderte regalar el dorado." if not MShooter_Bracelet == "GOLD": # GOLD
                call p_Help

                show night03_bar_barra_barman_eyes angry
                show night03_bar_barra_barman_pupils angry_front
                show night03_bar_barra_barman_mouth happy_Silent

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows angryx01
                show night03_bar_barra_n_mouth sad_Talkingx01
                with dissolve

                ne "Tonto..."

                show night03_bar_barra_barman_eyes surprise
                show night03_bar_barra_barman_pupils surprise_left
                show night03_bar_barra_barman_mouth sad_Silent

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows serious
                show night03_bar_barra_n_mouth sad_Talkingx02
                with dissolve

                ne "Ya te he dicho que me encanta el que me has regalado."

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows normal
                show night03_bar_barra_n_mouth happy_Talkingx02
                with dissolve

                ne "Aunque no hubieras conseguido premio alguno,"

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows sadx01
                show night03_bar_barra_n_mouth happy_Talkingx01
                with dissolve

                ne "con el simple hecho de que lo hayas intentado,"

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows surprisex02
                show night03_bar_barra_n_mouth happy_Talkingx02
                with dissolve

                ne "ya me has hecho muy feliz."

                show night03_bar_barra_barman_eyes angry
                show night03_bar_barra_barman_pupils angry_front
                show night03_bar_barra_barman_mouth sad_Silent

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows normal
                show night03_bar_barra_n_mouth happy_Silentx04
                with dissolve

                p "..."

                jump night05_Park_MinigameShooter_Finished_HerPresent

            "Quizás uno negro te hubiera quedado mejor.":
                call p_Help

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows surprisex02
                show night03_bar_barra_n_mouth sad_Talkingx02
                with dissolve

                ne "Naah..."

                show night03_bar_barra_barman_eyes surprise
                show night03_bar_barra_barman_pupils surprise_left

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows suspiciousx01
                show night03_bar_barra_n_mouth sad_Talkingx03
                with dissolve

                ne "No creo..."

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows suspiciousx02
                show night03_bar_barra_n_mouth happy_Talkingx02
                with dissolve

                ne "Hubiera pasado desapercibido con el guante y mi vestimenta."

                if MShooter_Bracelet == "GOLD": # GOLD

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows surprisex01
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "El dorado siempre ha sido un metal preciado y mágico,"

                elif MShooter_Bracelet == "SILVER": # SILVER

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows surprisex01
                    show night03_bar_barra_n_mouth happy_Talkingx03
                    with dissolve

                    ne "Además, el plateado se parece mucho al blanco,"

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows surprisex02
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "y no desentona tanto con mi vestido."

                elif MShooter_Bracelet == "BRONZE": # BRONZE

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows surprisex01
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "El bronce es un metal con mucha historia y no es tan ostentoso como el oro,"

                elif MShooter_Bracelet == "PLASTIC": # PLASTIC PINK

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows surprisex01
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "Así rosado me da un toque de color,"

                if (MShooter_Bracelet == "GOLD" or MShooter_Bracelet == "BRONZE"):

                    show night03_bar_barra_n_eyes 03
                    show night03_bar_barra_n_pupils front03
                    show night03_bar_barra_n_eyebrows surprisex03
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "además me da un toque de color entre tanto blanco y negro."

                show night03_bar_barra_n_eyes 01
                show night03_bar_barra_n_pupils front01
                show night03_bar_barra_n_eyebrows surprisex03
                show night03_bar_barra_n_mouth happy_Talkingx03
                with dissolve

                ne "¿No crees?"

                if MShooter_Bracelet == "PLASTIC": # PLASTIC PINK

                    show night03_bar_barra_n_eyes 01
                    show night03_bar_barra_n_pupils front01
                    show night03_bar_barra_n_eyebrows suspiciousx03
                    show night03_bar_barra_n_mouth happy_Talkingx02
                    with dissolve

                    ne "Quizás hasta parezco más femenina y todo."

                show night03_bar_barra_barman_eyes angry
                show night03_bar_barra_barman_pupils angry_front

                show night03_bar_barra_n_eyes 03
                show night03_bar_barra_n_pupils front03
                show night03_bar_barra_n_eyebrows suspiciousx01
                show night03_bar_barra_n_mouth happy_Silentx02
                with dissolve

                menu night05_Park_MinigameShooter_BraceletLooking_Color_Question:

                    "Me gustas más cuando solo vistes en blanco y negro.":
                        call p_Help

                        $pl.ch_pts("np",1)

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex03
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        ne "..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "Me alegra saber que te gusta mi estilo de vestir,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth happy_Talkingx01
                        with dissolve

                        ne "pero a veces también puedo llevar otros colores..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx02
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "Tampoco soy un televisor en blanco y negro."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex02
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        p "Te lo decía como un cumplido."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Talkingx01
                        with dissolve

                        ne "Lo sé..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "Pero me gustaría pensar que te seguiría gustando,"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows surprisex03
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "aunque no llevase ropa encima..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx01
                        show night03_bar_barra_n_mouth happy_Silentx01
                        with dissolve

                        p "..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_front

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth happy_Silentx02
                        with dissolve

                        p "No he dicho en ningún momento lo contrario."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx02
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "Pervertido..."

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx03
                        show night03_bar_barra_n_mouth sad_Silentx03
                        with dissolve

                        p "Pero si has sido tú..."

                        play sound "audio/characters/neus/gigglemalicious01.ogg"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows surprisex03
                        show night03_bar_barra_n_mouth happy_Silentx05
                        with dissolve

                        n "Una sonrisa pueblerina y maliciosa se dibuja en su rostro."

                        jump night05_Park_MinigameShooter_Finished_HerPresent

                    "Para darte un toque de color, ya tienes tus ojos de color esmeralda.":
                        call p_Help

                        $pl.ch_pts("np",2)

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        ne "..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_front

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex02
                        show night03_bar_barra_n_mouth sad_Silentx02
                        with dissolve

                        p "Sin mencionar cuando te brillan de color violáceo,"

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows suspiciousx02
                        show night03_bar_barra_n_mouth sad_Silentx02
                        with dissolve

                        p "tampoco son siempre de un verde puro."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows suspiciousx01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        p "Cuando estoy cerca y puedo apreciarlos mejor,"

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Silentx02
                        with dissolve

                        p "en ocasiones tienden a una tonalidad azulada,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth happy_Silentx03
                        with dissolve

                        p "y otras veces incluso amarillenta..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx03
                        show night03_bar_barra_n_mouth happy_Silentx04
                        with dissolve

                        ne "..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth happy_Talkingx01
                        with dissolve

                        ne "En realidad el misterio de los {a=https://commons.wikimedia.org/wiki/File:Greeneye2.jpg}ojos verdes{/a}"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left


                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "es que el color verde y azul no existen en el ojo humano..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth happy_Silent


                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx01
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "es más bien una reinterpretación que hacemos,"

                        show night03_bar_barra_n_eyes 03 
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows serious
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "según el color y la iluminación que nos rodea."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows normal
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "Es más,"

                        show night03_bar_barra_n_eyes 03 
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows serious
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "algunos {a=http://cogweb.ucla.edu/ep/Frost_06.html}genetistas{/a} afirman"

                        show night03_bar_barra_n_eyes 03 
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows normal
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "que la razón de porque los europeos desarrollaran este tipo de colores en los ojos"

                        show night03_bar_barra_n_eyes 01 
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth happy_Talkingx04
                        with dissolve

                        ne "fue para recurrir a una mejor estrategia para captar la atención de una posible pareja..."

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows serious
                        show night03_bar_barra_n_mouth happy_Silentx03
                        with dissolve

                        p "..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        ne "..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows suspiciousx01
                        show night03_bar_barra_n_mouth sad_Silentx02
                        with dissolve

                        pt "Yo aquí intentando ser cursi,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth sad_Silentx03
                        with dissolve

                        pt "y ella me salta con una clase de biología..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx03
                        show night03_bar_barra_n_mouth sad_Talkingx01
                        with dissolve

                        ne "Lo siento,"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx04
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "te he interrumpido..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_front
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        p "¿Qué más toque de color quieres,"

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Silentx02
                        with dissolve

                        p "que esos ojos tan hermosos,"

                        extend " expresivos,"

                        extend " y multicolor?"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx03
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "No me digas esas cosas [protname],"

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_left
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth happy_Talkingx03
                        with dissolve

                        ne "que me pones colorada,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx04
                        show night03_bar_barra_n_mouth happy_Talkingx02
                        with dissolve

                        ne "y luego me pongo a decir tonterías..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth happy_Talkingx02

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows surprisex01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        rat "Vaya moñería te acaba de soltar..."

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front
                        show night03_bar_barra_barman_mouth happy_Silent

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils right03
                        show night03_bar_barra_n_eyebrows suspiciousx03
                        show night03_bar_barra_n_mouth sad_Silentx04
                        with dissolve

                        ne "..."

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows angryx03
                        show night03_bar_barra_n_mouth sad_Talkingx03
                        with dissolve

                        ne "Como si tú no fueras diciendo este tipo de cursiladas a cada clienta que te encuentras..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils right03
                        show night03_bar_barra_n_eyebrows angryx03
                        show night03_bar_barra_n_mouth sad_Silentx03
                        with dissolve

                        rat "..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth happy_Silentx02
                        with dissolve

                        jump night05_Park_MinigameShooter_Finished_HerPresent

                    "No tiene nada de malo que no parezcas femenina.":
                        call p_Help

                        $pl.ch_pts("np",-1)

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx05
                        show night03_bar_barra_n_mouth sad_Talkingx03
                        with dissolve

                        ne "¿Insinúas que no tengo nada de femenina?"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx04
                        show night03_bar_barra_n_mouth sad_Silentx05
                        with dissolve

                        p "Lo decía como un cumplido..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx01
                        show night03_bar_barra_n_mouth sad_Talkingx01
                        with dissolve

                        ne "O sea,"

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx04
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "el hecho de que me parezca más a un tío que a una chica,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx06
                        show night03_bar_barra_n_mouth sad_Talkingx04
                        with dissolve

                        ne "¡¿te parece un cumplido?!"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx04
                        show night03_bar_barra_n_mouth sad_Silentx04
                        with dissolve

                        p "No he dicho que te parezcas a un tío..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx06
                        show night03_bar_barra_n_mouth sad_Talkingx04
                        with dissolve

                        ne "¡Entonces no me parezco a nada directamente!"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx05
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "Pues muchas gracias,"

                        extend " oye..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx03
                        show night03_bar_barra_n_mouth sad_Talkingx03
                        with dissolve

                        ne "Me siento,"

                        extend " uff..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx06
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "superelogiada,"

                        extend " vamos."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx04
                        show night03_bar_barra_n_mouth sad_Silentx02
                        with dissolve

                        p "No me has entendido..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx03
                        show night03_bar_barra_n_mouth sad_Talkingx04
                        with dissolve

                        ne "¡Claro que te he entendido!"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows angryx05
                        show night03_bar_barra_n_mouth sad_Silentx05
                        with dissolve

                        p "..."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows sadx03
                        show night03_bar_barra_n_mouth sad_Talkingx01
                        with dissolve

                        ne "Ya sé que solo mido metro cincuenta y dos,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx02
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "y no tengo un noventa-sesenta-noventa de cuerpo."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx04
                        show night03_bar_barra_n_mouth sad_Talkingx03
                        with dissolve

                        ne "Pero al menos esperaba que no te pareciera un {a=https://es.wikipedia.org/wiki/Marimacho}marimacho{/a},"

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows angryx03
                        show night03_bar_barra_n_mouth sad_Talkingx02
                        with dissolve

                        ne "en mi forma de vestir y actuar."

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils front01
                        show night03_bar_barra_n_eyebrows sadx01
                        show night03_bar_barra_n_mouth sad_Silentx01
                        with dissolve

                        p "La belleza de una mujer,"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows suspiciousx01
                        show night03_bar_barra_n_mouth sad_Silentx02
                        with dissolve

                        p "no radica necesariamente en su feminidad..."

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx04
                        show night03_bar_barra_n_mouth sad_Talkingx03
                        with dissolve

                        ne "¡¿Y qué tengo yo de hermosa entonces?!"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_front
                        show night03_bar_barra_barman_mouth happy_Talkingx02

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows surprisex02
                        show night03_bar_barra_n_mouth sad_Silentx04
                        with dissolve

                        rat "¡Estás hecho un Romeo, marinero!"

                        show night03_bar_barra_barman_eyes surprise
                        show night03_bar_barra_barman_pupils surprise_left
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 01
                        show night03_bar_barra_n_pupils right01
                        show night03_bar_barra_n_eyebrows angryx06
                        show night03_bar_barra_n_mouth sad_Talkingx04
                        with dissolve

                        ne "¡Tú cállate Rata!"

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils right03
                        show night03_bar_barra_n_eyebrows angryx05
                        show night03_bar_barra_n_mouth sad_Silentx06
                        with dissolve

                        rat "..."

                        show night03_bar_barra_barman_eyes angry
                        show night03_bar_barra_barman_pupils angry_front
                        show night03_bar_barra_barman_mouth sad_Silent

                        show night03_bar_barra_n_eyes 03
                        show night03_bar_barra_n_pupils front03
                        show night03_bar_barra_n_eyebrows sadx04
                        show night03_bar_barra_n_mouth sad_Silentx05
                        with dissolve

                        menu night05_Park_MinigameShooter_BraceletLooking_Femenine_Question:

                            "En tu bondad, tu sinceridad, tu empatía y tu forma de ver el mundo en general.":
                                call p_Help

                                $pl.ch_pts("np",-1)

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "¿En serio...?"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "¿Lo único que tengo hermoso,"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "es precisamente lo que no se ve?"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡Pues vaya forma más sutil de llamarme fea!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "Yo no he dicho que seas..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Así no me extraña que nunca me hayas dirigido la palabra..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "Neus..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡¿Qué?!"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Por muy simpática y amable que pueda ser,"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "si te parezco un adefesio;"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡¿qué sentido tiene todo esto?!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "Prefiero cien veces a chicas agradables,"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "que saben compartir una entrañable tarde entre risas y anécdotas,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "que a una modelo que no sabe ni sonreír."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Como si no hubiera modelos que son también maravillosas personas,"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "con un gran sentido del humor e inteligencia..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                pt "¿Tiene que encontrarle a todo una pega?"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Ahora también me vas a decir que me prefieres como amiga..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "Porque yo no veo que te vayas follando a chicas feas y gordas,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "simplemente porque te caigan bien;"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "como mucho las tendrás de amigas..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "pero nada más."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¿O me equivoco?"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx06
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "No eres fea ni gorda."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "No..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Soy peor."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "Bajita,"

                                extend  "plana,"

                                extend " y con cara de niña;"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                pt "¿Y eso es peor que ser fea y gorda?"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "que solo sirve para estar en la {a=https://es.wikipedia.org/wiki/Zona_de_amigos}{i}friendzone{/i}{/a}..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Talkingx02

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows angryx01
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                rat "Yo nunca te he puesto en la friend..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "¡Ahora no estoy de humor, Rata!"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                rat "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx01
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "Desde luego;"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "tú te lo guisas,"

                                extend " tú te lo comes..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Silentx06
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows serious
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "¿Por qué no puedes quererte un poco más por cómo eres?"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Porque no me lo pones fácil con lo que me dices..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                jump night05_Park_MinigameShooter_Finished_HerPresent

                            "En tus hermosos ojos, tu carita de niña buena y tu sonrisa angelical.":
                                call p_Help

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Vamos,"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "que lo único bueno que tengo,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "es mi cara de niña pequeña."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "Pues muchas gracias..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "¿No te lo puedes tomar como un cumplido?"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx02
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Depende..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_left
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡¿Te gusta acostarte con niñas?!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_left
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Pues eso."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Me gustaría que me tomaras como a una adulta,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "y no que solo te fijaras en mi cara..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡También tengo un cuerpo!"

                                extend " ¡¿sabes?!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx01
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "Lo sé."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows normal
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                p "Con este vestido no dejas demasiado a la imaginación..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows suspiciousx01
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "Ya sé que soy plana..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "¡Mujer!"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows suspiciousx01
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "¡No eres tan plana!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡Seguro que Dídac tiene mejor pecho que yo!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Pero te sorprendería saber de lo que soy capaz de hacer,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "a pesar de mi aspecto..."

                                if night04_pedrera_blowjob_DONE == True:

                                    show night03_bar_barra_barman_eyes surprise
                                    show night03_bar_barra_barman_pupils surprise_front
                                    show night03_bar_barra_barman_mouth sad_Silent

                                    show night03_bar_barra_n_eyes 03
                                    show night03_bar_barra_n_pupils front03
                                    show night03_bar_barra_n_eyebrows serious
                                    show night03_bar_barra_n_mouth sad_Silentx04
                                    with dissolve

                                    p "Desde luego,"

                                    show night03_bar_barra_n_eyes 01
                                    show night03_bar_barra_n_pupils front01
                                    show night03_bar_barra_n_eyebrows surprisex01
                                    show night03_bar_barra_n_mouth sad_Silentx01
                                    with dissolve

                                    p "lo de ayer fue bastante increíble..."

                                    show night03_bar_barra_n_eyes 03
                                    show night03_bar_barra_n_pupils front03
                                    show night03_bar_barra_n_eyebrows suspiciousx02
                                    show night03_bar_barra_n_mouth happy_Talkingx01
                                    with dissolve

                                    ne "Pues eso no es ni la punta del iceberg."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows normal
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "¿No puedes simplemente aceptar que me gustas tal y como eres?"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Yo..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows normal
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                p "Neus..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx01
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "Ya sé que eres una mujer con una inseguridad grande como un elefante,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "pero al menos,"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "trata de no preocuparte tanto por estas cosas conmigo."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "¿De acuerdo?"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "Al menos no me has dicho fea..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "¡Coño!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx01
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                p "¡Porque no eres fea!"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx01
                                show night03_bar_barra_n_mouth happy_Silentx02
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth happy_Talkingx02
                                with dissolve

                                ne "Gracias [protname]."

                                jump night05_Park_MinigameShooter_Finished_HerPresent

                            "Eres hermosa tal y como eres, sin necesidad de compararte con nadie más.":
                                call p_Help

                                $pl.ch_pts("np",-1)

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx02
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "La única persona con la que deberías compararte,"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "es con la persona que eras ayer."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows normal
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "Ámate,"

                                extend " respétate,"

                                extend " y perdónate."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx01
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Una mujer que confía en sí misma siempre se ve más bella."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡¿Es eso lo que me querías decir?!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "Neus..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_left
                                show night03_bar_barra_barman_mouth happy_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡¿Te crees que no me he leído ya toda esa basura de autoayuda barata?!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows suspiciousx03
                                show night03_bar_barra_n_mouth sad_Silentx06
                                with dissolve

                                p "Yo no opino que sea basura..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx03
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Pero sí crees que la necesito, por lo visto..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "Mujer,"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                p "debes admitir que tienes muy poca autoestima..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows sadx01
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "Diciéndome que soy poco femenina tampoco me ayudas mucho..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Talkingx02

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                rat "Eres un misera..."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows angryx01
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Rata."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx01
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "Por favor..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                rat "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                pt "Es como pelearse contra la pared..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "No importa..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Soy consciente de cómo soy."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Talkingx01
                                with dissolve

                                ne "Lamento darte la lata con mis problemas..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "Neus..."

                                jump night05_Park_MinigameShooter_Finished_HerPresent

                            "Tienes razón, he visto niñas de quince años con mejores atributos que tú.":
                                call p_Help

                                $pl.ch_pts("np",-3)

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                p "¿Qué?"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "¿No me has pedido sinceridad?"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                ne "..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Talkingx02

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                rat "¡¿Cómo te atreves a decirle eso a esta princesa?!"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Talkingx01

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows suspiciousx01
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                rat "¡Te voy a romper la cara!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex02
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "Si te la rompo yo,"

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx01
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "seguramente hasta te la arregle."

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "Dudo que pudiera llegar a estropearla aún más..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Talkingx02
                                with dissolve

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows angryx06
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡Basta!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Talkingx01

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                rat "¡¿Has oído lo que...?!"

                                show night03_bar_barra_barman_eyes surprise
                                show night03_bar_barra_barman_pupils surprise_left
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows angryx05
                                show night03_bar_barra_n_mouth sad_Talkingx04
                                with dissolve

                                ne "¡He dicho que basta!"

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows angryx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                rat "..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "[protname]..."

                                show night03_bar_barra_barman_eyes angry
                                show night03_bar_barra_barman_pupils angry_front
                                show night03_bar_barra_barman_mouth sad_Silent

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Tampoco hacía falta ser tan específico."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows surprisex01
                                show night03_bar_barra_n_mouth sad_Silentx01
                                with dissolve

                                p "Pues deja de auto-compadecerte de ti misma."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Silentx02
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                p "Ya te he dicho que me gustas tal y como eres."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "Así que si no me crees,"

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils front01
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve

                                p "es tu problema."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx04
                                with dissolve

                                p "No el mío."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils right03
                                show night03_bar_barra_n_eyebrows sadx03
                                show night03_bar_barra_n_mouth sad_Silentx03
                                with dissolve

                                ne "..."

                                show night03_bar_barra_n_eyes 01
                                show night03_bar_barra_n_pupils right01
                                show night03_bar_barra_n_eyebrows sadx02
                                show night03_bar_barra_n_mouth sad_Talkingx03
                                with dissolve

                                ne "Me ha quedado claro..."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Talkingx02
                                with dissolve

                                ne "Tranquilo."

                                show night03_bar_barra_n_eyes 03
                                show night03_bar_barra_n_pupils front03
                                show night03_bar_barra_n_eyebrows sadx04
                                show night03_bar_barra_n_mouth sad_Silentx05
                                with dissolve


                                jump night05_Park_MinigameShooter_Finished_HerPresent

                    "<No decir nada>":
                        call p_Help

                        jump night05_Park_MinigameShooter_Finished_HerPresent

    else:

        jump night05_Park_MinigameShooter_Finished_HerPresent

label night05_Park_MinigameShooter_Finished_HerPresent:

    $ MShooter_Present_Necklace_Ankh = True

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "Toma,"

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "tu regalo."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve


    show bg_dark_a
    show night05_tibidabo_bracelet_MCShow_necklace_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 15.0 zoom 0.375 xpos 0.5 ypos 0.5
    with fade

    p "¿Un collar de oro?"

    p "Tiene el mismo símbolo que tienes tatuado en el esternón."

    ne "Es una cruz ansada que se llama {a=https://es.wikipedia.org/wiki/Anj}Ankh{/a};"

    ne "y es un jeroglífico egipcio que significa \"vida\"."

    ne "Quizás no creas en el poder de los símbolos,"

    ne "pero te prometo que puede resultarte muy útil para protegerte de lo que aún desconoces."

    pt "Después de todo lo que he visto estos días,"

    pt "es mejor ir prevenido..."

    if MShooter_points == 25:

        pt "Pero si yo he ganado una pulsera dorada,"

        pt "y no un collar..."

        pt "Además,"

        pt "que esto de oro tiene más bien poco,"

        pt "parece más bien una pieza metálica,"

        pt "con una capa de color que intenta imitar el oro..."

        pt "sin embargo este collar,"

        pt "no parece una imitación..."

    hide bg_dark_a
    hide night05_tibidabo_bracelet_MCShow_necklace_comp

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth sad_Silentx01
    with fade

    p "¿Cuántos puntos has ganado?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "Unos cuantos."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Silentx02
    with dissolve

    pt "La verdad es que para ser una versión barata de los chinos tiene muy buena pinta."

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex03
    show night03_bar_barra_n_mouth sad_Silentx01
    with dissolve

    p "¿Estás segura que no te lo quieres quedar tú?"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows angryx02
    show night03_bar_barra_n_mouth sad_Talkingx02
    with dissolve

    ne "Habíamos quedado en que nos intercambiábamos los regalos."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth sad_Talkingx01
    with dissolve

    ne "Además,"

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve

    ne "yo ya lo llevo tatuado."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Talkingx01
    with dissolve

    ne "Quiero que te quedes este collar,"

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "para que nunca olvides el tiempo que hemos estado juntos."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    p "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx05
    with dissolve

    rat "Qué cursi eres cuando quieres..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth sad_Talkingx02
    with dissolve

    ne "Rata..."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows suspiciousx01
    show night03_bar_barra_n_mouth happy_Silentx02
    with dissolve

    rat "..."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "Espero que tu primo se recupere pronto y no te cargues demasiado trabajo."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth sad_Silentx02
    with dissolve

    rat "..."

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth happy_Silentx01
    with dissolve

    rat "No te preocupes cariño,"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_left
    show night03_bar_barra_barman_mouth happy_Talkingx02

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Silentx02
    with dissolve

    rat "soy un hombre de muchos recursos,"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows sadx01
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    rat "ya lo sabes."

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows angryx01
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "Me alegra oír eso."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows sadx02
    show night03_bar_barra_n_mouth happy_Silentx02
    with dissolve

    p "..."

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Talkingx03
    with dissolve

    ne "¿Nos vamos?"

    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils front03
    show night03_bar_barra_n_eyebrows surprisex01
    show night03_bar_barra_n_mouth happy_Silentx05
    with dissolve

    window hide dissolve
    pause

    ##
    ## 


    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################

    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################
    ##############################################################################


label night05_Park_MinigameShooter_After:

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    n "Sientes otra vez su cálida mano."

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx1')

    if night05_Park_MinigameShooter_Participate_RatAgainst_Cond == True:

        pt "A pesar de lo que le he dicho,"

        extend " sigue cogiéndome de la mano..."

    elif night05_Park_MinigameShooter_Played == False:

        pt "Aun así sigue cogiéndome de la mano..."

    ne "Vamos,"

    ne "aún hay tiempo para probar alguna atracción más."

    ## Pregunta

    menu night05_Park_MinigameShooter_After_RatLife_Question:

        "<Preguntarle por su extraña relación con Rata>":

            $pl.ch_pts("np",1)

            $ night05_Park_MinigameShooter_After_RatLife_Cond = True

            jump night05_Park_MinigameShooter_After_RatLife

        "<No decir nada>":

            jump night05_Park_Cups_Beginning

label night05_Park_MinigameShooter_After_RatLife:

    p "Una pregunta, Neus..."

    scene bg_dark_a
    show n_closefromup_body sd:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris front01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows surprisex01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears empty:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Talkingx01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:
        zoom 0.5 xalign 0.5 yalign 0.5
    with fade

    ne "¿Sí?"

    show n_closefromup_eyes 00
    show n_closefromup_iris front00
    show n_closefromup_eyebrows surprisex03
    show n_closefromup_mouth sad_Silentx01
    with dissolve

    p "¿Qué tipo de relación tienes con Rata?"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    pt "Me sigue pareciendo un nombre muy raro..."

    if music_play != "are_you_still_dreaming":
        play music "audio/music/alcaknight/are_you_still_dreaming.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "are_you_still_dreaming"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    ne "..."

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Talkingx02
    with dissolve

    ne "Soy una clienta habitual de su bar,"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sad_Talkingx03
    with dissolve

    ne "nos conocemos desde hace más de un año,"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth happy_Talkingx02
    with dissolve

    ne "por lo que ya hay cierta confianza."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows surprisex01
    show n_closefromup_mouth sadbiting_Silentx02
    with dissolve

    p "Eso me parece muy bien..."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    p "Pero me da la sensación de que él en ti"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happybiting_Silentx03
    with dissolve

    p "ve algo más que una simple clienta,"

    extend " o amiga."

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows suspiciousx03
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "¿Estás celoso...?"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth happy_Silentx02
    with dissolve

    p "Puedo ser curioso,"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth happy_Silentx01
    with dissolve

    p "¿no?"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "Ya..."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    p "Debes admitir que te trata de una forma que va más allá del apego amistoso..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "No seas exagerado."

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "En realidad llama cariño a casi todas las chicas que vienen a menudo en el bar y le parecen monas."

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth happy_Talkingx01
    with dissolve

    ne "No tengo nada de especial."

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    pt "Ya..."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "Simplemente le sigo el juego para poder verle sonreír,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "no lo hace con ninguna mala intención."

    ## If YOU PLAYED

    if night05_Park_MinigameShooter_Played == True:

        show n_closefromup_eyes 00
        show n_closefromup_iris front00
        show n_closefromup_eyebrows surprisex02
        show n_closefromup_mouth sadbiting_Silentx02
        with dissolve

        p "¿Y qué me dices del modo en que me ha estado atacando,"

        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows sadx01
        show n_closefromup_mouth sadbiting_Silentx03
        with dissolve

        p "faltando al respeto constantemente,"

        show n_closefromup_eyes 02
        show n_closefromup_iris right02
        show n_closefromup_eyebrows sadx03
        show n_closefromup_mouth sad_Silentx04
        with dissolve

        p "para hundirme y flirtear contigo?"

        show n_closefromup_eyes 04
        show n_closefromup_iris right04
        show n_closefromup_eyebrows sadx04
        show n_closefromup_mouth sadbiting_Silentx05
        with dissolve

        p "Eso no tiene nada de agradable y mucho menos de amistoso."

        show n_closefromup_eyes 02
        show n_closefromup_iris right02
        show n_closefromup_eyebrows suspiciousx03
        show n_closefromup_mouth sadbiting_Silentx09
        with dissolve

        p "Son claras evidencias de celosía enfermiza."

    else:

        show n_closefromup_eyes 01
        show n_closefromup_iris front01
        show n_closefromup_eyebrows surprisex01
        show n_closefromup_mouth sadbiting_Silentx02
        with dissolve

        p "¿Y qué me dices del modo en que me trata?"

        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows normal
        show n_closefromup_mouth sadbiting_Silentx03
        with dissolve

        p "No parece que sea demasiado amigable conmigo,"

        show n_closefromup_eyes 02
        show n_closefromup_iris right02
        show n_closefromup_eyebrows suspiciousx01
        show n_closefromup_mouth sadbiting_Silentx04
        with dissolve

        p "casi parece que se alegre cuando me distancio de ti,"

        show n_closefromup_eyes 01
        show n_closefromup_iris right01
        show n_closefromup_eyebrows normal
        show n_closefromup_mouth sadbiting_Silentx02
        with dissolve

        p "o te decepciono."

    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    ne "..."

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx003
    with dissolve

    ne "En realidad la vida no lo ha tratado demasiado bien."

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "Es un hombre que ha pasado por dos divorcios,"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx03
    with dissolve

    ne "y aún está pagando la manutención de sus tres hijos, que ama con locura,"

    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "a los cuales hace años que ni siquiera puede tocar debido a la distancia."

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    pt "Lo que me extraña es que alguien hubiera querido casarse con él..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "Eso le ha impedido poder invertir tiempo y dinero en su sueño de ser {a=https://es.wikipedia.org/wiki/Tatuaje}tatuador{/a},"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "y al final ha tenido que conformarse con ser barman."

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx004
    with dissolve

    ne "Lo cual le llevó a tener una profunda depresión,"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "que se trató con medicamentos y especialistas,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows suspiciousx03
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "en mi opinión de dudosa profesionalidad;"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "y para que sigue medicándose a día de hoy."

    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "Debido a esto,"

    extend " engordó casi sesenta kilos en menos de quince años,"

    show n_closefromup_eyes 05
    show n_closefromup_iris left05
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    pt "Coño..."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "perdió una melenaza que sería la envidia de cualquiera,"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "hasta tener tan poco pelo,"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx003
    with dissolve

    ne "aunque en mi opinión se vería más favorecido si se rapara del todo la cabeza."

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    pt "Eso no lo niego,"

    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    pt "bien sexy que estoy yo sin pelo..."

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx002
    with dissolve

    ne "Perdiendo así todo el encanto físico que tuvo en su día,"

    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "encontrándose inmerso en una espiral de fatiga,"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "obesidad,"

    extend " depresión,"

    extend " alcohol,"

    extend " y autocastigo,"

    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "de la que cada vez se va hundiendo más,"

    extend " y más,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "y de la cual se ve incapaz de salir."

    ##

    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    p "..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "En verdad es una bellísima persona que ama a sus hijos con locura,"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows angryx01
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "trabajador como el que más,"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows angryx02
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "fiel a su palabra,"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "que no duda un instante en sacrificarse cuando alguien le pide un favor;"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "pero atrapado en una rutina de la que él mismo se ha vuelto carcelero,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "por los errores que cometió de joven,"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx07
    with dissolve

    ne "y de los que ahora no puede escapar;"

    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "si quiere mantener la esperanza"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx004
    with dissolve

    ne "de volver abrazar algún día a sus hijos,"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx08
    with dissolve

    ne "que están al cuidado de sus dos ex-esposas,"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "las cuales viven en el extranjero,"

    show n_closefromup_eyes 05
    show n_closefromup_iris left05
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "y vuelven a estar casadas con hombres más apuestos,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx004
    with dissolve

    ne "y con mejor estabilidad económica."

    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx06
    show n_closefromup_mouth sad_Silentx06
    with dissolve

    p "..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx003
    with dissolve

    ne "Y aun así,"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth happy_Talkingx06
    with dissolve

    ne "nunca pierde la sonrisa para sus clientes."

    show n_closefromup_eyes 00
    show n_closefromup_iris front00
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sadbiting_Silentx03
    with dissolve

    p "¿En el extranjero?"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx01
    with dissolve

    ne "Sí..."

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx03
    with dissolve

    ne "una de ellas,"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "con la que tuvo sus dos niñitas,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "vive en Londres."

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "La otra,"

    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "con la que tuvo su primer varón,"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx03
    with dissolve

    ne "vive en Nueva York."

    show n_closefromup_eyes 05
    show n_closefromup_iris left05
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    p "..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    p "Sientes lástima por él."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sadbiting_Silentx04
    with dissolve

    p "¿No es así?"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx02
    with dissolve

    ne "Sé lo que es vivir sin esperanza."

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "Y por raro que parezca,"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Talkingx004
    with dissolve

    ne "te aseguro que no se lo deseo ni a mi padre..."

    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    p "..."

    window hide dissolve
    pause

    jump night05_Park_Cups_Beginning

    ###

label night05_Park_Cups_Beginning:

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.set_volume(1.0, delay=2.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene bg night05_bg_tibidabo_park_around01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 20.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "Volvéis a cruzar gran parte del parque hasta llegar a ese lugar tan repleto de gente."

    $ renpy.music.set_volume(0.1, delay=20.0, channel='sfx1')

    scene bg night05_bg_cups_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.15 ypos 0.25
        easein_quad 20.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    ne "¡Uooh!"

    if music_play != "fireflies_and_stardust":
        play music "audio/music/kevinmacleod/fireflies_and_stardust.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "fireflies_and_stardust"

    ne "¡Las tazas!"

    #########################################################
    
    if config.version < "00.11.08": # Shooting mini-game.
        
        call endupdatescript
    
    #######################################################

    p "Euh..."

    p "Esto parece más bien globos aerostáticos que vuelan y giran."

    
    scene night05_bg_cups_01:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth happy_Talkingx08:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris left01:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex02:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "¡Hace años que no me subo a una atracción así!"

    show neus_exp_blush 01
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "Neus..."

    #scene day05
    #with fade
    #call endillustrations # NOT FINISHED
    
    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    p "No sé si es buena idea..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "¿Qué problema tienes ahora?"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows suspiciousx02
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Es que me mareo con facilidad,"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows suspiciousx03
    with dissolve

    p "y esta atracción está pensada para crear vómitos en cadena..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Eres un exagerado..."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    ne "¿Cuántos años hace que no te subes algo así?"

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    p "Pues..."

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Ni te acuerdas,"

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows suspiciousx03
    with dissolve

    ne "¿verdad?"

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_eyebrows normal
    with dissolve

    p "Pero tengo un pésimo recuerdo de ello."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Venga..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Por favor..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx06
    with dissolve

    pt "Obligar,"

    pt "no obliga..."

    pt "pero lo que es insistir..."

    menu night05_Park_Cups_Go_Question:

        "De acuerdo...":
            call p_Help

            $pl.ch_pts("np",1)

            $ night05_Park_Cups_Go_Cond = True

            jump night05_Park_Cups_Go_Accept

        "Lo siento, pero me niego.":
            call p_Help

            $pl.ch_pts("np",-1)

            if music_play != "bittersweet":
                play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bittersweet"

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyes 02
            show neus_exp_iris front02
            show neus_exp_eyebrows angryx01
            with dissolve

            if ((night05_Park_RollerCoaster_Used == False) or 
                (night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False) or 
                (night05_Park_MinigameShooter_Played == False)):

                if night05_Plaza_NeusLooking_BadAnswer_Cond == True:

                    show neus_exp_mouth sad_Talkingx04
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "Me has dicho que me quitara el color de ojos que llevaba;"

                if night05_Park_RollerCoaster_Used == False:

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "No has querido subir a la montaña rusa;"

                elif night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False:

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Me has puesto morros mientras hacíamos la cola para subir a la montaña rusa;"

                if night05_Park_MinigameShooter_Played == False:

                    show neus_exp_mouth sad_Talkingx05
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx05
                    with dissolve

                    ne "No te ha dado la gana de probar suerte con la escopeta;"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "y ahora te niegas a subir a las tazas."

                show neus_exp_mouth sad_Talkingx08
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx05
                with dissolve

                ne "¡¿Para qué diablos has aceptado venir al parque,"

                show neus_exp_mouth sad_Talkingx07
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows angryx05
                with dissolve

                ne "si no quieres hacer nada conmigo?!"

                show neus_exp_mouth sad_Silentx07
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows angryx05
                with dissolve


            else:

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows serious
                with dissolve

                ne "Pero..."

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "¿Por qué?"

                show neus_exp_mouth sad_Silentx03
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows serious
                with dissolve

                p "Porque no me apetece marearme."

                show neus_exp_mouth sad_Talkingx004
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "¿Ni si te lo pido por favor,"

                extend " por favorcito?"

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyes 02
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx01
                with dissolve

                p "¡¿Pero no te das cuenta de que me voy a poner morado de tanto dar vueltas?!"

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Inténtalo por mí,"

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyes 03
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "por fi..."

                show neus_exp_mouth sad_Silentx05
                show neus_exp_eyes 01
                show neus_exp_iris front01
                show neus_exp_eyebrows sadx06
                with dissolve

                pt "Realmente parece que le haga mucha ilusión esto de las tazas..."

                show neus_exp_mouth sad_Silentx04
                show neus_exp_eyes 04
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx07
                with dissolve

            menu night05_Park_Cups_Go_02_Question:

                "<Recordarle que no tienes ninguna obligación>":
                    call p_Help
                    $pl.ch_pts("np",-5)

                    $ night05_Park_Cups_Used = False # Not necessary, but just to remember the Conditional.

                    show neus_exp_mouth sad_Silentx03
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows serious
                    with dissolve

                    p "Que yo sepa,"

                    if night05_Interrogation_DidacAgainBeingMan_Cond == True:

                        show neus_exp_mouth sad_Silentx02
                        show neus_exp_eyes 01
                        show neus_exp_iris front01
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        p "Dídac volverá a ser hombre tanto si me quedo como si me voy."

                        show neus_exp_mouth sad_Silentx04
                        show neus_exp_eyes 02
                        show neus_exp_iris right02
                        show neus_exp_eyebrows angryx01
                        with dissolve

                        p "Además;"

                    show neus_exp_mouth sad_Silentx05
                    show neus_exp_eyes 03
                    show neus_exp_iris right03
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    p "el trato era que acudiera a tus tres citas,"

                    show neus_exp_mouth sad_Silentx04
                    show neus_exp_eyes 02
                    show neus_exp_iris right02
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    p "sin ningún otro compromiso,"

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    p "a menos que yo quisiera."

                    show neus_exp_mouth sadbiting_Silentx05
                    show neus_exp_eyes 04
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    p "¿O has cambiado de opinión,"

                    show neus_exp_mouth sad_Silentx07
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    p "y ahora quieres obligarme?"

                    show neus_exp_mouth sad_Silentx08
                    show neus_exp_eyes 08
                    show neus_exp_iris front08
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx07
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx03
                    with dissolve

                    ne "Está bien."

                    show neus_exp_mouth sad_Talkingx06
                    show neus_exp_eyes 02
                    show neus_exp_iris front02
                    show neus_exp_eyebrows angryx04
                    with dissolve

                    ne "Tampoco hace falta ponerse así."

                    show neus_exp_mouth sad_Silentx06
                    show neus_exp_eyes 04
                    show neus_exp_iris right04
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "..."

                    jump night05_Park_Cups_After

                "De acuerdo...":
                    call p_Help

                    $pl.ch_pts("np",2)

                    show neus_exp_mouth sad_Talkingx002
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    ne "¡Vamos!"

                    show neus_exp_mouth sad_Talkingx03
                    show neus_exp_eyes 01
                    show neus_exp_iris front01
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "¡Tampoco lo digas con tanto ánimo!"

                    show neus_exp_mouth happy_Talkingx03
                    show neus_exp_eyes 03
                    show neus_exp_iris front03
                    show neus_exp_eyebrows sadx03
                    with dissolve

                    ne "Ya verás que te gustará."

                    show neus_exp_mouth happy_Silentx02
                    show neus_exp_eyes 04
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    pt "Desde luego,"

                    show neus_exp_mouth happy_Silentx03
                    show neus_exp_eyes 06
                    show neus_exp_iris front06
                    show neus_exp_eyebrows sadx02
                    with dissolve

                    pt "no hay manera de quitarle esa sonrisa de niña mimada..."

                    jump night05_Park_Cups_Go_Accept


label night05_Park_Cups_Go_Accept:

    $ night05_Park_Cups_Used = True

    play sound "audio/characters/neus/giggle04.ogg"

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "*risilla femenina*" # Feminine giggle *risilla femenina*

    show neus_exp_mouth happy_Silentx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    n "Afortunadamente,"

    scene black
    show bg night05_bg_cups_ridebg_comp_01:
        truecenter
        zoom 1.0 xpos 4.0 ypos 0.5 #Stop
        #zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
    show night05_bg_cups_rideseat shadow_no:
        truecenter
        zoom 0.5
    with fade

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "la cola para esta atracción es bastante menor que la anterior,"

    $ saturation_tint_level = "dark"

    n "y en menos de diez minutos ya podéis acceder a ella."

    show night05_bg_cups_rideseat shadow_yes
    # Neus sentada.

    #scene bg n_s_bg_sd_01:
        #truecenter
        #zoom 0.5

    show n_s_b_sd_hair_back:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_body:
        n_s_b_sd_cup_close_position
    show n_s_b_sd_face:
        n_s_b_sd_cup_close_position

    # Neus Expressions:

    show n_s_exp_blush 01:
        n_s_exp_sd_cup_close_position
    show n_s_exp_mouth happy_Silentx04:
        n_s_exp_sd_cup_close_position
    show n_s_exp_eyes 02:
        n_s_exp_sd_cup_close_position
    show n_s_exp_iris front02:
        n_s_exp_sd_cup_close_position
    show n_s_exp_tears empty:
        n_s_exp_sd_cup_close_position
    show n_s_exp_eyebrows surprisex02:
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
        n_s_b_sd_table_position
    show n_s_b_sd_arm_r empty:
        n_s_b_sd_table_position

    with dissolve

    $ renpy.music.set_volume(0.1, delay=20.0, channel='sfx1')

    n "Ambos os subís a una de las cabinas,"

    show n_s_exp_blush 02
    show n_s_exp_mouth happy_Silentx02
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    with dissolve

    n "agarrándote fuertemente a la barandilla deseando que no se mueva demasiado rápido,"

    show n_s_exp_blush 03
    show n_s_exp_mouth happy_Silentx08
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    n "mientras Neus te sonríe de oreja a oreja como una niña mimada."

    show bg night05_bg_cups_ridebg_comp_01:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 20.0 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_blush 02
    show n_s_exp_mouth happy_Silentx04
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris left01
    with Dissolve (1.0)

    n "Poco después empezáis a dar vueltas,"

    extend " vueltas,"

    extend " y más vueltas."

    show bg night05_bg_cups_ridebg_comp_01:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 10.0 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    n "A los pocos segundos sientes que la atracción se eleva y desciende,"

    show bg night05_bg_cups_ridebg_comp_02:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 4.0 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    n "con mayor celeridad a medida que pasa el tiempo."

    show n_s_exp_mouth happy_Silentx06
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    n "El bullicio de la gente,"

    show n_s_exp_mouth happy_Silentx07
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 07
    show n_s_exp_iris front07
    with dissolve

    n "las estelas de luz rodeando la oscuridad que te envuelve,"

    extend " la risa de Neus,"

    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    n "los chillidos de los críos,"

    extend " las explosiones de algunos fuegos pirotécnicos en el fondo."

    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    pt "Dios..."

    show n_s_exp_mouth happybiting_Silentx05
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 02
    show n_s_exp_iris left02
    with dissolve

    pt "Esto se mueve muy rápido..."

    show n_s_exp_mouth happy_Talkingx07
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "¿Qué tal si le damos un poco de vidilla a esto?"

    show n_s_exp_mouth happybiting_Silentx07
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 00
    show n_s_exp_iris down00
    with dissolve

    p "Neus..."

    show bg night05_bg_cups_ridebg_comp_03:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 1.5 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth happybiting_Silentx09
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 02
    show n_s_exp_iris down02
    with Dissolve (1.0)

    n "No solo la plataforma donde están todas las cabinas da vueltas,"

    show n_s_exp_mouth happybiting_Silentx08
    show n_s_exp_eyebrows surprisex03
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    with dissolve

    n "mientras un brazo mecánico las eleva y las hace descender de forma trepidante,"

    show n_s_exp_mouth happybiting_Silentx06
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    with dissolve

    n "sino que además, ella empieza a mover la barandilla,"

    show bg night05_bg_cups_ridebg_comp_04:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 0.5 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth happy_Talkingx08
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with Dissolve (1.0)

    n "para que el propio habitáculo, gire sobre sí mismo."

    show n_s_exp_mouth happy_Silentx07
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 07
    show n_s_exp_iris front07
    with dissolve

    p "Dios..."

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with dissolve

    ne "¿Euh?"

    show bg night05_bg_cups_ridebg_comp_03:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 1.5 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth sad_Silentx06
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    with Dissolve (0.5)

    n "Detiene en seco el movimiento que estaba llevando a cabo con la barandilla,"

    show bg night05_bg_cups_ridebg_comp_02:
        truecenter
        zoom 1.0 xpos 6.5 ypos 0.5 #Top Left
        linear 4.0 zoom 1.0 xpos -4.5 ypos 0.5 #Top Right
        repeat
    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with Dissolve (0.5)

    n "y la cabina cesa en su rotación paulatinamente."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Te encuentras bien?"

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    n "Sin embargo la atracción sigue dando vueltas de forma frenética."

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Yo..."

    show n_s_exp_mouth sad_Talkingx003
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    with dissolve

    ne "Lo siento..."

    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 01
    show n_s_exp_iris right01
    with dissolve

    ne "No pensé que te afectaría tan rápidamente."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows sadx07
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    n "Instintivamente te llevas una mano a la boca."

    show n_s_exp_mouth sadbiting_Silentx02
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    with vpunch

    p "Ughh..."

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Quieres que ordene detener la atracción?"

    show n_s_exp_mouth sadbiting_Silentx06
    show n_s_exp_eyebrows sadx06
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    menu night05_Park_Cups_StopRide_Question:

        pt "¡¿Ahora se preocupa?!"

        "¡¿Por qué coño te has puesto a girar esto si te he dicho que me mareaba?!":
            call p_Help

            $pl.ch_pts("np",-1)

            show n_s_exp_mouth sadbiting_Silentx08
            show n_s_exp_eyebrows sadx04
            show n_s_exp_eyes 01
            show n_s_exp_iris right01
            with dissolve

            ne "..."

            show n_s_exp_mouth sad_Talkingx003
            show n_s_exp_eyebrows sadx06
            show n_s_exp_eyes 02
            show n_s_exp_iris right02
            with dissolve

            ne "Lo siento..."

            show n_s_exp_mouth sad_Silentx07
            show n_s_exp_eyebrows sadx08
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

            p "Diciendo lo siento no vas a arreglar nada..."

            jump night05_Park_Cups_StopRide_Eyes

        "<Decirle que puedes aguantar>":
            call p_Help
            
            $pl.ch_pts("np",1)

            show n_s_exp_mouth sadbiting_Silentx04
            show n_s_exp_eyebrows sadx04
            show n_s_exp_eyes 02
            show n_s_exp_iris front02
            with dissolve

            p "No,"

            extend " no..."

            show n_s_exp_mouth sadbiting_Silentx05
            show n_s_exp_eyebrows sadx05
            show n_s_exp_eyes 04
            show n_s_exp_iris front04
            with dissolve

            p "Creo que puedo aguantar."

            show n_s_exp_mouth sad_Talkingx06
            show n_s_exp_eyebrows sadx04
            show n_s_exp_eyes 01
            show n_s_exp_iris front01
            with dissolve

            ne "Lo lamento mucho."

            show n_s_exp_mouth sad_Talkingx03
            show n_s_exp_eyebrows sadx05
            show n_s_exp_eyes 02
            show n_s_exp_iris right02
            with dissolve

            ne "Debería haberte hecho caso."

            show n_s_exp_mouth sadbiting_Silentx06
            show n_s_exp_eyebrows sadx07
            show n_s_exp_eyes 04
            show n_s_exp_iris right04
            with dissolve

            p "..."

            show n_s_exp_mouth sadbiting_Silentx07
            show n_s_exp_eyebrows sadx08
            show n_s_exp_eyes 05
            show n_s_exp_iris right05
            with dissolve

            pt "¡Pero es que encima se ha puesto a girar la cabina sin que le diera una respuesta!"

            jump night05_Park_Cups_StopRide_Eyes

        "<No decir nada>":
            call p_Help

            jump night05_Park_Cups_StopRide_Eyes

label night05_Park_Cups_StopRide_Eyes:

    show n_s_exp_mouth sad_Talkingx02
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    ne "[protname]."

    show n_s_exp_mouth sadbiting_Silentx05
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "¿Euh...?"

    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "Mírame a los ojos."

    show n_s_exp_mouth sadbiting_Silentx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    with dissolve

    p "..."

    show n_s_exp_mouth sad_Silentx05
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 00
    show n_s_exp_iris front00b_bright
    with dissolve

    pt "Otra vez ese brillo violáceo..."

    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 00
    show n_s_exp_iris front00_bright
    with dissolve

    show black02

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    with fade

    p "¿Uh?"

    show bg night05_bg_cups_ridebg_comp_01:
        truecenter
        zoom 1.0 xpos 4.0 ypos 0.5 #Stop

    show n_s_exp_mouth sad_Silentx03
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    with dissolve

    pt "Nos hemos parado."

    hide black02

    with fade

    pt "¿Tan rápido ha pasado el tiempo?"

    show n_s_exp_mouth happy_Silentx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    n "Su rostro es dulce y sonriente."

    show n_s_exp_mouth happy_Talkingx03
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    ne "¿Te encuentras bien?"

    show n_s_exp_mouth happy_Silentx04
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve

    p "Sí..."

    show n_s_exp_mouth happy_Silentx05
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    p "Aún un poco mareado..."

    scene black
    with fade

    n "Te dispones a salir del cubículo,"

    play sound "audio/sfx/fall01.ogg"

    scene black
    with hpunch

    n "cuando por poco caes al suelo por falta de equilibrio."

    ne "¡[protname]!"

    scene bg_dark_a
    show n_closefromup_body sd:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 02:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris front01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows sadx04:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears empty:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Talkingx02:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:
        zoom 0.5 xalign 0.5 yalign 0.5
    with fade

    ne "Cuidado..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "Cógete a mí."

    scene black
    with fade

    pt "Para lo pequeña que es,"

    pt "tiene bastante fuerza..."

    scene night05_bg_cups_01:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5

    with fade
    
    n "Ambos salís de la atracción,"

    n "atraídos por la mirada curiosa y aborrecida de la gente que hace fila para acceder a ella."

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
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris front04:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx03:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "¿Te encuentras mejor?"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with dissolve

    p "Sí..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with dissolve

    p "ya me estoy recuperando..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_eyebrows sadx04
    with dissolve

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "almost_new_kevin"

    ne "Por lo menos no te has caído al suelo como hice yo en nuestra primera cita."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    p "Me he mareado,"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    p "no voy bebido."

    show neus_exp_mouth sad_Talkingx001
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Jo..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "Lo dices como si yo fuera una borracha."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows serious
    with dissolve

    p "Hombre,"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "creo que le dejaste sin existencias de licor de café al pobre barman..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 00
    show neus_exp_iris right00
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "En realidad la primera vez que fui pasó algo parecido,"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_eyebrows normal
    with dissolve

    ne "pero con el tiempo,"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "al ser una clienta habitual,"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "supo cuanto me gusta el {a=https://es.wikipedia.org/wiki/Black_Russian}ruso negro{/a}."

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "Eso no ayuda a quitarme esa imagen de borrachina..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows serious
    with dissolve

    ne "Tampoco voy todos los días..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "Pero de tanto en cuanto,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "me apetece ahogar mis recuerdos en licor."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_eyebrows serious
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Conmigo también querías ahogar mi recuerdo?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "Contigo estaba más nerviosa que {a=https://es.wikipedia.org/wiki/Pinocho}Pinocho{/a} atrapado en un incendio..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Así que no pude contenerme,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows serious
    with dissolve

    ne "y pedí una bebida tras otra..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Pensé que si estaba desinhibida podría ser más valiente,"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "pero terminé haciendo el ridículo..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with dissolve

    if night04_pedrera_blowjob_DONE == True:

        p "Creo que ayer demostraste lo atrevida y juguetona que puedes llegar a ser."

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_eyebrows sadx01
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyes 02
        show neus_exp_iris right02
        show neus_exp_eyebrows suspiciousx01
        with dissolve

        pt "Aunque en la parte final con esa lengua,"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_eyebrows suspiciousx02
        with dissolve

        pt "esos ojos detrás y la cara que ponía..."

        show neus_exp_mouth happybiting_Silentx03
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_eyebrows suspiciousx03
        with dissolve

        pt "excitación no sería la palabra adecuada..."

        show neus_exp_mouth happy_Talkingx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows angryx01
        with dissolve

        ne "No quieras saber lo que soy capaz de hacer..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex01
    with vpunch

    p "Uff..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "¿Qué te pasa?"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with dissolve

    p "Creo que debería ir al baño."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "¿Sigues mareado?"

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with dissolve

    p "Un poco,"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx05
    with dissolve

    p "pero tranquila,"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx06
    with dissolve

    p "ya se me va pasando."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Por suerte hay uno aquí cerca,"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "te acompaño."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿Hasta dentro del lavabo?"

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    ne "Si es lo que quieres..."

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows serious
    with dissolve

    p "Lo decía en broma, mujer."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Yo no..."

    show neus_exp_mouth happybiting_Silentx06
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows normal
    with dissolve

    p "Eres una chica muy mala."

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Lo sé."

    play sound "audio/characters/neus/giggle03.ogg"

    show neus_exp_mouth happy_Silentx08
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows surprisex01
    with dissolve

    n "Una sonrisa pícara -y discutiblemente inocente- emerge de sus labios,"

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with dissolve

    n "mientras te despides de ella a la puerta del baño."

label night05_Park_WC:

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.set_volume(0.5, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_hospital.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene bg night05_bg_tibidabo_bathroom_comp_01:
        truecenter
        zoom 0.5
    with fade

    $ saturation_tint_level = "default"

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx1')

    n "Tan solo encuentras un hombre lavándose las manos a punto de irse."

    #scene day05
    #with fade
    #call endillustrations

    # Escene Baño

    play sound "audio/sfx/toilet_flush01.ogg"

    scene bg night05_bg_tibidabo_bathroom_toilet:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos -0.25
        ease_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "Aprovechas para relajar tu vejiga en uno de los retretes,"

    scene bg night05_bg_tibidabo_bathroom_sink:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 1.0
        easein_quad 5.0 zoom 0.75 xpos 0.5 ypos 0.35
        ease_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    # Pica

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/water_tap01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)


    n "para luego regresar a la pica donde te lavas las manos, al mismo tiempo que el rostro,"

    # MC Face (grab hands)

    scene night05_park_Ngrabbingshirt_scene 01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 12.0 zoom 1.0 xpos 0.5 ypos 1.25 # Batman Mouth
        #zoom 0.35 xpos 0.5 ypos 0.0 # General

    $ renpy.music.set_volume(0.1, delay=10.0, channel='sfx2')

    n "mientras te miras al espejo."

    pt "Dios..."

    pt "qué mareo he cogido con la maldita atracción."

    pt "Otra vez sus ojos..."

    pt "Es como si hubiera avanzado el tiempo,"

    $ renpy.music.stop(channel='sfx2', fadeout=3.0)

    pt "o hubiera hecho que olvidara el lapso transcurrido hasta detenerse la máquina..."

    window hide dissolve
    pause

    play sound "audio/sfx/fall06.ogg"

    show night05_park_Ngrabbingshirt_scene 02:
        subpixel True
        zoom 1.0 xpos 0.5 ypos 1.25
        easein_elastic 1.0 zoom 1.0 xpos 0.5 ypos 0.5
    with hpunch

    p "¿Euh?"

    p "¡¿Neus?!"

    show night05_park_Ngrabbingshirt_scene 02:
        subpixel True
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "loopster"

    n "Sientes su cuerpo en tu espalda mientras desliza sus manos por tu parte abdominal,"

    if afternight04_DidacisNOTatHome == False:

        n "del mismo modo que ayer con Dídac,"

        n "pero esta vez siendo ella,"

        n "y en un baño público."

    p "Neus..."

    p "Este es el servicio de hombres."

    show night05_park_Ngrabbingshirt_scene 02:
        subpixel True
        zoom 1.5 xpos 0.5 ypos -0.2
        easein_quad 20.0 ypos 0.6
    with dissolve

    ne "Si es eso lo que te preocupa,"

    ne "podría hacerme crecer un enorme rabo como el tuyo,"

    ne "y entonces nadie podría decirme nada..."

    p "..."

    show night05_park_Ngrabbingshirt_scene 02:
        easein_quad 10.0 ypos 0.4

    ne "Estoy de broma, hombre."

    if night04_pedrera_blowjob_DONE == True:

        ne "A estas alturas necesitaría que me volvieras a dar de comer..."

        p "¿Cómo?"

    else:

        p "..."

    play sound "audio/sfx/fall02.ogg"

    show night05_park_Ngrabbingshirt_scene 03:
        subpixel True
        easein_quad 1.0 zoom 1.5 xpos 0.5 ypos -1.2

    n "Sientes su mano acercándose a tu entrepierna y agarrándotela con fuerza."

    show night05_park_Ngrabbingshirt_scene 04:
        subpixel True
        ease_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.25

    ne "Me alegra ver que el mareo no ha desanimado demasiado a tu amiguito..."

    pt "Desde luego,"

    pt "cuando se pone en modo cachonda,"

    pt "su personalidad cambia radicalmente."

    play sound "audio/sfx/door_open01.ogg"

    ono "Clock"

    scene black
    with hpunch

    stop music fadeout 3.0
    $ music_play = ""

    play sound "audio/sfx/fall09.ogg"

    $ renpy.music.set_volume(1.0, delay=5.0, channel='sfx1')

    ne "¡Ey!"

    scene bg night05_bg_tibidabo_bathroom_wall_door
    show n_closefromup_body sd:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris front01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows surprisex02:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears empty:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Silentx01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:
        zoom 0.5 xalign 0.5 yalign 0.5
    with fade

    n "El ruido de la puerta del baño abriéndose"

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx1')

    show n_closefromup_blush 02
    show n_closefromup_eyes 00
    show n_closefromup_iris left00
    show n_closefromup_eyebrows surprisex03
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    n "hace que instintivamente la empujes hasta uno de los reducidos habitáculos del baño,"

    show n_closefromup_blush 03
    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    n "y cierres la puerta para evitar que alguien os vea."

    show n_closefromup_blush 03
    show n_closefromup_eyes 01
    show n_closefromup_iris down01
    show n_closefromup_eyebrows surprisex03
    show n_closefromup_mouth sadbiting_Silentx01
    with dissolve

    p "..."

    show n_closefromup_blush 04
    show n_closefromup_eyes 04
    show n_closefromup_iris down04
    show n_closefromup_eyebrows angryx01
    show n_closefromup_mouth happybiting_Silentx08
    with dissolve

    n "No puedes evitar sentir las palpitaciones de tu miembro viril,"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows surprisex01
    show n_closefromup_mouth happybiting_Silentx10
    with dissolve

    n "encima de su cálida barriga al descubierto."

    show n_closefromup_blush 04
    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows angryx02
    show n_closefromup_mouth happy_Talkingx05
    with dissolve

    if music_play != "bummin-on-tremelo":
        play music "audio/music/kevinmacleod/bummin_on_tremelo.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bummin-on-tremelo"

    ne "Pillín..."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows surprisex01
    show n_closefromup_mouth sadbiting_Silentx09
    with dissolve

    p "{size=20}<Habla más bajo,>{/size}"

    show n_closefromup_eyes 02
    show n_closefromup_iris left02
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Silentx05
    with dissolve

    p "{size=20}<o nos oirá...>{/size}"

    show n_closefromup_eyes 04
    show n_closefromup_iris left04
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth sadbiting_Silentx05
    with dissolve

    ne "..."

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows angryx02
    show n_closefromup_mouth happybiting_Silentx10
    with dissolve

    p "..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "{size=20}<Por muchas ganas que tenga,>{/size}"

    show n_closefromup_eyes 01
    show n_closefromup_iris right01
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "{size=20}<no es buena idea hacerlo en un lugar así...>{/size}"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sadbiting_Silentx02
    with dissolve

    p "{size=20}<Eres tú quien me ha estado toqueteando en el baño de caballeros.>{/size}"

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows suspiciousx03
    show n_closefromup_mouth happybiting_Silentx08
    with dissolve

    ne "..."

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows angryx01
    show n_closefromup_mouth happy_Talkingx06
    with dissolve

    ne "{size=20}<Ya lo sé...>{/size}"

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    show n_closefromup_blush 02
    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "{size=20}<Quería pedirte disculpas por haberte forzado a subir a esa atracción,>{/size}"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth sad_Talkingx07
    with dissolve

    ne "{size=20}<a pesar de tus advertencias.>{/size}"

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    p "{size=20}<Tampoco me has puesto una pistola en la sien;>{/size}"

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sad_Silentx06
    with dissolve

    p "{size=20}<podía haber dicho que no.>{/size}"

    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "{size=20}<Pero a veces soy demasiado insistente...>{/size}"

    show n_closefromup_tears 05_01
    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx06
    show n_closefromup_mouth sadbiting_Silentx09
    with dissolve

    p "{size=20}<No te diré que no.>{/size}"

    show n_closefromup_tears 04_01
    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "{size=20}<En el fondo me parezco más a mi padre,>{/size}"

    show n_closefromup_tears 05_01
    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx06
    show n_closefromup_mouth sad_Talkingx003
    with dissolve

    ne "{size=20}<de lo que soy capaz de admitir...>{/size}"

    show n_closefromup_tears 02_03
    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sadbiting_Silentx03
    with dissolve

    n "Una lágrima empieza a derramarse por su mejilla."

    show n_closefromup_tears 05_03
    show n_closefromup_eyes 05
    show n_closefromup_iris right05
    show n_closefromup_eyebrows sadx07
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    menu night05_Park_WC_NeusCry:

        pt "Quizás debería decirle algo..."

        "<Darle la razón en que actúa de forma demasiado egoísta>":

            call p_Help
            
            $pl.ch_pts("np",-1)

            $ night05_Park_WC_NeusCry_BeingRude_Cond = True

            show n_closefromup_tears 02_03
            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth sad_Silentx04
            with dissolve

            p "{size=20}<No conozco a tu padre,>{/size}"

            show n_closefromup_tears 04_03
            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sad_Silentx03
            with dissolve

            p "{size=20}<pero a ti ya te conozco un poco.>{/size}"

            show n_closefromup_tears 05_03
            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            ne "..."

            show n_closefromup_tears 02_03
            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows suspiciousx01
            show n_closefromup_mouth sad_Silentx04
            with dissolve

            p "{size=20}<Y sinceramente,>{/size}"

            show n_closefromup_tears 00_03
            show n_closefromup_eyes 00
            show n_closefromup_iris front00
            show n_closefromup_eyebrows surprisex03
            show n_closefromup_mouth sad_Silentx03
            with dissolve

            p "{size=20}<eres como una niña mimada.>{/size}"

            if music_play != "colorless_aura":
                play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "colorless_aura"

            show n_closefromup_tears 02_03
            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows serious
            show n_closefromup_mouth sad_Silentx04
            with dissolve

            p "{size=20}<Debes aprender a aceptarlo,>{/size}"

            show n_closefromup_tears 04_03
            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx03
            show n_closefromup_mouth sad_Silentx06
            with dissolve

            p "{size=20}<cuando alguien te dice que no le gusta algo.>{/size}"

            show n_closefromup_tears 05_03
            show n_closefromup_eyes 05
            show n_closefromup_iris right05
            show n_closefromup_eyebrows angryx04
            show n_closefromup_mouth sad_Silentx09
            with dissolve

        "<Decirle algo positivo>":

            call p_Help
            
            $pl.ch_pts("np",2)

            $ night05_Park_WC_NeusCry_BeingNice_Cond = True

            show n_closefromup_tears 01_03
            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows normal
            show n_closefromup_mouth sad_Silentx03
            with dissolve

            p "{size=20}<Dios, Neus...>{/size}"

            show n_closefromup_tears 00_03
            show n_closefromup_eyes 00
            show n_closefromup_iris front00
            show n_closefromup_eyebrows surprisex01
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            p "{size=20}<Eso no es verdad.>{/size}"

            show n_closefromup_tears 04_03
            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows sadx01
            show n_closefromup_mouth sadbiting_Silentx05
            with dissolve

            p "{size=20}<Eres una chica maravillosa,>{/size}"

            show n_closefromup_tears 01_03
            show n_closefromup_eyes 01
            show n_closefromup_iris right01
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sadbiting_Silentx09
            with dissolve

            p "{size=20}<con un corazón que no te cabe en el pecho.>{/size}"

            show n_closefromup_tears 05_03
            show n_closefromup_eyes 05
            show n_closefromup_iris right05
            show n_closefromup_eyebrows sadx04
            show n_closefromup_mouth sadbiting_Silentx05
            with dissolve

            p "{size=20}<Simplemente te cuesta aceptar un no por respuesta.>{/size}"

        "<No decir nada>":

            call p_Help

    ne "..."

    $ renpy.music.set_volume(1.0, delay=0.2, channel='sfx2')
    $ renpy.music.play("audio/sfx/hand_dryer01.ogg", channel="sfx2",loop=False, fadeout=1.0, synchro_start=True, fadein=1.0)
    $ renpy.music.set_volume(0.5, delay=10.0, channel='sfx2')

    show n_closefromup_tears 01_03
    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    n "Escucháis el ruido del secador de manos."

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)

    if night05_Park_WC_NeusCry_BeingNice_Cond == True:

        show n_closefromup_tears 01_03
        show n_closefromup_eyes 01
        show n_closefromup_iris front01
        show n_closefromup_eyebrows surprisex01
        show n_closefromup_mouth sad_Silentx04
        with dissolve

        p "{size=20}<Pero eso no es necesariamente algo malo,>{/size}"

        show n_closefromup_tears 02_03
        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows serious
        show n_closefromup_mouth sad_Silentx03
        with dissolve

        p "{size=20}<siempre y cuando termines resignándote,>{/size}"

        show n_closefromup_tears 04_03
        show n_closefromup_eyes 04
        show n_closefromup_iris front04
        show n_closefromup_eyebrows sadx02
        show n_closefromup_mouth sad_Silentx02
        with dissolve

        p "{size=20}<cuando recibas una respuesta clara y rotunda.>{/size}"

    if night05_Park_WC_NeusCry_BeingRude_Cond == True:
        show n_closefromup_tears 04_05
        show n_closefromup_eyes 04
        show n_closefromup_iris left04
        show n_closefromup_eyebrows angryx03
        show n_closefromup_mouth sad_Silentx05
        with dissolve

    else:

        show n_closefromup_tears 01_03
        show n_closefromup_eyes 01
        show n_closefromup_iris left01
        show n_closefromup_eyebrows serious
        show n_closefromup_mouth sad_Silentx03
        with dissolve

    play sound "audio/sfx/door_close01.ogg"

    n "Para luego oír cómo ese desconocido camina hasta la salida."

    if night05_Park_WC_NeusCry_BeingRude_Cond == True:
        show n_closefromup_tears 05_05
        show n_closefromup_eyes 05
        show n_closefromup_iris left05
        show n_closefromup_eyebrows angryx03
        show n_closefromup_mouth sad_Silentx06
        with dissolve

    else:

        show n_closefromup_tears 02_03
        show n_closefromup_eyes 02
        show n_closefromup_iris left02
        show n_closefromup_eyebrows sadx01
        show n_closefromup_mouth sadbiting_Silentx03
        with dissolve

    ne "..."

    if night05_Park_WC_NeusCry_BeingRude_Cond == True:
        show n_closefromup_tears 05_05
        show n_closefromup_eyes 05
        show n_closefromup_iris right05
        show n_closefromup_eyebrows angryx03
        show n_closefromup_mouth sad_Silentx06
        with dissolve

    else:

        show n_closefromup_tears 04_03
        show n_closefromup_eyes 04
        show n_closefromup_iris left04
        show n_closefromup_eyebrows sadx02
        show n_closefromup_mouth sadbiting_Silentx04
        with dissolve

    p "Bien,"

    p "parece que ya estamos solos."

    p "Deberíamos aprovecharlo para salir..."

    if (night05_Park_RollerCoaster_Used == True and 
        night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == True and 
        night05_Park_MinigameShooter_Played == True and
        night05_Park_WC_NeusCry_BeingNice_Cond == True):

        if pl.np >= 100:
            call p_Help
            if PlatinumHelp:
                $ renpy.notify("[p_pos] 100[hn]") # NOT FINISHED not sure how many points should be here.
            jump night05_Park_Bathroom_Sweet

        else:
            call p_Help
            if PlatinumHelp:
                $ renpy.notify("[p_neg] 100[hn]")

            jump night05_Park_Bathroom_Bad
    else:

        jump night05_Park_Bathroom_Bad

label night05_Park_Bathroom_Bad:

    $ night05_Park_Bathroom_Bad_Cond = True

    ne "..."

    p "¿Qué ocurre?"

    show n_closefromup_tears 02_03
    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows angryx05
    show n_closefromup_mouth sad_Talkingx11
    with dissolve

    ne "Nada,"

    extend " no importa,"

    show n_closefromup_tears 01_03
    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows angryx05
    show n_closefromup_mouth sad_Talkingx08
    with dissolve

    ne "tienes razón."

    scene bg an04_Dgrabbingshirt_bg_bathroom:
        truecenter
        zoom 0.5
    with dissolve

    n "Observas a Neus saliendo del pequeño habitáculo en el que os encontrabais."

    play sound "audio/sfx/door_slam01.ogg"

    scene bg night05_bg_tibidabo_bathroom_wall_door:
        truecenter
        zoom 0.5
    with hpunch

    ne "Te espero fuera."

    n "Para luego desaparecer de tu vista dirigiéndose a la salida."

    p "..."

    if night05_Park_RollerCoaster_Used == False:

        pt "Quizás debería haber subido a la montaña rusa con ella;"

    if night05_Park_MinigameShooter_Played == False:

        pt "Quizás debería haber aceptado probar suerte con la escopeta;"

    if night05_Park_WC_NeusCry_BeingRude_Cond == True:

        pt "Quizás no debería haberle dicho que es una niña mimada;"

    if night05_Park_RollerCoaster_Queuing_Enjoyed_Cond == False:

        pt "Quizás no debería haberle reprochado que me obligara a comer esos platos veganos de ayer."

        pt "Es insistente,"

        pt "pero realmente no me ha obligado a nada realmente por ahora..."

    else:

        pt "Quizás debería haber intentado ser más amable con ella durante la cita..."

    pt "¿De qué sirve lamentarse ahora?"

    pt "Lo hecho,"

    extend " hecho está."

    pt "Queda apenas una hora y algo para el cierre del parque,"

    pt "y para el final de esta cita."

    jump night05_Park_Cups_After

            #ne "Sigamos."

            #p "¿Qué hora es?"

label night05_Park_Bathroom_Sweet:

    $ night05_Park_Bathroom_Sweet_Cond = True

    show n_closefromup_tears 01_03
    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "¿Por qué eres tan dulce conmigo?"

    show n_closefromup_tears 02_03
    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth sadbiting_Silentx09
    with dissolve
    
    p "..."

    show n_closefromup_tears 04_03
    show n_closefromup_eyes 04
    show n_closefromup_iris right04
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Talkingx06
    with dissolve

    ne "Harás que me enamore de ti más de lo que soy capaz de soportar..."

    show n_closefromup_tears 02_03
    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx05
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    p "Neus..."

    show n_closefromup_tears 00_01
    show n_closefromup_eyes 00
    show n_closefromup_iris left00
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth sadbiting_Silentx02
    with dissolve

    play sound "audio/sfx/door_open02.ogg"

    stop music fadeout 3.0
    $ music_play = ""

    b01 "Oye..."

    show n_closefromup_tears 01_01
    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Silentx04
    with dissolve

    b01 "¿Has oído eso?"

    show n_closefromup_tears 01_01
    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Silentx03
    with dissolve

    p "{size=20}<¡Mierda!>{/size}"

    show n_closefromup_tears 01_01
    show n_closefromup_eyes 01
    show n_closefromup_iris left01
    show n_closefromup_eyebrows suspiciousx02
    show n_closefromup_mouth sad_Silentx02
    with dissolve

    p "{size=20}<Ha entrado alguien nuevo...>{/size}"

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "loopster"

    show n_closefromup_tears 05_01
    show n_closefromup_eyes 05
    show n_closefromup_iris left05
    show n_closefromup_eyebrows suspiciousx03
    show n_closefromup_mouth happybiting_Silentx06
    with dissolve

    ne "..."

    scene night05_tibidabo_bathroom_n_comp 01:
        subpixel True
        truecenter
        zoom 0.75 xpos -0.5 ypos 2.0 # Top a bit on the right.
        #ease 15.0 zoom 0.5 xpos 0.5 ypos 0.2 # Ass
        easein_quad 25.0 zoom 0.3 xpos 0.5 ypos 0.5 # General
    with fade
        
    n "Neus te da la espalda posando su oreja en la puerta para escuchar mejor lo que ocurre ahí fuera."

    n "En esa posición, y a falta de espacio en ese lugar tan reducido,"

    n "sientes las palpitaciones de tu entrepierna en erección,"

    n "en claro contacto con sus nalgas cubiertas por la delgada tela de su corta falda."

    window hide dissolve
    pause

    #########################################################
    
    if config.version < "00.11.09": # Fairground Cups and beginning of WC.
        
        call endupdatescript
    
    #######################################################

    scene night05_tibidabo_bathroom_n_comp_00a:
        truecenter
        zoom 0.75 xpos 0.0 ypos 1.0

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_blush 02:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_eyes 02:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_pupils cameradown02:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_glasses:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_hair_front:
        truecenter
        zoom 0.75  xpos 0.0 ypos 1.0

    show night05_tibidabo_bathroom_n_arm_r up:
        truecenter
        zoom 0.75  xpos 0.0 ypos 1.0
    with fade


    ne "{size=20}<[protname]...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_blush 03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils cameradown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    ne "..."

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_blush 03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    ne "{size=20}<Pillín...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils cameradown04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx02
    with dissolve

    ne "{size=20}<¿Qué quieres hacer conmigo en un lugar tan estrecho?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    ne "{size=20}<Ya te he dicho que el plato principal,>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    ne "{size=20}<no te lo puedo dar hasta que volvamos...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    b01 "No estamos solos..."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b02 "Cállate idiota."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    p "{size=20}<Nos están oyendo...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils cameradown02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    ne "{size=20}<Y tú te estás poniendo más caliente por momentos...>{/size}"

    show night05_tibidabo_bathroom_n_comp 01:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.25 ypos 0.5 # Don´t know
        ease 3.0 zoom 0.5 xpos 0.5 ypos 0.2 # Ass
    with fade

    p "..."

    window hide dissolve
    pause

    hide night05_tibidabo_bathroom_n_comp

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b01 "{size=20}<¡Sabes que en lugares públicos no me gusta!>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows serious
    with dissolve

    pt "¿Qué diablos están haciendo?"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    b02 "No seas tan nenaza."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 05
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b01 "{size=20}<Te he dicho miles de veces que no me llames así.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    b02 "Ven,"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b02 "entremos en este retrete,"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b02 "así seguro que no nos verá nadie."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doordown02
    show night05_tibidabo_bathroom_n_exp_eyebrows serious
    with dissolve

    pt "¿Se están drogando?"

    play sound "audio/sfx/door_open01.ogg"

    scene bg night05_bg_tibidabo_bathroom_wc_wall:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.5 ypos 0.5
        easein_quad 25.0 zoom 0.3 xpos 0.5 ypos 0.5
    with fade

    n "Escucháis la puerta del habitáculo de vuestra izquierda abriéndose,"

    play sound "audio/sfx/door_close01.ogg"
    pause 0.2
    play sound "audio/sfx/door_close_key01.ogg"

    n "para luego cerrarse con pestillo."

    pt "Se han puesto justo a nuestro lado."

    scene night05_tibidabo_bathroom_n_comp 02:
        subpixel True
        truecenter
        zoom 0.75 xpos -0.5 ypos 2.0 # Top a bit on the right.
        easein_quad 25.0 zoom 0.3 xpos 0.5 ypos 0.5 # General
    with fade

    n "Neus saca la oreja de la puerta para ponerla a la pared que os conecta con esos dos individuos desconocidos."

    p "{size=20}<Neus...>{/size}"

    p "{size=20}<deberíamos aprovechar el momento para salir.>{/size}"

    window hide dissolve
    pause

    scene night05_tibidabo_bathroom_n_comp_00a:
        truecenter
        zoom 0.75 xpos 0.0 ypos 1.0 # Speak

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_blush 04:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_eyes 00:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_pupils camerafront00:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_eyebrows angryx03:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_exp_glasses:
        night05_tibidabo_bathroom_n_exp_position_00a

    show night05_tibidabo_bathroom_n_hair_front:
        truecenter
        zoom 0.75  xpos 0.0 ypos 1.0

    show night05_tibidabo_bathroom_n_arm_r up:
        truecenter
        zoom 0.75  xpos 0.0 ypos 1.0
    with fade

    play sound "audio/characters/neus/shh01.ogg"

    ne "{size=20}<Shhh...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    ne "{size=20}<Se está poniendo interesante.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<¿Que dos tíos se estén drogando te parece interesante?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    ne "{size=20}<¿Drogándose?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    ne "{size=20}<Si consideras el amor una droga...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    p "..."

    show night05_tibidabo_bathroom_n_comp 02:
        subpixel True
        truecenter
        zoom 0.75 xpos 1.0 ypos 2.0 # Top a bit on the left.
        easein_quad 25.0 zoom 0.4 xpos 0.7 ypos 0.75 # Top a bit on the left a bit far.
        #easein_quad 25.0 zoom 0.3 xpos 0.5 ypos 0.5 # General
    with fade

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/clothes01.ogg", channel="sfx2",loop=False, fadeout=0.1, synchro_start=True, fadein=0.1)
    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx3')
    $ renpy.music.play("audio/sfx/clothes02.ogg", channel="sfx3",loop=False, fadeout=0.1, synchro_start=True, fadein=0.1)

    n "Oyes repentinamente el forcejeo de dos personas quitándose la ropa salvajemente,"

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx4')
    $ renpy.music.play("audio/sfx/kiss_french03.ogg", channel="sfx4",loop=True, fadeout=0.1, synchro_start=True, fadein=0.1)

    n "mientras se escucha el sonido particular de dos bocas entrelazándose con pasión."

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx4')

    p "..."

    pt "Vale,"

    pt "no se trata de drogas..."

    hide night05_tibidabo_bathroom_n_comp

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    $ renpy.music.stop(channel='sfx2', fadeout=5.0)
    $ renpy.music.stop(channel='sfx3', fadeout=5.0)
    $ renpy.music.stop(channel='sfx4', fadeout=5.0)

    b01 "{size=20}<Creo que el ruido venía del lavabo de al lado...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    b02 "¿Y qué?"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doordown00
    show night05_tibidabo_bathroom_n_exp_eyebrows serious
    with dissolve

    b02 "Si no han dicho nada hasta ahora,"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b02 "es porque tampoco les molesta,"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    b02 "o están haciendo lo mismo que nosotros."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    b01 "{size=20}<Tengo miedo de que nos hagan una foto con el móvil,>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx02
    with dissolve

    b01 "{size=20}<y se enteren mis...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    play sound "audio/sfx/kiss_french02.ogg"

    n "El sonido de un beso apasionado silencia sus palabras."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 07
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b02 "Calladito estás más guapo."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<Neus...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    play sound "audio/characters/neus/shh01.ogg"

    ne "{size=20}<Shhh...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    ne "{size=20}<Ya sé que a ti quizás no te motive imaginarte a dos tíos enrollándose,>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    ne "{size=20}<pero a mí me está poniendo a cien.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    play sound "audio/sfx/kiss_french04.ogg"

    p "{size=20}<{a=https://es.wikipedia.org/wiki/Yaoi}Yaoi{/a}.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    ne "{size=20}<¿Eh...?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<Es el tipo de manga en el que te basas al hacer tus dibujos,>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    play sound "audio/sfx/kiss_french05.ogg"

    p "{size=20}<¿No es así?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    ne "{size=20}<No pienso responder a esa pregunta sin la presencia de mi {a=https://es.wikipedia.org/wiki/Abogado}abogado{/a}...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    pt "El que tengo aquí colgado,"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04
    show night05_tibidabo_bathroom_n_exp_eyes 06
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    pt "no te jode..."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b01 "¡Auhg...!"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Silentx04
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b01 "{size=20}<No me la muerdas...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Silentx05
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doordown02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx02
    with dissolve
    
    b02 "También podrías hacérmelo tú alguna vez,"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    window hide dissolve
    pause 0.25

    show night05_tibidabo_bathroom_n_comp 02:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.8 ypos 1.65 # Hand
        ease_quad 5.0 zoom 0.55 xpos 0.7 ypos 0.6 # hips
    with fade

    pause 2.0

    show night05_tibidabo_bathroom_n_comp 03
    with dissolve

    b02 "y así me enseñas cómo te gusta que te lo hagan..."

    show night05_tibidabo_bathroom_n_comp 03:
        subpixel True
        ease 5.0 zoom 0.55 xpos 0.5 ypos -0.2 # Ass
    with dissolve

    pt "¿Qué demonios hace...?"

    n "Observas que Neus se desliza la minifalda por encima de su cadera,"

    if music_play != "bummin-on-tremelo":
        play music "audio/music/kevinmacleod/bummin_on_tremelo.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bummin-on-tremelo"

    show night05_tibidabo_bathroom_n_comp 04
    with Dissolve (1.5)

    window hide dissolve
    pause

    show night05_tibidabo_bathroom_n_comp 04:
        subpixel True
        ease_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
    with dissolve

    n "mostrándote sus nalgas desnudas,"

    n "en contacto con la delgada tela de tus pantalones que la separa de tu erecto miembro."

    p "{size=20}<Neus.>{/size}"

    p "{size=20}<¿Se puede saber qué estás haciendo?>{/size}"

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with fade

    ne "{size=20}<Ponerme incluso más cachonda.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    ne "{size=20}<Me encantaría que hubiera un agujero aquí para poder verlos...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    p "{size=20}<También podrías usar tus ojos brillantes.{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    ne "{size=20}<No puedo usarlos tan a la ligera...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<¿Y si luego resultan ser más feos que {a=https://es.wikipedia.org/wiki/Gollum}Gollum{/a}?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx03
    with dissolve

    ne "{size=20}<Mira que eres cenizo cuando quieres eh...>{/size}"

    show night05_tibidabo_bathroom_n_comp 05:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
        ease 5.0 zoom 0.55 xpos 0.5 ypos 0.0 # Ass
    with fade

    n "Sus nalgas empiezan a desplazarse a lo largo de tu erección."

    show night05_tibidabo_bathroom_n_comp 05:
        truecenter
        zoom 0.55 xpos 0.5 ypos 0.0 # Ass 
        ease 10.0 zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
    with dissolve

    b01 "{size=20}<El que lleva toda la jodida tarde salido como un depravado eres tú.>{/size}"

    ono "slurp slurp"

    hide night05_tibidabo_bathroom_n_comp

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 07
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b01 "{size=20}<Me prometiste que nos lo tomaríamos con calma.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils doordown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    b01 "Ugh..."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doordown02
    show night05_tibidabo_bathroom_n_exp_eyebrows serious
    with dissolve

    b02 "¿Cuándo aprenderás a no fiarte de mi palabra?"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    b01 "..."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04
    show night05_tibidabo_bathroom_n_exp_eyes 06
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    b02 "No puedo evitar metérmela en la boca cuando está así de dura."

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    p "{size=20}<Neus...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
    with dissolve

    ne "{size=20}<Confiesa que la tienes tan dura como un tanque apuntando a un campanario.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils cameradown04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    p "..."

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    show night05_tibidabo_bathroom_n_comp 06:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
    with fade

    p "{size=20}<Eso es porque no has dejado de magrearme en ningún momento.>{/size}"

    hide night05_tibidabo_bathroom_n_comp

    if Nfjob >= 8:

        show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
        show night05_tibidabo_bathroom_n_exp_eyes 04
        show night05_tibidabo_bathroom_n_exp_pupils cameradown04
        show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
        with dissolve

        ne "{size=20}<Ni ayer cuando estuve masturbándotela con los pies la tenías tan dura.>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth blush 05
    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    ne "{size=20}<Admite al menos que esta situación es bastante excitante...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    p "..."

    show night05_tibidabo_bathroom_n_comp 06:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
    with fade

    menu night05_Park_WC_Lawyer_Question:

        pt "Cuando se pone en plan zorra, es bastante juguetona..."

        "Lo es, porque estás aquí conmigo.":
            call p_Help

            $pl.ch_pts("np",1)

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
            with fade

            ne "{size=20}<Ya...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
            show night05_tibidabo_bathroom_n_exp_eyes 02
            show night05_tibidabo_bathroom_n_exp_pupils camerafront02
            show night05_tibidabo_bathroom_n_exp_eyebrows serious
            with dissolve

            ne "{size=20}<El ponerte cursi,>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
            with dissolve

            ne "{size=20}<no te va a salvar del hecho de que te estás poniendo cachondo>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
            show night05_tibidabo_bathroom_n_exp_eyes 02
            show night05_tibidabo_bathroom_n_exp_pupils doorup02
            show night05_tibidabo_bathroom_n_exp_eyebrows normal
            with dissolve

            ne "{size=20}<teniendo tan cerca a un tío chupándosela a otro,"

            extend " [protname].>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx04
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
            with dissolve

            p "..."

        "Yo también voy a necesitar un abogado para responder a eso.":
            call p_Help

            $pl.ch_pts("np",2)

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth happy_Silentx05
            show night05_tibidabo_bathroom_n_exp_eyes 06
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
            with fade

            ne "*risilla femenina*"

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
            show night05_tibidabo_bathroom_n_exp_eyes 02
            show night05_tibidabo_bathroom_n_exp_pupils camerafront02
            show night05_tibidabo_bathroom_n_exp_eyebrows normal
            with dissolve

            ne "{size=20}<Serás tontín...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
            show night05_tibidabo_bathroom_n_exp_eyes 02
            show night05_tibidabo_bathroom_n_exp_pupils cameradown02
            show night05_tibidabo_bathroom_n_exp_eyebrows serious
            with dissolve

            p "..."

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils cameradown04
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
            with dissolve

            ne "{size=20}<No hace falta que me respondas con palabras...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
            with dissolve

            pt "Será zorra..."

        "¿Te gustaría estar ahí con ellos, en lugar de aquí conmigo?":
            call p_Help

            $pl.ch_pts("np",2)

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
            show night05_tibidabo_bathroom_n_exp_eyes 00
            show night05_tibidabo_bathroom_n_exp_pupils doorup00
            show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
            with fade

            ne "{size=20}<Hmm...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
            with dissolve

            ne "{size=20}<¿Por qué no los cuatro juntos...?>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils camerafront04
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
            with dissolve

            pt "Será zorra..."

        "<No decir nada>":
            call p_Help

            p "..."

        "<Hacerle un cunnilingus>":

            call p_Help

            $pl.ch_pts("np",2)

            $ night05_Park_WC_Lawyer_Cunnilingus = True

            show night05_tibidabo_bathroom_n_comp 04:
                subpixel True
                truecenter
                zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
                ease 5.0 zoom 0.5 xpos 0.5 ypos -0.6 # Going to Pussy.
            with dissolve

            n "Tomas asiento sobre el retrete, detienes sus nalgas,"

            ne "..."

            if music_play != "loopster":
                play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "loopster"

            show night05_tibidabo_bathroom_n_comp 04:
                ease 5.0 zoom 1.2 xpos 0.5 ypos -2.0 # Pussy Close
            with dissolve

            n "y acercas tu rostro a su cálida entrepierna."

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
            show night05_tibidabo_bathroom_n_exp_blush 04
            show night05_tibidabo_bathroom_n_exp_eyes 00
            show night05_tibidabo_bathroom_n_exp_pupils cameradown00
            show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
            with dissolve

            ne "{size=20}<¿Qué...?>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01
            show night05_tibidabo_bathroom_n_exp_blush 04
            show night05_tibidabo_bathroom_n_exp_eyes 02
            show night05_tibidabo_bathroom_n_exp_pupils cameradown02
            show night05_tibidabo_bathroom_n_exp_eyebrows angryx01
            with dissolve

            ne "{size=20}<[protname]...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01
            show night05_tibidabo_bathroom_n_exp_blush 05
            show night05_tibidabo_bathroom_n_exp_eyes 04
            show night05_tibidabo_bathroom_n_exp_pupils cameradown04
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
            with dissolve

            ne "{size=20}<Te he dicho que en público...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
            show night05_tibidabo_bathroom_n_exp_blush 05
            show night05_tibidabo_bathroom_n_exp_eyes 05
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
            with dissolve

            ne "{size=20}<no...>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx03
            show night05_tibidabo_bathroom_n_exp_blush 06
            show night05_tibidabo_bathroom_n_exp_eyes 06
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
            with dissolve

            ne "{size=25}<MMMhhhmmnhff...>{/size}"

            show night05_tibidabo_bathroom_n_comp 04:
                subpixel True
                truecenter
                zoom 2.5 xpos 0.5 ypos -4.0 # Pussy SuperClose Up
                block:
                    easein 2.0 ypos -4.8 # Pussy SuperCLose Down
                    easeout 2.0 ypos -4.4 # Pussy SuperClose Up
                    repeat

            with fade

            b01 "{size=20}<¿Has oído eso...?>{/size}"

            b02 "¿El cómo estás gimiendo como una chica?"

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
            show night05_tibidabo_bathroom_n_exp_blush 05
            show night05_tibidabo_bathroom_n_exp_eyes 05
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
            with dissolve

            ne "{size=20}<[protname]...>{/size}"

            show night05_tibidabo_bathroom_n_comp 04:
                subpixel True
                truecenter
                zoom 2.5 xpos 0.5 ypos -4.0 # Pussy SuperClose Up
                block:
                    easein 2.0 ypos -4.8 # Pussy SuperCLose Down
                    easeout 2.0 ypos -4.4 # Pussy SuperClose Up
                    repeat

            with fade

            b01 "{size=20}<¡Yo no he gemido de esa manera!>{/size}"

            b02 "Ya sé cómo gimes, idiota."

            b02 "Te estoy tomando el pelo."

            b02 "Si los de al lado se lo están pasando bien,"

            b02 "¿quiénes somos nosotros para juzgarlos?"

            b01 "{size=20}<¡Eres tú quien ha empezado!>{/size}"

            b02 "Y tú eres quien no me está deteniendo."

            b01 "..."

            hide night05_tibidabo_bathroom_n_comp
            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx02
            show night05_tibidabo_bathroom_n_exp_blush 05
            show night05_tibidabo_bathroom_n_exp_eyes 05
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
            with dissolve

            ne "{size=25}<¡[protname]!>{/size}"

            show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03
            show night05_tibidabo_bathroom_n_exp_blush 06
            show night05_tibidabo_bathroom_n_exp_eyes 06
            show night05_tibidabo_bathroom_n_exp_pupils empty
            show night05_tibidabo_bathroom_n_exp_eyebrows sadx04
            with dissolve

            ne "AAAAhhhhhhmmm..."

            show night05_tibidabo_bathroom_n_comp 04:
                subpixel True
                truecenter
                zoom 2.5 xpos 0.5 ypos -4.0 # Pussy SuperClose Up
                easein_quad 2.0 zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
                #easein_quad 1.0 zoom 0.5 xpos 0.5 ypos -0.6 # Going to Pussy.

            with fade

            scene bg an04_Dgrabbingshirt_bg_bathroom:
                truecenter
                zoom 0.5
            show n_closefromup_body sd:
                truecenter
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_blush 07:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_eyes 07:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_iris front06:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_eyebrows sadx01:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_tears empty:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_mouth sadbiting_Silentx09:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_glasses:
                zoom 0.4 xalign 0.5 yalign 0.5
            show n_closefromup_hair_front:
                zoom 0.4 xalign 0.5 yalign 0.5
            with hpunch

            n "Neus abre repentinamente la puerta y sale del habitáculo de golpe."

            if music_play != "bummin-on-tremelo":
                play music "audio/music/kevinmacleod/bummin_on_tremelo.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bummin-on-tremelo"

            show n_closefromup_eyes 08
            show n_closefromup_iris front07
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sad_Talkingx03
            with dissolve

            ne "Ahhh-ahhh-ahh..."

            show n_closefromup_blush 06
            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx01
            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "¡Te había dicho que aquí no!"

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows serious
            show n_closefromup_mouth sadbiting_Silentx02
            with dissolve

            p "Pero bien que has tardado en abrir la puerta..."

            show n_closefromup_eyes 04
            show n_closefromup_iris right04
            show n_closefromup_eyebrows suspiciousx01
            show n_closefromup_mouth sadbiting_Silentx03
            with dissolve

            p "Tan mal no lo estarías pasando."

            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows suspiciousx02
            show n_closefromup_mouth sad_Silentx04
            with dissolve

            ne "..."

            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx02
            show n_closefromup_mouth sad_Talkingx002
            with dissolve

            ne "¡Por supuesto que no lo estaba pasando mal!"

            show n_closefromup_eyes 02
            show n_closefromup_iris left02
            show n_closefromup_eyebrows angryx01
            show n_closefromup_mouth sad_Talkingx005
            with dissolve

            ne "No..."

            show n_closefromup_eyes 04
            show n_closefromup_iris left04
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "No se trata de eso..."

            show n_closefromup_blush 05
            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows suspiciousx02
            show n_closefromup_mouth happy_Talkingx03
            with dissolve

            ne "Idiota."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows surprisex01
            show n_closefromup_mouth sad_Silentx01
            with dissolve

            p "Entonces no se me da tan mal,"

            extend " ¿verdad?"

            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows suspiciousx03
            show n_closefromup_mouth happybiting_Silentx05
            with dissolve

            ne "..."

            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows suspiciousx02
            show n_closefromup_mouth happy_Talkingx02
            with dissolve

            ne "No..."

            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows angryx02
            show n_closefromup_mouth happy_Talkingx04
            with dissolve

            ne "Nada mal."

            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx01
            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "¡Pero aprende a obedecer un poco más!"

            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows serious
            show n_closefromup_mouth sadbiting_Silentx02
            with dissolve

            p "No suelo ser de acatar órdenes."

            show n_closefromup_eyes 00
            show n_closefromup_iris left00
            show n_closefromup_eyebrows surprisex02
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            b02 "¡Di que no campeón!"

            show n_closefromup_eyes 02
            show n_closefromup_iris left02
            show n_closefromup_eyebrows surprisex01
            show n_closefromup_mouth happy_Silentx02
            with dissolve

            b01 "¡Oye!"

            show n_closefromup_eyes 01
            show n_closefromup_iris left01
            show n_closefromup_eyebrows suspiciousx02
            show n_closefromup_mouth sadbiting_Silentx03
            with dissolve

            b01 "¡Ugh...!"

            show n_closefromup_eyes 04
            show n_closefromup_iris left04
            show n_closefromup_eyebrows sadx01
            show n_closefromup_mouth sadbiting_Silentx05
            with dissolve

            ne "..."

            show n_closefromup_eyes 05
            show n_closefromup_iris left05
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth sadbiting_Silentx09
            with dissolve

            b01 "¡Dios...!"

            show n_closefromup_blush 06

            show n_closefromup_eyes 05
            show n_closefromup_iris left05
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sadbiting_Silentx09
            with dissolve

            b01 "Si no paras,"

            show n_closefromup_eyes 05
            show n_closefromup_iris left05
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sadbiting_Silentx10
            with dissolve

            b01 "voy a..."

            show n_closefromup_eyes 04
            show n_closefromup_iris left04
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth happybiting_Silentx06
            with dissolve

            b02 "¿Parar?"

            show n_closefromup_eyes 05
            show n_closefromup_iris left05
            show n_closefromup_eyebrows sadx04
            show n_closefromup_mouth happybiting_Silentx07
            with dissolve

            b02 "¡Reviéntame la tráquea con tu corrida!"

            show n_closefromup_blush 07

            show n_closefromup_eyes 08
            show n_closefromup_iris front07
            show n_closefromup_eyebrows sadx03
            show n_closefromup_mouth sadbiting_Silentx09
            with dissolve

            ne "HMmmff..."

            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows normal
            show n_closefromup_mouth sadbiting_Silentx02
            with dissolve

            if night05_Park_WC_Lawyer_Cunnilingus:

                p "Aunque no estoy muy seguro de si te ha puesto más caliente mi lengua en tus labios menores,"

            else:

                p "Aunque no estoy seguro de si te ha puesto más ter mi dura polla tan cerca,"

            show n_closefromup_eyes 01
            show n_closefromup_iris left01
            show n_closefromup_eyebrows surprisex02
            show n_closefromup_mouth sadbiting_Silentx01
            with dissolve

            p "o los de aquí al lado."

            show n_closefromup_eyes 04
            show n_closefromup_iris right04
            show n_closefromup_eyebrows sadx02
            show n_closefromup_mouth happybiting_Silentx06
            with dissolve

            ne "..."

            if night04_pedrera_blowjob_DONE:

                show n_closefromup_eyes 04
                show n_closefromup_iris front04
                show n_closefromup_eyebrows angryx01
                show n_closefromup_mouth happy_Talkingx05
                with dissolve

                ne "Ya sabes cómo me gusta el esperma caliente..."

                show n_closefromup_eyes 05
                show n_closefromup_iris front05
                show n_closefromup_eyebrows serious
                show n_closefromup_mouth happybiting_Silentx07
                with dissolve

                pt "Será zorra..."

            else:

                show n_closefromup_eyes 04
                show n_closefromup_iris front04
                show n_closefromup_eyebrows suspiciousx01
                show n_closefromup_mouth happy_Talkingx03
                with dissolve

                ne "Y luego yo soy la perturbada..."

            show n_closefromup_blush 06

            show n_closefromup_eyes 02
            show n_closefromup_iris front02
            show n_closefromup_eyebrows surprisex01
            show n_closefromup_mouth happy_Talkingx04
            with dissolve

            ne "Te espero fuera."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows surprisex02
            show n_closefromup_mouth sadbiting_Silentx02
            with dissolve

            p "¿Me vas a dejar así?"

            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx02
            show n_closefromup_mouth sad_Talkingx004
            with dissolve

            ne "Como si tú me hubieras dejado mucho mejor..."

            show n_closefromup_eyes 01
            show n_closefromup_iris front01
            show n_closefromup_eyebrows normal
            show n_closefromup_mouth sad_Silentx02
            with dissolve

            p "Pero yo no tenía intención de parar."

            show n_closefromup_eyes 04
            show n_closefromup_iris front04
            show n_closefromup_eyebrows angryx01
            show n_closefromup_mouth sadbiting_Silentx03
            with dissolve

            ne "..."

            show n_closefromup_eyes 05
            show n_closefromup_iris front05
            show n_closefromup_eyebrows angryx02
            show n_closefromup_mouth happy_Talkingx05
            with dissolve

            ne "Tonto."

            show n_closefromup_eyes 06
            show n_closefromup_iris front06
            show n_closefromup_eyebrows normal
            show n_closefromup_mouth happy_Silentx05
            with dissolve

            pause 0.5

            play sound "audio/sfx/door_close01.ogg"

            scene bg night05_bg_tibidabo_bathroom_wall_door
            with dissolve

            p "..."

            b01 "Te dije que había alguien más..."

            b02 "MMmm..."

            b02 "Y yo te dije que me importaba una mierda."

            p "..."

            $ saturation_tint_level = "dark"

            pt "¡¿Y ahora cómo me bajo esto?!"

            jump night05_Park_Bathroom_After

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex01
    with dissolve

    b01 "{size=20}<Si no paras,>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 07
    show night05_tibidabo_bathroom_n_exp_pupils empty
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    b01 "{size=20}<voy a...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happybiting_Silentx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    b02 "¿Parar?"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils doorup00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    b02 "Reviéntame la tráquea con tu corrida."

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx01
    with dissolve

    ne "{size=20}<Qué salvaje es este...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx03
    with dissolve

    ne "{size=20}<¿No te parece?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows serious
    with dissolve

    ne "{size=20}<¿[protname]..?>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    p "{size=20}<Yo...>{/size}"

    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<Tampoco creo que vaya a durar mucho más...>{/size}"

    stop music fadeout 3.0
    $ music_play = ""

    show night05_tibidabo_bathroom_n_comp 06:
        truecenter
        zoom 0.55 xpos 0.5 ypos 0.0 # Ass
    with fade

    show night05_tibidabo_bathroom_n_comp 04
    with dissolve

    n "Las nalgas de Neus se detienen al instante."

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth sad_Talkingx03
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils camerafront02
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx02
    with fade

    ne "{size=20}<¡De eso ni hablar!>{/size}"

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows angryx03
    with dissolve

    b01 "¡No pares...!"

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx01
    show night05_tibidabo_bathroom_n_exp_eyes 04
    show night05_tibidabo_bathroom_n_exp_pupils camerafront04
    show night05_tibidabo_bathroom_n_exp_eyebrows normal
    with dissolve

    ono "Glup Glup Glup"

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "loopster"

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth happy_Talkingx02
    show night05_tibidabo_bathroom_n_exp_eyes 02
    show night05_tibidabo_bathroom_n_exp_pupils doorup02
    show night05_tibidabo_bathroom_n_exp_eyebrows sadx02
    with dissolve

    ne "{size=20}<Se me hace la boca agua...>{/size}"

    hide night05_tibidabo_bathroom_n_comp
    show night05_tibidabo_bathroom_n_exp_mouth sad_Silentx03
    show night05_tibidabo_bathroom_n_exp_eyes 00
    show night05_tibidabo_bathroom_n_exp_pupils camerafront00
    show night05_tibidabo_bathroom_n_exp_eyebrows surprisex02
    with dissolve

    p "{size=20}<Voy a...>{/size}"

    play sound "audio/sfx/fall05.ogg"

    scene bg night05_bg_tibidabo_bathroom_wc_wall:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.0 ypos 1.0 # Face
        #pause 0.5
        #easein_elastic 1.0 zoom 0.5 xpos 0.5 ypos 0.47 # Ass_Eyes
        #easein_quad 1.0 zoom 0.3 xpos 0.5 ypos 0.5 # General
    with hpunch

    n "Rápidamente sale del pequeño habitáculo en el que os encontrabais."

    scene bg an04_Dgrabbingshirt_bg_bathroom:
        truecenter
        zoom 0.5
    show n_closefromup_body sd:
        truecenter
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_blush 05:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 04:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_iris front04:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows angryx01:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_tears empty:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_mouth happy_Talkingx04:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:
        zoom 0.4 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:
        zoom 0.4 xalign 0.5 yalign 0.5
    with fade

    ne "{size=20}<Te espero fuera.>{/size}"

    show n_closefromup_eyes 00
    show n_closefromup_iris front00
    show n_closefromup_eyebrows surprisex02
    show n_closefromup_mouth sad_Silentx01
    with dissolve

    p "{size=20}<Eres una calienta braguetas...>{/size}"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows angryx02
    show n_closefromup_mouth happy_Talkingx03
    with dissolve

    ne "{size=20}<En este caso,>{/size}"

    show n_closefromup_eyes 07
    show n_closefromup_iris front06
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "{size=20}<no puedo negártelo,>{/size}"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows sadx04
    show n_closefromup_mouth happy_Silentx07
    with dissolve

    pt "Será cabrona..."

    show n_closefromup_eyes 04
    show n_closefromup_iris front04
    show n_closefromup_eyebrows sadx02
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "{size=20}<es literalmente lo que te he hecho.>{/size}"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows suspiciousx03
    show n_closefromup_mouth happy_Talkingx05
    with dissolve

    ne "{size=20}<Pero de este modo lo tendrás mucho más espeso esta noche...>{/size}"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows sadx03
    show n_closefromup_mouth happybiting_Silentx07
    with dissolve

    pause 0.5

    play sound "audio/sfx/door_close01.ogg"

    scene bg night05_bg_tibidabo_bathroom_wall_door
    with dissolve

    n "Rápidamente desaparece de tu vista al dirigirse a la salida."

    pt "Será cabrona..."

    b01 "{size=20}<Te dije que había alguien más...>{/size}"

    b02 "Mmm..."

    b02 "Y yo te dije que me importaba una mierda."

    p "..."

    $ saturation_tint_level = "dark"

    pt "¡¿Y ahora cómo me bajo esto?!"

label night05_Park_Bathroom_After:

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.2, delay=15.0, channel='sfx1')

    scene bg night05_bg_tibidabo_park_around01:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
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
    show neus_exp_mouth sad_Talkingx002:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with fade

    ne "Has tardado bastante."

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "He creído oportuno no salir con la bandera en alto."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_eyebrows serious
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows angryx02
    with dissolve

    ne "Espero que no se te haya pasado por la cabeza hacerlo tú solo ahí dentro."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Se me ha ocurrido,"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows serious
    with dissolve

    p "pero luego he pensado en ti"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "y me ha dado miedo tu posible reacción."

    if music_play != "almost_new_kevin":
        play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "almost_new_kevin"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyes 02
    show neus_exp_iris down02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Tampoco quiero darte miedo..."

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Pero me alegro de que te hayas aguantado por mí."

    show neus_exp_mouth happy_Silentx03
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx02
    with dissolve

    pt "También me aguantaría las ganas de bañarme en un río donde hay un cocodrilo,"

    show neus_exp_mouth happy_Silentx03
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx01
    with dissolve

    pt "y eso no significa que me esté enamorando del reptil..."

    ##

label night05_Park_Cups_After:

    $ saturation_tint_level = "verydark"

    stop music fadeout 3.0
    $ music_play = ""
    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.1, delay=20.0, channel='sfx1')

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    ne "Sigamos."

    if night05_Park_WC_NeusCry_BeingRude_Cond == True:

        pt "A pesar de haber salido del baño llorando,"

        pt "sigue cogiéndome de la mano..."

    #########################################################
    
    if config.version < "00.12.00": # Voyeurism (?) in WC with Neus.
        
        call endupdatescript
    
    #######################################################

    p "¿Qué hora es?"

    scene bg_dark_a
    show n_closefromup_body sd:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 02:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris front01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows sadx01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears empty:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Siletx01:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:
        zoom 0.5 xalign 0.5 yalign 0.5

    if night05_Park_Bathroom_Bad_Cond == True:

        if music_play != "bittersweet":
            play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "bittersweet"

        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows angryx02
        show n_closefromup_mouth sad_Talkingx05
        with fade

        ne "¿Tantas ganas tienes de que termine esta cita?"

        show n_closefromup_eyes 04
        show n_closefromup_iris front04
        show n_closefromup_eyebrows sadx01
        show n_closefromup_mouth sad_Silentx03
        with dissolve

        p "..."

    elif night05_Park_Cups_Used == False:

        if music_play != "bittersweet":
            play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "bittersweet"

        show n_closefromup_eyes 04
        show n_closefromup_iris front04
        show n_closefromup_eyebrows angryx03
        show n_closefromup_mouth sad_Talkingx03
        with fade

        ne "¿Por qué?"

        show n_closefromup_eyes 02
        show n_closefromup_iris front02
        show n_closefromup_eyebrows sadx01
        show n_closefromup_mouth sad_Talkingx04
        with dissolve

        ne "¿Tanta prisa tienes de volver a casa?"

        show n_closefromup_eyes 05
        show n_closefromup_iris front05
        show n_closefromup_eyebrows sadx01
        show n_closefromup_mouth sad_Silentx04
        with dissolve

        p "..."

    else:

        show n_closefromup_eyes 04
        show n_closefromup_iris front04
        show n_closefromup_eyebrows serious
        show n_closefromup_mouth sad_Silentx01
        with dissolve

        ne "..."

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows surprisex01
    with dissolve

    p "¿Crees que nos queda tiempo para ir a otra atracción?"

    show n_closefromup_eyes 02
    show n_closefromup_iris right02
    show n_closefromup_eyebrows suspiciousx01
    show n_closefromup_mouth sad_Talkingx002
    with dissolve

    ne "Queda una hora para que cierre el parque,"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows serious
    show n_closefromup_mouth sad_Talkingx05
    with dissolve

    ne "seguramente será la última."

    show n_closefromup_eyes 02
    show n_closefromup_iris front02
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth sad_Talkingx04
    with dissolve

    ne "Pero no quisiera irme"

    show n_closefromup_eyes 01
    show n_closefromup_iris front01
    show n_closefromup_eyebrows sadx01
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "sin visitar el castillo."

    show n_closefromup_eyes 00
    show n_closefromup_iris front00
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth happy_Silentx04
    with dissolve

    p "¿Hay un castillo?"

    show n_closefromup_eyes 05
    show n_closefromup_iris front05
    show n_closefromup_eyebrows normal
    show n_closefromup_mouth happy_Talkingx04
    with dissolve

    ne "Ya lo verás."

    show n_closefromup_eyes 07
    show n_closefromup_iris front06
    show n_closefromup_eyebrows surprisex01
    show n_closefromup_mouth happy_Silentx07
    with dissolve

    pause 0.5

    scene bg night04_fnac_01_blur_03
    show night04_pedrera_Ngrabhand_hold_night05_park:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5    
    with fade

    n "Vuelves a sentir el calor de su mano."

    n "Mientras te arrastra suavemente a través de medio parque,"

    scene night05_bg_castle_flag:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    stop music fadeout 3.0
    $ music_play = ""

    $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_theme01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "hasta llegar a lo que efectivamente es un gran edificio de falsa piedra,"

    $ renpy.music.set_volume(0.1, delay=20.0, channel='sfx1')

    n "en forma de fortaleza con toques de fantasía."

    scene night05_bg_castle_queue:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    pt "Con la gente que hay esperando a la entrada,"

    pt "no hay duda de que haremos por lo menos otra media hora de cola..."

    p "¿Qué tiene de especial este castillo?"

    if music_play != "fireflies_and_stardust":
        play music "audio/music/kevinmacleod/fireflies_and_stardust.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "fireflies_and_stardust"

    scene night05_bg_castle_queue:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
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
    show neus_exp_mouth happy_Talkingx05:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris left01:
        neus_exp_atright_position
    show neus_exp_eyebrows normal:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "Es como un museo de cuentos de fantasía y folclore."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "¿Qué?"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "¿No ves a muchos niños con sus padres haciendo cola?"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyes 00
    show neus_exp_iris left00
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows suspiciousx01
    with dissolve

    ne "También he visto varios en las otras atracciones..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "Pero no tantos."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_eyebrows suspiciousx02
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_eyebrows serious
    with dissolve

    ne "Ahora que lo mencionas..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¿No crees que será un poco demasiado infantil?"

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "Es que en el fondo soy como una niña."

    play sound "audio/characters/neus/giggle02.ogg"

    show neus_exp_mouth happy_Silentx08
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "..."

    if pl.np < 100: #NOT FINISHED how many points? opinion.

        show neus_exp_mouth happy_Silentx05
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_eyebrows normal
        with dissolve

        pt "No tengo ninguna excusa realmente para rechazar esta atracción,"

        show neus_exp_mouth happy_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows serious
        with dissolve

        pt "no parece que sea de las que marean,"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_eyebrows sadx01
        with dissolve

        pt "o vaya a ser peligrosa..."

    show neus_exp_mouth happy_Silentx05
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows normal
    with dissolve

    p "Vale,"

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows surprisex01
    with dissolve

    p "como quieras."

    show neus_exp_mouth happy_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "Viendo lo mucho que se han trabajado el exterior,"

    show neus_exp_mouth happy_Silentx08
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows surprisex03
    with dissolve

    p "me imagino que también habrá algo bonito que ver dentro."

    show neus_exp_mouth happy_Talkingx06
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_eyebrows surprisex01
    with dissolve

    ne "Así me gusta."

    scene night05_bg_castle_flag:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease_quad 40.0 zoom 1.0 xpos 0.5 ypos 0.5
    with fade
    # show flag and tower.

    n "Durante el transcurso de la espera,"

    n "debatís en qué cuentos están inspirados los distintos elementos decorativos que ornamentan el castillo,"

    n "como la longeva trenza que cuelga de una de las ventanas,"

    n "o los pictogramas que se encuentran en la bandera que cuelga a su lado,"

    scene night05_bg_castle_queue:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.25 ypos 0.75
        easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "mientras te percatas de que uno de los niños que os acompaña en la cola,"

    n "se va acercando poco a poco a Neus,"

    scene night05_bg_castle_queue:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
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
    show neus_exp_mouth sadbiting_Silentx05:
        neus_exp_atright_position
    show neus_exp_eyes 00:
        neus_exp_atright_position
    show neus_exp_iris down00:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    n "hasta quedarse embobado mirando descaradamente su trasero,"

    show neus_exp_blush 03
    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_eyebrows suspiciousx02
    with dissolve

    show black
    with fade

    n "y para cuando es un poco tarde,"

    # Kid staring to Neus # NOT FINISHED

    n "esta se da cuenta de que lleva la minifalda muy corta,"

    n "y que, debido a la altura del niño,"

    n "es capaz de comprobar su ausencia de ropa interior."

    hide black
    show neus_exp_blush 04
    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_eyebrows suspiciousx02
    with dissolve

    n "No puedes evitar reírte a pesar de que ella te pide que guardes silencio para no generar polémica,"

    show neus_exp_blush 05
    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyes 04
    show neus_exp_iris down04
    show neus_exp_eyebrows sadx04
    with dissolve

    n "mientras se sonroja por la situación,"

    show black
    with fade

    n "e intenta hablar con el niño para que no le explique nada a su madre."

    $ mmouthp = "_Blue"

    scene bg night05_bg_castle_siege_comp_01:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.9
        ease_quad 15.0 xpos 0.5 ypos 0.11
    with fade

    # Txell Guard. # Not finished

    n "Finalmente llegáis a lo que a todas luces parece una reinterpretación de una torre de asedio medieval,"

    n "con dos escalinatas distintas que llevan a la entrada del castillo,"

    n "unas normales, y las otras mecánicas con un ritmo arquetípico para simular un terremoto;"

    n "custodiada por una mujer morena de pelo largo,"

    n "alta y voluptuosa con gafas de sol y una gorra de seguridad,"

    n "que os cierra el paso;"

    n "a la espera de que el anterior grupo haya hecho su recorrido,"

    n "para poder vosotros empezar el vuestro."

    pt "¿Qué hace esta mujer con gafas de sol en plena noche?"

    ne "Uooh..."

    show bg night05_bg_castle_siege_comp_01:
        zoom 0.5 xpos 0.5 ypos 0.11

    #show m_body guard:
        #mtxell_body_onleftpark_position
        #alpha 0.5
    #show m_arm_r guard_hip:
        #mtxell_body_onleftpark_position
    #show m_exp_mouth sad_Silentx02:
        #mtxell_exp_onleftpark_position
    #how m_exp_over hat:
        #mtxell_exp_onleftpark_position

    show neus_arm_r sd:
        neus_body_atright_position
    show neus_body sd_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arm_l sd:
        neus_body_atright_position

    show neus_exp_blush 04:
        neus_exp_atright_position
    show neus_exp_mouth happy_Talkingx06:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_iris front01:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    ne "Me encantan este tipo de atracciones donde las escaleras o el suelo se mueven."

    show neus_exp_mouth happy_Silentx07
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "..."

    show bg night05_bg_castle_siege_comp_02
    show neus_exp_mouth happy_Silentx08
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_eyebrows normal
    with dissolve

    n "Finalmente, la mujer de seguridad os da la señal para permitiros el paso a la atracción."

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex02
    with dissolve

    ne "¡Te espero arriba [protname]!"

    show neus_exp_mouth happy_Silentx06
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_eyebrows normal
    with dissolve

    scene bg night05_bg_castle_siege_comp_02:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.11
    with dissolve

    p "Vale..."

    jump night05_NeusLastDate_HotelKrueger

    ## AQUI ES CUANDO ELGUÍ APARECE ILUMINÁNDOSE EL ROSTRO Y DICIENDO QUE SIGAS ESE CAMINO.


## Después de pasar tu polla por sus nalgas y llegar al punto de casi correrte, sale del baño y te dice que te espera fuera, que ni se te ocurra terminar de masturbarte, que se lo reserves todo para ella, ya que aún no ha cenado.

# Una vez fuera veis que ya es muy tarde, pero aún así te pide que probeis de ir a otra atracción. El castillo.


###


#Le preguntas dónde tiene pensado ir a comer, ella responde, que no había pensado en la comida, que tiene otra cosa en mente de comer esa noche, pero entiende tu hambre. Te pregunta si prefieres cenar un hot-dog una pizza.


#Le comentas que ayer ella te hizo un interrogatorio, pero ahora es hora de que seas tú quien le hagas ciertas preguntas.


#Acepta a regañadientes y te promete serte sincera, pero también que quizás no te responda todas las preguntas, a lo que le respondes que tú sí lo hiciste, y ell te dice que tampoco te obligó a ello.


#Tiene recuerdos del lugar cuando lo inauguraron en 1905 con las primeras atracciones, los espejos, telescopios, biniculares, los primeros autómatas, columpios, el tiro Flobert, juegos de bolos, una estación de palomas mensajeras..


#Cuando le preguntas cómo recuerda todo eso si paso hace más de 100 años, te dice que se ha equivocado, que eso es lo que le contó su padre con tal viveza que pareciera que lo hubiera vivido ella misma.


#En general aquí hay que informar un poco sobre las sospechas de la longeva edad de Neus, su amor por su madre y su extraña desaparición, el hecho de que solo tenga hermanas que tuvo que abandonar, su estrecha pero odiosa relación con su padre, más parecido a un culto satánico que una relación sana, del que dispone de mucho dinero y poder, por lo que no puede denunciar y sólo puede esconderse.


#Una vez terminado de comer te dice dir a los caballitos, para luego ir a las tazas, finalmente al tren con las gafas... No sé que coño haré en esta parte... sería interesante probar algo erótico en los baños? En el parque mientras van a comer en los terrenos del bosque? No sé... Le ha hecho algo de comer ella en plan vegetariano que quizás le guste más que ayer, o aceptará comerse un sandwich o una pizza del telepizza? En cualquier caso irán a comer no sé dónde... Luego el baño?


#La penúltima atracción es el Castillo de los cuentos del que hacen la cola más larga, pero cuando por fin llegan, Neus empieza a subir mientras la segurata con gafas de sol, te detiene, luego oyes el grito de Neus preguntándote porque tardas tanto en subir, sientes un pinchazo en el cuello mientras la segurata te sonríe y te invita a subir, cuando atraviesas el portal, sólo hay oscuridad. Empieza el camino por el Hotel Kruger. (Dónde experimentas los recuerdos de la gente muerte a manos de ella).


#Cuando sales del hotel, te descubres que te han sacado de la entrada del castillo que ni siquiera has llegado a subir las escaleras, dónde te encuentras a un equipo médico que te hace unas preguntas para saber cómo te encuentras, una vez asegurado que te encuentras bien y que sólo ha sido un mareo, le dan a Neus el número que tiene que llamar si vuelve a ocurrir algo parecido y que tenga cuidado de ti.


#Te pregunta que ha ocurrido y le respondes la verdad, entonces ella queda sorprendida y aparentemente preocupada, te propone que quizás lo más sensato sea salir del parque, pero poco antes de salir, vuelves a mirar la Nória y le recuerdas que antes había dicho que debía de ser precioso poder subir a la Noria cuando se hace de noche para poder ver la ciudad iluminada.


#Ella accede teniendo en cuenta que no es una atracción de acción, y cuando estáis en la cima, te dice algo bonito, o yo que sé, el cielo se ilumina con fuegos de artificio por gente preparando el día de San Juany entre los fuegos de artificio te vuelve a besar.


#En medio del beso recibes un mensaje de Dídac, en el que aparece desnudo y perturbador en la Pedrera, dándote a entender que regreses lo más pronto posible sino quieres perderlo o algo así...


#Volveis rápidamente cogiendo un taxi en lugar del metro y el funicular y una vez llegáis y abrís la puerta oís los gemidos de Dídac que proceden de la habitación de Neus, ahí encuentras a Txell encima de Dídac lamiendole coño.

############################

## Os encontráis en Plaza Cataluña como la última vez.

## Pero en esta ocasión te ha pedido citarte allí un poco más temprano, a las 7 de la tarde, siendo verano aún es de día. (El parque cierra a las 9 de la noche).

# Ir con bus con el TIBIBUS o con 

# Abierto de Marzo a Diciembre.

# Pero en esta ocasión te dice que tiene intención de ir un poco más lejos, por lo que vais a tener que coger el metro, durante el viaje te muestra su sinverguenza al abrirse de piernas sobre el asiento y mostrarte que como siempre nunca llevaje ropa interior bajo sus prendas.

# Una vez llegais al destino descubres que tenéis que coger la tirolina para subiros a la montaña de Montjuic para llegar al parque de atracciones del Tibidabo.

# Final: Estación Funicular Tibidabo cuando están tirando los fuegos de artificio el 23 de Junio de 2019 en toda la Barceloneta). (Solsticio de Verano, es cuando toca nuevo Akelarre).