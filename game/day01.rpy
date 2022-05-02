##My Script

default neus_glasses = True # Temporal

#if renpy.variant("touch"):
default preferences.mobile_rollback_side = "left"

# init python:
#     modal True

    ##Booleans - Conditionals

default afternoon01_rapedickface = False
default afternoon01_NotPunchDidac = False

default dad = d_dad

# The game starts here.

label start:

    ## Custom name from Forum.
    scene black

    ##Call instructions
    call warning02
    call instructions02

    $ neyesp = "" # Neus Eyes Painted # To avoid a bug.
    $ deyesp = "" # Didac Eyes Painted # To avoid a bug(?)

    call instructions03
    call PlatinumHelp_label

    d_dad "La persona a la que vas a poseer se llama Jordi y es varón."

    d_dad "Puedes cambiar ese nombre, pero ten en cuenta que solo tú serás capaz de leer ese cambio."

    menu:

        d_dad "¿Deseas cambiar el nombre?"

        "<Personalizar el nombre>":
            $ protname = renpy.input("", default="Jordi")
            $ protname = protname.strip()

        "Jordi está bien.":
            pass
    
    if not protname:
         $protname = "Jordi"

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()
    with dissolve

    call jumpday
    #jump afternoon01
    
    return


label afternoon01:

    $ pdaytime = "01_afternoon"
    
    ##Miercoles
        ## Show Screen stadistics:
    $ p_ao_n_horns = "_cut01"

    stop music fadeout 2.0
    play music "audio/music/alcaknight/crimson_waltz.ogg" fadeout 3.0 fadein 3.0
    
    scene black
    show screen quick_menu()
    if PlatinumHelp == True:
        show screen Points()
        #show screen my_scr()
        with dissolve

    #voice "voices/day01/d_corre_sigueme.ogg"
    
    d "¡Corre!"

    extend " ¡Sígueme!"

    play sound "audio/sfx/grabarm01.ogg"

    scene afternoon01_Grabbed with hpunch
    n "Sientes en tu muñeca el fuerte agarrón de la mano de tu amigo de la infancia"

    n "que te arranca de la pared en la que estabas reposando de un tirón."
    
    p "¡¿Qué?!"

    p "¿A dónde me llevas ahora, payaso?"

    p "¡Me vas a arrancar el brazo!"
    
    scene afternoon01_bg Toilet with dissolve

    n "Os detenéis delante de la puerta de los servicios."
    
    p "Oye..."

    p "si te estás cagando me parece muy bien..."

    p "Pero,"

    p "¿por qué diablos me traes hasta el lavabo?"
    
    show afternoon01_Toilet_Didac_body
    show afternoon01_Toilet_Didac_eyes front01
    with dissolve
    
    play sound "audio/characters/didacmale/shh01.ogg"
    
    d "Shhh..."

    d "Cállate..."

    d "Hazme un favor,"

    extend " ¿quieres?"
    
    d "Pase lo que pase,"

    extend " no dejes que nadie entre..."

    d "¿De acuerdo?"
       
    d "Ya me debes algún que otro favor,"

    d "así que,"

    extend " por lo que más quieras,"

    d "no la cagues."

    pt "¡¿Que yo le debo a él?!"

    pt "Será caradura..."
    
    show afternoon01_Toilet_Didac_eyes left01 with dissolve

    p "¿Puedo saber al menos qué coño estás pensando hacer?"
    
    show afternoon01_Toilet_Didac_eyes front01 with dissolve
    
    play sound "audio/characters/didacmale/shh01.ogg"

    d "Shh... "
    
    show afternoon01_Toilet_Didac_eyes left01 with dissolve

    n "Tu compañero mira atento a ambos lados del pasillo por si ve -o escucha- algo."
       
    n "A esas horas de la tarde, es extraño que alguien circule por la escuela privada de Ilustración."
    
    play sound "audio/sfx/door_open01.ogg"
    
    hide afternoon01_Toilet_Didac_body
    hide afternoon01_Toilet_Didac_eyes
    show afternoon01_bg Toilet_02
    with dissolve

    n "Una vez asegurado el perímetro, abre la puerta, y entra."
    
    show afternoon01_bg Toilet with dissolve
    
    play sound "audio/sfx/door_close01.ogg"
    
    p "..."
    
    show afternoon01_bg Toilet_Close with dissolve

    n "Cuando levantas tu mirada,"

    n "te das cuenta de que el lavabo en el que ha entrado tu amigo no es ni más ni menos que el baño de mujeres."

    pt "¿Qué diablos está haciendo?"
    
    show afternoon01_bg Toilet_Close with hpunch
    
    play sound "audio/characters/neus/scream02.ogg"

    gn "{size=82}¡AAAAH!{/size}" # *Loud Scream*

    gn "¡APÁRTATE DE MÍ CAPULLO!"

    pt "¡Mierda!"
    
    menu afternoon01_posiblerape:
        
        pt "¡¿Qué puñetas está haciendo el muy imbécil?!"
        
        "<Será mejor que entre y detenga esta locura>":
            
            call p_Help
            
            $pl.ch_pts("np",1)
            
            $pl.ch_pts("dp", -3)
            
            jump afternoon01_rape_entering
        
        "<Quizás me quieran tomar el pelo... No voy a caer en una broma tan absurda>":
            
            call p_Help
        
            $ afternoon01_rapedickface = True
            
            $pl.ch_pts("np",-1)
            
            $pl.ch_pts("dp", 1)
            
            jump afternoon01_rape_entering
            
