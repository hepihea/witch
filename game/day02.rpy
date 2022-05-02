
## Conditionals day02

default afternoon02_didac_beforeshower_ambulance = False

default meyesc = ""
default deyesc = ""

#ShowerDidac

default afternoon02_ShowerPiernas = False
default afternoon02_ShowerBack = False
default afternoon02_ShowerAbs = False

label morning02:

    $ pdaytime = "02_morning"

    $ p_ao_n_horns = "_cut01"
    
    ##Jueves
    
    play music "audio/sfx/birds01.ogg" fadeout 3.0 fadein 3.0
    
    scene beds_morning_lightOff_blindUp_Dbusy01MCbusy
    show beds_D01b_morning_lightOff_blindUp
    with fade
    
    $ renpy.notify("Day 02")
    
    n "Apenas ha amanecido y sin demasiada demora te levantas de la cama para comprobar cómo está tu compañero."
    
    #show morning02_bg onbed with dissolve
    
    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 02
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    show didac_bed_d_hair 02
    show didac_bed_headtowel dry
    show didac_bed_d_blanket 01
    with dissolve
    
    window hide dissolve
    pause

    n "Encuentras su cama empapada de sudor, pero al menos el ardor de la frente ha disminuido."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyebrows angryx02
    with dissolve

    n "Al mirarle detenidamente, te da la extraña sensación de que ha perdido gran parte de su complexión muscular en una sola noche."

    n "Le ayudas a que se tome otra aspirina."
    
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyebrows normal
    with dissolve
       
    n "Le dejas su móvil cerca de la mesita de noche, por si acaso,"

    n "antes de salir por la puerta para asistir a las clases de Diseño gráfico."
    
    jump morning02_school
    
label morning02_school:

    $ meyesc = "_red"
    
    stop music fadeout 3.0
    
    scene morning02_bg schoolwall with fade
    
    n "Poco después de terminar la primera clase de la mañana, te dispones a buscar a la extraña chica de ayer."
    
    gm "Buenos días,"

    extend " [protname]."
    
    play music "audio/music/meritxell_theme.ogg" fadeout 3.0 fadein 3.0

    show m_bodynew relax_02:
        mtxell_body_ontheright_position

    show m_exp_blush 02:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Silentx05:
        mtxell_exp_ontheright_position
    show m_exp_eyes 03:
        mtxell_exp_ontheright_position
    show m_exp_piris front03:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows normal:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_mouth happy_Silentx05:
        #m_face_atright_position
    #show m_exp_eyes 03:
        #m_face_atright_position
    #show m_exp_piris front03:
        #m_face_atright_position
    ##show m_pupils front03a:
        ##m_face_atright_position
    #show m_exp_eyebrows normal:
        #m_face_atright_position
    #with dissolve
    
    p "¿Euhh...?"
    
    n "En tu intento por alcanzarla, te topas con la que es, sin duda, la chica más alta..."

    n "y pechugona de la escuela."

    pt "No recuerdo que tuviera los ojos de ese color..."

    pt "¿Llevará lentillas?"

    menu morning02_MeetingMeritxell:
        
        pt "Diablos... ¿Cómo se llamaba esta?"
        
        "Buenos días...":
            
            call p_Help
            
            $pl.ch_pts("mp",2)
            $pl.ch_pts("np",-1)
                  
            jump morning02_MeetingMeritxell_handsome
        
        "¿Y tú quién eres?...":
            
            call p_Help
            
            $pl.ch_pts("mp",-2)
            $pl.ch_pts("np",+1)
                  
            jump morning02_MeetingMeritxell_andwhoareyou
            
        "Lo siento, tengo prisa.":
            
            call p_Help
            
            $pl.ch_pts("mp",-2)
            $pl.ch_pts("np",+1)
                  
            jump morning02_MeetingMeritxell_iminahurry
            
label morning02_MeetingMeritxell_iminahurry:

    $ meyesc = "_goat"
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows angryx04
    with dissolve

    $ meyesc = "_red"
    show m_exp_eyes 04
    show m_exp_piris front04
    with Dissolve(0.5)
    
    
    gm "..."
    
    stop music fadeout 3.0
    
    scene morning02_bg schoolwall 
    with dissolve
    
    n "El hecho de que pases olímpicamente de ella no es algo que le haya sentado demasiado bien..."
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0
    
    show neus_body_full day02:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_mouth happy_Silentx04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    jump morning02_namegirlNeus
            
label morning02_MeetingMeritxell_andwhoareyou:

    $ meyesc = "_goat"
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows angryx04
    with dissolve

    $ meyesc = "_red"
    show m_exp_eyes 04
    show m_exp_piris front04
    with Dissolve(0.5)
    
    gm "..."

    stop music fadeout 3.0
    
    scene morning02_bg schoolwall 
    with dissolve
    
    n "Parece que no se ha tomado muy bien el hecho de que no me acuerde de su nombre..."
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0
    
    show neus_body_full day02:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_mouth happy_Silentx04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    jump morning02_namegirlNeus
            
label morning02_MeetingMeritxell_handsome:
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Hoy no he visto a Dídac,"

    extend " espero que esté bien,"

    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "Especialmente después de ver en las noticias,"

    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyebrows normal
    with dissolve

    gm "la triste noticia sobre la desaparición de ese niño,"

    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyebrows sadx01
    with dissolve

    gm "Espero que puedan encontrarlo pronto y esté bien."

    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Sí..."

    extend "\nyo también lo espero..."

    show m_exp_eyes 06
    show m_exp_piris front06
    #show m_pupils front05a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows sadx01
    with dissolve

    gm "Bueno,"

    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyebrows normal
    with dissolve
       
    gm "que pases un buen día,"

    $ meyesc = "_goat"
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyebrows surprisex001
    with dissolve

    $ meyesc = "_red"
    show m_exp_eyes 04
    with dissolve

    gm "{b}guapo{/b}."
    
    scene morning02_bg schoolwall 
    with dissolve
    
    pt "¿Guapo?"

    pt "¿Qué le ha picado a esta?"

    pt "Se pasa todo el año saludándome de forma fría y distante..."

    pt "¿y ahora esto?"
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0

    show neus_body_full day02:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx02:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx05:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    n "Apenas te da tiempo a parpadear cuando ves que aparece la chica de ayer en frente de ti."
    
    gn "..."
    
    n "¿Y a esta qué le pasa?"

    n "Parece que quiera matar a alguien..."

    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris left03:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atright_position
    show neus_exp_tears empty
    show neus_exp_glasses:
        neus_exp_atright_position
    with dissolve
    
    jump morning02_namegirlNeus
    
