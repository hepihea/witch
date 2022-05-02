
default sexbattle_Skipping_cheated = False

# Esto es el mini-juego con Dídac.

# Tu objetivo es lograr que tenga cuantos más orgasmos mejor antes de que tú llegues a tener tres.

# Si logras que tenga cuatro o más antes de usar el último condón, hay un final distinto.4


image sexbattletutorial A001 = "images/sexbattle/tutorial/A001.webp"
image sexbattletutorial A002 = "images/sexbattle/tutorial/A002.webp"
image sexbattletutorial A003 = "images/sexbattle/tutorial/A003.webp"
image sexbattletutorial A004 = "images/sexbattle/tutorial/A004.webp"
image sexbattletutorial A005 = "images/sexbattle/tutorial/A005.webp"
image sexbattletutorial A006 = "images/sexbattle/tutorial/A006.webp"
image sexbattletutorial A007 = "images/sexbattle/tutorial/A007.webp"
image sexbattletutorial A008 = "images/sexbattle/tutorial/A008.webp"
image sexbattletutorial A009 = "images/sexbattle/tutorial/A009.webp"

image sexbattletutorial B000 = "images/sexbattle/tutorial/B000.webp"
image sexbattletutorial B001 = "images/sexbattle/tutorial/B001.webp"
image sexbattletutorial B002 = "images/sexbattle/tutorial/B002.webp"
image sexbattletutorial B003 = "images/sexbattle/tutorial/B003.webp"
image sexbattletutorial B004 = "images/sexbattle/tutorial/B004.webp"
image sexbattletutorial B005 = "images/sexbattle/tutorial/B005.webp"
image sexbattletutorial B006 = "images/sexbattle/tutorial/B006.webp"
image sexbattletutorial B007 = "images/sexbattle/tutorial/B007.webp"

style sexbattle_tutorial_typo:

    font "fonts/chinrg__.ttf"
    outlines [ (5, "#000", 0, 0) ]
    #drop_shadow (2,2)
    size 20

screen tutorial_B001:

    modal False
    add "sexbattletutorial B001"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 495 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("{size=27}Este es {color=#399}tu estado{/color}.{/size}\n\n{image=icon_pleasure_you} {size=15}{color=#399}PLACER{/color}:{/size} Cómo de cerca estás de correrte*.\n\n{image=icon_orgasm_you} {size=15}{color=#399}CORRIDAS{/color}:{/size} (3 es tu límite).")):
                    style "sexbattle_tutorial_typo"

        vbox:

            yanchor -6.0

            text (_("* {size=15}La barra y el límite incrementa.\n   1º orgasmo = 50   2º= 100    3º o += 150{/size}")):
                style "sexbattle_tutorial_typo"

screen tutorial_B002:

    modal False
    add "sexbattletutorial B002"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 495 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("{size=27}Este es {color=#c63}su estado{/color}.{/size}\n\n{image=icon_pleasure_didac} {size=15}{color=#c63}PLACER{/color}:{/size} Cómo de cerca está de correrse*.\n\n{image=icon_enslavery_didac} {size=15}{color=#c63}LUJURIA{/color}:{/size} Cómo de dócil es.\n   {size=15}Después de cada 10 puntos, baja un punto la dificultad.{/size}\n\n{image=icon_orgasm_didac} {size=15}{color=#c63}CORRIDAS{/color}:{/size} sin límite.")):
                    style "sexbattle_tutorial_typo"

        vbox:

            yanchor -6.0

            text (_("* {size=15}La barra y el límite incrementa.\n   1º orgasmo = 50   2º= 100    3º o += 150{/size}")):
                style "sexbattle_tutorial_typo"


screen tutorial_B003:

    #tag menu
    modal False
    add "sexbattletutorial B003"

    #add "icon_pleasure_you":
        #yalign 0.5
        #xalign 0.5

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 490 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True
            #yalign 0.0
            #xalign 0.0
            #spacing 8

            vbox:
                
                text (_("{size=27}Estos son {color=#399}tus DADOS{/color}.{/size}\n\n\n{size=27}Esta es la {color=#399}ACCIÓN{/color} que estás haciendo.{/size}\n\n\n{size=27}Esta es la {color=#399}DIFICULTAD{/color} de la acción{/size}.\n{size=15}Esta varía según varios factores.{/size}\n\n   {size=15}No es lo mismo acariciar su {color=#c63}clitoris{/color},\n   que besarla en la {color=#c63}boca{/color} (Lo odia).\n\n   Especialmente si su {color=#c63}LUJURIA{/color} {image=icon_enslavery_didac} es baja.{/size}")):
                    style "sexbattle_tutorial_typo"

            #null height 80