label afternoon01_rape_entering:
    
    if afternoon01_rapedickface == True:
    
        n "Decides quedarte delante de la puerta del baño,"
        
        n "esperando a que tu compañero salga y te diga:"

        n "{i}¡Era una broma, tío!{/i}"
        
        gn "{size=54}¡HIJO DE PUTA!{/size}"
        
        d "¿De qué te quejas, zorra?"

        extend "\n¡Si estás empapada!"
        
        gn "¡NO ME TOQUES ENFERMO MENTAL!"
        
        d "¿Que no te toque?"

        extend " Pero si te estoy metiendo los dedos hasta el fondo..."
           
        d "y no parece disgustarte,"

        extend " por lo que veo aquí abajo..."
        
        p "..."

        play sound "audio/sfx/fall01.ogg"
        
        n "Oyes el golpe de alguien cayendo al suelo."

        play sound "audio/sfx/zip01.ogg"
        
        n "Te parece oír también el ruido de una cremallera deslizándose."
        
        d "¡Veamos qué tal la tragas,"

        extend " zorrilla!"
        
        play sound "audio/sfx/door_open01.ogg"
        
        play music "audio/music/alcaknight/bury_it.ogg"
    
        show afternoon01_bg Bathroom_02 
        
        show afternoon01_BathroomrapeB00 at Move((-0.1, 0.0), (0.0, -0.75), 15.0):
            subpixel True
            zoom 1.5
            ease 15.0 zoom 0.85
            
        show afternoon01_Bathroom rapeB01 at Move((-0.1, 0.0), (0.0, -0.75), 15.0):
            subpixel True
            zoom 1.5
            ease 15.0 zoom 0.85
            
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeB_glasses at Move((-0.1, 0.0), (0.0, -0.75), 15.0):
                subpixel True
                zoom 1.5
                ease 15.0 zoom 0.85
        with fade
    
        n "Esta vez, sin pensártelo más, entras en el baño de chicas que estabas custodiando,"
           
        n "y lo que encuentras es a tu amigo agarrando con una mano dos brazos femeninos y delicados," 
           
        n "mientras con la otra agarra por el pelo a la chica más introvertida y tímida de la escuela."
        
        show afternoon01_BathroomrapeB00 at Position(xpos = 0.0, ypos = -0.75):
            subpixel True
            zoom 0.85
            
        show afternoon01_Bathroom rapeB02 at Position(xpos = 0.0, ypos = -0.75):
            subpixel True
            zoom 0.85
            
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeB_glasses at Position(xpos = 0.0, ypos = -0.75):
                subpixel True
                zoom 0.85
        with dissolve
        
        n "Ves los ojos de la chica que te miran fijamente tras la polla de tu amigo que le oculta parte del rostro,"
        
        n "mostrando una expresión de abatimiento y tristeza."
        
        pt "Realmente debería haber entrado antes..."

        pt "¡Mierda!"
        
        n "Se encuentra prácticamente desnuda con un pecho al descubierto"
           
        n "y con la polla de tu compañero restregándose por su cara."

        window hide dissolve
        pause
        
        jump afternoon01_Bathroomm_thispig
        
    else:
        
        play sound "audio/sfx/door_open01.ogg"
        
        show afternoon01_bg Bathroom_02 
        
        play music "audio/music/alcaknight/bury_it.ogg"
        
        show afternoon01_Bathroom rapeA01 at Move((0.0, 0.0), (-0.17, -0.4), 10.0):
            subpixel True
            
            zoom 1.5
            ease 15.0 zoom 0.85
        with fade
        
        n "Sin pensártelo demasiado, entras en el baño de chicas que estabas custodiando" 
           
        n "y lo que encuentras es a tu amigo"
        
        n "agarrándole las muñecas a la chica más introvertida de la escuela con una mano" 
           
        n "y con la otra su pecho desnudo."
        
        window hide dissolve
        pause
        
        jump afternoon01_Bathroomm_thispig
        
