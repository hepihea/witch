
default afternoon04_waxbar_fcbcn_Cond = False
default p_prot_analgesic = ""

#Afternoon04_Images


image afternoon04_paint empty = "images/general/empty.webp"

        ##Paints Classic
image afternoon04_paint c_giovanni_madonna = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_giovanni_madonna.webp"
image afternoon04_paint c_gustavecourbet_originedumonde = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_gustavecourbet_originedumonde.webp"
image afternoon04_paint c_miguelangel_creationofadam = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_miguelangel_creationofadam.webp"
image afternoon04_paint c_visoki_crucifixion = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_visoki_crucifixion.webp"
image afternoon04_paint c_fussli_nightmare = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_fussli_nightmare.webp"
image afternoon04_paint c_fussli_nightmare_02 = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_fussli_nightmare_02.webp"
image afternoon04_paint c_goya_akelarre1797 = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_goya_akelarre1797.webp"
image afternoon04_paint c_mucha_lepater = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_mucha_lepater.webp"
image afternoon04_paint c_waterhouse_magiccircle = "images/day04/afternoon04/paint_clas/afternoon04_paint_c_waterhouse_magiccircle.webp"

        ##Paints Modern
image afternoon04_paint m_dali_granmast = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_dali_granmast.webp"
image afternoon04_paint m_dali_persistentofmemory = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_dali_persistentofmemory.webp"
image afternoon04_paint m_duchamp_fountain = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_duchamp_fountain.webp"
image afternoon04_paint m_magritte_treacheryofimages = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_magritte_treacheryofimages.webp"
image afternoon04_paint m_magritte_treacheryofimages_02 = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_magritte_treacheryofimages_02.webp"
image afternoon04_paint m_paulnoth_rabbitduckarmy = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_paulnoth_rabbitduckarmy.webp"
image afternoon04_paint m_picasso_guernica = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_picasso_guernica.webp"
image afternoon04_paint m_pollock_number01 = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_pollock_number01.webp"
image afternoon04_paint m_warhol_selfportrait = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_warhol_selfportrait.webp"

image afternoon04_paint m_pietm_compositionwithredblueandyellow = "images/day04/afternoon04/paint_mod/afternoon04_paint_m_pietm_compositionwithredblueandyellow.webp"
image afternoon04_paint inMACBA_Txell_Mucus = "images/day04/afternoon04/inMACBA_art/afternoon04_paint_inMACBA_Txell_Mucus.webp"
image afternoon04_paint inMACBA_Txell_StripedAss = "images/day04/afternoon04/inMACBA_art/afternoon04_paint_inMACBA_Txell_StripedAss.webp"
image afternoon04_paint inMACBA_Txell_ManTable = "images/day04/afternoon04/inMACBA_art/afternoon04_paint_inMACBA_Txell_ManTable.webp"
image afternoon04_paint inMACBA_Txell_Succubus = "images/day04/afternoon04/inMACBA_art/afternoon04_paint_inMACBA_Txell_Succubus.webp"

    #Afternoon04_Backgrounds
image afternoon04_bg macba_outside = "images/day04/afternoon04/afternoon04_bg_macba_outside.webp"
image afternoon04_bg macba_entrance = "images/day04/afternoon04/afternoon04_bg_macba_entrance.webp"
image afternoon04_bg macba_posters = "images/day04/afternoon04/afternoon04_bg_macba_posters.webp"
image afternoon04_bg macba_room01 = "images/day04/afternoon04/afternoon04_bg_macba_room01.webp"
image afternoon04_bg macba_room02 = "images/day04/afternoon04/afternoon04_bg_macba_room02.webp"
image afternoon04_bg macba_infantile = "images/day04/afternoon04/afternoon04_bg_macba_room_infantile.webp"

# afternoon04_grabbingdick

image afternoon04_macba_grabbingdick = "images/day04/afternoon04/afternoon04_macba_grabbingdick.webp"

# afternoon04_macba_txellwalkingaway

image afternoon04_macba_txellwalkingaway normal = "images/day04/afternoon04/afternoon04_macba_txellwalkingaway_normal.webp"
image afternoon04_macba_txellwalkingaway briefcase = "images/day04/afternoon04/afternoon04_macba_txellwalkingaway_briefcase.webp"

image afternoon04_macba_briefcase = "images/day04/afternoon04/afternoon04_macba_briefcase.webp"


transform afternoon04_macba_whisper_pos:
    subpixel True
    zoom 1.0 xanchor 0.5 yanchor 0.5
    easeout_quad 5.0 zoom 0.5 xanchor 0.0 yanchor 0.0


label afternoon04_TxellMacba:

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ saturation_tint_level = "default"
    $ meyesc = ""

    stop music fadeout 3.0
    
    $ afternoon04_TxellMacbaDate = True

    $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    
    ###
    
    scene afternoon04_bg macba_outside
    with fade

    gm "Bueno,"

    extend " por lo menos veo que eres puntual."

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.set_volume(0.2, delay=10.0, channel='sfx1')
    
    #La chica está fumando un cigarrillo largo. #NOT FINISHED
    show afternoon04_paint empty:
        xanchor 0.25 yanchor 0.25 zoom 1.0
    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_blush 00:
        #m_face_atright_position
    #show m_exp_mouth serious_Silentx01:
        #m_face_atright_position
    #show m_exp_eyes 04:
        #m_face_atright_position
    #show m_exp_piris front04:
        #m_face_atright_position
    ##show m_pupils front04a:
        #m_face_atright_position
    #show m_exp_eyebrows surprisex001:
        #m_face_atright_position
    #with dissolve
    #
    # pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Silentx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex01:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    p "Euh..."

    
    pt "Cuando me dio su número de teléfono,"

    pt "parecía mucho más simpática..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    n "En realidad aún faltan escasos minutos para que sean las tres de la tarde."
    
    n "La plaza delante del emblemático edificio de Richard Meier se encuentra frecuentada por un considerable número de {i}skaters{/i},"
    
    n "así como también de un número considerable de adolescentes comiéndose el almuerzo en pequeños {i}guettos{/i}."
    
    p "..."
    
    pt "¿No tenía los ojos de otro color?"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Y bien,"

    extend " ¿has comido?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "Euh,"

    extend " no..."

    p "No he almorzado aún."
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Quizás debería habértelo dicho antes,"

    extend " yo sí he comido ya."
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Toma,"

    extend " cómete este sándwich."

    gm "No es mucho,"

    extend " pero te bastará por ahora."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_sandwich_question:
        
        pt "¿Me está tratando como a un perro?"
        
        "No, gracias.":
            
            call p_Help
            
            $pl.ch_pts("mp",1)
                  
            jump afternoon04_sandwich_reject
        
        "<Cogerlo> Gracias":
            
            call p_Help
            
            jump afternoon04_sandwich_accept
    
label afternoon04_sandwich_accept:
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "De nada."
    
    jump afternoon04_sandwith_after
    
label afternoon04_sandwich_reject:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Bah..."

    gm "Como quieras."
    
    jump afternoon04_sandwith_after
    
label afternoon04_sandwith_after:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Te gustan los museos?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_LikeMuseums_question:
        
        pt "Lo que sí sé... es que no sería mi primera opción para una {b}primera cita{/b}."
        
        "La verdad es que me aburren.":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
                  
            jump  afternoon04_LikeMuseums_boring
        
        "¡Me encantan!":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
            
            jump  afternoon04_LikeMuseums_Ilovethem
            
        "Depende del museo.":
            
            call p_Help
            
            jump  afternoon04_LikeMuseums_Depend
            
label afternoon04_LikeMuseums_Ilovethem:
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "No hace falta que grites..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Ni que tuvieras ocho años..."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Qué simpatía desprende esta mujer..."
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
    
    #NOT FINISHED
            
label afternoon04_LikeMuseums_boring:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Supongo que pedirle algo de reflexión,"

    extend " estudio,"

    extend " y cultura,"

    gm "a un montón de testosterona con patas,"

    extend " es demasiado..."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    p "..."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    pt "No está siendo para nada la misma de ayer..."

    pt "¿Es bipolar,"

    extend " o qué pasa?"
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
    
    #NOT FINISHED
    
label afternoon04_LikeMuseums_Depend:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Depende de si el museo es de cera o del Barça,"

    extend " ¿no?"
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."
    
    menu afternoon04_waxbar_question:
        
        pt "¿Me está provocando?"
        
        "¿Qué tienes en contra del Museo de Cera de Barcelona?":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
                  
            jump  afternoon04_waxbar_waxbcn
        
        "¿Qué tienes en contra del Museo del Fútbol Club Barcelona?":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
            
            jump  afternoon04_waxbar_fcbcn
            
        "La verdad es que no me gusta ninguno de los dos...":
            
            call p_Help
                
            $pl.ch_pts("mp",+1)
            
            jump  afternoon04_waxbar_none
            
        "¿Por qué? ¿Son los únicos que conoces?":
            
            call p_Help
            
            $pl.ch_pts("mp",+2)
            
            jump  afternoon04_waxbar_incite
            
label afternoon04_waxbar_waxbcn:
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Recuerdo cuando era pequeña."
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    #show m_pupils right02a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Era pasear por la rambla,"

    gm "pasar justo delante,"

    extend " y querer recorrer ese callejón para llegar al fondo y ver a Superman y C3-PO,"
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows normal
    with dissolve
        
    gm "encaramados en el tejado de la entrada del museo."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Conseguir las entradas,"

    extend " y recorrer sus estancias llenas de decoraciones mágicas,"
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows serious
    with dissolve
        
    gm "estatuas memorables,"

    extend " historia,"

    extend " cultura,"

    extend " y música ambiente."
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "También recuerdo haberme acercado hace un par de años,"

    extend " siendo ya mayorcita."
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 06
    show m_exp_piris front06
    #show m_pupils right05a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "No paramos de reír en todo el rato."

    gm "Reíamos de lo mal hechas que están,"
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
        
    gm "lo poco distintas que son entre ellas,"

    gm "salvo por las pelucas y los ropajes."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Gracias a los cartelitos,"

    extend " puedes saber a quién se refieren,"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "y aun así, es difícil encontrar el rostro de esas personas reflejado en la figura."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Lo único realmente interesante es la antigüedad del edificio,"

    gm "cómo están adornadas algunas estancias,"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris left03
    #show m_pupils left03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "y especialmente el bar {a=http://www.museocerabcn.com/en/bosc.html}{i}El Bosc de les Fades{/i}{/a} que hay al lado."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    #show m_pupils left03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "El cual no ha cambiado en veinte años,"

    gm "pero sigue siendo igual de mágico."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows sadx01
    with dissolve
    
    pt "No me da la sensación de que odie el lugar,"

    pt "sino más bien como si le entristeciera un lugar que antaño amó tanto."
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
            
label afternoon04_waxbar_fcbcn:

    $ afternoon04_waxbar_fcbcn_Cond = True
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Qué tengo en contra de una disciplina deportiva que se ha convertido en el circo romano moderno,"
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "donde veintidós niñatos millonarios chutan un balón,"

    gm "para que millones de espectadores cómodamente sentados en sofás o en bares,"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "la mayoría de los cuales suelen ser cuarentones barrigudos,"

    gm "con una birra en una mano"

    extend " y un cigarro en la otra,"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "mientras despotrican a esos chavales por qué no corren más con los millones que cobran?..."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Cualquier multitud movida por una idea tan básica como unos colores,"

    extend " o un \"enfrentamiento\" deportivo,"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "merece mi desprecio por conseguir que se les lavara el cerebro de esa forma tan simple."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "El deporte es mucho más que eso;"

    p "se trata de valores,"

    extend " de respeto,"

    extend " de deportividad,"

    extend " de juego limpio,"

    extend " de sana y justa competitividad..."
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Eso crees?"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Entonces,"

    gm "el básquet,"

    extend " el balonmano,"

    extend " el rugby,"

    extend " el waterpolo,"

    extend " el hockey,"

    extend " el fútbol femenino..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "¿No son deportes que tratan los mismos valores?"
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Qué gritan los aficionados cuando pierden un partido importante, o una liga?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Si han jugado mal,"

    extend " se les critica,"

    p "pero hay veces en los que el aficionado ha dado su apoyo."

    p "¡No me jodas!"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Ya..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Sea la directiva,"

    extend " el entrenador,"

    extend " o algún jugador,"

    gm "siempre acaba recibiendo y se va a la calle."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Porque no importa si han jugado bien o mal,"

    gm "siempre debe haber un responsable para echarle toda la culpa y limpiar la imagen."
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "El fútbol es un negocio,"

    gm "como lo es la comida rápida,"

    extend " o la telebasura."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Un servicio simple de entender,"

    gm "que ofrece adicción,"

    extend " morbo,"

    extend " y entretenimiento."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "{a=https://es.wikipedia.org/wiki/Panem_et_circenses}Pan y circo{/a}."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
            
label afternoon04_waxbar_none:
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Hmm..." #Cara aburrida
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
            
label afternoon04_waxbar_incite:
            
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "..." #Cara cabreada.
    
    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Hmm..." #Cara sonriente.
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
    