screen tutorial_B004:

    modal False
    add "sexbattletutorial B004"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 490 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("{size=15}Como {color=#399}uno de los dados{/color} está por encima de la dificultad,{/size}\n{size=27}És un {color=#0c0}SUCCESS{/color}{/size}.\n\n\nLa dificultad es {color=#399}7{/color};\n{size=15}Si en lugar de obtener como resultado un {color=#399}10&5{/color},\nse hubiera obtenido un {color=#399}6&5{/color},{/size}\nhubiera sido un {color=#F00}FAIL{/color}.\n\nSi cometes más de 3 {color=#F00}FAILS{/size} en la misma acción,\n{size=27}{color=#c63}Dídac{/color} puede {color=#c63}violarte{/color}.{/size}")):
                    style "sexbattle_tutorial_typo"

screen tutorial_B005:

    modal False
    add "sexbattletutorial B005"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 490 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("{size=27}Estos son sus {color=#c63}DADOS{/color}.{/size}\n\n{size=27}Si está tirando los dados.{/size} {size=15}(en proceso){/size}\n\n{size=27}Esto muestra la {color=#c63}DIFICULTAD{/color} de la acción.{/size}\nEsta varía según la situación.\n\n{color=#c63}No puede tirar los dados{/color},\na menos que haya cometido más de 3 {color=#f00}FAILS{/color},\no hayas tenido más de 6 {color=#0c0}SUCCESS{/color} (misma acción).")):
                    style "sexbattle_tutorial_typo"

screen tutorial_B006:

    modal False
    add "sexbattletutorial B006"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 490 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("{size=15}---EJEMPLO---{/size}\n\nEn este caso, le he abofeteado el pecho {color=#0c0}satisfactoriamente{/color} {color=#399}más de 6 veces{/color}, así que {color=#c63}ha hecho la tirada{/color}.\n{size=15}(ya que se ha cansado de que hiciera tantas veces lo mismo).{/size}\n\n{size=15}{color=#c63}Su dificultad{/color} era {color=#c63}5{/color},\nal menos uno de sus dados estaba por encima de este número,{/size}\nasí que también ha sido {color=#0c0}SUCCESS{/color}.\n\n{size=15}{color=#399}Has conseguido un resultado{/color} {color=#0c0}satisfactorio{/color}, pero cansada de tu repetida acción, como ha conseguido también un éxito,{/size}\n{color=#c63}te violará{/color} de todos modos.")):
                    style "sexbattle_tutorial_typo"

screen tutorial_B007:

    modal False
    add "sexbattletutorial B007"

    frame:
        background None
        xanchor -0.15 #Position of the frame
        yanchor -0.085
        xsize 490 #Size of the Frame
        ysize 650

        hbox:

            box_wrap True

            vbox:
                
                text (_("Estos aparecen cuando los puntos han {color=#0c0}aumentado{/color} o {color=#f00}disminuido{/color}.")):
                    style "sexbattle_tutorial_typo"

                text (_("\n\n\n              Exit")):
                    style "sexbattle_tutorial_typo"

                text (_("\nCon esto, abandonas el {color=#969}mini-juego{/color}, dejando a {color=#c63}Dídac{/color} a medias y cabreada.")):
                    style "sexbattle_tutorial_typo"

                text (_("\n\n              Ocultar               Mostrar")):
                    style "sexbattle_tutorial_typo"

                text (_("\nEsto debería ocultar el {color=#969}Tablero-Premium{/color}, por ahora solo lo hace semi-invisible.")):
                    style "sexbattle_tutorial_typo"

        vbox:
            yanchor -1.8

            text (_(" {image=but_exit_idle}"))

        vbox:
            yanchor -4.3

            text (_(" {image=but_eye_hide_idle}       {image=but_eye_show_idle}"))


##########################################################################################################
#########################################################################################################
########################################################################################################
#######################################################################################################

label sexbattle_tutorial_question:

    if PlatinumHelp:

        menu sexbattle_tutorial_question_b:

            aj "¿Quieres ver el tutorial del {color=#969}mini-juego{/color} con {color=#c63}Dídac{/color}?"

            "Sí":
                
                call p_Help
                        
                jump sexbattle_tutorial_start

            "No":

                return

    return


