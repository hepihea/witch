default afternoon05_TxellWorkPlace_Leavethemalone = False
default afternoon05_TxellWorkPlace_FuckHiromi_Accepted_Cond = False

default afternoon05_Akelarre_Told = False
default afternoon05_NeusMeeting_Told = False

default FuckH_SUCCESS = False

default FuckH_ThreatFailed = False

default FuckT_Possible = False
default FuckT_Beginning_domination_question_failed = False
default FuckT_Beginning_domination_Pasive_anal_permision = False

default afternoon05_Library_Continue_WithGuro = False
default afternoon05_Library_Continue_WithoutGuro = False
default afternoon05_Library_Continue_Cond = False # With or Without Guro-Gore.


label afternoon05_TxellWorkPlace:

    scene bg 05afternoon_entrance_doorbell_bg:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    stop music fadeout 3.0

    #call endillustrations

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    play sound "audio/sfx/doorbell01.ogg"

    ono "MIIIIC"

    tx "¿Quién es?"

    $ renpy.music.set_volume(0.1, delay=10.0, channel='sfx1')

    #########################################################

    if config.version < "00.14.04": # How did you imagine the end of our date? (After Neus Date players will be able to play this part.)
        call endupdatescript
    
    #######################################################

    p "Buenas,"

    p "soy [protname]."

    p "No sé si hoy te acordarás de mí..."

    tx "Mierda..."

    pt "¿Mierda?"

    pt "Empezamos bien..."

    tx "No esperaba que llegaras tan temprano."

    p "..."

    p "¿Ocurre algo?"

    tx "He tenido una visita inesperada."

    p "Pensaba que no trabajabas los domingos..."

    tx "Por eso he dicho que es inesperada."

    p "..."

    tx "..."

    p "Entonces..."

    p "¿Quieres que me vaya a dar una vuelta...?"

    p "¿O...?"

    tx "No."

    tx "Sube."

    tx "Es posible que puedas echarme una mano y todo."

    p "..."

    play sound "audio/sfx/doorbellaccess01.ogg"

    ono "MEEEEEC"

    n "Presionas la puerta del bloque de pisos para abrirla."

    pt "Tampoco es que sea muy normal que me cite en su despacho un domingo..."

    play sound "audio/sfx/door_open01.ogg"

    ##

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    scene bg 05afternoon_entrance_receptiondoor_closed_bg:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.55 ypos 0.9
        easein 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    play sound "audio/sfx/knock_wood_01.ogg"

    ono "toc"

    play sound "audio/sfx/knock_wood_02.ogg"

    extend " toc"

    play sound "audio/sfx/door_open02.ogg"

    show bg 05afternoon_entrance_receptiondoor_open_bg
    with dissolve

    tx "Buenas [protname]."

    tx "Por favor,"

    extend " pasa."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "meritxell_theme"

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    scene bg 05afternoon_entrance_reception_bg:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.7 ypos 0.8
        easein_quad 15.0 zoom 0.3335  xpos 0.5 ypos 0.5
    with fade

    pt "Caray con la recepción de la consulta de la dominatrix,"

    pt "no quiero imaginarme cómo debe de ser su despacho..."

    pt "desde luego, no necesita pedir caridad."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    #show hiromi_gen_PROVE_space:
        #truecenter
        #zoom 0.2 alpha 1.0

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_left_zoom_0_4_pos
    show hiromi_gen_body_c_crossed_dressed:
        hiromi_gen_body_left_zoom_0_4_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_left_zoom_0_4_pos

    show hiromi_gen_exp_blush 01:
        hiromi_gen_exp_left_zoom_0_4_pos
    show hiromi_gen_exp_mouth sad_Talkingx15:
        hiromi_gen_exp_left_zoom_0_4_pos
    show hiromi_gen_exp_eyes 04:
        hiromi_gen_exp_left_zoom_0_4_pos
    show hiromi_gen_exp_piris front04:
        hiromi_gen_exp_left_zoom_0_4_pos
    show hiromi_gen_exp_eyebrows angryx06:
        hiromi_gen_exp_left_zoom_0_4_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_left_zoom_0_4_pos
    with vpunch

    play sound "audio/sfx/meme_surprise02.ogg"

    if music_play != "frailty":
        play music "audio/music/alcaknight/frailty.ogg" fadein 0.5 fadeout 0.5
        $ music_play = "frailty"

    g04 "{size=30}¡¿Y ESTE QUIÉN DIABLOS ES?!{/size}"

    scene bg 05afternoon_entrance_reception_bg:
        truecenter
        zoom 0.3335  xpos 0.5 ypos 0.5

    show m_bodynew hips_04:
        mtxell_body_ontheright_zoom_0_3_pos

    show m_exp_blush 01:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_mouth sad_Talkingx10:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyes 04:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_piris left04:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyebrows angryx04:
        mtxell_exp_ontheright_zoom_0_3_pos

    show m_exp_hair_front:
        mtxell_exp_ontheright_zoom_0_3_pos

    
    show hiromi_gen_h_hair_back:
        hiromi_gen_body_left_zoom_0_3_pos
    show hiromi_gen_body_c_crossed_dressed:
        hiromi_gen_body_left_zoom_0_3_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_left_zoom_0_3_pos

    show hiromi_gen_exp_blush 01:
        hiromi_gen_exp_left_zoom_0_3_pos
    show hiromi_gen_exp_mouth sad_Silentx10:
        hiromi_gen_exp_left_zoom_0_3_pos
    show hiromi_gen_exp_eyes 03:
        hiromi_gen_exp_left_zoom_0_3_pos
    show hiromi_gen_exp_piris right03:
        hiromi_gen_exp_left_zoom_0_3_pos
    show hiromi_gen_exp_eyebrows angryx05:
        hiromi_gen_exp_left_zoom_0_3_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_left_zoom_0_3_pos
    with dissolve

    tx "{size=30}¡No te importa una mierda!{/size}"

    show m_exp_blush 01
    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx11
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris left02
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    pt "O es una amiga,"

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    pt "o una clienta con quien tiene demasiada confianza..."

    #show m_exp_blush 01
    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 02
    show m_exp_piris left01
    show m_exp_eyebrows surprisex001

    show hiromi_gen_exp_mouth sad_Talkingx10
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    g04 "¡¿Por qué diablos le has abierto la puerta?!"

    #show m_exp_blush 02
    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02

    show hiromi_gen_exp_mouth sad_Talkingx11
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    g04 "¡Pensaba que me habías dicho que en domingo no aceptabas visitas!"

    #show m_exp_blush 02
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    tx "¡Él no es una jodida visita!"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx03
    
    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    g04 "..."

    show m_exp_blush 06
    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 00
    show m_exp_piris left00
    show m_exp_eyebrows surprisex02
    
    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 00
    show hiromi_gen_exp_piris right00
    show hiromi_gen_exp_eyebrows surprisex03
    with dissolve

    g04 "¿Es tu novio?"

    show m_exp_blush 03
    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx05
    
    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows surprisex01
    with dissolve

    tx "¡Maldita sea Hiromi!"

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx04
    
    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows surprisex02
    with dissolve

    tx "¡Una puede tener amigos sin tener que follárselos!"

    show m_exp_blush 02
    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx05
    
    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows suspiciousx02
    with dissolve

    pt "¿Hiromi?"

    #show m_exp_blush 02
    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx05
    
    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    g04 "Ya sabes a qué me refiero."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows suspiciousx02
    with dissolve

    pt "¿No es eso un nombre japonés?"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    tx "No,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    tx "me siguen gustando las chicas,"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows suspiciousx01
    with dissolve

    pt "Nunca había visto a una japonesa con la piel tan oscura..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    tx "es simplemente un amigo."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx07

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows suspiciousx02
    with dissolve

    tx "¡¿Vale?!"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 00
    show m_exp_piris left00
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows surprisex001
    with dissolve

    g04 "Ya..."

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows surprisex02
    with dissolve

    tx "¡Ni que tuviera que darte explicaciones!"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    tx "¡Aún no entiendo por qué no te he echado a patadas!"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Talkingx02
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    g04 "Porque realmente necesito tu ayuda."

    show m_exp_mouth sad_Silentx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    g04 "Sabes que no habría acudido a ti si no fuera importante."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sad_Talkingx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows surprisex01
    with dissolve

    tx "Para ti siempre he sido solo una simple herramienta."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    g04 "Sabes que no es así."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Talkingx02
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    g04 "Txell,"

    extend " hace años que nos conocemos..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    tx "..."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    pt "Txell..."

    pt "Desde luego, es más corto que {b}Meritxell{/b}..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    tx "Ese es el problema, {b}Hiromi{/b},"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    tx "que te conozco demasiado bien."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    hi "Fuimos pareja durante más de dos años."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    tx "Yo no lo describiría así precisamente..."

    show m_exp_blush 03
    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows surprisex01

    show hiromi_gen_exp_blush 03
    show hiromi_gen_exp_mouth sad_Talkingx04
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    hi "Sabes lo que sentía por ti."

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx07

    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    tx "Por eso un buen día me dejaste diciendo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    tx "\"lo nuestro ha terminado\""

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx07

    show hiromi_gen_exp_mouth sadbiting_Silentx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    tx "sin ninguna explicación más."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx07

    show hiromi_gen_exp_mouth sad_Talkingx01
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    hi "Txell..."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx07

    show hiromi_gen_exp_mouth sadbiting_Silentx08
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    tx "¡¿Qué?!"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx08
    with dissolve

    hi "..."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx07

    show hiromi_gen_exp_mouth sadbiting_Silentx10
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows sadx07
    with dissolve

    tx "..."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sadbiting_Silentx11
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    p "..."

    show m_exp_blush 02
    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 00
    show m_exp_piris left00
    show m_exp_eyebrows surprisex01

    show hiromi_gen_exp_mouth sad_Talkingx15
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "¡¿Tiene que estar el cavernícola este de las narices aquí delante?"

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx16
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "¿No tiene una cueva donde ir a perderse?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sad_Silentx13
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    p "..."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth happy_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    p "La verdad es que la conversación parece más bien algo privada..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    tx "Él se queda,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sad_Talkingx01
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    tx "que para eso le he invitado."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    tx "A menos que quieras irte, [protname]."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Silentx10
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    menu afternoon05_TxellWorkPlace_Leavethemalone_Question:

        pt "¿He venido hasta aquí para irme ahora?"

        "<Irte a casa>":

            call p_Help

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex02

            show hiromi_gen_exp_mouth happy_Silentx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            p "Creo que lo mejor es que os deje a solas y me vaya a casa."

            show m_exp_mouth sad_Talkingx01
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01

            show hiromi_gen_exp_mouth happy_Silentx06
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            tx "¿Qué?"

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 02
            show m_exp_piris left02
            show m_exp_eyebrows angryx01

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "Gracias por entenderlo."

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows angryx04

            show hiromi_gen_exp_mouth happy_Talkingx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "Al fin y al cabo, es algo que no te incumbe."

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows angryx05

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris right01
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            tx "¡Hiromi!"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows sadx01

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris right03
            show hiromi_gen_exp_eyebrows sadx03
            with dissolve

            hi "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx03

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris right03
            show hiromi_gen_exp_eyebrows sadx02
            with dissolve

            tx "[protname];"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx03

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows sadx03
            with dissolve

            tx "¿Estás seguro de que quieres irte?"

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx04

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows sadx03
            with dissolve

            menu afternoon05_TxellWorkPlace_Leavethemalone_Question_02:

                pt "¿He venido hasta aquí para irme ahora?"

                "<Irte a casa>":

                    call p_Help
                    
                    $pl.ch_pts("mp",-5)

                    $ afternoon05_TxellWorkPlace_Leavethemalone = True

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows sadx03

                    show hiromi_gen_exp_mouth happy_Silentx05
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "Sea lo que sea que debieras contarme,"

                    show m_exp_mouth sad_Silentx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows sadx04

                    show hiromi_gen_exp_mouth happy_Silentx07
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    p "estoy seguro que lo tuyo con esta mujer es más importante."

                    show m_exp_mouth sad_Silentx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows sadx05

                    show hiromi_gen_exp_mouth happy_Silentx08
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx02
                    with dissolve

                    p "Espero que podáis arreglar las cosas entre vosotras."

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 08
                    show m_exp_piris empty
                    show m_exp_eyebrows sadx04

                    show hiromi_gen_exp_mouth happy_Silentx08
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx03
                    with dissolve

                    p "Que tengáis un buen día."

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows sadx06

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris right02
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    tx "Espera..."

                    scene bg 05afternoon_entrance_receptiondoor_open_bg:
                        subpixel True
                        truecenter
                        zoom 1.0 xpos 0.55 ypos 0.9
                        easein 15.0 zoom 0.5 xpos 0.5 ypos 0.5
                    with fade

                    pause 0.5

                    play sound "audio/sfx/door_close01.ogg"

                    show bg 05afternoon_entrance_receptiondoor_closed_bg
                    with dissolve

                    n "Oyes a tu espalda que Hiromi la agarra del brazo y empiezan a discutir al poco después de cerrar la puerta tras de ti."

                    jump morning05_NeusFinalDate

                "<Quedarte>":

                    call p_Help
                    
                    $pl.ch_pts("mp",1)

                    jump afternoon05_TxellWorkPlace_Leavethemalone_No

        "<Quedarte>":

            call p_Help
            
            $pl.ch_pts("mp",1)

            jump afternoon05_TxellWorkPlace_Leavethemalone_No

