

default room_3doors_met = False
default day04_Didac_Foreplay = False
default day05_BeachDidacSex = False

default DidacSex_Unsafe = False
default DidacSex_Vaginal = False
default DidacSex_JustForePlay = False
default DidacSex_NotEvenForePlay = False
# default DidacMCPregnant = False
# default DidacOKUPregnant = False
default DidacPregnant = False
default DidacOKUPregnant_YouKnowIt = False
default NeusCuckolded = False
default NeusCuckolded_Sexually_Didac = False
default NeusCuckolded_Sexually = False

default afternight05_Pedrera_HotelExplanation_Loop_Cond = 0

default afternight05_Pedrera_Vegan_TellMeIsALie = False
default afternight05_Pedrera_Vegan_ColdBlood = True
default afternight05_Pedrera_Vegan_AnimalsOverHumans = False

default night05_Interrogation_GrowYouADick_LikeToTry = False
default night05_Interrogation_GrowYouADick_NotAProblem = False
default night05_Interrogation_GrowYouADick_Disgusting_Cond = False
default night05_Interrogation_GrowYouADick_DontBotherYou = False
default night05_Interrogation_GrowYouADick_EternalLove_Cond = False

default afternight05_Pedrera_OtherOption_NeusAppear_Assasin = False
default afternight05_Pedrera_OtherOption_NeusAppear_Neus = False

default afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat = 0
default afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat_b = 0

default afternight05_Pedrera_AntExplanation_Cond = False
default afternight05_Pedrera_Guarantee_IPromise = False

default afternight05_Pedrera_Guarantee_ContactYou_Cond = False
default afternight05_Pedrera_NoChoice_Refuse_Cond = False
default afternight05_Pedrera_NeusWillDie_Forced_Cond = False
default afternight05_Pedrera_MotherConverstaion_ToldHerNotTriedCookies = False

default afternight05_Pedrera_Guarantee_DirtyHeartlessKiller_Cond = False
default afternight05_Pedrera_TwoBirdsOneShot_IOnlyNeedNeus = False

default afternight05_Pedrera_WhyNotKillMe_ImNotAKiller = False
default afternight05_Pedrera_WhyNotKillMe_NoneDeserveDeath = False
default afternight05_Pedrera_WhyNotKillMe_FollowOrders = False
default afternight05_Pedrera_WhyNotKillMe_WhoILove = False

default gensex_ILoveYouNeus = False
default gensex_INotLoveYouNeus = False
default gensex_YoureAMonster = False
###
default gensex_NotLoveSister = False # If you told her you don't love her because she is your sister.
default gensex_LikeYou = False # You like her, but not love her. (Not sure if I'm gonna use it.)



default afternight05_Pedrera_Food_Biscuit_MotherTold = False

default NeusDick_NoProblem = False

default afternight05_Pedrera_NeusLoveDoubts_Cond = False

default ped_neusname_angry = False

# n "Agarras de la mano a tu compañera,"

# n "como si fuera una niña pequeña sigue tus pasos con la mirada perdida y el rostro en un mar de lágrimas."

# n "Conseguís coger un taxi justo en la salida y durante el transcurso del viaje,"

# n "Neus sigue manteniendo esa mirada perdida en la nada,"

# n "cogida de los hombros y temblando de miedo."

# pt "¿Qué diablos será lo que aún no me ha contado...?"

label afternight05_Pedrera_arrive:

    #scene morning04_bedroom_Neus_body_body 02c with ImageDissolve("images/day04/morning04_bedroom_Didac_body_body_02c.webp", 3.0, ramplen=8, reverse=True, alpha=True, time_warp=None)

    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx1')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx2')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx3')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx4')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx5')
    $ renpy.music.set_volume(0.0, delay=3.0, channel='sfx6')

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    stop music fadeout 3.0

    $ saturation_tint_level = "default"
    $ deyesp = "_rim"
    $ p_deyesp = "_rim"

    ##

    #call endtranslation

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene night03_bg street_pedrera_far
    with fade

    n "Viendo que Neus sigue en su trance,"

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/traffic01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    if music_play != "lostFrontier":
        play music "audio/music/kevinmacleod/sad/lostFrontier.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "lostFrontier"

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
    show neus_exp_mouth sad_Silentx04:
        neus_exp_atright_position
    show neus_exp_eyes 02:
        neus_exp_atright_position
    show neus_exp_iris right02:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx03:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position

    with dissolve

    n "decides tomar la iniciativa y pagar tú mismo al taxista una vez llegáis delante del emblemático edificio."

    show neus_exp_blush 02
    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyes 01
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    play sound "audio/sfx/grabarm01.ogg"

    scene bg dark_a_blurry_01
    show night04_pedrera_Ngrabhand_hold_night05:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0
        ease 2.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "cogiéndola de la mano,"

    scene night03_bg street_pedrera_close
    with fade

    n "la arrastras hasta llegar al portal."

    play sound "audio/sfx/door_old_short_open02.ogg"

    # El jugador puede no haber ido a su casa...? En teoría no... no tendría suficientes puntos... NO? # NOT FINISHED

    scene night03_bg_street_pedrera_door_opened02
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
    show neus_exp_mouth sad_Silentx04:
        neus_exp_atright_position
    show neus_exp_eyes 04:
        neus_exp_atright_position
    show neus_exp_iris left04:
        neus_exp_atright_position
    show neus_exp_eyebrows sadx03:
        neus_exp_atright_position
    show neus_exp_glasses:
        neus_exp_atright_position
    show neus_exp_hairfront:
        neus_exp_atright_position
    with dissolve

    n "Nerviosamente consigue abrir la puerta."

    $ pdaytime = "05_night_Pedrera"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    scene night03_bg street_pedrera_entrance
    with fade
    show night03_bg_street_pedrera_entrance_lightson:
        subpixel True
        alpha 0.0
        easein_quad 5.0 alpha 1.0

    n "Una vez dentro decides subir por las escaleras sin esperar el ascensor."

    scene night03_bg street_pedrera_corridorclosed:
        truecenter
    with fade

    play sound "audio/characters/didac/orgasm01.ogg"

    d "{size=15}AAAhhhmmm...{/size}"

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    n "Apenas a unos metros de la puerta que da lugar al piso,"

    n "oyes, lo que es sin duda alguna, los gemidos de Dídac."

    p "¡¿Qué diablos?!"

    n "Sientes como Neus aminora el paso,"

    show night03_bg street_pedrera_corridorclosed:
        subpixel True
        #truecenter
        easein_quad 5.0 zoom 2.0 xpos 0.8 ypos 0.3

    n "pero aún así consigues arrastrarla para llegar hasta la puerta,"

    play sound "audio/sfx/door_old_short_open03.ogg"

    scene night03_bg street_pedrera_hall01
    with fade

    n "y abrirla con sus llaves."

    play sound "audio/characters/didac/orgasm03.ogg"

    d "{size=35}¡¡MMMHHMFFF...!!{/size}"

    if night04_Neus_Blowjob_Cum_Affirmative:

        pt "Sus gemidos provienen de la habitación dónde Neus me arrastró para hacerme esa extraña mamada."

        pt "Dónde hay esa cuna,"

        if night05_Plaza_Food_Biscuit:

            extend " y el mismo olor que las galletas de Neus..."

        else:

            extend " y ese olor tan familiar..."

    else:

        n "Os dirigís hacia el origen de los gemidos."

        if night05_Plaza_Food_Biscuit:

            pt "Esta habitación..."

            pt "Huele igual que las galletas que me ha dado de comer Neus."

        else:

            pt "¿Y este olor a galletas?"

    #$ saturation_tint_level = "default"
    $ saturation_tint_level = "dark"

    scene bg night04_pedrera_bedroom_69:
        subpixel True
        truecenter
        zoom 1.0 ypos 0.5 xpos -1.0
        easein 20.0 zoom 0.5 ypos 0.5 xpos 0.5
    with fade

    # scene bg night04_pedrera_bedroom_69:
    #     truecenter
    #     zoom 0.5

    play sound "audio/characters/didac/moanings03.ogg"


    n "Con la luz encendida, ves dos cuerpos desnudos encima de la cama,"

    n "uno de ellos, obviamente es Dídac,"

    n "con su cuerpo menos musculado y completamente desnuda."

    n "Pero entre sus piernas completamente abiertas, encuentras a la rubia tetuda de clase,"

    show bg night04_pedrera_bedroom_69:
        #truecenter
        
        ease 5.0 zoom 2.0 xpos 0.0 ypos -0.15 

    play sound "audio/characters/didac/orgasm01.ogg"

    n "dándole un repaso a su entrepierna con su lengua."

    # O Txell

    $ dad = d_txell
    $ dadname = "Meritxell"

    $ meyesc = "_red"
    $ mmouthp = ""
    $ deyesc = "_red"

    if night05_Interrogation_TxellName_Cond or afternoon04_MACBA_TxellName_Know:

        p "¡¿Meritxell?!"

        p "¡¿Qué-"

        extend "qué estás haciendo aquí?!"

    else:

        ne "Meritxell..."

        pt "¿Así es cómo se llama la rubia?"

        pt "¡¿Qué diablos está haciendo aquí?!"

    if music_play != "rightBehindYou":
        play music "audio/music/kevinmacleod/creepy/rightBehindYou.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "rightBehindYou"

    ## DryingChin

    $ meyesc = "_red"

    $ Pedrera_char_Cond = "TxellDChin"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx03
    show m_hand drying:
        subpixel True
        transform_anchor True
        xalign 0.39 yalign 0.35
        zoom 1.5
        xpos 0.5 ypos 0.5 # beginning
        ease_quad 8.0 xpos 1.0 ypos 0.68 # End
    with fade_long305s

    n "Secándose la barbilla húmeda por el flujo vaginal de Dídac,"

    n "te observa con sus ojos completamente rojizos y una sonrisa de oreja a oreja."

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    $ meyesc = "_red"

    show m_hand drying:
        ease 5.0 xpos 1.5 ypos 1.5 # Down

    dad "Al fin llegasteis,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx03
    with dissolve

    dad "tardasteis tanto que empezamos sin vosotros."

    $ meyesc = "_goat"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx03
    with dissolve

    p "Pero..."

    $ nteye = 5
    $ ntlong = 1

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03

    with fade

    ne "Sus ojos."
    
    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx05
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "No es Meritxell."

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 8
    if ntlong in range (0,6):
        if ntlong < 5:
            $ ntlong += 1
    call neus_exp_tears_tears
    show neus_exp_iris front08
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "Es mi padre."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows sadx05
    with dissolve

    $ meyesc = "_red"

    $ Pedrera_char_Cond =  "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with fade

    dad "\"{i}Nire elur maluta txikia{/i}\"."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Te he echado de menos,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    dad "{i}Txiki{/i}."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sad_Silentx06
    show neus_exp_iris right05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    
    with fade

    ne "..."

    #########################################################

    if config.version < "00.13.08": # Seeing Situation at Pedrera.
        call endupdatescript
    
    #######################################################

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris front06
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx06
    with dissolve

    n "Neus se encuentra completamente sin habla, congelada, temblando, y con la mirada perdida entre lágrimas."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_iris right04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    dad "Os dije que encontraros es solo una cuestión de tiempo,"

    extend " nada más."

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex01

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_iris front03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx01
    with dissolve

    p "Neus..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex001

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_iris left02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx02
    with dissolve

    dad "Es verdad,"

    extend " que ahora tu nombre es Neus."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex002

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris left03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    dad "Nieve en {a=https://es.wikipedia.org/wiki/Idioma_catalán}catalán{/a}."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris right02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    dad "No se te ocurrió un nombre más original,"

    extend " ¿Verdad?"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_iris front02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx01
    with dissolve

    p "¿De qué estás hablando?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex001

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris left03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx03
    with dissolve

    dad "No se llama {a=https://www.name-doctor.com/name-neus-meaning-of-neus-23945.html}Neus{/a}."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris left04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    dad "Su nombre es {a=https://eu.wikipedia.org/wiki/Elur}{i}Elur{/i}{/a}."


    show neus_exp_iris right04
    $ nteye = 4
    call neus_exp_tears_tears

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows normal

    with dissolve

    dad "Nieve en {a=https://es.wikipedia.org/wiki/Euskera}Euskera{/a}."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show neus_exp_mouth sadbiting_Silentx06
    #show neus_exp_eyes 05
    show neus_exp_iris right05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05
    with dissolve

    ##

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_iris right05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx05

    with fade


    n "Fijas tu mirada en Neus, que sigue completamente en silencio."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_iris front02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx01
    with dissolve

    p "¿Es eso verdad?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_iris right03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "Por supuesto que es verdad,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    dad "pero tranquilo,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "no es lo único en que te ha mentido."

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx02
    with fade

    dad "¿Verdad que no?"

    show neus_exp_mouth sad_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)
    
    dad "{i}Txiki{/i}."

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex01

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyes 05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    p "..."

    menu:

        pt "¿Su nombre es Elur...?"

        "<Defender su cambio de nombre>":
            call p_Help
            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyes 01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            p "Es normal que se cambie de nombre si sabe que la estás buscando."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyes 02
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows serious
            with dissolve

            p "Además,"

            extend " lo único que hizo fue traducirlo,"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious

            show neus_exp_mouth happy_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx03
            with dissolve

            p "a eso no lo llamo mentir."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious

            show neus_exp_mouth sad_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx02
            with dissolve

            dad "Caray,"

            extend " caray,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sad_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx02
            with dissolve

            dad "con mi niño..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sad_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with dissolve

            dad "Defendiendo a su amada..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sad_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx03
            with dissolve

            jump an05_Pedrera_lover
            #dad "¿Pero es realmente ella tú única amante?"

        "¿Por qué no me dijiste tu nombre real?":
            call p_Help
            $pl.ch_pts("np",-1)

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with fade

            ne "..."

            show neus_exp_mouth sad_Talkingx04
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "Te lo tendría que haber contado esta noche,"

            show neus_exp_mouth sad_Talkingx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "pero no pensé que fuera tan importante."

            if night05_Interrogation_YourFathersPower_Cond:

                show neus_exp_mouth sad_Talkingx06
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris right03
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Especialmente cuando sabes que me estoy escondiendo de mi padre."

                show neus_exp_mouth sad_Silentx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx05
                with dissolve

            else:

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris right02
                show neus_exp_eyebrows sadx04
                with dissolve

                ne "Además,"

                extend " las preguntas me las quisiste hacer tú..."

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx05
                with dissolve

                menu:

                    pt "Porque es muy común preguntarle a alguien, oye, ¿me diste bien tu nombre?"

                    "¡¿Esa es tu excusa?!":
                        call p_Help
                        $pl.ch_pts("np",-3)

                        $ ped_neusname_angry = True

                        show neus_exp_mouth sadbiting_Silentx02
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris front02
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "..."

                    "¿Y querías que te preguntara también por el nombre?":
                        call p_Help
                        $pl.ch_pts("np",-1)

                        $ ped_neusname_angry = True

                        show neus_exp_mouth sad_Talkingx003
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx02
                        with dissolve

                        ne "No..."

                        show neus_exp_mouth sad_Talkingx05
                        $ nteye = 1
                        call neus_exp_tears_tears
                        show neus_exp_iris right01
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        ne "Simplemente no pensé que te iba a importar tanto..."

                    "...":
                        call p_Help

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx05
                with dissolve

                ne "..."

            menu:

                pt "¿No confía lo suficiente en mí?"

                "Me hubiera gustado que me lo contaras, por lo menos, cuando estábamos solos.":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth sadbiting_Silentx03
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris front01
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sad_Talkingx03
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris right03
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "Lo siento,"

                    show neus_exp_mouth sad_Talkingx05
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris right02
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    ne "no pensé que fuera tan importante,"

                    show neus_exp_mouth sad_Talkingx04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx05
                    with dissolve

                    ne "al fin y al cabo,"

                    extend " solo traducí el nombre..."

                    show neus_exp_mouth sadbiting_Silentx04
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris right04
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    menu:

                        "Pero eso demuestra que confías poco en mi.":
                            call p_Help

                            if night05_Interrogation_YourFathersPower_Cond:
                                $pl.ch_pts("np",-1)

                                show neus_exp_mouth sad_Talkingx08
                                $ nteye = 2
                                call neus_exp_tears_tears
                                show neus_exp_iris front02
                                show neus_exp_eyebrows angryx03
                                with dissolve

                                ne "¡Te respondí sobre mi padre!"

                            if night05_Interrogation_WhatAboutYourMother_Cond:

                                show neus_exp_mouth sad_Talkingx07
                                $ nteye = 3
                                call neus_exp_tears_tears
                                show neus_exp_iris front03
                                show neus_exp_eyebrows angryx02
                                with dissolve

                                ne "Te hable de mi madre;"

                            if night05_Interrogation_FamilySect_Cond:

                                show neus_exp_mouth sad_Talkingx06
                                $ nteye = 1
                                call neus_exp_tears_tears
                                show neus_exp_iris front01
                                show neus_exp_eyebrows angryx01
                                with dissolve

                                ne "Te hablé de mi familia;"

                            if night05_Interrogation_InLoveWithAMan_Cond:

                                show neus_exp_mouth sad_Talkingx06
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris front04
                                show neus_exp_eyebrows sadx01
                                with dissolve

                                ne "Te abrí mi corazón..."

                            if (
                                night05_Interrogation_WhatAboutYourMother_Cond == True or
                                night05_Interrogation_FamilySect_Cond == True or
                                night05_Interrogation_InLoveWithAMan_Cond == True
                                ):

                                show neus_exp_mouth sad_Talkingx07
                                $ nteye = 3
                                call neus_exp_tears_tears
                                show neus_exp_iris front03
                                show neus_exp_eyebrows sadx04
                                with dissolve

                                ne "Te he contado todo lo que he podido..."

                                show neus_exp_mouth sadbiting_Silentx05
                                $ nteye = 1
                                call neus_exp_tears_tears
                                show neus_exp_iris left01
                                show neus_exp_eyebrows sadx01
                                with dissolve

                                dad "¿Seguro que se lo has contado todo?"

                            else:

                                $pl.ch_pts("np",-3)

                                show neus_exp_mouth sad_Talkingx06
                                $ nteye = 3
                                call neus_exp_tears_tears
                                show neus_exp_iris front03
                                show neus_exp_eyebrows angryx01
                                with dissolve

                                ne "Si no te he contado más cosas,"

                                show neus_exp_mouth sad_Talkingx05
                                $ nteye = 4
                                call neus_exp_tears_tears
                                show neus_exp_iris front04
                                show neus_exp_eyebrows sadx02
                                with dissolve

                                ne "es porque no me lo has preguntado esta noche."

                                show neus_exp_mouth sadbiting_Silentx06
                                $ nteye = 0
                                call neus_exp_tears_tears
                                show neus_exp_iris left00
                                show neus_exp_eyebrows normal
                                with dissolve

                                dad "¿Seguro que se lo habrías contado todo?"

                                show neus_exp_mouth sadbiting_Silentx07
                                $ nteye = 2
                                call neus_exp_tears_tears
                                show neus_exp_iris front02
                                show neus_exp_eyebrows sadx05
                                with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Talkingx003
                            $ nteye = 4
                            call neus_exp_tears_tears
                            show neus_exp_iris right04
                            show neus_exp_eyebrows sadx03
                            with dissolve

                            ne "Yo..."

                            show neus_exp_mouth sadbiting_Silentx06
                            $ nteye = 5
                            call neus_exp_tears_tears
                            show neus_exp_iris right05
                            show neus_exp_eyebrows sadx05
                            with dissolve

                        "...":
                            call p_Help

                "...":
                    call p_Help

            jump an05_Pedrera_lover
                #dad "¿Pero es realmente ella tú única amante?"

        "...":

            call p_Help

            jump an05_Pedrera_lover
                #dad "¿Pero es realmente ella tú única amante?"

######################################################################
######################################################################

label an05_Pedrera_lover:

    ######################################################################
######################################################################
        ## CONDITIONALS

    if ((night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_family_met_Cond or room_01_cemetery_mother_met_Cond) and
        room_02_child_room_but_kid_Cond and
        room_03_marriage_far_woman_Cond
        ):

        $ room_3doors_met = True

    if (
        morning04_DidacHotforyou_Cond or 
        aftermorning04_FittingRoom_ButtocksDickOver or 
        aftermorning04_FittingRoom_ButtocksDickOverMasturbate or 
        aftermorning04_FittingRoom_FuckherConsent or 
        morning04_Shopping_didaccum_Cond or
        morning04_Shopping_didaccumANAL_Cond or
        morning04_Shopping_youcum_Cond
        ):
        $ day04_Didac_Foreplay = True

    if (
        aftermorning05_Deepsea_Fuck_PussyCOND_Cond or
        aftermorning05_Deepsea_Fuck_PussyRAW_Cond or
        aftermorning05_Deepsea_Fuck_AnalRAW_Cond or
        beach_sex_MC_Fucking_02_Cond
        ):
        $ day05_BeachDidacSex = True

    #### These should be deleted in the future:

    if (morning05_DidacSex_Pussy_Cond and morning05_DidacSex_UsingCondom_Cond == False):
        $ morning05_DidacSex_Pussy_Unsafe_Cond = True


    if(aftermorning05_AfterDeepsea_WakeUp_Sex and aftermorning05_AfterDeepsea_PublicSex_Condom_Use_Cond == False):
        $ aftermorning05_AfterDeepsea_PublicSex_RAW_Cond = True

    #####

    if (
        morning05_DidacSex_Pussy_Unsafe_Cond or
        aftermorning05_Deepsea_Fuck_PussyRAW_Cond or
        aftermorning05_AfterDeepsea_PublicSex_RAW_Cond
        ):
        $ DidacSex_Unsafe = True # Without Condom

    if (
        aftermorning04_FittingRoom_FuckherConsent or
        (afternight04_Pussy_dick_med_Speed_0_Done > 1 or
        afternight04_Pussy_dick_med_Speed_0_Rape_Done > 1) or
        morning05_missionary_cond_01 or
        day05_BeachDidacSex
        ):

        $ DidacSex_Vaginal = True # You had Intercourse With Didac.

    if (
        afternight04_sexbattle_started and
        (afternight04_Pussy_dick_med_Speed_0_Done == 0 and
        afternight04_Anal_dick_med_Speed_0_Done == 0 and
        afternight04__MMouth_dick_Done) and
        DidacSex_Vaginal == False
        ):

        $ DidacSex_JustForePlay = True # You had no ORIFICE (Vaginal-Anal-Oral) penetration with Didac

    if (
        day04_Didac_Foreplay == False and
        afternight04_sexbattle_started == False and
        DidacSex_Vaginal == False
        ):

        $ DidacSex_NotEvenForePlay = True

    if (
        DidacMCPregnant or 
        DidacOKUPregnant or 
        aftermorning05_DidacFar_01_Cond
        ):
        $ DidacPregnant = True # Didac Pregnant by anyone

    if (afternight04_Park_HelpDidacPolice_Cond or 
        afternight04_Park_AbandonDidacPolice_Cond):
        $ DidacOKUPregnant_YouKnowIt = True

###
    
    if (
        day04_Didac_Foreplay or 
        afternight04_sexbattle_started or 
        morning05_missionary_cond_01 or
        day05_BeachDidacSex or
        FuckM_Start_Cond or 
        FuckH_Start_Cond
        ):

        $ NeusCuckolded = True # Neus had been cuckolded.

    if (
        afternight04_sexbattle_started or 
        morning05_missionary_cond_01 or
        day05_BeachDidacSex
        ):

        $ NeusCuckolded_Sexually_Didac = True # Neus had been cuckolded with Didac.

    if (
        afternight04_sexbattle_started or 
        morning05_missionary_cond_01 or
        day05_BeachDidacSex or
        FuckM_Start_Cond or 
        FuckH_Start_Cond
        ):

        $ NeusCuckolded_Sexually = True # Neus had been cuckolded.

    ######################################################################
######################################################################

    menu:

        pt "¿Debería seguir llamándola Neus? ¿O es mejor que a partir de ahora la llame Elur?"

        "Seguir llamándola Neus.":
            call p_Help
            pass

        "Llamarla Elur a partir de ahora.":
            call p_Help
            $ neusname = "Elur"

###
    
    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    if NeusCuckolded == True:

        if music_play != "airPrelude":
            play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "airPrelude"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx02
        with fade

        dad "¿Pero es realmente ella tú única amante?"

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows surprisex001
        with dissolve

    else:

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows normal
        with fade

    if NeusCuckolded == True:
        with dissolve

    else:
        with fade

    p "..."

###
    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    # show m_exp_mouth happy_Talkingx09
    # show m_exp_eyes 01
    # show m_exp_piris right01
    # show m_exp_eyebrows suspiciousx01

    # show neus_exp_mouth sadbiting_Silentx06
    # $ nteye = 5
    # call neus_exp_tears_tears
    # show neus_exp_iris right05
    # show neus_exp_eyebrows sadx05

    if DidacPregnant == True:

        jump an05_Pedrera_DidacPregnant

    else:

        if NeusCuckolded:

            $pl.ch_pts("np",-3)

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex002

            show neus_exp_mouth sad_Silentx03
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx01
            with fade

            dad "No parece que sea realmente tu única distracción..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sad_Silentx02
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            dad "¿Me equivoco?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sad_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

        else:

            $pl.ch_pts("np",3)

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001

            show neus_exp_mouth sad_Silentx03
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows surprisex01
            with fade

            dad "Eres un chico bastante fiel,"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth happy_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx01
            with dissolve

            dad "eso te lo debo reconocer."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01

            show neus_exp_mouth happy_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            dad "Aunque si me lo preguntas a mí,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth happy_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx03
            with dissolve

            dad "yo lo llamaría más bien estupidez."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx02

            show neus_exp_mouth happy_Silentx06
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx02
            with dissolve

        p "..."

        jump an05_Pedrera_BeenInYourMind

            # p "¿Cómo sabes...?"
            # dad "Por favor,"
            # extend " ahorrémonos preguntas estúpidas."
            # dad "He estado en tus sueños,"
            # extend " en tu mente;"
            # dad "sé más de lo que imaginas."

label an05_Pedrera_DidacPregnant:

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious

    show neus_exp_mouth sad_Silentx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx02
    with fade

    dad "Hablando de mentiras;"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows normal

    show neus_exp_mouth sad_Silentx02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "entre los jugos de tu amigo con sus recientes tetas,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows serious

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "he encontrado un sabor..."

    if DidacMCPregnant:

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "familiar."

    else:

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve

        dad "peculiar."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with dissolve

    dad "¿No sabrás por casualidad a qué me refiero,"

    extend " ¿Verdad?"

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "..."

    menu:

        pt "¿Qué se supone que debo responder?"

        "<Reconocer que tuviste sexo con Dídac, pero que usaste condón todo el tiempo>" if DidacSex_Vaginal:

            call p_Help
            $pl.ch_pts("np",-6)

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows normal
            with dissolve

            p "Sí,"

            extend " es cierto."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            p "Lo hice con Dídac."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            p "Pero nunca me corrí dentro de él."

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with fade

            dad "Hmm..."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show neus_exp_mouth sad_Silentx07
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            pause 0.2

            show neus_exp_mouth sad_Silentx08
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx07
            with Dissolve(0.5)

            pause 0.2

            if DidacSex_Vaginal:

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with fade

                dad "¿Estás seguro de ello?"

                extend " mi niño."

                #Le llama hijo?

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                p "¡Por supuesto!"

                show m_exp_mouth happy_Silentx02
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                p "Si en alguna ocasión lo he hecho sin condón,"

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                p "me he corrido siempre fuera."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx04
                with fade

                ne "..."

            else:

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with fade

                dad "Hmmm..."

            call an05_Pedrera_DPreg
                # dad "Ayer por la noche,"

            jump an05_Pedrera_BeenInYourMind
                # p "¿Cómo sabes...?"
                # dad "Por favor,"
                # extend " ahorrémonos preguntas estúpidas."

        "<Reconocer que tuviste sexo con Dídac, pero que nunca fue vaginalmente>" if NeusCuckolded_Sexually_Didac: #rollback
            call p_Help
            $pl.ch_pts("np",-3)

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02

            show neus_exp_mouth sad_Silentx07
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with dissolve

            p "Quizás he jugueteado con él..."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal

            show neus_exp_mouth sad_Silentx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx01
            with dissolve

            p "¡Pero nunca lo he penetrado!"

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            if DidacSex_Vaginal:

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with fade

                dad "¿De verdad?"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex002
                with dissolve

                dad "¿Realmente crees que puedes mentirme?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx01
                with dissolve

                p "¡No estoy mintiendo!"

                if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

                    $pl.ch_pts("np",-2)

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx02
                    with dissolve

                    dad "Pero si se la metiste entera..."

                    if afternight04_Pussy_dick_deep_Speed_3_Done > 0:

                        $pl.ch_pts("np",-3)

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows angryx03
                        with dissolve

                        dad "Y además le diste bien duro."

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    $pl.ch_pts("np",-2)

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx04
                    with dissolve

                    dad "Sin mencionar el agujero de atrás..."

                    if afternight04_Anal_dick_deep_Speed_0_Done > 0:

                        $pl.ch_pts("np",-2)

                        show m_exp_mouth happy_Talkingx11
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx05
                        with dissolve

                        dad "que hasta el fondo se la metiste."

                        if afternight04_Anal_dick_deep_Speed_3_Done > 0:

                            $pl.ch_pts("np",-3)

                            show m_exp_mouth happy_Talkingx12
                            show m_exp_eyes 00
                            show m_exp_piris front00
                            show m_exp_eyebrows normal
                            with dissolve

                            dad "A toda leche..."

                if day05_BeachDidacSex:

                    $pl.ch_pts("np",-3)

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "Tampoco es que en la playa jugarais demasiado a la pelota..."

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    dad "Aunque supongo que eso dependerá de lo que entendamos por pelotas..."

                if aftBeach_DidacSex:

                    $pl.ch_pts("np",-6)

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx01
                    with dissolve

                    dad "Aunque no hay nada como volver a casa,"

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows sadx02
                    with dissolve

                    dad "después de disfrutar del calor de la playa,"

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx02
                    with dissolve

                    dad "para seguir follando como conejos en la comodidad y privacidad del hogar."

                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "Hmm..."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                p "¡Eso no es cierto!"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows normal
                with dissolve

                dad "¿Tampoco es cierto que llevaba todo el día masturbándose pensando en tu polla?"

                if afternight04_sexbattle_started:

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "Y que al final aceptaste,"

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "al verla desnuda a oscuras en el salón de vuestro diminuto piso,"

                    show m_exp_mouth sad_Talkingx008
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "para luego tirarte al sofá,"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    dad "y montarse encima de ti."

                    show m_exp_mouth happy_Silentx07
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                else:

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "Y que al final la rechazate,"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    dad "porque pensaste que podrías resistir la tentación..."

                    if day05_BeachDidacSex:

                        $pl.ch_pts("np",-6)

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        dad "Pero en la playa,"

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        dad "desnudos,"

                        extend " mojados por el sudor y el agua,"

                        show m_exp_mouth sad_Talkingx005
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows sadx01
                        with dissolve

                        dad "el calor..."

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        dad "Eso fue más difícil de resistir,"

                        show m_exp_mouth happy_Talkingx07
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        dad "¿Verdad?"

                        show m_exp_mouth happy_Silentx06
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                    #p "..."

                p "..."

            else:

                if afternight04_Anal_dick_med_Speed_0_Done > 0 or afternight04__MMouth_dick_Done > 0:

                    $pl.ch_pts("np",-3)

                    show m_exp_mouth sad_Talkingx005
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "Quizás no vaginalmente..."

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "Pero hay otros orificios en su cuerpo..."

                    if (
                        (afternight04__Anal_dick_deep_Failed > afternight04__Anal_dick_deep_Success) or
                        (afternight04__Anal_dick_med_Failed > afternight04__Anal_dick_med_Success)
                        ):

                        $pl.ch_pts("np",-5)

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        dad "Aunque le resultase más doloroso que placentero,"

                        if afternight04__Anal_dick_deep_Done > 0:

                            $pl.ch_pts("np",-3)

                            show m_exp_mouth happy_Talkingx10
                            show m_exp_eyes 01
                            show m_exp_piris front01
                            show m_exp_eyebrows surprisex001
                            with dissolve

                            dad "cuando se la metiste entera por detrás..."

                        elif afternight04__Anal_dick_med_Done > 0:

                            show m_exp_mouth happy_Talkingx09
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                            dad "cuando se la metiste por detrás..."

                    if afternight04__MMouth_dick_Done > 0:

                        show m_exp_mouth happy_Talkingx07
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows normal
                        with dissolve

                        dad "¿Te imaginabas hace cuatro días que tendrías tu polla en su boca?"

                        if afternight04__MMouth_dick_Success > 0:

                            $pl.ch_pts("np",-3)

                            show m_exp_mouth happy_Talkingx06
                            show m_exp_eyes 03
                            show m_exp_piris front03
                            show m_exp_eyebrows suspiciousx01
                            with dissolve

                            dad "Siendo saboreada por su juguetona lengua."

                            show m_exp_mouth sad_Talkingx04
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows surprisex001
                            with dissolve

                            dad "Por mucho que diga,"

                            show m_exp_mouth sad_Talkingx06
                            show m_exp_eyes 04
                            show m_exp_piris right04
                            show m_exp_eyebrows normal
                            with dissolve

                            dad "disfrutó de tu polla mucho más de lo que se imaginaba."

                            show m_exp_mouth happy_Talkingx07
                            show m_exp_eyes 04
                            show m_exp_piris front04
                            show m_exp_eyebrows angryx01
                            with dissolve

                            dad "¿Me equivoco...?"

                        else:

                            $pl.ch_pts("np",-1)

                            show m_exp_mouth happy_Talkingx08
                            show m_exp_eyes 02
                            show m_exp_piris front02
                            show m_exp_eyebrows surprisex01
                            with dissolve

                            dad "Aunque por desgracia solo recibiste su mordisco."

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                    $pl.ch_pts("np",-3)


                # Not Vaginal, Not Anal, not Oral sex.

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Hmm..."

                if FuckM_Start_Cond or FuckH_Start_Cond:

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "Quizás no te hayas querido follar a tu compañero de piso,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    dad "Pero desde luego,"

                    if FuckM_Start_Cond and FuckH_Start_Cond:

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows angryx01
                        with dissolve

                        dad "no tuviste ningún reparo en follarte a esta rubia tetuda,"

                        show m_exp_mouth happy_Talkingx09
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx02
                        with dissolve

                        dad "y a ese oriental moreno con tetas."

                    elif FuckH_Start_Cond:

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows angryx01
                        with dissolve

                        dad "no tuviste ningún reparo en follarte a ese oriental moreno con tetas."

                    if FuckM_Start_Cond:

                        # FOR FUTURE, I still have to make the PASSIVE and ACTIVE roles and the sex scene.

                        show m_exp_mouth sad_Talkingx004
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        dad "Aunque eso de que te desvirgara el trasero,"

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        dad "no debió de resultarte muy varonil..."

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    dad "¿Me equivoco?"

                elif afternight04_sexbattle_started:

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "Aunque bien que dejaste que se te montara encima de ti."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    p "Sí,"

                    extend " es verdad que se montó encima de mi,"

                    $pl.ch_pts("np",2)

                    show m_exp_mouth sad_Silentx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    p "pero no follé con él en ningún momento."

                    $ Pedrera_char_Cond = "TxellNeus"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows serious

                    show neus_exp_mouth happy_Silentx04
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris front03
                    show neus_exp_eyebrows sadx01
                    with fade

                    dad "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Silentx07
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows suspiciousx02
                    with fade

                    dad "En eso debo darte la razón."

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve

                

                else: # No sex, no minigame... is it possible?

                    "No sex with Didac or Minigame? Is it possible? This shouldn't be readable. 32984"

                    # NOT FINISHED

            call an05_Pedrera_DPreg
                # dad "Ayer por la noche,"

            # NOT FINISHED

            jump an05_Pedrera_BeenInYourMind
                    # p "¿Cómo sabes...?"
                    # dad "Por favor,"
                    # extend " ahorrémonos preguntas estúpidas."

        "<Decirle que nunca has tenido sexo con él>":
            call p_Help

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with fade

            p "[neusname],"

            extend " nunca he tenido sexo con Dídac."

            show neus_exp_mouth happybiting_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with dissolve

            if DidacSex_Vaginal:

                $pl.ch_pts("np",-2)

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows normal
                with dissolve

                dad "Suenas hasta convincente."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows serious
                with dissolve

                p "¡Porque es la verdad!"

                if DidacSex_Unsafe:

                    $pl.ch_pts("np",-3)

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 0
                    call neus_exp_tears_tears
                    show neus_exp_iris left00
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    dad "Hasta sin condón se la metiste,"

                    show neus_exp_mouth sad_Silentx08
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris front01
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    dad "¿no es verdad?"

                    show neus_exp_mouth sad_Silentx09
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx04
                    with dissolve

                    p "No eres más que un monstruo mentiroso."

                    show neus_exp_mouth sadbiting_Silentx07
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows sadx05
                    with Dissolve(0.5)

                else:

                    show neus_exp_mouth sad_Silentx05
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx01
                    with Dissolve(0.5)

                dad "Yo seré un monstruo,"

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex02
                with fade

                dad "pero no soy tan mentiroso como tú."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx02
                with dissolve

                p "..."

            elif (afternight04_Anal_dick_med_Speed_0_Done or afternight04__MMouth_dick_Done) > 0:

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows normal
                with dissolve

                if afternight04_Anal_dick_med_Speed_0_Done > 0:

                    $pl.ch_pts("np",-3)

                    dad "¿Si te lo follaste analmente no cuenta?"

                elif afternight04__MMouth_dick_Done > 0:

                    $pl.ch_pts("np",-2)

                    dad "¿Si le has follado la boca no cuenta?"

                    if afternight04_CumInThroat > 0:

                        $pl.ch_pts("np",-3)

                        dad "Si hasta te corriste en su garganta..."

                    elif afternight04_CumInMouth > 0:

                        $pl.ch_pts("np",-2)

                        dad "Si hasta te corriste en su boca..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx01
                with dissolve

                p "..."

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris right03
                show neus_exp_eyebrows sadx02
                with Dissolve(0.5)

                dad "Quizás ya tenías incluso fantasías sexuales con él,"

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with Dissolve(0.5)

                dad "cuando no tenía este cuerpo de mujer..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex01
                with fade

                p "El enfermo eres tú."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex001
                with dissolve

                dad "Quizás sea un enfermo,"

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 00
                show m_exp_piris front00
                show m_exp_eyebrows angryx01
                with dissolve

                dad "pero por lo menos no soy un mentiroso como tú."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx02
                with dissolve

            elif day04_Didac_Foreplay:

                $pl.ch_pts("np",2)

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows normal
                with dissolve

                dad "Quizás no la has penetrado,"

                show neus_exp_mouth sadbiting_Silentx01
                $ nteye = 8
                call neus_exp_tears_tears
                show neus_exp_iris front08
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "pero no me puedes negar que has jugueteado un poco con ella,"

                show neus_exp_mouth happybiting_Silentx02
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "¿o debería decir él?"

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows suspiciousx02

                p "..."

            else:

                show neus_exp_mouth sad_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows normal
                with dissolve

                dad "Hmmm..."

                $pl.ch_pts("np",4)

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Siletx04
                show m_exp_eyes 05
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sad_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows suspiciousx01
                with fade

                dad "..."

                show m_exp_mouth sad_Siletx06
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows suspiciousx02

                show neus_exp_mouth happy_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx03
                with dissolve

                ne "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sadbiting_Siletx06
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious

                dad "..."

            if (DidacSex_JustForePlay or DidacSex_NotEvenForePlay) == True:

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx05
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx02
                with fade

                ne "Si la volviste la ninfómana que es,"

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sad_Talkingx07
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows angryx03
                with fade

                ne "es todo un prodigio que consiguiera no tener sexo con él."

                show neus_exp_mouth sad_Talkingx08
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "Cualquiera hubiera aprovechado la situación,"

                show neus_exp_mouth sad_Talkingx005
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx01
                with dissolve

                ne "y no se hubiera quedado satisfecho solo con los preliminares."

                show neus_exp_mouth happy_Talkingx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "Es algo que estoy segura que Dídac te agradecerá,"

                extend " [protname]."

                show neus_exp_mouth happy_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "..."

                show neus_exp_mouth happy_Talkingx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx02
                with dissolve

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx01
                with fade

                dad "Hmmph..."

                if DidacPregnant:

                    if DidacMCPregnant:

                        aj "Didac Pregnant By you? That makes no sense here... Error. This SHOULDN'T BE READABLE. 4863875"

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex001

                    dad "Quizás sí,"

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious

                    dad "o quizás no..."

                    show m_exp_mouth happy_Silentx07
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01

                    pt "¿De qué está hablando?"

            call an05_Pedrera_DPreg
                # dad "Ayer por la noche,"

            jump an05_Pedrera_BeenInYourMind
                    # p "¿Cómo sabes...?"
                    # dad "Por favor,"
                    # extend " ahorrémonos preguntas estúpidas."



