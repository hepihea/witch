default night03_NeusFall_NotPanties = False

default morning03_Meritxell_Phonenumber_Accepted = False
default night03_PedreraHome = False
default night03_MidnightProblem04_GoUp_Boolean = False
default night03_MidnightProblem03_Gentleman_Gentes = False
default night03_SaySomething_KissNo = False
default afternight03_Didac_AfterShower_Melons = False
default morning03_Neus_Wall_Grabbing = False
default morning03_Neus_Wall_Bite_Afraid = False

# NEW
default night03_barmaninsult_01_AskedWater = False
default night03_barmaninsult_02_YouDefendeYourself = False

default night03_SaySomething_KissSucces_Cond = False

label beforemorning03:

    $ pdaytime = "03_beforeMorning"

    $ p_ao_n_horns = "_cut01"

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    
    ##Viernes
    
    play music "audio/sfx/birds01.ogg" fadeout 3.0 fadein 3.0

    scene beds_morning_lightOff_blindDown_Dbusy02MCbusy
    show beds_D02_morning_lightOff_blindDown
    with fade
    
    $ renpy.notify("Day 03")
    
    d "Kgaah..."
    
    n "Lo normal es que la dichosa alarma te despierte."
    
    d "Ggg..."

    extend " kkk..."
    
    n "Pero los gruñidos de dolor de Dídac consiguen arrancarte de los brazos de Morfeo."
    
    scene beds_morning_lightOff_blindDown_Dbusy02MCmessy
    show beds_D02_morning_lightOff_blindDown
    with dissolve
    
    n "Te levantas y te acercas a su cama sin encender las luces por temor a causarle otra molestia más."
    
    n "La tenue luz que se filtra por las pequeñas rendijas de la persiana"
    
    n "ilumina la cama totalmente desbaratada,"

    n "las sábanas arrugadas y visiblemente empapadas en sudor."
    
    p "..."

    p "¿Dídac...?"
    
    scene didac_bed_bed over
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade
    
    n "Al primer vistazo no logras reconocer a la persona que está frente a ti."
    
    n "Un cuerpo mucho menos voluminoso que la noche anterior en la ducha,"
    
    n "aparentemente más delicado, con más curvas y de menor estatura..."
    
    p "..."

    pt " ¿Qué...?"

    extend " ¿Qué le pasa en el pecho?"
    
    n "Acercas tus dedos a su pecho musculado, que siempre había sido su orgullo,"

    n "y que ahora parecía incluso más hinchado que el día anterior."
    
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve
    
    d "Ahh..." # *soft moans of pain*

    extend " Ggaaah..."
    
    show didac_bed_d_blush 03
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyebrows angryx02
    with dissolve
    
    n "Nunca habrías imaginado oír semejantes gruñidos y suspiros salir de los labios de Dídac." 
       
    n "Su voz no solo era más débil, sino... distinta."
    
    p "Maldita sea,"

    p "Dídac..."

    extend " ¿Qué demonios te pasa?"
    
    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    with dissolve
    
    d "Aahh..."   
    
    show didac_bed_d_mouth sad_Silentx01
    with dissolve
    
    n "Parece que por fin ha conseguido tranquilizarse."
    
    show didac_bed_MC_handonfront
    with dissolve
    
    n "Percibes que que la fiebre ha disminuido."
    
    n "Sus facciones faciales parecen haberse suavizado, los rasgos de su mandíbula son mucho menos marcados."
    
    n "Sientes la mano de Dídac buscando la tuya"

    n "y casi inconscientemente se la sujetas."
    
    show didac_bed_d_mouth sad_Talkingx01
    with dissolve   
    
    d "[protname],"

    extend " por favor..."

    extend "\nPerdóname..."
    
    show didac_bed_d_mouth sad_Silentx04
    with dissolve    
    
    n "Parece hablar en sueños."
    
    n "Decir que esto es extraño es quedarse corto."
    
    n "Si el día anterior alguien te hubiera dicho que estarías preocupado por el capullo de Dídac,"
    
    n "le hubieras metido una colleja considerable."
    
    n "Y sin embargo,"

    extend " aquí estás."

    n "Con una mano en su frente húmeda y con la otra sujetándole la suya."
    
    pt "Hace solo dos días esta misma mano me derrotó en uno de nuestros habituales pulsos..."
    
    show didac_bed_d_mouth sad_Talkingx01
    with dissolve   
    
    d "Aahh..."
    
    show didac_bed_d_mouth sad_Silentx01
    with dissolve  
    
    pt "¿Y si realmente esa chica lo ha envenenado y no la encuentro en clase?"
    
    pt "¿He hecho bien en no llevarlo al hospital?"
    
    pt "Aunque..."

    extend " desde luego, esto no parece un resfriado común..."
        
    pt "de hecho,"

    extend " no se parece a ninguna enfermedad que haya visto antes,"

    extend " ni siquiera en una película..."
    
    menu beforemorning03_Hospital_Question:
        
        pt "¿Aún estaré a tiempo de llevarlo al hospital? O quizás es mejor hablar con esa extraña chica..."
        
        "<Aunque más vale tarde que nunca, es mejor llevarlo al hospital>":
            
            call p_Help
            
            jump afternoon02_HospitalDefinitiv
        
        "<Ir a clase a buscar a la chica extraña>":
            
            call p_Help
            
            jump morning03

label morning03:

    $ meyesc = "_red"
    
    stop music fadeout 3.0
    
    scene morning02_bg schoolwall with fade
    
    pt "{i}A menos que quede preñada...{/i}."

    pt "¡¿Qué diablos quiso decir con esta frase?!"

    n "Justo la clase en la que estás con Neus acaba de terminar,"
    
    n "y te plantas cerca de la puerta para esperarla."
    
    if pl.mp >= 0:
         
        $pl.ch_pts("mp",1)
        
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 0[hm]")
                                
        jump morning03_RemeetingMeritxellagain
        
    else:
        
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 0[hm]")
                
        jump morning03_Meritxelldesapearing
    
label morning03_Meritxelldesapearing:
    
    play music "audio/music/meritxell_theme.ogg" fadeout 3.0 fadein 3.0

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 00:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Silentx06:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows suspiciousx02:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve

    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_eyes 04:
        #m_face_atright_position
    #show m_exp_piris front04:
        #m_face_atright_position
    ##show m_pupils front04a:
        ##m_face_atright_position
    #how m_exp_mouth sad_Silentx03:
        #m_face_atright_position
    #show m_exp_eyebrows suspiciousx02:
        #m_face_atright_position
    #with dissolve

    pause

    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "..."
    
    stop music fadeout 3.0
    
    scene morning02_bg schoolwall 
    with dissolve
    
    n "Ves pasar a la atractiva chica de ayer,"

    n "que te dirige una mirada de pocos amigos justo antes de desaparecer por la puerta."
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0
    
    show neus_body_full day03:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_blush 00:
        neus_exp_atright_position
    show neus_exp_mouth happy_Silentx05:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_eyebrows normal:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
label morning03_Neusmeeting:
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0
    
    show neus_body_full day03:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_blush 00:
        neus_exp_atright_position
    
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_mouth happy_Silentx04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
       
    n "Poco después ves llegar a Neus."
    
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_mouth happy_Silentx05
    with dissolve
    
    pt "Maldita hija de una hiena..."
    
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth sadbiting_Silentx05
    with dissolve
    
    n "El contraste de su alegre actitud con el estado de salud de Dídac consigue ponerte de los nervios."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "Vaya..."

    extend " ¿A qué viene este mal genio por la mañana, [protname]?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    jump morning03_Neus

    
label morning03_RemeetingMeritxellagain:
    
    play music "audio/music/meritxell_theme.ogg" fadeout 3.0 fadein 3.0

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 02:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Talkingx03:
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
    #how m_exp_eyes 03:
        #m_face_atright_position
    #show m_exp_piris front03:
        #m_face_atright_position
    ##show m_pupils front03a:
        #m_face_atright_position
    #show m_exp_mouth happy_Talkingx03:
        #m_face_atright_position
    #show m_exp_eyebrows normal:
        #m_face_atright_position
    #ith dissolve
    
    gm "Buenos días, [protname]."
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve

    menu morning03_RemeetingMeritxell:
        
        pt "¿Otra vez ella?"
        
        "Buenos días...":
            
            call p_Help
            
            $pl.ch_pts("mp",2)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_goodmorning
        
        "¿Otra vez tú...?":
            
            call p_Help
            
            $pl.ch_pts("mp",-2)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
        "Lo siento, tengo prisa.":
            
            call p_Help
            
            $pl.ch_pts("mp",-2)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
label morning03_MeetingMeritxell_bad:

    $ meyesc = "_goat"
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front04a
    show m_exp_mouth sad_Silentx02
    show m_exp_eyebrows angryx04
    with dissolve

    $ meyesc = "_red"
    show m_exp_eyes 04
    show m_exp_piris front04
    with Dissolve(0.5)
    
    # show m_exp_eyes 04
    # show m_exp_piris front04
    # #show m_pupils front04a
    # show m_exp_mouth sad_Silentx02
    # show m_exp_eyebrows angryx04
    # with dissolve
    
    gm "..."
    
    stop music fadeout 3.0
    
    scene morning02_bg schoolwall 
    with dissolve
    
    pt "Hummm..."

    pt "quizás podría haber sido un poco más amable con ella..."
    
    jump morning03_Neusmeeting
    
label morning03_MeetingMeritxell_goodmorning:
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Veo que hoy tampoco ha venido Dídac..."
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "¿Le pasa algo grave?"
    
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows serious
    with dissolve

    menu morning03_SomethingSerious:
        
        pt "¿A qué viene ese interés por Dídac?"
        
        "No, tranquila, no es nada grave...":
            
            call p_Help
            
            $pl.ch_pts("mp",1)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_gladtohear
        
        "¿Y a ti qué te importa?":
            
            call p_Help
            
            $pl.ch_pts("mp",-4)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
label morning03_MeetingMeritxell_gladtohear:
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Vaya,"

    extend " me alegro..."
    
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "Parece que te preocupas por Dídac..."

    extend " Nunca te he visto hablando con él..."
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "Bueno,"

    extend " en realidad, quien me interesa no es él..."
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Pero, si te soy sincera,"

    gm " me ha parecido una buena excusa para romper el hielo contigo."
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows sadx01
    with dissolve
    
    p "¿Romper el hielo?"

    extend " ¿Para hablar conmigo?"
    
    pt "¿A eso lo llama \"romper el hielo\"?"
    
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Dime [protname],"

    extend " ¿tienes novia?"
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve
    
    p "Euh..."
    
    menu morning03_Meritxell_Girlfriend:
        
        pt "¡¿No está siendo demasiado directa?!"
        
        "Sí.":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_YesGF
        
        "No.":
            
            call p_Help
            
            $pl.ch_pts("mp",+2)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_NoGF
            
        "No es de tu incumbencia.":
            
            call p_Help
            
            $pl.ch_pts("mp",-5)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
label morning03_MeetingMeritxell_YesGF:
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "Vaya..."

    extend " No tenía ni idea..."
    
    show m_exp_mouth serious_Silentx01
    with dissolve
    
    pt "¿Por qué me da la sensación de que la conversación aún no termina aquí...?"
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "¿Cómo se llama?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows serious
    with dissolve
    
    menu morning03_Meritxell_GFname:
        
        pt "¡¿El nombre de mi novia ficticia?!"
        
        "¿Y a ti que más te da?":
            
            call p_Help
            
            $pl.ch_pts("mp",-5)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
        
        "Lo siento, te he mentido, no tengo novia.":
            
            call p_Help
            
            $pl.ch_pts("mp",+1)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_WhyLie
            
        "No tengo novia, solo quería deshacerme de ti.":
            
            call p_Help
            
            $pl.ch_pts("mp",-5)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
label morning03_MeetingMeritxell_WhyLie:
    
    show m_exp_eyes 00
    show m_exp_piris front00
    #show m_pupils front00a
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "¿Y por qué me has mentido?"
    
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows serious
    with dissolve
    
    menu morning03_Meritxell_GFLie:
        
        pt "¡¿Quizás porque me estás incomodando con esta pregunta?!"
        
        "Porque creo que es un tema personal que no te incumbe en absoluto.":
            
            call p_Help
            
            $pl.ch_pts("mp",-5)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
        
        "Porque me has puesto nervioso...":
            
            call p_Help
            
            $pl.ch_pts("mp",+1)
            $pl.ch_pts("np",-1)
                  
            jump morning03_MeetingMeritxell_NoGF
            
        "No lo sé...":
            
            call p_Help
            
            $pl.ch_pts("mp",+1)
            $pl.ch_pts("np",-1)
            
            jump morning03_MeetingMeritxell_NoGF
    
label morning03_MeetingMeritxell_NoGF:
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Vaya..."

    extend " me alegro..."
    
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve
    
    pt "¿Se puede saber a qué viene esto?"
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Dime,"

    extend " ¿haces algo mañana a mediodía?"
    
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve
    
    n "Tienes la extraña sensación de que alguien te observa y te entran unos escalofríos."
    
    menu morning03_Meritxell_ForTomorrow:
        
        pt "¿Me está proponiendo una cita?"
        
        "La verdad es que no.":
            
            call p_Help
            
            $pl.ch_pts("mp",+2)
            $pl.ch_pts("np",-3)
                  
            jump morning03_Meritxell_Phonenumber
        
        "Lo tengo ocupado, lo siento.":
            
            call p_Help
            
            $pl.ch_pts("mp",-6)
            $pl.ch_pts("np",+1)
                  
            jump morning03_MeetingMeritxell_bad
            
label morning03_Meritxell_Phonenumber:
    
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¡Perfecto!"

    extend " Aquí te dejo escrito mi número de teléfono,"
    
    $ morning03_Meritxell_Phonenumber_Accepted = True
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "si te apetece hacer algo,"

    $ meyesc = "_goat"
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows normal
    with Dissolve(0.5)

    $ meyesc = "_red"
    show m_exp_eyes 05
    show m_exp_piris front05
    with dissolve

    gm "llámame."
    
    scene morning02_Txell_Kiss:
        subpixel True
        truecenter
        zoom 1.2 xpos 0.2 ypos 0.2
        easein_quad 6.0 zoom 0.8
    with fade
    
    n "Sorprendido, ves cómo se te acerca y te da un beso en la mejilla para,"

    n "justo después, salir por la puerta."

    scene morning02_bg schoolwall 
    with fade
    
    p "..."

    pt "Me da su número de teléfono,"

    pt "pero no me dice cómo se llama,"

    extend " ni me lo escribe en el papel,"
    
    p "..."

    pt "Pero no se puede negar que está un rato buena..."
    
    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0
    
    show neus_body_full day03:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_exp_blush 00:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx05:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris left02:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    ne "Haciendo amistades..."

    extend " ¿Eh?"
    
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx002
    with dissolve
    
    ne "Hay que reconocer que sabes elegirlas..."
    
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_iris left02:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx04
    with dissolve
    
    jump morning03_Neus
    
label morning03_Neus:

    p "Neus..."

    extend "\nDídac"

    extend " está... "

    p "Me dijiste que no lo llevara al hospital..."

    extend " Sabes lo que le está pasando,"

    extend " ¿verdad?"

    p "¡Ayer parecía que se iba a morir!"
    
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris front02:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx04:
        neus_exp_atright_position
    show neus_exp_tears empty:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    with dissolve

    ne "Grita más alto, anda..."

    ne " creo que no te han oído en recepción."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¿Por qué me dijiste que no puedo llevarlo al hospital?"
    
    show neus_exp_iris front03
    with dissolve

    ne "Hmm..."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth happy_Talkingx03
    with dissolve
        
    ne "quizás porque quería que muriese"

    extend " y que tú parecieras el culpable..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx04
    with dissolve

    p "¿Qué...?"
    
    pt "Será hija de..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "No..."

    extend " nunca te haría eso,"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 04
    show neus_exp_iris right04
    show neus_exp_mouth sad_Talkingx03
    with dissolve

    ne "además..."

    extend " tampoco le tengo tanto odio a tu amigo. "
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    ne "En realidad,"

    extend " más que un castigo,"

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne " lo que estoy haciendo es darle una lección."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¿Pero de qué diablos estás hablando?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "¿Cómo ves a tu amigo?"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Talkingx03
    with dissolve

    ne " ¿Qué crees que le está ocurriendo?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Tú..."

    extend " ¿de qué dirías que estoy hablando?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "..."

    p "No lo sé,"

    extend " está muy cambiado..."

    extend " físicamente no es el de antes..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth sad_Talkingx04
    with dissolve

    ne "¿Y psicológicamente?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¡Y yo qué sé!"

    show neus_exp_eyebrows serious
    show neus_exp_eyes 02
    show neus_exp_iris front02
    show neus_exp_mouth happy_Silentx04
    with dissolve

    p "Tampoco lo parece..."

    show neus_exp_eyebrows angryx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx05
    with dissolve

    p "¡Es como si tuviera a un extraño durmiendo en mi habitación!"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "¿Y ese alguien dirías que es hombre o mujer?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¿Qué?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    ne "Antes has dicho que parecía como si su cuerpo estuviera cambiando..."

    extend " ¿No es verdad?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¡Lo único que sé es que no parece él mismo!"
    
    p "¡Su fiebre era tan grave que apenas se podía mantener en pie!"
    
    p "¡Cuando no dormía solo oía sus gritos y sus gemidos de dolor!" 
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
 
    ne "Tranquilízate, [protname],"

    extend " estás alzando la voz..."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    p "..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "¿Y qué dirías que es lo que está cambiando en él?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "..."

    p "No sé..."

    extend " ha perdido peso..."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx04
    with dissolve

    ne "¿Solo eso?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "No..."

    p "No tiene la misma masa muscular de hace dos días,"

    extend " y..."

    extend " parece que haya encogido."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth sadbiting_Silentx02
    with dissolve

    ne "Humm..."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_eyes 01
    show neus_exp_iris left01
    show neus_exp_mouth sad_Talkingx02
    with dissolve
        
    ne "Vaya..."

    extend " Qué cosas más raras para ser un resfriado o una enfermedad..."

    show neus_exp_eyebrows surprisex01
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_mouth sad_Talkingx002
    with dissolve

    ne "¿No crees?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    p "¡¿Y cómo quieres que yo lo sepa?!"
    
    p "¡Tú sabías que se pondría enfermo!"

    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 04
    show neus_exp_iris front04
    with dissolve
    
    p "¡Por Dios!"

    show neus_exp_mouth happy_Silentx05
    with dissolve

    p "¡Me amenazaste con que si lo llevaba al hospital no lo volvería a ver con vida!"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx04
    with dissolve
    
    ne "¿Vas a pegarme?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿Qué?"
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 03
    show neus_exp_iris left03
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    p "¡No!"

    p "¡Solo quiero ayudar a mi amigo!"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    p "¿Qué puñetas me estás ocultando?"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 02
    show neus_exp_iris left02
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "¿De verdad hace falta que te lo diga...?"

    show neus_exp_eyebrows sadx02
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Talkingx02
    with dissolve

    ne "Mis palabras no cambiarán lo que tus ojos han visto."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_eyes 03
    show neus_exp_iris front03
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "Es más..."

    extend " si te hubiera dicho la verdad ayer,"

    extend " tampoco me hubieras creído."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "Sin embargo hoy..."

    extend " ya te veo más receptivo."
    
    show neus_exp_eyebrows normal
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    

    
    menu morning03_Neus_Wall:
        
        pt "Esta tía me está tomando por imbécil, ¿o qué?"
        
        "<Cogerla por las muñecas contra la pared para demostrar tu enfado>":
            
            call p_Help
            
            $pl.ch_pts("np",4)
            
            $ morning03_Neus_Wall_Grabbing = True
                  
            jump morning03_Neus_Wall_Against
        
        "<Retener tus ganas de ponerla contra la pared>":
            
            call p_Help
            
            $pl.ch_pts("np",2)
            
            jump morning03_Neus_Wall_Against_WhatsHappening
            
label morning03_Neus_Wall_Against:
    
    play music "audio/music/alcaknight/bury_it.ogg" fadeout 0.2 fadein 0.1
    
    play sound "audio/sfx/grabarm01.ogg"
    
    scene N_Against_bg
    show N_Against_N_body tensed_shadow
    show N_Against_N_blush 01:
        N_Against_N_expressions_position
    show N_Against_N_eyes 01:
        N_Against_N_expressions_position
    show N_Against_N_pupils front_01:
        N_Against_N_expressions_position
    show N_Against_N_eyebrows surprise:
        N_Against_N_expressions_position
    show N_Against_N_glasses:
        N_Against_N_expressions_position
    show N_Against_N_mouth sad_Talking:
        N_Against_N_expressions_position
    show N_Against_N_hair_front:
        N_Against_N_expressions_position
    show N_Against_P_Arm
    show N_Against_P_Body
    with hpunch

    n "La agarras por las muñecas contra la pared acercándote a ella," 
    
    show N_Against_N_blush 02
    show N_Against_N_eyes 01
    show N_Against_N_pupils front_01
    show N_Against_N_eyebrows sad
    show N_Against_N_mouth sadbiting_Silent
    with dissolve
       
    n "hasta prácticamente sentir su aliento."
    
    show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "Caray, [protname]..."

    extend " qué fuerte eres."

    show N_Against_N_mouth sadbitingx02_Silent
    show N_Against_P_Body
    with dissolve

    pt "Suerte que es hora de clase y no hay nadie por los pasillos,"

    pt "porque no sabría cómo explicar esta situación..."
    