label afternoon05_TxellWorkPlace_Leavethemalone_No:

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx03

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    p "Podría dejaros a solas,"

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01

    show hiromi_gen_exp_mouth sad_Silentx10
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    p "pero hay algo que tenemos que hablar que no puede esperar a mañana."

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows surprisex001

    show hiromi_gen_exp_mouth sad_Talkingx13
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "¡¿Te crees que lo mío sí puede esperar?!"

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Talkingx14
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "¿No puedes irte durante una hora a dar un paseo o algo?"

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sadbiting_Silentx10
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    tx "He dicho que él se queda."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx03

    show hiromi_gen_exp_mouth sadbiting_Silentx09
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    tx "Si no te gusta,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx10
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    tx "te vas."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx06

    show hiromi_gen_exp_mouth sadbiting_Silentx11
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    tx "Que eres \"tú\" quien ha venido realmente sin invitación."

    show m_exp_mouth sad_Silentx09
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    hi "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sadbiting_Silentx12
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    pt "Si su mirada lanzara cuchillos,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx03

    show hiromi_gen_exp_mouth sadbiting_Silentx14
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    pt "ya estaría agujereado por todas partes..."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows normal

    show hiromi_gen_exp_mouth sad_Talkingx01
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "Pff..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    tx "De todos modos, es lo que te he dicho antes,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    tx "no puedo ayudarte."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 00
    show m_exp_piris left00
    show m_exp_eyebrows surprisex01

    show hiromi_gen_exp_mouth sad_Talkingx12
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "¡Deja el jodido código moral a tomar por el culo!"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx14
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    hi "¡Te estoy pidiendo un favor!"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx02

    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris left03
    show hiromi_gen_exp_eyebrows suspiciousx03
    with dissolve

    tx "Los principios éticos terapéuticos existen por una razón,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx03

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 00
    show hiromi_gen_exp_piris right00
    show hiromi_gen_exp_eyebrows surprisex02
    with dissolve

    tx "especialmente cuando se tratan sentimientos."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sad_Talkingx02
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    hi "Han pasado diez años."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    tx "No sé tú Hiromi,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    tx "pero para mí fue algo más que \"sexo duro\"."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx05

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    hi "..."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    tx "Realmente te amé."

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx03
    with dissolve

    hi "¿Aún...?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    tx "No."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    tx "Ya no."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    hi "¿Entonces...?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx04

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx05
    with dissolve

    tx "Tan testaruda como siempre."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx02

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    tx "Puedo recomendarte otras especialistas, que de bien seguro, serán capaces de ayudarte mejor."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sad_Talkingx07
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "No lo entiendes."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "¡Ya he acudido a otras especialistas y no ha servido de nada!"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04

    show hiromi_gen_exp_mouth sad_Talkingx11
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    hi "Eres la única persona que me conoce lo suficiente como para poder ayudarme de verdad."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows sadx04
    with dissolve

    tx "..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows suspiciousx03
    with dissolve

    hi "Además,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    hi "sabes muy bien que eres la mejor especialista en este campo del país."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx03

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx02

    show hiromi_gen_exp_mouth sad_Talkingx001
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    hi "Y no;"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows surprisex002

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows suspiciousx02
    with dissolve

    hi "no te estoy tirando flores,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    hi "lo sabes de sobra."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    tx "En primer lugar,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx02

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows suspiciousx01
    with dissolve

    tx "eso no es del todo cierto,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex03

    show hiromi_gen_exp_mouth sad_Silentx17
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    tx "hay muchos campos en los que..."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 00
    show m_exp_piris left00
    show m_exp_eyebrows surprisex03

    show hiromi_gen_exp_mouth sad_Talkingx15
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "¡Para ya!"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Talkingx13
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "¡Déjate de palabrería fácil!"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01

    show hiromi_gen_exp_mouth sad_Talkingx11
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "¡Si no quieres ayudarme, dilo!"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows surprisex002

    show hiromi_gen_exp_mouth sad_Talkingx009
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "Aceptaré mejor tu rechazo que una burda mentira."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    tx "..."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth happybiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows surprisex01
    with dissolve

    tx "..."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "¿Por qué le estás mirando a él?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows surprisex001

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris right01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    tx "¿Me dejas unos minutos a solas con mi invitado?"

    show m_exp_mouth happybiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows surprisex01

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    hi "..."

    show m_exp_mouth happybiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx01

    show hiromi_gen_exp_mouth sad_Talkingx01
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    hi "Pfff..."

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows normal

    show hiromi_gen_exp_mouth sad_Talkingx04
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "Como quieras."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows suspiciousx03
    with dissolve

    pause 0.2

    scene bg 05afternoon_entrance_reception_bg:
        truecenter
        zoom 0.3335  xpos 0.5 ypos 0.5

    show m_bodynew hips_04:
        mtxell_body_ontheright_zoom_0_3_pos

    show m_exp_blush 02:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_mouth sad_Silentx04:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyes 03:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_piris left03:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyebrows serious:
        mtxell_exp_ontheright_zoom_0_3_pos

    show m_exp_hair_front:
        mtxell_exp_ontheright_zoom_0_3_pos

    with fade

    n "A regañadientes, ves su figura desaparecer tras cruzar una puerta al fondo de un pasillo lejano."

    show m_exp_mouth sad_Talkingx01
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "<Suspiro prolongado>"

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "meritxell_theme"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Lo siento de verdad, [protname]."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "No es lo que tenía pensado cuando te invité a venir a mi despacho."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "¿Qué es lo que tenía pensado?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    p "Por lo que he entendido,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "es tu ex,"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿verdad?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "Así es."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "¿Pero exactamente qué es lo que te está pidiendo?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Hace unos meses conoció a un hombre de alto poder ejecutivo con el que tenía tratos laborales."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious
    with dissolve

    tx "Con el tiempo fue dejando la profesionalidad un poco de lado,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "hasta el punto de llegar a tener fuertes sentimientos hacia él."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pensaba que tiraba más por el pescado que por los embutidos..."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Digamos que Hiromi es alguien particularmente especial en el campo de los cánones de la sexualidad..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "Es {a=https://es.wikipedia.org/wiki/Pansexualidad}pansexual{/a}."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Le gustan tanto hombres,"

    extend " mujeres,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "como cualquier otra definición que quieras encontrar en medio."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    tx "En realidad el sexo no es en sí lo que más le interesa."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex03
    with dissolve

    p "¿A dónde quieres ir a parar?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "Es {a=https://es.wikipedia.org/wiki/Transexualidad}transexual{/a}."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "Lo que me faltaba..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "Nació siendo hombre,"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows normal
    with dissolve

    tx "pero de bien pequeña empezó un tratamiento hormonal,"

    tx "por lo que ahora es difícil distinguir su rasgos masculinos."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    p "Pero su voz no es nada masculina..."

    show m_exp_mouth happy_Talkingx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Así es,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "aunque tiene otras partes no tan femeninas..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿Me estás diciendo que tiene...?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Sí."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Ahhmm..."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "Y eso hace aún más difícil lo que voy a pedirte."

    show m_exp_mouth happy_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿Qué?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious
    with dissolve

    tx "El hombre del que se está enamorando,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "resulta ser alguien parecido a ella."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Una mujer convertida en hombre?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "No."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "No creo, vaya..."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "¿Entonces?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Hiromi siempre ha sido alguien extremadamente dominante,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "de hecho, ella fue quien me inició plenamente en este mundo de placer y sumisión."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "¿Entonces con ella eras sumisa?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "No completamente."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "En sus propias palabras,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows angryx02
    with dissolve

    tx "{i}No me gustan las muñecas{/i}."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious
    with dissolve

    tx "{i}Para sentir atracción por alguien,{/i}"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "{i}tiene que ser una persona con sueños,"

    extend " esperanzas,"

    extend " ilusiones,"

    extend " metas...{/i}"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "{i}Que una persona sea algo más que un trozo de carne para llegar a un orgasmo vacío y torpe.{/i}"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Pero a pesar de eso,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "le encantaba doblegar esa fuerte personalidad a su voluntad y deseo."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Hablas en pasado..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Así es."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Aunque estoy segura de que sigue teniendo esa filia por la dominación,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "ha conseguido el sueño húmedo de toda dominante"

    tx "que se precie a sí misma como exploradora de su sexualidad."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Enamorarse de alguien que ha conseguido someterla."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Ya..."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿Pero cuál es el problema entonces?"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Que la muy gilipollas ha roto la primera norma de su propio código."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¿Cuál?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    tx "No mentir."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿Y en qué le ha mentido?"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve
    
    tx "En su absoluta carencia y falta de experiencia como sumisa."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pensaba que habías dicho que no eras completamente sumisa con ella."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Eso es porque no se lo ponía fácil,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "o porque no siempre claudicaba fácilmente;"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "al fin y al cabo, le gustaba que mantuviera mi propio criterio y personalidad."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Pero jamás conseguí doblegarla a mi voluntad,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "y no fue porque no me diera oportunidades,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "pero en ese entonces yo era una novata."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Y tampoco me lo puso nada fácil,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "para ser sincera."

    show m_exp_mouth sadbiting_Silentx01
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    p "¿Pero no sería más simple admitir su error y que fueran explorando poco a poco su sumisión?"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿No es algo que una dominante como tú disfrutaría?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Desde luego,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "especialmente si hay sentimientos en medio."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    p "¿Entonces?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Como te he dicho,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "resulta ser alguien incluso mucho más dominante que ella."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Y?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "Me parece que no eres consciente de la importancia que tiene la honestidad en nuestro mundo."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Joder,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "un error lo puede tener cualquiera."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "No en estos términos."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Sería confesarle abiertamente que le ha mentido sin tapujos sobre un tema tan delicado."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Perdería completamente su confianza y,"

    extend " por lo que ella dice,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "incluso la oportunidad de explicarse."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex03
    with dissolve

    p "Quien habla aquí es su miedo a perderlo,"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "no la razón."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Ciertamente."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Pero creo que eres incapaz de imaginar"

    tx "las atrocidades que puede hacer la mente de una persona"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "que tiene miedo a perder a alguien amado."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "En realidad lo único que necesita es un pequeño \"empujón\"."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    p "¿Empujón?"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Por mucho que lo ame,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "si este empieza de cero a cien a tratarla como sumisa,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Hiromi puede implosionar por dentro,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "no ser capaz de contenerse en ese momento,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "y una mentira descubierta"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "es bastante peor que confesada."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Cómo os gusta dramatizar las cosas..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "Con lo fácil que es la sinceridad."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Exacto,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "de ahí todo el problema."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex03
    with dissolve

    p "¿Y a qué te refieres con el empujón?"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Lo que realmente necesita es que alguien la someta completamente a su voluntad,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "desarmarla por completo sin que ofrezca resistencia alguna y termine,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "no solo aceptándolo"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03
    with dissolve

    tx "sino además, consiguiendo gozar absolutamente de su falta de control sobre la situación;"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "algo que nunca ha experimentado antes,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "o al menos no plenamente."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Pero antes has dicho que este hombre es dominante."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    p "Algo habrán hecho ya..."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿No?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Por el modo en que me lo ha explicado,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "esta noche será la primera vez en la que existe la posibilidad real de que lleguen a esa fase."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "¿Y qué han hecho hasta ahora?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "El sexo o el orgasmo no son el verdadero objetivo de una dominación."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Lo que realmente importa es el transcurso y desarrollo que existe en ese camino."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "De hecho,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "las que terminan sin orgasmo"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex002
    with dissolve

    tx "suelen ser las mejores experiencias que he tenido."

    show m_exp_mouth happybiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    show m_exp_blush 03
    show m_exp_mouth happybiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    pt "Lo que tú digas..."

    extend " frígida..."

    show m_exp_blush 02
    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "Bueno..."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Más o menos he entendido lo del empujón."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pero ¿qué pinto yo en todo esto?"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "No puedo ser yo quien la ayude a dar ese empujón."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    with dissolve

    p "..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¿Y eso qué significa?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Que tendrías que ayudarla tú."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex03
    with dissolve

    p "¿Quieres que me folle a un tío con tetas?"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx04
    with dissolve

    tx "..."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx05
    with dissolve

    pt "¿He dicho eso en voz alta?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "En primer lugar,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx04
    with dissolve

    tx "no es un tío,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "es una mujer atrapada en el cuerpo de un hombre"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx04
    with dissolve

    tx "que ha luchado toda su vida para conseguir ese derecho."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    pt "Mejor no digo nada más en voz alta..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "En segundo lugar,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "no."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "No te estoy pidiendo que folles con ella."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "De hecho,"

    extend " lo ideal es que no hubiera penetración de ningún tipo."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris down03
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Especialmente teniendo en cuenta que tu polla no es precisamente tamaño estándar..."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows serious
    with dissolve

    tx "Lo que importa es que sea consciente de su ausencia de control,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "de que está completamente sometida a cualquier deseo a la que le expongas."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Tengo permiso para hacerle cualquier cosa?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "He dicho que tiene que pensar eso."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Pero te voy a estar observando."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx04
    with dissolve

    p "¿Vas a estar dentro con nosotros?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "No."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Si estoy allí contigo,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "será consciente en todo momento de que no eres tú quien domina la situación"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "y perderás el poder de someterla."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Creo que ya es bastante consciente que estarás ahí presente en todo momento."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Sí."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pero la sugestión y la falta de contacto visual directo"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "ayudan mucho a la inmersión."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex03
    with dissolve

    p "¿Es que tienes un agujero en la pared por donde mirar?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Os voy a estar vigilando mediante una cámara web."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "¿Tienes una webcam en una de las salas dónde tratas a tus pacientes?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Siempre."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    pt "¿Eso no es algo ilegal?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Tampoco lo escondo."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Es una de las condiciones que pongo si alguien quiere tratar conmigo,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "ya he tenido suficientes sustos en el pasado"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows angryx01
    with dissolve

    tx "por no ser capaz de demostrar lo sucedido en la intimidad del {b}calabozo{/b}."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Si veo algo fuera de lo normal,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "u oigo que usa la palabra clave,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx02
    with dissolve

    tx "la sesión habrá terminado."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    p "¿Palabra clave?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "En realidad es un ritmo,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "por si decides amordazarle la boca."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿Qué tipo de sumisión esperas que use con ella?"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Verás que en la sala dispones de bastantes recursos para poder hacer volar tu imaginación;"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "desde fustas o látigos para caricias o azotes,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "mordaza de bola,"

    extend " de hueso,"

    extend " o hasta con abertura para mantenerle la boca abierta,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "esposas con muñequeras de peluche,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "una cinta de metro y medio satinada y opaca para inmovilizar o cubrir."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "varios packs de cuerdas para {a=https://es.wikipedia.org/wiki/Bondage}{i}bondage{/i}{/a},"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "pinzas para pezones con posibilidad de descarga,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "o sujetas a su miembro por si pierde la erección,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "una jaula de castidad masculina de acero con barrotes,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "y en general, otras sorpresas que ya irás descubriendo tú mismo ahí dentro."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Ten en mente que su placer siempre lo ha basado en la dominación,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "por lo tanto,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "más en la penetración que en ser penetrada o dominada,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "de hecho,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "apenas está acostumbrada a recibir placer anal"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "más allá de un dedo furtivo o una lengua juguetona."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Así que, si pierde la erección,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "te resultará mucho más difícil convencerla a hacer algo arriesgado o doloroso."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Al mismo tiempo, ten en cuenta que su límite son tres orgasmos,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "a partir de ahí cualquier intento de dominación será completamente en vano;"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "así que daré por terminada la sesión."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pero no olvides que se trata de someterla mediante el placer y la ausencia de él;"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "no necesariamente usando el dolor extremo."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    p "Pero puedo recurrir a él."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows normal
    with dissolve

    tx "Puedes."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Pero no olvides que te estaré vigilando."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pt "Le gusta repetirse..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Y ella podrá detener la sesión en el momento que lo desee."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Entonces,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "¿crees que eres capaz de conseguirlo?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    menu  afternoon05_TxellWorkPlace_FuckHiromi_Question:

        "<Aceptar el reto>":

            call p_Help

            $pl.ch_pts("mp",3)

            $ afternoon05_TxellWorkPlace_FuckHiromi_Accepted_Cond = True

            jump afternoon05_TxellWorkPlace_FuckHiromi_Yes

        "<Negarte a ello>":

            call p_Help

            $pl.ch_pts("mp",-5)

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows normal
            with dissolve

            p "Lo lamento,"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx01
            with dissolve

            p "pero me temo que en esto no voy a poder ayudarte."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows sadx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows sadx04
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 03
            show m_exp_piris left03
            show m_exp_eyebrows sadx03
            with dissolve

            tx "Lo entiendo."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows sadx04
            with dissolve

            p "..."

            show m_exp_mouth sadbiting_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx05
            with dissolve

            pt "Qué silencio más incómodo..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows sadx02
            with dissolve

            tx "Por favor,"

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx01
            with dissolve

            tx "¿podrías ir a buscar a Hiromi y decirle que venga,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            tx "te agradecería que esperaras en esa misma sala;"

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "tengo algo que comentarte ahí."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx02
            with dissolve

            p "Como quieras."

            scene bg 05afternoon_library_door_far_bg:
                subpixel True
                truecenter
                zoom 0.5
                pause 0.5
                ease_quad 10.0 zoom 1.0
            with fade

            n "Abandonas la estancia para recorrer ese largo pasillo hasta llegar a la puerta indicada."

            
            play sound "audio/sfx/knock_wood_01.ogg"

            scene bg 05afternoon_library_door_close_closed_bg:
                truecenter
                zoom 0.5
            with fade

            play sound "audio/sfx/knock_wood_01.ogg"

            n "Al poco de llamar,"

            play sound "audio/sfx/door_open02.ogg"

            if music_play != "frailty":
                play music "audio/music/alcaknight/frailty.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "frailty"

            show bg 05afternoon_library_door_close_open_bg:
                truecenter
                zoom 0.5
            with dissolve

            
            show hiromi_gen_h_hair_back:
                hiromi_gen_body_left_zoom_0_4_pos
            show hiromi_gen_body_c_crossed_dressed:
                hiromi_gen_body_left_zoom_0_4_pos
            show hiromi_gen_h_head earrings:
                hiromi_gen_body_left_zoom_0_4_pos

            show hiromi_gen_exp_blush 01:
                hiromi_gen_exp_left_zoom_0_4_pos
            show hiromi_gen_exp_mouth sad_Silentx05:
                hiromi_gen_exp_left_zoom_0_4_pos
            show hiromi_gen_exp_eyes 04:
                hiromi_gen_exp_left_zoom_0_4_pos
            show hiromi_gen_exp_piris front04:
                hiromi_gen_exp_left_zoom_0_4_pos
            show hiromi_gen_exp_eyebrows angryx05:
                hiromi_gen_exp_left_zoom_0_4_pos

            show hiromi_gen_h_hair_front:
                hiromi_gen_body_left_zoom_0_4_pos
            with dissolve


            n "aparece Hiromi con cara de malas pulgas."

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            n "Le transmites el mensaje que te ha dado"

            show hiromi_gen_exp_mouth sadbiting_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris left04
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            play sound "audio/sfx/hit02.ogg"

            scene bg 05afternoon_library_door_close_open_bg:
                truecenter
                zoom 0.5
            with hpunch

            n "y -con cierto desdén- roza con ensañamiento y furia tu hombro al alejarse."

            pt "Sin duda,"

            pt "son tal para cual..."

            show bg 05afternoon_library_door_close_open_bg:
                subpixel True
                ease 5.0 zoom 1.0
            with dissolve

            jump afternoon05_Library

#label afternoon05_Library:

    #ono "Pum"

    #p "Desde luego,"

    #p "tiene bastantes libros."

    #n "En la enorme sala en la que te encuentras,"

label afternoon05_Library:

    $ saturation_tint_level = "default"

    play sound "audio/sfx/door_close01.ogg"

    if music_play != "Sinfonia":
        play music "audio/music/alcaknight/Sinfonia.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "Sinfonia"

    scene bg 05afternoon_library_bg:
        subpixel True
        truecenter
        zoom 0.5
        easein_quad 15.0 zoom 0.2
    with fade

    p "Desde luego,"

    p "el nombre de biblioteca le encaja bastante bien a esta habitación..."

    n "En la enorme sala en la que te encuentras,"

    n "rodeado de estanterías repletas de conocimiento y entretenimiento,"

    n "destacan los enormes sillones y butacas que hay frente a ti."
 
    p "Esta debe de ser la sala que usa para tratar a sus clientes antes de ir al \"calabozo\","

    p "me imagino..."

    show bg 05afternoon_library_bg:
        subpixel True
        ease 30.0 zoom 1.0 xpos -0.2 ypos 0.6
        
    n "Casi sin poder evitarlo, tu curiosidad te empuja a revisar qué tipo de libros rellenan esta estancia."

    n "Sin demasiada sorpresa, descubres que la mayoría tratan sobre el poder y la debilidad de la mente humana,"

    n "así como de historia, ciencia, clásicos de la literatura,"

    n "otros más actuales y populares, aunque de dudosa calidad,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    scene bg 05afternoon_library_close_bg:
        subpixel True
        truecenter
        zoom 0.65 xpos 1.8 ypos 0.4 # Sex book Begining
        pause 1.5
        ease 5.0 zoom 0.65 xpos 1.5 ypos 0.4
    with fade

    n "otro departamento entero obviamente sobre sexualidad, dominación, psicología..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    scene bg 05afternoon_library_close_bg:
        subpixel True
        truecenter
        zoom 1.0 rotate 90 xpos 0.55 ypos 1.5 # Mystery 02 Beginning
        pause 1.5
        ease 25.0 ypos -0.5 # Mystery 02 Ending
        #ypos -0.5 # Mystery 02 Ending
    with fade

    n "Sin embargo, hay una sección que te llama particularmente la atención;"

    n "libros sobre {a=https://es.wikipedia.org/wiki/Ufología}ufología{/a}, {a=https://es.wikipedia.org/wiki/Viaje_a_través_del_tiempo}viajes en el tiempo{/a},"

    n "conspiraciones en el {a=https://es.wikipedia.org/wiki/Ciudad_del_Vaticano}Vaticano{/a} y {a=https://es.wikipedia.org/wiki/Nuevo_Orden_Mundial_(conspiración)}sociedades secretas{/a},"

    show bg:
        subpixel True
        ease 30.0 ypos -3.0 # Mystery 03 Ending

    n "el {a=https://es.wikipedia.org/wiki/Antiguo_Egipto}antiguo Egipto{/a}, {a=https://es.wikipedia.org/wiki/Dioses_egipcios}dioses antiguos{/a}, {a=https://es.wikipedia.org/wiki/Magia_blanca}magia blanca{/a}, {a=https://es.wikipedia.org/wiki/Misa_negra}rituales satánicos{/a},"

    n "{a=https://es.wikipedia.org/wiki/Vampiro}vampiros{/a}, {a=https://es.wikipedia.org/wiki/Licantropía_clínica}licantropía{/a}, {a=https://es.wikipedia.org/wiki/Vida_después_de_la_muerte}más allá de la muerte{/a},"

    n "{a=https://es.wikipedia.org/wiki/H._P._Lovecraft}H.P. Lovecraft{/a}, {a=https://es.wikipedia.org/wiki/Posesión_demoníaca}posesión demoníaca{/a}, {a=https://es.wikipedia.org/wiki/Demonología}demonología{/a}, {a=https://es.wikipedia.org/wiki/Súcubo}súcubos{/a}..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    scene bg 05afternoon_library_close_bg:
        subpixel True
        truecenter
        zoom 1.0 xpos -1.6 ypos 0.6 # Interview
        pause 1.5
        ease 15.0 zoom 1.7  xpos -2.9 ypos 0.9 # Interview Close
    with fade

    n "Prestas especial atención a cierto libro,"

    n "que parece estar menos ordenadamente ubicado que los demás,"

    n "como si hubiera sido leído recientemente."

    scene 05af_lib_book 00:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0 # up
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "En él encuentras un lazo satinado de color rojo que parece hacer de marca-páginas,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    scene 05af_lib_book 01:
        subpixel True
        truecenter
        zoom 1.0 xpos -0.2 ypos 1.3
        ease 20.0 zoom 0.2 xpos 0.5 ypos 0.5 

    with fade

    # Book_01 Macho cabrío rodeado de sus hijas para ser fecundadas.

    n "al abrirlo en esa parte para revelar en qué punto de la lectura se encuentra,"

    n "descubres que dicha sección habla sobre el \"{a=https://es.wikipedia.org/wiki/Macho_cabrío}macho cabrío{/a}\"."

    n "En dicho apartado se describe uno de los propósitos del {a=https://es.wikipedia.org/wiki/Aquelarre}{i}aquelarre{/i}{/a};"

    n "la gestación de una futura nueva estirpe {a=https://es.wikipedia.org/wiki/Nigromancia}nigromántica{/a} mediante una orgía entre todas las mujeres ahí presentes,"

    n "con el símbolo fálico del hombre vestido de bestia que ha sido poseído por el mismísimo diablo,"

    n "el cual fecunda a sus propias hijas para que prosiga su linaje de {a=https://es.wikipedia.org/wiki/Bruja}brujas{/a}."

    p "..."

    p "¿Y qué ocurriría si el feto resultase ser un varón?"

    tx "Se le sacrificaría en el siguiente {b}aquelarre{/b} a los pocos meses de nacer."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "meritxell_theme"

    scene bg 05afternoon_library_bg:
        truecenter
        zoom 1.0 xpos -0.2 ypos 0.6

    show m_bodynew hips_04:
        mtxell_body_ontheright_zoom_0_3_pos

    show m_exp_blush 01:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_mouth happy_Silentx02:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyes 03:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_piris front03:
        mtxell_exp_ontheright_zoom_0_3_pos
    show m_exp_eyebrows normal:
        mtxell_exp_ontheright_zoom_0_3_pos

    show m_exp_hair_front:
        mtxell_exp_ontheright_zoom_0_3_pos
    with fade

    p "¡¿Txell?!"

    show m_exp_blush 01
    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "No te he oído entrar."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "Supongo que ya hay la suficiente confianza como para que me tutees reduciéndome el nombre." 
    #Not finished, it depends on the mood. She told him before, that her friend was sent to home.

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "..."

    #########################################################

    if config.version < "00.14.06": # Library Part.
        call endupdatescript
    
    #######################################################

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris down03
    show m_exp_eyebrows serious
    with dissolve

    tx "De hecho esa es solo una de las interpretaciones,"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "lo que se conoce como el \"diablo\","

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "en realidad suele estar sujeto a muchas otras entidades,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "cada una con sus caprichos y sus dogmas."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Se tiene la popular creencia de que es un ser único e indivisible,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "cuando en verdad es tan abundante y distópico como la humanidad misma."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows serious
    with dissolve

    tx "En este caso, adopta el cuerpo de un hombre elegido por su progenie para el ritual,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "en el que suele reunir a su abolengo de brujas,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "y copula con ellas con la intención de procrear,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious
    with dissolve

    tx "cuando el número desciende más de lo habitual;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "que suele ser alrededor de la docena..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    p "Se folla a sus propias hijas,"

    extend " para hacer nuevas hijas,"

    extend " que se follará otro día."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Es un buen resumen."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Patriarcado satanista incestuoso en su máximo esplendor."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "De este modo la sangre siempre se mantiene \"limpia\"."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Como ya te he dicho,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "te he hecho venir a la biblioteca"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "porque me gustaría hablar del libro que tienes entre las manos."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Pero te advierto que no va a ser corto,"

    extend "\nni agradable de escuchar."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿A qué te refieres?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Esta obra contiene toda la crueldad,"

    extend " sangre,"

    extend " e inmundicia"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "que pueda uno imaginarse."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "¿Estás seguro de que quieres que continúe?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    pt "Sangre y vísceras en medio de una orgía,"

    pt "qué relato más agradable me va a contar..."

    pt "¿Acaso tengo otra opción si quiero llevarte al calabozo...?"

    menu afternoon05_Library_Continue_question:

        pt "Espero que por lo menos valga la pena..."
        
        "Por favor, continúa.":

            call p_Help

            $ pl.ch_pts("mp",3)

            $ afternoon05_Library_Continue_Cond = True
            $ afternoon05_Library_Continue_WithGuro = True

            jump afternoon05_Library_Continue_question_Yes

        "Por favor, continúa;\npero agradecería no tener que ver imágenes demasiado desagradables...":

            call p_Help

            $ pl.ch_pts("mp",3)

            $ afternoon05_Library_Continue_Cond = True
            $ afternoon05_Library_Continue_WithoutGuro = True

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx02
            with dissolve

            tx "Tranquilo,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows sadx01
            with dissolve

            tx "lo entiendo."

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows sadx02
            with dissolve

            tx "A veces hasta a mí me cuesta ver estas imágenes tan desagradables..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris left04
            show m_exp_eyebrows sadx03
            with dissolve

            tx "Pero la autora del libro encontró oportuno no escatimar en detalles."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx02
            with dissolve

            p "..."

            jump afternoon05_Library_Continue_question_Yes

        "Preferiría que no, sinceramente.":

            call p_Help

            $ pl.ch_pts("mp",-1)

            if music_play != "frost_waltz":
                play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "frost_waltz"

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "No te tenía por un pusilánime."

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex01
            with dissolve

            p "Ni yo te tenía a ti por una \"{a=https://es.wikipedia.org/wiki/Vampirismo}hematofílica{/a}\"."

            show m_exp_mouth sad_Silentx09
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows angryx03
            with dissolve

            tx "..."

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx02
            with dissolve

            pt "Además, para ser sinceros,"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx01
            with dissolve

            pt "no tengo ganas de escuchar un muro de texto..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx02
            with dissolve

            tx "No te contaría esto para ponernos a tono,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with dissolve

            tx "sino para ponerte en contexto con la cita que tendrás esta noche."

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "Te refieres a..."

            jump afternoon05_Library_Continue_question_No

                #tx "Verás,"

                #tx "ayer no me vi con las fuerzas ni la confianza suficiente como para contarte cómo conocí a Neus..."

                #tx "O más bien,"

                #tx "cómo volví a recordarla."

label afternoon05_Library_Continue_question_Yes:

    $ afternoon05_Akelarre_Told = True

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "En esta versión,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "el {b}aquelarre{/b} se suele llevar a cabo una vez en cada {a=https://es.wikipedia.org/wiki/Solsticio}solsticio{/a},"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    show m_exp_eyebrows sadx01
    with dissolve

    pt "¿Solo dos veces por año?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    pt "Pensaba que en {a=https://es.wikipedia.org/wiki/Zugarramurdi}Zugarramurdi{/a} se celebraba tres veces por semana..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "con la aparición de la primera estrella en el firmamento vespertino."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Se untan agua verdinegra y repugnante, obtenida de un sapo, por sus cuerpos desnudos;"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "para conseguirla,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx03
    with dissolve

    tx "lo azotan con una varilla,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "y una vez está bien hinchado,"

    extend " lo aprietan con el pie contra el suelo"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "hasta que vomita el agua hedionda que cuidadosamente recogen y guardan."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Mientras hacen esa guarrería,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx01
    with dissolve

    tx "recitan las palabras:"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "{i}Señor,"

    extend " en tu nombre me unto;{/i}"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "{i}de aquí en adelante yo he de ser una misma cosa contigo,"

    extend " yo he de ser demonio{/i}."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Te sabes el libro de memoria?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Lo he leído muchas veces."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pt "Esta tía necesita una novia..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "En otras zonas,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "los mecanismos más usuales para convocar el ritual,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "eran una campana que tan solo oían los adeptos,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "además de un escozor en la llamada,"

    extend " \"marca del diablo\","

    extend " que el brujo ocultaba."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Algo que los inquisidores utilizaban como prueba en los juicios por brujería."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Me imagino que en la mayoría de los casos,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "fueron ellos mismos quienes debieron haber tatuado esa \"marca\" durante las sesiones de tortura."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Es bastante probable."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "La gente es bastante susceptible cuando le domina el terror a lo desconocido."

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    # Book_02 Ilustración Adoración al diablo.

    show 05af_lib_book 02:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5 
    with fade

    tx "La sesión suele iniciarse adorando al \"diablo\","

    tx "postrándose de rodillas y besándole en sus pudendas."

    pt "En sus huevos."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_03 Danza around the fire.

    show 05af_lib_book 03:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Después se mezclan entre ellos y comienzan a danzar y bailar alrededor de la figura o el fuego."

    tx "Estas sesiones se usan también en parte para borrar su rastro,"

    tx "usando el \"mal de ojo\","

    tx "o directamente con la muerte de aquellas pobres almas que se hubieran cruzado en su camino;"

    tx "bien por protección,"

    extend " venganza,"

    extend " celos,"

    extend " o por simple capricho;"

    tx "sin importarles si se trata de clérigos,"

    extend " reyes,"

    extend " ancianos,"

    extend " mujeres embarazadas,"

    extend " o recién nacidos."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with fade

    tx "Por otro lado,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "si en algún momento alguna de las hijas pronuncia el nombre de {a=https://es.wikipedia.org/wiki/Jesús_de_Nazaret}Jesús{/a},"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious
    with dissolve

    tx "el {b}aquelarre{/b} corre el riesgo de desvanecerse,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "por lo que en la próxima reunión será severamente castigada."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    pt "¿Qué se desvanecía?"

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    pt "¿El fuego?"

    extend " ¿Las mujeres bailando?"

    if night04_Neus_Blowjob_Cum_Affirmative == True:

        pt "¿O quizás se refiere a los ojos rojos que vi en la oscuridad con Neus?"

    ##

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx01
    with dissolve

    tx "El ritual acostumbra a estar dividido en tres partes;"

    # Book_04 # Ilustración Bautismo (Hija con cara ensagrentanda de sangre)

    if afternoon05_Library_Continue_WithGuro:

        hide screen Points
        hide screen quick_menu
        with dissolve

        show 05af_lib_book 04:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    else:

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve


    tx "La {a=https://es.wikipedia.org/wiki/Sacramento_de_la_penitencia}penitencia{/a} o {a=https://es.wikipedia.org/wiki/Bautismo}bautismo{/a},"

    if afternoon05_Library_Continue_WithGuro:

        window hide dissolve
        pause

    # Book_05 # Comunión (cabrío de espaldas alzando cráneo bebé y corazón)

    if afternoon05_Library_Continue_WithGuro:

        hide screen Points
        hide screen quick_menu
        with dissolve

        show 05af_lib_book 05:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    else:

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

    tx "la {a=https://es.wikipedia.org/wiki/Eucaristía}comunión{/a},"

    if afternoon05_Library_Continue_WithGuro:

        window hide dissolve
        pause

    # Book_06 # Dance around fire. (it's 04)

    show 05af_lib_book 03:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "y finalmente la {a=https://es.wikipedia.org/wiki/Misa}celebración{/a}."

    # Book_07 # Macho Cabrío vestido, hija ante sus pies.

    show 05af_lib_book 07:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 30.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "En la primera parte,"

    tx "el macho cabrío,"

    tx "revestido con ornamentos negros,"

    extend " desagradables,"

    extend " y pestilentes,"

    tx "suele recibir una a una a sus hijas postradas ante sus pies,"

    tx "las cuales se confiesan ante este y se acusan de haber entrado en una iglesia,"

    tx "de haber oído misa,"

    tx "de haber rezado,"

    tx "de los males o sacrificios que hubieran podido realizar y no hicieron,"

    tx "o de haber tenido tentaciones de abandonar el credo y construir una familia."

    tx "Estas confesiones suelen venir acompañadas por ofrendas a modo de perdón o gratitud;"

    tx "a veces son producto de un robo"

    tx "o la prueba de que se ha cometido un acto ilícito a ojos de la ley divina."

    tx "Otras son ofrendas humanas,"

    tx "generalmente niños de corta edad o bien gente de clase alta en la sociedad,"

    tx "atados y amordazados ante las patas de su padre."

    tx "Las primeras en pasar por semejante humillación"

    tx "suelen ser las hijas de mayor edad o jerarquía;"

    tx "que generalmente, si desean quedar embarazadas,"

    tx "necesitan traer a una mujer recientemente fecundada."

    tx "Para generar vida,"

    tx "el diablo necesita primero arrebatarla."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell talking

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with fade

    tx "Las últimas suelen ser novicias,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "recién iniciadas,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx04
    with dissolve

    tx "las hijas de sus hijas,"

    extend " que a duras penas han pasado por su primera menstruación;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "a estas se les coloca la marca en una parte recóndita del cuerpo"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "y pasan desde ese momento a ser miembros plenos de la cofradía incestuosa."

    ##

    if music_play != "crypticSorrow":
        play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "crypticSorrow"

    # Book_08 Illustration de misa negra, sermón

    show 05af_lib_book 08:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0 ypos 0.35
        pause 1.0
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "La segunda parte consiste en una burda copia de la misa sacrílega celebrada por el demonio,"

    tx "durante la cual se siguen los mismos pasos que en la cristiana."

    tx "Tras el sermón en el que el cabrón exhorta a sus hijas a hacer el mal,"

    tx "prometiéndoles a cambio placeres indescriptibles,"

    tx "un poder absoluto e inimaginable,"

    tx "la capacidad para manipular o comunicarse con la mente de sus víctimas,"

    extend " sus sueños,"

    tx "y otorgarles no solo la posibilidad de la inmortalidad,"

    tx "sino también la juventud eterna;"

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with fade

    p "¿Te refieres a la telepatía?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "De hecho en el libro se expone que, en la mayor parte del ritual,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "no usaban palabras para comunicarse."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows serious
    with dissolve

    tx "Una a una,"

    extend " se acercan a la figura del {b}Padre{/b}"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "y se vuelven a arrodillar ante él,"

    extend " besándole la mano izquierda,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "los pechos,"

    extend " los genitales,"

    extend " y el {a=https://es.wikipedia.org/wiki/Osculum_infame}osculum infame{/a}."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    pt "Me imagino que eso debe de ser el culo..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Según las confesiones de las supuestas brujas,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "cuando llega el momento de la consagración,"

    # Book_09 # Ilustration Heart y cráneo niño con sangre.

    if afternoon05_Library_Continue_WithoutGuro:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

    else:

        show 05af_lib_book 09:
            subpixel True
            truecenter
            zoom 1.0 xpos 1.0 ypos 0.35
            ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

        
    tx "el demonio alza el corazón aún latiendo de un recién nacido"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows angryx01
        with dissolve

    tx "derramándose su sangre por su brazo,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows serious
        with dissolve

    tx "al grito de:"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx02
        with dissolve

    tx "{i}Tomad,"

    extend " comed,"

    extend " este es mi cuerpo.{/i}"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows serious
        with dissolve

    tx "Para a continuación encumbrar del mismo modo"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows sadx01
        with dissolve

    tx "el cráneo recién cercenado de ese mismo infante,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx02
        with dissolve

    tx "invertido a modo de vaso rellenado con su sangre,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows serious
        with dissolve

    tx "oscura y caliente."

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx02
        with dissolve

    pt "¿Era necesario tanto detalle?"

    if afternoon05_Library_Continue_WithoutGuro == False:

        hide screen Points
        hide screen quick_menu
        with dissolve

        pause

        if PlatinumHelp == True:
            show screen Points()
            show screen quick_menu()

    # Book_10 # Ilustración de mujer acercándose al padre.

    show 05af_lib_book 10:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Después estas se acercan al \"altar\","

    tx "cubierto por un paño negro,"

    extend " deteriorado,"

    extend " y agujereado;"

    tx "para luego comer y beber lo que el oficiante ha \"consagrado\"."

    tx "Mientras el {b}macho cabrío{/b} les dice:"

    tx "{i}Bebed de ella todas,{/i}"

    tx "{i}porque esta es mi sangre de la Alianza,{/i}"

    tx "{i}que es derramada por muchos para perdón de los pecados.{/i}"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with fade

    p "Un tanto macabro..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "En este tipo de misas negras,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "en la sangre suelen meter algún tipo de estupefaciente para ir preparando el ambiente que vendrá después."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Lo que hay después es peor?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "Hasta aquí se podría decir que la misa negra ha sido una réplica exacta de la cristiana;"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "pero el final es completamente distinto."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    if music_play != "anguish":
        play music "audio/music/kevinmacleod/sad/anguish.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "anguish"

    # Book_11 Ilustration Dance Fire.

    show 05af_lib_book 11:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Las asistentes se abandonan en una danza que comienza con movimientos organizados;"

    tx "Brincando en círculo,"

    tx "unidas por los hombros"

    tx "o formando el {a=https://es.wikipedia.org/wiki/Uróboros}uróboros{/a}."

    pt "La serpiente que se muerde la cola."

    tx "Poco a poco,"

    tx "la celebración pierde unidad"

    tx "y en mitad del baile y el griterío,"

    tx "empiezan a consumir sustancias psicoactivas."

    pt "¿Por qué no lo llama drogas?"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_12 # WitchBroom
    show 05af_lib_book 12:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.0 ypos 0.15
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Debido a que en medio del caos es prácticamente imposible calibrar con exactitud la dosis,"

    tx "ya que la cantidad de uso habitual está muy cerca de la letal;"

    tx "este tipo de sustancias se aplicaban en forma de ungüento por vía vaginal,"

    extend " o rectal,"

    tx "mediante troncos o escobas."

    pt "De ahí me imagino que viene lo de que vuelan con ellas..."

    pt "no,"

    extend " si de volar,"

    extend " ya volaban..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_13 Frog
    show 05af_lib_book 13:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.3 ypos 0.9
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Por otro lado,"

    tx "muchos sapos son venenosos por contacto"

    tx "y su piel puede ser alucinógena,"

    tx "algo similar sucede con algunas setas venenosas;"

    tx "convirtiendo así la danza"

    tx "en algo que se va transmutando en una sucesión enajenada de sacudidas,"

    tx "risas histéricas y frenéticas,"

    extend " con movimientos erráticos."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_14 Ilustration Orgy around fire.
    show 05af_lib_book 14:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "A medida que estas van perdiendo la consciencia de la realidad,"

    tx "empiezan a toquetearse de forma descarada,"

    tx "a besarse,"

    extend " lamerse,"

    extend " a retorcerse unas con otras contra el suelo..."

    p "..."

    tx "Cuanto más repugnante y ofensivo sea el espectáculo a ojos del {b}macho cabrío{/b},"

    tx "más pronto se levanta este para copular con ellas en grupo,"

    extend " o individualmente."

    pt "Mujeres retorciéndose por el suelo mientras se besan y se masturban entre ellas,"

    pt "no me parece algo precisamente repugnante u ofensivo..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with fade

    tx "De hecho para algunos inquisidores,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "la razón última del {a=https://es.wikipedia.org/wiki/Misa_negra}sabbat{/a},"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "era precisamente el emparejamiento sexual con el diablo."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    pt "No creo que se refiera al {a=https://es.wikipedia.org/wiki/Sabbat}{i}shabbath{/i} judío{/a}..."

    # Book_15 # Ringing Bells with a roach over it at dawn.

    show 05af_lib_book 15:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.15
        ease 8.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "El {b}aquelarre{/b} termina al amanecer,"

    tx "cuando suenan las primeras campanadas de la iglesia,"

    tx "o con el canto del primer gallo."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"

    # Book_16 # Goat man dead.

    show 05af_lib_book 16:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Generalmente, el hombre poseído por el {b}macho cabrío{/b}"

    tx "moría tanto por extenuación,"

    extend " al mantener sexo desenfrenado durante toda la noche"

    tx "como por la posesión misma,"

    tx "que le causaba graves trastornos psicológicos"

    tx "y le convertían en algo menos que un ser humano."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with fade

    p "Pero con ese tipo de orgías,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "parece que el control de quien quedaba embarazada o no"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "se iba un poco a tomar por saco."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿No?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "No todos los {b}aquelarres{/b} sirven para fecundar,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "a veces son simplemente para recordar quién es el \"padre\" de ese {a=https://es.wikipedia.org/wiki/Harén}harén{/a};"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Dudo que llevaran ningún tipo de condón este tipo de gente..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "En el libro se menciona que todas ellas son estériles."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Solo en el {b}aquelarre{/b},"

    extend " su padre puede dejarlas encinta,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "sin mencionar que el ritual para embarazarlas"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "es de las cosas más desagradables que he leído..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    pt "¿Por qué tanto interés en este libro?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Lo que realmente es curioso"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "es qué tipo de entidades son llamadas al ritual."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    p "¿Euh?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿Entidades?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Estoy segura de que ya los habrás visto a estas alturas."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿A qué te refieres?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "A los ojos rojos en la oscuridad."

    if night04_Neus_Blowjob_Cum_Affirmative == True:

        show m_exp_mouth sadbiting_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        pt "Difíciles de olvidar..."

    else:

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 00
        show m_exp_piris front00
        show m_exp_eyebrows surprisex03
        with dissolve

        p "¿En la oscuridad?"

        show m_exp_mouth sadbiting_Silentx04
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows serious
        with dissolve

        p "¿De qué estás hablando?"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows sadx03
        with dissolve

        tx "No me puedo creer que aún no los hayas visto..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Verás,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "cuando te he comentado que el {b}macho cabrío{/b} se levanta solo cuanto más repugnante y ofensivo es el espectáculo,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "no me refería únicamente a ver a sus hijas regocijándose entre ellas mientras bailan"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "o se retuercen por el barro del suelo."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex02
    with dissolve

    p "En realidad me las he imaginado peleando desnudas sobre el lodo;"

    show m_exp_mouth sad_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "y yo no lo describiría precisamente como desagradable..."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    pt "Estoy seguro de que este tipo de espectáculos le gustarán más a ella que a mí..."

    # Book_17 # Host being liberated (ropes being cut)..

    show 05af_lib_book 17:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Una vez presentadas ante {b}el padre{/b},"

    tx "las ofrendas humanas se ponen en círculo alrededor del fuego."

    tx "Es durante la danza,"

    tx "que estas los liberan de sus ataduras entre risas histéricas y delirantes,"

    tx "para luego proseguir con el perturbador baile,"

    tx "desnudas y sucias de barro y sangre."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex02
    with fade

    p "¡Joder!"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    p "Soy yo y me largo cagando leches de ahí una vez liberado."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Esa es la idea."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    with dissolve

    p "¿Euh?"

    # Book_18a # Man running into darkness.

    if music_play != "movementProposition":
        play music "audio/music/kevinmacleod/fast/movementProposition.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "movementProposition"

    show 05af_lib_book 18a:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 3.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Generalmente,"

    tx "los primeros en ser liberados arrancan a correr a toda prisa"

    tx "desnudos y sin calzado, alejándose de la enorme fogata."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_18b # Man disapearing in the darkness.

    if music_play != "theDread":
        play music "audio/music/kevinmacleod/creepy/theDread.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theDread"

    show 05af_lib_book 18b:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Pero, una vez en la completa oscuridad,"

    tx "sus gritos desgarradores consiguen incluso superar el vocerío enajenado,"

    tx "y las risas histriónicas de esas perturbadas mujeres,"

    tx "parecen celebrar el sacrificio como quien celebra la victoria contra su rival."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_18c # Red eyes appearing in darkness.

    show 05af_lib_book 18c:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.5 ypos 0.45
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause


    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    tx "Al mismo tiempo que centenares de ojos rojos brillantes"

    tx "reaparecen con más intensidad en la absoluta oscuridad,"

    tx "como pidiendo más carnaza,"

    tx "mantenidos a distancia solo por el calor luminoso que ofrece la enorme fogata."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()


    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with fade

    tx "Según cuenta,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "algunos de los infantes se ahogan en sus propios llantos de terror y angustia,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "los ancianos tiemblan con tanta intensidad"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "que pierden hasta algún que otro diente por el incontrolable temblor,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "las mujeres gestantes sienten el feto en su interior más vivo que nunca,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "al mismo tiempo que empiezan a romper aguas,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "aunque apenas lleven escasos meses de embarazo."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "ni siquiera los hombres más corpulentos y valientes"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "o los que ostentan mayor posición en la cultura,"

    extend " sociedad,"

    extend " o Iglesia,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "son capaces de imaginar la horrenda atrocidad que se les avecina."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    # Book_18d Ilustración Nightmares.
    # NOT FINISHED

    show 05af_lib_book 18d:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.5
        ease 25.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Sus mentes se llenan de sus peores pesadillas,"

    tx "de aquellos recuerdos que en muchas ocasiones no te dejan dormir por las noches;"

    tx "de aquellos que te empujarían a saltar al abismo si los experimentaras con tanto realismo,"

    tx "que pareciera que los revivieras de nuevo."

    tx "La reminiscencia de aquellos seres queridos que te abandonaron cuando más los necesitabas,"

    tx "de hijos y amores fallecidos de forma injusta,"

    tx "de hermanas y hermanos muertos por crueles y desgarradoras enfermedades que son imposibles de sanar,"

    tx "de hombres sin escrúpulos que abusaron no solo de tu hospitalidad,"

    tx "sino también de tus bienes,"

    extend " de tu mujer"

    extend " y de tus hijas."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if music_play != "bentAndBroken":
        play music "audio/music/kevinmacleod/creepy/bentAndBroken.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bentAndBroken"

    # Book_18e Ilustration Violence over guests (not yet fucking).
    # NOT FINISHED

    show 05af_lib_book 18e:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.75
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Al mismo tiempo las risas de esas crueles arpías"

    tx "empiezan a resonar como enlatadas en sus cabezas"

    tx "y a ser golpeados físicamente con rudeza a lo largo y ancho de su cuerpo"

    tx "con palos,"

    extend " rocas,"

    extend " o a puño descubierto;"

    tx "con una fuerza tan sobrehumana,"

    tx "que en ocasiones algún que otro hueso se quiebra por completo."

    pt "¿A puño descubierto?"

    tx "Por si la situación no fuera lo suficientemente grotesca,"

    tx "mientras algunas siguen bailando y gritando alocadamente,"

    tx "otras agarran a sus presas y empiezan a cabalgarlos"

    tx "o a meterles el puño en ese momento por sus orificios de modo primitivo,"

    extend " asqueroso,"

    extend " y desgarrador."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

# que les salga polla es más adelante.

    # Txell Taking

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"

    hide 05af_lib_book
    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with fade

    p "¿De verdad eran capaces de tenerla dura después de todo lo que me estás contando?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "No solo ellas tomaban drogas."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    # Book_19a # Transformation of her bodies into other persons with violence.

    show 05af_lib_book 19a:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.75
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "El cuerpo de estas empieza a transmutar durante el forzado coito,"

    tx "en algunas de ellas sus pechos y caderas aumentan o reducen,"

    tx "el pelo cambia de color,"

    tx "sus pieles palidecen o se oscurecen;"

    tx "adoptan la figura de aquellos a quienes aman,"

    tx "o amaron en algún momento."

    tx "Al mismo tiempo que siguen forzándolos con torpeza,"

    tx "los golpean o los estrangulan mientras les escupen y los insultan."

    tx "A veces incluso cambian completamente de sexo"

    tx "o sencillamente les crece un enorme miembro de entre sus piernas,"

    tx "manteniendo su figura femenina,"

    tx "para humillar y sodomizar a sus presas."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_19b Illustration Bright Red Eyes.

    show 05af_lib_book 19b:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.75
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Pero sus ojos permanecen en todo momento brillantes,"

    tx "con el mismo color rojizo sangriento que los rodea en la oscuridad."

    pt "Recuerdo que cuando mordió a Dídac,"

    extend " sus ojos eran casi rojizos..."

    if night04_Neus_Blowjob_Cum_Affirmative:

        pt "Aunque cuando tenía mi polla en su boca,"

        extend " parecían más bien violáceos..."

        pt "¿Por qué...?"

    tx "Sus víctimas gritan de horror,"

    tx "pero cualquier intento de sacárselas de encima"

    tx "o golpearlas es completamente inútil."

    tx "La fuerza que poseen sobrepasa los límites humanos."

    tx "A medida que el orgasmo se acerca,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_20 # Illustration Becoming Sucubo (Look from behind -William Blake Demon-)

    show 05af_lib_book 20:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "sus aspectos degeneran en algo más monstruoso y aterrador,"

    tx "sus pieles palidecen,"

    tx "sus cabellos se alargan y oscurecen,"

    tx "de sus piernas empieza a crecer un pelo sombrío y tupido,"

    tx "hasta ocultar completamente su piel"

    tx "sus pies se prolongan exageradamente,"

    tx "mientras sus dedos se unen para convertirse en una enorme pezuña."

    tx "Los dedos y uñas de las manos,"

    tx "así como sus brazos,"

    tx "se extienden de un modo exagerado,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"


    # Book_21 #  Creepy Demon Jaws

    show 05af_lib_book 21:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "sus mandíbulas se despliegan de forma inhumana,"

    tx "como las de una serpiente antes de devorar su presa, "

    tx "sus lenguas repletas de sangre y saliva"

    tx "brotan de sus fosas guturales extendiéndose de forma grotesca,"

    tx "unas protuberancias emergen de sus cráneos como cuernos largos,"

    extend " negros y robustos;"

    tx "de sus espaldas emergen alas oscuras y membranosas como las de un murciélago,"

    tx "de sus traseros emerge una cola reptiliana,"

    extend " negra y viscosa;"

    tx "y sus dientes incrementan de tamaño al mismo tiempo que se afilan tenebrosamente."

    tx "Cuando la transformación parece culminar,"

    # Book_22 Red eyes looking to her victim.

    show 05af_lib_book 22:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "sus brillantes ojos rojizos se redireccionan de nuevo con apetito hacia sus víctimas"

    tx "y sin que estos tengan posibilidad alguna de librarse,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_23 Blood Festival and Darkness

    if afternoon05_Library_Continue_WithoutGuro:
        hide 05af_lib_book
        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris left04
        show m_exp_eyebrows sadx01
        with fade

    else:

        show 05af_lib_book 23:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    tx "son parcialmente devorados sin compasión en distintas partes de su cuerpo,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx02
        with dissolve

    tx "en el cuello,"

    extend " el pecho,"

    extend " algún que otro dedo,"

    extend " una mejilla,"

    extend " la nariz,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

    tx "o incluso en el propio miembro viril en el momento del clímax,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

    tx "desgarrándoles de su carne,"

    extend " sangre,"

    extend " y esperma."

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx01
        with dissolve

    p "..."

    if afternoon05_Library_Continue_WithoutGuro == False:

        hide screen Points
        hide screen quick_menu
        with dissolve

        pause

        if PlatinumHelp == True:
            show screen Points()
            show screen quick_menu()

    # Txell Talking

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious

    if afternoon05_Library_Continue_WithoutGuro:
        with dissolve
    else:
        with fade

    tx "En cualquier caso,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    tx "el falo les es arrancado de un modo u otro"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y es arrojado a la oscuridad donde esos escalofriantes orbes rojos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "se propagan hacia él,"

    extend " como depredadores hambrientos acechando su carnaza."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Entre gritos de desesperación y dolor,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "empiezan a descuartizar lo que queda de su cuerpo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    tx "hasta que saciado su frenesí enfermizo de ira o capricho,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "arrojan el resto de lo que queda lejos de la fogata,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "donde desaparecen en la negrura de la noche."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Cuando el anfitrión lo considera oportuno,"

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    # Book_24 # Demon Asking one Daughter. (Hand of Goat asking to coming.)

    show 05af_lib_book 24:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "reclama la atención de la hija que previamente le había pedido ser fecundada,"

    tx "para que vuelva a traer su ofrenda."

    pt "Una de las mujeres que está embarazada."

    tx "Cuanto más hermosa y joven sea esta,"

    tx "mejor será el fruto de su unión."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_25 # Random woman getting naked.

    show 05af_lib_book 25:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Su hija la desnuda ante él"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_26 # Random woman over Macho Cabrío(Disfraz).

    show 05af_lib_book 26:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "para luego abrirla de piernas entre gritos ahogados por el bullicio y las risas,"

    tx "hasta posarla encima de su enorme,"

    extend " hedionda,"

    extend " viscosa,"

    extend " y negra polla en erección."

    p "¿Cómo de enorme?"

    tx "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    if music_play != "frost_waltz":
        play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "frost_waltz"

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with fade

    tx "¿De verdad?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "¿Con todo lo que he dicho hasta ahora,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "lo único que te importa es comparar tamaños?"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Me entras en detalles de lo asquerosa,"

    extend " pútrida,"

    extend " maloliente,"

    extend " y salpicante que es toda la situación,"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "pero te pido un detalle más,"

    extend " y me llamas falocentrista..."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "La narradora no entra en pormenores en cuanto a centímetros,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "pero por lo que acontece a continuación,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "me imagino que es incluso más grande que la de un potro semental."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "¿O es que también estás celoso de los penes ecuestres?"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿A continuación...?"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    if music_play != "lightless_dawn":
        play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "lightless_dawn"

    # Book_27 # Difraz Goat, Dick deep in a random pussy.

    show 05af_lib_book 27:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.3 ypos 0.15
        ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Una vez llegado hasta el fondo,"

    tx "el atuendo de bestia que lleva el hombre"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_28 # macho cabrío volviéndose en Monster.

    show 05af_lib_book 28:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.0
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "empieza a pegársele en la piel como si formara parte de la suya propia,"

    tx "al mismo tiempo que su cuerpo aumenta de tamaño,"

    tx "sus pies se alargan hasta convertirse en pezuñas,"

    tx "su mandíbula se extiende en horizontal,"

    tx "como si se tratara del morro de un caballo,"

    tx "mientras su nariz se aplasta de un modo grotesco,"

    tx "sus ojos se agrandan y se apartan uno del otro,"

    tx "y sus pupilas se aplastan,"

    tx "hasta que su rostro se asemeja más a una cabra monstruosa."

    p "Y su polla..."

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    tx "Efectivamente,"

    tx "su miembro viril crece en consonancia a su cuerpo"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if afternoon05_Library_Continue_WithoutGuro:
        hide 05af_lib_book
        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with fade

    else:

        # Book_29 Random woman Dying for the huge penis.

        show 05af_lib_book 29:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 7.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    tx "y la pobre y desgraciada mujer sufre un dolor indescriptible,"

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx09
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows angryx03
        with dissolve

    else:

        hide screen Points
        hide screen quick_menu
        with dissolve

        pause

        if PlatinumHelp == True:
            show screen Points()
            show screen quick_menu()

        # Book_30 Rests on ground.

        show 05af_lib_book 30:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 7.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    tx "muriendo desangrada y abierta en canal entre sus piernas."

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx02
        with dissolve

    else:

        hide screen Points
        hide screen quick_menu
        with dissolve

        pause

        if PlatinumHelp == True:
            show screen Points()
            show screen quick_menu()

        # Book_31 Macho Cabrío eating, or swallowing from top (como si comiera uvas en plano romano).
        show 05af_lib_book 31:
            subpixel True
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5
            ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
        with fade

    tx "El monstruo entonces recoge lo que queda del feto y lo engulle entre sus fauces,."

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

    tx "tirando a un lado el cuerpo retorcido y sin vida de esa mujer."

    if afternoon05_Library_Continue_WithoutGuro:
        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows sadx02
        with dissolve

    else:

        hide screen Points
        hide screen quick_menu
        with dissolve

        pause

        if PlatinumHelp == True:
            show screen Points()
            show screen quick_menu()

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    # Book_32 # macho cabrío Open legs waiting her daughter.
    show 05af_lib_book 32a:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Abriendo de nuevo sus peludas patas empapadas en sangre,"

    tx "invita a su hija a subirse."

    tx "Con una sonrisa que helaría la sangre a las mismísimas {a=https://es.wikipedia.org/wiki/Gorgona}gorgonas{/a} de la mitología griega,"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    show 05af_lib_book 32b:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 8.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "emprende el ascenso por sus felpudas rodillas como si fuera una araña,"

    tx "mientras su cuerpo se va transmutando en lo que anteriormente ya he descrito;"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    # Book_33 # Daughter becoming a Succubus over Macho Cabrío dick (Sexy monster but faceless).

    show 05af_lib_book 33:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.45 ypos 1.3
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "como una mujer de cabello largo oscuro y piel pálida,"

    tx "cubierta por un tupido pelo por debajo de la cintura con patas de cabra,"

    tx "alada,"

    extend " y con cuernos."

    pt "La imagen clásica de una súcubo..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_34 # Daughter Fucking her Father.

    show 05af_lib_book 34a:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.0
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Sin demasiados reparos,"

    extend " empieza a cabalgarlo llenando su barriga"

    tx "y desangrándose la entrepierna al mismo tiempo que su interior;"

    # Book_35 # Long tongues Touching.

    show 05af_lib_book 35a:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "mientras sus desproporcionadamente extensas lenguas"

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    show 05af_lib_book 35b:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade


    tx "se entremezclan en una desagradable unión de saliva,"

    extend " sangre,"

    extend " y gritos;"

    pt "Un beso de película,"

    extend " vamos..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_36 # Huge hands grabing her ass with blood.

    show 05af_lib_book 36:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5
        ease 20.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade


    tx "Mientras este,"

    tx "con sus enormes zarpas, le clava las uñas en sus nalgas"

    tx "agarrándola con fuerza,"

    extend " para obligarla a aumentar el ritmo de su cabalgata."

    tx "Arañazos,"

    extend " bofetones,"

    extend" y bocados,"

    tx "hasta sangrar por todo el cuerpo,"

    extend " en un acto tan obsceno y violento"

    tx "que hasta a la autora del libro le resulta difícil de describir."

    pt "No será por la falta de detalles hasta el momento..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_37 # Cumshot inside daughter womb getting fullfilled too much.

    show 05af_lib_book 37:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.6 ypos 0.0
        ease 5.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Todo ello culmina en el momento en que termina eyaculando en su interior."

    p "..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Book_38 # Baby girl crying.

    show 05af_lib_book 38:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.55 ypos 0.9
        pause 1.0
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with fade

    tx "Si el fruto de su unión es una chica,"

    tx "esta crecerá junto a su madre y sus tías,"

    tx "hasta que tenga la edad del primer sangrado,"

    tx "momento en que se la llevará por primera vez al rito de iniciación."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with fade

    p "¿Y si resultase ser varón?"

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "También lo acabará llevando a la ceremonia,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "pero no precisamente para su iniciación."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "En el siguiente ritual después del embarazo,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    p "solo habrán pasado seis meses."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "Aunque, por lo que cuentas,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    p "quizás no son necesarios los nueve meses,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    p "al fin y al cabo tampoco es un embarazo habitual..."

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "No,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "pero por lo visto,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "independientemente de lo avanzado que estuviera previamente el feto,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "los nueve meses son igualmente necesarios en el nuevo vientre de la bruja."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve
    
    p "Ya veo..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Así que no habría dado a luz hasta el posterior {b}aquelarre{/b},"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "donde habría tenido el bebé tres meses antes de que este sucediera."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Así es."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Esa madre no solo habría llevado nueve meses en su barriga"

    p "a alguien a quien no sabe si terminaría sacrificando,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "sino que, cuando el infante varón naciera finalmente,"

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "ya sabría con certeza que acabaría muriendo,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve
    
    p "probablemente de la forma más cruel y sanguinaria posible;"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    p "y aun así tendría que convivir con él durante tres meses más."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Sin mencionar que será ella misma quien deberá sacrificar a su propio hijo frente a su padre."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    p "Joder..."

    # Book_00 #Cover of the book.

    show 05af_lib_book 00:
        subpixel True
        truecenter
        zoom 1.0
        ypos 1.0 # up
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade
    

    tx "\"{b}Entrevista con una bruja{/b}\"."

    tx "Así es como se titula el libro."

    pt "{i}Anna Arrós{/i}..."

    pt "este nombre me recuerda al de {a=https://es.wikipedia.org/wiki/Anne_Rice}{i}Anna Rice{/i}{/a}..."

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    # Txell Talking

    hide 05af_lib_book
    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with fade

    tx "Habla de la experiencia de una de estas {b}hijas{/b},"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "de toda la vivencia experimentada en sus largos años de existencia"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "y de que, debido al amor que siente al coger a su hijo por primera vez en sus brazos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "decide abandonar el credo,"

    extend " y a sus hermanas,"

    extend " para poder salvarlo."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "Lo que no entiendo es por qué no lo abandonaría antes,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    p "después de todas las atrocidades que me has contado."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Bueno..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows serious
    with dissolve

    tx "El libro es bastante extenso en detalles que te hacen comprender mejor"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "qué es lo que realmente las retiene irremediablemente en este oscuro culto."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿El poder?"

    extend " ¿La inmortalidad?"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    p "¿La capacidad de cambiar el aspecto o manipular a la gente?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "El sexo."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "¿En serio?"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "No sé tú,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    p "pero yo no me veo a una ninfómana,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    p "por muy desesperada que esté,"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    p "capaz de realizar ni siquiera la más inocente de las atrocidades que me has contado."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Imagina beber el más exquisito champán,"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "y la sensación del coito más sensual que hayas tenido,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "súmale el éxtasis del fumador de opio al darle la primera calada a la pipa,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "y puede que empieces a hacerte una mínima,"

    extend " infinitesimal idea,"

    extend " de lo que ellas sienten."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    pt "Esta {a=http://little-regina-blue.tumblr.com/post/75582101239/imagine-drinking-the-finest-champagne-and-the}descripción{/a} ya la he oído en alguna parte..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Los drogadictos modernos mentirán,"

    extend " robarán,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y matarán por sus pequeños viajes al Cielo;"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "el suyo es inimaginablemente mejor,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "dependen de ello para sobrevivir"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "y además las hace inmortales."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "¿Puedes imaginar lo que harías para saciar esa hambre?"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Pero,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "según lo que comentas,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    p "se supone que la narradora del libro consiguió abandonar el credo."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Así es."

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "Entonces en teoría,"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02
    with dissolve

    p "existe la posibilidad de huir."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Pero ¿a qué precio?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    p "¿A qué te refieres?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Lo que sean esos \"ojos rojos\","

    extend " parecen estar en comunicación con lo que sea ese {b}macho cabrío{/b}."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Es como si fuera su catalizador de poder."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "En el momento en el que una de sus hijas huye,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "no puede volver a alimentarse de otro ser humano sin tomar precauciones"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "o usar sus poderes a la ligera."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "De lo contrario,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "sería como lanzar una baliza para ser encontrada"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "y sería sentenciada a un horrible castigo."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "Eso significa que pudo alimentarse de forma normal,"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿no?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "La comida mundana no le quita la hambruna,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "el agua o el vino ya no le sacia."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    pt "¿Por eso Neus es vegana?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    pt "Aunque sean verduras, sigue siendo comida..."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    pt "¿No?"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Entonces de qué se alimentaría?"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Animales de menor tamaño que apenas mitigan esa sed,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "pero consiguen pasar desapercibidas para aquellos que nunca dejan de observar."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Palomas,"

    extend " ratas,"

    extend " cucarachas,"

    extend " gusanos..."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex03
    with dissolve

    p "¡¿Estás hablando de zoofilia con cucarachas?!"

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "No necesariamente,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "tanto la sangre como el esperma"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "en realidad funcionan como conductores de ese reclamo que tan desesperadamente buscan."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Pero lo que realmente alimenta a esos entes oscuros,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "es la existencia misma."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "La vida se paga con la muerte."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Aunque así es posible que consiga sobrevivir;"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "en realidad su cuerpo se irá degradando con el tiempo"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "hasta convertirse en algo menos que piel arrugada y decrépitos músculos"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "y con los años solo quedará un recuerdo horripilante de lo que una vez fue."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "De hecho, en el libro ya comenta cómo empieza a notar los efectos de esa {b}desnutrición{/b}."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "También expone que la mejor manera para que en un futuro nunca pueda ser encontrada"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "sería arrancándose los ojos,"

    extend " y perforarse los tímpanos."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    p "¿No sería más fácil suicidarse?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Si hiciera eso,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "sus recuerdos serían canalizados a esas entidades,"

    extend " y por lo tanto,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "el lugar donde escondió a su hijo llegaría hasta su padre,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "que no dudaría en encontrarlo y matarlo."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Aun así,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "arrebatarse la vida,"

    extend " no es algo que les resulte tan simple."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "A pesar de que se tirara de un rascacielos,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "intentara ahogarse bajo el agua,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "aunque necesitaría ayuda para hundir su cuerpo bajo el agua;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "se amputara el cuerpo,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "se disparara en la cabeza,"

    extend " o el corazón,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "su cuerpo volvería a unirse,"

    extend " o reconstruirse para volver a la vida,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "al caer la noche siguiente."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Aunque la velocidad y carencia de dolor"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "dependería de los últimos sacrificios otorgados."

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex03
    with dissolve

    p "Y por lo visto, las ratas y los gusanos no serían demasiado apreciados..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Eso parece."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿La luz del sol no las mata?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "No son vampiras."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "Lo parecen..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Aunque sí es cierto que no pueden usar esos poderes a la luz del sol,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "y por lo tanto son más vulnerables durante el día."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Entonces serían completamente inmortales?"

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "No."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Solo la destrucción absoluta de su cuerpo es capaz de otorgarles el {b}descanso eterno{/b}."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "¿Como una bomba?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Si explotaran quizás quedaría algún resto intacto."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Pero si su cuerpo arde en llamas,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "difícilmente podría regresar de entre los muertos."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Como imaginarás,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "no es precisamente la forma más agradable de pasar a mejor vida."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Entonces, en teoría,"

    extend " la {a=https://es.wikipedia.org/wiki/Inquisición_española}Inquisición{/a} seguía alguna clase de pista acertada"

    show m_exp_mouth sadbiting_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex03
    with dissolve

    p "cuando decidió terminar con la vida de las brujas en la hoguera..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Es posible."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "Pero estoy convencida de que no llegaron a quemar ni una sola bruja real."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "Hombre,"

    extend " si se supone que acertaron con el método,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex03
    with dissolve

    p "me imagino que por lo menos con la primera acertarían."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "En el libro se comenta que en su máximo esplendor,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "son capaces de transmutar en cuestión de horas su cuerpo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    tx "para ocultarse entre la muchedumbre,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "o conseguir una apariencia mucho más seductora"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "para poder conquistar a su siguiente presa."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿No has dicho que en el {b}aquelarre{/b} se transformaban en cuestión de segundos?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "En el ritual,"

    extend " la historia es completamente distinta;"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    tx "el {b}macho cabrío{/b} está presente,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "todas sus hijas están alrededor de una enorme fogata,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "en una de las noches más mágicas del año,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    pt "Lo único que puede matarlas, por lo visto..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "rodeadas de sacrificios a escasas horas de ser ofrecidos"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "a las tenebrosas entidades que acechan en la oscuridad."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Por lo visto, el flujo de energía que se cocería ahí,"

    extend " debería de ser importante..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Eso parece."

##

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Todo esto del libro está muy bien,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "pero..."

    if night04_Neus_Blowjob_Cum_Affirmative == True:

        show m_exp_mouth sad_Silentx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows suspiciousx02
        with dissolve

        p "aparte de los ojos rojos,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "¿a qué viene todo este rollo que me has contado?"

label afternoon05_Library_Continue_question_No:

    $ afternoon05_NeusMeeting_Told = True

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Verás,"

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "ayer no me vi con las fuerzas"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "ni la confianza suficiente"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "como para contarte cómo conocí a Neus..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "O más bien,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "cómo volví a recordarla."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02
    with dissolve

    pt "¿Volver a recordarla?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Hará casi un año,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "se sentaba en ese mismo sillón de ahí,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "mientras yo escuchaba sus dificultades para resistir el anhelo,"

    extend " y la desesperación,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "que sufría en sus carnes."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "De cómo recorría las calles a altas horas de la noche en busca de algún bar nocturno,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "de alguna discoteca vespertina"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "con jóvenes mostrando sus vergüenzas embriagados por el exceso de alcohol,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris down03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "de algún callejón oscuro y maloliente donde se frecuentaran malas compañías,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "le parecía que al tener cerca la tentación le aliviaría las ansias."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    p "Eso parece un poco ilógico..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Algunos clientes tienen esa falsa ilusión;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "que no es otra cosa que la gula arrastrándolos al deseo prohibido."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Al principio pensaba que hablaba de su adicción al sexo."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    tx "Como cualquier otro cliente que llama a mi puerta,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "me gusta pensar que cada paciente es especial"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "y todos los casos son únicos y fascinantes;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "pero el suyo era sin duda algo fuera de mi especialidad,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "solo que en aquel entonces,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "no tenía ninguna posibilidad de ser consciente de ello."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Su cuerpo temblaba,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "sus labios estaban completamente resecos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "sus mejillas daban fe de que, apenas unas horas antes,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "había experimentado un llanto considerable,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "sus ojos sufrían de grandes ojeras por clara falta de sueño,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "al mismo tiempo que seguían estando algo húmedos,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "sus pupilas estaban midriáticas,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "y su respiración era arrítmica."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Ahí me di cuenta de que, en realidad, lo que sufría"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "era un grave estado del síndrome de abstinencia."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "pero a un nivel que no había visto nunca."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Sin embargo,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "el foco de su deseo estaba completamente relacionado con el sexo;"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "oscuro,"

    extend " perturbador,"

    extend " y sin tabúes."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Me dijo que por razones religiosas no podía,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "bajo pena capital,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "ser palpada o penetrada en ningún tipo de contacto físico directo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "ni siquiera usando un dedo,"

    extend " o un simple e inocente beso."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Obviamente no le pregunté qué tipo de religión le prohibía semejante particularidad,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "pero tampoco me interesé demasiado en aquel entonces."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Me hizo prometer que una vez estuviéramos en el calabozo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "la revistiera a toda ella de látex o cuero,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "la mantuviera atada"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "y amordazada en todo momento,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y que no la liberara bajo ninguna circunstancia,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "hasta que hubiera calmado sus ansias."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Que intentara saciarla mejor a través del dolor,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "no tanto con el placer"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "y que evitara a ser posible penetrar su interior"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "o que la llevase al orgasmo."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx02
    with dissolve

    tx "En realidad no entendía muy bien"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "qué es lo que le estaba causando ese estado físico tan preocupante,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "pero me dijo que si conseguía saciar sus necesidades sexuales,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "era posible que consiguiera ayudarla."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Todo hay que decirlo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "no suelo rechazar clientes a la ligera,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "mucho menos si me resultan interesantes"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows normal
    with dissolve

    tx "y menus aún si me pagan cuantiosos {b}agradecimientos{/b}."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Pero a pesar de que había algo en ella que me resultaba inquietante y perturbador,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "y que mi sentido común me gritaba a todas luces,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    tx "{i}huye,"

    extend "\nlárgate de aquí{/i};"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "mi niña interna,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "curiosa y traviesa"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "no podía estar más apresada en el interés que me causaba esa chica de ojos color esmeralda,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "y de apenas metro y medio de altura."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Solía pedirme las cosas más arriesgadas que he llegado a hacer con una clienta,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "sobre todo,"

    extend " me pedía humillación extrema,"

    extend " y dolor sin límites."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Desde luego,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "quería castigarse a sí misma por algo que nunca llegó a revelarme por completo."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Aunque parezca pequeña e indefensa,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "la sensación que me produjo al conocerla a lo largo de esos meses fue todo lo contrario."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Me considero una persona abierta,"

    extend " curiosa"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y que ha recorrido medio mundo en busca de nuevas experiencias,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "tanto en manjares,"

    extend " arqueología,"

    extend " historia,"

    extend " arte,"

    extend " religiones,"

    extend " amistades..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows serious
    with dissolve

    pt "La modestia no es su fuerte..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Sin embargo cuando hablaba con ella,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "sentía que no era más que una cría"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "que apenas estaba abriendo la ventana para observar al vecindario."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "La riqueza de detalles con que exponía sus experiencias,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "la sensación de abismo al relatarme la pérdida de sus seres queridos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious
    with dissolve

    tx "el relato de una vida que parecía tan fascinante como inalcanzable."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    tx "Me quedaba tan absorta prestándole atención sentada en mi butaca,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "que a veces olvidaba que era ella quien me pagaba para escucharla."

    ###

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "He tratado con muchas sumisas que me han pedido que las tratase como a un sucio trapo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows normal
    with dissolve

    tx "e incluso he conseguido ayudar a un gran número de ellas que estaban al borde del suicidio"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows serious
    with dissolve

    tx "debido a la rudeza con la que se trataban a sí mismas."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Pero con Neus,"

    extend " todo era distinto..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Aunque era ella la que estaba atada,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    tx "y yo quien usaba el látigo,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "e incluso en alguna que otra ocasión,"

    extend " el consolador con arnés para sodomizarla,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "en mi interior sentía algo completamente distinto."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Por las noches solo podía soñar con su rostro y su cuerpo desnudo,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "cada semana contaba los días que me faltaban para tener de nuevo una sesión con ella,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "en mis fantasías necesitaba que me azotara y humillara,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "sentía que un par de horas con ella a la semana no eran suficientes,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "necesitaba tenerla a mi lado."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Sin mencionar que, aunque la mayoría de las veces la amordazaba,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "a veces me parecía oír sus súplicas en mi cabeza."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Sorprendentemente,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "parecía que el tratamiento la estaba ayudando a recuperar su estabilidad física y emocional;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "De hecho, en algunas sesiones tenía la impresión de que su cuerpo no era el de siempre,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "en ocasiones sus pechos lucían más esbeltos y voluminosos,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "su cuerpo parecía haber aumentado de tamaño,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "con un rostro que aparentaba mayor madurez,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "sus labios más carnosos..."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "Pero en las siguientes reuniones la veía como siempre."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "En ese entonces lo achaqué a mi falta de sueño."

    ##

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Lo que realmente sentía a esas alturas,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "era entre fascinación,"

    extend " miedo"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "y un deseo galopante e incontrolable por ella."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Nunca he intimado con ninguna paciente,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "es una norma que la cumplo a raja-tabla,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "pero, por alguna razón,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "ella me inducía a todo lo contrario,"

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx02
    with dissolve

    tx "a quemar en la hoguera las normas."

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Ya no quería causarle dolor,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "ni siquiera quería ayudarla como clienta,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "solo quería complacerla,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "de un modo que ni siquiera había llegado a experimentar con {b}Hiromi{/b}."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "A medida que iban pasando las semanas,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    tx "apenas sin darme cuenta,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "mi profesionalidad iba haciéndose a un lado"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "para dar paso a un interés emocional y cercano hacia ella,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "llamándola fuera de la oficina,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "excusándome en que se trataba de un método habitual en mis tratamientos;"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "algo completamente falso,"

    extend " y que jamás había hecho con un cliente."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Cada vez me resultaba más difícil amordazarla o azotarla,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "en cada nueva reunión intentaba cubrir menos partes de su cuerpo"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "para poder apreciar mejor su desnuda piel."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Intentaba aproximarme más a ella en cada nueva sesión,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve
    
    tx "al principio con caricias a través de los guantes de látex,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "luego sutilmente con la mano desnuda,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "con el tiempo conseguí convencerla,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "de que, por razones terapéuticas,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "necesitaba unos masajes,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "hasta llegué a darle abrazos una vez las reuniones finalizaban."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Desde luego ella se quedaba sorprendida,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "pero lo achacó a la confianza que hasta un profesional puede tener con su cliente con el paso del tiempo."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "Soy incapaz de describirte lo que siento cada vez que recuerdo su sonrisa,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "o su cara angelical cuando me contagiaba con su risa..."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Hasta que, en una despedida,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "fui incapaz de resistirme a darle un beso apasionado entremezclando nuestras lenguas."

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Allí es cuando todo el castillo de naipes se desmoronó de golpe."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Había incurrido en uno de los mayores errores que una profesional puede cometer."

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx07
    with dissolve

    tx "Me había enamorado perdidamente de mi paciente."

    show m_exp_mouth sadbiting_Silentx11
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx07
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Su rostro de sorpresa y al mismo tiempo de lo que me pareció completo terror,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx06
    with dissolve

    tx "se convirtió en un gélido recuerdo que nunca podría sacarme de la cabeza."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "O eso es lo que pensé."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx07
    with dissolve

    p "¿Qué?"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "En ese momento me quedé sin palabras,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious
    with dissolve

    tx "no sabía cómo reaccionar,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx04
    with dissolve

    tx "había soñado tantas veces con esa situación,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "pero nunca me hubiera podido imaginar lo que realmente ocurrió."

    show m_exp_mouth sadbiting_Silentx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Su expresión cambió repentinamente,"

    if music_play != "ossuary_6_air":
        play music "audio/music/kevinmacleod/ossuary_6_air.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "ossuary_6_air"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx05
    with dissolve

    tx "volviéndose en algo más bien tétrico e inquietante,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "su piel palideció mientras abría sus ojos de par en par"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows sadx02
    with dissolve

    tx "a la vez que el arco que envuelve sus pupilas transmutó hacia un violeta vivaz"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "con un brillo propio tan intenso,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "que hasta me cegó los ojos."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    pt "Violetas,"

    pt "cuando mordió a Dídac parecían más bien rosados,"

    extend " tirando a rojizos..."

    if night04_Neus_Blowjob_Cum_Affirmative == True:

        pt "pero ayer,"

        extend " mientras tenía mi polla en su boca,"

        extend " sí que eran completamente violáceos."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "Lo siguiente que recuerdo es estar sentada en mi despacho,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "con la puerta cerrada,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "y recibiendo una llamada de mi secretaria"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "preguntándome si quería que pasara el siguiente paciente."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "No recordaba el brillo en sus ojos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "ni el beso,"

    extend " ni la sesión anterior,"

    extend " ni ninguna otra;"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "nada;"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "como si nunca hubiera existido."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows normal
    with dissolve

    tx "Lo primero que me pasó por la cabeza"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "fue coger mi agenda para ver cuál era el siguiente cliente."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "No estaba en su sitio,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "no la encontré por ninguna parte."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Todas sus grabaciones habían desaparecido,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "todo rastro de ella se había desvanecido completamente."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "Luego descubrí que fui yo misma quien destruyó todas las pruebas"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "para luego olvidar por completo lo que había hecho."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex03
    with dissolve

    p "Si tan bien supo cubrir sus huellas,"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿cómo es que ahora la recuerdas con tanta nitidez y me cuentas todo esto?"

    show m_exp_mouth sadbiting_Silentx10
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx04
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Semanas después,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "en lo que a todas luces fue una pesadilla,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "aunque lo viví en mis carnes como si fuera más real que la vida misma."

    show m_exp_mouth sadbiting_Silentx09
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    pt "¿Más real?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Me encontraba en medio de un prado salvaje en plena noche,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "sintiendo el frío y la humedad del césped bajo mis pies."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "A lo lejos se divisaba una enorme fogata."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Me acerqué a ella por mera curiosidad"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "y porque prácticamente no podía ver nada más a mi alrededor."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    tx "A medida que me acercaba a ella,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "las llamas se hacían más grandes,"

    extend " más luminosas"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "y mi entorno se oscurecía,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "hasta que solo me envolvió la negrura más absoluta."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "El viento dejó de soplar"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "y los grillos cesaron en su canto nocturno."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Lo único que se oía era el crepitar de las llamas."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Hasta que de la completa oscuridad un par de pequeños ojos rojizos"

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "extremadamente separados uno del otro aparecieron de la oscuridad."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "De ahí surgió la figura humanoide de un {b}macho cabrío{/b} gigante y monstruoso"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris down02
    show m_exp_eyebrows angryx01
    with dissolve

    tx "con una polla desproporcionada y amorfa."

    if afternoon05_Akelarre_Told == True:

        show m_exp_mouth sadbiting_Silentx08
        show m_exp_eyes 08
        show m_exp_piris empty
        show m_exp_eyebrows sadx06
        with dissolve

        pt "El mismo macho cabrío del {b}aquelarre{/b} del libro..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Sin darme tiempo a reaccionar,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "me agarró por los brazos,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "me desgarró el traje de noche con un par de zarpazos"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "y poniéndome a cuatro patas empezó a violarme brutalmente"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "sin ningún tipo de piedad sobre el húmedo,"

    extend " frío,"

    extend " y duro césped."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx07
    with dissolve

    tx "Lo único que podía hacer era gritar,"

    extend " chillar,"

    extend " y llorar."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "Mis manos sangraban del roce constante con el suelo,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "mis rodillas estaban completamente en carne viva"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "y todo mi cuerpo estaba entumecido por el dolor."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Las constantes embestidas las sentía como si me quisiera abrir en canal."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx07
    with dissolve

    tx "Soy consciente de que la percepción del tiempo se ralentiza en las peores experiencias,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "pero aun así,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "juraría que me estuvo violando durante horas."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Después de lo que me pareció una eternidad,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx05
    with dissolve

    tx "terminó corriéndose de un modo inhumano,"

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows angryx04
    with dissolve

    tx "hinchándome la barriga,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "hasta el punto de que su esperma salía a borbotones de mi entrepierna."

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "Cuando aún seguía sintiendo su corrida derramándose por mis temblorosas piernas,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx07
    with dissolve

    tx "al mismo tiempo que escuchaba el goteo incesante contra el césped,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "percibí su respiración apenas a escasos centímetros de mi cuello,"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx02
    with dissolve

    tx "y susurrándome al oído me dijo con voz profunda y gutural;"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx03
    with dissolve

    tx "{i}Recuerda{/i}."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "Acto seguido me agarró con fuerza de la muñeca"

    show m_exp_mouth sad_Talkingx12
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    tx "y me lanzó con fuerza a las llamas,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows angryx04
    with dissolve

    tx "haciéndome caer encima de los afilados troncos que ardían con enorme intensidad."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "¿Entonces despertaste?"

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "No..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Pensé que nunca experimentaría nada peor que ser empotrada bestialmente durante horas"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "por un monstruo inmundo y escalofriante..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Pero, sinceramente,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    tx "después de estar ardiendo durante lo que me pareció otra eternidad..."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "no sabría decirte qué fue peor."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx07
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 07
    show m_exp_piris empty
    show m_exp_eyebrows sadx06
    with dissolve

    pt "Uno no suele tardar tanto en morir en la hoguera,"

    extend " y aún menos en una pesadilla..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Cuando finalmente creí haber muerto entre las llamas;"

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "volví a abrir los ojos para encontrarme sorprendida en mi cama,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris down02
    show m_exp_eyebrows sadx05
    with dissolve

    tx "completamente empapada en sudor."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows surprisex002
    with dissolve

    tx "En ese instante todos mis recuerdos de lo sucedido con Neus regresaron a la vez."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Fue en aquel entonces cuando descubrí"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "que no solo seguíamos coincidiendo en las clases de arte,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "a las que me apunté para estar más cerca de ella,"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "sino que además estaba encaprichándose de ti."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "Con sinceridad,"

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "desde ese momento empecé a odiarte."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    pt "No lo había notado..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Pero tampoco podía decirte nada;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Aun recordando lo ocurrido con Neus,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "seguía dándome cierto respeto el hecho de que no entendía nada de lo que había sucedido."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Pero independientemente de los horrores que sufrí en la pesadilla,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "y de sus ojos brillantes;"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "lo que realmente me estremece"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx04
    with dissolve

    tx "y aún no me deja dormir por las noches,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx05
    with dissolve

    tx "es su rostro de sorpresa,"

    extend " tristeza"

    extend " y terror"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx06
    with dissolve

    tx "al descubrir que la amaba."

    if music_play != "frost_waltz":
        play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "frost_waltz"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Supongo que el destruir todas las pruebas de su existencia"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "y borrarte la memoria para que la olvidaras,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx04
    with dissolve

    p "tampoco te ayudará mucho a romper el hielo con ella..."

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx06
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx05
    with dissolve

    tx "No hagas que cambie mi opinión sobre ti, [protname]."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pt "A veces soy un poco bocazas..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Así que opté por la opción más bochornosa y despreciable,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx04
    with dissolve

    tx "os estuve observando a distancia en el bar."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "También te seguí en los grandes almacenes con tu \"compañero\" de piso."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "Porque es compañero..."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "¿Verdad?"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows serious
    with dissolve

    tx "Horas después,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    tx "recibí tu llamada;"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "en el móvil cuyo número jamás te di."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex03
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "Si por lo que dices,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "cuando hablé contigo te lo di mientras coqueteaba contigo,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    tx "es algo que no recuerdo;"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "pero cuando me dijiste que tenía los {b}ojos rojos{/b},"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "ahí es cuando realmente me llamaste la atención."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Qué diablos son estos ojos rojos?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx03
    with dissolve

    tx "No lo sé."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    if afternoon05_Akelarre_Told == True:

        p "¿Y el libro que me has estado describiendo antes?"

    else:

        p "¿Y el libro que me querías describir antes?"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¿De dónde lo sacaste?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Me lo encontré en mi buzón pocos días después de esa pesadilla."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Al principio pensé que era de algún paciente,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve
    
    tx "pero luego entre las páginas vi una nota en la que ponía"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "{i}Recuerda{/i}."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Hmm..."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "¿Qué?"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    if music_play != "vanishing":
        play music "audio/music/kevinmacleod/vanishing.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "vanishing"


    p "Todo lo que me has contado parece sacado de una novela macabra escrita por un sádico lunático."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pero como dijiste ayer,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "he visto cosas que no encajan con la realidad en la que vivimos..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "No te hubiera contado todo esto si no tuviera una buena razón."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Al final pensaré que te preocupas más por mí que por Neus."

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "..."
##

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Si me has llegado a odiar tanto,"

    if music_play != "meritxell_theme":
        play music "audio/music/meritxell_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "meritxell_theme"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¿por qué me has ofrecido la posibilidad de ayudar a tu ex?"

    show m_exp_mouth sad_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex03
    with dissolve

    p "La excusa de que era tu única opción,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "de que estabas entre la espada y la pared,"

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "no cuela."

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "Podías haberla despedido y dejar las cosas como estaban,"

    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "sin embargo has pensado que yo era una opción."

    show m_exp_mouth sadbiting_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    p "¿Por qué?"

    show m_exp_mouth sadbiting_Silentx09
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex03
    with dissolve

    tx "Como ya te he dicho,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "al principio el rencor hacia ti iba incrementando"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    tx "al mismo tiempo que veía cómo Neus intentaba acercarse a ti."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Por un lado me alegraba cuando la ignorabas por completo,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "pero al mismo tiempo sentía asco al ver cómo podías despreciarla de ese modo."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "¿Yo la ignoraba?"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    tx "¿No veías que intentaba entablar conversación contigo"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "con las mejillas completamente rojizas y la voz temblorosa?"

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pero si lo único que me decía era buenos días,"

    extend " buenas tardes,"

    extend " y que pases un buen día..."

    show m_exp_mouth sadbiting_Silentx10
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx05
    with dissolve

    p "A eso lo llamo educación,"

    show m_exp_mouth sad_Silentx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx06
    with dissolve

    p "no entablar conversación."

    show m_exp_mouth sad_Talkingx11
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx05
    with dissolve

    tx "No seas imbécil,"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Neus es una chica tremendamente insegura de sí misma,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "solo intentaba iniciar una conversación contigo."

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Pensaba que habías dicho que era valiente y con una vasta experiencia en el mundo."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Nunca he dicho que fuera valiente."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Cuando he llegado a la oficina y me has presentado a Hiromi,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "le has dicho que has conseguido olvidarla y pasar página."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿Es Neus la razón?"

    show m_exp_blush 03
    show m_exp_mouth sadbiting_Silentx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx03
    with dissolve

    tx "..."

    show m_exp_blush 04
    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Sí..."

    show m_exp_blush 05
    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    p "Desde luego,"

    show m_exp_mouth sadbiting_Silentx11
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx05
    with dissolve

    p "no tienes mucha suerte con las relaciones amorosas..."

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx07
    with dissolve

    tx "..."

    show m_exp_blush 04
    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx06
    with dissolve

    pt "Tengo que aprender a callarme..."

    
    show m_exp_blush 03
    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows angryx04
    with dissolve

    tx "Debo confesarte,"

    show m_exp_blush 02
    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "que aunque me resultases alguien arrogante y prepotente en un inicio,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pt "Me lo dice el ejemplo vivo de la humildad..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "a medida que he ido conociéndote,"

    if Martq >= 11 or Cartq >= 12 and  inMACBAq >= 1: ## Just 1 failed.

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

        tx "no solo me has sorprendido por tus conocimientos de arte y cultura..."

    if Martq == 12 or Cartq == 13 and inMACBAq >= 2: # All Correct.

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Respondiendo todas y cada una de mis preguntas de forma correcta,"

        show m_exp_mouth sad_Talkingx008
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "algo que,"

        extend " sinceramente nunca me hubiera imaginado,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 07
        show m_exp_piris empty
        show m_exp_eyebrows sadx02
        with dissolve

        tx "incluso algunas me hubieran costado a mí..."

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 06
        show m_exp_piris front06
        show m_exp_eyebrows sadx03
        with dissolve

        pt "Será..."

    elif Martq >= 11 or Cartq >= 12 and  inMACBAq >= 1: ## Just 1 failed.

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows normal
        with dissolve

        tx "Respondiendo a casi todas mis preguntas de forma correcta,"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx01
        with dissolve

        tx "algo que sinceramente me sorprendió bastante."

    elif Martq >= 9 or Cartq >= 10:  # Some failed.

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "me sorprendió que respondieras algunas de mis preguntas correctamente."

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex02
        with dissolve

        p "No me lo pusiste fácil tampoco..."

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "No soy de poner las cosas fáciles."

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        pt "Lo he notado."

    else: #Martq >= 5 or Cartq >= 6: # Some answered, but very badly.

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex002
        with dissolve

        tx "y a pesar de que respondieras bastante mal las preguntas que te hice en el museo..."

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex001
        with dissolve

        pt "Será..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Hay algo en ti que me recuerda extrañamente a Neus."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex001
    with dissolve

    p "..."

    if ((Martq >= 11 or Cartq >= 12) and  (inMACBAq >= 1) and (FuckH_SUCCESS == True)):
        $ FuckT_Possible = True

    ## TxellSlave > 1: ## Means you enjoy to be submissive.

    if Martq >= 9 or Cartq >= 10: # Minimum of good answers. You can be fucked or fuck her.

        jump afternoon05_TxellWorkPlace_FuckTxell_Beginning_YES

    else:

        jump afternoon05_TxellWorkPlace_FuckTxell_Beginning_NO

label afternoon05_TxellWorkPlace_FuckTxell_Beginning_YES:

    if FuckH_SUCCESS:

        show m_exp_blush 03
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx01
        with dissolve

        tx "Y al verte sodomizar y poner bajo tu control a Hiromi..."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx03
        with dissolve

        tx "Has conseguido despertar algo en mí"

        show m_exp_blush 04
        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows sadx04
        with dissolve

        tx "que creía que jamás sería capaz de sentir por un hombre."

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex01
        with dissolve

        p "Creo que es la primera vez que me dices algo bonito con sinceridad."

###

    show m_exp_blush 05
    show m_exp_mouth sadbiting_Silentx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "..."

    show m_exp_blush 04
    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "Sé que esta noche tienes la última cita con ella;"

    if FuckT_Possible == True:

        show m_exp_blush 03
        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        tx "pero me pregunto..."

        show m_exp_mouth sadbiting_Silentx07
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows suspiciousx01
        with dissolve

        p "..."

        show m_exp_mouth sadbiting_Silentx09
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx01
        with dissolve

        tx "..."

        show m_exp_mouth sadbiting_Silentx08
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        p "¿Qué?"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Si tienes aún alguna hora libre..."

        show m_exp_mouth sadbiting_Silentx09
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex03
        with dissolve

    else:

        
        show m_exp_blush 03
        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        tx "pero me pregunto,"

        show m_exp_blush 02
        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "si tienes alguna hora libre."

        show m_exp_mouth sadbiting_Silentx03
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows suspiciousx01
        with dissolve

    p "¿Para qué?"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx03
    with dissolve

    tx "¿Tengo que hacerte un mapa?"

    show m_exp_mouth sad_Silentx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "Por favor."

    if FuckT_Possible == True:

        show m_exp_blush 03
        show m_exp_mouth sadbiting_Silentx07
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx03
        with dissolve

        tx "..."

        show m_exp_blush 04
        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx04
        with dissolve

        tx "Me gustaría ver si eres capaz de hacerme lo mismo que le has hecho a Hiromi."

        show m_exp_mouth sadbiting_Silentx05
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex02
        with dissolve

    else:

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "Me parece que no estás entiendo a lo que me refiero."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex03
        with dissolve

        p "Entonces,"

        extend " explícate mejor."

        if TxellSlave > 1:

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Ayer me comentaste que la idea de ser dominado"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "era algo que no te disgustaba del todo."

            if TxellSlave > 3:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Es más,"

                extend " diría que hasta me lo estabas pidiendo..."

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "¿O me estabas mintiendo?"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            p "..."

            menu FuckT_Beginning_domination_lie_question:

                pt "Lo que le dije ayer en el museo de que me gustaría ser dominado..."

                "Te dije la verdad.":
                    call p_Help
                    $ pl.ch_pts("mp",1)

                    show m_exp_mouth happy_Silentx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    tx "Hmm..."

                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx02
                    with dissolve

                    tx "No esperaba menos de ti."

                "Lo siento, pero te mentí.":
                    call p_Help
                    $ pl.ch_pts("mp",-3)

                    show m_exp_mouth sad_Silentx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx05
                    with dissolve

                    tx "..."

                    show m_exp_mouth sad_Talkingx005
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "¿Y qué diablos esperabas conseguir con eso?"

                    show m_exp_mouth sad_Silentx09
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    tx "¿Seducirme y dominarme mintiéndome en la cara al decirme que eres sumiso?"

                    show m_exp_mouth sad_Silentx10
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx04
                    with dissolve

                    tx "¿Qué clase de estrategia cutre de pacotilla es esa?"

                    show m_exp_mouth sadbiting_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx03
                    with dissolve

                    p "..."

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Como ya te dije,"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "yo soy la que domina."

        show m_exp_mouth sad_Talkingx008
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex001
        with dissolve

        tx "Así que bien puedes aceptar mis normas,"

        extend " o irte."

        show m_exp_mouth sadbiting_Silentx07
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex02
        with dissolve

    p "¿Quieres que le ponga los cuernos a Neus para que me deje por ti?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "No..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    tx "No es eso..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Pensaba que eras lesbiana y detestabas a los hombres."

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "No detesto a los hombres,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "sencillamente los aborrezco."

    show m_exp_mouth sadbiting_Silentx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pt "Ya..."

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Mira,"

    extend " es igual."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03
    with dissolve

    tx "Olvídalo."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    ##

    ## CHOICE

    menu FuckT_Beginning_domination_question:

        pt "Si dejo que me domine ella, es probable que tenga problemas mañana para poder sentarme..."

        "<Intentar dominarla>" if FuckT_Beginning_domination_question_failed == False:
            call p_Help

            if FuckT_Possible == True:
                $ pl.ch_pts("mp",+3)

                #if TxellSlave > 2: # Just for telling him that she though you would prefer to be submissive.


                jump FuckT_Beginning_domination_Yes

            else:

                $ FuckT_Beginning_domination_question_failed = True

                show m_exp_mouth sadbiting_Silentx07
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex02
                with dissolve

                p "¿Eres consciente de que estarás completamente bajo mi dominio,"

                show m_exp_mouth sad_Silentx08
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows serious
                with dissolve

                p "y de que es bastante probable que experimentes en tus carnes...?"

                stop music fadeout 3.0
                $ music_play = ""

                play sound "audio/sfx/meme_surprise02.ogg"

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex02
                with dissolve

                tx "¡Quieto ahí!"

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                p "..."

                if music_play != "funkorama":
                    play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "funkorama"

                show m_exp_mouth sad_Talkingx008
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex002
                with dissolve

                tx "Estás de coña,"

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                tx "¿verdad?"

                show m_exp_mouth sad_Silentx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with dissolve

                p "..."

                show m_exp_mouth sad_Talkingx007
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx02
                with dissolve

                tx "Te acabo de decir que soy yo quien domina la situación en mis relaciones sexuales."

                show m_exp_mouth sad_Silentx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with dissolve

                menu FuckT_Beginning_domination_try_question:

                    pt "¿Y ahora qué le digo?"

                    "Quizás te gustaría probar ser sumisa por una vez.":
                        call p_Help

                        if FuckH_SUCCESS == True:

                            $ pl.ch_pts("mp",1)

                            show m_exp_mouth sad_Talkingx07
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows serious
                            with dissolve

                            tx "Confieso que me has sorprendido con Hiromi."

                            show m_exp_mouth sad_Talkingx007
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                            tx "Pero no caigas en el error de creer que por ello,"

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows serious
                            with dissolve

                            tx "vas a poder hacer lo mismo conmigo."

                            show m_exp_mouth happy_Talkingx06
                            show m_exp_eyes 02
                            show m_exp_piris front02
                            show m_exp_eyebrows sadx01
                            with dissolve

                            tx "Te estoy muy agradecida,"

                            show m_exp_mouth happy_Talkingx08
                            show m_exp_eyes 03
                            show m_exp_piris right03
                            show m_exp_eyebrows serious
                            with dissolve

                            tx "por lo que estoy dispuesta a no ser tan..."

                            show m_exp_mouth happy_Talkingx07
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                            tx "dura contigo,"

                            show m_exp_mouth happy_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows surprisex001
                            with dissolve

                            tx "o, en realidad,"

                            extend " puedo serlo más si lo prefieres de ese modo."

                            show m_exp_mouth happy_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx01
                            with dissolve

                        else:

                            $ pl.ch_pts("mp",-2)

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows serious
                            with dissolve

                            tx "..."

                            show m_exp_mouth sad_Silentx05
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows surprisex001
                            with dissolve

                            p "¿Qué...?"

                            if afternoon05_TxellWorkPlace_FuckHiromi_Accepted_Cond == True:

                                show m_exp_mouth sad_Talkingx008
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows surprisex03
                                with dissolve

                                tx "No has sido capaz ni de dominar a Hiromi,"

                                show m_exp_mouth happy_Talkingx07
                                show m_exp_eyes 03
                                show m_exp_piris front03
                                show m_exp_eyebrows angryx01
                                with dissolve

                                tx "¿y ahora crees que podrías hacerlo conmigo?"

                            else:

                                show m_exp_mouth sad_Talkingx09
                                show m_exp_eyes 08
                                show m_exp_piris front08
                                show m_exp_eyebrows angryx02
                                with dissolve

                                tx "No has querido ni dominar a Hiromi,"

                                show m_exp_mouth sad_Talkingx10
                                show m_exp_eyes 02
                                show m_exp_piris front02
                                show m_exp_eyebrows angryx02
                                with dissolve

                                tx "y ahora crees que aceptaré ser dominada,"

                                show m_exp_mouth sad_Talkingx009
                                show m_exp_eyes 03
                                show m_exp_piris front03
                                show m_exp_eyebrows angryx02
                                with dissolve

                                tx "por alguien tan pusilánime con el tema sexual."

                            show m_exp_mouth sad_Talkingx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx01
                            with dissolve

                            tx "No,"

                            extend " gracias."

                            show m_exp_mouth sad_Talkingx09
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows angryx02
                            with dissolve

                            tx "O aceptas ser un buen sumiso,"

                            extend " o te vas."

                            show m_exp_mouth sad_Talkingx08
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                            tx "No hay mucho más que hablar sobre este tema."

                            show m_exp_mouth sad_Silentx06
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx02
                            with dissolve

                        p "..."

                        #jump FuckT_Beginning_domination_question

                    "Yo también soy una persona únicamente dominante.":
                        call p_Help

                        if FuckH_SUCCESS == True:

                            $ pl.ch_pts("mp",-2)

                            show m_exp_mouth sad_Talkingx09
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows serious
                            with dissolve

                            tx "Por mucho que me hayas ayudado con Hiromi,"

                            show m_exp_mouth sad_Talkingx07
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows angryx01
                            with dissolve

                            tx "las cosas siguen como antes."

                        else:

                            $ pl.ch_pts("mp",-3)

                            show m_exp_mouth sad_Talkingx08
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows angryx02
                            with dissolve

                            tx "Parece que te cuesta entenderlo..."

                            show m_exp_mouth sad_Talkingx008
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows angryx02
                            with dissolve

                            tx "Así que te lo voy a repetir por última vez."

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows serious
                        with dissolve

                        tx "Prefiero las mujeres,"

                        extend " y soy estrictamente dominante."

                        show m_exp_mouth sad_Talkingx008
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx01
                        with dissolve

                        tx "Así que lo aceptas,"

                        extend " o te largas."

                        show m_exp_mouth sad_Silentx06
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx02
                        with dissolve

                    "Tenía que intentarlo...":
                        call p_Help

                        $ pl.ch_pts("mp",-1)

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows normal
                        with dissolve

                        tx "¿Y quedar estúpidamente en ridículo sabiendo de antemano la respuesta?"

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx01
                        with dissolve

                        tx "Te tenía por alguien ligeramente más inteligente,"

                        extend " [protname]."

                        show m_exp_mouth sad_Silentx07
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                    "Lo siento...":
                        call p_Help

                        $ pl.ch_pts("mp",-2)

                        show m_exp_mouth sadbiting_Silentx06
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "..."

                        show m_exp_mouth sad_Talkingx08
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        tx "Se me están quitando hasta las ganas de someterte..."

                        show m_exp_mouth sad_Talkingx07
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        tx "No hagas que me arrepienta."

                        show m_exp_mouth sad_Silentx07
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx01
                        with dissolve

                jump FuckT_Beginning_domination_question

        "<Intentar violarla>" if FuckT_Beginning_domination_question_failed == True:
            call p_Help

            call WIP

            jump FuckT_Beginning_domination_question

        "<Decirle que te gustaría ser dominado por ella>":
            call p_Help
            #$ pl.ch_pts("mp",+1)

            jump FuckT_Beginning_domination_Pasive

        "<Decirle que lo mejor es dejarlo aquí e irte a casa>":
            call p_Help
            #$ pl.ch_pts("mp",+1)

            show m_exp_mouth sad_Silentx08
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex03
            with dissolve

            if music_play != "bittersweet":
                play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bittersweet"

            p "Tienes razón,"

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "es mejor no complicar las cosas."

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Te agradezco lo que me has contado sobre Neus."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows serious
            with dissolve

            tx "..."

            jump FuckT_Beginning_domination_goHome

            #label FuckT_Beginning_domination_goHome
            # tx "No sé cuales son realmente sus intenciones contigo,"
            # tx "ni sé muy bien porque convirtió a tu amigo en una mujer,"
            # pt "Mejor no comentarlo..."

label FuckT_Beginning_domination_Pasive:

    if TxellSlave > 2:

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows suspiciousx01
        with dissolve

        tx "Con lo que me dijiste ayer,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "ya me imaginaba que preferirías ser sometido a dominar la situación."

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        p "..."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    tx "Está bien."

    if music_play != "funkorama":
        play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "funkorama"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pero quiero dejar las cosas bien claras."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿A qué te refieres?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "¿Eres consciente de que estarás completamente bajo mi dominio?"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "Y cuando digo \"COMPLETAMENTE\","

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "no lo digo a la ligera."

    show m_exp_mouth sadbiting_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Sí..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "¿Y que también vas a dejar de ser virgen por detrás?"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "Euh..."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    tx "¿Cómo sé que eres virgen analmente?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Digamos que una no necesita ser una profesional en este campo,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "para saber eso de ti."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    menu FuckT_Beginning_domination_Pasive_anal_question:

        pt "Si dejo que me domine ella, es probable que tenga problemas mañana para poder sentarme..."

        "Preferiría seguir manteniendo mi virginidad anal intacta.":
            call p_Help

            if FuckT_Possible == True:

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Hmm..."

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows surprisex01
                with dissolve

                tx "Teniendo en cuenta que al final has podido ayudarme con lo de Hiromi,"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                tx "supongo que te has ganado el derecho a pedirme ese favor."

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                tx "Pero ten en cuenta que, en todo lo demás,"

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx01
                with dissolve

                tx "pienso tratarte como a un cliente más."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx02
                with dissolve

                tx "Y te aseguro que no suelo ser demasiado clemente con ellos..."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with dissolve

                p "..."

            else:

                show m_exp_mouth sad_Talkingx005
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex001
                with dissolve

                tx "Me temo que perdiste ese privilegio,"

                if afternoon05_TxellWorkPlace_FuckHiromi_Accepted_Cond == True:

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx01
                    with dissolve

                    tx "al no conseguir tratar a Hiromi."

                else:

                    show m_exp_mouth sad_Talkingx08
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx02
                    with dissolve

                    tx "al no aceptar tratar a Hiromi."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            tx "Entonces,"

            extend " ¿qué me dices?"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            menu FuckT_Beginning_domination_Pasive_anal_question_02:

                "De acuerdo.":
                    call p_Help

                    if FuckT_Possible == False:

                        $ FuckT_Beginning_domination_Pasive_anal_permision = True

                    jump FuckT_Beginning_domination_Pasive_Accepted

                "Lo siento, pero me niego":
                    call p_Help

                    show m_exp_mouth sad_Talkingx007
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    tx "Una lástima..."

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows normal
                    with dissolve

                    pt "Eso lo dirás por ti."

                    jump FuckT_Beginning_domination_goHome

                    #label FuckT_Beginning_domination_goHome
                    # tx "No sé cuales son realmente sus intenciones contigo,"
                    # tx "ni sé muy bien porque convirtió a tu amigo en una mujer,"
                    # pt "Mejor no comentarlo..."


        "Está bien.":
            call p_Help

            $ FuckT_Beginning_domination_Pasive_anal_permision = True

label FuckT_Beginning_domination_Pasive_Accepted:

    if FuckT_Beginning_domination_Pasive_anal_permision == True:

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows normal
        with dissolve

        pt "¡¿CÓMO QUE ESTÁ BIEN?!"

        show m_exp_mouth happy_Silentx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        pt "¡¿ESTÁ BIEN QUE UNA LESBIANA LOCA DEL COÑO ME QUIERA FOLLAR EL CULO?!"

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        pt "¡¿QUIEN DIABLOS ESTÁ TOMANDO DECISIONES POR MÍ?!"

        show m_exp_mouth sad_Talkingx006
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows normal
        with dissolve

        tx "No temas..."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx01
        with dissolve

        tx "Recuerda que soy una profesional."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx02
        with dissolve

        tx "Pero eso no significa que no vayas a sufrir..."

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "Aunque es bastante probable,"

        extend " que haya otras cosas que te vayan a doler más..."

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

        pt "¡¿Y SE SUPONE QUE ESO TIENE QUE TRANQUILIZARME?!"

    else:

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows normal
        with dissolve

        pt "¡¿Cómo que estoy de acuerdo en que una {b}jodida sádica lesbiana{/b} me trate como a un puto trapo?!"

        show m_exp_mouth happy_Silentx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        pt "¡¿En qué momento he cambiado tanto mi forma de pensar?!"

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        pt "¡¿Es que me he vuelto loco?!"

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

        pt "¡¿Quién está tomando decisiones por mí?!"


    call WIP

    jump morning05_NeusFinalDate


label FuckT_Beginning_domination_Yes:

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Eres consciente de que estarás completamente bajo mi dominio,"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with dissolve

    p "y que es bastante probable que experimentes en tus carnes,"

    show m_exp_mouth sadbiting_Silentx04
    show m_exp_eyes 03
    show m_exp_piris down03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "el monstruo que tengo entre las piernas?"

    show m_exp_mouth sadbiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Soy consciente."

    if TxellSlave > 2:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows suspiciousx01
        with dissolve

        tx "Pensé que con lo que me dijiste ayer,"

        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows suspiciousx02
        with dissolve

        tx "preferirías ser más bien sumiso."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx03
        with dissolve

        p "Bueno,"

        extend " te comenté que no me disgustaba la idea,"

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex01
        with dissolve

        p "pero contigo prefiero ser dominante ahora mismo."

        show m_exp_mouth happybiting_Silentx03
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows sadx01
        with dissolve

        tx "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    p "Entonces ve al calabozo y espérame ahí."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "..."

    show m_exp_mouth happybiting_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    tx "..."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx02
    with dissolve

    tx "Como quieras..."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "Y a partir de ahora,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    p "no me llames por mi nombre."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "..."

    p "Llámame..."

    menu afternoon05_Library_protmastername_question:
        
        "[protname]":

            call p_Help

            $ protmaster = protname.strip()

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Ese es tu nombre."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx03
            with dissolve

            p "Sí..."

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with dissolve

            tx "¡¿Entonces?!"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "No es cómo me llamo,"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "es el modo en que debes decir mi nombre."

            show m_exp_mouth sadbiting_Silentx06
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "Hmm..."

            show m_exp_blush 03
            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Creo que te sigo..."

            show m_exp_blush 04
            show m_exp_mouth happybiting_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            pt "¿En serio?"

            pt "porque ni yo mismo lo entiendo..."

            jump afternoon05_Library_protmastername_after

        "Maestro.":

            call p_Help

            $ protmaster = "Maestro"

            show m_exp_blush 03
            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "¿Quieres que sea tu alumna?"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "¿Es que tienes algo que enseñarme?"

            show m_exp_blush 04
            show m_exp_mouth happybiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            p "Es posible."

            show m_exp_mouth happybiting_Silentx06
            show m_exp_eyes 06
            show m_exp_piris front06
            show m_exp_eyebrows sadx01
            with dissolve

            jump afternoon05_Library_protmastername_after

        "Mi Señor.":

            call p_Help

            $ protmaster = "Mi Señor"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Lo dices como si yo fuera de tu propiedad."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Y así será mientras estemos en el calabozo."

            show m_exp_blush 03
            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Hmm..."

            show m_exp_blush 04
            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "Me gusta."

            show m_exp_mouth happybiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            pt "¿En serio?"

            jump afternoon05_Library_protmastername_after

        "Domador de culos.":

            call p_Help

            $ protmaster = "Domador de culos"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex002
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "¿De culos...?"

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            tx "¿Qué clase de nombre es ese?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex03
            with dissolve

            p "Me gusta tu culo,"

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "y lo voy a domar."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Tengo otras partes en mi cuerpo."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿En serio?"

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            p "No lo había notado."

            show m_exp_mouth happybiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_blush 03
            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "Pícaro..."

            show m_exp_blush 04
            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            jump afternoon05_Library_protmastername_after

        "Benito Camela.":

            call p_Help

            $ protmaster = "Benito Camela"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "{size=15}Ven y tócamela...{/size}"

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            tx "¿Eres consciente de que cada vez que tenga que llamarte por ese nombre"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx01
            with dissolve

            tx "perderé la más mínima libido que pueda tener?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            p "Quizás sea al contrario,"

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "ya que al ser un nombre tan incómodo para ti,"

            show m_exp_mouth sad_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "vas a tener que someterte más a mis deseos."

            show m_exp_mouth sad_Silentx07
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows serious
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with dissolve

            tx "No confundas sumisión con erotismo."

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            tx "Por mucho que logres que te obedezca,"

            show m_exp_mouth sad_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with dissolve

            tx "si no estoy bien lubricada ahí abajo,"

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            tx "no voy a disfrutarlo demasiado."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex03
            with dissolve

            p "¿No has sido tú la que ha dicho que las mejores experiencias"

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "son aquellas en las que no has tenido ni un solo orgasmo?"

            show m_exp_mouth sadbiting_Silentx07
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "..."

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            p "¿Qué tal si me dejas tomar a mí las decisiones?"

            show m_exp_mouth happybiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            jump afternoon05_Library_protmastername_after

        "Vegeta.":

            call p_Help

            $ protmaster = "Vegeta"

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "Como al {a=https://es.wikipedia.org/wiki/Vegeta}Príncipe de los Saiyajins{/a}."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Hmm..."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Es posible que sea el único hombre al que le quedan bien esas enormes entradas que tiene."

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            tx "Y aunque aborrezco a este tipo de hombre déspota,"

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            tx "arrogante,"

            extend " envidioso,"

            extend " narcisista,"

            extend " egoísta,"

            extend " y prepotente,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "reconozco que desde pequeña siempre he tenido un amor platónico por ese personaje."

            show m_exp_mouth happybiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pt "Quizás de ahí venga todo su odio al {a=https://es.wikipedia.org/wiki/Macho_ibérico}macho ibérico{/a}..."

            pt "que en la realidad,"

            pt "nunca logró encontrar a un {a=https://es.wikipedia.org/wiki/Saiyajin}Saiyajin{/a} con cola por delante,"

            extend " y por detrás..."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows sadx02
            with dissolve

            tx "Aunque te falte pelo,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx01
            with dissolve

            tx "no se puede negar que eres tan musculoso como él,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            tx "y quizás más alto."

            show m_exp_mouth happybiting_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 08
            show m_exp_piris empty
            show m_exp_eyebrows sadx01
            with dissolve

            tx "Aunque no me quejaré por ello..."

            show m_exp_mouth happybiting_Silentx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            jump afternoon05_Library_protmastername_after

        "<Personalizado>":

            call p_Help

            $ protmaster = renpy.input(_("¿Cómo debería de llamarme?"))
            $ protmaster = protmaster.strip()
            if not protmaster:
                $ protmaster = "Maestro"

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Llámame [protmaster]."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            tx "..."

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx02
            with dissolve

            tx "Eh..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "¿En serio?"

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¿Te parece que estoy de broma?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx03
            with dissolve

            tx "..."

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex001
            with dissolve

            jump afternoon05_Library_protmastername_after

label afternoon05_Library_protmastername_after:

    tx "..."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows surprisex002
    with dissolve

    tx "Como quieras..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx04
    with dissolve

    tx "[protmaster]."

    show m_exp_mouth happybiting_Silentx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx06
    with dissolve

    call WIP

    # NOT FINISHED # TXELL DOMINATION.

    jump morning05_NeusFinalDate

    #jump endupdate


label afternoon05_TxellWorkPlace_FuckTxell_Beginning_NO:

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    show m_exp_blush 01
    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Sé que esta noche tienes la última cita con ella."

label FuckT_Beginning_domination_goHome:

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    tx "No sé cuáles son realmente sus intenciones contigo,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "ni sé muy bien por qué convirtió a tu amigo en una mujer,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    pt "Mejor no comentarlo..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx01
    with dissolve

    tx "y aunque en el fondo sé,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    tx "de hecho estoy segura,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "que no es una mala persona;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    tx "la estuve tratando durante más de medio año"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    tx "y no soy de las que se enamoran de una persona sin alma ni corazón."

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Aun así,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "te recomiendo precaución,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "tampoco es alguien con quien puedas bajar la guardia."

    if afternoon05_Akelarre_Told == True:

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx01
        with dissolve

        tx "Espero que también te resulte útil lo que te he contado del libro."

        show m_exp_mouth sadbiting_Silentx05
        show m_exp_eyes 08
        show m_exp_piris empty
        show m_exp_eyebrows sadx01
        with dissolve

        p "Hmm..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Mucha suerte, [protname]."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Gracias por todo, Txell."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    jump morning05_NeusFinalDate

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################


label afternoon05_TxellWorkPlace_FuckHiromi_Yes:

    show m_exp_mouth happy_Silentx01
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "No veo por qué no."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "Al fin y al cabo he conseguido que me invitaras a tu oficina,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "me imagino que el tema con Neus habrá ayudado;"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx03
    with dissolve

    p "pero algo habré conseguido despertar en ti,"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001
    with dissolve

    p "si me ofreces la oportunidad de sodomizar a tu ex,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "que encima fue quien te aventuró en este mundillo."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    tx "..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    tx "Esa arrogancia te puede ser útil;"

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "hasta cierto punto."

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "Aquí tienes la llave del calabozo,"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    tx "te doy cinco minutos para que te familiarices con lo que vas a encontrar ahí."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "Tienes permiso para usarlo todo siempre y cuando seas responsable y cuidadoso."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Pasado ese tiempo oirás que golpea la puerta."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    tx "A partir de ahí ya no podré guiarte más."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    tx "¿De acuerdo?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "No lo haría de ningún otro modo."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    tx "..."

############################ ############################ ############################ ############################ ############################

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"
    
    scene bg 05afternoon_dungeon_bg:
        truecenter
        #zoom 0.5 xpos 1.75 ypos 0.5 # Top Left 0.5zoom
        zoom 1.0 
        xpos 3.5 ypos .35 # Top left

    with fade

    pt "No mentía."

    pt "Realmente parece un calabozo..."

    show bg:
        subpixel True
        ease 10.0 xpos 3.0 ypos .3 # Throne


    pt "¡¿Qué hace una espada en la pared?!"

    pt "Un trono y..."

    pt "¿Esa silla tiene forma de escorpión?"

    show bg:
        easein 10.0 xpos 2.8 ypos .3 # vaginal thing

    pt "Esto parece bastante útil..."

    pt "Aunque para Hiromi sería quizás mejor usarlo analmente."

    show bg:
        easein 10.0 xpos 2.3 ypos .3 # Vibrators

    pt "Desde luego tiene bastantes juguetes en esa vitrina,"

    pt "todo tipo de cadenas y látigos para elegir."

    show bg:
        easein 10.0 xpos 1.7 ypos .2 # Ginecolo

    pt "Esto parece la silla de un ginecólogo..."

    pt "Una silla para inmovilizar con cierta abertura por la parte de abajo."

    show bg:
        easein 10.0 xpos 0.9 ypos .7 # manillas

    pt "Manillas de suspensión,"

    pt "parece que hay posibilidad de bajarlo o alzarlo mecánicamente."

    pt "Me imagino que también se la podría colgar de los pies..."

    show bg:
        easein 10.0 xpos 0.5 ypos .0 # little dungeon

    pt "Esto parece que sirve para poner cómodamente a alguien a cuatro patas sin posibilidad de moverse."

    pt "¿Lo de atrás es un calabozo en forma de caja?"

    show bg:
        easein 10.0 xpos 0.3 ypos .5 # mirrors

    pt "Parece que hay un televisor y todo."

    pt "No creo que sirva para mirar el fútbol."

    pt "Espejos no faltan..."

    pt "En el fondo parece que está el baño."

    show bg:
        easein 10.0 xpos -0.1 ypos .3 # bed

    pt "¿Hay una cama?"

    pt "Es lo último que me esperaba encontrar..."

    pt "Aunque viendo que hay cuatro postes con posibilidad de encajar cadenas,"

    pt "me imagino que tendrá su función poco romántica también..."

    show bg:
        easein 10.0 xpos -0.7 ypos .65 # swing

    pt "Esto parece un columpio,"

    pt "pero con connotaciones poco infantiles..."

    pt "Lo de abajo parece el taburete del placer,"

    pt "puede resultar útil..."

    pt "¿Cuántas manillas de suspensión hay en esta habitación?"

    show bg:
        easein 10.0 xpos -0.9 ypos .3 # Cross

    pt "Una cruz en forma de aspa,"

    pt "creo que eso lo llamó {a=https://es.wikipedia.org/wiki/Cruz_de_San_Andrés}Saint Andrew Cross{/a}."

    show bg:
        easein 8.0 zoom 0.7 xpos -1.15 ypos .4 # swing

    pt "Una pared acolchada."

    show bg:
        easein 5.0 zoom 1.0 xpos -2.4 ypos 0.0 # Vibrator

    pt "Esto debe de ser la máquina sexual."

    show bg:
        easein 5.0 zoom 1.0 xpos -2.5 ypos .35 # Final

    pt "Y volvemos a estar ante la puerta de entrada."

############################ ############################ ############################ ############################ ############################

    hide screen Points
    show screen PointsDungeon()
    with dissolve

    $ saturation_tint_level = "verydark"

    $pLockerC.hi_dom = (-15 + dundiff) #35
    $pLockerC.hi_ple = (-5 + dundiff) #45
    $pLockerC.hi_hap = (-15 + dundiff) #35
    $pLockerC.hi_love = (-30 + dundiff)
    $pLockerC.hi_dilass = (10 + dundiff) #60 Dilation of the asshole.
    $pLockerC.hi_dilthroat = (10 + dundiff) #60 # Dilatation of the throat.
    $pLockerC.hi_painass = (0 + dundiff) #50
    $pLockerC.hi_sti = 0 # Stimulation to have an orgasm.
    $pLockerC.hi_org = 0 # Counter. Not bar.

    $pLockerC.hi_time = 0.0 # Counter. Not bar.

    ##

    $pLockerC.mc_ple = (5 + dundiff) #45
    $pLockerC.mc_dilass = (0 + dundiff) #50 Dilation of the asshole.
    $pLockerC.mc_dilthroat = (0 + dundiff) #50 # Dilatation of the throat.
    $pLockerC.mc_painass = (0 + dundiff) #50
    $pLockerC.mc_sti = 5 # Stimulation to have an orgasm.
    $pLockerC.mc_org = 0 # Counter. Not bar.


    play sound "audio/sfx/door_old_short_open01.ogg"

    scene bg 05afternoon_dungeon_door_open_bg:
        truecenter
        zoom 0.5

    with dissolve

    ono "Meeec"

    if music_play != "frailty":
        play music "audio/music/alcaknight/frailty.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "frailty"

    show bg 05afternoon_dungeon_door_closed_bg

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_left_zoom_0_25_pos
    show hiromi_gen_body_c_crossed_dressed:
        hiromi_gen_body_left_zoom_0_25_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_left_zoom_0_25_pos

    show hiromi_gen_exp_blush 00:
        hiromi_gen_exp_left_zoom_0_25_pos
    show hiromi_gen_exp_mouth sad_Silentx04:
        hiromi_gen_exp_left_zoom_0_25_pos
    show hiromi_gen_exp_eyes 04:
        hiromi_gen_exp_left_zoom_0_25_pos
    show hiromi_gen_exp_piris left04:
        hiromi_gen_exp_left_zoom_0_25_pos
    show hiromi_gen_exp_eyebrows normal:
        hiromi_gen_exp_left_zoom_0_25_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_left_zoom_0_25_pos
    with dissolve

    hi "..."

    menu afternoon05_TxellWorkPlace_FuckHiromi_Beginning_question:
        
        pt "No he oído que llamase a la puerta."

        "Pensaba que por lo menos le harías caso a Txell y llamarías a la puerta.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",1)
            $pLockerC.ch_pts_C("hi_hap",-1)

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "Si fuera ella la que estuviera aquí dentro,"

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            hi "eso es lo que habría hecho."

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "Pero a ti no tengo por qué darte ninguna explicación."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows surprisex02
            with dissolve

            p "No creo que ella opine del mismo modo."

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows surprisex01
            with dissolve

            hi "Tienes razón,"

            show hiromi_gen_exp_mouth happy_Talkingx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "será mejor llamarla para que te sustituya."

            show hiromi_gen_exp_mouth happy_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            pt "Será cabrona..."

            pt "Tengo que redirigir esto cuanto antes."
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_Beginning_Ready

        "¿No te ha dicho Txell que llamaras a la puerta primero?":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",2)
            $pLockerC.ch_pts_C("hi_hap",-2)

            show hiromi_gen_exp_mouth sad_Talkingx001
            show hiromi_gen_exp_eyes 07
            show hiromi_gen_exp_piris front07
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            hi "Pff..."

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "Como si tu opinión me importara."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows surprisex02
            with dissolve

            p "No es mi opinión,"

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            p "es una orden bien simple,"

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows surprisex01
            with dissolve

            p "que ni siquiera has sido capaz de acatar."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows surprisex01
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sadbiting_Silentx04
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            p "Pensaba que por lo menos a ella la respetabas."

            show hiromi_gen_exp_mouth sadbiting_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows sadx01
            with dissolve

            hi "..."
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_Beginning_Ready

        "He visto perros más educados que tú.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",-1)
            $pLockerC.ch_pts_C("hi_hap",-2)

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "Si te crees que así me vas a convencer de algún modo,"

            show hiromi_gen_exp_mouth happy_Talkingx04
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx01
            with dissolve

            hi "lo llevas claro, cavernícola."

            show hiromi_gen_exp_mouth happy_Silentx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            pt "No creo que insultándola gratuitamente vaya a conseguir nada bueno..."
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_Beginning_Ready

label afternoon05_TxellWorkPlace_FuckHiromi_Beginning_Ready:

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows surprisex01
    with dissolve

    p "¿Estás preparada para empezar?"

    show hiromi_gen_exp_mouth sad_Talkingx002
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows surprisex001
    with dissolve

    hi "No."

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows suspiciousx01
    with dissolve

    pt "¿No?"

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    hi "No sé qué historias le habrás contado a Txell para convencerla de esta estupidez,"

    show hiromi_gen_exp_mouth sad_Talkingx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    hi "pero será mejor que salgas ahí fuera y vuelvas a hablar con ella."

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    hi "Esto es una payasada,"

    show hiromi_gen_exp_mouth sad_Talkingx10
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve
    
    hi "y no tengo el tiempo,"

    show hiromi_gen_exp_mouth sad_Talkingx12
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris left02
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    hi "ni la paciencia,"

    show hiromi_gen_exp_mouth sad_Talkingx11
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    hi "para este circo que te has montado en tu cabeza."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    p "..."

    menu afternoon05_TxellWorkPlace_FuckHiromi_Circus_question:
        
        pt "No está demasiado entusiasmada con la idea de que la domine..."

        "Tienes razón, esto está resultando una total pérdida de tiempo.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",-10)
            $pLockerC.ch_pts_C("hi_hap",-5)
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves

                #hi "Si te piensas que te voy a detener,"

                #hi "lo llevas claro figura."

                #p "No me estoy echando un farol."
        
        "<Explicarle que le estás haciendo un favor a Meritxell>":
            
            call p_Help

            $pLockerC.ch_pts_C("hi_dom",1)
            $pLockerC.ch_pts_C("hi_hap",-1)
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_Circus_TxellIdea

        "¿Te crees que no tengo otras cosas mejores que hacer?":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",-1)
            $pLockerC.ch_pts_C("hi_hap",-3)

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx02
            with dissolve

            hi "Que yo sepa, Txell no te ha puesto una pistola en la cabeza obligándote a ello."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            p "..."
                  
            jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_before

label afternoon05_TxellWorkPlace_FuckHiromi_Circus_TxellIdea:

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows surprisex03
    with dissolve

    p "Te equivocas, Hiromi."

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "Ha sido ella quien me ha convencido para ayudarte."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    p "Después de que te lo haya intentado explicar por activa y por pasiva,"

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    p "sigues sin entender que ella no puede,"

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "o no quiere ayudarte."

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    p "Así que, como última opción, me ha pedido este favor,"

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    p "pero si realmente no quieres mi ayuda,"

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    p "tampoco tengo el tiempo ni la paciencia para convencerte de lo contrario."

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows suspiciousx01
    with dissolve

    p "Al fin y al cabo le estoy haciendo un favor a ella,"

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "a ti ni siquiera te conozco."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    p "Por lo que, si crees que eres capaz de convencerla"

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "y quieres que salga,"

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    p "lo haré."

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris right02
    show hiromi_gen_exp_eyebrows suspiciousx01
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "Pero ten en cuenta que no voy a volver a entrar por esa puerta,"

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    p "aunque las dos me lo pidáis de rodillas."

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows suspiciousx02
    with dissolve

    hi "..."

label afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_before:

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "Eres consciente de que tengo polla,"

    show hiromi_gen_exp_mouth sad_Talkingx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "¿verdad?"

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    p "Sí."

    show hiromi_gen_exp_mouth sad_Talkingx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows surprisex001
    with dissolve

    hi "¿Te molan los rabos?"

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    menu afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_question:
        
        pt "..."

        "¿Y qué problema hay si no me disgustan?":

            call p_Help

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            hi "¿Eres gay?"

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            menu afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_Gay_question:

                pt "Nunca he estado con un tío, no sé si es buena idea mentirle..."

                "Sí.":

                    call p_Help

                    $pLockerC.ch_pts_C("hi_dom",-5)

                    show hiromi_gen_exp_mouth sad_Silentx05
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows suspiciousx02
                    with dissolve

                    hi "..."

                    show hiromi_gen_exp_mouth sad_Silentx06
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows suspiciousx03
                    with dissolve

                    p "¿Qué?"

                    show hiromi_gen_exp_mouth sad_Talkingx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    hi "No veo a Txell interesándose por un homosexual."

                    show hiromi_gen_exp_mouth sad_Silentx02
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows surprisex01
                    with dissolve

                    p "¿Cuándo has visto que se interese por un {a=https://es.wikipedia.org/wiki/Heterosexualidad}hetero{/a}?"

                    show hiromi_gen_exp_mouth happy_Silentx04
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    hi "Hmm..."

                    show hiromi_gen_exp_mouth happy_Talkingx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "Se nota que no la conoces demasiado bien."

                    show hiromi_gen_exp_mouth sad_Talkingx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    hi "Aunque tienes pinta de maromo descamisado en el día del orgullo gay,"

                    show hiromi_gen_exp_mouth happy_Talkingx06
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "salta a la vista que por lo menos tienes un alto interés en el cuerpo femenino."

                    show hiromi_gen_exp_mouth sad_Silentx03
                    show hiromi_gen_exp_eyes 01
                    show hiromi_gen_exp_piris front01
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "Eso es solo tu opinión."

                    show hiromi_gen_exp_mouth happy_Talkingx07
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "No."

                    show hiromi_gen_exp_mouth happy_Talkingx09
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx02
                    with dissolve

                    hi "Es un hecho."

                    show hiromi_gen_exp_mouth happy_Talkingx08
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows angryx03
                    with dissolve

                    hi "Si fueras {a=https://es.wikipedia.org/wiki/Gay}gay{/a},"

                    show hiromi_gen_exp_mouth happy_Talkingx10
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx03
                    with dissolve

                    hi "no habrías estado mirándole el pecho a cada rato que tenías ocasión."

                    show hiromi_gen_exp_mouth happy_Silentx06
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx03
                    with dissolve

                    pt "¡¿Cuándo me ha visto?!"

                    show hiromi_gen_exp_mouth sad_Silentx03
                    show hiromi_gen_exp_eyes 01
                    show hiromi_gen_exp_piris front01
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "Como para no verla."

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    p "Hasta un gay como yo,"

                    show hiromi_gen_exp_mouth happy_Silentx03
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows suspiciousx02
                    with dissolve

                    p "no puede evitar fijarse en esa delantera."

                    show hiromi_gen_exp_mouth happy_Talkingx03
                    show hiromi_gen_exp_eyes 07
                    show hiromi_gen_exp_piris front07
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    hi "No digo que no,"

                    show hiromi_gen_exp_mouth happy_Talkingx07
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows surprisex01
                    with dissolve

                    hi "Pero a un homosexual no se le estaría poniendo dura ahora mismo solo de recordarlo..."

                    show hiromi_gen_exp_mouth happy_Silentx06
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    p "..."

                    show hiromi_gen_exp_mouth happy_Silentx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris down04
                    show hiromi_gen_exp_eyebrows surprisex001
                    with dissolve

                    hi "..."

                    show hiromi_gen_exp_mouth happy_Silentx07
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    pt "¡PUTA POLLA!"

                    show hiromi_gen_exp_mouth sad_Talkingx05
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows surprisex001
                    with dissolve

                    hi "Si crees que mintiendo vas a lograr algo conmigo,"

                    show hiromi_gen_exp_mouth happy_Talkingx07
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    hi "lo llevas muy mal..."

                    show hiromi_gen_exp_mouth happy_Silentx07
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    p "..."

                    jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

                "No.":

                    call p_Help

                    $pLockerC.ch_pts_C("hi_dom",2)
                    $pLockerC.ch_pts_C("hi_ple",1)
                    $pLockerC.ch_pts_C("hi_hap",2)
                    $pLockerC.ch_pts_C("hi_love",1)

                    show hiromi_gen_exp_mouth sad_Talkingx07
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx03
                    with dissolve

                    hi "¿Entonces de qué diablos hablas?"

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "Una polla es un elemento visual bastante evidente del rubor y placer de alguien."

                    show hiromi_gen_exp_mouth sad_Silentx05
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    p "Además,"

                    show hiromi_gen_exp_mouth sad_Silentx03
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "si la poseedora de ese \"rabo\" tiene un aspecto femenino como el tuyo,"

                    show hiromi_gen_exp_blush 01
                    show hiromi_gen_exp_mouth sad_Silentx02
                    show hiromi_gen_exp_eyes 01
                    show hiromi_gen_exp_piris front01
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    p "¿por qué debería disgustarme?"

                    show hiromi_gen_exp_blush 02
                    show hiromi_gen_exp_mouth sadbiting_Silentx05
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris right03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "..."

                    jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

                "Es posible.":

                    call p_Help

                    $pLockerC.ch_pts_C("hi_dom",-3)

                    show hiromi_gen_exp_mouth happy_Talkingx07
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "Se te da fatal mentir, polluelo."

                    show hiromi_gen_exp_mouth happy_Silentx06
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    pt "¡¿Polluelo?!"

                    show hiromi_gen_exp_mouth happy_Talkingx04
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "O eres un hetero curioso que ni siquiera lo ha probado,"

                    show hiromi_gen_exp_mouth happy_Talkingx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    hi "o sencillamente me estás mintiendo en toda la cara."

                    show hiromi_gen_exp_mouth happy_Talkingx06
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx02
                    with dissolve

                    hi "No sé qué es peor."

                    show hiromi_gen_exp_mouth sad_Silentx03
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows serious
                    with dissolve

                    p "Quizás simplemente no me conoces lo suficiente."

                    show hiromi_gen_exp_mouth sad_Talkingx002
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows surprisex001
                    with dissolve

                    hi "Si realmente fueras gay,"

                    show hiromi_gen_exp_mouth happy_Talkingx05
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    hi "tus ojos no se habrían clavado tan detenidamente en los {b}voluptuosos pechos{/b} de Txell."

                    show hiromi_gen_exp_mouth happy_Silentx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    p "..."

                    show hiromi_gen_exp_mouth happy_Silentx06
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    pt "¡¿Tanto se me ha notado?!"

                    show hiromi_gen_exp_mouth happy_Talkingx04
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    hi "Tu homosexualidad brilla por su ausencia."

                    show hiromi_gen_exp_mouth sad_Silentx02
                    show hiromi_gen_exp_eyes 01
                    show hiromi_gen_exp_piris front01
                    show hiromi_gen_exp_eyebrows surprisex01
                    with dissolve

                    p "¿Y si me gustan ambos sexos?"

                    show hiromi_gen_exp_mouth sad_Talkingx05
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "Entonces no serías \"homo\","

                    show hiromi_gen_exp_mouth sad_Talkingx06
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows normal
                    with dissolve

                    hi "solo un idiota que no entiende el significado de las palabras."

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows surprisex01
                    with dissolve

                    p "..."

                    jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

#label afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_after:

    #p "Pídeme amablemente que no me vaya,"

    #p "y quizás me quede."

    #hi "Estás de coña."

        "No me está gustando tu actitud.":

            call p_Help

            show hiromi_gen_exp_mouth sad_Talkingx003
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows surprisex01
            with dissolve

            hi "No me digas..."

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows surprisex02
            with dissolve

            hi "¿No te gusta que sea una niña traviesa?"

            show hiromi_gen_exp_mouth happy_Silentx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            menu afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_naughtygirl_question:
                
                pt "¿Niña? ¿cuántos años cree que tiene?"

                "Creo que ya tienes una edad como para llamarte niña.":

                    call p_Help

                    $pLockerC.ch_pts_C("hi_dom",1)

                    show hiromi_gen_exp_mouth sad_Talkingx02
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows surprisex001
                    with dissolve

                    hi "Encima me estás llamando vieja."

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 03
                    show hiromi_gen_exp_piris front03
                    show hiromi_gen_exp_eyebrows suspiciousx02
                    with dissolve

                    p "No creo que te consideres una niña."

                    show hiromi_gen_exp_mouth sadbiting_Silentx06
                    show hiromi_gen_exp_eyes 01
                    show hiromi_gen_exp_piris front01
                    show hiromi_gen_exp_eyebrows surprisex03
                    with dissolve

                    p "Ni que te guste ese rollo de colegiala perturbada."

                    show hiromi_gen_exp_mouth sadbiting_Silentx07
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris right04
                    show hiromi_gen_exp_eyebrows suspiciousx03
                    with dissolve

                    hi "..."

                    jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

                "Con lo que tienes entre piernas, yo no te llamaría precisamente niña.":

                    call p_Help

                    #$pLockerC.ch_pts_C("hi_dom",-1) 
                    $pLockerC.ch_pts_C("hi_hap",-1)

                    show hiromi_gen_exp_mouth sad_Talkingx002
                    show hiromi_gen_exp_eyes 02
                    show hiromi_gen_exp_piris front02
                    show hiromi_gen_exp_eyebrows suspiciousx02
                    with dissolve

                    hi "¿Ah no?"

                    show hiromi_gen_exp_mouth sad_Talkingx05
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows angryx01
                    with dissolve

                    hi "¿Y qué me llamarías entonces?"

                    show hiromi_gen_exp_mouth sad_Silentx04
                    show hiromi_gen_exp_eyes 04
                    show hiromi_gen_exp_piris front04
                    show hiromi_gen_exp_eyebrows suspiciousx01
                    with dissolve

                    menu afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_naughtygirl_WhatYouCallMe_question:
                        
                        pt "¿Cómo llamaría a alguien como tú...?"

                        "Hombre transexual adulto.":

                            call p_Help

                            $pLockerC.ch_pts_C("hi_dom",-3) 
                            $pLockerC.ch_pts_C("hi_hap",-1)

                            show hiromi_gen_exp_mouth sad_Silentx08
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx03
                            with dissolve

                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx04
                            with dissolve

                            hi "No eres capaz de ver más allá..."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "¿Verdad?"

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            p "Tú lo has dicho antes,"

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            p "¿no?"

                            show hiromi_gen_exp_mouth sad_Silentx06
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            p "Tienes rabo,"

                            show hiromi_gen_exp_mouth sad_Silentx08
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx03
                            with dissolve

                            p "por lo tanto no eres una mujer."

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            hi "Dime una cosa..."

                            show hiromi_gen_exp_mouth sad_Talkingx03
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            hi "Si fuera a la cocina a coger unas tijeras,"

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex03
                            with dissolve

                            hi "y te la cortara de raíz."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "¿Serías hombre o mujer?"

                            show hiromi_gen_exp_mouth happy_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            p "..."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "Según tu teoría,"

                            show hiromi_gen_exp_mouth sad_Talkingx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            hi "los hombres tienen pene,"

                            show hiromi_gen_exp_mouth sad_Talkingx005
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            hi "y las mujeres vagina."

                            show hiromi_gen_exp_mouth happy_Talkingx03
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "Así que en ese caso,"

                            show hiromi_gen_exp_mouth happy_Talkingx04
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "¿serías un hombre sin pene?"

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "¿o una mujer sin genitales con apariencia de hombre?"

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows surprisex03
                            with dissolve

                            p "Lo que tengo claro"

                            show hiromi_gen_exp_mouth sad_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            p "es que tú eres una psicópata en potencia."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "Del mismo modo que {a=https://es.wikipedia.org/wiki/Gato_de_Schrödinger}Schrödinger{/a} fue un asesino de gatos en potencia para probar su paradoja..."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "¿Verdad?"

                            show hiromi_gen_exp_mouth happy_Silentx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            p "..."

                            show hiromi_gen_exp_mouth happy_Talkingx08
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "Al final pensaré que provienes de los {a=https://es.wikipedia.org/wiki/Homo_neanderthalensis}neandertales{/a} en realidad..."

                            show hiromi_gen_exp_mouth happy_Silentx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                        "Mariposón oscuro achinado.":

                            call p_Help

                            $pLockerC.ch_pts_C("hi_dom",-2) 
                            $pLockerC.ch_pts_C("hi_hap",-3)

                            show hiromi_gen_exp_mouth sad_Silentx02
                            show hiromi_gen_exp_eyes 01
                            show hiromi_gen_exp_piris front01
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve
                            
                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx002
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "Encima de homófobo,"

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            hi "racista de las pelotas."

                            show hiromi_gen_exp_mouth sad_Talkingx09
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            hi "¿Qué otras sorpresas tienes, cavernícola?"

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            p "Has empezado tú insultándome."

                            show hiromi_gen_exp_mouth happy_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "Y eres tan maduro,"

                            show hiromi_gen_exp_mouth happy_Talkingx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            hi "que has pensado que es mejor actuar del mismo modo,"

                            show hiromi_gen_exp_mouth happy_Talkingx08
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            hi "cayendo así en mi provocación."

                            show hiromi_gen_exp_mouth happy_Silentx08
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            p "..."

                            show hiromi_gen_exp_mouth sad_Talkingx03
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "He visto monos más listos que tú."

                            show hiromi_gen_exp_mouth happy_Silentx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            pt "Desde luego, Meritxell y ella son tal para cual..."

                        "Mujer adulta con sorpresa entre las piernas.":

                            call p_Help

                            $pLockerC.ch_pts_C("hi_dom",1) 
                            $pLockerC.ch_pts_C("hi_hap",2)

                            show hiromi_gen_exp_mouth sad_Silentx02
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx03
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            hi "Pensaba que ibas a decir otra cosa..."

                            show hiromi_gen_exp_mouth sad_Silentx01
                            show hiromi_gen_exp_eyes 01
                            show hiromi_gen_exp_piris front01
                            show hiromi_gen_exp_eyebrows surprisex02
                            with dissolve

                            p "¿Qué otra cosa te esperabas?"

                            show hiromi_gen_exp_mouth sadbiting_Silentx04
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris right03
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx03
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "Olvídalo."

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris right03
                            show hiromi_gen_exp_eyebrows sadx01
                            with dissolve

                        "Bollera negra con Piolín.":

                            call p_Help

                            $pLockerC.ch_pts_C("hi_dom",-3) 
                            $pLockerC.ch_pts_C("hi_hap",-2)

                            show hiromi_gen_exp_mouth sad_Silentx01
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            hi "¿Ese es el límite de tus neuronas?"

                            show hiromi_gen_exp_mouth sad_Talkingx003
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            hi "¿No llegas a nada mejor?"

                            show hiromi_gen_exp_mouth sad_Silentx03
                            show hiromi_gen_exp_eyes 01
                            show hiromi_gen_exp_piris front01
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            p "¿Preferías que te llamara {a=https://es.wikipedia.org/wiki/Homosexualidad}julandrón{/a}?"

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            hi "..."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "¿Debo sentirme elogiada,"

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "porque me has insultado despectivamente como mujer,"

                            show hiromi_gen_exp_mouth sad_Talkingx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            hi "en lugar de como hombre?"

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            pt "Yo no lo habría dicho mejor."

                            show hiromi_gen_exp_mouth sad_Talkingx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx03
                            with dissolve

                            hi "¿Qué mierda le has soltado a Txell para que creyera que eres mínimamente una opción...?"

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx04
                            with dissolve

                            hi "Esto no tiene ningún sentido."

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                        "Locaza sin coño.":

                            call p_Help

                            $pLockerC.ch_pts_C("hi_dom",-3) 
                            $pLockerC.ch_pts_C("hi_hap",-3)

                            show hiromi_gen_exp_mouth sad_Talkingx003
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "Locaza..."

                            show hiromi_gen_exp_mouth sad_Talkingx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            hi "¿Pretendes conseguir algo usando estos insultos de tan bajo nivel?"

                            show hiromi_gen_exp_mouth happy_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "¿O te crees que me vas a ofender porque me considere mujer,"

                            show hiromi_gen_exp_mouth happy_Talkingx04
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "a pesar de conservar mi miembro masculino?"

                            show hiromi_gen_exp_mouth sad_Silentx03
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            p "Mira,"

                            show hiromi_gen_exp_mouth sad_Silentx03
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            p "puedo llegar a entender que te quieras sentir mujer,"

                            show hiromi_gen_exp_mouth sad_Silentx02
                            show hiromi_gen_exp_eyes 01
                            show hiromi_gen_exp_piris front01
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            p "pero si te llegaste a operar los pechos,"

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            p "¿por qué no te erradicaste también la polla?"

                            show hiromi_gen_exp_mouth sad_Silentx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            p "Y no me vengas con que la operación es muy cara,"

                            show hiromi_gen_exp_mouth sad_Silentx08
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx03
                            with dissolve

                            p "puedo intuir claramente que vives en tanta o más opulencia que Meritxell,"

                            show hiromi_gen_exp_mouth sad_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            p "así que el dinero no es realmente el problema aquí..."

                            show hiromi_gen_exp_mouth happy_Talkingx03
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "Por lo menos hay cosas que no intuyes tan mal."

                            show hiromi_gen_exp_mouth sad_Silentx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            p "¿Entonces qué sentido tiene que te sientas mujer"

                            show hiromi_gen_exp_mouth sad_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            p "pero al mismo tiempo conserves aquello que nos hace hombres?"

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            p "No es demasiado lógico."

                            show hiromi_gen_exp_mouth sad_Talkingx004
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            hi "Aquello que nos hace hombres..."

                            show hiromi_gen_exp_mouth sad_Talkingx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "En primer lugar, niño,"

                            show hiromi_gen_exp_mouth sad_Talkingx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "no estoy aquí para darte clases de sociología."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            hi "Pero confundir la biología,"

                            show hiromi_gen_exp_mouth happy_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx03
                            with dissolve

                            hi "con el {a=https://es.wikipedia.org/wiki/Statu_quo}{i}statu quo{/i}{/a} de la sociedad actual,"

                            show hiromi_gen_exp_mouth happy_Talkingx07
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows surprisex001
                            with dissolve

                            hi "es de un nivel preocupante."

                            show hiromi_gen_exp_mouth sad_Silentx03
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows surprisex02
                            with dissolve

                            p "¿De qué estás hablando?"

                            show hiromi_gen_exp_mouth sad_Talkingx05
                            show hiromi_gen_exp_eyes 07
                            show hiromi_gen_exp_piris front07
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "Es probable que sea difícil de entender para un hombre de las cavernas como tú,"

                            show hiromi_gen_exp_mouth sad_Talkingx10
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows angryx02
                            with dissolve

                            hi "pero estamos en el siglo XXI."

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            p "..."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "¿Qué te hace ser un hombre?"

                            show hiromi_gen_exp_mouth sad_Talkingx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "¿El que te gusten las mujeres y no los hombres?"

                            show hiromi_gen_exp_mouth sad_Talkingx07
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows suspiciousx01
                            with dissolve

                            hi "¿Tu cuerpo robusto, musculoso y masculino?"

                            show hiromi_gen_exp_mouth sad_Talkingx004
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "¿Tu voz ruda y varonil?"

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris down02
                            show hiromi_gen_exp_eyebrows sadx01
                            with dissolve

                            hi "¿Tu miembro viril...?"

                            show hiromi_gen_exp_mouth sad_Silentx03
                            show hiromi_gen_exp_eyes 01
                            show hiromi_gen_exp_piris front01
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            p "¡¿Y qué entiendes tú por ser una mujer?!"

                            show hiromi_gen_h_hair_back:
                                hiromi_gen_body_left_zoom_0_4_pos
                            show hiromi_gen_body_c_crossed_dressed:
                                hiromi_gen_body_left_zoom_0_4_pos
                            show hiromi_gen_h_head earrings:
                                hiromi_gen_body_left_zoom_0_4_pos

                            show hiromi_gen_exp_blush 01:
                                hiromi_gen_exp_left_zoom_0_4_pos
                            show hiromi_gen_exp_mouth happy_Silentx06:
                                hiromi_gen_exp_left_zoom_0_4_pos
                            show hiromi_gen_exp_eyes 04:
                                hiromi_gen_exp_left_zoom_0_4_pos
                            show hiromi_gen_exp_piris front04:
                                hiromi_gen_exp_left_zoom_0_4_pos
                            show hiromi_gen_exp_eyebrows suspiciousx01:
                                hiromi_gen_exp_left_zoom_0_4_pos

                            show hiromi_gen_h_hair_front:
                                hiromi_gen_body_left_zoom_0_4_pos
                            with Dissolve(1.0)

                            n "Con cierta gracilidad se acerca sugerentemente a escasos centímetros de ti."

                            show hiromi_gen_exp_mouth happy_Talkingx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "Hombre,"

                            extend " mujer..."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "No son más que etiquetas para poder clasificar mejor nuestra sociedad distópica."

                            show hiromi_gen_h_hair_back:
                                hiromi_gen_body_left_zoom_0_75_pos
                            show hiromi_gen_body_c_crossed_dressed:
                                hiromi_gen_body_left_zoom_0_75_pos
                            show hiromi_gen_h_head earrings:
                                hiromi_gen_body_left_zoom_0_75_pos

                            show hiromi_gen_exp_blush 01:
                                hiromi_gen_exp_left_zoom_0_75_pos
                            show hiromi_gen_exp_mouth happy_Silentx08:
                                hiromi_gen_exp_left_zoom_0_75_pos
                            show hiromi_gen_exp_eyes 04:
                                hiromi_gen_exp_left_zoom_0_75_pos
                            show hiromi_gen_exp_piris front04:
                                hiromi_gen_exp_left_zoom_0_75_pos
                            show hiromi_gen_exp_eyebrows suspiciousx02:
                                hiromi_gen_exp_left_zoom_0_75_pos

                            show hiromi_gen_h_hair_front:
                                hiromi_gen_body_left_zoom_0_75_pos
                            with Dissolve(1.0)

                            n "Livianamente acerca su mano sobre tu pecho sin hacer contacto sobre tu piel,"

                            show hiromi_gen_exp_mouth happybiting_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris down04
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            n "como si te acariciara con delicadeza con la yema de sus delgados dedos."

                            show hiromi_gen_exp_mouth happybiting_Silentx09
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            p "..."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "En realidad nunca me he considerado plenamente como un hombre o una mujer,"

                            show hiromi_gen_exp_mouth sad_Talkingx03
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows sadx01
                            with dissolve

                            hi "pero, ya que nuestra sociedad nos exige elegir una etiqueta para relacionarnos,"

                            show hiromi_gen_exp_mouth happybiting_Silentx05
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows sadx02
                            with dissolve

                            n "Su voz se va edulcorando y volviéndose más tierna."

                            show hiromi_gen_exp_mouth happy_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows sadx03
                            with dissolve

                            hi "en mi opinión creo que me encaja mejor el rol femenino."

                            show hiromi_gen_exp_mouth sad_Talkingx02
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows sadx02
                            with dissolve

                            hi "¿Tú qué opinas?"

                            show hiromi_gen_exp_mouth happybiting_Silentx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            p "Yo..."

                            show hiromi_gen_exp_mouth happy_Talkingx03
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx01
                            with dissolve

                            hi "Tranquilo cavernícola,"

                            show hiromi_gen_exp_mouth happy_Talkingx04
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            hi "no hace falta que respondas,"

                            show hiromi_gen_h_hair_back:
                                hiromi_gen_body_left_zoom_0_25_pos
                            show hiromi_gen_body_c_crossed_dressed:
                                hiromi_gen_body_left_zoom_0_25_pos
                            show hiromi_gen_h_head earrings:
                                hiromi_gen_body_left_zoom_0_25_pos

                            show hiromi_gen_exp_blush 01:
                                hiromi_gen_exp_left_zoom_0_25_pos
                            show hiromi_gen_exp_mouth happy_Silentx05:
                                hiromi_gen_exp_left_zoom_0_25_pos
                            show hiromi_gen_exp_eyes 04:
                                hiromi_gen_exp_left_zoom_0_25_pos
                            show hiromi_gen_exp_piris front04:
                                hiromi_gen_exp_left_zoom_0_25_pos
                            show hiromi_gen_exp_eyebrows normal:
                                hiromi_gen_exp_left_zoom_0_25_pos

                            show hiromi_gen_h_hair_front:
                                hiromi_gen_body_left_zoom_0_25_pos
                            with Dissolve(1.0)

                            n "Con sutileza se aparta de ti."

                            show hiromi_gen_exp_mouth happy_Talkingx06
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            hi "tu polla ya lo hace por ti."

                            show hiromi_gen_exp_mouth happy_Talkingx05
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris down02
                            show hiromi_gen_exp_eyebrows sadx01
                            with dissolve

                            hi "A menos que creas que alguien etiquetado como hombre masculino"

                            show hiromi_gen_exp_mouth happy_Talkingx07
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows sadx02
                            with dissolve

                            hi "pueda ponértela dura tan fácilmente..."

                            show hiromi_gen_exp_mouth happy_Silentx05
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            pt "¡¿EN SERIO?!"

                            show hiromi_gen_exp_mouth happy_Silentx06
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows normal
                            with dissolve

                            pt "¡PERO SI NI SIQUIERA ME HA TOCADO!"

                            show hiromi_gen_exp_mouth happy_Silentx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            pt "¿¡QUÉ MIERDA DE AGUANTE TENGO!?"

                            show hiromi_gen_exp_mouth happy_Silentx06
                            show hiromi_gen_exp_eyes 02
                            show hiromi_gen_exp_piris front02
                            show hiromi_gen_exp_eyebrows surprisex01
                            with dissolve

                            p "No soy dueño de mis impulsos."

                            show hiromi_gen_exp_mouth sad_Talkingx04
                            show hiromi_gen_exp_eyes 03
                            show hiromi_gen_exp_piris front03
                            show hiromi_gen_exp_eyebrows serious
                            with dissolve

                            hi "Tampoco eres culpable de haber nacido así."

                            show hiromi_gen_exp_mouth sad_Talkingx07
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows angryx04
                            with dissolve

                            hi "Sin embargo, sí eres dueño de tus pensamientos y tus palabras."

                            show hiromi_gen_exp_mouth sad_Silentx04
                            show hiromi_gen_exp_eyes 04
                            show hiromi_gen_exp_piris front04
                            show hiromi_gen_exp_eyebrows suspiciousx02
                            with dissolve

                            p "..."

                    jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

                        #p "Pero si tanto te incomoda toda esta situación,"

                        #p "te recuerdo que la puerta por la que has entrado sigue abierta."

        "El favor se lo estoy haciendo a ella, no a ti.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",2)
            $pLockerC.ch_pts_C("hi_hap",-1)

            jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell

        "Al final te vas a arrepentir de lo que me estás diciendo.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",-2)
            $pLockerC.ch_pts_C("hi_hap",-2)

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows sadx01
            with dissolve

            hi "¿Que me voy a qué...?"

            show hiromi_gen_exp_mouth happy_Silentx07
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows sadx02
            with dissolve

            p "Ya me has oído."

            show hiromi_gen_exp_mouth happy_Talkingx07
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows sadx02
            with dissolve

            hi "¿Pero tú te escuchas?"

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows suspiciousx02
            with dissolve

            hi "Ni que fuera una colegiala a la que hay que castigar..."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex02
            with dissolve

            p "..."

            show hiromi_gen_exp_mouth sad_Talkingx004
            show hiromi_gen_exp_eyes 07
            show hiromi_gen_exp_piris front07
            show hiromi_gen_exp_eyebrows suspiciousx02
            with dissolve

            hi "Lo siento,"

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            hi "pero ese rollo ya hace tiempo que no me va..."

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            hi "Además,"

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            hi "tampoco me van las amenazas infantiles."

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            p "Te la estás jugando..."

            show hiromi_gen_exp_mouth sad_Talkingx005
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            hi "No lo pillas..."

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows suspiciousx02
            with dissolve

            hi "¿Verdad?"

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_after

label afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_DoingFavorToTxell:

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    p "Si tanto te incomoda toda esta situación,"

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "te recuerdo que la puerta por la que has entrado sigue abierta."

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris left03
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows suspiciousx03
    with dissolve

    p "..."

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    hi "¿Qué?"

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    p "Estoy esperando tu respuesta."

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    hi "Sigo aquí."

    show hiromi_gen_exp_mouth sad_Talkingx003
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "¿No?"

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris left03
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    menu afternoon05_TxellWorkPlace_FuckHiromi_ImStillHere_Question:

        pt "..."

        "De acuerdo.":

            call p_Help

            jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_after

        "Eso no es una respuesta.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",2)
            $pLockerC.ch_pts_C("hi_hap",-2)

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            hi "¿Y qué demonios quieres que diga?"

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows surprisex02
            with dissolve

            p "Un agradecimiento no estaría de más."

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "No pienso agradecerte algo que aún ni has empezado."

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris front01
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            p "Sigo aquí,"

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            p "¿no?"

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "..."

            jump afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_after

label afternoon05_TxellWorkPlace_FuckHiromi_LovingCocks_after:

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows surprisex01
    with dissolve

    p "Pídeme amablemente que no me vaya,"

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows surprisex001
    with dissolve

    p "y quizás me quede."

    show hiromi_gen_exp_blush 01
    show hiromi_gen_exp_mouth happy_Talkingx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows suspiciousx03
    with dissolve

    hi "Estás de coña."

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_right_zoom_0_5_pos
    show hiromi_gen_body_c_crossed_dressed:
        hiromi_gen_body_right_zoom_0_5_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_right_zoom_0_5_pos

    show hiromi_gen_exp_blush 01:
        hiromi_gen_exp_right_zoom_0_5_pos
    show hiromi_gen_exp_mouth sad_Silentx03:
        hiromi_gen_exp_right_zoom_0_5_pos
    show hiromi_gen_exp_eyes 01:
        hiromi_gen_exp_right_zoom_0_5_pos
    show hiromi_gen_exp_piris front01:
        hiromi_gen_exp_right_zoom_0_5_pos
    show hiromi_gen_exp_eyebrows surprisex03:
        hiromi_gen_exp_right_zoom_0_5_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_right_zoom_0_5_pos
    with dissolve

    n "Con cierto desdén pasas por su lado para alejarte de ella."

    scene bg 05afternoon_dungeon_door_closed_bg:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        easein_quad 5.0 zoom 1.0 xpos 0.8 ypos 1.0
    with Dissolve (1.0)

    show bg 05afternoon_dungeon_door_open_bg
    with Dissolve (1.0)

    play sound "audio/sfx/door_old_short_open01.ogg"

    ono "Meec"

    if pLockerC.hi_dom > (-11 + dundiff): # real number=38

        if Tendolarsversion:
            $ renpy.notify("[p_pos] -11[hir_dom]")

        hi "¡Espera!"

        n "Te detienes pausadamente al cruzar el umbral de la puerta."

        hi "Por favor..."

        #scene bg 05afternoon_dungeon_bg:
            #truecenter
            #zoom 0.75 xpos 1.5 ypos 0.5

        scene bg 05afternoon_dungeon_wall_01:
            truecenter
            zoom 0.5

        show hiromi_gen_h_hair_back:
            hiromi_gen_body_right_zoom_0_2_pos
        show hiromi_gen_body_c_crossed_dressed:
            hiromi_gen_body_right_zoom_0_2_pos
        show hiromi_gen_h_head earrings:
            hiromi_gen_body_right_zoom_0_2_pos

        show hiromi_gen_exp_blush 01:
            hiromi_gen_exp_right_zoom_0_2_pos
        show hiromi_gen_exp_mouth sad_Silentx06:
            hiromi_gen_exp_right_zoom_0_2_pos
        show hiromi_gen_exp_eyes 02:
            hiromi_gen_exp_right_zoom_0_2_pos
        show hiromi_gen_exp_piris front02:
            hiromi_gen_exp_right_zoom_0_2_pos
        show hiromi_gen_exp_eyebrows serious:
            hiromi_gen_exp_right_zoom_0_2_pos

        show hiromi_gen_h_hair_front:
            hiromi_gen_body_right_zoom_0_2_pos
        with dissolve

        p "Por favor,"

        extend " ¿qué?"

        jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername

    else: # Hiromi is leaving.

        if Tendolarsversion:
            $ renpy.notify("[p_neg] -11[hir_dom]")

        $ FuckH_ThreatFailed = True

        jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves

label afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves:

    if FuckH_ThreatFailed == False:
        show hiromi_gen_exp_mouth happy_Talkingx05
        show hiromi_gen_exp_eyes 02
        show hiromi_gen_exp_piris front02
        show hiromi_gen_exp_eyebrows angryx01
        with dissolve

    hi "Si te piensas que te voy a detener,"

    if FuckH_ThreatFailed == False:
        show hiromi_gen_exp_mouth happy_Talkingx07
        show hiromi_gen_exp_eyes 03
        show hiromi_gen_exp_piris front03
        show hiromi_gen_exp_eyebrows angryx02
        with dissolve

    hi "lo llevas claro figura."

    if FuckH_ThreatFailed == False:
        show hiromi_gen_exp_mouth sad_Silentx01
        show hiromi_gen_exp_eyes 01
        show hiromi_gen_exp_piris front01
        show hiromi_gen_exp_eyebrows normal
        with dissolve

    p "No me estoy echando un farol."

    if FuckH_ThreatFailed == False:
        show hiromi_gen_exp_mouth happy_Talkingx06
        show hiromi_gen_exp_eyes 03
        show hiromi_gen_exp_piris front03
        show hiromi_gen_exp_eyebrows angryx03
        with dissolve

    hi "Ni yo tampoco, cenutrio."

    if FuckH_ThreatFailed == False:
        scene bg 05afternoon_dungeon_door_open_bg:
            truecenter
            zoom 0.5
        with dissolve
    else:
        show hiromi_gen_h_hair_back:
            hiromi_gen_body_right_zoom_0_5_pos
        show hiromi_gen_body_c_crossed_dressed:
            hiromi_gen_body_right_zoom_0_5_pos
        show hiromi_gen_h_head earrings:
            hiromi_gen_body_right_zoom_0_5_pos

        show hiromi_gen_exp_blush 00:
            hiromi_gen_exp_right_zoom_0_5_pos
        show hiromi_gen_exp_mouth happy_Silentx05:
            hiromi_gen_exp_right_zoom_0_5_pos
        show hiromi_gen_exp_eyes 04:
            hiromi_gen_exp_right_zoom_0_5_pos
        show hiromi_gen_exp_piris front04:
            hiromi_gen_exp_right_zoom_0_5_pos
        show hiromi_gen_exp_eyebrows angryx03:
            hiromi_gen_exp_right_zoom_0_5_pos

        show hiromi_gen_h_hair_front:
            hiromi_gen_body_right_zoom_0_5_pos
        with dissolve


    n "Sin apenas darte tiempo a reaccionar,"

    if FuckH_ThreatFailed == False:
        show bg 05afternoon_dungeon_door_closed_bg
        with hpunch
    else:
        scene bg 05afternoon_dungeon_door_open_bg:
            truecenter
            zoom 1.0 xpos 0.8 ypos 1.0
        with dissolve

    n "con su grácil andar te pasa por delante alejándose del calabozo en dirección a la recepción."

    p "..."

    pt "Quizás no he sabido medir demasiado bien las palabras y ahora ya es demasiado tarde."

    jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02

label afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02:

    $ saturation_tint_level = "default"

    if PlatinumHelp == True:
        hide screen PointsDungeon
        show screen Points()
        
    scene black
    with fade

    scene bg 05afternoon_entrance_reception_bg:
        truecenter
        zoom 0.3335  xpos 0.5 ypos 0.5

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_left_zoom_0_2_pos
    show hiromi_gen_body_c_crossed_dressed:
        hiromi_gen_body_left_zoom_0_2_pos
    show hiromi_gen_h_head earrings:
        hiromi_gen_body_left_zoom_0_2_pos

    show hiromi_gen_exp_blush 01:
        hiromi_gen_exp_left_zoom_0_2_pos
    show hiromi_gen_exp_mouth sad_Silentx07:
        hiromi_gen_exp_left_zoom_0_2_pos
    show hiromi_gen_exp_eyes 04:
        hiromi_gen_exp_left_zoom_0_2_pos
    show hiromi_gen_exp_piris right04:
        hiromi_gen_exp_left_zoom_0_2_pos
    show hiromi_gen_exp_eyebrows surprisex001:
        hiromi_gen_exp_left_zoom_0_2_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_left_zoom_0_2_pos

    show m_bodynew hips_04:
        mtxell_body_ontheright_zoom_0_2_pos

    show m_exp_blush 01:
        mtxell_exp_ontheright_zoom_0_2_pos
    show m_exp_mouth sad_Silentx07:
        mtxell_exp_ontheright_zoom_0_2_pos
    show m_exp_eyes 02:
        mtxell_exp_ontheright_zoom_0_2_pos
    show m_exp_piris left02:
        mtxell_exp_ontheright_zoom_0_2_pos
    show m_exp_eyebrows angryx03:
        mtxell_exp_ontheright_zoom_0_2_pos

    show m_exp_hair_front:
        mtxell_exp_ontheright_zoom_0_2_pos
    with dissolve

    n "Sin demasiada demora sigues sus pasos hasta llegar a la enorme estancia."


    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx03

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx05
    with dissolve

    tx "Ya te he dicho que en persona no pienso tratarte, Hiromi."

    show hiromi_gen_exp_mouth sadbiting_Silentx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx04

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows angryx05
    with dissolve

    tx "Es él o nada."

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx05

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows surprisex01
    with dissolve

    hi "Te prometo que lo he intentado."

    show hiromi_gen_exp_mouth sad_Talkingx004
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex03
    with dissolve
    
    hi "Pero este tipo es más corto que una camisa sin mangas."

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows suspiciousx02

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx03
    with dissolve

    tx "..."

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows sadx01

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05 
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows surprisex001

    show m_bodynew hips_04:
        mtxell_body_ontheright_zoom_0_4_pos

    show m_exp_blush 01:
        mtxell_exp_ontheright_zoom_0_4_pos
    show m_exp_mouth sad_Silentx06:
        mtxell_exp_ontheright_zoom_0_4_pos
    show m_exp_eyes 03:
        mtxell_exp_ontheright_zoom_0_4_pos
    show m_exp_piris front03:
        mtxell_exp_ontheright_zoom_0_4_pos
    show m_exp_eyebrows sadx01:
        mtxell_exp_ontheright_zoom_0_4_pos

    show m_exp_hair_front:
        mtxell_exp_ontheright_zoom_0_4_pos
    with dissolve

    n "Meritxell se acerca a ti hablándote con un tono de voz menos acalorado."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "¿Qué ha ocurrido ahí dentro?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows sadx01
    with dissolve

    p "¿No me has dicho que nos estarías espiando?"

    
    if FuckH_Start_Cond == False:

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx03
        with dissolve

        tx "Si apenas me ha dado tiempo de hacerme un café..."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows sadx04
        with dissolve

        p "..."

    else:

        show m_exp_mouth sad_Talkingx03
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows sadx01
        with dissolve

        tx "He visto y he oído lo que ha ocurrido,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows sadx02
        with dissolve

        tx "pero no sé qué ha pasado por tu cabeza."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows sadx01
    with dissolve

    p "Lo siento,"

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx06
    with dissolve

    p "pero tu amiga no parece que sea de trato fácil."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx07
    with dissolve

    tx "Nunca he dicho que fuera fácil,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx05
    with dissolve

    tx "por eso he intentado ser tan clara y sincera dándote mi confianza para este caso."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx04
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Lo siento,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx06
    with dissolve

    tx "quizás me he excedido al pedírtelo sin conocerte lo suficiente."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Supongo que no estás hecho de la pasta que pensaba."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx06
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx05
    with dissolve

    tx "Por favor,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    tx "espérame en la biblioteca al fondo del pasillo."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx01
    with dissolve

    tx "Antes me gustaría poder despedirme de Hiromi como es debido."

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "¿Qué quieres contarme en la biblioteca?"

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    tx "Hay un libro sobre el que te quiero hablar."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    pt "¿Un libro?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx01
    with dissolve

    pt "Tiene pinta de que me va a echar un sermón de mil narices..."

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx03
    with dissolve

    n "Tus ojos se fijan por un breve instante en los de Hiromi."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 08
    show m_exp_piris empty
    show m_exp_eyebrows sadx05
    with dissolve

    pt "No creo que me tenga en muy alta estima..."

    scene bg 05afternoon_library_door_far_bg:
        subpixel True
        truecenter
        zoom 0.5
        pause 0.5
        ease_quad 10.0 zoom 1.0
    with fade

    n "Decides dejarlas solas e ir donde te ha indicado Txell."

    show bg 05afternoon_library_door_close_open_bg:
        subpixel True
        ease 5.0 zoom 1.0
    with dissolve

    pause 2.0

    jump afternoon05_Library