label sexbattle_tutorial_start:

    scene black
    with fade


    aj "Lo que te pide {color=#c63}Dídac{/color},"

    extend " es que le consigas tantos {color=#c63}orgasmos{/color} cómo puedas antes de llegar a tu {color=#399}límite{/color},"

    extend " 3 orgasmos."

    aj "El primer orgasmo,"

    extend " (para ambos),"

    extend " es mucho más rápido que el segundo,"

    aj "y el segundo es algo más rápido de conseguir que el tercero."

    aj "{color=#c63}Dídac{/color} puede tener un número infinito de orgasmos,"

    aj "pero no va a ser tan fácil a partir del tercero."

    
    ##

    scene sexbattletutorial A001
    with fade

    aj "La acción empieza teniendo a {color=#c63}Dídac{/color} encima de ti."

    aj "En esta posición siempre tendrá algo de ventaja"

    aj "y dónde más fácilmente podrá cabalgarte contra tu voluntad."

    aj "Para poder cambiar de posición y ponerla a cuatro patas,"

    aj "debes cogerla por el {color=#c63}brazo{/color};"

    aj "aunque no va a ser nada fácil conseguirlo,"

    aj "tendrás que esperar a poder {color=#399}someterla{/color} más a tu voluntad."

    aj "Aunque los {color=#c63}orgasmos{/color} ayudan,"

    aj "no son el único modo de conseguir su sumisión."

    scene sexbattletutorial A007
    with dissolve

    aj "Existe otra posición con dos variantes,"

    extend " dónde consigues someterla con más facilidad"

    scene sexbattletutorial A008
    with dissolve

    aj "y dónde puedes hacer cosas que teniéndola encima no te dejaría."

    aj "pero como puedes ver,"

    extend " aún está en proceso."

    ##

    scene sexbattletutorial A002
    with dissolve

    aj "Existen varios lugares en los que puedes interactuar,"

    aj "simplemente tienes que encontrarlos y hacer {i}clic{/i} en ellos."

    ##
    scene sexbattletutorial A009
    with dissolve

    aj "Este botón en forma de aspa,"

    extend " es algo especial,"

    aj "Te permite apartarte de {color=#c63}ella{/color} y empezar de cero,"

    aj "aunque no es buena idea abusar,"

    extend " porque también se cansará si lo haces."

    scene sexbattletutorial A002
    with dissolve

    aj "Cuando haces {i}clic{/i} en un círculo,"

    extend " puedes encontrar distintas opciones,"

    scene sexbattletutorial A003
    with dissolve

    aj "como el {color=#c63}clítoris{/color},"

    extend " dónde puedes lamérselo {image=but_tongue} o masajearlo {image=but_hand}."

    ##

    scene sexbattletutorial A004
    with dissolve

    aj "El coño y el ano (este último está en proceso),"

    aj "son un tanto especial."

    aj "Especialmente cuando se trata de usar tu enorme polla."

    scene sexbattletutorial A005
    with dissolve

    aj "Aquí puedes controlar cómo de PROFUNDO quieres meterla."

    scene sexbattletutorial A006
    with dissolve

    aj "Aquí puedes controlar cómo de RÁPIDO quieres meterla."

    aj "Ten en cuenta,"

    extend " que por mucho que te lo pida,"

    aj "al principio no te resultará fácil metérsela de golpe"

    extend " y mucho menos hacerlo rápidamente,"

    aj "al mismo tiempo,"

    extend " como más profundo y veloz lo hagas,"

    aj "más rápidamente llegarás al {color=#399}orgasmo{/color}."

    ##

    scene sexbattletutorial A001
    with dissolve

    aj "Si repites tres veces el mismo {color=#f00}error{/color},"

    aj "o si {color=#399}repites demasiadas veces{/color} una misma acción aunque sea de forma {color=#0f0}satisfactoria{/color},"

    aj "{color=#c63}Dídac{/color} se cansará y tomará la iniciativa."

    aj "A medida que avance el {color=#969}mini-juego{/color} se irá poniendo más complicado,"

    aj "así que trata de no hacerla cabrear demasiado"

    aj "y prueba todas las opciones que creas conveniente."

    if Tendolarsversion == True or Platinumversion == True:

        call sexbattle_tutorial_patreon

    aj "Ten en cuenta,"

    extend " como en todo el juego,"

    aj "pero especialmente en este {color=#969}mini-juego{/color},"

    aj "que las decisiones que tomes tendrán sus consecuencias en el futuro."

    if Tendolarsversion == True or Platinumversion == True:

        aj "Siendo {color=#9ab}PLATINUM{/color} o {color=#fa0}PREMIUM{/color},"

        extend " tienes la opción de hacer trampas."

        aj "La {color=#c63}LUJURIA{/color} {image=icon_enslavery_didac},"

        aj "que sirve para que te permita hacer cosas que de otro modo no te dejaría,"

        aj "equivale al número de corazones que tienes con {color=#c63}Dídac{/color}."

        aj "Accede al {color=#fa0}CHEAT MODE{/color},"

        extend " apretando la letra \"C\" de tu teclado,"

        extend " como ya deberías saber..."

        aj "y desde ahí sube sus corazones para que cuando llegue el {color=#969}mini-juego{/color},"

        aj "tengas más facilidad,"

        extend " o si eres muy bruto subiendo el número,"

        aj "puedas hacerle lo que quieras."

        aj "Y por cierto,"

        extend " si quieres un final especial,"

        aj "asegúrate de que {color=#c63}Dídac{/color} haya tenido {color=#c63}como mínimo 4 orgasmos{/color},"

        aj "antes de usar el último {color=#399}preservativo{/color}."

    aj "Espero que esto haya despejado tus posibles dudas y puedas disfrutar del {color=#969}mini-juego{/color}."

    return


    #####
    ####
    ##