label morning02_namegirlNeus:
    
    pt "Curioso..."

    pt "pensaba que lo de ayer le habría creado algún trauma..."

    pt "pero parece que va incluso más ligera de ropa que ayer..."
    
    menu morning02_namegirl:
        
        pt "Y esta... ¿cómo se llamaba?"
        
        "Buenos días, {b}Noa{/b}":
            
            call p_Help
            
            jump morning02_afterwrongname
        
        "Buenos días, {b}Núria{/b}":
            
            call p_Help

            jump morning02_afterwrongname
            
        "Buenos días, {b}Neus{/b}":
            
            call p_Help
            
            $pl.ch_pts("np",2)
            
            jump morning02_aftercorrectname
            
        "Buenos días, {b}Nerea{/b}":
            
            call p_Help
            
            jump morning02_afterwrongname
            
            
label morning02_afterwrongname:
    
    $pl.ch_pts("np",-2)
    
    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    gn "..."
    
    show neus_exp_eyebrows sadx02
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Talkingx04
    with dissolve
    
    gn "No..."

    show neus_exp_eyebrows sadx03
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_tears 04_02
    show neus_exp_mouth sad_Talkingx03
    with dissolve

    gn "Me llamo Neus..."
    
    show neus_exp_eyebrows sadx02
    show neus_exp_tears 02_02
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    p "Vaya..."

    show neus_exp_eyebrows sadx04
    show neus_exp_tears 03_02
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "Ehem..."

    show neus_exp_eyebrows sadx04
    show neus_exp_tears 02_03
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "lo siento,"

    show neus_exp_eyebrows sadx05
    show neus_exp_tears 03_03
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_mouth sad_Silentx06
    with dissolve

    p "ya te dije que tenía mala memoria..."
    
    show neus_exp_eyebrows sadx05
    show neus_exp_tears 04_03
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth sad_Talkingx04
    with dissolve
    
    ne "No pasa nada..."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_tears 02_03
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "¿Está llorando?"

    show neus_exp_eyebrows angryx02
    show neus_exp_tears 08_03
    show neus_exp_eyes 08
    show neus_exp_iris front08
    show neus_exp_mouth sad_Silentx05
    with dissolve

    show neus_exp_tears empty
    with dissolve
    
    jump morning02_aftername
            
label morning02_aftercorrectname:
       
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "Vaya..."

    show neus_exp_eyebrows normal
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne "Veo que te acuerdas de mi nombre."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 06
    show neus_exp_iris front06
    show neus_exp_mouth happy_Silentx04
    with dissolve

    p "Te dije que tengo mala memoria..."

    show neus_exp_eyebrows sadx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx05
    with dissolve

    p "pero tampoco es tan horrible."
    
    jump morning02_aftername
    
label morning02_aftername:
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    ne "¿Cómo está tu \"compañero\"?"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "Pues la verdad es que no muy bien..."

    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth happy_Silentx02
    with dissolve
       
    p "Ayer empezó a tener dolor de cabeza y mucha fiebre."

    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve
       
    p "Y esta mañana seguía sin tener muy buena cara."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    ne "Bah..."

    show neus_exp_eyebrows surprisex02
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx03
    with dissolve

    ne "No te preocupes por él, [protname],"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_mouth sad_Talkingx05
    with dissolve

    ne "aunque llegue un punto en el que parezca que se vaya a morir,"

    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
        
    ne "en realidad,"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne "lo único que hará es mejorar a tus ojos."

    show neus_exp_eyebrows normal
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¿Qué?"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx04
    with dissolve

    p "¿De qué estás hablando?"
    
    show neus_exp_eyebrows suspiciousx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    ne "Tu amigo va a cambiar."

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 01
    show neus_exp_iris right01
    show neus_exp_mouth happy_Talkingx06
    with dissolve

    ne "A algo mejor,"

    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne "te lo aseguro... "

    show neus_exp_eyebrows suspiciousx01
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    ne "a pesar de que a él probablemente no le parezca así al principio."
    
    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    ne "Aunque..."

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth sad_Talkingx05
    with dissolve

    ne "a menos que se quede preñada,"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    ne "aún tendrá la oportunidad de volver a ser lo que era."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "..."

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris right03
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "¿Cómo?"
    
    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx05
    with dissolve

    ne "Si realmente quieres ayudarlo,"

    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx06
    with dissolve

    ne "te voy a dar un consejo,"

    show neus_exp_eyebrows suspiciousx01
    show neus_exp_eyes 02
    show neus_exp_iris right02
    show neus_exp_mouth sad_Talkingx004
    with dissolve

    ne "aunque no se lo merezca ese sinvergüenza."

    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Talkingx07
    with dissolve

    ne "Ni se te ocurra llevarlo a un hospital,"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx06
    with dissolve

    ne "pase lo que pase y esté como esté,"

    show neus_exp_eyebrows angryx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth sad_Talkingx05
    with dissolve

    ne "o nunca más volverás a verlo con vida."
    
    show neus_exp_mouth sad_Silentx04
    with dissolve

    p "... ¿Puedes explicarme esto de una manera en que pueda...?"
    
    play sound "audio/sfx/ring_phone01.ogg"


    show neus_exp_eyebrows serious
    show neus_exp_eyes 04
    show neus_exp_iris down04
    show neus_exp_mouth sad_Silentx04
    with vpunch

    n "En ese momento, el teléfono móvil empieza a vibrar y a sonar en tu bolsillo." 

    show neus_exp_iris front04
    show morning04_bg_livingroom_mc_resting_phone didac_calling:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with dissolve

    pause 1.0

    hide neus_body_full
    hide neus_head
    hide neus_exp_eyebrows surprisex01
    hide neus_exp_eyes 04
    hide neus_exp_iris left04
    hide neus_exp_mouth happy_Silentx04
    hide neus_exp_tears empty
    hide neus_exp_glasses
    hide neus_exp_hairfront
    with dissolve
    
    p "¡Mierda!"

    extend " ¡Es Dídac!"

    scene morning02_bg schoolwall with dissolve
    
    n "Al levantar la mirada del teléfono, Neus había desaparecido."
    
    pt "Mierda,"

    pt "no tengo tiempo para ir a buscarla ahora..."

    extend " Tengo que largarme ya."
    
    window hide dissolve
    
    pause
    
    jump afternoon02
    