label afternoon05_TxellWorkPlace_FuckHiromi_protmastername:

    show hiromi_gen_exp_mouth sad_Talkingx002
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    hi "No sé tu nombre."

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows surprisex001
    with dissolve

    menu afternoon05_TxellWorkPlace_FuckHiromi_protmastername_question:
        
        pt "¿Mi nombre?"
        
        "[protname]":

            call p_Help

            $ protmaster = protname.strip()

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 07
            show hiromi_gen_exp_piris front07
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris left04
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            hi "Por favor,"

            extend " [protname]."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            pm "Eso está mucho mejor."

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            pm "Ahora;"

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris front01
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            pm "desnúdate."

            jump afternoon05_TxellWorkPlace_FuckHiromi_whystillout_GetNaked

            #label afternoon05_TxellWorkPlace_FuckHiromi_whystillout_GetNaked:

                #$pLockerC.ch_pts_C("hi_dom",1)
                #$pLockerC.ch_pts_C("hi_hap",-1)

                #pm "Desnúdate."

                #hi "..."

                #pm "Ya has tratado con muchas sumisas,"

                #pm "sabes como funciona."

        "Maestro":

            call p_Help

            $ protmaster = "Maestro"

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            hi "¡¿Te crees que voy a ser tu alumna?!"

            show hiromi_gen_exp_mouth sad_Talkingx08
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "¡Ni que tuviera diez años!"

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

        "Mi Señor":

            call p_Help

            $ protmaster = "Mi Señor"

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx02
            with dissolve

            hi "¿Te crees que estamos en la {a=https://es.wikipedia.org/wiki/Edad_Media}Edad Media{/a} o algo?"

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "Estás soñando si crees que voy a tratarte de ese modo."

            show hiromi_gen_exp_mouth sad_Silentx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

        "Domador de culos":

            call p_Help

            $ protmaster = "Domador de culos"

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx003
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            hi "¿De culos...?"

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "¡¿A ti qué coño te pasa por la cabeza?!"

            show hiromi_gen_exp_mouth sad_Talkingx08
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "¡¡Estás como un cencerro si crees que te voy a llamar de esa manera!!"

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 034
            show hiromi_gen_exp_piris front034
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

        "Benito Camela":

            call p_Help

            $ protmaster = "Benito Camela"

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx03
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            hi "{size=15}Ven y tócamela...{/size}"

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            hi "¿Qué tienes?"

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "¿Diez años?"

            show hiromi_gen_exp_mouth sad_Talkingx09
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "No pienso llamarte de esa manera."

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

        "Vegeta":

            call p_Help

            $ protmaster = "Vegeta"

            show hiromi_gen_exp_mouth sad_Silentx03
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx003
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            hi "Estás de coña..."

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            hi "¿Verdad?"

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris front01
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            p "No."

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "¡¿Cuántos años tienes?!"

            show hiromi_gen_exp_mouth sad_Talkingx09
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "¡No pienso llamarte como al {a=https://es.wikipedia.org/wiki/Vegeta}Príncipe de los Saiyajins{/a}!"

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            p "Oh..."

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            p "parece que conoces {a=https://es.wikipedia.org/wiki/Dragon_Ball}Dragon Ball{/a}."

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "¡¿Y quién no lo conoce?!"

            show hiromi_gen_exp_mouth happy_Talkingx03
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "Además,"

            show hiromi_gen_exp_mouth sad_Talkingx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows normal
            with dissolve

            hi "aunque tenga más entradas que una autopista,"

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            hi "por lo menos él tiene pelo."

            show hiromi_gen_exp_mouth happy_Silentx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx02
            with dissolve

            pt "Será cabrona..."

            show hiromi_gen_exp_mouth sad_Talkingx05
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows suspiciousx03
            with dissolve

            hi "De ninguna manera te voy a llamar de ese modo."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

        "<Personalizado>":

            call p_Help

            $ protmaster = renpy.input(_("¿Cómo debería llamarme?"))
            $ protmaster = protmaster.strip()
            if not protmaster:
                $ protmaster = (_("Maestro"))

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris front01
            show hiromi_gen_exp_eyebrows surprisex03
            with dissolve

            p "Llámame [protmaster]."

            show hiromi_gen_exp_mouth sad_Talkingx06
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "¡No pienso llamarte así!"

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after

