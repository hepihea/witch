
default MShooter_fired = 0
default MShooter_points = 0
default MShooter_target_05 = 0
default MShooter_target_04 = 0
default MShooter_target_03 = 0
default MShooter_target_02 = 0
default MShooter_target_01 = 0
default MShooter_target_00 = 0
default night05_Park_MinigameShooter_Played = False

#default MShooter_Bracelet = 0 # 1 GOLD, # 2 SILVER, # 3 BRONZE, # 4 PLASTIC PINK.
default MShooter_Bracelet = "" # 1 GOLD, # 2 SILVER, # 3 BRONZE, # 4 PLASTIC, # 5 None
 
image shooter_target:
    "images/day05/night/minigameshooter/shooter_target.webp"
    zoom 0.5

image shooter_bg:
    "images/day05/night/minigameshooter/shooter_bg.webp"

image shooter_waves:
    "images/day05/night/minigameshooter/shooter_waves.webp"

image shooter_waves_02:
    im.MatrixColor("images/day05/night/minigameshooter/shooter_waves.webp",
        im.matrix.saturation(0.5) * im.matrix.tint(.45, .45, .8))

transform shooter_waves_position:
    transform_anchor True
    xalign 0.5 yalign 1.0
    xpos 0.75 ypos 1.0
    block:
        easein_quad 5.0 xpos 0.25 ypos 1.0
        easeout_quad 5.0 xpos 0.75 ypos 1.025
        repeat

transform shooter_waves_position_02:
    transform_anchor True
    xalign 0.5 yalign 1.0
    xpos 0.7 ypos 1.0
    block:
        easein_quad 5.0 xpos 0.275 ypos 1.025
        easeout_quad 5.0 xpos 0.725 ypos 1.05
        repeat

transform shooter_target_move:
    transform_anchor True
    xalign 0.5 yalign 0.13
    block:
        xpos -250 #Max Left is -200 # Origin
        pause 0.5
        easeout_quad 1.5 xpos 1050 #Max Right is 1000 (800 + 200)
        xpos -250 #Max Left is -200 # Origin
        pause 0.5
        easein_quad 2.0 xpos 1050
        repeat


label night05_Park_MinigameShooter_Introduction:

    if music_play != "twisted":
        play music "audio/music/kevinmacleod/twisted.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "twisted"

    $ night05_Park_MinigameShooter_Played = True

    scene shooter_bg
    show shooter_waves at shooter_waves_position
    show shooter_waves_02 at shooter_waves_position_02
    show shooter_target:
        transform_anchor True
        xalign 0.5 yalign 0.13
    with fade

    rat "La mec??nica es muy simple,"

    rat "Ten??is {b}cinco{/b} tiros."

    rat "Cuanto m??s cerca dispar??is del {b}centro de la diana{/b},"

    rat "m??s puntos tendr??is."

    rat "El centro amarillo vale cinco,"

    rat "cada anillo que se aleja es {b}un punto menos{/b}."

    rat "As?? que se puede ganar hasta un m??ximo de {b}veinticinco{/b} puntos."

    show night05_tibidabo_bracelet_bracelets:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    rat "Estos son los premios."

    window hide dissolve
    pause

    hide night05_tibidabo_bracelet_bracelets
    with fade

    pt "Bueno,"

    pt "ah?? vamos."

    call night05_Park_MinigameShooter_Game

    jump night05_Park_MinigameShooter_Finished

    # MINIJUEGO? ESPERO QUE NO MUY COMPLICADO...

    # Premios: Un globo, un peluche de una rana, de un mono, una pulsera de tela o de metal, seg??n los puntos.

    # Premios:

        # 10: Pulsera de goma rosa.
        # 15: Pulsera de bronze.
        # 20: Pulsera de plata.
        # 25: Pulsera dorada.

############################################################################
############################################################################