label morning03_Neus_Wall_Against_WhatsHappening:
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_N_mouth sadbitingx02_Silent
        show N_Against_P_Body Talking
        with dissolve
        
    else:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 04
        show neus_exp_mouth happy_Silentx03
        with dissolve

    p "¡Neus!"

    extend " ¡¿Qué le está pasando?!"
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_N_blush 01
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_eyebrows angry
        show N_Against_N_mouth happy_Talking
        show N_Against_P_Body
    else:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Talkingx08
    with dissolve
    
    ne "¿No le has notado las caderas más anchas?"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx06
    with dissolve

    ne "¿La piel del cuerpo y del rostro más suave?"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx07
    with dissolve
        
    ne "¿El pecho un poco más voluminoso?"
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_N_mouth happyx02_Silent
    else:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Silentx04
    with dissolve

    p "..."
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body Talking
    else:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx03
    with dissolve
       
    p "Sí..."
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body
        show N_Against_N_mouth sad_Talking
    else:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "Esta misma noche,"

    extend " tu amigo será por completo una chica."
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body Talking
        show N_Against_N_mouth happyx01_Silent
    else:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Silentx03
    with dissolve
        
    p "¿Qué?"
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body
        show N_Against_P_Arm notTensed
        with dissolve
    else:
        
        jump morning03_Neus_Wall_Against_OhComeon

    
    n "Dejas de apretar con tanta fiereza sus hombros."
    
label morning03_Neus_Wall_Against_OhComeon:
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth happy_Talking
    
    else:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx08
    with dissolve

    ne "Ohh..."

    extend " vamos..."

    extend "\nme dirás que no has notado los cambios... "
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body Talking
        show N_Against_N_mouth happyx01_Silent
        with dissolve
    
    else:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Silentx04
        with dissolve
    
    p "Una cosa es ver algunos cambios..."

    extend " otra muy distinta;"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¡es una inversión de sexo!"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Silentx05
    with dissolve
    
    p "Pero..."

    extend " ¿Cómo es...?" 
    
    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body
        show N_Against_N_mouth happy_Talking
        with dissolve
    
    else:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx08
        with dissolve

    ne "Por la mordida."

    if morning03_Neus_Wall_Grabbing == True:
        show N_Against_P_Body
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_eyebrows angry
        show N_Against_N_mouth happyx02_Silent
    
    else:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx08
    with dissolve
    
    if morning03_Neus_Wall_Grabbing == True:
        
        jump morning03_Neus_Wall_Bite_Question
        
    else:
        
        jump morning03_Neus_Wall_Against_RelaxIwontbiteyou
        
     
    menu morning03_Neus_Wall_Bite_Question:
        
        pt "¡¿Mi compañero se está convirtiendo en chica por ese mordisco?!"
        
        "<Apartar tus manos por temor a que te muerda>":
            
            call p_Help
            
            $pl.ch_pts("np",2)
            
            $ morning03_Neus_Wall_Bite_Afraid = True
                  
            jump morning03_Neus_Wall_Bite
        
        "<Volver a agarrarla con fuerza para que no se mueva>":
            
            call p_Help
            
            $pl.ch_pts("np",3)
            
            jump morning03_Neus_Wall_Bite
            
label morning03_Neus_Wall_Bite:
        
    if morning03_Neus_Wall_Bite_Afraid == True:
    
        hide N_Against_P_Body
        hide N_Against_P_Arm
        show N_Against_N_blush 01
        show N_Against_N_body tensed
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_eyebrows angry
        show N_Against_N_mouth happyx03_Silent
        with dissolve

        n "Te apartas instintivamente de ella."
    
        show N_Against_N_body relaxed
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_eyebrows surprise
        show N_Against_N_mouth happy_Talking
        with dissolve
        
    else:
        
        show N_Against_P_Arm
        show N_Against_N_eyebrows surprise
        show N_Against_N_blush 02
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Talking
        with dissolve
        
        ne "Caray..."

        extend " me sorprendes, [protname]..."
        
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        with dissolve
        
        ne "Pensé que te apartarías enseguida cuando te dijera lo peligroso que puede ser uno de mis mordiscos..."
        
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        with dissolve
        
        ne "Pero quizás te he subestimado..."
        
        show N_Against_N_mouth sadbitingx02_Silent
        with dissolve
        
        p "..."
        
        pt "No las tengo todas..."

        extend " la verdad..."
        
        show N_Against_N_eyebrows surprise
        show N_Against_N_blush 01
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth happy_Talking
        with dissolve
        
label morning03_Neus_Wall_Against_RelaxIwontbiteyou:
    
    if morning03_Neus_Wall_Grabbing == False:

        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx04
        
        p "..."
        
        show neus_exp_eyebrows surprisex02
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx04
    with dissolve
        
    ne "Tranquilo..."

    extend " no te voy a morder..."

    if morning03_Neus_Wall_Grabbing == False:

        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne "bueno..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_blush 03
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Talkingx08
        
    else:

        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_eyebrows surprise
        show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "a menos que quieras,"

    extend " claro..."
    
    if morning03_Neus_Wall_Grabbing == False:
        
        show neus_exp_blush 03
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sadbiting_Silentx05
    
    else:

        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_eyebrows sad
        show N_Against_N_mouth sadbitingx03_Silent
    with dissolve

    ne "..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_blush 02
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Talkingx04
    else:

        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_eyebrows sad
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "No..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx004
    with dissolve

    ne "aunque te mordiera ahora,"

    extend " tampoco te pasaría nada."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_blush 01
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx03
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "¿Entonces?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_blush 01
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx02
    
    if morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
        show N_Against_N_blush 00
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_eyebrows surprise
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "No quiero aburrirte,"

    extend " y dicho sea de paso,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx05
    with dissolve

    ne "tampoco te voy a revelar todos mis secretos"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Talkingx02
    else:
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_eyebrows angry
        show N_Against_N_mouth sad_Talking
    with dissolve
        
    ne "para que luego quieras denunciarme a la policía o algo por el estilo..."
    
    if morning03_Neus_Wall_Grabbing == False: 
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx03
    else:
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_eyebrows sad
        show N_Against_N_mouth happy_Talking
    with dissolve
        
    ne "por ahora sería simplemente tu palabra contra la mía."
        
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Silentx03
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "Neus..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx02
    with dissolve

    p "sé que mi amigo fue un capullo integral..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx02
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_mouth sad_Silentx04
    with dissolve
       
    p "¿Pero no crees que tampoco se merece tal castigo?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Talkingx04
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "¿Acaso sugieres que ser mujer es un castigo?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sadbiting_Silentx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "¡¿Qué?!"

    extend " ¡No!"

    extend "\n¡Yo no he dicho eso!"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
        show N_Against_N_mouth sad_Talking
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
    with dissolve

    ne "Has dicho,"

    extend "\n{i}¿no crees que tampoco se merece tal castigo?{/i}."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx02
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx005
    with dissolve

    ne "¿En qué te basas para decir que convertir a alguien en mujer puede suponer un castigo?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Silentx03
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking

        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "Es algo malvado si lo haces en contra de su voluntad,"

    extend " Neus."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Talkingx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body

        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_blush 01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "En eso te doy la razón... "
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx04
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking
    
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "Entonces..."

    extend " ¿Puedes ayudar a Dídac?"
    
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
        
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_blush 00
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Puedo."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx03
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "Pero no quiero."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Silentx04
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking

        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happyx02_Silent
    with dissolve

    p "Pero..."

    extend " ¡¿Por qué?!"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth happy_Talkingx08
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
    
        show N_Against_N_eyebrows surprise
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "¿Por qué debería?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx02
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
    with dissolve
        
    ne "No es alguien que me caiga especialmente bien..." 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx02
    else:
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
    with dissolve

    ne "más bien todo lo contrario."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Talkingx03
    else:
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Siempre ha estado mofándose de mí,"

    extend " poniéndome motes para ponerme en ridículo;"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx04
    else:
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "como hobbit de Mordor,"

    extend " Quasimodo de Transilvania,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx02
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx05
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "que no podría ponérsela dura ni a un pedófilo,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Talkingx04
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "o que soy la versión antropomórfica de la {a=https://es.wikipedia.org/wiki/Comic_Sans}Comic Sans{/a}."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx06
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Haciéndome sentir a menudo como si fuera una atracción de feria,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_mouth sad_Talkingx07
    with dissolve

    ne "riéndose a carcajadas en los pasillos,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Talkingx06
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "con esos capullos con los que suele frecuentar cuando no estás con él,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 04
        show neus_exp_iris down04
        show neus_exp_mouth sad_Talkingx07
    with dissolve

    ne "y a menudo incluso en medio de la clase"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx02
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_mouth sad_Talkingx09
    with dissolve

    ne "mofándose de la graduación de mis gafas y de mi estatura."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx03
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Silentx05
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Talkingx06
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Como cuando los escuché murmurar que sería la novia perfecta,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Talkingx08
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "ya que, según él,"

    extend " no me haría falta ponerme ni de rodillas para hacerle una mamada."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx07
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx03
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_mouth sadbiting_Silentx07
    with dissolve

    pt "Cuando no está conmigo,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_mouth sadbiting_Silentx06
    with dissolve

    pt "y se junta con ciertas \"amistades\" de por aquí,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx05
    with dissolve

    pt "reconozco que su actitud se vuelve realmente detestable..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris right04
        show neus_exp_mouth sadbiting_Silentx04
    with dissolve

    pt "a veces ni conmigo sabe mantener el pico cerrado;"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sadbiting_Silentx04
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_mouth sad_Silent
    with dissolve

    pt "Y aunque eso,"

    extend " desde luego, no es ninguna excusa..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_mouth sadbiting_Silentx05
    with dissolve

    pt "Nunca me imaginé que ayer llegaría tan lejos..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx06
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "Si de mí depende,"

    extend " se puede quedar tal y como está..." 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Talkingx02
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "es más,"

    extend " creo que mejorará como persona."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Silentx02
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happyx02_Silent
    with dissolve
    
    pt "Maldito seas Dídac,"

    pt "Si no fuera porque te conozco desde que tengo uso de razón..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Silentx02
    
    elif morning03_Neus_Wall_Grabbing == True:

        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body Talking

        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "Yo no opino igual..."

    extend " quizás se merezca la expulsión,"

    extend " o que sea juzgado por la justicia,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Silentx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "pero no se merece lo que le estás haciendo, Neus..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Silentx05
    with dissolve

    p "Si hubieras hablado conmigo,"

    extend " yo habría..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sad_Talkingx07
    
    elif morning03_Neus_Wall_Grabbing == True:

        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Porque necesito de la ayuda de un hombre para defenderme..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx08
    
    elif morning03_Neus_Wall_Grabbing == True:

        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "¿Verdad?"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx05
    
    elif morning03_Neus_Wall_Grabbing == True:

        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx05
    
    elif morning03_Neus_Wall_Grabbing == True:

        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "No,"

    extend " gracias."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx04
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Talkingx07
    
    elif morning03_Neus_Wall_Grabbing == True:

        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Sé defenderme..."
    
    if morning03_Neus_Wall_Grabbing == False:

        show neus_exp_eyebrows angryx02
        show neus_exp_eyes 08
        show neus_exp_iris front08
        show neus_exp_mouth happy_Silentx05
        with dissolve

        p "..."

        show neus_exp_eyebrows serious
        show neus_exp_blush 01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx03

    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_P_Body
            show N_Against_P_Arm notTensed
            show N_Against_N_mouth sad_Silent
            with dissolve
            n "Decides relajar la situación soltándola de las manos."

            hide N_Against_P_Body
            hide N_Against_P_Arm
            show N_Against_N_body tensed

        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "¿Hasta dónde llegarías para ayudar a tu amigo?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 02
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sadbiting_Silentx02
    
    elif morning03_Neus_Wall_Grabbing == True:
        if morning03_Neus_Wall_Bite_Afraid == False:
            show N_Against_N_body relaxed
        show N_Against_N_mouth happyx02_Silent
    with dissolve

    p "Hasta donde haga falta."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sadbiting_Silentx03
    with dissolve
    
    p "Te prometo,"

    extend " que me aseguraré de que no se vuelva a repetir nada de lo que me has comentado. "

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Talkingx04
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "¿Le harás de niñera para vigilarlo?"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx02
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "Si hace falta,"

    extend " sí."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx04
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth happyx02_Silent
    with dissolve

    ne "Hmm..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx03
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Bien..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne " entonces hagamos un"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth happy_Talkingx07
        with dissolve

    extend " {size=32}{b}pacto{/b}{/size}."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 02
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Talkingx02
    else:
    
        show N_Against_N_eyebrows surprise
        show N_Against_N_blush 02
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
    with dissolve

    ne "Cena conmigo \"tres\" veces:"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Hoy, viernes,"

    extend " mañana, sábado,"

    extend " y pasado mañana, domingo."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 01
        show neus_exp_iris right01
        show neus_exp_mouth sad_Talkingx004
    with dissolve
    
    ne "Y,"

    extend " al final de la última noche,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx06
    with dissolve
        
    ne "te diré cómo ayudar a tu amigo a recuperar su cuerpo original."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sadbiting_Silentx05
        
    else:
        show N_Against_N_blush 01
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "¡¿Qué?!"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 03
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_mouth sad_Talkingx04
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Repites muchas veces ese monosílabo,"

    extend " [protname]..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth sadbiting_Silentx02
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "No entiendo..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_mouth sadbiting_Silentx05
    with dissolve
       
    p "¿Me estás diciendo que, para ayudar a mi amigo,"

    extend " debo tener tres citas contigo?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 04
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Silentx05
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth sad_Silent
    with dissolve

    ne "..."
    
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Talkingx04
        
    else:
        show N_Against_N_mouth sad_Talking
    with dissolve
    
    ne "¿Tanto..."

    extend " te disgusta la idea?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    n "El tono de seguridad que había mantenido su voz hasta el momento, se oye ahora ligeramente menos firme."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Talkingx04
        
    else:
        show N_Against_N_blush 02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Sé que no soy tu tipo de mujer ideal..." 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 03
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx06
        
    else:
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
    with dissolve
        
    ne "de eso no me cabe la menor duda... "
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 02
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx05
        
    else:
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
    with dissolve
        
    ne "He visto cómo miras a las otras compañeras de clase que tienen más y mejores curvas que yo."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 00
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "..."

    p "Pero..."

    extend " ¿Por qué...?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Talkingx10
        
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "¿No te basta con saber que, si cumples mis exigencias,"

    extend " conseguirás ayudar a tu amigo?" 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx02
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx08
        
    else:
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
    with dissolve
        
    ne "Tampoco creo estar pidiéndote nada del otro mundo." 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx02
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
    with dissolve
        
    ne "¿Verdad?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 01
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sad_Silentx05
        
    else:
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "¿Solo cenar?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 02
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Talkingx04
        
    else:
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Bueno..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 03
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Talkingx04
        
    else:
        show N_Against_N_blush 03
        show N_Against_N_eyes 03
        show N_Against_N_pupils left_03
    with dissolve

    ne "No haremos nada que tú no quieras,"

    extend " eso te lo garantizo."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 03
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sadbiting_Silentx02
        
    else:
        show N_Against_N_mouth sadbitingx02_Silent
    with dissolve

    p "Y después de las tres citas,"

    extend " ¿me prometes que Dídac se pondrá bien?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_blush 05
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sadbitingx03_Silent
    with dissolve

    ne "{size=15}Citas...{/size}"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 04
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth sadbiting_Silentx05
        
    else:
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
    with dissolve

    ne "..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 04
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth happy_Talkingx04
        
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Sí."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 03
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx03
        
    else:
        show N_Against_N_blush 02
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
    with dissolve

    ne "Tienes mi palabra."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx04
        
    else:
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "¿Me aseguras que no le pasará nada malo a Dídac?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 02
        show neus_exp_eyes 03
        show neus_exp_iris left03
        show neus_exp_mouth happy_Talkingx04
        
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_blush 02
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Sí..."

    ne " Lo peor ya ha pasado..." 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth happy_Talkingx03
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils left_02
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Ahora es cuando realmente dejará de reconocerse ante el espejo."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Silentx03
        
    else:

        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "Pero sigo sin entender la frase que dijiste..."

    extend " {i}A menos que quede preñada...{/i}" 
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 01
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
    with dissolve
       
    p "¿A qué te referías con eso?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx08
        
    else:
        show N_Against_N_eyebrows angry
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Que, si en algún momento tu amigo,"

    extend " que ahora es una chica,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx002
    with dissolve

    ne "quedara encinta,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx06
    with dissolve
    
    ne "ya no habría nada que pudiéramos hacer ni tú ni yo,"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx05
    with dissolve

    ne "para poder ayudarle a recuperar su forma original."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Talkingx04
    with dissolve
        
    ne "Mantendría dicha forma para siempre."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows angryx01
        show neus_exp_blush 00
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Silentx04
        
    else:
        show N_Against_N_mouth sad_Silent
    with dissolve

    p "..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 00
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx04
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils front_01
        show N_Against_N_mouth sad_Talking
    with dissolve

    ne "Creí que sería bueno que supieras esta regla básica desde el principio..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 00
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_mouth happy_Talkingx03
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Por si te diera por jugar a papás y a mamás con tu amigo de la infancia..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_blush 00
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "¡¿Qué?!"
        
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 00
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx04
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Ohh..."

    extend " vamos..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx06
    with dissolve

    ne "Me dirás que no has intentado mirarle desnudo..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_blush 00
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Talkingx08
        
    else:
        show N_Against_N_eyes 03
        show N_Against_N_pupils front_03
        show N_Against_N_mouth happy_Talking
    with dissolve

    ne "Siendo chicos,"

    extend " hay que reconocer que tenéis un cuerpo de modelo..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Talkingx05
    with dissolve
        
    ne "eso no cambia en exceso cuando el sexo se invierte..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows suspiciousx01
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx05
    with dissolve
        
    ne "estoy convencida de que tendrá un cuerpo espectacular..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Talkingx004
    with dissolve

    ne "¿O eres tan caballero que no has tenido aún la tentación?"

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows normal
        show neus_exp_blush 00
        show neus_exp_eyes 02
        show neus_exp_iris front02
        show neus_exp_mouth happy_Silentx03
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_mouth happyx01_Silent
    with dissolve

    p "..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows surprisex01
        show neus_exp_eyes 01
        show neus_exp_iris front01
        show neus_exp_mouth sad_Silentx02
    with dissolve

    p "Eumm..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 00
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth sad_Silentx06
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
        show N_Against_N_mouth sad_Silent
    with dissolve

    ne "..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx03
        show neus_exp_blush 00
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_mouth sad_Talkingx02
        
    else:
        show N_Against_N_blush 00
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth sad_Talking
    with dissolve
    
    ne "¿Eso es que sí...?"
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx04
        show neus_exp_blush 00
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx05
        
    else:
        show N_Against_N_mouth sadx02_Silent
    with dissolve

    p "..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx03
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth sad_Silentx06
    with dissolve

    p "Con la jodida fiebre de las narices y sin poderlo llevar a un hospital," 

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx02
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth sad_Silentx05
    with dissolve
       
    p "¿qué crees que he tenido que hacer?"

    extend " Sino ayudarlo a ducharse..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 00
        show neus_exp_eyes 03
        show neus_exp_iris right03
        show neus_exp_mouth sad_Silentx04
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_blush 01
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
    with dissolve
       
    p "Tampoco es que me hubieras dejado muchas más opciones..."
    
    if morning03_Neus_Wall_Grabbing == False:
        
        show neus_exp_iris left03
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
        show N_Against_N_mouth sad_Silent
    with dissolve

    ne "..."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 00
        show neus_exp_eyes 04
        show neus_exp_iris front04
        show neus_exp_mouth happy_Silentx03
        
    else:
        show N_Against_N_blush 01
        show N_Against_N_mouth happyx01_Silent
    with dissolve
    
    ne "Humm..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows serious
        show neus_exp_blush 01
        show neus_exp_eyes 01
        show neus_exp_iris left01
        show neus_exp_mouth happy_Talkingx04
        
    else:
        show N_Against_N_mouth happy_Talking
    with dissolve
    
    ne "Supongo que tienes razón..."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx03
        show neus_exp_eyes 07
        show neus_exp_iris front07
        show neus_exp_mouth happy_Talkingx03
    with dissolve

    ne "muchas opciones tampoco te dejé."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 02
        show neus_exp_eyes 03
        show neus_exp_iris front03
        show neus_exp_mouth happy_Talkingx05
        
    else:
        show N_Against_N_eyebrows surprise
        show N_Against_N_eyes 02
        show N_Against_N_pupils front_02
    with dissolve

    ne "Bueno,"

    extend " entonces te espero a las diez,"

    extend "\ndelante del {i}CAFN{/i} de {a=https://es.wikipedia.org/wiki/Plaza_de_Cataluña}Plaça Catalunya{/a}."
    
    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx01
        show neus_exp_blush 03
        show neus_exp_eyes 02
        show neus_exp_iris left02
        show neus_exp_mouth happy_Talkingx08
        
    else:
        show N_Against_N_eyebrows sad
        show N_Against_N_blush 02
        show N_Against_N_eyes 01
        show N_Against_N_pupils left_01
    with dissolve

    ne "No hagas esperar a una dama."

    if morning03_Neus_Wall_Grabbing == False:
        show neus_exp_eyebrows sadx03
        show neus_exp_blush 04
        show neus_exp_eyes 04
        show neus_exp_iris left04
        show neus_exp_mouth happybiting_Silentx05
        with dissolve
    
    if morning03_Neus_Wall_Grabbing == False:
        scene  morning02_bg schoolwall
        
    else:
        scene N_Against_bg
    with dissolve

    n "Todavía sin poder reaccionar, ves cómo desaparece al cruzar la puerta."

    p "..."

    pt "¿Cómo diablos ha llegado a ser tan bizarra toda esta situación?"
    
    window hide dissolve
    
    pause
    
    jump night03
    