label afternoon01_Bathroomm_thispig:
    
    if afternoon01_rapedickface == True:
        
        scene afternoon01_bg Bathroom
        show afternoon01_Bathroom_rape_bodies
        show afternoon01_Bathroom_rape_didac_eyes front01
        show afternoon01_Bathroom_rape_didac_mouth happy_Silent
        show afternoon01_Bathroom_rape_neus_eyes surprise_front
        if neus_glasses == True: 
            show afternoon01_Bathroom_rape_neus_glasses
        show afternoon01_Bathroom_rape_neus_mouth sad_Silent
        with dissolve
        
    else:
        
        scene afternoon01_bg Bathroom
        show afternoon01_Bathroom_rapeB_bodies
        show afternoon01_Bathroom_rapeB_didac_eyes front01
        show afternoon01_Bathroom_rapeB_didac_mouth happy_Silent
        show afternoon01_Bathroom_rapeB_neus_eyes front01
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeB_neus_glasses
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve
        
    p "¡¿Se puede saber qué estás haciendo Dídac?!"

    p "¡¿Te has vuelto loco?!"
    
    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_didac_eyes front01
        show afternoon01_Bathroom_rape_didac_mouth happy_Talking
        show afternoon01_Bathroom_rape_neus_eyes surprise_front
        show afternoon01_Bathroom_rape_neus_mouth sad_Silent
        with dissolve
        
    else:

        show afternoon01_Bathroom_rapeB_didac_mouth happy_Talking
        with dissolve

    d "Esta guarra de aquí se ha reído demasiadas veces de mis trabajos..."
    
    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_neus_eyes angry_up
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_neus_eyes down01
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve
    
    d "ahora le voy a enseñar lo que pasa cuando se ríen de mí..."
    
    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_didac_eyes down01
        show afternoon01_Bathroom_rape_didac_mouth happy_Talking
        show afternoon01_Bathroom_rape_neus_mouth sad_Silent
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_didac_eyes left01
        show afternoon01_Bathroom_rapeB_didac_mouth happy_Talking
        show afternoon01_Bathroom_rapeB_neus_eyes right01
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve
        #show afternoon01_Bathroomm rapeB05  with dissolve

    d "En realidad,"

    extend " es una cachonda mental..."

    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_didac_eyes front01
        show afternoon01_Bathroom_rape_didac_mouth happy_Talking
        show afternoon01_Bathroom_rape_neus_mouth sad_Silent
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_didac_eyes front01
        show afternoon01_Bathroom_rapeB_didac_mouth happy_Talking
        show afternoon01_Bathroom_rapeB_neus_eyes right01
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve

    d "¿Qué?"

    d "¿Es que te quieres apuntar?"
    
    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_didac_eyes front01
        show afternoon01_Bathroom_rape_neus_eyes surprise_front
        show afternoon01_Bathroom_rape_didac_mouth happy_Silent
        #show afternoon01_Bathroomm rapeB07  with dissolve
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_didac_eyes front01
        show afternoon01_Bathroom_rapeB_didac_mouth happy_Silent
        show afternoon01_Bathroom_rapeB_neus_eyes front01
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve
    
    menu afternoon01_wannarape:
        
        pt "¿A qué? ¿A violarla...?"
        
        "¡Por supuesto que no!":
            
            call p_Help
            
            $pl.ch_pts("np",3)
            
            $pl.ch_pts("dp", -1)
                
            jump afternoon01_ofcoursenot
            
        "¿Y por qué no?":
                
            aj "..."
                
            aj "Violarla..."
                
            aj "Así que realmente has clicado esta opción..."

            aj "Si quieres seguir por este camino,"

            aj "tendrás que descargarte el juego:"

            extend "\n\"Pact with a Witch: REDEMPTION\""

            aj "Dónde en lugar de tu amigo,"

            aj "serás tú quien sufra el castigo."

            aj "Desgraciadamente por ahora solo está disponible en {color=#f00}inglés{/color} y {color=#f00}sin ninguna ilustración{/color}."
                
            menu afternoon01_wannarape02:
            
                pt "¿A qué? ¿A violarla...?"
            
                "¡Por supuesto que no!\n(Seguir jugando a \"Pacto con una bruja\")":
                    
                    call p_Help
                    
                    $pl.ch_pts("np",3)
            
                    $pl.ch_pts("dp", -1)
                        
                    jump afternoon01_ofcoursenot
                    
                "¿Y por qué no?\n(Descargar \"Pact with a Witch: REDEMPTION\")":
                    
                    call p_Help

                    $ web_pwawredemption()

                    jump afternoon01_wannarape02

                    #$ renpy.run("https://www.patreon.com/posts/pact-with-witch-39733016")

                    #aj "Descargar {a=https://www.patreon.com/posts/pact-with-witch-39733016}\"Pact with a witch: REDEMPTION\"{/a}."

                    #$ renpy.call_in_new_context("https://www.patreon.com/posts/pact-with-witch-39733016")
                        
                    # aj "humm..."
                        
                    # aj "..."
                        
                    # aj "Veo"

                    # extend " que te aburres,"

                    # extend " con facilidad..."
                        
                    # jump afternoon01_wannarape02

