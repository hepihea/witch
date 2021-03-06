
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
    
    #La chica est?? fumando un cigarrillo largo. #NOT FINISHED
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

    
    pt "Cuando me dio su n??mero de tel??fono,"

    pt "parec??a mucho m??s simp??tica..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    n "En realidad a??n faltan escasos minutos para que sean las tres de la tarde."
    
    n "La plaza delante del emblem??tico edificio de Richard Meier se encuentra frecuentada por un considerable n??mero de {i}skaters{/i},"
    
    n "as?? como tambi??n de un n??mero considerable de adolescentes comi??ndose el almuerzo en peque??os {i}guettos{/i}."
    
    p "..."
    
    pt "??No ten??a los ojos de otro color?"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Y bien,"

    extend " ??has comido?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "Euh,"

    extend " no..."

    p "No he almorzado a??n."
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Quiz??s deber??a hab??rtelo dicho antes,"

    extend " yo s?? he comido ya."
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Toma,"

    extend " c??mete este s??ndwich."

    gm "No es mucho,"

    extend " pero te bastar?? por ahora."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_sandwich_question:
        
        pt "??Me est?? tratando como a un perro?"
        
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
    
    gm "??Te gustan los museos?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_LikeMuseums_question:
        
        pt "Lo que s?? s??... es que no ser??a mi primera opci??n para una {b}primera cita{/b}."
        
        "La verdad es que me aburren.":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
                  
            jump  afternoon04_LikeMuseums_boring
        
        "??Me encantan!":
            
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
    
    gm "Ni que tuvieras ocho a??os..."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Qu?? simpat??a desprende esta mujer..."
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
    
    #NOT FINISHED
            
label afternoon04_LikeMuseums_boring:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Supongo que pedirle algo de reflexi??n,"

    extend " estudio,"

    extend " y cultura,"

    gm "a un mont??n de testosterona con patas,"

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
    
    pt "No est?? siendo para nada la misma de ayer..."

    pt "??Es bipolar,"

    extend " o qu?? pasa?"
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
    
    #NOT FINISHED
    
label afternoon04_LikeMuseums_Depend:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Depende de si el museo es de cera o del Bar??a,"

    extend " ??no?"
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "..."
    
    menu afternoon04_waxbar_question:
        
        pt "??Me est?? provocando?"
        
        "??Qu?? tienes en contra del Museo de Cera de Barcelona?":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
                  
            jump  afternoon04_waxbar_waxbcn
        
        "??Qu?? tienes en contra del Museo del F??tbol Club Barcelona?":
            
            call p_Help
            
            $pl.ch_pts("mp",-1)
            
            jump  afternoon04_waxbar_fcbcn
            
        "La verdad es que no me gusta ninguno de los dos...":
            
            call p_Help
                
            $pl.ch_pts("mp",+1)
            
            jump  afternoon04_waxbar_none
            
        "??Por qu??? ??Son los ??nicos que conoces?":
            
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
    
    gm "Recuerdo cuando era peque??a."
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    #show m_pupils right02a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Era pasear por la rambla,"

    gm "pasar justo delante,"

    extend " y querer recorrer ese callej??n para llegar al fondo y ver a Superman y C3-PO,"
    
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

    extend " y recorrer sus estancias llenas de decoraciones m??gicas,"
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows serious
    with dissolve
        
    gm "estatuas memorables,"

    extend " historia,"

    extend " cultura,"

    extend " y m??sica ambiente."
    
    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Tambi??n recuerdo haberme acercado hace un par de a??os,"

    extend " siendo ya mayorcita."
    
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 06
    show m_exp_piris front06
    #show m_pupils right05a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "No paramos de re??r en todo el rato."

    gm "Re??amos de lo mal hechas que est??n,"
    
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

    extend " puedes saber a qui??n se refieren,"
    
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "y aun as??, es dif??cil encontrar el rostro de esas personas reflejado en la figura."
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Lo ??nico realmente interesante es la antig??edad del edificio,"

    gm "c??mo est??n adornadas algunas estancias,"
    
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
    
    gm "El cual no ha cambiado en veinte a??os,"

    gm "pero sigue siendo igual de m??gico."
    
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris left04
    #show m_pupils left04a
    show m_exp_eyebrows sadx01
    with dissolve
    
    pt "No me da la sensaci??n de que odie el lugar,"

    pt "sino m??s bien como si le entristeciera un lugar que anta??o am?? tanto."
    
    jump afternoon04_LikeMuseums_MuseumMoreVisited
            
label afternoon04_waxbar_fcbcn:

    $ afternoon04_waxbar_fcbcn_Cond = True
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "??Qu?? tengo en contra de una disciplina deportiva que se ha convertido en el circo romano moderno,"
    
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "donde veintid??s ni??atos millonarios chutan un bal??n,"

    gm "para que millones de espectadores c??modamente sentados en sof??s o en bares,"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "la mayor??a de los cuales suelen ser cuarentones barrigudos,"

    gm "con una birra en una mano"

    extend " y un cigarro en la otra,"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "mientras despotrican a esos chavales por qu?? no corren m??s con los millones que cobran?..."
    
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
    
    gm "Cualquier multitud movida por una idea tan b??sica como unos colores,"

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
    
    p "El deporte es mucho m??s que eso;"

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
    
    gm "??Eso crees?"
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Entonces,"

    gm "el b??squet,"

    extend " el balonmano,"

    extend " el rugby,"

    extend " el waterpolo,"

    extend " el hockey,"

    extend " el f??tbol femenino..."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "??No son deportes que tratan los mismos valores?"
    
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
    
    gm "??Qu?? gritan los aficionados cuando pierden un partido importante, o una liga?"
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Si han jugado mal,"

    extend " se les critica,"

    p "pero hay veces en los que el aficionado ha dado su apoyo."

    p "??No me jodas!"
    
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

    extend " o alg??n jugador,"

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
    
    gm "El f??tbol es un negocio,"

    gm "como lo es la comida r??pida,"

    extend " o la telebasura."
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Un servicio simple de entender,"

    gm "que ofrece adicci??n,"

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
    
    gm "??Cu??l dir??as que es el museo m??s visitado de Catalu??a?" # Museo FC Barcelona.
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_MuseumMoreVisited_question:
        
        pt "Creo que el Prado est?? en Madrid..."
        
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
            
            gm "Aunque tampoco sea santo de mi devoci??n,"
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "lo que me parece triste es que el m??s visitado sea precisamente el del F??tbol Club Barcelona."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Para que te hagas una idea del nivel cultural general de este pa??s."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "..."
                  
            jump  afternoon04_LikeModernArt
        
        "El Museo de Dal??.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "Aunque sigo creyendo que {a=https://es.wikipedia.org/wiki/Salvador_Dal??}Dal??{/a} fue un payaso vendido a los medios durante la mayor parte de su vida,"
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 02
            show m_exp_piris right02
            #show m_pupils right02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "reconozco que su arte tiene algo especial que no he sabido ver en casi ning??n otro artista,"
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "y que, sin duda,"

            extend " ten??a un talento especial."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "L??stima que se echara a perder con {a=https://es.wikipedia.org/wiki/Gala_Dal??}Gala{/a}..."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Pero no,"

            extend " no es el museo m??s visitado de Catalu??a,"

            gm "en realidad lo es el {a=https://es.wikipedia.org/wiki/Museo_del_F??tbol_Club_Barcelona}museo del F??tbol Club Barcelona{/a}."

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
            
        "El Museo del F??tbol Club Barcelona.":
            
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

            extend " as?? es."
            
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

            extend " cuando te fijas en el desinter??s que produce sobre otras cosas m??s importantes,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "el simple hecho de que sea \"el museo\" m??s visitado,"

            gm "cuando no se expone ninguna obra cultural o art??stica..."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "Me produce n??useas,"

            extend " y un asco profundo,"

            gm "en esta putrefacta sociedad afectada por la idiocracia."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Me imagino que esta chica debe de ser la alegr??a en las fiestas..."
            
            jump  afternoon04_LikeModernArt
            
        "El Born Centre Cultural.":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
                
            gm "Es un espacio polivalente de acceso al p??blico con una extensa programaci??n"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "que tiene el objetivo de invitar a la reflexi??n sobre el pasado,"

            gm "presente,"

            extend " y futuro de Barcelona;"

            gm "y de hecho, de Catalu??a en general."
            
            show m_exp_mouth sad_Talkingx001
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Pero no,"

            extend " no es el museo m??s visitado de Catalu??a,"

            gm "en realidad lo es el {a=https://es.wikipedia.org/wiki/Museo_del_F??tbol_Club_Barcelona}museo del F??tbol Club Barcelona{/a}."
            
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
            
            pt "No s?? si es que odia el f??tbol en general,"

            pt "o sencillamente es una amante incondicional de la cultura y el arte..."
            
            jump  afternoon04_LikeModernArt

label afternoon04_LikeModernArt:
    
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    gm "??Te gusta el arte contempor??neo?"
    
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
        
        pt "Llamas arte moderno a algo que ya tiene m??s de medio siglo..."
        
        "Aunque lo conozco, prefiero el arte figurativo cl??sico...":
            
            call p_Help
                
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "??Sabes cu??l era el prop??sito principal de los artistas en la antig??edad?"
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Crear obras de arte..."

            p "Como siempre ha sido,"

            extend " ??no?"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Te crees que exist??an centenares de museos como hoy en d??a,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "donde el p??blico puede acceder para contemplar esas obras,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "en una sociedad que se mor??a de peste y hambre por las calles?"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Donde los ni??os eran explotados,"

            gm "donde no exist??a la escuela,"

            gm "donde la gente no sab??a ni leer,"

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
            
            gm "que b??sicamente sol??an ser gente noble o adinerada que ped??a que se le hicieran retratos."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Porque en esa ??poca no exist??a la fotograf??a."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "??Pero hay obras de arte que van m??s all?? del simple retrato!"
            
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
            
            gm "Porque en esa ??poca tambi??n exist??a gente a la que le sobraba el dinero de forma escandalosa."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Pero eso no quita que la mayor parte de las obras que se hicieron antes de la ??poca de la fotograf??a,"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "ten??an el prop??sito de satisfacer los deseos y la demanda de un solo cliente."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo Davinci{/a} trabaj?? para los {a=https://es.wikipedia.org/wiki/M??dici}M??dici de Italia{/a}."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Miguel_??ngel}Miguel ??ngel{/a} trabaj?? para el mism??simo {a=https://es.wikipedia.org/wiki/Ciudad_del_Vaticano}Vaticano{/a}."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Claro que ambos tuvieron su \"cierta\" libertad art??stica debido a su gran talento,"

            extend " pero aun as??,"
            
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

            extend " respond??an a simples \"encargos\"."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No representaban lo que realmente quer??an expresar,"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "su arte estaba sujeto a las ??rdenes de un cliente adinerado y exigente."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "????Acaso hoy en d??a los artistas no ganan dinero con sus obras como anta??o?!"
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "La diferencia es que, hoy d??a,"

            gm "el cliente va a ver la obra que el artista ha hecho,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "no exige al artista qu?? obra quiere que haga."
            
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
            
            gm "Esa es tu opini??n."
            
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve
            
            pt "Resume m??s de tres mil a??os de historia del arte en un solo argumento y se queda tan ancha..."
                  
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
            
            gm "Expl??cate."
            
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
            
            p "??ser??n tambi??n reconocidos como grandes maestros dentro de trescientos a??os?"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "??Crees que {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Picasso{/a} ser?? olvidado?"
            
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
            
            p "Despu??s de {a=https://es.wikipedia.org/wiki/Marcel_Duchamp}Duchamp{/a}, qued?? poco m??s por hacer."
            
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

            extend " a ser vistos como creadores con absoluta autonom??a."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Esta libertad art??stica termina sin embargo en el momento en el que el artista procede a vender su obra."
            
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
               
            p "el creador y la galer??a,"

            p "que servir?? de intermediaria entre artista y observador."
            
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
            
            p "Al amante del arte ya no se le muestra la calidad ni la pasi??n,"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            p "sino que se pretende dejar huella en todo aquel que contemple la obra a trav??s del \"morbo\","
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "lo \"chocante\","

            extend " e incluso lo \"s??dico\"."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Te crees que el arte es solo expresi??n est??tica gratuita?"
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "????Crees que Goya pintaba jardines de flores y arco??ris?!"
            
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
                    
                    gm "??Dir??as que una mesa hecha artesanalmente al estilo renacentista es una obra de arte?"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    p "Si est?? bien hecha,"

                    extend " ??por qu?? no?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "A pesar de ser un trabajo con la ayuda de poca tecnolog??a,"

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows serious
                    with dissolve
                    
                    gm "no es arte porque se producen piezas en forma serializada,"

                    extend " casi id??nticas."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    p "Hay obras de arte que tambi??n son \"series\"."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front06
                    #show m_pupils front06a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "As?? es,"

                    gm "est??n enumeradas,"

                    extend " y solo existen en una cantidad muy limitada."
                    
                    jump afternoon04_Q_LikeClassicArt_after
    
                "No, pero s?? lo es cuando dicha obra se aleja de la primera plana o de la opini??n p??blica.":
                    
                    call p_Help
                    $ pl.ch_pts("mp",+1)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Porque no sale en los telediarios, ??deja de ser arte?"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    menu afternoon04_LikeModernArt_Fraud02_question:
                        
                        pt "Vaya tost??n pseudofilos??fico me est?? pegando la t??a..."
                        
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

                            gm "que, como la mayor??a de primates,"

                            extend " cuando no entiendes algo,"

                            show m_exp_mouth sad_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "coges una pataleta,"

                            extend " y lo insultas sin ning??n tipo de inter??s ni respeto."

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
                            
                            gm "Est?? impl??cito en lo que opinas."
                            
                            jump afternoon04_Q_AfterInterrogation
                    
                        "El principal problema del arte en la actualidad es que la gran mayor??a del p??blico no lo entiende.":
                            
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
                            
                            p "Esto hace que muchas veces el espectador caiga en la idea err??nea de que una obra se le escapa,"

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
                            
                            gm "??Entonces una obra deja de ser art??stica si depende de su explicaci??n?"

                            show m_exp_mouth sad_Silentx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            menu afternoon04_LikeModernArt_Fraud03_question:
                                
                                pt "Parece que la chica se toma en serio el asunto este..."
                                
                                "S??, desde luego.":
                                    
                                    call p_Help
                                    $ pl.ch_pts("mp",-1)

                                    show m_exp_mouth sad_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    gm "Supongo que eres de los que prefiere ir a ver pel??culas de {a=https://es.wikipedia.org/wiki/Michael_Bay}{i}Michael Bay{/i}{/a}"

                                    extend " o {a=https://es.wikipedia.org/wiki/The_Fast_and_the_Furious_(pel??culas)}{i}Fast & Furious{/i}{/a},"
                                    
                                    show m_exp_mouth happy_Talkingx09
                                    show m_exp_eyes 02
                                    show m_exp_piris front02
                                    #show m_pupils front02a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve

                                    gm "o quiz??s prefieras ir a ver alguna pel??cula de {a=https://es.wikipedia.org/wiki/Sesame_Street}Barrio S??samo{/a}"

                                    extend " o {a=https://es.wikipedia.org/wiki/Winnie_the_Pooh}Winnie-the-Pooh{/a},"
                                        
                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows angryx01
                                    with dissolve

                                    gm "me imagino que estar??n m??s adaptadas a tu comprensi??n..."

                                    show m_exp_mouth sad_Silentx03
                                    show m_exp_eyes 02
                                    show m_exp_piris front02
                                    #show m_pupils front02a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    p "??No puedo tener una opini??n?"

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

                                    extend " y ca??tica;"

                                    p "la cual puede provocar un efecto igual o incluso m??s intenso."
                                    

                                    show m_exp_mouth serious_Silentx01
                                    show m_exp_eyes 01
                                    show m_exp_piris right01
                                    #show m_pupils right01a
                                    show m_exp_eyebrows surprisex02
                                    with dissolve

                                    p "Pero la cuesti??n es que, al necesitar una explicaci??n previa,"

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
                                    
                                    p "El tiempo acabar?? por recoger y conservar lo valioso;"

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

                                    gm "??te consideras un experto en arte moderno?"

                                    extend " ??o en arte cl??sico?"

                                    show m_exp_mouth sad_Silentx02
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows surprisex001
                                    with dissolve
                                    
                                    menu afternoon04_LikeModernArt_Fraud04_question:
                                        
                                        "Conozco mejor el arte cl??sico.":
                                            
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

                                            gm "??s??...?"
                                            
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
            
            gm "??S??...?"
            
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

            gm "??te consideras un experto en arte moderno?"

            extend " ??o en arte cl??sico?"

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
    
    gm "??De verdad conoces el arte moderno?"

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

    gm "??Qui??n es el artista de este cuadro?" #Pollock Number 01
    
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
        
        pt "Esto parece como si un mont??n de potes de pintura hubiesen estornudado..."
        
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
            
            gm "{a=https://es.wikipedia.org/wiki/Vasili_Kandinski}Kandinski{/a} fue un precursor de la {a=https://es.wikipedia.org/wiki/Abstracci??n_l??rica}abstracci??n l??rica{/a} y el {a=https://es.wikipedia.org/wiki/Expresionismo}expresionismo{/a} en la pintura."
            
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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Qu?? representa este cuadro?" #El caos que hubo despu??s del bombardeo de Guernica (Picasso)
    
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
            
            p "Quiz??s..."

            p "es por una alegor??a dramatizada..."
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No intentes estropearlo m??s,"

            extend " [protname]..."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Quedas mejor diciendo simplemente:"

            extend " {i}no tengo ni la m??s \"pu??etera\" idea{/i}."
                
            jump afternoon04_Q_Guernica_after
        
        "Una demostraci??n grotesca de una org??a alocada con incesto, pedofilia y zoofilia.":
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
            
            gm "Lo tuyo s?? que es grotesco..."
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "??Ey!"
            
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
            
            gm "A??n me estoy quedando corta..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            pt "Ser?? hija de..."
                
            jump afternoon04_Q_Guernica_after
        
        "La miseria y el sufrimiento que hubo despu??s del bombardeo de Guernica.": #Correct
            
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
            
        "No lo s??...":
        
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
            
            pt "??Por qu?? co??o sonr??e?"
                
            jump afternoon04_Q_Guernica_after
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??C??mo se llama el tipo de arte de este cuadro?" #Arte on??rico (Dal??)
    
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
        
        pt "Qu?? tipo de drogas se debi?? tomar para hacer semejante cuadro..."
        
        "Fumada mental.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
                
            gm "Si te vas a tomar a co??a mis preguntas debido a tu ignorancia y petulancia,"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "ser?? mejor que dejes de hacerme perder el tiempo."
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??Queda claro?"
            
            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "??Es que acaso no te parece esto de aqu?? una fumada de mil narices?"
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "??Qu?? pu??etas representa esto?"
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "??Acaso sabes c??mo se llama esta obra pict??rica?"
            
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
                
                pt "??Desvar??os de un drogadicto talentoso?"
                
                "Relojes que se funden.":
                    call p_Help
                    $ pl.ch_pts("mp",-2)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Tu mente s?? que se funde..."

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    p "??No hace falta insultar!"

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve
                    
                    gm "No lo har??a si no dijeras gilipolleces."

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

                    gm "??Verdad?"

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "Vaya comparaci??n me da la t??a..."
                        
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
                            
                        "Y por cierto, el tipo de arte se llama {a=https://es.wikipedia.org/wiki/Realismo_art??stico}Realismo{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)
                            
                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "??Realismo?"
                            
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
                            
                            gm "??A ti te parece esto un paisaje habitual en cualquier parte del mundo?"
                            
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
                            
                            gm "????Cu??ndo has visto que los relojes se fundan de esta manera?!"
                            
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
                            
                            pt "Ser?? zorra..."

                            pt "????Por qu?? co??o sonr??e?!"
                            
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
                        
                        "Y esta obra est?? realizada por {a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo da Vinci{/a}.":
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
                            
                            gm "Este talentoso artista hace este cuadro en esa ??poca,"

                            gm "y por mucho que tuviera el benepl??cito de los {a=https://es.wikipedia.org/wiki/M??dici}M??dici{/a},"
                            
                            show m_exp_mouth happy_Talkingx09
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            #show m_pupils front03a
                            show m_exp_eyebrows suspiciousx02
                            with dissolve
                            
                            gm "lo queman en la hoguera,"

                            extend " o le cortan la cabeza en p??blico,"

                            gm "por alegor??a a lo f??nebre y demon??aco."
                            
                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows surprisex001
                            with dissolve
                            
                            pt "Creo que no lo he acertado entonces..."
                            
                            jump afternoon04_Q_OniricArt_after
                            
                        "Y esta obra est?? realizada por {a=https://es.wikipedia.org/wiki/Joan_Mir??}Joan Mir??{/a}.":
                            call p_Help
                            $ pl.ch_pts("mp",-2)

                            show m_exp_mouth happy_Talkingx03
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            gm "Pero..."

                            gm "??T?? has visto alguna vez una obra de Joan Mir???"

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows angryx01
                            with dissolve
                            
                            menu afternoon04_Q_OniricArt_Name03_JoanMiro01_question:
                            
                                "S??...":
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
                                
                                gm "Sab??as que naci?? en Barcelona,"

                                extend " ??verdad?"

                                show m_exp_mouth happy_Silentx05
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows suspiciousx02
                                with dissolve
                                        
                                menu afternoon04_Q_OniricArt_Name03_JoanMiro02_question:
                                
                                    "S??.":
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
                            
                                gm "????Qu?? trazo de este cuadro te recuerda remotamente al estilo gr??fico de Mir???!"

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
                                
                                gm "Si no tienes ni puta idea de quien es Mir??,"

                                extend " ni de qui??n pint?? este cuadro,"

                                show m_exp_mouth happy_Talkingx09
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows suspiciousx02
                                with dissolve
                                
                                gm "es mejor decir: \"No lo s??\";"

                                extend " antes de decir semejante estupidez."

                                show m_exp_mouth happy_Silentx08
                                show m_exp_eyes 04
                                show m_exp_piris front04
                                #show m_pupils front04a
                                show m_exp_eyebrows angryx01
                                with dissolve
                                
                                pt "Joder,"

                                extend " c??mo se lo toma la chica..."
                                
                                # NOT FINISHED
                                
                                jump afternoon04_Q_OniricArt_after
                       
                        "y esta obra est?? realizada por {a=https://es.wikipedia.org/wiki/Salvador_Dal??}Salvador Dal??{/a}.":
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
                            
                        "Y esta obra est?? realizada por {a=https://es.wikipedia.org/wiki/Caravaggio}Caravaggio{/a}.":
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
                            
                            gm "??pint?? un cuadro modernista del siglo XX...?"

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
                            
                            gm "Sabes cu??ndo se inici?? el arte Barroco,"

                            extend " ??verdad?"

                            show m_exp_mouth happy_Silentx02
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            #show m_pupils front04a
                            show m_exp_eyebrows normal
                            with dissolve
                            
                            menu afternoon04_Q_OniricArt_Name03_Caravaggio01:
                                
                                pt "Si mal no recuerdo, empez?? alrededor del a??o 1600..."
                                
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

                                    extend " solo te has equivocado en doscientos a??os."

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

                                    extend " te equivocas de cien a??os."

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
                                    
                                    gm "Por lo menos no eres un completo in??til despu??s de todo..."

                                    show m_exp_mouth sad_Silentx06
                                    show m_exp_eyes 04
                                    show m_exp_piris right04
                                    #show m_pupils right04a
                                    show m_exp_eyebrows angryx04
                                    with dissolve
                                    
                                    pt "Pero,"

                                    extend " ????De qu?? cojones va esta t??a?!"

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
                                    
                                    gm "Uno podr??a pensar que, al florecer alrededor del 1600,"

                                    show m_exp_mouth happy_Talkingx05
                                    show m_exp_eyes 03
                                    show m_exp_piris right03
                                    #show m_pupils right03a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "ocurri?? en el XVII,"

                                    extend " pero en realidad empez?? m??s bien unos a??os antes,"

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
                                    
                                    gm "Es como si dijeras que la \"Segunda Guerra Mundial\" ocurri?? antes de la Primera..."

                                    show m_exp_mouth happy_Talkingx10
                                    show m_exp_eyes 03
                                    show m_exp_piris front03
                                    #show m_pupils front03a
                                    show m_exp_eyebrows suspiciousx02
                                    with dissolve
                                    
                                    gm "Totalmente l??gico para tu mente primitiva..."

                                    show m_exp_mouth happy_Silentx08
                                    show m_exp_eyes 04
                                    show m_exp_piris front04
                                    #show m_pupils front04a
                                    show m_exp_eyebrows angryx01
                                    with dissolve
                                    
                                    pt "Pero,"

                                    extend " ????de qu?? cojones va esta t??a?!"
                                    
                                    jump afternoon04_Q_OniricArt_after
                                
                                "Paso de responder a estas est??pidas preguntas...": #Go to Hell
                                    
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
                        
                        p "??Alguna pregunta m??s?"

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
                    
                    gm "El t??tulo es {a=https://es.wikipedia.org/wiki/La_persistencia_de_la_memoria}La Persistencia de la Memoria{/a}."
                        
                    #NOT FINISHED
                        
                    jump afternoon04_Q_OniricArt_after
                    
                "Paso de responder a estas est??pidas preguntas...": #Go to Hell
                    
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
            
                gm "Los simbolistas cre??an que el arte deb??a apuntar a capturar las verdades m??s absolutas,"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "las cuales solo pod??an ser obtenidas por m??todos indirectos y ambiguos."

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
                    
                gm "posee intenciones metaf??sicas,"

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "adem??s, intenta utilizar el lenguaje literario como instrumento cognoscitivo,"

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
                
                p "??Pero lo he acertado o no?"

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
                
                pt "Entonces, ????por qu?? se enrolla tanto?!"
                    
                jump afternoon04_Q_OniricArt_after
        
        "Surrealismo.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ Martq += 3 #If the answer is correct. This answer Surrealism, Persistent of time and Salvador Dal?? Questions of "Fumada mental".

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
                
                gm "El {a=https://es.wikipedia.org/wiki/Expresionismo}Expresionismo{/a} suele ser entendido como la deformaci??n de la realidad,"

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows serious
                with dissolve
                    
                gm "para expresar de forma m??s subjetiva la naturaleza y el ser humano,"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "dando primac??a a la expresi??n de los sentimientos sobre la descripci??n objetiva de la realidad."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris left02
                #show m_pupils left02a
                show m_exp_eyebrows surprisex02
                with dissolve
                
                gm "Los expresionistas defend??an un arte m??s personal e intuitivo,"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "donde predominase la visi??n interior del artista,"

                extend " la \"expresi??n\","

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris front02
                #show m_pupils front02a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "frente a la plasmaci??n de la realidad,"

                extend " la \"impresi??n\"."

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
                
                p "??Entonces lo he acertado?"

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 02
                show m_exp_piris left02
                #show m_pupils left02a
                show m_exp_eyebrows angryx01
                with dissolve
                
                gm "??A ti te parece este cuadro una expresi??n subjetiva de la naturaleza y el ser humano?"

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

                extend " no me parece una representaci??n muy objetiva de la realidad..."

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
                
            gm "El {a=https://es.wikipedia.org/wiki/Realismo_art??stico}Realismo{/a} es una postura que plasma la realidad o naturaleza de una manera imitativa."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "??A ti te parece que este cuadro est?? representando fielmente la realidad?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " no..."

            p "pero sin duda est?? hecho con mucho esmero,"

            extend " y parece real..."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Lo que una tiene que o??r..."

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
                
            gm "??Por qu?? no me extra??a...?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
                
            p "..."
                
            jump afternoon04_Q_OniricArt_after
        

        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??C??mo se llama esta obra?" #El gran masturbador.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_GranMasurbador_question:
        
        pt "Ese careto raro con esas pesta??as, ??no estaban en el cuadro anterior...?"
        
        "Mujer olfateando las partes nobles de un hombre con la polla enana.":
            call p_Help
            $ pl.ch_pts("mp",-2)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Est??s describiendo una parte del cuadro,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "sencillamente porque no tienes ni la m??s remota idea de c??mo diablos se titula esta obra."

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

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dal??}Salvador Dal??{/a}."
            
            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Una cara de le??n con una lengua enorme,"

            pt "un grillo bocabajo con su trasero repleto de hormigas,"
            
            pt "una especie de careto deformado esnifando el suelo,"

            pt "una mujer olfateando unos test??culos m??s largos que el micropene,"

            extend " sin mencionar todo lo dem??s..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "??Qu?? pu??etas tiene esto de \"masturbaci??n\"?"
            
            pt "De hecho..."

            extend " ????Qu?? pu??etas tiene esto de er??tico?!"
            
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
            
            gm "??Y qui??n fue su pintor?"

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
                    
                    gm "Tuvieron una relaci??n espor??dica y mayormente rivalizada."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Pero no podr??an ser m??s diferentes gr??ficamente..."

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
                    
                    gm "Por ser un artista que muri?? en el 1828,"

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    #show m_pupils right03a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "la verdad es que se avanz?? bastante a su ??poca."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "Pero no,"

                    extend " te has equivocado por m??s de cien a??os..."

                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "Maldita sea..."
                    
                    #NOT FINISHED TEXT
                    
                    jump afternoon04_Q_GranMasturbador_after
                
                "Salvador Dal??.": #Correct
                    
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
                    
                "Un enfermo talentoso del psiqui??trico.":
                    call p_Help
                    $ pl.ch_pts("mp",-3)
                    
                    #NOT FINISHED

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex02
                    with dissolve
                    
                    gm "T?? s?? que est??s enfermo."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve
                    
                    gm "Pero por desgracia,"

                    extend " lo tuyo no tiene otra cura que la educaci??n,"

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "y est?? claro que contigo ha sido un fracaso."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    #show m_pupils front02a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    p "??No puedo tener opini??n?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    gm "??Hablando sin respeto quieres dar tu opini??n?"

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve
                    
                    pt "????Ella me habla de respeto?!"
                    
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
                    
                    gm "Aunque trabaj?? estrechamente con este artista en 1945 con el cortometraje {a=https://es.wikipedia.org/wiki/Destino_(cortometraje)}Destino{/a},"

                    show m_exp_mouth sad_Talkingx007
                    show m_exp_eyes 03
                    show m_exp_piris left03
                    #show m_pupils left03a
                    show m_exp_eyebrows surprisex001
                    with dissolve
                    
                    gm "no hay nada de este cuadro que recuerde m??nimamente la obra de {a=https://es.wikipedia.org/wiki/Walt_Disney}{i}Disney{/i}{/a},"

                    extend " mucho menos su t??tulo..."
                    
                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris left04
                    #show m_pupils left04a
                    show m_exp_eyebrows normal
                    with dissolve

                    p "..."

                    pt "??Y se puede saber cu??l es su t??tulo?"
                    
                    jump afternoon04_Q_GranMasturbador_after
                    
                "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
                    
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
            
            gm "??Qu?? parte de este cuadro te hace pensar que se llama as???"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "No s??..."

            extend " supongo que la mujer me ha llamado mucho la atenci??n..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "??Y todos los dem??s elementos del cuadro?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows serious
            with dissolve
            
            p "Pues..."

            extend " el narizotas parece como sumiso,"

            p "y lo dem??s,"

            extend " realmente no sabr??a c??mo catalogarlo..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Esta obra se llama {a=https://es.wikipedia.org/wiki/El_gran_masturbador}El Gran Masturbador{/a},"

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dal??}{i}Salvador Dal??{/i}{/a}."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "????Y qui??n co??o se est?? masturbando aqu???!"
            
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

            extend " de {a=https://es.wikipedia.org/wiki/Salvador_Dal??}{i}Salvador Dal??{/i}{/a}."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "??Y hay alguien sensato que pudiera llegar a adivinar el t??tulo viendo este batiburrillo de ideas sin ninguna l??gica?"
            
            jump afternoon04_Q_GranMasturbador_after
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Qu?? es esto?" #Le Fountain de Marcel Duchamp

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_FountainDuchamp_question:
        
        pt "??Qu?? cojones hace un urinario expuesto en un museo?"
        
        "Esto es un urinario con una firma en una exposici??n.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Eso lo dices porque desconoces c??mo se titula esta pieza art??stica,"

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
            
            p "T?? me has preguntado:"

            extend " {i}??Qu?? es esto?{/i}."

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
            
            p "??C??mo se llama esta obra?"

            p "Seguramente es lo que quer??as preguntar..."

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
            
            p "??C??mo la definir??as t???"

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

            extend " se inici?? una aut??ntica revoluci??n en el mundo del arte al demostrar..."

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
            
            p "{i}??Qu?? es esto?{/i}"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No me has preguntado qu?? significa,"

            p "c??mo se llama,"

            extend " o qu?? repercusiones tuvo esta obra."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "..."

            # No hace falta a??adir m??s puntos, porque lo haces m??s adelante.

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Y bien..."

            extend " listillo,"

            gm "??C??mo se llama?"

            extend " ??y qui??n es su autor?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            menu afternoon04_Q_FountainDuchamp_urinary01_question:
                
                "No ha colado... Tendr?? que responder algo..."
                
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
                    
                    p "??Alguna pregunta m??s?"

                    p "que puedas formular correctamente..."

                    show m_exp_mouth sadbiting_Silentx07
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx05
                    with dissolve
                    
                    gm "..."

                    jump afternoon04_Q_FountainDuchamp_after
                    
                "{i}Au fond ?? droite{/i} de Jackson Pollock.":
                    jump afternoon04_Q_FountainDuchamp_Pollock
                    
                "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
                    call p_Help
                        
                    jump afternoon04_Q_AfterInterrogationFail
        
        "La {i}Fontaine{/i} de Duchamp.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1) #If there??s no more correct answers, otherwise will be more than +1
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
                
                gm "Nunca trat?? con el {a=https://es.wikipedia.org/wiki/Arte_encontrado}{i}ready-made{/i}{/a}."

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Adem??s,"

                extend " el t??tulo en franc??s \"Al fondo a la derecha\","

                show m_exp_mouth happy_Talkingx10
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows serious
                with dissolve
                
                gm "me parece un tanto cutre,"

                gm "y m??s dici??ndolo al azar para probar suerte."

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex001
                with dissolve
                
                gm "??No tienes verg??enza alguna?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows serious
                with dissolve
                
                p "..."

                pt "Uno tiene que probar suerte a veces,"

                extend " ??no...?"

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows angryx01
                with dissolve

                pt "????Por qu?? diablos sonr??e?!"

                extend " Ser?? perra..."
                
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

                extend " en franc??s..."

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

                gm "te has comido mucho la mollera para sacar este t??tulo..."

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
                
                gm "La obra m??s conocida de esta serie es {a=https://es.wikipedia.org/wiki/La_imposibilidad_f??sica_de_la_muerte_en_la_mente_de_algo_vivo}La imposibilidad de la muerte f??sica en la mente de alguien vivo{/a},"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris right02
                #show m_pupils right02a
                show m_exp_eyebrows normal
                with dissolve

                gm "un tibur??n tigre de catorce pies sumergido en formol en una vitrina transparente."

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
                
                p "??Un animal muerto en una vitrina te parece una obra de arte?"

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "No me ser??s otro progre-vegano-come-hierba..."

                extend " ??Verdad?"

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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
    