label sexbattle_tutorial_patreon:

    # PREMIUM

    scene black
    with fade

    aj "A continuación,"

    extend " el tablero que solo está disponible para los {color=#9ab}PLATINUM{/color} y {color=#fa0}PREMIUM{/color}."

    scene sexbattletutorial B000
    with fade

    aj "Originalmente este tablero lo diseñé para trabajar de forma interna,"

    aj "El {color=#969}mini-juego{/color} está pensado para que puedas darte cuenta,"

    aj "por los diálogos y sus reacciones,"

    extend " si estás haciendo algo {color=0f0}bien{/color} o {color=#f00}mal{/color}."

    aj "Luego pensé que sería una buena idea que los {color=#f63}Patrons{/color} también pudieran acceder a él,"

    aj "aunque entiendo que pueda ser confuso,"

    aj "así que trataré de explicarlo para que sea algo más entendible"

    aj "(especialmente el sistema de dados)."


    show screen tutorial_B001()
    with fade

    pause

    show screen tutorial_B002()
    with dissolve

    pause

    show screen tutorial_B003()
    with dissolve

    pause

    show screen tutorial_B004()
    with dissolve

    pause

    show screen tutorial_B005()
    with dissolve

    pause

    show screen tutorial_B006()
    with dissolve

    pause

    show screen tutorial_B007()
    with dissolve

    pause

    ##

    hide screen tutorial_B001
    hide screen tutorial_B002
    hide screen tutorial_B003
    hide screen tutorial_B004
    hide screen tutorial_B005
    hide screen tutorial_B006
    hide screen tutorial_B007
    scene black
    with fade

    return














##########################################################################################################
#########################################################################################################
########################################################################################################
#######################################################################################################

### To jump the Sex Scene with Didac.

### 5 Orgasmos ha tenido ella.

# mc_body.orgasm = 3

# girl_1.pleasure = 0
# girl_1.enslavement = 250
# girl_1.orgasm = 5


## - Le has metido la polla por el coño hasta el fondo?

    # afternight04_Pussy_dick_deep_Speed_0_Done = 5
    # afternight04_Pussy_dick_deep_Speed_1_Done = 5
    # afternight04_Pussy_dick_deep_Speed_2_Done = 5
    # afternight04_Pussy_dick_deep_Speed_3_Done = 5

    # afternight04_Pussy_dick_deep_Speed_0_Success = 5
    # afternight04_Pussy_dick_deep_Speed_1_Success = 5
    # afternight04_Pussy_dick_deep_Speed_2_Success = 5
    # afternight04_Pussy_dick_deep_Speed_3_Success = 5

## - Le has follado el culo?

    # afternight04_Anal_dick_med_Speed_0_Done = 5
    # afternight04_Anal_dick_med_Speed_1_Done = 5
    # afternight04_Anal_dick_med_Speed_2_Done = 5
    # afternight04_Anal_dick_med_Speed_3_Done = 5

    # afternight04_Anal_dick_med_Speed_0_Success = 5
    # afternight04_Anal_dick_med_Speed_1_Success = 5
    # afternight04_Anal_dick_med_Speed_2_Success = 5
    # afternight04_Anal_dick_med_Speed_3_Success = 5