label afternoon01_ofcoursenot:

    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_neus_eyes angry_up
        #show afternoon01_Bathroomm rapeB06  with dissolve
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_didac_eyes front01
        show afternoon01_Bathroom_rapeB_didac_mouth happy_Silent
        show afternoon01_Bathroom_rapeB_neus_eyes right01
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Silent
        with dissolve
        
    p "¡Por supuesto que no!"
    
    if afternoon01_rapedickface == True:
        
        show afternoon01_Bathroom_rape_neus_eyes angry_up_2col
        show afternoon01_Bathroom_rape_neus_mouth sadx2_Silent
        #show afternoon01_Bathroomm rapeB06  with dissolve
        with dissolve
        
    else:
        
        show afternoon01_Bathroom_rapeB_neus_eyes down01_2col
        show afternoon01_Bathroom_rapeB_neus_mouth sad_Talking
        with dissolve
    
    p "¡Déjala ahora mismo!"
    
    play sound "audio/characters/didacmale/scream01.ogg"
    
    if afternoon01_rapedickface == True:
        
        scene afternoon01_Bathroomm rapeBiteCock
        if neus_glasses == True:
            show afternoon01_Bathroomm_rapeBiteCock_glasses
        with hpunch
        
        $ persistent.unlock_rape_neus_dick = True
        
        d "{size=72}¡¡AAAAARGH!!{/size}" # *Painful Scream, his Dick is bitten*
        
        n "La chica, que aún estaba agarrada fuertemente contra la pica del baño,"
        
        n "consigue darle un fuerte mordisco a la polla de Dídac."
        
    else:
        
        scene afternoon01_Bathroom rapeBite
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeBite_glasses
        with hpunch
        
        $ persistent.unlock_rape_neus_hand = True

        d "{size=72}¡¡AAAAARGH!!{/size}" # *Painful Scream, his hand is bitten*
        
    play sound "audio/sfx/slap01.ogg"
    
    if afternoon01_rapedickface == True:
        
        scene afternoon01_Bathroom_rapeSlap
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeSlap_glasses
        with hpunch
        
    else:

        scene afternoon01_Bathroom_rapeSlap
        if neus_glasses == True:
            show afternoon01_Bathroom_rapeSlap_glasses
        show afternoon01_Bathroom_rapeSlap_blood
        with hpunch

    n "Este le da una bofetada tirándola al suelo"
    
    if afternoon01_rapedickface == True:
        
        n "mientras, con la otra, se agarra su miembro viril que empieza a sangrar."
        
    else:

        n "Vuelve a agarrar a la chica mientras se desangra por el mordisco con clara señal de dolor."
    
    d "¡Maldita ramera!"

    extend " ¡No eres más que una perra rabiosa!"

    d "¡Te voy a enseñar lo que es bueno!"
    
    jump afternoon01_rapereaction
    
    menu afternoon01_rapereaction:
        
        pt "Debería hacer algo... ¿No?"
        
        "<Ignorar a tu amigo y ayudar a la chica a salir del baño>":
            
            call p_Help
            
            $ afternoon01_NotPunchDidac = True
            
            $pl.ch_pts("np",-2)
            
            $pl.ch_pts("dp", -1)
                
            jump afternoon01_Bathroom_OfferingHandtoNeus
            
        "<Darle un puñetazo a Dídac en la cara>":
            
            call p_Help
                
            $pl.ch_pts("np",5)
            
            $pl.ch_pts("dp", -5)
    
            jump afternoon01_Bathroom_PunchDidacFace
    
label afternoon01_Bathroom_PunchDidacFace:
    
    play sound "audio/sfx/punch01.ogg"

    scene hit_15
    pause 0.05
    scene hit_16
    pause 0.05
    scene hit_17
    pause 0.05
    scene hit_21
    pause 0.05
    scene hit_22
    pause 0.05
    scene hit_23
    pause 0.05
    scene hit_24
    pause 0.05
    
    scene afternoon01_Bathroom rapePunch:
        subpixel True
        zoom 1.5 xanchor 0.3 yanchor 0.3
        easein_quad 0.3 zoom 0.5 xanchor 0.0 yanchor 0.0
    with vpunch

    n "Te acercas a él y le das un puñetazo (al estilo {a=https://hunterxhunter.fandom.com/wiki/Episode_5_(2011)}Hisoka{/a}) en la cara, haciéndolo caer al suelo."

    p "¡Estás majara, idiota!"
    
    jump afternoon01_Bathroom_OfferingHandtoNeus
    
label afternoon01_Bathroom_OfferingHandtoNeus:
    
    scene afternoon01_bg Bathroom_cryingneus
    show afternoon01_Bathroom_Rape_Crying_neus_body 01
    if neus_glasses == True:
        show afternoon01_Bathroom_Rape_Crying_neus_glasses
    show afternoon01_Bathroom_Rape_Crying_neus_eyes down
    with dissolve

    n "Te acercas a ella para extenderle tu mano."
    
    show afternoon01_Bathroom_Rape_Crying_prot_hand
    with dissolve

    p "Por favor,"

    extend " disculpa al idiota de mi compañero,"
       
    p "no sé qué le está ocurriendo hoy,"

    extend "\nde verdad que no suele ser así."

    pt "¡¿En serio?!"

    if afternoon01_rapedickface == True:

        pt "¡¿Le estoy diciendo esto a una chica que acaba de tener la polla de un extraño en su cara?!"

    else:

        pt "¡¿Qué clase de imbécil soy para darle semejante excusa tan estúpida?!"

    pt "¡Maldito seas Dídac!"
    
    show afternoon01_Bathroom_Rape_Crying_neus_eyes up with dissolve

    n "La chica aún está temblando en el suelo, pero te mira con ojos menos atemorizados que antes."
    
    if afternoon01_NotPunchDidac:
        show afternoon01_Bathroom_Rape_Crying_neus_eyes down 
        with dissolve
        
    else:
        show afternoon01_Bathroom_DidacBeated_body
        show afternoon01_Bathroom_DidacBeated_eye front01
        show afternoon01_Bathroom_DidacBeated_mouth sad_Talking
        with dissolve

    d "Joder [protname]..."

    extend " Cómo te lo tomas..."

    extend " solo estaba bromeando."
    
    if afternoon01_NotPunchDidac:
        
        hide afternoon01_Bathroom_Rape_Crying_prot_hand
        
    else:
        
        show afternoon01_Bathroom_DidacBeated_eye right01
        hide afternoon01_Bathroom_DidacBeated_mouth
        with dissolve
        

    p "¡Tú estás enfermo, jodido imbécil!"

    p "¡Sabes perfectamente que acabarás expulsado por esto!"

    p "¡¿Crees que la chica no te va a denunciar por esto?!"

    p "¡Idiota!"
    
    if not afternoon01_NotPunchDidac:
        show afternoon01_Bathroom_DidacBeated_eye front01
        show afternoon01_Bathroom_DidacBeated_mouth sad_Talking
        with dissolve

    d "¡Joder!"

    extend "\n¡Ella me ha mordido!"
    
    if not afternoon01_NotPunchDidac:
        show afternoon01_Bathroom_DidacBeated_eye right01
        hide afternoon01_Bathroom_DidacBeated_mouth
        with dissolve
    
    if afternoon01_rapedickface == True:
        
        p "¡¡Te ha mordido LA POLLA,"

        extend " CAPULLO!!"
        
    else:
        p "¡Y yo te voy a romper los dientes!"
    
    p "¡¿Qué coño tienes por cerebro?!"
    
    jump afternoon01_Bathroom_AcceptingHandNeus
        
