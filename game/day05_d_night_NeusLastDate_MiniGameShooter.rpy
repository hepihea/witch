
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

    rat "La mecánica es muy simple,"

    rat "Tenéis {b}cinco{/b} tiros."

    rat "Cuanto más cerca disparéis del {b}centro de la diana{/b},"

    rat "más puntos tendréis."

    rat "El centro amarillo vale cinco,"

    rat "cada anillo que se aleja es {b}un punto menos{/b}."

    rat "Así que se puede ganar hasta un máximo de {b}veinticinco{/b} puntos."

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

    pt "ahí vamos."

    call night05_Park_MinigameShooter_Game

    jump night05_Park_MinigameShooter_Finished

    # MINIJUEGO? ESPERO QUE NO MUY COMPLICADO...

    # Premios: Un globo, un peluche de una rana, de un mono, una pulsera de tela o de metal, según los puntos.

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
    #with vpunch # If used, time doesn´t work.
    $ MShooter_fired += 1

    #if 0.45 <= position_shooter_target.xpos <= 0.55: # CENTER 5 POINTS # With Float numbers.
    if position_shooter_target.xpos in range (360, 440): # CENTER 5 POINTS
        call p_Help
        with vpunch
        $ MShooter_target_05 += 1
        $ MShooter_points += 5
        pt "¡Amarillo!"

        extend " ¡Cinco puntos!"

        if MShooter_target_05 == 1:

            ne "¡Muy bien [protname]!"

            if MShooter_fired == 1:

                ne "¡El centro de la diana a la primera!"

            rat "¡Bah!"

            rat "La suerte del principiante..."

        elif MShooter_target_05 == 2:

            p "¿No decías que era la suerte del principiante?"

            rat "A veces esa suerte se alarga un par de veces..."

            p "Ya..."

        elif MShooter_target_05 == 3:

            rat "..."

            p "Te veo muy calladito..."

            rat "Bah..."

            rat "Acertar tres veces tampoco es ninguna proeza..."

            ne "Como si tú lo consiguieras a menudo..."

            rat "..."

            if MShooter_fired == 5:

                rat "Lástima que no te queden más tiros para demostrar que ha sido simple suerte..."

                ne "La que a ti te faltó en tu primera vez,"

                ne "que no acertaste ni una."

                ne "A eso te refieres,"

                ne "¿no?"

                extend " Rata."

                rat "..."

            else:

                rat "Pero seguro que no aciertas el centro de la diana otra vez."

        elif MShooter_target_05 == 4:

            rat "..."

            p "Mucha suerte del principiante me parece a mí..."

            if MShooter_fired == 4:

                p "Cuatro dianas de cuatro tiros."

                p "Y aún me queda otro."

                rat "No creo que seas capaz de darle al centro otra vez."

            else:

                rat "Qué lástima que te ya no te queden más tiros para conseguir un pleno."

                ne "Rata,"

                ne "tú nunca has conseguido hacer cuatro seguidos al centro,"

                ne "así que no te tires tantas flores..."

                rat "..."

        elif MShooter_target_05 == 5:

            p "Perdona..."

            p "No recuerdo muy bien qué habías dicho antes..."

            p "Algo sobre que no sería capaz..."

            p "¿Verdad?"

            rat "..."

            ne "Debes admitir que nunca has pasado de tres tiros seguidos al centro Rata."

            ne "Ha conseguido mejor resultado que tú a la primera,"

            ne "cuando tú llevas años intentándolo."

            p "Es bastante patético que no hayas logrado algo tan fácil..."

            ne "Tampoco te pases con él [protname]..."

            rat "¡Seguro que has hecho trampas!"

            p "¿Haciendo qué?"

            p "¿Magia vudú?"

            if (PlatinumHelp) == True:

                rat "Seguro que has usado la rueda del ratón cuando has fallado para volverlo a intentar."

                ne "¿Cómo dices?"

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

            ne "¡No está mal [protname]!"

            ne "Casi le das al centro."

        elif MShooter_target_04 == 2:

            ne "¡Otra vez casi rozas el centro!"

            ne "¡A ver cómo te va el siguiente tiro!"

        elif MShooter_target_04 == 3:

            ne "¡Muy bien!"

            ne "¡Por poco rozas el amarillo!"

        elif MShooter_target_04 == 4:

            ne "Cuatro veces en el rojo."

            ne "¡No está mal!"

        elif MShooter_target_04 == 5:

            ne "¡Has conseguido un buen resultado!"

            rat "No le ha dado ni una sola vez al centro."

            ne "Ni tú tampoco lo hiciste en tu primera vez."

            rat "..."

            ne "Y ha conseguido bastantes más puntos que los que lograste tú en aquel entonces."

            rat "..."

            ne "Además no es nada fácil disparar cinco veces al mismo color."

            rat "Eso es porque quería darle al amarillo y ha fallado en todos sus tiros."

            ne "¡¿Quieres dejar de ser tan negativo, Rata?!"

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

                ne "La próxima la harás mejor,"

                ne "ya lo verás."

            else:

                ne "¡Casi!"

        else:

            rat "¡Ja!"

        if MShooter_target_03 == 2:

            rat "El tiro ha sido bastante mediocre,"

            rat "debes admitirlo."

            ne "Como si tú fueras mucho mejor."

            rat "..."

        elif MShooter_target_03 == 3:

            rat "Como para confiar en él para traernos el fruto de su caza."

            ne "Ni que estuviéramos viviendo en el siglo XV, Rata."

            rat "..."

        elif MShooter_target_03 == 4:

            rat "Es la cuarta vez que dispara tan lejos del centro."

            rat "Hasta yo lo hice mejor mi primera vez."

            ne "Veo que no te acuerdas muy bien de tu primera vez..."

            rat "..."

            pt "¿Siguen hablando de disparar con la escopeta,"

            pt "o de otra cosa?"

        if MShooter_fired < 5:

            ne "Sigue intentándolo [protname]."

        if MShooter_target_03 == 5:

            ne "Los cinco tiros casi en el centro de la diana."

            ne "¡Nada mal para tu primera vez, [protname]!"

            rat "Bah..."

            rat "No le ha dado ni una sola vez al centro."

            ne "Ni tú tampoco lo hiciste en tu primera vez,"

            ne "además ha conseguido más puntos que los que tu obtuviste en aquel entonces."

            rat "Pero ahora lo hago mucho mejor..."

            ne "No demasiado más."

            rat "Qué cruel que eres conmigo cuando estás con él, cariño..."

            ne "Eres tú que no dejas meterte con él todo el rato."

            rat "..."

    elif (position_shooter_target.xpos in range (520, 560)) or (position_shooter_target.xpos in range (240, 280)): # 2 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_02 += 1
        $ MShooter_points += 2
        pt "Negro..."

        extend " Solo dos puntos."

        if MShooter_target_02 == 1:

            rat "Quizás tengas más suerte en el siguiente tiro,"

            rat "¿no?"

            if MShooter_fired == 5:

                rat "Ah..."

                extend " no..."

                rat "espera..."

                rat "que no te quedan más..."

                pt "Puto gordo seboso..."

            else:

                rat "O quizás no..."

                rat "Jajaja"

        elif MShooter_target_02 == 2:

            rat "Un poco lejos del centro,"

            rat "¿no te parece?"

            p "..."

        elif MShooter_target_02 == 3:

            rat "¿Quieres que te traiga una diana más grande?"

            rat "O quizás prefieras que haga el círculo amarillo más ancho,"

            rat "Así seguro que le darías al centro..."

            p "..."

            rat "Jajaja"

            ne "¡Rata!"

            rat "Vale,"

            extend " vale," 

            rat "ya me callo."

        elif MShooter_target_02 == 4:

            rat "Cuatro veces en el mismo círculo..."

            rat "Lástima que no sea al que debas apuntar..."

            rat "¿Verdad?"

            ra "Jajaja"

            ne "Como si tú fueras mucho mejor..."

            rat "..."

        elif MShooter_target_02 == 5:

            rat "Ni siquiera has tocado al azul,"

            rat "como para acercarte al centro de la diana."

            ne "Debes admitir, por eso,"

            ne "que darle las cinco veces al mismo color tampoco es tarea fácil."

            rat "Bah..."

            rat "En su caso es pura chiripa,"

            rat "además el objetivo era darle al medio..."

            rat "así que muy bueno no es el chico."

            ne "Ni que tú fueras {a=https://es.wikipedia.org/wiki/Legolas}Legolas{/a}..."

            rat "..."


    elif (position_shooter_target.xpos in range (560, 600)) or (position_shooter_target.xpos in range (200, 240)): # 1 POINTS
        with vpunch
        call p_Help
        $ MShooter_target_01 += 1
        $ MShooter_points += 1
        pt "Blanco..."

        extend " Solo un punto..."

        if MShooter_target_01 == 1:

            pt "¿Tan malo soy?"

            pt "Al menos no le he dado a la pared..."

            rat "Suerte que no dependes de este mozo para sobrevivir cazando con la escopeta."

            rat "Seguramente morirías de hambre."

            ne "Como contigo..."

            ne "¿No es así?"

            ne "Incluso después de años jugando a esto,"

            ne "apenas sueles lograr tocar la diana, Rata."

            rat "Eso es porque siempre me pillas algo ebrio cuando lo hago..."

            ne "¿Y cuándo no lo estás?"

            ne "Si te pasas el día bebiendo."

            rat "..."

        else:

            pt "¡¿Otra vez?!"

            rat "¡Jajaja!"

        if MShooter_target_01 == 2:

            rat "Desde luego,"

            rat "la escopeta no es lo tuyo, chico."

            if MShooter_target_05 > 1:

                ne "Pero al menos ha dado en el centro de la diana [MShooter_target_05] veces."

                ne "Que yo recuerde,"

                ne "en tu primera vez ni lo rozaste una sola vez."

                ne "Así que baja esos humos, Rata."

                rat "..."

                pt "Puto gordo..."

        elif MShooter_target_01 == 3:

            rat "Quizás en el siguiente tiro tengas más suerte,"

            rat "y le des a la pared."

            ne "Como hiciste tú en tu primera vez,"

            ne "¿no?"

            rat "..."

        elif MShooter_target_01 == 4:

            rat "Pensaba que no habría nadie peor que yo con la escopeta..."

            p "..."

            rat "¡Pero por lo visto me equivoqué!"

            ne "..."

            if MShooter_fired == 5:

                ne "No le hagas caso [protname],"

                if MShooter_target_05 == 1:

                    ne "le has dado en el centro de la diana al menos una vez."

                    ne "Algo que Rata no consiguió en su primer intento."

                if MShooter_target_00 < 1:

                    ne "Al menos no has disparado ninguna vez fuera de la diana."

                    ne "Algo que Rata sí hizo."

                else:

                    ne "Era tu primera vez,"

                    ne "es normal que no fuera algo fácil."

                    if night05_Park_MinigameShooter_HowGood_NotGood == True:

                        p "Te dije que no era muy bueno en esto..."

                        ne "No seas ridículo,"

                        ne "lo has hecho muy bien."

                    rat "¡Ni yo fui tan malo mi primera vez!"

                    ne "¡¿QUIERES CALLARTE DE UNA VEZ RATA?!"

                    ne "¡He sido yo quien le ha forzado a intentarlo,"

                    ne "así que no le pinches más!"

                rat "..."


        elif MShooter_target_01 == 5:

            rat "Los cinco tiros en la peor anilla..."

            rat "Por poco casi tocas la pared en lugar de la tabla."

            p "..."

            rat "Por lo menos se puede decir que le has dado al blanco en todos los disparos..."

            rat "Jajaja"

            ne "¡Rata!"

            ne "¡Te recuerdo que en tu primera vez también sacaste un resultado horrible!"

            rat "Pero fue mejor que esto."

            ne "Al menos él no ha disparado fuera de la diana ni una sola vez."

            rat "..."
            
    else:
        $ MShooter_target_00 += 1
        call p_Help

        if MShooter_target_00 == 1:

            pt "¡Mierda!"

            pt "¡No le he dado ni a la diana!"

            rat "¡Jajaja!"

            rat "¡Eres más malo que mi abuelo el tuerto pata de palo!"

            p "..."

            ne "¡Rata!"

            rat "¿Qué?"

            rat "Es verdad..."

        else:

            pt "¡¿Otra vez?!"

            rat "¡Jajaja!"

        if MShooter_target_00 == 2:

            rat "¡Ni estando ciego como una almeja apunto tan mal!"

            ne "Cuando estás ebrio no te aguantas ni en pie,"

            ne "así que mucho menos eres capaz de aguantar una escopeta."

            rat "..."

            ne "Menos humos, Rata."

            rat "Cómo te pones cariño..."

            pt "¡¿Por qué demonios la llama cariño?!"

        elif MShooter_target_00 == 3:

            rat "¡Ni en las {a=https://es.wikipedia.org/wiki/Stormtrooper}tropas de asalto de Star wars{/a} son tan malos!"

            p "..."

        elif MShooter_target_00 == 4:

            rat "¿Te dejo entrar?"

            rat "A ver si de más cerca apuntas mejor."

            p "..."

        elif MShooter_target_00 == 5:

            rat "¡Ni un solo tiro en toda la diana!"

            rat "¡No será porque no es suficientemente grande!"

            p "..."

            rat "Hijo,"

            rat "¿quieres que llame a un médico?"

            rat "Lo tuyo no es normal..."

            p "No me llames hijo."

            ne "Un poco de razón tiene..."

            ne "¿Estás seguro de que te encuentras bien, [protname]?"

            ne "Parece como si lo hubieras hecho aposta..."

            pt "¿Solo lo parece?"

    ###############

    if MShooter_fired >= 5:

        pt "Este ha sido mi [MShooter_fired]º y último disparo."

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