label afternoon02:
    
    play music "audio/music/didac_theme.ogg" fadeout 3.0 fadein 3.0
    
    #scene morning02_didac_onbed_body
    #show morning02_didac_onbed_eyes relaxed04
    #show morning02_didac_onbed_mouth sad_Silent
    #with fade
    
    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 02
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    show didac_bed_d_hair 02
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 00
    with fade
    
    window hide dissolve
    pause
    
    p "¡¿Cómo estás?!"

    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    n "No te ha dado tiempo ni a dejar las llaves sobre la mesita de la entrada," 
       
    n "y ya te ves dentro de vuestra habitación sudando casi tanto como él"
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    with dissolve
       
    n "después de haber recorrido varias calles corriendo a toda prisa."
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Hola... "
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve
       
    d "Joder..."

    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve
       
    d "Antes he intentado levantarme para ir a buscar otra aspirina... "
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    n "La voz de Dídac suena entrecortada y cansada."
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve
       
    d "Pero no he podido moverme..."
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
       
    d "No sé qué me pasa, tío..."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve
       
    d "es como si me estuviera muriendo..."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "Ahora vengo,"

    p "voy a buscar otra aspirina."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with vpunch

    d "¡Serás capullo!"

    show didac_bed_d_mouth sad_Talkingx02
    with dissolve

    d "¿No ves cómo estoy?"
    
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    n "Con la cama y la manta completamente empapadas por el sudor, se vislumbra mucho mejor su silueta."

    n "Da la sensación de que no solo ha perdido un montón de peso," 
       
    n "sino que parece que haya incluso reducido su estatura."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "Coño..."

    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve
    d "¡Llama a una puta ambulancia!"

    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    with dissolve

    d "¡¿No crees?!"
    
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    menu afternoon02_Hospitalquestion:
        
        pt "Si le ataco la moral, se enfadará, pero quizás así evite que vaya al hospital..."
        
        "<Mejor será ignorar el consejo de Neus y llevarlo al hospital, realmente no me fio de esa mujer>":
            
            call p_Help
            
            jump afternoon02_Hospital
        
        "<Herirle el orgullo de macho alfa por tenerle miedo a una fiebre, siendo algo que hasta los niños pasan en casa>":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
            
            jump afternoon02_damageproud
            
        "<Contarle la verdad>":
            
            call p_Help
            
            jump afternoon02_Truth01
            

label afternoon02_Truth01:
    
    pt "Neus me aconsejó que no lo llevara al hospital..."
    
    pt "Pero..."

    pt "¿cómo puedo confiar en esa mujer ciegamente?"
    
    pt "La vida de mi compañero puede correr un serio peligro."
    
    pt "Lo más justo sería que fuera él mismo quien eligiera qué hacer sabiendo toda la verdad."
    
    pt "Pero..."

    pt "¿Realmente podrá tomar una decisión sabia en su estado actual?"
    
    pt "De hecho..."

    pt "¿Sería capaz de tomar una decisión sabia aunque no estuviera como está?"
    
    pt "Nunca ha sido una persona con demasiada materia gris..."
    
    pt "Es de los que disparan antes de preguntar."
    
    pt "En realidad,"

    pt "no creo que sea una buena idea contarle nada."

    menu afternoon02_HospitalquestionTruth:
        
        pt "¿Le digo la verdad? ¿O intento retenerlo aquí durante más tiempo?"
        
        "<Herirle el orgullo de macho alfa por tenerle miedo a una fiebre alta por ser algo que hasta los niños pasan en casa>":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
            
            jump afternoon02_damageproud
        
        "<Definitivamente se merece saber la verdad, aunque eso le cueste la vida>":
            
            call p_Help
            
            jump afternoon02_Truth02
            
            
label afternoon02_Truth02:
    
    p "Dídac,"

    extend " hay algo que tienes que saber."
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    d "¿Euh?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    d "Te veo muy serio..."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    n "A pesar de que su vista debe de estar algo nublada,"

    n "se percata de que mi rostro denota algo más que simple preocupación por su salud."
    
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    d "¿Qué ocurre, [protname]?"
    
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve
    
    p "¿Te acuerdas de lo que ocurrió ayer en el baño de la escuela?"
    
    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    n "Un silencio incómodo llena la habitación, que huele a sudor rancio."
    
    show didac_bed_d_mouth sad_Talkingx01
    with dissolve
    
    d "Sí..."

    d "creo..."

    extend " que sí..."
    
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    d "¿A qué coño viene esto ahora?"
    
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    p "Recuerdas que Neus te mordió..."

    p "¿verdad?"
    
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    d "¿Me mordió?"
    
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    pt "¿A qué puñetas está jugando?"
    
    show didac_bed_d_mouth sad_Silentx02
    with dissolve
    
    p "¡Sí!"

    extend " Imbécil,"

    extend " ¡te mordió!"
    
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve
    
    p "No te hagas el idiota ahora."
    
    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    pt "Parece que la fiebre le está afectando más de lo que imaginaba."
    
    show didac_bed_d_mouth sad_Silentx02
    with dissolve
    
    p "El caso es que creo que no fue una simple mordida."
    
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve
    
    d "¿A qué coño te refieres?"
    
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve
    
    p "Creo que para protegerse,"

    p "te inyectó alguna especie de veneno y por eso estás sufriendo de esta manera."
    
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve
    
    d "¡¿Cómo?!"
    
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    pt "Aunque, ahora que lo pienso..."

    pt "si es un veneno para prevenir la violación,"

    pt "actúa de una forma un tanto lenta..."
    
    pt "Creo que más bien es una forma de venganza a largo plazo."
    
    pt "Pero,"

    extend " digo yo..."

    pt "si se permite poder usar un veneno,"
    
    pt "¿por qué no usar uno que actúe de forma inmediata?"
    
    pt "Aunque sea a modo de somnífero para que le dé tiempo a huir..."
    
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve
    
    d "¡Joder!"

    extend " ¡Me cago en...!"
    
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve
    
    d "[protname]..."

    d "Te lo juro,"

    d "¡como me muera,"

    extend " te voy a matar!"

    extend "\n¡Cabrón!"
    
    show didac_bed_d_mouth sad_Talkingx04
    with dissolve
    
    d "Llévame al puto hospital,"

    d "¡por lo que más quieras!"
    
    show didac_bed_d_mouth sad_Talkingx02
    with dissolve
    
    d "¡Y diles toda esta mierda que me has contado ahora!"
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with vpunch
    
    d "Pero que desaparezca ya este maldito dolor..."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx05
    with dissolve
    
    jump afternoon02_Hospital02