label afternoon05_TxellWorkPlace_FuckHiromi_protmastername_after:

    show bg02 05afternoon_dungeon_door_closed_bg:
        subpixel True
        truecenter
        zoom 0.5
        easein_quad 5.0 zoom 1.0 xpos 0.8 ypos 1.0
    with fade

    pause 0.5

    play sound "audio/sfx/door_old_short_open01.ogg"

    show bg02 05afternoon_dungeon_door_open_bg
    with dissolve

    n "Vuelves a darle la espalda."

    hi "{size=50}¡¡ESTÁ BIEN!!{/size}"

    $pLockerC.ch_pts_C("hi_dom",3)
    $pLockerC.ch_pts_C("hi_hap",-1)

    hide bg02
    show hiromi_gen_exp_mouth sad_Talkingx002
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "{size=15}[protmaster]{/size}..."

    show hiromi_gen_exp_mouth sad_Talkingx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows sadx01
    with dissolve

    hi "¿Podrías quedarte y ayudarme?"

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    menu afternoon05_TxellWorkPlace_FuckHiromi_protmastername_louder_question:
        
        pt "¿Mi nombre?"
        
        "Como no hables un poco más alto, me temo que no voy a poder escucharte.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",2)
            $pLockerC.ch_pts_C("hi_hap",-2)

            #call WIP ## NOT FINISHED

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_louder_01

        "<Será mejor no tentar demasiado la suerte>":

            call p_Help

            # No points needed.

            jump afternoon05_TxellWorkPlace_FuckHiromi_protmastername_louder_02


label afternoon05_TxellWorkPlace_FuckHiromi_protmastername_louder_01:

    show hiromi_gen_exp_mouth sadbiting_Silentx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sadbiting_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx15
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "{size=32}¡[protmaster]!{/size}"

    show hiromi_gen_exp_mouth sad_Talkingx13
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "{size=32}¡¿Podrías quedarte y ayudarme?!{/size}"

    show hiromi_gen_exp_mouth sadbiting_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    pm "¿No te falta algo?"

    show hiromi_gen_exp_mouth sadbiting_Silentx06
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx03
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "Por favor..."

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "¿Qué...?"

    show hiromi_gen_exp_mouth sad_Silentx17
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    pm "No te oigo..."

    show hiromi_gen_exp_mouth sad_Talkingx14
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "{size=32}¡POR FAVOR!{/size}"

    show hiromi_gen_exp_mouth sad_Silentx13
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    pm "..."

label afternoon05_TxellWorkPlace_FuckHiromi_protmastername_louder_02:

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "¡He hecho lo que me has pedido!"

    show hiromi_gen_exp_mouth sad_Talkingx007
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "¡¿No?!"

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    pm "Sí."

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "¡¿Entonces por qué sigues ahí fuera?!"

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    menu afternoon05_TxellWorkPlace_FuckHiromi_whystillout_question:
        
        pt "¿Que por qué sigo aquí fuera?"

        "Será mejor que olvidemos esto.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",-10)

            show hiromi_gen_exp_mouth sad_Talkingx09
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx07
            with dissolve

            hi "Si te piensas que te voy a detener,"

            show hiromi_gen_exp_mouth happy_Talkingx05
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx06
            with dissolve

            hi "lo llevas claro, figura."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows surprisex001
            with dissolve

            p "No pienso detenerte."

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows serious
            with dissolve

            p "He aceptado la oferta de Meritxell por simple curiosidad."

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 01
            show hiromi_gen_exp_piris front01
            show hiromi_gen_exp_eyebrows surprisex01
            with dissolve

            p "Pero después de conocerte algo mejor,"

            show hiromi_gen_exp_mouth sad_Silentx09
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            p "prefiero simplemente no perder mi tiempo."

            show hiromi_gen_exp_mouth sad_Silentx11
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            hi "..."

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx06
            with dissolve

            hi "¿Conocerme algo mejor?"

            show hiromi_gen_exp_mouth sad_Talkingx08
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx07
            with dissolve

            hi "No tienes ni la más remota idea de cómo soy."

            show hiromi_gen_exp_mouth sad_Silentx06
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows suspiciousx01
            with dissolve

            p "¿Y te crees que así me va a interesar conocerte?"

            show hiromi_gen_exp_mouth sad_Talkingx007
            show hiromi_gen_exp_eyes 02
            show hiromi_gen_exp_piris front02
            show hiromi_gen_exp_eyebrows angryx07
            with dissolve

            hi "Como si me importara tu opinión..."

            
            show hiromi_gen_h_hair_back:
                hiromi_gen_body_left_zoom_0_5_pos
            show hiromi_gen_body_c_crossed_dressed:
                hiromi_gen_body_left_zoom_0_5_pos
            show hiromi_gen_h_head earrings:
                hiromi_gen_body_left_zoom_0_5_pos

            show hiromi_gen_exp_blush 01:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_mouth sad_Silentx10:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_eyes 04:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_piris front04:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_eyebrows angryx06:
                hiromi_gen_exp_left_zoom_0_5_pos

            show hiromi_gen_h_hair_front:
                hiromi_gen_body_left_zoom_0_5_pos
            with dissolve

            n "Con cierto desdén pasa por tu lado alejándose del calabozo."

            #scene bg 05afternoon_dungeon_bg:
                #truecenter
                #zoom 0.75 xpos 1.5 ypos 0.5
            scene bg 05afternoon_dungeon_wall_01:
                truecenter
                zoom 0.5
            with hpunch

            p "Son tal para cual..."

            jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02

                #n "Sin demasiada demora sigues sus pasos hasta llegar a la enorme estancia."

                #tx "Ya te he dicho que yo no pienso tratarte Hiromi."

                #tx "Es él o nada."
        
        "Desnúdate.":

            call p_Help

            jump afternoon05_TxellWorkPlace_FuckHiromi_whystillout_GetNaked

        "Te he dicho que me lo pensaría.":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",3)
            $pLockerC.ch_pts_C("hi_hap",-1)

            jump afternoon05_TxellWorkPlace_FuckHiromi_whystillout_Illthinkaboutit

label afternoon05_TxellWorkPlace_FuckHiromi_whystillout_Illthinkaboutit:

    show hiromi_gen_exp_mouth sad_Silentx10
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx10
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "¡¿Hablas en serio?!"

    show hiromi_gen_exp_mouth sad_Silentx11
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    pm "Hablo muy en serio."

    show hiromi_gen_exp_mouth sad_Silentx12
    show hiromi_gen_exp_eyes 00
    show hiromi_gen_exp_piris front00
    show hiromi_gen_exp_eyebrows surprisex03
    with dissolve

    pm "O bajas ese tono de niña malcriada,"

    show hiromi_gen_exp_mouth sad_Silentx13
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    pm "o ya puedes olvidarte de mi ayuda."

    show hiromi_gen_exp_mouth sad_Silentx14
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx15
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "¡¿Qué se supone que tengo que hacer?!"

    show hiromi_gen_exp_mouth sadbiting_Silentx03
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    p "Desnúdate."

    jump afternoon05_TxellWorkPlace_FuckHiromi_whystillout_GetNaked

label afternoon05_TxellWorkPlace_FuckHiromi_whystillout_GetNaked:

    if not protmaster == protname.strip():
        $pLockerC.ch_pts_C("hi_dom",1)
        $pLockerC.ch_pts_C("hi_hap",-1)

    #$ protmaster = protname.strip()

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "Ya has tratado con muchas sumisas,"

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    pm "sabes cómo funciona."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    pm "Compláceme,"

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "y es posible que te lo recompense."

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris right03
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "Si sigues aquí dentro es porque quieres,"

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    pm "así que, a partir de ahora,"

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    pm "haz lo que te pido"

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris left03
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    pm "o sal por esta puerta."

    show hiromi_gen_exp_mouth sad_Silentx02
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows normal
    with dissolve

    pm "¿Me explico?"

    show hiromi_gen_exp_mouth sad_Silentx09
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx12
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    pm "¿Y bien?"

    show hiromi_gen_exp_mouth sad_Talkingx03
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "Sí..."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve
    
    pm "Sí,"

    extend " ¿qué?"

    show hiromi_gen_exp_mouth sad_Silentx17
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx05
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    hi "Sí,"

    extend " [protmaster]."

    show hiromi_gen_exp_mouth sad_Silentx05
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "Ahora haz lo que te he pedido."

    show hiromi_gen_exp_mouth sad_Silentx06
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "..."

    #scene day05
    #with fade

    #scene bg 05afternoon_dungeon_bg:
        #truecenter
        #zoom 0.75 xpos 1.5 ypos 0.5

    scene bg 05afternoon_dungeon_wall_01:
        truecenter
        zoom 0.5

    show hiromi_gen_h_hair_back:
        hiromi_gen_body_right_zoom_0_2_pos

    show hiromi_gen_body_down panties:
        hiromi_gen_body_right_zoom_0_2_pos
    show hiromi_gen_body_up crossed_bra:
        hiromi_gen_body_right_zoom_0_2_pos

    show hiromi_gen_body_c_crossed_pants:
        hiromi_gen_body_right_zoom_0_2_pos
    show hiromi_gen_body_c_crossed_shirt pants:
        hiromi_gen_body_right_zoom_0_2_pos
    show hiromi_gen_body_c_crossed_tie:
        hiromi_gen_body_right_zoom_0_2_pos
    show hiromi_gen_body_c_crossed_jacket:
        hiromi_gen_body_right_zoom_0_2_pos

    show hiromi_gen_h_head earrings:
        hiromi_gen_body_right_zoom_0_2_pos

    show hiromi_gen_exp_blush 02:
        hiromi_gen_exp_right_zoom_0_2_pos
    show hiromi_gen_exp_mouth sad_Silentx07:
        hiromi_gen_exp_right_zoom_0_2_pos
    show hiromi_gen_exp_eyes 04:
        hiromi_gen_exp_right_zoom_0_2_pos
    show hiromi_gen_exp_piris right04:
        hiromi_gen_exp_right_zoom_0_2_pos
    show hiromi_gen_exp_eyebrows sadx01:
        hiromi_gen_exp_right_zoom_0_2_pos

    show hiromi_gen_h_hair_front:
        hiromi_gen_body_right_zoom_0_2_pos
    with dissolve

    hide hiromi_gen_body_c_crossed_jacket
    with Dissolve(1.0)

    pause 1.0

    hide hiromi_gen_body_c_crossed_tie
    with Dissolve(1.0)

    pause 1.0

    hide hiromi_gen_body_c_crossed_pants
    show hiromi_gen_body_c_crossed_shirt free
    with Dissolve(1.0)

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    n "Con lentitud y a regañadientes, empieza a desvestirse,"

    show hiromi_gen_exp_mouth sadbiting_Silentx08
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows sadx02
    with dissolve

    hide hiromi_gen_body_c_crossed_shirt
    with Dissolve(2.0)

    hide screen Points
    hide screen quick_menu
    with dissolve

    pause

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()

    n "hasta que solo le cubren el cuerpo un sujetador rojizo de encaje,"

    show hiromi_gen_exp_mouth sadbiting_Silentx10
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris left04
    show hiromi_gen_exp_eyebrows angryx03
    with dissolve

    n "y unas bragas que no pueden ocultar una cierta protuberancia en su entrepierna."

    show hiromi_gen_exp_mouth sad_Silentx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris right04
    show hiromi_gen_exp_eyebrows angryx02
    with dissolve

    n "En ese instante se detiene."

    show hiromi_gen_exp_mouth sad_Silentx07
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Silentx04
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows serious
    with dissolve

    pm "No te he dicho que pares."

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx04
    with dissolve

    hi "No voy a quitarme nada más."

    show hiromi_gen_exp_mouth sadbiting_Silentx05
    show hiromi_gen_exp_eyes 01
    show hiromi_gen_exp_piris front01
    show hiromi_gen_exp_eyebrows angryx01
    with dissolve

    pm "¿Estás segura?"

    show hiromi_gen_exp_mouth sad_Silentx12
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx05
    with dissolve

    pm "Con esa actitud no vas a tener mucha suerte esta noche."

    show hiromi_gen_exp_mouth sad_Silentx15
    show hiromi_gen_exp_eyes 07
    show hiromi_gen_exp_piris front07
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "..."

    show hiromi_gen_exp_mouth sad_Talkingx09
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "Si te quieres largar,"

    show hiromi_gen_exp_mouth sad_Talkingx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    hi "te largas."

    show hiromi_gen_exp_mouth sad_Talkingx10
    show hiromi_gen_exp_eyes 03
    show hiromi_gen_exp_piris front03
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "Pero te pongas como te pongas,"

    show hiromi_gen_exp_mouth sad_Talkingx13
    show hiromi_gen_exp_eyes 02
    show hiromi_gen_exp_piris front02
    show hiromi_gen_exp_eyebrows angryx07
    with dissolve

    hi "no voy a quitarme esto."

    show hiromi_gen_exp_mouth sadbiting_Silentx08
    show hiromi_gen_exp_eyes 04
    show hiromi_gen_exp_piris front04
    show hiromi_gen_exp_eyebrows angryx06
    with dissolve

    pt "Parece que empezamos a entrar en terreno delicado."

    menu afternoon05_TxellWorkPlace_FuckHiromi_underwear_question:
        
        pt "¿Exigirle que se quite también la ropa interior?"
        
        "O te lo quitas todo, o me voy.":

            call p_Help

            show hiromi_gen_exp_mouth sad_Silentx04
            show hiromi_gen_exp_eyes 07
            show hiromi_gen_exp_piris front07
            show hiromi_gen_exp_eyebrows sadx07
            with dissolve

            hi "..."

            $pLockerC.ch_pts_C("hi_dom",-15)
            $pLockerC.ch_pts_C("hi_hap",-15)

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "AL fin y al cabo debía de habérmelo imaginado."

            show hiromi_gen_exp_mouth sad_Talkingx005
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "Mi instinto no suele fallar."

            show hiromi_gen_exp_mouth sad_Talkingx10
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx06
            with dissolve

            hi "No eres más que un cenutrio ególatra que no sabe dónde cambiar de marcha o parar."

            show hiromi_gen_exp_mouth sad_Silentx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris right04
            show hiromi_gen_exp_eyebrows angryx05
            with dissolve

            pt "¿Acaso le da vergüenza poner su polla al descubierto?"

            show hiromi_gen_exp_mouth sadbiting_Silentx04
            show hiromi_gen_exp_eyes 07
            show hiromi_gen_exp_piris front07
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            pt "¿o quizás sus pechos operados?"

            show hiromi_gen_exp_mouth sad_Talkingx07
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx04
            with dissolve

            hi "Tranquilo,"

            show hiromi_gen_exp_mouth sad_Talkingx08
            show hiromi_gen_exp_eyes 03
            show hiromi_gen_exp_piris front03
            show hiromi_gen_exp_eyebrows angryx03
            with dissolve

            hi "no hace falta que te vayas."

            show hiromi_gen_exp_mouth sad_Talkingx006
            show hiromi_gen_exp_eyes 04
            show hiromi_gen_exp_piris front04
            show hiromi_gen_exp_eyebrows angryx06
            with dissolve

            hi "Ya me voy yo."

            scene bg 05afternoon_dungeon_wall_01:
                truecenter
                zoom 0.5

            show hiromi_gen_h_hair_back:
                hiromi_gen_body_left_zoom_0_5_pos
            show hiromi_gen_body_c_crossed_dressed:
                hiromi_gen_body_left_zoom_0_5_pos
            show hiromi_gen_h_head earrings:
                hiromi_gen_body_left_zoom_0_5_pos

            show hiromi_gen_exp_blush 01:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_mouth sad_Silentx10:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_eyes 04:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_piris front04:
                hiromi_gen_exp_left_zoom_0_5_pos
            show hiromi_gen_exp_eyebrows angryx06:
                hiromi_gen_exp_left_zoom_0_5_pos

            show hiromi_gen_h_hair_front:
                hiromi_gen_body_left_zoom_0_5_pos
            with dissolve

            n "Rápidamente recoge sus cosas y sale del calabozo."

            #scene bg 05afternoon_dungeon_bg:
                #truecenter
                #zoom 0.75 xpos 1.5 ypos 0.5
            scene bg 05afternoon_dungeon_wall_01:
                truecenter
                zoom 0.5
            with hpunch

            p "..."

            pt "Me parece que he tensado demasiado la cuerda..."

            jump afternoon05_TxellWorkPlace_FuckHiromi_SheLeaves_02

                #n "Sin demasiada demora sigues sus pasos hasta llegar a la enorme estancia."

                #tx "Ya te he dicho que yo no pienso tratarte Hiromi."

                #tx "Es él o nada."

        "<Aceptar por ahora que esté con su lencería>":

            call p_Help

            $pLockerC.ch_pts_C("hi_dom",1)
            $pLockerC.ch_pts_C("hi_hap",1)

            jump FuckH_underwear_No