label afternoon01_Bathroom_AcceptingHandNeus:
    
    scene afternoon01_bg Bathroom_cryingneus
    show afternoon01_Bathroom_Rape_Crying_neus_body 01
    if neus_glasses == True:
        show afternoon01_Bathroom_Rape_Crying_neus_glasses
    show afternoon01_Bathroom_Rape_Crying_neus_eyes up
    show afternoon01_Bathroom_Rape_Crying_prot_hand
    with dissolve

    n "Te vuelves a acercar a ella para ofrecerle tu mano."
    
    show afternoon01_Bathroom_Rape_Crying_neus_body arm
    with dissolve

    n "La chica se agarra a ti,"
       
    n "y ambos salís del baño de chicas dejando atrás a tu amigo de la infancia."
    
    jump afternoon01_outwc
    
label afternoon01_outwc:
    
    play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
    
    $ persistent.unlock_rape_neus_out = True
    
    scene afternoon01_bg Toilet
    #show N raped_body at right 
    show neus_body_full afterrape:
        neus_body_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris left03:
        neus_exp_atright_position
    show neus_exp_tears 03_03:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atright_position
    if neus_glasses == True:
        show neus_exp_glasses:
            neus_exp_atright_position
    show neus_body_full_afterrape_hair:
        neus_body_atright_position
    with fade

    p "Perdóname,"

    extend " de verdad,"

    p "te juro que no tenía ni idea de qué tenía pensado el gilipollas de mi amigo..." 

    show neus_exp_eyes 04
    show neus_exp_iris front04 
    show neus_exp_tears 04_03
    show neus_exp_mouth sad_Silentx02
    with dissolve
       
    p "¿Te duele mucho la mejilla?"
    
    show neus_exp_eyes 03
    show neus_exp_iris front03 
    show neus_exp_tears 03_03
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    gn "Ya no..."

    extend " Gracias."
    
    show neus_exp_eyes 03
    show neus_exp_iris left03 
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "Si quieres denunciarlo,"

    extend " o llamar a la policía,"

    show neus_exp_eyebrows sadx03
    show neus_exp_eyes 03
    show neus_exp_iris front03 
    show neus_exp_tears 03_03
    show neus_exp_mouth sad_Silentx02
    with dissolve
    
    p "lo entenderé perfectamente;"

    show neus_exp_eyes 02
    show neus_exp_iris front02 
    show neus_exp_tears 02_03
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "aunque..."
    
    show neus_exp_eyes 03
    show neus_exp_iris front03 
    show neus_exp_tears 03_02
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    gn "Tranquilo."

    show neus_exp_eyes 04
    show neus_exp_iris front04 
    show neus_exp_tears 04_02
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    gn "No voy a denunciar a tu amigo."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 04
    show neus_exp_iris left04 
    show neus_exp_tears 04_02
    show neus_exp_mouth happy_Silentx03
    with dissolve

    pt "¿Está..."

    extend " sonriendo?"

    show neus_exp_eyes 03
    show neus_exp_iris left03 
    show neus_exp_tears 04_02
    show neus_exp_mouth happy_Silentx04
    with dissolve
        
    pt "¿Después de lo que le ha sucedido?"
    
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_tears 02_02
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "Vaya..."

    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_tears 02_02
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "Odio tener que admitirlo..."

    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_tears 01_02
    show neus_exp_mouth sad_Silentx02
    with dissolve

    p "Pero te lo agradezco."

    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_02
    show neus_exp_mouth sadbiting_Silentx03
    with dissolve

    pt "Soy basura humana por decirle esto..."

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_tears 01_02
    show neus_exp_mouth sad_Silentx01
    with dissolve

    p "Te prometo que no es así," 

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_tears 02_02
    show neus_exp_mouth sad_Silentx04
    with dissolve
       
    p "de verdad que no sé qué demonios se habrá tomado hoy el muy gilipollas..."

    show neus_exp_eyebrows sadx02
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Silentx05
    with dissolve

    pt "¡¿De verdad tengo que repetirle la misma estúpida excusa otra vez?!"

    show neus_exp_eyebrows sadx03
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_02
    show neus_exp_mouth sad_Silentx06
    with dissolve

    p "¿Estás segura de que no necesitas que te miren la mejilla?"

    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_tears 06_02
    show neus_exp_mouth sad_Silentx05
    with dissolve
       
    p "El golpe ha sido bastante fuerte..."
    
    show neus_exp_eyebrows serious
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Silentx04
    with dissolve

    pt "Te voy a matar Dídac..."

    show neus_exp_eyebrows sadx02
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_tears 04_02
    show neus_exp_mouth sad_Silentx02
    with dissolve

    gn "..."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris down03
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    gn "Euh..."
    
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_tears 03_02
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    gn "No..."
    
    extend " de verdad que no,"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_tears 03_01
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    gn "estoy bien..."

    show neus_exp_eyebrows suspiciousx01
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_tears 04_01
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    gn "al menos mucho mejor que tu estúpido amigo... "
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 07
    show neus_exp_iris front07
    show neus_exp_tears 06_01
    show neus_exp_mouth happy_Silentx05
    with dissolve
    
    pt "¿Mucho mejor que mi amigo?"

    show neus_exp_eyebrows sadx03
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_tears 06_01
    show neus_exp_mouth happy_Silentx03
    with dissolve

    pt "¿Por qué sonríe?"

    if afternoon01_NotPunchDidac == False:

        show neus_exp_eyebrows surprisex02
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_tears 01_01
        show neus_exp_mouth sad_Silentx03
        with dissolve

        p "No te preocupes por él,"
        
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_tears empty
        show neus_exp_mouth sad_Silentx04
        with dissolve
           
        p "a veces le he dado una mayor tunda,"

        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears empty
        show neus_exp_mouth sad_Silentx04
        with dissolve

        p "y en este caso se merecía mucho más de lo que le he hecho."
        
        show neus_exp_eyebrows sadx03
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_mouth sad_Silentx05
        with dissolve

        gn "..."
        
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Silentx03
        with dissolve

    else:

        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_tears empty
        show neus_exp_mouth sad_Silentx03
        with dissolve

    p "Por favor,"

    extend " perdona mis modales,"

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Silentx02
    with dissolve

    p "sé que estás en nuestra clase;"

    show neus_exp_eyebrows normal
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Silentx03
    with dissolve

    pt "Y de hecho,"

    extend " creo que hace unos días que no la veo por la escuela;"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sadbiting_Silentx03
    with dissolve

    pt "¿Será que ya se intuía lo que Dídac tenía planeado?..."

    show neus_exp_eyebrows surprisex03
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "Pero no logro recordar cómo te llamabas."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Talkingx002
    with dissolve

    gn "¿Euh?"

    show neus_exp_eyebrows normal
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    gn "¿Mi nombre?"

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 00
    show neus_exp_iris front00
    show neus_exp_mouth sad_Talkingx03
    with dissolve

    gn "¿Quieres saber cómo me llamo?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_blush 02
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "Sí..."

    extend " bueno..."

    show neus_exp_eyebrows surprisex02
    show neus_exp_blush 03
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_mouth sad_Silentx05
    with dissolve

    p "creo que suele ser lo normal cuando uno se presenta,"

    show neus_exp_eyebrows surprisex01
    show neus_exp_blush 03
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_mouth sad_Silentx02
    with dissolve
       
    p "yo me llamo [protname],"

    show neus_exp_eyebrows sadx01
    show neus_exp_blush 04
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "creo que vamos a la misma clase..."

    show neus_exp_eyebrows sadx03
    show neus_exp_blush 04
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    p "Perdona mi memoria..."

    show neus_exp_eyebrows sadx04
    show neus_exp_blush 04
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "soy terrible para los nombres."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris down01
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    gn "Sí,"

    extend " sé quién eres,"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth sad_Talkingx002
    with dissolve

    gn "[protname]..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "Vaya..."

    extend " pues ahora me siento fatal por no recordar el tuyo..."

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_mouth sad_Silentx04
    with dissolve
       
    p "Creo que te sientas en la parte de atrás del todo en clase,"

    extend " ¿verdad?"

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_mouth sad_Silentx02
    with dissolve
       
    p "También creo recordar que dibujas estilo {a=https://es.wikipedia.org/wiki/Shōjo}Shojo{/a} y {a=https://es.wikipedia.org/wiki/Yaoi}Yaoi{/a} muy bien."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_blush 03
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth sad_Silentx04
    with dissolve

    gn "..."
    
    show neus_exp_eyebrows sadx03
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_mouth sad_Talkingx04
    with dissolve
    
    ne "Me llamo {b}Neus{/b}."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_blush 02
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_mouth sad_Silentx04
    with dissolve

    n "Se oye el ruido del grifo dentro del baño y unas salpicaduras de agua."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "Es un placer conocerte al fin, Neus,"

    extend "\npero sería mejor que ahora te fueras." 
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth sad_Silentx03
    with dissolve
       
    p "Si no te importa..."

    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "me gustaría tener una conversación con mi \"compañero de piso\" a solas."

    show neus_exp_eyebrows sadx04
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    scene afternoon01_bg Toilet
    with dissolve

    n "La chica ladea la cabeza a modo de aprobación y desaparece al cruzar el fondo del pasillo."
    
    play sound "audio/sfx/door_open01.ogg"
    
    show afternoon01_bg Toilet_02 with dissolve

    n "La puerta del baño se abre tímidamente y de él aparece tu {b}amigo de la infancia{/b}."
    
    play sound "audio/sfx/door_close01.ogg"
    
    play music "audio/music/alcaknight/crimson_waltz.ogg" fadein 3.0 fadeout 3.0
    
    show afternoon01_bg Toilet
    show D_damagedIndifferent_body at right
    if afternoon01_NotPunchDidac == False:
        show D_damagedIndifferent_cheek at right
    show D_damagedIndifferent_eyes left01 at right
    show D_damagedIndifferent_mouth sad_Talking at right
    with dissolve

    d "¿Esa bruja ya se ha pirado?"
    
    show D_damagedIndifferent_mouth sad_Silent
    with dissolve

    p "Maldito hijo de puta..."

    show D_damagedIndifferent_eyes front01
    with dissolve

    p "¡¿Qué coño te pasa por la cabeza?!"
    
    show D_damagedIndifferent_eyes front01
    show D_damagedIndifferent_mouth sadx2_Talking
    with dissolve

    d "Oye,"

    extend " tío,"

    d "lo siento..."

    extend " ¿vale?"

    show D_damagedIndifferent_eyes left01
    with dissolve

    d "Solo quería tomarle un poco el pelo."
    
    show D_damagedIndifferent_eyes left01
    show D_damagedIndifferent_mouth sad_Talking
    with dissolve
       
    d "Me jode mucho que se rían de mis dibujos..."

    extend " ya lo sabes,"

    extend " joder..."
    
    show D_damagedIndifferent_eyes left01
    show D_damagedIndifferent_mouth sad_Silent
    with dissolve
        
    if afternoon01_rapedickface == True:
        
        p "La tenías de rodillas desnuda de cintura para arriba"
        
        p "y encima le habías puesto la polla en la puta cara."
    
    else:
        
        p "Estaba medio desnuda,"

        extend " la tenías cogida por el cuello" 
           
        p "y le estabas agarrando un pecho al descubierto con la otra mano."

    p "Eso no es {i}tomarle un poco el pelo{/i};"

    if afternoon01_rapedickface == True:

        p "¡Estabas a punto de meterle la polla en la boca!"

    else:

        p "Son claros indicios de violación."

    extend " ¡Capullo!"
    
    show D_damagedIndifferent_mouth sad_Talking
    with dissolve

    d "Vale,"

    extend " vale..."

    d "Joder..."

    show D_damagedIndifferent_mouth sadx2_Talking

    d "Quizás me haya pasado un poco,"

    extend " lo reconozco..."
       
    show D_damagedIndifferent_eyes front01
    show D_damagedIndifferent_mouth sad_Talking
    with dissolve

    d "pero es que me he ido animando..."
    
    show D_damagedIndifferent_eyes left01
    with dissolve
       
    d "la chica tampoco ofrecía mucha resistencia,"

    extend " parecía que quería que lo hiciera..."
    
    show D_damagedIndifferent_mouth sad_Silent
    with dissolve

    p "Cuando una chica quiere que hagas algo,"

    extend "\nte lo pide,"

    p "no te grita,"

    extend " {i}¡Suéltame capullo!{/i}"

    show D_damagedIndifferent_eyes front01
    with dissolve

    if afternoon01_rapedickface == True:

        p "mientras le pones la polla al descubierto en su cara..."

    else:

        p "mientras la estás estrangulando y desnudando a la fuerza..."

    show D_damagedIndifferent_eyes left01
    with dissolve

    d "..."

    p "¿Qué coño voy a hacer contigo?"

    show D_damagedIndifferent_eyes front01
    with dissolve

    p "Debería denunciarte yo mismo ante dirección."
    
    show D_damagedIndifferent_eyes front01
    show D_damagedIndifferent_mouth sadx2_Talking
    with dissolve

    d "Joder tío,"

    extend " no te pases..."

    show D_damagedIndifferent_mouth sad_Talking
    with dissolve

    d "Te he pedido perdón,"

    extend " ¿no?"
    
    show D_damagedIndifferent_mouth sad_Silent
    with dissolve

    p "¡¿Y a ella qué?!" 
    
    show D_damagedIndifferent_eyes left01
    with dissolve

    p "¿Y si no te llego a parar?"

    extend " ¿Qué coño le habrías hecho?"
    
    show D_damagedIndifferent_eyes front01
    show D_damagedIndifferent_mouth sad_Talking
    with dissolve

    d "Joder,"

    extend " no lo sé..."

    d "¿Vale?"

    d "No sé qué me ha pasado..."
    
    show D_damagedIndifferent_eyes left01
    with dissolve

    d "Mañana ya le pediré perdón cuando la vea."
    
    show D_damagedIndifferent_mouth sad_Silent
    with dissolve

    p "Más te vale imbécil."

    extend " Más te vale..."
    
    window hide dissolve
    
    pause

    
    jump night01
    
    