label night03:
    
    play music "audio/music/didac_theme.ogg" fadeout 3.0 fadein 3.0

    scene beds_afternoon_lightOff_blindDown_Dbusy02MCempty
    show beds_D02_afternoon_lightOff_blindDown
    with fade
    
    n "Vuelves a casa después de tus clases,"

    n "y de haber dado un par de horas de extraescolares de Dibujo a alumnos de tu antiguo colegio."

    n "Tu compañero sigue metido en la cama, pero parece que duerme con mayor tranquilidad y, aunque sigue sudando,"
       
    n "la cama ya no está empapada."
    
    n "Tienes la ligera sensación de que su pecho ha aumentado de volumen,"
    
    n "pero prefieres no encender las luces para comprobarlo, y así no tentar a la suerte y despertarlo."

    n "Decides acicalarte tan bien como sabes y te preparas para asistir a la cita con la bruja."

    window hide dissolve
    pause
    
    play music "audio/music/kevinmacleod/ultralounge.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.play("audio/sfx/crowd_bar01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.15, delay=0, channel='sfx1')
    
    show night03_bg bar_general 
    with fade

    $ saturation_tint_level = "default"

    ne "¡Míralo!"

    extend " Si parece un caballero y todo visto de lejos..."
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 01:
        neus_exp_atright_position
    show neus_exp_mouth happy_Silentx04:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris front02:
        neus_exp_atright_position
    show neus_exp_eyebrows normal:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    n "Como siempre, viste con su ropa oscura," 

    n "pero esta vez su vestido es más parecido al que una mujer se suele poner para despedir a un difunto" 
       
    n "que para asistir a una cita normal en la calle."
    
    window hide dissolve
    pause

    n "El lugar escogido no es un restaurante como uno se hubiera imaginado," 
       
    n "sino que se trata de un bar oscuro perdido en el barrio antiguo de Barcelona."

    p "Pensé que íbamos a cenar..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "Bueno,"

    extend " aquí también se podría comer..."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
    
    ne "Pero pensé que sería más informal ir a tomar algo para empezar a conocernos mejor,"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris front02
    show neus_exp_eyes 02
    with dissolve
    
    ne "que ir a un lugar algo más lleno de gente y en el que se pide más silencio y respeto."
    
    show neus_exp_mouth happy_Silentx03
    with dissolve

    p "¿No será esto acaso una excusa para emborracharme?"

    extend " {i}Lady Neus...{/i}"
    
    show neus_exp_eyebrows surprisex01 
    show neus_exp_iris front01 
    show neus_exp_eyes 01 
    show  neus_exp_mouth sad_Talkingx02
    with dissolve

    ne "¿Por qué lo dices?"

    extend " ¿Eres de borrachera fácil?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front03 
    show neus_exp_eyes 03 
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "No me dé usted ideas,"

    extend " caballero..."
    
    show neus_exp_mouth happy_Silentx04
    with dissolve

    n "El lugar tiene una iluminación tenue," 
       
    n "pero el ambiente es aparentemente agradable."

    n "Al fondo, un par de siluetas parecen estar jugando tranquilamente en una mesa de billar," 
       
    n "algunos clientes desperdigados por el local parecen disfrutar de una cerveza tranquilamente."
    
    scene night03_bg bar_barra
    #show night03_bar_barra_prove:
        #alpha 1.0
    show night03_bar_barra_copas empty:
        night03_bar_barra_copas_expressions_pos
    show night03_bar_barra_barman_body
    show night03_bar_barra_barman_eyes angry:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_pupils angry_front:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_mouth sad_Silent:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_n_body_ld
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
    with dissolve

    window hide dissolve
    pause
    
    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Talkingx02
    with dissolve

    ba "¡Buenas noches Calavera!"

    show night03_bar_barra_barman_mouth happy_Talkingx01

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve
    
    ba "Qué mozo más {i}mainstream{/i} te has traído esta noche..."

    extend " ¿Es algún primo tuyo?"
    
    show night03_bar_barra_n_mouth sad_Talkingx04
    show night03_bar_barra_barman_mouth sad_Silent
    with dissolve

    ne "No, Rata."

    ne " El chico que ves aquí,"

    extend " es mi cita de esta noche,"

    ne " para que lo sepas."
    
    show night03_bar_barra_n_mouth happy_Silentx03
    show night03_bar_barra_barman_mouth happy_Silent
    with dissolve
    
    n "No es extraño que el mote del barman sea \"Rata\"," 
    
    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent
    with dissolve
       
    n "su rostro es particularmente extraño y tiene una ligera apariencia de roedor."
    
    show night03_bar_barra_barman_mouth sad_Talkingx02
    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    with dissolve

    ba "Me rompes el corazón, querida..."

    extend " pensé que lo nuestro tenía futuro..."
    
    show night03_bar_barra_barman_mouth sad_Silent
    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows surprisex02
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "Lo nuestro no tiene final,"

    extend " querido..." 
        
    ne "eres mi amante hasta que los cuervos y los gusanos devoren cada centímetro de mis huesos..."

    extend " ya lo sabes."
    
    play sound "audio/characters/barman/laugh_stupid01.ogg"
    
    show night03_bar_barra_barman_mouth happy_Talkingx02
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve

    ba "Je, je, je."
    
    show night03_bar_barra_barman_mouth happy_Talkingx01
    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    with dissolve

    ba "¿Qué van a tomar entonces este par de tortolitos?"
    
    show night03_bar_barra_barman_mouth happy_Silent
    show night03_bar_barra_n_mouth happy_Talkingx04
    with dissolve

    ne "A mí ponme un ruso negro."
    
    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_barman_mouth sad_Silent
    with dissolve

    ne "¿Qué vas a tomar tú? [protname]."
    
    show night03_bar_barra_barman_mouth happy_Silent
    show night03_bar_barra_n_mouth happy_Silentx03
    with dissolve
            
    menu night03_barmaninsult_01:
        
        pt "¿Alcohol?, yo nunca tomo alcohol..."
        
        "<Pedir tímidamente agua>":
            
            call p_Help

            $ night03_barmaninsult_01_AskedWater = True
            
            $pl.ch_pts("np",-2)
                  
            jump night03_barman_water
        
        "<Pedir lo mismo que Neus>":
            
            call p_Help
            
            $pl.ch_pts("np",2)
            
            jump night03_barman_blackrussian
            
label night03_barman_water:
    
    show night03_bar_barra_n_mouth sad_Silentx03
    show night03_bar_barra_barman_mouth sad_Talkingx02
    with dissolve

    ba "¿Agua?"
    
    play sound "audio/characters/barman/laugh_stupid02.ogg"
    
    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_barman_mouth happy_Talkingx02
    with dissolve

    ba "JAJAJAJA"

    show night03_bar_barra_barman_mouth happy_Talkingx01

    ba "¿De qué agua dulce has sacado a este ganapán?"
    
    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve
    
    ne "Este ganapán,"

    extend " es capaz de atraer la atención de una chica como yo"

    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth sad_Silent

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows suspiciousx01
    show night03_bar_barra_n_mouth happy_Talkingx02
    with dissolve
        
    ne "y de complacerla en la cama si fuera necesario,"

    extend " el triple de tiempo que tú."

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth sad_Talkingx01
    with dissolve
    
    ne "No creo que seas el más indicado para criticar al chico,"

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_n_eyebrows suspiciousx02
    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve
    
    ne "teniendo en cuenta que no tiene nada de malo llevar una dieta sana."
    
    show night03_bar_barra_barman_mouth sad_Talkingx02

    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_eyebrows serious
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    ba "Vaya por Dios..."

    extend " Cómo defiendes al grumete,"

    extend " ¿eh?"

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows normal
    show night03_bar_barra_n_mouth sad_Silentx02
    
    show night03_bar_barra_barman_mouth sad_Silent
    with dissolve

    p "..."
    
    menu night03_barmaninsult_02:
        
        pt "Puto barman..."
        
        "<Mantenerte callado>":
            
            call p_Help
            
            $pl.ch_pts("np",1)
                  
            jump night03_barmaninsult_silence
        
        "<Defenderte>":
            
            call p_Help
            
            $pl.ch_pts("np",-2)

            $ night03_barmaninsult_02_YouDefendeYourself = True
            
            jump night03_barmaninsult_defend
            

label night03_barmaninsult_defend:

    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils front01
    show night03_bar_barra_n_eyebrows surprisex02
    with dissolve
    
    p "Con esa barriga no creo que tengas muy bien el colesterol."
    
    show night03_bar_barra_n_eyebrows angryx04
    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    with dissolve

    window hide dissolve
    pause
    
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "¡[protname]!"

    extend " ¡Cierra la boca!"

    show night03_bar_barra_n_mouth sad_Talkingx03
    with dissolve

    ne "Rata y yo hace años que nos conocemos..."

    ne " ¡No son maneras de tratar a un viejo amigo!"
    
    show night03_bar_barra_barman_eyes surprise
    show night03_bar_barra_barman_pupils surprise_left
    show night03_bar_barra_barman_mouth happy_Silent
    show night03_bar_barra_n_mouth sad_Silentx03
    with dissolve

    pt "¡¿Qué?!"

    pt " Pero si has sido tú misma la que lo ha tratado como si fuera un trapo sucio..."
    
    jump night03_barmaninsult_silence
    
label night03_barmaninsult_silence:
    
    show night03_bar_barra_barman_mouth sad_Silent
    show night03_bar_barra_barman_eyes angry
    show night03_bar_barra_barman_pupils angry_front
    show night03_bar_barra_n_mouth sad_Talkingx04
    with dissolve

    ne "Bah..."

    ne "ponle lo mismo que a mí,"

    ne "por una noche tampoco creo que se vaya a morir... "
    
    jump night03_barman_blackrussian

label night03_barman_blackrussian:
    
    show night03_bar_barra_n_eyes 03
    show night03_bar_barra_n_pupils right03
    show night03_bar_barra_n_mouth sad_Silentx03
    hide night03_bar_barra_barman_body
    hide night03_bar_barra_barman_eyes
    hide night03_bar_barra_barman_pupils
    hide night03_bar_barra_barman_mouth
    with dissolve

    n "El barman se aparta de la barra refunfuñando algo ininteligible para tus oídos,"
    
    show night03_bar_barra_copas copas
    show night03_bar_barra_n_eyes 01
    show night03_bar_barra_n_pupils right01
    show night03_bar_barra_barman_body
    show night03_bar_barra_barman_eyes angry:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_pupils angry_front:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_mouth sad_Silent:
        night03_bar_barra_barman_expressions_pos

    with dissolve
       
    n "y al poco rato trae dos vasos negros con hielo y una pajita en cada uno."
    
    scene night03_bg bar_barra
    show night03_bar_barra_barman_body
    show night03_bar_barra_barman_eyes angry:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_pupils angry_front:
        night03_bar_barra_barman_expressions_pos
    show night03_bar_barra_barman_mouth sad_Silent:
        night03_bar_barra_barman_expressions_pos
    with dissolve
       
    with dissolve

    n "Neus coge ambos vasos y, dando las gracias al barman, se dirige a la mesa"
    
    n "que se encuentra en el rincón más oscuro y alejado del resto de clientes del bar."
    
    pt "No sé por qué..."

    pt "pero tengo la extraña sensación de que a este tío no le hace mucha gracia que esté con Neus..."

    transform night03_bar_drinking_body_pos:
        xanchor -1.06 yanchor -0.26 zoom 0.2

    transform night03_bar_drinking_expressions_pos:
        xanchor -3.71 yanchor -1.485 zoom 0.2
    
    scene night03_bg bar_backstage
    #show night03_bar_drinking_n_body
    #show night03_bar_drinking_n_eyes normal
    #show n_s_exp_blush 00
    #show n_s_exp_tears empty
    #show night03_bar_drinking_n_glasses
    #show n_s_exp_mouth happy_Silentx02
    #show n_s_b_ld_arm rest

    show n_s_b_ld_body:
        night03_bar_drinking_body_pos

    show n_s_b_ld_hair_pigtails:
        night03_bar_drinking_body_pos

    show n_s_exp_blush 02:
        night03_bar_drinking_expressions_pos

    show n_s_exp_eyes 02:
        night03_bar_drinking_expressions_pos

    show n_s_exp_iris front02:
        night03_bar_drinking_expressions_pos

    show n_s_exp_tears empty:
        night03_bar_drinking_expressions_pos

    show n_s_exp_eyebrows normal:
        night03_bar_drinking_expressions_pos

    show n_s_exp_glasses:
        night03_bar_drinking_expressions_pos

    show n_s_exp_mouth happy_Silentx04:
        night03_bar_drinking_expressions_pos

    show n_s_b_ld_hairfront:
        night03_bar_drinking_body_pos

    show n_s_b_ld_arm rest:
        night03_bar_drinking_body_pos

    #show  n_s_b_ld_provec:
        #zoom 0.2

    show night03_bar_drinking_coaster:
        zoom 0.5
    show night03_bar_drinking_glass full:
        zoom 0.5
    show night03_bar_drinking_straw:
        zoom 0.5

    with fade
    
    n "Al sentarte, Neus te acerca la copa con una mano mientras con la otra quita la pajita de la suya."
    
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth happy_Silentx04

    hide night03_bar_drinking_straw
    show night03_bar_drinking_glass empty
    show n_s_b_ld_arm glass
    with dissolve

    n "Coge el vaso, se lo acerca a los labios, y le da un sorbo pronunciado."

    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth happy_Silentx04
    with dissolve

    n "Bajas la mirada hacia el tuyo y decides cogerlo con las manos para acercártelo a la boca."

    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Silentx04
    with dissolve

    n "El vaso está congelándote los dedos, pero aun así acercas la pajita a tus labios y le das un sorbo."
    
    show night03_bar_drinking_glass half01:
        zoom 0.5

    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Silentx03

    show n_s_b_ld_arm rest
    with dissolve

    n "El sabor amargo del café, junto con un fuerte sabor a alcohol, hace que se te dibuje en la cara una mueca extraña."
    

    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "¿Qué pasa?"

    extend " ¿No te gusta?"
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "¿Se puede saber qué estoy bebiendo?"

    extend " Pensaba que era Coca-Cola con algo..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "No."

    ne "Es un cóctel de vodka y licor de café."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "¿Café?"

    extend " ¿Por la noche?"

    pt "No me extraña que tenga esas pedazo de ojeras..."

    extend " ¿A qué hora se irá a dormir esta friki?"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx05
    with dissolve

    ne "Me imagino que,"

    extend " como un buen niño de papá,"

    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth happy_Talkingx07
    with dissolve

    ne "tú irás a dormir prontito..."

    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Talkingx06
    with dissolve

    ne "¿A qué hora?"

    extend " ¿A medianoche,"

    extend " como Cenicienta?"

    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx04
    with dissolve

    ne "¿O quizás a las diez?"

    ne "como {a=https://es.wikipedia.org/wiki/Familia_Telerín}La Familia Telerín{/a},"

    extend " porque {i}hay que ir a la cama, que hay que descansar{/i}..."
    
    show n_s_exp_eyebrows suspiciousx01
    show n_s_exp_eyes 05
    show n_s_exp_iris down05

    show n_s_b_ld_arm glass
    show n_s_exp_mouth happy_Silentx02
    show night03_bar_drinking_glass empty
    with dissolve

    n "Una sonrisa inocente pero burlona aparece en la comisura de sus labios mientras le da otro sorbo al vaso."
    
    pt "¿Es consciente de que está hablando de una sintonía española televisiva que hace como cuarenta años que dejó de emitirse?"

    p "Perdona si querer mantener un sueño largo y distendido,"

    extend " hace que tus noches de bruja se alteren."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 01
    show n_s_exp_iris front01b
    show n_s_exp_mouth sad_Silentx08

    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half02:
        zoom 0.5
    with dissolve

    n "..."
    
    show n_s_exp_iris front01

    show n_s_exp_mouth sad_Talkingx09
    with dissolve

    ne "¿Bruja?"

    ne "¿Tan fea me ves,"

    extend " que te parezco una bruja?"
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04b
    show n_s_exp_mouth sad_Silentx05

    with dissolve

    p "..."
    
    $ night03_Neus_ugly = False
            
    menu night03_NeusWitch_01:
        
        pt "¿Que si se parece a una bruja?"
        
        "No lo digo por tu aspecto, sino por lo que le hiciste a mi compañero.":
            
            call p_Help
            
            $pl.ch_pts("np",1)
                  
            jump night03_NeusWitch_nice
        
        "Sí... un poco sí.":
            
            call p_Help
            
            $pl.ch_pts("np",-7)
            
            $ night03_Neus_ugly = True
            
            jump night03_NeusWitch_bad
            
label night03_NeusWitch_bad:

    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris front00b
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    n "El rostro de Neus se ensombrece."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 01
    show n_s_exp_iris front01b
    show n_s_exp_mouth sad_Silentx05
    with dissolve
    
    n "Una mirada que helaría a la Reina de las Nieves, te atraviesa hasta el punto de producirte escalofríos."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "Quería que me respondieras a ciertas preguntas que me inquietan sobre ti,"

    ne "y sobre qué piensas realmente de mí."
    
    show n_s_b_ld_arm glass
    show n_s_exp_mouth sad_Silentx03
    show night03_bar_drinking_glass empty
    with dissolve
    
    n "Ves a Neus ponerse el vaso en los labios con cara enfurruñada."
    
    show n_s_b_ld_arm rest
    show n_s_exp_mouth sad_Talkingx03
    show night03_bar_drinking_glass half03:
        zoom 0.5
    with dissolve

    ne "Pero es obvio que estás aquí a la fuerza,"

    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 04
    show n_s_exp_iris left04
    show n_s_exp_mouth sad_Talkingx04
    with dissolve

    ne "como si prefirieras estar en cualquier otro sitio antes que aquí."
    
    show n_s_exp_eyebrows sadx05
    show n_s_exp_eyes 05
    show n_s_exp_iris left05
    show n_s_exp_mouth sad_Silentx04
    with dissolve
    
    jump night03_NeusWitch_porqueestasaqui
            
            
label night03_NeusWitch_nice:
    
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "Amm..."

    ne "lo dices por eso..."

    ne "bueno,"

    extend " en realidad no vas tan mal encaminado."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    n "Un silencio incómodo reina en la estancia durante unos segundos."
    
    jump night03_NeusWitch_akelarre
    
label night03_NeusWitch_akelarre:
    
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "Entonces..."

    p "¿Es magia vudú?"

    extend " ¿Magia negra?"

    extend " ¿Algún tipo de aquelarre?"

    extend " ¿Misa negra?"
    
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "Un {a=https://es.wikipedia.org/wiki/Aquelarre}aquelarre{/a} es una reunión de brujas,"

    extend " no es un conjuro en sí mismo."

    ne "La {a=https://es.wikipedia.org/wiki/Misa_negra}misa negra{/a},"

    extend " no es más que la antítesis de la celebración del cuerpo de Cristo,"

    ne "nada tiene que ver con conjuros tampoco."

    ne "El {a=https://es.wikipedia.org/wiki/Vudú}vudú{/a},"

    extend " es en realidad una religión teísta de un sistema animista,"

    ne "cuya variante caribeña tiene un fuerte componente \"mágico\"."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "{a=https://es.wikipedia.org/wiki/Magia_negra}Magia negra{/a}..."

    ne "Hoy día a todo se le llama magia negra o magia blanca."

    ne "Pero en realidad,"

    extend " la magia no existe."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Llamamos magia a la ciencia que aún no comprendemos,"

    extend "\no no queremos comprender."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "¿No queremos comprender?"

    extend " ¿Quién no querría comprender?"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx05
    with dissolve

    ne "Si yo te dijera que mientras duermes a solas en tu habitación a oscuras,"

    extend " tranquilamente bajo tus sábanas,"
    
    ne "en realidad,"

    extend " no estás tan solo como crees..." 
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "¿De verdad querrías saber quién te observa en la oscuridad,"

    extend " y por qué?"
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "..."
    
    menu night03_6sentido:
        
        pt "¿Quién me observa en la oscuridad cuando estoy solo...?"
        
        "Eso es que has visto demasiadas veces {b}El sexto sentido{/b}...":
            
            call p_Help
            
            $pl.ch_pts("np",-3)
                  
            jump night03_6sentidoisnotjoke
        
        "Me imagino que te estás cachondeando de mi...":
            
            call p_Help
            
            $pl.ch_pts("np",-1)
            
            jump night03_6sentidoisnotjoke

        "¿Lo dices en serio?":
            
            call p_Help
            
            $pl.ch_pts("np",2)
            
            jump night03_6sentidoisnotjoke
   