label an05_Pedrera_DPreg:

    # Can Didac get pregnant at the beach?

    if music_play != "nervous":
        play music "audio/music/kevinmacleod/creepy/nervous.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nervous"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    if DidacPregnant:

        if DidacMCPregnant or DidacOKUPregnant:

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Ayer por la noche,"

        if DidacMCPregnant:

            $pl.ch_pts("np",-8)

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "cuando Dídac te puso el último condón,"

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "no lo notaste algo..."

            extend " ¿Diferente?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            p "Te refieres a que..."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx04
            with dissolve

            dad "Oh sí..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Tu amigo de la infancia está empezando a gestar a tu pequeño retoño."

        elif DidacOKUPregnant:

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "cuando rechazaste hacerlo con él,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "se fue de casa,"

            extend " ¿Verdad?"

            if DidacOKUPregnant_YouKnowIt:

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "Y lo seguiste..."

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with dissolve

                dad "¿Qué fue lo que ocurrió?"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Por que estuviste ahí para ver lo que pasó..."

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                dad "¿Me equivoco?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                p "..."

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                dad "Y sin embargo,"

                extend " no hiciste nada para detenerlo."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows serious
                with dissolve

                ne "..."

            else:

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                dad "Pero no lo seguiste."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows normal
                with dissolve

                dad "Dejaste que se fuera de casa yendo más caliente que un cura en una guardería."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "Y pasó lo que sabías que iba a pasar."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

                ne "..."

                menu:

                    "¡Fue él quien decidió largarse!":
                        call p_Help
                        $pl.ch_pts("np",-6)

                        show m_exp_mouth sad_Talkingx004
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        dad "Ohh..."

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "Sí."

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx03
                        with dissolve

                        dad "De eso no me cabe la menor duda."

                        show m_exp_mouth sad_Talkingx003
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows sadx01
                        with dissolve

                        dad "¿Pero no te pidió ayuda primero?"

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "¿No te suplicó como nunca había hecho en su vida, que le ayudaras?"

                        show m_exp_mouth sad_Talkingx07
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        dad "¿Realmente no podías hacer absolutamente nada por él?"

                        show m_exp_mouth sad_Talkingx006
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows suspiciousx02
                        with dissolve

                        dad "¿No te habría intentado ayudar si hubiera estado en tu lugar?"

                        show m_exp_mouth happy_Silentx06
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "Hmmm..."

                        show m_exp_mouth happy_Talkingx07
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex001
                        with dissolve

                        dad "Quizás mejor que pienses de ese modo."

                    "No quería follarme a Dídac, tampoco me dejó muchas más opciones.":
                        call p_Help
                        $pl.ch_pts("np",-4)

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        dad "¿Es eso verdad Txiki?"

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 02
                        show m_exp_piris right02
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "¿Realmente no podía haber hecho absolutamente nada por él?"

                        show m_exp_mouth happy_Silentx06
                        show m_exp_eyes 05
                        show m_exp_piris right05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        pause 0.2

                        $ Pedrera_char_Cond = "NeusClose"
                        call Pedrera_char_lab

                        show neus_exp_mouth sadbiting_Silentx06
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx06
                        with fade

                        ne "..."

                        $ Pedrera_char_Cond = "TxellClose"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Talkingx04
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex001
                        with fade

                        dad "Lo que me querida hija no es capaz de decirte,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspicious01
                        with dissolve

                        dad "es que si hubieras jugueteado un poco con él,"

                        show m_exp_mouth sad_Talkingx06
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows surprisex002
                        with dissolve

                        dad "sin llegar a lo sexual;"

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 03
                        show m_exp_piris front03
                        show m_exp_eyebrows sadx01
                        with dissolve

                        dad "quizás hubiera sido suficiente para calmar sus ansias,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "y haber evitado tenir que salir a la calle,"

                        extend " y quedarse preñada en el porceso."

                        $ Pedrera_char_Cond = "TxellNeus"
                        call Pedrera_char_lab

                        show m_exp_mouth sad_Talkingx006
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        show m_exp_eyebrows surprisex002

                        show neus_exp_mouth sadbiting_Silentx04
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris left02
                        show neus_exp_eyebrows sadx01
                        with fade

                        dad "¿Pero qué va a saber ella?"

                        show m_exp_mouth sad_Talkingx006
                        show m_exp_eyes 04
                        show m_exp_piris right04
                        show m_exp_eyebrows serious

                        show neus_exp_mouth sadbiting_Silentx06
                        $ nteye = 3
                        call neus_exp_tears_tears
                        show neus_exp_iris left03
                        show neus_exp_eyebrows sadx03
                        with dissolve

                        dad "Al fin y al cabo,"

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 03
                        show m_exp_piris right03
                        show m_exp_eyebrows angryx01

                        show neus_exp_mouth sadbiting_Silentx07
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris front04
                        show neus_exp_eyebrows sadx04
                        with dissolve

                        dad "fue ella quien lo convirtió en mujer,"

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows surprisex001

                        show neus_exp_mouth sad_Silentx07
                        $ nteye = 3
                        call neus_exp_tears_tears
                        show neus_exp_iris right03
                        show neus_exp_eyebrows sadx05
                        with dissolve

                        dad "tú no tienes ninguna culpa."

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows angryx01

                        show neus_exp_mouth sad_Silentx08
                        $ nteye = 4
                        call neus_exp_tears_tears
                        show neus_exp_iris right04
                        show neus_exp_eyebrows sadx06
                        with dissolve

                        dad "¿Verdad?"

                        $ Pedrera_char_Cond = "TxellClose"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx03
                        with fade

                        p "..."
        else:

            aj "Pregnant by someone else, work in progress."

            # FOR FUTRE WIP

            # Can Didac get pregnant at the beach?

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Espero que no eches de menos su antigua forma masculina y musculada,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows surprisex002
        with dissolve

        dad "porque ya no la volverás a ver nunca más."

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        p "..."

        show m_exp_mouth happy_Silentx08
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows angryx02
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "NeusClose"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx06
        with fade

        ne "..."

    else:

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "Hmmm..."

        # Dídac is not pregnant.

    return


label an05_Pedrera_BeenInYourMind:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with fade

    p "¿Cómo sabes...?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Por favor,"

    extend " ahorrémonos preguntas estúpidas."

    $ meyesc = "_goat"    

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "He estado en tus sueños,"

    extend " en tu mente;"

    $ meyesc = "_red" 

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "sé más de lo que imaginas."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    p "Eres tú el que se me aparecía en sueños con esos ojos rojos."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Aún lo dudas?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    if morning03_Meritxell_Phonenumber_Accepted:

        p "Fuiste tú quien me dio el número de teléfono de Meritxell,"

        show m_exp_mouth happy_Silentx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex001
        with dissolve

        p "cuando te vi en la escuela con estos mismos ojos rojos,"

        extend " ¿Verdad?"

    else:

        p "Fuiste tú el que en realidad me llamó guapo,"

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows serious
        with dissolve

        p "en el pasillo de la escuela cuando estabas en este mismo cuerpo."

        p "¿Verdad?"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Así es."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex01
    with dissolve

    p "También has sido tú el que me ha pinchado en la nuca esta noche,"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "antes de subir esas escaleras en el parque de atracciones."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "¿Qué fue lo que me delató?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿la estatura de esta rubia?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿sus labios pintados de azul?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "¿la peluca negra barata?"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris down03
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "¿O este par de melones?"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    p "¿Por qué?"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Acaso no es obvio?"

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    $ dad = d_didac
    $ dadname = "Dídac"
    $ deyesc = "_red"
    $ meyesc = ""

    $ Pedrera_char_Cond = "ALL"
    call Pedrera_char_lab

    show m_bodynew naked_rest

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious

    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx06

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01
    with fade

    dad "Mira que par de melones tiene."

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx07

    show neus_exp_mouth sad_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with dissolve

    dad "Ni las de tu compañero de piso se pueden comparar."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx03
    with dissolve

    p "¡Dídac!"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    with dissolve

    p "Tú también..."

    show m_exp_mouth sad_Talkingx01
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Silentx04
    with dissolve

    tx "¿Qué...?"

    show m_bodynew naked_down

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris down01
    show m_exp_eyebrows surprisex001

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    with dissolve

    tx "¡¿Qué está pasando aquí?!"

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex002

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows normal
    show didacf_mouth happy_Silentx06
    with dissolve

    tx "¿[protname]?"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows sadx01

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx05

    show neus_exp_mouth sad_Silentx06
    $ nteye = 8
    call neus_exp_tears_tears
    show neus_exp_iris front08
    show neus_exp_eyebrows sadx04
    with dissolve

    tx "¿¡Neus?!"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx05

    show neus_exp_mouth sad_Silentx04
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "..."

    if NeusCuckolded:

        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx06
        with dissolve

        dad "Te entiendo mi niño,"

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows surprisex01

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows serious
        show didacf_mouth happy_Talkingx05
        with dissolve

        dad "¿Para qué conformarse con una insípida enana de pecho plano?"

        show m_exp_mouth sad_Silentx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows suspiciousx02

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx01
        show didacf_mouth happy_Talkingx07
        with dissolve

        dad "Cuando tienes este doble par de razones mucho más interesantes."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 01
        show m_exp_piris right01
        show m_exp_eyebrows surprisex002

        if afternoon04_TxellMacbaDate:

            show didacf_eyes 03
            show didacf_pupils left03
            show didacf_eyebrows suspiciousx02
            show didacf_mouth happy_Talkingx05
            with dissolve


            dad "Aunque es verdad,"

            extend " que esta rubia tetuda no te lo ha puesto nada fácil..."

        else:

            show didacf_eyes 02
            show didacf_pupils left02
            show didacf_eyebrows suspiciousx01
            show didacf_mouth sad_Talkingx05
            with dissolve


            dad "Aunque no le hayas dado ni una oportunidad a esta rubia de aquí..."

    show m_exp_mouth sad_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx03
    with dissolve

    tx "¡Eres el padre de Neus!"

    show m_exp_mouth sad_Talkingx009
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx03

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Silentx06
    with dissolve

    tx "¡Tú eres quien se me apareció en sueños!"

    show m_exp_mouth sad_Silentx12
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth happy_Talkingx05
    with dissolve

    dad "Chica lista."

    if FuckH_Start_Cond or FuckM_Start_Cond:

        if FuckH_Start_Cond:

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows serious

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Talkingx06
            with dissolve

            dad "Aunque me sorprendió lo que hiciste con ese asiático tetudo..."

        if FuckM_Start_Cond: # FOR FUTURE Depends PASIVE, OR ACTIVE SEX?!

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 01
            show m_exp_piris right01
            show m_exp_eyebrows surprisex01

            show didacf_eyes 02
            show didacf_pupils left02
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Talkingx04
            with dissolve

            dad "También me sorprendió que te dejaras dar por detrás con esta rubia..."

            show m_exp_mouth sadbiting_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01

        else:

            show m_exp_mouth sad_Silentx09
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows angryx01

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx01
        show didacf_mouth happy_Talkingx06
        with dissolve

        dad "¿No será que empiezas a tener dudas sobre tu sexualidad?"

    elif DidacSex_JustForePlay:

        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx04
        with dissolve

        dad "Contentarte con tan poco..."

        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows suspiciousx01
        show didacf_mouth happy_Talkingx05
        with dissolve

        dad "pudiendo haberte follado a estas preciosidades,"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows suspiciousx02
        show didacf_mouth sad_Talkingx005
        with dissolve

        dad "en lugar de la enana de mi {i}Txiki{/i}..."

        show didacf_mouth sad_Talkingx04
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows surprisex001
        with dissolve

        dad "Me decepcionas,"

    if afternight04_sexbattle_started:

        $ Pedrera_char_Cond = "DidacClose"
        call Pedrera_char_lab

        show didacf_mouth sad_Talkingx004
        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows surprisex01
        with fade

        if FuckH_Start_Cond or FuckM_Start_Cond:

            dad "Además,"

        else:

            dad "Al menos,"

        # show didacf_mouth happy_Talkingx05
        # show didacf_eyes 04
        # show didacf_pupils front04
        # show didacf_eyebrows suspiciousx01
        # with dissolve

        extend " disfrutaste de este nuevo compañero con sus nuevas tetas."

        show didacf_mouth sad_Talkingx05
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx01
        with dissolve

        dad "Por mucho que te lo suplicara,"

        show didacf_mouth happy_Talkingx06
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows suspiciousx02
        with dissolve

        dad "¿No te sientes culpable por usarlo?"

        show didacf_mouth happy_Silentx04
        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows normal
        with dissolve

        menu:

            "¡No hice nada que él no quisiera!":
                call p_Help

                $pl.ch_pts("np",-4)

                show didacf_mouth sad_Talkingx002
                show didacf_eyes 08
                show didacf_pupils front08
                show didacf_eyebrows surprisex01
                with dissolve

                dad "Por supuesto que no,"

                show didacf_mouth happy_Talkingx06
                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows surprisex02
                with dissolve

                dad "solo digo que te aprovechaste bien de la situación..."

                show didacf_mouth happy_Silentx07
                show didacf_eyes 04
                show didacf_pupils right04
                show didacf_eyebrows angryx02
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx04
                with fade

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with Dissolve(0.5)

                p "..."

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab

                show didacf_mouth happy_Talkingx04
                show didacf_eyes 05
                show didacf_pupils front05
                show didacf_eyebrows angryx02
                with fade

                dad "¿Verdad que sí?"

            "¡No lo he usado!":

                call p_Help

                if afternight04_Anal_dick_deep_Speed_0_Done > 0:

                    $pl.ch_pts("np",-3)

                    show didacf_mouth sad_Talkingx003
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows sadx01
                    with dissolve

                    dad "Me dirás que después de meterle la polla hasta el fondo de su trasero,"

                    if afternight04_Anal_dick_deep_Speed_3_Done:

                        $pl.ch_pts("np",-3)

                        show didacf_mouth happy_Talkingx06
                        show didacf_eyes 05
                        show didacf_pupils front05
                        show didacf_eyebrows surprisex01
                        with dissolve

                        dad "a toda leche,"

                    if afternight04_Anal_dick_deep_Speed_3_Failed > afternight04_Anal_dick_deep_Speed_3_Success:

                        $pl.ch_pts("np",-4)

                        show didacf_mouth happy_Talkingx08
                        show didacf_eyes 05
                        show didacf_pupils front05
                        show didacf_eyebrows suspiciousx02
                        with dissolve

                        dad "Aunque le doliera más que otra cosa..."

                elif afternight04_Pussy_dick_med_Speed_0_Done > 0:

                    $pl.ch_pts("np",-2)

                    show didacf_mouth sad_Talkingx004
                    show didacf_eyes 04
                    show didacf_pupils front04
                    show didacf_eyebrows surprisex01
                    with dissolve

                    dad "Me dirás que después de meterle la polla hasta el fondo de su concha,"

                    if afternight04_Pussy_dick_deep_Speed_3_Done:

                        $pl.ch_pts("np",-3)

                        show didacf_mouth happy_Talkingx05
                        show didacf_eyes 05
                        show didacf_pupils front05
                        show didacf_eyebrows surprisex01
                        with dissolve

                        dad "a toda leche,"

                    if afternight04_Pussy_dick_deep_Speed_3_Failed > afternight04_Pussy_dick_deep_Speed_3_Success:

                        $pl.ch_pts("np",-3)

                        show didacf_mouth happy_Talkingx04
                        show didacf_eyes 05
                        show didacf_pupils front05
                        show didacf_eyebrows surprisex01
                        with dissolve

                        dad "Aunque le doliera más que otra cosa..."

                else:

                    $pl.ch_pts("np",-2)

                    show didacf_mouth sad_Talkingx003
                    show didacf_eyes 08
                    show didacf_pupils front08
                    show didacf_eyebrows surprisex01
                    with dissolve

                    dad "Me dirás que después de lo que hiciste con él ayer por la noche,"

                if afternight04__MMouth_dick_Done > 0:

                    $pl.ch_pts("np",-1)

                    show didacf_mouth happy_Talkingx05
                    show didacf_eyes 04
                    show didacf_pupils front04
                    show didacf_eyebrows surprisex01
                    with dissolve

                    dad "Metiéndosela en la boca,"

                    show didacf_mouth happy_Talkingx06
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows suspiciousx01
                    with dissolve

                    dad "a pesar de que sabías que era algo que aparentemente le disgustaba tanto..."

                ## CUM

                if afternight04_CumInThroat > 1:

                    $pl.ch_pts("np",-3)

                    show didacf_mouth happy_Talkingx07
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows angryx01
                    with dissolve

                    dad "y de correrte [afternight04_CumInThroat] veces en su garganta;"

                elif afternight04_CumInMouth > 1:

                    $pl.ch_pts("np",-2)

                    show didacf_mouth happy_Talkingx06
                    show didacf_eyes 04
                    show didacf_pupils front04
                    show didacf_eyebrows angryx01
                    with dissolve

                    dad " y correrte [afternight04_CumInMouth] veces en su boca;"

                elif afternight04_CumInThroat == 1:

                    $pl.ch_pts("np",-2)

                    show didacf_mouth happy_Talkingx05
                    show didacf_eyes 04
                    show didacf_pupils front04
                    show didacf_eyebrows angryx01
                    with dissolve

                    dad "y de correrte al menos una vez en su garganta;"

                elif afternight04_CumInMouth == 1:

                    $pl.ch_pts("np",-1)

                    show didacf_mouth sad_Talkingx004
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows surprisex01
                    with dissolve

                    dad "y de correrte al menos una vez en su boca;"

                elif mc_body.orgasm == 3:

                    $pl.ch_pts("np",-1)

                    show didacf_mouth sad_Talkingx004
                    show didacf_eyes 05
                    show didacf_pupils front05
                    show didacf_eyebrows surprisex01
                    with dissolve

                    dad " hasta correrte tres veces;,"

                # else:

                #     $pl.ch_pts("np",-1)

                #     show didacf_mouth sad_Talkingx004
                #     show didacf_eyes 05
                #     show didacf_pupils front05
                #     show didacf_eyebrows surprisex01
                #     with dissolve

                #     dad "hasta que decidiste ;"

                show didacf_mouth happy_Talkingx07
                show didacf_eyes 02
                show didacf_pupils front02
                show didacf_eyebrows angryx01
                with dissolve

                dad "¿No es usarlo?"

                show didacf_mouth happy_Talkingx04
                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                with dissolve

                dad "¿A quien quieres engañar?"

                show didacf_mouth happy_Silentx06
                show didacf_eyes 05
                show didacf_pupils right05
                show didacf_eyebrows angryx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx02
                with fade

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with Dissolve(0.5)

                ne "..."

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab

                show didacf_mouth happy_Talkingx04
                show didacf_eyes 04
                show didacf_pupils right04
                show didacf_eyebrows normal
                with fade

                dad "Tranquilo,"

                show didacf_mouth sad_Talkingx04
                show didacf_eyes 05
                show didacf_pupils front05
                show didacf_eyebrows surprisex01
                with dissolve

                dad "no te juzgo."

                show didacf_mouth happy_Talkingx05
                show didacf_eyes 02
                show didacf_pupils front02
                show didacf_eyebrows sadx01
                with dissolve

                dad "Pero entre familia,"

                show didacf_mouth happy_Talkingx06
                show didacf_eyes 02
                show didacf_pupils right02
                show didacf_eyebrows angryx01
                with dissolve

                dad "es importante que pongamos las cartas sobre la mesa,"

            "...":

                call p_Help
                $pl.ch_pts("np",-3)

                show didacf_mouth sad_Talkingx004
                show didacf_eyes 08
                show didacf_pupils front08
                show didacf_eyebrows surprisex01
                with dissolve

                dad "Así me gusta."

                show didacf_mouth happy_Talkingx05
                show didacf_eyes 04
                show didacf_pupils front04
                show didacf_eyebrows angryx02
                with dissolve

                dad "¿Por qué sentirte culpable por algo así?"

                show didacf_mouth happy_Talkingx06
                show didacf_eyes 03
                show didacf_pupils front03
                show didacf_eyebrows sadx01
                with dissolve

                dad "Siempre y cuando no traiciones a tu sangre,"

                show didacf_mouth happy_Talkingx07
                show didacf_eyes 05
                show didacf_pupils front05
                show didacf_eyebrows angryx03
                with dissolve

                dad "lo demás está permitido,"

    else:

        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx003
        with dissolve

        dad "Verás,"

    extend " mi niño..."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "¡Deja de llamarme así!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Silentx02
    with dissolve

    p "¡No soy tu niño!"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows surprisex01
    show didacf_mouth happy_Talkingx06
    with dissolve

    dad "¿Estás seguro de ello?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx06
    with dissolve

    p "¿Euh...?"

    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx06
    with dissolve

    dad "¿Por qué crees que se interesó tanto por ti?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx03
    with dissolve

    dad "¿Por tu cuerpo musculado?"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx004
    with dissolve

    dad "¿Por tu enorme polla?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx05
    with dissolve

    dad "No negaré que pueden ser razones de peso,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx01
    show didacf_mouth happy_Talkingx06
    with dissolve

    dad "pero nada en comparación con lo que realmente le interesa de ti."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx07
    with dissolve

    p "..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Talkingx05
    with dissolve

    dad "Tu esperma."

    show didacf_eyes 01
    show didacf_pupils right01
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx06
    with dissolve

    dad "¿O debería decir mi semilla?"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx03
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "ALL"
    call Pedrera_char_lab

    show m_bodynew naked_down

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows surprisex001

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx03

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with fade

    pt "¡¿De qué diablos está hablando?!"

    if music_play != "theDread":
        play music "audio/music/kevinmacleod/creepy/theDread.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theDread"

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx05
    with fade

    dad "¿Acaso no es obvio?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx03
    with dissolve

    dad "Yo,"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx002
    with dissolve

    extend " {a=https://www.youtube.com/watch?v=l1fMjcWbIrc}soy tu padre{/a}."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth happy_Silentx04
    with dissolve

    p "..."

    $ Pedrera_char_Cond = "ALL"
    call Pedrera_char_lab

    show m_bodynew naked_down

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex002

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx06

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    ne "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    
    show neus_exp_mouth sad_Silentx07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx06
    with dissolve

    dad "..."

    show m_exp_mouth sad_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx02

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Silentx04

    show neus_exp_mouth sad_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx02
    with dissolve

    p "[neusname]..."

    show m_exp_mouth sad_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx03

    show neus_exp_mouth sad_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx04

    
    if night04_NeusInterview_Incest_Cond:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows normal
        show didacf_mouth sad_Talkingx03
        with dissolve

        dad "¿No te pareció extraño que te hiciera esas preguntas tan extrañas,"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Talkingx04
        with dissolve

        dad "mientras esperabais la cena ayer por la noche?"

    else:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows suspiciousx02
        show didacf_mouth happy_Talkingx03
        with dissolve

        dad "Me dirás que no lo has notado,"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows serious
        show didacf_mouth happy_Talkingx04
        with dissolve

        dad "con todas las indirectas que te ha llegado a lanzar..."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx01
        show didacf_mouth happy_Silentx04
        with dissolve

        p "..."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx06
    with fade

    dad "Quería saber cómo encajarías la verdad."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx04
    with dissolve

    dad "Saber,"

    extend " si serías capaz de acostarte,"

    extend " y embarazar,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Talkingx06
    with dissolve

    dad "a tu propia hermana."

    $ Pedrera_char_Cond = "ALL"
    call Pedrera_char_lab

    show m_bodynew naked_down

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Silentx06

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx04
    with dissolve

    #########################################################

    if config.version < "00.14.00": # Pedrera- Secrets unfolding.
        call endupdatescript
    
    #######################################################

    menu:

        pt "¡¿Ha dicho embarazar?!"

        "¿Por qué debería creerte?":
            call p_Help

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx01

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows normal
            show didacf_mouth sad_Talkingx04

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx03
            with dissolve

            dad "No me creas a mi."

            show didacf_eyes 04
            show didacf_pupils right04
            show didacf_eyebrows serious
            show didacf_mouth happy_Talkingx04

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx03
            with dissolve

            dad "Pregúntale a ella,"

            extend " si quieres."

            show didacf_eyes 05
            show didacf_pupils right05
            show didacf_eyebrows normal
            show didacf_mouth happy_Silentx06

            show neus_exp_mouth sadbiting_Silentx01
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx01
            with dissolve

            p "..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            menu:

                pt "¿En serio...?"

                "[neusname], ¿De qué está hablando?":
                    call p_Help

                    show neus_exp_mouth sadbiting_Silentx06
                    $ nteye = 6
                    call neus_exp_tears_tears
                    show neus_exp_iris front06
                    show neus_exp_eyebrows sadx05
                    with dissolve

                "...":
                    call p_Help

        "...":
            call p_Help

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx06
    with fade

    ne "..."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx003
    with fade

    dad "Pero por lo visto,"

    extend " no tuvo,"

    extend " ni tiene,"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth happy_Talkingx05
    with dissolve

    dad "las narices de contártelo."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx05
    with dissolve

    dad "Supongo que es normal,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows normal
    show didacf_mouth happy_Talkingx06
    with dissolve

    dad "al fin y al cabo el incesto entre humanos no es algo,"

    extend " deseable..."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx04
    with dissolve

    dad "Aunque eso no quita que mi {i}Txiki{/i},"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Talkingx06
    with dissolve

    dad "ha sido siempre una cobarde."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    with dissolve

    menu:

        pt "Una cobarde dice..."

        "De ti no me creo ni una palabra.":
            call p_Help
            $pl.ch_pts("np",1)

        "¿Por qué debería creerte?":
            call p_Help
            $pl.ch_pts("np",1)

        "...":
            call p_Help

            jump an05_Pedrera_DidacIdiocracy

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx04
    with dissolve

    dad "..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx004
    with dissolve

    dad "Oh,"

    extend " vamos..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve

    pause 0.1

label an05_Pedrera_DidacIdiocracy:

    if music_play != "wounded":
        play music "audio/music/kevinmacleod/sad/wounded.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "wounded"

    $ dad = d_txell
    $ dadname = "Meritxell"

    $ deyesc = ""
    $ meyesc = "_red"

    $ Pedrera_char_Cond = "ALL"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx01

    with fade_long1s

    dad "Conoces a Dídac desde tu tierna infancia,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx03
    with dissolve

    dad "sabes que es un gilipollas,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "¿Pero realmente le ves capaz de intentar violar a una chica?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01

    show neus_exp_mouth sad_Silentx06
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris right03
    show neus_exp_eyebrows sadx04
    with dissolve

    dad "¿Por qué?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02

    show neus_exp_mouth sad_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with dissolve

    dad "¿Porque se rió de uno de sus dibujitos?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Hay que admitir que su estilo de dibujo es bastante {a=https://es.wikipedia.org/wiki/Arte_naíf}naíf{/a},"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "pero eso es algo que ya tiene interiorizado,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "sus afrentas no van más allá de hacerse el gallito,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "y mostrar un poco de músculo."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex002

    show neus_exp_mouth sad_Silentx08
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with dissolve

    dad "¿Pero hasta el punto de intentar violar a alguien...?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01

    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    dad "¿Realmente lo ves capaz?"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx02
    with dissolve

    dad "Se sincero."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¡¿Euh?!"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡¿Qué coño está pasando aquí?!"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    dad "Tú duérmete."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show neus_exp_mouth sad_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with Dissolve (0.5)

    n "Dídac vuelve a caer rendido sobre la cama."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    p "..."

    menu:

        pt "No sé si es buena idea seguirle el juego..."

        "¿A dónde quieres ir a parar?":
            call p_Help
        "...":
            call p_Help


            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "Hmm..."