label afternoon04_LikeMuseums_MuseumMoreVisited:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Cuál dirías que es el museo más visitado de Cataluña?" # Museo FC Barcelona.
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_MuseumMoreVisited_question:
        
        pt "Creo que el Prado está en Madrid..."
        
        "El Museo de Cera.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "No."
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Aunque tampoco sea santo de mi devoción,"
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "lo que me parece triste es que el más visitado sea precisamente el del Fútbol Club Barcelona."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Para que te hagas una idea del nivel cultural general de este país."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "..."
                  
            jump  afternoon04_LikeModernArt
        
        "El Museo de Dalí.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "Aunque sigo creyendo que {a=https://es.wikipedia.org/wiki/Salvador_Dalí}Dalí{/a} fue un payaso vendido a los medios durante la mayor parte de su vida,"
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 02
            show m_exp_piris right02
            #show m_pupils right02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "reconozco que su arte tiene algo especial que no he sabido ver en casi ningún otro artista,"
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "y que, sin duda,"

            extend " tenía un talento especial."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Lástima que se echara a perder con {a=https://es.wikipedia.org/wiki/Gala_Dalí}Gala{/a}..."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Pero no,"

            extend " no es el museo más visitado de Cataluña,"

            gm "en realidad lo es el {a=https://es.wikipedia.org/wiki/Museo_del_Fútbol_Club_Barcelona}museo del Fútbol Club Barcelona{/a}."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            if afternoon04_waxbar_fcbcn_Cond == True:
            
                gm "Como te dije,"

                extend " pan y circo."

            else:

                gm "{a=https://es.wikipedia.org/wiki/Panem_et_circenses}Pan y circo{/a}."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "..."
            
            jump  afternoon04_LikeModernArt
            
        "El Museo del Fútbol Club Barcelona.":
            
            call p_Help
            $ Martq += 1
            $ Cartq += 1
                
            $pl.ch_pts("mp",+1)
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "Hmm..."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Por desgracia,"

            extend " así es."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "No me parece que un lugar que rememora la historia,"

            p "aunque sea sobre un club deportivo,"

            extend " sea una desgracia."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
               
            gm "Lo es,"

            extend " cuando te fijas en el desinterés que produce sobre otras cosas más importantes,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "el simple hecho de que sea \"el museo\" más visitado,"

            gm "cuando no se expone ninguna obra cultural o artística..."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Me produce náuseas,"

            extend " y un asco profundo,"

            gm "en esta putrefacta sociedad afectada por la idiocracia."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Me imagino que esta chica debe de ser la alegría en las fiestas..."
            
            jump  afternoon04_LikeModernArt
            
        "El Born Centre Cultural.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "Es un espacio polivalente de acceso al público con una extensa programación"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "que tiene el objetivo de invitar a la reflexión sobre el pasado,"

            gm "presente,"

            extend " y futuro de Barcelona;"

            gm "y de hecho, de Cataluña en general."
            
            show m_exp_mouth sad_Talkingx001
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Pero no,"

            extend " no es el museo más visitado de Cataluña,"

            gm "en realidad lo es el {a=https://es.wikipedia.org/wiki/Museo_del_Fútbol_Club_Barcelona}museo del Fútbol Club Barcelona{/a}."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Como te dije,"

            extend " pan y circo."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "No sé si es que odia el fútbol en general,"

            pt "o sencillamente es una amante incondicional de la cultura y el arte..."
            
            jump  afternoon04_LikeModernArt

label afternoon04_LikeModernArt:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    gm "¿Te gusta el arte contemporáneo?"
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Especialmente el de mediados del siglo XX."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    menu afternoon04_LikeModernArt_question:
        
        pt "Llamas arte moderno a algo que ya tiene más de medio siglo..."
        
        "Aunque lo conozco, prefiero el arte figurativo clásico...":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "¿Sabes cuál era el propósito principal de los artistas en la antigüedad?"
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Crear obras de arte..."

            p "Como siempre ha sido,"

            extend " ¿no?"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Te crees que existían centenares de museos como hoy en día,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "donde el público puede acceder para contemplar esas obras,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "en una sociedad que se moría de peste y hambre por las calles?"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Donde los niños eran explotados,"

            gm "donde no existía la escuela,"

            gm "donde la gente no sabía ni leer,"

            extend " ni escribir."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Quienes daban de comer a los artistas"

            gm "eran los {a=https://es.wikipedia.org/wiki/Mecenazgo}mecenas{/a},"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "que básicamente solían ser gente noble o adinerada que pedía que se le hicieran retratos."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Porque en esa época no existía la fotografía."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "¡Pero hay obras de arte que van más allá del simple retrato!"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Cierto."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Porque en esa época también existía gente a la que le sobraba el dinero de forma escandalosa."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Pero eso no quita que la mayor parte de las obras que se hicieron antes de la época de la fotografía,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "tenían el propósito de satisfacer los deseos y la demanda de un solo cliente."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo Davinci{/a} trabajó para los {a=https://es.wikipedia.org/wiki/Médici}Médici de Italia{/a}."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Miguel_Ángel}Miguel Ángel{/a} trabajó para el mismísimo {a=https://es.wikipedia.org/wiki/Ciudad_del_Vaticano}Vaticano{/a}."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Claro que ambos tuvieron su \"cierta\" libertad artística debido a su gran talento,"

            extend " pero aun así,"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "tuvieron que reinventarse para esconder mensajes ocultos en sus obras."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Porque, en realidad,"

            gm "estas,"

            extend " respondían a simples \"encargos\"."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No representaban lo que realmente querían expresar,"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "su arte estaba sujeto a las órdenes de un cliente adinerado y exigente."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¡¿Acaso hoy en día los artistas no ganan dinero con sus obras como antaño?!"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "La diferencia es que, hoy día,"

            gm "el cliente va a ver la obra que el artista ha hecho,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "no exige al artista qué obra quiere que haga."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            p "..."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
               
            p "Son mercados distintos."

            p "Eso no menosprecia en absoluto el valor de una obra."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Esa es tu opinión."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve
            
            pt "Resume más de tres mil años de historia del arte en un solo argumento y se queda tan ancha..."
                  
            jump  afternoon04_Q_LikeClassicArt_after
        
        "Creo que el arte moderno es un timo para sacarles el dinero a los necios.":
            
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "..."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Explícate."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Los artistas que viven y trabajan en la actualidad,"
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿serán también reconocidos como grandes maestros dentro de trescientos años?"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¿Crees que {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Picasso{/a} será olvidado?"
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Estoy hablando de los artistas \"pintores\" posteriores a los noventa."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Después de {a=https://es.wikipedia.org/wiki/Marcel_Duchamp}Duchamp{/a}, quedó poco más por hacer."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
               
            p "Los artistas comenzaron como meros artesanos y fabricantes,"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "para pasar a depender de un mecenas,"

            p "y, finalmente,"

            extend " a ser vistos como creadores con absoluta autonomía."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Esta libertad artística termina sin embargo en el momento en el que el artista procede a vender su obra."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
            
            p "Se desarrolla todo un \"circo\" en torno al producto,"
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
               
            p "el creador y la galería,"

            p "que servirá de intermediaria entre artista y observador."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Al amante del arte ya no se le muestra la calidad ni la pasión,"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            p "sino que se pretende dejar huella en todo aquel que contemple la obra a través del \"morbo\","
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "lo \"chocante\","

            extend " e incluso lo \"sádico\"."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Te crees que el arte es solo expresión estética gratuita?"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¡¿Crees que Goya pintaba jardines de flores y arcoíris?!"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            menu afternoon04_LikeModernArt_Fraud01_question:
                
                pt "Si las obras de arte deben ser forzosamente agradables a la vista?"
                
                "Una obra que no entra bien por los ojos no creo que deba considerarse \"obra de arte\".":
                    
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "¿Dirías que una mesa hecha artesanalmente al estilo renacentista es una obra de arte?"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    p "Si está bien hecha,"

                    extend " ¿por qué no?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "A pesar de ser un trabajo con la ayuda de poca tecnología,"

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows serious
                    with dissolve
                    
                    gm "no es arte porque se producen piezas en forma serializada,"

                    extend " casi idénticas."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    p "Hay obras de arte que también son \"series\"."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Así es,"

                    gm "están enumeradas,"

                    extend " y solo existen en una cantidad muy limitada."
                    
                    jump afternoon04_Q_LikeClassicArt_after
    
                "No, pero sí lo es cuando dicha obra se aleja de la primera plana o de la opinión pública.":
                    
                    call p_Help
                    $ pl.ch_pts("mp",+1)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Porque no sale en los telediarios, ¿deja de ser arte?"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    menu afternoon04_LikeModernArt_Fraud02_question:
                        
                        pt "Vaya tostón pseudofilosófico me está pegando la tía..."
                        
                        "Si un cuadro no se entiende, tiene el mismo valor que un garabato, o sea, ninguno.":
                        
                            call p_Help
                            $ pl.ch_pts("mp",-1)

                            show m_exp_mouth sad_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "Vamos,"

                            gm "que, como la mayoría de primates,"

                            extend " cuando no entiendes algo,"

                            show m_exp_mouth sad_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "coges una pataleta,"

                            extend " y lo insultas sin ningún tipo de interés ni respeto."

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            p "Yo no he dicho eso."

                            show m_exp_mouth sad_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris right04
                            #show m_pupils right04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Está implícito en lo que opinas."
                            
                            jump afternoon04_Q_AfterInterrogation
                    
                        "El principal problema del arte en la actualidad es que la gran mayoría del público no lo entiende.":
                            
                            call p_Help
                            $ pl.ch_pts("mp",+1)

                            show m_exp_mouth serious_Silentx01
                            show m_exp_eyes 02
                            show m_exp_piris front02
                            #show m_pupils front02a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                    
                            gm "..."

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 03
                            show m_exp_piris left03
                            #show m_pupils left03a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            p "Esto hace que muchas veces el espectador caiga en la idea errónea de que una obra se le escapa,"

                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 03
                            show m_exp_piris left03
                            #show m_pupils left03a
                            show m_exp_eyebrows serious
                            with dissolve
                               
                            p "porque no alcanza a entender su nivel de profundidad."

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 03
                            show m_exp_piris left03
                            #show m_pupils left03a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            p "Como si uno fuera un ignorante por no saber ver el universo en un lienzo en blanco."

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris left04
                            #show m_pupils left04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "..."

                            show m_exp_mouth sad_Talkingx10
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx04
                            with dissolve
                            
                            gm "¿Entonces una obra deja de ser artística si depende de su explicación?"

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            menu afternoon04_LikeModernArt_Fraud03_question:
                                
                                pt "Parece que la chica se toma en serio el asunto este..."
                                
                                "Sí, desde luego.":
                                    
                                    call p_Help
                                    $ pl.ch_pts("mp",-1)

                                    show m_exp_mouth sad_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    gm "Supongo que eres de los que prefiere ir a ver películas de {a=https://es.wikipedia.org/wiki/Michael_Bay}{i}Michael Bay{/i}{/a}"

                                    extend " o {a=https://es.wikipedia.org/wiki/The_Fast_and_the_Furious_(películas)}{i}Fast & Furious{/i}{/a},"
                                    
                                    show m_exp_mouth happy_Talkingx09
                                    show m_exp_eyes 02
                                    show m_exp_piris front02
                                    #show m_pupils front02a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve

                                    gm "o quizás prefieras ir a ver alguna película de {a=https://es.wikipedia.org/wiki/Sesame_Street}Barrio Sésamo{/a}"

                                    extend " o {a=https://es.wikipedia.org/wiki/Winnie_the_Pooh}Winnie-the-Pooh{/a},"
                                        
                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows angryx01
                                    with dissolve

                                    gm "me imagino que estarán más adaptadas a tu comprensión..."

                                    show m_exp_mouth sad_Silentx03
                                    show m_exp_eyes 02
                                    show m_exp_piris front02
                                    #show m_pupils front02a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    p "¿No puedo tener una opinión?"

                                    show m_exp_mouth sad_Talkingx003
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "Claro,"

                                    extend " claro que puedes..."

                                    show m_exp_mouth happy_Silentx05
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    pt "Su sarcasmo no es precisamente muy sutil..."
                                    
                                    jump afternoon04_Q_AfterInterrogation
                                
                                "No necesariamente.":
                                    
                                    call p_Help
                                    $ pl.ch_pts("mp",+1)

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                            
                                    p "Puede serlo."

                                    p "No hay que olvidar que lo que hace que el arte sea lo que es;"

                                    show m_exp_mouth sad_Silentx03
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    p "al final siempre es la carga emocional que le transmite a aquel que lo contempla."

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 03
                                    show m_exp_piris right03
                                    #show m_pupils right03a
                                    show m_exp_eyebrows normal
                                    with dissolve
                                    
                                    p "Del mismo modo que nos emocionamos al ver la {a=https://es.wikipedia.org/wiki/Capilla_Sixtina}Capilla Sixtina{/a},"

                                    extend " la {a=https://es.wikipedia.org/wiki/La_Gioconda}Mona Lisa{/a},"
                                    

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 02
                                    show m_exp_piris right02
                                    #show m_pupils right02a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve

                                    p "o una obra de {a=https://es.wikipedia.org/wiki/Jackson_Pollock}Pollock{/a},"

                                    extend " abstracta"

                                    extend " y caótica;"

                                    p "la cual puede provocar un efecto igual o incluso más intenso."
                                    

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 01
                                    show m_exp_piris right01
                                    #show m_pupils right01a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve

                                    p "Pero la cuestión es que, al necesitar una explicación previa,"

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 01
                                    show m_exp_piris front01
                                    #show m_pupils front01a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                       
                                    p "deja de ser accesible a cualquiera que contemple esa obra."

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 01
                                    show m_exp_piris right01
                                    #show m_pupils right01a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    gm "..."

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 02
                                    show m_exp_piris left02
                                    #show m_pupils left02a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    p "Lo cierto es que no existen respuestas correctas para estas preguntas."

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 03
                                    show m_exp_piris left03
                                    #show m_pupils left03a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    p "El tiempo acabará por recoger y conservar lo valioso;"

                                    extend " y desechar lo banal,"

                                    show m_exp_mouth sad_Silentx02
                                    show m_exp_eyes 04
                                    show m_exp_piris left04
                                    #show m_pupils left04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    p "con mayor o menor acierto..."

                                    show m_exp_mouth sad_Silentx03
                                    show m_exp_eyes 04
                                    show m_exp_piris left04
                                    #show m_pupils left04a
                                    show m_exp_eyebrows serious
                                    with dissolve
                                    
                                    p "tal y como ha ocurrido siempre en la historia del arte."

                                    show m_exp_mouth sad_Silentx04
                                    show m_exp_eyes 08
                                    show m_exp_piris front06
                                    #show m_pupils left06a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "Hmmm..."

                                    show m_exp_mouth sad_Talkingx003
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    gm "Entonces,"

                                    gm "¿te consideras un experto en arte moderno?"

                                    extend " ¿o en arte clásico?"

                                    show m_exp_mouth sad_Silentx02
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    menu afternoon04_LikeModernArt_Fraud04_question:
                                        
                                        "Conozco mejor el arte clásico.":
                                            
                                            call p_Help

                                            show m_exp_mouth sad_Talkingx05
                                            show m_exp_eyes 04
                                            show m_exp_piris front04
                                            #show m_pupils front04a
                                            show m_exp_eyebrows serious
                                            with dissolve
                                                
                                            gm "Ah,"

                                            show m_exp_mouth happy_Talkingx03
                                            show m_exp_eyes 04
                                            show m_exp_piris front04
                                            #show m_pupils front04a
                                            show m_exp_eyebrows surprisex001
                                            with dissolve

                                            gm "¿sí...?"
                                            
                                            jump afternoon04_Q_LikeClassicArt_after
                                        
                                        "Conozco mejor el arte moderno.":
                                            
                                            call p_Help

                                            show m_exp_mouth happy_Talkingx03
                                            show m_exp_eyes 04
                                            show m_exp_piris front04
                                            #show m_pupils front04a
                                            show m_exp_eyebrows angryx01
                                            with dissolve
                                                
                                            gm "Ya veo..."
                                         
                                            jump afternoon04_Q_LikeModernArt_after
                                            
                                        "No me interesa ninguno de los dos.":
                                            
                                            call p_Help
                                                
                                            jump afternoon04_Q_AfterInterrogationFail
            
        "Soy un experto en arte moderno.":
            
            call p_Help

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
                
            gm "Ah,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¿Sí...?"
            
            jump  afternoon04_Q_LikeModernArt_after
            
        "Lo conozco, pero no me entusiasma.":
            
            call p_Help

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "Ya veo..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Entonces,"

            gm "¿te consideras un experto en arte moderno?"

            extend " ¿o en arte clásico?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            jump afternoon04_LikeModernArt_Fraud04_question
            
            #jump  afternoon04_Q_LikeModernArt_after
    
    #arte moderno
    
label afternoon04_Q_LikeModernArt_after:

    $ afternoon04_Q_ModernArt = True

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "¿De verdad conoces el arte moderno?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "Claro..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    n "De su bolsillo saca un {i}smartphone{/i}, y haciendo como si no existieras, empieza a manejarlo."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "Euhmm..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Dime..."

    play music "audio/music/alcaknight/memories_of_the_east.ogg" fadein 3.0 fadeout 3.0
    
    scene black
    show afternoon04_paint m_pollock_number01:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    gm "¿Quién es el artista de este cuadro?" #Pollock Number 01
    
    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_blush 00:
        #m_face_atright_position
    #show m_exp_mouth serious_Silentx01:
        #m_face_atright_position
    #show m_exp_eyes 04:
        #m_face_atright_position
    #show m_exp_piris front04:
        #m_face_atright_position
    ##show m_pupils front04a:
        ##m_face_atright_position
    #show m_exp_eyebrows surprisex001:
        #m_face_atright_position
    #with dissolve


    
#########################################################
    
    if config.version <= "00.06.06": #Introduction to date with Mystery Woman.
        
        call endupdatescript
    
#######################################################
    
    menu afternoon04_Q_Pollock_question:
        
        pt "Esto parece como si un montón de potes de pintura hubiesen estornudado..."
        
        "Wassily Kandinsky.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "No."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Vasili_Kandinski}Kandinski{/a} fue un precursor de la {a=https://es.wikipedia.org/wiki/Abstracción_lírica}abstracción lírica{/a} y el {a=https://es.wikipedia.org/wiki/Expresionismo}expresionismo{/a} en la pintura."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Pero fue algo anterior al pintor de esta obra."
                
            #NOT FINISHED TEXT
                
            jump afternoon04_Q_Pollock_after
            
        "Vincent Van Gogh.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "No."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Vincent_van_Gogh}Van Gogh{/a} fue un exponente del {a=https://es.wikipedia.org/wiki/Posimpresionismo}postimpresionismo{/a} en el siglo XIX."
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Solo te has equivocado por un siglo..."
            
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "Su sarcasmo no es nada sutil..."
                
            #NOT FINISHED TEXT
                
            jump afternoon04_Q_Pollock_after
            
        "Jackson Pollock.": #Correct
            
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Martq += 1 #If the answer is correct.
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
                
            gm "Hmm..."
                
            jump afternoon04_Q_Pollock_after
            
        "Edward Munch.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "No."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Edvard_Munch}Munch{/a} evocaba sentimientos,"

            extend " tragedias humanas,"

            extend " y fue precursor del {a=https://es.wikipedia.org/wiki/Expresionismo}expresionismo{/a}."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero mayoritariamente sus obras fueron figurativas,"

            extend " como {a=https://es.wikipedia.org/wiki/El_grito}El Grito{/a}."
                
            #NOT FINISHED TEXT
                
            jump afternoon04_Q_Pollock_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_Pollock_after:

    scene afternoon04_bg macba_outside


    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex01:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve


    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_blush 00:
        #m_face_atright_position
    #show m_exp_mouth sad_Talkingx03:
        #m_face_atright_position
    #show m_exp_eyes 04:
        #m_face_atright_position
    #show m_exp_piris front04:
        #m_face_atright_position
    ##show m_pupils front04a:
        ##m_face_atright_position
    #show m_exp_eyebrows surprisex001:
        #m_face_atright_position
    #with dissolve
    
    gm "Sigamos..."
    
    scene black
    show afternoon04_paint m_picasso_guernica:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    gm "¿Qué representa este cuadro?" #El caos que hubo después del bombardeo de Guernica (Picasso)
    
    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    #show m_body 01_relax:
        #m_body_atright_position
    #show m_exp_blush 00:
        #m_face_atright_position
    #show m_exp_mouth serious_Silentx01:
        #m_face_atright_position
    #show m_exp_eyes 04:
        #m_face_atright_position
    #show m_exp_piris front04:
        #m_face_atright_position
    ##show m_pupils front04a:
        ##m_face_atright_position
    #show m_exp_eyebrows surprisex001:
        #m_face_atright_position
    #with dissolve
    
    menu afternoon04_Q_Guernica_question:
        
        pt "Desde luego este cuadro parece un caos."
        
        "Una pelea en un bar nocturno.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "Claro..."

            gm "porque en un bar es muy normal que haya caballos y vacas."
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Por no mencionar que suele haber incendios,"

            gm "y madres llorando por sus hijos muertos."
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Quizás..."

            p "es por una alegoría dramatizada..."
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No intentes estropearlo más,"

            extend " [protname]..."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Quedas mejor diciendo simplemente:"

            extend " {i}no tengo ni la más \"puñetera\" idea{/i}."
                
            jump afternoon04_Q_Guernica_after
        
        "Una demostración grotesca de una orgía alocada con incesto, pedofilia y zoofilia.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "..."
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Lo tuyo sí que es grotesco..."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¡Ey!"
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "No hace falta insultar."
            
            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Aún me estoy quedando corta..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "Será hija de..."
                
            jump afternoon04_Q_Guernica_after
        
        "La miseria y el sufrimiento que hubo después del bombardeo de Guernica.": #Correct
            
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Martq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "Hmm..."
            
            #NOT FINISHED TEXT
                
            jump afternoon04_Q_Guernica_after
            
        "No lo sé...":
        
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
                
            gm "No conocer uno de los iconos del siglo XX;"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "aprecies o no su arte..."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Es simplemente muy triste."
            
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            show m_exp_mouth happy_Silentx05
            with dissolve
            
            pt "¿Por qué coño sonríe?"
                
            jump afternoon04_Q_Guernica_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_Guernica_after:
    
    scene black
    with fade
    
    gm "A ver este otro..."
    
    scene black
    show afternoon04_paint m_dali_persistentofmemory:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    gm "¿Cómo se llama el tipo de arte de este cuadro?" #Arte onírico (Dalí)
    
    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    menu afternoon04_Q_OniricArt_question:
        
        pt "Qué tipo de drogas se debió tomar para hacer semejante cuadro..."
        
        "Fumada mental.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "Si te vas a tomar a coña mis preguntas debido a tu ignorancia y petulancia,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "será mejor que dejes de hacerme perder el tiempo."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿Queda claro?"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¿Es que acaso no te parece esto de aquí una fumada de mil narices?"
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¿Qué puñetas representa esto?"
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¿Acaso sabes cómo se llama esta obra pictórica?"
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Listillo..."
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            menu afternoon04_Q_OniricArt_Name01_question:
                
                pt "¿Desvaríos de un drogadicto talentoso?"
                
                "Relojes que se funden.":
                    call p_Help
                    $ pl.ch_pts("mp",-2)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Tu mente sí que se funde..."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    p "¡No hace falta insultar!"

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve
                    
                    gm "No lo haría si no dijeras gilipolleces."

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    p "..."
                    
                    #NOT FINISHED
                        
                    jump afternoon04_Q_OniricArt_after
                    
                "La memoria del tiempo.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows sadx01
                    with dissolve
                    
                    gm "Casi..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "pero no."

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows normal
                    with dissolve
                    
                    gm "Se llama {a=https://es.wikipedia.org/wiki/La_persistencia_de_la_memoria}la persistencia de la memoria{/a}."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    p "Bueno,"

                    extend " es casi lo mismo..."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "..."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    gm "No es lo mismo decir:"

                    extend " \"se avecina una tormenta\","

                    gm "que decir:"

                    extend " \"se atormenta una vecina\"."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "¿Verdad?"

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "Vaya comparación me da la tía..."
                        
                    jump afternoon04_Q_OniricArt_after
                
                "La persistencia de la memoria.":
                    call p_Help
                    $ pl.ch_pts("mp",+2)
                    $ Martq += 1 #If the answer is correct.
                    
                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    #show m_pupils front02a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                        
                    gm "..."
                    
                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx04
                    with dissolve
                    
                    p "Que algo me parezca una fumada,"

                    p "no significa que me guste,"

                    extend " o me disguste;"

                    p "simplemente lo estoy definiendo."
                    
                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx04
                    with dissolve
                    
                    gm "..."
                    
                    menu afternoon04_Q_OniricArt_Name02_question:
                        
                        "Y por cierto, el tipo de arte se llama {a=https://es.wikipedia.org/wiki/Simbolismo}Simbolismo{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)
                            
                            jump afternoon04_Q_OniricArt_Symbolism
                        
                        "Y por cierto, el tipo de arte se llama {a=https://es.wikipedia.org/wiki/Surrealismo}Surrealismo{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",+1)
                            $ Martq += 1 #If the answer is correct.
                            
                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "..."
                            
                            jump afternoon04_Q_OniricArt_Name03_question
                            
                        "Y por cierto, el tipo de arte se llama {a=https://es.wikipedia.org/wiki/Expresionismo}Expresionismo{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)
                            
                            jump afternoon04_Q_OniricArt_Expressionism
                            
                        "Y por cierto, el tipo de arte se llama {a=https://es.wikipedia.org/wiki/Realismo_artístico}Realismo{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)
                            
                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "¿Realismo?"
                            
                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            p "..."
                            
                            show m_exp_mouth happy_Talkingx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex02
                            with dissolve
                            
                            gm "¿A ti te parece esto un paisaje habitual en cualquier parte del mundo?"
                            
                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            p "Eumm..."
                            
                            show m_exp_mouth sad_Talkingx003
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            #show m_pupils front03a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            gm "¡¿Cuándo has visto que los relojes se fundan de esta manera?!"
                            
                            show m_exp_mouth happy_Silentx08
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            #show m_pupils front03a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            p "..."
                            
                            show m_exp_mouth happy_Talkingx09
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex02
                            with dissolve
                            
                            gm "Con lo bien que ibas y la cagas..."
                            
                            show m_exp_mouth happy_Silentx08
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex02
                            with dissolve
                            
                            pt "Será zorra..."

                            pt "¡¿Por qué coño sonríe?!"
                            
                            #NOT FINISHED
                            
                            jump afternoon04_Q_OniricArt_after
                            
                        "<Callarte y no cagarla>":
                            call p_Help
                            $ pl.ch_pts("mp",-1)
                            
                            show m_exp_mouth sad_Silentx02
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows serious
                            with dissolve
                            
                            gm "..."
                            
                            jump afternoon04_Q_OniricArt_after
                            
                    menu afternoon04_Q_OniricArt_Name03_question:
                        
                        "Y esta obra está realizada por {a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo da Vinci{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-3)
                            
                            show m_exp_mouth sad_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "Leonardo de la Venecia {a=https://es.wikipedia.org/wiki/Renacimiento}renacentista{/a} de los siglos XV-XVI..."
                            
                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Este talentoso artista hace este cuadro en esa época,"

                            gm "y por mucho que tuviera el beneplácito de los {a=https://es.wikipedia.org/wiki/Médici}Médici{/a},"
                            
                            show m_exp_mouth happy_Talkingx09
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            #show m_pupils front03a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "lo queman en la hoguera,"

                            extend " o le cortan la cabeza en público,"

                            gm "por alegoría a lo fúnebre y demoníaco."
                            
                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            pt "Creo que no lo he acertado entonces..."
                            
                            jump afternoon04_Q_OniricArt_after
                            
                        "Y esta obra está realizada por {a=https://es.wikipedia.org/wiki/Joan_Miró}Joan Miró{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)

                            show m_exp_mouth happy_Talkingx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Pero..."

                            gm "¿Tú has visto alguna vez una obra de Joan Miró?"

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            menu afternoon04_Q_OniricArt_Name03_JoanMiro01_question:
                            
                                "Sí...":
                                    call p_Help
                                    $ pl.ch_pts("mp",-1)
                                    
                                    jump afternoon04_Q_OniricArt_Name03_JoanMiro01
                                
                                "No...":
                                    call p_Help
                                        
                                    jump afternoon04_Q_OniricArt_Name03_JoanMiro01
                                    
                            label afternoon04_Q_OniricArt_Name03_JoanMiro01:

                                show m_exp_mouth happy_Talkingx05
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows surprisex02
                                with dissolve
                                
                                gm "Sabías que nació en Barcelona,"

                                extend " ¿verdad?"

                                show m_exp_mouth happy_Silentx05
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows suspiciousx02
                                with dissolve
                                        
                                menu afternoon04_Q_OniricArt_Name03_JoanMiro02_question:
                                
                                    "Sí.":
                                        call p_Help
                                            
                                        jump afternoon04_Q_OniricArt_Name03_JoanMiro02
                                    
                                    "No.":
                                        call p_Help
                                        $ pl.ch_pts("mp",-1)
                                        
                                        jump afternoon04_Q_OniricArt_Name03_JoanMiro02
                                        
                            label afternoon04_Q_OniricArt_Name03_JoanMiro02:

                                show m_exp_mouth sad_Talkingx10
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows angryx04
                                with dissolve
                            
                                gm "¡¿Qué trazo de este cuadro te recuerda remotamente al estilo gráfico de Miró?!"

                                show m_exp_mouth sad_Silentx04
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows angryx01
                                with dissolve
                                
                                p "..."

                                show m_exp_mouth sad_Talkingx10
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows angryx01
                                with dissolve
                                
                                gm "Si no tienes ni puta idea de quien es Miró,"

                                extend " ni de quién pintó este cuadro,"

                                show m_exp_mouth happy_Talkingx09
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows suspiciousx02
                                with dissolve
                                
                                gm "es mejor decir: \"No lo sé\";"

                                extend " antes de decir semejante estupidez."

                                show m_exp_mouth happy_Silentx08
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows angryx01
                                with dissolve
                                
                                pt "Joder,"

                                extend " cómo se lo toma la chica..."
                                
                                # NOT FINISHED
                                
                                jump afternoon04_Q_OniricArt_after
                       
                        "y esta obra está realizada por {a=https://es.wikipedia.org/wiki/Salvador_Dalí}Salvador Dalí{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",+1)
                            $ Martq += 1 #If the answer is correct.

                            show m_exp_mouth sad_Silentx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx04
                            with dissolve
                            
                            gm "Hmm..."

                            jump afternoon04_Q_OniricArt_Name04
                            
                        "Y esta obra está realizada por {a=https://es.wikipedia.org/wiki/Caravaggio}Caravaggio{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)

                            show m_exp_mouth sad_Talkingx007
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            #show m_pupils front03a
                            show m_exp_eyebrows serious
                            with dissolve
                            
                            gm "El primer gran exponente de la {a=https://es.wikipedia.org/wiki/Pintura_del_Barroco}pintura del Barroco{/a},"

                            show m_exp_mouth happy_Talkingx09
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "¿pintó un cuadro modernista del siglo XX...?"

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 08
                            show m_exp_piris front06
                            #show m_pupils front06a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            p "Eumm..."

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Sabes cuándo se inició el arte Barroco,"

                            extend " ¿verdad?"

                            show m_exp_mouth happy_Silentx02
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows normal
                            with dissolve
                            
                            menu afternoon04_Q_OniricArt_Name03_Caravaggio01:
                                
                                pt "Si mal no recuerdo, empezó alrededor del año 1600..."
                                
                                "En el siglo XIV.":
                                    call p_Help
                                    $ pl.ch_pts("mp",-3)

                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                    
                                    gm "No,"

                                    extend " solo te has equivocado en doscientos años."

                                    show m_exp_mouth happy_Silentx08
                                    show m_exp_eyes 08
                                    show m_exp_piris front06
                                    #show m_pupils front06a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    p "..."
                                    
                                    jump afternoon04_Q_OniricArt_after
                                
                                "En el siglo XV.":
                                    call p_Help
                                    $ pl.ch_pts("mp",-2)

                                    show m_exp_mouth sad_Talkingx003
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    gm "No,"

                                    extend " te equivocas de cien años."

                                    show m_exp_mouth sad_Silentx04
                                    show m_exp_eyes 02
                                    show m_exp_piris front02
                                    #show m_pupils front02a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                    
                                    p "Bueno,"

                                    extend " casi lo acierto..."

                                    show m_exp_mouth happy_Silentx05
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    gm "..."

                                    show m_exp_mouth happy_Silentx08
                                    show m_exp_eyes 08
                                    show m_exp_piris front06
                                    #show m_pupils front06a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    p "..."
                                    
                                    jump afternoon04_Q_OniricArt_after
                                
                                "En el siglo XVI.":
                                    call p_Help
                                    $ pl.ch_pts("mp",+1)
                                    
                                    # NOT FINISHED

                                    show m_exp_mouth sad_Silentx06
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "Hmm..."

                                    show m_exp_mouth sad_Talkingx003
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    gm "Por lo menos no eres un completo inútil después de todo..."

                                    show m_exp_mouth sad_Silentx06
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows angryx04
                                    with dissolve
                                    
                                    pt "Pero,"

                                    extend " ¡¿De qué cojones va esta tía?!"

                                    jump afternoon04_Q_OniricArt_after
                                
                                "En el siglo XVII.":
                                    call p_Help
                                    $ pl.ch_pts("mp",-1)
                                    
                                    # NOT FINISHED

                                    show m_exp_mouth sad_Talkingx003
                                    show m_exp_eyes 02
                                    show m_exp_piris right02
                                    #show m_pupils right02a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                    
                                    gm "Uno podría pensar que, al florecer alrededor del 1600,"

                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris right03
                                    #show m_pupils right03a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "ocurrió en el XVII,"

                                    extend " pero en realidad empezó más bien unos años antes,"

                                    show m_exp_mouth happy_Talkingx03
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                    
                                    gm "y eso pertenece al siglo XVI."

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 01
                                    show m_exp_piris front01
                                    #show m_pupils front01a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve
                                    
                                    p "No he fallado de tanto entonces..."

                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    gm "Solo te has equivocado de siglo..."

                                    show m_exp_mouth happy_Silentx02
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows normal
                                    with dissolve
                                    
                                    p "..."

                                    show m_exp_mouth happy_Talkingx09
                                    show m_exp_eyes 03
                                    show m_exp_piris right03
                                    #show m_pupils right03a
                                    show m_exp_eyebrows normal
                                    with dissolve
                                    
                                    gm "Es como si dijeras que la \"Segunda Guerra Mundial\" ocurrió antes de la Primera..."

                                    show m_exp_mouth happy_Talkingx10
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "Totalmente lógico para tu mente primitiva..."

                                    show m_exp_mouth happy_Silentx08
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    pt "Pero,"

                                    extend " ¡¿de qué cojones va esta tía?!"
                                    
                                    jump afternoon04_Q_OniricArt_after
                                
                                "Paso de responder a estas estúpidas preguntas...": #Go to Hell
                                    
                                    call p_Help
                                        
                                    jump afternoon04_Q_AfterInterrogationFail
                            
                        "<Callarte y no cagarla>":
                            call p_Help
                            $ pl.ch_pts("mp",-1)

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 08
                            show m_exp_piris front06
                            #show m_pupils front06a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "..."

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Me lo imaginaba..."
                            
                            jump afternoon04_Q_OniricArt_after
                            
                            
                    label afternoon04_Q_OniricArt_Name04:

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        #show m_pupils right04a
                        show m_exp_eyebrows angryx04
                        with dissolve
                        
                        p "¿Alguna pregunta más?"

                        show m_exp_mouth sad_Silentx04
                        show m_exp_eyes 08
                        show m_exp_piris front06
                        #show m_pupils right06a
                        show m_exp_eyebrows angryx01
                        with dissolve
                        
                        gm "..."
                        
                        #NOT FINISHED
                    
                        jump afternoon04_Q_OniricArt_after
                    
                "Tempus Fugit.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows surprisex02
                    with dissolve
                    
                    gm "El tiempo se escapa como una nube,"

                    gm "como una ola,"

                    extend " como una sombra."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "{a=https://es.wikipedia.org/wiki/Tempus_fugit}El tiempo huye{/a}."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Buen intento,"

                    extend " pero no..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "El título es {a=https://es.wikipedia.org/wiki/La_persistencia_de_la_memoria}La Persistencia de la Memoria{/a}."
                        
                    #NOT FINISHED
                        
                    jump afternoon04_Q_OniricArt_after
                    
                "Paso de responder a estas estúpidas preguntas...": #Go to Hell
                    
                    call p_Help
                        
                    jump afternoon04_Q_AfterInterrogationFail
        
        "Simbolismo.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            label afternoon04_Q_OniricArt_Symbolism:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows angryx01
                with dissolve
            
                gm "Los simbolistas creían que el arte debía apuntar a capturar las verdades más absolutas,"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "las cuales solo podían ser obtenidas por métodos indirectos y ambiguos."

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 02
                show m_exp_piris right02
                #show m_pupils right02a
                show m_exp_eyebrows angryx01
                with dissolve
                
                gm "El {a=https://es.wikipedia.org/wiki/Simbolismo}Simbolismo{/a} busca vestir la idea de una forma sensible,"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 03
                show m_exp_piris right03
                #show m_pupils right03a
                show m_exp_eyebrows surprisex001
                with dissolve
                    
                gm "posee intenciones metafísicas,"

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "además, intenta utilizar el lenguaje literario como instrumento cognoscitivo,"

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "por lo cual se encuentra impregnado de misterio y misticismo."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve
                    
                gm "Fue considerado en su tiempo por algunos como el lado oscuro del {a=https://es.wikipedia.org/wiki/Romanticismo}Romanticismo{/a}."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                p "¿Pero lo he acertado o no?"

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "No."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve
                
                pt "Entonces, ¡¿por qué se enrolla tanto?!"
                    
                jump afternoon04_Q_OniricArt_after
        
        "Surrealismo.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Martq += 3 #If the answer is correct. This answer Surrealism, Persistent of time and Salvador Dalí Questions of "Fumada mental".

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Hmm..."
                
            jump afternoon04_Q_OniricArt_after
            
        "Expresionismo.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            label afternoon04_Q_OniricArt_Expressionism:

                show m_exp_mouth sad_Talkingx001
                show m_exp_eyes 03
                show m_exp_piris right03
                #show m_pupils right03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "El {a=https://es.wikipedia.org/wiki/Expresionismo}Expresionismo{/a} suele ser entendido como la deformación de la realidad,"

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows serious
                with dissolve
                    
                gm "para expresar de forma más subjetiva la naturaleza y el ser humano,"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "dando primacía a la expresión de los sentimientos sobre la descripción objetiva de la realidad."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris left02
                #show m_pupils left02a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "Los expresionistas defendían un arte más personal e intuitivo,"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "donde predominase la visión interior del artista,"

                extend " la \"expresión\","

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris front02
                #show m_pupils front02a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "frente a la plasmación de la realidad,"

                extend " la \"impresión\"."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows serious
                with dissolve
                
                p "..."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                #show m_pupils front02a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                p "¿Entonces lo he acertado?"

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 02
                show m_exp_piris left02
                #show m_pupils left02a
                show m_exp_eyebrows angryx01
                with dissolve
                
                gm "¿A ti te parece este cuadro una expresión subjetiva de la naturaleza y el ser humano?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris left04
                #show m_pupils left04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                p "Eumm..."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                pt "Hombre,"

                extend " no me parece una representación muy objetiva de la realidad..."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "No, [protname],"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "este cuadro no es expresionista..."

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve

                p "..."
                    
                jump afternoon04_Q_OniricArt_after
        
        "Realismo.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "El {a=https://es.wikipedia.org/wiki/Realismo_artístico}Realismo{/a} es una postura que plasma la realidad o naturaleza de una manera imitativa."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "¿A ti te parece que este cuadro esté representando fielmente la realidad?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " no..."

            p "pero sin duda está hecho con mucho esmero,"

            extend " y parece real..."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Lo que una tiene que oír..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 06
            show m_exp_piris front06
            #show m_pupils front05a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
                
            jump afternoon04_Q_OniricArt_after
            
        "No tengo ni idea...":
            call p_Help

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "¿Por qué no me extraña...?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
                
            p "..."
                
            jump afternoon04_Q_OniricArt_after
        

        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_OniricArt_after:
    
    scene black
    with fade
    
    gm "Sigamos..."
    
    scene black
    show afternoon04_paint m_dali_granmast:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Cómo se llama esta obra?" #El gran masturbador.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_GranMasurbador_question:
        
        pt "Ese careto raro con esas pestañas, ¿no estaban en el cuadro anterior...?"
        
        "Mujer olfateando las partes nobles de un hombre con la polla enana.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Estás describiendo una parte del cuadro,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "sencillamente porque no tienes ni la más remota idea de cómo diablos se titula esta obra."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "No se lo puedo negar..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Esta obra se llama {a=https://es.wikipedia.org/wiki/El_gran_masturbador}{i}El Gran Masturbador{/i}{/a},"

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dalí}Salvador Dalí{/a}."
            
            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Una cara de león con una lengua enorme,"

            pt "un grillo bocabajo con su trasero repleto de hormigas,"
            
            pt "una especie de careto deformado esnifando el suelo,"

            pt "una mujer olfateando unos testículos más largos que el micropene,"

            extend " sin mencionar todo lo demás..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "¿Qué puñetas tiene esto de \"masturbación\"?"
            
            pt "De hecho..."

            extend " ¡¿Qué puñetas tiene esto de erótico?!"
            
            jump afternoon04_Q_GranMasturbador_after
        
        "El gran masturbador.": #Correct
            
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Martq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx04
            with dissolve
                
            gm "Hmm..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¿Y quién fue su pintor?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            menu afternoon04_Q_GranMasurbador_02_question:
                
                pt "Parece una fumada mental como la anterior..."
                
                "Pablo Picasso.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)
                    
                    #NOT FINISHED

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Para nada."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    #show m_pupils right03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Ambos fueron dos de los mayores exponentes del arte del siglo XX."

                    show m_exp_mouth sad_Talkingx007
                    show m_exp_eyes 03
                    show m_exp_piris left03
                    #show m_pupils left03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Tuvieron una relación esporádica y mayormente rivalizada."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Pero no podrían ser más diferentes gráficamente..."

                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    pt "Parece que disfruta viendo como me equivoco..."
                
                    jump afternoon04_Q_GranMasturbador_after
                    
                "Francisco de Goya.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Por ser un artista que murió en el 1828,"

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    #show m_pupils right03a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "la verdad es que se avanzó bastante a su época."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Pero no,"

                    extend " te has equivocado por más de cien años..."

                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "Maldita sea..."
                    
                    #NOT FINISHED TEXT
                    
                    jump afternoon04_Q_GranMasturbador_after
                
                "Salvador Dalí.": #Correct
                    
                    call p_Help
                    $ pl.ch_pts("mp",+1)
                    $ Martq += 1 #If the answer is correct.
                    
                    #NOT FINISHED

                    show m_exp_mouth sadbiting_Silentx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx04
                    with dissolve
                    
                    gm "Hmm..."

                    jump afternoon04_Q_GranMasturbador_after
                    
                "Un enfermo talentoso del psiquiátrico.":
                    call p_Help
                    $ pl.ch_pts("mp",-3)
                    
                    #NOT FINISHED

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve
                    
                    gm "Tú sí que estás enfermo."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Pero por desgracia,"

                    extend " lo tuyo no tiene otra cura que la educación,"

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "y está claro que contigo ha sido un fracaso."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    #show m_pupils front02a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    p "¿No puedo tener opinión?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "¿Hablando sin respeto quieres dar tu opinión?"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "¡¿Ella me habla de respeto?!"
                    
                    jump afternoon04_Q_GranMasturbador_after
                    
                "Walt Disney.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)
                    
                    #NOT FINISHED

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    #show m_pupils right03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Aunque trabajó estrechamente con este artista en 1945 con el cortometraje {a=https://es.wikipedia.org/wiki/Destino_(cortometraje)}Destino{/a},"

                    show m_exp_mouth sad_Talkingx007
                    show m_exp_eyes 03
                    show m_exp_piris left03
                    #show m_pupils left03a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "no hay nada de este cuadro que recuerde mínimamente la obra de {a=https://es.wikipedia.org/wiki/Walt_Disney}{i}Disney{/i}{/a},"

                    extend " mucho menos su título..."
                    
                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris left04
                    #show m_pupils left04a
                    show m_exp_eyebrows normal
                    with dissolve

                    p "..."

                    pt "¿Y se puede saber cuál es su título?"
                    
                    jump afternoon04_Q_GranMasturbador_after
                    
                "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
                    
                    call p_Help
                        
                    jump afternoon04_Q_AfterInterrogationFail
                    
        "El poder de la mujer.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "¿Qué parte de este cuadro te hace pensar que se llama así?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "No sé..."

            extend " supongo que la mujer me ha llamado mucho la atención..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "¿Y todos los demás elementos del cuadro?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows serious
            with dissolve
            
            p "Pues..."

            extend " el narizotas parece como sumiso,"

            p "y lo demás,"

            extend " realmente no sabría cómo catalogarlo..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Esta obra se llama {a=https://es.wikipedia.org/wiki/El_gran_masturbador}El Gran Masturbador{/a},"

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dalí}{i}Salvador Dalí{/i}{/a}."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¡¿Y quién coño se está masturbando aquí?!"
            
            jump afternoon04_Q_GranMasturbador_after
            
        "No tengo ni idea...":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Por lo menos eres sincero..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Esta obra se llama {a=https://es.wikipedia.org/wiki/El_gran_masturbador}El Gran Masturbador{/a},"

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dalí}{i}Salvador Dalí{/i}{/a}."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "¿Y hay alguien sensato que pudiera llegar a adivinar el título viendo este batiburrillo de ideas sin ninguna lógica?"
            
            jump afternoon04_Q_GranMasturbador_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_GranMasturbador_after:

    scene black
    with fade

    gm "Sigamos."
    
    scene black
    show afternoon04_paint m_duchamp_fountain:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Qué es esto?" #Le Fountain de Marcel Duchamp

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_FountainDuchamp_question:
        
        pt "¿Qué cojones hace un urinario expuesto en un museo?"
        
        "Esto es un urinario con una firma en una exposición.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Eso lo dices porque desconoces cómo se titula esta pieza artística,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "y tu cultura es tan limitada que no consigues entender la trascendencia de esta obra."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            p "No."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            p "Tú me has preguntado:"

            extend " {i}¿Qué es esto?{/i}."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Y yo te he respondido,"

            extend " lo que es."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."


            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "¿Cómo se llama esta obra?"

            p "Seguramente es lo que querías preguntar..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Definir esta obra de forma tan simplista como has hecho,"

            extend " es de mente limitada..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿Cómo la definirías tú?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Con esta obra,"

            extend " se inició una auténtica revolución en el mundo del arte al demostrar..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No,"

            extend " no..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "{i}¿Qué es esto?{/i}"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No me has preguntado qué significa,"

            p "cómo se llama,"

            extend " o qué repercusiones tuvo esta obra."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            # No hace falta añadir más puntos, porque lo haces más adelante.

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Y bien..."

            extend " listillo,"

            gm "¿Cómo se llama?"

            extend " ¿y quién es su autor?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            menu afternoon04_Q_FountainDuchamp_urinary01_question:
                
                "No ha colado... Tendré que responder algo..."
                
                "Une urine normale devenue art de Damien Hirst.":
                    jump afternoon04_Q_FountainDuchamp_Hirst
                
                "La {i}Fountaine{/i} de Marcel Duchamp.": #Correct
                    call p_Help
                    $ pl.ch_pts("mp",+4)
                    $ Martq += 1 #If the answer is correct.
                    
                    #NOT FINISHED TEXT

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    #show m_pupils front02a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "..."

                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 04
                    show m_exp_piris left04
                    #show m_pupils left04a
                    show m_exp_eyebrows angryx04
                    with dissolve
                    
                    p "¿Alguna pregunta más?"

                    p "que puedas formular correctamente..."

                    show m_exp_mouth sadbiting_Silentx07
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx05
                    with dissolve
                    
                    gm "..."

                    jump afternoon04_Q_FountainDuchamp_after
                    
                "{i}Au fond à droite{/i} de Jackson Pollock.":
                    jump afternoon04_Q_FountainDuchamp_Pollock
                    
                "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
                    call p_Help
                        
                    jump afternoon04_Q_AfterInterrogationFail
        
        "La {i}Fontaine{/i} de Duchamp.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1) #If there´s no more correct answers, otherwise will be more than +1
            $ Martq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_Q_FountainDuchamp_after
            
        "Au fond a droite de Jackson Pollock.":
            
            label afternoon04_Q_FountainDuchamp_Pollock:
                
                call p_Help
                $ pl.ch_pts("mp",-2)

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "{a=https://es.wikipedia.org/wiki/Jackson_Pollock}Jackson Pollock{/a} fue un artista expresionista abstracto."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "Nunca trató con el {a=https://es.wikipedia.org/wiki/Arte_encontrado}{i}ready-made{/i}{/a}."

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Además,"

                extend " el título en francés \"Al fondo a la derecha\","

                show m_exp_mouth happy_Talkingx10
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "me parece un tanto cutre,"

                gm "y más diciéndolo al azar para probar suerte."

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "¿No tienes vergüenza alguna?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows serious
                with dissolve
                
                p "..."

                pt "Uno tiene que probar suerte a veces,"

                extend " ¿no...?"

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve

                pt "¡¿Por qué diablos sonríe?!"

                extend " Será perra..."
                
                jump afternoon04_Q_FountainDuchamp_after
            
        "{i}Une urine normale devenue art{/i} de Damien Hirst.":
            
            label afternoon04_Q_FountainDuchamp_Hirst:
                
                call p_Help
                $ pl.ch_pts("mp",-2)
                
                #NOT FINISHED

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "{i}Un urinario normal convertido en arte{/i},"

                extend " en francés..."

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Original eres poniendo nombres..."

                show m_exp_mouth happy_Silentx02
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve

                p "Euh..."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "te has comido mucho la mollera para sacar este título..."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve
                
                pt "Sin duda su sarcasmo es sutil,"

                extend " sutil..."

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "Provocar y escandalizar es el tema central en la obra de Hirst."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris right03
                #show m_pupils right03a
                show m_exp_eyebrows normal
                with dissolve
                
                gm "La obra más conocida de esta serie es {a=https://es.wikipedia.org/wiki/La_imposibilidad_física_de_la_muerte_en_la_mente_de_algo_vivo}La imposibilidad de la muerte física en la mente de alguien vivo{/a},"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris right02
                #show m_pupils right02a
                show m_exp_eyebrows normal
                with dissolve

                gm "un tiburón tigre de catorce pies sumergido en formol en una vitrina transparente."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 03
                show m_exp_piris right03
                #show m_pupils right03a
                show m_exp_eyebrows normal
                with dissolve
                
                p "..."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                #show m_pupils front02a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                p "¿Un animal muerto en una vitrina te parece una obra de arte?"

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "No me serás otro progre-vegano-come-hierba..."

                extend " ¿Verdad?"

                show m_exp_mouth sad_Silentx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                p "Hombre..."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris right03
                #show m_pupils right03a
                show m_exp_eyebrows angryx04
                with dissolve
                
                gm "Mira,"

                extend " da igual."

                gm "No quiero hablar sobre eso."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows angryx01
                with dissolve
                
                p "..."
                
                jump afternoon04_Q_FountainDuchamp_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_FountainDuchamp_after:

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "¿Cómo es posible que un sucio y maloliente urinario sacado de un vertedero se pueda llegar a considerar arte?" 
    #Porque demostró que una obra de arte no tenía que ser hermosa sino que debía provocar al intelecto.

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    menu afternoon04_Q_DuchampArt_question:
        
        pt "¿Por qué la gente que considera esto arte no ha acudido a ayuda profesional?"
        
        "Porque supo sobornar a la gente adecuada y tenía buenos contactos.":
            call p_Help
            $ pl.ch_pts("mp",-4)
            
            #NOT FINISHED

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Si realmente piensas esto,"

            extend " me das bastante lástima."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¡¿Acaso tú consideras esto una obra de arte?!"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            p "¡Es un puñetero urinario puesto del revés con una puta firma!"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¿Qué tiene de arte?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Cuando algo se escapa a tu comprensión,"

            gm "sencillamente coges una pataleta."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Como si fueras un niño pequeño."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Te tendrían que dar dos medallas,"

            gm "una por corto y otra por si la pierdes."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Qué chispa tiene la chica..."

            pt "en unos años será un mechero."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows sadx05
            with dissolve

            gm "Por curiosidad..."

            gm "¿Tus padres son hermanos?"

            show m_exp_mouth happy_Talkingx10 # Sound Laugh NOT FINISHED
            show m_exp_eyes 06
            show m_exp_piris front06
            #show m_pupils front05a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿Me encerrarían en prisión si le metiera una paliza a la pajarraca esta...?"
            
            jump afternoon04_Q_DuchampArt_after
            
        "Porque demostró que una obra de arte no tenía que ser hermosa, sino que debía provocar al intelecto.": #Correct
            
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ Martq += 1 #If the answer is correct.

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve
                
            gm "Hmm..."
            
            #NOT FINISHED TEXT
                
            jump afternoon04_Q_DuchampArt_after
        
        "Porque demostró que solo hace falta la aprobación de un crítico para que algo se considere arte.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "La visión especializada y crítica ayuda,"

            gm "promueve y aporta sin lugar a duda"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
                                                                                               
            gm "una mirada más neutral, y por lo tanto,"

            extend " más profesional."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Sin embargo y afortunadamente,"

            gm "el papel del crítico parece estar superado."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Era una figura casposo-naftalínica."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Siempre me ha interesado más la visión personal,"

            gm "al margen de las calificaciones profesionales."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Un buen crítico de arte tiene que poder nacer cada vez en una obra"

            gm "y morir también en ella."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Entonces es verdad,"

            extend " una obra no se considera arte hasta que un crítico lo ratifica..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Aunque fueras el último hombre en el mundo"

            gm "y crearas una obra que nadie volviera nunca más a contemplar,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "tu obra seguiría considerándose \"obra de arte\","

            gm "aunque por desgracia no habría nadie para poder apreciarla."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Pero es difícil que algo se exponga en un museo o galería importante sin el respaldo de un crítico de prestigio."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "El mercado ha suplantado al crítico."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "La crítica adorna,"

            extend" pero no encumbra."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Puede más un precio alto en una subasta,"

            extend " que un comentario del mejor crítico."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Entonces..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "No, [protname],"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Podría haber empezado por ahí y no haberme soltado semejante rollo..."
            
            jump afternoon04_Q_DuchampArt_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_DuchampArt_after:
    
    scene black
    with fade
    
    gm "Sigamos..."
    
    scene black
    show afternoon04_paint m_warhol_selfportrait:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Qué pretendía realmente {a=https://es.wikipedia.org/wiki/Andy_Warhol}{i}Andy Warhol{/i}{/a} con sus obras?" 
    #Trivializar y vulgarizar el propio arte para que dejara de pertenecer solo a la clase alta.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_AndyWarholPurpose_question:
        
        pt "Vivir de la fama de los demás, me imagino..."
        
        "Ganar dinero gracias a la ignorancia de la gente que compraba sus obras.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿Tú comprarías su obra?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Supongo que no."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Entonces te estás contradiciendo."

            show m_exp_mouth happy_Silentx08 #sound before Laugh.
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "..."

            show m_exp_mouth happy_Talkingx10 #sound belly Laugh
            show m_exp_eyes 06
            show m_exp_piris front06
            #show m_pupils front05a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Será cabrona..."
                
            jump afternoon04_Q_AndyWarholPurpose_after
        
        "Trivializar y vulgarizar el propio arte para que dejara de pertenecer solo a la clase alta.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ Martq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
                
            gm "Hmm..."
            
            #NOT FINISHED
                
            jump afternoon04_Q_AndyWarholPurpose_after
            
        "Conseguir fama mediante referencias populares de la cultura de su tiempo.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Eso lo consiguió indirectamente."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Pero no fue su pretensión inicial."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿Acaso no todos los artistas ansían conseguir fama y dinero?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "¿O realmente crees que los artistas viven del aire que respiran?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Tienes mucho que aprender sobre el significado de arte si piensas así..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Lo que tú digas..."
                
            jump afternoon04_Q_AndyWarholPurpose_after
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_AndyWarholPurpose_after:

    scene black
    with fade

    gm "Sigamos."
    
    scene black
    show afternoon04_paint m_magritte_treacheryofimages:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    n "Al mirar el cuadro, te fijas en que debajo hay un texto escrito en francés en el que pone \"Esto no es una pipa\"."

    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Cuál es la paradoja de esta obra?" #Que en realidad esto es la representación gráfica de una pipa pintada en un cuadro vista a través de un móvil.
    #La traición de las imágenes "Ceci n´est pas una pipe".

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_NestPasUnaPipe_question:
        
        pt "Esto es una pipa... ¿No?"
        
        "Que en realidad, es una ilustración gráfica del objeto representado.": #Correct
            
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ Martq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Bueno,"

            extend " de hecho es la ilustración de una pipa pintada en un cuadro,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "capturada fotográficamente,"

            extend " y vista a través de un móvil."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "{i}\"Ceci n'est pas une pipe\"{/i}."

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            p "Y por cierto,"

            extend " El título de esta obra es"

            extend " {a=https://es.wikipedia.org/wiki/La_traición_de_las_imágenes}La Traición de las Imágenes{/a}."
                
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils right06a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Mmm..."
            
            jump afternoon04_Q_AfterInterrogation
        
        "Que en realidad, si pones la imagen ante un espejo, ves una imagen completamente distinta.":
            
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Y se supone que el espejo lo tiene que llevar el que viene a ver la obra?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No..."

            extend " bueno,"

            p "se supone que en la misma exposición debería de estar el espejo..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿Y qué es lo que se ve, una vez la imagen está reflejada?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No sé..."

            extend " ¿Un conejo?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No, [protname],"

            extend " en esta imagen no se ve una pipa;"

            gm "sino una representación gráfica de una pipa."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Creo que no te sigo..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Si observas estas dos páginas del libro {a=https://es.wikipedia.org/wiki/Entender_el_cómic}Entendiendo los cómics{/a} de {a=https://es.wikipedia.org/wiki/Scott_McCloud}Scott McCloud{/a} lo entenderás mejor:"
            
            scene black
            show afternoon04_paint m_magritte_treacheryofimages_02:
                subpixel True
                xanchor 0.05 yanchor 0.05 zoom 0.55
                easein_quad 5.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            window hide dissolve
            pause
            
            pt "Con esta letra tan pequeña no veo un carajo... si por lo menos tuviera la {a=https://jynnemason.files.wordpress.com/2015/07/mccloud2.png}imagen en grande{/a} para verla bien..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "Que, aunque es lo primero que ves, si te fijas bien, verás representado en el cuadro algo que no es una pipa.":
            
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Y qué es lo que se supone que se ve si no es una pipa?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No sé..."

            extend " ¿Un pato?"

            extend " ¿Un conejo?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No, [protname],"

            extend " a lo que tú te estás refiriendo se llama {a=https://es.wikipedia.org/wiki/Imagen_ambigua}imagen ambigua{/a}."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Y, en el caso de que así fuera,"

            gm "en el texto no pondría"

            extend " \"Esto no es una pipa\","

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "en todo caso habría escrito:"

            extend " \"No solo es una pipa\","

            gm "o:"

            extend" \"Hay algo más que una pipa\"."
            
            scene black
            show afternoon04_paint m_paulnoth_rabbitduckarmy:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            n "En el pie de página de esta ilustración se puede leer:"
            
            n "\"No puede haber paz hasta que renuncien a su Dios Conejo y acepten a nuestro Dios Pato.\""

            n "\"Firmado: {a=http://www.paulnoth.com/}Paul Noth{/a}\"."
            
            window hide dissolve
            pause

            show m_bodynew relax_03:
                mtxell_body_ontheright_position

            show m_exp_blush 01:
                mtxell_exp_ontheright_position
            show m_exp_mouth sad_Talkingx03:
                mtxell_exp_ontheright_position
            show m_exp_eyes 04:
                mtxell_exp_ontheright_position
            show m_exp_piris front04:
                mtxell_exp_ontheright_position
            show m_exp_eyebrows surprisex001:
                mtxell_exp_ontheright_position

            show m_exp_hair_front:
                mtxell_exp_ontheright_position
            with dissolve

            gm "Del mismo modo que en esta ilustración algunos verán que defienden al ejército conejo y otros al ejército pato."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Una tira cómica,"

            gm "por cierto,"

            extend " muy mordaz con el delirio bélico de la mayoría de las religiones..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "¿Hay alguna cosa que deje sin criticar esta mujer?"
            
            jump afternoon04_Q_AfterInterrogation
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail

label afternoon04_Q_LikeClassicArt_after:
    
    #arte figurativo clásico

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Entonces..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "¿Tienes conocimientos de arte clásico?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
#########################################################
    
    if config.version <= "00.06.06": #Introduction to date with Mystery Woman.
        
        call endupdatescript
    
#######################################################
    
    menu afternoon04_Q_LikeClassicArt_after_question:
        
        pt "¿Y a qué siglo se refiere con arte clásico?"
        
        "Sí, por supuesto.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_PaintingName
        
        "No, para nada, sencillamente aprecio el buen arte.":
            call p_Help

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "Entonces no conoces a los artistas como {a=https://es.wikipedia.org/wiki/Rafael_Sanzio}Raffaello{/a},"

            extend " {a=https://es.wikipedia.org/wiki/Miguel_Ángel}Michelangelo{/a},"

            extend " {a=https://es.wikipedia.org/wiki/Donatello}Donatello{/a},"

            extend " {a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo{/a}..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¡Esos sí los conozco!"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No me dirás que son las {a=https://es.wikipedia.org/wiki/Tortugas_Ninja}Tortugas Ninja{/a},"

            extend " ¿verdad?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Entonces no..."
                
            jump afternoon04_Q_AfterInterrogationFail
        
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
            
label afternoon04_paint_c_gustavecourbet_originedumonde_PaintingName:

    $ afternoon04_Q_ClassicArt = True

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Dime..."

    play music "audio/music/alcaknight/sinfonia.ogg" fadein 3.0 fadeout 3.0
    
    scene black
    show afternoon04_paint c_gustavecourbet_originedumonde:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
        
    gm "¿Cómo se titula este cuadro?" #El origen del mundo.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_gustavecourbet_originedumonde_PaintingName_question:
    
        pt "Un felpudo algo abundante..."
        
        "El inicio de la humanidad.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "No te culpo por pensar que este pudiera ser el título,"

            extend " pero no..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Entonces,"

            extend " sería un acierto..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Va a ser que no,"

            extend " porque el título de la obra es {a=https://es.wikipedia.org/wiki/El_origen_del_mundo}{i}L´Origine du Monde{/i}{/a}."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Claro..."

            pt "porque del útero de una mujer salieron los peces,"

            extend " los elefantes,"

            extend " y hasta los volcanes..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "No te jode..."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
        
        "El origen del mundo.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
            
        "Máquina de sacar punta al lápiz.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Con esa forma de pensar,"

            extend " el tuyo estará aún para estrenar..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Si es que hay algo que hacerle punta..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Si tú supieras..."

            extend " perra."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
        
        "La perdición del hombre.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Sin duda sería un título apropiado."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "Pero..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Pero no."

            gm "El título de la obra es {a=https://es.wikipedia.org/wiki/El_origen_del_mundo}{i}L´origine du monde{/i}{/a}."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿Del mundo?"

            pt "Un poco {a=https://es.wikipedia.org/wiki/Antropocentrismo}antropocentrista{/a} el título..."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
        
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
            
label afternoon04_paint_c_gustavecourbet_originedumonde_paradox:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
            
    gm "Y bien..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Sabrías decirme cuál es la paradoja de esta obra?" #Es una obra famosa, pero poco vista.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_gustavecourbet_originedumonde_paradox_question:
    
        #pt "¿Paradoja? No es que deje mucho a la imaginación... es un cuadro bastante explícito..."
        
        "Que durante años el patriarcado ha marcado el esperma como símbolo de origen, pero es la matriz donde realmente se gesta el milagro.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "La verdad es que erraste miserablemente,"

            gm "pero reconozco que tu inocente respuesta me ha sorprendido."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿Por qué?"

            pt "¿Porque es un comentario en contra del patriarcado?..."

            pt "Majara..."

            extend " está majara..."
            
            jump afternoon04_paint_c_CreationOfAdam_Artist
        
        "Que en realidad no es una mujer, sino un hombre operado.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Claro..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Eran muy comunes en el año 1866,"

            extend " las operaciones de cambio de sexo..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¿Acaso no tenían derecho a cambiar de sexo si querían?"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Aunque lo tuvieran en su momento,"

            extend " que por desgracia no es el caso..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Si hubiera quedado como en el cuadro,"

            gm "habría sido la proeza quirúrgica del siglo."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Pero existe la remota posibilidad que fuera así entonces..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No, [protname],"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Tenía que intentarlo..."
            
            jump afternoon04_paint_c_CreationOfAdam_Artist
        
        "Es una obra famosa, pero poco vista.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_CreationOfAdam_Artist
            
        "Que aunque el pintor fuera homosexual, le fascinaba la parte íntima femenina." if afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿El autor era homosexual?"

            gm "¿De dónde diablos has sacado eso?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Bueno,"

            extend " a menudo representaba su mundo interno con sus amigos masculinos."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Eso no convierte a nadie en homosexual,"

            extend " y mucho menos en esa época."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Hay que mencionar también que sus obras más íntimas solían ser homosociales."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Mujeres semidesnudas,"

            extend " o completamente desnudas,"

            extend " acariciándose mutuamente,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "luchas varoniles entre hombres musculosos,"

            extend " sudorosos,"

            extend " y semidesnudos..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front07
            #show m_pupils left06a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Digamos que tienes tu punto..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "¡Bien!"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero esta no es la respuesta que esperaba."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Te repetiré la pregunta,"

            gm "¿Sabrías decirme cuál es la paradoja de esta obra?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox_question
        
        "No tengo ni idea...":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No me sorprende..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            pt "Esta mujer es realmente irritable..."
            
            jump afternoon04_paint_c_CreationOfAdam_Artist
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail


label afternoon04_paint_c_CreationOfAdam_Artist:
    
    scene black
    with fade
    
    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_miguelangel_creationofadam:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Quién pintó esta obra?" #Miguel Ángel

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_question:
    
        pt "De la Edad Media no parece..."
        
        "Leonardo da Vinci.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "En realidad,"

            extend " si tenemos que hacer caso a las memorias del {a=http://rbscp.lib.rochester.edu/3456}Anónimo Gaddiano{/a},"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "probablemente {a=https://es.wikipedia.org/wiki/Miguel_Ángel}Miguel Ángel{/a},"

            extend " el verdadero autor de esta obra,"

            gm "saldría de su tumba para destrozarte a golpes."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Después de lo que le costó realizar tal magna obra,"

            gm "y aun así,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo{/a} sigue siendo considerado el mayor exponente del {a=https://es.wikipedia.org/wiki/Renacimiento}Renacimiento{/a}."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "Cuando la mayoría de sus obras no salieron del papel,"

            gm "y sin embargo, él no tuvo descanso alguno en su ardua vida como artista."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Con decirme que no lo había acertado,"

            extend " hubiera bastado."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Y perderme esa expresión tuya de pura ignorancia?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            pt "Simpática la mujer cuando quiere..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
            
        "El Bosco.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Aunque vivieron más o menos en la misma época,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "la verdad es que sus estilos no podrían ser más distintos."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/El_Bosco}Hieronymus Bosch{/a} fue un magnífico artista tratando temas religiosos,"

            extend " surrealistas,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "con un gran número de simbolismos folclóricos y humor burlesco,"

            extend " a veces cruel."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Pero su estilo seguía anclado a la Edad Media."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "O sea,"

            extend " que no lo he acertado..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
        
        "Miguel Ángel.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
            
        "Sandro Botticelli.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "En realidad,"

            extend " Botticelli es más del {a=https://es.wikipedia.org/wiki/Quattrocento}Quattrocento{/a}."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Su estilo sigue manteniendo muchos elementos aún arcaicos,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "pero por lo menos te has acercado..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
            
        "Diego Velázquez.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "El maestro Velázquez no tenía demasiado que envidiar del talentosísimo artista de esta obra."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero, al nacer treinta y cinco años después de su muerte,"

            extend " tenía cierta ventaja técnica y cultural."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "O sea..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Que no lo has acertado."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Ya..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
            
        "No lo sé.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Ya lo veo..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName:

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Y dime..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "¿Cómo se titula este fragmento?" #La creación de Adán

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_PaintingName_question:
    
        pt "¿Fragmento? Eso es que la obra entera es bastante mayor..."
        
        "Hombre desnudo en la montaña tomando droga dura.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Se supone que me tengo que reír?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Hombre,"

            extend " una sonrisita tampoco te haría ningún daño..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "..." #Con cara de pocos amigos.

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "Vale,"

            extend " quizás no es mucho de la coña esta loca amargada..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum
        
        "La creación de Adán.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum
            
        "El hombre creando a Dios."if afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_miguelangel_creationofadam_PaintingName_ManCreatingGod = True
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Hmm..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Reconozco que probablemente hubiera sido el elegido por el autor,"

            gm "teniendo en cuenta el mensaje que oculta esta obra."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Debido a que me has sorprendido con tu atrevimiento,"

            gm "te concedo otra oportunidad..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¿Cómo se llama \"realmente\" este fragmento?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            jump afternoon04_paint_c_miguelangel_creationofadam_PaintingName_question
            
        "El origen del mundo.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Ese era el título de la obra anterior..."

            gm "¿O es que ya ni te acuerdas de eso?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            p "..."

            p "Pero quizás se llaman igual..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No,"

            extend " no es el caso."

            gm "Hubiera sido de mal gusto por parte de {a=https://es.wikipedia.org/wiki/Gustave_Courbet}Coubert{/a},"

            extend " llamarlo igual que esta famosísima pieza artística."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Mierda..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum
            
        "EL sexto día.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Sí,"

            gm "es cierto que, en el sexto día,"

            extend " según el {a=https://es.wikipedia.org/wiki/Génesis}Génesis Bíblico{/a},"

            gm "Dios creó a {a=https://es.wikipedia.org/wiki/Adán}Adán{/a},"

            extend " el primer hombre."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Pero también creó muchísimas cosas más,"

            gm "entre ellas a {a=https://es.wikipedia.org/wiki/Eva}Eva{/a},"

            extend " la primera mujer,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "con el permiso de {a=https://es.wikipedia.org/wiki/Lilit}Lilith{/a},"

            extend " claro..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "por si se te había olvidado..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No..."

            extend " no se me había olvidado..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Entonces es peor,"

            gm "porque das por entendido que lo realmente importante de ese día fue únicamente la creación del hombre."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No..."

            extend " yo no he dicho eso."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¡¿Entonces por qué llamarlo \"El Sexto Día\"?!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "No sé..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¡Exacto!"

            extend " No tienes ni puñetera idea de nada."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            pt "Jodeeer..."

            extend " como está la pava..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum

            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_miguelangel_creationofadam_Museum:

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Y bien..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "¿En qué museo se expone?" #En ninguno, se expone en el techo de la capilla sixtina.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_Museum_question:
    
        pt "No veo ningún marco..."
        
        "En el {i}Louvre{/i} de París.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "El {a=https://es.wikipedia.org/wiki/Museo_del_Louvre}{i}Louvre{/i}{/a} es uno de mis museos favoritos,"

            gm "no solo porque ahí se expone {a=https://es.wikipedia.org/wiki/La_Gioconda}{i}La Gioconda{/i}{/a},"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "aunque tengo mis dudas de que sea la auténtica..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Sino porque además fue la sede real del poder en {a=https://es.wikipedia.org/wiki/Francia}Francia{/a} hasta que {a=https://es.wikipedia.org/wiki/Luis_XIV_de_Francia}Luis XIV{/a} se trasladó a {a=https://es.wikipedia.org/wiki/Palacio_de_Versalles}Versalles{/a}."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Sin menospreciar el magnífico trabajo de {a=https://es.wikipedia.org/wiki/Ieoh_Ming_Pei}Ieoh Ming Pei{/a},"

            gm "con la ambiciosa modernización que recibió el lugar en los ochenta."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Entonces..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No, [protname],"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
        
        "En el Museo Nacional del Prado de Madrid.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Museo_del_Prado}El museo del Prado{/a} es uno de los mayores museos del mundo y especialmente de {a=https://es.wikipedia.org/wiki/España}España{/a}."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Pero no,"

            extend " esta obra está bastante lejos de {a=https://es.wikipedia.org/wiki/Madrid}Madrid{/a}..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "La cagué..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
        
        "En el techo de la Capilla {i}Sixtina{/i} del Vaticano.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
        
        "En la Galería {i}Uffizi{/i} de Florencia.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Por lo menos has adivinado el país donde está expuesto,"

            extend " pero no la ciudad."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "Mierda..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
            
        "Ni idea.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Al menos eres sincero contigo mismo,"

            extend " pero a mí me daría vergüenza no saber esto."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "A mí me daría más vergüenza ser tan estúpida y prepotente como tú..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_miguelangel_creationofadam_Message:

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Y ahora..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "¿Cuál es el mensaje oculto en contra de la Iglesia que se le presume?" #El manto donde está Dios en realidad representa un cerebro.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_Message_question:
    
        pt "Qué manía con buscar mensajes ocultos..."
        
        "El manto donde está Dios, en realidad, representa un cerebro humano.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_madonnagiovannino_Strange
            
        "El manto rojo alrededor de Dios tiene la forma del útero humano y la bufanda verde es el cordón umbilical recién cortado." if afternoon04_paint_c_miguelangel_creationofadam_Message_womb == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿De dónde sacas esa idea?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " {a=https://www.theverge.com/2016/12/6/13852240/westworld-finale-ford-dolores-michelangelo-brain-creation-of-adam}lo leí en alguna parte...{/a}"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "La idea es interesante,"

            gm "pero no."

            gm "No creo que sea un útero lo que esté aquí representado."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Esa será su opinión,"

            extend " ¿no?"

            pt "Al fin y al cabo lo más probable es que se trate de una simple {a=https://es.wikipedia.org/wiki/Pareidolia}pareidolia{/a}..."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Te repito la pregunta,"

            gm "¿Cuál crees que es el mensaje oculto en esta obra?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message_question
        
        "Que Dios en realidad es una nave espacial conducida por pequeños seres del espacio.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿De dónde has sacado esa idea?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Bueno,"

            extend " existe la creencia de que los dioses antiguos eran en realidad seres de otros mundos que esclavizaron a la humanidad..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Y dónde están ahora?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Yo qué sé..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "¿Y en qué te basas para creer que Miguel Ángel quiso retratar esa idea en este cuadro?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No sé,"

            extend " quizás lo sospechó y quiso retratarlo para la inmortalidad en esta pieza artística..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Interesante,"

            gm "pero no."

            gm "No es la respuesta que esperaba."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            jump afternoon04_paint_c_madonnagiovannino_Strange
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
            

#Until now Cartq = 7 if all questions are correct (Even FCBarcelona) It´s ncessary 5 points more to get 12.

label afternoon04_paint_c_madonnagiovannino_Strange:
    
    scene black
    with fade
    
    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_giovanni_madonna:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Qué hay de extraño en la obra {a=https://es.wikipedia.org/wiki/Archivo:Madonna_Col_Bambino_e_San_Giovannino_-_1400s.png}{i}Madonna de Saint Giovannino{/i}{/a}?" #Aparece un objeto volador no identificado.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_madonnagiovannino_Strange_question:
    
        pt "Todo en este cuadro parece extraño... empezando por esas caras..."
        
        "La vaca y el burro están tan juntos que parece que compartan un mismo cuerpo.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿Qué?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "De todo el cuadro..."

            gm "¿Te fijas en eso?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Soy observador."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "No,"

            extend " para nada..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Salen así de juntos como en la mayoría de obras antiguas porque es la mínima demostración de que se trata de un establo,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "porque son un detalle que no debe destacar en lo más mínimo."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Por eso están así a oscuras,"

            gm "casi imperceptibles,"

            extend " y ocupando el mínimo espacio."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Eso es que no lo he acertado..."
            
            jump afternoon04_paint_c_goya_akelarre1798_PaintingName
        
        "Es curioso que María tenga una corona brillante en la cabeza si representa que no está muerta...":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Qué?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "¿Las coronas no representan a los ángeles y a los difuntos?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Las {a=https://es.wikipedia.org/wiki/Aureola}aureolas{/a} son la forma de representar la iluminación a los {a=https://es.wikipedia.org/wiki/Ángel}ángeles{/a} y a las figuras sagradas,"
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "como lo son {a=https://es.wikipedia.org/wiki/Jesús_de_Nazaret}Jesucristo{/a},"

            extend " los {a=https://es.wikipedia.org/wiki/Santo}santos{/a},"

            gm "o, como lo es en este caso,"

            extend " la {a=https://es.wikipedia.org/wiki/María_(madre_de_Jesús)}Virgen María{/a}."
            
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            p "..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Tú has visto mucho {a=https://es.wikipedia.org/wiki/Dragon_Ball}{i}Dragon Ball{/i}{/a},"

            extend " ¿verdad?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows sadx01
            with dissolve
            
            p "..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "No, [protname],"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_paint_c_goya_akelarre1798_PaintingName
            
        "Aparece una constelación de estrellas y se ve un planeta siendo pleno día.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Constelación de estrellas?"

            extend " ¿Planeta?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Reconozco que lo que se ve a la izquierda no sé muy bien qué demonios representa que es."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "En un inicio,"

            extend " uno puede pensar que representa a {a=https://es.wikipedia.org/wiki/Santísima_Trinidad}la Santísima Trinidad{/a}."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero desde luego,"

            extend " lo de la derecha no es un planeta."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Es que se ve muy pequeño para poderlo distinguir..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Eso demuestra que es la primera vez que ves este cuadro,"

            extend " y, por lo tanto,"

            extend " que lo desconocías."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_paint_c_goya_akelarre1798_PaintingName
        
        "Aparece un objeto volador no identificado.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_goya_akelarre1798_PaintingName
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_goya_akelarre1798_PaintingName:
    
    scene black
    with fade

    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_goya_akelarre1797:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿De quién es esta obra?" # Francisco Goya. (1798) +1 

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_goya_akelarre1798_PaintingName_question:
    
        pt "Esto es un macho cabrío humanizado, ¿no?"
        
        "Vicente López Portaña.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Vicente_López_Portaña}Portaña{/a} era un artista {a=https://es.wikipedia.org/wiki/Pintura_neoclásica}neoclasicista{/a},"
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "y fue considerado en su época el mejor retratista,"

            extend " con permiso de {a=https://es.wikipedia.org/wiki/Francisco_de_Goya}Goya{/a}."
            
            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "De hecho, le hizo un retrato en el 1826."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "O sea..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Que no, [protname],"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
        
        "Francisco Goya.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
            
        "Diego Velázquez.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Velázquez fue también un pintor de la realeza,"

            extend " como el artista de esta obra."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Solo que nació ciento cincuenta años antes..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Cagada pues..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
        
        "William Blake.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris right02
            #show m_pupils right02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Aunque fue un artista romántico,"

            gm "al igual que el artista de esta obra,"

            extend " y vivieron en la misma época,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "sus estilos pictóricos eran realmente muy distintos."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "A pesar de que la calidad de {a=https://es.wikipedia.org/wiki/William_Blake}{i}Blake{/i}{/a} no era tan buena,"

            extend " debo confesar que me cautivan mucho más..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Quizás sea porque sus obras mezclan arte y poesía de una forma magistral..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Bueno..."

            p "el caso es que no lo he acertado,"

            extend " ¿verdad?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No, [protname],"

            extend " has errado miserablemente."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
               
            pt "¡Pues no te enrolles tanto cabrona!"
        
            jump afternoon04_paint_c_goya_akelarre1798_Influence
        
        "William Waterhouse.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/John_William_Waterhouse}Waterhouse{/a} nació un siglo después que el artista de este cuadro."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Aunque imbuido también por el {a=https://es.wikipedia.org/wiki/Romanticismo}Romanticismo{/a},"

            gm "que le permitió encuadrar, parte de sus obras, dentro del {a=https://es.wikipedia.org/wiki/Simbolismo}Simbolismo{/a};"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve

            gm "su estilo inicial como {a=https://es.wikipedia.org/wiki/Hermandad_Prerrafaelita}Prerrafealita{/a} lo mantuvo durante toda su vida,"
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows sadx01
            with dissolve

            gm "y en mi opinión es uno de los mayores artistas que ha habido."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Queda claro que no lo he acertado..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
        
        "No lo sé.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿En serio?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "¿No te da vergüenza no conocer a este gran maestro de las artes plásticas?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Joder,"

            p "quizás conozca al artista,"

            extend " pero esta obra no me suena..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Es una de sus obras más famosas,"

            extend " especialmente en su etapa más oscura."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Pues no,"

            extend " no lo reconozco."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Vaya tela..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Joder..."

            extend " cómo se pone la pava por un puto cuadro..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
    #faltan 4 puntos
    
label afternoon04_paint_c_goya_akelarre1798_Influence:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "A ver..."

    show m_exp_mouth sad_Talkingx05
    with dissolve
    
    gm "¿Qué suceso le influyó para crear esta obra?" #El caso de las Brujas de Zugarramurdi +1

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_goya_akelarre1798_Influence_question:
    
        pt "Cuanto más te fijas en esta obra, más cosas raras ves..."
        
        "Un {b}aquelarre{/b} que presenció el artista cuando era pequeño.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Te refieres a que vio como un macho cabrío se comía a recién nacidos en medio de un descampado a plena noche?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "He dicho \"cuando era pequeño\","

            extend " sencillamente fue una escena que lo traumatizó"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
               
            p "y con la inocencia de la niñez transformó la realidad que luego representó en este cuadro."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "Aunque es una teoría bastante interesante,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "el hecho es que desconoces que el cuadro es en realidad una crítica de un caso real que hubo en {a=https://es.wikipedia.org/wiki/País_Vasco}Euskadi{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Mierda,"

            extend " no ha colado..."
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "Está basado en una pesadilla que tuvo el artista.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No niego que la visión sea pesadillesca..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero no,"

            extend " no es un cuadro {a=https://en.wikipedia.org/wiki/Dream_art}onírico{/a}," # No Spanish Wiki.

            gm "como lo pueden ser las obras de {a=https://es.wikipedia.org/wiki/Salvador_Dalí}Dalí{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Tenía que intentarlo..."
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "El caso de las brujas de Salem.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Más de ciento cincuenta personas fueron detenidas y encarceladas,"

            extend " solo con acusaciones."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Al menos cinco de los acusados fallecieron en prisión,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "catorce mujeres y cinco hombres fueron ahorcados."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "Un hombre,"

            extend " {a=https://es.wikipedia.org/wiki/Giles_Corey}Giles Corey{/a},"

            gm "se negó a emitir declaración,"

            extend " y murió aplastado en un intento de obligarlo."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Este acontecimiento ha sido usado retóricamente en la política y la literatura popular"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "como una advertencia real sobre los peligros del extremismo religioso,"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "acusaciones falsas,"

            extend " fallos en el proceso,"

            extend " y la intromisión gubernamental en las libertades individuales."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            p "..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Aunque este cuadro critica precisamente el absurdo del fanatismo religioso,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "en realidad, se está refiriendo a otro caso que ocurrió en 1610;"

            gm "casi un siglo antes que el de {a=https://es.wikipedia.org/wiki/Juicios_de_Salem}Salem{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿Tanto le cuesta decirme simplemente?"

            extend " {i}Erraste miserablemente{/i};"

            pt "en lugar de soltar semejante rollo..."
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName

        "El caso de las brujas de Zugarramurdi.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "No lo sé.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Puedo entender que esta pregunta está quizás un poco demasiado por encima de tus posibilidades."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Pero, ¡¿quién se cree que es esta tía?!"
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
    #faltan 3 puntos
    
    ##
    
label afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName:
    
    scene black
    with fade

    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_waterhouse_magiccircle:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    gm "¿Cómo se titula esta obra?" # john_william_waterhouse_MagicCircle_1886 +1
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    p "¿Esto es arte clásico?"

    show m_exp_mouth sad_Talkingx03
    with dissolve
    
    gm "Es de 1886."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "¿Por qué lo preguntas?"

    gm "¿Acaso te rindes porque no sabes la respuesta?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Zorra..."
    
    window hide dissolve
    pause
    
    menu afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName_question:
    
        pt "¿Cómo se llama esta obra? ¡Y yo qué sé! Espero que tenga algo que ver con lo que se ve en el cuadro..."
        
        "El círculo mágico.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Hmm..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
            
        "Protección contra los cuervos.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Para qué querría alguien protegerse contra los cuervos?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "No sé..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve

            gm "Creo que has visto demasiadas veces la película {a=https://es.wikipedia.org/wiki/Los_pájaros}Los Pájaros{/a}."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows sadx05
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Pero en el cuadro da la sensación de que los cuervos no entran en el círculo que está marcando..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Quizás ese círculo sería algo más adecuado para el título..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¡Y yo qué sé!"
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
        
        "El humo del caldero.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No niego que el humo toma gran parte del cuadro,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "pero no,"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Joder..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
        
        "Una bruja buenorra.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Te cachondeas de mí?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Bueno,"

            extend " en realidad tú estás más buena..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Ya veo que no te quieres tomar más en serio estas preguntas..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Tienes la mente perturbada..."
            
            jump afternoon04_Q_AfterInterrogationFail
        
        "Bruja preparando su caldero.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Sería un título muy simplista..."

            extend " ¿No crees?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Me parece un título razonable."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No es su título."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Tenía que probarlo..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
            
        "No tengo ni la más remota idea.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Por lo menos eres sincero y confiesas tu absoluto desconocimiento."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Aunque no creo que sea algo de lo que enorgullecerse..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            p "Esta obra no es tan conocida..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Es una obra clásica,"

            extend " te guste o no."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Si buscara yo una obra perdida de esa época,"

            pt "seguro que tampoco sabría responderme bien..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_fussli_nightmare_PaintingName:
    
    scene black
    with fade

    $ afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = False  ########## DELETE THIS!!!!!!!!!!!!!!!!!!!!!!!!

    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_fussli_nightmare:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Cómo se titula esta obra?" # La pesadilla, también conocida como el íncubo de Johann Heinrich Füssli. La pesadilla. +1

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_fussli_nightmare_PaintingName_question:
    
        pt "Este cuadro me da escalofríos..."
        
        "El íncubo."if afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Aunque esta obra es también conocida con este nombre,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "no es exactamente su título."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Pero también debería valer..."

            p "¿No?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No me disgusta la respuesta,"

            gm "pero no es la que esperaba."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Prueba otra vez."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            pt "Jodida tiquismiquis..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName_question
            
        "El súcubo.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Un {a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a} es un demonio que toma la forma de una mujer atractiva para seducir a los varones."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "En esta obra es totalmente lo contrario,"

            gm "pues la víctima es una mujer y los demonios son varones."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "O sea,"

            extend " que no lo he acertado..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Exacto,"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "No me parece a mí que estos demonios tomen la forma de un hombre atractivo para seducir a la dama precisamente..."
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
            
        "Parálisis del sueño.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Ciertamente se trata de una interpretación folclórica de la parálisis del sueño."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Una incapacidad transitoria para realizar cualquier tipo de movimiento voluntario,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "que tiene lugar durante el periodo de transición entre el estado de sueño y de vigilia."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Durante el episodio,"

            gm "la persona está totalmente consciente,"

            gm "con capacidad auditiva y táctil,"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "pero es incapaz de moverse o hablar,"

            extend " lo que suele provocar gran ansiedad."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Antaño se creía que eso era causado por un íncubo o duende que oprimía el pecho del durmiente."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "De ahí esta representación gráfica de esta obra."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Entonces,"

            p "he acertado..."

            extend " ¿No?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "No,"

            extend " has errado miserablemente."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Su título es {a=https://es.wikipedia.org/wiki/La_pesadilla}{i}The Nightmare{/i}{/a},"

            extend " pero me resulta interesante que supieras lo que representa."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "Que manía tiene la pava esta de enrollarse..."
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
        
        "La pesadilla.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Hmm..."

            if afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond == False:

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
            
                gm "De hecho también es conocida como el {a=https://es.wikipedia.org/wiki/Íncubo}Íncubo{/a}."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows angryx04
                with dissolve
                
                gm "Pero así es,"

                extend " {a=https://es.wikipedia.org/wiki/La_pesadilla}{i}The Nightmare{/i}{/a} es su verdadero título."
            
            scene black
            show afternoon04_paint c_fussli_nightmare_02:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with dissolve
            
            gm "De hecho existe otra versión de esta obra realizada diez años después por el mismo autor."
            
            pt "Sinceramente,"

            extend " no sé cuál de las dos imágenes es más perturbadora..."
            
            window hide dissolve
            pause
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
        "Resacón con alucinaciones demoníacas.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
            
            p "¿Pero no ves a la chica cómo está?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿Qué formas son esas de dormir?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Es evidente que llevaba una turca enorme antes de ponerse a dormir..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Se supone que me tiene que hacer gracia?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿Qué mierda de sentido de humor tiene esta amargada?..."
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_paint_c_alfonsmucha_lepater_Theme:
    
    scene black
    with fade

    gm "Sigamos..."
    
    scene black
    show afternoon04_paint c_mucha_lepater:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    gm "¿Cuál es el tema principal de esta obra?" # Ilustración 1899 Alfons Mucha Le pater. El ocultismo y la religión. +1
    
    window hide dissolve
    pause
    
    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth serious_Silentx01:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    p "En serio..."

    extend " ¿esta obra es clásica?"

    show m_exp_mouth sad_Talkingx03
    with dissolve
    
    gm "Es del año 1899,"

    gm "por lo tanto es anterior al siglo XX,"

    extend " y es figurativa."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "¿Te rindes?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve
    
    pt "Esto es jugar sucio..."
    
    window hide dissolve
    pause
    
    menu afternoon04_paint_c_alfonsmucha_lepater_Theme_question:
    
        pt "¿El tema principal de esta obra? No sé... pero estos ojos brillantes en la oscuridad son algo perturbadores..."
        
        "El espiritismo y la resurrección.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No negaré que la mujer de blanco tiene un aspecto algo fantasmagórico..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            pt "Algo, dice..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Pero no hay ningún fantasma ni resurrección en esta obra."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Pff..."
            
            jump afternoon04_Q_AfterInterrogation
        
        "El ocultismo y la religión.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Cartq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "..."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "En todas sus ilustraciones se esconde una gran cantidad de símbolos {a=https://es.wikipedia.org/wiki/Francmasonería}masónicos{/a} y ocultistas."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils left06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Esta obra de {a=https://es.wikipedia.org/wiki/Alfons_Mucha}Alfons Mucha{/a},"

            extend " ilustra un fragmento del {a=https://es.wikipedia.org/wiki/Padre_nuestro}Padre Nuestro{/a}."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Vemos cómo un alma es tentada por entidades diabólicas"

            extend " y una figura femenina pura la protege."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{i}No nos dejes caer en la tentación{/i}."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Hombre,"

            extend " tanto como \"figura femenina pura\","

            pt "a mí me da más mal rollo la mujer esta con los ojos blancos,"

            extend " que los bichos de atrás..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "La fantasía y el folclore.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿En qué fantasía o historia folclórica dirías que se basa en esta obra?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Yo qué sé..."

            p "hay un montón que hablan sobre demonios y damas de blanco rescatando a doncellas en apuros."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "En realidad, suele ser más bien,"

            gm "príncipe valiente con su armadura y corcel,"

            extend " rescata a princesa cautiva."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "¿Eso no son más bien las historias épicas medievales para niños?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "De todos modos,"

            extend " erraste miserablemente."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Me lo he imaginado..."
            
            jump afternoon04_Q_AfterInterrogation
        
        "La vida y la muerte.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿Y quién es el que está muerto?"

            extend " ¿y quién es el que está vivo?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " la dama de blanco parece como un ente poderoso que está resucitando a la mujer que tiene entre sus manos."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Entonces el tema debería ser la resurrección, si seguimos tu lógica..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_Q_AfterInterrogation
        
        "La mitología y la historia.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿En qué narración histórica o mitológica te basas para decir que esto forma parte de ello?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "No sé,"

            p "me imagino que en alguna narración griega,"

            extend " con tantos dioses e hijos bastardos de Zeus..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "O quizás se basa en las historias medievales sobre los milagros de la Virgen..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Entonces eso sería más religión que mitología,"

            extend " ¿no crees?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿Cuál?"

            pt "¿El que he dicho de Zeus,"

            extend " o el de la Virgen...?"
            
            jump afternoon04_Q_AfterInterrogation
            
        "Droga, droga muy dura...":
            call p_Help
            #$ pl.ch_pts("mp",+0)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "¿Qué?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "¿Cuál es tu camello?"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¡¿Cómo?!"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "¿A cuánto el gramo?"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¡¿De qué que cojones estás hablando?!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Eso tú... "

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "¿Cómo cojones quieres que te diga de qué coño va esta obra?"

            extend " Si es la primera vez que la veo..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "No me interesa una mierda responder tus estúpidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
###
    
label afternoon04_Q_AfterInterrogationFail: #Si te niegas a responder.
    
    $ pl.ch_pts("mp",-2)
    
    scene afternoon04_bg macba_outside
    show afternoon04_paint empty:
        xanchor 0.25 yanchor 0.25 zoom 1.0

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "Es evidente por qué."
    
    jump afternoon04_Q_AfterInterrogation
    
###
    
label afternoon04_Q_AfterInterrogation:
    
#########################################################
    
    if config.version <= "00.06.07": #1rst Questionary of Modern or Classic Art.
        
        call endupdatescript
    
#######################################################

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0

    if Martq == 12 or Cartq == 13: #MAX (Classic Puntuation Max:30 hearts)

        scene afternoon04_bg macba_outside

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Talkingx10:
            mtxell_exp_ontheright_position
        show m_exp_eyes 08:
            mtxell_exp_ontheright_position
        show m_exp_piris front06:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve

        gm "Las has respondido todas correctamente..."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Desde luego no eres una masa de músculos sin cerebro como pensé..."
        
    elif Martq >= 11 or Cartq >= 12:
        scene afternoon04_bg macba_outside

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Silentx03:
            mtxell_exp_ontheright_position
        show m_exp_eyes 08:
            mtxell_exp_ontheright_position
        show m_exp_piris front06:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
        
        gm "Hmmm..."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows surprisex001
        with dissolve
            
        gm "Esperaba que las respondieras todas mal..."

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Y al final resulta que solo has fallado una..."

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "No eres una simple masa de músculos sin cerebro al fin y al cabo..."
        
    elif Martq >= 9 or Cartq >= 10: 

        scene afternoon04_bg macba_outside

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Silentx02:
            mtxell_exp_ontheright_position
        show m_exp_eyes 08:
            mtxell_exp_ontheright_position
        show m_exp_piris front06:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
    
        gm "Hmmm..."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils right06a
        show m_exp_eyebrows surprisex001
        with dissolve
            
        gm "Esperaba que las respondieras todas mal..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Y al final resulta que has acabado acertando algunas..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "No eres una simple masa de músculos sin cerebro al fin y al cabo..."
        
    elif Martq >=5 or Cartq >= 5:

        scene afternoon04_bg macba_outside

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth serious_Silentx01:
            mtxell_exp_ontheright_position
        show m_exp_eyes 08:
            mtxell_exp_ontheright_position
        show m_exp_piris front06:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
        
        gm "Has respondido alguna pregunta bien..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Quizás aprobarías la Educación Primaria y todo al final..."
        
    else:

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Desde luego, eres exactamente como pensaba."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Una masa de músculos sin cerebro."

    if Martq >= 12 or Cartq >= 13: #MAX

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx04
        with dissolve

        pt "Parece como si estuviera realmente molesta por ello..."

    elif Martq >= 11 or Cartq >= 12:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve

        pt "Parece como si estuviera molesta por ello..."

    else:

        show m_exp_mouth serious_Silentx01
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve

        pt "¿Qué?"

        extend " ¡¿Pero de qué va esta tía?!"
    
    if Martq >= 9 or Cartq >= 10:

        show m_exp_mouth serious_Silentx01
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows surprisex001
        with dissolve
    
        p "Oye..."

        p "Y todas estas preguntas,"

        extend " ¿a qué diablos vienen?"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Si no te gustan ya te puedes largar,"

        gm "así es como soy."
        
    else:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "Oye, payasa..."

        p "Y todas estas puñeteras preguntas..."

        extend " ¿a qué coño vienen?"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "No me tomo a bien que se me insulte."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        p "Has sido tú quien me ha insultado primero."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows surprisex02
        with dissolve

        gm "Lo único que he hecho es definirte,"

        gm "deberías sentirte adulado,"

        extend " muchos desearían tener el cuerpo que tú tienes."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Aunque, desde luego,"

        extend " no envidiarían tu materia gris."

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows normal
        with dissolve
        
        p "Pero,"

        extend "¡¿de qué coño vas?!"

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Si no te gusta,"

        extend " ya te puedes largar,"

        gm "así es como soy."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "¿Para eso me pediste quedar?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Te \"sugerí\" quedar,"

    extend " para que me aclarares quién demonios te había dado mi número de móvil."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "Pero si fuiste tú..."
    
    #Observas como apaga el cigarro y se enciende otro.
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Dime,"

    extend " estás saliendo con Neus..."

    gm "¿No es así?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    gm "Se lo sacaste de su móvil,"

    extend " ¿verdad?"
    #Una sonrisa maquiavelica.
    
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿De qué está hablando?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "O quizás te lo dio ella..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "No..."

    extend " eso no tendría sentido..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx04
    with dissolve
    
    pt "Aparte de problemas de memoria,"

    extend " es paranoica."

    pt "Genial..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿Conoces a Neus?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Sí,"

    extend " la conozco."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    gm "Mucho mejor que tú."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows sadx01
    with dissolve
    
    pt "Woah,"

    extend " ahora me viene a la ofensiva."

    pt "Esta tía está fatal..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows sadx03
    with dissolve
    
    gm "¿Te gusta?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris right02
    #show m_pupils right02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿Te refieres a Neus?"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    gm "No,"

    gm "me refiero a mi coño,"

    extend " no te jode..."

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows angryx05
    with dissolve
    
    gm "¡Claro que me refiero a Neus!"

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx05
    with dissolve
    
    pt "Definitivamente no se parece en nada a la chica de esta mañana,"

    pt "es bipolar seguro..."
    
    menu afternoon04_doyoulikeNeus_question:
        
        pt "¿Qué puñetas le digo yo a esta loca ahora?"
        
        "Bueno, estamos empezando a conocernos...":#Correct
            call p_Help
            
            if morning04_ShoppingDidac_Cond == True:
                jump afternoon04_DidacShoppingCenter
            else:
                jump afternoon04_RedHairGirl_after
            
        "La verdad es que se ve realmente mona es interesante.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows sadx05
            with dissolve
            
            gm "..." #cara de pocos amigos.
            
            if morning04_ShoppingDidac_Cond == True:
                jump afternoon04_DidacShoppingCenter
            else:
                jump afternoon04_RedHairGirl_after
            
        "Solo salgo con ella para hacerle un favor a un amigo.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            show m_exp_blush 01
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¿Un favor a un amigo?"

            show m_exp_blush 01
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "¿Qué tipo de favor?"

            show m_exp_blush 02
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Eso no te incumbe."

            show m_exp_blush 03
            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "..."
            
            if morning04_ShoppingDidac_Cond == True: #Dídac centro comercial (hace el griterío, sí o sí).
                jump afternoon04_DidacShoppingCenter
            else:
                jump afternoon04_RedHairGirl_after
            
label afternoon04_DidacShoppingCenter:

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
            
    gm "Ya veo..."

    show m_exp_blush 01
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "También veo que estás empezando a conocer a una hermosa pelirroja sin que Neus lo sepa..."

    extend " ¿Verdad?"

    show m_exp_blush 01
    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    p "¿Hermosa pelirroja?"

    extend " ¡¿Qué?!"

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "No te hagas el idiota,"

    extend " un pajarito me ha contado que además tiene muy mal humor"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "cuando la gente se ríe de ella por vestir como una fresca en un lugar público como un centro comercial."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¡Está hablando de Dídac!"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 01
    show m_exp_piris right01
    #show m_pupils right01a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "A saber qué estaríais haciendo en los probadores..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Estaba ayudando a una amiga."

    p "Aunque,"

    extend " ¿acaso me espías?"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Qué más quisieras..."

    gm "pero si te pones a hacer un griterío en un centro comercial,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "puedes esperarte que alguien lo suba en las redes sociales."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Reconocerte no fue nada complicado."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    pt "Nota mental,"

    extend " recordar que vivimos en el siglo XXI..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Así que jugando a dúo..."

    gm "¿Y conmigo qué?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "¿Buscas el trío?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "O quizás más bien el cuarteto..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "¿No te basta solo con la pelirroja?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    menu afternoon04_RedHairGirl_question:
        
        pt "¿Qué le digo yo ahora?"
        
        "No es de tu incumbencia.":
            call p_Help
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Hmm..." #cara de pocos amigos.

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Ya veo..."
            
            jump afternoon04_RedHairGirl_after
            
        "La pelirroja que tú llamas es en realidad mi amigo Dídac." if afternoon04_RedHairGirl_DidacRisk_Cond == False:
            call p_Help
            $ afternoon04_RedHairGirl_DidacRisk_Cond = True
            
            #NOT FINISHED
            
            pt "No..."

            extend " no puedo arriesgarme a decirle esto..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "Ni siquiera la conozco y tampoco es que sea una mujer que inspire mucha confianza..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "Si lo que me dijo Neus es cierto,"

            pt "podría poner en peligro su vida,"

            extend " y todo porque esta tía me está provocando..."
            
            jump afternoon04_RedHairGirl_question
            
        "¿Estás celosa?":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 01
            show m_exp_piris front01
            #show m_pupils front01a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "¿Celosa dices?"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Pobre infeliz,"

            gm "no sabes nada de mí,"

            extend " ¿verdad...?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            pt "¿A qué se refiere?"
            
            jump afternoon04_RedHairGirl_after
            
    
label afternoon04_RedHairGirl_after:

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Bah..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Venga,"

    extend " Sígueme."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils right06a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_FollowTxellinMACBA_question:
        
        pt "¿Acaso me va a seguir tratando como a un perro todo el rato?"
        
        "¿Sabes qué...? Mejor me voy a casa, no eres lo que me esperaba.":
            call p_Help

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Bah..."

            jump afternoon04_GoHome
        
        "<Seguirla>":
            call p_Help
                
            jump afternoon04_FollowTxellinMACBA
            
        "¿Nadie te ha enseñado nunca educación?":
            call p_Help

            if Martq >= 11 or Cartq >= 12:
                
                $ pl.ch_pts("mp",+1)
                $ TxellSlave -= 1

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                #show m_pupils front02a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "..."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows angryx04
                with dissolve
                
                gm "Si esperas que te lo pida por favor,"

                extend " puedes esperar sentado."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx04
                with dissolve
                
                menu afternoon04_FollowTxellinMACBA_02_question:
                    
                    pt "La verdad es que dan ganas de enviarla a la mierda."
                    
                    "<Seguirla>":
                        call p_Help
                        
                        pt "Aunque sea una gilipollas de campeonato,"

                        pt "debo admitir que me consume la curiosidad."
                        
                        pt "Tampoco hay que menospreciar el hecho de que tiene una buena delantera..."
                        
                        jump afternoon04_FollowTxellinMACBA
                        
                    "<Irte a casa>":
                        call p_Help
                        $ pl.ch_pts("mp",+1)
                        
                        p "¿Sabes qué?..."

                        p "Tu compañía no es que sea muy agradable,"
                        
                        p "creo que tendrás mejores cosas que hacer,"

                        p "especialmente si encuentras a alguien que te aguante."
                        
                        jump afternoon04_GoHome
                
            else:
                
                $ pl.ch_pts("mp",-1)

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex001
                with dissolve
                            
                gm "Mira, niñato,"

                extend " si me quieres seguir,"

                extend " bien."

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex002
                with dissolve
                
                gm "Si no,"

                extend " ya te puedes largar."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve
                
            jump afternoon04_FollowTxellinMACBA
            
label afternoon04_GoHome:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Como quieras,"

    gm "tampoco me gusta perder el tiempo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve

    pause 0.2

    scene afternoon04_bg macba_outside
    with fade
    
    pt "La verdad es que ya empezaba a sacarme de mis casillas la loca del coño esta..."
    
    jump afternoon04_AloneatHome
            
label afternoon04_FollowTxellinMACBA:

    scene afternoon04_bg macba_posters
    with fade
    
    n "Cerca del portal de la entrada, tres pilares con un cartel enorme en cada uno de ellos te llaman la atención."
    
        #Cartel dónde aparece el nombre de la chica misteriosa junto con su obra artística: El reflexe obscur (?).
    
    pt "¿Qué diablos me va a querer enseñar dentro de este \"museo\"?"
    
    n "Observas cómo le muestra lo que parece ser una acreditación al vigilante de la puerta y ambos conseguís entrar."
       
       ##---
    
    n "Desde fuera sin duda el edificio MACBA era una espléndida obra arquitectónica, por dentro tampoco decepcionaba."

    scene afternoon04_bg macba_entrance
    with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    stop music fadeout 3.0
    
    n "Quizás poco original por el abusivo blanco en todas partes, pero por lo demás era bastante imponente."
    
    n "Después de subir por una rampa considerablemente larga, llegáis a lo que parece ser el primer piso."

    scene afternoon04_bg macba_room01
    with fade

    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
    
    n "Siluetas retorcidas y lúgubres se vislumbran en las ilustraciones -con marco oscuro- colgadas en las paredes blancas,"
    
    n "y una figura negra, brillante y grotesca rellena el espacio vacío del centro de la sala."

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Sabes qué diferencia hay entre el arte abstracto y el figurativo?"

    show m_exp_mouth serious_Silentx01
    with dissolve
    
#########################################################
    
    if config.version <= "00.06.08": #Getting inside the MACBA museum.
        
        call endupdatescript
    
#######################################################
    
    menu afternoon04_MACBA_DifferenceAbsFig_question:
        
        pt "Pesadita la chica con las preguntitas de los cojones..."
        
        "El arte figurativo es una sub-rama del arte abstracto donde lo representado son figuras.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Una subrama dice..."

            gm "Es preferible que calles,"

            extend " antes de afirmar algo y demostrar así tu ignorancia."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "..."
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
            
        "Al contrario del arte abstracto, se define por la representación de figuras geométricas.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Figuras geométricas..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "¿En serio?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "¿Entonces en el Cubismo no hay ninguna forma geométrica?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "En el Cubismo la mayoría de obras son figurativas."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Tú lo has dicho,"

            extend " \"la mayoría\","

            gm "las hay que son totalmente abstractas con formas geométricas."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
        
        "El arte figurativo se define por la representación de formas reconocibles.": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
                
            gm "Sí,"

            extend " así es."

            show m_exp_mouth sad_Silentx06
            with dissolve
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
        
        "Uno es abstracto y el otro con figuras.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Y el caballo blanco de Santiago era de color blanco."

            gm "¿Me tomas por imbécil?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "No sé quién toma por imbécil a quién?"
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
            
        "No tengo ni idea...":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            if Martq >= 11 or Cartq >= 12:

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Algo tan básico,"

                extend " ¿no lo sabes?"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Entonces, ¿las preguntas que acertaste antes fueron por pura suerte?"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows sadx01
                with dissolve
                
                gm "Qué decepción..."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows angryx01
                with dissolve
                
                pt "No parece precisamente decepcionada..."
                
            else:

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 02
                show m_exp_piris right02
                #show m_pupils right02a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "Por qué será que no me sorprende..."

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows angryx01
                with dissolve
                
                p "..."
        
        "¿Sabes qué...? Estoy bastante cansadito de tus estúpidas preguntas.":
            call p_Help
            
            jump afternoon04_GoHome
        
label afternoon04_MACBA_DifferenceAbsFig_after:
    
    scene black
    show afternoon04_paint m_picasso_guernica:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Dirías que el cuadro de {a=https://es.wikipedia.org/wiki/Guernica_(cuadro)}{i}Guernica{/i}{/a} es abstracto o figurativo?"

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    
    menu afternoon04_MACBA_PicassoGuernicaFigurative_question:
        
        pt "¿Qué pretende con tantas preguntitas?"
        
        "Es totalmente abstracto.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            #NOT FINISHED TEXT
            
            if Martq >= 10:

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "No consigo entender cómo es posible que alguien que haya respondido tan bien las preguntas sobre {a=https://es.wikipedia.org/wiki/Arte_moderno}Arte Moderno{/a},"
                
                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows normal
                with dissolve

                gm "pueda dar como respuesta semejante estupidez..."
                
            elif Cartq >= 11:

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Quizás conozcas bastante sobre {a=https://es.wikipedia.org/wiki/Arte_y_cultura_clásicos}arte clásico{/a},"

                gm "pero está claro que eres un inepto total en cuanto a {a=https://es.wikipedia.org/wiki/Arte_moderno}arte moderno{/a}."
                
            else:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows angryx01
                with dissolve
                
                gm "Está claro que no entiendes absolutamente nada de arte moderno..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "¿Acaso no identificas mínimamente ojos,"

            gm "bocas,"

            extend " manos,"

            extend " rostros de animales antropomórficos,"

            extend " una espada rota, ..?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Euh..."

            extend " Seh..."

            p "Pero dibujados de forma bastante pésima..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Tú sí que eres pésimo..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Esto se llama Figuración Deconstruida."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Una obra magnífica e iconográfica del siglo XX,"

            gm "retratando los horrores de la {a=https://es.wikipedia.org/wiki/Guerra_civil_española}Guerra Civil Española{/a} por {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Pablo Picasso{/a}."
            
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve

            pt "Llámalo como quieras,"

            extend " pero estoy seguro de que un niño de cinco años sabría hacerlo mejor..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Pero cualquiera la contradice a esta..."
        
            jump afternoon04_MACBA_PicassoGuernicaFigurative_after
            
        "Es totalmente figurativo.": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "De hecho, es una figuración deconstruida."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Un crítico francés llamado {a=https://es.wikipedia.org/wiki/Louis_Vauxcelles}Louis Vauxelles{/a} lo llamó {a=https://es.wikipedia.org/wiki/Cubismo}Cubismo{/a}."
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows normal
            with dissolve

            p "Básicamente trata la realidad con figuras geometrizadas y con ausencia absoluta de perspectiva y profundidad."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Sin ir más lejos,"

            extend " {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Picasso{/a} mismo fue quien inició este movimiento con sus {a=https://es.wikipedia.org/wiki/Las_señoritas_de_Avignon}{i}Señoritas de Avignon{/i}{/a}."
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¿Acaso estás leyendo la {a=https://www.wikipedia.org/}Wikipedia{/a} por el móvil?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 01
            show m_exp_piris front01
            #show m_pupils front01a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Al igual que tú,"

            extend " estudio en una escuela de Ilustración."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils right06a
            show m_exp_eyebrows angryx04
            with dissolve
            
            p "No soy simplemente \"{i}un montón de testosterona con patas{/i}\"."
            
            jump afternoon04_MACBA_PicassoGuernicaFigurative_after
        
        "Es un poco de ambos.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Una obra abstracta,"

            extend " entendida de forma estricta,"

            gm "no puede hacer referencia a algo exterior a la obra en sí misma."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Sino que propone una nueva realidad distinta a la natural."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows sadx05
            with dissolve
            
            gm "Espacio real,"

            extend " objetos,"

            extend " paisajes,"

            extend " figuras,"

            extend " seres animados,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "e incluso formas geométricas,"

            extend " si se representan como objetos reales,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Si hay alguna referencia a algo exterior a la obra misma,"

            extend " deja de ser abstracta."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Pero..."

            extend " ¿No puede haber partes del cuadro que se entiendan y otras que son totalmente abstractas?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "¿Te refieres a lo que hacían en el {a=https://es.wikipedia.org/wiki/Expresionismo}Expresionismo{/a}?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No..."

            p "bueno,"

            extend " no sé..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Exacto,"

            extend " no tienes ni puñetera idea."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "La madre que la parió..."
        
            jump afternoon04_MACBA_PicassoGuernicaFigurative_after
        
        "Es abstracción constructiva.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            #NOT FINISHED TEXT
            
            scene black
            show afternoon04_paint m_pietm_compositionwithredblueandyellow:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            gm "La {a=https://es.wikipedia.org/wiki/Abstracción_constructiva}abstracción constructiva{/a} es sinónimo de recuperación del orden y la racionalidad en el arte frente al {a=https://es.wikipedia.org/wiki/Informalismo}informalismo{/a}."
            
            gm "Como en esta obra de {a=https://es.wikipedia.org/wiki/Piet_Mondrian}Piet Mondrian{/a},"
            
            gm "{a=http://en.roomeon.com/p/composition-with-large-red-plane-yellow-black-grey-and-blue-1921-wall-decoration/3003}Composición con un gran plano rojo, amarillo, negro, gris y azul{/a} de 1921."
            
            window hide dissolve
            pause
            
            pt "Vamos,"

            extend " que no lo he acertado..."
            
            jump afternoon04_MACBA_PicassoGuernicaFigurative_after
            
label afternoon04_MACBA_PicassoGuernicaFigurative_after:
    
    if Martq >= 12 or Cartq >= 13 and inMACBAq >= 2:#MAX

        show m_exp_mouth sadbiting_Silentx07
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "..."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Vale..."

        gm "No eres para nada lo que me esperaba,"

        extend " lo admito..."

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils right06a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Has acertado todas y cada una de las preguntas que te he hecho..."
    
    elif Martq >= 9 or Cartq >= 10 and  inMACBAq >= 1:

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Silentx04:
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
        
        gm "..."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Nada mal..."

        gm "No has acertado todas mis preguntas,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "pero has respondido mucho más bien de lo que me hubiera podido llegar a imaginar..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "¿Y se puede saber qué diablos imaginabas?"
        
    elif Martq >= 5 or Cartq >= 6 and  inMACBAq >= 1:

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "..."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Bueno,"

        gm "has respondido alguna bien..."

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "No es que se te dé demasiado bien el arte,"

        gm "pero he conocido a peores que tú..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "¡Oye!"

        extend " ¿De qué vas?"

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "¡Hey!"

        extend " tranquilo,"

        gm "aprende a aceptar cuando alguien te ofrece un cumplido."

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        pt "¡¿Eso es un cumplido?!"
        
    elif Martq == 0 or Cartq == 0 and  inMACBAq == 0:

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows serious
        with dissolve
        
        gm "Has superado todas mis expectativas."

        gm "Ni una sola respuesta correcta..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Desde luego,"

        extend " das honor al estereotipo de musculoso idiota como nadie..."
        
    else:

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Talkingx06:
            mtxell_exp_ontheright_position
        show m_exp_eyes 04:
            mtxell_exp_ontheright_position
        show m_exp_piris front04:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows surprisex001:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
        
        gm "Desde luego,"

        extend " no me has defraudado en absoluto."

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows serious
        with dissolve
        
        p "Ah,"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve

        p "¿no?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "En absoluto,"

        extend " eres el típico musculoso idiota que suelo conocer."
        
    if Martq >= 5 or Cartq >= 6 and  inMACBAq >= 1:

        scene afternoon04_bg macba_room01

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth sad_Talkingx03:
            mtxell_exp_ontheright_position
        show m_exp_eyes 04:
            mtxell_exp_ontheright_position
        show m_exp_piris right04:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
        
        gm "Reconozco que había aceptado quedar contigo cuando he recibido tu llamada,"

        extend " sencillamente,"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows normal
        with dissolve

        gm "porque sabía que me caerías mal."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        pt "¡¿Qué?!"

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        gm "Suelo recibir llamadas de tipos extraños y desconocidos"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows suspiciousx02
        with dissolve
            
        gm "que intentan ridículamente seducirme sin otro argumento que sus músculos"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 03
        show m_exp_piris right03
        #show m_pupils right03a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "rellenados con {a=https://es.wikipedia.org/wiki/Proteína}proteínas{/a} artificiales,"

        gm "{a=https://es.wikipedia.org/wiki/Creatina}creatinas{/a} varias,"

        extend " {a=https://es.wikipedia.org/wiki/Aminoácido}aminoácidos{/a},"

        extend " {a=https://es.wikipedia.org/wiki/Glúcido}carbohidratos{/a}..."
        
        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils right06a
        show m_exp_eyebrows angryx01
        with dissolve

        pt "¿De verdad no se acuerda de que fue ella misma quien me dio su número de teléfono?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Y pensé,"

        extend " mira..."

        gm "Otro típico idiota de los que cuelgan fotos en {a=https://www.facebook.com/}{i}Facebook{/i}{/a} o {a=https://www.instagram.com/}{i}Instagram{/i}{/a},"
        
        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 03
        show m_exp_piris right03
        #show m_pupils right03a
        show m_exp_eyebrows angryx01
        with dissolve

        gm "para mostrar cómo de efectivas son las inyecciones de {a=https://es.wikipedia.org/wiki/Anabolizante_androgénico_esteroideo}esteroides anabólicos androgénicos{/a}."

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows normal
        with dissolve
        
        pt "¿Entonces por qué aceptó quedar conmigo?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows sadx01
        with dissolve
        
        gm "Confieso que me divierte quedar con ellos,"

        extend " llevarlos a mi terreno"

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "y demostrarles en su cara, que hasta {a=https://es.wikipedia.org/wiki/Homer_Simpson}Homer Simpson{/a},"

        extend " es más inteligente y culto que ellos."

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Ni te imaginas la de tíos que hay así de imbéciles..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 01
        show m_exp_piris front01
        #show m_pupils front01a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "¿Para eso habías quedado conmigo?"

        extend " ¿Para reírte en mi puñetera cara?"

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils right06a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "..."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Bueno,"

        extend " reconozco que contigo había otro motivo."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Quería descubrir por mí misma qué había visto Neus en ti."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        p "..."

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve

        
        p "¿Te molesta que salga con Neus?"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "No me entusiasma la idea."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        p "..."

        show m_exp_blush 01
        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows angryx01
        with dissolve
        
        p "¿Por qué?"

        extend " ¿Qué tipo de relación tienes con Neus?"

        show m_exp_blush 02
        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Digamos que entre Neus y yo pasó algo que no es de tu incumbencia."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        pt "Es evidente que me guarda cierto rencor..."
        
    else:

        scene afternoon04_bg macba_room01

        show m_bodynew relax_03:
            mtxell_body_ontheright_position

        show m_exp_blush 01:
            mtxell_exp_ontheright_position
        show m_exp_mouth happy_Silentx05:
            mtxell_exp_ontheright_position
        show m_exp_eyes 04:
            mtxell_exp_ontheright_position
        show m_exp_piris front04:
            mtxell_exp_ontheright_position
        show m_exp_eyebrows angryx01:
            mtxell_exp_ontheright_position

        show m_exp_hair_front:
            mtxell_exp_ontheright_position
        with dissolve
        
        p "Pero..."

        extend " ¡¿De qué vas?!"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "En serio..."

        gm "En los gimnasios,"

        extend " ¿os lobotomizan el cerebro?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "¿O es que ya naciste así de idiota y los músculos no dejan espacio en tu cráneo?"

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "Si no fueras una chica..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Además de imbécil,"

        extend " misógino de mierda..."

        gm "El perfecto {i}pack{/i} de {a=https://es.wikipedia.org/wiki/Macho_ibérico}macho ibérico{/a} español."

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "¿Hay algún estereotipo de gilipollas nacional en el que no encajes?"

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "No he venido aquí para ser insultado por una niña pija repelente sin educación."

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Perdone usted,"

        extend " pero yo no te he insultado."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        p "{size=40}¡¿CÓMO QUE NO?!{/size}"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows surprisex02
        with dissolve

        gm "Tampoco hace falta que grites..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Yo no te he insultado,"

        extend " solo te he definido."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Si te sientes ofendido por decirte lo que eres,"

        gm "entonces tienes un problema bastante serio."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 06
        show m_exp_piris front06
        #show m_pupils front05a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Quizás necesites ayuda profesional..."

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "{size=35}¡¿Es que quieres que te rompa la puta cara puta asquerosa?!{/size}"

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows serious
        with dissolve
        
        s "¡¿Se puede saber qué está pasando aquí?!"

        show m_exp_mouth happy_Silentx05
        with dissolve
        
        n "La voz autoritaria de lo que parecía obviamente un agente de seguridad,"

        show m_exp_mouth happy_Silentx08
        with dissolve
        
        n "detuvo en seco la discusión."

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        p "..."

        
        $ afternoon04_MACBA_Agent01Talk_Cond = True #Habla con el agente 01 en el MACBA.

        show afternoon04_securityagent01_body:
            MACBA04_securityagent01_pos
        show afternoon04_securityagent01_mouth Talking:
            MACBA04_securityagent01_mouth_pos

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        s "Meritxell,"

        extend " ¿este tipo te está causando alguna molestia?"

        show afternoon04_securityagent01_mouth Silent

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris left03
        #show m_pupils left03a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        tx "En verdad creo que ya se iba..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "¿O no es así...?"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        pt "¡¿Meritxell?!"

        extend " Así es como se llama esta puta asquerosa..."
        
        pt "¡Maldita sea...!"

        pt "Al entrar con acreditación es obvio que la conoce..."
        
        pt "Sería una estupidez enfrentarme con el puñetero segurata de las narices..."
        
        p "Sí,"

        extend " ya me iba..."

        jump afternoon04_MACBA_GettingOut

        label afternoon04_MACBA_GettingOut:
        

        if morning04_Shopping_AgentsTalk_Cond == True: #Hablas con agentes en los probadores.
            
            pt "Un segundo..."

            extend " ¿Este tipo no es el mismo segurata que había en el centro comercial?"

        show afternoon04_securityagent01_mouth Talking
        with dissolve
        
        s "Acompáñeme a la salida entonces."

        show afternoon04_securityagent01_mouth Silent
        with dissolve
        
        if morning04_ShoppingDidac_Cond == True: #Dídac ha hecho el escándalo en el centro comercial.

            show afternoon04_securityagent01_mouth Silent

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
        
            tx "Por cierto,"

            extend " ten cuidado,"

            tx "no te encariñes demasiado de la pelirroja,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            tx "porque creo que sabes muy bien quién es en realidad..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¡¿Qué?!"

            extend " ¡¿Sabe algo de la transformación de Dídac?!"

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows surprisex02

        show afternoon04_securityagent01_mouth Silent
        with dissolve
            
        tx "Ah..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "y yo de ti iría con cuidado con tener un final feliz cerca de Neus..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows angryx01
        with dissolve
        
        tx "Luego no digas que no te he avisado..."

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        pt "¡¿Pero de qué puñetas está hablando?!"

        show afternoon04_securityagent01_body:
            subpixel True
            xzoom -1.0
            ease_quad 0.5 zoom 1.5 xanchor -0.0 yanchor 0.1
        show afternoon04_securityagent01_mouth Silent:
            subpixel True
            xzoom -1.0
            ease_quad 0.5 zoom 1.5 xanchor -2.33 yanchor -0.7
        with vpunch
        
        n "Sientes un empujón autoritario por parte del agente de seguridad."

        show afternoon04_securityagent01_mouth Talking
        with dissolve
        
        s "Andando."

        show afternoon04_securityagent01_mouth Silent
        with dissolve
        
        pt "¡Mierda!..."

        #Cambio de escenario.

        scene afternoon04_bg_macba_outside
        with fade

        stop music fadeout 3.0

        $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
        $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        n "Seguido celosamente por el agente vuelves a estar en el exterior del museo."
        
        pt "¡¿Quién diablos es esta loca del coño?!"
            
        if morning04_ShoppingDidac_Cond == True: #Dídac ha hecho el escándalo en el centro comercial.
            
            pt "¡¿Cómo puñetas sabe lo de Dídac?!"
            
        pt "¿Y a qué cojones se ha referido con lo de Neus?"
        
        pt "Podría esperar a que saliera para exigirle respuestas..."
        
        pt "Pero con la atenta mirada del agente de seguridad y estando rodeados de tanta gente,"
        
        pt "sería una estupidez forzarla a darme respuestas..."
        
        pt "No tengo otro remedio que volver a casa..."
        
        jump afternoon04_AloneatHome
        
    if Martq >= 12 or Cartq >= 13 and inMACBAq >= 2:#MAX

        show m_exp_blush 02
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve
    
        gm "Y bien,"

        extend " profesor en Historia del Arte,"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "ya que hasta ahora no has fallado ni una sola pregunta,"

        extend " por extraño que parezca..."
        
    elif Martq >= 9 or Cartq >= 10 and  inMACBAq >= 1:
        
        show m_exp_blush 00
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve

        gm "Y bien,"

        extend " conocedor de Historia del Arte,"
        
    elif Martq >= 5 or Cartq >= 6 and  inMACBAq >= 1:

        show m_exp_blush 00
        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Y bien,"

        extend " si conoces algo de Historia del Arte,"
        
    else:

        show m_exp_blush 00
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Bueno,"

        extend " aunque realmente no sepas mucho sobre Historia del Arte,"
        
        gm "a ver si me sabes decir..."

    show m_exp_blush 00
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
            
    gm "¿En qué estilo describirías lo que hay en el centro de esta sala?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Me acaba de decir en toda la cara que me odia en su fuero interno y ahora actúa tan tranquila..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils left06a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    n "La mirada de la chica cuyo nombre aún desconoces,"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows angryx01
    with dissolve
       
    n "se fija en la figura oscura y grotesca que ocupa gran parte del centro de la sala."
    
    #############################################################
    #############################################################
    #############################################################
    #############################################################
    #############################################################WORKING ON THIS RIGHT NOW 2017-08-01
    
    #La cámara se centra en la figura que hay en medio de la sala... Una pieza artística oscura y brillante.
    #goetandocera imagen.

    scene black
    show afternoon04_paint inMACBA_Txell_Mucus:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    window hide dissolve
    pause
    
    pt "¿Qué demonios es esto?"

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Y bien...?"

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    p "¿Y bien qué?"

    extend " ¿Qué quieres que te diga sobre esto?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    gm "¿Dirías que es abstracta o figurativa?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    menu afternoon04_MACBA_Mucus_AbsorFig_question:
        
        pt "Parece una cueva agujereada con mocos..."
        
        "Parece abstracto.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "No,"

            extend " es figurativa."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Amm..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿Y qué puñetas representa?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y siendo así..."

            extend " ¿Qué crees que representa?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "La muy jodida me lo tenía que preguntar..."

            jump afternoon04_MACBA_Mucus_AbsorFig_after

        "Parece figurativo.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Ya veo..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Y siendo así..."

            extend " ¿Qué crees que representa?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternoon04_MACBA_Mucus_AbsorFig_after

        "No lo sé." if afternoon04_MACBA_Mucus_AbsorFig_Cond == False:
            call p_Help
            $ afternoon04_MACBA_Mucus_AbsorFig_Cond = True

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Te he preguntado \"dirías\","

            extend " así que pido tu opinión."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Decir no sé,"

            extend " me parece una respuesta cobarde en este caso."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternoon04_MACBA_Mucus_AbsorFig_question

label afternoon04_MACBA_Mucus_AbsorFig_after:

    $ afternoon04_MACBA_Mucus_Represent_Cond = False

    menu afternoon04_MACBA_Mucus_Represent_question:

        pt "¡¿Qué puñetas le digo yo ahora?!"

        "Es como si un tío se intentara hacer una auto-felación.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            jump afternoon04_MACBA_Mucus_Represent_after

        "Parece como un 69 fusionado.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            jump afternoon04_MACBA_Mucus_Represent_after

        "Parece como un hombre en posición puente al que le cuelgan varios testículos.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            jump afternoon04_MACBA_Mucus_Represent_after

        "Parece una cueva agujereada con mocos.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿En serio?"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Realmente crees que es eso lo que representa?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "No sé..."

            extend " es lo que yo veo ahí..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Tienes un grave problema de imaginación entonces..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Yo creo que el que tiene un problema es el que ha hecho esta cosa rara..."

            jump afternoon04_MACBA_Mucus_Represent_after

        "Lo siento, pero sinceramente yo no veo nada aquí..." if afternoon04_MACBA_Mucus_Represent_Cond == False:

            call p_Help
            $ afternoon04_MACBA_Mucus_Represent_Cond = True

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Sabes que es figurativa y aun así no te atreves a dar una respuesta."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "No te estoy pidiendo que lo aciertes,"

            gm "solo he pedido tu opinión."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "¿Tan poco valoras tu criterio?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternoon04_MACBA_Mucus_Represent_question

label afternoon04_MACBA_Mucus_Represent_after:

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "Hmmm..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris left03
    #show m_pupils left03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Sigamos."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Eso es que lo he acertado..."

    pt "¿O no?"
    
    #Imagen, nalgas con código de barras.
    scene black
    show afternoon04_paint inMACBA_Txell_StripedAss:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    n "Os alejáis de la escultura central y a pocos pasos llegáis frente a un cuadro con una imagen peculiar."

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "Y este cuadro,"

    extend " ¿qué te transmite?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "Parecen unas nalgas de mujer,"

    p "con unos códigos de barra pintados en sangre,"

    extend " o tatuados en rojo por encima."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
       
    gm "He dicho \"qué te transmite\","

    extend " no"

    extend " \"qué ves\"."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    window hide dissolve
    pause

    menu afternoon04_MACBA_StripedAss_Transmit_question:

        "Pues que se ha operado las nalgas para que la aprecie gente que ni conoce, por un precio desgarrador.": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Hmm..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No está mal..."

            jump afternoon04_MACBA_StripedAss_Transmit_after

        "Pues que las mujeres son objetos de valor.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "¿Acaso tú traficas con esclavas?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¡¿Qué?!"

            extend " ¡No!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Me refiero a que se hacen valer..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "O sea,"

            extend " que somos como ganado exhibiéndonos en una subasta."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Yo no he dicho eso..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "Pero está claro que lo piensas por el modo en que te has expresado."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Esa es tu opinión..."

            jump afternoon04_MACBA_StripedAss_Transmit_after

        "Pues que sus nalgas tienen un precio y debe vender su cuerpo en contra de su voluntad.": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Hmm..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No está mal..."

            jump afternoon04_MACBA_StripedAss_Transmit_after

        "Pues las mujeres que no saben ganarse la vida, siempre pueden vender su culo al mejor postor.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Se calcula que en España hay unas cien mil prostitutas,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "el doble que {a=https://es.wikipedia.org/wiki/Fisioterapia}fisioterapeutas{/a} colegiados y el triple que {a=https://es.wikipedia.org/wiki/Odontología}dentistas{/a}."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Sin embargo,"

            gm "solo un 20\% de ellas son españolas,"

            gm "y en torno a un tercio,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "son víctimas de la trata de personas,"

            gm "obligadas a desarrollar esta actividad contra su voluntad."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Algunas de estas \"esclavas sexuales\" relatan cómo más de la mitad de los clientes,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "tratan de tener sexo con ellas sin {a=https://es.wikipedia.org/wiki/Preservativo}preservativo{/a}"

            gm "y como el 45\% les pide que consuma {a=https://es.wikipedia.org/wiki/Cocaína}cocaína{/a} antes del acto."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "¿Sigues pensando que es fácil ganarse la vida vendiendo el culo al mejor postor?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Antes de hablar,"

            extend " piensa un poco,"

            gm "que no cuesta tanto..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Cualquiera le dice nada..."

            jump afternoon04_MACBA_StripedAss_Transmit_after

label afternoon04_MACBA_StripedAss_Transmit_after:

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    gm "Sigamos."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿Me vas a preguntar sobre cada \"puto\" cuadro de esta exposición?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Es posible."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "..."
        
    pt "¿Qué cojones pretende?"

    scene afternoon04_bg macba_entrance
    with fade
    
    n "Seguís avanzando a lo largo de la galería dejando atrás varias obras pictóricas enmarcadas en la pared"

    scene afternoon04_bg_macba_room02
    with fade
    
    n "hasta llegar a otra sala idéntica a la anterior con distintos cuadros y otra pieza \"artística\" en medio de la sala."

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "Y bien,"

    extend " ¿qué te transmite esta otra obra?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "¡¿Qué narices?!"

    play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0

    scene black
    show afternoon04_paint inMACBA_Txell_ManTable:
        subpixel True
        xanchor 0.10 yanchor 0.35 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.25
    with fade

    window hide dissolve
    pause
    
    n "Una mesa de cristal sujeta por un hombre de plástico a cuatro patas con un traje de látex"
       
    n "que le cubre el cuerpo entero excepto las partes nobles y sus ojos,"
    
    n " los cuales miran fijamente a un espejo por el que se vería reflejada su entrepierna cubierta por un candado."

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Y bien?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    window hide dissolve
    pause

    menu afternoon04_MACBA_ManTable_Transmit_question:

        pt "¿Qué me transmite semejante humillación masculina?"

        "Que hay que tener una mente muy retorcida para crear semejante \"obra\".": 
            call p_Help

            if Martq >= 9:
                $ inMACBAq += 1 #If the answer is correct.
                $ pl.ch_pts("mp",+1)

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "Me resulta curioso,"

                extend " y triste a la vez,"

                gm "que siendo un buen conocedor de arte moderno,"

                gm "opines de esa manera."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex001
                with dissolve

                p "El arte expresa ideas y emociones,"

                p "o en general una visión del mundo."

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                p "Esta obra de aquí es simplemente..."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve

                gm "Continúa..."

                jump afternoon04_MACBA_ManTable_Transmit_after

            elif Cartq >= 10:
                $ inMACBAq += 1 #If the answer is correct.
                $ pl.ch_pts("mp",+1)

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve

                gm "Eres un buen conocedor del arte clásico,"

                extend " pero, desde luego;"

                gm "te queda mucho que aprender del arte moderno."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex02
                with dissolve

                p "¿No puedo tener una opinión?"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "¿Y qué opinión tienes sobre esta obra?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                jump afternoon04_MACBA_ManTable_Transmit_after

            else:
                $ pl.ch_pts("mp",-5)

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "Viendo tu incapacidad para entender el arte,"

                gm "¿te crees con la libertad de juzgar a un artista de esta manera?"

                show m_exp_mouth serious_Silentx01
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front043
                show m_exp_eyebrows surprisex001
                with dissolve

                p "¡Tú me has pedido mi opinión!"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve

                gm "Sobre la obra,"

                extend " no tu juicio moral sobre el artista."

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "Que, desde luego,"

                extend " juzgar una obra sin conocer el trasfondo de un artista,"

                gm "es de ser corto de miras."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve

                p "Opino distinto."

                jump afternoon04_MACBA_SadomasoquismAngry

        "La representación de un hombre que ha perdido completamente la cordura.": 
            call p_Help
            $ pl.ch_pts("mp",-5)

            label afternoon04_MACBA_SadomasoquismAngry:

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Estás diciendo que todo aquel que disfrute de la sumisión en el {a=https://es.wikipedia.org/wiki/Sadomasoquismo}sadomasoquismo{/a}"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "es un enfermo mental?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¡Yo no he dicho que sea un enfermo!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "Cuando alguien pierde completamente la cordura,"

            gm "es porque necesita tratamiento profesional."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Un poco de ayuda no le vendría mal en estos casos."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Si piensas así,"

            extend " realmente eres un miserable."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¡Oye!"

            p "No hace falta insultar."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Tú me has insultado a mí."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "¿Te gusta el {a=https://es.wikipedia.org/wiki/Sadomasoquismo}sadomasoquismo{/a}?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Más concretamente el {a=https://es.wikipedia.org/wiki/BDSM}BDSM{/a}."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "¡¿Me estás diciendo que disfrutarías siendo usada como apoyo de mesa estando amordazada y esclavizada?!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "En realidad mi rol en este tipo de juegos es más bien de dominante."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Hey,"

            extend " eso es algo distinto..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "No,"

            extend " no lo es."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "Estás afirmando que estoy tratando con gente enferma a la que le gusta que la traten de esta manera."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Quién te crees que eres para opinar de forma tan estúpida sobre algo que claramente desconoces por completo?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Sinceramente,"

            extend " lo que haga cada uno en la privacidad,"

            p "supongo que es cosa de cada uno,"

            extend " pero exponerlo en un museo..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Empezaba a tener cierta curiosidad sobre ti,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "pero desde luego,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "ya no me interesa en lo más mínimo seguir hablando contigo."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No sé qué ha visto en ti Neus..."

            gm "pero me imagino que no duraréis mucho."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "Eso será tu opinión,"

            p "pero vaya, viendo lo que te gusta,"

            p "me imagino que un poco de ayuda profesional,"

            extend " no te vendría mal."

            stop music fadeout 3.0

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve

            s "Meritxell,"

            extend " ¿hay algún problema?"

            $ afternoon04_MACBA_TxellName_Know = True

            # AGENTE NOT FINISHED

            scene afternoon04_bg_macba_room02

            show m_bodynew relax_03:
                mtxell_body_ontheright_position

            show m_exp_blush 01:
                mtxell_exp_ontheright_position
            show m_exp_mouth happy_Silentx02:
                mtxell_exp_ontheright_position
            show m_exp_eyes 04:
                mtxell_exp_ontheright_position
            show m_exp_piris front04:
                mtxell_exp_ontheright_position
            show m_exp_eyebrows suspiciousx02:
                mtxell_exp_ontheright_position

            show m_exp_hair_front:
                mtxell_exp_ontheright_position

            show afternoon04_securityagent01_body:
                MACBA04_securityagent01_pos
            show afternoon04_securityagent01_mouth Silent:
                MACBA04_securityagent01_mouth_pos
            with dissolve

            play music "audio/music/alcaknight/crimson_waltz.ogg" fadein 3.0 fadeout 3.0

            n "La voz imponente de un agente de seguridad del museo paró en seco la conversación que estabais teniendo."

            pt "¿Meritxell?"

            extend " ¿Es así como se llama esta chica?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Tranquilo,"

            extend " estamos bien."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Creo que el caballero sabe perfectamente dónde está la salida."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04

            show afternoon04_securityagent01_body:
                subpixel True
                xzoom -1.0
                ease_quad 0.5 zoom 1.5 xanchor -0.0 yanchor 0.1
            show afternoon04_securityagent01_mouth Talking:
                subpixel True
                xzoom -1.0
                ease_quad 0.5 zoom 1.5 xanchor -2.33 yanchor -0.7
            with vpunch

            s "Acompáñeme."

            show afternoon04_securityagent01_mouth Silent
            with dissolve

            p "¿No le ha dicho la señorita {b}Meritxell{/b},"

            p "que ya sé dónde está la salida?"

            jump afternoon04_MACBA_GettingOut

        "La {b}sumisión masculina{/b} en su máxima expresión.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Qué te hace pensar eso?"

            jump afternoon04_MACBA_ManTable_Transmit_after

        "¿No es esto denunciable?": 
            call p_Help

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Es curioso que esto te parezca denunciable y del cuadro anterior no dijeras nada."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "El cuadro anterior presumo que es una denuncia a la prostitución forzada..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Pero esto..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "¿Crees que no existen los hombres que disfrutan de la sumisión?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "¿Acaso te ofende porque te sientes identificado...?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            menu afternoon04_MACBA_ManTable_Transmit_Submission_question:

                "Para nada.": 
                    call p_Help
                    $ inMACBAq += 1 #If the answer is correct.

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "¿Entonces?"

                    jump afternoon04_MACBA_ManTable_Transmit_after

                "Simplemente me parece algo insultante y denigrante moralmente.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)
                    $ inMACBAq += 1 #If the answer is correct.
                    $ TxellSlave += 1

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Me parece que tienes la sensibilidad muy fina..."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    gm "O quizás es porque no has estudiado bien la obra que tienes en frente..."

                    jump afternoon04_MACBA_ManTable_Transmit_after

                "Quizás.":
                    call p_Help
                    $ pl.ch_pts("mp",+1)
                    $ inMACBAq += 1 #If the answer is correct.

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    gm "¿En serio?"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    p "Creo que no me conoces lo suficiente."

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Explícate..."

                    jump afternoon04_MACBA_ManTable_Transmit_after

label afternoon04_MACBA_ManTable_Transmit_after:

    scene black
    show afternoon04_paint inMACBA_Txell_ManTable:
        subpixel True
        xanchor 0.75 yanchor 0.59 zoom 1.0 #Boot
        ease_quad 15.0 xanchor 0.55 yanchor 0.15 zoom 1.0 #Ass - Correct
        ease_quad 15.0 xanchor 0.13 yanchor 0.58 zoom 1.0 #Mirror - Correct
        ease_quad 20.0 xanchor 0.0 yanchor 0.0 zoom 0.25 # General - Correct
    with fade

    p "Bueno,"

    extend " digamos que no es algo muy dominante ser usado como soporte"

    p "para una mesa por la cual se puede ver a través."
    
    p "El hecho de que solo tenga expuestas sus partes nobles,"
       
    p "con el culo al aire, con espacio suficiente por si alguien quiere darle \"amor\" por detrás,"
    
    p "con la mirada fija en un espejo que le refleja sus cojones colgando y su polla encerrada con candado..."
    
    p "No ofrece demasiadas dudas respecto a si es o no sumiso."
    
    p "Eso sin mencionar que el látex siempre se ha relacionado con el {b}masoquismo{/b},"
    
    p "especialmente cuando es tan estrecho que apenas deja respirar la piel."

    stop music fadeout 3.0

    #play sound "audio/characters/neus/breath_sigh01.ogg"

    $ renpy.music.set_volume(0.5, delay=2.0, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/breath_sigh01.ogg", channel="sfx1",loop=False, fadeout=1.0, synchro_start=True, fadein=1.0)

    scene afternoon04_macba_whisper_bg:
        afternoon04_macba_whisper_pos
    show whisper_mc_front:
        afternoon04_macba_whisper_pos
    show whisper_tx_mouth sad_Talking:
        afternoon04_macba_whisper_pos
    show whisper_tx_nose:
        afternoon04_macba_whisper_pos
    show eyeopen02:
        subpixel True
        zoom 1.0 xanchor 0.0 yanchor 0.0
        easeout_quad 10.0 zoom 2.0 xanchor 0.3 yanchor 0.3
    with fade
    
    #Susurro en la oreja
    gm "Parece como si hubieras usado alguna vez ropajes de látex..."

    play sound "audio/sfx/fall02.ogg"

    hide whisper_mc_front
    show whisper_tx_mouth happy_Silent
    with hpunch

    #Te apartas de ella, en el dibujo tu cabeza desaparece y solo se ve a ella sonriendo en primer plano sin ojos.
    
    p "¡Euh!"
    
    n "El cálido aliento detrás de tu oreja -tan repentino e inesperado-, consigue sobresaltarte ligeramente."

    scene afternoon04_bg_macba_room02

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Silentx05:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex02:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve

    p "¡¿Qué haces?!"

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Tienes pinta de ser un chico bastante dominante en la cama..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "¿Me equivoco?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    pt "Toma cambio de tema..."

    pt "aunque para ser justos,"

    extend " me ha traído a esta exposición para algo..."

    pt "Me imagino..."

    menu afternoon04_MACBA_ManTable_Dominance_question:

        pt "Por lo que me ha estado contando, ella tiene poco de sumisa..."

        "Así es, soy cien por cien dominante.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ TxellSlave -= 1

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Quizás pienses eso,"

            gm "porque nunca has estado con una mujer que sepa realmente cómo doblegar tu hombría..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿Les preguntas lo mismo a las mujeres homosexuales que no han estado con hombres?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Ahí has sido agudo, [protname],"

            extend " lo reconozco..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y hablando de edades..."

            #gm "¿Qué edad dirías que tengo? Hombretón..."

            jump afternoon04_MACBA_ManTable_Dominance_after

        "Soy totalmente sumiso si a la chica le atrae eso.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "¿Totalmente sumiso?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Ya veo..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "¿Y te ponen más las jovencitas o las maduritas?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            menu afternoon04_MACBA_ManTable_Domaninace_Age_question:

                "Me ponen más las jovencitas.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Así que sumiso pervertido..."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "Pillín..."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Y dime..."

                    jump afternoon04_MACBA_ManTable_Dominance_after

                "Me ponen más las maduritas.":
                    call p_Help
                    $ TxellSlave += 1

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Te gustan con experiencia por lo que veo..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Dime..."

                    jump afternoon04_MACBA_ManTable_Dominance_after

                "¿Y qué te hace pensar que solo me atraen las mujeres?":
                    call p_Help
                    $ pl.ch_pts("mp",+1)
                    $ TxellSlave += 1

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    gm "..."

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Esa respuesta es muy simple..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "En clase nunca te he visto mirar a los chicos sin camiseta,"

                    extend " ni sus entrepiernas..."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Sin embargo,"

                    extend " nunca quitas ojo a mi delantera."

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "Por algo será..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    p "Quizás disfruto de la visión de tu cuerpo,"

                    p "pero eso no significa que no me pueda atraer el mismo sexo..."

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Si tú lo dices..."

                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    pt "Nota mental:"

                    extend " Debo aprender a disimular mejor..."

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Por curiosidad..."

                    jump afternoon04_MACBA_ManTable_Dominance_after

                "Me resulta bastante indiferente si la persona me atrae lo suficiente.":
                    call p_Help
                    $ pl.ch_pts("mp",+1)
                    $ TxellSlave += 1

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Ya veo..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "Y hablando de edades..."

                    jump afternoon04_MACBA_ManTable_Dominance_after

        "La verdad es que lo que más disfruto es ser sumiso cuando quien me domina sabe lo que hace.":
            call p_Help
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Así que sumiso..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Pero no con cualquiera..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Y qué hace falta para que alguien te domine?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Pues una cierta experiencia y edad son cosas que ayudan,"

            extend " la verdad."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Ya veo."

            gm "Y dime..."

            #gm "¿Qué edad dirías que tengo? Hombretón..."

            jump afternoon04_MACBA_ManTable_Dominance_after


        "Supongo, nunca he encontrado a nadie que consiguiera hacerme sumiso.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ TxellSlave += 1

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Quizás porque siempre te has acostado con \"quinceañeras\"."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Me he acostado con mujeres más maduras que tú..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Ah..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "¿Sí...?"

            gm "A ver,"

            extend " dime..."

            jump afternoon04_MACBA_ManTable_Dominance_after

label afternoon04_MACBA_ManTable_Dominance_after:

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "¿Qué edad dirías que tengo?"

    extend " Hombretón..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    menu afternoon04_MACBA_TxellAge_question:

        pt "Pregunta venenosa... Si le digo menos, la trataré de niña; y si le digo más, la trataré de vieja..."

        "Menos de 20.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "[protname],"

            extend " en serio..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Te crees que conjeturar, según tu opinión, que soy una adolescente, a modo de elogio barato,"

            gm "te va a funcionar?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Quizás si hubieras disimulado un poco más,"

            extend " te hubiera funcionado mejor..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Perdona,"

            extend " pero yo te he respondido sinceramente la edad que creo que tienes."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Pues entonces me confirmas que realmente no tienes ni idea sobre mujeres de verdad..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿Insinúas que una chica mayor de dieciocho,"

            extend " pero menor de veinte,"

            p "es menos mujer que tú?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¿En qué te basas para decir eso?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "La edad no es siempre lo único que importa realmente en una persona."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Claro..."

            gm "como si te fijaras en eso,"

            extend " con las chicas que a duras penas han llegado a la mayoría de edad..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Esa es tu opinión..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Ya..."

            jump afternoon04_MACBA_TxellAge_after

        "Entre 20 y 25.":
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "No."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Pero supongo que me alegra saber que me ves tan joven..."

            jump afternoon04_MACBA_TxellAge_after

        "Entre 25 y 30.":
            call p_Help
            $ pl.ch_pts("mp",+2)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Hmm..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Ya veo..."

            jump afternoon04_MACBA_TxellAge_after

        "Entre 30 Y 35.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "¿Tan madurita me ves?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "¿La habré cagado?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Hmm..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "reconozco que tienes buen ojo."

            gm "Eso no te lo puedo negar."

            jump afternoon04_MACBA_TxellAge_after

        "Entre 35 y 40.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿Tan madura me ves?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿La he cagado?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No, [protname],"

            extend " no tengo más de treinta y cinco..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Sí,"

            extend " definitivamente la he cagado."

            jump afternoon04_MACBA_TxellAge_after

        "Entre 40 y 45.":
            call p_Help
            $ pl.ch_pts("mp",-4)

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with vpunch

            gm "{size=40}¡¿QUÉ?!{/size}"

            show m_exp_mouth sad_Talkingx12
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "¡¿Se puede saber en qué parte de mí aparento tener más de cuarenta años?!"

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            p "No sé..."

            p "se te ve una mujer inteligente,"

            extend " madura,"

            extend " desarrollada..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "¡Que esté desarrollada y sea inteligente no hace que me pongas más de diez años encima!"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve

            s "¿Hay algún problema?"

            $ afternoon04_MACBA_Agent01Talk_Cond = True #Habla con el agente 01 en el MACBA.

            show afternoon04_securityagent01_body:
                MACBA04_securityagent01_pos
            show afternoon04_securityagent01_mouth Silent:
                MACBA04_securityagent01_mouth_pos
            with dissolve

            n "Debido a su agudo tono de voz,"

            n "había llamado la atención del agente de seguridad del museo."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No,"

            extend " no,"

            extend " tranquilo..."

            gm "Solo me he puesto nerviosa porque me ha dicho que aparento tener más de cuarenta años..."

            show afternoon04_securityagent01_mouth Talking
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve

            s "Este tío es idiota."

            s "¿Quieres que lo eche a patadas?"

            show afternoon04_securityagent01_mouth Silent
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "No,"

            extend " gracias,"

            gm "en el fondo le he pedido su opinión."

            gm "No puedo enfadarme por ello."

            if morning04_Shopping_AgentsTalk_Cond == True: #Hablas con agentes en los probadores.
                
                pt "Un segundo..."

                extend " ¿Este tipo no es el mismo segurata que había en el centro comercial?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Me alegro de que no te lo hayas tomado mal..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx04
            with vpunch

            gm "{size=35}¡Me lo he tomado fatal!{/size}"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "Pero no por ello voy a echarte..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            p "..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Quizás soy yo,"

            extend " pero a veces me cuesta entender a las mujeres así..."

            show afternoon04_securityagent01_body:
                easein_quad 5.0 xanchor 0.5
            show afternoon04_securityagent01_mouth:
                easein_quad 5.0 xanchor 0.63
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve

            n "El agente se distancia de vosotros,"

            extend " no sin antes lanzarte una mirada realmente inquietante."

            
            hide afternoon04_securityagent01_body
            hide afternoon04_securityagent01_mouth
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Bah..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Será mejor cambiar de tema..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "Sí,"

            extend " quizás será lo mejor..."

            jump afternoon04_MACBA_TxellAge_after

        "La edad no define la madurez mental de una persona." if afternoon04_MACBA_TxellAge_Cond == False:
            call p_Help
            $ afternoon04_MACBA_TxellAge_Cond = True

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "¿Me estás diciendo que mentalmente soy una inmadura?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¿Euh?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¡Yo no he dicho eso!"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No me evadas la pregunta, [protname],"

            extend " responde."

            gm "¿Qué edad dirías que tengo?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "No ha colado..."

            jump afternoon04_MACBA_TxellAge_question

label afternoon04_MACBA_TxellAge_after:

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Dime..."

    gm "¿Has usado látex o cuero en algún encuentro íntimo?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    pt "Está claro que no me va a revelar la edad exacta que tiene..."

    menu afternoon04_MACBA_LatexUse_question:

        pt "¿Látex o cuero? ¿Pero qué entiende esta mujer por sexo...?"

        "Alguna vez, pero no es mi preferencia.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ TxellSlave -= 1

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Al menos lo has probado,"

            extend " aunque es una lástima que no te haya gustado lo suficiente."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Es probable que fuera con una niñata quinceañera,"

            gm "que no tuviera ni puñetera idea de lo que hacía..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows normal
            with dissolve

            p "Opinas sobre algo de lo que no tienes ni idea..."

            p "además,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "puedo tener mi opinión,"

            extend " ¿no?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "También puedes cambiar de idea,"

            extend " ¿verdad?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¿A qué viene ese interés para saber si me podrían gustar o no estas cosas?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿Acaso admites que quizás te puedan atraer los hombres?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Aunque es poco probable,"

            extend " no niego esa posibilidad."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Pero confieso que me despiertas interés,"

            gm "aunque por ahora es meramente curiosidad."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿A qué viene entonces la pregunta del látex?"

            #gm "El látex es un material que requiere una serie de cuidados," 
            jump afternoon04_MACBA_LatexUse_after

        "Me encantaría someterte vestida así.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave -= 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "¿Te gustaría...?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¡Por supuesto!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows sadx01
            with dissolve

            gm "Pff..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Qué novedad..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No eres nada original,"

            extend " ¿sabes?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            p "Bueno,"

            extend " si no quieres,"

            p "tampoco te voy a obligar,"

            extend " eh."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Con esa actitud de niñato consentido,"

            extend " ¿pretendes seducirme?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "¿Con qué mierda de niñatas has estado?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "¿O es que en realidad eres más de encerrarte en una habitación con tu amiga \"la mano derecha\","

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "jugando o viendo historias,"

            extend " con personajes con \"{a=https://es.wikipedia.org/wiki/Muerte_encefálica}encefalograma plano{/a}\","

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "y de niñitas que dicen tener dieciocho,"

            gm "pero que aparentan quince"

            extend " y tienen tetas tan grandes como su cabeza?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "Como si tus tetas fueran enanas..."

            extend " ¡No te jode!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿A qué viene entonces la preguntita sobre el látex y el cuero de las narices?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Hmm..."

            #gm "El látex es un material que requiere una serie de cuidados," 
            jump afternoon04_MACBA_LatexUse_after

        "Me encantaría que me sometieras mientras yo me visto así.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Ya sé que te gustaría."

            gm "No serías el primero..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Pensé que no te gustaban los hombres..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Y no me gustan."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            p "¿Entonces?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Me gusta la dominación."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "En ese aspecto me da igual si es un hombre,"

            gm "una mujer,"

            extend " un transexual,"

            extend " o lo que sea,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "mientras sea un ser racional"

            extend " y mínimamente culto."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            pt "Lo dice como si lo hubiera hecho con marcianillos verdes..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Ni siquiera tendría que llegar a tocarte para que te corrieras como un caballo en celo desbocado."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "No se lo tiene creído la tía ni nada..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Sé que ahora mismo eres incapaz de ser consciente de las posibilidades..."

            #gm "El látex es un material que requiere una serie de cuidados," 
            jump afternoon04_MACBA_LatexUse_after

        "Nunca, pero es algo con lo que he tenido curiosidad.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Hay una frase que dice;"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "\"La curiosidad mató al gato\"."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Pero en realidad es una mala traducción,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "ya que proviene de una expresión inglesa del siglo XVIII,"

            extend " que dice;"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "{i}\"{a=https://en.wikipedia.org/wiki/Curiosity_killed_the_cat}Care{/a} killed the cat\"{/i}." # No Spanish Wiki.

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "{i}Care{/i} significa preocupación,"

            extend " no curiosidad."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No niego que esta pueda matar,"

            extend " pero, desde luego..."


            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Qué vida más mísera y olvidable viviríamos si no fuéramos curiosos."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Supongo..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Hmm..."

            jump afternoon04_MACBA_LatexUse_after

        "Nunca, ni ganas.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave -= 1

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Bueno,"

            extend " es una pena que pienses así..."

            jump afternoon04_MACBA_LatexUse_after

label afternoon04_MACBA_LatexUse_after:

    play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
            
    gm "El {a=https://es.wikipedia.org/wiki/Fetichismo_de_látex}látex{/a} es un material que requiere una serie de cuidados," 

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows normal
    with dissolve
        
    gm "de lo contrario puede estropearse muy rápido."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    n "Su tono de voz es distinto, más calmado, más femenino, más evocador..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Aplicar un abrillantador sobre la superficie,"

    gm "y talco en el revés forma parte del ritual."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "La fuerte estimulación erótica provocada por el látex se basa,"

    extend " ante todo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "en la visión del cuerpo ceñido y realzado."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "El tacto"

    extend " y el olor característico del caucho,"

    gm "también entran en juego."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "El sonido del roce de dos cuerpos vestidos con látex es especialmente estimulante para los {a=https://es.wikipedia.org/wiki/Fetichismo_sexual}fetichistas{/a},"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "que en ocasiones,"

    extend " llegan a hacer el amor en una cama con sábanas de látex. "
    
    #Sientes como la chica se acerca sugerentemente hacia ti.

    show m_bodynew relax_03:
        m_txell_atright_pos_zoom0_25

    show m_exp_blush 01:
        m_txell_atright_pos_zoom0_25
    show m_exp_mouth happy_Talkingx03:
        m_txell_atright_pos_zoom0_25
    show m_exp_eyes 04:
        m_txell_atright_pos_zoom0_25
    show m_exp_piris front04:
        m_txell_atright_pos_zoom0_25
    show m_exp_eyebrows surprisex001:
        m_txell_atright_pos_zoom0_25

    show m_exp_hair_front:
        m_txell_atright_pos_zoom0_25
    with Dissolve (1.0)
    
    gm "A algunos les gusta por su olor,"

    extend " por su particular suavidad"

    gm "y por el calor que transmite el cuerpo desnudo que hay debajo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Otros disfrutarán pensando en la idea de sentirse \"como aprisionados\","

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows sadx03
    with dissolve

    gm "y por lo tanto,"

    extend " preferirán los trajes de cuerpo entero percibiendo las partes más sensibles del cuerpo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "siendo frotados continuamente en cada simple roce o gesto."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "O incluso la sensación de sentirse maltratados por su propia prenda..."

    #Como se acerca un poco más.

    show m_bodynew relax_03:
        m_txell_atright_pos_zoom0_5

    show m_exp_blush 02:
        m_txell_atright_pos_zoom0_5
    show m_exp_mouth happy_Talkingx10:
        m_txell_atright_pos_zoom0_5
    show m_exp_eyes 04:
        m_txell_atright_pos_zoom0_5
    show m_exp_piris front04:
        m_txell_atright_pos_zoom0_5
    show m_exp_eyebrows sadx05:
        m_txell_atright_pos_zoom0_5

    show m_exp_hair_front:
        m_txell_atright_pos_zoom0_5
    with Dissolve (1.0)

    #show m_body 01_relax:
        #m_body_atright_position_zoom0_6_anim
    #show m_exp_blush 02:
        #m_face_atright_position_zoom0_6_anim
    #show m_exp_mouth happy_Talkingx10:
        #m_face_atright_position_zoom0_6_anim
    #show m_exp_eyes 04:
        #m_face_atright_position_zoom0_6_anim
    #show m_exp_piris front04:
        #m_face_atright_position_zoom0_6_anim
    ##show m_pupils front04a:
        ##m_face_atright_position_zoom0_6_anim
    #show m_exp_eyebrows sadx05:
        #m_face_atright_position_zoom0_6_anim
    #with dissolve
    
    gm "Una \"segunda piel\" que puede dar cierta seguridad para la persona dominante"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "creando un personaje para exhibir un mayor {a=https://es.wikipedia.org/wiki/Atracción_sexual}{i}sex-appeal{/i}{/a},"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
        
    gm "para satisfacción del sumiso fetichista."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "La presión,"

    extend " sentir tu cuerpo ceñido,"

    extend " comprimido,"

    extend " encerrado."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Incluso el hecho de usar una máscara para eliminar completamente la identidad,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows sadx05
    with dissolve
    
    gm "relegándote a simple \"objeto\""

    show m_bodynew relax_03:
        m_txell_atright_pos_zoom0_75

    show m_exp_blush 01:
        m_txell_atright_pos_zoom0_75
    show m_exp_mouth sad_Talkingx003:
        m_txell_atright_pos_zoom0_75
    show m_exp_eyes 04:
        m_txell_atright_pos_zoom0_75
    show m_exp_piris front04:
        m_txell_atright_pos_zoom0_75
    show m_exp_eyebrows surprisex001:
        m_txell_atright_pos_zoom0_75

    show m_exp_hair_front:
        m_txell_atright_pos_zoom0_75
    with Dissolve (1.0)

    #show m_body 01_relax:
        #m_body_atright_position_zoom1_0_anim
    #show m_exp_blush 03:
        #m_face_atright_position_zoom1_0_anim
    #show m_exp_mouth sad_Talkingx003:
        #m_face_atright_position_zoom1_0_anim
    #show m_exp_eyes 04:
        #m_face_atright_position_zoom1_0_anim
    #show m_exp_piris front04:
        #m_face_atright_position_zoom1_0_anim
    ##show m_pupils front04a:
        ##m_face_atright_position_zoom1_0_anim
    #show m_exp_eyebrows surprisex001:
        #m_face_atright_position_zoom1_0_anim
    #with dissolve

    gm "en símbolo de sumisión absoluta a tu dueña..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Realmente está muy cerca..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Dime, [protname],"

    gm "¿crees que no disfrutarías de esta experiencia dejándote llevar completamente como sumiso?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    menu afternoon04_MACBA_LatexSubmissive_question:

        pt "¿Me está intentado seducir o intenta convertirme en su muñeco?"

        "Desde luego que sí.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave += 1

            show  m_exp_blush 02
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Vaya,"

            extend " creía que ofrecerías más resistencia..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¿Por?"

            show  m_exp_blush 01
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Tienes pinta de ser el típico {a=https://es.wikipedia.org/wiki/Macho_ibérico}macho ibérico{/a} español que no permite que se le manche su masculinidad..."

            show  m_exp_blush 00
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "A veces las apariencias engañan..."

            show  m_exp_blush 00
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternoon04_MACBA_LatexSubmissive_after_02

        "Desde luego que no.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ TxellSlave -= 1

            #Direct Jump

            jump afternoon04_MACBA_LatexSubmissive_after

        "Lo dudo mucho.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+2)

            #Direct Jump

            jump afternoon04_MACBA_LatexSubmissive_after

        "Me estás dando miedo...":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave += 1

            show  m_exp_blush 03
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "¿Te doy miedo?"

            show  m_exp_blush 02
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y eso que no has visto nada aún..."

            show  m_exp_blush 00
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            jump afternoon04_MACBA_LatexSubmissive_after_02
            
    #Te agarra la polla con fuerza con su mano mientras con la otra te coge del hombro con fuerza.

label afternoon04_MACBA_LatexSubmissive_after:

    stop music fadeout 1.0

    $ afternoon04_macba_TxellGrabYourBalls_Cond = True

    scene afternoon04_macba_grabbingdick:
        subpixel True
        zoom 1.0 xanchor 0.28 yanchor 0.2
        easein_quad 1.0 zoom 0.5 xanchor 0.0 yanchor 0.0 #General View

    show border_lines 01:
        subpixel True
        zoom 0.5 xanchor 0.0 yanchor 0.0
        block:
            easein_quad 1.0 zoom 0.9 xanchor 0.23 yanchor 0.23
            easein_quad 1.0 zoom 0.7 xanchor 0.18 yanchor 0.18
            repeat
    with hpunch

    play sound "audio/sfx/fall02.ogg"
    
    p "¡Ey!"
    
#########################################################
    
    if config.version <= "00.06.09": #She gets really close to you after the interrogation.
        
        call endupdatescript
    
#######################################################

    scene afternoon04_bg_macba_room02

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 02:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Silentx08:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with vpunch

    play sound "audio/sfx/fall04.ogg"
    
    n "Te apartas instintivamente de ella."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¡¿Qué haces?!"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
    
    gm "Si dices que no lo disfrutarías en absoluto,"

    gm "¿a qué se debe esa erección matutina?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¡¿Qué?!"

    scene black
    with dissolve
    
    n "Con el roce del momento no te habías percatado, pero efectivamente tu miembro estaba terso y duro como una roca"
    
    n "haciendo cierta presión debajo de de la tela de ropa que la cubre."

    scene afternoon04_bg_macba_room02

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 02:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx10:
        mtxell_exp_ontheright_position
    show m_exp_eyes 02:
        mtxell_exp_ontheright_position
    show m_exp_piris down02:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex02:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "Coño..."

    extend " Pedazo de paquete gastas..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris down03
    #show m_pupils down03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "¿Es que eres tataranieto de {a=https://es.wikipedia.org/wiki/Grigori_Rasputín}Rasputín{/a}?"

    extend " ¿o qué?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "La erección la tengo por tenerte tan cerca y por tu tono de voz..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¡No por lo que me has contado!"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Ya..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Si eres tan iluso como para creer tu propia mentira para evitar la realidad,"

    extend " allá tú..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "¿Se puede saber qué pretendes?"

    p "Pensaba que habías dicho que no estabas interesado en mí..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Estoy curiosa de saber por qué le interesas a Neus,"

    extend " ya te lo he dicho."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Qué rollo se llevará esta con Neus?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris down03
    #show m_pupils down03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Aunque es evidente que yo sí te atraigo."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Pero lo tienes bastante difícil para que yo me interese por ti,"

    gm "de cualquier otro modo que no sea mera curiosidad..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Creo que eso ya me lo ha dejado bastante claro antes..."

    show m_exp_blush 01
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve

label afternoon04_MACBA_LatexSubmissive_after_02:
    
    gm "Sigamos..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows normal
    with dissolve

    menu afternoon04_MACBA_LatexSubmissive_Leaving_question:

        pt "Su personalidad es jodidamente irritable..."

        "Y una mierda, paso de seguir escuchando gilipolleces.":
            call p_Help
            $ pl.ch_pts("mp",-5)
            $ TxellSlave += 1

            if music_play != "dreamsBecomeReal_fast":
                play music "audio/music/kevinmacleod/sad/dreamsBecomeReal_fast.ogg" fadein 2.0 fadeout 2.0
                $ music_play = "dreamsBecomeReal_fast"

            scene afternoon04_bg_macba_room02

            show m_bodynew relax_03:
                mtxell_body_ontheright_position

            show m_exp_blush 00:
                mtxell_exp_ontheright_position
            show m_exp_mouth sad_Talkingx03:
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

            # totoro

            # show m_exp_blush 00
            # show m_exp_mouth sad_Talkingx03
            # show m_exp_eyes 04
            # show m_exp_piris front04
            # #show m_pupils front04a
            # show m_exp_eyebrows suspiciousx02
            # with dissolve

            gm "Tú mismo..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Total,"

            gm "si tampoco me vas a meter la polla entre las piernas..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Para qué perder más el tiempo..."

            extend " ¿No?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Qué mentalidad más desesperadamente arcaica y {a=https://es.wikipedia.org/wiki/Ingenuidad}naïf{/a}..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            # NOT FINISHED "Dibujo: poner mano en el bolsillo para sacar un dispositivo con botón rojo."

            n "De su bolsillo saca lo que parece una especie de dispositivo con un botón rojo."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¿Qué es eso?"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Nada que te importe,"

            extend " ¿No te ibas?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Aún no me has dicho de qué conoces a Neus."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve

            s "¿Hay algún problema con este caballero?"

            extend " Meritxell."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve

            n "A tu espalda, una voz profunda, seca -y autoritaria-, te deja sorprendido por unos segundos."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Meritxell..."

            extend " ¿Así es como se llama esta rubia tetona?"

            $ afternoon04_MACBA_Agent01Talk_Cond = True #Habla con el agente 01 en el MACBA.

            show afternoon04_securityagent01_body:
                MACBA04_securityagent01_pos
            show afternoon04_securityagent01_mouth Silent:
                MACBA04_securityagent01_mouth_pos

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Digamos que,"

            extend " el \"Caballero\","

            extend" ya se iba..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿No es así...?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Sí,"

            extend" supongo que sí..."

            jump afternoon04_MACBA_GettingOut

        "<Seguirla>":
            call p_Help

            jump afternoon04_MACBA_LatexSubmissive_Leaving_after

label afternoon04_MACBA_LatexSubmissive_Leaving_after:

    play music "audio/music/kevinmacleod/happy_boy_end_theme.ogg" fadein 3.0 fadeout 3.0

    scene afternoon04_bg macba_infantile:
        subpixel True
        zoom 1.0 xanchor 0.0 yanchor 0.0
        ease_quad 30.0 zoom 0.5 xanchor 0.0 yanchor 0.0
    with fade
             
    n "Siguiendo la misma ruta que la vez anterior,"

    n "tus pasos te llevan a lo que sería la siguiente sala."

    n "Predomina un color rosado combinado con otros colores vivos,"
    
    n "con unas figuras dulces y entrañables en los cuadros colgados en las paredes de la nueva sala."
    
    n "Paraguas en los que cuelgan hilos con trozos de arcoíris como si fueran bolas de nieve por la sala,"
       
    n "letras infantiles por todas partes de todos los colores imaginables,"
    
    n "y una figura de un pez de estética grácil -con ojos saltones y enternecedores-,"

    n "ocupa el centro de la sala."
    
    gm "[protname],"

    extend " ¿se puede saber a dónde vas?"
    
    gm "Eso es otra exposición."
    
    p "..."
    
    pt "Ya decía yo..."

    window hide dissolve
    pause

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0

    scene afternoon04_bg_macba_room02

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx003:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex02:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    gm "¿Es que acaso no has visto el panfleto en la entrada sobre lo que se expone en el museo este mes al entrar?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "Sí..."
       
    pt "pero quizás no le he prestado suficiente atención..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "¿No has leído mi nombre ahí?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿Tu nombre?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Supongo que sabes cómo me llamo..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "¿Verdad?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "No tendrás los suficientes \"cojones\" como para quedar con una chica que pretendes tirarte y ni siquiera sabes cómo se llama..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¿Y qué te hace pensar que quiero follarte?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Si tu mirada,"

    extend " que no quita ojo a mis pechos,"

    gm "no fuera suficiente indicio,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "tu erección,"

    extend " que sigue estando igual,"

    gm "creo que responde a tu pregunta."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Me cago en la polla..."

    extend " ¡¿Es que no sabes disimular jodía?!"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Y bien,"

    extend " ¿cómo me llamo?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    $ afternoon04_MACBA_TxellName_silence = False
    
    menu afternoon04_MACBA_TxellName_question:

        pt "Ya tardaba en preguntarme su nombre..."

        "Montse.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "Marta.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "Míriam.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "Mercedes.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "Meritxell.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            $ afternoon04_MACBA_TxellName_Know = True

            show m_exp_blush 02
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Bueno,"

            extend " me imagino que por lo menos mala memoria no tienes,"

            tx "después de todo..."

            show m_exp_blush 01
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "¿Qué ñordo de concepto tiene esta tía de mí?"

            jump afternoon04_MACBA_TxellName_after

        "Meredith.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "María.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "¿Todo esto que hemos visto es obra tuya?" if afternoon04_MACBA_TxellName_silence == False:
            call p_Help
            $ afternoon04_MACBA_TxellName_silence = True

            show m_exp_eyebrows angryx01
            show m_exp_mouth sad_Talkingx06
            with dissolve

            gm "No me cambies de tema, listillo..."

            show m_exp_eyebrows serious
            show m_exp_mouth sad_Talkingx05
            with dissolve

            gm "¿Cómo me llamo?"

            show m_exp_eyebrows angryx01
            show m_exp_mouth serious_Silentx01
            with dissolve

            pt "Mierda..."

            extend " no ha colado..."

            jump afternoon04_MACBA_TxellName_question

label afternoon04_MACBA_TxellName_Fail:

    $ afternoon04_MACBA_TxellName_Know = True

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    gm "No."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    gm "Mi nombre es {a=https://en.wikipedia.org/wiki/Meritxell_(given_name)}\"Meritxell\"{/a}." # No Spanish Wiki.

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve

    pt "Un nombre catalán,"

    extend " catalán..."

    show m_exp_blush 01
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "Jodido de pronunciar el cabrón, además..."

    show m_exp_blush 02
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows surprisex001
    with dissolve

    pt "El que le puso este nombre,"

    pt "parece que quiere ver cómo la gente de otras lenguas lo pronuncia mal..."

    show m_exp_blush 01
    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx04
    with dissolve

    aj ":)"

    jump afternoon04_MACBA_TxellName_after

label afternoon04_MACBA_TxellName_after:

    show m_exp_blush 00
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    p "Y bien,"

    extend " Meritxell..."

    p "¿Se puede saber por qué hemos venido aquí?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Te he traído aquí para que me des tu opinión como ilustrador,"

    if Cartq >= 10:

        tx "y, por lo visto,"

    if Martq >= 12: #MAX 

        show m_exp_blush 02
        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows surprisex02
        with dissolve

        tx "experto en el arte moderno;"

    elif Cartq >= 13: #MAX

        show m_exp_blush 02
        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows surprisex02
        with dissolve

        tx "experto en arte clásico;"

    elif Martq >= 9:

        show m_exp_blush 01
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex02
        with dissolve
    
        tx "conocedor de historia del arte moderno;"

    elif Cartq >= 10:

        show m_exp_blush 01
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "conocedor de historia del arte clásico;"

    else:

        show m_exp_blush 00
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "aunque en arte quizás no eres un experto,"

        extend " apreciaría igualmente tu opinión sobre mi obra."


    if (Cartq or Martq) >= 10:
        extend " sobre mi obra."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿No habías dicho que me habías hecho venir para reírte en mi jodida cara?"

    show m_exp_blush 01
    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Como sueles hacer con otros tipos que te llaman por el móvil,"

    extend " por lo visto..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve 
    
    tx "Sí."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "Esa era la idea inicial."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    pt "Y lo dice tan tranquila..."

    if Martq >= 9 or Cartq >= 10:

        if Martq >= 12 or Cartq >= 13: #MAX 

            show m_exp_blush 02
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex02
            with dissolve

        elif Martq >= 9 or Cartq >= 10:

            show m_exp_blush 01
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex02
            with dissolve

        tx "Pero, francamente,"

        if Martq >= 12 or Cartq >= 13: #MAX 
        
            extend " viendo que eres todo un ilustrado de la cultura artística,"

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            tx "ahora me interesa realmente tu opinión."

        elif Martq >= 9 or Cartq >= 10:
        
            extend " viendo que tampoco se te da tan mal la cultura artística,"

            show m_exp_mouth happy_Talkingx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "ahora me interesa tu opinión."

    else:

        show m_exp_blush 00
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "aunque en arte quizás no eres un experto, apreciaría igualmente tu opinión sobre mi obra."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Si sigues aquí,"

    extend " es porque al fin y al cabo tampoco detestas del todo mi compañía."

    show m_exp_blush 01
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Si sigo aquí, es quizás,"

    extend " porque al igual que tú,"

    p "también soy alguien curioso."

    show m_exp_blush 02
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Hmm..."

    show m_exp_blush 01
    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve

    pt "Jodida loca del coño..."

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "Y bien [protname],"

    extend " ¿qué te ha parecido mi obra?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve

    menu afternoon04_MACBA_TxellHerArt_question:

        pt "¿..Todo lo expuesto en este museo es obra de esta tía?"

        "Excitante.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿Excitante?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Por qué...?"

            show m_exp_blush 01
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Tengo la sensación de que sabes mucho más de lo que cuentas."

            show m_exp_blush 02
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "No has creado todo lo que hay en esta galería por simple amor al arte,"

            p "o para pagar tus impuestos."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Algo me dice que es también tu modo de vida,"

            p "la raíz de tu curiosidad y tu pasión."

            jump afternoon04_MACBA_TxellHerArt_after

        "Enfermiza.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave -= 1

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿Por qué?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Porque se aleja de los convencionalismos tradicionales?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "¿Porque no hablo de practicar el sexo únicamente después del matrimonio y solo para procrear?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "¿Es que tienes pensado ingresar en una hermandad religiosa?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Cachondéate lo que quieras..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Pero no me parece muy normal que alguien se emperifolle de plástico negro por todo su cuerpo desnudo y sudoroso,"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "mientras una loca sádica y enfermiza"

            p "le esté dando con un látigo,"

            extend " o vete tú a saber qué..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Eso sin mencionar que todas las obras aquí expuestas giran en torno al sexo,"

            extend " pero al sexo retorcido..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            p "¡¿Es que no sabes disfrutar de una compañía agradable y normal?!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Normal..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Qué entiendes por \"normal\"?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "No me vengas con rollos psicoanalíticos ahora..."

            jump afternoon04_MACBA_TxellHerArt_after

        "Intrigante.":
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿Intrigante?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Por qué...?"

            show m_exp_blush 01
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
                
            p "Me hace preguntarme qué tipo de experiencias habrás vivido,"

            show m_exp_blush 02
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "para poderlas plasmar en algo tangible al compartirlas como obras de arte."

            jump afternoon04_MACBA_TxellHerArt_after

        "Entretenida.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Creo que nunca habían definido mi obra de forma tan hastiada"

            extend " y soporífera."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Bueno,"

            extend " es mi opinión,"

            p "no sé,"

            extend " no me ha parecido mala..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Pero si es con lo que te ganas la vida,"

            extend " me parece bien..."

            show m_exp_mouth sad_Talkingx12
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "¡Suerte que no te ha parecido mala pues!"

            tx "No sé qué hubieras dicho entonces..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿Es que no sabe aceptar una opinión...?"

            jump afternoon04_MACBA_TxellHerArt_after
            

label afternoon04_MACBA_TxellHerArt_after:

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    tx "Así que no sabes a qué me dedico,"

    extend " ¿verdad?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "¿No eres artista?"

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Lo soy,"

    extend " pero no es mi único oficio."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Hay algo que no entiendo,"

    p "viendo que ya tienes una proyección profesional bien encarrilada,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¿por qué vienes a clase de Ilustración?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "El saber no ocupa lugar,"

    tx "siempre me ha gustado aprender cosas nuevas,"

    tx "y quiero expandir mis habilidades artísticas."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Especialmente,"

    extend " en anatomía masculina."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "¿Hay algo de malo en ello?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "No..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Me da miedo preguntar lo siguiente..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "¿Cuál es tu otro oficio?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "¿De verdad quieres saberlo?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "No lo preguntaría si no me interesara..."
    
    pt "Tampoco es que me dejes ninguna otra opción..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Teniendo en cuenta lo que has visto hasta ahora;"

    tx "mi obra,"

    extend " y mi personalidad..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    tx "¿A qué dirías que me dedico profesionalmente?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    menu afternoon04_MACBA_TxellJob_question:

        pt "Si existiera el oficio, sería el de toca-cojones profesional, con tanta preguntita de las narices..."

        "Diseñadora de moda especializada en látex.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Aunque reconozco que el trabajo de {a=http://www.latexwiki.com/index.php?title=Atsuko_Kudo}Atsuko Kudo{/a},"

            extend " la mejor diseñadora de moda en látex,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "es excepcional,"

            extend " y es posible que, en alguna ocasión,"

            tx "pudiera llegar a llevar algún traje suyo en alguna gala o exposición,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            tx "no es realmente de mi gusto llevar látex fuera de las fantasías eróticas."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Creo que cubierta de un látex oscuro,"

            extend " ceñido al cuerpo,"

            extend " con el estilismo de una buena diseñadora,"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "no te quedaría nada mal..."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "De eso no te quepa la menor duda."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Pero digamos que me gusta mantener separados mis encuentros íntimos,"

            extend " mi trabajo,"

            extend " y mi vida personal."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Cuando entro en el juego de la seducción,"

            extend " me pongo una máscara,"

            tx "y esa máscara en parte,"

            extend " es el látex que me cubre el cuerpo desnudo."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Así que, aunque no me disguste para nada el diseño de {a=http://www.latexwiki.com/index.php?title=Atsuko_Kudo}Atsuko Kudo{/a},"

            tx "veo difícil que algún día pueda llevar una prenda suya,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "y mucho menos, ser yo quien la pueda diseñar."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt"Vamos..."

            extend " que no lo he acertado..."

            jump afternoon04_MACBA_TxellJob_definition

        "Escort.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ KnowTxellwasEscort_Cond = True

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "¿En serio me ves como una puta de lujo?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Bueno,"

            extend " yo no lo hubiera expresado así quizás..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Cómo, entonces?"

            tx "¿Acompañante?"

            extend " ¿Dama de compañía?"

            extend " ¿Trabajadora sexual para ricachones?"

            extend " ¿{a=https://es.wikipedia.org/wiki/Chica_de_compañía}{i}Call-Girl{/i}{/a}?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Caray..."

            extend " sí que te sabes maneras distintas de llamar esta \"profesión\"..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Es un trabajo."

            tx "El cual no muchas personas son capaces de hacer;"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "sea por ineptitud,"

            extend " o por las consecuencias que ello conlleva."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¿A qué te refieres?"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            tx "A veces ser una dama de compañía,"

            extend " no solo se limita a la intimidad de la alcoba,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "en ocasiones el cliente te pide que asistas a una boda,"

            tx "bautizo,"

            extend " fiesta,"

            extend " galería,"

            extend " o hasta un funeral."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Hay que saber mantener las apariencias sin destacar más de lo necesario o solicitado por el cliente."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Además,"

            extend " eso implica ser expuesta en grupos sociales de alto grado económico,"

            tx "si no sabes llevarlo bien,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "puede arruinar tu reputación"

            extend " y luego impedirte llegar a tener una vida \"normal\"."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "..."

            p "Me da la sensación de que conoces bastante bien el oficio..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Lo conozco así de bien,"

            extend " porque durante unos años fue una de mis profesiones para pagarme los estudios superiores."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Ah..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "¿Te desagrada que haya sido una puta de lujo?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            menu afternoon04_MACBA_TxellJob_Escort_question:

                pt "En realidad, esto explica muchas cosas..."

                "La verdad es que no me entusiasma la idea...":
                    call p_Help
                    $ pl.ch_pts("mp",-5)
                    $ DislikeTxellwasEscort_Cond = True

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    tx "¿Y qué más te da?"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "Puedes estar tranquilo,"

                    tx "que estos labios,"

                    extend " esta lengua,"

                    extend " estos pechos,"

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris down04
                    #show m_pupils down04a
                    show m_exp_eyebrows normal
                    with dissolve

                    tx "y especialmente este coño seco como el desierto,"

                    tx "no van a mancillar tu casto y virtuoso cuerpo."

                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    p "Tampoco te lo he pedido."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Ya,"

                    extend " pero está claro que tu polla, por lo menos,"

                    tx "tiene esa ilusión."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    p "¡¿Por qué no dejas de mirarme la polla?!"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "Me gusta observarlo todo,"

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "supongo que serán gajes del oficio..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    pt "Puta..."

                    jump afternoon04_MACBA_TxellJob_after

                "En realidad, creo que eso te hace más interesante aún.":
                    call p_Help
                    $ pl.ch_pts("mp",+2)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "¿Por qué?"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "¿Te crees que voy a poner en práctica lo aprendido contigo para que disfrutes de mi compañía gratuitamente?"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "Estoy seguro de que aprendiste también muchas cosas aparte de las que obviamente supongo que se te dan muy bien."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    #show m_pupils front02a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "..."

                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "Es evidente que sabes cómo tratar a las personas,"

                    extend " y si no voy mal encaminado,"

                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows serious
                    with dissolve

                    p "los estudios que te pagaste,"

                    extend " según mencionaste antes,"

                    p "muy probablemente eran sobre psicología"

                    extend " o filosofía..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "Hmm..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Eres agudo, [protname],"

                    extend " lo reconozco."

                    jump afternoon04_MACBA_TxellJob_definition

                "Sinceramente, me importa bien poco.":
                    call p_Help

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "No sé muy bien cómo tomarme este comentario..."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "Tómatelo como quieras,"

                    p "es tu vida,"

                    extend " no voy a juzgarte por ello."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "..."

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "Bah,"

                    extend " da igual,"

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "te lo contaré de todos modos..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    pt "¿Es que no me ha oído...?"

                    jump afternoon04_MACBA_TxellJob_definition
            

        "Hacker.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            jump afternoon04_MACBA_TxellJob_wrong

        "Psicóloga.":
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Erraste."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Pero por lo menos, no lo hiciste de forma miserable..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            pt "Mira tú,"

            extend " algo es algo..."

            jump afternoon04_MACBA_TxellJob_definition

        "Dominatrix.":
            call p_Help
            $ pl.ch_pts("mp",+2)
            $ inMACBAq += 1
            #$ TxellSlave += 1 # Not necessary on this case.

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "¿Tanto se me nota?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows normal
            with dissolve
            
            p "Tu conversación sobre el látex,"

            extend " tu aparente aprecio por la dominación,"

            p "y el hecho de que hagas tantas preguntas."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            tx "..." #Mirada seria

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..." #Sonrisa pícara.

            jump afternoon04_MACBA_TxellJob_definition

        "Directora de Arte en una empresa de diseño.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            jump afternoon04_MACBA_TxellJob_wrong

        "Directora de Arte de este museo.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            jump afternoon04_MACBA_TxellJob_wrong
    

label afternoon04_MACBA_TxellJob_wrong:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "No."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "No sé de dónde demonios has sacado esta idea..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    pt "No sé..."

    extend " tenía que probar..."

    jump afternoon04_MACBA_TxellJob_definition

label afternoon04_MACBA_TxellJob_definition:

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Soy {b}psicóloga-dominatrix{/b},"

    extend " especializada en conductas sexuales masculinas y de pareja."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Masculinas?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Pensé que tendrías más experiencia con mujeres..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Por mujeres siento atracción,"

    tx "y eso, en general, suele traer más bien problemas laborales."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    p "¿Y nunca te has sentido atraída por la esposa en una de las parejas que has tratado?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "La mayoría de las veces,"

    extend " especialmente cuando veo el idiota del marido con el que está casada o comprometida."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    p "¿Entonces...?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Sé separar el placer del trabajo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Además,"

    extend " como ya te he comentado,"

    tx "esa \"segunda piel\" ayuda."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Cuando entro en mi despacho,"

    extend " o me enfundo en mi traje de látex en la otra sala,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve

    tx "dejo de ser yo misma para ser otra persona,"

    tx "redirecciono mis fantasías para tratar sus problemas."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Y qué ocurre cuando ellos no comparten tus mismas fantasías?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "En primer lugar,"

    tx "hay un letrero bastante visible en el marco de mi puerta que pone \"Dominatrix\"."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Si eso no les queda suficientemente claro,"

    tx "que te sorprendería saber la de veces que no es así..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve

    tx "Suelo ser algo flexible según el caso,"

    tx "ya que en realidad,"

    extend " más allá del sexo,"

    tx "lo que realmente disfruto,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "es \"follarme las mentes\"."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 06
    show m_exp_piris front06
    #show m_pupils front05a
    show m_exp_eyebrows angryx01
    with dissolve

    p "¡¿Cómo?!"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Tranquilo,"

    extend " no voy con una sierra abriendo cráneos y extrayendo cerebros."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    pt "La verdad,"

    extend " es que de esta ya me lo imagino casi todo..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "En realidad es una expresión que oí por primera vez en la película {a=https://es.wikipedia.org/wiki/Martín_(Hache)}{i}Martín (hache){/i}{/a} y me encanta."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    tx "Te la recomiendo si no la has visto."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve

    p "..."

    show m_exp_blush 02
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "*Ejem*..."

    show m_exp_blush 01
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "Aún así,"

    extend " no sé muy bien si yo iría a una psicóloga que quiere follarme la mente,"

    pt "sea retóricamente"

    extend " o no..."

    jump afternoon04_MACBA_TxellJob_after

label afternoon04_MACBA_TxellJob_after:

    show m_exp_blush 00
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Por último,"

    extend " dime..."

    tx "¿Qué te parece este cuadro?"

    play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0

    scene black
    show afternoon04_paint inMACBA_Txell_Succubus:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 ypos 0.5
        easein_quad 25.0 zoom 0.5 xpos 0.5 ypos 0.5
        #xanchor 0.25 yanchor 0.25 zoom 1.5
        #easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    window hide dissolve
    pause
    
    #El cuadro muestra dos cuerpos desnudos uno encima del otro sin perspectiva uno con los ojos negros y el otro, el femenino con los ojos rojos y dientes afilados,
    #Rodeados de manos negras por todos lados.
    
    pt "¡¿Qué puñetas es esto?!"

    n "La figura aparentemente femenina de una monstruosidad peluda con piernas ecuestres,"

    n "dedos desfiguradamente longevos, con dos enormes cuernos al lado de dos orejas aparentemente élficas,"

    n "una enorme lengua que rodea su propio miembro mientras acaricia el interior de su vagina;"

    n "acompañada de varios cuerpos desnudos, uno encima del otro, sin aparente perspectiva;"

    n "el del centro con la concavidad de los ojos vacía y su boca carente de dientes."

    n "Todo la pintura envuelta por manos negras que surgen de la oscuridad,"

    n "como si intentaran entrar en el cuadro cuyo fondo parece ser una fogata."

    n "Sin mencionar lo que llama más la atención;"

    n "esos ojos brillantes de color rojizo en esa figura monstruosa."

    window hide dissolve
    pause

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows surprisex001:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve
    
    tx "¿Has oído hablar alguna vez sobre las criaturas mitológicas"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "que toman la forma de mujeres de gran sensualidad,"

    tx "y de una extrema belleza incandescente,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "que se cuelan en tu alcoba al reunirte con Morfeo,"

    tx "mostrándose en tus sueños y fantasías,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "para succionar tu semilla,"

    extend " tu alma,"

    extend " o tu propia existencia?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "Algo me suena..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Ah,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "¿Sí...?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Cómo se llama esta criatura?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
#########################################################
    
    if config.version <= "00.07.00": #You discover her name and presents you an strange art.
        
        call endupdatescript
    
#######################################################

    menu afternoon04_MACBA_CreatureName_question:

        pt "Definitivamente no se cansa..."

        "Íncubo.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Casi,"

            extend " pero no..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "En realidad se llama {a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a}."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Pero es lo mismo,"

            extend " ¿no?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "O sea,"

            extend " en el fondo son demonios,"

            p "que adoptan una forma humana,"

            extend " sea masculina o femenina."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Depende bastante de la fuente de la que bebas..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "¿Beber de una fuente?"

            extend " pero ¡¿qué dice?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Lo que está claro,"

            extend " es que la lengua los diferencia por sexos,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "y yo te he preguntado concretamente por el \"femenino\"."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Tiquismiquis de las narices..."

            jump afternoon04_MACBA_CreatureName_after

        "Vampiro.":
            call p_Help

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Un vampiro es,"

            extend " según el {a=https://es.wikipedia.org/wiki/Folclore}folclore{/a} de varios países;"

            tx "una criatura que se alimenta de la esencia vital de otros seres vivos,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "usualmente bajo la forma de {a=https://es.wikipedia.org/wiki/Sangre}sangre{/a},"

            extend " para así mantenerse activo."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "En la cultura europea y occidental,"

            extend " así como en la cultura global contemporánea,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "el arquetipo de vampiro más popular es el de origen {a=https://es.wikipedia.org/wiki/Pueblos_eslavos}eslavo{/a},"

            extend " es decir,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "el de un ser humano convertido después de morir en un {a=https://es.wikipedia.org/wiki/No_muerto}cadáver activo{/a}"

            extend " o reviviente depredador {a=https://es.wikipedia.org/wiki/Hematofagia}chupador de sangre{/a}."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Entonces lo he acertado..."

            extend " ¿No?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "No."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Aunque es cierto que guardan muchos puntos en común,"

            extend " sus diferencias son notables."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "En realidad podría tratarse de la misma criatura,"

            p "solo que en distintas culturas lo llaman de manera diferente..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 06
            show m_exp_piris front06
            #show m_pupils front05a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Es posible..."

            tx "Si es que realmente crees que el {a=https://es.wikipedia.org/wiki/Folclore}folclore{/a} se puede tomar como referencia de un pasado real."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¡Eres tú la que me estás sacando estos cuentos de fantasía!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "La criatura a la que yo me refería se llama \"{a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "Atrapasueños.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "No."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Un {a=https://es.wikipedia.org/wiki/Atrapasueños}atrapasueños{/a} o cazador de sueños,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "es un adminículo hecho a mano,"

            extend " cuya función consiste en filtrar los sueños de las personas."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "No tiene nada que ver con una \"criatura\"..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¿Estás segura de que no existe una criatura con ese nombre?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Me suena haber leído por ahí que se trata de un ser alto,"

            extend " negro,"

            extend " sin ojos,"

            p "y con una boca enorme con colmillos afilados..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Eso lo habrás leído en alguna {a=https://es.wikipedia.org/wiki/Leyenda_urbana}leyenda urbana{/a}..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            pt "Es posible, ahora que lo menciona..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Y, en todo caso,"

            tx "la criatura que mencionas no se llama así;"

            tx "tienen otro nombre."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿Tienen?"

            extend " ¿De qué está hablando?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "La criatura a la que yo me refería,"

            extend " se llama \"{a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "Súcubo.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Hmm..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Veo que tienes buena memoria..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "En efecto..."

            jump afternoon04_MACBA_CreatureName_after

        "Demonio.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Es de hecho,"

            extend " según las leyendas medievales occidentales,"

            tx "un {a=https://es.wikipedia.org/wiki/Demonio}demonio{/a} que toma la forma de una mujer."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "El problema es que llamar a esta criatura \"{a=https://es.wikipedia.org/wiki/Demonio}demonio{/a}\","

            tx "es como llamar {a=https://es.wikipedia.org/wiki/Pez}pez{/a},"

            extend " a una {a=https://es.wikipedia.org/wiki/Cetacea}ballena{/a}..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "En cierto modo,"

            extend " es un pez..."

            extend " ¿No?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "No."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Los peces son animales {a=https://es.wikipedia.org/wiki/Ectotermia}ectotérmicos{/a},"

            extend " con respiración por branquias"

            extend " y mayoritariamente ovíparos,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "con ciertas excepciones,"

            tx "como los {a=https://es.wikipedia.org/wiki/Rajiformes}rajiformes{/a},"

            extend " los {a=https://es.wikipedia.org/wiki/Chimaeriformes}quimeriformes{/a},"

            extend " o los {a=https://es.wikipedia.org/wiki/Selachimorpha}tiburones{/a}..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Una ballena,"

            extend " o también llamado {a=https://es.wikipedia.org/wiki/Cetacea}cetáceo{/a},"

            tx "es un mamífero {a=https://es.wikipedia.org/wiki/Eutheria}euterio{/a},"

            extend " completamente adaptado a la vida acuática."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "De hecho el nombre {a=https://es.wikipedia.org/wiki/Cetacea}cetáceo{/a}"

            extend " deriva del griego que significa \"monstruo marino\","

            tx "y fue acuñado por {a=https://es.wikipedia.org/wiki/Aristóteles}Aristóteles{/a}."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            tx "para referirse a los animales acuáticos dotados de respiración pulmonar."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Resumiendo..."

            extend " que no lo he acertado..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "No,"

            extend " erraste miserablemente."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "El nombre de la criatura a la que me refería es \"{a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "Esposa.":
            call p_Help
            $ pl.ch_pts("mp",-5)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "A ver si no..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "{i}Toman la forma de mujeres de gran sensualidad y de una belleza incandescente{/i}..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "¿Tú has visto esa misma mujer treinta años después?"

            p "¡Quién la ha visto!"

            extend " ¡y quién la ve!"

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "Por mi experiencia tratando parejas,"

            tx "el marido suele ser el que peor envejece."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "Eso es por lo que has dicho antes."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "¿Por lo que yo he dicho?..." 

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "{i}Se cuelan en tu alcoba,"

            extend " mostrándose en tus sueños y fantasías{/i},"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "\"para succionar tu semilla\","

            p "que tú puedes pensar,"

            extend " {i}se refiere al esperma...{/i}"

            p "¡Pero no!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Se refiere a la cartera,"

            extend " que anda que no la dejan vacía ni nada..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Ya te digo yo que así uno envejece muy rápido..."

            p "¡Succionándote el alma!"

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "¿Eso es humor catalán?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            p "..."

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx04
            with dissolve

            p "Mujer..."

            extend " que no sabes ni aceptar una broma,"

            p "qué poco sentido del humor,"

            extend " de verdad..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "Lo único que veo, es que con esa actitud,"

            tx "vas a morir abandonado,"

            extend " desgraciado,"

            extend " apaleado,"

            extend" y olvidado."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            pt "La que fue a hablar de \"actitud\"..."

            extend " la madre que la..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "Bahh..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Da igual..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "El nombre de lo que te estaba hablando se llama \"{a=https://es.wikipedia.org/wiki/Súcubo}súcubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "Suegra.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿Se supone que tiene que hacerme gracia?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Bueno,"

            extend " si le quitamos lo de \"belleza incandescente\"..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "¡¿Y lo de que se cuelan en tu habitación para tragarse tu semen?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¡¿Qué tipo de suegras has tenido tú?!"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "A ver..."

            extend " eso es metafóricamente hablando,"

            p "lo de colarse en tu \"alcoba\""

            extend " para \"mostrarse\" en tus sueños y fantasías..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Madres exageradamente marujas que no pueden evitar poner la oreja tras la puerta para escuchar a su hija follando con otro..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¡Eso me ha pasado!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "¿Con qué clase de mujeres te has acostado tú?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "En realidad la chica no estaba nada mal,"

            extend " era la madre que estaba un poco p´allá..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Supongo que estaría llamando a la policía al ver..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "¡que estabas abusando de su hija menor de edad!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¡Que no coño!"

            extend " ¡Si tenía la misma edad que yo!"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "¿Y esa edad cuál era?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Ahora que lo menciona..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Mira,"

            extend " da igual."

            tx "Que me estás sacando del tema..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿Qué tema?"

            pt "Si aún no sé a qué viene todo esto que me estás contando..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Estas criaturas se llaman \"{a=https://es.wikipedia.org/wiki/Súcubo}súcubos{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

label afternoon04_MACBA_CreatureName_after:

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Estos demonios poseen siempre el aspecto de una mujer de belleza extraordinaria,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "piel perfecta y cabello oscuro o rojizo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    tx "Posiblemente,"

    extend " el mismo aspecto que \"{a=https://es.wikipedia.org/wiki/Lilit}Lilith{/a}\","

    tx "Reina de la Oscuridad y la Noche,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "de quien se cree que descienden todos los demás {b}súcubos{/b}."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "{a=https://es.wikipedia.org/wiki/Lilit}Lilith{/a}..."

    extend " creo que se trata de la primera mujer en el Génesis del folclore judío,"

    pt "antes de que existiera Eva..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Se esconden tras esta atractiva fachada para conseguir atraer y tentar a los mortales que se cruzan en su camino."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Sus movimientos son ágiles y precisos."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    #show m_pupils right02a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "Su forma de caminar es muy seductora y cuentan con una gran presencia y carisma."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Aunque un espectador avispado podría saber que se trata de un demonio por ese destello en su mirada de oscuro y enfermizo deseo."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Tu mirada tampoco es que sea de niña inocente..."

    pt "aunque me imagino que no debe de ser por deseo hacia mí."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Hablan varios idiomas,"

    extend " por lo que no tienen problemas para entablar conversaciones y establecer nuevas relaciones sociales."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Podrían considerarse la compañía ideal si no fuese porque,"

    tx "en ocasiones,"

    extend " se dejan llevar y sacan su lado más lascivo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Los demonios súcubos no necesitan mostrarse agresivos y,"

    tx "además,"

    extend " rehúyen los conflictos."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "Eso sin mencionar que,"

    extend " en caso de necesidad,"

    tx "no dudarán en adoptar el papel de víctima o de damisela en apuros."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Incluso pueden enredar y poner a unos en contra de otros por simple diversión."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Lo dice como si inicialmente ella no me hubiera invitado a venir aquí solo para reírse de mi \"incultura\"..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Una vez tienen elegido al mortal procuran alejarse con él de la multitud,"

    tx "y entonces usan su capacidad de sugestión,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
        
    tx "muy parecida a la de los \"vampiros\","

    tx "para hacerle creer prácticamente cualquier cosa que deseen."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Ahora se me pone a hablar de vampiros?"

    pt "¿Pero de qué demonios me está hablando?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Cuando la víctima entra en ese estado hipnótico, pasa a ser atacada por el súcubo,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "que consume la energía de la víctima mientras mantienen relaciones sexuales."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Como si no hubiera mujeres que se aprovechan del momento íntimo de la alcoba,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    pt "para extraer algo que no es precisamente energía ni semen..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris left03
    #show m_pupils left03a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Estos demonios se nutren de la energía vital del mortal,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "energía que también les permite mantener ese aspecto joven y encantador."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Los más afortunados pueden acabar en un estado de inconsciencia,"

    extend " parecido al sueño profundo,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    tx "del que suelen despertar agotados,"

    extend " con depresión,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "y de haber tenido terribles pesadillas,"

    extend " que les dejan marcados de por vida,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "necesitando en muchos casos ayuda profesional."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Pero generalmente el súcubo suele excederse extrayendo energía,"

    tx "dando a su víctima el obsequio del sueño eterno."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Palmarla después de echar un polvo,"

    pt "hay maneras peores de morir..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Aunque no es habitual,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "en ciertas ocasiones los súcubos muestran su verdadero aspecto mientras mantienen relaciones con sus víctimas."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Ojos felinos,"

    extend " o, según otros reptilianos,"

    extend " que brillan en la oscuridad,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "una lengua de serpiente exageradamente larga,"

    tx "colmillos largos y afilados,"

    extend " alas como de murciélago,"

    extend " una cola..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Qué diablos me está describiendo?"

    extend " ¿Un dragón?"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Son atributos que suelen manifestarse cuando el súcubo pierde el control por el placer y el éxtasis."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Cuando ocurre esto,"

    extend " es porque su víctima no tiene ninguna posibilidad de escapar de su destino."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows normal
    with dissolve
    
    pt "Me imagino que sigue habiendo peores formas de ir al otro barrio,"

    pt "cierras los ojos,"

    extend " o lo haces a oscuras,"

    extend " y a disfrutar..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Aunque eso de que la acabes palmando,"

    extend " sin duda es una putada..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Bonita información de {a=http://www.seresmitologicos.net/angeles-demonios/sucubos-incubos}seresmitologicos.net{/a},"

    p "pero exactamente,"

    extend " ¿para qué diablos me cuentas todo esto?"
    
    play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0

    scene afternoon04_bg macba_room02

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth happy_Talkingx09:
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

    tx "Dime, [protname],"

    extend " ¿no ves algo extraño en Neus?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "¿Neus?"
    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04

    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    pt "Después de que su mordida convirtiera a mi amigo en tía..."
        
    pt "La verdad es que ya no sé qué pensar."

    pt "En realidad,"

    extend " ya no estoy seguro de nada..."

    show m_exp_blush 02
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Sí,"

    extend " la oscura morenita de ojos verde esmeralda y de piel suave que te roba el alma solo de mirarla."

    show m_exp_blush 03
    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Hombre..."

    extend " tú tienes mejor delantera..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Aunque con tanto interrogatorio,"

    extend " me pregunto si habrá descubierto lo que le ha ocurrido a Dídac..."

    show m_exp_eyebrows serious
    with dissolve
    
    pt "No,"

    extend " no tendría sentido que me hubiera acusado de haber quedado con una pelirroja si lo supiera..."

    show m_exp_eyebrows normal
    with dissolve
    
    pt "Aunque viendo lo retorcida que es esta mujer..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "¿Nunca le has visto un brillo extraño en sus ojos?"

    show m_exp_blush 01
    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "..."

    show m_exp_blush 00
    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    menu afternoon04_MACBA_NeusEyesShine_question:

        pt "¿A dónde quiere ir a parar?"

        "No, nunca he visto semejante cosa.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Ya..."

            extend " como si no supiera cuando alguien me engaña..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¡¿Para qué te iba a engañar?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Quizás,"

            extend " porque eres hombre,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "y te cuesta entender las cosas..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Tienes un problema;"

            p "Lo sabes,"

            extend " ¿verdad?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "¿Me estás diciendo que no has visto nada raro en ella?"

            jump afternoon04_MACBA_NeusEyesShine_after

        "Una vez me pareció ver que sus ojos cambiaban de color...": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Así que lo has visto..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Bueno,"

            p "pensé que habían sido imaginaciones mías,"

            extend " quizás..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Imaginaciones, dice..."

            jump afternoon04_MACBA_NeusEyesShine_after

label afternoon04_MACBA_NeusEyesShine_after:

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Lo que no he visto es que camine de forma {i}muy seductora{/i}"

    p "ni que tenga precisamente una {i}gran presencia y carisma{/i}..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Eso es porque quizás contigo no ha tenido necesidad de mostrarse de esa manera."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "O porque quizás te equivocas..."

    pt "pero cualquiera le lleva la contraria..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Ya sé que hace tiempo que conoces a Neus de la clase de Ilustración..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Pero desde el principio siempre habías prestado más atención a mis pechos que a su cara."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Debo aprender a disimular mejor..."

    pt "Pero con semejante delantera,"

    extend " realmente es difícil..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Dime, [protname],"

    extend " ¿cómo consiguió llamar tu atención para que ahora salgas con ella?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Toma preguntita..."

    extend " ¿Y ahora qué le respondo?"
    
    pt "Neus me dijo que no le contara a nadie lo que sucedió con Dídac después de morderlo,"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    pt "que existía el riesgo de que si alguien en el hospital,"

    extend " o donde fuera,"

    pt "se enterase de lo que le ha sucedido..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows surprisex001
    with dissolve
    
    pt "Dídac acabaría muerto."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    pt "Quizás fue solo una trola para mantenerme callado y debería haberlo llevado al hospital..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Pero si no es una mentira,"

    extend " Dídac podría morir..."

    menu afternoon04_MACBA_TellTruth_question:

        pt "¿Se lo cuento?"

        "Si te lo cuento, ¿qué garantías tengo de que no se lo contarás a nadie?":
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            tx "Ya veo..."

            jump afternoon04_MACBA_TellTruth_after

        "Sencillamente me propuso ir a tomar algo y realmente me cayó bien, no tiene más misterio.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TellTruth_after

        "Lo siento, no puedo contártelo.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TellTruth_after

label afternoon04_MACBA_TellTruth_after:

    $ afternoon04_MACBA_TxellTruth_Cond = True

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Hizo algo que te hizo romper la ilusión de la realidad en la que vivimos."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    pt "¿Qué puñetas dice ahora?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Experimentaste algo que te hizo dudar de si lo que viste fue real o no."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "Te mostró algo que no encaja en las leyes físicas o naturales en las que hemos sido educados."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Casi como si se tratara de una novela,"

    extend " película,"

    extend " o sueño."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    p "¿Estás insinuando que podría haber afectado mi mente para que me imaginara cosas que no son reales?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Hasta cierto punto no sería descabellado pensar en esa posibilidad..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve 
    
    tx "A veces no somos conscientes de que seguimos durmiendo,"

    tx "incluso cuando soñamos que despertamos."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Nuestras sensaciones están limitadas por nuestro consciente."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Me está hablando de {a=https://es.wikipedia.org/wiki/The_Matrix}Matrix{/a} o de {a=https://es.wikipedia.org/wiki/Inception}Inception{/a}?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Pero, si cuando despiertas,"

    tx "sigue existiendo ese cambio de la realidad,"

    tx "entonces no es una simple ilusión."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Y aun así,"

    extend " las ilusiones no son siempre lo que parecen."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Ya me está recordando a Neus con su charlatanería sin sentido..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Dime, [protname],"

    extend " ¿Es esa pelirroja de los grandes almacenes, Dídac convertido en mujer?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "¡Es astuta la muy zorra!"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    p "¿Qué...?"

    p "¿Qué te hace pensar eso?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Varias cosas,"

    extend " pero tu reacción confirma mis dudas."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Oye,"

    extend " una cosa..."

    p "Hay algo que no entiendo."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "¿Hmm?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Si toda esta historia es real..."

    p "Digamos que me creo todo lo que me has contado,"

    p "sobre brujas,"

    extend " demonios,"

    extend " y ninfómanas reptilianas..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "¿Sí...?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "Digo yo que viviendo en pleno siglo XXI,"

    extend " la gente ya conocería toda esta fauna..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Vamos,"

    extend " digo yo,"

    p "que la gente que supiera de su existencia,"

    p "los habría expuesto a la luz,"

    extend " saldría en las noticias,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    p "¡Joder!"

    p "¡saldría en alguna fotografía de alguien de {i}Instagram{/i} o {i}Facebook{/i},"

    extend " con los dichosos {a=https://es.wikipedia.org/wiki/Autofoto}{i}selfies{/i}{/a}!"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Si tú supieras la verdad,"

    tx "¿se lo explicarías a alguien?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "¿Por qué no?"

    p "¡¿Tú no lo harías?!"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Entonces..."

    extend " ¿porqué no me lo has comentado en ningún momento?"

    tx "O sencillamente," 

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "¿Por qué no has acudido a la policía?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Bueno..."

    p "quizás fue por temor,"

    extend " quizás por ignorancia..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "O quizás por amenaza."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Pero..."

    extend " si de verdad existieran dichas criaturas {b}bizarras{/b},"

    p "la gente en realidad estaría en peligro..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Especialmente si no saben ni que existen."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "¿Verdad?"

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Si fueras una oveja en un rebaño de cien,"

    extend " y supieras que existe un lobo,"

    tx "que una vez al año,"

    extend " se lleva a una de vosotras."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Avisarías al resto del peligro?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "¿Qué sentido tendría esconderlo?"

    p "Tarde o temprano te podría tocar a ti..."

    extend " ¿No?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Si tú supieras que existe,"

    extend " te asegurarías de alejarte tanto del peligro como pudieras..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "A riesgo de que mataran a otra..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Ley de supervivencia."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Ley del egoísta psicótico."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Qué ocurriría si las avisaras?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Habría terror,"

    extend " pánico,"

    tx "todas viviríais con miedo."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Y el lobo seguiría viniendo a llevarse su parte."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Solo que quizás con más violencia."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Qué arreglarías?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Pues que quizás nos levantaríamos en armas para luchar,"

    p "como centenares de veces ha ocurrido en la historia."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Luchando unos contra otros,"

    tx "no contra algo que ni siquiera sabes que existe..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Luchando contra algo a lo que,"

    extend " si se te ocurriera algún día mencionar la posibilidad de que existe,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "la gente te respondería con mofas,"

    extend " risas,"

    extend " e insultos."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    tx "Casi como si te pusieran un velo delante de tus ojos constantemente,"

    tx "para que dejaras de mirar allí,"

    extend " en la oscuridad."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Se trataría de dar pruebas de que lo que cuento existe."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "¿Tienes pruebas para demostrar lo que has experimentado?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Cuándo has visto que una oveja luche contra un lobo?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "{i}BEeeeee...{/i}" # Sound imitating a sheep. *imitando oveja*

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "No somos ovejas..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "¿De verdad crees eso?"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 06
    show m_exp_piris front06
    #show m_pupils front05a
    show m_exp_eyebrows angryx01
    with dissolve

    play sound "audio/characters/txell/laugh02.ogg"
        
    #tx "*risilla odiosa femenina* Jajaja"
    tx "*Jajaja*" # hateful female gigle-laugh

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Qué inocente..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    pt "¿Por qué sigo aguantando a esta tía?..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¿Y qué me dices de nuestra historia?"

    p "Habría escritos,"

    extend " ¡pruebas!"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
       
    p "Algo más que simple entretenimiento folclórico sobre todo esto..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "A menos que quemaran dichas pruebas y libros por orden \"divina\","

    tx "en tiempos oscuros en los que el pueblo no sabía ni leer..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows normal
    with dissolve
    
    pt "Sin duda se está refiriendo a los tiempos de la {a=https://es.wikipedia.org/wiki/Inquisición_española}santa inquisición{/a}..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Hay cosas de nuestro pasado escondidas bajo mantos de sangre y fuego que es mejor no destapar..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Sinceramente,"

    extend " esta conversación me está resultando muy surrealista..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Y sin embargo, aquí sigues,"

    extend " escuchándome,"

    extend " y argumentándome."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Como te he dicho,"

    extend " sigo aquí por simple curiosidad."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Por lo que te he comentado antes,"

    tx "has visto"

    extend " \"algo\""

    extend " que te ha apartado ese velo de tus ojos,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "y ahora te haces preguntas,"

    tx "que no tienen una respuesta sencilla,"

    extend " ni agradable."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve

    tx "Si de verdad tienes tanta curiosidad,"

    tx "podría enseñarte más sobre todo esto en mi taller,"

    show m_exp_blush 01
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "si estás libre mañana por la tarde a la misma hora que hoy."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Ahí es donde guardo las cosas que pueden darte una mejor idea de lo que te estoy contando,"

    tx "si es que te interesa..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "¿Taller?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¿A qué te refieres con \"taller\"?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Mi oficio,"

    extend " aparte del que estás observando en esta galería,"

    tx "es el de \"sexóloga-dominatrix\"."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Básicamente trato con maridos infieles,"

    extend " impotentes,"

    tx "o parejas que han perdido la pasión."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "¿Acaso tienes algún problema de impotencia que quieras discutir?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "¡¿Euh?!"

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
       
    p "¡Cla-"

    extend "Claro que no!"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils down03a
    show m_exp_eyebrows suspiciousx01
    with dissolve
    
    tx "No,"

    extend " yo tampoco lo creo,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris down03
    #show m_pupils down03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "salta a la vista..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Entonces por qué pregunta?"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Esta noche vas a tener otra cita con Neus,"

    extend " ¿verdad?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Sí..."

    extend " así es..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Te daré un consejo,"

    extend " hombretón..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Cuídate de no tener un orgasmo cerca de ella."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Quizás no vivas para contarlo..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "¿Lo dice en coña?,"

    extend " ¿es por celos?,"

    pt "¿o lo dice en serio?"

    ## ADD HERE the new sene with the cloroform. NOT FINISHED

    call afternoon04_MACBA_TellTruth_anestesic

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Si me disculpas tengo otros asuntos que atender,"

    tx "si te interesa la oferta,"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front06a
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "por lo visto,"

    extend " ya sabes mi número."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Suerte esta noche."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "No tengo duda de que la vas a necesitar..."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pause 0.2

    scene afternoon04_macba_whisper_bg
    if p_prot_analgesic == "refused":
        show afternoon04_macba_txellwalkingaway briefcase:
            subpixel True
            zoom 1.0 xanchor 0.2 yanchor 0.85 #Feet
            easein_quad 20.0 zoom 1.0 xanchor 0.15 yanchor 0.4 #Ass
    else:
        show afternoon04_macba_txellwalkingaway normal:
            subpixel True
            zoom 1.0 xanchor 0.2 yanchor 0.85 #Feet
            easein_quad 20.0 zoom 1.0 xanchor 0.15 yanchor 0.4 #Ass
    with fade

    window hide dissolve
    pause
    
    n "Sin que apenas te dé tiempo a darle una respuesta,"

    n "ves cómo se retira de tu presencia con un movimiento de caderas realmente hipnótico."

    show afternoon04_macba_txellwalkingaway:
        subpixel True
        easein_quad 15.0 zoom 0.8 xanchor 0.28 yanchor 0.02 #Head

    window hide dissolve
    pause

    pt "¡¿Acaso sabe que le estoy mirando el trasero?!"

    window hide dissolve
    pause

    scene afternoon04_bg macba_room02
    with fade

    pt "Posiblemente no le atraigan los hombres,"

    pt "pero sin duda, disfruta seduciéndolos de forma enfermiza..."
    
    pt "Mi amigo convertido en chica que parece ser una ninfómana,"

    pt "la bruja friki que me chantajea,"

    pt "y esta loca del coño..."
    
    pt "¡¿Por qué no puedo conocer a una chica normal?!"
    
    p "..."
    
    pt "Será mejor volver a casa y prepararme para la cita de esta noche..."
    
    jump night04_restaurant
    
#############

    #(Luego estaría bien que en la cita con Neus se tratara el tema de que has quedado con la chica tetuda 
    #y Neus te expliqué lo que ocurrió con ella).




#################################################################################
###########################################################################################
#################################################################################
###########################################################################################
#################################################################################
###########################################################################################
#################################################################################
###########################################################################################
#################################################################################
###########################################################################################
#################################################################################
###########################################################################################


label afternoon04_MACBA_TellTruth_anestesic:
        # pt "¿Lo dice en coña?,"
        # extend " ¿es por celos?,"
        # pt "¿o lo dice en serio?"


    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "Antes de que te vayas,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    tx "por favor,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    tx "espera aquí un segundo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    p "¿Qué...?"

    scene afternoon04_bg macba_room02
    with dissolve

    n "Sin esperar tu respuesta, la ves alejarse hasta desaparecer tras una puerta en la misma sala donde estás."

    n "De ahí reaparece con un maletín negro."

    pt "¿Qué demonios llevará ahí dentro?"

    show m_bodynew relax_03:
        mtxell_body_ontheright_position

    show m_exp_blush 01:
        mtxell_exp_ontheright_position
    show m_exp_mouth sad_Talkingx03:
        mtxell_exp_ontheright_position
    show m_exp_eyes 04:
        mtxell_exp_ontheright_position
    show m_exp_piris front04:
        mtxell_exp_ontheright_position
    show m_exp_eyebrows serious:
        mtxell_exp_ontheright_position

    show m_exp_hair_front:
        mtxell_exp_ontheright_position
    with dissolve

    tx "Toma."

    show m_exp_mouth sad_Talkingx003
    with dissolve

    tx "Ábrelo."

    show m_exp_mouth sad_Silentx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx02
    with dissolve

    p "¿Qué hay aquí dentro?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Algo que espero que no necesites usar."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris down05
    show m_exp_eyebrows sadx01
    with dissolve

    n "Decides abrirlo."

    show afternoon04_macba_briefcase:
        subpixel True
        truecenter
        zoom 1.5
        ease 10.0 zoom 0.5
    with fade

    p "¿Qué...?"

    n "En su interior encuentras una mordaza de bola agujereada,"

    n "una botella deportiva de plástico adjunta a una pajita larga,"

    n "otra botella pequeña y oscura sin ningún tipo de etiqueta,"

    n "un pañuelo y lo que parecen cuatro esposas de cuero,"

    n "cada una de ellas conectadas a una larga cadena de hierro"

    n "las cuales también terminan en otras esposas, pero estas hechas del mismo metal que las cadenas."

    pt "¿Esto no será...?"

    hide afternoon04_macba_briefcase

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    tx "Lo que hay en el botellín oscuro es {a=https://es.wikipedia.org/wiki/Cloroformo}cloroformo{/a}."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    pt "¿Qué...?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Te aconsejo que no lo uses con Neus,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "no creo que eso fuera una buena idea."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    pt "¿Entonces...?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    tx "Me imagino que te habré resultado una insoportable {a=https://es.wikipedia.org/wiki/Esnob}esnob{/a}."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Y en cierto modo no te equivocas."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Pero una de las razones por las que he intentado llevar al límite tu paciencia"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "es porque quería ver como reaccionas ante una situación estresante"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "y hasta qué punto puedes pensar en frío."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Debo reconocer que desconozco la verdadera situación de tu compañero de piso,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "y con sinceridad, espero equivocarme,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "pero cabe la posibilidad de que tengas que recurrir a esto."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    pt "¿Qué sabe realmente sobre Dídac?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows serious
    with dissolve

    tx "Deberás usar todo el líquido del pote y darte prisa, pues no tardará en evaporarse."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Es especialmente importante que tenga la boca cerrada"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y que lo inhale por la nariz en lugar de la boca,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "no quieres que muera ahogado por su propia lengua."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Pero ten en en cuenta que el cloroformo no funciona como en las películas,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows sadx02
    with dissolve

    tx "no surte efecto en segundos,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx05
    with dissolve

    tx "si no en minutos."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    tx "Deberás mantener tu mano pegada en su nariz durante al menos unos cuatro o cinco minutos"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "mientras intenta gritar y golpearte para liberarse de ti."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Estoy segura que con tu masa muscular tendrás más suerte de la que tuve yo."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx05
    with dissolve

    pt "¿De qué está hablando?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    tx "Una vez pierda la conciencia,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "aparta el pañuelo de inmediato y llévalo a un lugar dónde puedas encadenarlo con seguridad."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "Es mejor que uses el extremo hecho de cuero para que no sufra tanto la piel con el roce."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    tx "Estas cadenas tienen la longitud para ser usadas en una cama de matrimonio,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "pero siempre puedes voltear la cadena en torno a la pata de la cama para que no tenga tanta libertad."

    show m_exp_mouth sad_Talkingx05
    with dissolve

    tx "Hay que ajustarla para que no goce de demasiada libertad y haga de las suyas,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    tx "pero la suficiente para que pueda estar horas inmóvil sin que le perjudiques los músculos y tendones."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Si no usas una cama, asegúrate de dejarlo lo más cómodo posible con varios cojines."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pero si la usas, no le pongas cojín."

    show m_exp_mouth sad_Talkingx04
    with dissolve

    tx "es mejor que la cabeza esté en perpendicular con el resto del cuerpo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Y para qué sirven la mordaza y el botellín deportivo con pajita?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Una persona con un índice de masa corporal normal podría sobrevivir más de un día sin beber agua,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "pero si no quieres que tenga problemas de hígado o derivados,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    tx "es mejor que lo mantengas hidratado."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "No querrás que grite demasiado alertando a tus vecinos,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "¿no?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Por eso la mordaza tiene agujeros,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "para que pueda pasar el agua a través."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Solo asegúrate de cerrar bien las ventanas."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "¿Está hablando en serio?"

        "¿Y si tiene que ir al baño?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            tx "Me temo que tendrá que dejar la cama empapada,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows sadx01
            with dissolve

            tx "el artilugio que tengo para esta emergencia no sirve en mujeres."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "Por tu propio bien, y el suyo,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "espero que no lo dejes ahí demasiado tiempo."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            menu:

                pt "¿Qué clase de psicópata es esta mujer?"

                "¿Lo usaste para violar a alguien?":
                    call p_Help

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "¡No seas idiota!"

                    show m_exp_mouth sad_Silentx08
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows angryx06
                    with dissolve

                    p "..."

                    show m_exp_mouth sad_Talkingx02
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows sadx05
                    with dissolve

                    tx "No..."

                "¿Lo usaste contra alguien?":
                    call p_Help

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx04
                    with dissolve

                    tx "Por lo menos lo intenté..." 

                "<No decir nada>":
                    call p_Help

                    pass

        "<No decir nada>":
            call p_Help

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx04
            with dissolve

            tx "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "En su tiempo lo compré en el mercado negro"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows angryx04
    with dissolve

    tx "precisamente para defenderme de cierto ex-cliente que no dejaba de atosigarme."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¿No hubiera sido más práctico usar un espray de pimienta?"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Me seguía a todas partes,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx04
    with dissolve

    tx "me llamaba a altas horas de la noche,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx05
    with dissolve

    tx "me jaqueó el móvil varias veces,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx06
    with dissolve

    tx "y hasta acosaba a las chicas con las que quedaba para que no me volvieran a ver."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx07
    with dissolve

    tx "No quería alejarle temporalmente,"

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx06
    with dissolve

    tx "sino darle un escarmiento para que ni se le ocurriera volver a acercarse a mi."

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx06
    with dissolve

    p "Joder..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¿Y por qué no lo denunciaste?"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx06
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx06
    with dissolve

    tx "En su momento pensé que no necesitaba involucrar a las autoridades para defenderme de ese maldito energúmeno."

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    p "No parece que la cosa terminase bien..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Por eso te he dicho que no funciona como en las películas."

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "Por lo que dices,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows sadx04
    with dissolve

    p "esto pasó hace años,"

    extend " ¿no?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Unos cuantos."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿Esto no tiene data de caducidad?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Sí."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "En parte,"

    extend " por eso te he dicho que lo uses solo si no tienes ninguna otra opción."

    tx "Ah..."

    tx "Y por si no había quedado claro."

    tx "Yo nunca te he ofrecido este maletín."

    tx "Ahora es cosa tuya."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    tx "O simplemente devuélvemelo."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve


    menu:

        pt "¿Tan mal estará Dídac para que vaya a necesitar esto?"

        "¿Y qué te hace pensar que lo vaya a necesitar?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Llámalo intuición."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pt "Ya,"

            extend " y una mierda."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows sadx01
            with dissolve

            menu:

                pt "¿Y a ella qué le importe lo que le pase a Dídac?"

                "¿Desde cuando te preocupas tanto por mi?":
                    call p_Help

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    pause 0.2

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "No eres tú quien me preocupa."

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows suspiciousx03
                    with dissolve

                    p "¿De Neus?"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows normal
                    with dissolve

                    tx "No."

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows sadx04
                    with dissolve

                    tx "Te aseguro que ella no necesita de mi protección."

                    show m_exp_mouth sadbiting_Silentx04
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx03
                    with dissolve

                    pt "¿De Dídac?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "No te equivoques,"

                    show m_exp_mouth sad_Talkingx005
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "no hago esto para ayudarte a ti o nadie en particular,"

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows angryx02
                    with dissolve

                    tx "simplemente me asquea que la gente sea usada contra su voluntad."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows normal
                    with dissolve

                    tx "Si puedo hacer algo para impedir que eso ocurra,"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "no me importa a quien esté ayudando."

                "...":
                    call p_Help
                    pass

        "...":
            call p_Help
            pass

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "¿Y cómo sé que no me está tendiendo una trampa?"

        "Te prometo que lo usaré solo como último recurso.":
            call p_Help

            $ p_prot_analgesic = "accepted"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal
            with dissolve

            p "Te lo prometo."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx03
            with dissolve

            tx "Honestamente,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx04
            with dissolve

            tx "espero que no tengas que usarlo."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx03
            with dissolve

        "<Devolverle el maletín>":
            call p_Help

            $ p_prot_analgesic = "refused"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Agradezco el gesto,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "pero no lo necesito."

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows sadx02
            with dissolve

            tx "Eso espero."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx03
            with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    tx "Bien..."

    return

        # tx "Si me disculpas tengo otros asuntos que atender,"
        # tx "si te interesa la oferta,"
        # tx "por lo visto,"
        # extend " ya sabes mi número."