############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

            # Redireccionar ahora conversación a amordazar y follar a Meritxell o ser follada por ella... Dependería. :P (Pero primero escribir la primera opción.)



# Sé que esta noche tienes la última cita con ella... No sé cuales son sus intenciones contigo, ni sé muy bien por qué convirtió a tu amigo en mujer, pero solo puedo decirte, ten cuidado. No es alguien con quien puedas bajar la guardia.


## Al final de la conversación, esta te agradece tu ayuda con su ex y con insinuaciones te ofrece la posibilidad de demostrar tus habilidades con una profesional como ella (Dependiendo de si has demostrado ser sumiso o dominante en la anterior cita). Si aceptas, lo hace con una condición. Una palabra clave "Súcubo" o pellizco en tu piel para indicarte que detengas en seco lo que estés haciendo. Te confiesa que no es la primera vez que actua como esclava, pero sí es la primera vez que lo hace siendo el dominante un hombre.

    # aker = Macho cabrío, larre = prado. (Euskera)  == Sabbat, tradición precristiana. (La religión judía santificaba el sabbat, Sábado, jornada de descanso). El término sabbat fue acuñado en sentido peyorativo como "reunión para ejecutar prácticas demoníacas, acusando a los judíos de adoradores del diablo."

    # Antropologicamente, los aquelarres eran reminiscencias de ritos paganos, como los bacantes, Neodruidismos y cultos célticos, celebraciones clandestinas al no estar admitidas por las autoridades religiosas de la época.

    # Sorginak = Bruja (En euskera también)

############################################################################################################
# Protagonista llega hasta la dirección indicada por Txell, frente al timbre de su oficina.

# Al llamar, le sale la voz de Txell lamentándose de que ha tenido una visita imprevista, de todos modos te invita a subir.

# Una vez en la oficina, te encuentras a Txell en su despacho y a una chica desconocida.

# La chica se pone a discutir con Txell preguntando por tu presencia y esta discutiendo con ella que no es de su incunvencia, que es ella a que se ha presentado sin previo aviso.

# Reprochándole los años que hace que se conocen, le pide el favor de forma extra-oficial, esta le responde que no puede ayudarla, que entre ellas hay una relación sentimental y que no puede atenderla de forma profesional, que le ayudará a encontrar a otra dominatrix que pueda atenderla y ayudarla como es debido.

# Esta se niega rotundamente, que la única persona que la conoce y puede ayudarla es ella, y es la única persona con la que confía lo suficiente.

# Le reprocha varias cosas, primero que Domingo festivo, que aceptado verla por su antigua relación, pero que no puede tratarla por razones éticas y profesionales.

# Después de una discusión algo acalorada y en la que ninguna de las dos partes parece ponerse de acuerdo, le pide unos minutos para poder hablar con su invitado.

# Se acerca a ti y te pide que la sigas.

# Te lleva a la "mazmorra". Te explica que tiene varias salas con las que trata distintos casos.

# Te pide disculpas por la situación. (Dependiendo de qué tipo de sumiso o dominante eres te lo menciona).

# Te pregunta si estarías dispuesto a ayudarla.

# Te explica la situación resumidamente.

# Se llama Angustias, fue durante 2 años su pareja sentimental cuando aún era Escort y se pagaba sus estudios. La relación entre ellas no era lo que se podría llamar convencional.

# Le está pidiendo ayuda porque ha conocido a un hombre del que se está enamorando profundamente, pero este resulta ser un sádico BDSM que le gustan las cosas muy duras, este realmente no le pide nada porque no quiere forzarla, pero ella tiene ganas de satisfacer sus necesidades, pero no es algo que le resulte fácil habiéndo ella sido antes mucho más dominante y apenas habiendo probado la experiencia de haber sido sumisa. (Han pasado 10 años desde que Txell y ella cortaron).

# Te pregunta si te verías capaz de actuar como su dueño durante una sesión, ella como expareja, no puede hacerlo y en realidad ya de por si que te ofrezca hacer semejante cosa a alguien como tú sin experiencia en este campo ya le podría suponer la suspensión de su cargo y además una multa considerable, pero por otra parte quiere ayudar a su amiga.

# El problema es que ella no te podrá guiar durante el transcurso, ya que si hiciera eso, no se sentiría realmente dominada por su dueño y sería algo equívoco, ella estará ahí presente para detener el circo si realmente escala demasiado o ve algo que no le gusta demasiado.

# La mayoría de sus clientes requieren de sus servicios para liberar tensión, pero este caso es algo distinto y más delicado, que debería llevar más sesiones, lo ideal sería demostrarle a su amiga, que no requiere realmente de los servicios de Txell y que podrá buscar ayuda o aceptar el proceso de forma pausada y a su ritmo, pero para ello necesita romper el hielo del miedo que la posee, o puede llegar a destrozarle por dentro poco a poco si no saca el tema.

#Lo ideal en esta sesión es de que no hubiera sexo a menos que ella realmente te lo pidiera y en ese caso habría que verlo... NO es el sexo lo que se trata en esta sesión, sino de tener el control de la situación siendo ella sumisa (no humillada), aceptando su rol de Sumisa, mediante azotes

# No se trata de que consiga orgasmos, se trata de que sea completamente abierta a cualquier orden o acto de sumisión que puedas llevar a cabo y para ello hay que ir paso a paso, consiguiendo que acepte su rol.

# Una vez la das por terminada o ella ha perdido el conocimiento por la cantidad de orgasmos logrados, Txell da por conluída la sesión.



########################
########################



# La lleva a la ducha y te pide que la esperes en la biblioteca, acompañándote hasta ella.

# Una vez allí, encuentras una silla muy cómoda para poder dedicarlo a la lectura.

# Empiezas a indagar en los libros que hay en la estanterías, entre ellos destacan libros clásicos, otros más populares, una sección entera obviamente sobre sexualidad, dominación, psicología.

# Sin embargo hay una sección que te llama particularmente la atención, libros sobre ufología, posesión demoníaca, viajes en el tiempo, el vaticano, Antiguo Egipto, Dioses antiguos, magia blanca, rituales satánicos, vampiros, licantropía, más allá de la muerte, demonología, Súcubos.

# Prestas especial atención a ese libro, que parece estar menos ordenado y bien puesto que los demás, como si hubiera sido leído recientemente. En él te encuentras un marca páginas en el que decides echarle un ojo y ver que dicha sección habla sobre el "macho cabrío".

# En dicha descripción se describe uno de los propósitos del akelarre, la gestación de una futura bruja mediante una orgía entre todas las mujeres ahí presentes con el símbolo fálico del hombre vestido en bestia que ha sido poseído por el mismísimo diablo, el cual fecunda a sus hijas para que prosiga su linaje.

# Pensando en voz alta. "¿Y que ocurriría si el feto resultase siendo varón?"

# La voz de Txell: "Se le sacrificaría en nombre del macho cabrío."

# En realidad esa es una versión de muchas otras, lo que se conoce como el "diablo", en realidad suele estar sujeto a muchas otras entidades, cada una con sus caprichos y sus dogmas, la gente cree en que el diablo es una entidad única e indivisible, cuando en relidad es tan abundante como la humanidad misma.

# En este caso habla de que esta entidad adopta el cuerpo del hombre elegido para el akelarre, en el que fecunda a sus hijas, mujeres que ya fueron parte de su herencia antiguamente, suele tener un harén de unas 10 mujeres aproximadamente por akelarre, de este modo la sangre siempre se mantiene. El akelarre se suele llevar a cabo una vez por cada solsticio (2 veces por año). Aunque en Zugarramurdi se celebraba tres veces por semana, los lunes, miércoles y viernes después de las nueve de la noche.

# Se untaban agua verdinegra y repugnante obtenida del sapo, para conseguirla azotaban al sapo cono una varilla y una vez que estaba bien hinchado lo apretaban con el pie contra el suelo hasta que vomitaba el agua hedionda que cuidadosamente recogían y guardaban. Mientras se untaba recitaban la fórumal "Señor, en tu nombre me unto; de aquí en adelante yo he ser una misma cosa contigo, yo he de ser demonio". Y gracias al ungüento podían salir volando por ventanas, agujeros o grietas que abre el demonio. Obviamente estas delaraciones tan coherentes fueron extraídas después de varios días de suave y delicada tortura por parte de la inquisición.

# En otras zonas los mecanimos más usuales para convocar el aquelarre eran una campana que sólo oían los adeptos y un escozor en la llamada marca del Diablo, que el brujo ocultaba y que los inquisidores utilizaban como prueba en los juicios por brujería.


# Según la relación del proceso de Zugarramurdi, en cuanto llegaban los brujos y brujas al lugar del aquelarre, adoraban al diablo postrándose de rodillas ante él y besándole en sus pudendas. Después se mexclaban entre ellos y comenzaban a danzar y a bailar. 

# Estas sesiones se usaban en parte para borrar su rastro, usar el mal de ojo o bien su muerte a hombres, mujeres, niños, ancianos o incluso los aún no nacidos; bien por protección, por veganza, por celos o por simple capricho.

# "Por otro lado, si a algún brujo o bruja se le escapaba el nombre de Jesús, el aquelarre se desvanecía, por lo que en la próxima reunión era severamente castigado".

#"Pero pronto comienzan sus escapadas para a sustar a pasajeros nocturnos, a pastores, marineros, molineros, amigos y enemigos, para romper platos en las cocinas y tejas en las casas, destruir granos, frutos y ganado, y también para causar muertes especialmente de niños."

# En otras zonas el homenaje al demonio va acompañado de ofrendas, aunque éstas no siempre tienen un carácter siniestro, sino que pueden ser simplemente objetos producto de un robo o la prueba de que se ha cometido un acto ilícito a ojos de la ley divina. Los primeros en ofrecer estos votos son los brujos de mayor jerarquía; los últimos los brujos novicios o recién iniciados. A estos se les coloca la marca que distingue a un brujo en una parte recóndita del cuerpo y pasan desde ese momento a ser miembros plenos de la cofradía. En cuanot al baile, en otras zonas los asistentes se abandonan a una danza que comienza con movimientos organizados; pueden danzar en círculo, unidos por los hombros o formando el uróboros, la serpiente qeu se muerde la cola. Pooco a poco, la danza pierde unidad y se va transformando en una sucesión frenética de sacudidas.

# Según lo que creyeron averiguar los inquisidores del caso de Zugarramurdi, en algunas noches señaladas como la víspera de Reyes, de la Ascensión, del Corpus Christi, de Todos los Santos, de la Asunción de la Virgen o de San Juan se celebraba un ritual especial, que constaba de dos partes.

# En la primera los brujos y brujas se confesaban ante el demonio y se acusaban de haber entrado en una iglesia, de haber oído misa... y de los males que habían podido hacer y no habían causado.

# La segunda era la misa sacrílega celebrada por el demonio revestido con ornamentos negros, feos y sucios. Durante la misma se seguían los mismos pasos que en la misa cristiana. Tras el sermón en el que el demonio exhortaba a los brujos y brujas a hacer el mal, prometiéndoles a cambio el paraíso, los "feligreses" uno por uno se acercaban al demonio y se arrodillaban ante él besándole la mano izquierda, los pechos, los genitales y el ano (el llamado osculum infame).

# Según las confesiones de los supuestos brujos y brujas, cuando llegaba el momento de la consagración el demonio alzaba algo parecido a una suela de zapato donde estaba su figura y decía Esto es mi cuerpo y a continuación un cáliz de madera, negro y feo, mientras los brujos lo adoraban arrodillados. Después los brujos y brujas se acercaban al "altar", que estaba cubierto con un viejo paño negro, feo y deslucido y comían y bebían lo que el oficiante había "consagrado".

# Hasta aquí la misa negra había sido una réplica exacta de la misa cristiana, pero el final era completamente diferente. El demonio copulaba con las brujas y sodomizaba a los brujos y después comenzaba la orgía, en la que volvía a participar el diablo. "Brujos y brujas se mezclan sexualmente y aparean unos con otros en total promiscuidad, sin consideraciones de sexo ni grados de parentesco".19​ >

# Para algunos inquisidores, la razón última del sabbat era precisamente el emparejamiento sexual con el Diablo y el de los brujos entre sí. Cuanto más repugnante y ofensivo fuera el acto sexual, más favorable era a los ojos de Satanás, concluían.

## https://es.wikipedia.org/wiki/Aquelarre (Seguir por aquí)

# Según la relación publicada en 1611 sobre el proceso de Zugarramurdi, durante el aquelarre los brujos y brujas celebraban un "banquete" en el que comían cadáveres de brujos fallecidos recientemente o de víctimas de sus actos maléficos, especialmente niños, que desenterraban de las sepulturas acompañados del demonio y de sus criados.

# "Allí mismo y sobre la sepultura les sacan las tripas y los descuartizan; cubren la sepultura para que no se advierta la profanación y se ponen en camino de vuelta al aquelarre con gran regocijo y contento, llevando los padres los cadáveres de los hijos o los hijos a los de sus padres y hermanos y las mujeres a sus maridos. Allí los despedazan y los dividen en tres partes: una la asan, otra la cuecen y la tercera la dejan cruda; puesto todo sobre una mesa de manteles sucios y negros, reparten las viandas los parientes más cercanos, reservando el corazón para el demonio". Algunos de los interrogados por los inquisidores confesaron también que raptaban niños y les chupaban la sangre, mientras el demonio les decía: "Chupa y traga eso, que es bueno para vosotras".20​

# El aquelarre acaba al amanecer cuando suenan las primeras campanadas de la iglesia21​ o con el canto del gallo.


# aker = Macho cabrío, larre = prado. (Euskera)  == Sabbat, tradición precristiana. (La religión judía santificaba el sabbat, Sábado, jornada de descanso). El término sabbat fue acuñado en sentido peyorativo como "reunión para ejecutar prácticas demoníacas, acusando a los judíos de adoradores del diablo."

# El Sabbat empieza con la aprición de la primera estrella en el firmamento vespertino del viernes.

# Sacrificios humanos, para poder dar vida, primero había que quitarla, generalmente el hombre poseído por el macho cabrío moría tanto por extenuación al mantener sexo desenfrenado durante toda la noche y por la posesión misma que le causaba graves trastornos psicológicos que le convertían en algo menos que un ser humano.

# Antropologicamente, los aquelarres eran reminiscencias de ritos paganos, como los bacantes, Neodruidismos y cultos célticos, celebraciones clandestinas al no estar admitidas por las autoridades religiosas de la época.

# Sorginak = Bruja (En euskera también)

# Es frecuente el uso de diversas sustancias para alcanzar el éxtasis durante el rito. Como no se pueden calibrar con exactitud las dosis, es muy peligroso administrarlas por vía oral cuando una cantidad letal está muy cercana a la dosis de uso. Por ello algunas sustancias se aplicaron en forma de ungüento por vía vaginal o rectal, lo que podría haber dado origen a algunas leyendas sobre el carácter sexual de las reuniones de brujas o el uso de calderos para la preparación de algunas de las sustancias. La aplicación de una de las sustancias sobre la vagina con una especie de consolador pudo dar origen a la imagen que representa a las brujas con un palo entre las piernas o bien una escoba. Por otro lado, muchos sapos son venenosos por contacto y su piel puede ser alucinógena; por ello también forman parte de la imaginería vinculada al mundo de la brujería. Algo similar sucede con algunas setas venenosas, como la Amanita muscaria.

# Formas de matar a una bruja, era popular quemarlas vivas o hacer la prueba del agua. Ciertas malas lenguas, dicen que estas son capaces de transmutar su cuerpo para ocultarse entre la muchedumbre, o conseguir una apariencia mucho más seductora para poder conquistar a su siguiente presa, ahí es dónde la brujería y la demonología se mezclan. Dicho de otro modo, no hay forma posible de matar a una bruja facilmente, pues una vez bien alimentadas son capaces de regenerarse en un lapso de tiempo asombroso, su cambio de imagen no es instantáneo ni gratuito, requieren de sacrificios de sangre y alma. AL mismo tiempo se dice que envejecen rápidamente sino consumen con asiduidad, que su vida puede llegar a ser eterna si están bien alimentadas, que debido a esto no pueden hundir su cuerpo bajo el agua que el único modo de asegurarte de que no regresará de entre los muertos es desangrarla por completo o quemar su cuerpo.

# No todos los akelarres servían para fecundar, a veces eran simplemente para recordar quien es el "padre" de ese matriarcado, y también obviamente porque es un momento máximo de energías que fluyen, otro modo de decir que debía de ser una orgía de dimensiones bíblicas.

# 1. Que se sacrificaban a los hijos varones.
# 2. Que se procreaban a través del Akelarre con incesto con el macho cabrío.
# 3. Que se comunicaban mediante telepatía.
# 4. Que consumían drogas de todo tipo. (Ranas, setas, engunges)
# 5. Que sacrificaban a varones que se follaban y luego morían.
# 6. Que sacrificaban a un recién nacido antes de procrear para tener un hijo.
# 7. Que celebraban una misa negra (parodia de la real) para iniciar la sesión, cuando aún estaban cuerdos.
# 8. Se comían carne real y sangre real, en esta última contenía gran parte de la droga ya mencionada.
# 9. Poco después es cuando empezaban a tomar drogas más fuertes, empezaban desnudándose y bailando ensangrentadas alrededor de los hombres inducidos en una hipnósis.
# 10. Pueden recrear imágenes en la mente de los demás.
# 11. Pueden cambiar su morfologia con tiempo, pero en un akelarre, la energía es tan grande que son capaces de hacerlo bastante más rápido.
# 12. La energía que fluye en un akelarre, alrededor del fuegon el oscuridad, en realidad el fuego en el medio es un tipo de protección para que no se acerquen demasiado, debido a la enorme energía que se origina en el centro, no es otra cosa que entes oscuros hambrientos de un alimento que no es carne ni nada material.
# 13. Cuando ha terminado la misa negra y mientras algunas danzan, otras se drogan, otras empiezan a follarse a su carnada, estas no tienen ningún tipo de compasión con sus víctimas, no solo los violan de forma encarnizada, les hacen cortes, se beben su sangre, les muerden, les cortan los dedos, se transforman en criaturas grotescas con mandíbulas caninas y empiezan a devorarlos en vida mientras este no puede evitar tener un orgasmo y justo en ese instante muchas suelen amputarles el organo sexual, bien mediante cuchillo, mordida o con una fuerza increíble arracándosela de cuajo.
# 14. Una vez la víctima ha sufrido una de las peores muertes posibles, es arrojado a lo lejos del fuego en la oscuridad, dónde su cuerpo es arrastrado por esas entes ocultas en las tinieblas, desapareciendo en la inmensidad del prado.
# 15. Después de eso, el macho cabrío reclama su parte del premio y estas empiezan a copular con él, solo si alguna de ellas tiene alguna ofrenda especial, como un recien nacido para tener progenie. Este sacrifica el niño, bien comiéndoselo, desangrándolo vivo o destrozándolo con su organo fálico para luego lanzarlo a la oscuridad. Después de eso empieza a copular con su hija para ofrecerle la progenie que pide.
# 16. Si la mujer trae a su hijo y este es varón se le sacrifica, debe de haberlo escondido durante 3 meses, pero debe traerlo o el castigo puede ser terrible.
# 17. Es la madre quien tiene que matar a su propio hijo en frente del macho cabrío mediante el método que pida este a su propia hija.
# 18. Si el hijo resulta ser hembra, a esta se le hace un ritual de iniciacion, que es como un bautizo, pero en parodia. La niña va creciendo de forma natural hasta que tiene su primera regla, que es cuando puede empezar a actuar como una bruja más de su harén.
# 19. Los entes son el verdadero poder del macho cabrío, estos le otorgan poder e inmortalidad en el otro plano mediante sacrificios otorgados en el momento del orgasmo, dónde sus hijas no solo succionan su semilla para alimentrase, sino también su alma, estos también se encargan de hacer desaparecer el cuerpo.



## Al final de la conversación, esta te agradece tu ayuda con su ex y con insinuaciones te ofrece la posibilidad de demostrar tus habilidades con una profesional como ella (Dependiendo de si has demostrado ser sumiso o dominante en la anterior cita). Si aceptas, lo hace con una condición. Una palabra clave "Súcubo" o pellizco en tu piel para indicarte que detengas en seco lo que estés haciendo. Te confiesa que no es la primera vez que actua como esclava, pero sí es la primera vez que lo hace siendo el dominante un hombre.

## Después de la sesión,

# Te confiesa que estuvo tratando a Neus como una clienta más durante casi un año, ella le pedía que la tratara como sumisa, como una clienta más en el fondo. Pero no era una clienta más, en cada nueva sesión, por alguna razón sentía que a pesar de que yo era la que usaba el látigo y la amordazaba, era yo quien me sentía cada vez más sumisa ante ella, aunqeu no hablara, tenía la sensación que oía su voz en mi cabeza en alguna ocasión. Nunca he intimado con ninguna clienta, es una norma que la cumplo a raja tabla, pero no sé por qué, ella me inducía a todo lo contrario, no solo ello, tenía la sensación que quería complacerla. Tampoco era una clienta habitual, solía pedirme las cosas más extremas que he llegado a hacer en una sesión, sobretodo me pedía humillación y dolor, sentía que de algún modo, quería castigarse a si misma por algo que nunca llegó a revelarme del todo. Aunque parezca pequeña e indefensa, la sensación que he ma ha dado al conocerla durante todo este tiempo es todo lo contrario. Tengo la sensación de estar hablando con alguien mucho más mayor, con mucha más experiencia, con un dolor y un sufrimiento que no tiene nombre, a veces incluso me daba la sensación que su cupero no era siempre el mismo, incluso sus pechos parecían de distinto tamaño según la sesión. 

# La sensación era entre fascinación, miedo y deseo por ella. pero de un modo que jamás antes he llegado a experimentar. En cada nueva sesión quería acercarme a ella, al principio como profesional tenía la curiosidad de conocer más detalles sobre su vida, sobre sus problemas, sus preocupaciones, pero a medida que el tiempo avanzaba, mi profesionalidad iba apartándose para dar paso a un interés emocional por ella, preocupándome por ella, cada vez me costaba ofrecerle el dolor y la humillación que me pedía, intentaba acercarme a ella, abrazarla, besarla... Ahí es donde ella se dio cuenta y me frenó en seco. Había cometido el mayor error que una profesional puede cometer, me enamoré de ella. Fue entonces cuando ocurrió lo más extraño de todo ello... le vi sus ojos, violeta brillante, lo siguiente que recuerdo es estar en mi despacho, vestida... y aún más extraño, ni si quiera la recordaba. Nada, como si nunca hubiera existido, lo primero que hice fue coger mi agenda para ver cuando sería el siguiente cliente, ni siquiera me pregunté como llegué allí o que pasó antes... Nada. ¿Cómo me acuerdo de ella? ¿Como recuperé la memoria?

# Semanas después en un sueño me encontraba en medio de un prado en plena noche y había una fogata a lo lejos, me acerqué a ella, no había nadie, hasta que de la oscuridad unos ojos rojizos extraños aparecieron de la nada, hasta que vi que se trataba de un macho cabrío gigante y monstruoso, me agarró por los brazos, me desnudó violentamente y empezó a violarme de forma indescriptible sobre el húmedo y frío suelo, yo no podía hacer absolutamente nada, más que chillar y llorar, cuando terminó dentro de mi, me susurró al oído: Recuerda. Me lanzó a las llamas y de pronto me desperté completamente sudando en la cama... Y ahí lo recordé todo lo sucedido con Neus.

# Fue entonces cuando descubrí que no solo seguíamos coincidiendo en clase de arte, sino que además estaba interesado por ti, sinceramente desde ese momento empezé a cogerte rabia, pero tampoco podía decirte nada, Aún recordando lo ocurrido con Neus, seguía dándome cierto respeto el hecho de que no entendía nada de lo que había sucedido, sus ojos brillantes tampoco me ayudaron a hablar con ella, y el enamorarme de alguien que luego fue capaz de borrarme la memoria no me ayudó a entablar conversación, así que intenté observaros en la distancia... Te seguí (o lo vio por internet?) en los grandes almacenes con tu compañero de piso convertido en chica... y luego recibí tu llamada, en el móvil del número que yo jamás te di.

# Si por lo que dices, cuando me conociste tenía los ojos rojos y te di mi número coqueteando contigo... es algo que tampoco recuerdo. Sé que esta noche tienes la última cita con ella... No sé cuales son sus intenciones contigo, ni sé muy bien por qué convirtió a tu amigo en mujer, pero solo puedo decirte, ten cuidado. No es alguien con quien puedas bajar la guardia.

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################