label night03_6sentidoisnotjoke:
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "Te sorprendería saber qué cosas no somos capaces de ver ni de oír."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    n "Su vaso ya está por debajo de la mitad,"

    extend " mientras que el tuyo apenas lo has tocado."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Talkingx05
    with dissolve

    ne "Me gustaría poder conocerte mejor."
    
    show n_s_exp_mouth happy_Silentx02
    with dissolve

    p "Para eso estamos aquí..."

    extend "\n¿No?"

    show n_s_exp_mouth happy_Talkingx05
    with dissolve

    ne "Así es."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Pero me refiero a que me respondieras a ciertas preguntas que me inquietan sobre ti,"

    extend " y sobre qué piensas realmente de mí."
    
    show n_s_exp_mouth happy_Silentx02
    with dissolve

    p "Bueno..."

    extend "\nsi eso es lo que quieres..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Silentx03
    show n_s_b_ld_arm glass
    show night03_bar_drinking_glass empty
    with dissolve

    n "Ves que se pone el vaso en los labios con cara enfurruñada."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Talkingx03
    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half03
    with dissolve

    ne "Me da la sensación de que estás aquí a la fuerza,"

    ne "como si prefirieras estar en cualquier otro sitio,"

    extend " antes que aquí."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    jump night03_NeusWitch_porqueestasaqui

label night03_NeusWitch_porqueestasaqui:
    
    menu night03_NeusWitch_02:
        
        pt "¿Que si estoy aquí a la fuerza?"
        
        "Preferiría estar aquí contigo después de que me lo hubieras pedido sin tener que hacerme chantaje.":
            
            call p_Help
            
            $pl.ch_pts("np",2)
                  
            jump night03_NeusWitch_sinchantaje
        
        "Mujer... ¿Y qué esperabas? La vida de mi amigo depende de satisfacer tus caprichos.":
            
            call p_Help
            
            $pl.ch_pts("np",-8)
            
            if pl.np == -13:
                
                jump night03_Neusendnight
                
            else:
                
                jump night03_NeusWitch_caprichos
            
        "Para nada, la verdad es que deseaba estar contigo esta noche.":
            
            call p_Help
            
            if pl.np >= 4:
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 4[hn]")
                
                $pl.ch_pts("np",-1)
                
                jump night03_NeusWitch_deseabaestarcontigo
                
                
            else:
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 4[hn]")
                                
                show n_s_exp_eyebrows angryx04
                show n_s_exp_eyes 02
                show n_s_exp_iris front02
                show n_s_exp_mouth sad_Talkingx03
                with dissolve
                
                ne "Mintiéndome descaradamente..."
                
                ne "Qué bien..."
                
                jump night03_Neusendnight
                
                $pl.ch_pts("np",-3)
            
            
label night03_NeusWitch_caprichos:
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_tears 04_01
    with dissolve
    
    n "Un silencio incómodo llena la sala."
    
    show n_s_b_ld_arm glass
    show night03_bar_drinking_glass empty
    show n_s_exp_tears 04_02
    with dissolve
    
    n "Observas a Neus agarrar el vaso con fuerza sin apartar la vista de él."
    
    n "Te da la sensación de que una pequeña lágrima empieza a nacer en sus ojos."

    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_tears 04_03
    with dissolve
    
    n "Ira."

    n "No es pena ni desdicha lo que ves a través de sus ojos."
    
    n "La has llamado fea en toda su cara."

    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_tears 04_02
    with dissolve
    
    n "Tienes la sensación de que tu amigo está perdido."
    
    jump night03_NeusWitch_cambiandodetema
            
label night03_NeusWitch_deseabaestarcontigo:
    
    if night03_Neus_ugly == True:
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_mouth sad_Talkingx03
        with dissolve
        
        ne "A ver si lo he entendido bien..."
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 01
        show n_s_exp_iris front01
        with dissolve
        
        ne "Dices que me parezco a una bruja,"
        
        ne "y ahora me vienes con que deseabas estar conmigo."
        
        ne "¿Qué pasa?"
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_mouth sad_Talkingx05
        with dissolve
        
        ne "¿Es que te ponen las mujeres feas?"
        
        show n_s_exp_mouth sad_Silentx04
        
        menu night03_NeusHotWitch:
                
                pt "Da por hecho que todas las brujas son feas..."
                
                "<Demostrarle tu conocimiento de las brujas>":
                    
                    call p_Help
                    
                    $pl.ch_pts("np",15)
                          
                    jump night03_NeusWitch_knowledge
                
                "<Admitir que si estás ahí, es para ayudar a tu amigo, aunque sea sufriendo su fealdad>":
                    
                    call p_Help
                    
                    $pl.ch_pts("np",-8)
                        
                    jump night03_Neusendnight
    else:
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        show n_s_exp_mouth sad_Talkingx05
        with dissolve
        
        ne "No te he traído aquí para que me mientas como a una jodida imbécil."
        
        show n_s_exp_mouth sad_Silentx04
        with dissolve

        n "En su rostro se puede apreciar que no está de muy buen humor."
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_mouth sad_Talkingx05
        with dissolve
        
        ne "Me da igual cómo seduzcas a las demás rameras que te encuentres por el camino."
        
        show n_s_exp_eyebrows angryx04
        show n_s_exp_eyes 02
        show n_s_exp_iris front02
        
        ne "Pero,"

        extend " por favor,"
        
        
        show n_s_exp_blush 01
        show n_s_exp_mouth sad_Silentx04
        with dissolve
        
        n "Sus ojos, inundados de rabia contenida, están clavados a los tuyos."
        
        show n_s_exp_eyebrows sadx05
        show n_s_exp_eyes 04
        show n_s_exp_iris front04
        show n_s_exp_mouth sad_Talkingx05
        with dissolve
            
        ne "no me trates como a una furcia barata."
        
        show n_s_exp_eyebrows sadx03
        show n_s_exp_eyes 05
        show n_s_exp_iris down05
        show n_s_exp_mouth sad_Silentx04
        with dissolve
    
        jump night03_NeusWitch_cambiandodetema
        

label night03_NeusWitch_knowledge:
    
    p "¿Que si me ponen las mujeres feas?"

    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04b
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿Por qué dices eso?"
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "Me has dicho que parezco una bruja."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿Y quién te ha dicho a ti que las brujas son necesariamente feas?"

    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    show n_s_exp_mouth sad_Silentx04
    with dissolve
    
    ne "..."
    
    p "Una bruja es una persona que practica la brujería."
    
    p "Si bien la imagen típica de un brujo o de una bruja es muy variable según la cultura..."
    
    p "Sí es cierto que el {a=https://es.wikipedia.org/wiki/Folclore}folclore{/a} se encargó de desprestigiar su imagen para calumniar su culto,"
    
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve
    
    p "así como la Iglesia católica hizo lo mismo con el dios {a=https://es.wikipedia.org/wiki/Pan_(mitología)}Pan{/a},"

    extend " al convertirlo en el {a=https://en.wikipedia.org/wiki/Horned_God}macho cabrío{/a}." # No Spanish Wiki.
    
    p "Pero eso en realidad, son cuentos para niños."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve
    
    p "El aspecto de una bruja es el de una persona normal."
    
    p "Es su conocimiento arcano y prohibido"

    extend " lo que las convierte en maravillosas y temibles."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 01
    show n_s_exp_iris down01
    show n_s_b_ld_arm glass
    show night03_bar_drinking_glass empty
    show n_s_exp_blush 01
    with dissolve
    
    ne "..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_blush 02
    with dissolve
    
    ne "..."
    
    p "¿Qué?"
    
    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half03
    with dissolve
    
    ne "..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "Esto te lo habías preparado..."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿No te parece de mal gusto que te encasillen en algo que no eres?"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "..."
    
    ne "Sí..."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    p "No hagas lo mismo conmigo entonces,"

    extend "\npor favor."
    
    ne "..."
    
    jump night03_NeusWitch_sinchantaje
    
    
label night03_Neusendnight:
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx05
    show n_s_exp_tears 04_01
    with dissolve
    
    ne "Creo que esto es una absoluta pérdida de tiempo."
    
    ne "Y soy una persona a la que no le gusta nada perder el tiempo."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_tears 04_02
    with dissolve 
    
    ne "No sé si todo esto ha sido un error."
    
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_blush 01
    show n_s_exp_mouth sad_Silentx04
    with dissolve
    
    ne "..."
    
    scene night03_bg bar_backstage
    with dissolve

    n "De repente, ves cómo se levanta de la silla."
    
    n "Agarra sus cosas y se dirige a la puerta."
    
    p "¡Oye!"
    
    ne "¿Qué?"
    
    p "¿Y mañana...?"
    
    n "Realmente no sabías cómo terminar la frase."
    
    ne "¿Todavía quieres ayudar a tu amigo?"
        
    ne "¿O prefieres avergonzarme aún más?"
    
    p "Yo..."
    
    ne "Mañana nos volveremos a ver."
    
    n "Desaparece tras cerrar la puerta."
    
    pt "Pero..."

    extend " ¿por qué...?"
        
    pt "Después de todo lo que le he dicho,"

    extend "\n¿aún le quedan ganas de quedar conmigo?"
    
    pt "¿Es masoquista?"
    
    window hide dissolve
    pause
    
    jump afternight03


label night03_NeusWitch_sinchantaje:
    
    show n_s_b_ld_arm glass
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_blush 01
    show n_s_exp_mouth sad_Silentx03
    show night03_bar_drinking_glass empty
    with dissolve

    ne "..."

    ne "Humm..."
    
    show n_s_exp_blush 02
    show n_s_exp_mouth sad_Talkingx03
    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half03
    with dissolve

    ne "¿Con eso te refieres a que,"

    extend " si te hubiera pedido salir,"

    ne "hubieras aceptado de buena gana,"

    extend "\nasí como así?"

    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "¿Qué te hace pensar que no me hubieras interesado?"
    
    show n_s_exp_eyebrows angryx03
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "Sencillamente el hecho de que no me miras como a las otras chicas,"

    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris right02
    show n_s_exp_mouth sad_Talkingx04
    with dissolve

    ne " esas con muchas mejores curvas que yo..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris right04
    show n_s_exp_mouth sad_Silentx05
    with dissolve

    ne "..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    with dissolve

    p "Quizás no eres el tipo de mujer con el que suelo soñar,"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve
       
    p "pero te garantizo que ninguna de las chicas con las que he estado,"

    p "son, ni de lejos, la mujer de mis sueños."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    with dissolve

    p "Me tomas por alguien superficial por mi aspecto."
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "¿Y cómo es la mujer de tus sueños?"
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "Alguien que me escuche sin juzgarme."

    p "Alguien que opine sin aconsejarme."

    p "Alguien que confíe en mí sin exigirme."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    p " Alguien que me ayude sin intentar decidir por mí."

    p "Alguien que me cuide sin anularme."

    p "Alguien que me mire sin proyectar sus cosas en mí."

    p "Alguien que me abrace sin asfixiarme."

    p "Alguien que me anime sin empujarme."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "Alguien que me sostenga sin hacerse cargo de mí."

    p "Alguien que me proteja sin mentiras."

    p "Alguien que se acerque sin invadirme."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_blush 01
    with dissolve

    p "Alguien que conozca mis defectos que más le disgusten,"

    p "que los acepte,"

    extend " y no pretenda cambiarlos."

    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 01
    show n_s_exp_iris front01
    with dissolve

    p "Para que sepa que hoy,"

    extend " mañana,"

    extend " o cualquier día,"

    p " puede contar conmigo."

    p "Sin condiciones."

    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 00
    show n_s_exp_iris front00
    show n_s_exp_blush 02
    with dissolve

    n "La mirada de Neus está totalmente petrificada, casi parece que se le haya hecho un nudo en el estómago."
    
    show n_s_exp_mouth sad_Talkingx05
    with dissolve

    ne "..."

    ne "Ca-"

    extend "ray..."

    ne "Jamás había oído algo parecido..."

    ne "Eso no te lo has inventado tú,"

    ne "¿verdad?"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    p "Ja..."

    p "no..."

    extend " para nada;"

    p "es un texto de {a=https://es.wikipedia.org/wiki/Jorge_Bucay}Jorge Bucay{/a}."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    p "¿Te creías que a una persona como yo no le gusta leer?"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_blush 02
    show n_s_exp_mouth happy_Silentx02
    show n_s_b_ld_arm glass
    show night03_bar_drinking_glass empty
    with dissolve

    ne "..."
    
    show n_s_exp_mouth happy_Talkingx05
    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half04:
        zoom 0.5
    with dissolve

    ne "La verdad es que estás lleno de sorpresas, [protname],"

    extend " lo admito."
    
    show n_s_exp_mouth happy_Silentx02
    with dissolve
    
label night03_NeusWitch_cambiandodetema:
    

    show n_s_exp_tears empty
    show n_s_b_ld_arm rest
    show night03_bar_drinking_glass half04:
        zoom 0.5
    with dissolve
    
    ne "..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    show n_s_exp_blush 01
    with dissolve

    ne "Al menos podrías darle algún que otro sorbo."

    ne "Tampoco te va a matar..." 
    
    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    with dissolve
    
    n "Fijas la mirada en tu vaso y descubres, sin demasiado asombro, que efectivamente, sigue prácticamente lleno del todo."
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve 

    ne "Puedes estar tranquilo."

    ne "No le he puesto ningún embrujo."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    n "Decides coger el vaso y darle otro trago largo," 
       
    n "llenando tu garganta de ese escozor que produce el vodka, al cual no estás nada acostumbrado."
    
    play sound "audio/characters/protagonist/cough01.ogg"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Silentx03
    with vpunch

    p "¡Cof! ¡Cof! ¡Cof! ¡Cof! {size=18}¡Cof!{/size} {size=18}¡Cof!{/size}..."
    
    show n_s_exp_mouth happy_Talkingx05
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    ne "¡Así me gusta!"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "¡Pronto podrás convertirte en un hombre hecho y derecho si sigues por el buen camino, caballero!"
    
    show n_s_exp_eyebrows surprisex02
    show n_s_exp_eyes 06
    show n_s_exp_iris front06
    show n_s_exp_mouth happy_Silentx07
    with dissolve

    n "La miras con cierto odio contenido mientras ella te sonríe como una dulce niña malnacida y pícara."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth happy_Talkingx05
    with dissolve

    ne "Trae..."

    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx04
    with dissolve

    ne "ya me terminaré yo el vaso,"

    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Talkingx06
    with dissolve

    ne "sería una lástima desperdiciar semejante brebaje de los Dioses."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth happy_Silentx02
    show n_s_exp_mouth happy_Silentx02
    show n_s_b_ld_arm glass
    with dissolve

    n "Le das el vaso sin rechistar y ves cómo en una sola ronda vacía el vaso entero con cuatro tragos sin prácticamente ninguna pausa."
    
    play sound "audio/characters/neus/breath_sigh01.ogg"

    show n_s_exp_mouth happy_Talkingx05
    show n_s_b_ld_arm rest
    show night03_bar_drinking_coaster empty
    show night03_bar_drinking_glass empty2:
        zoom 0.5
    with dissolve

    ne "Aaaaaaaahhhhh..." # *exhale after a long drink.*
    
    show n_s_exp_mouth happy_Silentx02
    with dissolve

    n "Esa exhalación de satisfacción después de semejante trago continuo de vodka, no se lo habías visto hacer a nadie antes." 
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_blush 02
    with dissolve
    
    n "Es toda una bebedora profesional, de eso no tienes dudas."

    p "Caray..."

    p "te lo has bebido de golpe..."
    
    play sound "audio/characters/neus/pff01.ogg"

    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve

    ne "Pfff..." 
    

    show n_s_exp_mouth happy_Talkingx05
    with dissolve
        
    ne "Esto no es nada..."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve
        
    ne "Tendrías que ver al que nos hace de {a=https://es.wikipedia.org/wiki/Director_de_juego_(juegos_de_rol)}narrador{/a} en {a=https://es.wikipedia.org/wiki/Vampiro:_la_mascarada}Vampiro: La Mascarada{/a},"
    
    ne "cuando se toma un trago de absenta negra Hapsburg Gold de Irlanda."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    with dissolve

    ne "Eso sí es fuego puro."

    ne "Y encima se traga todo un vaso más largo que este de golpe."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "Yo a eso no llego."
    
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Silentx02
    show n_s_exp_mouth happy_Silentx02
    with dissolve

    pt "Hay que reconocer que es bastante mona cuando sonríe..."
    
    n "La noche se iba alargando sin que prácticamente os dierais cuenta de cómo pasaban las horas."
    
    window hide dissolve
    pause
    
    scene night03_bg bar_backstage

    #show night03_bar_drinking_n_body
    #show n_s_exp_eyebrows normal
    #show n_s_exp_eyes 04
    #show n_s_exp_iris front04
    #show n_s_exp_blush 03
    #show n_s_exp_tears empty
    #show night03_bar_drinking_n_glasses
    #show n_s_exp_mouth happy_Silentx02

    show n_s_b_ld_body:
        night03_bar_drinking_body_pos

    show n_s_b_ld_hair_pigtails:
        night03_bar_drinking_body_pos

    show n_s_exp_blush 05:
        night03_bar_drinking_expressions_pos

    show n_s_exp_eyes 04:
        night03_bar_drinking_expressions_pos

    show n_s_exp_iris front04:
        night03_bar_drinking_expressions_pos

    show n_s_exp_tears empty:
        night03_bar_drinking_expressions_pos

    show n_s_exp_eyebrows normal:
        night03_bar_drinking_expressions_pos

    show n_s_exp_glasses:
        night03_bar_drinking_expressions_pos

    show n_s_exp_mouth happy_Silentx02:
        night03_bar_drinking_expressions_pos

    show n_s_b_ld_hairfront:
        night03_bar_drinking_body_pos


    show n_s_b_ld_arm rest:
        night03_bar_drinking_body_pos

    show night03_bar_drinking_coaster:
        zoom 0.5
    show night03_bar_drinking_glass empty_alot:
        zoom 0.5

    with fade
    
    p "¡Caray!"

    extend "\n¡Si son casi las doce!"
    
    ne "Humm..."
    
    play sound "audio/characters/neus/hip01.ogg"
    
    show n_s_exp_mouth happy_Talkingx05
    with dissolve
    
    ne "<hip>"

    extend " Vaya..."

    extend " así sí que no habrá manera de encontrar un restaurante abierto a estas horas..."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Silentx04
    with dissolve
    
    p "¡¿Cómo se ha hecho tan tarde?!"
    
    show n_s_exp_eyebrows angryx01
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx05
    with dissolve
    
    ne "Eso es que quizás disfrutabas de mi compañía..."
    
    show n_s_exp_eyebrows sadx01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth happy_Silentx06
    with dissolve
    
    n "Sus ojos están contorsionados como si fuera una gata en celo."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth happy_Talkingx05
    with dissolve
    
    play sound "audio/characters/neus/hip02.ogg"
    
    ne "<hip>"

    extend " Creo que debes de estar hambriento..."

    ne "¿Por qué no te vienes a mi casa y te doy de comer ahí?"
    
    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Silentx02
    with dissolve
    
    p "Lo dices como si quisieras alimentarme como a un gato callejero..."
    
    show n_s_exp_eyebrows sadx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx04
    with dissolve
    
    ne "Venga ya..."

    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Talkingx06
    with dissolve

    ne "¡No seas así!"
    
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris right05
    show n_s_exp_mouth sad_Silentx06
    with dissolve
    
    n "Está claro que, aunque ha tardado en afectarle,"
    
    n "los abundantes {b}rusos negros{/b} que se había tomado empezaban a manifestarse en su forma de hablar."
    
    p "Mañana tengo que levantarme a las siete de la mañana,"

    p "y si voy a dormir más tarde de las doce, no soy persona."
    
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    play sound "audio/characters/neus/hip03.ogg"
    
    ne "<hip>"

    extend " Anda ya..."

    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Talkingx05
    with dissolve

    ne "Pareces un niño de parvulario..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx06
    with dissolve
    
    ne "¿Eres un niño,"

    extend "\no un adulto?"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Silentx05
    with dissolve

    p "..."

    show n_s_exp_eyebrows angryx02
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx07
    with dissolve
    
    play sound "audio/characters/neus/hip01.ogg"
    
    ne "<hip>"

    extend " ¿Acaso vas a rechazar la oferta de una dama?"
    
    show n_s_exp_eyebrows sadx04
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Silentx05
    with dissolve
    
    menu night03_MidnightProblem:
                
            pt "No creo que sea buena idea ir a su casa en el estado en el que está..."
                
            "Lo siento de verdad, Neus... si fueran las diez y media o las once quizás aceptaría de buena gana.":
                
                call p_Help
                
                $pl.ch_pts("np",-2)
                          
                jump night03_MidnightProblem_ItsTooLate
                
            "Lo que sí podría hacer es acompañarte a casa.":
                
                call p_Help
                
                $pl.ch_pts("np",2)
                        
                jump night03_MidnightProblem02_Accompany
                
                