label afternoon02_Hospital:
    
    pt "¿Y por qué no llevarlo al hospital?"
    
    pt "Es evidente que esto que le está sucediendo no tiene nada de normal."
    
    pt "Sé muy bien que lo que le hizo, no tiene nombre,"

    pt "y que le debe desear el peor mal del mundo."
    
    pt "Y, aunque en el fondo se lo merezca..."

    pt "Es mi amigo."
    
    pt "No voy a dejar que muera..."
    
    pt "pero,"

    pt "al mismo tiempo..."
    
    pt "tengo la corazonada de que llevarlo al hospital es un terrible error."
    
    menu afternoon02_HospitalSure:
        
        pt "¿Lo llevo al hospital? ¿O intento retenerlo aquí durante más tiempo?"
        
        "<Herirle el orgullo de macho alfa por tenerle miedo a una fiebre alta por ser algo que hasta los niños pasan en casa>":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
            
            jump afternoon02_damageproud
        
        "<Definitivamente tiene que ir al hospital>":
            
            call p_Help
            
            jump afternoon02_Hospital02
                             
label afternoon02_Hospital02:

    p "Tienes razón Dídac,"

    p "lo mejor será llamar a una ambulancia."
    
    if afternoon02_didac_beforeshower_ambulance == True:
        
        show afternoon02_beforeshower_eyebrows sad
        show afternoon02_beforeshower_eyes front01
        show afternoon02_beforeshower_mouth sad_Talking
        with dissolve
        
    else:
        
        show didac_bed_d_blush 02
        show didac_bed_d_mouth sad_Talkingx02
        show didac_bed_d_eyes 06
        show didac_bed_d_eyespup empty
        show didac_bed_d_eyebrows angryx02
        with dissolve
    
    d "Gracias [protname],"

    if afternoon02_didac_beforeshower_ambulance == False:

        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        with dissolve

    d "te lo digo en serio..."

    if afternoon02_didac_beforeshower_ambulance == False:

        show didac_bed_d_eyes 07
        show didac_bed_d_eyespup empty
        with dissolve

    d "estoy hecho mierda."
    
    if afternoon02_didac_beforeshower_ambulance == True:
        
        show afternoon02_beforeshower_eyes right01
        show afternoon02_beforeshower_mouth sad_Silent
        with dissolve
        
    else:
        
        show didac_bed_d_blush 02
        show didac_bed_d_mouth sad_Silentx04
        show didac_bed_d_eyes 06
        show didac_bed_d_eyespup empty
        show didac_bed_d_eyebrows normal
        with dissolve
    
    n "Sales al pasillo, y con el móvil en mano, marcas el número de urgencias."
    
    window hide dissolve
    pause
    
    jump afternoon02_HospitalDefinitiv
    