label an05_Pedrera_ThreeDates:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "Dime,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿porqué has tenido tres citas con tu hermana?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "¿Es realmente [neusname] mi hermana?"

        "...":
            call p_Help

        "Por que me chantajeó.":
            call p_Help
            $pl.ch_pts("np",-3)

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Al menos lo admites..."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellNeus"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx05
            with fade

            ne "..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

        "Quizás no me lo pidió de la mejor manera, pero hubiera aceptado igualmente salir con ella.":
            call p_Help
            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth happy_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with fade

            ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex002
            with fade

            dad "¿De verdad...?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "Por supuesto."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "Ya veo..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Aún así;"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Que casualidad,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "que el mejor amigo de su hermano,"

    extend " intentara violarla,"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "teniéndote a ti tan cerca,"

    extend " para poder salvarla."

    if music_play != "dayOfChaos":
        play music "audio/music/kevinmacleod/creepy/dayOfChaos.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "dayOfChaos"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    dad "Lo que hace el azar,"

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with Dissolve(0.5)

    pause 0.2

    # $ Pedrera_char_Cond = "TxellClose"
    # call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "¿No crees?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    menu:

        pt "¿Será verdad que Dídac no fue realmente culpable de lo que le hizo en el baño?"

        "[neusname], dime que es mentira.":
            call p_Help

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "..."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx02

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx05
            with dissolve

        "¡¿Qué clase de monstruo crees que es [neusname]?!":
            call p_Help
            $pl.ch_pts("np",-3)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows normal
            with dissolve

            ne "..."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sad_Silentx06
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows sadx01
            with dissolve

            dad "Hmm..."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal

            show neus_exp_mouth sad_Silentx08
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx01
            with dissolve

            dad "La misma que ha sido siempre."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious

            show neus_exp_mouth sad_Silentx09
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx02
            with dissolve

            p "[neusname]..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            p "Tú no..."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx01

            show neus_exp_mouth sad_Silentx09
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx05
            with dissolve

        "¡Por supuesto que fue una coincidencia!":
            call p_Help

            show m_exp_mouth happy_Talkingx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "A menudo,"

            extend " las casualidades no son más que estrategias ocultas,"

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "por quien no observa cautelosamente."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01
            with dissolve

        "...":
            call p_Help

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx02
            with dissolve

    ne "..."

    jump an05_Pedrera_ThreeDates_ThereStillMore