label night03_MidnightProblem_ItsTooLate:
    
    p "Pero soy incapaz de funcionar al día siguiente si no tengo un sueño reparador."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    ne "Nenaza..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "¿Sabes?"

    ne "Acabas de perder gran parte del atractivo masculino que te da ese cuerpazo que tienes..."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    pt "Está claro que su inhibición ha bajado debido al alcohol que ha tomado..."
        
    pt "Incluso más que cuando está serena,"

    extend " que ya es decir..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve 
    
    ne "Bah..."

    ne "¿Qué le vamos a hacer?"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    play sound "audio/characters/neus/hip02.ogg"
    
    ne "<hip>"

    extend " Dicen que lo bueno se hace esperar..."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve

    pt "Es muy tarde y no va muy fina,"
    
    menu night03_MidnightProblem02:
                
            pt "pero quizás podría acompañarla a su casa..."
                
            "Lo que sí podría hacer es acompañarte a casa.":
                
                call p_Help
                
                $pl.ch_pts("np",2)
                          
                jump night03_MidnightProblem02_Accompany

                
            "Mejor así, mañana nos volveremos a ver entonces.":
                
                call p_Help
                
                $pl.ch_pts("np",-2)
                        
                jump night03_MidnightProblem02_GoHome
                
label night03_MidnightProblem02_GoHome:
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    ne "Vaya..."

    ne "Ya veo que te quieres desprender de mí lo antes posible..."
    
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    p "Neus..."

    extend " no te lo tomes a mal..."
    
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    play sound "audio/characters/neus/hip03.ogg"
    
    ne "<hip>"

    extend " No,"

    extend "\ntranquilo..."

    ne "Lo entiendo,"

    ne "tienes mejores cosas que hacer que estar conmigo."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve
    
    ne "Buenas noches,"

    extend " [protname]."

    scene night03_bg bar_backstage
    show night03_bar_drinking_glass empty_alot:
        zoom 0.5
    with dissolve
    
    n "Ves cómo sale del bar sin mirar atrás y con cara de pocos amigos."
    
    pt "Supongo que podría haber sido un poco más amable..."
    
    pt "De todos modos, mañana será otro día."
    
    pt "Lo mejor será volver a casa y ver cómo está Dídac."
    
    window hide dissolve
    
    pause
    
    jump afternight03


label night03_MidnightProblem02_Accompany:
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve

    ne "¿Acompañarme...?"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    with dissolve
    
    play sound "audio/characters/neus/hip01.ogg"
    
    ne "<hip>"

    extend " ¿Por qué...?"
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx04
    with dissolve
    
    ne "¿Tienes miedo de que me pierda?"
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx06
    with dissolve
    
    ne "¿De que me asalten por el camino unos bravucones con malas intenciones?"
    
    show n_s_exp_eyebrows serious
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx07
    with dissolve
    
    ne "¿Te crees que es la primera vez que vuelvo a casa sola pasadas las tres de la madrugada?"

    show n_s_exp_eyebrows surprisex01
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Talkingx004
    with dissolve
    
    play sound "audio/characters/neus/hip03.ogg"
    
    ne "<hip>"

    extend " Sé defenderme sola..."

    ne "¿Sabes?"
    
    show n_s_exp_eyebrows angryx02
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Silentx05
    with dissolve
    
    menu night03_MidnightProblem03:
                
            pt "¿Quiere o no quiere que vaya a su casa? ¿En qué quedamos?"
                
            "Pero quizás me gustaría saber dónde vives":
                
                call p_Help
                
                $pl.ch_pts("np",3)
                
                $ night03_PedreraHome = True
                          
                jump night03_MidnightProblem03_WhereNeusLive

                
            "Pero quizás me gustaría actuar contigo como un caballero hasta el final de la velada":
                
                call p_Help
                
                $pl.ch_pts("np",4)
                
                $ night03_PedreraHome = True
                        
                jump night03_MidnightProblem03_Gentleman
                
            "Entonces no hace falta que te acompañe a casa.":
                
                call p_Help
                
                $pl.ch_pts("np",-1)
                        
                jump night03_MidnightProblem03_NotNecessary
                
label night03_MidnightProblem03_NotNecessary:
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "Bueno..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve
        
    ne "tampoco he dicho eso..."
    
    show n_s_exp_mouth sad_Silentx04
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    with dissolve
    
    ne "..."
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
        
    play sound "audio/characters/neus/hip01.ogg"
    
    ne "<hip>"

    extend " Jo..."
    
    show n_s_exp_mouth sad_Silentx04
    with dissolve
    
    n "Un leve y triste gesto en su cara enrojecida por el exceso de alcohol hace que hasta parezca inocente."
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "No te lo tomes de forma literal..."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    with dissolve
    
    ne "Estaba tomándote el pelo."
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris down05
    show n_s_exp_mouth sad_Silentx04
    with dissolve
    
    menu night03_MidnightProblem03_Pissoff:
                
            pt "Chiflada... está chiflada..."
                
            "Bueno, entonces permíteme ser un buen caballero y llevarte a casa.":
                
                call p_Help
                
                $ night03_PedreraHome = True
                $pl.ch_pts("np",4)
                          
                jump night03_MidnightProblem03_Gentleman

                
            "Da igual, es muy tarde y estoy cansado":
                
                call p_Help
                
                $pl.ch_pts("np",-2)
                        
                jump night03_MidnightProblem02_GoHome

label night03_MidnightProblem03_WhereNeusLive:
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "¿Quieres saber dónde vivo?..."
    
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    play sound "audio/characters/neus/hip02.ogg"
    
    ne "<hip>"

    extend " ¿Por qué...?"
    
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth happy_Talkingx05
    with dissolve
    
    ne "¿Tienes intención de asaltar mi habitación en la oscuridad de la noche?"
    
    show n_s_exp_eyebrows sadx03
    show n_s_exp_eyes 05
    show n_s_exp_iris front05
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    ne "¿Mientras esté haciendo cosas indecorosas pensando en ti...?"
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    show n_s_exp_eyebrows angryx04
    show n_s_exp_eyes 02
    show n_s_exp_iris front02
    show n_s_exp_mouth sad_Talkingx05
    with dissolve
    
    play sound "audio/characters/neus/hip03.ogg"
    
    ne "<hip>"

    extend " También me lo podrías preguntar directamente..."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "Quizás hasta te sorprenda mi respuesta..."
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris down04
    show n_s_exp_mouth sad_Silentx03
    with dissolve
    
    menu night03_MidnightProblem03_Pissoff02:
                
            pt "Creo que de ella ya no me podría sorprender nada..."
                
            "Neus, permíteme acompañarte.":
                
                call p_Help
                
                $ night03_PedreraHome = True
                $pl.ch_pts("np",4)
                          
                jump night03_MidnightProblem03_Gentleman

                
            "Neus... no estás bien... Lo mejor es que te vayas a dormir.":
                
                call p_Help
                
                $pl.ch_pts("np",-2)
                        
                jump night03_MidnightProblem02_GoHome
                
    
label night03_MidnightProblem03_Gentleman:
    
    show n_s_exp_eyebrows normal
    show n_s_exp_eyes 04
    show n_s_exp_iris front04
    show n_s_exp_mouth sad_Talkingx03
    with dissolve
    
    ne "{i}Como un caballero{/i}..."

    show n_s_exp_mouth sad_Silentx03
    with dissolve
        
    ne "Humm..."
    
    play sound "audio/characters/neus/giggle01.ogg"
    
    show n_s_exp_mouth happy_Talkingx05
    with dissolve
    
    ne "je, je, je..."
    
    ne "De acuerdo..."

    ne "{i}dulce caballero{/i},"

    ne "lléveme a casa con su bello corcel..."
    
    show n_s_exp_mouth happy_Silentx02
    with dissolve
    
    window hide dissolve
    pause
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    
    play music "audio/sfx/traffic01.ogg" fadein 3.0 fadeout 3.0
    
    scene night03_bg street_rambla_colon

    with fade
    
    window hide dissolve
    pause
    
    n "Hace una reverencia clásica como si llevara un miriñaque flexionando las piernas."
    
    n "Mientras hace este gesto, está a punto de caerse al suelo por falta de equilibrio;" 
    
    n "pero consigue mantenerse en pie."
    
    n "Os paseáis por la rambla de Barcelona"
    
    scene night03_bg street_catalunya_square
    with fade
    
    window hide dissolve
    pause
    
    n "subiendo hasta llegar a {i}Plaça Catalunya{/i},"
    
    scene night03_bg street_pedrera_far
    with fade
    
    window hide dissolve
    pause
    
    n "Atravesáis la plaza por {i}Passeig de Gràcia{/i} hasta llegar a un edificio que reconoces con facilidad."
    
    p "Vaya..."

    p "¿Vives cerca de la {a=https://es.wikipedia.org/wiki/Casa_Milà}{b}Pedrera{/b}{/a}?"
    
    play music "audio/music/neus_theme.ogg" fadein 3.0 fadeout 3.0
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth happy_Talkingx03:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
       
    ne "¿Por qué...?"

    extend "\n¿Te gusta...?"
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    p "Hombre..."

    p "habrá a quien no le guste,"

    p "pero me parece un edificio peculiar y original."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Eso es decir poco..."
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "El aliento le sigue oliendo a alcohol y su tono, así como la forma en que se expresa,"
       
    n "delatan que su estado está lejos de la sobriedad."
    
    pt "Vaya..."

    extend " ¡¿ahora también se ofende si le digo que el edificio no me parece una puñetera maravilla?!"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "No es solo su aspecto..."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Aquí vivieron {b}personas{/b} muy acaudaladas de la ciudad en el siglo pasado..."
    
    $ night03_MidnightProblem03_Gentleman_Gentes = True
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front01
    show neus_exp_eyes 01
    with dissolve
    
    ne "{i}Personas{/i},"

    extend " que hablaban en idiomas olvidados,"

    ne "y cantaban canciones que no hay que cantar."
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    pt "¿De qué puñetas está hablando?"
    
    scene night03_bg street_pedrera_close
    with fade
    
    n "Os acercáis hasta la puerta del emblemático edificio de Gaudí."
    
    window hide dissolve
    pause
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx02:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris front03:
        neus_exp_atright_position
    show neus_exp_eyebrows surprisex01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    ne "Gracias por acompañarme..." 
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    with dissolve
        
    ne "Al final sí has resultado ser todo un {b}caballero{/b}."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "La sorna con la que pronuncia esa última palabra no te deja claro si lo dice riéndose de ti,"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
       
    n "o sencillamente ya desvaría del todo."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    p "Hummmm..."

    p "gracias,"

    p " pero..."

    extend "\n¿Dónde vives exactamente?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris down01
    show neus_exp_eyes 01
    with dissolve
    
    pt "No puedo dejarla deambulando por las calles en este estado..."
    
    play sound "audio/sfx/plastic_condoms01.ogg"
    
    show neus_exp_eyebrows normal
    show neus_exp_iris down03
    show neus_exp_eyes 03
    show neus_arms ld_purse_opened
    with dissolve
    
    n "Neus empieza a meter la mano dentro de su bolso como si fuera un profundo pozo sin fondo."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris down02
    show neus_exp_eyes 02
    show neus_exp_mouth sad_Silentx03
    show neus_arms ld_condoms
    with dissolve
    
    n "Pasados unos segundos reaparece su mano sosteniendo un extraño objeto entre sus dedos."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¡Ups!"

    ne "No..."

    ne "Esto no sirve..."
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    pt "¿Son condones?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Mira que confundir algo duro,"

    extend " con esto tan suave..."
    
    play sound "audio/characters/neus/giggle02.ogg"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Je, je..."

    ne "Hay que ser tonta."
    
    play sound "audio/sfx/metal_keys_jingle01.ogg"
    
    show neus_exp_eyebrows normal
    show neus_exp_iris down03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Silentx03
    show neus_arms ld_purse_opened
    with dissolve
    
    n "Segundos después oyes el tintineo de unas llaves y consigue sacarlas del bolso."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris down04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    show neus_arms ld_keys
    with dissolve
    
    ne "¡Aquí están!"
    
    play sound "audio/characters/neus/gigglesinister02.ogg"
    
    show neus_exp_iris left04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "Se dirige al pomo de la puerta del afamado edificio."
    
    scene night03_bg street_pedrera_door
    with fade
    
    window hide dissolve
    pause
    
    play sound "audio/sfx/metal_clancks01.ogg"
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_keystry:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    n "Clinck, clanck, clinck."
    
    show neus_body ld_default
    show neus_exp_eyebrows angryx01
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    show neus_exp_hairfront
    with dissolve
    
    ne "Caray..."

    ne "sí que está difícil este pomo..."

    ne "¿Por qué se mueve...?"
    
    show neus_exp_iris down04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Silentx03
    show neus_arms ld_keys
    with dissolve
    
    pt "¡Está loca!"

    extend "\n¡Está loca!"
    
    show neus_exp_iris left04
    with dissolve
    
    pt "Nos va a meter en un buen lío como pase por aquí un policía..."

    pt "o peor aún..."

    extend " ¡Un {a=https://es.wikipedia.org/wiki/Mozos_de_Escuadra}Mosso d´Esquadra{/a}!"
    
    show neus_exp_iris down04
    show neus_exp_eyes 04
    with dissolve
    
    p "Neus..."

    p "Esto es la Pedrera,"

    extend "\nno tu casa..."
    
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
    
    p "Dime..."

    extend " ¿Dónde vives?"
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Vivo aquí..."

    ne "¿Por qué?"
    
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "¿Quieres subir?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front02
    show neus_exp_eyes 02
    show neus_exp_mouth sad_Talkingx004
    with dissolve
    
    ne "¿O al menos descubrir qué entidades se esconden tras estos muros?"
    
    play sound "audio/sfx/metal_clancks01.ogg"
    
    show neus_arms ld_keystry
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    pt "Está como una chota..."
    
    play sound "audio/sfx/door_open02.ogg"
    
    show neus_arms ld_keysinsert
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris left01
    show neus_exp_eyes 01
    with dissolve
    
    n "Clic."
    
    play sound "audio/sfx/metal_door_unlocked01.ogg"
    
    show neus_exp_eyebrows angryx01
    with dissolve
    
    n "De pronto oyes el ruido característico de una llave entrando en una cerradura"
    
    show neus_arms ld_keysinsert
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    with dissolve
       
    n "y el clic siguiente de cuando se abre."
    
    play sound "audio/sfx/door_old_open01.ogg"
    
    show night03_bg street_pedrera_door_opened
    show neus_arms ld_keys
    with dissolve
    
    window hide dissolve
    pause
    
    n "Unos segundos en silencio inundan ese rincón del {i}Passeig de Gràcia{/i}."
    
    p "¡¿Qué?!"
    
    show neus_exp_eyebrows angryx01
    show neus_arms ld_rest
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Qué pasa ahora...?"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿Vives aquí?"
    
    show neus_exp_eyebrows angryx01
    show neus_arms ld_rest
    show neus_exp_iris left01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Bueno..."

    ne "este edificio no deja de ser un bloque de pisos..."

    extend "\n¿No?"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris down03
    show neus_exp_eyes 03
    with dissolve
    
    ne "Sí,"

    extend " vale..."

    ne "es verdad que en realidad somos cuatro vecinos mal contados..."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    with dissolve
    
    ne "Y que la mayoría de los restantes son propiedad del puñetero banco..."
    
    show neus_exp_iris left03
    show neus_exp_eyes 03
    with dissolve
    
    ne "Pero sí."
    
    show neus_exp_mouth happy_Talkingx03
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
    
    ne "Mi familia tiene un trato con una encantadora anciana a la que llamo {a=https://es.wikipedia.org/wiki/Baba_Yagá}Baba{/a},"

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_iris front04
    show neus_exp_eyes 04
    with dissolve

    ne "propietaria de uno de estos pisos."

    show neus_exp_mouth happy_Talkingx03
    show neus_exp_iris front06
    show neus_exp_eyes 06
    with dissolve
    
    ne "Así que me deja dormir aquí mientras estoy en Barcelona."

    show neus_exp_iris left04
    show neus_exp_eyes 04
    with dissolve

    ne "Deberías conocerla..."

    show neus_exp_eyebrows serious
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx06
    with dissolve

    ne "hace unas galletas riquísimas..."

    show neus_exp_eyebrows sadx01
    show neus_exp_iris front06
    show neus_exp_eyes 06
    show neus_exp_mouth happy_Silentx06
    with dissolve
    
    n "Una sonrisa boba delata en su cara que está rememorando el sabor que describe."

    show neus_exp_mouth happy_Silentx05
    with dissolve
    
    p "..."

    show neus_exp_eyebrows serious
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Silentx03
    with dissolve

    p "¿Un trato con una de las propietarias?"

    show neus_exp_eyebrows surprisex02
    show neus_exp_iris front01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Silentx02
    with dissolve
       
    p "¿Tu familia?"

    show neus_exp_eyebrows angryx01
    show neus_exp_iris left02
    show neus_exp_eyes 02
    show neus_exp_mouth sad_Silentx04
    with dissolve
    
    p "¿Qué familia tienes?"
    
    show neus_exp_eyebrows angryx03
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Una que jamás desearías haber tenido..."
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "..."
    
    p "Bueno,"

    p "viendo cómo el dinero no os resulta un problema,"

    extend " realmente dudo que sea tan desagradable."

    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Bah..."

    extend " No sabes de qué diablos estás hablando."
    
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/scream_stop01.ogg", channel="sfx1", loop=False, synchro_start=True)
    $ renpy.music.play("audio/sfx/fall18.ogg", channel="sfx2",loop=False, synchro_start=True)
    
    scene black with vpunch

    scene night03_pedrera_neusground:
        subpixel True
        zoom 1.5 xanchor 0.57 yanchor 0.78 # Foot
        ease 20.0 zoom 0.4 xanchor 0.14 yanchor 0.12 #All Image
    with fade

    $ night03_NeusFall_NotPanties = True

    n "Con un movimiento brusco y por evidente falta de coordinación,"

    n "Neus cae al suelo de espaldas con cierta mueca de dolor."

    pt "¡¿Qué coño?!"

    pt "¡¿No lleva bragas?!"
    
    window hide dissolve
    pause

    play sound "audio/sfx/clothes01.ogg"
    
    scene night03_bg_street_pedrera_door_opened02
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris left03:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with fade

    n "Con cierta torpeza, consigue volverse a poner de pie agarrándose al pomo de la puerta."
    
    pt "Es evidente que los síntomas del cansancio debidos al alcohol empiezan a manifestarse."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Entonces"

    extend " ¡¿Qué?!"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris left01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Subes o no...?"

    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    menu night03_MidnightProblem04_GoToSleep:
                
            pt "Subir... a estas horas, asunto turbio..."
                
            "<Cambiar de tema>.":
                
                call p_Help
                
                $pl.ch_pts("np",-1)
                
                jump night03_MidnightProblem04_TopicChange
                
            "Neus, no estás bien... Lo mejor es que te vayas a dormir.":
                
                call p_Help
                
                $pl.ch_pts("np",-3)
                        
                jump night03_MidnightProblem04_GoodNight
                
            "Bueno, si me invitas tan amablemente, es difícil rechazar tu oferta.":
                
                call p_Help
                
                $pl.ch_pts("np",2)
                
                $ night03_MidnightProblem04_GoUp_Boolean = True
                        
                jump night03_MidnightProblem04_GoUp
        