## - Hasta el fondo y a toda leche?

    # afternight04_Anal_dick_deep_Speed_0_Done = 5
    # afternight04_Anal_dick_deep_Speed_1_Done = 5
    # afternight04_Anal_dick_deep_Speed_2_Done = 5
    # afternight04_Anal_dick_deep_Speed_3_Done = 5

    # afternight04_Anal_dick_deep_Speed_0_Success = 5
    # afternight04_Anal_dick_deep_Speed_1_Success = 5
    # afternight04_Anal_dick_deep_Speed_2_Success = 5
    # afternight04_Anal_dick_deep_Speed_3_Success = 5

## - Le has besado? 

    # afternight04__MMouth_Tongue_Done = 5
    # afternight04__MMouth_Tongue_Deep_Done = 5

        ## - Metiéndole la lengua?

            # afternight04__MMouth_Tongue_Success = 5
            # afternight04__MMouth_Tongue_Deep_Success = 5

## - Le has metido la polla por la boca?

    # afternight04__MMouth_dick_Deep_Done = 5
    # afternight04__MMouth_dick_Deep_Success = 5

        ## - Hasta la garganta?

            # afternight04__MMouth_dick_Done = 5
            # afternight04__MMouth_dick_Success = 5

####

## - Ha tenido 0, 1, 2, 3, 4, 5 o 6 orgasmos?

    # girl_1.orgasm = 6

## - Has hecho que tuviera más de 3 orgasmos antes de usar el último condón? 

        # afternight04_condom_broken = True
        # afternight04_didac_pregnant = True # Didac is pregnant?

    ## - La primera corrida ha sido en el condón, la barriga o en su boca?
    ## - La segunda corrida ha sido en el condón, la barriga o en su boca?

    ## - La tercera corrida ha sido en el condón, la barriga o en su boca?

        # afternight04_CumOnBack = 3
        # afternight04_CumOnStomach = 3
        # afternight04_CumInCondom = 3
        # afternight04_CumInMouth = 3



label sexbattle_Skipping_start:

    stop music fadeout 5.0
    play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0

    scene black
    with fade

    aj "A continuación viene la escena de tener sexo con Dídac."

    aj "Debido a que lo he enfocado más como un \"combate\" que como una simple escena de sexo, he creado en ella un mini-juego."

    aj "El problema es que sigue estando algo incompleto después de más de medio año trabajando en él."

    aj "Así que entendería que quisieras saltártelo, como donador en Patreon, tienes esta opción."


    menu sexbattle_Skipping_question:

        # if PlatinumHelp: ## NOT FINISHED, so not yet available.

        aj "¿Quieres saltarte el {color=#969}mini-juego{/color} con {color=#c63}Dídac{/color}?"

        "Sí":
            
            call p_Help

            $ sexbattle_Skipping_cheated = True
                    
            jump sexbattle_Skipping_questions

        "No":

            return