label afternoon02_HospitalDefinitiv:
    
    play music "audio/sfx/crowd_hospital.ogg" fadein 2.0 fadeout 2.0
    
    scene afternoon02_bg HospitalWaitingRoom with fade
    
    pt "Las sillas de los hospitales no son precisamente el ejemplo de comodidad,"

    pt "pero es mejor eso que nada."

    n "Los responsables de la ambulancia tardaron un buen rato en llegar,"

    n "pero después, todo fue muy fluido."
    
    pt "Por lo visto creen que es un simple catarro,"

    pt "aunque le ha cogido muy fuerte."
    
    n "Estás sentado en la sala de espera del hospital,"

    n "mientras a tu compañero le están dando una ducha fría."

    pt "Deberían haber terminado hace rato..."
    
    n "Por alguna extraña razón, el lugar empieza a oler como a pelo quemado."
    
    pt "¿Y este olor...?"
    
    play sound "audio/sfx/scream_hospital.ogg"
    
    show afternoon02_bg HospitalWaitingRoom with hpunch
    
    gn "{size=72}¡¡¡AAAAAHHH!!!{/size}" # *Scream of terror*
    
    pt "¡¡¿Pero qué...?!!"
    
    n "Escuchas el grito desgarrador de una mujer"

    n "que proviene del lugar en el que habías visto a tu compañero desaparecer en la camilla de urgencias."
    
    n "Te levantas a toda prisa y vas corriendo hacia el interior de la zona restringida para averiguar qué ha sido ese grito."
    
    window hide dissolve
    pause
    
    show afternoon02_bg HospitalCorridor
    show afternoon_nurse notPointing at left
    with fade
    
    n "Te encuentras a una mujer vestida de enfermera contra la pared con una mano temblorosa tapándose la boca,"

    n "completamente petrificada."
    
    p "¡Señora!"

    p "¡¿Qué ocurre?!"
    
    show afternoon_nurse Pointing with dissolve
    
    n "Levantando lentamente y con movimiento errático la mano,"

    n "señala con su dedo índice el interior de una sala de urgencias sin poder articular palabra."
    
    n "A medida que te vas acercando a la puerta,"

    n "el extraño olor a quemado es más fuerte."
    
    p "..."

    p "¿Qué...?"
    
    n "Inundado por un pavor indescriptible, avanzas a más velocidad;"

    n "hasta que tus pies sienten el suelo más resbaladizo de lo normal."
    
    n "Una tonalidad oscura predomina en la habitación, "
       
    n "especialmente encima de la camilla situada en el centro de la sala."
    
    n "Te llevas la mano a la boca al descubrir el origen del olor que llevas un rato percibiendo."
    
    pt "Dios..."
    
    window hide
    pause
    
    play  music "audio/music/kevinmacleod/welcome_to_horror_land.ogg" fadein 2.0 fadeout 2.0

    # Plano Pies cercenados.

    scene afternoon02_bg EmergencyRoom:
        subpixel True
        zoom 1.8 xanchor 0.55 yanchor 0.66
        easein_quad 20.0 zoom 1.0 xanchor 0.57 yanchor 0.67
    with fade
    
    n "En el borde inferior de la camilla ves los restos de unas piernas seccionadas a la altura de la pantorrilla."
    
    n "Observas que el lugar del corte está completamente carbonizado y oscuro."
    
    n "Aun así, la parte que no está quemada"

    n "conserva en casi perfecto estado las zapatillas deportivas,"
       
    n "que inconfundiblemente son las que llevaba tu compañero al llegar al hospital."

    # Plano Brazo cercenado.

    show afternoon02_bg EmergencyRoom:
        subpixel True
        zoom 1.0 xanchor 0.25 yanchor 0.65
        easein_quad 25.0 zoom 1.4 xanchor 0.30 yanchor 0.84
    
    n "Un escalofrío recorre tu cuerpo."
    
    n "Intentas dar un paso hacia atrás, y descubres que aquello que te resultó resbaladizo al entrar,"
       
    n "es hollín grasiento y pegajoso,"
       
    n "que se encuentra esparcido en cada rincón de la sala."
    
    n "Bajo la camilla se encuentran los brazos seccionados de la misma manera que las piernas,"

    n "con las yemas de los dedos carbonizados."
    
    n "Y donde debería estar el cuerpo de tu compañero," 
       
    n "en el centro de la camilla,"

    # De Cabeza a cuerpo entero.

    scene afternoon02_bg EmergencyRoom:
        subpixel True
        zoom 1.2 xanchor 0.4 yanchor 0.48
        ease_quad 25.0 zoom 0.5 xanchor 0.36 yanchor 0.52
    with dissolve
    
    n "se encuentra un montón de ceniza oscura rodeada por otra un poco más grisácea en forma de estrella."
    
    n "Como si su cuerpo se hubiera vuelto ceniza dejándose en el camino las extremidades."
    
    p "..."

    p "¿Qué...?"
    
    n "En tu mente golpeaban esas palabras como si fueran un taladro atravesando tu materia gris sin piedad:"
    
    ne "{i}Ni se te ocurra llevarlo a un hospital, pase lo que pase, y esté como esté,{/i}"

    ne "{i}o nunca más volverás a verlo con vida{/i}."
    
    n "Jamás volviste a ver a Neus en la escuela,"
    
    n "desapareció como polvo en el viento."
    
    n "Los cuerpos de seguridad no supieron encontrar explicación a la muerte de Dídac,"
    
    n "dijeron que había existido algún caso parecido en el pasado,"

    # De cuerpo entero a Plano completo.

    scene afternoon02_bg EmergencyRoom :
        subpixel True
        zoom 0.5 xanchor 0.36 yanchor 0.52
        ease_quad 30.0 zoom 0.2 xanchor 0.0 yanchor 0.0
    
    n "lo llaman {a=https://es.wikipedia.org/wiki/Combustión_espontánea_humana}combustión espontánea{/a}."
    
    n "pero aunque hace décadas que se sabe que existe,"

    n "nadie ha descubierto cómo ocurre ni por qué."
    
    n "Ese grito aterrador de la enfermera..."
    
    n "lo oyes sin falta, torturándote cada noche en tus sueños."
    
    n "Sin duda alguna,"

    n "habías sido el último responsable de la desdicha de tu amigo."
    
    n "Pero incluso, tras ser capaz de apaciguar ese amargo recuerdo,"
       
    n "y a pesar de los años transcurridos,"
    
    n "te sigue siendo imposible olvidar ese olor nauseabundo a carne quemada de tu compañero."
    
    window hide dissolve
    
    pause
    
    aj "Final alternativo 01"

    $ persistent.gameOver_hospital = True # day02
    
    jump gameover
       