label night03_MidnightProblem04_GoUp:
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿En...?"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
        
    ne "..."

    extend  " serio...?"
    
    play sound "audio/characters/neus/giggle02.ogg"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "Sientes que su respiración es entrecortada y notas cómo su cuerpo empieza a temblar."
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    p "¿Subimos?"
    
    play sound "audio/characters/neus/giggle03.ogg"
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Sí..."
    
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    window hide dissolve
    pause
    
    scene night03_bg street_pedrera_entrance
    with fade
    
    n "Al entrar, el único foco de luz que permite distinguir las siluetas del lugar"
    
    n "es la iluminación indirecta de las farolas de la ciudad."

    $ saturation_tint_level = "verydark"
    
    p "¿No hay luz?"
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx02:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris front04:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve
    
    ne "Seeeh..."
    
    show neus_exp_eyebrows surprisex01
    with dissolve
    
    ne "Claaaro que hay luz..."
    
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "qué pregunta más estúpida..."
    
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "Parece que el alcohol incrementa incluso más su dichoso sarcasmo..."
    
    show neus_exp_iris left03
    show neus_exp_eyes 03
    with dissolve
    
    p "¿Y por qué no la enciendes?"
    
    show neus_exp_iris down01:
        neus_exp_atright_position
    show neus_exp_eyes 01:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "No me hace falta..."
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Cógete de mi mano,"

    extend " y sígueme..."
    
    show neus_exp_mouth happy_Silentx03
    with dissolve
    
    p "..."
    
    pt "A este paso, nos meteremos una hostia subiendo las escaleras con su falta de equilibrio..."
    
    scene night03_bg street_pedrera_entrance
    with dissolve
    
    n "Obedeces, y agarrado a su mano, puedes adivinar, por las siluetas oscuras de las barandillas, que os alejáis de las escaleras."
    
    pt "¿A dónde diablos irá?"
    
    window hide dissolve
    pause
    
    scene night03_bg street_pedrera_elevator
    with fade
    
    n "Os paráis frente a un aparato extraño después de haber andado haciendo eses por su precario equilibrio."
    
    p "¿Qué diablos es esto?"
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx02:
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
    
    ne "¿No lo ves...?"
    
    show neus_exp_eyebrows surprisex01 
    show neus_exp_iris front03 
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "Si no estuviera esto tan oscuro,"

    extend " quizás vería mejor..."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front01 
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Es..."

    extend "\n¡Un ascensor!"
    
    show neus_exp_eyebrows normal 
    show neus_exp_iris front04 
    show neus_exp_eyes 04
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    n "Su tono de voz es como de niña pequeña y algo juguetona."
    
    show neus_exp_eyebrows normal 
    show neus_exp_iris front03 
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    p "¿En serio?"
    
    p "¿De qué siglo?"
    
    show neus_exp_eyebrows normal 
    show neus_exp_iris left03 
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "De principios del veinte..."
    
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    n "Moviendo unos hierros que se pliegan sobre sí mismos,"
    
    scene night03_bg street_pedrera_elevator
    with dissolve
       
    n "Neus consigue abrir lo que parece la puerta de acceso."
    
    n "De milagro no se cae al suelo."
    
    window hide dissolve
    pause

    #call night03_midnightProblem_newLabel
    
    play sound "audio/sfx/door_open02.ogg"
    
    scene black
    with fade
    
    ono "Clic"
    
    play sound "audio/sfx/door_old_open01.ogg"
    
    n "Oyes el particular sonido de la cerradura de la pequeña puerta de madera, que conduce al piso, abriéndose."
    
    scene night03_bg street_pedrera_hall01
    with fade
    
    n "Observas cómo Neus se adentra en la enorme entrada iluminada tenuemente"
    
    show night03_n_pedrera_hall_back_body 01
    show night03_n_pedrera_hall_back_head 01
    with dissolve

    window hide dissolve
    pause
    
    n "por la luz procedente de la puerta abierta, y más al fondo,"

    n "por los enormes ventanales que se encuentran en lo que parece ser la sala de estar."
    
    ne "..."
    
    p "..."
    
    n "Neus se queda quieta en medio de la oscura sala, de espaldas a ti."
    
    show night03_n_pedrera_hall_back_head 03
    with dissolve
    
    n "Con un gesto tímido y tambaleante gira su cabeza para mirarte de reojo."
    
    ne "Pue..."

    extend " puedes entrar..."
    
    pt "¿Acaso no encenderá ninguna luz?"
    
    play sound "audio/sfx/door_old_open01.ogg"
    
    show night03_bg street_pedrera_hall02
    show night03_n_pedrera_hall_back_body 02
    show night03_n_pedrera_hall_back_head 04
    with dissolve
    
    n "Decides obedecer y entrar, ajustando la puerta."

    show night03_n_pedrera_hall_back_head 02
    with dissolve
    
    ne "¿Puedes cerrar la puerta...?"

    extend " Completamente..."
        
    p "Sí..."

    extend " claro..."

    extend " Por supuesto..."
    
    scene night03_bg street_pedrera_flatdoor_open
    with fade
    
    n "Le das un segundo la espalda a Neus para asegurarte de no hacer demasiado ruido al cerrarla."
    
    pt "¿No me había dicho que vivía una vieja en el piso con ella?"
    
    pt "Debe de estar durmiendo."
    
    play sound "audio/sfx/door_close01.ogg"
    
    show night03_bg street_pedrera_flatdoor_closed
    with dissolve
    
    ono "Clack"
    
    n "Consigues cerrar la puerta sin hacer demasiado ruido."
    
    n "Aunque al cerrarla, has quedado aún más a oscuras que antes."
    
    n "A diferencia de otros bloques de pisos en Barcelona," 
       
    n "la Pedrera tiene una estructura que da a un cielo abierto en el centro del edificio,"
    
    n "así que siempre hay algo de luz para poder abrir las puertas de aquel lugar emblemático"
    
    n "sin necesidad de ninguna luz."
    
    n "A principios del siglo XX, la luz eléctrica no era precisamente tan accesible como hoy."
    
    play music "audio/music/kevinmacleod/last_kiss_goodnight.ogg" fadein 3.0 fadeout 3.0

    $ saturation_tint_level = "superdark"
    
    scene night03_bg street_pedrera_hall03
    show neus_body_full ld_boobs:
        neus_body_atcenter_position
    show neus_head:
        neus_body_atcenter_position
    show neus_arms empty:
        neus_body_atcenter_position
    show neus_exp_blush 07:
        neus_exp_atcenter_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atcenter_position
    show neus_exp_eyes 04:
        neus_exp_atcenter_position
    show neus_exp_iris left04:
        neus_exp_atcenter_position
    show neus_exp_tears empty:
        neus_exp_atcenter_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atcenter_position
    show neus_exp_glasses:
        neus_exp_atcenter_position
    show neus_exp_hairfront:
        neus_exp_atcenter_position
    with fade
    
    window hide dissolve
    pause
    
    n "Al darte la vuelta, todavía distraído en tus pensamientos,"

    n "descubres el cuerpo semidesnudo de Neus justo enfrente de ti."
    
    n "Al quitarse el corsé, descubres que no lleva sujetador alguno."
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    with dissolve
    
    p "Euh..."
    
    show neus_exp_iris left04
    with dissolve
    
    ne "..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Qué...?"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "Sus pechos, ahora al descubierto, son apenas perceptibles por su reducido tamaño,"
    
    show neus_exp_iris left04
    with dissolve
    
    n "y especialmente debido a la oscuridad de la estancia."
    
    ne "..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Demasiado pequeños..."

    ne "¿Verdad...?"
    
    show neus_body_full ld_covered
    show neus_exp_tears 04_02
    show neus_exp_mouth sad_Silentx03
    show neus_exp_hairfront
    with dissolve

    n "Con un rápido gesto, se oculta ambos pechos poniendo los brazos entrecruzados haciendo presión sobre ellos."
    
    n "Como si intentara demostrar con eso, que -efectivamente-, hay un buen par de senos en su pecho."
    
    p "Euh..."
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_tears 04_03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Di algo..."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_tears 04_05
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "Es apenas perceptible en la abundante oscuridad,"
    
    n "pero jurarías que de su mejilla se desprende una lágrima."

    pt "Está totalmente borracha..."
    
    menu night03_SaySomething:
        
        pt "No sé yo si es buena idea aprovecharse de la situación..."
        
        "<Hacerle entender que está demasiado borracha>":
            
            call p_Help
            
            $pl.ch_pts("np",-1)
                  
            jump night03_SaySomething_TooDrunk
        
        "<Acercarte a ella para darle un beso>":
            
            call p_Help
            
            $pl.ch_pts("np",-1)
            
            if pl.np >= 6:
                $pl.ch_pts("np",8)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_pos] 6[hn]")
                
                $ morning04_DidacHotforyou = True
                
                jump night03_SaySomething_Kiss
                            
            else:
                $pl.ch_pts("np",-3)
                
                if PlatinumHelp:
                    $ renpy.notify("[p_neg] 4[hn]")
                                
                $ night03_SaySomething_KissNo = True
                
                jump night03_SaySomething_Kiss
                

label night03_SaySomething_TooDrunk:
    
    p "Neus..."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_tears 03_05
    with dissolve
    
    ne "¿Hum...?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    p "Esta noche has bebido mucho..."
    
    show neus_exp_iris left03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "He bebido bastante..."
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_tears 04_05
    show neus_exp_mouth sad_Talkingx08
    with dissolve
       
    ne "¡Pero no estoy borracha!"
    
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    p "¿Me lo podrías demostrar?"
    
    show neus_exp_mouth sad_Talkingx08
    with dissolve
    
    ne "¡Cuando quieras!"
    
    show neus_exp_mouth sad_Silentx06
    with dissolve

    pt "Si no está borracha,"

    extend "\nque lo demuestre..."
    
    menu night03_SaySomething_DrunkProve:
        
        pt "¿O quizás sería pasarme?"
        
        "<Ponerla a prueba con una postura para que vea que está borracha>":
            
            call p_Help
            
            $pl.ch_pts("np",-2)
                  
            jump night03_SaySomething_DrunkProve_Try
            
        "<Irte diciéndole adiós>":
            
            call p_Help
            
            $pl.ch_pts("np",-3)
            
            p "Creo que es una mala idea, Neus,"

            p "realmente no estás en tus cabales,"

            extend " y te harás daño."
            
            show neus_exp_mouth sad_Silentx06
            with dissolve
            
            p "Lo mejor será que te dé las buenas noches y me vaya..."
            
            show neus_exp_eyebrows angryx02
            show neus_exp_iris left03
            show neus_exp_eyes 03
            show neus_exp_tears 03_04
            show neus_exp_mouth sad_Talkingx08
            with dissolve
            
            ne "Si te quieres largar,"

            extend "\nvete..."

            ne "Tú mismo."
                  
            jump night03_DrunkFallen_Bye
            
label night03_SaySomething_DrunkProve_Try:

    play music "audio/music/kevinmacleod/teddy_bear_waltz.ogg" fadein 1.0 fadeout 3.0

    p "Vale,"

    extend "\nsi me lo quieres demostrar,"
       
    p "haz esto."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front01
    show neus_exp_eyes 01
    show neus_exp_tears 01_05
    show neus_exp_mouth sad_Silentx05
    with dissolve
    
    n "Con la mano derecha te agarras la pierna sosteniéndote a la pata coja,"
    
    n "mientras te acercas la otra mano frente a la cara,"

    n "y con el dedo anular, te tocas la punta de la nariz."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_tears 03_05
    with dissolve
    
    p "Si consigues mantener esta posición como hago yo durante cinco segundos,"

    p "tocándote la punta de la nariz,"

    extend "\nte creeré."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Idiota..."

    ne "¿Me tomas por estúpida...?"

    show neus_exp_eyebrows normal
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_mouth sad_Talkingx003
    with dissolve
    
    ne "Claro que pue..."
    
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/scream_stop01.ogg", channel="sfx1", loop=False, synchro_start=True)
    $ renpy.music.play("audio/sfx/fall18.ogg", channel="sfx2",loop=False, synchro_start=True)
    
    scene night03_bg street_pedrera_hall03 with vpunch
    
    ono "{size=72}PAM{/size}"
    
    n "Ves a Neus en el suelo, después de haber caído estrepitosamente al faltarle el equilibrio."
    
    menu night03_SaySomething_DrunkFallen:
        
        pt "Al final se ha caído, era de esperar..."
        
        "<Reírte en su cara>":
            
            call p_Help
            
            $pl.ch_pts("np",-8)
                  
            jump night03_DrunkFallen_Laughing
            
        "<Ayudarla a levantarse>":
            
            call p_Help
            
            $pl.ch_pts("np",2)
                  
            jump night03_DrunkFallen_HelpHer
            
label night03_DrunkFallen_Laughing:
    
    play sound "audio/characters/protagonist/laugh01.ogg"
    
    p "JA JA JA"

    p "¿No decías que no estabas borracha?"

    p "Era evidente que te ibas a caer..."

    p "¿Qué esperabas?"

    p "Estás borracha como una cuba, Neus..."

    show neus_body ld_default:
        neus_body_atcenter_position
    show neus_head:
        neus_body_atcenter_position
    show neus_arms ld_rest:
        neus_body_atcenter_position
    show neus_exp_blush 05:
        neus_exp_atcenter_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atcenter_position
    show neus_exp_eyes 04:
        neus_exp_atcenter_position
    show neus_exp_iris front04:
        neus_exp_atcenter_position
    show neus_exp_eyebrows angryx02:
        neus_exp_atcenter_position
    show neus_exp_glasses:
        neus_exp_atcenter_position
    show neus_exp_hairfront:
        neus_exp_atcenter_position
    with dissolve
     
    n "La ves reincorporándose con cara de pocos amigos."

    play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
    
    show neus_exp_mouth sad_Talkingx08
    with dissolve

    ne "Tampoco hacía falta que te rieras en mi cara..."
    
    show neus_exp_mouth sad_Talkingx07
    show neus_exp_iris left04
    with dissolve

    ne "Es mejor que te vayas [protname]..."

    ne "Ha sido una mala idea invitarte a subir."
    
    show neus_exp_mouth sad_Silentx06
    with dissolve

    jump night03_DrunkFallen_LeavePlease
            
label night03_DrunkFallen_HelpHer:

    play music "audio/music/neus_theme.ogg" fadeout 3.0 fadein 3.0

    $ saturation_tint_level = "superdark"
    
    n "Te arrodillas ante ella para ayudarla a levantarse."
    
    scene bg dark_a
    show n_closefromup_body ld:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 02:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 01:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris right01:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows angryx01:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears 01_01:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Silentx03:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:##
        zoom 0.5 xalign 0.5 yalign 0.5
    with fade
    
    n "Ves su rostro a escasos centímetros del tuyo."
    
    p "¿Estás bien Neus?"
    
    show n_closefromup_eyes 02##
    show n_closefromup_iris right02##
    show n_closefromup_mouth sad_Talkingx02##
    with dissolve
    
    ne "Sí..."
    
    show n_closefromup_mouth sad_Silentx05##
    with dissolve
    
    p "No debería haberte puesto a prueba..."
    
    show n_closefromup_blush 03##
    show n_closefromup_eyes 01##
    show n_closefromup_iris left01##
    show n_closefromup_eyebrows sadx05##
    show n_closefromup_mouth sad_Talkingx05##
    with dissolve
    
    ne "No..."

    extend " bueno..."

    extend "\nyo..."
    
    scene night03_bg street_pedrera_hall03
    show neus_body ld_default:
        neus_body_atcenter_position
    show neus_head:
        neus_body_atcenter_position
    show neus_arms ld_rest:
        neus_body_atcenter_position
    show neus_exp_blush 06:
        neus_exp_atcenter_position
    show neus_exp_mouth sad_Silentx03:
        neus_exp_atcenter_position
    show neus_exp_eyes 03:
        neus_exp_atcenter_position
    show neus_exp_iris left03:
        neus_exp_atcenter_position
    show neus_exp_tears 03_03:
        neus_exp_atcenter_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atcenter_position
    show neus_exp_glasses:
        neus_exp_atcenter_position
    show neus_exp_hairfront:
        neus_exp_atcenter_position
    with fade
    
    n "Ves cómo se aparta ligeramente de ti."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Lo siento [protname],"

    extend " pero..."

    extend "\ncomo bien has dicho,"
    
    ne "creo que lo más sensato sería que te fueras a casa..."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_tears 04_03
    with dissolve
    
    ne "Creo que no me encuentro nada bien..."
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    jump night03_DrunkFallen_LeavePlease

label night03_SaySomething_Kiss:   
    
    pt "Qué demonios..."
    
    pt "Si he subido hasta aquí..."

    extend " no me tiraré atrás ahora..."

    show neus_exp_iris front01
    show neus_exp_eyes 01
    show neus_exp_tears 01_05
    with dissolve
    
    n "Te acercas a ella."
    
    scene bg dark_a
    show n_closefromup_body ld:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_blush 05:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 02:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_iris front02:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sad_Talkingx04:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows surprisex01:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_tears 01_05:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:##
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_prothand empty:
        zoom 0.5 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:##
        zoom 0.5 xalign 0.5 yalign 0.5
    with dissolve
    
    n "La suave brisa de una ciudad de costa como es Barcelona"
    
    show n_closefromup_eyebrows sadx05##
    show n_closefromup_eyes 01##
    show n_closefromup_iris left01##
    show n_closefromup_mouth sad_Silentx03##
    with dissolve
    
    n "entra por las ventanas semiabiertas de este edificio emblemático y soñado."
    
    show n_closefromup_eyes 04##
    show n_closefromup_iris front04##
    show n_closefromup_tears 01_03##
    with dissolve
    
    n "Apenas a unos centímetros de ella,"

    show n_closefromup_eyebrows surprisex01##
    show n_closefromup_eyes 01##
    show n_closefromup_iris right01##
    show n_closefromup_tears 01_03##
    show n_closefromup_prothand :##
        zoom 0.5 xalign 0.5 yalign 0.5
    with dissolve
       
    n "con tu mano derecha le acaricias la mejilla húmeda para secarle una lágrima"
    
    show n_closefromup_eyebrows sadx05##
    show n_closefromup_eyes 04##
    show n_closefromup_iris front04##
    show n_closefromup_tears 01_03##
    with dissolve

    pause 1.0

    #scene bg dark_a
    hide n_closefromup_prothand
    show n_closefromup_body ld:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_blush 05:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_eyes 05:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_iris front05:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_mouth sadbiting_Silentx11:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_eyebrows sadx05:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_tears 05_03:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_glasses:##
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_prothand empty:
        zoom 1.0 xalign 0.5 yalign 0.5
    show n_closefromup_hair_front:##
        zoom 1.0 xalign 0.5 yalign 0.5
    with Dissolve (1.0)
    
    n "y acercas tus labios a los suyos,"

    scene night03_n_pedrera_hall_fondlebreast_comp 01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.9 ypos 0.5
        easein_quad 15.0 zoom 0.37 xpos 0.5 ypos 0.5
    with fade

    window hide dissolve
    pause 
    
    show night03_n_pedrera_hall_fondlebreast_comp 02
    with dissolve
    
    n "mientras con la otra mano, acaricias uno de sus senos desnudos."
    
    if night03_SaySomething_KissNo == True:
        
        jump night03_SaySomething_KissFailure
        
    else:
        
        jump night03_SaySomething_KissSucces
        
label night03_SaySomething_KissFailure:
    
    #show night03_n_pedrera_hall_fondlebreast_stop
    show night03_n_pedrera_hall_fondlebreast_comp 03
    with hpunch
    
    window hide dissolve
    pause
    
    n "Sientes su mano cogiéndote el brazo con el que le acaricias el pecho"
    
    n "haciendo ahínco para apartártelo."
    
    n "Mientras hace una pequeña presión con la otra mano en tu pecho, para intentar alejarse de ti."
    
    scene night03_bg street_pedrera_hall03
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_mouth sad_Talkingx02:
        neus_exp_atright_position
    show neus_exp_eyes 03:
        neus_exp_atright_position
    show neus_exp_iris left03:
        neus_exp_atright_position
    show neus_exp_tears 03_03:
        neus_exp_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with fade
    
    ne "Lo siento [protname],"

    extend " quizás tengas razón y no me encuentro muy bien..."
    
    show neus_exp_eyes 04
    show neus_exp_iris left04
    show neus_exp_tears 04_03
    with dissolve
    
    ne "Creo que me he precipitado al invitarte a subir..."
    
    show neus_exp_eyes 04
    show neus_exp_iris front04
    show neus_exp_tears 04_02
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    pt "Será cabrona la muy guarra..."
    
    pt "Primero me calienta, y luego me dice que me vaya a paseo..."
    
    show neus_exp_iris down03
    show neus_exp_eyes 03
    show neus_exp_tears 03_02
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Agradezco el detalle de que me hayas acompañado hasta casa..."
    
    show neus_exp_iris front03
    with dissolve
    
    ne "Pero ahora te pediría por favor que te fueras..."

    ne "realmente no me encuentro muy bien..."

    show neus_exp_iris left03
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    menu night03_DrunkFallen_LeavePlease:
        
        pt "¿Se cree que estas son formas de tratarme después de haberla acompañado y haber aceptado subir hasta aquí?"
        
        "<Violarla>":
            
            call p_Help

            pt "Mala idea, dice..."

            jump night04_Neus_Rape_Yes
            
            #aj "Lo siento... aún no está disponible esta opción."

            # NOT FINISHED, WORK IN PROGRESS WIP
                  
            jump night03_DrunkFallen_LeavePlease
            
        "<Aceptar sus disculpas y volver a casa>":
            
            call p_Help
            
            $pl.ch_pts("np",2)
                  
            jump night03_DrunkFallen_HelpHer_GoHome
            