label an05_Pedrera_ThreeDates_ThereStillMore:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    dad "Tranquilo,"

    extend " solo estamos acariciando la verdad."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    dad "Hay mucho más que aún no te ha contado mi querida {i}Txiki{/i}."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    menu:

        pt "¿Será verdad...?"

        "¡No creo que estuviera fingiendo esas lágrimas al salir del baño!":
            call p_Help
            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious
            with dissolve

            p "¡Eso no es tan fácil de fingir!"

            show m_exp_mouth happy_Talkingx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "Que inocente eres..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Pero no,"

        "Dime que es mentira.":
            call p_Help

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex01
            with fade

            ne "..."

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            p "[neusname]..."

            show neus_exp_mouth sad_Silentx08
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with fade

            dad "Humm,"


    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "quizás esas lágrimas fueran reales,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    dad "al fin y al cabo,"

    extend " lo que hizo fue exacerbar su libido,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "y anular por completo su sentimiento de culpa,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "lo que hizo que sus acciones fueran erráticas e imprevisibles,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "si hubieras tardado mucho más en entrar al baño,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "quizás entonces hubiera terminado siendo violada realmente."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with fade

    p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with fade

    dad "Pero la salvaste,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y al mismo tiempo te hizo sentir asquerosamente culpable,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "por el comportamiento de tu amigo,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "del cual ni siquiera fue realmente responsable."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious

    show neus_exp_mouth sad_Silentx09
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with fade

    menu:

        pt "¿Por qué debería creerlo?"

        "Estás mintiendo.":
            call p_Help
            #$pl.ch_pts("np",1)

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "Hmm..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01
            with fade

            dad "¿De verdad lo crees?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¡Sí!"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx04
            with dissolve

            dad "Espera a escuchar el resto."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

        "...":
            call p_Help

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with fade

    if music_play != "echoesOfTimev2":
        play music "audio/music/kevinmacleod/creepy/echoesOfTimev2.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "echoesOfTimev2"

    dad "Días después,"

    extend " descubriste las repercusiones de su mordida,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "y te hizo chantaje para que tuvieras tres citas con ella;"

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows normal

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with fade

    dad "mi pequeña e inocente Elur..."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with dissolve

    menu:

        pt "¿Pasar un calvario así, solo para evitar que la pudiera rechazar?"

        "¡Lo que dices no tiene sentido!":
            call p_Help
            #$pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows surprisex01
            with dissolve

            p "¡¿Por qué tomarse tantas molestias?!"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows normal

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows serious
            with dissolve

            p "¡Podría habérmelo pedido sin tener que pasar por todo este calvario!"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex001

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx02
            with dissolve

            dad "Ohhh..."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx02

            show neus_exp_mouth sad_Silentx08
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx05
            with dissolve

            dad "He ahí la cuestión."


        "...":
            call p_Help

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "¿Hubieras aceptado de buenas a primeras tener una cita con una chica"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "que se ha pasado medio año observándote en las sombras"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    dad "sin dirigirte apenas la palabra?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx03
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx02
    with fade

    # show m_exp_mouth happy_Talkingx03
    # show m_exp_eyes 03
    # show m_exp_piris front03
    # show m_exp_eyebrows normal
    # with dissolve

    dad "¿Hubieras tenido más de una cita con ella después de habértela follado?"

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with dissolve

    # show m_exp_mouth happy_Talkingx04
    # show m_exp_eyes 04
    # show m_exp_piris front04
    # show m_exp_eyebrows angryx01
    # with dissolve

    dad "¿Te hubieras conformado solo con ella teniendo otras opciones?"

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sad_Silentx08
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx02
    with fade

    menu:

        pt "¡¿Qué clase de monstruo cree que soy?!"

        "¡Por supuesto que sí!":
            call p_Help

            if NeusCuckolded_Sexually:

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex002

                show neus_exp_mouth happy_Silentx02
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "Hmmm..."

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex02

                show neus_exp_mouth sad_Silentx03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "¿Después de lo que has llegado a hacer?"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows normal

                show neus_exp_mouth sad_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx03
                with dissolve

                dad "Desde luego..."

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 07
                show m_exp_piris front07
                show m_exp_eyebrows sadx02

                show neus_exp_mouth sad_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx05
                with dissolve

                dad "Tienes que aprender a mentir mejor."

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows normal

                show neus_exp_mouth sad_Silentx07
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx06
                with dissolve

                p "¡Eso lo dirás por ti!"

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with dissolve

                $pl.ch_pts("np",-2)

                ne "..."

            else:

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth happy_Silentx02
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "Hmm..."

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris left04
                show m_exp_eyebrows suspiciousx02

                show neus_exp_mouth sad_Silentx03
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "Supongo que eso no lo sabremos nunca..."

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth happy_Silentx03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                p "Habla por ti."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious

                show neus_exp_mouth happy_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx03
                with dissolve

                $pl.ch_pts("np",2)

                ne "..."

        "...":
            call p_Help

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "¿Estaría cómoda en una relación en la que por primera vez en siglos,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious

    show neus_exp_mouth sad_Silentx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows surprisex01
    with dissolve

    dad "ella no domina la situación?"

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris left00
    show neus_exp_eyebrows surprisex02
    with dissolve

    dad "¿Hubieras aceptado dejarla embarazada en menos de una semana de la primera cita?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious

    show neus_exp_mouth sad_Silentx08
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with Dissolve(0.5)

    pause 0.2

    show neus_exp_mouth sad_Silentx09
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve (0.5)

    menu:

        pt "¡¿Embarazada?!"

        "¡¿Por qué debería dejarla embarazada?!":
            call p_Help
            $pl.ch_pts("np",-1)

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

    dad "Preguntas,"

    extend " preguntas,"

    extend " preguntas..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    # show m_exp_mouth happy_Silentx04
    # show m_exp_eyes 04
    # show m_exp_piris front04
    # show m_exp_eyebrows serious
    # with dissolve

    p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "Verás,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows normal
    with dissolve

    dad "a diferencia de la mayoría de sus víctimas,"

    extend " tú eres alguien distinto."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "A ti no te puede borrar la memoria,"

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "porque eres fruto de mi semilla."

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "No..."

    $ meyesc = "_red"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Si hubiera metido la pata,"

    extend " no habría vuelta atrás."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Y para qué engañarnos?"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows serious
    with dissolve

    dad "Una chica como Elur,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "sin transmutar ninguna parte de su cuerpo,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "no es alguien que levante pasiones."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Menos aún si tenemos en cuenta,"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "que hace más de medio año que ingresó en tu misma clase,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y aún no ha sido capaz,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "de tener una simple e inocente conversación contigo."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with fade

    show neus_exp_mouth sad_Silentx09
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows surprisex01
    with Dissolve(0.5)

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    dad "Sin los poderes que le ofrecen mis queridas criaturas,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "no es más que una niña estúpida,"

    extend " cobarde,"

    extend " e inútil."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    menu:

        pt "¿Me está provocando a mí, o a ella?"

        "No te permito que hables así de ella.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01

            with dissolve

            pause 0.2

            show neus_exp_mouth happybiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with Dissolve(0.5)

            dad "..."

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01

            show neus_exp_mouth sad_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx04
            with dissolve

            dad "¿Y qué harás para evitarlo?"

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex02
            with fade

            p "Si hace falta te romperé los dientes."

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows angryx01
            with dissolve

            dad "No seas necio."

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "Para empezar,"

            extend " no sería a mi a quien se los romperías,"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "sino a esta rubia a quien poseo."

            $ meyesc = "_goat"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Y en segundo lugar,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 00
            show m_exp_piris front00
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "no puedes dar un paso sin que yo te lo permita."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows serious
            with dissolve

            n "Instintivamente intentas dar un paso hacia adelante,"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with dissolve

            n "pero descubres sin demasiada sorpresa,"

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            n "que eres incapaz de mover un músculo."

            $ meyesc = "_red"

            if NeusCuckolded_Sexually:

                $pl.ch_pts("np",-1)

                show m_exp_mouth happy_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "¿Te molesta que hable mal de tu harén?"

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex001
                with dissolve

                dad "Tranquilo,"

                extend " lo entiendo."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows normal
                with dissolve

                p "¡¿De qué demonios estás ha...?!"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                p "¡Guhh!"

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                pt "¡¿No puedo hablar?!"

                show m_exp_mouth sad_Talkingx001
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows normal
                with dissolve

                dad "Shhh..."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Sigue escuchándome."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx02
                with dissolve

            else:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Aún no he terminado,"

                extend " mi pequeño."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx02
                with dissolve

            p "..."



        "...":
            call p_Help

    if music_play != "nervous":
        play music "audio/music/kevinmacleod/creepy/nervous.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nervous"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "Me imagino que sentía la presión del tiempo."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Cuando sabe que la estoy buscando,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "no es algo inteligente quedarse demasiado tiempo en un mismo lugar,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "ni tratar con la misma gente."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Pero contigo,"

    extend " solo podía jugarse una carta,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y te aseguro que jugó fuerte;"

    if music_play != "dreamsBecomeReal_slow":
        play music "audio/music/kevinmacleod/sad/dreamsBecomeReal_slow.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "dreamsBecomeReal_slow"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "mucho más de lo que te imaginas."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with Dissolve(0.5)

    p "..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx02
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with Dissolve(0.5)

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)


    pt "¿De qué demonios está hablando?"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "Me imagino que te preguntarás qué fue lo que te hice ver en ese hotel,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "en esas tres habitaciones."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        "Tú eras ese hombre vestido de botones con esos ojos rojos.":
            call p_Help

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows normal
            with dissolve

            p "¡¿No es así?!"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "Hmmm..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Mi querido niño,"

            extend " lo que viste no fue más que una ilusión,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "para contarte una verdad."

            $ meyesc = "_goat"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Yo no tengo cuerpo,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious
            with dissolve

            dad "lo único que viste es una simple representación."

            show m_exp_mouth happy_Silentx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            $ meyesc = "_red"

        "...":
            call p_Help

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "¿No tienes ninguna pregunta?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

    menu:

        "¿Quien era esa anciana y esa mujer tetuda?":
            call p_Help

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "¿De verdad no lo adivinas?"

        "...":
            call p_Help

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal
            with dissolve

            dad "Sé que te estás preguntando por quienes debían ser esas dos hembras..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Pero estoy seguro,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            dad "que ya debes imaginártelo."



    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab


    show neus_exp_mouth sad_Silentx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx02
    with fade

    pause 0.2

    show neus_exp_mouth sad_Silentx04
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with Dissolve(0.5)

    ne "..."

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01

    show neus_exp_mouth sad_Silentx05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx04
    with fade

    menu:

        pt "Dudo que nada de lo que viera fuera real."

        "La mujer se parecía mucho a [neusname].":
            call p_Help

        "Lo que vi no fue más que una ilusión.":
            call p_Help

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Es posible,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "pero no me negarás,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "que tenía un cierto parecido con mi querida {i}Elur{/i}."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "..."

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Esa mujer tan impactante,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "tenía un cierto parecido con mi querida {i}Elur{/i},"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "¿No crees?"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Aunque con un cuerpo mucho más voluptuoso e interesante,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "¿no te parece?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    menu:

        pt "¿Se está cachondeando de ella?"

        "¡Eso será tu opinión!":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with dissolve

            p "¡A mi me gusta [neusname] tal y como está!"

            if NeusCuckolded:

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows surprisex01

                if NeusCuckolded_Sexually:
                    $pl.ch_pts("np",-2)

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve
                else:
                    $pl.ch_pts("np",-1)

                    show m_exp_mouth happy_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                dad "Hmm..."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "Quizás no te disguste,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows angryx02

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx03
                with dissolve

                dad "pero desde luego no te conformas solo con ella..."

                if NeusCuckolded_Sexually:

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx01

                    show neus_exp_mouth sadbiting_Silentx03
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris left02
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    dad "eso está claro..."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx04
                with dissolve

            else:

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows normal

                show neus_exp_mouth sad_Silentx03
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "Hmmm..."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                show neus_exp_mouth happy_Silentx03
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "..."

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows angryx02

                show neus_exp_mouth happy_Silentx04
                $ nteye = 6
                call neus_exp_tears_tears
                show neus_exp_iris front06
                show neus_exp_eyebrows sadx02
                with dissolve

            p "..."

        "Eso es porque solo juzgas su físico.":
            call p_Help
            #$pl.ch_pts("np",-1)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002

            show neus_exp_mouth sad_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            ne "..."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01

            show neus_exp_mouth sad_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx03
            with dissolve

            dad "Hmm..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows serious

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            dad "Claro,"

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show m_exp_mouth sad_Talkingx002
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows surprisex01

            show neus_exp_mouth sad_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx05
            with dissolve

            dad "porque cuando vas a ligar en bares,"

            extend " o discotecas,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sad_Silentx08
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx05
            with dissolve

            dad "lo primero en que te fijas en las mujeres,"

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with fade

            dad "es si leen a {a=https://es.wikipedia.org/wiki/Friedrich_Nietzsche}Nietzsche{/a},"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx02
            with dissolve

            dad "separan el plástico del orgánico cuando reciclan,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "o si se ríen con los {a=https://es.wikipedia.org/wiki/Monty_Python}Monty Python{/a}..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "El físico y la apariencia no es nada importante,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "El varón humano no se fija en esas nimiedades en lo absoluto."

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Lo que más te llamó la atención de la tetuda del hotel,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal
            with dissolve

            dad "fue su pulsera verde."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "Porque era verde,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "¿verdad?"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "¿O era azul?"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows serious
            with dissolve

            dad "¿Por qué crees que {i}Elur{/i} se ha puesto este vestido,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows normal
            with dissolve

            dad "mucho más provocativo que el de las otras dos citas,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            if neyesp == "True":

                dad "y se ha pintado los ojos?"

            else:

                dad "y se pintó los ojos?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve


            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx06
            with fade

            ne "..."


            if neyesp == "":

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx06
                with dissolve

                dad "Si realmente el físico o lo visual no importara,"

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx07
                with dissolve

                dad "¿Por qué le dijiste que se quitara la sombra de ojos?"

                show neus_exp_mouth sad_Silentx09
                $ nteye = 6
                call neus_exp_tears_tears
                show neus_exp_iris front06
                show neus_exp_eyebrows sadx07
                with dissolve

            else:

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx07
                with dissolve

            p "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with fade


            dad "¿Y qué me dices del tiempo y esfuerzo que le dedicas a mantener este cuerpo tan musculado?"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "¿No te gusta ver el fruto de tu sacrificio reflejado en el espejo?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Y no acudirás a una cita con el mismo chándal del gimnasio,"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "¿Verdad?"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "No..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious
            with dissolve

            dad "Tienes que arreglarte y acicalarte para dar una buena imagen."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Porque lo visual quizás importa más de lo que a menudo sois capaces de reconocer;"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "¿O me equivoco?"

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx06
            with fade


        "Eso no te lo voy a poder negar...":
            call p_Help
            $pl.ch_pts("np",-2)

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious

            show neus_exp_mouth sadbiting_Silentx01
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with fade

            ne "..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx07
            with Dissolve(0.5)

            pause 0.2

        "...":
            call p_Help

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            pause 0.2


    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    dad "Pero entonces,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "¿quien diablos era es anciana?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Te estarás preguntando..."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    pause 0.2

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with Dissolve(0.5)

    pause 0.1

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows sadx03
    with fade

    ne "..."

    show neus_exp_mouth sad_Silentx09
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows normal
    with Dissolve(0.5)

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with Dissolve(0.5)

    ne "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with fade

    dad "Aunque me imagino que también sabrás la respuesta,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿no es así?"

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:
        pt "¿Me lee la mente?"

        "También me recordaba algo a [neusname]...":
            call p_Help

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 01
            show m_exp_piris right01
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Curioso,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "¿no crees?"

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "¿No se le parecía?"

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Pero..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Por qué debería mostrarte una versión anciana de mi querida {i}Txiki{/i}?"

    if music_play != "wounded":
        play music "audio/music/kevinmacleod/sad/wounded.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "wounded"

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿O prefieres obviar la verdad?"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        pt "No... No puede ser..."

        "¡¿Qué verdad?!":
            call p_Help

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Hmmm..."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "¿De verdad hace falta que te lo diga?"

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

        "...":
            call p_Help

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "¿Cuantos años crees que tiene {i}Elur{/i}?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx08
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx03
    with fade

    p "..."

    show neus_exp_mouth sad_Silentx09
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with fade

    dad "¿Cómo crees que se vería si no tuviera juventud eterna?"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "En realidad a estas alturas,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "no sería más que un montón de polvo;"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "pero preferí darle una imagen algo más..."

    extend " humana."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx08
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx04
    with fade

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx05
    with Dissolve(0.5)

    menu:

        pt "¿Qué edad tendrá...?"

        "[neusname], ¿Cuantos años tienes?":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx03
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            dad "Ncht,"

            extend " ncht,"

            extend " ncht..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with fade

            dad "Es de mala educación preguntarle eso a una dama."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Tendré que enseñarte modales,"

            # show m_exp_mouth happy_Talkingx08
            # show m_exp_eyes 05
            # show m_exp_piris front05
            # show m_exp_eyebrows angryx03
            # with dissolve

        "No es su edad lo que me importa.":
            call p_Help

            $pl.ch_pts("np",1)

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with fade

            dad "Claro que no..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Porque luce joven,"

            extend " hermosa,"

            extend " y casi hasta pre-adolescente."

            show m_exp_mouth sad_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Si luciera el físico que le corresponde por su edad,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows serious
            with dissolve

            dad "quizás pensarías de otra forma."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Sin duda alguna,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows normal
            with dissolve

            dad "mucho mejor que esa anciana que viste en el hotel."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            pause 0.2

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows serious
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx02
            with fade

            p "..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows suspiciousx01
            with fade

            dad "¿Pero no te preguntas qué precio hay que pagar para mantener esta juventud?"

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Es mejor no hacerse esas preguntas."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "¿Verdad que no?"

            # show m_exp_mouth happy_Talkingx07
            # show m_exp_eyes 05
            # show m_exp_piris front05
            # show m_exp_eyebrows angryx01
            # with dissolve

        "...":
            call p_Help

            dad "Hmm..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with fade

            dad "Curioso..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "¿No tienes interés en saber más sobre ella?"

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            menu:

                "Si me lo quiere contar, me lo dirá ella misma.":
                    call p_Help

                    $pl.ch_pts("np",2)

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth happy_Silentx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx02
                    with fade

                    ne "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx002
                    show m_exp_eyes 03
                    show m_exp_piris right03
                    show m_exp_eyebrows surprisex01
                    with fade

                    dad "Oh..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "¿Pero realmente crees que lo hará?"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    dad "Que inocente eres,"

                "No es de tu incumbencia.":
                    call p_Help

                    $pl.ch_pts("np",1)

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth happy_Silentx02
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris front05
                    show neus_exp_eyebrows sadx03
                    with fade

                    ne "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with fade

                    dad "Pero quizás sí tendría que serlo de la tuya,"

                "No tengo porque responder a tu pregunta.":
                    call p_Help

                    $pl.ch_pts("np",1)

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth happy_Silentx03
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris left05
                    show neus_exp_eyebrows serious
                    with fade

                    ne "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with fade

                    dad "No,"

                    extend " realmente no hace falta que respondas..."

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve

                    dad "sé lo que pasa por tu cabeza,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "así que realmente no me hace falta preguntarte nada,"

    extend " mi niño..."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        pt "Que pesadito con lo de \"mi niño\"..."

        "¡Aunque fueras realmente mi padre, no tienes derecho a llamarme así!":
            call p_Help

            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "..."

        "¡Deja de llamarme así!":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows normal
            with dissolve

            dad "Hmm..."

        "...":
            call p_Help

            jump afternight05_Pedrera_HotelExplanation

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "¿Te molesta la verdad?"

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Te he dicho que apenas estamos empezando..."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    $ meyesc = "_red"

    jump afternight05_Pedrera_HotelExplanation

label afternight05_Pedrera_HotelExplanation:

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 3:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        dad "¿Qué crees que te estaba mostrando tras esas tres puertas?"

    elif night05_NeusLastDate_HotelKrueger_Door_Used_Number > 0:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        dad "¿Qué crees que estaba intentando mostrarte tras esas tres puertas?"

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 1:

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond:

                dad "Ya que solo entraste en la del cementerio."

            elif night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond:

                dad "Ya que solo entraste en la del niño en su cama."

            elif night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond:

                dad "Ya que solo entraste en la de la iglesia."

        elif night05_NeusLastDate_HotelKrueger_Door_Used_Number == 2:

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            if night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond == False:

                dad "Ya que solo entraste en la casa a oscuras en medio de una tormenta,"

                extend " y la iglesia."

            elif night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False:

                dad "Ya que solo entraste en la del cementerio,"

                extend " y la iglesia."

            elif night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == False:

                dad "Ya que solo entraste en la del cementerio,"

                extend " y la casa a oscuras en medio de una tormenta."

        if (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond and 
            room_02_child_room_but_kid_Cond == False):

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¿Lo que había bajo esa sábana era un niño...?"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "Ni más ni menos."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Pero fuiste tan cobarde,"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            dad "que ni siquiera te atreviste a acercarte a él."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            p "¡No quería entrar en tu juego!"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "Hmmm..."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Y bien..."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "¿Qué imaginas que quería mostrarte tras esas puertas?"

    else:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows normal
        with dissolve

        dad "¿Qué imaginas que quería mostrarte tras esas tres puertas que no quisiste entrar?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        pt "Nada bueno, eso seguro..."

        "¡Una fantasía perturbada de las tuyas!":
            call p_Help
            $pl.ch_pts("np",1)

        "Ni lo sé, ni me interesa.":
            call p_Help

            $pl.ch_pts("np",1)

        "...":
            call p_Help

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Oh,"

    extend " vamos..."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Aunque sea solo para seguirme un poco el juego,"

    if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 0:

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        dad "¿qué fue lo que viste?"

    else:

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "ya que no entraste en ninguna,"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "al menos intenta adivinarlo."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    menu:

        "<Responderle>" if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 0:
            call p_Help

            jump afternight05_Pedrera_HotelExplanation_Answer

        "<Intentar adivinarlo>" if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 0:
            call p_Help

            jump afternight05_Pedrera_HotelExplanation_Answer

        "<Negarte a responder>":
            call p_Help

            $pl.ch_pts("np",1)

            jump afternight05_Pedrera_HotelExplanattion_RefuseToAnswer

label afternight05_Pedrera_HotelExplanattion_RefuseToAnswer:

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "No pienso entrar en tu telaraña de mentiras."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "¿De verdad...?"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Elur sabe muy bien lo que ocurre cuando no se hace lo que pido."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx09
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx04
    with fade

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with fade

    p "No te tengo miedo."

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Quizás tú no."

    show m_exp_mouth happy_Silentx12
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "¿Vas a responder?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    menu:

        "<Permanecer callado>":
            call p_Help

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Como gustes..."

            if music_play != "oppressiveGloom":
                play music "audio/music/kevinmacleod/sad/oppressiveGloom.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "oppressiveGloom"

            play sound "audio/characters/neus/scream02.ogg"

            $ Pedrera_char_Cond = "NeusPain"
            call Pedrera_char_lab

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show neus_exp_mouth sad_Talkingx11
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows angryx03
            with hpunch

            ne "{size=40}¡¡¡AAAAHHHH!!!{/size}"

            scene ped_pain_neus:
                subpixel True
                truecenter
                zoom 1.0 xpos 0.3 ypos 0.9
                easein_quad 10.0 zoom 0.5 xpos 0.5 ypos 0.5
            show border_darkness_02:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 10.0 zoom 1.0
            with vpunch

            p "¡[neusname]!"

            n "Observas su cuerpo caer al suelo, mientras tiembla y se agarra fuertemente de los hombros,"

            n "al mismo tiempo que parece sufrir un dolor indescriptible."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with fade

            dad "Quizás prefieras permanecer callado."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx03
            with dissolve

            dad "Debo reconocer que echaba de menos los gritos de mi {i}Txiki{/i}."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¡Es tu hija!"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx01
            with dissolve

            dad "También es tu hermana."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            p "¡¿Acaso no te importa lo más mínimo?!"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Ahh..."

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows angryx03
            with dissolve

            dad "Pero eres tú quien puede evitarlo."

            show m_exp_mouth happy_Silentx10
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx03
            with dissolve

            if night05_NeusLastDate_HotelKrueger_Door_Used_Number < 3:

                if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 0:

                    p "¡¿Qué quieres que te responda,"

                    extend " si ni siquiera entré a ninguna puerta!"

                else:

                    p "¡¿Qué quieres que te responda,"

                    if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 2:

                        extend " si no entré en la última puerta!"

                    elif night05_NeusLastDate_HotelKrueger_Door_Used_Number == 1:

                        extend " si solo entré en una puerta!"

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Solo te pido que lo intentes."

                show m_exp_mouth sad_Talkingx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows normal
                with dissolve

                dad "No te pido tanto,"

                extend " ¿No crees?"

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

            p "..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "¿Vas a seguir sin responder?"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

            menu:

                pt "¡Maldito monstruo!"

                "<Permanecer callado>":
                    call p_Help

                    $pl.ch_pts("np",-1)

                    $ Pedrera_char_Cond = "NeusPain"
                    call Pedrera_char_lab

                    if ntlong in range (0,6):
                        if ntlong < 5:
                            $ ntlong += 1
                    show neus_exp_mouth sad_Talkingx11
                    $ nteye = 7
                    call neus_exp_tears_tears
                    show neus_exp_iris front07
                    show neus_exp_eyebrows angryx03
                    with hpunch

                    play sound "audio/characters/neus/scream04.ogg"

                    ne "{size=50}¡¡¡AAAAHHHH!!!{/size}"

                    scene ped_pain_neus:
                        subpixel True
                        truecenter
                        zoom 1.0 xpos 0.3 ypos 0.9
                        easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
                    show border_darkness_02:
                        subpixel True
                        truecenter
                        zoom 0.5
                        easein_quad 5.0 zoom 1.0
                    with vpunch

                    p "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth happy_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows normal
                    with fade

                    dad "Hmmm..."

                    $pl.ch_pts("dp",-1)

                    $ Pedrera_char_Cond = "DidacPain"
                    call Pedrera_char_lab

                    show didacf_mouth sad_Talkingx09
                    show didacf_eyes 07
                    show didacf_pupils front07
                    show didacf_eyebrows angryx03
                    with vpunch
                    with vpunch

                    play sound "audio/characters/didac/scream_au15.ogg"

                    d "{size=50}¡¡AAAAAARGHH!!{/size}"

                    scene ped_pain_didac:
                        subpixel True
                        truecenter
                        zoom 1.0 xpos 0.95 ypos 1.0
                        easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
                    show border_darkness_02:
                        subpixel True
                        truecenter
                        zoom 0.5
                        easein_quad 5.0 zoom 1.0
                    with vpunch
                            
                    p "¡Dídac!"

                    p "¡¿Él también?!"

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx01
                    with fade

                    dad "Por supuesto."

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "Sino se lo hago a la rubia,"

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "es porque ahora mismo,"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    dad "me tomaría demasiadas molestias no causarme dolor a mi mismo."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    p "¡Eres un maldito bastardo!"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex002
                    with dissolve

                    dad "En realidad el bastardo eres tú,"

                    show m_exp_mouth happy_Talkingx11
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    dad "pero empiezas a entenderlo."

                    show m_exp_mouth happy_Silentx09
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    jump afternight05_Pedrera_HotelExplanation_Loop

                "<Responder>":
                    call p_Help

                    jump afternight05_Pedrera_HotelExplanation_Answer

        "<Responder>":
            call p_Help

            jump afternight05_Pedrera_HotelExplanation_Answer


label afternight05_Pedrera_HotelExplanation_Loop:

    $ afternight05_Pedrera_HotelExplanation_Loop_Cond += 1

    menu:

        pt "¡¿Voy a seguir callado?!"

        "<Permanecer callado>":
            call p_Help

            $pl.ch_pts("np",-1)

            $ Pedrera_char_Cond = "NeusPain"
            call Pedrera_char_lab

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1
            show neus_exp_mouth sad_Talkingx11
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows angryx03
            with hpunch
            with hpunch

            play sound "audio/characters/didac/scream01.ogg"

            ne "{size=55}¡¡¡AAAAHHHH!!!{/size}"

            scene ped_pain_neus:
                subpixel True
                truecenter
                zoom 1.0 xpos 0.3 ypos 0.9
                easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
            show border_darkness_02:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 5.0 zoom 1.0
            with vpunch

            p "..."

            $pl.ch_pts("dp",-1)

            $ Pedrera_char_Cond = "DidacPain"
            call Pedrera_char_lab

            show didacf_mouth sad_Talkingx09
            show didacf_eyes 07
            show didacf_pupils front07
            show didacf_eyebrows angryx03
            with vpunch
            with vpunch

            play sound "audio/characters/didac/scream_au16.ogg"

            d "{size=55}¡¡AAAAAARGHH!!{/size}"

            scene ped_pain_didac:
                subpixel True
                truecenter
                zoom 1.0 xpos 0.95 ypos 1.0
                easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
            show border_darkness_02:
                subpixel True
                truecenter
                zoom 0.5
                easein_quad 5.0 zoom 1.0

            p "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with fade

            p "..."

            jump afternight05_Pedrera_HotelExplanation_Loop

        "<Responder>":
            call p_Help

            jump afternight05_Pedrera_HotelExplanation_Answer

label afternight05_Pedrera_HotelExplanation_Answer:

    $ meyesc = "_red"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    if room_3doors_met:

        p "Una mujer que ha perdido a su hijo,"

        p "un niño que ha perdido a su padre,"

        p "y una esposa que ha sido abandonada por su marido poco antes de la boda."

        jump afternight05_Pedrera_HotelExplanation_After

    elif night05_NeusLastDate_HotelKrueger_Door_Used_Number > 0:

        ### A

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 1:

            p "En la primera habitación vi,"

        call afternight05_Pedrera_HotelExplanation_DoorsVisited_A

        ### B

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 1:

            p "Y en la otra,"

            # If you visited the Three doors, you wouldn't explain those things here.

        call afternight05_Pedrera_HotelExplanation_DoorsVisited_A

        ### C

        call afternight05_Pedrera_HotelExplanation_DoorsVisited_A

        ####

        show m_exp_mouth sad_Silentx01
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex002
        with dissolve

        dad "Hmmm..."

        show m_exp_mouth sad_Talkingx002
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "¿Por qué debería enseñarte algo así...?"

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows normal
        with dissolve

        p "..."

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01
        with dissolve

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 1:

            dad "Como solo entraste en una de las habitaciones,"

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "te diré lo que había en las otras dos."

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 2:

            dad "Como no entraste en la última puerta,"

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "te diré lo que había."

        jump afternight05_Pedrera_HotelExplanation_After

    else:

        menu afternight05_Pedrera_HotelExplanattion_NoDoorsVisited_Question:

            pt "¡¿Qué se supone que le tengo que decir?!"

            "Alguna clase de monstruo o criatura no muerta.":
                call p_Help

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "¿Y qué sentido tendría mostrarte algo así?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                jump afternight05_Pedrera_HotelExplanation_AnswerWrong

            "Lo más probable es que apareciera algún {i}jump scare{/i} sin to ni son.":
                call p_Help

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "Si quisiera asustarte de un modo tan gratuito,"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "no necesitaría llevarte a ningún hotel,"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows normal
                with dissolve

                dad "ni darte a elegir ninguna puerta."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                jump afternight05_Pedrera_HotelExplanation_AnswerWrong

            "Algo que me mostrara lo monstruosa y mentirosa que es [neusname], según tu retorcida imaginación.":
                call p_Help

                $ pl.ch_pts("np",1)

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "¿Qué sacaría yo en mentirte?"

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex002
                with dissolve

                p "¿Qué saca el diablo de mentir a sus víctimas?"

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Escribió {a=https://es.wikipedia.org/wiki/Lord_Byron}Lord Byron{/a} una vez,"

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex002
                with dissolve

                dad "{i}\"El diablo dice la verdad más a menudo de lo que se cree,"

                extend " pero tiene un público ignorante\"{/i}"

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                p "..."

                jump afternight05_Pedrera_HotelExplanation_After

label afternight05_Pedrera_HotelExplanation_AnswerWrong:

    p "¡Y yo que sé como funciona tu mente retorcida!"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Hmm..."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "Ni siquiera te has acercado."

    jump afternight05_Pedrera_HotelExplanation_After

###

default Doors_Visited_A_Cemetery = False
default Doors_Visited_A_Kid = False
default Doors_Visited_A_Marriage = False



label afternight05_Pedrera_HotelExplanation_DoorsVisited_A:

    if (night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond and
        Doors_Visited_A_Cemetery == False):

        $ Doors_Visited_A_Cemetery = True

        if (night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_family_met_Cond or room_01_cemetery_mother_met_Cond):

            p "una mujer que ha perdido a su hijo."

        else:

            p "lo que parecía una pareja llorando a un ser querido en el cementerio."

    elif (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond and
        Doors_Visited_A_Kid == False):

        $ Doors_Visited_A_Kid = True

        if room_02_child_room_but_kid_Cond:

            p "un niño que ha perdido a su padre."

        else:

            p "lo que parecían los sollozos de un niño,"

            p "escondido bajo las sábanas de su habitación."

    elif (night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond and
        Doors_Visited_A_Marriage == False):

        $ Doors_Visited_A_Marriage = True

        if room_03_marriage_far_woman_Cond:

            p "Una esposa que ha sido abandonada por su marido poco antes de la boda."

        else:

            p "Lo que parecía una esposa,"

            p "llorando la perdida de su marido,"

            extend " supongo..."
    return


###

default Doors_Visited_B_Cemetery = False
default Doors_Visited_B_Kid = False
default Doors_Visited_B_Marriage = False


label afternight05_Pedrera_HotelExplanation_DoorsVisited_B:

    if (night05_NeusLastDate_HotelKrueger_Door_01_Cemetery_Cond == False and 
        Doors_Visited_B_Cemetery == False):

        $ Doors_Visited_B_Cemetery = True

        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx01
        with dissolve

        dad "una mujer en un cementerio de niños al lado de su marido,"

        dad "llorando la reciente muerte de su pequeño."

    ####

    elif (night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False and 
        Doors_Visited_B_Kid == False):

        $ Doors_Visited_B_Kid = True

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows sadx02
        with dissolve

        dad "Un niño,"

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx01
        with dissolve

        dad "cubierto entre sus sábanas,"

        #if night05_NeusLastDate_HotelKrueger_Door_02_Childhood_Cond == False:

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "en una noche tormentosa,"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        dad "que ha perdido a su padre;"

    #####

    elif ((night05_NeusLastDate_HotelKrueger_Door_03_Marriage_Cond == False) and (Doors_Visited_B_Marriage == False)):

        $ Doors_Visited_B_Marriage = True

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows sadx01
        with dissolve

        dad "Una esposa en medio de una iglesia,"

        show m_exp_mouth sad_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows sadx02
        with dissolve

        dad "que ha sido abandonada por su marido poco antes de la boda."

    return



label afternight05_Pedrera_HotelExplanation_After:

    #$ Doors_Visited_B_Review = 0

    if afternight05_Pedrera_HotelExplanation_Loop_Cond > 1:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "Has tardado [afternight05_Pedrera_HotelExplanation_Loop_Cond] veces en entender que era mejor responderme."

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 0:

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Aunque hayas sido tan cobarde,"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "como para no entrar ni siquiera a una sola puerta."

        show m_exp_mouth happy_Talkingx03
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex02
        with dissolve

        dad "Pero supongo que es mejor tarde que nunca."

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows normal
        with dissolve

        p "..."

    if room_3doors_met == False:

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 2:

            #dad "En la que te faltaba por visitar,"
            pass

        else:

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "En una de ellas había,"

        ### A
        call afternight05_Pedrera_HotelExplanation_DoorsVisited_B

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 1:

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "y en la otra,"

        elif night05_NeusLastDate_HotelKrueger_Door_Used_Number == 0:

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "en otra,"

        ### B
        call afternight05_Pedrera_HotelExplanation_DoorsVisited_B

        if night05_NeusLastDate_HotelKrueger_Door_Used_Number == 0:

            show m_exp_mouth sad_Talkingx002
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Y en la última,"

        ### C
        call afternight05_Pedrera_HotelExplanation_DoorsVisited_B

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows normal
        with dissolve

        p "..."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "¿Qué crees que hay en común entre estos tres casos?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    p "..."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    p "Aparentemente,"

    extend " la pérdida de alguien amado."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Hmmm..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx07
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx06
    with fade

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    p "..."

    if music_play != "heartbreaking":
        play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "heartbreaking"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with fade

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "¿Qué debió sentir esa mujer?"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "vestida de blanco,"

    extend " con toda su familia presente,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "para celebrar el que debía ser ese día soñado desde que apenas era una niña,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows normal
    with dissolve

    dad "recordando lo felices que eran esas añoradas princesas de {a=https://es.wikipedia.org/wiki/The_Walt_Disney_Company}Disney{/a} con ese final feliz,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "junto al amor de su vida;"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    dad "para descubrir,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "que no tan solo ha sido rechazada en el altar,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx02
    with dissolve

    dad "ante la atenta mirada de todos cuantos conoce y ama,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "sino que además,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "ha sido porque se ha fugado con otra,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "mucho más joven y hermosa..."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx08
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx05
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx03
    with Dissolve(0.5)

    pause 0.2

    show neus_exp_mouth sad_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    p "..."

    #

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with fade

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Y qué me dices de ese pobre niño?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "solo en casa,"

    extend " en una noche tormentosa y tenebrosa,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    dad "oculto bajo su suave manta de tela,"

    extend " usada a modo de escudo,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows sadx02
    with dissolve

    dad "contra esos susurros,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "y la atenta mirada de mis queridas criaturas;"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "a la espera de su amado y protector padre,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx02
    with dissolve

    dad "el cual no volvió a ver nunca más con vida,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx02
    with dissolve

    dad "por culpa de esa oscura y voluptuosa mujer de la cual él mismo ya le advertía."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Quien podría ser esa mujer tan oscura...?"

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    ne "..."

    #

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with fade

    pause 0.2

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Sin mencionar esa madre,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "destrozada y perdida entre lamentos y lágrimas,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows sadx02
    with dissolve

    dad "al perder a su hijo no nato a pocas semanas de dar a luz,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx03
    with dissolve

    dad "apoyada por su amado marido,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    dad "que sufre en silencio el mismo lamento."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "rodeada de tantas lápidas con niños que sufrieron el mismo destino."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 6
    call neus_exp_tears_tears
    show neus_exp_iris front06
    show neus_exp_eyebrows sadx07
    with fade

    ne "..."

    #

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with fade

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Puedes imaginarte semejante dolor?"

    if night05_NeusLastDate_HotelKrueger_Door_Used_Number > 1:

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Eso sin contar las voces que oíste al poco de salir de esas habitaciones..."

        show m_exp_mouth sad_Talkingx002
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows serious
        with dissolve

        dad "Que no son más que ecos de un destino parecido,"

        extend " perdidos en el tiempo."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "¿A cuanto sumaría entonces el número de gritos de desesperación,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows sadx01
    with dissolve

    dad "de lamentos,"

    extend " de víctimas,"

    extend " de sacrificios...?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "¿Qué clase de pecado justifica semejante castigo?"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    dad "¿Dónde está la justicia divina?"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "El Karma,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "o como lo quieras llamar..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "¿Qué clase de monstruo es capaz de hacer semejantes atrocidades?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with Dissolve(0.5)

    menu:

        pt "Dijo el padre de los monstruos..."

        "¡Cómo sé que no eres tú mismo el responsable de todas estas barbaridades?!":
            call p_Help
            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Por favor,"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "ni dudes un instante que sería capaz de esto,"

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx01
            with dissolve

            dad "y de mucho más..."

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Pero por desgracia,"

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Por desgracia,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris down04
    show m_exp_eyebrows suspiciousx01
    with dissolve
    
    tx" debido a mi condición incorpórea,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "no soy capaz de llevar a cabo estas fechorías,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "no..."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "alguien las tiene que llevar a cabo en mi lugar,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    dad "para complacer a mis queridas criaturas oscuras."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx05
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx03
    with fade

    p "..."

    show neus_exp_mouth sad_Silentx04
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with Dissolve(0.5)

    dad "Durante décadas,"

    show neus_exp_mouth sad_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with Dissolve(0.5)

    dad " a centenares de madres,"

    extend " hijos,"

    extend " hijas,"

    extend " esposas..."

    show neus_exp_mouth sad_Silentx08
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris front05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with fade

    menu:

        pt "¿A dónde quiere ir a parar?"

        "Me niego a creer tus sucias mentiras.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "..."

            jump afternight05_Pedrera_NeusIsNotLikeThat_Before

        "¡Te equivocas! ¡[neusname] no es así!":
            call p_Help

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "..."

            jump afternight05_Pedrera_NeusIsNotLikeThat_Before

        "...":
            call p_Help

            jump afternight05_Pedrera_NeusIsNotLikeThat

    ne "..."

    jump afternight05_Pedrera_NeusIsNotLikeThat_Before

label afternight05_Pedrera_NeusIsNotLikeThat_Before:

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    $ meyesc = "_goat"

    dad "Ohh..."

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "¿Pero realmente no empiezas a dudarlo?"

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    ne "..."

    $ meyesc = "_red"

    jump afternight05_Pedrera_NeusIsNotLikeThat

label afternight05_Pedrera_NeusIsNotLikeThat:

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    pt "[neusname]..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with fade

    pt "no..."

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with fade

    menu:

        "¡Fuiste tú quien la obligaste a llevar a cabo todas estas monstruosidades!":
            call p_Help

            $pl.ch_pts("np",3)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            p "¡Por eso huyó!"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¡Porque el monstruo eres tú!"

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex001
            with dissolve

            p "¡No ella!"

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Imaginemos en parte,"

            extend " que quizás tengas un ápice de razón."

            jump afternight05_Pedrera_DadInfluence

        "No me creo nada de lo que me estás contando.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex002
            with dissolve

            ne "..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Entonces sería mejor que se lo preguntaras a ella."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

            jump afternight05_Pedrera_DadInfluence

        "...":
            call p_Help

            jump afternight05_Pedrera_DadInfluence

label afternight05_Pedrera_DadInfluence:

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Ten en cuenta,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "que fuera de dos días al año,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "no puedo influir en ellas directamente,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "tienen trescientos sesenta y tres días de libre albedrío,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    dad "con lo que realmente,"

    extend " son ellas quienes eligen a sus víctimas,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "y el modo en que los sacrifican."

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx04
    with fade

    p "..."

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    dad "Mi querida {i}Txiki{/i},"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows sadx01
    with fade

    dad "es sin duda,"

    extend " una de mis hijas favoritas,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y no únicamente por su adorable sonrisa,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "especialmente cuando está impregnada de sangre..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    dad "No,"

    extend " no solo por eso."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "También porque tiene la habilidad de encandilar a su víctimas de tal modo,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "que suelen caer en sus encantos,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "sentir verdaderos sentimientos hacia ella."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Y una vez en el sacrificio;"

    extend " el pesar,"

    extend " el dolor,"

    extend " la angustia,"

    extend " la traición;"

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "la incredulidad de la persona amada..."

    show m_exp_mouth happybiting_Silentx05
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Mmmmmm..."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Como echo de menos esos rostros,"

    extend " esos llantos"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "esas palabras incrédulas de súplica,"

    extend " de clemencia..."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx03
    with dissolve

    dad "Preguntándose el por qué;"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "el cómo su amada ha sido capaz de lanzarlo a las llamas..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Cuando creían que mi {i}Txiki{/i},"

    show m_exp_mouth happy_Talkingx12
    show m_exp_eyes 06
    show m_exp_piris front06
    show m_exp_eyebrows sadx01
    with dissolve

    dad "era el amor de sus vidas."

    show m_exp_mouth happy_Silentx10
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx06
    with fade

    p "..."

    $ meyesc = "_red"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with fade

    dad "¿Crees que es difícil de creer?"

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Al fin y al cabo,"

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "ha sido capaz de convencerte a ti también."

    show m_exp_mouth happy_Silentx14
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    $ meyesc = "_red"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex002
    with dissolve

    ne "No..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx08
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with fade

    ne "¡En eso no le he mentido!"

    show neus_exp_mouth sad_Talkingx10
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "¡A él no!"

    show neus_exp_mouth sad_Silentx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows serious
    with Dissolve(0.5)

    menu:

        pt "¿A mí no?"

        "¡¿Y al resto?!":
            call p_Help
            #$pl.ch_pts("np",-1)

            show neus_exp_mouth sad_Silentx04
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows normal
            with dissolve

            ne "..."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            jump afternight05_Pedrera_NeusNeeds

        "¡[neusname]! No le sigas el juego.":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with Dissolve(0.5)

            jump afternight05_Pedrera_NeusNeeds

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            ne "..."

            jump afternight05_Pedrera_NeusNeeds

label afternight05_Pedrera_NeusNeeds:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with fade

    dad "Hmm..."

    show m_exp_mouth sad_Talkingx002
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Verás,"

    if music_play != "sadTrio":
        play music "audio/music/kevinmacleod/sad/sadTrio.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "sadTrio"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "tengo la teoría de que mi hija,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "o sea,"

    extend " tu hermana,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "tiene la extraña necesidad de sentirse..."

    extend " amada."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "Supongo que mi amor por ella no le basta."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "así que busca en otros,"

    extend " ese reclamo."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "un requerimiento banal y absurdo si me preguntas,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "pues apenas le puede llegar a durar unos míseros seis meses,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx01
    with dissolve

    dad "siendo muy optimistas..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Pero además en su caso,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "completamente artificial."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "pues siempre les encandila con una imagen de si misma muy distinta a la que ves ahora."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "De esa clase de imagen,"

    extend " de la que quizás sí es más fácil sentirte atraído."

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "O me dirás que no te llamó la atención esa mujer voluptuosa que viste en la recepción del hotel?"

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex001
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Esa clase de mujer que te quita el hipo."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Dinero,"

    extend " poder,"

    extend " y belleza..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "Una combinación letal."

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "¿No te parece?"

    show m_exp_mouth happy_Silentx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex002
    with dissolve

    menu:

        pt "¿Debería responderle?"

        "<Reprocharle que lejos de él, [neusname] es una persona completamente distinta>":
            call p_Help

            $pl.ch_pts("np",2)

            if music_play != "almost_new_kevin":
                play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "almost_new_kevin"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            p "¡Dirás lo que quieras sabandija!"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex02
            with dissolve

            p "Pero está demostrado que lejos de ti,"

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            p "[neusname] puede ser una persona completamente distinta."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "¿Eso crees...?"

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

            p "¡Sí!"

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex02
            with dissolve

            p "¡Lo creo!"

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows normal
            with dissolve

            dad "Vaya,"

            extend " vaya..."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Supongamos que tienes razón;"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows normal
            with dissolve

            dad "y efectivamente ha estado más de un año lejos de mi,"

            jump afternight05_Pedrera_FarFromDad

        "...":
            call p_Help

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Hmmm..."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 03
            show m_exp_piris right03
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Mi querida {i}Txiki{/i},"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows sadx01
            with dissolve

            dad "ha estado ya más de un año lejos de mi,"

    
label afternight05_Pedrera_FarFromDad:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "y de sus queridas hermanas,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    dad "tiempo más que suficiente,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "para perder la influencia de mis queridos amiguitos de ojos rojizos,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    dad "sin sacrificar a ningún humano,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "perdiendo así sus poderes,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    dad "Y poco a poco,"

    extend " su habilidad de transformar su figura."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    dad "Alejada de esta influencia,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "apenas sería otra chica inofensiva más."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "Pero sin embargo,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "fue capaz de convertir a tu amigo en una mujer,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y no solo durante unos minutos,"

    if music_play != "chamber":
        play music "audio/music/kevinmacleod/chamber.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "chamber"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "sino ni más ni menos,"

    extend " que durante tres días."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Te aseguro que eso no es una ofrenda fácil de pedir a mi amiguitos oscuros."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "No..."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "El sacrificio a ofrecer,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "tiene que estar a la altura de lo que se pide,"

    show m_exp_mouth happy_Talkingx12
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "o incluso más."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Especialmente cuando hace tanto tiempo que los has dejado de lado."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with fade

    dad "¿No te preguntas qué sacrificó para poder transformar a tu amigo en mujer,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "durante estos tres días?"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Te aseguro que con insectos,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "ratas,"

    extend " conejos,"

    extend " o mamíferos de mayor tamaño,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "necesitaría sacrificar centenares de hectáreas en bosques;"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "y lo más probable es que ni así les bastara."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Ni aunque sacrificara a una docena de indigentes,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "seguramente tampoco sería suficiente."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "No..."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    dad "No sé si te lo habrá contado,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "pero el jugo del sacrificio no está en la persona ejecutada,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "no..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "De ahí se alimentan otras criaturas,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "de las cuales puedo sacarles algún rédito,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    dad "pero no..."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "mis amiguitos oscuros buscan otro tipo de alimento..."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    dad "de aquellos que siguen en pie,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "respirando,"

    extend " andando,"

    extend " llorando,"

    extend " lamentándose,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "preguntándose el por qué de lo sucedido,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "si hubieran podido evitarlo,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx02
    with dissolve

    dad "recordando las últimas palabras,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows sadx03
    with dissolve

    dad "si terminaron discutiendo y no pudieron despedirse,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows sadx04
    with dissolve

    dad "durante días,"

    extend " semanas,"

    extend " años,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris left01
    show m_exp_eyebrows sadx02
    with dissolve

    dad "o incluso décadas..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx02
    with dissolve

    dad "de las personas que amaron a aquellos que ya no están."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx03
    with dissolve

    dad "Ese dolor,"

    extend " esa angustia,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    dad "es lo que alimenta a mis queridas criaturas."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx03
    with dissolve

    dad "Si matas a un animal,"

    extend " apenas llorará esa muerte su dueño."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows surprisex02
    with dissolve


    dad "Si matas a un indigente,"

    extend " quizás algún que otro compañero suyo sienta lástima."

    if music_play != "nervous":
        play music "audio/music/kevinmacleod/creepy/nervous.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nervous"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "Pero si sacrificas a alguien conocido,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "que además aparezca en los medios de comunicación,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "amado por centenares,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "millares,"

    extend " quizás incluso más;"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "y si además es un ser diminuto,"

    extend " e inocente."

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "Ahí no necesitas una montaña de cadáveres,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "con uno solo basta."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with fade

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)


    p "..."

    menu:

        pt "¿Diminuto e inocente que haya salido en los medios de comunicación?"

        "No... no te creo.":
            call p_Help

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with fade

            jump afternight05_Pedrera_InnocentVictim

        "¿De quien estás hablando...?":
            call p_Help

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with fade

            jump afternight05_Pedrera_InnocentVictim

        "...":
            call p_Help

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with fade

            jump afternight05_Pedrera_InnocentVictim

label afternight05_Pedrera_InnocentVictim:

    dad "..."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Oh,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "vamos..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Seguro que a estas alturas ya te imaginarás de quien estoy hablando."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Lo habrás visto en las noticias,"

    extend " en el metro,"

    extend " en las paredes..."

    show m_exp_mouth happy_Silentx10
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth happy_Silentx12
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx02
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    menu:

        pt "Tiene que ser otra ilusión, [neusname] no..."

        "No. [neusname] no sería capaz.":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            jump afternight05_Pedrera_InnocentVictim_Procedure

        "¡No me creo una mierda de lo que me estás contando!":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            jump afternight05_Pedrera_InnocentVictim_Procedure

        "[neusname], Dime que es mentira.":
            call p_Help

            show neus_exp_mouth sad_Silentx08
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with Dissolve(0.5)

            jump afternight05_Pedrera_InnocentVictim_Procedure

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            jump afternight05_Pedrera_InnocentVictim_Procedure

label afternight05_Pedrera_InnocentVictim_Procedure:

    ne "..."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with Dissolve(0.5)

    dad "Bueno,"

    if music_play != "crypticSorrow":
        play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "crypticSorrow"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with fade

    dad "confieso que hacerlo durante el día,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "fue una jugada arriesgada,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "pues a la luz del sol,"

    extend " estos poderes son apenas útiles."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    dad "Pero a decir verdad,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "es la mejor hora para ocultarse de mi radar."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Aunque lo que tiene de arriesgado,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "en pocas palabras,"
    
    extend " lo tiene de simple."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "Uno pensaría que rodeada de tanta gente le resultaría imposible esconder a alguien;"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "pero en realidad es el mejor escondite para alguien con las habilidades que gozan mis hijas."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Lo primero que tuvo que hacer,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "probablemente,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows serious
    with dissolve

    dad "fue cambiar su propio rostro,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "por alguien que al pequeño le resultara familiar,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "protector incluso."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Luego,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "una vez a cierta distancia de sus padres,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows sadx01
    with dissolve

    dad "y de los cuerpos de seguridad,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "le debió cambiar su rostro angelical,"

    extend " por la de cualquier otro mocoso,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "y hacerle ver en su mente que se encontraba en otro sitio,"

    extend " un lugar seguro,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows normal
    with dissolve

    dad "quizás incluso junto a sus padres..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "Manipular la mente de un niño,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    dad "es tan fácil como convencerle,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows sadx02
    with dissolve

    dad "de que existe un gordo vestido de rojo,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "que reparte regalos alrededor del mundo,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "en un carro volador tirado por renos."

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001
    with dissolve

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx05
    with fade

    p "..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    dad "Luego me imagino que solo tuvo que esperar a que anocheciera un poco,"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with fade

    dad "para salir por la puerta principal,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "como cualquier otra turista,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "llevando a su hijo de la mano."

    show m_exp_mouth happy_Silentx11
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    menu:

        pt "¿Y qué hizo luego?"

        "[neusname], ¿Qué hiciste con el niño?":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            ne "..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            dad "¿Le preguntas si tuvo sexo con un menor?"

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            dad "Te preguntas si tuvo sexo con él."

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            dad "¿Verdad?"

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            p "..."


label afternight05_Pedrera_InnocentVictim_Execution:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with fade

    dad "No..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    dad "No lo creo,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "Nunca le ha gustado demasiado esta parte en nuestros {i}akelarres{/i}..."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Así como tampoco es de las que les gusta tragarse a sus víctimas mientras están vivas"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "para exprimir aún más el jugo del sacrificio."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    pause 0.2

    pt "¿¡Cómo dice?!"

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx09
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx06
    with fade

    p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with fade

    dad "Tampoco es algo que sea realmente necesario,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "así como tampoco lo es para los humanos practicar sexo,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "con métodos anticonceptivos,"

    extend " para evitar bastardos indeseados,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    dad "pero a veces no se trata solo de sobrevivir,"

    extend " sino también de gozar de la vida;"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "¿No crees?"

    show m_exp_mouth happy_Silentx09
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        "Eres un puto enfermo.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 07
            show m_exp_piris front07
            show m_exp_eyebrows sadx03
            with vpunch

            dad "JAJAJAJAJA"

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows sadx04
            with dissolve

            dad "No me hagas reír..."

            jump afternight05_Pedrera_InnocentVictim_After

        "...":
            call p_Help

            show m_exp_mouth happy_Silentx10
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "Hmm..."

            jump afternight05_Pedrera_InnocentVictim_After

label afternight05_Pedrera_InnocentVictim_After:

    show m_exp_mouth happy_Silentx12
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with fade

    menu:

        "¿Qué pasó con el niño...?":
            call p_Help

            show neus_exp_mouth sad_Silentx08
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            dad "¿Realmente hace falta que responda a esa pregunta?"

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris left03
            show neus_exp_eyebrows serious
            with Dissolve(0.5)

            dad "¿Acaso no ves a tu amigo transformado en mujer?"

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            dad "Si eso no te satisface,"

        "...":
            call p_Help

            show neus_exp_mouth sad_Silentx08
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            dad "Si tienes dudas sobre lo que le pasó al niño,"

label afternight05_Pedrera_InnocentVictim_AskNeus:

    show neus_exp_mouth sad_Silentx09
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris left00
    show neus_exp_eyebrows surprisex02
    with dissolve

    dad "pregúntale."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    menu:

        pt "No... no puede ser..."

        "[neusname], Dime que es mentira.":
            call p_Help

            $ afternight05_Pedrera_Vegan_TellMeIsALie = True

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with dissolve

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            ne "..."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with vpunch

            p "{size=40}¡DIME QUE ES MENTIRA!{/size}"

            show neus_exp_mouth sad_Talkingx002
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris right02
            show neus_exp_eyebrows sadx02
            with dissolve

            ne "Yo..."

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx04
            with dissolve

            p "¿¡Sacrificaste a un niño inocente para convertir a Dídac!?"

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx05
            with dissolve

            p "¿¡Quien acusaste de haberte intentado violar!?"

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx06
            with dissolve

            p "{size=30}¿¡Para chantajearme y salir conmigo!?{/size}"

            show neus_exp_mouth sad_Silentx10
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx07
            with vpunch

            p "{size=35}¡¡¿QUÉ CLASE DE MENTE RETORCIDA TIENES?!!{/size}"

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show neus_exp_mouth sad_Silentx09
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with dissolve

            dad "Hmm..."

            show neus_exp_mouth sad_Silentx07
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx06
            with dissolve

            dad "La misma que ha tenido siempre."

            jump afternight05_Pedrera_OneNeverChange

        "No tengo que preguntarle eso, [neusname] no sería capaz de hacer algo así.":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with dissolve

            dad "Ohh..."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx03
            with dissolve

            dad "¿Pero realmente la conoces?"

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx01
            with dissolve

            p "¡Lo suficiente como para saber que no tiene nada que ver contigo!"

            $ Pedrera_char_Cond = "TxellNeus"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows serious

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris left01
            show neus_exp_eyebrows sadx02
            with fade

            dad "¿Y realmente crees que es tan diferente de lo que fue hace apenas un año?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx05
            with dissolve

            p "Sí."

        "No voy a entrar en tu juego.":
            call p_Help

            show neus_exp_mouth happy_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx03
            with Dissolve(0.5)

            dad "Hmmm..."

            show neus_exp_mouth sad_Silentx06
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows serious
            with dissolve

            dad "Conozco a mi niña mucho mejor que tú."

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows sadx01
            with Dissolve(0.5)

            p "..."

        "...":
            call p_Help

label afternight05_Pedrera_OneNeverChange:

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with fade

    dad "Uno no cambia así como así..."

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx12
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows angryx01
    with dissolve

    dad "no después de siglos repitiendo el mismo patrón."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "Por mucho que se mienta a si misma,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx04
    with dissolve

    dad "Por mucho que se vista de inocente ovejita,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "sigue siendo mi lobita sangrienta,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "mi {i}Txiki{/i}."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    $ meyesc = "_red"

    show neus_exp_mouth sad_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows angryx01
    with fade

    pause 0.2

    menu:

        "[neusname], ¿Por qué me llevaste a ese restaurante vegano?":
            call p_Help

            if music_play != "bentAndBroken":
                play music "audio/music/kevinmacleod/creepy/bentAndBroken.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "bentAndBroken"

            show neus_exp_mouth sad_Silentx06
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows surprisex01
            with dissolve

            p "¿Por qué me dijiste que eras vegana?"

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx05
            with dissolve

            ne "..."

            menu:

                "¡¡Qué clase de vegana mataría a un niño a sangre fría?!":
                    call p_Help

                    $ afternight05_Pedrera_Vegan_ColdBlood = True

                    show neus_exp_mouth sad_Silentx09
                    $ nteye = 7
                    call neus_exp_tears_tears
                    show neus_exp_iris front07
                    show neus_exp_eyebrows sadx07
                    with vpunch

                    ne "..."

                    if ntlong in range (0,6):
                        if ntlong < 5:
                            $ ntlong += 1

                    show neus_exp_mouth sadbiting_Silentx06
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows sadx06
                    with dissolve

                    dad "Para ser justos,"

                    show neus_exp_mouth sadbiting_Silentx07
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx07
                    with dissolve

                    dad "ser vegano no te impide ser asesino en serie,"

                    show neus_exp_mouth sad_Silentx10
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris left05
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    dad "al menos en humanos."

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    ne "..."

                    show neus_exp_mouth sadbiting_Silentx07
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows sadx06
                    with dissolve

                "...":
                    call p_Help

            menu:

                "¡¿Acaso te importa más la vida de los animales que la de las personas?!":
                    call p_Help

                    $pl.ch_pts("np",-1)

                    $ afternight05_Pedrera_Vegan_AnimalsOverHumans = True

                    show neus_exp_mouth sad_Talkingx06
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows angryx02
                    with vpunch

                    ne "¡No!"

                    show neus_exp_mouth sad_Silentx08
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris front01
                    show neus_exp_eyebrows sadx01
                    with dissolve

                    p "¡¿Que la de los niños?!"

                    show neus_exp_mouth sad_Talkingx10
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris front02
                    show neus_exp_eyebrows angryx05
                    with vpunch

                    ne "¡Por supuesto que no!"

                    show neus_exp_mouth sadbiting_Silentx04
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris front01
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    p "¡¿Entonces?!"

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris front04
                    show neus_exp_eyebrows sadx03
                    with Dissolve(0.5)

                    ne "..."

                    show neus_exp_mouth sad_Silentx09
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows sadx06
                    with Dissolve(0.5)

                "...":
                    call p_Help

                    show neus_exp_mouth sad_Silentx09
                    $ nteye = 5
                    call neus_exp_tears_tears
                    show neus_exp_iris right05
                    show neus_exp_eyebrows sadx06
                    with Dissolve(0.5)

            p "..."

            jump afternight05_Pedrera_TwoBirdsOneShot


        "...":
            call p_Help


label afternight05_Pedrera_TwoBirdsOneShot:

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx03
    with Dissolve(0.5)

    dad "Mataba dos pájaros de un tiro."

    if music_play != "playWithMe":
        play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "playWithMe"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with fade

    dad "No necesitaba convencerte de que lo sobrenatural existe,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "tú mismo lo experimentarías con tus propios ojos,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx02
    with dissolve

    dad "al contemplar la transformación de tu amigo;"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "y además mediante el chantaje,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "conseguía de forma práctica el control absoluto de la situación,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "sin depender de tus deseos,"

    extend " ni de tus caprichos."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    dad "Tal y como a ella le gusta."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    ne "No..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx08
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows angryx03
    with fade

    ne "¡No quería controlar la situación!"

    show neus_exp_mouth sad_Talkingx06
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows angryx01
    with dissolve

    ne "Ni tampoco sus deseos..."

    show neus_exp_mouth sad_Talkingx002
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "Yo..."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris right03
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "solo quería que me diera la oportunidad de conocerme,"

    show neus_exp_mouth sad_Talkingx03
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris right04
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "al menos durante tres citas."

    show neus_exp_mouth sad_Talkingx001
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05
    with dissolve

    ne "Solo eso..."

    show neus_exp_mouth sad_Silentx07
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "Claaaro..."

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02

    show neus_exp_mouth sad_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with fade

    dad "Tenías miedo que al final de la primera cita,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows suspiciousx01

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "si hubieras tenido sexo con él,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx02

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows serious
    with dissolve

    dad "se hubiera asustado demasiado al ver que tienes transformaciones monstruosas y desagradables,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "especialmente con su esperma,"

    extend " y tu frenesí sexual;"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "y por lo contrario,"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with fade

    dad "si no hubiera habido sexo de por medio,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "temías que te desechara como a un trapo sucio,"

    extend " y se fuera a por otra."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Que lógica más aplastante."

    show m_exp_mouth happy_Silentx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex001
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx001
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx02
    with fade

    ne "No..."

    show neus_exp_mouth sad_Talkingx003
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with Dissolve(0.5)

    ne "Yo..."

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx07
    with Dissolve(0.5)

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows surprisex01
    with fade

    dad "Es mejor sacrificar a un niño inocente,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "convertir a su amigo en mujer como castigo por algo que provocaste tú misma,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "y asegurarse así,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "que acuda sí o sí a las tres citas mediante el chantaje,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "muy lista mi {i}Txiki{/i},"

    extend " muy lista..."

    if NeusCuckolded:

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx01
        with dissolve

        dad "Pero es que además,"

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx02
        with dissolve

        dad "tu amado hermanito,"

        if NeusCuckolded_Sexually:

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "ya se ha follado,"

            if DidacSex_Vaginal:

                $pl.ch_pts("np",-2)

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "al amigo de aquí atrás"

                show m_exp_mouth happy_Talkingx12
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows angryx01
                with dissolve

                dad "que tú misma convertiste en mujer;"

            if FuckM_Start_Cond:

                $pl.ch_pts("np",-3)

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 02
                show m_exp_piris frontdown02
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "a esta rubia tetuda;"

            if (DidacSex_Vaginal or FuckM_Start_Cond) and FuckH_Start_Cond:

                $pl.ch_pts("np",-2)

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "y hasta un asiático con polla."

            elif FuckH_Start_Cond:

                $pl.ch_pts("np",-2)

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "hasta a un asiático con polla."

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Imagínate lo brillante que fue tu plan."

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "De película vamos."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows angryx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx07
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx03
            with fade

            ne "..."

            show neus_exp_mouth sad_Silentx09
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            p "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex001
            with fade

            dad "Quizás olvidaste,"

            extend " que también es mi vástago;"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows sadx01
            with dissolve

            dad "y algo de mi sangre,"

            extend " también lleva."

        else:

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "ha jugueteado un poquito con el experimento que hiciste con su compañero de piso."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Aunque si me preguntas,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "yo hubiera ido algo más lejos,"

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "que parece que tengas doce años."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            menu:

                pt "De ti ya no me extraña nada."

                "Hice lo que hice para apoyarlo, no para aprovecharme de él.":
                    call p_Help
                    $pl.ch_pts("np",1)

                    show m_exp_mouth sad_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "No quería que lo apoyaras,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "lo que deseaba era tu polla."

                "...":
                    call p_Help
                    pass

    else:

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Por desgracia,"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows serious
        with dissolve

        dad "tu hermanito es tan imbécil,"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "que no ha sabido ni aprovecharse de la situación que le has brindado,"

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 03
        show m_exp_piris down03
        show m_exp_eyebrows surprisex001
        with dissolve

        dad "ni siquiera de esta rubia con este par de buenas razones."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "¿No será que eres de la otra acera?"

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        menu:

            p "¡¿Y qué coño le importa si soy gay?!"

            "Con [neusname] no necesito a nadie más.":
                call p_Help

                $ afternight05_Pedrera_TwoBirdsOneShot_IOnlyNeedNeus = True

                $pl.ch_pts("np",5)

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows serious

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with fade

                ne "..."

                if ntlong in range (0,6):
                    if ntlong > 0:
                        $ ntlong -= 1

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "¿Después de todo lo que te he contado?"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows angryx02

                show neus_exp_mouth sad_Silentx02
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx03
                with dissolve

                dad "No eres tan diferente de mi como crees,"

                extend " entonces."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with fade

                p "Eso será tu retorcida opinión."

                jump afternight05_Pedrera_NeusBothDirections

            "Responderte es una pérdida de tiempo.":
                call p_Help

                $pl.ch_pts("np",2)

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with dissolve

                dad "¿Realmente crees que te estoy mintiendo?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with dissolve

                p "Piensa lo que quieras."

                jump afternight05_Pedrera_NeusBothDirections

            "No te importa una mierda.":
                call p_Help

                $pl.ch_pts("np",1)

                show m_exp_mouth sad_Talkingx003
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx02
                with dissolve

                dad "¿Crees que es inteligente provocarme?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows serious
                with dissolve

                p "No te tengo miedo."

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Deberías."

            "...":
                call p_Help

                jump afternight05_Pedrera_RealParents

label afternight05_Pedrera_NeusBothDirections:

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Hmmm..."

        if music_play != "playWithMe":
            play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "playWithMe"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "Quizás te van las dos direcciones,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "Mi {i}Txiki{/i} tiene esa habilidad,"

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows sadx01
        with dissolve

        dad "ya imagino que te lo habrá contado."

        show m_exp_mouth happy_Silentx07
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows serious
        with dissolve

        menu:

            "No solo me lo ha contado, sino me encantaría probarlo." if night05_Interrogation_GrowYouADick_Cond:
                call p_Help

                $pl.ch_pts("np",4)

                $ night05_Interrogation_GrowYouADick_LikeToTry = True

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                if music_play != "darkestChild":
                    play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "darkestChild"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 00
                show m_exp_piris front00
                show m_exp_eyebrows surprisex02

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows surprisex01
                with fade

                dad "..."

                if ntlong in range (0,6):
                    if ntlong > 0:
                        $ ntlong -= 1

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx02

                show neus_exp_mouth happybiting_Silentx02
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris right01
                show neus_exp_eyebrows surprisex02
                with dissolve

                ne "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx02
                with fade

                dad "¿Qué clase de hijo degenerado he engendrado?"

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Sino fuera porque sé que has dicho eso en un tono más sumiso que dominante,"

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx02
                with dissolve

                dad "hasta podría sentirme orgulloso de ti."

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows serious
                with dissolve

                p "Me importa tres cojones lo que opines."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "..."

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Supongo que eso confirma mi teoría."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                p "..."

                jump afternight05_Pedrera_NeusBothDirections_NeusPlain

            "Sí, me lo ha contado y no tengo ningún problema en ello." if night05_Interrogation_GrowYouADick_Cond:
                call p_Help

                $pl.ch_pts("np",3)

                if music_play != "darkestChild":
                    play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "darkestChild"

                $ night05_Interrogation_GrowYouADick_NotAProblem = True

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sad_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with fade

                dad "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                if FuckM_Start_Cond: # FOR FUTURE for future when Passive sex is done.

                    #$pl.ch_pts("np",-3)

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows normal
                    with fade

                    dad "Después de lo que has hecho con esta rubia,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    dad "tampoco me extraña..."

                else:

                    $pl.ch_pts("np",3)

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows suspiciousx01
                    with fade

                    dad "¿No será que empieza a gustarte más usar la puerta de atrás?"

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    p "No es de tu incumbencia."

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex002
                    with dissolve

                    dad "Que decepción de hijo..."

                jump afternight05_Pedrera_NeusBothDirections_NeusPlain

            "Sí, lo sé, pero a pesar de ello, no me importa." if night05_Interrogation_GrowYouADick_Cond:
                call p_Help

                $pl.ch_pts("np",1)

                $ night05_Interrogation_GrowYouADick_DontBotherYou =True

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sad_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows surprisex01
                with fade

                dad "..."

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx02


                show neus_exp_mouth happy_Silentx04
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "..."

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows normal
                with dissolve

                dad "{i}A pesar de ello{/i}..."

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex001
                with dissolve

                dad "Eso significa,"

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows suspiciousx02

                show neus_exp_mouth sad_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "que realmente no te gustaría verla con el elefante al aire,"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows sadx02
                with dissolve

                dad "¿verdad?"

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx02

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx03
                with dissolve

                p "..."

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex002

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows normal
                with dissolve

                dad "¿Pero qué pasaría si a mi {i}\"Txiki\"{/i},"

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows surprisex01
                with dissolve

                dad "le diera por juguetear un poco con tu trasero,"

                show m_exp_mouth sad_Talkingx005
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex002

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris left00
                show neus_exp_eyebrows surprisex02
                with dissolve

                dad "con su plátano?"

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sad_Talkingx09
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "¡Nunca le forzaría a ello!"

                if night05_Interrogation_EnjoyMoreDickOrPussy_Cond:

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows normal

                    show neus_exp_mouth sad_Talkingx07
                    $ nteye = 2
                    call neus_exp_tears_tears
                    show neus_exp_iris left02
                    show neus_exp_eyebrows angryx01
                    with dissolve

                    ne "Además,"

                    extend " ya le he dicho que es algo que tampoco me entusiasma."

                    show m_exp_mouth happy_Talkingx04
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows suspiciousx01

                    show neus_exp_mouth sadbiting_Silentx02
                    $ nteye = 1
                    call neus_exp_tears_tears
                    show neus_exp_iris left01
                    show neus_exp_eyebrows surprisex01
                    with dissolve

                    dad "Te he visto usarlo bastantes veces esta última década,"

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris right04
                    show m_exp_eyebrows serious

                    show neus_exp_mouth sad_Silentx08
                    $ nteye = 8
                    call neus_exp_tears_tears
                    show neus_exp_iris front08
                    show neus_exp_eyebrows angryx02
                    with dissolve

                    dad "así que no me vengas con que no te gusta usarlo."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sad_Talkingx08
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx02
                with dissolve

                ne "Prefiero cien veces ser penetrada por su pollón que cualquier otra cosa."

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows normal

                show neus_exp_mouth sad_Silentx07
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows angryx03
                with dissolve

                dad "..."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex001

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows serious
                with dissolve

                dad "Apenas hace tres días que lo conoces en persona,"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows surprisex002

                show neus_exp_mouth sadbiting_Silentx01
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows surprisex01
                with dissolve

                dad "y ya crees que podrás amarle de por vida,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sad_Silentx06
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx01
                with dissolve

                dad "sin tener fantasías más allá de las que él pueda aceptar?"

                show m_exp_mouth happy_Talkingx10
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sad_Silentx07
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows angryx02
                with dissolve

                dad "¿Realmente crees que no caerás en la tentación?"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows normal

                show neus_exp_mouth sad_Talkingx08
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx04
                with dissolve

                ne "¡Por supuesto que no!"

                show m_exp_mouth sad_Talkingx005
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows surprisex02
                with dissolve

                dad "¿Y de verdad piensas que él no sucumbirá a tus espaldas,"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows sadx01

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows normal
                with dissolve

                dad "a los encantos de una mujer de verdad?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with dissolve

                ne "..."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx02

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx04
                with dissolve

                menu:

                    pt "Maldito seas..."

                    "Por supuesto que no. Le seré fiel toda mi eternidad.":
                        call p_Help

                        $pl.ch_pts("np",3)

                        $ night05_Interrogation_GrowYouADick_EternalLove_Cond = True

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx02

                        show neus_exp_mouth happy_Silentx02
                        $ nteye = 2
                        call neus_exp_tears_tears
                        show neus_exp_iris front02
                        show neus_exp_eyebrows surprisex01
                        with dissolve

                        dad "..."

                        if afternight05_Pedrera_Vegan_TellMeIsALie:

                            $ Pedrera_char_Cond = "TxellClose"
                            call Pedrera_char_lab

                            show m_exp_mouth sad_Talkingx04
                            show m_exp_eyes 08
                            show m_exp_piris front08
                            show m_exp_eyebrows surprisex001
                            with fade

                            dad "Después de saber que le importan más los animales que los humanos"

                            show m_exp_mouth happy_Talkingx05
                            show m_exp_eyes 05
                            show m_exp_piris front05
                            show m_exp_eyebrows suspiciousx02
                            with dissolve

                            dad "¿cuanto crees que tardará en desecharte como si fueras un trapo sucio?"

                            $ Pedrera_char_Cond = "TxellNeus"
                            call Pedrera_char_lab

                            show m_exp_mouth sad_Silentx04
                            show m_exp_eyes 04
                            show m_exp_piris right04
                            show m_exp_eyebrows normal

                            show neus_exp_mouth sad_Talkingx08
                            $ nteye = 1
                            call neus_exp_tears_tears
                            show neus_exp_iris left01
                            show neus_exp_eyebrows angryx03
                            with fade

                            ne "¡Nunca he dicho que me importen más los animales que los humanos!"

                            show neus_exp_mouth sadbiting_Silentx05
                            $ nteye = 2
                            call neus_exp_tears_tears
                            show neus_exp_iris left02
                            show neus_exp_eyebrows serious
                            with dissolve

                            dad "Hay hechos que hablan mejor que las palabras,"

                            extend "mi pequeña."

                            show neus_exp_mouth sad_Silentx07
                            $ nteye = 3
                            call neus_exp_tears_tears
                            show neus_exp_iris left03
                            show neus_exp_eyebrows angryx01
                            with dissolve

                            ne "..."

                            show neus_exp_mouth sad_Silentx06
                            $ nteye = 4
                            call neus_exp_tears_tears
                            show neus_exp_iris front04
                            show neus_exp_eyebrows serious
                            with dissolve

                            dad "Hmm..."

                            show neus_exp_mouth sad_Silentx05
                            $ nteye = 1
                            call neus_exp_tears_tears
                            show neus_exp_iris left01
                            show neus_exp_eyebrows serious
                            with dissolve

                            dad "Eternidad dices..."

                        $ Pedrera_char_Cond = "TxellClose"
                        call Pedrera_char_lab

                        show m_exp_mouth happy_Talkingx08
                        show m_exp_eyes 02
                        show m_exp_piris front02
                        show m_exp_eyebrows surprisex01
                        with fade

                        dad "No tienes ni idea del verdadero significado de esa palabra."

                        show m_exp_mouth sad_Silentx04
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        p "Eso será tu opinión."

                        show m_exp_mouth happy_Talkingx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows normal
                        with dissolve

                        dad "Eso es mi experiencia."

                        show m_exp_mouth sad_Silentx05
                        show m_exp_eyes 01
                        show m_exp_piris front01
                        show m_exp_eyebrows surprisex01
                        with dissolve

                        p "Que no será como la mía."

                        show m_exp_mouth sad_Talkingx05
                        show m_exp_eyes 08
                        show m_exp_piris front08
                        show m_exp_eyebrows normal
                        with dissolve

                        dad "Si sigues vivo dentro de unos cuantos siglos,"

                        show m_exp_mouth happy_Talkingx06
                        show m_exp_eyes 04
                        show m_exp_piris front04
                        show m_exp_eyebrows serious
                        with dissolve

                        dad "podremos discutir este tema con más seriedad."

                        show m_exp_mouth happy_Silentx05
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows angryx01
                        with dissolve

                        p "..."

                    "Lo que pase entre nosotros, no es de tu incumbencia.":
                        call p_Help

                        $pl.ch_pts("np",1)

                        show m_exp_mouth sad_Silentx03
                        show m_exp_eyes 05
                        show m_exp_piris front05
                        show m_exp_eyebrows suspiciousx01
                        with dissolve

                        dad "..."

                    "...":
                        call p_Help

                #dad "Hmm..."

                jump afternight05_Pedrera_NeusBothDirections_NeusPlain

            "Sí, es algo asqueroso, no te lo voy a negar." if night05_Interrogation_GrowYouADick_Cond:
                call p_Help

                $pl.ch_pts("np",-1)

                $ night05_Interrogation_GrowYouADick_Disgusting_Cond = True

                if music_play != "nervous":
                    play music "audio/music/kevinmacleod/creepy/nervous.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "nervous"

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "..."

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx02
                with Dissolve(0.5)

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx03
                with fade

                dad "Hmmm..."

                if ntlong in range (0,6):
                    if ntlong < 5:
                        $ ntlong += 1

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with Dissolve(0.5)

                ne "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex001
                with fade

                dad "Al menos eres sincero,"

                show m_exp_mouth happy_Talkingx10
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx01
                with dissolve

                dad "eso no te lo voy a negar."

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious
                with dissolve

                pause 0.2

                jump afternight05_Pedrera_NeusBothDirections_NeusPlain

            "¡¿Cómo dices?!" if night05_Interrogation_GrowYouADick_Cond == False:
                call p_Help

                $pl.ch_pts("np",-1)

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "Oh,"

                show m_exp_mouth happy_Talkingx10
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows serious
                with dissolve

                dad "vamos..."

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows normal
                with dissolve

                dad "No esperarías que te contara algo así en la primera cita,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "¿Verdad?"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Estas cosas son mejores explicarlas cuando ya te tiene bien caliente,"

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex001
                with dissolve

                dad "y a punto de caramelo..."

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "¿Verdad que sí?"

                extend " mi Txiki."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious
                with dissolve

                ne "No..."

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Talkingx07
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx03
                with fade

                ne "Nunca hubiera hecho nada que él no hubiese querido."

                show neus_exp_mouth sad_Talkingx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows angryx01
                with dissolve

                ne "Además,"

                show neus_exp_mouth sad_Talkingx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows angryx02
                with dissolve

                ne "sabes que es algo que no disfrutamos en exceso,"

                show neus_exp_mouth sad_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows serious
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sad_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris left04
                show neus_exp_eyebrows serious
                with fade

                dad "Hablarás por ti,"

                extend " querida."

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows sadx02

                show neus_exp_mouth sad_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris left05
                show neus_exp_eyebrows sadx01
                with dissolve

                dad "Sabes de sobra lo mucho que lo gozan algunas de tus hermanas."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows serious

                show neus_exp_mouth sad_Talkingx09
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows angryx03
                with dissolve

                ne "¡Pero no yo!"

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows surprisex001

                show neus_exp_mouth sad_Silentx09
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris left03
                show neus_exp_eyebrows angryx02
                with dissolve

                dad "Quizás físicamente no te complazca en exceso,"

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex02

                show neus_exp_mouth sad_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris left02
                show neus_exp_eyebrows serious
                with dissolve

                dad "pero desde luego,"
                
                extend " te he visto regodearte como pocas veces,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows surprisex002

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris left00
                show neus_exp_eyebrows surprisex02
                with dissolve

                dad "cuando lo usabas para sodomizar a ciertas víctimas."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows serious

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "..."

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx02

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx05
                with dissolve

                dad "Te conozco bien,"

                extend " mi {i}Txiki{/i}."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx09
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx03
                with fade

                p "..."

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows normal
                with dissolve

                if afternoon05_Library_Continue_Cond:

                    pt "¿Sería lo que Txell me contó en la biblioteca...?"

                else:

                    pt "¡¿De qué está...?!"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Hmm..."

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Tienes tanto que aprender,"

                jump afternight05_Pedrera_RealParents

            "No es de tu incumbencia." if night05_Interrogation_GrowYouADick_Cond:
                call p_Help

                $pl.ch_pts("np",1)

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows serious
                with dissolve

                p "Y aunque así fuera,"

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex01
                with dissolve

                p "tampoco tendría por que avergonzarme de ello."

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "Defendiendo a la chica."

                if NeusCuckolded_Sexually:

                    $pl.ch_pts("np",-1)

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    dad "Uno tiene que proteger a su harén..."

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "¿Verdad?"

                    show m_exp_mouth happy_Silentx08
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris right02
                show m_exp_eyebrows surprisex002
                with dissolve

                dad "Pero mírala..."

                jump afternight05_Pedrera_NeusBothDirections_NeusPlain


            "...":
                call p_Help

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Tienes mucho que aprender,"

                jump afternight05_Pedrera_RealParents

label afternight05_Pedrera_NeusLoveDoubts:

    $ afternight05_Pedrera_NeusLoveDoubts_Cond = True

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿No te carcome pensar,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "que en realidad está contigo,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "porque en tu entrepierna,"

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "tienes lo único que puede evitar que la encuentre?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    if pl.np > 120:

        ne "¡Eso es mentira!"

    else:

        ne "¡Eso no es verdad!"

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious

    show neus_exp_mouth sad_Talkingx07
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows angryx03
    with fade

    ne "¡Sabes que hubiera podido convertirlo en piedra,"

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx09
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "esconderlo en un almacén,"

    show neus_exp_mouth sad_Talkingx08
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "y usarlo para recolectar el esperma cuando me hiciera falta!"

    show neus_exp_mouth sad_Talkingx10
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "¡Si hubiera hecho lo que he aprendido de ti,"

    show neus_exp_mouth sad_Talkingx09
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows angryx04
    with dissolve

    ne "no me hubiera hecho falta tener tres citas para conocerlo!"

    show neus_exp_mouth sad_Talkingx11
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows angryx05
    with dissolve

    ne "¡Pero yo no soy como tú!"

    show neus_exp_mouth sad_Talkingx004
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx01
    with dissolve

    ne "¡Realmente quería conocerlo!"

    if pl.np > 120:

        show neus_exp_mouth sad_Talkingx07
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows angryx02
        with dissolve

        ne "¡¿Y sabes una cosa?!"

        show neus_exp_mouth sad_Talkingx09
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris left05
        show neus_exp_eyebrows angryx03
        with dissolve

        ne "¡No se parece en nada a ti!"

        if pl.np > 150:

            show neus_exp_mouth sad_Talkingx004
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris left02
            show neus_exp_eyebrows angryx04
            with dissolve

            ne "¡Absolutamente en nada!"

    show neus_exp_mouth sad_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx03
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx04
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows normal
    with dissolve

    p "¿Convertirme en piedra?"

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex02
    with dissolve

    p "¡¿Esconderme en un almacén para recolectar mi esperma?!"

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris front02
    show neus_exp_eyebrows sadx02
    with dissolve

    p "¡¿QUÉ?!"

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx003
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx02
    with dissolve

    ne "No..."

    show neus_exp_mouth sad_Talkingx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris right02
    show neus_exp_eyebrows sadx03
    with dissolve

    ne "No hagas caso de lo que acabo de decir..."

    if pl.np > 120:

        show neus_exp_mouth happy_Talkingx03
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with dissolve

    else:

        show neus_exp_mouth sad_Talkingx03
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with dissolve


    ne "Nunca te haría eso [protname]..."

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows surprisex01
    with vpunch

    dad "¡JAJAJAJA!"

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sad_Silentx08
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx02
    with fade

    dad "Siempre y cuando le vayas dando de comer,"

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows suspiciousx01
    with fade

    dad "y no la hagas enfadar demasiado..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Medios tiene para hacer eso;"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "o algo peor."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Que no te engañe su inocente rostro,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows normal
    with dissolve

    dad "es una loba vestida de inocente ovejita,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "que no te quepa la menor duda."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx08
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx02
    with fade

    ne "..."

    show neus_exp_mouth sad_Silentx09
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows angryx03
    with dissolve

    dad "Pero realmente,"

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows angryx02
    with dissolve

    dad "¿Qué te hace pensar que está contigo por cómo eres,"

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris left01
    show neus_exp_eyebrows serious
    with dissolve

    dad "y no por ser quien eres,"

    extend " y por tener lo que tienes entre las piernas?"

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 1
    call neus_exp_tears_tears
    show neus_exp_iris front01
    show neus_exp_eyebrows sadx01
    with dissolve

    dad "¿De verdad crees que eso es amor?"

    show neus_exp_mouth sad_Silentx06
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows angryx02
    with dissolve

    dad "¿O es interés...?"

    if pl.np > 100:

        show neus_exp_mouth sad_Talkingx08
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris left01
        show neus_exp_eyebrows angryx03
        with dissolve

        ne "¡No!"

        if ntlong in range (0,6):
            if ntlong > 5:
                $ ntlong -= 1

        show neus_exp_mouth sad_Talkingx09
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris left03
        show neus_exp_eyebrows angryx04
        with dissolve

        ne "¡No estoy con él por simple interés!"

        if music_play != "musicForManatees":
            play music "audio/music/kevinmacleod/happy/musicForManatees.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "musicForManatees"

        show neus_exp_mouth happy_Talkingx04
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx04
        with Dissolve(0.5)

        ne "Es mucho mejor persona de lo que me había dicho."

        show neus_exp_mouth happy_Silentx04
        $ nteye = 6
        call neus_exp_tears_tears
        show neus_exp_iris front06
        show neus_exp_eyebrows sadx05
        with dissolve

        pt "¿De lo que le había dicho?"

        show neus_exp_mouth happy_Silentx05
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris front05
        show neus_exp_eyebrows sadx06
        with dissolve

        pt "¡¿Quien?!"

        show neus_exp_mouth sad_Talkingx01
        $ nteye = 3
        call neus_exp_tears_tears
        show neus_exp_iris left03
        show neus_exp_eyebrows sadx07
        with dissolve

        ne "y..."

        if pl.np > 140:

            show neus_exp_mouth happy_Talkingx03
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris front05
            show neus_exp_eyebrows sadx04
            with dissolve

            ne "me estoy enamorando perdidamente de él..."

            show neus_exp_mouth happy_Silentx02
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

        else:

            show neus_exp_mouth happy_Talkingx04
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx01
            with dissolve

            ne "me ha encantado pasar estas tres citas con él..."

            show neus_exp_mouth happy_Silentx02
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

        $ Pedrera_char_Cond = "TxellClose"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows suspiciousx01
        with fade

        dad "Hmmm..."

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows normal
        with dissolve

        dad "Pero la pregunta es,"

        if music_play != "QuinnsSongANewMan":
            play music "audio/music/kevinmacleod/sad/QuinnsSongANewMan.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "QuinnsSongANewMan"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows sadx01
        with dissolve

        dad "si te fuera mal con él..."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "O el sentimiento que sentís uno por el otro se desvaneciera..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "¿Qué otras alternativas tendrías?"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows suspiciousx02
        with dissolve

        $ Pedrera_char_Cond = "NeusClose"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris left01
        show neus_exp_eyebrows sadx01
        with fade

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows angryx04
        with Dissolve(0.5)

        ne "..."

        $ Pedrera_char_Cond = "TxellClose"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows sadx01
        with dissolve

        dad "Solo puedes sobrevivir conmigo,"

        extend " o con él."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris right03
        show m_exp_eyebrows sadx01
        with dissolve

        dad "Y seamos sinceros,"

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows surprisex001
        with dissolve

        dad "te conformarías hasta con un viejo verde,"

        extend " gordo,"

        extend " y seboso,"

        show m_exp_mouth happy_Talkingx10
        show m_exp_eyes 02
        show m_exp_piris right02
        show m_exp_eyebrows angryx03
        with dissolve

        dad "que se dedica a maltratar animales,"

        show m_exp_mouth happy_Talkingx11
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx02
        with dissolve

        dad "y a violar a menores de edad;"

        show m_exp_mouth sad_Talkingx006
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows surprisex001
        with dissolve

        dad "Antes de recibir el castigo que sabes que voy a darte,"

        show m_exp_mouth happy_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows sadx01
        with dissolve

        dad "por haber escapado."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 05
        show m_exp_piris right05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "NeusClose"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris left02
        show neus_exp_eyebrows sadx01
        with fade

        show neus_exp_mouth sadbiting_Silentx06
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris left04
        show neus_exp_eyebrows sadx04
        with Dissolve(0.5)

        ne "..."

        $ Pedrera_char_Cond = "TxellNeus"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows surprisex001

        show neus_exp_mouth sadbiting_Silentx03
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
        with fade

        p "Tú eres peor que eso."

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01

        show neus_exp_mouth sadbiting_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows normal
        with Dissolve(0.2)

        pause 0.2

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01

        show neus_exp_mouth happy_Silentx02
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx01
        with Dissolve(0.5)

        pause 0.2

        $ Pedrera_char_Cond = "TxellClose"
        call Pedrera_char_lab

        show m_exp_mouth sad_Silentx02
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with fade

        dad "Hmm..."

        show m_exp_mouth sad_Talkingx003
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex001
        with dissolve

        dad "Probablemente."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        dad "Pero como puedes apreciar,"

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "tampoco tienes que hacerlo mucho mejor yo,"

        show m_exp_mouth happy_Talkingx09
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "para convencerla de que eres mejor compañía;"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows surprisex002
        with dissolve

        dad "¿no crees?"

        show m_exp_mouth happy_Silentx05
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx02
        with dissolve

        pause 0.2

        $ Pedrera_char_Cond = "TxellNeus"
        call Pedrera_char_lab

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 04
        show m_exp_piris right04
        show m_exp_eyebrows angryx02

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris left05
        show neus_exp_eyebrows angryx03
        with fade

        p "..."

        $ Pedrera_char_Cond = "NeusClose"
        call Pedrera_char_lab

        show neus_exp_mouth sadbiting_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris left01
        show neus_exp_eyebrows sadx01
        with fade

        dad "¿Realmente puedes llamar entonces a eso amor?"

        show neus_exp_mouth sadbiting_Silentx02
        $ nteye = 1
        call neus_exp_tears_tears
        show neus_exp_iris front01
        show neus_exp_eyebrows sadx01
        with Dissolve(0.5)

        pause 0.2

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx06
        with Dissolve(0.5)

        ne "..."

    else:

        show neus_exp_mouth sad_Talkingx004
        $ nteye = 4
        call neus_exp_tears_tears
        show neus_exp_iris front04
        show neus_exp_eyebrows sadx02
        with dissolve

        ne "Yo..."

        show neus_exp_mouth sadbiting_Silentx04
        $ nteye = 2
        call neus_exp_tears_tears
        show neus_exp_iris left02
        show neus_exp_eyebrows sadx03
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx07
        $ nteye = 5
        call neus_exp_tears_tears
        show neus_exp_iris right05
        show neus_exp_eyebrows sadx06
        with dissolve

        p "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01
    with fade

    dad "..."

    return


label afternight05_Pedrera_NeusBothDirections_NeusPlain:

    show m_exp_mouth happybiting_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with Dissolve(0.5)

    dad "Hmm..."

    $ NeusDick_NoProblem = False

    if night05_Interrogation_GrowYouADick_LikeToTry or night05_Interrogation_GrowYouADick_NotAProblem or night05_Interrogation_GrowYouADick_DontBotherYou:

        $ NeusDick_NoProblem = True

    if NeusDick_NoProblem:

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "Quizás no te moleste que tenga un rabo,"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "tus gustos tendrás..."

        if afternight05_Pedrera_NeusLoveDoubts_Cond == False:

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Pero..."

            call afternight05_Pedrera_NeusLoveDoubts

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Mi {i}Txiki{/i} ahora mismo es tan plana,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "que hasta un homosexual se sentiría atraído por ella."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex001
    with dissolve

    p "Eres un jodido enfermo."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Y tú llevas mi sangre,"

    jump afternight05_Pedrera_RealParents

label afternight05_Pedrera_RealParents:

    extend " mi niño."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "..."

    menu:

        pt "Entonces, mis verdaderos padres no murieron en un accidente de tráfico..."

        "Si soy tu hijo, ¿Qué fue lo que leí en el periódico sobre mis padres?":
            call p_Help

        "...":
            call p_Help

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Hmmm..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "¿No quieres preguntármelo directamente?"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "No importa,"

            extend " te lo responderé igualmente."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

    if music_play != "atlanteanTwilight":
        play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "atlanteanTwilight"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Tus \"verdaderos\" padres,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "probablemente no fueran más que dos vagabundos sin nombre ni identificación,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "que fueron asesinados,"

    extend " camuflando su muerte en un accidente de tráfico,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "en el que sospechosamente sus cuerpos quedaron calcinados."

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Tus padres adoptivos solo te contaron la mentira que se les inyectó en su cerebro,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "de un modo parecido a lo que debió de quedar por escrito en los registros oficiales."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Una clase de manipulación así,"

    extend " requiere tiempo,"

    extend " planificación,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows normal
    with dissolve

    dad "y bastante gente ligeramente manipulada."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Pero tampoco es nada del otro mundo si se hace sin prisas."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Toda tu infancia es simplemente una función bien orquestada,"

    extend " para esconder la verdad."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        pt "Si él es mi padre..."

        "¿Quien es entonces mi madre?":
            call p_Help

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows serious
            with dissolve

            dad "Tu madre..."

            show m_exp_mouth sadbiting_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pt "Sin duda,"

            extend " es capaz de leerme la mente."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

    if music_play != "crypticSorrow":
        play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "crypticSorrow"

    dad "Una hermosa mujer,"

    extend " sin duda alguna."

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "La joya de la corona de mis queridas hijas."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows serious
    with dissolve

    dad "La madre de Elur."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "De hecho,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "la madre de la mayoría de ellas."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "La única que hasta el momento,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "nunca había tenido un hijo varón."

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Hasta que te tuvo a ti."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "La cruda realidad,"

    extend " es que eres fruto de mis entrañas,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "una criatura que no debería existir."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx03
    with dissolve

    p "..."

    menu:

        pt "Si quisiera acabar con mi vida, ¿Por qué se molesta en explicarme todo esto?"

        "¿Vas a matarme?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Eso dependerá de ti."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

        "...":
            call p_Help

    # 

label afternight05_Pedrera_MaleBastards:

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "Verás,"

    if music_play != "QuinnsSongANewMan":
        play music "audio/music/kevinmacleod/sad/QuinnsSongANewMan.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "QuinnsSongANewMan"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "generalmente suelo matar a mi progenie masculina,"

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "para no tener competencia en mi harén;"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "y para que negarlo,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "porque si tuviera demasiados vástagos varones,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "quizás me resultaría difícil controlarlos."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "¿Pero uno solo?"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "No me supones ninguna amenaza."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Siempre y cuando aceptes acatar mis ordenes."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    menu:

        pt "Las órdenes de un psicópata mal nacido..."

        "¿Qué clase de órdenes?":
            call p_Help

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Hmm..."

        "...":
            call p_Help

label afternight05_Pedrera_Obedience:

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Tal y como lo veo,"

    extend " tienes dos opciones."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    dad "Acudes mañana al {i}akelarre{/i} que se llevará a cabo en {a=https://es.wikipedia.org/wiki/Guipúzcoa}Guipúzcoa{/a},"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "dónde te desnudarás ante los presentes,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "participarás de la fiesta con mis hijas,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "y me prometerás lealtad eterna."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "..."

    menu:

        pt "¿Junto a sus hijas?"

        "¿No tienes miedo que deje preñada a tus hijas?":
            call p_Help

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "No durante el {i}akelarre{/i}."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Ahí puedo volver en agua tu esperma fácilmente."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Pero si osas acercarte lo más mínimo a ninguna de ellas cualquier otro día del año,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "vivirás el resto de tus días para lamentar esa decisión."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "..."

        "...":
            call p_Help

    
label afternight05_Pedrera_InReturn:

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "A cambio,"

    extend " te ofreceré la posibilidad de gozar de una vida de placeres,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "que las palabras humanas se quedan cortas para describirlo."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "No solo tu existencia será eterna,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "también lo será tu juventud."

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "Serás capaz de transmutar tu cuerpo,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "de hacer más pequeño,"

    extend " o incluso más grande,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "tu miembro viril,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "convertirte en mujer si es eso lo que te place,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "transmutar tu rostro y tu cuerpo,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "cambiar el color del pelo,"

    extend " o de la piel."

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "Sería como pactar con el diablo."

        "Y me imagino que a cambio, también querrás que mate a gente inocente por ti.":
            call p_Help

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "¿¡Me equivoco?!"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "No tienen por que ser necesariamente inocentes,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "pero desde luego,"

            extend " son los que más prefieren."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Todo tiene su precio,"

            extend " hijo."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with dissolve

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "¿No tienes nada que decir?"

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve


    menu:

        pt "¿A qué precio?"

        "Básicamente quieres que me convierta en otra parte de tu harén.":
            call p_Help

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Tranquilo,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "no tengo ningún interés sexual contigo,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "por mucho que te convirtieras en mujer,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "sabría respetar tu decisión."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Aunque si quisieras,"

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "durante el {i}akelarre{/i} podría hacer una excepción."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Te sorprendería ver lo imaginativas que se vuelven mis hijas,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows serious
            with dissolve

            dad "cuando intentan seducirme para que les de,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "lo que solo yo puedo ofrecerles."

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "¿Verdad que sí?"

            extend " mi Txiki."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows sadx06
            with fade

            ne "..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx07
            with Dissolve(0.5)

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with fade

            dad "Pero solo si sabes cómo pedírmelo."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            menu:

                pt "¿Pedirle a mi padre transformado que me folle con un pollón caprino?"

                "Dudo mucho que te fuera a pedir algo parecido.":
                    call p_Help

                    $pl.ch_pts("np",1)

                    show m_exp_mouth sad_Talkingx005
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "El tiempo es algo que aprenderás a entender de un modo distinto,"

                    show m_exp_mouth sad_Talkingx06
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "la línea que separa la castidad,"

                    extend " el orgullo,"

                    extend " la identidad sexual,"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "suelen difuminarse fácilmente,"

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "cuando descubres el poder de romper las limitaciones físicas."

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "Te darás cuenta,"

                    extend " que la perspectiva de las cosas cambia bastante,"

                    show m_exp_mouth happy_Talkingx09
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx02
                    with dissolve

                    dad "una vez pasas el siglo de existencia."

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 06
                    show m_exp_piris front06
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "Ni qué contarte cuando sobrepasas el milenio..."

                    show m_exp_mouth happy_Silentx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows angryx02
                    with dissolve

                    dad "Hmmm..."

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "Habrá que ver si consigues mantener tu palabra hasta entonces,"

                    extend " por eso..."

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx02
                    with dissolve


                "...":
                    call p_Help

        "...":
            call p_Help


    p "..."


label afternight05_Pedrera_OtherOption:

    menu:

        pt "¿Por qué será, que ya me imagino la alternativa...?"

        "¿Y cual es la otra opción?":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Obviamente,"

            extend " la muerte."

            
        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            dad "Aunque si rechazaras esta oferta,"

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Obviamente,"

            extend " la otra opción es la muerte."

    
label afternight05_Pedrera_OtherOption_Hope:

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    p "..."

    menu:

        pt "Olvidar todo lo que ha ocurrido desde que conocí a [neusname], ¿es posible?"

        "¿No podrías volver a dejarme vivir como lo he estado haciendo hasta ahora?":
            call p_Help

            $pl.ch_pts("np",-3)

            jump afternight05_Pedrera_OtherOption_LikeBefore

        "...":
            call p_Help

            jump afternight05_Pedrera_HowWillEnd

                # dad "Aceptes una opción u otra,"
                # dad "[neusname] morirá esta noche."
                # dad "Y tú,"
                # extend " serás quien la mate."

label afternight05_Pedrera_OtherOption_LikeBefore:

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    if music_play != "grooveGrove":
        play music "audio/music/kevinmacleod/sad/grooveGrove.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "grooveGrove"

    dad "¿Hmm...?"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    p "Llevaba una vida mundana,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "y a duras penas llegaba a final de mes,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "pero sinceramente,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "amo la tranquilidad y normalidad que tenía mi vida antes de todo esto;"

    menu:

        pt "Antes..."

        "Antes de que esta loca asesina de las narices apareciera.":
            call p_Help

            $ afternight05_Pedrera_OtherOption_NeusAppear_Assasin = True

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx06
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows sadx03
            with fade

            ne "..."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            if night05_Interrogation_GrowYouADick_EternalLove_Cond:

                $pl.ch_pts("np",-10)

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx04

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx02
                with fade

                dad "No has dicho antes que le prometerías amor eterno?"

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx05

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows normal
                with dissolve

                dad "¿En qué quedamos ahora?"

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows surprisex01
                with fade

                p "Aprecio mi vida por encima de todo."

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "Hmm..."

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows normal
                with dissolve

                ne "¿A eso lo llamas amor?"

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows angryx02
                with fade

                p "..."

                show neus_exp_mouth sad_Talkingx07
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris right03
                show neus_exp_eyebrows angryx03
                with Dissolve(0.5)

                ne "Quizás sea verdad entonces que volver con Padre no sea un error..."

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris right04
                show neus_exp_eyebrows sadx04
                with Dissolve(0.5)

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx03
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows sadx01
                with fade

                dad "..."

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "La verdad es que te contradices un poco,"

                extend " mi niño..."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows suspiciousx02
                with dissolve

            elif night05_Interrogation_GrowYouADick_LikeToTry:

                $pl.ch_pts("np",-7)

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx02

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx02
                with fade

                dad "¿No habías dicho antes d que te encantaría probar su polla en ti?"

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx05

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows normal
                with dissolve

                p "Aprecio más mi vida que gozar del sexo."

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx07

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows serious
                with dissolve

                dad "Chico listo."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows normal
                with fade

            else:

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Silentx07
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx01
                with fade

                $pl.ch_pts("np",-6)

        "Antes de que [neusname] apareciera.":
            call p_Help
            $pl.ch_pts("np",-2)

            $ afternight05_Pedrera_OtherOption_NeusAppear_Neus = True

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx01

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with fade

    ne "..."


    if DidacPregnant:

        jump afternight05_Pedrera_OtherOption_DidacPreg

    else:

        $ Pedrera_char_Cond = "TxellClose"
        call Pedrera_char_lab

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with fade

        dad "Como si nada hubiera ocurrido..."

        show m_exp_mouth sad_Silentx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex02
        with dissolve

        p "Exacto."

        show m_exp_mouth sad_Talkingx006
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex002
        with dissolve

        dad "Lo lamento,"

        if music_play != "anguish":
            play music "audio/music/kevinmacleod/sad/anguish.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "anguish"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        dad "pero eso no será posible."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows serious
        with dissolve

        p "..."

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx01
        with dissolve

        pt "¡¿Lo lamenta?!"

        pt "¡Este monstruo no lamenta una mierda!"

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex002
        with dissolve

        dad "Quizás si hubieras dejado preñado a tu amigo,"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "hubiera tenido algo con lo que chantajearte."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows normal
        with dissolve

        p "..."

        menu:

            pt "¿Servirá de algo suplicárselo?"

            "Por favor...":
                call p_Help

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows serious
                with dissolve

                dad "..."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "No te ridiculices más de lo necesario."

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows normal
                with dissolve

                dad "Es absurdo,"

                extend " ridículo,"

                extend " y una pérdida de tiempo."

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows serious
                with dissolve

                dad "Algo que aprenderás sobre mi,"

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "si vives para contarlo."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

            "Te prometo que no contaré nunca a nadie lo que he visto estos días.":
                call p_Help

                show m_exp_mouth sad_Talkingx005
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex02
                with dissolve

                dad "¿Te crees que soy imbécil?"

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows angryx01
                with dissolve

                dad "El único modo de estar seguro que harás lo que te ordeno,"

                show m_exp_mouth sad_Talkingx06
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows angryx01
                with dissolve

                dad "será mañana si me prometes obediencia eterna en el {i}akelarre{/i}."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

            "...":
                call p_Help

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

        p "..."

        show m_exp_mouth sad_Talkingx006
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "Tal y como lo veo tienes dos alternativas."

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        dad "Acatar mis órdenes al pie de la letra,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx02
        with dissolve

        dad "o la muerte."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx02
        with dissolve

        p "..."

        jump afternight05_Pedrera_HowWillEnd

            # dad "Aceptes una opción u otra,"
            # dad "[neusname] morirá esta noche."
            # dad "Y tú,"
            # extend " serás quien la mate."

label afternight05_Pedrera_OtherOption_DidacPreg:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex02
    with Dissolve(0.5)

    dad "Eres consciente,"

    extend " que no puedo devolverle el estado masculino a tu amigo,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Verdad?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        "Lo sé.":
            call p_Help

        "...":
            call p_Help

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows serious
            with dissolve

            dad "Ya que tu amigo ha sido transformado mediante un poder,"

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "al que la humanidad no tiene acceso."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Si alguien descubriera su verdadera identidad,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "resultaría un riesgo demasiado grande para mis amiguitos dejarlo con vida."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Eso lo entiendes,"

    extend " ¿Verdad?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    menu afternight05_Pedrera_OtherOption_DidacPreg_Risk_Question:

        "Sí, lo entiendo.":
            call p_Help

        "...":
            call p_Help

            if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat == 0:

                show m_exp_mouth sad_Talkingx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

                dad "Responde."

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

            if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat == 1:

                show m_exp_mouth sad_Talkingx004
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "¿Tanto te cuesta entender una pregunta tan simple?"

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

            if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat > 1:

                if music_play != "oppressiveGloom":
                    play music "audio/music/kevinmacleod/sad/oppressiveGloom.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "oppressiveGloom"

                $pl.ch_pts("dp",-2)

                $ Pedrera_char_Cond = "DidacPain"
                call Pedrera_char_lab

                show didacf_mouth sad_Talkingx09
                show didacf_eyes 07
                show didacf_pupils front07
                show didacf_eyebrows angryx03
                with vpunch
                with vpunch

                play sound "audio/characters/didac/scream_au15.ogg"

                d "¡AARRGHH!"

                scene ped_pain_didac:
                    subpixel True
                    truecenter
                    zoom 1.0 xpos 0.95 ypos 1.0
                    easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
                show border_darkness_02:
                    subpixel True
                    truecenter
                    zoom 0.5
                    easein_quad 5.0 zoom 1.0

                p "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat == 2:

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows normal
                    with fade

                    p "¡¿Qué diablos haces?!"

                    show m_exp_mouth sad_Talkingx003
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex001
                    with dissolve

                    dad "Usarlo para que respondas."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                elif afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat == 3:

                    show m_exp_mouth sad_Talkingx005
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows surprisex002
                    with fade

                    dad "¿Va a tener que sufrir durante mucho rato?"

                    show m_exp_mouth sad_Talkingx05
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "Quizás es algo que hasta disfrutes,"

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "pero dudo que a él le guste demasiado."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx02
                    with dissolve

                elif afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat == 4:

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows normal
                    with fade

                    dad "Podemos estar así todo el día."

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx03
                    with dissolve
                else:

                    show m_exp_mouth happy_Silentx05
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx02
                    with fade

            p "..."

            $afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat += 1

            jump afternight05_Pedrera_OtherOption_DidacPreg_Risk_Question


    if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat > 1:

        show m_exp_mouth sad_Talkingx008
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "Te ha costado responder..."

label afternight05_Pedrera_OtherOption_DidacPreg_Libido:

    show m_exp_mouth happybiting_Silentx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Humm..."

    if music_play != "grooveGrove":
        play music "audio/music/kevinmacleod/sad/grooveGrove.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "grooveGrove"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "¿Acaso quieres que le mantenga la libido a esta ninfómana de aquí atrás,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "para podértela follar sin control cada día?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        "Mucho mejor que [neusname], desde luego.":
            call p_Help

            if night05_Interrogation_GrowYouADick_EternalLove_Cond:
                $pl.ch_pts("np",-10)

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex001
                with dissolve

                pause 0.5

                if music_play != "atlanteanTwilight":
                    play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "atlanteanTwilight"

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth happybiting_Silentx04
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx02

                show neus_exp_mouth sadbiting_Silentx02
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows sadx01
                with fade

                dad "..."

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx06
                with fade

                pause 0.2

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx07
                with Dissolve(0.5)

                ne "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx05
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with fade

                dad "Cuando precisamente antes,"

                extend " le has prometido amor eterno..."

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Hmmm..."

                show m_exp_mouth happy_Talkingx06
                show m_exp_eyes 08
                show m_exp_piris front08
                show m_exp_eyebrows surprisex01
                with dissolve

                dad "Bueno,"

                extend " supongo que tener a una amante,"

                show m_exp_mouth happy_Talkingx08
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex002
                with dissolve

                dad "aún y estando casado,"

                show m_exp_mouth happy_Talkingx09
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "es un tradición muy humana."

                show m_exp_mouth happy_Talkingx11
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows suspiciousx02
                with dissolve

                dad "¿O no sueles seducir a hombres casados?"

                extend " {i}Txiki{/i}"

                show m_exp_mouth happy_Silentx08
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows angryx01
                with dissolve

                pause 0.2

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                show neus_exp_mouth sad_Silentx07
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris left01
                show neus_exp_eyebrows sadx01
                with fade

                pause 0.2

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows sadx01
                with Dissolve(0.5)

                pause 0.2

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris right05
                show neus_exp_eyebrows sadx06
                with Dissolve(0.5)

                ne "..."

            else:

                $pl.ch_pts("np",-8)

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx02
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows surprisex02

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 0
                call neus_exp_tears_tears
                show neus_exp_iris front00
                show neus_exp_eyebrows surprisex01
                with fade

                dad "..."

                if music_play != "atlanteanTwilight":
                    play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
                    $ music_play = "atlanteanTwilight"

                show m_exp_mouth sad_Silentx03
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows normal

                show neus_exp_mouth sadbiting_Silentx03
                $ nteye = 1
                call neus_exp_tears_tears
                show neus_exp_iris front01
                show neus_exp_eyebrows sadx01
                with dissolve

                ne "..."

                p "Al menos no ha estado calentándome el paquete,"

                show m_exp_mouth happybiting_Silentx03
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sadbiting_Silentx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx04
                with Dissolve(0.5)

                p "sin darme nada a cambio."

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                if ntlong in range (0,6):
                    if ntlong < 5:
                        $ ntlong += 1

                show neus_exp_mouth sadbiting_Silentx07
                $ nteye = 5
                call neus_exp_tears_tears
                show neus_exp_iris front05
                show neus_exp_eyebrows sadx06
                with fade

                ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx02
            with fade

            dad "Hmmm..."

        "No negaré que es algo que he disfrutado bastante.":
            call p_Help

            $pl.ch_pts("np",-2)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex02
            with dissolve

            pause 0.2

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex001
            with Dissolve(0.5)

            pause 0.2

            if music_play != "atlanteanTwilight":
                play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "atlanteanTwilight"

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with fade

            ne "..."

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows surprisex001
            with fade

            dad "Dicen que la sinceridad es importante en una relación."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "Una relación basada en la verdad,"

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows normal
            with dissolve

            p "es mucho más real y auténtica,"

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "que cualquiera que haya sido construida con enredos,"

            extend " manipulaciones"

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            p "y telarañas de mentiras."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx05
            $ nteye = 7
            call neus_exp_tears_tears
            show neus_exp_iris front07
            show neus_exp_eyebrows sadx07
            with fade

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx07
            with Dissolve(0.5)

            ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with fade

            dad "Quizás..."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows serious
            with dissolve

            dad "Aunque eso suelen decirlo aquellos tan estúpidos e ineptos,"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx03
            with dissolve

            dad "que se ven incapaces de mantener una mentira."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex002
            with dissolve

            p "O aquellos que creen en el amor de verdad."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Lo que he dicho,"

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            dad "estúpidos."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Hmm..."

        "...":
            call p_Help

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Quizás harías menos aburrida tu existencia..."

label afternight05_Pedrera_OtherOption_DidacPreg_MuchBetter:

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Desde luego,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows serious
    with dissolve

    dad "mucho más satisfactorio que follarse a esta enana manipuladora durante años."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx08
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx04
    with fade

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx03
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris front03
    show neus_exp_eyebrows sadx01
    with Dissolve(0.5)

    ne "..."

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx05

    with Dissolve(0.5)

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with fade

    dad "Nunca entenderé los humanos que se mantienen fieles a una sola mujer."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        pt "¿Es buena idea provocarle?"

        "Eso es porque a lo que tú llamas sentimientos, yo lo llamo enfermedad mental.":
            call p_Help

            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            p "En el fondo,"

            extend " me das lástima."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "..."

            if music_play != "darkestChild":
                play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "darkestChild"

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 07
            show m_exp_piris front07
            show m_exp_eyebrows surprisex002
            with vpunch
            with vpunch

            dad "JAJAJAJAJA"

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 06
            show m_exp_piris front06
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Hacía tiempo que nadie me hacía reír de esta manera..."

            show m_exp_mouth happy_Silentx12
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            p "..."

        "...":
            call p_Help

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "Aún así,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    dad "¿por qué conformarte con una simple esclava?"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Cuando podrías tener centenares."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

label afternight05_Pedrera_OtherOption_DidacPreg_Slaves:

    menu:

        "Porque con Dídac me basta y me sobra.":
            call p_Help

            $pl.ch_pts("np",-1)

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Claro,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "usar a un querido amigo transformado en una jodida ninfómana,"

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "como castigo por algo que no cometió,"

            show m_exp_mouth sad_Talkingx07
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "en un contenedor de esperma,"

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "puede no parecer algo bondadoso o justo."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows normal
            with dissolve

            dad "Pero a decir verdad,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "es toda una experiencia,"

            extend " tener a una esclava sexual que te pide acción a todas horas,"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx03
            with dissolve

            dad "especialmente cuando solo tu semilla,"

            extend " puede realmente satisfacerla."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Aunque lo más probable,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "es que te aburras de ella con facilidad,"

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "al usar siempre a la misma hembra humana."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            menu:

                pt "Trata a las personas como si fueran de usar y tirar..."

                "Eso es porque eres incapaz de sentir algo por nadie.":
                    call p_Help

                    $pl.ch_pts("np",1)

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows normal
                    with dissolve

                    dad "..."

                    show m_exp_mouth happy_Silentx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex01
                    with dissolve

                    dad "Hmmm..."

                    if music_play != "crypticSorrow":
                        play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "crypticSorrow"

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "O quizás es porque tu limitada comprensión de la realidad,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows serious
                    with dissolve

                    dad "solo es capaz de observar el arbusto que tiene enfrente,"

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "el cual le impide ver el enorme y frondoso bosque que hay detrás."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows serious
                    with dissolve

                    pt "¿De qué está hablando?"

                    jump afternight05_Pedrera_AntExplanation
                        # dad "A los humanos suelen educarlos en escuelas para criarlos,"
                        # extend " disciplinarlos,"
                        # extend " adoctrinarlos;"

                "...":
                    call p_Help

                    p "..."

            jump afternight05_Pedrera_Guarantee
                # dad "¿Qué garantías tengo de que después del aquelarre de mañana,"
                # dad "no irías en busca de Elur?"
                # dad "Y antes de que respondas,"

        "Porque no soy un asesino.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows normal
            with dissolve

            dad "Si quieres vivir,"

            show m_exp_mouth sad_Talkingx009
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "lo vas a ser,"

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx03
            with dissolve

            dad "al menos una vez."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx02
            with dissolve

            pt "¿De qué está...?"

            jump afternight05_Pedrera_Guarantee
                # dad "¿Qué garantías tengo de que después del akelarre de mañana,"
                # dad "no irías en busca de Elur?"
                # dad "Y antes de que respondas,"

        "Porque prefiero amar a alguien con sinceridad, que tener un harén repleto de mujeres sin el mismo amor mutuo.":
            call p_Help
            $pl.ch_pts("np",2)

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "..."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Eso es porque te faltaría mejorar tu resistencia física."

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            p "No hablo de sexo."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Aunque el dinero es lo que más suelen usar los mortales para retenerlas,"

            show m_exp_mouth sad_Talkingx003
            show m_exp_eyes 05
            show m_exp_piris left05
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "especialmente a cierta edad,"

            show m_exp_mouth happy_Talkingx03
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "o sin ser muy agraciados físicamente,"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx03
            with dissolve

            dad "el sexo es una de las mejores herramientas para mantenerlas cerca,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx01
            with dissolve

            dad "especialmente si sabes complacerlas adecuadamente."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 02
            show m_exp_piris right02
            show m_exp_eyebrows sadx02
            with dissolve

            dad "¿Verdad que sí?"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx03
            with dissolve

            dad "{i}Txiki{/i}."

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx03
            with dissolve

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sad_Silentx08
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris left04
            show neus_exp_eyebrows angryx01
            with fade

            ne "..."

            show neus_exp_mouth sad_Silentx09
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris left05
            show neus_exp_eyebrows angryx02
            with dissolve

            dad "Tanto el dinero como el placer,"

            show neus_exp_mouth sad_Silentx09
            $ nteye = 6
            call neus_exp_tears_tears
            show neus_exp_iris front06
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            dad "son realmente apreciados por la hembra humana,"

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 3
            call neus_exp_tears_tears
            show neus_exp_iris front03
            show neus_exp_eyebrows sadx01
            with Dissolve(0.5)

            dad "a veces incluso buscándolo en hombres distintos al mismo tiempo."

            show neus_exp_mouth sadbiting_Silentx03
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows surprisex001
            with fade

            p "..."

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            dad "Pero con los poderes que te otorgaría,"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "no solo podrías complacerlas llevándolas a lugares de ensueño y arcanos."

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Dignos de la realeza,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows sadx01
            with dissolve

            dad "y repletos de gente de alta cuna;"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows angryx02
            with dissolve

            dad "sino además,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx03
            with dissolve

            dad "podrías ir más allá de sus sueños más húmedos,"

            extend " y prohibidos."

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "El sexo te bastaría para obrar milagros,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows serious
            with dissolve

            dad "pero eso solo sería el aperitivo,"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx02
            with dissolve

            dad "te lo garantizo."

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "Tampoco estoy hablando de eso."

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "Entonces de lo que hablas,"

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "es de la fantasía creada para la mente de una {b}hormiga{/b}."

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            p "¿De una hormiga?"

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows normal
            with dissolve

            p "¡¿De qué estás hablando?!"

            jump afternight05_Pedrera_AntExplanation

            ##

            menu:

                "Como si me importara tu opinión.":
                    call p_Help

                "...":
                    call p_Help

        "...":
            call p_Help

            dad "Hmmm..."


label afternight05_Pedrera_OtherOption_DidacPreg_After:

    jump afternight05_Pedrera_Guarantee


label afternight05_Pedrera_AntExplanation:

    if music_play != "crypticSorrow":
        play music "audio/music/kevinmacleod/sad/crypticSorrow.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "crypticSorrow"

    $ afternight05_Pedrera_AntExplanation_Cond = True

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "A los humanos suelen educarlos en escuelas para criarlos,"

    extend " disciplinarlos,"

    extend " adoctrinarlos;"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "mediante juegos,"

    extend " sueños,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "y esperanzas de un futuro mejor."

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "Para luego echarlos al mundo en busca de una ardua y pesada labor,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "a la que le dedicaran gran parte de su corta existencia;"

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "para finalmente descubrir,"

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "que no son más que piezas de un engranaje mayor,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows sadx01
    with dissolve

    dad "que les permite sobrevivir."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Mientras otros más listos y privilegiados,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "consiguen vivir a costa de ellos."

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Para que la colonia no se rebele y asalte los cielos,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "se crean sueños y esperanzas,"

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows sadx01
    with dissolve

    dad "que las hormigas consumen día sí,"

    extend " y día también,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "mediante historias idílicas y fantasiosas de amores imposibles,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris left02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "películas románticas con presupuestos millonarios,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "llevadas a cabo por atractivos y famosos actores,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "o las telenovelas pasadas de rosa,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "para mujeres que siguen soñando en su hombre ideal."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "¿Llama a la gente sin recursos hormigas?"

        "Lo que dices, es producto de una mente paranoica y enfermiza.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "..."

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "¿Crees realmente que soy yo el que necesita ayuda?"

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx01
            with dissolve

            p "No creo que tu caso tenga remedio."

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 07
            show m_exp_piris front07
            show m_exp_eyebrows sadx03
            with vpunch
            with vpunch

            dad "JAJAJAJAJA"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows sadx01
            with dissolve

            dad "Eres hasta gracioso..."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "Hmmm..."

        "...":
            call p_Help

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Mira a la naturaleza,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "¿Cuantos animales ves que sean monógamos?"

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        pt "¡¿Me está comparando con un animal?!"

        "¡Existen!":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx04
            with dissolve

            dad "Por razones de supervivencia de la especie."

            show m_exp_mouth sad_Talkingx005
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Aunque de las cinco mil especies de mamíferos que conoce la humanidad hoy día,"

            show m_exp_mouth sad_Talkingx007
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows normal
            with dissolve

            dad "solo el tres por ciento practica la monogamia."

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "Ni tan siquiera los primates,"

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "vuestros parientes más cercanos en la escala evolutiva,"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "son en general proclives a ceñirse a una sola pareja."

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "En realidad,"

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "lo que conoces como {a=https://es.wikipedia.org/wiki/Amor}amor{/a},"

            show m_exp_mouth happy_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows sadx01
            with dissolve

            dad "no es más que una falsa ilusión,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows sadx03
            with dissolve

            dad "creada por tus antepasados,"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx01
            with dissolve

            dad "para sobrevivir en aquellos tiempos en los que ya no vivían en la seguridad de los árboles,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "y la comida,"

            extend " especialmente en la {a=https://es.wikipedia.org/wiki/Glaciación_Würm_(Edad_de_Hielo)}última edad de hielo{/a},"

            show m_exp_mouth happy_Talkingx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "más bien escaseaba."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "¿Qué razones tiene hoy en día un varón humano de ser monógamo para sobrevivir?"

            show m_exp_mouth happy_Talkingx10
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "Uno sólo,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows serious
            with dissolve

            dad "que sea relativamente fértil,"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "puede fecundar a decenas de mujeres."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex01
            with dissolve

            dad "O mejor ninguna,"

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "pues quizás vuelve a haber demasiadas hormigas en el mundo..."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            menu:

                "Desde luego, ¿Qué va a entender de amor fraternal, alguien que sacrifica a sus hijos?":
                    call p_Help

                    $pl.ch_pts("np",2)

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "Hmmm..."

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx01
                    with dissolve

                    dad "Los sacrifico al poco de nacer,"

                    show m_exp_mouth sad_Talkingx004
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "precisamente porque conozco muy bien lo que es la traición de un hijo."

                    show m_exp_mouth sad_Silentx03
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve

                    pause 0.2

                    show m_exp_mouth sad_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris right05
                    show m_exp_eyebrows suspiciousx02
                    with dissolve

                    pause 0.2

                    $ Pedrera_char_Cond = "NeusClose"
                    call Pedrera_char_lab

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 3
                    call neus_exp_tears_tears
                    show neus_exp_iris left03
                    show neus_exp_eyebrows sadx04
                    with fade

                    pause 0.2

                    show neus_exp_mouth sad_Silentx07
                    $ nteye = 4
                    call neus_exp_tears_tears
                    show neus_exp_iris left04
                    show neus_exp_eyebrows sadx06
                    with Dissolve(0.5)

                    p "..."

                    $ Pedrera_char_Cond = "TxellClose"
                    call Pedrera_char_lab

                    show m_exp_mouth sad_Talkingx03
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows sadx01
                    with fade

                    dad "Pero entiendo que te parezca una barbaridad,"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows sadx02
                    with dissolve

                    dad "como muchas otras cosas."

                    show m_exp_mouth happy_Talkingx06
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows suspiciousx01
                    with dissolve

                    dad "En eso no te voy a juzgar,"

                    show m_exp_mouth happy_Talkingx08
                    show m_exp_eyes 02
                    show m_exp_piris front02
                    show m_exp_eyebrows angryx03
                    with dissolve

                    dad "te faltan demasiadas lunas para entender lo que te estoy contando."

                    show m_exp_mouth happy_Silentx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows angryx01
                    with dissolve

                    p "..."

                "Esa será tu opinión.":
                    call p_Help

                    show m_exp_mouth happy_Silentx02
                    show m_exp_eyes 04
                    show m_exp_piris front04
                    show m_exp_eyebrows sadx02
                    with dissolve

                    dad "Hmmm..."

                "...":
                    call p_Help

        "...":
            call p_Help

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "No seas una hormiga,"

    extend " mi niño."

    show m_exp_mouth sad_Talkingx007
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "No hagas que sienta vergüenza de ti."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    pt "Como si me importara su opinión..."

    # probably other jump if I use this later.

    jump afternight05_Pedrera_Guarantee


label afternight05_Pedrera_Guarantee:

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Qué garantías tengo de que después del {i}akelarre{/i} de mañana,"

    if music_play != "lostFrontier":
        play music "audio/music/kevinmacleod/sad/lostFrontier.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "lostFrontier"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "no irías en busca de Elur?"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "Y antes de que respondas,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "te recuerdo que mentirme,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "no es una idea inteligente."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    menu afternight05_Pedrera_Guarantee_Question:

        "¿Crees que me han quedado ganas de volver a quedar con esta sucia asesina sin corazón?":
            call p_Help

            $ afternight05_Pedrera_Guarantee_DirtyHeartlessKiller_Cond = True

            $ Pedrera_char_Cond = "TxellNeus"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows surprisex01

            show neus_exp_mouth sadbiting_Silentx02
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex01
            with fade

            dad "..."

            if night05_Interrogation_GrowYouADick_EternalLove_Cond:

                $pl.ch_pts("np",-10)

                show m_exp_mouth sad_Talkingx008
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx04
                with Dissolve(0.5)

                dad "{i}Sucia asesina sin corazón{/i}..."

                if ntlong in range (0,6):
                    if ntlong < 5:
                        $ ntlong += 1

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows surprisex01

                show neus_exp_mouth sadbiting_Silentx06
                $ nteye = 4
                call neus_exp_tears_tears
                show neus_exp_iris front04
                show neus_exp_eyebrows sadx05
                with Dissolve(0.5)

                dad "Suerte que le has prometido amor eterno."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris right05
                show m_exp_eyebrows surprisex01
                with dissolve

            else:

                $pl.ch_pts("np",-8)

                if ntlong in range (0,6):
                    if ntlong < 5:
                        $ ntlong += 1

                show m_exp_mouth happy_Silentx04
                show m_exp_eyes 03
                show m_exp_piris right03
                show m_exp_eyebrows suspiciousx01

                show neus_exp_mouth sadbiting_Silentx05
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx04
                with Dissolve(0.5)

                ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows surprisex01
            with fade

            jump afternight05_Pedrera_Guarantee_LookForMyDaughters

        "Te lo prometo." if afternight05_Pedrera_Guarantee_IPromise == False:
            call p_Help

            $pl.ch_pts("np",-1)

            $ afternight05_Pedrera_Guarantee_IPromise = True

            $ Pedrera_char_Cond = "TxellNeus"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows sadx02
            with fade

            dad "..."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows sadx01

            show neus_exp_mouth sadbiting_Silentx06
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris right04
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            dad "Hmmm..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with fade

            dad "Las promesas vacías me resultan inútiles."

            show m_exp_mouth sad_Talkingx05
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Creí que habías dicho que preferías vivir a morir."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            p "Y así es."

            show m_exp_mouth happy_Talkingx04
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Entonces dime lo mucho que te disgusta Elur."

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            jump afternight05_Pedrera_Guarantee_Question

        "No puedo decirte eso." if afternight05_Pedrera_Guarantee_IPromise:
            call p_Help

            $pl.ch_pts("np",2)

            $ Pedrera_char_Cond = "TxellNeus"
            call Pedrera_char_lab

            show m_exp_mouth sad_Silentx04
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows suspiciousx01

            show neus_exp_mouth sadbiting_Silentx01
            $ nteye = 2
            call neus_exp_tears_tears
            show neus_exp_iris front02
            show neus_exp_eyebrows normal
            with fade

            dad "..."

            if ntlong in range (0,6):
                if ntlong > 0:
                    $ ntlong -= 1

            show m_exp_mouth sad_Silentx05
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx02

            show neus_exp_mouth happybiting_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx02
            with Dissolve(0.5)

            dad "Hmmm..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx04
            with fade

            dad "Entonces no me hagas perder el tiempo con preguntas estúpidas."

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows angryx02
            with dissolve

            dad "Aún así,"

            extend " si prefieres no morir,"

            show m_exp_mouth happy_Talkingx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            dad "tienes la alternativa de obedecerme ciegamente."

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 01
            show m_exp_piris front01
            show m_exp_eyebrows angryx03
            with dissolve

            dad "Tú eliges."

            show m_exp_mouth happy_Silentx06
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx01
            with dissolve

            pt "¿De qué está hablando...?"

            jump afternight05_Pedrera_HowWillEnd
                # dad "Aceptes una opción u otra,"
                # dad "[neusname] morirá esta noche."
                # dad "Y tú,"
                # extend " serás quien la mate."

        "No te voy a dar ninguna garantía de nada, ¡Púdrete!":
            call p_Help

            $pl.ch_pts("np",3)

            show m_exp_mouth sadbiting_Silentx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows angryx03
            with dissolve

            dad "..."

            if music_play != "atlanteanTwilight":
                play music "audio/music/kevinmacleod/sad/atlanteanTwilight.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "atlanteanTwilight"

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth happybiting_Silentx02
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx04
            with fade

            ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth sad_Talkingx006
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with fade

            dad "Eres tú quien me ha pedido otra alternativa."

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Desde luego,"

            show m_exp_mouth sad_Talkingx008
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "te tenía por alguien más inteligente."

            jump afternight05_Pedrera_HowWillEnd
                # dad "Aceptes una opción u otra,"
                # dad "[neusname] morirá esta noche."
                # dad "Y tú,"
                # extend " serás quien la mate."

        "...":

            call p_Help

            $ afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat_b += 1

            if afternight05_Pedrera_OtherOption_DidacPreg_Risk_Repeat_b > 1:

                
                $pl.ch_pts("dp",-2)

                $ Pedrera_char_Cond = "DidacPain"
                call Pedrera_char_lab

                show didacf_mouth sad_Talkingx09
                show didacf_eyes 07
                show didacf_pupils front07
                show didacf_eyebrows angryx03
                with vpunch
                with vpunch

                d "¡AARRGHH!"

                scene ped_pain_didac:
                    subpixel True
                    truecenter
                    zoom 1.0 xpos 0.95 ypos 1.0
                    easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5
                show border_darkness_02:
                    subpixel True
                    truecenter
                    zoom 0.5
                    easein_quad 5.0 zoom 1.0

                p "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows angryx02
                with fade

                dad "Podemos estar así todo el día."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx01
                with dissolve

            else:

                show m_exp_mouth happy_Talkingx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "Será mejor que respondas a la pregunta."

                show m_exp_mouth happy_Talkingx04
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows sadx01
                with dissolve

                dad "Por el bien de tu amigo..."

                show m_exp_mouth happy_Silentx05
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows suspiciousx01
                with dissolve

            p "..."

            jump afternight05_Pedrera_Guarantee_Question


label afternight05_Pedrera_Guarantee_LookForMyDaughters:

    # show m_exp_mouth sad_Silentx04
    # show m_exp_eyes 05
    # show m_exp_piris front05
    # show m_exp_eyebrows serious
    # with dissolve

    ne "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Hmm..."

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "¿Y qué me dices de intentar buscar a alguna otra de mis hijas?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        "Por lo que me has contado, no son mucho mejores que [neusname].":
            call p_Help

            $pl.ch_pts("np",-2)

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 03
            show m_exp_piris front03
            show m_exp_eyebrows surprisex01
            with dissolve

            p "son todas unas arpías manipuladoras,"

            extend " mentirosas,"

            extend " y asesinas."

            show m_exp_mouth happy_Silentx04
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows suspiciousx01
            with dissolve

            pause 0.2

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx04
            $ nteye = 1
            call neus_exp_tears_tears
            show neus_exp_iris front01
            show neus_exp_eyebrows sadx01
            with fade

            pause 0.2

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 5
            call neus_exp_tears_tears
            show neus_exp_iris right05
            show neus_exp_eyebrows sadx06
            with Dissolve(0.5)

            ne "..."

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Silentx05
            show m_exp_eyes 04
            show m_exp_piris right04
            show m_exp_eyebrows suspiciousx02
            with fade

            dad "..."

            show m_exp_mouth happy_Silentx02
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex02
            with dissolve

            dad "Hmmm..."

        "Tampoco sabría por dónde empezar a buscarlas.":
            call p_Help

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "Hmmm..."

        "No tengo ningún interés en ellas.":
            call p_Help

            show m_exp_mouth sad_Talkingx004
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "Eso dices ahora."


label afternight05_Pedrera_Guarantee_MyDaughtersLookForYou:

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "¿Y si ellas vinieran a buscarte a ti?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Qué harías entonces?"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    menu:

        pt "¿Que debería hacer si me encuentro con una de sus hijas?"

        "Intentar hablar con ellas y decirles que no estoy interesado en ellas.":
            call p_Help

            show m_exp_mouth sad_Talkingx04
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "Hablar con ellas..."

            show m_exp_mouth sad_Talkingx06
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01
            with dissolve

            dad "¿De verdad crees que mis hijas son tan estúpidas?"

            show m_exp_mouth sad_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            dad "No insultes a nuestra sangre."

            jump afternight05_Pedrera_Guarantee_TheBestApproach

        "Intentar matarlas.":
            call p_Help

            show m_exp_mouth sad_Silentx02
            show m_exp_eyes 02
            show m_exp_piris front02
            show m_exp_eyebrows suspiciousx02
            with dissolve

            dad "..."

            show m_exp_mouth happy_Talkingx12
            show m_exp_eyes 07
            show m_exp_piris front07
            show m_exp_eyebrows sadx04
            with vpunch

            dad "JAJAJAJAJA"

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows sadx05
            with dissolve

            dad "No me hagas reír..."

            show m_exp_mouth happy_Talkingx08
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows angryx02
            with dissolve

            dad "No durarías ni un minuto con ninguna de ellas."

            jump afternight05_Pedrera_Guarantee_TheBestApproach

        "Huir bien lejos e intentar ponerme en contacto contigo.":
            call p_Help

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 08
            show m_exp_piris front08
            show m_exp_eyebrows suspiciousx01

            dad "Hmm..."

            jump afternight05_Pedrera_Guarantee_ContactYou


label afternight05_Pedrera_Guarantee_TheBestApproach:

    show m_exp_mouth sad_Talkingx008
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Lo mejor que podrías hacer,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "es ponerte en contacto conmigo lo más pronto que te fuera posible."

    jump afternight05_Pedrera_Guarantee_ContactYou

label afternight05_Pedrera_Guarantee_ContactYou:

    $ afternight05_Pedrera_Guarantee_ContactYou_Cond = True

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¿Sería eso posible?"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Sí."

    show m_exp_mouth happy_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "En realidad sería más fácil de lo que te imaginas."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Aunque suene a \"cliché\","

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    dad "lo único que tendrías que hacer,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "entre la media noche,"

    extend " y las tres de la mañana,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "es ponerte ante un espejo,"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows normal
    with dissolve

    dad "poner cerca algún objeto que te recuerde a mi,"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "y mirando tu reflejo,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows normal
    with dissolve

    dad "repetir mi nombre trece veces."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows surprisex01
    with dissolve

    p "¿Y cual es tu nombre?"

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Papá."

    show m_exp_mouth happy_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "Papi,"

    extend " si lo prefieres..."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "Eso se parece bastante a la historia del fantasma del espejo,"

    p "sobre una tal {a=https://es.wikipedia.org/wiki/Verónica_(leyenda_urbana)}Verónica{/a}..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    dad "La mayoría de las leyendas urbanas,"

    extend " son producto de la imaginación de alguien,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    dad "pero muchas de ellas esconden una verdad,"

    extend" en su fuente original."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows normal
    with dissolve

    p "¿Entonces tendría esa opción?"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows serious
    with dissolve

    dad "Digamos que lo estoy meditando."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Aún tengo que comprobar que eres capaz de mantener tu palabra."

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Aún así,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "tendrías que demostrarme tu lealtad hacia mi."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris left04
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Eso sin mencionar el trabajo que me darías,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris left05
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "para darle credibilidad a la existencia de alguien que surge de la nada."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    p "..."

    jump afternight05_Pedrera_HowWillEnd

    ##

label afternight05_Pedrera_HowWillEnd:

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Aceptes una opción u otra,"

    if music_play != "rightBehindYou":
        play music "audio/music/kevinmacleod/creepy/rightBehindYou.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "rightBehindYou"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Elur morirá esta noche."

    $ meyesc = "_goat"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    dad "Y tú,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx03
    with dissolve

    dad "serás quien la mate."

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    menu:

        pt "¡¿Que yo mataré a [neusname]?!"

        "¡¿Qué?!":
            call p_Help
            $pl.ch_pts("np",1)

            show m_exp_mouth happybiting_Silentx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows angryx01
            with dissolve

            dad "..."

        "...":
            call p_Help

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Lo hagas por voluntad propia,"

    extend " o no,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "acabará siendo estrangulada con tus propias manos."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Puedo poseerte para forzarte a ello,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "pero preferiría que fuera elección tuya."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    p "..."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Al fin y al cabo,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "ahora que sabes la clase de monstruo que es mi {i}Txiki{/i},"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "sin mencionar que transformó injustamente a tu amigo,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    dad "para engañarte y manipularte;"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "no debería resultarte algo tan difícil..."

    show m_exp_mouth happy_Silentx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    menu:

        pt "¿Quiere que estrangule a [neusname]..?"

        "¡No pienso hacer eso!":
            call p_Help
            $pl.ch_pts("np",2)

            jump afternight05_Pedrera_NoChoice

        "Lo lamento, pero no puedo hacer lo que me pides.":
            call p_Help
            $pl.ch_pts("np",1)

            jump afternight05_Pedrera_NoChoice

        "De acuerdo, haré lo que me pides.":
            call p_Help
            $pl.ch_pts("np",-15)

            show m_exp_mouth happy_Silentx08
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx04
            with dissolve

            pause 0.1

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show neus_exp_mouth sadbiting_Silentx07
            $ nteye = 0
            call neus_exp_tears_tears
            show neus_exp_iris front00
            show neus_exp_eyebrows surprisex02
            with fade

            ne "..."

            if ntlong in range (0,6):
                if ntlong < 5:
                    $ ntlong += 1

            show neus_exp_mouth sad_Silentx09
            $ nteye = 4
            call neus_exp_tears_tears
            show neus_exp_iris front04
            show neus_exp_eyebrows sadx05
            with Dissolve(0.5)

            pause 0.2

            $ Pedrera_char_Cond = "TxellClose"
            call Pedrera_char_lab

            show m_exp_mouth happy_Talkingx11
            show m_exp_eyes 05
            show m_exp_piris right05
            show m_exp_eyebrows angryx04
            with fade

            dad "Así me gusta,"

            extend " mi niño."

            jump afternight05_Pedrera_NeusWillDie


label afternight05_Pedrera_NoChoice:

    $ afternight05_Pedrera_NoChoice_Refuse_Cond = True

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Veo que no lo has entendido."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "Quiero observar su rostro,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "justo antes de que desfallezca,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 00
    show m_exp_piris right00
    show m_exp_eyebrows serious
    with dissolve

    dad "la expresión al ver cómo el autor de su muerte,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows angryx01
    with dissolve

    dad "resulta ser el mismo que el que hasta ahora,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx02
    with dissolve

    dad "era el de su esperanza."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx03
    with dissolve

    dad "El hijo de su amada madre,"

    extend " su propio hermano."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    p "¡Pensaba que habías dicho que amabas a tus hijas!"

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "Y las amo con locura;"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "que no te quepa la menor duda."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¡¿Y estás dispuesto a matarla?!"

    jump afternight05_Pedrera_NeusWillDie

    ##

label afternight05_Pedrera_NeusWillDie:

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx04
    with dissolve

    dad "Morirá esta noche;"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows normal
    with dissolve

    dad "para resucitar mañana poco después del crepúsculo,"

    extend " junto a sus hermanas,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows angryx04
    with dissolve

    dad "y se arrastrará por el suelo sin piernas ni brazos durante diez años,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    dad "para suplicar mi perdón,"

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows angryx03
    with dissolve

    dad "dando ejemplo de lo que significa traicionarme."

    show m_exp_mouth happy_Silentx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Además,"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows angryx03
    with dissolve

    dad "así perderá este estúpido tatuaje que se ha hecho en el pecho."

    show m_exp_mouth happy_Talkingx10
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    dad "¿Te creías que tatuándote el símbolo favorito de tu querida madre,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 01
    show m_exp_piris right01
    show m_exp_eyebrows angryx04
    with dissolve

    dad "serías capaz de encontrarla?"

    show m_exp_mouth happy_Talkingx12
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows normal
    with dissolve

    dad "¿Te crees que es tan incauta y estúpida?"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    dad "Si ha estado más de veinte años escondida,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx04
    with dissolve

    dad "es porque no es la niñata patosa y cobarde que eres tú."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows angryx03
    with dissolve

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx05
    with fade

    ne "..."

    # show m_exp_mouth sad_Talkingx004
    # show m_exp_eyes 08
    # show m_exp_piris front08
    # show m_exp_eyebrows serious
    # with dissolve

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx07
    with Dissolve(0.5)

    dad "Elur..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx01
    with fade

    dad "¿Realmente creías que después de tantas décadas acostumbrada a vivir con tanto poder,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 03
    show m_exp_piris right03
    show m_exp_eyebrows sadx02
    with dissolve

    dad "serías capaz de sobrevivir,"

    extend " y esconderte de mi,"

    extend " al mismo tiempo?"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "¿sin usar más sacrificios?"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Tu madre entendió ese principio tan básico mucho mejor que tú."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    ne "..."

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx002
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx05
    with fade

    ne "No..."

    show neus_exp_mouth sad_Talkingx04
    $ nteye = 3
    call neus_exp_tears_tears
    show neus_exp_iris left03
    show neus_exp_eyebrows sadx04
    with dissolve

    ne "No quería matar más..."

    show neus_exp_mouth sadbiting_Silentx04
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx01
    with dissolve

    pt "¿Más...?"

    show neus_exp_mouth sad_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows sadx03
    with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris front04
    show neus_exp_eyebrows sadx05
    with Dissolve(0.5)

    dad "¿A quien quieres engañar?"

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris right05
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx01
    with fade

    dad "Mi preciosa niñita de ojos verdes;"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris right02
    show m_exp_eyebrows sadx03
    with dissolve

    dad "te falta tanto aún por aprender..."

    show m_exp_mouth happy_Silentx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows serious
    with dissolve

    ne "..."

    ##

    if afternight05_Pedrera_Guarantee_ContactYou_Cond: # Le has pedido de volver a tu antigua vida en lugar de formar parte de su harén.

        jump afternight05_Pedrera_NeusWillDie_DidacOption

    else:

        jump afternight05_Pedrera_NeusWillDie_IfYouDieNow
            # dad "Ten en cuenta que si te mato ahora,"
            # dad "tendrás una muerte más o menos,"
            # extend " poco dolorosa."

label afternight05_Pedrera_NeusWillDie_DidacOption:

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "¿Realmente quieres volver a intentar vivir tu aburrida"

    extend " monótona,"

    extend " y pésima existencia,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "como hormiga?"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Nunca olvidarás lo que has experimentado estos días."

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "Piénsatelo bien."

    show m_exp_mouth sad_Talkingx02
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows angryx01
    with dissolve

    dad "Porque por mucho que luego me lo implores,"

    show m_exp_mouth sad_Talkingx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx02
    with dissolve

    dad "no te lo volveré a ofrecer."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth happy_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "¿O quizás prefieras la muerte?"

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    menu:

        "¿Por qué iba a preferir la muerte?":
            call p_Help

            jump afternight05_Pedrera_NeusWillDie_WhyDeath

        "...":
            call p_Help

            jump afternight05_Pedrera_NeusWillDie_ItsTime
                # dad "Ya va siendo hora de terminar con esto."

            # jump afternight05_Pedrera_NeusWillDie_IfYouDieNow
            #     # dad "Ten en cuenta que si te mato ahora,"
            #     # dad "tendrás una muerte más o menos,"
            #     # extend " poco dolorosa."
            #     # dad "Pero si intentaras contactar con mis hijas,"

label afternight05_Pedrera_NeusWillDie_WhyDeath:

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "Vivir una vida en la que cualquiera con una pistola puede volarte los sesos,"

    show m_exp_mouth sad_Talkingx07
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    dad "en la que en cualquier día puedes sufrir un accidente mortal,"

    show m_exp_mouth sad_Talkingx08
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows angryx01
    with dissolve

    dad "tener una enfermedad terminal,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "usar plásticos incómodos en el sexo,"

    show m_exp_mouth sad_Talkingx09
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "para no contraer una enfermedad,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "o tener un molesto vástago."

    if afternight05_Pedrera_AntExplanation_Cond:

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows normal
        with dissolve

        dad "En definitiva,"

        extend " como ya te he comentado antes,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 01
        show m_exp_piris front01
        show m_exp_eyebrows angryx01
        with dissolve

        dad "para no ser una hormiga más."

        show m_exp_mouth sad_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows serious
        with dissolve

        p "..."

    else:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "En dónde la mitad de la vida te la pasas durmiendo,"

        show m_exp_mouth sad_Talkingx005
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows normal
        with dissolve

        dad "y la otra la dedicas a algo que si a corto plazo no te aburre,"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows serious
        with dissolve

        dad "a la larga te desespera."

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows angryx01
        with dissolve

        dad "Simplemente para ser una hormiga más en un mundo,"

        show m_exp_mouth sad_Talkingx06
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows serious
        with dissolve

        dad "dónde el noventa por ciento de los recursos,"

        extend " el tiempo,"

        extend " y los lujos,"

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "les pertenece al diez por ciento más adinerado;"

        show m_exp_mouth happy_Talkingx06
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex001
        with dissolve

        dad "y los demás tenéis que repartiros las sobras."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows serious
        with dissolve

        dad "No solo trabajando como esclavos,"

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows normal
        with dissolve

        dad "sino además dando las gracias por tener ese trabajo,"

        show m_exp_mouth happy_Talkingx08
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows suspiciousx02
        with dissolve

        dad "aunque sea con horas extras,"

        extend " y salvando la empresa de la quiebra,"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "creyendo que así podrán conservar el empleo;"

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows surprisex02
        with dissolve

        dad "pues muchos no tienen ni eso."

        show m_exp_mouth happy_Silentx03
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows suspiciousx01
        with dissolve

        p "..."

        show m_exp_mouth happy_Talkingx05
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve

        dad "Los animales de compañía vivirán en una prisión de cuatro paredes,"

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows surprisex01
        with dissolve

        dad "y sin demasiada libertad,"

        show m_exp_mouth sad_Talkingx08
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx02
        with dissolve

        dad "pero diablos..."

        show m_exp_mouth happy_Talkingx07
        show m_exp_eyes 02
        show m_exp_piris front02
        show m_exp_eyebrows suspiciousx01
        with dissolve

        dad "seguro que la mayoría de dueños envidian el estilo de vida de sus mascotas."

        show m_exp_mouth sad_Talkingx04
        show m_exp_eyes 03
        show m_exp_piris left03
        show m_exp_eyebrows surprisex02
        with dissolve

        dad "Aunque eso de que se los castre,"

        extend " ya es otro tema..."

        show m_exp_mouth happy_Silentx04
        show m_exp_eyes 08
        show m_exp_piris front08
        show m_exp_eyebrows angryx01
        with dissolve

    menu:

        "¿Y qué me dices de vivir tu vida inmortal carente de afecto y sentimientos?":
            call p_Help

            $pl.ch_pts("np",1)

            jump afternight05_Pedrera_NeusWillDie_EmptyImmortalLife

        "...":
            call p_Help

            jump afternight05_Pedrera_NeusWillDie_IfYouDieNow
                # dad "Ten en cuenta que si te mato ahora,"
                # dad "tendrás una muerte más o menos,"
                # extend " poco dolorosa."
                # dad "Pero si intentaras contactar con mis hijas,"

label afternight05_Pedrera_NeusWillDie_EmptyImmortalLife:

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    p "En la que no existe la adrenalina,"

    extend " ni la emoción de vivir al límite,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex02
    with dissolve

    p "no hay ningún reto que suponga un verdadero desafío,"

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "dónde todo es posible,"

    extend " y al mismo tiempo nada es nuevo."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    p "dónde dices tener libertad,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    p "pero prohíbes cualquier tipo de sentimiento,"

    extend " u amistad,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex001
    with dissolve

    p "que no esté en tu circulo incestuoso."

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "Aprenderás que solo en la sangre uno puede confiar,"

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows angryx01
    with dissolve

    dad "e incluso así,"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "a veces te traicionan."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx02
    with fade

    ne "..."

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with fade

    p "No me imagino vivir así durante cien años."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¿Qué clase de vida es esta,"

    show m_exp_mouth sad_Silentx05
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "en la que no puedes tener amigos,"

    extend " o conocidos,"

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    p "sin tener la sensación,"

    extend " que si te encariñas demasiado con ellos,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows surprisex001
    with dissolve

    p "lo más probable es que tenga que acabar matándolos yo mismo"

    p "por tu miedo,"

    extend " o tu capricho."

    show m_exp_mouth sad_Silentx02
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex002
    with dissolve

    dad "Hmm..."

    show m_exp_mouth sad_Silentx04
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "Quizás es verdad que en ocasiones se vive"

    extend " y se ama,"

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows normal
    with dissolve

    p "como si cada día fuera el último;"

    show m_exp_mouth happy_Silentx02
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¡pero eso también le da mucho más valor!"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 04
    show m_exp_piris right04
    show m_exp_eyebrows suspiciousx02
    with dissolve

    dad "Elur es alguien que ama así."

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows sadx01
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 2
    call neus_exp_tears_tears
    show neus_exp_iris left02
    show neus_exp_eyebrows sadx01
    with fade

    p "..."

    show neus_exp_mouth sadbiting_Silentx06
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows sadx04
    with Dissolve(0.5)

    dad "Porque sabe que todo aquel que ha amado en su vida,"

    if ntlong in range (0,6):
        if ntlong < 5:
            $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows angryx01
    with Dissolve(0.5)

    dad "ha acabado muerto en menos de seis meses."

    show neus_exp_mouth sad_Silentx08
    $ nteye = 5
    call neus_exp_tears_tears
    show neus_exp_iris left05
    show neus_exp_eyebrows angryx03
    with dissolve

    dad "Eso es amar con intensidad."

    $ Pedrera_char_Cond = "TxellNeus"
    call Pedrera_char_lab

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows suspiciousx02

    show neus_exp_mouth sad_Silentx07
    $ nteye = 4
    call neus_exp_tears_tears
    show neus_exp_iris left04
    show neus_exp_eyebrows angryx01
    with Dissolve(0.5)

    with dissolve

    dad "¿Verdad que sí?"

    extend " {i}Txiki{/i}"

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02

    show neus_exp_mouth sadbiting_Silentx07
    $ nteye = 7
    call neus_exp_tears_tears
    show neus_exp_iris front07
    show neus_exp_eyebrows sadx06
    with Dissolve(0.5)

    pause 0.2

    $ Pedrera_char_Cond = "TxellClose"
    call Pedrera_char_lab

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris right05
    show m_exp_eyebrows angryx02
    with fade

    menu:

        "Creo que no entiendes el significado del amor.":
            call p_Help

            $pl.ch_pts("np",1)

            show m_exp_mouth sad_Silentx03
            show m_exp_eyes 04
            show m_exp_piris front04
            show m_exp_eyebrows surprisex001
            with dissolve

            dad "¿Hmm...?"

            show m_exp_mouth happy_Talkingx09
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows surprisex002
            with dissolve

            dad "¿Y tú sí?"

            show m_exp_mouth happy_Silentx07
            show m_exp_eyes 05
            show m_exp_piris front05
            show m_exp_eyebrows normal
            with dissolve

            menu:

                "¡Al menos mucho mejor que tú!":
                    call p_Help

                    $pl.ch_pts("np",1)

                    show m_exp_mouth happy_Talkingx10
                    show m_exp_eyes 01
                    show m_exp_piris front01
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    dad "¿Con menos de cien años?"

                    show m_exp_mouth happy_Talkingx07
                    show m_exp_eyes 03
                    show m_exp_piris front03
                    show m_exp_eyebrows angryx01
                    with dissolve

                    dad "Permíteme que lo dude..."

                    show m_exp_mouth happy_Silentx06
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve

                    p "..."

                    if afternight05_Pedrera_NeusLoveDoubts_Cond == False:

                        call afternight05_Pedrera_NeusLoveDoubts

                "...":
                    call p_Help

        "...":
            call p_Help

    
    ##

label afternight05_Pedrera_NeusWillDie_IfYouDieNow:

    $ meyesc = "_red"

    show m_exp_mouth sad_Talkingx005
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Ten en cuenta hijo,"

    show m_exp_mouth sad_Talkingx05
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows normal
    with dissolve

    dad "que si te mato ahora,"

    show m_exp_mouth sad_Talkingx006
    show m_exp_eyes 03
    show m_exp_piris left03
    show m_exp_eyebrows suspiciousx01
    with dissolve

    dad "tendrás una muerte más o menos,"

    extend " poco dolorosa."

    show m_exp_mouth sad_Talkingx04
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    dad "Pero si intentaras contactar con mis hijas,"

    show m_exp_mouth sad_Talkingx06
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    if DidacPregnant:

        dad "o pusieras al descubierto el origen de la transformación de tu amigo a algún humano;"

    else:

        dad "o intentaras contarle a alguien lo que le pasó a tu amigo;"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "lamentarías esa decisión por el resto de tu nueva eternidad."

    show m_exp_mouth sad_Silentx03
    show m_exp_eyes 03
    show m_exp_piris front03
    show m_exp_eyebrows serious
    with dissolve

    p "¿Nueva eternidad?"

    show m_exp_mouth happy_Silentx01
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows suspiciousx01
    with dissolve

    p "¿Ese sería tu castigo?"

    if music_play != "echoesOfTimev2":
        play music "audio/music/kevinmacleod/creepy/echoesOfTimev2.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "echoesOfTimev2"

    show m_exp_mouth happy_Silentx03
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows suspiciousx02
    with dissolve

    p "¿Darme la vida eterna?"

    show m_exp_mouth happy_Silentx05
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows normal
    with dissolve

    dad "Hmm..."

    $ meyesc = "_goat"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "No sería precisamente para disfrutar de los placeres que te me he mencionado antes."

    show m_exp_mouth sad_Talkingx003
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "No..."

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows surprisex02
    with dissolve

    dad "Si te parece cruel lo que {a=https://www.youtube.com/watch?v=o2W3jfvZU4w}Zeus{/a} le hizo a {a=https://es.wikipedia.org/wiki/Prometeo}Prometeo{/a},"

    show m_exp_mouth happy_Talkingx08
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "al encadenarlo a una roca,"

    show m_exp_mouth happy_Talkingx07
    show m_exp_eyes 04
    show m_exp_piris front04
    show m_exp_eyebrows serious
    with dissolve

    dad "sin movilidad alguna,"

    show m_exp_mouth happy_Talkingx09
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "para que su hígado fuera devorado sin piedad por un águila durante el día,"

    show m_exp_mouth happy_Talkingx06
    show m_exp_eyes 02
    show m_exp_piris front02
    show m_exp_eyebrows serious
    with dissolve

    dad "y regenerado durante la noche,"

    show m_exp_mouth happy_Talkingx11
    show m_exp_eyes 01
    show m_exp_piris front01
    show m_exp_eyebrows surprisex001
    with dissolve

    dad "para repetir el mismo proceso cada día hasta el fin de los días;"

    show m_exp_mouth happy_Talkingx12
    show m_exp_eyes 00
    show m_exp_piris front00
    show m_exp_eyebrows serious
    with dissolve

    dad "es porque aún no me conoces lo suficiente."

    show m_exp_mouth happy_Silentx08
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx01
    with dissolve

    p "..."

    show m_exp_mouth happy_Silentx10
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows angryx02
    with dissolve

    n "Sientes una gota de sudor frío recorriendo tu frente."

label afternight05_Pedrera_NeusWillDie_ItsTime:

    $ meyesc = "_goat"

    # These can be deleted in the future?
    $ nleye = ""
    $ p_ao_n_horns = ""
    $ nblush = 2
    $ dteye = 0
    $ dtlong = 0

    show m_exp_mouth sad_Talkingx004
    show m_exp_eyes 08
    show m_exp_piris front08
    show m_exp_eyebrows surprisex01
    with dissolve

    dad "Ya va siendo hora de terminar con esto."

    if music_play != "theDread":
        play music "audio/music/kevinmacleod/creepy/theDread.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theDread"

    show m_exp_mouth happy_Silentx07
    show m_exp_eyes 05
    show m_exp_piris front05
    show m_exp_eyebrows serious
    with dissolve

    if afternight05_Pedrera_NoChoice_Refuse_Cond == False:

        show m_exp_mouth sad_Talkingx05
        show m_exp_eyes 03
        show m_exp_piris front03
        show m_exp_eyebrows angryx01
        with dissolve

        dad "Ahora acércate a mi hija y ponle las manos sobre su tierno cuello,"

        show m_exp_mouth sad_Talkingx004
        show m_exp_eyes 04
        show m_exp_piris front04
        show m_exp_eyebrows normal
        with dissolve

        dad "como me has dicho que harías."

        show m_exp_mouth happy_Silentx06
        show m_exp_eyes 05
        show m_exp_piris front05
        show m_exp_eyebrows angryx01
        with dissolve

        menu:

            "<Obedecerle>":
                call p_Help
                $pl.ch_pts("np",-15)

            "Lo siento, pero no puedo...":
                call p_Help

                $pl.ch_pts("np",5)

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 03
                show m_exp_piris front03
                show m_exp_eyebrows suspiciousx01
                with dissolve

                dad "..."

                $ Pedrera_char_Cond = "NeusClose"
                call Pedrera_char_lab

                if ntlong in range (0,6):
                    if ntlong > 0:
                        $ ntlong -= 1

                show neus_exp_mouth happybiting_Silentx03
                $ nteye = 2
                call neus_exp_tears_tears
                show neus_exp_iris front02
                show neus_exp_eyebrows sadx01
                with fade

                ne "..."

                $ Pedrera_char_Cond = "TxellNeus"
                call Pedrera_char_lab

                show m_exp_mouth sad_Silentx05
                show m_exp_eyes 04
                show m_exp_piris right04
                show m_exp_eyebrows angryx01

                show neus_exp_mouth happy_Silentx04
                $ nteye = 3
                call neus_exp_tears_tears
                show neus_exp_iris front03
                show neus_exp_eyebrows sadx02
                with fade

                dad "..."

                $ Pedrera_char_Cond = "TxellClose"
                call Pedrera_char_lab

                show m_exp_mouth sad_Talkingx07
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows surprisex01
                with fade

                dad "Después de lo que me has dicho;"

                if afternight05_Pedrera_Guarantee_ContactYou_Cond:

                    show m_exp_mouth sad_Talkingx04
                    show m_exp_eyes 05
                    show m_exp_piris front05
                    show m_exp_eyebrows serious
                    with dissolve

                    dad "y de estar planeando como devolverte a tu antigua vida,"

                    show m_exp_mouth happy_Talkingx05
                    show m_exp_eyes 08
                    show m_exp_piris front08
                    show m_exp_eyebrows surprisex02
                    with dissolve

                    dad "con tu nueva ninfómana..."

                show m_exp_mouth sad_Talkingx08
                show m_exp_eyes 02
                show m_exp_piris front02
                show m_exp_eyebrows angryx01
                with dissolve

                dad "¿Ahora te niegas?"

                show m_exp_mouth sad_Silentx04
                show m_exp_eyes 04
                show m_exp_piris front04
                show m_exp_eyebrows suspiciousx01
                with dissolve

                p "..."

                show m_exp_mouth sadbiting_Silentx04
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows serious
                with dissolve

                p "No soy un asesino."

                show m_exp_mouth happy_Talkingx07
                show m_exp_eyes 01
                show m_exp_piris front01
                show m_exp_eyebrows angryx01
                with dissolve

                dad "Pues entonces serás un cadáver."

                show m_exp_mouth happy_Silentx06
                show m_exp_eyes 05
                show m_exp_piris front05
                show m_exp_eyebrows angryx02
                with dissolve

                $ afternight05_Pedrera_NeusWillDie_Forced_Cond = True

    else:

        $ afternight05_Pedrera_NeusWillDie_Forced_Cond = True

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    $ nteye = 0
    call neus_exp_tears_tears
    show neus_exp_iris front00
    show neus_exp_eyebrows surprisex02
    with fade

    pause 0.1

    play sound "audio/sfx/fall01.ogg"

    $ p_neuspos = "n_closefromup_"

    #scene bg dark_a
    scene night04_pedrera_baba02_background:
            truecenter
            zoom 1.0 xpos 0.5 ypos 1.0
    show n_closefromup_body sd:
        n_closefromup_05_position
    show n_closefromup_blush 03:
        n_closefromup_05_position
    show n_closefromup_eyes 00:
        n_closefromup_05_position
    show n_closefromup_iris front00:
        n_closefromup_05_position
    show n_closefromup_eyebrows sadx01:
        n_closefromup_05_position
    show n_closefromup_tears 00_03:
        n_closefromup_05_position
    show n_closefromup_mouth sadbiting_Silentx01:
        n_closefromup_05_position
    show n_closefromup_glasses:
        n_closefromup_05_position
    show n_closefromup_hair_front:
        n_closefromup_05_position
    show stra_handR empty
    show stra_handL empty
    call n_closefromup_tears_tears
    with vpunch
    with vpunch

    if afternight05_Pedrera_NeusWillDie_Forced_Cond:

        show n_closefromup_mouth sadbiting_Silentx03
        #show n_closefromup_tears 01_05
        #show n_closefromup_eyes 01
        $ nteye = 1
        call n_closefromup_tears_tears 
        show n_closefromup_iris front01
        show n_closefromup_eyebrows sadx02
        with dissolve

        n "Sientes que tus piernas se mueven por si solas dirigiéndose hasta dónde está [neusname],"

        show n_closefromup_mouth sadbiting_Silentx04
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_iris right01
        show n_closefromup_eyebrows sadx03
        with dissolve

        n "la cual retrocede inconscientemente al ver como te le acercas,"

        show n_closefromup_mouth sadbiting_Silentx05
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_iris right02
        show n_closefromup_eyebrows sadx04
        with dissolve

        n "hasta chocar su espalda contra la pared"

        if ntlong in range (0,6):
            if ntlong < 5:
                $ ntlong += 1

        show n_closefromup_mouth sadbiting_Silentx09
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_iris right04
        show n_closefromup_eyebrows sadx04
        with dissolve

        ne "..."

    else:

        show n_closefromup_mouth sadbiting_Silentx02
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_iris front01
        show n_closefromup_eyebrows sadx02
        with dissolve

        n "Obedeces sus órdenes acercándote a ella,"

        if ntlong in range (0,6):
            if ntlong < 5:
                $ ntlong += 1

        show n_closefromup_mouth sadbiting_Silentx10
        $ nteye = 0
        call n_closefromup_tears_tears
        show n_closefromup_iris right00
        show n_closefromup_eyebrows sadx01
        with dissolve

        n "mientras esta retrocede al ver como te acercas sin titubeos hacia ella,"

        show n_closefromup_mouth sad_Silentx08
        $ nteye = 7
        call n_closefromup_tears_tears
        show n_closefromup_iris front07
        show n_closefromup_eyebrows sadx05
        with dissolve

        n "hasta chocar su espalda contra la pared."

    show n_closefromup_mouth sadbiting_Silentx04
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_iris front05
    show n_closefromup_eyebrows sadx04
    with dissolve

    n "deteniéndote a escasos centímetros de su rostro."

    if afternight05_Pedrera_NeusWillDie_Forced_Cond == False:

        show n_closefromup_mouth sadbiting_Silentx03
        $ nteye = 1
        call n_closefromup_tears_tears
        show n_closefromup_iris down01
        show n_closefromup_eyebrows surprisex01

        show stra_handR rest:
            ypos 1.3
        show stra_handL rest:
            ypos 1.3
        with Dissolve(0.5)

        n "Para luego alzar tus manos,"

        show n_closefromup_mouth sadbiting_Silentx04
        $ nteye = 2
        call n_closefromup_tears_tears
        show n_closefromup_iris front02
        show n_closefromup_eyebrows sadx01
        with Dissolve(0.5)

        n "y acercar tus dedos al suave cuello cubierto por esa delgada tela."

    show n_closefromup_mouth sadbiting_Silentx02
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_iris front05
    show n_closefromup_eyebrows sadx05
    with dissolve

    p "..."

    if ntlong in range (0,6):
        if ntlong < 5:
            $ ntlong += 1

    show n_closefromup_mouth sadbiting_Silentx03
    $ nteye = 5
    call n_closefromup_tears_tears
    show n_closefromup_iris front05
    show n_closefromup_eyebrows sadx06
    with dissolve

    dad "Que imagen tan hermosa entre hermanos..."

    show n_closefromup_mouth sad_Silentx07
    $ nteye = 6
    call n_closefromup_tears_tears
    show n_closefromup_iris front06
    show n_closefromup_eyebrows sadx06
    with dissolve

    dad "Ahora estrangulala."

label afternight05_Pedrera_NeusWillDie_HandsUp:

    if afternight05_Pedrera_NeusWillDie_Forced_Cond:

        show n_closefromup_mouth sadbiting_Silentx03
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_iris front05
        show n_closefromup_eyebrows sadx01
        with dissolve

        p "No..."

        show n_closefromup_mouth happybiting_Silentx01
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_iris front04
        show n_closefromup_eyebrows sadx02
        with dissolve

        p "No puedo..."

        show n_closefromup_mouth happy_Silentx01
        $ nteye = 5
        call n_closefromup_tears_tears
        show n_closefromup_iris front05
        show n_closefromup_eyebrows sadx01
        with dissolve

        dad "Hmm..."

        show n_closefromup_mouth sadbiting_Silentx03
        $ nteye = 4
        call n_closefromup_tears_tears
        show n_closefromup_iris front04
        show n_closefromup_eyebrows sadx03
        with dissolve

        n "Sin poder evitarlo,"

        #scene bg dark_a
        scene night04_pedrera_baba02_background:
            truecenter
            zoom 1.0 xpos 0.5 ypos 1.0
        show n_closefromup_body_sd_FULL:
            stra_neus_exp_pos
        show n_closefromup_blush 03:
            stra_neus_exp_pos
        show n_closefromup_mouth sadbiting_Silentx03:
            stra_neus_exp_pos
        show n_closefromup_tears 06_05:
            stra_neus_exp_pos

        show stra_handR rest
        show stra_handL rest
        with fade

        n "sientes que los músculos de tus extremidades superiores levantan tus brazos,"

        # show n_closefromup_mouth sadbiting_Silentx02
        # with dissolve

        n "y tus manos se posan en el cuello de [neusname]."

        # show n_closefromup_mouth sad_Silentx03
        # with dissolve

        dad "A partir de ahora,"

        extend " es cosa tuya."

    else:

        #scene bg dark_a
        scene night04_pedrera_baba02_background:
            truecenter
            zoom 1.0 xpos 0.5 ypos 1.0
        show n_closefromup_body_sd_FULL:
            stra_neus_exp_pos
        show n_closefromup_blush 03:
            stra_neus_exp_pos
        show n_closefromup_mouth sadbiting_Silentx03:
            stra_neus_exp_pos
        show n_closefromup_tears 06_05:
            stra_neus_exp_pos

        show stra_handR rest
        show stra_handL rest
        with fade

        p "..."

    # show n_closefromup_mouth sad_Silentx03
    # with dissolve

    if renpy.variant("pc"):

        show stra_handR empty
        with Dissolve(0.5)

        dad "Si no sujetas con fuerza su cuello con la mano izquierda,"

        extend " {font=fonts/chinrg__.ttf}{color=#f00}{i}(\"Botón: Espacio del teclado\"){/i}{/color}{/font}"

        show stra_handR rest
        show stra_handL empty
        with Dissolve(0.5)

        dad "y derecha,"

        extend " {font=fonts/chinrg__.ttf}{color=#f00}{i}(\"Botón: Izquierdo del Ratón\"){/i}{/color}{/font}"

        show stra_handR rest
        show stra_handL rest
        with Dissolve(0.5)

    else:

        show stra_handR stra
        show stra_handL stra
        with Dissolve(0.5)

        dad "Si no sujetas con fuerza su cuello con ambas manos,"

        extend " {font=fonts/chinrg__.ttf}{color=#f00}{i}(\"Aguantar botón encima de la pantalla\"){/i}{/color}{/font}"

        aj "Si hay errores en la versión Android en esta acción, por favor, decídmelo."

        show stra_handR rest
        show stra_handL rest
        with Dissolve(0.5)

    dad "los latidos de tu corazón irán reduciéndose,"

    dad "hasta detenerse del todo."

    p "..."

    dad "Tranquilo,"

    extend " ella no podrá hacerte nada,"

    dad "de eso me aseguro yo."

    show n_closefromup_mouth sadbiting_Silentx03
    with dissolve

    $ dad = d_dad

    p "..."

    hide screen Points
    hide screen quick_menu

    #########################################################

    if config.version < "00.14.02": # Pedrera - Now do it.
        call endupdatescript
    
    #######################################################



#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

label afternight05_Pedrera_Strangle:

    if music_play != "theHouseOfLeaves":
        play music "audio/music/kevinmacleod/creepy/theHouseOfLeaves.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theHouseOfLeaves"

    show stra_handR empty
    show stra_handL empty
    show n_closefromup_mouth empty

    show screen stra_neus_transpa
    call screen stra_neus

    if stra_number < 1000:

        show stra_handL rest
        show stra_handR rest
        show n_closefromup_mouth sadbiting_Silentx03
        pause 0.1

    #"YOUUUUH"

    if (stra_number > 0) and (stra_number < 1000):

        $ randomnum_1to5 = renpy.random.randint(1, 5)

#### FATHER
        if (stra_number < 15):

            if randomnum_1to5 == 1:

                dad "Patético."

            elif randomnum_1to5 == 2:

                dad "Que decepción..."

            elif randomnum_1to5 == 3:
            
                dad "Hormiga tenías que ser."

            elif randomnum_1to5 == 4:

                dad "Que pérdida de tiempo."

            elif randomnum_1to5 == 5:

                dad "Adiós hijo."    
#### #####

        elif (stra_number < 55) and (str_talkNeus == 5):

            show n_closefromup_mouth sad_Silentx08
            with dissolve

            n "Sientes tus párpados cada vez más pesados."

            show n_closefromup_mouth sad_Talkingx07
            with dissolve

            ne "¡[protname]!"

            show n_closefromup_mouth sad_Talkingx08
            with dissolve

            ne "¡Aprieta!"

            show n_closefromup_mouth sad_Talkingx05
            with dissolve

            ne "¡No mueras por mi culpa!"

            show n_closefromup_mouth sad_Talkingx09
            with dissolve

            ne "¡Resucitaré mañana!"

            show n_closefromup_mouth sad_Talkingx10
            with dissolve

            ne "¡Pero tú no!"

            show n_closefromup_mouth sad_Talkingx07
            with dissolve

            ne "¡No te detengas ahora!"

            # show n_closefromup_mouth sad_Silentx09
            # with dissolve

#### FATHER
        elif (stra_number < 105):

            if randomnum_1to5 == 1:

                dad "Vas a morir."

            elif randomnum_1to5 == 2:

                dad "¿Morirás por no matarla?"

            elif randomnum_1to5 == 3:
            
                dad "Es tu última oportunidad."

            elif randomnum_1to5 == 4:

                dad "Si no reaccionas,"

                extend " morirás."

            elif randomnum_1to5 == 5:

                dad "Este es tu fin."
#### #####

        elif (stra_number < 155) and (str_talkNeus == 4):

            show n_closefromup_mouth sad_Talkingx03
            with dissolve

            ne "Si hubiera sido más valiente..."

            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "Si te lo hubiera pedido directamente..."

            show n_closefromup_mouth sad_Talkingx02
            with dissolve

            ne "Quizás hubieras aceptado,"

            if pl.np < 100:

                show n_closefromup_mouth sad_Talkingx01
                with dissolve

                ne "Quizás hubiera podido gustarte un poco más..."

            else:

                show n_closefromup_mouth sad_Talkingx03
                with dissolve

                ne "quizás hubiéramos sido felices..."

            # show n_closefromup_mouth sadbiting_Silentx05
            # with dissolve

#### FATHER
        elif (stra_number < 255):

            if randomnum_1to5 == 1:

                dad "No tenemos todo el día."

            elif randomnum_1to5 == 2:

                dad "¿A qué estás esperando?"

            elif randomnum_1to5 == 3:
            
                dad "Se va a hacer de noche."

            elif randomnum_1to5 == 4:

                dad "Al final se me acabará la paciencia."

            elif randomnum_1to5 == 5:

                dad "Acabarás muerto como esperes demasiado."
#### #####

        elif (stra_number < 325) and (str_talkNeus == 3):

            if pl.np < 100:

                show n_closefromup_mouth sad_Talkingx04
                with dissolve

                ne "Quizás, si hubiera hecho las cosas de otra manera,"

                show n_closefromup_mouth sad_Talkingx03
                with dissolve

                ne "hubieras actuado de forma distinta conmigo..."

            else:

                show n_closefromup_mouth sad_Talkingx03
                with dissolve

                ne "Tendría que haber hecho las cosas de otra manera;"

                show n_closefromup_mouth sad_Talkingx04
                with dissolve

                ne "Me hubiera gustado poder pasar más tiempo contigo..."

                # show n_closefromup_mouth sad_Silentx05
                # with dissolve

        elif (stra_number < 375) and (str_talkNeus == 2):

            show n_closefromup_mouth sad_Talkingx05
            with dissolve

            ne "No debí haberle hecho nada a aquel pobre niño..."

            show n_closefromup_mouth sad_Talkingx03
            with dissolve

            ne "Este es mi castigo."

            if pl.np < 100:

                show n_closefromup_mouth sad_Talkingx02
                with dissolve

                ne "Quizás no eres exactamente cómo te describió,"

                show n_closefromup_mouth sad_Talkingx03
                with dissolve

                ne "pero estoy contenta de saber,"

                extend " que por lo menos,"

                show n_closefromup_mouth sad_Talkingx04
                with dissolve

                ne "no eres el monstruo que es nuestro padre."

                show n_closefromup_mouth sad_Silentx06
                with dissolve

                pt "¿Que te describió?"

                show n_closefromup_mouth sad_Silentx07
                with dissolve

                pt "¿Quien?"

            else:

                show n_closefromup_mouth happy_Talkingx03
                with dissolve

                ne "Al menos sé que tenía razón..."

                show n_closefromup_mouth happy_Silentx02
                with dissolve

                pt "¿Tenía razón?"

                extend " ¿quien?"

                show n_closefromup_mouth sad_Talkingx03
                with dissolve

                ne "realmente,"

                show n_closefromup_mouth happy_Talkingx02
                with dissolve

                ne "eres una buena persona,"

                show n_closefromup_mouth sad_Talkingx02
                with dissolve

                ne "[protname]..."

                # show n_closefromup_mouth sad_Silentx04
                # with dissolve

        elif (stra_number < 405) and (str_talkNeus == 1):

            show n_closefromup_mouth sad_Talkingx03
            with dissolve

            ne "Hazlo [protname]."

            show n_closefromup_mouth sad_Talkingx04
            with dissolve

            ne "Es lo que realmente merezco."

            # show n_closefromup_mouth sad_Silentx06
            # with dissolve

#### FATHER
        elif (stra_number < 455):

            if renpy.variant("pc"):

                dad "Agárrala con tu mano izquierda,"

                extend " {font=fonts/chinrg__.ttf}{color=#fff}{i}(\"Botón: Espacio del teclado\"){/i}{/color}{/font}"

                dad "y con tu mano derecha,"

                extend " {font=fonts/chinrg__.ttf}{color=#fff}{i}(\"Botón: Izquierdo del Ratón\"){/i}{/color}{/font}"

            else:

                dad "Agarrála con fuerza,"

            dad "y no la sueltes hasta que deje de respirar."
#### #####

        elif stra_number > 500:

            $ str_adviceDad = 0

        show stra_handL empty
        show stra_handR empty
        show n_closefromup_mouth empty
    
        jump afternight05_Pedrera_Strangle

    elif stra_number <= 0:
        # You're dead.

        jump afternight05_Pedrera_Strangle_LastBeat


    elif stra_number >= 1000:


        show n_closefromup_mouth sad_Talkingx02
        show stra_handR stra
        show stra_handL stra

        pause 0.1

        stop music fadeout 3.0

        pause

        play sound "audio/sfx/fall01.ogg"

        scene bg dark_a
        with vpunch

        hide screen stra_neus_transpa
        with Dissolve(3.0)

        pause

        pt "[neusname]..."

        if music_play != "colorless_aura":
            play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "colorless_aura"

        dad "No está mal hijo,"

        extend " no está mal..."
        
        pt "Está muerta..."

        jump endupdate

    else:
        n "Error... fuck."

    hide screen stra_neus_transpa
    with fade


    # dad "Date prisa."

    # # pasados unos segundos.

    # dad "No tenemos toda la noche."

    # ne "Hazlo [protname]."

    # ne "Es lo que realmente merezco."

    # #
    # #

    # ne "No debí lastimar a aquel niño..."

    # if pl.np < 100:

    #     ne "Quizas si hubiera las cosas distintas,"

    #     ne "hubieras actuado de forma distinta conmigo..."

    # else:

    #     ne "Tendría que haber hecho las cosas distintas..."

    # ne "Si hubiera sido más valiente..."

    # ne "si te lo hubiera pedido directamente..."

    # ne "quizás hubieras aceptado,"

    # if pl.np < 100:

    #     ne "quizás hubiera podido gustarte un poco más..."

    # else:

    #     ne "quizás hubiéramos sido felices..."

    # ne "y nada de esto hubiera ocurrido."

    # ne "Este es mi castigo."

    # if pl.np < 100:

    #     ne "Quizás no eres exactamente cómo te describió,"

    #     ne "pero estoy contenta de saber,"

    #     extend " que por lo menos,"

    #     ne "no eres el monstruo que es nuestro padre."

    #     pt "¿Que te describió?"

    #     pt "¿Quien?"

    # else:

    #     ne "Al menos sé que tenía razón..."

    #     pt "¿Tenía razón?"

    #     extend " ¿quien?"

    #     ne "realmente,"

    #     ne "eres una buena persona,"

    #     ne "[protname]..."

    #     ne "Me hubiera gustado poder pasar más tiempo contigo..."

    # #
    # #

    # ne "Hazlo..."

    # ne "Por favor..."

    # ne "No mueras por mi..."

    # ne "Te lo pido..."

    # # Estas conversaciones van apareciendo según si aprietas o no.

    # # Si terminas por ahogarla te vas al final en el que él te da la opción de formar parte de su harén o volver a tu antigua vida.

    # ne "Ughh..."

    # # Pero si terminas por no asfixiarla... tu corazón se detiene.

    # ono "{size=40}BU-"

    # extend "BUM{/size}"

    # ono "{size=35}BU-"

    # extend "BUM{/size}"

    # ono "{size=30}BU-"

    # extend "BUM{/size}"

    # n "Sientes tus párpados cada vez más pesados."

    # ne "¡[protname]!"

    # ne "¡Aprieta!"

    # ne "¡No mueras por mi culpa!"

    # ne "¡Por favor!"

    # ne "¡Resucitaré mañana!"

    # ne "¡Pero tú no!"

    # ne "Por favor..."

    # ne "¡No te detengas ahora!"

    # p "No..."

    # p "No puedo..."

    # dad "Hmmmph..."

    # dad "Que decepción de hijo."

    # ono "{size=20}BU-"

    # extend "BUM{/size}"

    # ono "{size=15}BU-"

    # extend "BUM{/size}"

    # ono "{size=10}BU-"

    # extend "BUM{/size}"

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

#####################################################################################
#####################################################################################
#####################################################################################
#####################################################################################

label afternight05_Pedrera_Strangle_LastBeat:

    hide screen Points
    hide screen quick_menu

    hide screen stra_neus_transpa
    scene black
    with fade

    stop music fadeout 3.0

    pause

    if pl.np < 50: # NOT FINISHED... number?

        pt "Quizás..."

        extend " si hubiera hecho las cosas distintas con [neusname]..."

        pt "Quizás..."

        pause

        jump gameover

    play sound "audio/sfx/heartbeat_01.ogg"

    ono "{size=10}BU-{w=0.25}{nw}"

    extend "BUM{/size}"

    pt "¿Uh...?"

    play sound "audio/sfx/heartbeat_01.ogg"

    ono "{size=20}BU-{w=0.25}{nw}"

    extend "BUM{/size}"

    pt "¿Estoy muerto...?"

    play sound "audio/sfx/heartbeat_01.ogg"

    ono "{size=30}BU-{w=0.25}{nw}"

    extend "BUM{/size}"

    play sound "audio/sfx/door_old_open01_otherroom.ogg"

    ono "{size=12}NEEEEEEC{/size}"

    if PlatinumHelp == True:
        show screen Points()
        show screen quick_menu()
        with fade

    n "Oyes el ruido lejano de una puerta chirriante abriéndose."

    pt "¿Qué...?"

    play sound "audio/sfx/step_bare01_otherroom.ogg"

    ono "{size=10}Tap{/size}"

    play sound "audio/sfx/step_bare02_otherroom.ogg"

    extend " {size=12}Tap{/size}"

    play sound "audio/sfx/step_bare03_otherroom.ogg"

    extend " {size=15}Tap{/size}"

    if music_play != "theDread":
        play music "audio/music/kevinmacleod/creepy/theDread.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "theDread"

    n "Rendido en el suelo,"

    n "sin apenas fuerzas ni para mantener los párpados separados,"

    n "oyes unas pisadas desnudas en el pasillo exterior que se acercan a la habitación."

    pt "¿Qué-"

    extend "qué está pasando?"

    ne "No..."

    n "Oyes la voz de [neusname], quebrada por un llanto y un dolor,"

    ne "Por favor..."

    n "distinto al que habías oído hasta ahora,"

    ne "no salgas..."

    n "como si se lamentara por otra persona."

    pt "¿De qué está...?"

    play sound "audio/sfx/step_bare04_otherroom.ogg"

    ono "{size=20}Tap{/size}"

    play sound "audio/sfx/step_bare05_otherroom.ogg"

    extend " {size=30}Tap{/size}"

    play sound "audio/sfx/step_bare06_otherroom.ogg"

    extend " {size=40}Tap{/size}"

    play sound "audio/sfx/step_bare07_otherroom.ogg"

    ono "{size=50}Tap{/size}"

    show night04_pedrera_baba01_background:
        subpixel True
        zoom 0.6
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4
    show morning04_bedroom_DMast_blinkeye

    show border_darkness:
        subpixel True
        truecenter
        zoom 0.5
        ease 50.0 zoom 0.7
    with fade

    n "Oyes esa última pisada,"

    n "justo en frente de la puerta que da paso a la habitación."

    pt "¡Al final será verdad que vive una anciana!"

    pt "¡Váyase buena mujer!"

    pt "¡Aquí corre peligro!"

    pt "Mierda,"

    extend " no puedo ni hablar..."

    scene night04_pedrera_baba01_background:
        subpixel True
        zoom 0.6
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_body:
        subpixel True
        zoom 0.4 xanchor 0.6
        # xanchor 0.0 yanchor 0.0
    show night04_pedrera_baba01_hand:
        subpixel True
        zoom 0.4 yanchor -1.0
        # xanchor 0.0 yanchor 0.0
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4 xanchor -0.1
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_fingers:
        subpixel True
        zoom 0.4 yanchor -1.0
        # xanchor 0.0 yanchor 0.0
    show morning04_bedroom_DMast_blinkeye #Not yet.

    show border_darkness:
        subpixel True
        truecenter
        zoom 0.6
        ease 50.0 zoom 0.8
    with fade

    play sound "audio/sfx/door_old_open02.ogg"

    n "Con un sonido estridente, ves como se abre ligeramente."

    show night04_pedrera_baba01_door:
        easein_quad 20.0 zoom 0.4 xanchor -0.5

    play sound "audio/sfx/door_old_open03.ogg"

    if music_play != "welcome_to_horror_land":
        play music "audio/music/kevinmacleod/welcome_to_horror_land.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "welcome_to_horror_land"

    pt "¿Qué demonios...?"

    show night04_pedrera_baba01_hand:
        easein_quad 30.0 xanchor 0.0 yanchor 0.0
    show night04_pedrera_baba01_fingers:
        easein_quad 30.0 xanchor 0.0 yanchor 0.0
    with dissolve

    n "La imagen de una mano pálida, decrépita y casi grotesca,"

    n "empieza a asomarse por el marco de la puerta."

    n "Sin movilidad alguna y forzando los párpados para intentar ver lo que ocurre,"

    n "empiezas a vislumbrar,"

    show night04_pedrera_baba01_body:
        easein_quad 30.0 xanchor 0.0 yanchor 0.0

    n "lo que podría describirse como el cuerpo de una mugrienta"

    n "y decrépita anciana, por su extrema avanzada edad,"

    n  "con la piel en los huesos, rugosa, pálida,"

    n "con el rostro y su repulsiva e inhumana lengua carente de mandíbula inferior,"

    n "oculta bajo su longeva y grasienta mata de pelo."

    window hide dissolve
    pause

    pt "¿Qué...?"

    pt "¡¿QUÉ COÑO ES ESO?!"

    scene black
    with fade

    dad "Al fin..."

    play sound "audio/sfx/fall02.ogg"

    scene night04_pedrera_baba02_background:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos 1.0
    show night04_pedrera_baba02 empty:
        subpixel True
        truecenter
    show ped_motherOnTxell happy_Talking:
        subpixel True
        truecenter
        zoom 1.0 xpos -0.6 ypos 0.0 # Her feet.
        ease 25.0 zoom 1.0 xpos 0.9 ypos 0.4 # Father 0.5
        #ease 50.0 zoom 0.5 xpos 0.6 ypos 0.5 # Final Image.

        #ease 10.0 zoom 1.0 xpos 0.9 ypos 0.6 # Centered zoom 1.0
        #zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.
        #zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    show morning04_bedroom_DMast_blinkeye
    show border_darkness:
        subpixel True
        truecenter
        zoom 0.8
        ease 50.0 zoom 1.0
    with hpunch

    n "Con una velocidad que tus cansados ojos son incapaces de seguir,"

    n "esa figura horripilante se lanza encima del cuerpo desnudo de Meritxell."

    dad "Mi primogénita,"

    dad "mi inolvidable amante,"

    dad "mi Reina."

    dad "Realmente te he echado de menos,"

    extend " querida."

    if MShooter_Present_Necklace_Ankh:

        mom "[protname]..."

        pt "¿Y esta voz...?"

    #else:

    show ped_motherOnTxell happy_Talking:
        ease 15.0 zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.

    n "Lentamente, esa extraña criatura, dirige su ausente mirada hacia ti,"

    show ped_motherOnTxell empty
    show night04_pedrera_baba02_background:
        truecenter
        zoom 1.0 xpos 0.5 ypos 1.0

    show night04_pedrera_baba02 05:
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5 # Far 0.4
        ease 25.0 zoom 0.7 xpos 0.5 ypos 0.5 # 0.6
    show border_darkness:
        truecenter
        zoom 0.5
        ease 50.0 zoom 1.0
    with fade

    n "A pesar del tupido y grasiento pelo que le cubre gran parte del rostro,"

    n "eres capaz de apreciar que tiene dos orificios en lugar de orejas,"

    n "que su mandíbula inferior es completamente ausente,"

    n "que le falta media nariz,"

    n "y que sus concavidades oculares están completamente vacías."

    if MShooter_Present_Necklace_Ankh:

        jump afternight05_Pedrera_MotherConverstaion

    else:

        n "A pesar de ello,"

        if music_play != "heartbreaking":
            play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 5.0 fadeout 5.0
            $ music_play = "heartbreaking"

        n "sus lagrimales desprenden un baño de lágrimas que recorren sus arrugadas y blanquecinas mejillas,"

        n "dejándote una extraña sensación en el estómago,"

        n "como si de algún modo esa criatura te resultara familiar,"

        n "y esas lágrimas fueran por ti."

        jump afternight05_Pedrera_MotherDisappear

            # n "Como si de arena se tratara,"
            # n "se deshace encima del cuerpo desnudo de Meritxell."
            # dad "¡COF-COF-COF!"

label afternight05_Pedrera_MotherConverstaion:

    $ dad = d_dad

    mom "Has crecido tanto..."

    pt "¿Es de esa criatura?"

    mom "Gracias al medallón que te dio tu hermana,"

    mom "puedes oírme."

    mom "Al menos,"

    extend " gracias a ello,"

    mom "podré despedirme."

    pt "¡¿Euh?!"

    pt "¿Se refiere al medallón de oro con la cruz egipcia?"

    if music_play != "heartbreaking":
        play music "audio/music/kevinmacleod/sad/heartbreaking.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "heartbreaking"

    mom "Por favor,"

    extend " perdona a tu hermana."

    p "..."

    mom "Si tienes que culpar a alguien,"

    extend " cúlpame a mi."

    pt "¿Por qué debería culparte a ti?"

    mom "Fui yo quien la convencí de sacrificar a ese niño."

    p "..."

    pt "¿Por qué...?"

    mom "Porque no había otro modo,"

    extend " y el tiempo se acababa."

    mom "Porque si vuelve con su Padre,"

    mom "hará cosas peores,"

    extend " mucho peores..."

    mom "a millares de otros niños."

    p "..."

    if pl.np > 100:

        mom "Porque sé que tienes un buen corazón."

    else:

        mom "Porque en el fondo sé que tienes buen corazón."

    mom "Porque se merece ser feliz."

    mom "Porque sé que puedes ser distinto a tu padre."

    mom "Porque eres la única esperanza que tiene de tener una vida."

    p "..."

    menu:

        pt "Puede escuchar mis pensamientos gracias al medallón..."

        "<Por mucho que fuera tu idea, fue ella quien eligió matar a ese niño.":
            call p_Help

            pt "Es una asesina."

            mom "¿Sabes porqué eligió intentar ser vegana?"

            p "..."

            mom "Para que no tuviera que hacerte responsable a ti,"

            mom "de las muertes que ella necesita para sobrevivir;"

            mom "aunque estas fueran de animales."

            p "..."

            mom "Pues alimentándose de ti,"

            extend " tendría suficiente;"

            mom "pero tú no."

            p "..."

        "...":
            call p_Help

    mom "Huir de ese infierno,"

    extend " ha sido siempre nuestro sueño,"

    mom "tener una vida tranquila,"

    extend " en paz,"

    extend " y amor."

    mom "Darle esa oportunidad,"

    mom "solo depende de ti,"

    extend " hijo."

    p "..."

    mom "Es directa,"

    extend " se enerva con facilidad,"

    extend " tiene un carácter fuerte,"

    mom "miente cuando cree que la verdad puede causar algún daño,"

    mom "pero cuando la conoces mejor,"

    mom "ves que en realidad es un trozo de pan,"

    mom "que solo quiere ser correspondida."

    mom "Por eso,"

    extend " cuando descubrí que había escapado,"

    mom "la dirigí entre sueños y susurros hasta Barcelona."

    mom "Por eso conseguí que llegara hasta la puerta de la Pedrera,"

    mom "le imploré que te diera la oportunidad de conocerte,"

    extend " de hablar contigo."

    mom "De ahí que la empujara a cometer el sacrificio de ese niño."

    mom "Porque era la única manera de evitar más muertes innecesarias en sus manos,"

    mom "porque no había otro modo de que pudierais ser felices."

    menu:

        "Sigue siendo una asesina.":
            call p_Help

            show ped_motherOnTxell happy_Talking:
                zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
            with dissolve

            dad "¡Claro que es una asesina!"

            dad "¡Pero peor es tu madre!"

            show ped_motherOnTxell pain
            with hpunch

            dad "¡Uurghh...!"

            show ped_motherOnTxell sad_Silent:
                ease 10.0 zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.
            with dissolve
            
            mom "Si hubieras sufrido lo que ella ha vivido,"

            extend " quizás opinarías de forma distinta."

            p "..."

            mom "No olvides,"

            extend " que existes gracias a los sacrificios que yo misma he tenido que hacer,"

            mom "para verte crecer."

            menu:

                "Nunca te pedí nada.":
                    call p_Help

                    mom "..."

                    mom "Una madre que ama a su hijo,"

                    mom "hará lo que esté en sus manos para protegerlo,"

                    mom "aún sabiendo que puede llegar el día,"

                    mom "que su hijo no llegue a perdonarla jamás."

                    p "..."

                    mom "Aún así,"

                    extend " habrá valido la pena,"

                    mom "porque has tenido la oportunidad de vivir y ser feliz."

                    p "..."

                "...":
                    call p_Help

        "...":
            call p_Help

    pt "¿Qué le estás haciendo...?"

    mom "No te preocupes por tu amiga,"

    mom "ella no sufrirá ningún daño."

    pt "¿Y tú?"

    mom "Yo volveré con Padre."

    mom "Ya nunca más volveremos a hablar,"

    mom "y si volvieras a verme;"

    mom "Huye."

    p "..."

    mom "No podré protegerte nunca más."

    p "..."

    pt "¿Intentarás matarme?"

    mom "Por desgracia soy muy buena en ello."

    p "..."

    show ped_motherOnTxell happy_Talking:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with dissolve

    dad "Desgracia para ti..."

    dad "Hahaha..."

    show ped_motherOnTxell pain:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with hpunch
    dad "¡Ugh!"

    show ped_motherOnTxell sad_Silent:
        ease 10.0 zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.
    with dissolve
    
    mom "Quise hacerte tantas fotos cuando apenas cabías entre mis brazos,"

    mom "inmortalizar el instante más feliz de mi vida."

    mom "Pero la existencia de esas fotos hubieran podido ponerte en peligro."

    mom "Quise mantenerte a mi lado,"

    mom "hacer de verdadera madre,"

    extend " educarte,"

    extend " cuidarte..."

    mom "Pero a medida que crecías,"

    mom "mi hambre aumentaba,"

    mom "y no..."

    extend " no podía cometer incesto con mi niño,"

    mom "no a esa edad tan temprana."

    mom "Ni siquiera cuando creciste me vi capaz."

    mom "Menos aún,"

    extend " cuando ya tenías a unos padres adoptivos que te amaban con locura,"

    mom "Si me hubiera acercado a ti,"

    extend " aunque fuera solo para darte un abrazo,"

    mom "te hubiera expuesto demasiado al peligro."

    show ped_motherOnTxell happy_Talking:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with dissolve

    dad "Pero enviar a tu hija,"

    dad "¡eso fue muy inteligente...!"

    show ped_motherOnTxell pain:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with hpunch
    dad "¡Ugh...!"

    show ped_motherOnTxell sad_Silent:
        ease 10.0 zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.
    with dissolve

    mom "Espero que te gustaran las galletas que te preparó Elur para cenar esta noche."

    if night05_Plaza_Food_Biscuit:

        menu:

            "La verdad es que eran muy ricas.":
                call p_Help

                $ afternight05_Pedrera_Food_Biscuit_MotherTold = True

                mom "Me alegra escuchar eso."

            "...":
                call p_Help
                pass

    else:

        "..."

    mom "Las hizo con la misma receta,"

    mom "que usaba para hacerte las papillas,"

    mom "cuando aún tenías los dientes de leche."

    mom "Aunque en lugar de usar lactosa de vaca,"

    mom "ella insistió en usar la de soja."

    if night05_Plaza_Food_Biscuit == False:

        menu:

            "Lo lamento, pero no llegué a probarlas.":
                call p_Help

                $ afternight05_Pedrera_MotherConverstaion_ToldHerNotTriedCookies = True

                mom "..."

                mom "Vaya..."

            "...":
                call p_Help

    if afternight05_Pedrera_MotherConverstaion_ToldHerNotTriedCookies:

        mom "Bueno,"

        extend " supongo que tampoco hubiera bastado solo con eso."

        mom "Eras demasiado pequeño para recordar nada de mi."

        mom "Pero al menos me quedaba la esperanza..."

    else:

        mom "Supongo que son recuerdos demasiado tempranos para que puedas recordar algo de mí,"

        if afternight05_Pedrera_Food_Biscuit_MotherTold:

            mom "pero al menos me alegra saber que siguen gustándote."

        else:

            mom "pero al menos quería que recordaras el sabor de la comida de tu madre,"

            mom "por última vez."

    p "..."

    mom "Soy feliz,"

    extend " porque sé que eres feliz."

    show ped_motherOnTxell happy_Talking:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with dissolve

    dad "¿Y era preferible lucir como una criatura monstruosa sin mandíbula inferior,"

    extend " orejas,"

    extend " ni ojos?"

    dad "¿Tanto te costaba pedirle un poco de semen de tanto en cuanto a tu querido hijo?"

    show ped_motherOnTxell pain:
        zoom 1.5 xpos 1.1 ypos 0.1 # Father face.
    with hpunch
    dad "¡Arghh!"

    show ped_motherOnTxell sad_Silent:
        ease 10.0 zoom 1.5 xpos 1.5 ypos 1.0 # Mother face.
    with dissolve

    p "..."

    show ped_motherOnTxell empty
    show night04_pedrera_baba02 05:
        truecenter
        zoom 0.7 xpos 0.5 ypos 0.5 # 0.6
        ease 25.0 zoom 0.55 xpos 0.5 ypos 0.5 # Far 0.4
    with fade

    mom "Haz que tu hermana pueda serlo también."

    mom "Es lo único que te pido."

    p "..."

    mom "Gracias por darme los momentos más felices de mi vida."

    show ped_motherOnTxell sad_Silent:
        ease 10.0 zoom 0.5 xpos 0.6 ypos 0.5 # Final Image.
    with fade

    pt "¡E-"

    extend " espera!"

    window hide dissolve
    pause

    jump afternight05_Pedrera_MotherDisappear