label sexbattle_Skipping_questions:

    $ afternight04_mc_orgasms = 3
    $ mc_body.orgasm = 3

    # DONE

    $ afternight04__Remove_Done = 5

    $ afternight04__LBoob_Grab_Done = 15
    $ afternight04__LBoob_Slap_Done = 15
    $ afternight04__LButtock_Massage_Done = 15
    $ afternight04__LButtock_Slap_Done = 15
    $ afternight04__LLeg_Massage_Done = 15
    $ afternight04__LNipple_Lick_Done = 15
    $ afternight04__LNipple_Pinch_Done = 15

    $ afternight04__MBelly_Massage_Done = 15
    $ afternight04__MClitoris_Massage_Done = 15
    $ afternight04__MClitoris_Tongue_Done = 15

    $ afternight04__MMouth_Fingers_Done = 15
    $ afternight04__MStomach_Massage_Done = 15

    $ afternight04__Pussy_Fingers_Done = 15
    $ afternight04__Pussy_Tongue_Done = 15 # Cunnilingus

    $ afternight04__RArm_Grab_Done = 15
    $ afternight04__RBoob_Grab_Done = 15
    $ afternight04__RBoob_Slap_Done = 15
    $ afternight04__RButtock_Massage_Done = 15
    $ afternight04__RButtock_Slap_Done = 15
    $ afternight04__RLeg_Massage_Done = 15
    $ afternight04__RNipple_Lick_Done = 15
    $ afternight04__RNipple_Pinch_Done = 15

    $ afternight04__Boob_Grab_Both_Done = 15
    $ afternight04__Boob_Slap_Both_Done = 15
    $ afternight04__Buttock_Massage_Both_Done = 15
    $ afternight04__Buttock_Slap_Both_Done = 15
    $ afternight04__Leg_Massage_Both_Done = 15
    $ afternight04__Nipple_Lick_Both_Done = 15
    $ afternight04__Nipple_Pinch_Both_Done = 15

    # SUCCESS

    $ afternight04__Remove_Success = 5

    $ afternight04__LBoob_Grab_Success = 15
    $ afternight04__LBoob_Slap_Success = 15
    $ afternight04__LButtock_Massage_Success = 15
    $ afternight04__LButtock_Slap_Success = 15
    $ afternight04__LLeg_Massage_Success = 15
    $ afternight04__LNipple_Lick_Success = 15
    $ afternight04__LNipple_Pinch_Success = 15

    $ afternight04__MBelly_Massage_Success = 15
    $ afternight04__MClitoris_Massage_Success = 15
    $ afternight04__MClitoris_Tongue_Success = 15

    $ afternight04__MMouth_Fingers_Success = 15
    $ afternight04__MStomach_Massage_Success = 15

    $ afternight04__Pussy_Fingers_Success = 15
    $ afternight04__Pussy_Tongue_Success = 15 # Cunnilingus

    $ afternight04__RArm_Grab_Success = 15
    $ afternight04__RBoob_Grab_Success = 15
    $ afternight04__RBoob_Slap_Success = 15
    $ afternight04__RButtock_Massage_Success = 15
    $ afternight04__RButtock_Slap_Success = 15
    $ afternight04__RLeg_Massage_Success = 15
    $ afternight04__RNipple_Lick_Success = 15
    $ afternight04__RNipple_Pinch_Success = 15

    $ afternight04__Boob_Grab_Both_Success = 15
    $ afternight04__Boob_Slap_Both_Success = 15
    $ afternight04__Buttock_Massage_Both_Success = 15
    $ afternight04__Buttock_Slap_Both_Success = 15
    $ afternight04__Leg_Massage_Both_Success = 15
    $ afternight04__Nipple_Lick_Both_Success = 15
    $ afternight04__Nipple_Pinch_Both_Success = 15

    # Sex is  NOT by default, Coño!

    # low

    menu sexbattle_Skipping_Q_DidacPussyFuck:

        aj "¿Has penetrado vaginalmente a tu amigo de la infancia?"

        "Sí":

            call p_Help

            $ afternight04_Pussy_dick_low_Speed_0_Done = 10
            $ afternight04_Pussy_dick_low_Speed_1_Done = 10
            $ afternight04_Pussy_dick_low_Speed_2_Done = 10
            $ afternight04_Pussy_dick_low_Speed_3_Done = 10

            $ afternight04_Pussy_dick_low_Speed_0_Success = 10
            $ afternight04_Pussy_dick_low_Speed_1_Success = 10
            $ afternight04_Pussy_dick_low_Speed_2_Success = 10
            $ afternight04_Pussy_dick_low_Speed_3_Success = 10

            # med

            $ afternight04_Pussy_dick_med_Speed_0_Done = 10
            $ afternight04_Pussy_dick_med_Speed_1_Done = 10
            $ afternight04_Pussy_dick_med_Speed_2_Done = 10
            $ afternight04_Pussy_dick_med_Speed_3_Done = 10

            $ afternight04_Pussy_dick_med_Speed_0_Success = 10
            $ afternight04_Pussy_dick_med_Speed_1_Success = 10
            $ afternight04_Pussy_dick_med_Speed_2_Success = 10
            $ afternight04_Pussy_dick_med_Speed_3_Success = 10

        "No":

            call p_Help

    if afternight04_Pussy_dick_med_Speed_2_Success > 3:

        menu sexbattle_Skipping_Q_PussyDeep:

            aj "¿Le has metido la polla por el coño hasta el fondo?"

            "Sí":

                call p_Help

                # deep

                $ afternight04_Pussy_dick_deep_Speed_0_Done = 5
                $ afternight04_Pussy_dick_deep_Speed_1_Done = 5
                $ afternight04_Pussy_dick_deep_Speed_2_Done = 5
                $ afternight04_Pussy_dick_deep_Speed_3_Done = 5

                $ afternight04_Pussy_dick_deep_Speed_0_Success = 5
                $ afternight04_Pussy_dick_deep_Speed_1_Success = 5
                $ afternight04_Pussy_dick_deep_Speed_2_Success = 5
                $ afternight04_Pussy_dick_deep_Speed_3_Success = 5

            "No":

                call p_Help

    if afternight04_Pussy_dick_med_Speed_1_Done > 0:

        menu sexbattle_Skipping_Q_DidacPregnant:

            aj "¿Has conseguido que tuviera más de 3 orgasmos antes de usar el último condón?"

            "Sí":

                call p_Help

                $ afternight04_condom_broken = True
                $ afternight04_didac_pregnant = True # Didac is pregnant
                $ DidacMCPregnant = True
                $ DidacPregnant = True

                $pl.ch_pts("dp", 15) #She Had +4 orgasms. (She´s Pregnant)

            "No":

                call p_Help

        # NOT FINISHED, DEDO POR EL CULO.

        menu sexbattle_Skipping_Q_AnalFinger:

            aj "¿Le has metido el dedo y la lengua por el culo?"

            "Sí":
                call p_Help

                $ afternight04__Anal_Fingers_Done = 5
                $ afternight04__Anal_Fingers_Success = 5

                $ afternight04__Pussy_Tongue_Done = 5
                $ afternight04__Pussy_Tongue_Success = 5

            "No":
                call p_Help

        menu sexbattle_Skipping_Q_Anal:

            aj "¿Le has follado el culo?"

            "Sí":

                call p_Help

                $ afternight04__Anal_dick_low_Done = 5
                $ afternight04__Anal_dick_med_Done = 5
                #afternight04__Anal_dick_out_Done = 5
                #afternight04__Anal_Fingers_Done = 0
                $ afternight04__Anal_Tongue_Done = 5 # Anilingus/ Rim Job


                $ afternight04__Anal_dick_low_Success = 5
                $ afternight04__Anal_dick_med_Success = 5
                #afternight04__Anal_dick_out_Success = 0
                #afternight04__Anal_Fingers_Success = 0
                $ afternight04__Anal_Tongue_Success = 5 # Anilingus/ Rim Job

                $ afternight04_Anal_dick_low_Speed_0_Done = 5
                $ afternight04_Anal_dick_low_Speed_1_Done = 5
                $ afternight04_Anal_dick_low_Speed_2_Done = 5
                $ afternight04_Anal_dick_low_Speed_3_Done = 5

                $ afternight04_Anal_dick_low_Speed_0_Success = 5
                $ afternight04_Anal_dick_low_Speed_1_Success = 5
                $ afternight04_Anal_dick_low_Speed_2_Success = 5
                $ afternight04_Anal_dick_low_Speed_3_Success = 5

                $ afternight04_Anal_dick_med_Speed_0_Done = 5
                $ afternight04_Anal_dick_med_Speed_1_Done = 5
                $ afternight04_Anal_dick_med_Speed_2_Done = 5
                $ afternight04_Anal_dick_med_Speed_3_Done = 5

                $ afternight04_Anal_dick_med_Speed_0_Success = 5
                $ afternight04_Anal_dick_med_Speed_1_Success = 5
                $ afternight04_Anal_dick_med_Speed_2_Success = 5
                $ afternight04_Anal_dick_med_Speed_3_Success = 5

                menu sexbattle_Skipping_Q_AnalDeep:

                    aj "¿Hasta el fondo y a toda leche?"

                    "Sí":

                        call p_Help

                        $ afternight04__Anal_dick_deep_Done = 5 # Anal
                        $ afternight04__Anal_dick_deep_Success = 5 # Anal

                        $ afternight04_Anal_dick_deep_Speed_0_Done = 5
                        $ afternight04_Anal_dick_deep_Speed_1_Done = 5
                        $ afternight04_Anal_dick_deep_Speed_2_Done = 5
                        $ afternight04_Anal_dick_deep_Speed_3_Done = 5

                        $ afternight04_Anal_dick_deep_Speed_0_Success = 5
                        $ afternight04_Anal_dick_deep_Speed_1_Success = 5
                        $ afternight04_Anal_dick_deep_Speed_2_Success = 5
                        $ afternight04_Anal_dick_deep_Speed_3_Success = 5

                    "No":

                        call p_Help

            "No":

                call p_Help

    menu sexbattle_Skipping_Q_Kiss:

        aj "¿Le has besado?"

        "Sí":

            call p_Help

            $ afternight04__MMouth_Tongue_Done = 5
            $ afternight04__MMouth_Tongue_Success = 5
            
            menu sexbattle_Skipping_Q_KissFrench:

                aj "¿Metiéndola lengua hasta el fondo?"

                "Sí":

                    $ afternight04__MMouth_Tongue_Deep_Done = 5
                    $ afternight04__MMouth_Tongue_Deep_Success = 5

                "No": 

                    call p_Help

        "No":

            call p_Help

    menu sexbattle_Skipping_Q_Blowjob:

        aj "¿Le has metido la polla por la boca?"

        "Sí":

            call p_Help
            
            $ afternight04__MMouth_dick_Done = 5
            $ afternight04__MMouth_dick_Success = 5

            menu sexbattle_Skipping_Q_Blowjob_DeepThroat:

                aj "¿Hasta el fondo de su garganta?"

                "Sí":

                    $ afternight04__MMouth_dick_Deep_Done = 5
                    $ afternight04__MMouth_dick_Deep_Success = 5
                    $ afternight04__MMouth_dick_Deep_Success_Cond = True

                "No" if afternight04_CumInThroat < 1:

                    call p_Help

        "No" if afternight04_CumInMouth < 1:

            call p_Help


    menu sexbattle_Skipping_Q_DidacOrgasms:

        aj "¿Cuántos orgasmos has conseguido que tenga Dídac?"

        "0" if afternight04_didac_pregnant == False:

            $ girl_1.orgasm = 0
            $ afternight04_didac_orgasms = 0
            $pl.ch_pts("dp", -10)

        "1" if afternight04_didac_pregnant == False:

            $ girl_1.orgasm = 1
            $ afternight04_didac_orgasms = 1
            $pl.ch_pts("dp", 1)

        "2" if afternight04_didac_pregnant == False:

            $ girl_1.orgasm = 2
            $ afternight04_didac_orgasms = 2
            $pl.ch_pts("dp", 2)

        "3" if afternight04_didac_pregnant == False:

            $ girl_1.orgasm = 3
            $ afternight04_didac_orgasms = 3
            $pl.ch_pts("dp", 4)

        "4" if afternight04_didac_pregnant == False:

            $ girl_1.orgasm = 4
            $ afternight04_didac_orgasms = 4
            $pl.ch_pts("dp", 6)

        "5":

            $ girl_1.orgasm = 5
            $ afternight04_didac_orgasms = 5

        "6":

            $ girl_1.orgasm = 6
            $ afternight04_didac_orgasms = 6

    menu sexbattle_Skipping_Q_MCCumshot_01:

        # ¿Se puede correr dentro del ano quitándose el condón?

        aj "La primera corrida ha sido:"

        "Dentro del Condón":

            $ afternight04_CumInCondom += 1

        "En su barriga":

            $ afternight04_CumOnStomach += 1

        "En su espalda":

            $ afternight04_CumOnBack += 1

        "En su boca" if afternight04__MMouth_dick_Success > 3:

            $ afternight04_CumInMouth += 1

        "En su garganta" if afternight04__MMouth_dick_Deep_Success > 3:

            $ afternight04_CumInThroat += 1


    menu sexbattle_Skipping_Q_MCCumshot_02:

        aj "La segunda corrida ha sido:"

        "Dentro del Condón":

            $ afternight04_CumInCondom += 1

        "En su barriga":

            $ afternight04_CumOnStomach += 1

        "En su espalda":

            $ afternight04_CumOnBack += 1

        "En su boca" if afternight04__MMouth_dick_Success > 3:

            $ afternight04_CumInMouth += 1

        "En su garganta" if afternight04__MMouth_dick_Deep_Success > 3:

            $ afternight04_CumInThroat += 1

    if afternight04_condom_broken == False:

        menu sexbattle_Skipping_Q_MCCumshot_03:

            aj "La tercera corrida ha sido:"

            "Dentro del Condón":

                $ afternight04_CumInCondom += 1

            "En su barriga":

                $ afternight04_CumOnStomach += 1

            "En su espalda":

                $ afternight04_CumOnBack += 1

            "En su boca" if afternight04__MMouth_dick_Success > 3:

                $ afternight04_CumInMouth += 1

            "En su garganta" if afternight04__MMouth_dick_Deep_Success > 3:

                $ afternight04_CumInThroat += 1

    stop music fadeout 5.0

    jump morning05