label night01:
    
    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0

    scene bg tv_kid_comp:
        subpixel True
        truecenter
        zoom 1.5 xpos 1.5 ypos 1.1
        easein_quad 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    ptv "Hace ya tres días que sigue sin haber noticias de la desaparición del pequeño Edward,"

    ptv "el hijo de seis años"

    ptv "del famoso matrimonio compuesto por el popular cantante"

    extend " y la galardonada actriz,"

    ptv "ambos también fervientes activistas dedicados a salvar el Amazonas,"

    ptv "y en luchar contra el monopolio de la farmacéutica {i}{a=https://es.wikipedia.org/wiki/Arkham}Arkham{/a} industries{/i},"

    ptv "que desapareció sin dejar rastro,"

    show bg tv_sagradafamilia_comp
    with dissolve

    ptv "tras la visita,"

    extend " a plena luz del día,"

    ptv "de la {a=https://es.wikipedia.org/wiki/Templo_Expiatorio_de_la_Sagrada_Familia}Sagrada Familia{/a} en Barcelona,"

    ptv "durante sus vacaciones de verano."

    show bg tv_kid_comp
    with dissolve

    ptv "Aunque las autoridades piden calma a la familia,"

    ptv "sus padres siguen insistiendo en los medios de comunicación,"

    ptv "que pagarían cualquier suma que se pidiera por su rescate."

    pt "Madre mía,"

    extend " qué peligrosa se está volviendo Barcelona últimamente..."

    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0

    scene bg tv_background_off:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
    with dissolve

    pt "Para oír este tipo de noticias,"

    extend " mejor apago el televisor."
    
    scene night01_bg espaguetti
    with fade
    
    n "El olor de espaguetis al pesto inunda todo el comedor."

    n "No es que seas un {a=https://es.wikipedia.org/wiki/Ferran_Adrià}Ferran Adrià{/a},"
       
    n "así que tampoco eres precisamente muy {a=https://es.wikipedia.org/wiki/Sibarita}sibarita{/a} con la comida."
    
    show night01_bg dinner
    show night01_dinner_didac_body
    show night01_dinner_didac_mouth sad_Silent
    with dissolve

    n "Tampoco lo es tu compañero de piso, sin embargo, con lo poco que te queda a ti para terminar el plato," 
       
    n "él apenas ha tocado el tenedor."

    p "Tío..."

    p "¿Te pasa algo?"

    extend "\nTienes mala cara..."

    pt "Por lo que me ha dicho,"

    pt "la mordida le ha dejado de sangrar,"

    if afternoon01_rapedickface == True:

        extend " y tampoco voy a bajarle los pantalones para comprobarlo..."

    else:

        extend " y de hecho, su mano se ve mucho mejor..."
    
    show night01_dinner_didac_mouth sad_Talking
    with dissolve

    d "Sí..."

    extend " no sé..."
       
    d "No me encuentro muy bien..."
    
    show night01_dinner_didac_mouth sad_Silent
    show night01_dinner_prot_hand
    with dissolve

    n "Te levantas de la silla y le pones una mano en la frente."

    p "Macho..."

    extend "\n¡Estás ardiendo!" 
    
    hide night01_dinner_prot_hand with dissolve
    
    p "Será mejor que te metas en la cama ahora mismo."
    
    show night01_dinner_didac_mouth sad_Talking
    with dissolve

    d "Sí..."

    extend "\nquizás tengas razón..."
    
    #scene night01_bg onbed
    #with fade
    
    scene didac_bed_bed over
    show didac_bed_d_body 01
    show didac_bed_d_sweat 01
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    show didac_bed_d_hair 01
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 00
    with fade
    
    window hide dissolve
    pause

    n "Cogiéndolo por el hombro le ayudas a llegar a la cama."

    n "Su cuerpo está sudoroso y muy caliente."

    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyebrows normal
    show didac_bed_headtowel wet
    show didac_bed_d_blanket 02
    with dissolve

    n "Le ayudas a desvestirse y le traes una aspirina."

    show 01_aspiring_bg
    show 01_aspirin:
        subpixel True
        truecenter
        zoom 1.0
        ease 10.0 zoom 0.5
    with Dissolve (1.0)

    pt "Estas aspirinas de Arkham son bastante más caras que las de cualquier otra marca,"

    pt "pero no se puede negar que funcionan mucho mejor que las demás..."

    hide 01_aspiring_bg
    hide 01_aspirin
    with dissolve

    n "Decides quedarte para comprobar que la cosa no empeora, pero ves que la aspirina le ha bajado un poco la fiebre,"
    
    scene beds_night_lightOn_blindUp_Dbusy01MCbusy
    show beds_D01_night_lightOn_blindUp
    with fade
       
    n "así que decides limpiar la mesa y meterte en tu cama, que está en la misma habitación."

    n "Es un piso pequeño, muy pequeño," 
    
    play sound "audio/sfx/click_turnofflights.ogg"
    
    scene beds_night_lightOff_blindUp_Dbusy01MCbusy
    show beds_D01b_night_lightOff_blindUp
    with dissolve
       
    n "pero para dos estudiantes que a duras penas pueden pagarse los estudios y el alquiler del piso," 
       
    n "está más que bien."
    
    window hide dissolve
    
    pause
    
    jump morning02
    


    
    