label night03_DrunkFallen_HelpHer_GoHome:
    
    p "Como quieras, Neus..."
    
    jump night03_DrunkFallen_Bye
    
label night03_DrunkFallen_Bye:
    
    show neus_exp_eyebrows sadx03
    show neus_exp_mouth sad_Silentx06
    with dissolve
    
    p "Buenas noches."

    stop music fadeout 25.0
    $ renpy.music.set_volume(0.2, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    scene night03_bg street_pedrera_corridorclosed
    with fade
    
    n "Te retiras sin mirar atrás, y justo cuando cierras la puerta,"
    
    n "te parece oír el correteo de sus pies,"

    play sound "audio/characters/neus/puke01.ogg"
    
    n "seguido del ruido de su garganta echando el alcohol consumido"

    n "por lo que supones que debe de ser el retrete."
    
    jump afternight03
    
label night03_SaySomething_KissSucces:

    $ saturation_tint_level = "superdark"

    $ night03_SaySomething_KissSucces_Cond = True
        
    scene bg_dark_a
    show kiss_ n_n_01:
        truecenter
    with fade
    
    n "Se deja llevar abriendo la boca a modo de invitación mientras os mezcláis en un suave beso."
    
    play sound "audio/sfx/kiss_french01.ogg"
    
    show kiss_ n_n_02##
    with dissolve
    
    n "Tus párpados se relajan y se cierran del mismo modo que habían hecho los suyos."
    
    play sound "audio/sfx/kiss_french02.ogg"
    
    show kiss_ n_n_03##
    with dissolve
    
    n "Su aliento huele a una mezcla entre alcohol y café."
    
    play sound "audio/sfx/kiss_french03.ogg"
    
    show kiss_ n_n_04##
    with dissolve
    
    n "No es que fuera un olor con el que estuvieras muy familiarizado,"
    
    play sound "audio/sfx/kiss_french04.ogg"
    
    show kiss_ n_n_05##
    with dissolve
    
    n "pero hay que reconocer que era cálido y acogedor estar en manos de esa chica tan curiosa,"
    
    play sound "audio/sfx/kiss_french05.ogg"
    
    show kiss_ n_n_02##
    with dissolve
    
    n "Y... ¿para qué negarlo?"
    
    play sound "audio/sfx/kiss_french01.ogg"
    
    show kiss_ n_n_03##
    with dissolve
    
    n "bastante mona."
    
    window hide dissolve
    pause
    
    ##vpunch
    
    play sound "audio/characters/neus/hip01.ogg"
    
    show kiss_ n_n_04##
    with vpunch
    
    ne "¡Hip!"
    
    show black
    with fade
    
    n "De pronto percibes un extraño y amargo sabor subiendo a toda prisa por la garganta de Neus."
    
    play music "audio/music/alcaknight/bury_it.ogg" fadeout 0.5 fadein 0.1
    
    #scene kissn_n_surprise
    #with fade

    scene bg dark_a
    show n_closefromup_body ld:##
        kissn_n_surprise
    show n_closefromup_blush 06:##
        kissn_n_surprise
    show n_closefromup_eyes 06:##
        kissn_n_surprise
    show n_closefromup_iris front06:##
        kissn_n_surprise
    show n_closefromup_eyebrows normal:##
        kissn_n_surprise
    show n_closefromup_tears 00_00:##
        kissn_n_surprise
    show n_closefromup_mouth extra_tongueOut:##
        kissn_n_surprise
    show n_closefromup_glasses:##
        kissn_n_surprise
    show n_closefromup_hair_front:##
        kissn_n_surprise
    show n_closefromup_prothand empty:
        kissn_n_surprise
    show n_closefromup_prothandchin empty:
        kissn_n_surprise
    show eyesclosing03
    with fade
    
    n "Abres los ojos para verla de nuevo."


    show n_closefromup_blush 06##
    show n_closefromup_eyes 00##
    show n_closefromup_iris front00##
    show n_closefromup_eyebrows sadx05##
    show n_closefromup_tears 00_00##
    show n_closefromup_mouth extra_tongueOut##
    hide eyesclosing03
    with vpunch
    
    n "La descubres con un rostro perplejo y asustada, a corta distancia,"

    n "sin haber separado aún vuestros labios."
    
    pt "¿Es lo que creo que es?"
    
    n "Ese olor particularmente extraño..."
    
    scene night03_bg street_pedrera_hall03
    with dissolve
    
    n "Sientes cómo se desprende de ti fuertemente y se aleja a toda prisa en dirección a lo que parece ser el baño."
    
    play sound "audio/characters/neus/puke01.ogg"
    
    scene night03_bg street_pedrera_hall03
    with hpunch
    
    ne "{size=72}BLUEEEEEERGH{/size}"
    
    p "..."
    
    pt "Está vomitando..."
    
    n "Intentas acercarte al baño para hablar con ella sin hacer demasiado ruido."
    
    p "..."

    p "Neus..."

    $ saturation_tint_level = "verydark"

    p "¿Estás bien?"
    
    scene night03_n_pedrera_puking_bg 
    #show night03_n_pedrera_puking_body
    show night03_n_pedrera_puking_body
    show night03_n_pedrera_puking_eyes 06
    show night03_n_pedrera_puking_pupils empty
    show night03_n_pedrera_puking_eyebrows angry
    #show night03_n_pedrera_puking_eye closed
    show night03_n_pedrera_puking_glasses
    show night03_n_pedrera_puking_door open
    with fade
        
    n "Te la encuentras con la puerta del baño abierta sin haber encendido la luz,"
       
    n "decaída en el suelo sin fuerzas delante del váter" 
       
    n "Con sus lágrimas dibujadas con el rímel en sus mejillas,"
    
    n "iluminadas por la tenue luz blanca de la luna, que se cuela por la pequeña ventana del baño."
    
    n "Esa leve cantidad de luz te permite ver restos de vómito en la comisura de sus labios,"
    
    n "entremezclados con su pelo, completamente revuelto y manchado de restos de comida indigesta."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows surprise
    #show night03_n_pedrera_puking_eye open_surprise
    with dissolve
    
    ne "¡No entres!"
    
    show night03_n_pedrera_puking_eyebrows sad
    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Tranquilo,"

    extend " [protname]..." 
        
    ne "En un minuto estoy contigo..."
    
    show night03_n_pedrera_puking_eyebrows surprise
    #show night03_n_pedrera_puking_eye open_surprise
    with dissolve
    
    ne "No te preocup..."
    
    play sound "audio/characters/neus/puke02.ogg"
    
    show night03_n_pedrera_puking_eyes 06
    show night03_n_pedrera_puking_pupils empty
    show night03_n_pedrera_puking_eyebrows angry
    #show night03_n_pedrera_puking_eye closed
    with vpunch
    
    ne "{size=82}BLUEEEEEERGH{/size}"
    
    n "Sin darte tiempo a apartar la vista,"

    n "ves cómo prácticamente todos los rusos negros que había tomado se pierden por el retrete,"

    n "y algo más que debió de haber comido al mediodía,"
       
    n "a juzgar por los trozos sólidos que te parece ver..."
    
    n "Ofreciéndote así, un espectáculo no precisamente demasiado erótico..."
    
    pt "Dios..."

    extend "\nes que me están dando ganas de potar hasta a mí con esto..."
    
    n "Intentas en la medida de lo posible apartar tu mirada de ese espectáculo."
    
    menu night03_MidnightProblem04_GoUp_vomit:
        
        pt "Creo que lo mejor es que la deje sola..."
        
        "<Intentar sacarle una sonrisa y preguntarle si puedes hacer algo para ayudarla>":
            
            call p_Help
            
            $pl.ch_pts("np",3)
            
            jump night03_MidnightProblem04_GoUp_vomit_Leave
        
        "<Ayudarla a ponerla en cama trayendo un cubo para que pueda vomitar si quiere>":
            
            call p_Help
            
            $pl.ch_pts("np",1)
            
            jump night03_MidnightProblem04_GoUp_vomit_Help
    
label night03_MidnightProblem04_GoUp_vomit_Leave:
    
    p "Neus..."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows sad
    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Lo siento [protname]..."
    
    ne "Supongo que peor no he podido hacerlo,"

    extend " ¿Verdad...?"
    
    n "Sus lágrimas aparecen cada vez más evidentes en su rostro,"

    n "sobre todo por el rímel, que dibuja finas líneas negras por sus mejillas."
    
    p "¿Te refieres a que justo cuando te estaba besando te han entrado ganas de vomitar?"
    
    ne "..."
    
    p "Sí..."

    p "Debo reconocer que nunca me hubiera imaginado que llegara a besar tan mal..."
    
    
    show night03_n_pedrera_puking_eyebrows angry
    #show night03_n_pedrera_puking_eye open_angry
    with dissolve
    
    ne "¡No!"

    ne "..."
    
    p "No..."

    extend " ¿Qué?"
    
    ne "No he vomitado porque me estuvieras besando..."

    show night03_n_pedrera_puking_eyebrows angry
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils down
    with dissolve
    
    n "Su rostro es como de niña ofendida mirando a otra parte."

    show night03_n_pedrera_puking_eyebrows sad
    with dissolve
    
    ne "..."

    ne "Idiota..."

    show night03_n_pedrera_puking_pupils front
    with dissolve
    
    p "¿Entonces debo interpretar que no te ha disgustado del todo?"
    
    show night03_n_pedrera_puking_eyebrows surprise
    #how night03_n_pedrera_puking_eye open_surprise
    with dissolve
    
    n "Parece que una ligera sonrisa se dibuja en sus labios."
    
    ne "Claro que no..."
    
    p "Me alegro..."
    
    p "Por un momento pensé que me tenías alergia o algo..."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows sad
    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Idiota..."
    
    n "Da la sensación de que su ceño ya no está tan fruncido."
    
    p "¿Puedo hacer algo para ayudarte?"
    
    ne "No..."
    
    ne "Gracias, [protname],"

    ne "pero ahora preferiría que me dejaras a solas."
    
    p "Como quieras, Neus..."
    
    ne "No sabes cómo funciona el ascensor..."
    
    p "Bajaré por las escaleras,"

    extend "\nno te preocupes."
    
    p "El ejercicio no es algo que me venga de nuevo..."
    
    show night03_n_pedrera_puking_eyes 06
    show night03_n_pedrera_puking_pupils empty
    show night03_n_pedrera_puking_eyebrows sad
    #show night03_n_pedrera_puking_eye open_surprise
    with dissolve
    
    ne "¡Uggh!"
    
    play sound "audio/characters/neus/puke03.ogg"

    show night03_n_pedrera_puking_eyebrows angry
    
    #show night03_n_pedrera_puking_eye closed
    with vpunch
    
    ne "{size=72}BLUEEEEEERGH{/size}"
    
    ne "..."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows sad

    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Lo siento..."
    
    p "No te disculpes."

    show night03_n_pedrera_puking_pupils down
    with dissolve
    
    ne "Ahora mismo te debo parecer la cosa más antierótica del puñetero mundo..."

    show night03_n_pedrera_puking_pupils front
    with dissolve
    
    p "En realidad,"

    extend " lo que estoy pensando es que mañana"
    
    p "tendré que mejorar mis habilidades para besarte mejor..."
    
    p "No me gustaría causarte este efecto una segunda vez..."

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows surprise
    with dissolve

    
    n "Oyes una inocente pero tímida risa."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils down
    show night03_n_pedrera_puking_eyebrows angry

    #show night03_n_pedrera_puking_eye open_angry
    with dissolve
    
    ne "Idiota..."

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows surprise
    with dissolve
    
    p "Buenas noches,"

    extend " Lady Neus."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils down
    show night03_n_pedrera_puking_eyebrows sad

    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Buenas noches..."

    extend "\nmi {a=https://es.wikipedia.org/wiki/Lanzarote_del_Lago}\"Lancelot\"{/a}..."

    show night03_n_pedrera_puking_pupils front
    with dissolve
    
    window hide dissolve
    pause
    
    jump afternight03
    
label night03_MidnightProblem04_GoUp_vomit_Help:
    
    p "Oye,"

    extend " Neus..."

    p "Creo que no estás en muy buenas condiciones..."
    
    p "Déjame ayudarte a llegar a la cama..."
    
    p "Dime dónde guardas un cubo,"

    extend " creo que lo vas a necesitar."

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils down
    show night03_n_pedrera_puking_eyebrows angry
    
    #show night03_n_pedrera_puking_eye open_angry
    with dissolve
    
    ne "..."

    show night03_n_pedrera_puking_eyes 06
    show night03_n_pedrera_puking_pupils empty
    show night03_n_pedrera_puking_eyebrows sad
    with dissolve
    
    p "¿Neus?"

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows angry
    with dissolve
    
    ne "¡Vete!"

    show night03_n_pedrera_puking_pupils down
    with dissolve
    
    p "¿Qué?"

    show night03_n_pedrera_puking_pupils front
    with dissolve
    
    ne "¡Vete!"
    
    p "¿Por qué?"

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils down
    show night03_n_pedrera_puking_eyebrows sad
    
    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Por favor..."

    extend " [protname]..."

    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows angry
    
    #show night03_n_pedrera_puking_eye open_angry
    with dissolve
    
    ne "Lárgate..."

    show night03_n_pedrera_puking_eyes 06
    show night03_n_pedrera_puking_pupils empty
    show night03_n_pedrera_puking_eyebrows sad
    with dissolve
    
    n "Entreabriendo los ojos de nuevo, la encuentras exactamente en el mismo sitio,"
    
    n "pero esta vez reposando su cabeza sobre sus antebrazos sobre el retrete y conteniendo el sollozo."

    show night03_n_pedrera_puking_eyebrows angry
    with dissolve 
    
    p "Bueno..."

    extend " si realmente es lo que quieres..."
    
    show night03_n_pedrera_puking_eyes 01
    show night03_n_pedrera_puking_pupils front
    show night03_n_pedrera_puking_eyebrows sad
    
    #show night03_n_pedrera_puking_eye open_sad
    with dissolve
    
    ne "Sí..."
    
    n "Decides obedecer y apartarte de ahí."

    scene night03_n_pedrera_puking_door closed
    with dissolve

    scene night03_bg_street_pedrera_hall03
    with fade

    scene night03_bg_street_pedrera_flatdoor_open
    with dissolve
    
    n "Sales por la puerta y cierras con suavidad,"

    scene black
    with dissolve
    
    n "no sin antes oír los agudos sollozos de Neus desde el cuarto de baño."
    
    window hide dissolve
    pause

    jump afternight03
    
        
label night03_MidnightProblem04_GoodNight:
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¡¿Que no estoy bien?!"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "El tono de voz de Neus iba aumentando por momentos."
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Talkingx02
    with vpunch
    
    ne "{size=52}¡¿Que no estoy bien?!{/size}"
    
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
    
    ne "¡Que haya bebido un par de copas no significa que ya esté borracha!"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve    
    
    pt "¿Un par de copas dice?"
    
    pt "¡Si se ha bebido por lo menos seis o siete!"
    
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¡Si no quieres subir, lo dices y punto!"
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¡Sé entender un no por respuesta!"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "Si sabes entender que no me gusta hacerlo con mujeres que no están en sus plenas facultades,"
    
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
       
    p "entonces sí,"

    extend "\nlo entiendes."
    
    show neus_exp_iris front02
    show neus_exp_eyes 02
    with dissolve
                                   
    p "De lo contrario,"

    extend " tampoco me interesa si lo has entendido o no."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    with dissolve
    
    ne "..."
    
    n "Se respira una tensión palpitante en el ambiente."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Bah..."

    extend " tú sabrás..."
    
    show neus_exp_iris front03
    show neus_exp_eyes 03
    with dissolve
    
    ne "Buenas no..."
    
    play sound "audio/characters/neus/scream_auch01.ogg"
    
    scene night03_bg street_pedrera_door_opened
    with vpunch
    
    ne "{size=52}¡¡AAUCH!!{/size}"
    
    n "Con la puerta abierta y sin mirar detrás de ella,"
       
    n "choca con el escalón de la puerta y cae al suelo estrepitosamente."
    
    p "¡Neus!"
    
    p "¿Estás bien?"
    
    show neus_body ld_default:
        neus_body_atright_position
    show neus_head:
        neus_body_atright_position
    show neus_arms ld_rest:
        neus_body_atright_position
    show neus_exp_blush 05:
        neus_exp_atright_position
    show neus_exp_mouth sad_Talkingx02:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_eyebrows angryx01:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    ne "¡Que sí!"

    extend " ¡Que sí!"

    ne " ¡Estoy bien!"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "De forma torpe consigue volver a ponerse en pie."
    
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¡Todo el mundo puede tropezar!"

    ne "¡¿No?!"
    
    show neus_exp_iris front01
    show neus_exp_eyes 01
    with dissolve
    
    ne "¡Buenas noches!"
    
    play sound "audio/sfx/door_slam01.ogg"

    scene night03_bg street_pedrera_door
    with hpunch
    
    n "Oyes cómo cierra la puerta dando un fuerte portazo."
    
    window hide dissolve
    
    pause
    
    jump afternight03
    
        ### CHALLENGE: Boolean of apologie for the next time.
        
        ##NOT FINISHED
        
label night03_MidnightProblem04_TopicChange:
    
    p "Antes me habías comentado que querías hacerme una serie de preguntas."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Qué mierda de proposición es esta?"
        
    ne "¿Dónde te sacaste el título de caballero?"
    
    show neus_exp_eyebrows sadx01
    with dissolve
    
    ne "¿En una cuadra pordiosera?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    ne "..."
    
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Preguntas...?"
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front04
    show neus_exp_eyes 04
    with dissolve
    
    ne "¿Qué preguntas?"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "Eso quería saber yo..."

    p "Pero supongo que mañana,"

    extend " cuando volvamos a quedar,"

    p "será un mejor momento para seguir hablando."
    
    p "¿No te parece?"
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    with dissolve
    
    ne "Eummm..."
    
    show neus_exp_eyebrows normal
    show neus_exp_iris left03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "sí..."

    ne "supongo que sí."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris front02
    show neus_exp_eyes 02
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    p "¿Tienes que subir muchos escalones?"
    
    show neus_exp_eyebrows angryx01
    show neus_exp_iris front04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "¿Por qué?"

    ne "¿Acaso te parece que vaya en silla de ruedas?"
    
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    pt "Diría que se pone un poco hostil cuando bebe,"
    
    pt "pero creo recordar que incluso antes de entrar en el bar ya respondía de esta manera."
    
    show neus_exp_eyebrows sadx01
    show neus_exp_iris left04
    show neus_exp_eyes 04
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "Bah..."
    
    ne "Tranquilo,"

    ne "el edificio será antiguo,"

    extend " pero tiene ascensor,"
    
    show neus_exp_eyebrows normal
    show neus_exp_iris down03
    show neus_exp_eyes 03
    show neus_exp_mouth sad_Talkingx02
    with dissolve
    
    ne "puedes bajar la guardia..."

    ne "tu damisela no está en peligro."
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front03
    show neus_exp_eyes 03
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Aunque agradezco tu preocupación..."
    
    show neus_exp_eyebrows normal
    show neus_exp_iris front06
    show neus_exp_eyes 06
    show neus_exp_mouth happy_Silentx04
    with dissolve
    
    p "..."
    
    n "Inclinas un poco la cabeza ante ella con un ligero toque teatral."
    
    show neus_exp_iris front04
    show neus_exp_eyes 04
    with dissolve
    
    p "Entonces te deseo buenas noches,"

    extend "\n{i}Lady Neus{/i}."
    
    show neus_exp_mouth happy_Talkingx03
    with dissolve
    
    ne "Dulces sueños,"

    extend "\nmi querido \"Lancelot\"."
    
    show neus_exp_eyebrows surprisex01
    show neus_exp_iris left01
    show neus_exp_eyes 01
    show neus_exp_mouth sad_Silentx03
    with dissolve
    
    n "Y no con menos torpeza,"
    
    scene night03_bg street_pedrera_door
    with hpunch
       
    n "atraviesa el portal, cerrando la entrada de un portazo, usando el pomo para no caerse al suelo."
    
    window hide dissolve
    
    pause
    
    jump afternight03

    
label afternight03:

    $ saturation_tint_level = "superdark"
    
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    
    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    
    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade

    n "Entras en casa despacio, sin hacer demasiado ruido,"

    n "dejando las llaves con suavidad sobre la mesita de entrada."

    play sound "audio/sfx/metal_keys_deposit.ogg"
    

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    pt "A estas horas Dídac debe de estar durmiendo,"

    pt "lo mejor será darse una ducha rápida e ir a la cama."

    pt "Ha sido un día largo..."

    n "Dejas la ropa en la cocina, donde está la cesta de la ropa sucia y te diriges al baño."
    
    scene afternight03_bg hallway_doorclosed with fade

    n "Justo cuando llegas al pasillo donde están las habitaciones y el baño,"

    n "oyes el ruido de una puerta abriéndose."

    $ saturation_tint_level = "verydark"
    
    show afternight03_bg hallway_dooropen with dissolve

    n "Al alzar la vista para mirar a la puerta que conduce al cuarto de baño, ves, a contraluz," 

    show didacfbodybelow naked:
        dfbody_center_little
    show didacfbodybelow_naked_drops 01:
        dfbody_center_little
    show didacfbodytop naked:
        dfbody_center_little
    show didacfbodytop_naked_drops 01:
        dfbody_center_little
    show didacfhandl hip_naked:
        dfbody_center_little
    show didacfhandl_hip_naked_drops 01:
        dfbody_center_little
    show didacf_blush 01:
        dexpressions_center_little
    show didacf_eyes 00:
        dexpressions_center_little
    show didacf_pupils front00:
        dexpressions_center_little
    show didacf_eyebrows surprisex01:
        dexpressions_center_little
    #show didacfbodytop_hair_wet:
        #dfbody_center
    show didacfbodytop_hair wet_01:
        dfbody_center
    show didacfhandr towel:
        dfbody_center_little
    show didacf_mouth sad_Silentx03:
        dexpressions_center_little

    with dissolve
    
    window hide dissolve
    pause
       
    n "el cuerpo de una mujer con un cuerpo fibroso, musculado, y con un pecho voluptuoso,"
    
    show didacf_blush 01
    show didacf_eyes 01
    show didacf_pupils down01
    with dissolve

    n "desnuda, con el pelo aún mojado, y con una toalla en los hombros que apenas le oculta uno de sus pezones."
    
    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows serious
    with dissolve

    p "Euh..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve

    n "La sorpresa te deja sin habla."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¿Se puede saber qué coño haces desnudo en medio del pasillo tío?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Euh..."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx04
    with dissolve

    n "Una figura húmeda y desnuda, brillando con la luz del baño,"

    n "mostrando sus marcadas curvas, un cuerpo perfectamente esculpido."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve

    n "Esa visión te impide pensar una respuesta más elaborada."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Pues..."

    extend " iba a ducharme..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx04
    with dissolve

    d "Hummm..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    pt "¡¿Dónde está ese cuerpo alto,"

    extend " voluminoso,"

    extend " y de armario"

    extend "\nde mi compañero de piso?!"


    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "¡¿Es que no se ha visto en el espejo?!"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx05
    with dissolve
    
    pt "¿Por qué diablos está tan tranquilo?"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Quizás son imaginaciones tuyas,"

    n "pues con la oscuridad del pasillo apenas puedes ver a contraluz,"

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    n "pero te da la sensación de que sus ojos te están mirando la entrepierna."

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "Bueno,"

    extend " yo ya he terminado de ducharme..."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Talkingx002
    with dissolve
       
    d "hoy no ha hecho falta que me ayudases..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Una voz dulce y femenina, con un toque tímido pero irritado,"

    n "se desprende de su garganta al decirte esas palabras."

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    n "Ambos os quedáis quietos sin decir nada,"

    n "mirándoos el uno al otro en la oscuridad del pasillo."

    show didacf_blush 04
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    n "Tus ojos no pueden apartar la vista del pezón que está al descubierto."

    show didacf_blush 04
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    d "..."

    show didacf_blush 03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "Eres un puto enfermo, [protname]..."

    d "¿Qué coño me estás mirando?"

    show didacfbodybelow naked:
        dfbody_center_close_little
    show didacfbodybelow_naked_drops 01:
        dfbody_center_close_little
    show didacfbodytop naked:
        dfbody_center_close
    show didacfbodytop_naked_drops 01:
        dfbody_center_close
    show didacfhandl hip_naked:
        dfbody_center_close
    show didacfhandl_hip_naked_drops 01:
        dfbody_center_close
    show didacf_blush 02:
        dexpressions_center_close
    show didacf_eyes 04:
        dexpressions_center_close
    show didacf_pupils front04:
        dexpressions_center_close
    show didacf_eyebrows angryx02:
        dexpressions_center_close
    show didacfbodytop_hair wet_01:
        dfbody_center_close
    show didacfhandr towel:
        dfbody_center_close
    show didacf_mouth sad_Silentx04:
        dexpressions_center_close


    with dissolve

    window hide dissolve
    pause
    
    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "¡He preguntado qué coño miras!"

    show didacfbodybelow naked:
        dfbody_center_superclose
    show didacfbodybelow_naked_drops 01:
        dfbody_center_superclose
    show didacfbodytop naked:
        dfbody_center_superclose
    show didacfbodytop_naked_drops 01:
        dfbody_center_superclose
    show didacfhandl hip_naked:
        dfbody_center_superclose
    show didacfhandl_hip_naked_drops 01:
        dfbody_center_superclose
    show didacf_blush 03:
        dexpressions_center_superclose
    show didacf_eyes 05:
        dexpressions_center_superclose
    show didacf_pupils front05:
        dexpressions_center_superclose
    show didacf_eyebrows angryx03:
        dexpressions_center_superclose
    show didacfbodytop_hair wet_01:
        dfbody_center_superclose
    show didacfhandr towel:
        dfbody_center_superclose
    show didacf_mouth sad_Silentx04:
        dexpressions_center_superclose

    with dissolve

    window hide dissolve
    pause

    pt "Está muy cerca..."
    
    menu afternight03_Didac_AfterShower:
            
        pt "¿Que qué miro?" 
            
        "Dídac... tienes unos melones increíbles...":
            
            call p_Help
            
            $pl.ch_pts("dp",3)
            
            $ afternight03_Didac_AfterShower_Melons = True
                    
            jump afternight03_Didac_AfterShower_Watching
            
        "¡Joder! ¡Vas desnuda! ¡¿Qué quieres que mire?!":
            
            call p_Help
            
            $pl.ch_pts("dp",1)
                    
            jump afternight03_Didac_AfterShower_Watching
    
label afternight03_Didac_AfterShower_Watching:
    
    if afternight03_Didac_AfterShower_Melons == True:

        show didacf_blush 03
        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx01
        with dissolve
        
    else:

        show didacf_blush 02
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx03
        with dissolve

        
    d "{size=32}¡¿Es que acaso quieres hacer algo más que mirar?!{/size}"

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx001
    with dissolve
    
    d "{size=18}Puto enfermo...{/size}"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Sientes el calor que desprende su cuerpo,"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve
    
    n "claro indicio de que se ha dado una ducha bien caliente aun estando en pleno verano."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx04
    with dissolve

    n "No huele a perfume de mujer, sino al jabón varonil que soléis usar ambos."

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    n "Aun así, la impresión que te da al tenerla tan cerca es de todo menos varonil."
    
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx05
    with dissolve 
    
    pt "Pero, ¡¿qué diablos le pasa?!"
    
    window hide dissolve
    pause

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "Tío..."

    d "¡¿En serio?!"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx04
    with dissolve

    n "Cuando inclinas la cabeza para mirar tus partes íntimas, te percatas de que tienes una tremenda erección."
    

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "Así no hace falta que me confirmes que te alegro la vista..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "{size=35}¡Sexópata-degenerado-homosexual-sinvergüenza!{/size}"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Dídac..."

    extend " yo..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "No pasa nada..."

    d "supongo que es normal,"

    extend " me imagino que yo también reaccionaría así,"

    d "al fin y al cabo..."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    n "Se desliza por tu lado haciendo que su cadera y la tuya se toquen levemente,"
    
    scene afternight03_bg hallway_dooropen with hpunch
    play sound "audio/sfx/hit02.ogg"
       
    n "rozando ligeramente tu miembro viril con cierto descaro."

    pt "¡¿Pero qué demonios le pasa?!"

    pt "¿Lo ha hecho a propósito?"
    
    n "Después de mirar la silueta oscura de tu compañero (¿o compañera?) de piso desaparecer al entrar en la habitación," 
       
    n "decides que ahí en medio no haces nada."

    play music "audio/sfx/shower01.ogg" fadeout 3.0 fadein 3.0
    
    scene afternight03_bg shower with fade

    n "Entras en el baño y te tomas una ducha con agua más bien fría... "

    n "Mientras te duchabas no has podido evitar tener la sensación"

    n "de que alguien te estaba observando desde fuera del cuarto."

    p "..."

    pt "Bah..."

    extend " serán imaginaciones mías."

    play music "audio/music/kevinmacleod/senbazuru_restaurant.ogg" fadeout 3.0 fadein 3.0
    
    scene beds_night_lightOff_blindUp_DemptyMCempty
    show beds_D03b_night_lightOff_blindUp
    with fade

    n "Regresas a la habitación con una toalla cubriéndote del ombligo para abajo."

    n "Encuentras a tu compañero/a aparentemente durmiendo en la cama desprovista de sábana alguna,"

    n "con el cuerpo completamente desnudo y el pelo tapándole parte del rostro."

    n "No puedes evitar sentir cómo la sangre fluye de nuevo entre tus piernas" 
       
    n "y hace presión sobre la toalla que te cubre medio cuerpo."
    
    show afternight03_bg room02 #Cajón con ropa en la oscuridad.
    with dissolve

    n "Ignorando tus impulsos primarios, te acercas al cajón de la ropa y te quitas la toalla."

    play sound "audio/characters/didac/moanings06.ogg"

    d "Hummm..."

    n "Oyes un suave pero sonoro gemido femenino que proviene de su cama," 
       
    n "que consigue ponerte aún más nervioso, si es posible."

    n "Te giras inconscientemente para mirar detrás de ti."
    
    $ saturation_tint_level = "verydark"

    scene afternight03_didac_bedroom_onbed_body
    show afternight03_didac_bedroom_onbed_eyebrows surprise
    show afternight03_didac_bedroom_onbed_eyes front02
    show afternight03_didac_bedroom_onbed_pupils front02
    show afternight03_didac_bedroom_onbed_mouth sad_Talking
    show afternight03_didac_bedroom_onbed_hair
    show light 01_moon:
        xanchor 0.25 yanchor 0.3 rotate -60 zoom 0.5 additive 1.0
        
        parallel:
            ease 10.0 rotate -62
            ease 10.0 rotate -58
            repeat
            
        parallel:
            ease 30.0 zoom 1.0
            ease 30.0 zoom 0.6
            repeat
    
    with fade

    play music "audio/music/didac_theme.ogg" fadeout 3.0 fadein 3.0

    d "Veo que el mástil sigue estando bien firme..."
    
    show afternight03_didac_bedroom_onbed_eyebrows angry
    show afternight03_didac_bedroom_onbed_eyes front02
    show afternight03_didac_bedroom_onbed_mouth sad_Talking
    with dissolve
    
    d "¿Es que no tienes vergüenza?"
    
    show afternight03_didac_bedroom_onbed_eyebrows angry
    show afternight03_didac_bedroom_onbed_eyes front02
    show afternight03_didac_bedroom_onbed_mouth sad_Silent
    with dissolve

    n "En la penumbra de la habitación iluminada a duras penas por una luna creciente,"

    n "ves a tu compañero de piso estirado en la cama boca abajo."

    p "Dídac..."

    p "pe-"

    extend "pensé que estarías durmiendo... "
    
    show afternight03_didac_bedroom_onbed_eyebrows surprise
    show afternight03_didac_bedroom_onbed_eyes front02
    show afternight03_didac_bedroom_onbed_mouth sad_Talking
    with dissolve

    d "Ya ves que no..."

    scene beds_night_lightOff_blindUp_DemptyMCempty_blur02
    show didacfbodybelow naked:
        dfbody_center_little
    show didacfbodybelow_naked_drops 00:
        dfbody_center_little
    show didacfbodytop naked:
        dfbody_center_little
    show didacfbodytop_naked_drops 00:
        dfbody_center_little
    show didacfhandl hip_naked:
        dfbody_center_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_center_little
    show didacf_blush 03:
        dexpressions_center_little
    show didacf_eyes 04:
        dexpressions_center_little
    show didacf_pupils down04:
        dexpressions_center_little
    show didacf_eyebrows surprisex01:
        dexpressions_center_little
    show didacfbodytop_hair:
        dfbody_center_little
    show didacfhandr leg_naked:
        dfbody_center_little
    show didacf_mouth happy_Silentx02:
        dexpressions_center_little

    with dissolve
    
    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
    
    window hide dissolve
    pause

    n "Se levanta de la cama," 

    show didacf_eyebrows normal
    with dissolve
       
    n "sin cubrirse en absoluto su cuerpo desnudo."

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    n "Los detalles no se aprecian en la penumbra de la habitación,"

    show didacf_eyebrows sadx01
    with dissolve

    n "pero puedes ver claramente el brillo de su piel y la grácil silueta de su cuerpo."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx05
    with dissolve
    
    pt "¡¿Él me habla de vergüenza?!"

    pt "¡Es él quien está durmiendo en pelotas!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "Aún no me has respondido a la pregunta que te hice antes."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx03
    with dissolve


    p "¿Pre-"

    extend "pregunta?"

    scene beds_night_lightOff_blindUp_DemptyMCempty_blur03
    show didacfbodybelow naked:
        dfbody_center_superclose
    show didacfbodybelow_naked_drops 00:
        dfbody_center_superclose
    show didacfbodytop naked:
        dfbody_center_superclose
    show didacfbodytop_naked_drops 00:
        dfbody_center_superclose
    show didacfhandl hip_naked:
        dfbody_center_superclose
    show didacfhandl_hip_naked_drops 00:
        dfbody_center_superclose
    show didacf_blush 02:
        dexpressions_center_superclose
    show didacf_eyes 04:
        dexpressions_center_superclose
    show didacf_pupils left04:
        dexpressions_center_superclose
    show didacf_eyebrows angryx01:
        dexpressions_center_superclose
    show didacfbodytop_hair:
        dfbody_center_superclose
    show didacfhandr leg_naked:
        dfbody_center_superclose
    show didacf_mouth sadbiting_Silentx02:
        dexpressions_center_superclose
    with dissolve

    n "Se detiene a escasos centímetros de tu pene, duro como una roca."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows serious
    with dissolve
    
    pt "¿Está intentando rozar con su cadera la punta de mi polla?"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve

    d "..."

    show didacf_blush 03
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve
       
    p "..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx02
    with dissolve

    p "¿A..."

    extend " qué pregunta te-"

    extend "te refieres?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Talkingx04
    with dissolve

    d "Te gustaría tocarme..."

    d "¿Verdad que sí?"

    d "Degenerado mental..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Silentx04
    with dissolve
    
    menu afternight03_Didac_LikeToTouch:
            
        pt "¿Que si me gustaría tocarle?" 
            
        "No recuerdo que me hicieras esa pregunta...":
            
            call p_Help
            
            $pl.ch_pts("dp",-1)
                    
            jump afternight03_Didac_LikeToTouch_DontRemember
            
        "Dídac, nunca te haría esa pregunta. ¡Eres mi jodido amigo!":
            
            call p_Help
            
            $pl.ch_pts("dp",-5)
                    
            jump afternight03_Didac_LikeToTouch_YoureMyFriend
            
        "La verdad es que no me disgustaría...":
            
            call p_Help
            
            $pl.ch_pts("dp",3)
                    
            jump afternight03_Didac_LikeToTouch_IwouldLikeToTouchYou 

label afternight03_Didac_LikeToTouch_IwouldLikeToTouchYou:

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    d "..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    jump afternight03_Didac_LikeToTouch_WhatsWrongWithYou
    
label afternight03_Didac_LikeToTouch_YoureMyFriend:

    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve
    
    d "..."

    show didacf_blush 01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    jump afternight03_Didac_LikeToTouch_WhatsWrongWithYou
    
label afternight03_Didac_LikeToTouch_DontRemember:

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Notas tu boca completamente seca, te ves incapaz hasta de tragar saliva."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    d "Humm..."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "Quizás no..."

    extend "\nPero, ¿acaso me equivoco?"

    show didacf_blush 03
    show didacf_eyes 02
    show didacf_pupils down02
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx03
    with dissolve
    
    d "Solo hay que ver cómo tienes la"

    extend "\n{size=32}polla{/size}..."

    d "puto enfermo..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    pt "¡¿Y quién coño ha sido el que se ha acercado a mí rozándomela con su cuerpo desnudo?!"

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows normal
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
label afternight03_Didac_LikeToTouch_WhatsWrongWithYou:
    
    play music "audio/music/didac_theme.ogg" fadein 2.0 fadeout 2.0
    
    p "Dídac..."

    p "¿Se puede saber qué te pasa?"

    show didacf_blush 02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "¿Que qué me pasa?"

    show didacf_blush 01
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve
       
    d "¡Joder si lo supiera!"

    show didacf_blush 00
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡Por si no lo has notado, yo sí he perdido mi polla!"

    show didacf_eyes 01
    show didacf_pupils downLeft01
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "Tengo dos pechos que a cada hora que pasa van creciendo más y más..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "{size=38}¡Llevo dos días aquí encerrado sin poder salir!{/size}"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve

    p "Lo siento..."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "Me dijiste que era mejor que no fuera al hospital..."

    d "que era una simple fiebre..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Pero parece que sabías muy bien lo que me estaba pasando..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx07
    with dissolve


    d "y por eso evitaste a toda costa que me viera un médico."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¡Hasta me bañaste con tus manos desnudas!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx04
    with dissolve

    pt "Ayer no pareció molestarle tanto..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "[protname]..."

    extend " ¿Qué es lo que no me estás contando?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Bue-"

    extend "bueno..."

    extend " realmente sé muy poco... "

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "Sé quién es la responsable de lo que te ocurre y..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¡¿Hay una responsable?!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "{size=32}¡¿Quién?!{/size}"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Eumm..."

    p "bueno..."

    extend " digamos que fue la víctima del accidente del cuarto de baño en la escuela de Ilustración."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "¿Accidente?"
    
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¿En la escuela?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "¡¿De qué estás hablando?!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Como si no te acordaras de lo que le hiciste a..."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx05
    with dissolve

    d "¿Humm...?"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "A..."

    extend " Bueno,"

    p "el caso es que sé quién puede ayudarte."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¿De verdad?"

    extend " ¡¿Hay cura?!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Eso parece..."

    p "estoy trabajando en ello."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡¿Y a qué estás esperando?! ¡imbécil!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Antes tengo que hacerle unos favores a alguien..."

    p "como bien sabes,"

    extend " las cosas no se regalan porque sí..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "[protname]..."

    extend " como no te des prisa, creo que me voy a volver loca..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06
    with dissolve

    pt "¿Loca?"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Hay algo que debes tener claro antes que nada."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Es importantísimo que bajo ningún concepto te quedes embarazada."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "{size=35}¡¿Qué?!{/size}"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx03
    with dissolve

    pt "Que esa frase saliera de mis labios me resultó realmente muy bizarra..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx03
    with dissolve
        
    pt "y más diciéndosela a mi compañero de piso y amigo de infancia que ahora tiene cuerpo de \"{a=https://es.wikipedia.org/wiki/Mujer_fatal}{i}femme fatale{/i}{/a}\"..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "¡¿De qué puñetas me estás hablando?! ¡jodido enfermo!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Solo te digo que, si te quedas encinta,"

    p "jamás podrás regresar a tu forma de hombre."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx03
    with dissolve

    d "..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡¿Puedo quedarme embarazada?!"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx06
    with dissolve

    p "Eso parece..."

    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx07
    with dissolve

    d "..."

    show didacf_eyes 01
    show didacf_pupils right01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx08
    with dissolve
    
    n "Parecía como si lo que le había dicho le hubiera afectado más de lo que esperaba..."

    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx09
    with dissolve
    
    pt "¿Por qué pone esa cara?"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx04
    with dissolve
        
    pt "O sea,"

    extend " entiendo el drama de que quedarte por siempre como mujer puede ser traumatizante..."

    show didacf_blush 03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve
    
    pt "Pero nadie va a violarlo si se queda encerrado en casa..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx07
    with dissolve
    
    pt "y aunque saliera,"

    extend " a menos que lo hiciera de noche en rincones oscuros totalmente desnuda,"

    show didacf_blush 02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    pt "tampoco es algo que ocurra de forma sencilla,"

    extend " precisamente."

    show didacf_blush 03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."

    show didacf_blush 02
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Será mejor que durmamos un poco,"

    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "para mí ha sido un día un tanto largo,"

    p "y mañana sábado podremos hablar mejor del asunto."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx01
    with dissolve
    
    p "¿Te parece?"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve
    
    d "..."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx01
    with dissolve
    
    d "Sí,"

    extend " quizás tengas razón."
    
    scene beds_night_lightOff_blindUp_DemptyMCbusy
    show beds_D03b_night_lightOff_blindUp
    with fade
    
    n "Ambos os metéis en la cama."
    
    n "Aunque él seguía sin taparse lo más mínimo..."
    
    scene black
    with fade
    
    n "Tus párpados caen sumiéndote en un profundo sueño."

    window hide dissolve
    
    pause
    
    jump morning04