label night05_Park_MinigameShooter_Game:
    
    scene shooter_bg
    show shooter_waves at shooter_waves_position
    show shooter_waves_02 at shooter_waves_position_02
    show shooter_target at shooter_target_move
    $ position_shooter_target = At(ImageReference("shooter_target"), shooter_target_move)
    show expression position_shooter_target
    with fade

    $ ui.imagebutton("images/day05/night/minigameshooter/crosshair.webp", "images/day05/night/minigameshooter/crosshair_focused.webp", clicked = ui.returns("fired"), xpos= 300, ypos = 127)
    $ fired_gun = ui.interact()
    
    show expression position_shooter_target
    #with vpunch # If used, time doesn??t work.
    $ MShooter_fired += 1

    #if 0.45 <= position_shooter_target.xpos <= 0.55: # CENTER 5 POINTS # With Float numbers.
    if position_shooter_target.xpos in range (360, 440): # CENTER 5 POINTS
        call p_Help
        with vpunch
        $ MShooter_target_05 += 1
        $ MShooter_points += 5
        pt "??Amarillo!"

        extend " ??Cinco puntos!"

        if MShooter_target_05 == 1:

            ne "??Muy bien [protname]!"

            if MShooter_fired == 1:

                ne "??El centro de la diana a la primera!"

            rat "??Bah!"

            rat "La suerte del principiante..."

        elif MShooter_target_05 == 2:

            p "??No dec??as que era la suerte del principiante?"

            rat "A veces esa suerte se alarga un par de veces..."

            p "Ya..."

        elif MShooter_target_05 == 3:

            rat "..."

            p "Te veo muy calladito..."

            rat "Bah..."

            rat "Acertar tres veces tampoco es ninguna proeza..."

            ne "Como si t?? lo consiguieras a menudo..."

            rat "..."

            if MShooter_fired == 5:

                rat "L??stima que no te queden m??s tiros para demostrar que ha sido simple suerte..."

                ne "La que a ti te falt?? en tu primera vez,"

                ne "que no acertaste ni una."

                ne "A eso te refieres,"

                ne "??no?"

                extend " Rata."

                rat "..."

            else:

                rat "Pero seguro que no aciertas el centro de la diana otra vez."

        elif MShooter_target_05 == 4:

            rat "..."

            p "Mucha suerte del principiante me parece a m??..."

            if MShooter_fired == 4:

                p "Cuatro dianas de cuatro tiros."

                p "Y a??n me queda otro."

                rat "No creo que seas capaz de darle al centro otra vez."

            else:

                rat "Qu?? l??stima que te ya no te queden m??s tiros para conseguir un pleno."

                ne "Rata,"

                ne "t?? nunca has conseguido hacer cuatro seguidos al centro,"

                ne "as?? que no te tires tantas flores..."

                rat "..."

        elif MShooter_target_05 == 5:

            p "Perdona..."

            p "No recuerdo muy bien qu?? hab??as dicho antes..."

            p "Algo sobre que no ser??a capaz..."

            p "??Verdad?"

            rat "..."

            ne "Debes admitir que nunca has pasado de tres tiros seguidos al centro Rata."

            ne "Ha conseguido mejor resultado que t?? a la primera,"

            ne "cuando t?? llevas a??os intent??ndolo."

            p "Es bastante pat??tico que no hayas logrado algo tan f??cil..."

            ne "Tampoco te pases con ??l [protname]..."

            rat "??Seguro que has hecho trampas!"

            p "??Haciendo qu???"

            p "??Magia vud???"

            if (PlatinumHelp) == True:

                rat "Seguro que has usado la rueda del rat??n cuando has fallado para volverlo a intentar."

                ne "??C??mo dices?"

                rat "Nada,"

                extend " nada..."

                p "..."

            ne "No seas tan mal perdedor, Rata,"

            ne "admite que ha conseguido un pleno en su primer intento."

            rat "..."

    elif (position_shooter_target.xpos in range (440, 480)) or (position_shooter_target.xpos in range (320, 360)): # 4 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_04 += 1
        $ MShooter_points += 4
        pt "Rojo."

        extend " Cuatro puntos."

        if MShooter_target_04 == 1:

            ne "??No est?? mal [protname]!"

            ne "Casi le das al centro."

        elif MShooter_target_04 == 2:

            ne "??Otra vez casi rozas el centro!"

            ne "??A ver c??mo te va el siguiente tiro!"

        elif MShooter_target_04 == 3:

            ne "??Muy bien!"

            ne "??Por poco rozas el amarillo!"

        elif MShooter_target_04 == 4:

            ne "Cuatro veces en el rojo."

            ne "??No est?? mal!"

        elif MShooter_target_04 == 5:

            ne "??Has conseguido un buen resultado!"

            rat "No le ha dado ni una sola vez al centro."

            ne "Ni t?? tampoco lo hiciste en tu primera vez."

            rat "..."

            ne "Y ha conseguido bastantes m??s puntos que los que lograste t?? en aquel entonces."

            rat "..."

            ne "Adem??s no es nada f??cil disparar cinco veces al mismo color."

            rat "Eso es porque quer??a darle al amarillo y ha fallado en todos sus tiros."

            ne "????Quieres dejar de ser tan negativo, Rata?!"

            rat "..."
        

    elif (position_shooter_target.xpos in range (480, 520)) or (position_shooter_target.xpos in range (280, 320)): # 3 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_03 += 1
        $ MShooter_points += 3
        pt "Azul."

        extend " Tres puntos."

        if MShooter_target_03 == 1:

            if MShooter_fired < 5:

                ne "La pr??xima la har??s mejor,"

                ne "ya lo ver??s."

            else:

                ne "??Casi!"

        else:

            rat "??Ja!"

        if MShooter_target_03 == 2:

            rat "El tiro ha sido bastante mediocre,"

            rat "debes admitirlo."

            ne "Como si t?? fueras mucho mejor."

            rat "..."

        elif MShooter_target_03 == 3:

            rat "Como para confiar en ??l para traernos el fruto de su caza."

            ne "Ni que estuvi??ramos viviendo en el siglo XV, Rata."

            rat "..."

        elif MShooter_target_03 == 4:

            rat "Es la cuarta vez que dispara tan lejos del centro."

            rat "Hasta yo lo hice mejor mi primera vez."

            ne "Veo que no te acuerdas muy bien de tu primera vez..."

            rat "..."

            pt "??Siguen hablando de disparar con la escopeta,"

            pt "o de otra cosa?"

        if MShooter_fired < 5:

            ne "Sigue intent??ndolo [protname]."

        if MShooter_target_03 == 5:

            ne "Los cinco tiros casi en el centro de la diana."

            ne "??Nada mal para tu primera vez, [protname]!"

            rat "Bah..."

            rat "No le ha dado ni una sola vez al centro."

            ne "Ni t?? tampoco lo hiciste en tu primera vez,"

            ne "adem??s ha conseguido m??s puntos que los que tu obtuviste en aquel entonces."

            rat "Pero ahora lo hago mucho mejor..."

            ne "No demasiado m??s."

            rat "Qu?? cruel que eres conmigo cuando est??s con ??l, cari??o..."

            ne "Eres t?? que no dejas meterte con ??l todo el rato."

            rat "..."

    elif (position_shooter_target.xpos in range (520, 560)) or (position_shooter_target.xpos in range (240, 280)): # 2 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_02 += 1
        $ MShooter_points += 2
        pt "Negro..."

        extend " Solo dos puntos."

        if MShooter_target_02 == 1:

            rat "Quiz??s tengas m??s suerte en el siguiente tiro,"

            rat "??no?"

            if MShooter_fired == 5:

                rat "Ah..."

                extend " no..."

                rat "espera..."

                rat "que no te quedan m??s..."

                pt "Puto gordo seboso..."

            else:

                rat "O quiz??s no..."

                rat "Jajaja"

        elif MShooter_target_02 == 2:

            rat "Un poco lejos del centro,"

            rat "??no te parece?"

            p "..."

        elif MShooter_target_02 == 3:

            rat "??Quieres que te traiga una diana m??s grande?"

            rat "O quiz??s prefieras que haga el c??rculo amarillo m??s ancho,"

            rat "As?? seguro que le dar??as al centro..."

            p "..."

            rat "Jajaja"

            ne "??Rata!"

            rat "Vale,"

            extend " vale," 

            rat "ya me callo."

        elif MShooter_target_02 == 4:

            rat "Cuatro veces en el mismo c??rculo..."

            rat "L??stima que no sea al que debas apuntar..."

            rat "??Verdad?"

            ra "Jajaja"

            ne "Como si t?? fueras mucho mejor..."

            rat "..."

        elif MShooter_target_02 == 5:

            rat "Ni siquiera has tocado al azul,"

            rat "como para acercarte al centro de la diana."

            ne "Debes admitir, por eso,"

            ne "que darle las cinco veces al mismo color tampoco es tarea f??cil."

            rat "Bah..."

            rat "En su caso es pura chiripa,"

            rat "adem??s el objetivo era darle al medio..."

            rat "as?? que muy bueno no es el chico."

            ne "Ni que t?? fueras {a=https://es.wikipedia.org/wiki/Legolas}Legolas{/a}..."

            rat "..."


    elif (position_shooter_target.xpos in range (560, 600)) or (position_shooter_target.xpos in range (200, 240)): # 1 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_01 += 1
        $ MShooter_points += 1
        pt "Blanco..."

        extend " Solo un punto..."

        if MShooter_target_01 == 1:

            pt "??Tan malo soy?"

            pt "Al menos no le he dado a la pared..."

            rat "Suerte que no dependes de este mozo para sobrevivir cazando con la escopeta."

            rat "Seguramente morir??as de hambre."

            ne "Como contigo..."

            ne "??No es as???"

            ne "Incluso despu??s de a??os jugando a esto,"

            ne "apenas sueles lograr tocar la diana, Rata."

            rat "Eso es porque siempre me pillas algo ebrio cuando lo hago..."

            ne "??Y cu??ndo no lo est??s?"

            ne "Si te pasas el d??a bebiendo."

            rat "..."

        else:

            pt "????Otra vez?!"

            rat "??Jajaja!"

        if MShooter_target_01 == 2:

            rat "Desde luego,"

            rat "la escopeta no es lo tuyo, chico."

            if MShooter_target_05 > 1:

                ne "Pero al menos ha dado en el centro de la diana [MShooter_target_05] veces."

                ne "Que yo recuerde,"

                ne "en tu primera vez ni lo rozaste una sola vez."

                ne "As?? que baja esos humos, Rata."

                rat "..."

                pt "Puto gordo..."

        elif MShooter_target_01 == 3:

            rat "Quiz??s en el siguiente tiro tengas m??s suerte,"

            rat "y le des a la pared."

            ne "Como hiciste t?? en tu primera vez,"

            ne "??no?"

            rat "..."

        elif MShooter_target_01 == 4:

            rat "Pensaba que no habr??a nadie peor que yo con la escopeta..."

            p "..."

            rat "??Pero por lo visto me equivoqu??!"

            ne "..."

            if MShooter_fired == 5:

                ne "No le hagas caso [protname],"

                if MShooter_target_05 == 1:

                    ne "le has dado en el centro de la diana al menos una vez."

                    ne "Algo que Rata no consigui?? en su primer intento."

                if MShooter_target_00 < 1:

                    ne "Al menos no has disparado ninguna vez fuera de la diana."

                    ne "Algo que Rata s?? hizo."

                else:

                    ne "Era tu primera vez,"

                    ne "es normal que no fuera algo f??cil."

                    if night05_Park_MinigameShooter_HowGood_NotGood == True:

                        p "Te dije que no era muy bueno en esto..."

                        ne "No seas rid??culo,"

                        ne "lo has hecho muy bien."

                    rat "??Ni yo fui tan malo mi primera vez!"

                    ne "????QUIERES CALLARTE DE UNA VEZ RATA?!"

                    ne "??He sido yo quien le ha forzado a intentarlo,"

                    ne "as?? que no le pinches m??s!"

                rat "..."


        elif MShooter_target_01 == 5:

            rat "Los cinco tiros en la peor anilla..."

            rat "Por poco casi tocas la pared en lugar de la tabla."

            p "..."

            rat "Por lo menos se puede decir que le has dado al blanco en todos los disparos..."

            rat "Jajaja"

            ne "??Rata!"

            ne "??Te recuerdo que en tu primera vez tambi??n sacaste un resultado horrible!"

            rat "Pero fue mejor que esto."

            ne "Al menos ??l no ha disparado fuera de la diana ni una sola vez."

            rat "..."
            
    else:
        $ MShooter_target_00 += 1
        call p_Help

        if MShooter_target_00 == 1:

            pt "??Mierda!"

            pt "??No le he dado ni a la diana!"

            rat "??Jajaja!"

            rat "??Eres m??s malo que mi abuelo el tuerto pata de palo!"

            p "..."

            ne "??Rata!"

            rat "??Qu???"

            rat "Es verdad..."

        else:

            pt "????Otra vez?!"

            rat "??Jajaja!"

        if MShooter_target_00 == 2:

            rat "??Ni estando ciego como una almeja apunto tan mal!"

            ne "Cuando est??s ebrio no te aguantas ni en pie,"

            ne "as?? que mucho menos eres capaz de aguantar una escopeta."

            rat "..."

            ne "Menos humos, Rata."

            rat "C??mo te pones cari??o..."

            pt "????Por qu?? demonios la llama cari??o?!"

        elif MShooter_target_00 == 3:

            rat "??Ni en las {a=https://es.wikipedia.org/wiki/Stormtrooper}tropas de asalto de Star wars{/a} son tan malos!"

            p "..."

        elif MShooter_target_00 == 4:

            rat "??Te dejo entrar?"

            rat "A ver si de m??s cerca apuntas mejor."

            p "..."

        elif MShooter_target_00 == 5:

            rat "??Ni un solo tiro en toda la diana!"

            rat "??No ser?? porque no es suficientemente grande!"

            p "..."

            rat "Hijo,"

            rat "??quieres que llame a un m??dico?"

            rat "Lo tuyo no es normal..."

            p "No me llames hijo."

            ne "Un poco de raz??n tiene..."

            ne "??Est??s seguro de que te encuentras bien, [protname]?"

            ne "Parece como si lo hubieras hecho aposta..."

            pt "??Solo lo parece?"

    ###############

    if MShooter_fired >= 5:

        pt "Este ha sido mi [MShooter_fired]?? y ??ltimo disparo."

        pt "He conseguido [MShooter_points] puntos de 25."

        return

    else:

        pt "Llevo [MShooter_points] puntos de 25,"

        if MShooter_fired == 1:

            pt "y me quedan 4 tiros."

        elif MShooter_fired == 2:

            pt "y me quedan 3 tiros."

        elif MShooter_fired == 3:

            pt "y me quedan 2 tiros."

        elif MShooter_fired == 4:

            pt "y me queda 1 tiro."

        pt "Probemos de nuevo."

        call night05_Park_MinigameShooter_Game
    
    return