label afternoon02_damageproud:

    p "¿Al hospital?"

    p "¿En serio eres tan niñita?"

    p "¿No puedes soportar un simple resfriado?"
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Me cago en tus muertos!"

    d "¡¿Te crees que si fuera un simple resfriado te diría que llamases a una jodida ambulancia?!"
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "Aparte de la cabeza,"

    p "¿te duele algo más?"
    
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Te he dicho que me cuesta levantarme!"

    d "¿Qué más quieres?"

    d "¡¿Una muestra de orina?!"
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "A ver,"

    extend " haremos una cosa."

    p "Te voy a tomar la temperatura," 
       
    p "luego te tomarás otra aspirina,"

    p "y si vemos que la cosa no mejora,"

    extend " te llevo al hospital."

    p "¿Trato hecho?"
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "Humm..."

    p "¿Y bien?"
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "..."

    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "De acuerdo."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    pt "Bien..."

    extend " de este modo quizás gane algo de tiempo para evitar llevarlo al hospital..." 
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    with dissolve
        
    pt "y hasta quizás le baje un poco la fiebre..."
    
    pt "Tengo que averiguar qué demonios le está pasando"

    pt "y por qué no puedo llevarlo al hospital."
    
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyebrows angryx02
    with dissolve

    pt "¿Qué es lo que le habrá hecho?"
    
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    show didac_bed_d_blanket 02
    with dissolve

    n "Consigues tranquilizar ligeramente a tu compañero llevándole la aspirina y un vaso de agua caliente con azúcar."
    
    scene didac_bed_bed empty_cleansweaty
    with fade

    n "Poco después le recomiendas que lo mejor es que se tome una ducha" 
       
    n "mientras le cambias las sábanas y la almohada, pues su cama está hecha un charco de sudor."
    
    scene didac_bed_bed empty_clean
    with dissolve
    
    n "Acepta de mala gana, aunque sabe que son consejos coherentes y necesarios."
    
    window hide dissolve
    
    pause
    
    #scene afternoon02_bg bedroomEmpty
    #scene beds_midday_lightOff_blindDown_DemptyMCempty
    scene beds_midday_lightOff_blindDown_DmessyMCempty
    with dissolve

    d "¡[protname]!"
    
    scene beds_midday_lightOff_blindDown_DemptyMCempty
    with dissolve

    n "Oyes la voz de Dídac, que te llama desde el baño, mientras le estás arreglando la cama."

    p "¡¿Qué pasa tío?!"

    p "¡¿Necesitas algo?!"

    d "..."

    d "¡Bueno...!"

    p "¡¿Qué?!"

    d "¡Que conste que has sido tú el que ha insistido en no llevarme al puto hospital!"

    p "¿¡¡Quieres decirlo de una puñetera vez!!?"
    
    show afternoon02_beforeshower_didac_body
    show afternoon02_beforeshower_blush 01
    show afternoon02_beforeshower_mouth sad_Silent
    show afternoon02_beforeshower_eyes right03
    show afternoon02_beforeshower_eyebrows angry
    show afternoon02_beforeshower_didac_hair
    with dissolve
    #show afternoon02_bg shower_normal_Silent with dissolve

    n "Sales al pasillo para no tener que continuar hablando a voces."
    
    show afternoon02_beforeshower_mouth sad_Talking
    with dissolve

    d "Pues..."

    d "que necesito que me ayudes a ducharme..."
       
    d "No soy capaz de mantenerme en pie..."
    
    show afternoon02_beforeshower_mouth sad_Silent
    with dissolve

    p "¡¿Qué?!"
    
    show afternoon02_beforeshower_eyebrows angryx2
    show afternoon02_beforeshower_eyes front01
    show afternoon02_beforeshower_mouth sadx2_Talking
    with dissolve

    d "¡Oye capullo!"

    d "¡Aún puedes llamar a la jodida ambulancia!"

    d "¡¿Vale?!"
    
    $ afternoon02_didac_beforeshower_ambulance = True
    
    show afternoon02_beforeshower_eyes right01
    show afternoon02_beforeshower_mouth sadx2_Silent
    with dissolve
    
    menu afternoon02_showerorhospital:
        
        pt "¿Será buena idea?"
        
        "<No soy ninguna enfermera, será mejor llevarlo a un hospital>":
            
                call p_Help
            
                pt "¿Y por qué no llevarlo al hospital?"
    
                pt "Es evidente que esto que le está sucediendo no tiene nada de normal."
                
                pt "Sé muy bien que lo que le hizo no tiene nombre,"

                pt "y que le debe desear el peor mal del mundo."
                
                pt "Y, aunque en el fondo se lo merezca..."

                pt "Es mi amigo."
                
                pt "No voy a dejar que muera,"
                
                pt "pero al mismo tiempo..."
                
                pt "tengo la corazonada de que llevarlo al hospital es un terrible error."
                
                menu afternoon02_HospitalSure02:
                    
                    pt "¿Lo llevo al hospital? ¿O intento ayudarle a ducharse?"
                    
                    "<Mejor será ayudarle a ducharse>":
                        
                        call p_Help
            
                        $pl.ch_pts("dp",-1)
                        
                        jump afternoon02_enteringshower
                    
                    "<Definitivamente tiene que ir al hospital>":
                        
                        call p_Help
                        
                        jump afternoon02_Hospital02
    
        "<Mejor será que le ayude a ducharse>":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
            
            jump afternoon02_enteringshower
            