label afternoon04_Q_FountainDuchamp_after:

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "??C??mo es posible que un sucio y maloliente urinario sacado de un vertedero se pueda llegar a considerar arte?" 
    #Porque demostr?? que una obra de arte no ten??a que ser hermosa sino que deb??a provocar al intelecto.

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    menu afternoon04_Q_DuchampArt_question:
        
        pt "??Por qu?? la gente que considera esto arte no ha acudido a ayuda profesional?"
        
        "Porque supo sobornar a la gente adecuada y ten??a buenos contactos.":
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

            extend " me das bastante l??stima."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "????Acaso t?? consideras esto una obra de arte?!"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            p "??Es un pu??etero urinario puesto del rev??s con una puta firma!"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "??Qu?? tiene de arte?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Cuando algo se escapa a tu comprensi??n,"

            gm "sencillamente coges una pataleta."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Como si fueras un ni??o peque??o."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Te tendr??an que dar dos medallas,"

            gm "una por corto y otra por si la pierdes."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Qu?? chispa tiene la chica..."

            pt "en unos a??os ser?? un mechero."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows sadx05
            with dissolve

            gm "Por curiosidad..."

            gm "??Tus padres son hermanos?"

            show m_exp_mouth happy_Talkingx10 # Sound Laugh NOT FINISHED
            show m_exp_eyes 06
            show m_exp_piris front06
            #show m_pupils front05a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??Me encerrar??an en prisi??n si le metiera una paliza a la pajarraca esta...?"
            
            jump afternoon04_Q_DuchampArt_after
            
        "Porque demostr?? que una obra de arte no ten??a que ser hermosa, sino que deb??a provocar al intelecto.": #Correct
            
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
        
        "Porque demostr?? que solo hace falta la aprobaci??n de un cr??tico para que algo se considere arte.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "La visi??n especializada y cr??tica ayuda,"

            gm "promueve y aporta sin lugar a duda"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
                                                                                               
            gm "una mirada m??s neutral, y por lo tanto,"

            extend " m??s profesional."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Sin embargo y afortunadamente,"

            gm "el papel del cr??tico parece estar superado."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Era una figura casposo-naftal??nica."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Siempre me ha interesado m??s la visi??n personal,"

            gm "al margen de las calificaciones profesionales."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Un buen cr??tico de arte tiene que poder nacer cada vez en una obra"

            gm "y morir tambi??n en ella."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Entonces es verdad,"

            extend " una obra no se considera arte hasta que un cr??tico lo ratifica..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Aunque fueras el ??ltimo hombre en el mundo"

            gm "y crearas una obra que nadie volviera nunca m??s a contemplar,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "tu obra seguir??a consider??ndose \"obra de arte\","

            gm "aunque por desgracia no habr??a nadie para poder apreciarla."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Pero es dif??cil que algo se exponga en un museo o galer??a importante sin el respaldo de un cr??tico de prestigio."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "El mercado ha suplantado al cr??tico."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "La cr??tica adorna,"

            extend" pero no encumbra."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Puede m??s un precio alto en una subasta,"

            extend " que un comentario del mejor cr??tico."

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
            
            pt "Podr??a haber empezado por ah?? y no haberme soltado semejante rollo..."
            
            jump afternoon04_Q_DuchampArt_after
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Qu?? pretend??a realmente {a=https://es.wikipedia.org/wiki/Andy_Warhol}{i}Andy Warhol{/i}{/a} con sus obras?" 
    #Trivializar y vulgarizar el propio arte para que dejara de pertenecer solo a la clase alta.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_AndyWarholPurpose_question:
        
        pt "Vivir de la fama de los dem??s, me imagino..."
        
        "Ganar dinero gracias a la ignorancia de la gente que compraba sus obras.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??T?? comprar??as su obra?"

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
            
            gm "Entonces te est??s contradiciendo."

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
            
            pt "Ser?? cabrona..."
                
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
            
            gm "Eso lo consigui?? indirectamente."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Pero no fue su pretensi??n inicial."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "??Acaso no todos los artistas ans??an conseguir fama y dinero?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "??O realmente crees que los artistas viven del aire que respiran?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Tienes mucho que aprender sobre el significado de arte si piensas as??..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Lo que t?? digas..."
                
            jump afternoon04_Q_AndyWarholPurpose_after
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    n "Al mirar el cuadro, te fijas en que debajo hay un texto escrito en franc??s en el que pone \"Esto no es una pipa\"."

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
    
    gm "??Cu??l es la paradoja de esta obra?" #Que en realidad esto es la representaci??n gr??fica de una pipa pintada en un cuadro vista a trav??s de un m??vil.
    #La traici??n de las im??genes "Ceci n??est pas una pipe".

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_Q_NestPasUnaPipe_question:
        
        pt "Esto es una pipa... ??No?"
        
        "Que en realidad, es una ilustraci??n gr??fica del objeto representado.": #Correct
            
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

            extend " de hecho es la ilustraci??n de una pipa pintada en un cuadro,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "capturada fotogr??ficamente,"

            extend " y vista a trav??s de un m??vil."

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

            extend " El t??tulo de esta obra es"

            extend " {a=https://es.wikipedia.org/wiki/La_traici??n_de_las_im??genes}La Traici??n de las Im??genes{/a}."
                
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
            
            gm "??Y se supone que el espejo lo tiene que llevar el que viene a ver la obra?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No..."

            extend " bueno,"

            p "se supone que en la misma exposici??n deber??a de estar el espejo..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??Y qu?? es lo que se ve, una vez la imagen est?? reflejada?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No s??..."

            extend " ??Un conejo?"

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

            gm "sino una representaci??n gr??fica de una pipa."

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
            
            gm "Si observas estas dos p??ginas del libro {a=https://es.wikipedia.org/wiki/Entender_el_c??mic}Entendiendo los c??mics{/a} de {a=https://es.wikipedia.org/wiki/Scott_McCloud}Scott McCloud{/a} lo entender??s mejor:"
            
            scene black
            show afternoon04_paint m_magritte_treacheryofimages_02:
                subpixel True
                xanchor 0.05 yanchor 0.05 zoom 0.55
                easein_quad 5.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            window hide dissolve
            pause
            
            pt "Con esta letra tan peque??a no veo un carajo... si por lo menos tuviera la {a=https://jynnemason.files.wordpress.com/2015/07/mccloud2.png}imagen en grande{/a} para verla bien..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "Que, aunque es lo primero que ves, si te fijas bien, ver??s representado en el cuadro algo que no es una pipa.":
            
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Y qu?? es lo que se supone que se ve si no es una pipa?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No s??..."

            extend " ??Un pato?"

            extend " ??Un conejo?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No, [protname],"

            extend " a lo que t?? te est??s refiriendo se llama {a=https://es.wikipedia.org/wiki/Imagen_ambigua}imagen ambigua{/a}."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Y, en el caso de que as?? fuera,"

            gm "en el texto no pondr??a"

            extend " \"Esto no es una pipa\","

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "en todo caso habr??a escrito:"

            extend " \"No solo es una pipa\","

            gm "o:"

            extend" \"Hay algo m??s que una pipa\"."
            
            scene black
            show afternoon04_paint m_paulnoth_rabbitduckarmy:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            n "En el pie de p??gina de esta ilustraci??n se puede leer:"
            
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

            gm "Del mismo modo que en esta ilustraci??n algunos ver??n que defienden al ej??rcito conejo y otros al ej??rcito pato."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Una tira c??mica,"

            gm "por cierto,"

            extend " muy mordaz con el delirio b??lico de la mayor??a de las religiones..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "??Hay alguna cosa que deje sin criticar esta mujer?"
            
            jump afternoon04_Q_AfterInterrogation
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail

label afternoon04_Q_LikeClassicArt_after:
    
    #arte figurativo cl??sico

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
        
    gm "??Tienes conocimientos de arte cl??sico?"

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
        
        pt "??Y a qu?? siglo se refiere con arte cl??sico?"
        
        "S??, por supuesto.":
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

            extend " {a=https://es.wikipedia.org/wiki/Miguel_??ngel}Michelangelo{/a},"

            extend " {a=https://es.wikipedia.org/wiki/Donatello}Donatello{/a},"

            extend " {a=https://es.wikipedia.org/wiki/Leonardo_da_Vinci}Leonardo{/a}..."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??Esos s?? los conozco!"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "No me dir??s que son las {a=https://es.wikipedia.org/wiki/Tortugas_Ninja}Tortugas Ninja{/a},"

            extend " ??verdad?"

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
        
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
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
        
    gm "??C??mo se titula este cuadro?" #El origen del mundo.

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
            
            gm "No te culpo por pensar que este pudiera ser el t??tulo,"

            extend " pero no..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Entonces,"

            extend " ser??a un acierto..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Va a ser que no,"

            extend " porque el t??tulo de la obra es {a=https://es.wikipedia.org/wiki/El_origen_del_mundo}{i}L??Origine du Monde{/i}{/a}."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Claro..."

            pt "porque del ??tero de una mujer salieron los peces,"

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
            
        "M??quina de sacar punta al l??piz.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Con esa forma de pensar,"

            extend " el tuyo estar?? a??n para estrenar..."

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
            
            pt "Si t?? supieras..."

            extend " perra."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
        
        "La perdici??n del hombre.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Sin duda ser??a un t??tulo apropiado."

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

            gm "El t??tulo de la obra es {a=https://es.wikipedia.org/wiki/El_origen_del_mundo}{i}L??origine du monde{/i}{/a}."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??Del mundo?"

            pt "Un poco {a=https://es.wikipedia.org/wiki/Antropocentrismo}antropocentrista{/a} el t??tulo..."
            
            jump afternoon04_paint_c_gustavecourbet_originedumonde_paradox
        
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Sabr??as decirme cu??l es la paradoja de esta obra?" #Es una obra famosa, pero poco vista.

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_gustavecourbet_originedumonde_paradox_question:
    
        #pt "??Paradoja? No es que deje mucho a la imaginaci??n... es un cuadro bastante expl??cito..."
        
        "Que durante a??os el patriarcado ha marcado el esperma como s??mbolo de origen, pero es la matriz donde realmente se gesta el milagro.":
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
            
            pt "??Por qu???"

            pt "??Porque es un comentario en contra del patriarcado?..."

            pt "Majara..."

            extend " est?? majara..."
            
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
            
            gm "Eran muy comunes en el a??o 1866,"

            extend " las operaciones de cambio de sexo..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "??Acaso no ten??an derecho a cambiar de sexo si quer??an?"

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

            gm "habr??a sido la proeza quir??rgica del siglo."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Pero existe la remota posibilidad que fuera as?? entonces..."

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
            
            pt "Ten??a que intentarlo..."
            
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
            
        "Que aunque el pintor fuera homosexual, le fascinaba la parte ??ntima femenina." if afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_gustavecourbet_originedumonde_paradox_homosexual = True
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??El autor era homosexual?"

            gm "??De d??nde diablos has sacado eso?"

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

            extend " y mucho menos en esa ??poca."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Hay que mencionar tambi??n que sus obras m??s ??ntimas sol??an ser homosociales."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Mujeres semidesnudas,"

            extend " o completamente desnudas,"

            extend " acarici??ndose mutuamente,"

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
            
            pt "??Bien!"

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
            
            gm "Te repetir?? la pregunta,"

            gm "??Sabr??as decirme cu??l es la paradoja de esta obra?"

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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Qui??n pint?? esta obra?" #Miguel ??ngel

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

            extend " si tenemos que hacer caso a las memorias del {a=http://rbscp.lib.rochester.edu/3456}An??nimo Gaddiano{/a},"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "probablemente {a=https://es.wikipedia.org/wiki/Miguel_??ngel}Miguel ??ngel{/a},"

            extend " el verdadero autor de esta obra,"

            gm "saldr??a de su tumba para destrozarte a golpes."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Despu??s de lo que le cost?? realizar tal magna obra,"

            gm "y aun as??,"

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
            
            gm "Cuando la mayor??a de sus obras no salieron del papel,"

            gm "y sin embargo, ??l no tuvo descanso alguno en su ardua vida como artista."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Con decirme que no lo hab??a acertado,"

            extend " hubiera bastado."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Y perderme esa expresi??n tuya de pura ignorancia?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            pt "Simp??tica la mujer cuando quiere..."
            
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
            
            gm "Aunque vivieron m??s o menos en la misma ??poca,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "la verdad es que sus estilos no podr??an ser m??s distintos."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/El_Bosco}Hieronymus Bosch{/a} fue un magn??fico artista tratando temas religiosos,"

            extend " surrealistas,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "con un gran n??mero de simbolismos folcl??ricos y humor burlesco,"

            extend " a veces cruel."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Pero su estilo segu??a anclado a la Edad Media."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "O sea,"

            extend " que no lo he acertado..."
            
            jump afternoon04_paint_c_miguelangel_CreationOfAdam_PaintingName
        
        "Miguel ??ngel.": #Correct
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

            extend " Botticelli es m??s del {a=https://es.wikipedia.org/wiki/Quattrocento}Quattrocento{/a}."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Su estilo sigue manteniendo muchos elementos a??n arcaicos,"

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
            
        "Diego Vel??zquez.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "El maestro Vel??zquez no ten??a demasiado que envidiar del talentos??simo artista de esta obra."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero, al nacer treinta y cinco a??os despu??s de su muerte,"

            extend " ten??a cierta ventaja t??cnica y cultural."

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
            
        "No lo s??.":
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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??C??mo se titula este fragmento?" #La creaci??n de Ad??n

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_PaintingName_question:
    
        pt "??Fragmento? Eso es que la obra entera es bastante mayor..."
        
        "Hombre desnudo en la monta??a tomando droga dura.":
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
            
            gm "??Se supone que me tengo que re??r?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Hombre,"

            extend " una sonrisita tampoco te har??a ning??n da??o..."

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

            extend " quiz??s no es mucho de la co??a esta loca amargada..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum
        
        "La creaci??n de Ad??n.": #Correct
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
            
            gm "??C??mo se llama \"realmente\" este fragmento?"

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
            
            gm "Ese era el t??tulo de la obra anterior..."

            gm "??O es que ya ni te acuerdas de eso?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            p "..."

            p "Pero quiz??s se llaman igual..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "No,"

            extend " no es el caso."

            gm "Hubiera sido de mal gusto por parte de {a=https://es.wikipedia.org/wiki/Gustave_Courbet}Coubert{/a},"

            extend " llamarlo igual que esta famos??sima pieza art??stica."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Mierda..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum
            
        "EL sexto d??a.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "S??,"

            gm "es cierto que, en el sexto d??a,"

            extend " seg??n el {a=https://es.wikipedia.org/wiki/G??nesis}G??nesis B??blico{/a},"

            gm "Dios cre?? a {a=https://es.wikipedia.org/wiki/Ad??n}Ad??n{/a},"

            extend " el primer hombre."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Pero tambi??n cre?? much??simas cosas m??s,"

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
                
            gm "por si se te hab??a olvidado..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No..."

            extend " no se me hab??a olvidado..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Entonces es peor,"

            gm "porque das por entendido que lo realmente importante de ese d??a fue ??nicamente la creaci??n del hombre."

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
            
            gm "????Entonces por qu?? llamarlo \"El Sexto D??a\"?!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "No s??..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "??Exacto!"

            extend " No tienes ni pu??etera idea de nada."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."

            pt "Jodeeer..."

            extend " como est?? la pava..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Museum

            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??En qu?? museo se expone?" #En ninguno, se expone en el techo de la capilla sixtina.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_Museum_question:
    
        pt "No veo ning??n marco..."
        
        "En el {i}Louvre{/i} de Par??s.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "El {a=https://es.wikipedia.org/wiki/Museo_del_Louvre}{i}Louvre{/i}{/a} es uno de mis museos favoritos,"

            gm "no solo porque ah?? se expone {a=https://es.wikipedia.org/wiki/La_Gioconda}{i}La Gioconda{/i}{/a},"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "aunque tengo mis dudas de que sea la aut??ntica..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Sino porque adem??s fue la sede real del poder en {a=https://es.wikipedia.org/wiki/Francia}Francia{/a} hasta que {a=https://es.wikipedia.org/wiki/Luis_XIV_de_Francia}Luis XIV{/a} se traslad?? a {a=https://es.wikipedia.org/wiki/Palacio_de_Versalles}Versalles{/a}."
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Sin menospreciar el magn??fico trabajo de {a=https://es.wikipedia.org/wiki/Ieoh_Ming_Pei}Ieoh Ming Pei{/a},"

            gm "con la ambiciosa modernizaci??n que recibi?? el lugar en los ochenta."
            
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
            
            gm "{a=https://es.wikipedia.org/wiki/Museo_del_Prado}El museo del Prado{/a} es uno de los mayores museos del mundo y especialmente de {a=https://es.wikipedia.org/wiki/Espa??a}Espa??a{/a}."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Pero no,"

            extend " esta obra est?? bastante lejos de {a=https://es.wikipedia.org/wiki/Madrid}Madrid{/a}..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "La cagu??..."
            
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
        
        "En la Galer??a {i}Uffizi{/i} de Florencia.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Por lo menos has adivinado el pa??s donde est?? expuesto,"

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

            extend " pero a m?? me dar??a verg??enza no saber esto."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "A m?? me dar??a m??s verg??enza ser tan est??pida y prepotente como t??..."
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Cu??l es el mensaje oculto en contra de la Iglesia que se le presume?" #El manto donde est?? Dios en realidad representa un cerebro.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    menu afternoon04_paint_c_miguelangel_creationofadam_Message_question:
    
        pt "Qu?? man??a con buscar mensajes ocultos..."
        
        "El manto donde est?? Dios, en realidad, representa un cerebro humano.": #Correct
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
            
        "El manto rojo alrededor de Dios tiene la forma del ??tero humano y la bufanda verde es el cord??n umbilical reci??n cortado." if afternoon04_paint_c_miguelangel_creationofadam_Message_womb == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_miguelangel_creationofadam_Message_womb = True
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??De d??nde sacas esa idea?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " {a=https://www.theverge.com/2016/12/6/13852240/westworld-finale-ford-dolores-michelangelo-brain-creation-of-adam}lo le?? en alguna parte...{/a}"
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "La idea es interesante,"

            gm "pero no."

            gm "No creo que sea un ??tero lo que est?? aqu?? representado."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Esa ser?? su opini??n,"

            extend " ??no?"

            pt "Al fin y al cabo lo m??s probable es que se trate de una simple {a=https://es.wikipedia.org/wiki/Pareidolia}pareidolia{/a}..."
            
            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Te repito la pregunta,"

            gm "??Cu??l crees que es el mensaje oculto en esta obra?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve
            
            jump afternoon04_paint_c_miguelangel_creationofadam_Message_question
        
        "Que Dios en realidad es una nave espacial conducida por peque??os seres del espacio.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??De d??nde has sacado esa idea?"

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
            
            gm "??Y d??nde est??n ahora?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Yo qu?? s??..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "??Y en qu?? te basas para creer que Miguel ??ngel quiso retratar esa idea en este cuadro?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "No s??,"

            extend " quiz??s lo sospech?? y quiso retratarlo para la inmortalidad en esta pieza art??stica..."

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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
            call p_Help
                
            jump afternoon04_Q_AfterInterrogationFail
            

#Until now Cartq = 7 if all questions are correct (Even FCBarcelona) It??s ncessary 5 points more to get 12.

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
    
    gm "??Qu?? hay de extra??o en la obra {a=https://es.wikipedia.org/wiki/Archivo:Madonna_Col_Bambino_e_San_Giovannino_-_1400s.png}{i}Madonna de Saint Giovannino{/i}{/a}?" #Aparece un objeto volador no identificado.

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_paint_c_madonnagiovannino_Strange_question:
    
        pt "Todo en este cuadro parece extra??o... empezando por esas caras..."
        
        "La vaca y el burro est??n tan juntos que parece que compartan un mismo cuerpo.":
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
            
            p "??Qu???"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "De todo el cuadro..."

            gm "??Te fijas en eso?"

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
            
            gm "Salen as?? de juntos como en la mayor??a de obras antiguas porque es la m??nima demostraci??n de que se trata de un establo,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "porque son un detalle que no debe destacar en lo m??s m??nimo."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Por eso est??n as?? a oscuras,"

            gm "casi imperceptibles,"

            extend " y ocupando el m??nimo espacio."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Eso es que no lo he acertado..."
            
            jump afternoon04_paint_c_goya_akelarre1798_PaintingName
        
        "Es curioso que Mar??a tenga una corona brillante en la cabeza si representa que no est?? muerta...":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Qu???"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "??Las coronas no representan a los ??ngeles y a los difuntos?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Las {a=https://es.wikipedia.org/wiki/Aureola}aureolas{/a} son la forma de representar la iluminaci??n a los {a=https://es.wikipedia.org/wiki/??ngel}??ngeles{/a} y a las figuras sagradas,"
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "como lo son {a=https://es.wikipedia.org/wiki/Jes??s_de_Nazaret}Jesucristo{/a},"

            extend " los {a=https://es.wikipedia.org/wiki/Santo}santos{/a},"

            gm "o, como lo es en este caso,"

            extend " la {a=https://es.wikipedia.org/wiki/Mar??a_(madre_de_Jes??s)}Virgen Mar??a{/a}."
            
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
            
            gm "T?? has visto mucho {a=https://es.wikipedia.org/wiki/Dragon_Ball}{i}Dragon Ball{/i}{/a},"

            extend " ??verdad?"

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
            
        "Aparece una constelaci??n de estrellas y se ve un planeta siendo pleno d??a.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Constelaci??n de estrellas?"

            extend " ??Planeta?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Reconozco que lo que se ve a la izquierda no s?? muy bien qu?? demonios representa que es."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "En un inicio,"

            extend " uno puede pensar que representa a {a=https://es.wikipedia.org/wiki/Sant??sima_Trinidad}la Sant??sima Trinidad{/a}."

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
            
            p "Es que se ve muy peque??o para poderlo distinguir..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Eso demuestra que es la primera vez que ves este cuadro,"

            extend " y, por lo tanto,"

            extend " que lo desconoc??as."

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
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??De qui??n es esta obra?" # Francisco Goya. (1798) +1 

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_goya_akelarre1798_PaintingName_question:
    
        pt "Esto es un macho cabr??o humanizado, ??no?"
        
        "Vicente L??pez Porta??a.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "{a=https://es.wikipedia.org/wiki/Vicente_L??pez_Porta??a}Porta??a{/a} era un artista {a=https://es.wikipedia.org/wiki/Pintura_neocl??sica}neoclasicista{/a},"
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "y fue considerado en su ??poca el mejor retratista,"

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
            
        "Diego Vel??zquez.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Vel??zquez fue tambi??n un pintor de la realeza,"

            extend " como el artista de esta obra."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Solo que naci?? ciento cincuenta a??os antes..."

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
            
            gm "Aunque fue un artista rom??ntico,"

            gm "al igual que el artista de esta obra,"

            extend " y vivieron en la misma ??poca,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "sus estilos pict??ricos eran realmente muy distintos."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "A pesar de que la calidad de {a=https://es.wikipedia.org/wiki/William_Blake}{i}Blake{/i}{/a} no era tan buena,"

            extend " debo confesar que me cautivan mucho m??s..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Quiz??s sea porque sus obras mezclan arte y poes??a de una forma magistral..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Bueno..."

            p "el caso es que no lo he acertado,"

            extend " ??verdad?"

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
               
            pt "??Pues no te enrolles tanto cabrona!"
        
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
            
            gm "{a=https://es.wikipedia.org/wiki/John_William_Waterhouse}Waterhouse{/a} naci?? un siglo despu??s que el artista de este cuadro."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Aunque imbuido tambi??n por el {a=https://es.wikipedia.org/wiki/Romanticismo}Romanticismo{/a},"

            gm "que le permiti?? encuadrar, parte de sus obras, dentro del {a=https://es.wikipedia.org/wiki/Simbolismo}Simbolismo{/a};"
            
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

            gm "y en mi opini??n es uno de los mayores artistas que ha habido."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Queda claro que no lo he acertado..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
        
        "No lo s??.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??En serio?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "??No te da verg??enza no conocer a este gran maestro de las artes pl??sticas?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Joder,"

            p "quiz??s conozca al artista,"

            extend " pero esta obra no me suena..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Es una de sus obras m??s famosas,"

            extend " especialmente en su etapa m??s oscura."

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

            extend " c??mo se pone la pava por un puto cuadro..."
            
            jump afternoon04_paint_c_goya_akelarre1798_Influence
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Qu?? suceso le influy?? para crear esta obra?" #El caso de las Brujas de Zugarramurdi +1

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_goya_akelarre1798_Influence_question:
    
        pt "Cuanto m??s te fijas en esta obra, m??s cosas raras ves..."
        
        "Un {b}aquelarre{/b} que presenci?? el artista cuando era peque??o.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Te refieres a que vio como un macho cabr??o se com??a a reci??n nacidos en medio de un descampado a plena noche?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "He dicho \"cuando era peque??o\","

            extend " sencillamente fue una escena que lo traumatiz??"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
               
            p "y con la inocencia de la ni??ez transform?? la realidad que luego represent?? en este cuadro."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "Aunque es una teor??a bastante interesante,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "el hecho es que desconoces que el cuadro es en realidad una cr??tica de un caso real que hubo en {a=https://es.wikipedia.org/wiki/Pa??s_Vasco}Euskadi{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Mierda,"

            extend " no ha colado..."
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "Est?? basado en una pesadilla que tuvo el artista.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No niego que la visi??n sea pesadillesca..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Pero no,"

            extend " no es un cuadro {a=https://en.wikipedia.org/wiki/Dream_art}on??rico{/a}," # No Spanish Wiki.

            gm "como lo pueden ser las obras de {a=https://es.wikipedia.org/wiki/Salvador_Dal??}Dal??{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Ten??a que intentarlo..."
            
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
            
            gm "M??s de ciento cincuenta personas fueron detenidas y encarceladas,"

            extend " solo con acusaciones."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Al menos cinco de los acusados fallecieron en prisi??n,"

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

            gm "se neg?? a emitir declaraci??n,"

            extend " y muri?? aplastado en un intento de obligarlo."
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Este acontecimiento ha sido usado ret??ricamente en la pol??tica y la literatura popular"

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

            extend " y la intromisi??n gubernamental en las libertades individuales."

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
            
            gm "en realidad, se est?? refiriendo a otro caso que ocurri?? en 1610;"

            gm "casi un siglo antes que el de {a=https://es.wikipedia.org/wiki/Juicios_de_Salem}Salem{/a}."
            
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "??Tanto le cuesta decirme simplemente?"

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
            
        "No lo s??.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Puedo entender que esta pregunta est?? quiz??s un poco demasiado por encima de tus posibilidades."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Pero, ????qui??n se cree que es esta t??a?!"
            
            jump afternoon04_paint_c_johnwilliamwaterhouse_magiccircle_PaintingName
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??C??mo se titula esta obra?" # john_william_waterhouse_MagicCircle_1886 +1
    
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
    
    p "??Esto es arte cl??sico?"

    show m_exp_mouth sad_Talkingx03
    with dissolve
    
    gm "Es de 1886."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "??Por qu?? lo preguntas?"

    gm "??Acaso te rindes porque no sabes la respuesta?"

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
    
        pt "??C??mo se llama esta obra? ??Y yo qu?? s??! Espero que tenga algo que ver con lo que se ve en el cuadro..."
        
        "El c??rculo m??gico.": #Correct
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
            
        "Protecci??n contra los cuervos.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??Para qu?? querr??a alguien protegerse contra los cuervos?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "No s??..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve

            gm "Creo que has visto demasiadas veces la pel??cula {a=https://es.wikipedia.org/wiki/Los_p??jaros}Los P??jaros{/a}."

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
            
            p "Pero en el cuadro da la sensaci??n de que los cuervos no entran en el c??rculo que est?? marcando..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Quiz??s ese c??rculo ser??a algo m??s adecuado para el t??tulo..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??Y yo qu?? s??!"
            
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
            
            gm "??Te cachondeas de m???"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Bueno,"

            extend " en realidad t?? est??s m??s buena..."

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

            gm "Ya veo que no te quieres tomar m??s en serio estas preguntas..."

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
            
            gm "Ser??a un t??tulo muy simplista..."

            extend " ??No crees?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Me parece un t??tulo razonable."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No es su t??tulo."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Ten??a que probarlo..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
            
        "No tengo ni la m??s remota idea.":
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
            
            gm "Es una obra cl??sica,"

            extend " te guste o no."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Si buscara yo una obra perdida de esa ??poca,"

            pt "seguro que tampoco sabr??a responderme bien..."
            
            jump afternoon04_paint_c_fussli_nightmare_PaintingName
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??C??mo se titula esta obra?" # La pesadilla, tambi??n conocida como el ??ncubo de Johann Heinrich F??ssli. La pesadilla. +1

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    menu afternoon04_paint_c_fussli_nightmare_PaintingName_question:
    
        pt "Este cuadro me da escalofr??os..."
        
        "El ??ncubo."if afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond == False:
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ afternoon04_paint_c_fussli_nightmare_PaintingName_Incubus_Cond = True
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "Aunque esta obra es tambi??n conocida con este nombre,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "no es exactamente su t??tulo."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Pero tambi??n deber??a valer..."

            p "??No?"

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
            
        "El s??cubo.":
            call p_Help
            $ pl.ch_pts("mp",-3)
            
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Un {a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a} es un demonio que toma la forma de una mujer atractiva para seducir a los varones."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows sadx01
            with dissolve
            
            gm "En esta obra es totalmente lo contrario,"

            gm "pues la v??ctima es una mujer y los demonios son varones."

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
            
            pt "No me parece a m?? que estos demonios tomen la forma de un hombre atractivo para seducir a la dama precisamente..."
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
            
        "Par??lisis del sue??o.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Ciertamente se trata de una interpretaci??n folcl??rica de la par??lisis del sue??o."

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
            
            gm "que tiene lugar durante el periodo de transici??n entre el estado de sue??o y de vigilia."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "Durante el episodio,"

            gm "la persona est?? totalmente consciente,"

            gm "con capacidad auditiva y t??ctil,"

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
            
            gm "Anta??o se cre??a que eso era causado por un ??ncubo o duende que oprim??a el pecho del durmiente."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "De ah?? esta representaci??n gr??fica de esta obra."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Entonces,"

            p "he acertado..."

            extend " ??No?"

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
            
            gm "Su t??tulo es {a=https://es.wikipedia.org/wiki/La_pesadilla}{i}The Nightmare{/i}{/a},"

            extend " pero me resulta interesante que supieras lo que representa."
            
            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "Que man??a tiene la pava esta de enrollarse..."
            
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
            
                gm "De hecho tambi??n es conocida como el {a=https://es.wikipedia.org/wiki/??ncubo}??ncubo{/a}."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows angryx04
                with dissolve
                
                gm "Pero as?? es,"

                extend " {a=https://es.wikipedia.org/wiki/La_pesadilla}{i}The Nightmare{/i}{/a} es su verdadero t??tulo."
            
            scene black
            show afternoon04_paint c_fussli_nightmare_02:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with dissolve
            
            gm "De hecho existe otra versi??n de esta obra realizada diez a??os despu??s por el mismo autor."
            
            pt "Sinceramente,"

            extend " no s?? cu??l de las dos im??genes es m??s perturbadora..."
            
            window hide dissolve
            pause
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
        "Resac??n con alucinaciones demon??acas.":
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
            
            p "??Pero no ves a la chica c??mo est???"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "??Qu?? formas son esas de dormir?"

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
            
            gm "??Se supone que me tiene que hacer gracia?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??Qu?? mierda de sentido de humor tiene esta amargada?..."
            
            jump afternoon04_paint_c_alfonsmucha_lepater_Theme
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "??Cu??l es el tema principal de esta obra?" # Ilustraci??n 1899 Alfons Mucha Le pater. El ocultismo y la religi??n. +1
    
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

    extend " ??esta obra es cl??sica?"

    show m_exp_mouth sad_Talkingx03
    with dissolve
    
    gm "Es del a??o 1899,"

    gm "por lo tanto es anterior al siglo XX,"

    extend " y es figurativa."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "??Te rindes?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyebrows normal
    with dissolve
    
    pt "Esto es jugar sucio..."
    
    window hide dissolve
    pause
    
    menu afternoon04_paint_c_alfonsmucha_lepater_Theme_question:
    
        pt "??El tema principal de esta obra? No s??... pero estos ojos brillantes en la oscuridad son algo perturbadores..."
        
        "El espiritismo y la resurrecci??n.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "No negar?? que la mujer de blanco tiene un aspecto algo fantasmag??rico..."

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
            
            gm "Pero no hay ning??n fantasma ni resurrecci??n en esta obra."

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
        
        "El ocultismo y la religi??n.": #Correct
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

            gm "En todas sus ilustraciones se esconde una gran cantidad de s??mbolos {a=https://es.wikipedia.org/wiki/Francmasoner??a}mas??nicos{/a} y ocultistas."

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

            gm "Vemos c??mo un alma es tentada por entidades diab??licas"

            extend " y una figura femenina pura la protege."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "{i}No nos dejes caer en la tentaci??n{/i}."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "Hombre,"

            extend " tanto como \"figura femenina pura\","

            pt "a m?? me da m??s mal rollo la mujer esta con los ojos blancos,"

            extend " que los bichos de atr??s..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "La fantas??a y el folclore.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??En qu?? fantas??a o historia folcl??rica dir??as que se basa en esta obra?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "Yo qu?? s??..."

            p "hay un mont??n que hablan sobre demonios y damas de blanco rescatando a doncellas en apuros."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "En realidad, suele ser m??s bien,"

            gm "pr??ncipe valiente con su armadura y corcel,"

            extend " rescata a princesa cautiva."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "??Eso no son m??s bien las historias ??picas medievales para ni??os?"

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
            
            gm "??Y qui??n es el que est?? muerto?"

            extend " ??y qui??n es el que est?? vivo?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Bueno,"

            extend " la dama de blanco parece como un ente poderoso que est?? resucitando a la mujer que tiene entre sus manos."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Entonces el tema deber??a ser la resurrecci??n, si seguimos tu l??gica..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_Q_AfterInterrogation
        
        "La mitolog??a y la historia.":
            call p_Help
            $ pl.ch_pts("mp",-2)
            
            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "??En qu?? narraci??n hist??rica o mitol??gica te basas para decir que esto forma parte de ello?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "No s??,"

            p "me imagino que en alguna narraci??n griega,"

            extend " con tantos dioses e hijos bastardos de Zeus..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "O quiz??s se basa en las historias medievales sobre los milagros de la Virgen..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Entonces eso ser??a m??s religi??n que mitolog??a,"

            extend " ??no crees?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??Cu??l?"

            pt "??El que he dicho de Zeus,"

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
            
            gm "??Qu???"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "??Cu??l es tu camello?"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "????C??mo?!"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "??A cu??nto el gramo?"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "????De qu?? que cojones est??s hablando?!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Eso t??... "

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "??C??mo cojones quieres que te diga de qu?? co??o va esta obra?"

            extend " Si es la primera vez que la veo..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "..."
            
            jump afternoon04_Q_AfterInterrogation
            
        "No me interesa una mierda responder tus est??pidas preguntas.": #Go to Hell
            
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
    
    gm "Es evidente por qu??."
    
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
        
        gm "Desde luego no eres una masa de m??sculos sin cerebro como pens??..."
        
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
        
        gm "No eres una simple masa de m??sculos sin cerebro al fin y al cabo..."
        
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
        
        gm "No eres una simple masa de m??sculos sin cerebro al fin y al cabo..."
        
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
        
        gm "Quiz??s aprobar??as la Educaci??n Primaria y todo al final..."
        
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
        
        gm "Una masa de m??sculos sin cerebro."

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

        pt "??Qu???"

        extend " ????Pero de qu?? va esta t??a?!"
    
    if Martq >= 9 or Cartq >= 10:

        show m_exp_mouth serious_Silentx01
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows surprisex001
        with dissolve
    
        p "Oye..."

        p "Y todas estas preguntas,"

        extend " ??a qu?? diablos vienen?"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Si no te gustan ya te puedes largar,"

        gm "as?? es como soy."
        
    else:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "Oye, payasa..."

        p "Y todas estas pu??eteras preguntas..."

        extend " ??a qu?? co??o vienen?"

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
        
        p "Has sido t?? quien me ha insultado primero."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows surprisex02
        with dissolve

        gm "Lo ??nico que he hecho es definirte,"

        gm "deber??as sentirte adulado,"

        extend " muchos desear??an tener el cuerpo que t?? tienes."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "Aunque, desde luego,"

        extend " no envidiar??an tu materia gris."

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows normal
        with dissolve
        
        p "Pero,"

        extend "????de qu?? co??o vas?!"

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Si no te gusta,"

        extend " ya te puedes largar,"

        gm "as?? es como soy."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "??Para eso me pediste quedar?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Te \"suger??\" quedar,"

    extend " para que me aclarares qui??n demonios te hab??a dado mi n??mero de m??vil."
    
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "Pero si fuiste t??..."
    
    #Observas como apaga el cigarro y se enciende otro.
    
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Dime,"

    extend " est??s saliendo con Neus..."

    gm "??No es as???"
    
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
    
    gm "Se lo sacaste de su m??vil,"

    extend " ??verdad?"
    #Una sonrisa maquiavelica.
    
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??De qu?? est?? hablando?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "O quiz??s te lo dio ella..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "No..."

    extend " eso no tendr??a sentido..."

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
    
    p "??Conoces a Neus?"

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
    
    gm "S??,"

    extend " la conozco."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    gm "Mucho mejor que t??."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows sadx01
    with dissolve
    
    pt "Woah,"

    extend " ahora me viene a la ofensiva."

    pt "Esta t??a est?? fatal..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows sadx03
    with dissolve
    
    gm "??Te gusta?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris right02
    #show m_pupils right02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "??Te refieres a Neus?"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    gm "No,"

    gm "me refiero a mi co??o,"

    extend " no te jode..."

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows angryx05
    with dissolve
    
    gm "??Claro que me refiero a Neus!"

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx05
    with dissolve
    
    pt "Definitivamente no se parece en nada a la chica de esta ma??ana,"

    pt "es bipolar seguro..."
    
    menu afternoon04_doyoulikeNeus_question:
        
        pt "??Qu?? pu??etas le digo yo a esta loca ahora?"
        
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
            
            gm "??Un favor a un amigo?"

            show m_exp_blush 01
            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve
            
            gm "??Qu?? tipo de favor?"

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
            
            if morning04_ShoppingDidac_Cond == True: #D??dac centro comercial (hace el griter??o, s?? o s??).
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
    
    gm "Tambi??n veo que est??s empezando a conocer a una hermosa pelirroja sin que Neus lo sepa..."

    extend " ??Verdad?"

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
    
    p "??Hermosa pelirroja?"

    extend " ????Qu???!"

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "No te hagas el idiota,"

    extend " un pajarito me ha contado que adem??s tiene muy mal humor"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "cuando la gente se r??e de ella por vestir como una fresca en un lugar p??blico como un centro comercial."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Est?? hablando de D??dac!"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 01
    show m_exp_piris right01
    #show m_pupils right01a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "A saber qu?? estar??ais haciendo en los probadores..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Estaba ayudando a una amiga."

    p "Aunque,"

    extend " ??acaso me esp??as?"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    gm "Qu?? m??s quisieras..."

    gm "pero si te pones a hacer un griter??o en un centro comercial,"

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
    
    gm "As?? que jugando a d??o..."

    gm "??Y conmigo qu???"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "??Buscas el tr??o?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "O quiz??s m??s bien el cuarteto..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "??No te basta solo con la pelirroja?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    menu afternoon04_RedHairGirl_question:
        
        pt "??Qu?? le digo yo ahora?"
        
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
            
        "La pelirroja que t?? llamas es en realidad mi amigo D??dac." if afternoon04_RedHairGirl_DidacRisk_Cond == False:
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

            pt "podr??a poner en peligro su vida,"

            extend " y todo porque esta t??a me est?? provocando..."
            
            jump afternoon04_RedHairGirl_question
            
        "??Est??s celosa?":
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
                
            gm "??Celosa dices?"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
                
            gm "Pobre infeliz,"

            gm "no sabes nada de m??,"

            extend " ??verdad...?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            pt "??A qu?? se refiere?"
            
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

    extend " S??gueme."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils right06a
    show m_exp_eyebrows normal
    with dissolve
    
    menu afternoon04_FollowTxellinMACBA_question:
        
        pt "??Acaso me va a seguir tratando como a un perro todo el rato?"
        
        "??Sabes qu??...? Mejor me voy a casa, no eres lo que me esperaba.":
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
            
        "??Nadie te ha ense??ado nunca educaci??n?":
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
                        
                        p "??Sabes qu???..."

                        p "Tu compa????a no es que sea muy agradable,"
                        
                        p "creo que tendr??s mejores cosas que hacer,"

                        p "especialmente si encuentras a alguien que te aguante."
                        
                        jump afternoon04_GoHome
                
            else:
                
                $ pl.ch_pts("mp",-1)

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex001
                with dissolve
                            
                gm "Mira, ni??ato,"

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
    
    pt "La verdad es que ya empezaba a sacarme de mis casillas la loca del co??o esta..."
    
    jump afternoon04_AloneatHome
            
label afternoon04_FollowTxellinMACBA:

    scene afternoon04_bg macba_posters
    with fade
    
    n "Cerca del portal de la entrada, tres pilares con un cartel enorme en cada uno de ellos te llaman la atenci??n."
    
        #Cartel d??nde aparece el nombre de la chica misteriosa junto con su obra art??stica: El reflexe obscur (?).
    
    pt "??Qu?? diablos me va a querer ense??ar dentro de este \"museo\"?"
    
    n "Observas c??mo le muestra lo que parece ser una acreditaci??n al vigilante de la puerta y ambos consegu??s entrar."
       
       ##---
    
    n "Desde fuera sin duda el edificio MACBA era una espl??ndida obra arquitect??nica, por dentro tampoco decepcionaba."

    scene afternoon04_bg macba_entrance
    with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    stop music fadeout 3.0
    
    n "Quiz??s poco original por el abusivo blanco en todas partes, pero por lo dem??s era bastante imponente."
    
    n "Despu??s de subir por una rampa considerablemente larga, lleg??is a lo que parece ser el primer piso."

    scene afternoon04_bg macba_room01
    with fade

    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
    
    n "Siluetas retorcidas y l??gubres se vislumbran en las ilustraciones -con marco oscuro- colgadas en las paredes blancas,"
    
    n "y una figura negra, brillante y grotesca rellena el espacio vac??o del centro de la sala."

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
    
    gm "??Sabes qu?? diferencia hay entre el arte abstracto y el figurativo?"

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

            extend " antes de afirmar algo y demostrar as?? tu ignorancia."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "..."
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
            
        "Al contrario del arte abstracto, se define por la representaci??n de figuras geom??tricas.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "Figuras geom??tricas..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "??En serio?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "??Entonces en el Cubismo no hay ninguna forma geom??trica?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "En el Cubismo la mayor??a de obras son figurativas."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            gm "T?? lo has dicho,"

            extend " \"la mayor??a\","

            gm "las hay que son totalmente abstractas con formas geom??tricas."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            p "..."
            
            jump afternoon04_MACBA_DifferenceAbsFig_after
        
        "El arte figurativo se define por la representaci??n de formas reconocibles.": #Correct.
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
                
            gm "S??,"

            extend " as?? es."

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

            gm "??Me tomas por imb??cil?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "No s?? qui??n toma por imb??cil a qui??n?"
            
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
                
                gm "Algo tan b??sico,"

                extend " ??no lo sabes?"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows suspiciousx02
                with dissolve
                
                gm "Entonces, ??las preguntas que acertaste antes fueron por pura suerte?"

                show m_exp_mouth happy_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris right04
                #show m_pupils right04a
                show m_exp_eyebrows sadx01
                with dissolve
                
                gm "Qu?? decepci??n..."

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
                
                gm "Por qu?? ser?? que no me sorprende..."

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows angryx01
                with dissolve
                
                p "..."
        
        "??Sabes qu??...? Estoy bastante cansadito de tus est??pidas preguntas.":
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
    
    gm "??Dir??as que el cuadro de {a=https://es.wikipedia.org/wiki/Guernica_(cuadro)}{i}Guernica{/i}{/a} es abstracto o figurativo?"

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    
    menu afternoon04_MACBA_PicassoGuernicaFigurative_question:
        
        pt "??Qu?? pretende con tantas preguntitas?"
        
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
                
                gm "No consigo entender c??mo es posible que alguien que haya respondido tan bien las preguntas sobre {a=https://es.wikipedia.org/wiki/Arte_moderno}Arte Moderno{/a},"
                
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
                
                gm "Quiz??s conozcas bastante sobre {a=https://es.wikipedia.org/wiki/Arte_y_cultura_cl??sicos}arte cl??sico{/a},"

                gm "pero est?? claro que eres un inepto total en cuanto a {a=https://es.wikipedia.org/wiki/Arte_moderno}arte moderno{/a}."
                
            else:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 08
                show m_exp_piris front06
                #show m_pupils front06a
                show m_exp_eyebrows angryx01
                with dissolve
                
                gm "Est?? claro que no entiendes absolutamente nada de arte moderno..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
                
            gm "??Acaso no identificas m??nimamente ojos,"

            gm "bocas,"

            extend " manos,"

            extend " rostros de animales antropom??rficos,"

            extend " una espada rota, ..?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "Euh..."

            extend " Seh..."

            p "Pero dibujados de forma bastante p??sima..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            gm "T?? s?? que eres p??simo..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve
            
            gm "Esto se llama Figuraci??n Deconstruida."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve
            
            gm "Una obra magn??fica e iconogr??fica del siglo XX,"

            gm "retratando los horrores de la {a=https://es.wikipedia.org/wiki/Guerra_civil_espa??ola}Guerra Civil Espa??ola{/a} por {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Pablo Picasso{/a}."
            
            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows serious
            with dissolve

            pt "Ll??malo como quieras,"

            extend " pero estoy seguro de que un ni??o de cinco a??os sabr??a hacerlo mejor..."

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
            
            p "De hecho, es una figuraci??n deconstruida."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve
            
            p "Un cr??tico franc??s llamado {a=https://es.wikipedia.org/wiki/Louis_Vauxcelles}Louis Vauxelles{/a} lo llam?? {a=https://es.wikipedia.org/wiki/Cubismo}Cubismo{/a}."
            
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows normal
            with dissolve

            p "B??sicamente trata la realidad con figuras geometrizadas y con ausencia absoluta de perspectiva y profundidad."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris left02
            #show m_pupils left02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Sin ir m??s lejos,"

            extend " {a=https://es.wikipedia.org/wiki/Pablo_Picasso}Picasso{/a} mismo fue quien inici?? este movimiento con sus {a=https://es.wikipedia.org/wiki/Las_se??oritas_de_Avignon}{i}Se??oritas de Avignon{/i}{/a}."
            
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
            
            gm "??Acaso est??s leyendo la {a=https://www.wikipedia.org/}Wikipedia{/a} por el m??vil?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 01
            show m_exp_piris front01
            #show m_pupils front01a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Al igual que t??,"

            extend " estudio en una escuela de Ilustraci??n."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils right06a
            show m_exp_eyebrows angryx04
            with dissolve
            
            p "No soy simplemente \"{i}un mont??n de testosterona con patas{/i}\"."
            
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

            gm "no puede hacer referencia a algo exterior a la obra en s?? misma."

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
            
            gm "e incluso formas geom??tricas,"

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

            extend " ??No puede haber partes del cuadro que se entiendan y otras que son totalmente abstractas?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            gm "??Te refieres a lo que hac??an en el {a=https://es.wikipedia.org/wiki/Expresionismo}Expresionismo{/a}?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            p "No..."

            p "bueno,"

            extend " no s??..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            gm "Exacto,"

            extend " no tienes ni pu??etera idea."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "La madre que la pari??..."
        
            jump afternoon04_MACBA_PicassoGuernicaFigurative_after
        
        "Es abstracci??n constructiva.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            
            #NOT FINISHED TEXT
            
            scene black
            show afternoon04_paint m_pietm_compositionwithredblueandyellow:
                subpixel True
                xanchor 0.25 yanchor 0.25 zoom 1.0
                easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
            with fade
            
            gm "La {a=https://es.wikipedia.org/wiki/Abstracci??n_constructiva}abstracci??n constructiva{/a} es sin??nimo de recuperaci??n del orden y la racionalidad en el arte frente al {a=https://es.wikipedia.org/wiki/Informalismo}informalismo{/a}."
            
            gm "Como en esta obra de {a=https://es.wikipedia.org/wiki/Piet_Mondrian}Piet Mondrian{/a},"
            
            gm "{a=http://en.roomeon.com/p/composition-with-large-red-plane-yellow-black-grey-and-blue-1921-wall-decoration/3003}Composici??n con un gran plano rojo, amarillo, negro, gris y azul{/a} de 1921."
            
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
        
        gm "pero has respondido mucho m??s bien de lo que me hubiera podido llegar a imaginar..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "??Y se puede saber qu?? diablos imaginabas?"
        
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
        
        gm "No es que se te d?? demasiado bien el arte,"

        gm "pero he conocido a peores que t??..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "??Oye!"

        extend " ??De qu?? vas?"

        show m_exp_mouth sad_Talkingx007
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "??Hey!"

        extend " tranquilo,"

        gm "aprende a aceptar cuando alguien te ofrece un cumplido."

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        pt "????Eso es un cumplido?!"
        
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

        p "??no?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "En absoluto,"

        extend " eres el t??pico musculoso idiota que suelo conocer."
        
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
        
        gm "Reconozco que hab??a aceptado quedar contigo cuando he recibido tu llamada,"

        extend " sencillamente,"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows normal
        with dissolve

        gm "porque sab??a que me caer??as mal."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        pt "????Qu???!"

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        gm "Suelo recibir llamadas de tipos extra??os y desconocidos"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        #show m_pupils front03a
        show m_exp_eyebrows suspiciousx02
        with dissolve
            
        gm "que intentan rid??culamente seducirme sin otro argumento que sus m??sculos"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 03
        show m_exp_piris right03
        #show m_pupils right03a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "rellenados con {a=https://es.wikipedia.org/wiki/Prote??na}prote??nas{/a} artificiales,"

        gm "{a=https://es.wikipedia.org/wiki/Creatina}creatinas{/a} varias,"

        extend " {a=https://es.wikipedia.org/wiki/Amino??cido}amino??cidos{/a},"

        extend " {a=https://es.wikipedia.org/wiki/Gl??cido}carbohidratos{/a}..."
        
        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils right06a
        show m_exp_eyebrows angryx01
        with dissolve

        pt "??De verdad no se acuerda de que fue ella misma quien me dio su n??mero de tel??fono?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris right04
        #show m_pupils right04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "Y pens??,"

        extend " mira..."

        gm "Otro t??pico idiota de los que cuelgan fotos en {a=https://www.facebook.com/}{i}Facebook{/i}{/a} o {a=https://www.instagram.com/}{i}Instagram{/i}{/a},"
        
        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 03
        show m_exp_piris right03
        #show m_pupils right03a
        show m_exp_eyebrows angryx01
        with dissolve

        gm "para mostrar c??mo de efectivas son las inyecciones de {a=https://es.wikipedia.org/wiki/Anabolizante_androg??nico_esteroideo}esteroides anab??licos androg??nicos{/a}."

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows normal
        with dissolve
        
        pt "??Entonces por qu?? acept?? quedar conmigo?"

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

        extend " es m??s inteligente y culto que ellos."

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve
        
        gm "Ni te imaginas la de t??os que hay as?? de imb??ciles..."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 01
        show m_exp_piris front01
        #show m_pupils front01a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "??Para eso hab??as quedado conmigo?"

        extend " ??Para re??rte en mi pu??etera cara?"

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

        extend " reconozco que contigo hab??a otro motivo."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Quer??a descubrir por m?? misma qu?? hab??a visto Neus en ti."

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

        
        p "??Te molesta que salga con Neus?"

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
        
        p "??Por qu???"

        extend " ??Qu?? tipo de relaci??n tienes con Neus?"

        show m_exp_blush 02
        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris left04
        #show m_pupils left04a
        show m_exp_eyebrows angryx04
        with dissolve
        
        gm "Digamos que entre Neus y yo pas?? algo que no es de tu incumbencia."

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

        extend " ????De qu?? vas?!"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        gm "En serio..."

        gm "En los gimnasios,"

        extend " ??os lobotomizan el cerebro?"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "??O es que ya naciste as?? de idiota y los m??sculos no dejan espacio en tu cr??neo?"

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
        
        gm "Adem??s de imb??cil,"

        extend " mis??gino de mierda..."

        gm "El perfecto {i}pack{/i} de {a=https://es.wikipedia.org/wiki/Macho_ib??rico}macho ib??rico{/a} espa??ol."

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        gm "??Hay alg??n estereotipo de gilipollas nacional en el que no encajes?"

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex02
        with dissolve
        
        p "No he venido aqu?? para ser insultado por una ni??a pija repelente sin educaci??n."

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
        
        p "{size=40}????C??MO QUE NO?!{/size}"

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
        
        gm "Quiz??s necesites ayuda profesional..."

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 02
        show m_exp_piris front02
        #show m_pupils front02a
        show m_exp_eyebrows suspiciousx02
        with dissolve
        
        p "{size=35}????Es que quieres que te rompa la puta cara puta asquerosa?!{/size}"

        show m_exp_mouth happy_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front06
        #show m_pupils front06a
        show m_exp_eyebrows serious
        with dissolve
        
        s "????Se puede saber qu?? est?? pasando aqu???!"

        show m_exp_mouth happy_Silentx05
        with dissolve
        
        n "La voz autoritaria de lo que parec??a obviamente un agente de seguridad,"

        show m_exp_mouth happy_Silentx08
        with dissolve
        
        n "detuvo en seco la discusi??n."

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

        extend " ??este tipo te est?? causando alguna molestia?"

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

        tx "??O no es as??...?"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows angryx01
        with dissolve
        
        pt "????Meritxell?!"

        extend " As?? es como se llama esta puta asquerosa..."
        
        pt "??Maldita sea...!"

        pt "Al entrar con acreditaci??n es obvio que la conoce..."
        
        pt "Ser??a una estupidez enfrentarme con el pu??etero segurata de las narices..."
        
        p "S??,"

        extend " ya me iba..."

        jump afternoon04_MACBA_GettingOut

        label afternoon04_MACBA_GettingOut:
        

        if morning04_Shopping_AgentsTalk_Cond == True: #Hablas con agentes en los probadores.
            
            pt "Un segundo..."

            extend " ??Este tipo no es el mismo segurata que hab??a en el centro comercial?"

        show afternoon04_securityagent01_mouth Talking
        with dissolve
        
        s "Acomp????eme a la salida entonces."

        show afternoon04_securityagent01_mouth Silent
        with dissolve
        
        if morning04_ShoppingDidac_Cond == True: #D??dac ha hecho el esc??ndalo en el centro comercial.

            show afternoon04_securityagent01_mouth Silent

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve
        
            tx "Por cierto,"

            extend " ten cuidado,"

            tx "no te encari??es demasiado de la pelirroja,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            tx "porque creo que sabes muy bien qui??n es en realidad..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "????Qu???!"

            extend " ????Sabe algo de la transformaci??n de D??dac?!"

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

        tx "y yo de ti ir??a con cuidado con tener un final feliz cerca de Neus..."

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
        
        pt "????Pero de qu?? pu??etas est?? hablando?!"

        show afternoon04_securityagent01_body:
            subpixel True
            xzoom -1.0
            ease_quad 0.5 zoom 1.5 xanchor -0.0 yanchor 0.1
        show afternoon04_securityagent01_mouth Silent:
            subpixel True
            xzoom -1.0
            ease_quad 0.5 zoom 1.5 xanchor -2.33 yanchor -0.7
        with vpunch
        
        n "Sientes un empuj??n autoritario por parte del agente de seguridad."

        show afternoon04_securityagent01_mouth Talking
        with dissolve
        
        s "Andando."

        show afternoon04_securityagent01_mouth Silent
        with dissolve
        
        pt "??Mierda!..."

        #Cambio de escenario.

        scene afternoon04_bg_macba_outside
        with fade

        stop music fadeout 3.0

        $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx1')
        $ renpy.music.play("audio/sfx/crowd_park_day01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

        n "Seguido celosamente por el agente vuelves a estar en el exterior del museo."
        
        pt "????Qui??n diablos es esta loca del co??o?!"
            
        if morning04_ShoppingDidac_Cond == True: #D??dac ha hecho el esc??ndalo en el centro comercial.
            
            pt "????C??mo pu??etas sabe lo de D??dac?!"
            
        pt "??Y a qu?? cojones se ha referido con lo de Neus?"
        
        pt "Podr??a esperar a que saliera para exigirle respuestas..."
        
        pt "Pero con la atenta mirada del agente de seguridad y estando rodeados de tanta gente,"
        
        pt "ser??a una estupidez forzarla a darme respuestas..."
        
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

        extend " por extra??o que parezca..."
        
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
            
    gm "??En qu?? estilo describir??as lo que hay en el centro de esta sala?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Me acaba de decir en toda la cara que me odia en su fuero interno y ahora act??a tan tranquila..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils left06a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    n "La mirada de la chica cuyo nombre a??n desconoces,"

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
    
    #La c??mara se centra en la figura que hay en medio de la sala... Una pieza art??stica oscura y brillante.
    #goetandocera imagen.

    scene black
    show afternoon04_paint inMACBA_Txell_Mucus:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    window hide dissolve
    pause
    
    pt "??Qu?? demonios es esto?"

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
    
    gm "??Y bien...?"

    show m_exp_mouth serious_Silentx01
    with dissolve
    
    p "??Y bien qu???"

    extend " ??Qu?? quieres que te diga sobre esto?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    gm "??Dir??as que es abstracta o figurativa?"

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

            pt "??Y qu?? pu??etas representa?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y siendo as??..."

            extend " ??Qu?? crees que representa?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "La muy jodida me lo ten??a que preguntar..."

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

            gm "Y siendo as??..."

            extend " ??Qu?? crees que representa?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternoon04_MACBA_Mucus_AbsorFig_after

        "No lo s??." if afternoon04_MACBA_Mucus_AbsorFig_Cond == False:
            call p_Help
            $ afternoon04_MACBA_Mucus_AbsorFig_Cond = True

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Te he preguntado \"dir??as\","

            extend " as?? que pido tu opini??n."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Decir no s??,"

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

        pt "????Qu?? pu??etas le digo yo ahora?!"

        "Es como si un t??o se intentara hacer una auto-felaci??n.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            jump afternoon04_MACBA_Mucus_Represent_after

        "Parece como un 69 fusionado.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            jump afternoon04_MACBA_Mucus_Represent_after

        "Parece como un hombre en posici??n puente al que le cuelgan varios test??culos.":
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

            gm "??En serio?"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "??Realmente crees que es eso lo que representa?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "No s??..."

            extend " es lo que yo veo ah??..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Tienes un grave problema de imaginaci??n entonces..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Yo creo que el que tiene un problema es el que ha hecho esta cosa rara..."

            jump afternoon04_MACBA_Mucus_Represent_after

        "Lo siento, pero sinceramente yo no veo nada aqu??..." if afternoon04_MACBA_Mucus_Represent_Cond == False:

            call p_Help
            $ afternoon04_MACBA_Mucus_Represent_Cond = True

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Sabes que es figurativa y aun as?? no te atreves a dar una respuesta."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "No te estoy pidiendo que lo aciertes,"

            gm "solo he pedido tu opini??n."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "??Tan poco valoras tu criterio?"

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

    pt "??O no?"
    
    #Imagen, nalgas con c??digo de barras.
    scene black
    show afternoon04_paint inMACBA_Txell_StripedAss:
        subpixel True
        xanchor 0.25 yanchor 0.25 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade
    
    n "Os alej??is de la escultura central y a pocos pasos lleg??is frente a un cuadro con una imagen peculiar."

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

    extend " ??qu?? te transmite?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    p "Parecen unas nalgas de mujer,"

    p "con unos c??digos de barra pintados en sangre,"

    extend " o tatuados en rojo por encima."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
       
    gm "He dicho \"qu?? te transmite\","

    extend " no"

    extend " \"qu?? ves\"."

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

            gm "No est?? mal..."

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

            gm "??Acaso t?? traficas con esclavas?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "????Qu???!"

            extend " ??No!"

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

            extend " que somos como ganado exhibi??ndonos en una subasta."

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

            gm "Pero est?? claro que lo piensas por el modo en que te has expresado."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "Esa es tu opini??n..."

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

            gm "No est?? mal..."

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

            gm "Se calcula que en Espa??a hay unas cien mil prostitutas,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "el doble que {a=https://es.wikipedia.org/wiki/Fisioterapia}fisioterapeutas{/a} colegiados y el triple que {a=https://es.wikipedia.org/wiki/Odontolog??a}dentistas{/a}."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Sin embargo,"

            gm "solo un 20\% de ellas son espa??olas,"

            gm "y en torno a un tercio,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "son v??ctimas de la trata de personas,"

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

            gm "Algunas de estas \"esclavas sexuales\" relatan c??mo m??s de la mitad de los clientes,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "tratan de tener sexo con ellas sin {a=https://es.wikipedia.org/wiki/Preservativo}preservativo{/a}"

            gm "y como el 45\% les pide que consuma {a=https://es.wikipedia.org/wiki/Coca??na}coca??na{/a} antes del acto."

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

            gm "??Sigues pensando que es f??cil ganarse la vida vendiendo el culo al mejor postor?"

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
    
    p "??Me vas a preguntar sobre cada \"puto\" cuadro de esta exposici??n?"

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
        
    pt "??Qu?? cojones pretende?"

    scene afternoon04_bg macba_entrance
    with fade
    
    n "Segu??s avanzando a lo largo de la galer??a dejando atr??s varias obras pict??ricas enmarcadas en la pared"

    scene afternoon04_bg_macba_room02
    with fade
    
    n "hasta llegar a otra sala id??ntica a la anterior con distintos cuadros y otra pieza \"art??stica\" en medio de la sala."

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

    extend " ??qu?? te transmite esta otra obra?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "????Qu?? narices?!"

    play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0

    scene black
    show afternoon04_paint inMACBA_Txell_ManTable:
        subpixel True
        xanchor 0.10 yanchor 0.35 zoom 1.0
        easein_quad 25.0 xanchor 0.0 yanchor 0.0 zoom 0.25
    with fade

    window hide dissolve
    pause
    
    n "Una mesa de cristal sujeta por un hombre de pl??stico a cuatro patas con un traje de l??tex"
       
    n "que le cubre el cuerpo entero excepto las partes nobles y sus ojos,"
    
    n " los cuales miran fijamente a un espejo por el que se ver??a reflejada su entrepierna cubierta por un candado."

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
    
    gm "??Y bien?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    window hide dissolve
    pause

    menu afternoon04_MACBA_ManTable_Transmit_question:

        pt "??Qu?? me transmite semejante humillaci??n masculina?"

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

                p "o en general una visi??n del mundo."

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 03
                show m_exp_piris left03
                #show m_pupils left03a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                p "Esta obra de aqu?? es simplemente..."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows surprisex001
                with dissolve

                gm "Contin??a..."

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

                gm "Eres un buen conocedor del arte cl??sico,"

                extend " pero, desde luego;"

                gm "te queda mucho que aprender del arte moderno."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front03a
                show m_exp_eyebrows surprisex02
                with dissolve

                p "??No puedo tener una opini??n?"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                #show m_pupils front04a
                show m_exp_eyebrows suspiciousx02
                with dissolve

                gm "??Y qu?? opini??n tienes sobre esta obra?"

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

                gm "??te crees con la libertad de juzgar a un artista de esta manera?"

                show m_exp_mouth serious_Silentx01
                show m_exp_eyes 03
                show m_exp_piris front03
                #show m_pupils front043
                show m_exp_eyebrows surprisex001
                with dissolve

                p "??T?? me has pedido mi opini??n!"

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

        "La representaci??n de un hombre que ha perdido completamente la cordura.": 
            call p_Help
            $ pl.ch_pts("mp",-5)

            label afternoon04_MACBA_SadomasoquismAngry:

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "??Est??s diciendo que todo aquel que disfrute de la sumisi??n en el {a=https://es.wikipedia.org/wiki/Sadomasoquismo}sadomasoquismo{/a}"

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

            p "??Yo no he dicho que sea un enfermo!"

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

            p "Un poco de ayuda no le vendr??a mal en estos casos."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Si piensas as??,"

            extend " realmente eres un miserable."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "??Oye!"

            p "No hace falta insultar."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "T?? me has insultado a m??."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "??Te gusta el {a=https://es.wikipedia.org/wiki/Sadomasoquismo}sadomasoquismo{/a}?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "M??s concretamente el {a=https://es.wikipedia.org/wiki/BDSM}BDSM{/a}."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "????Me est??s diciendo que disfrutar??as siendo usada como apoyo de mesa estando amordazada y esclavizada?!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "En realidad mi rol en este tipo de juegos es m??s bien de dominante."

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

            gm "Est??s afirmando que estoy tratando con gente enferma a la que le gusta que la traten de esta manera."

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

            gm "??Qui??n te crees que eres para opinar de forma tan est??pida sobre algo que claramente desconoces por completo?"

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

            gm "ya no me interesa en lo m??s m??nimo seguir hablando contigo."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No s?? qu?? ha visto en ti Neus..."

            gm "pero me imagino que no durar??is mucho."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows serious
            with dissolve

            p "Eso ser?? tu opini??n,"

            p "pero vaya, viendo lo que te gusta,"

            p "me imagino que un poco de ayuda profesional,"

            extend " no te vendr??a mal."

            stop music fadeout 3.0

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows serious
            with dissolve

            s "Meritxell,"

            extend " ??hay alg??n problema?"

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

            n "La voz imponente de un agente de seguridad del museo par?? en seco la conversaci??n que estabais teniendo."

            pt "??Meritxell?"

            extend " ??Es as?? como se llama esta chica?"

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

            tx "Creo que el caballero sabe perfectamente d??nde est?? la salida."

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

            s "Acomp????eme."

            show afternoon04_securityagent01_mouth Silent
            with dissolve

            p "??No le ha dicho la se??orita {b}Meritxell{/b},"

            p "que ya s?? d??nde est?? la salida?"

            jump afternoon04_MACBA_GettingOut

        "La {b}sumisi??n masculina{/b} en su m??xima expresi??n.": #Correct
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ inMACBAq += 1 #If the answer is correct.

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "??Qu?? te hace pensar eso?"

            jump afternoon04_MACBA_ManTable_Transmit_after

        "??No es esto denunciable?": 
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

            p "El cuadro anterior presumo que es una denuncia a la prostituci??n forzada..."

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

            gm "??Crees que no existen los hombres que disfrutan de la sumisi??n?"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "??Acaso te ofende porque te sientes identificado...?"

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

                    gm "??Entonces?"

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

                    gm "O quiz??s es porque no has estudiado bien la obra que tienes en frente..."

                    jump afternoon04_MACBA_ManTable_Transmit_after

                "Quiz??s.":
                    call p_Help
                    $ pl.ch_pts("mp",+1)
                    $ inMACBAq += 1 #If the answer is correct.

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    gm "??En serio?"

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

                    gm "Expl??cate..."

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

    p "para una mesa por la cual se puede ver a trav??s."
    
    p "El hecho de que solo tenga expuestas sus partes nobles,"
       
    p "con el culo al aire, con espacio suficiente por si alguien quiere darle \"amor\" por detr??s,"
    
    p "con la mirada fija en un espejo que le refleja sus cojones colgando y su polla encerrada con candado..."
    
    p "No ofrece demasiadas dudas respecto a si es o no sumiso."
    
    p "Eso sin mencionar que el l??tex siempre se ha relacionado con el {b}masoquismo{/b},"
    
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
    gm "Parece como si hubieras usado alguna vez ropajes de l??tex..."

    play sound "audio/sfx/fall02.ogg"

    hide whisper_mc_front
    show whisper_tx_mouth happy_Silent
    with hpunch

    #Te apartas de ella, en el dibujo tu cabeza desaparece y solo se ve a ella sonriendo en primer plano sin ojos.
    
    p "??Euh!"
    
    n "El c??lido aliento detr??s de tu oreja -tan repentino e inesperado-, consigue sobresaltarte ligeramente."

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

    p "????Qu?? haces?!"

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
    
    gm "??Me equivoco?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    pt "Toma cambio de tema..."

    pt "aunque para ser justos,"

    extend " me ha tra??do a esta exposici??n para algo..."

    pt "Me imagino..."

    menu afternoon04_MACBA_ManTable_Dominance_question:

        pt "Por lo que me ha estado contando, ella tiene poco de sumisa..."

        "As?? es, soy cien por cien dominante.":
            call p_Help
            $ pl.ch_pts("mp",+1)
            $ TxellSlave -= 1

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Quiz??s pienses eso,"

            gm "porque nunca has estado con una mujer que sepa realmente c??mo doblegar tu hombr??a..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??Les preguntas lo mismo a las mujeres homosexuales que no han estado con hombres?"

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

            gm "Ah?? has sido agudo, [protname],"

            extend " lo reconozco..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y hablando de edades..."

            #gm "??Qu?? edad dir??as que tengo? Hombret??n..."

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

            gm "??Totalmente sumiso?"

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

            gm "??Y te ponen m??s las jovencitas o las maduritas?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            menu afternoon04_MACBA_ManTable_Domaninace_Age_question:

                "Me ponen m??s las jovencitas.":
                    call p_Help
                    $ pl.ch_pts("mp",-1)

                    show m_exp_mouth happy_Talkingx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "As?? que sumiso pervertido..."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    gm "Pill??n..."

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    gm "Y dime..."

                    jump afternoon04_MACBA_ManTable_Dominance_after

                "Me ponen m??s las maduritas.":
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

                "??Y qu?? te hace pensar que solo me atraen las mujeres?":
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

                    gm "Por algo ser??..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    p "Quiz??s disfruto de la visi??n de tu cuerpo,"

                    p "pero eso no significa que no me pueda atraer el mismo sexo..."

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    gm "Si t?? lo dices..."

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

        "La verdad es que lo que m??s disfruto es ser sumiso cuando quien me domina sabe lo que hace.":
            call p_Help
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "As?? que sumiso..."

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

            gm "??Y qu?? hace falta para que alguien te domine?"

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

            #gm "??Qu?? edad dir??as que tengo? Hombret??n..."

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

            gm "Quiz??s porque siempre te has acostado con \"quincea??eras\"."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve
            
            p "Me he acostado con mujeres m??s maduras que t??..."

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
            
            gm "??S??...?"

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
    
    gm "??Qu?? edad dir??as que tengo?"

    extend " Hombret??n..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    menu afternoon04_MACBA_TxellAge_question:

        pt "Pregunta venenosa... Si le digo menos, la tratar?? de ni??a; y si le digo m??s, la tratar?? de vieja..."

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

            gm "??Te crees que conjeturar, seg??n tu opini??n, que soy una adolescente, a modo de elogio barato,"

            gm "te va a funcionar?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Quiz??s si hubieras disimulado un poco m??s,"

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

            p "??Insin??as que una chica mayor de dieciocho,"

            extend " pero menor de veinte,"

            p "es menos mujer que t???"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "??En qu?? te basas para decir eso?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "La edad no es siempre lo ??nico que importa realmente en una persona."

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

            extend " con las chicas que a duras penas han llegado a la mayor??a de edad..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Esa es tu opini??n..."

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

            gm "??Tan madurita me ves?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve
            
            pt "??La habr?? cagado?"

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

            gm "??Tan madura me ves?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "??La he cagado?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No, [protname],"

            extend " no tengo m??s de treinta y cinco..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "S??,"

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

            gm "{size=40}????QU???!{/size}"

            show m_exp_mouth sad_Talkingx12
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "????Se puede saber en qu?? parte de m?? aparento tener m??s de cuarenta a??os?!"

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            p "No s??..."

            p "se te ve una mujer inteligente,"

            extend " madura,"

            extend " desarrollada..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "??Que est?? desarrollada y sea inteligente no hace que me pongas m??s de diez a??os encima!"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve

            s "??Hay alg??n problema?"

            $ afternoon04_MACBA_Agent01Talk_Cond = True #Habla con el agente 01 en el MACBA.

            show afternoon04_securityagent01_body:
                MACBA04_securityagent01_pos
            show afternoon04_securityagent01_mouth Silent:
                MACBA04_securityagent01_mouth_pos
            with dissolve

            n "Debido a su agudo tono de voz,"

            n "hab??a llamado la atenci??n del agente de seguridad del museo."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No,"

            extend " no,"

            extend " tranquilo..."

            gm "Solo me he puesto nerviosa porque me ha dicho que aparento tener m??s de cuarenta a??os..."

            show afternoon04_securityagent01_mouth Talking
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris left03
            #show m_pupils left03a
            show m_exp_eyebrows angryx01
            with dissolve

            s "Este t??o es idiota."

            s "??Quieres que lo eche a patadas?"

            show afternoon04_securityagent01_mouth Silent
            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "No,"

            extend " gracias,"

            gm "en el fondo le he pedido su opini??n."

            gm "No puedo enfadarme por ello."

            if morning04_Shopping_AgentsTalk_Cond == True: #Hablas con agentes en los probadores.
                
                pt "Un segundo..."

                extend " ??Este tipo no es el mismo segurata que hab??a en el centro comercial?"

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

            gm "{size=35}??Me lo he tomado fatal!{/size}"

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

            pt "Quiz??s soy yo,"

            extend " pero a veces me cuesta entender a las mujeres as??..."

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

            gm "Ser?? mejor cambiar de tema..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            pt "S??,"

            extend " quiz??s ser?? lo mejor..."

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

            gm "??Me est??s diciendo que mentalmente soy una inmadura?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "??Euh?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "??Yo no he dicho eso!"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            gm "No me evadas la pregunta, [protname],"

            extend " responde."

            gm "??Qu?? edad dir??as que tengo?"

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

    gm "??Has usado l??tex o cuero en alg??n encuentro ??ntimo?"

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

    pt "Est?? claro que no me va a revelar la edad exacta que tiene..."

    menu afternoon04_MACBA_LatexUse_question:

        pt "??L??tex o cuero? ??Pero qu?? entiende esta mujer por sexo...?"

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

            extend " aunque es una l??stima que no te haya gustado lo suficiente."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Es probable que fuera con una ni??ata quincea??era,"

            gm "que no tuviera ni pu??etera idea de lo que hac??a..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows normal
            with dissolve

            p "Opinas sobre algo de lo que no tienes ni idea..."

            p "adem??s,"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "puedo tener mi opini??n,"

            extend " ??no?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Tambi??n puedes cambiar de idea,"

            extend " ??verdad?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "??A qu?? viene ese inter??s para saber si me podr??an gustar o no estas cosas?"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??Acaso admites que quiz??s te puedan atraer los hombres?"

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

            gm "Pero confieso que me despiertas inter??s,"

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

            p "??A qu?? viene entonces la pregunta del l??tex?"

            #gm "El l??tex es un material que requiere una serie de cuidados," 
            jump afternoon04_MACBA_LatexUse_after

        "Me encantar??a someterte vestida as??.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave -= 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "??Te gustar??a...?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??Por supuesto!"

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

            gm "Qu?? novedad..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "No eres nada original,"

            extend " ??sabes?"

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

            gm "Con esa actitud de ni??ato consentido,"

            extend " ??pretendes seducirme?"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "??Con qu?? mierda de ni??atas has estado?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "??O es que en realidad eres m??s de encerrarte en una habitaci??n con tu amiga \"la mano derecha\","

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "jugando o viendo historias,"

            extend " con personajes con \"{a=https://es.wikipedia.org/wiki/Muerte_encef??lica}encefalograma plano{/a}\","

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "y de ni??itas que dicen tener dieciocho,"

            gm "pero que aparentan quince"

            extend " y tienen tetas tan grandes como su cabeza?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "Como si tus tetas fueran enanas..."

            extend " ??No te jode!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "??A qu?? viene entonces la preguntita sobre el l??tex y el cuero de las narices?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Hmm..."

            #gm "El l??tex es un material que requiere una serie de cuidados," 
            jump afternoon04_MACBA_LatexUse_after

        "Me encantar??a que me sometieras mientras yo me visto as??.":
            call p_Help
            $ pl.ch_pts("mp",-1)
            $ TxellSlave += 1

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "Ya s?? que te gustar??a."

            gm "No ser??as el primero..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Pens?? que no te gustaban los hombres..."

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

            p "??Entonces?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Me gusta la dominaci??n."

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

            extend " y m??nimamente culto."

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

            gm "Ni siquiera tendr??a que llegar a tocarte para que te corrieras como un caballo en celo desbocado."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            pt "No se lo tiene cre??do la t??a ni nada..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            gm "S?? que ahora mismo eres incapaz de ser consciente de las posibilidades..."

            #gm "El l??tex es un material que requiere una serie de cuidados," 
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

            gm "\"La curiosidad mat?? al gato\"."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            gm "Pero en realidad es una mala traducci??n,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "ya que proviene de una expresi??n inglesa del siglo XVIII,"

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

            gm "{i}Care{/i} significa preocupaci??n,"

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

            gm "Qu?? vida m??s m??sera y olvidable vivir??amos si no fu??ramos curiosos."

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

            extend " es una pena que pienses as??..."

            jump afternoon04_MACBA_LatexUse_after

label afternoon04_MACBA_LatexUse_after:

    play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
            
    gm "El {a=https://es.wikipedia.org/wiki/Fetichismo_de_l??tex}l??tex{/a} es un material que requiere una serie de cuidados," 

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows normal
    with dissolve
        
    gm "de lo contrario puede estropearse muy r??pido."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    n "Su tono de voz es distinto, m??s calmado, m??s femenino, m??s evocador..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    gm "Aplicar un abrillantador sobre la superficie,"

    gm "y talco en el rev??s forma parte del ritual."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "La fuerte estimulaci??n er??tica provocada por el l??tex se basa,"

    extend " ante todo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    gm "en la visi??n del cuerpo ce??ido y realzado."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows sadx01
    with dissolve
    
    gm "El tacto"

    extend " y el olor caracter??stico del caucho,"

    gm "tambi??n entran en juego."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "El sonido del roce de dos cuerpos vestidos con l??tex es especialmente estimulante para los {a=https://es.wikipedia.org/wiki/Fetichismo_sexual}fetichistas{/a},"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "que en ocasiones,"

    extend " llegan a hacer el amor en una cama con s??banas de l??tex. "
    
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
    
    gm "Otros disfrutar??n pensando en la idea de sentirse \"como aprisionados\","

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows sadx03
    with dissolve

    gm "y por lo tanto,"

    extend " preferir??n los trajes de cuerpo entero percibiendo las partes m??s sensibles del cuerpo,"

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
    
    gm "O incluso la sensaci??n de sentirse maltratados por su propia prenda..."

    #Como se acerca un poco m??s.

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
    
    gm "creando un personaje para exhibir un mayor {a=https://es.wikipedia.org/wiki/Atracci??n_sexual}{i}sex-appeal{/i}{/a},"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
        
    gm "para satisfacci??n del sumiso fetichista."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "La presi??n,"

    extend " sentir tu cuerpo ce??ido,"

    extend " comprimido,"

    extend " encerrado."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Incluso el hecho de usar una m??scara para eliminar completamente la identidad,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows sadx05
    with dissolve
    
    gm "releg??ndote a simple \"objeto\""

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

    gm "en s??mbolo de sumisi??n absoluta a tu due??a..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Realmente est?? muy cerca..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Dime, [protname],"

    gm "??crees que no disfrutar??as de esta experiencia dej??ndote llevar completamente como sumiso?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    menu afternoon04_MACBA_LatexSubmissive_question:

        pt "??Me est?? intentado seducir o intenta convertirme en su mu??eco?"

        "Desde luego que s??.":
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

            extend " cre??a que ofrecer??as m??s resistencia..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "??Por?"

            show  m_exp_blush 01
            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            gm "Tienes pinta de ser el t??pico {a=https://es.wikipedia.org/wiki/Macho_ib??rico}macho ib??rico{/a} espa??ol que no permite que se le manche su masculinidad..."

            show  m_exp_blush 00
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "A veces las apariencias enga??an..."

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

        "Me est??s dando miedo...":
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

            gm "??Te doy miedo?"

            show  m_exp_blush 02
            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            gm "Y eso que no has visto nada a??n..."

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
    
    p "??Ey!"
    
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
    
    p "????Qu?? haces?!"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
    
    gm "Si dices que no lo disfrutar??as en absoluto,"

    gm "??a qu?? se debe esa erecci??n matutina?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "????Qu???!"

    scene black
    with dissolve
    
    n "Con el roce del momento no te hab??as percatado, pero efectivamente tu miembro estaba terso y duro como una roca"
    
    n "haciendo cierta presi??n debajo de de la tela de ropa que la cubre."

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
    
    gm "Co??o..."

    extend " Pedazo de paquete gastas..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris down03
    #show m_pupils down03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    gm "??Es que eres tataranieto de {a=https://es.wikipedia.org/wiki/Grigori_Rasput??n}Rasput??n{/a}?"

    extend " ??o qu???"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "La erecci??n la tengo por tenerte tan cerca y por tu tono de voz..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "??No por lo que me has contado!"

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

    extend " all?? t??..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "??Se puede saber qu?? pretendes?"

    p "Pensaba que hab??as dicho que no estabas interesado en m??..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Estoy curiosa de saber por qu?? le interesas a Neus,"

    extend " ya te lo he dicho."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Qu?? rollo se llevar?? esta con Neus?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris down03
    #show m_pupils down03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    gm "Aunque es evidente que yo s?? te atraigo."

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
    
    gm "Pero lo tienes bastante dif??cil para que yo me interese por ti,"

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

            gm "T?? mismo..."

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

            gm "Para qu?? perder m??s el tiempo..."

            extend " ??No?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            gm "Qu?? mentalidad m??s desesperadamente arcaica y {a=https://es.wikipedia.org/wiki/Ingenuidad}na??f{/a}..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            # NOT FINISHED "Dibujo: poner mano en el bolsillo para sacar un dispositivo con bot??n rojo."

            n "De su bolsillo saca lo que parece una especie de dispositivo con un bot??n rojo."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "??Qu?? es eso?"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            gm "Nada que te importe,"

            extend " ??No te ibas?"

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "A??n no me has dicho de qu?? conoces a Neus."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris left04
            #show m_pupils left04a
            show m_exp_eyebrows normal
            with dissolve

            s "??Hay alg??n problema con este caballero?"

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

            extend " ??As?? es como se llama esta rubia tetona?"

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

            tx "??No es as??...?"

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

            p "S??,"

            extend" supongo que s??..."

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

    n "tus pasos te llevan a lo que ser??a la siguiente sala."

    n "Predomina un color rosado combinado con otros colores vivos,"
    
    n "con unas figuras dulces y entra??ables en los cuadros colgados en las paredes de la nueva sala."
    
    n "Paraguas en los que cuelgan hilos con trozos de arco??ris como si fueran bolas de nieve por la sala,"
       
    n "letras infantiles por todas partes de todos los colores imaginables,"
    
    n "y una figura de un pez de est??tica gr??cil -con ojos saltones y enternecedores-,"

    n "ocupa el centro de la sala."
    
    gm "[protname],"

    extend " ??se puede saber a d??nde vas?"
    
    gm "Eso es otra exposici??n."
    
    p "..."
    
    pt "Ya dec??a yo..."

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
    
    gm "??Es que acaso no has visto el panfleto en la entrada sobre lo que se expone en el museo este mes al entrar?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "S??..."
       
    pt "pero quiz??s no le he prestado suficiente atenci??n..."

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
        
    gm "??No has le??do mi nombre ah???"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "??Tu nombre?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    gm "Supongo que sabes c??mo me llamo..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    gm "??Verdad?"

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
    
    gm "No tendr??s los suficientes \"cojones\" como para quedar con una chica que pretendes tirarte y ni siquiera sabes c??mo se llama..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "??Y qu?? te hace pensar que quiero follarte?"

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
        
    gm "tu erecci??n,"

    extend " que sigue estando igual,"

    gm "creo que responde a tu pregunta."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Me cago en la polla..."

    extend " ????Es que no sabes disimular jod??a?!"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    gm "Y bien,"

    extend " ??c??mo me llamo?"

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

        "M??riam.":
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

            tx "despu??s de todo..."

            show m_exp_blush 01
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve
            
            pt "??Qu?? ??ordo de concepto tiene esta t??a de m???"

            jump afternoon04_MACBA_TxellName_after

        "Meredith.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "Mar??a.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TxellName_Fail

        "??Todo esto que hemos visto es obra tuya?" if afternoon04_MACBA_TxellName_silence == False:
            call p_Help
            $ afternoon04_MACBA_TxellName_silence = True

            show m_exp_eyebrows angryx01
            show m_exp_mouth sad_Talkingx06
            with dissolve

            gm "No me cambies de tema, listillo..."

            show m_exp_eyebrows serious
            show m_exp_mouth sad_Talkingx05
            with dissolve

            gm "??C??mo me llamo?"

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

    pt "Un nombre catal??n,"

    extend " catal??n..."

    show m_exp_blush 01
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "Jodido de pronunciar el cabr??n, adem??s..."

    show m_exp_blush 02
    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows surprisex001
    with dissolve

    pt "El que le puso este nombre,"

    pt "parece que quiere ver c??mo la gente de otras lenguas lo pronuncia mal..."

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

    p "??Se puede saber por qu?? hemos venido aqu???"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Te he tra??do aqu?? para que me des tu opini??n como ilustrador,"

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

        tx "experto en arte cl??sico;"

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

        tx "conocedor de historia del arte cl??sico;"

    else:

        show m_exp_blush 00
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "aunque en arte quiz??s no eres un experto,"

        extend " apreciar??a igualmente tu opini??n sobre mi obra."


    if (Cartq or Martq) >= 10:
        extend " sobre mi obra."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "??No hab??as dicho que me hab??as hecho venir para re??rte en mi jodida cara?"

    show m_exp_blush 01
    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Como sueles hacer con otros tipos que te llaman por el m??vil,"

    extend " por lo visto..."

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve 
    
    tx "S??."

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
        
            extend " viendo que eres todo un ilustrado de la cultura art??stica,"

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            tx "ahora me interesa realmente tu opini??n."

        elif Martq >= 9 or Cartq >= 10:
        
            extend " viendo que tampoco se te da tan mal la cultura art??stica,"

            show m_exp_mouth happy_Talkingx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "ahora me interesa tu opini??n."

    else:

        show m_exp_blush 00
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        #show m_pupils front04a
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "aunque en arte quiz??s no eres un experto, apreciar??a igualmente tu opini??n sobre mi obra."

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
    
    tx "Si sigues aqu??,"

    extend " es porque al fin y al cabo tampoco detestas del todo mi compa????a."

    show m_exp_blush 01
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Si sigo aqu??, es quiz??s,"

    extend " porque al igual que t??,"

    p "tambi??n soy alguien curioso."

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

    pt "Jodida loca del co??o..."

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "Y bien [protname],"

    extend " ??qu?? te ha parecido mi obra?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve

    menu afternoon04_MACBA_TxellHerArt_question:

        pt "??..Todo lo expuesto en este museo es obra de esta t??a?"

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

            tx "??Excitante?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??Por qu??...?"

            show m_exp_blush 01
            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Tengo la sensaci??n de que sabes mucho m??s de lo que cuentas."

            show m_exp_blush 02
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "No has creado todo lo que hay en esta galer??a por simple amor al arte,"

            p "o para pagar tus impuestos."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Algo me dice que es tambi??n tu modo de vida,"

            p "la ra??z de tu curiosidad y tu pasi??n."

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

            tx "??Por qu???"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??Porque se aleja de los convencionalismos tradicionales?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "??Porque no hablo de practicar el sexo ??nicamente despu??s del matrimonio y solo para procrear?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "??Es que tienes pensado ingresar en una hermandad religiosa?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Cachond??ate lo que quieras..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Pero no me parece muy normal que alguien se emperifolle de pl??stico negro por todo su cuerpo desnudo y sudoroso,"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "mientras una loca s??dica y enfermiza"

            p "le est?? dando con un l??tigo,"

            extend " o vete t?? a saber qu??..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Eso sin mencionar que todas las obras aqu?? expuestas giran en torno al sexo,"

            extend " pero al sexo retorcido..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            p "????Es que no sabes disfrutar de una compa????a agradable y normal?!"

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

            tx "??Qu?? entiendes por \"normal\"?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "No me vengas con rollos psicoanal??ticos ahora..."

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

            tx "??Intrigante?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??Por qu??...?"

            show m_exp_blush 01
            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve
                
            p "Me hace preguntarme qu?? tipo de experiencias habr??s vivido,"

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

            tx "Creo que nunca hab??an definido mi obra de forma tan hastiada"

            extend " y sopor??fera."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Bueno,"

            extend " es mi opini??n,"

            p "no s??,"

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

            tx "??Suerte que no te ha parecido mala pues!"

            tx "No s?? qu?? hubieras dicho entonces..."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "??Es que no sabe aceptar una opini??n...?"

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
        
    tx "As?? que no sabes a qu?? me dedico,"

    extend " ??verdad?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "??No eres artista?"

    show m_exp_blush 00
    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front06
    #show m_pupils front06a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Lo soy,"

    extend " pero no es mi ??nico oficio."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Hay algo que no entiendo,"

    p "viendo que ya tienes una proyecci??n profesional bien encarrilada,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "??por qu?? vienes a clase de Ilustraci??n?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "El saber no ocupa lugar,"

    tx "siempre me ha gustado aprender cosas nuevas,"

    tx "y quiero expandir mis habilidades art??sticas."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris down04
    #show m_pupils down04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Especialmente,"

    extend " en anatom??a masculina."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "??Hay algo de malo en ello?"

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
    
    p "??Cu??l es tu otro oficio?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "??De verdad quieres saberlo?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "No lo preguntar??a si no me interesara..."
    
    pt "Tampoco es que me dejes ninguna otra opci??n..."

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
        
    tx "??A qu?? dir??as que me dedico profesionalmente?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    menu afternoon04_MACBA_TxellJob_question:

        pt "Si existiera el oficio, ser??a el de toca-cojones profesional, con tanta preguntita de las narices..."

        "Dise??adora de moda especializada en l??tex.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Aunque reconozco que el trabajo de {a=http://www.latexwiki.com/index.php?title=Atsuko_Kudo}Atsuko Kudo{/a},"

            extend " la mejor dise??adora de moda en l??tex,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "es excepcional,"

            extend " y es posible que, en alguna ocasi??n,"

            tx "pudiera llegar a llevar alg??n traje suyo en alguna gala o exposici??n,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            tx "no es realmente de mi gusto llevar l??tex fuera de las fantas??as er??ticas."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Creo que cubierta de un l??tex oscuro,"

            extend " ce??ido al cuerpo,"

            extend " con el estilismo de una buena dise??adora,"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "no te quedar??a nada mal..."

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

            tx "Pero digamos que me gusta mantener separados mis encuentros ??ntimos,"

            extend " mi trabajo,"

            extend " y mi vida personal."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Cuando entro en el juego de la seducci??n,"

            extend " me pongo una m??scara,"

            tx "y esa m??scara en parte,"

            extend " es el l??tex que me cubre el cuerpo desnudo."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "As?? que, aunque no me disguste para nada el dise??o de {a=http://www.latexwiki.com/index.php?title=Atsuko_Kudo}Atsuko Kudo{/a},"

            tx "veo dif??cil que alg??n d??a pueda llevar una prenda suya,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "y mucho menos, ser yo quien la pueda dise??ar."

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

            tx "??En serio me ves como una puta de lujo?"

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

            extend " yo no lo hubiera expresado as?? quiz??s..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??C??mo, entonces?"

            tx "??Acompa??ante?"

            extend " ??Dama de compa????a?"

            extend " ??Trabajadora sexual para ricachones?"

            extend " ??{a=https://es.wikipedia.org/wiki/Chica_de_compa????a}{i}Call-Girl{/i}{/a}?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Caray..."

            extend " s?? que te sabes maneras distintas de llamar esta \"profesi??n\"..."

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

            p "??A qu?? te refieres?"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            tx "A veces ser una dama de compa????a,"

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

            extend " galer??a,"

            extend " o hasta un funeral."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris right03
            #show m_pupils right03a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Hay que saber mantener las apariencias sin destacar m??s de lo necesario o solicitado por el cliente."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "Adem??s,"

            extend " eso implica ser expuesta en grupos sociales de alto grado econ??mico,"

            tx "si no sabes llevarlo bien,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "puede arruinar tu reputaci??n"

            extend " y luego impedirte llegar a tener una vida \"normal\"."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "..."

            p "Me da la sensaci??n de que conoces bastante bien el oficio..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Lo conozco as?? de bien,"

            extend " porque durante unos a??os fue una de mis profesiones para pagarme los estudios superiores."

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

            tx "??Te desagrada que haya sido una puta de lujo?"

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

                    tx "??Y qu?? m??s te da?"

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

                    tx "y especialmente este co??o seco como el desierto,"

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

                    extend " pero est?? claro que tu polla, por lo menos,"

                    tx "tiene esa ilusi??n."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    p "????Por qu?? no dejas de mirarme la polla?!"

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

                    tx "supongo que ser??n gajes del oficio..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    pt "Puta..."

                    jump afternoon04_MACBA_TxellJob_after

                "En realidad, creo que eso te hace m??s interesante a??n.":
                    call p_Help
                    $ pl.ch_pts("mp",+2)

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "??Por qu???"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "??Te crees que voy a poner en pr??ctica lo aprendido contigo para que disfrutes de mi compa????a gratuitamente?"

                    show m_exp_mouth sad_Silentx02
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "Estoy seguro de que aprendiste tambi??n muchas cosas aparte de las que obviamente supongo que se te dan muy bien."

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

                    p "Es evidente que sabes c??mo tratar a las personas,"

                    extend " y si no voy mal encaminado,"

                    show m_exp_mouth serious_Silentx01
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    #show m_pupils right04a
                    show m_exp_eyebrows serious
                    with dissolve

                    p "los estudios que te pagaste,"

                    extend " seg??n mencionaste antes,"

                    p "muy probablemente eran sobre psicolog??a"

                    extend " o filosof??a..."

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

                    tx "No s?? muy bien c??mo tomarme este comentario..."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    #show m_pupils front03a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "T??matelo como quieras,"

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

                    tx "te lo contar?? de todos modos..."

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    #show m_pupils front04a
                    show m_exp_eyebrows angryx01
                    with dissolve

                    pt "??Es que no me ha o??do...?"

                    jump afternoon04_MACBA_TxellJob_definition
            

        "Hacker.":
            call p_Help
            $ pl.ch_pts("mp",-3)

            jump afternoon04_MACBA_TxellJob_wrong

        "Psic??loga.":
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

            pt "Mira t??,"

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

            tx "??Tanto se me nota?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows normal
            with dissolve
            
            p "Tu conversaci??n sobre el l??tex,"

            extend " tu aparente aprecio por la dominaci??n,"

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
            
            p "..." #Sonrisa p??cara.

            jump afternoon04_MACBA_TxellJob_definition

        "Directora de Arte en una empresa de dise??o.":
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

    tx "No s?? de d??nde demonios has sacado esta idea..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    pt "No s??..."

    extend " ten??a que probar..."

    jump afternoon04_MACBA_TxellJob_definition

label afternoon04_MACBA_TxellJob_definition:

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Soy {b}psic??loga-dominatrix{/b},"

    extend " especializada en conductas sexuales masculinas y de pareja."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve

    p "??Masculinas?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Pens?? que tendr??as m??s experiencia con mujeres..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Por mujeres siento atracci??n,"

    tx "y eso, en general, suele traer m??s bien problemas laborales."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    p "??Y nunca te has sentido atra??da por la esposa en una de las parejas que has tratado?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "La mayor??a de las veces,"

    extend " especialmente cuando veo el idiota del marido con el que est?? casada o comprometida."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve

    p "??Entonces...?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "S?? separar el placer del trabajo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Adem??s,"

    extend " como ya te he comentado,"

    tx "esa \"segunda piel\" ayuda."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Cuando entro en mi despacho,"

    extend " o me enfundo en mi traje de l??tex en la otra sala,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve

    tx "dejo de ser yo misma para ser otra persona,"

    tx "redirecciono mis fantas??as para tratar sus problemas."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve

    p "??Y qu?? ocurre cuando ellos no comparten tus mismas fantas??as?"

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

    tx "que te sorprender??a saber la de veces que no es as??..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve

    tx "Suelo ser algo flexible seg??n el caso,"

    tx "ya que en realidad,"

    extend " m??s all?? del sexo,"

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

    p "????C??mo?!"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Tranquilo,"

    extend " no voy con una sierra abriendo cr??neos y extrayendo cerebros."

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

    tx "En realidad es una expresi??n que o?? por primera vez en la pel??cula {a=https://es.wikipedia.org/wiki/Mart??n_(Hache)}{i}Mart??n (hache){/i}{/a} y me encanta."

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

    pt "A??n as??,"

    extend " no s?? muy bien si yo ir??a a una psic??loga que quiere follarme la mente,"

    pt "sea ret??ricamente"

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
    
    tx "Por ??ltimo,"

    extend " dime..."

    tx "??Qu?? te parece este cuadro?"

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
    
    pt "????Qu?? pu??etas es esto?!"

    n "La figura aparentemente femenina de una monstruosidad peluda con piernas ecuestres,"

    n "dedos desfiguradamente longevos, con dos enormes cuernos al lado de dos orejas aparentemente ??lficas,"

    n "una enorme lengua que rodea su propio miembro mientras acaricia el interior de su vagina;"

    n "acompa??ada de varios cuerpos desnudos, uno encima del otro, sin aparente perspectiva;"

    n "el del centro con la concavidad de los ojos vac??a y su boca carente de dientes."

    n "Todo la pintura envuelta por manos negras que surgen de la oscuridad,"

    n "como si intentaran entrar en el cuadro cuyo fondo parece ser una fogata."

    n "Sin mencionar lo que llama m??s la atenci??n;"

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
    
    tx "??Has o??do hablar alguna vez sobre las criaturas mitol??gicas"

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

    tx "mostr??ndose en tus sue??os y fantas??as,"

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

    tx "??S??...?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "??C??mo se llama esta criatura?"

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

        "??ncubo.":
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

            tx "En realidad se llama {a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a}."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Pero es lo mismo,"

            extend " ??no?"

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

            pt "??Beber de una fuente?"

            extend " pero ????qu?? dice?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Lo que est?? claro,"

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

            extend " seg??n el {a=https://es.wikipedia.org/wiki/Folclore}folclore{/a} de varios pa??ses;"

            tx "una criatura que se alimenta de la esencia vital de otros seres vivos,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "usualmente bajo la forma de {a=https://es.wikipedia.org/wiki/Sangre}sangre{/a},"

            extend " para as?? mantenerse activo."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "En la cultura europea y occidental,"

            extend " as?? como en la cultura global contempor??nea,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "el arquetipo de vampiro m??s popular es el de origen {a=https://es.wikipedia.org/wiki/Pueblos_eslavos}eslavo{/a},"

            extend " es decir,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "el de un ser humano convertido despu??s de morir en un {a=https://es.wikipedia.org/wiki/No_muerto}cad??ver activo{/a}"

            extend " o reviviente depredador {a=https://es.wikipedia.org/wiki/Hematofagia}chupador de sangre{/a}."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Entonces lo he acertado..."

            extend " ??No?"

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

            tx "Aunque es cierto que guardan muchos puntos en com??n,"

            extend " sus diferencias son notables."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "En realidad podr??a tratarse de la misma criatura,"

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

            pt "??Eres t?? la que me est??s sacando estos cuentos de fantas??a!"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "La criatura a la que yo me refer??a se llama \"{a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "Atrapasue??os.":
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

            tx "Un {a=https://es.wikipedia.org/wiki/Atrapasue??os}atrapasue??os{/a} o cazador de sue??os,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "es un admin??culo hecho a mano,"

            extend " cuya funci??n consiste en filtrar los sue??os de las personas."

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

            p "??Est??s segura de que no existe una criatura con ese nombre?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows serious
            with dissolve

            p "Me suena haber le??do por ah?? que se trata de un ser alto,"

            extend " negro,"

            extend " sin ojos,"

            p "y con una boca enorme con colmillos afilados..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Eso lo habr??s le??do en alguna {a=https://es.wikipedia.org/wiki/Leyenda_urbana}leyenda urbana{/a}..."

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

            tx "la criatura que mencionas no se llama as??;"

            tx "tienen otro nombre."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "??Tienen?"

            extend " ??De qu?? est?? hablando?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "La criatura a la que yo me refer??a,"

            extend " se llama \"{a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a}\"."

            jump afternoon04_MACBA_CreatureName_after

        "S??cubo.":
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

            extend " seg??n las leyendas medievales occidentales,"

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

            extend " ??No?"

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

            tx "Los peces son animales {a=https://es.wikipedia.org/wiki/Ectotermia}ectot??rmicos{/a},"

            extend " con respiraci??n por branquias"

            extend " y mayoritariamente ov??paros,"

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

            extend " o tambi??n llamado {a=https://es.wikipedia.org/wiki/Cetacea}cet??ceo{/a},"

            tx "es un mam??fero {a=https://es.wikipedia.org/wiki/Eutheria}euterio{/a},"

            extend " completamente adaptado a la vida acu??tica."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "De hecho el nombre {a=https://es.wikipedia.org/wiki/Cetacea}cet??ceo{/a}"

            extend " deriva del griego que significa \"monstruo marino\","

            tx "y fue acu??ado por {a=https://es.wikipedia.org/wiki/Arist??teles}Arist??teles{/a}."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows normal
            with dissolve

            tx "para referirse a los animales acu??ticos dotados de respiraci??n pulmonar."

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

            tx "El nombre de la criatura a la que me refer??a es \"{a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a}\"."

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

            p "??T?? has visto esa misma mujer treinta a??os despu??s?"

            p "??Qui??n la ha visto!"

            extend " ??y qui??n la ve!"

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

            tx "??Por lo que yo he dicho?..." 

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            #show m_pupils front02a
            show m_exp_eyebrows surprisex02
            with dissolve

            p "{i}Se cuelan en tu alcoba,"

            extend " mostr??ndose en tus sue??os y fantas??as{/i},"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "\"para succionar tu semilla\","

            p "que t?? puedes pensar,"

            extend " {i}se refiere al esperma...{/i}"

            p "??Pero no!"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Se refiere a la cartera,"

            extend " que anda que no la dejan vac??a ni nada..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris front06
            #show m_pupils front06a
            show m_exp_eyebrows angryx01
            with dissolve

            p "Ya te digo yo que as?? uno envejece muy r??pido..."

            p "??Succion??ndote el alma!"

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

            tx "??Eso es humor catal??n?"

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

            p "qu?? poco sentido del humor,"

            extend " de verdad..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "Lo ??nico que veo, es que con esa actitud,"

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

            tx "El nombre de lo que te estaba hablando se llama \"{a=https://es.wikipedia.org/wiki/S??cubo}s??cubo{/a}\"."

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

            tx "??Se supone que tiene que hacerme gracia?"

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

            tx "????Y lo de que se cuelan en tu habitaci??n para tragarse tu semen?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "????Qu?? tipo de suegras has tenido t???!"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            p "A ver..."

            extend " eso es metaf??ricamente hablando,"

            p "lo de colarse en tu \"alcoba\""

            extend " para \"mostrarse\" en tus sue??os y fantas??as..."

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

            p "??Eso me ha pasado!"

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

            tx "??Con qu?? clase de mujeres te has acostado t???"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "En realidad la chica no estaba nada mal,"

            extend " era la madre que estaba un poco p??all??..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Supongo que estar??a llamando a la polic??a al ver..."

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows angryx04
            with dissolve

            tx "??que estabas abusando de su hija menor de edad!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "??Que no co??o!"

            extend " ??Si ten??a la misma edad que yo!"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows angryx01
            with dissolve

            tx "??Y esa edad cu??l era?"

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

            tx "Que me est??s sacando del tema..."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows angryx01
            with dissolve

            pt "??Qu?? tema?"

            pt "Si a??n no s?? a qu?? viene todo esto que me est??s contando..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Estas criaturas se llaman \"{a=https://es.wikipedia.org/wiki/S??cubo}s??cubos{/a}\"."

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
    
    tx "de quien se cree que descienden todos los dem??s {b}s??cubos{/b}."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "{a=https://es.wikipedia.org/wiki/Lilit}Lilith{/a}..."

    extend " creo que se trata de la primera mujer en el G??nesis del folclore jud??o,"

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
    
    tx "Sus movimientos son ??giles y precisos."

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
    
    tx "Aunque un espectador avispado podr??a saber que se trata de un demonio por ese destello en su mirada de oscuro y enfermizo deseo."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Tu mirada tampoco es que sea de ni??a inocente..."

    pt "aunque me imagino que no debe de ser por deseo hacia m??."

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
    
    tx "Podr??an considerarse la compa????a ideal si no fuese porque,"

    tx "en ocasiones,"

    extend " se dejan llevar y sacan su lado m??s lascivo."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Los demonios s??cubos no necesitan mostrarse agresivos y,"

    tx "adem??s,"

    extend " reh??yen los conflictos."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "Eso sin mencionar que,"

    extend " en caso de necesidad,"

    tx "no dudar??n en adoptar el papel de v??ctima o de damisela en apuros."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Incluso pueden enredar y poner a unos en contra de otros por simple diversi??n."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Lo dice como si inicialmente ella no me hubiera invitado a venir aqu?? solo para re??rse de mi \"incultura\"..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Una vez tienen elegido al mortal procuran alejarse con ??l de la multitud,"

    tx "y entonces usan su capacidad de sugesti??n,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
        
    tx "muy parecida a la de los \"vampiros\","

    tx "para hacerle creer pr??cticamente cualquier cosa que deseen."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Ahora se me pone a hablar de vampiros?"

    pt "??Pero de qu?? demonios me est?? hablando?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Cuando la v??ctima entra en ese estado hipn??tico, pasa a ser atacada por el s??cubo,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "que consume la energ??a de la v??ctima mientras mantienen relaciones sexuales."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "Como si no hubiera mujeres que se aprovechan del momento ??ntimo de la alcoba,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    pt "para extraer algo que no es precisamente energ??a ni semen..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris left03
    #show m_pupils left03a
    show m_exp_eyebrows serious
    with dissolve
        
    tx "Estos demonios se nutren de la energ??a vital del mortal,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    tx "energ??a que tambi??n les permite mantener ese aspecto joven y encantador."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Los m??s afortunados pueden acabar en un estado de inconsciencia,"

    extend " parecido al sue??o profundo,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
        
    tx "del que suelen despertar agotados,"

    extend " con depresi??n,"

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
    
    tx "Pero generalmente el s??cubo suele excederse extrayendo energ??a,"

    tx "dando a su v??ctima el obsequio del sue??o eterno."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Palmarla despu??s de echar un polvo,"

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
    
    tx "en ciertas ocasiones los s??cubos muestran su verdadero aspecto mientras mantienen relaciones con sus v??ctimas."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Ojos felinos,"

    extend " o, seg??n otros reptilianos,"

    extend " que brillan en la oscuridad,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "una lengua de serpiente exageradamente larga,"

    tx "colmillos largos y afilados,"

    extend " alas como de murci??lago,"

    extend " una cola..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Qu?? diablos me est?? describiendo?"

    extend " ??Un drag??n?"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Son atributos que suelen manifestarse cuando el s??cubo pierde el control por el placer y el ??xtasis."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Cuando ocurre esto,"

    extend " es porque su v??ctima no tiene ninguna posibilidad de escapar de su destino."

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
    
    p "Bonita informaci??n de {a=http://www.seresmitologicos.net/angeles-demonios/sucubos-incubos}seresmitologicos.net{/a},"

    p "pero exactamente,"

    extend " ??para qu?? diablos me cuentas todo esto?"
    
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

    extend " ??no ves algo extra??o en Neus?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    p "??Neus?"
    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04

    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    pt "Despu??s de que su mordida convirtiera a mi amigo en t??a..."
        
    pt "La verdad es que ya no s?? qu?? pensar."

    pt "En realidad,"

    extend " ya no estoy seguro de nada..."

    show m_exp_blush 02
    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "S??,"

    extend " la oscura morenita de ojos verde esmeralda y de piel suave que te roba el alma solo de mirarla."

    show m_exp_blush 03
    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Hombre..."

    extend " t?? tienes mejor delantera..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Aunque con tanto interrogatorio,"

    extend " me pregunto si habr?? descubierto lo que le ha ocurrido a D??dac..."

    show m_exp_eyebrows serious
    with dissolve
    
    pt "No,"

    extend " no tendr??a sentido que me hubiera acusado de haber quedado con una pelirroja si lo supiera..."

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
    
    tx "??Nunca le has visto un brillo extra??o en sus ojos?"

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

        pt "??A d??nde quiere ir a parar?"

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

            extend " como si no supiera cuando alguien me enga??a..."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            #show m_pupils front03a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "????Para qu?? te iba a enga??ar?!"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris right04
            #show m_pupils right04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Quiz??s,"

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

            extend " ??verdad?"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "??Me est??s diciendo que no has visto nada raro en ella?"

            jump afternoon04_MACBA_NeusEyesShine_after

        "Una vez me pareci?? ver que sus ojos cambiaban de color...": #Correct.
            call p_Help
            $ pl.ch_pts("mp",+1)

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "As?? que lo has visto..."

            show m_exp_mouth serious_Silentx01
            show m_exp_eyes 04
            show m_exp_piris front04
            #show m_pupils front04a
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Bueno,"

            p "pens?? que hab??an sido imaginaciones m??as,"

            extend " quiz??s..."

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
    
    tx "Eso es porque quiz??s contigo no ha tenido necesidad de mostrarse de esa manera."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "O porque quiz??s te equivocas..."

    pt "pero cualquiera le lleva la contraria..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Ya s?? que hace tiempo que conoces a Neus de la clase de Ilustraci??n..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Pero desde el principio siempre hab??as prestado m??s atenci??n a mis pechos que a su cara."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Debo aprender a disimular mejor..."

    pt "Pero con semejante delantera,"

    extend " realmente es dif??cil..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Dime, [protname],"

    extend " ??c??mo consigui?? llamar tu atenci??n para que ahora salgas con ella?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Toma preguntita..."

    extend " ??Y ahora qu?? le respondo?"
    
    pt "Neus me dijo que no le contara a nadie lo que sucedi?? con D??dac despu??s de morderlo,"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
        
    pt "que exist??a el riesgo de que si alguien en el hospital,"

    extend " o donde fuera,"

    pt "se enterase de lo que le ha sucedido..."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyebrows surprisex001
    with dissolve
    
    pt "D??dac acabar??a muerto."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    pt "Quiz??s fue solo una trola para mantenerme callado y deber??a haberlo llevado al hospital..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Pero si no es una mentira,"

    extend " D??dac podr??a morir..."

    menu afternoon04_MACBA_TellTruth_question:

        pt "??Se lo cuento?"

        "Si te lo cuento, ??qu?? garant??as tengo de que no se lo contar??s a nadie?":
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

        "Sencillamente me propuso ir a tomar algo y realmente me cay?? bien, no tiene m??s misterio.":
            call p_Help
            $ pl.ch_pts("mp",-1)

            jump afternoon04_MACBA_TellTruth_after

        "Lo siento, no puedo cont??rtelo.":
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
    
    tx "Hizo algo que te hizo romper la ilusi??n de la realidad en la que vivimos."

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    pt "??Qu?? pu??etas dice ahora?"

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
    
    tx "Te mostr?? algo que no encaja en las leyes f??sicas o naturales en las que hemos sido educados."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Casi como si se tratara de una novela,"

    extend " pel??cula,"

    extend " o sue??o."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    p "??Est??s insinuando que podr??a haber afectado mi mente para que me imaginara cosas que no son reales?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Hasta cierto punto no ser??a descabellado pensar en esa posibilidad..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex001
    with dissolve 
    
    tx "A veces no somos conscientes de que seguimos durmiendo,"

    tx "incluso cuando so??amos que despertamos."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Nuestras sensaciones est??n limitadas por nuestro consciente."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Me est?? hablando de {a=https://es.wikipedia.org/wiki/The_Matrix}Matrix{/a} o de {a=https://es.wikipedia.org/wiki/Inception}Inception{/a}?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Pero, si cuando despiertas,"

    tx "sigue existiendo ese cambio de la realidad,"

    tx "entonces no es una simple ilusi??n."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Y aun as??,"

    extend " las ilusiones no son siempre lo que parecen."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "Ya me est?? recordando a Neus con su charlataner??a sin sentido..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Dime, [protname],"

    extend " ??Es esa pelirroja de los grandes almacenes, D??dac convertido en mujer?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    pt "??Es astuta la muy zorra!"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows serious
    with dissolve
    
    p "??Qu??...?"

    p "??Qu?? te hace pensar eso?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Varias cosas,"

    extend " pero tu reacci??n confirma mis dudas."

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
    
    tx "??Hmm?"

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

    extend " y ninf??manas reptilianas..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "??S??...?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    p "Digo yo que viviendo en pleno siglo XXI,"

    extend " la gente ya conocer??a toda esta fauna..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Vamos,"

    extend " digo yo,"

    p "que la gente que supiera de su existencia,"

    p "los habr??a expuesto a la luz,"

    extend " saldr??a en las noticias,"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve

    p "??Joder!"

    p "??saldr??a en alguna fotograf??a de alguien de {i}Instagram{/i} o {i}Facebook{/i},"

    extend " con los dichosos {a=https://es.wikipedia.org/wiki/Autofoto}{i}selfies{/i}{/a}!"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "Si t?? supieras la verdad,"

    tx "??se lo explicar??as a alguien?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "??Por qu?? no?"

    p "????T?? no lo har??as?!"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Entonces..."

    extend " ??porqu?? no me lo has comentado en ning??n momento?"

    tx "O sencillamente," 

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
        
    tx "??Por qu?? no has acudido a la polic??a?"

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

    p "quiz??s fue por temor,"

    extend " quiz??s por ignorancia..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "O quiz??s por amenaza."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "Pero..."

    extend " si de verdad existieran dichas criaturas {b}bizarras{/b},"

    p "la gente en realidad estar??a en peligro..."

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
        
    tx "??Verdad?"

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
    
    tx "Si fueras una oveja en un reba??o de cien,"

    extend " y supieras que existe un lobo,"

    tx "que una vez al a??o,"

    extend " se lleva a una de vosotras."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "??Avisar??as al resto del peligro?"

    show m_exp_mouth serious_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "??Qu?? sentido tendr??a esconderlo?"

    p "Tarde o temprano te podr??a tocar a ti..."

    extend " ??No?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Si t?? supieras que existe,"

    extend " te asegurar??as de alejarte tanto del peligro como pudieras..."

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
    
    p "Ley del ego??sta psic??tico."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "??Qu?? ocurrir??a si las avisaras?"

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
    
    tx "Habr??a terror,"

    extend " p??nico,"

    tx "todas vivir??ais con miedo."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Y el lobo seguir??a viniendo a llevarse su parte."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Solo que quiz??s con m??s violencia."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "??Qu?? arreglar??as?"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    p "Pues que quiz??s nos levantar??amos en armas para luchar,"

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

    extend " si se te ocurriera alg??n d??a mencionar la posibilidad de que existe,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "la gente te responder??a con mofas,"

    extend " risas,"

    extend " e insultos."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx04
    with dissolve
    
    tx "Casi como si te pusieran un velo delante de tus ojos constantemente,"

    tx "para que dejaras de mirar all??,"

    extend " en la oscuridad."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    #show m_pupils front02a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    p "Se tratar??a de dar pruebas de que lo que cuento existe."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "??Tienes pruebas para demostrar lo que has experimentado?"

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
    
    tx "??Cu??ndo has visto que una oveja luche contra un lobo?"

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
    
    tx "??De verdad crees eso?"

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

    tx "Qu?? inocente..."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows serious
    with dissolve

    pt "??Por qu?? sigo aguantando a esta t??a?..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "??Y qu?? me dices de nuestra historia?"

    p "Habr??a escritos,"

    extend " ??pruebas!"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
       
    p "Algo m??s que simple entretenimiento folcl??rico sobre todo esto..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "A menos que quemaran dichas pruebas y libros por orden \"divina\","

    tx "en tiempos oscuros en los que el pueblo no sab??a ni leer..."

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
    
    pt "Sin duda se est?? refiriendo a los tiempos de la {a=https://es.wikipedia.org/wiki/Inquisici??n_espa??ola}santa inquisici??n{/a}..."

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

    extend " esta conversaci??n me est?? resultando muy surrealista..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Y sin embargo, aqu?? sigues,"

    extend " escuch??ndome,"

    extend " y argument??ndome."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Como te he dicho,"

    extend " sigo aqu?? por simple curiosidad."

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

    tx "podr??a ense??arte m??s sobre todo esto en mi taller,"

    show m_exp_blush 01
    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris right03
    #show m_pupils right03a
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "si est??s libre ma??ana por la tarde a la misma hora que hoy."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows normal
    with dissolve
    
    tx "Ah?? es donde guardo las cosas que pueden darte una mejor idea de lo que te estoy contando,"

    tx "si es que te interesa..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows normal
    with dissolve
    
    p "??Taller?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "??A qu?? te refieres con \"taller\"?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Mi oficio,"

    extend " aparte del que est??s observando en esta galer??a,"

    tx "es el de \"sex??loga-dominatrix\"."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows surprisex02
    with dissolve
    
    tx "B??sicamente trato con maridos infieles,"

    extend " impotentes,"

    tx "o parejas que han perdido la pasi??n."

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
    
    tx "??Acaso tienes alg??n problema de impotencia que quieras discutir?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    #show m_pupils front03a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "????Euh?!"

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
       
    p "??Cla-"

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
    
    pt "??Entonces por qu?? pregunta?"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows surprisex001
    with dissolve
    
    tx "Esta noche vas a tener otra cita con Neus,"

    extend " ??verdad?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    p "S??..."

    extend " as?? es..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Te dar?? un consejo,"

    extend " hombret??n..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows suspiciousx02
    with dissolve
    
    tx "Cu??date de no tener un orgasmo cerca de ella."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    #show m_pupils front04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "Quiz??s no vivas para contarlo..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    #show m_pupils right04a
    show m_exp_eyebrows angryx01
    with dissolve
    
    pt "??Lo dice en co??a?,"

    extend " ??es por celos?,"

    pt "??o lo dice en serio?"

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

    extend " ya sabes mi n??mero."

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
    
    n "Sin que apenas te d?? tiempo a darle una respuesta,"

    n "ves c??mo se retira de tu presencia con un movimiento de caderas realmente hipn??tico."

    show afternoon04_macba_txellwalkingaway:
        subpixel True
        easein_quad 15.0 zoom 0.8 xanchor 0.28 yanchor 0.02 #Head

    window hide dissolve
    pause

    pt "????Acaso sabe que le estoy mirando el trasero?!"

    window hide dissolve
    pause

    scene afternoon04_bg macba_room02
    with fade

    pt "Posiblemente no le atraigan los hombres,"

    pt "pero sin duda, disfruta seduci??ndolos de forma enfermiza..."
    
    pt "Mi amigo convertido en chica que parece ser una ninf??mana,"

    pt "la bruja friki que me chantajea,"

    pt "y esta loca del co??o..."
    
    pt "????Por qu?? no puedo conocer a una chica normal?!"
    
    p "..."
    
    pt "Ser?? mejor volver a casa y prepararme para la cita de esta noche..."
    
    jump night04_restaurant
    
#############

    #(Luego estar??a bien que en la cita con Neus se tratara el tema de que has quedado con la chica tetuda 
    #y Neus te expliqu?? lo que ocurri?? con ella).




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
        # pt "??Lo dice en co??a?,"
        # extend " ??es por celos?,"
        # pt "??o lo dice en serio?"


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

    tx "espera aqu?? un segundo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    p "??Qu??...?"

    scene afternoon04_bg macba_room02
    with dissolve

    n "Sin esperar tu respuesta, la ves alejarse hasta desaparecer tras una puerta en la misma sala donde est??s."

    n "De ah?? reaparece con un malet??n negro."

    pt "??Qu?? demonios llevar?? ah?? dentro?"

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

    tx "??brelo."

    show m_exp_mouth sad_Silentx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx02
    with dissolve

    p "??Qu?? hay aqu?? dentro?"

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

    p "??Qu??...?"

    n "En su interior encuentras una mordaza de bola agujereada,"

    n "una botella deportiva de pl??stico adjunta a una pajita larga,"

    n "otra botella peque??a y oscura sin ning??n tipo de etiqueta,"

    n "un pa??uelo y lo que parecen cuatro esposas de cuero,"

    n "cada una de ellas conectadas a una larga cadena de hierro"

    n "las cuales tambi??n terminan en otras esposas, pero estas hechas del mismo metal que las cadenas."

    pt "??Esto no ser??...?"

    hide afternoon04_macba_briefcase

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    tx "Lo que hay en el botell??n oscuro es {a=https://es.wikipedia.org/wiki/Cloroformo}cloroformo{/a}."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    pt "??Qu??...?"

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

    pt "??Entonces...?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    tx "Me imagino que te habr?? resultado una insoportable {a=https://es.wikipedia.org/wiki/Esnob}esnob{/a}."

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

    tx "Pero una de las razones por las que he intentado llevar al l??mite tu paciencia"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "es porque quer??a ver como reaccionas ante una situaci??n estresante"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "y hasta qu?? punto puedes pensar en fr??o."

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

    tx "Debo reconocer que desconozco la verdadera situaci??n de tu compa??ero de piso,"

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

    pt "??Qu?? sabe realmente sobre D??dac?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows serious
    with dissolve

    tx "Deber??s usar todo el l??quido del pote y darte prisa, pues no tardar?? en evaporarse."

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

    tx "Pero ten en en cuenta que el cloroformo no funciona como en las pel??culas,"

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

    tx "Deber??s mantener tu mano pegada en su nariz durante al menos unos cuatro o cinco minutos"

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

    tx "Estoy segura que con tu masa muscular tendr??s m??s suerte de la que tuve yo."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows sadx05
    with dissolve

    pt "??De qu?? est?? hablando?"

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

    tx "aparta el pa??uelo de inmediato y ll??valo a un lugar d??nde puedas encadenarlo con seguridad."

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

    tx "pero la suficiente para que pueda estar horas inm??vil sin que le perjudiques los m??sculos y tendones."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Si no usas una cama, aseg??rate de dejarlo lo m??s c??modo posible con varios cojines."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pero si la usas, no le pongas coj??n."

    show m_exp_mouth sad_Talkingx04
    with dissolve

    tx "es mejor que la cabeza est?? en perpendicular con el resto del cuerpo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "??Y para qu?? sirven la mordaza y el botell??n deportivo con pajita?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Una persona con un ??ndice de masa corporal normal podr??a sobrevivir m??s de un d??a sin beber agua,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "pero si no quieres que tenga problemas de h??gado o derivados,"

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

    tx "No querr??s que grite demasiado alertando a tus vecinos,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "??no?"

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

    tx "para que pueda pasar el agua a trav??s."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Solo aseg??rate de cerrar bien las ventanas."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "??Est?? hablando en serio?"

        "??Y si tiene que ir al ba??o?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            tx "Me temo que tendr?? que dejar la cama empapada,"

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

            tx "espero que no lo dejes ah?? demasiado tiempo."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            menu:

                pt "??Qu?? clase de psic??pata es esta mujer?"

                "??Lo usaste para violar a alguien?":
                    call p_Help

                    show m_exp_mouth sad_Talkingx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "??No seas idiota!"

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

                "??Lo usaste contra alguien?":
                    call p_Help

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx04
                    with dissolve

                    tx "Por lo menos lo intent??..." 

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

    tx "En su tiempo lo compr?? en el mercado negro"

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

    p "??No hubiera sido m??s pr??ctico usar un espray de pimienta?"

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

    tx "Me segu??a a todas partes,"

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

    tx "me jaque?? el m??vil varias veces,"

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

    tx "No quer??a alejarle temporalmente,"

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

    p "??Y por qu?? no lo denunciaste?"

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

    tx "En su momento pens?? que no necesitaba involucrar a las autoridades para defenderme de ese maldito energ??meno."

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

    tx "Por eso te he dicho que no funciona como en las pel??culas."

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

    p "esto pas?? hace a??os,"

    extend " ??no?"

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

    p "??Esto no tiene data de caducidad?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "S??."

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

    extend " por eso te he dicho que lo uses solo si no tienes ninguna otra opci??n."

    tx "Ah..."

    tx "Y por si no hab??a quedado claro."

    tx "Yo nunca te he ofrecido este malet??n."

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

    tx "O simplemente devu??lvemelo."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve


    menu:

        pt "??Tan mal estar?? D??dac para que vaya a necesitar esto?"

        "??Y qu?? te hace pensar que lo vaya a necesitar?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows surprisex02
            with dissolve

            tx "Ll??malo intuici??n."

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

                pt "??Y a ella qu?? le importe lo que le pase a D??dac?"

                "??Desde cuando te preocupas tanto por mi?":
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

                    tx "No eres t?? quien me preocupa."

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows suspiciousx03
                    with dissolve

                    p "??De Neus?"

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

                    tx "Te aseguro que ella no necesita de mi protecci??n."

                    show m_exp_mouth sadbiting_Silentx04
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx03
                    with dissolve

                    pt "??De D??dac?"

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

                    tx "no me importa a quien est?? ayudando."

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

        pt "??Y c??mo s?? que no me est?? tendiendo una trampa?"

        "Te prometo que lo usar?? solo como ??ltimo recurso.":
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

        "<Devolverle el malet??n>":
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
        # extend " ya sabes mi n??mero."