label afternoon02_enteringshower:

    stop music fadeout 3.0

    $ renpy.music.set_volume(1.0, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene d_showerin_compilation:
        subpixel True
        zoom 5.0
        xanchor 0.25 yanchor 0.6
        ease_quad 30.0 xanchor 0.4 yanchor 0.2
    with fade

    n "Entras en el cuarto de baño."

    $ renpy.music.set_volume(0.5, delay=10.0, channel='sfx1')

    n "Es un reducido espacio, en consonancia con el resto del piso;"

    n "y ves a tu compañero sentado en el plato de ducha,"
    
    n "casi sin poder moverse mientras le cae la cascada de agua sobre la cabeza."

    n "Su cuerpo húmedo y desnudo, apenas unos días antes, era uno de los más esculpidos, voluminosos"
       
    n "y con mejor forma física de la escuela,"

    n "ahora, y aunque mantiene un cuerpo musculado y atlético,"

    n "es apenas una imitación reducida y ridícula de lo que fue."

    n "Los mechones de su pelo, pesados ahora por el agua, le ocultan parte del rostro,"

    n "que en este momento parece mucho menos varonil de lo que recuerdas."

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "loopster"
    
    window hide dissolve
    
    pause

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

    d "¡Capullo!"

    extend " No te quedes ahí mirándome,"

    extend " ¡ayúdame a levantarme!"
    
    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve
    
    n "Si antes de ayer te hubieran dicho que ahora estarías viendo desnudo a tu compañero de piso en la ducha" 
       
    n "pidiéndote que le frotes la espalda mientras lo sujetas de pie"

    n "con el agua cálida cayendo sobre vosotros..."

    n "te hubieras puesto a reír."

    p "..."

    p "¿Qué...?"

    p "¿Qué quieres que haga...?"
    
    show d_showerin_eyes 03
    show d_showerin_pupils right03
    show d_showerin_eyebrows sad
    show d_showerin_mouth sad_Talking
    with dissolve

    d "¿Vas a entrar completamente vestido?"
    
    show d_showerin_mouth sad_Silent
    with dissolve

    p "No..."

    extend " supongo que no."

    pt "Esta situación es un tanto bizarra..."
            
    menu afternoon02_keepornotboxers:
        
        pt "Él está desnudo..."
        
        "<Te desprendes de toda tu ropa a excepción de tus boxers>":
            
            call p_Help
            
            play sound "audio/sfx/clothes02.ogg"
            
            $pl.ch_pts("dp",1)
            
            jump afternoon02_keepboxers
        
        "<Te desnudas completamente>":
            
            call p_Help
            
            play sound "audio/sfx/clothes02.ogg"
            
            $pl.ch_pts("dp",2)
            
            jump afternoon02_showernude
            
label afternoon02_showernude:

    n "Estás desnudándote fuera de la ducha"
    
    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows sad
    with dissolve

    n "y te dispones a quitarte el bóxer, que ya te llega por la pantorrilla..."

    if music_play != "bummin_on_tremelo":
        play music "audio/music/kevinmacleod/bummin_on_tremelo.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "bummin_on_tremelo"
    
    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_blush 02
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Talking
    with dissolve
    
    d "[protname]..."

    d "¿Qué coño haces?"

    show d_showerin_mouth sad_Silent
    show d_showerin_eyebrows sad
    with dissolve
    
    p "..."

    p "¿Por qué?"

    show d_showerin_eyes 03
    show d_showerin_pupils front03
    show d_showerin_eyebrows angryx2
    show d_showerin_mouth sad_Talking
    with dissolve
    
    d "No hace falta que te quites los jodidos boxers,"

    extend " hombre..."

    show d_showerin_pupils right03
    with dissolve
       
    d "¿No crees que esta situación ya es jodidamente amariconada de por sí?"
    
    show d_showerin_eyes 02
    show d_showerin_pupils right02
    show d_showerin_blush 03
    show d_showerin_eyebrows angry
    show d_showerin_mouth sad_Silent
    with dissolve
    
    pt "¿Primero se me insinúa y me roza con la cadera, y ahora va de vergonzoso?"
    
    show d_showerin_eyes 03
    show d_showerin_pupils front03
    show d_showerin_blush 02
    with dissolve
    
    p "Sí..."

    p "quizás tengas razón."
    
    play sound "audio/sfx/clothes01.ogg"
    
    show d_showerin_eyes 03
    show d_showerin_pupils right03
    show d_showerin_blush 01
    with dissolve
    
    n "Vuelves a subirte los boxers a su sitio."
       
    jump  afternoon02_showergoing

label afternoon02_keepboxers:

    pt "Aunque se mojen un poco, tampoco va a pasar nada..."
    
    jump afternoon02_showergoing
    
label afternoon02_showergoing:

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "loopster"

    scene d_showerin_compilation:
        subpixel True
        zoom 5.0
        xanchor 0.4 yanchor 0.1
        ease_quad 30.0 xanchor 0.5 yanchor 0.55
    with fade

    n "Entras en la ducha con él,"

    n "dejando la puerta abierta para poder tener algo más de espacio,"

    n "colocas su brazo por encima de tus hombros y le ayudas a levantarse."

    n "Dídac alcanza a coger el jabón, pero se le escapa de las manos,"
       
    n "parece carecer completamente de fuerza y de equilibrio."

    d "A ver,"

    extend " tío..."

    d "te lo digo en serio,"

    d "¿no crees que me debería ver un puto jodido médico?"

    d "Esto que me está pasando no es normal,"

    extend " coño..."

    p "¿Por qué?"

    p "¿Nunca has tenido una fiebre alta?"

    p "Es normal perder un poco de fuerza."

    p "La ducha te hará bien,"

    extend " ya lo verás."

    n "Dídac se sujeta como puede a la pared mientras te agachas a coger la botella de jabón."

    n "Estando de rodillas, tus ojos no pueden evitar fijarse en lo que tienen delante."

    n "En la entrepierna de tu amigo ves el miembro viril más enano que jamás hayas podido imaginar."

    n "Es prácticamente como si estuviera a punto de desaparecer entre la piel."

    p "..."

    pt "Qué raro..."

    if afternoon01_rapedickface == True:

        pt "Cuando ayer tenía la polla encima de esa pobre chica,"

        pt "parecía mucho más grande..."

    else:

        pt "Nunca me había duchado con él tan cerca,"

        pt "por las veces que lo he visto desnudo,"

        p "era obvio que no la tenía tan grande como la mía,"

        # Didac Dick Talk

        pt "pero no recordaba que la tuviera así de diminuta..."
    
    scene afternoon02_bg showering_Silent
    show night05_Cemetery_smoke_comp
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    with fade

    n "Te levantas para intentar no despertar sospechas extrañas y empiezas por enjabonarle el pelo."

    pt "Debería limpiarle algo más que la cabeza..."                                                                         
    
    menu afternoon02_showerproblem:
        
        pt "¿Por dónde debería seguir?"
        
        "<Piernas>" if afternoon02_ShowerPiernas == False:
            
            call p_Help
            
            $ afternoon02_ShowerPiernas = True
            
            $pl.ch_pts("dp",2)
                  
            jump afternoon02_legs
        
        "<Espalda>" if afternoon02_ShowerBack == False:
            
            call p_Help
            
            $ afternoon02_ShowerBack = True
            
            $pl.ch_pts("dp",2)
            
            jump afternoon02_back
            
        "<Parte frontal>" if afternoon02_ShowerAbs == False:
            
            call p_Help
            
            $ afternoon02_ShowerAbs = True
            
            $pl.ch_pts("dp",3)
            
            jump afternoon02_abs

        "<Parte íntima>":
            
            call p_Help
            
            $pl.ch_pts("dp",5)
            
            jump afternoon02_privatepart
            
        "<Ya está lo suficientemente limpio>":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
            
            jump afternoon02_aftershower
            
label afternoon02_legs:

    scene d_showerin_compilation:
        subpixel True
        zoom 5.0
        xanchor 0.24 yanchor 0.8
        ease_quad 30.0 xanchor 0.43 yanchor 0.6
    with fade
    
    n "Al frotarle las piernas, te das cuenta de cuánto volumen ha perdido en realidad," 
       
    n "como exfutbolista, sus piernas eran parte de su orgullo como deportista."

    n "Ahora mantiene los músculos marcados,"

    n "pero lejos queda ese enorme volumen del que tanto se enorgullece."
    
    window hide dissolve
    pause

    jump afternoon02_showerproblem

label afternoon02_back:
    
    scene afternoon02_bg showering_Back:
        afternoon02_bg_showering_Back_move
    show night05_Cemetery_smoke_comp
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    show afternoon02_bg_showering_Back_hand:
        afternoon02_bg_showering_Back_hand_move
    with fade
    
    n "Al frotarle la espalda observas que su piel es ahora suave y delicada,"
       
    n "lejos de aquella espalda voluminosa,"

    n "aunque sigue tersa, marcándose cada músculo dorsal y lumbar."
    
    window hide dissolve
    pause

    jump afternoon02_showerproblem

label afternoon02_abs:

    scene d_showerin_compilation:
        subpixel True
        zoom 5.0
        xanchor 0.4 yanchor 0.5
        ease_quad 30.0 xanchor 0.42 yanchor 0.28
    with fade

    n "Los abdominales, enseña de su orgullo y satisfacción al tenerlos en mejor estado que los míos,"

    n "gracias a su duro entrenamiento,"

    n "y obviamente al tiempo libre que disfruta, y del que por desgracia, a veces yo no dispongo,"

    n "son aún un torso duro y marcado, pero con un menor volumen abdominal notable."

    n "Su pectoral no solo ha perdido toda su dureza, sino que además,"

    n "parece que haya ganado una capa extra de grasa." 

    n "Se notan más suaves y esponjosos de lo que recuerdas," 
       
    n "especialmente cuando os enfrentabais por alguna absurda disputa varonil,"

    n "fuera de clase, o en el piso que compartís."

    jump afternoon02_showerproblem

label afternoon02_privatepart:
    
    scene afternoon02_bg showering_intimate  at Move((.5, 1.3), (0.5, 0.5), 10.0,
                  xanchor="center", yanchor="center"):
        
        zoom 1.3
        ease_quad 15.0 zoom .5

    show night05_Cemetery_smoke_comp
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    with fade

    #show afternoon02_bg_showering_water:
        #afternoon02_bg_showering_water_move
    #show fog_02:
        ##additive 1.0
        #yanchor 0.25
        #afternoon02_bg_showering_smoke_move
    #with fade

    n "Acercas tus manos rebosantes de espuma a sus caderas," 
       
    n "acariciándolas, tienes la sensación de que son mucho más anchas de lo que recordabas."

    n "Continúas pasando por la parte interna de la ingle, tus dedos se deslizan con el agua caliente,"

    n "acariciando su suave y tierna piel..."

    if music_play != "clearWaters":
        play music "audio/music/kevinmacleod/happy/clearWaters.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "clearWaters"

    d "Oye..."

    d "¿Se puede saber qué coño estás haciendo...?" 

    n "Su voz no aparenta estar realmente enojada, parece más de confusión que de sorpresa," 
       
    n "como si fuera algo que esperaba, pero que al mismo tiempo seguía sin creerse."

    p "Perdón,"

    p "estaba distraído pensando en otra cosa..."
    
    window hide dissolve
    pause
    
    jump afternoon02_aftershower
    
label afternoon02_aftershower:

    if music_play != "clearWaters":
        play music "audio/music/kevinmacleod/happy/clearWaters.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "clearWaters"

    scene d_showerin_bg:
        d_showerin_base_close_pos
    show d_showerin_body:
        d_showerin_base_close_pos
    show d_showerin_blush 02:
        d_showerin_expressions_close_pos
    show d_showerin_mouth sad_Silent:
        d_showerin_expressions_close_pos
    show d_showerin_eyes 03:
        d_showerin_expressions_close_pos
    show d_showerin_pupils right03:
        d_showerin_expressions_close_pos
    show d_showerin_eyebrows angry:
        d_showerin_expressions_close_pos
    show d_showerin_hair:
        d_showerin_expressions_close_pos

    show night05_Cemetery_smoke_comp
    show afternoon02_bg_showering_water:
        afternoon02_bg_showering_water_move
    #with fade
    #show afternoon02_bg_showering_water:
        #afternoon02_bg_showering_water_move
    #show fog_01:
        ##additive 1.0
        #afternoon02_bg_showering_smoke_move
    show d_showerin_doors:
        d_showerin_base_close_pos
    with dissolve

    p "Creo que ya estás lo suficientemente limpio..."

    p "¿No crees?"
    
    show d_showerin_eyes 02
    show d_showerin_pupils front02
    show d_showerin_eyebrows sad
    show d_showerin_mouth sad_Talking
    with dissolve

    d "Sí..."

    d "supongo que sí..."

    scene d_showerin_compilation02:
        subpixel True
        zoom 5.0 xanchor 0.4 yanchor 0.1
        ease_quad 15.0 zoom 1.0 xanchor 0.0 yanchor 0.0 
    with dissolve

    n "Una ligera y sutil muestra de pena parece dibujarse en su tono de voz."

    window hide dissolve
    pause

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    play music "audio/music/didac_theme.ogg" fadeout 3.0 fadein 3.0
    
    scene beds_midday_lightOff_blindDown_Dbusy02MCempty
    show beds_D02_morning_lightOff_blindDown
    with fade

    n "Una vez le has aclarado el pelo y has secado su cuerpo entero,"

    n "lo ayudas a vestirse y lo acompañas a la cama."
    
    scene didac_bed_bed over
    show didac_bed_d_body 03
    show didac_bed_d_sweat 00
    show didac_bed_d_blush 02
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    show didac_bed_d_hair 03
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 00
    with fade
    
    window hide dissolve
    pause

    p "Bueno..."

    p "parece que la fiebre te ha bajado bastante... "

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Sí..."

    d "me siento algo mejor,"

    d "tenías razón,"

    d "una ducha me ha sentado muy bien."
    
    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    d "Después de todo,"

    extend " aún sirves para algo..."

    d "Gracias cabrón."
    
    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    with dissolve

    pt "¿Gracias?"

    pt "¿Desde cuándo es tan educado el imbécil de Dídac?"

    pt "Una cosa sí está clara;"

    pt "nada de esto está bien,"

    extend " ni es normal..."

    scene beds_midday_lightOff_blindDown_Dbusy02MCempty
    show beds_D02_morning_lightOff_blindDown
    with fade

    pt "Tengo que aclarar esto,"

    scene beds_afternoon_lightOff_blindDown_Dbusy02MCempty
    show beds_D02_afternoon_lightOff_blindDown
    with Dissolve (1.0)

    pt "mañana sin falta."
    
    scene beds_night_lightOff_blindDown_Dbusy02MCbusy
    show beds_D02_night_lightOff_blindDown
    with Dissolve (1.0)
    
    window hide dissolve
    pause
    
    jump beforemorning03
    

