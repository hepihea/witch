#default aftermorning05_beachafter_Stay_FuckingDidac_Cond = False
default aftBeach_DidacSex = False # Stay at home to fuck Didac.
default aftermorning05_beachafter_Stay_GoTxellDate_Cond = False # if True: <Dejar solo a Dídac en casa e irte a la cita con Meritxell>
default aftermorning05_beachafter_Stay_HomeWithoutFuck_Cond = False
default aftermorning05_beachafter_Stay_GouOutWithoutFuck_Cond = False
default p_prot_location = ""

default aftermorning05_DC_pregnantConver_Cond = False # Didac tells you she is pregnant.

label aftermorning05_AfterDeepsea_PublicSex_No_Didac_Accept:

    ###aftermorning05_Deepsea_Orgasm_Cond == True and pl.dp > 90: # how many points?

    $ aftermorning05_AfterDeepsea_PublicSex_No_DidacAccept_Cond = True

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:

        show gensex_oral_d_frontHead_exp_eyes 06
        show gensex_oral_d_frontHead_exp_iris front06
        show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
        show gensex_oral_d_frontHead_exp_eyebrows angryx05
        with dissolve

    else:

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx05
        with dissolve

    d "Tssk..."

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:

        $ beach_sex_blow_expression_Cond = "talk"
        $ gensex_oral_d_mast_left = "rest"
        $ gensex_oral_d_mast_right = "rest"
        $ gensex_oral_others_front_left_Cond = "left02_a"
        if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Blowjob_Cond == True:
            $ gensex_oral_others_front_right_Cond = "right02_b"

        else:
            $ gensex_oral_others_front_right_Cond = "right01_a"

        show beach_sex_blow_comp Talkative_mastOthers

        show gensex_oral_d_frontHead_exp_eyes 04
        show gensex_oral_d_frontHead_exp_iris right04
        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
        show gensex_oral_d_frontHead_exp_eyebrows angryx04
        with Dissolve(0.5)

    else:

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx06
        with dissolve

    d "Lo que más me jode es que en el fondo tienes razón..."

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:

        show gensex_oral_d_frontHead_exp_eyes 05
        show gensex_oral_d_frontHead_exp_iris right05
        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx06
        show gensex_oral_d_frontHead_exp_eyebrows angryx03
        with dissolve

    else:

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve

    pt "Increíble..."

    pt "¿Está entrando en razón?"

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:

        show gensex_oral_d_frontHead_exp_eyes 03
        show gensex_oral_d_frontHead_exp_iris front03
        show gensex_oral_d_frontHead_exp_mouth sad_Talkingx08
        show gensex_oral_d_frontHead_exp_eyebrows angryx05
        with dissolve

    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx07
        with dissolve

    d "Pero no te creas que esto se va a quedar así..."

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:

        show gensex_oral_d_frontHead_exp_eyes 04
        show gensex_oral_d_frontHead_exp_iris front04
        show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
        show gensex_oral_d_frontHead_exp_eyebrows angryx03
        with dissolve

    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx02
        show didacf_mouth happybiting_Silentx03
        with dissolve

    p "..."

    scene beach_outsexy_bg_sky:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.3 ypos 0.3

    show beach_outsexy_bg_withbeach_ 12:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.3
        zoom 0.6

    if aftermorning05_AfterDeepsea_PublicSex_EncourageHim_NOT_Cond:
        with fade

        n "En poco tiempo, la mayoría de la gente del alrededor empieza a irse al ver que la acción ha desaparecido."
        
    else:
        with dissolve

    n "Observas como se vuelve a poner el bikini, junto con el pareo, y recoge sus cosas."

    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties bikini:
        dfbody_atright_closex2
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_below empty:
        dfbody_atright_closex2
    show didacfhandrb empty:
        dfbody_atright_closex2
    show didacfbodytop brabikini:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodycloth_top empty:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandr empty:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacf_blush 02:
        dfexpressions_atright_closex2
    show didacf_eyes 03:
        dfexpressions_atright_closex2
    show didacf_pupils front03:
        dfexpressions_atright_closex2
    show didacf_eyebrows angryx01:
        dfexpressions_atright_closex2
    show didacfbodycloth_whole pareo_bagtowel:
        dfbody_atright_closex2
    show didacfbodytop_hair wet_01:
        dfbody_atright_closex2
    show didacf_mouth sad_Talkingx04:
        dfexpressions_atright_closex2
    with dissolve

    d "Venga,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "larguémonos,"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "antes de que vengan más buitres."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx04
    with dissolve

    scene beach_02_erection:
        subpixel True
        truecenter
        zoom 0.8 xpos 0.5 ypos 0.2 # initial image
        ease 15.0 zoom 0.35 xpos 0.4 ypos 0.7 # Final IMage
    with fade

    n "Observas a tu alrededor, y efectivamente divisas algún que otro hombre de avanzada edad,"

    n "acariciándose la entrepierna de forma poco sutil."

    pt "Madre mía,"

    pt "como hubiera terminado esto..."

    window hide dissolve
    pause

    jump aftermorning05_AfterBeach_DidacHome

label aftermorning05_AfterBeach_DidacHome:

    progcheck "How you got home: [aftermorning05_howYouGetHome]"

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    $ saturation_tint_level = "verydark"

    scene afternight03_bg_entrance_lightoff
    with fade
    
    n "Dejas las llaves en el recibidor,"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "mientras observas a tu compañero/a de piso dirigirse sin vacilar,"

    n "hacia el pasillo que conduce al cuarto de baño."

    if aftermorning05_howYouGetHome in ["battleThem", "runningPolice"]:

        show didacfbodybelow naked:
            dfbody_atright_closex2
        show didacfbodybelow_panties bikini:
            dfbody_atright_closex2
        show didacfbodybelow_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodycloth_below empty:
            dfbody_atright_closex2
        show didacfhandrb empty:
            dfbody_atright_closex2
        show didacfbodytop brabikini:
            dfbody_atright_closex2
        show didacfbodytop_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodycloth_top empty:
            dfbody_atright_closex2
        show didacfhandl hip_naked:
            dfbody_atright_closex2
        show didacfhandr empty:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright_closex2
        show didacf_blush 02:
            dfexpressions_atright_closex2
        show didacf_eyes 05:
            dfexpressions_atright_closex2
        show didacf_pupils front05:
            dfexpressions_atright_closex2
        show didacf_eyebrows surprisex01:
            dfexpressions_atright_closex2
        show didacfbodycloth_whole pareo_bagtowel:
            dfbody_atright_closex2
        show didacfbodytop_hair:
            dfbody_atright_closex2
        show didacf_mouth sad_Talkingx003:
            dfexpressions_atright_closex2

    if aftermorning05_howYouGetHome == "runningPolice":

        $ df_eye = "front04"
        show didacf_mouth happy_Talkingx02
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "Aún no sé cómo te lo has hecho"

        $ df_eye = "front03"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "para saber que ahí en el fondo habían esos coches patrulla..."

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "¡¿Eres consciente de que hemos salido de esta por los pelos?!"

        $ df_eye = "right02"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front04"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "Pero no me negarás que ha sido algo excitante..."

    if aftermorning05_howYouGetHome in ["battleThem", "runningPolice"]:

        $ df_eye = "front00"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex02
        call dfeye_lab
        with dissolve

        p "¡Dídac!"

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx01
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¡¿Tendré que atarte para que no vuelvas a salir de casa?!"

        $ df_eye = "left03"
        show didacf_mouth sad_Talkingx001
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "No..."

        $ df_eye = "left05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx02
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "Te prometo que no saldré más."

        $ df_eye = "right05"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        pause 0.2

        scene afternight03_bg_entrance_lightoff
        show afternight03_bg_entrance_keysmc lightoff_night:
            afternight03_bg_entrance_keys
        with Dissolve(0.5)

        n "Sin decir otra palabra desaparece de tu vista en dirección al pasillo."

        pt "Parece arrepentido,"

        pt "¿o quizás es lo que prefiero pensar?"

    else:

        pt "Es posible que no esté de muy buen humor."

        pt "Es como un niño al que si no le satisfaces sus caprichos,"

        pt "le coge un berrinche..."

    if music_play != "relent":
        play music "audio/music/kevinmacleod/sad/relent.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "relent"

    scene beds_midday_lightOff_blindUp_DemptyMCempty
    with fade

    $ saturation_tint_level = "default"

    n "Pasados unos minutos decides dejar la toalla en la habitación"

    n "mientras oyes a Dídac en la ducha."

    scene morning04_bg_kitch_toastwithjam
    with fade

    n "Te diriges a la cocina a ver si tienes algo para llevarte a la boca."

    pt "Desde luego,"

    pt "tendríamos que pasar por el supermercado,"

    pt "parece que esté comiendo todo el día lo mismo..."

    scene morning04_bg_livingroom_others_morning
    with fade

    if morning03_Meritxell_Phonenumber_Accepted == True:

        p "..."

        pt "{i}\"Dime,\"{/i}"

        pt "{i}\"¿Haces algo mañana por el mediodía?\"{/i}"

        # meritxell name
        
        pt "¡La chica rubia de clase!"
        
        pt "Es cierto..."

        extend " Me dijo..."
        
        pt "{i}\"Si te apetece hacer algo,\"{/i}"

        pt "{i}\"llámame\"{/i}."
        
        pt "Tengo su número apuntado en el móvil..."

        show morning04_bg_livingroom_mc_resting_phone 01:
            xpos 0.485 ypos 0.125
        show morning04_livingroom_mc_resting_handphone
        with dissolve
        
        n "Sacas el móvil del bolsillo y escribes en el buscador de nombres \"Rubia Tetuda\"."
        
        n "No se te ocurrió un nombre más original para denominar a esa despampanante mujer."

    play sound "audio/sfx/door_open02.ogg"

    n "A lo lejos oyes la puerta del baño abriéndose."

    if music_play != "deadly_roulette":
        play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 2.0 fadeout 2.0
        $ music_play = "deadly_roulette"

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone
    
    show didacfbodybelow_naked_drops 00:
        dfbody_atright
    show didacfhandr leg_naked:
        dfbody_atright
    show didacfbodytop park:
        dfbody_atright
    show didacfhandl hip_naked:
        dfbody_atright
    show didacf_blush 03:
        dfexpressions_atright
    show didacf_eyes 05:
        dfexpressions_atright
    show didacf_pupils front05:
        dfexpressions_atright
    show didacf_eyebrows angryx01:
        dfexpressions_atright
    show didacfbodytop_hair wet_01:
        dfbody_atright
    show didacf_mouth happybiting_Silentx03:
        dfexpressions_atright
    show morning04_bg_livingroom_mc_resting_phone 01:
            xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with dissolve

    p "¿Hmmm?"

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone
    with dissolve

    window hide dissolve
    pause

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Talkingx05
    with dissolve

    d "¿Y bien...?"

    # if ("battleThem" not in aftermorning05_howYouGetHome or
    #     "runningPolice" not in aftermorning05_howYouGetHome)
    if aftermorning05_howYouGetHome not in ["battleThem", "runningPolice"]:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx01
        show didacf_mouth happy_Talkingx06
        with dissolve

        d "¿Qué tal si continuamos lo que hemos dejado a medias en la playa?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Silentx05
    with dissolve

    p "¿Y esto que llevas?"

    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfbodytop park:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair wet_01:
        dfbody_atright_closex2
    show didacf_mouth sad_Talkingx003:
        dfexpressions_atright_closex2
    with Dissolve(1.0)

    d "¿No te gusta...?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth happy_Silentx05
    with dissolve

    pt "Puto Dídac..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx01
    show didacf_mouth happybiting_Silentx05
    with dissolve

    #########################################################
    
    if config.version < "00.99.99": # for FUTURE.
        
        call endupdatescript
    
#######################################################
    
    stop music fadeout 3.0

    if morning03_Meritxell_Phonenumber_Accepted == True:
        # afternoon04_MACBA_TxellName_Know # NOT NEEDED, you already know her name here.

        pt "Si no voy ahora mismo a la cita con Meritxell,"

        pt "ya será demasiado tarde."

    $ aftermorning05_beachafter_Stay_list = []

    menu aftermorning05_beachafter_Stay_question:
            
        pt "Si me quedo en casa, va a ser un peligro..."

        "¡¿Después de lo que ha pasado aún tienes ganas de hacer el imbécil?!" if (aftermorning05_howYouGetHome == "runningPolice") and ("runningPolice" not in aftermorning05_beachafter_Stay_list):
            call p_Help
            $pl.ch_pts("dp",-1)

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx002
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "Pero al final hemos logrado escapar."

            $ df_eye = "front04"
            show didacf_mouth sadbiting_Silentx04
            show didacf_eyebrows sadx04
            call dfeye_lab
            with dissolve

            p "¡Por puro milagro!"

            $ df_eye = "right05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows sadx03
            call dfeye_lab
            with dissolve

            d "..."

            $ aftermorning05_beachafter_Stay_list.append("runningPolice")

            jump aftermorning05_beachafter_Stay_question

        "¡¿Estás de broma?! ¡¿Después de que me hayan dado una paliza por tu culpa?!" if (aftermorning05_howYouGetHome == "battleThem") and ("battleThem" not in aftermorning05_beachafter_Stay_list):
            call p_Help
            #$pl.ch_pts("dp",-3)

            $ df_eye = "front01"
            show didacf_mouth sadbiting_Silentx02
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "right02"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "Lo-"

            extend "lo lamento."

            $ df_eye = "left01"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "No pensé que legarían tan lejos..."

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            p "¿¡Y qué coño esperabas?!"

            $ df_eye = "front05"
            show didacf_mouth sadbiting_Silentx04
            show didacf_eyebrows sadx03
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "right04"
            show didacf_mouth sad_Talkingx02
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "Solo quería ponerte un poco celoso."

            $ df_eye = "right05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            pt "La madre que lo parió...."

            $ aftermorning05_beachafter_Stay_list.append("battleThem")

            jump aftermorning05_beachafter_Stay_question
            
        "<Quedarte en casa y follarte a Dídac durante toda la tarde>":
            call p_Help
            $pl.ch_pts("dp",3)

            #$ aftermorning05_beachafter_Stay_FuckingDidac_Cond = True
            $ aftBeach_DidacSex = True
                    
            jump aftermorning05_beachafter_Stay_SexYes

        "<Dejar solo a Dídac en casa e irte a la segunda cita con Meritxell>" if afternoon04_MACBA_TxellTruth_Cond == True:

            call p_Help
            $pl.ch_pts("dp",-2)

            $ aftermorning05_beachafter_Stay_GoTxellDate_Cond = True

            jump aftermorning05_beachafter_Stay_GoTxellDate_label
                    
        "<Quedarte en casa, pero decirle a Dídac que es mejor que no hagáis nada>":

            call p_Help
            $pl.ch_pts("dp",-8)

            $ aftermorning05_beachafter_Stay_HomeWithoutFuck_Cond = True

            jump aftermorning05_beachafter_Stay_SexNo


        "<Salir de casa para evitar a Dídac y dar vueltas por la ciudad hasta la cita con Neus>":

            call p_Help
            $pl.ch_pts("dp",-3)

            $ aftermorning05_beachafter_Stay_GouOutWithoutFuck_Cond = True

            jump aftermorning05_beachafter_Stay_SexNo

label aftermorning05_beachafter_Stay_GoTxellDate_label:

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Dídac..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¡¿Qué pasa?!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡Has sido tú quien ha dicho que era mejor no hacerlo en un espacio público!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡Bien!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "¡Estamos en casa!"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡Esto no es un espacio público!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡¿Verdad?!"

    if aftermorning05_howYouGetHome in ["battleThem", "runningPolice"]:

        # NO_ILLUSTRATIONS

        p "Después de lo que ha pasado en la playa,"

        p "¡¿aún tienes los santos cojones de decirme esto?!"

        d "..."

    else:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx06
        with dissolve

        p "No se trata de eso..."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with dissolve

        d "¡¿ENTONCES?!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Aún quieres recuperar tu anterior cuerpo,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "¿No es así?"

    if DidacMCPregnant == True:

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx03
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx04
        show didacf_mouth sadbiting_Silentx05
        with dissolve

        d "Tssk..."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx003
        with dissolve

        d "Es posible..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        pt "¡¿Es posible?!"

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx03
        with dissolve

    else:

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "¡Pues claro!"

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "¡Pero no te estoy diciendo que me dejes preñada!"

        show didacf_eyes 02
        show didacf_pupils right02
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "¡Hay condones de sobra!"

        show didacf_eyes 02
        show didacf_pupils right02
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx02
        with dissolve

        p "No se trata de eso..."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx01
        with dissolve

    p "Estoy siguiendo la pista de alguien que puede ayudarme a resolver el problema,"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    p "pero sino salgo ahora mismo por esa puerta,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "llegaré demasiado tarde."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx01
    show didacf_mouth sadbiting_Silentx03
    with dissolve

    p "¿Es eso lo que quieres?"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    d "..."

    if DidacMCPregnant == True:

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "Preferiría que te quedaras..."

        show didacf_eyes 02
        show didacf_pupils left02
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx04
        with dissolve

        d "Es más..."

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "no tienes tampoco por que ir esta noche a la cita con la bruja que mencionaste."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx03
        with dissolve

        pt "¿La llamé bruja?"

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve

        p "¡¿Qué?!"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx03
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        p "¡¿Es que te has bebido el entendimiento?!"

        show didacf_eyes 06
        show didacf_pupils front06
        show didacf_eyebrows sadx04
        show didacf_mouth sadbiting_Silentx06
        with dissolve

        p "¡¿Acaso no ves que estás perdiendo la cabeza?!"

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        d "..."

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx004
        with dissolve

        d "¿De verdad sería tan terrible que me quedará así por siempre?"

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        p "..."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx02
        with dissolve

        p "No me importaría que te quedaras así por siempre,"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx01
        with dissolve

        p "si hubiera sido tu elección convertirte en lo que eres,"

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx02
        with dissolve

        p "sabiendo las repercusiones que eso aparentemente conlleva,"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        p "pero me niego a aceptar que te quedes así de por vida,"

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows suspiciousx01
        show didacf_mouth sad_Silentx02
        with dissolve

        p "¡del modo que sucedió!"

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows suspiciousx02
        show didacf_mouth sad_Silentx04
        with dissolve

        p "¡¿Ha quedado claro?!"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows serious
        show didacf_mouth sadbiting_Silentx03
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx01
        show didacf_mouth sadbiting_Silentx04
        with dissolve

    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx004
        with dissolve

        d "Me suena un poco a excusa..."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows serious
        show didacf_mouth sadbiting_Silentx02
        with dissolve

        p "Lo tuyo sí que suena a excusa..."

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows normal
        show didacf_mouth sadbiting_Silentx01
        with dissolve

        p "Que vas más perdido que un pedo en un jacuzzi."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx05
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx02
        show didacf_mouth sadbiting_Silentx04
        with dissolve

    d "Tsskk..."

    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "Haz lo que quieras..."

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve

    scene morning04_bg_livingroom_others_morning
    with dissolve

    n "De mala gana se retira de tu presencia, perdiéndose por el pasillo,"

    with hpunch

    n "para luego oír un portazo, aparentemente de vuestra habitación."

    p "..."

    p "Puto Dídac..."
            
    jump morning05_AfterDidac_02
            #pt "La cita con Txell fue rara de narices..."
            #if TxellSlave >= 1:
                #pt "Aunque confieso que la idea de someterme a alguien con su experiencia y su figura,"
                #if TxellSlave >= 1:
                    #pt "no es una idea que me desagrade demasiado..."
                #elif TxellSlave >= 3:
                    #pt "es algo en lo que mi mente está fantaseando... "
                    #pt "¿De verdad soy alguien tan sumiso?!"
                    #pt "¡¿O es que alguien está tomando decisiones por mí?!"


label aftermorning05_beachafter_Stay_SexNo:

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx03
    with dissolve

    p "Lo lamento Dídac."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sadbiting_Silentx01
    with dissolve

    p "Pero no pienso hacer nada contigo."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¿Qué?"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "En unas horas,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "voy a quedar con la persona que te transformó en lo que eres ahora,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve

    p "y según lo que me contó,"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    p "finalmente regresarás a tu cuerpo original."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Es absurdo que hagamos nada más hasta entonces."

    if DidacMCPregnant == True:

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx05
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx03
        show didacf_mouth sadbiting_Silentx06
        with dissolve

    else:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows suspiciousx01
        show didacf_mouth sad_Silentx03
        with dissolve

    if aftermorning05_howYouGetHome in ["battleThem", "runningPolice"]:

        pause 0.2

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows suspiciousx02
        show didacf_mouth sad_Silentx05
        with dissolve

        p "A pesar de lo estúpido que has sido en la playa."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx04
        with dissolve

    p "Sé que no eres un animal,"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    p "y serás capaz de controlarte."

    if aftermorning05_beachafter_Stay_HomeWithoutFuck_Cond == True: # Stay Vigilant

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx02
        with dissolve

        p "Pero lo mejor será que me quede en casa hasta entonces,"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx04
        with dissolve

        p "para vigilar que no te coja una vena extraña y te vayas por ahí."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx06
        with dissolve

    elif aftermorning05_beachafter_Stay_GouOutWithoutFuck_Cond == True: # Leave Didac at Home

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx03
        with dissolve

        p "Por eso creo que lo más sensato será que me vaya a dar un paseo para no tenerte cerca."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows suspiciousx01
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "¿Para no tenerme cerca?"

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx01
        show didacf_mouth happy_Talkingx05
        with dissolve

        d "¿Tan poca fe tienes en tu impulso primario?"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows normal
        show didacf_mouth sad_Silentx03
        with dissolve

        p "En mí confío,"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Silentx04
        with dissolve

        p "es de ti que no me fío..."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx05
        with dissolve

        p "a saber que me harás si me quedo."

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx06
        with dissolve

        d "..."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx09
        with dissolve

    d "¡¿De qué coño vas?!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    p "¡¡¿De qué coño vas tú?!!"

    if aftermorning05_howYouGetHome == "battleThem":

        # NO_ILLUSTRATIONS

        p "¡Joder!"

        p "¡Me han dado una jodida paliza por tu culpa!"

    elif aftermorning05_howYouGetHome == "runningPolice":

        p "¡Hemos tenido que escapar de los jodidos {a=https://es.wikipedia.org/wiki/Mozos_de_Escuadra}mossos d'escuadra{/a}!"

        p "¡Y HEMOS SALIDO POR LOS PELOS!"

        p "¡¿Qué coño te pasa por la cabeza?!"

    elif aftermorning05_BallWakeUp_GoToSea_Cond == True:

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx01
        with dissolve

        p "¡¿Acaso no has visto que querías hacerlo sin miedo ni vergüenza"

        p "cuando se acercaba un menor?!"

    else:

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx01
        with dissolve

        p "¡¿Acaso no has visto lo que has querido hacer en la playa en medio de toda esa gente?!"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx03
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    p "¡Se te está yendo de las manos y ni siquiera te importa una mierda!"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx05
    with dissolve

    p "¡Ya basta de esta broma!"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx06
    with dissolve

    p "¡Mañana será otro día!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "¡Solo tienes que esperar un poco más!"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx02
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "Eso para ti es fácil decirlo,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows serious
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "cuando no entiendes lo que me pasa."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    p "..."

    if DidacMCPregnant == True:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "No te estoy pidiendo que me dejes preñada..."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "Y si al final lo estuviera,"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows sadx02
        show didacf_mouth sad_Talkingx004
        with dissolve

        d "tampoco te pediría responsabilidades..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx03
        show didacf_mouth sadbiting_Silentx04
        with dissolve

        p "¡¿Qué?!"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Talkingx004
        with dissolve

    else:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "¡No te estoy pidiendo que me dejes preñada!"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx06
        with dissolve

    d "¡Solo que me ayudes a pasar mejor estas últimas horas!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "¡Tampoco te estoy pidiendo amor eterno!"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡Joder!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡No me seas pusilánime de mierda!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Mastúrbate todo lo que quieras,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "pero usar la polla es demasiado arriesgado."

    if afternight04_Pussy_dick_deep_Speed_1_Success > 0:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with dissolve

        d "¡Ayer me follaste hasta el fondo!"

    elif afternight04_Anal_dick_med_Speed_1_Success > 0 and afternight04_Pussy_dick_med_Speed_1_Success > 0:

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx08
        with dissolve

        d "¡Ayer me follaste por todas partes!"

    elif afternight04_Pussy_dick_med_Speed_1_Success > 0:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "¡Ayer bien que me follaste!"

    if morning05_missionary_cond_03 == True:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx08
        with dissolve

        d "Esta mañana te me has montado encima."

    if aftermorning05_AfterDeepsea_Blowjob_Cond == True:

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "Me has metido la polla por el gaznate bajo el agua."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡¿Y ahora me vienes con estas gilipolleces?!"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve

    p "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Corregir a tiempo es de sabios."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡Tú lo que eres es un imbécil!"

    if aftermorning05_howYouGetHome == "battleThem":

        # NO_ILLUSTRATIONS

        p "¡Por tu culpa casi me rompen las costillas!"

        d "..."

        p "Debería haberte dejado ahí con ellos."

        d "No digas eso..."

    elif aftermorning05_howYouGetHome == "runningPolice":

        p "¡Por tu culpa tendré que ir con cuidado al salir a la calle!"

        p "¡A saber si aún nos estará buscando la policía!"

        d "..."

    elif aftermorning05_DidacFar_Voyeur_01_aBeginning_Cond == True:

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx04
        with dissolve

        p "¡¿Qué se supone que ibas a hacer con esos desconocidos?!"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx03
        with dissolve

        p "¡¿Euh?!"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx05
        with dissolve

        p "¡Ibas a follártelos sin condón en medio de una playa abarrotada de gente?!"

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows sadx01
        show didacf_mouth sad_Silentx06
        with dissolve

        p "¡¿Esa es tu idea de mentalidad cuerda?!"

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows sadx02
        show didacf_mouth sadbiting_Silentx05
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows sadx01
        show didacf_mouth sadbiting_Silentx04
        with dissolve

    else:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx05
        with dissolve

    p "No hagas que te lo repita."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx05
    with dissolve

    d "..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "No eres mi padre."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx01
    with dissolve

    p "Ni tampoco soy tu {b}daddy{/b}."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx06
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx04
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    d "Tsskk..."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡Que te follen!"

    scene morning04_bg_livingroom_others_morning
    with dissolve

    n "Rápidamente se da la vuelta para dirigirse a su habitación,"

    with hpunch

    n "dando un portazo considerable."

    p "..."

    if aftermorning05_beachafter_Stay_HomeWithoutFuck_Cond == True: # Stay Vigilant

        pt "Por lo menos espero que no salte por la ventana..."

        scene morning04_livingroom_mc_resting_bg feet01
        with fade

        n "Pasas la tarde en el sofá revisando el móvil,"

        n "jugando a videojuegos absurdos sin contenido ni gracia,"

        n "pero que consiguen matar el tiempo mientras oyes de fondo gemidos,"

        extend " lamentos,"

        extend " y gritos,"

        n "por parte de tu compañero de piso,"

        n "a medida que percibes cómo intenta futilmente lograr un orgasmo,"

        n "en la intimidad de vuestra habitación,"

        n "mediante métodos que prefieres no visualizar en demasiado detalle en tu mente."

        scene morning04_bg_livingroom_room_morning_lingerie_others:
            truecenter
            zoom 1.0
        with fade

        n "Te sorprende lo obediente que es al no salir de ahí,"

        n "e intentar escapar para irse a la calle en busca de alguna víctima."

        pt "Aunque me va a tocar a mí limpiar todo esto."

        pt "Tan jetas como siempre..."

        show morning04_bg_livingroom_others_night_lightOn:
            truecenter
            zoom 1.0
        with Dissolve (1.5)

        pt "Las horas han pasado realmente lentas..."

        pt "pero ya va siendo hora de prepararse para la última cita con Neus."

    elif aftermorning05_beachafter_Stay_GouOutWithoutFuck_Cond == True: # Leave Didac at Home

        jump aftermorning05_beachafter_Stay_SexNo_Leaving

label aftermorning05_beachafter_Stay_SexNo_Leaving:

        scene afternight03_bg_entrance_lighton
        show afternight03_bg_entrance_keysmc lighton:
            afternight03_bg_entrance_keys
        show afternight03_bg_entrance_keysd lighton:
            afternight03_bg_entrance_keys
        with fade

        pause 0.2

        hide afternight03_bg_entrance_keysmc
        with dissolve

        n "Recoges las llaves, tus cosas y sales por la puerta."

        scene bg an04_flat_outside
        with fade

        pt "Espero que no se largue de casa cuando vea que me he ido."

        scene aftermorning04_bg_gothicquarter_01
        with fade

        show aftermorning04_bg gothicquarter_02:
            subpixel True
            alpha 0.0
            ease 7.0 alpha 1.0

        n "Deambulas por las calles del Barrio Gótico de Barcelona durante varias horas"

        n "saltando de tienda en tienda para ir matando el tiempo."

        n "Hasta que el sol empieza a acariciar el horizonte."

        window hide dissolve
        pause

        pt "Ya es la hora."

        jump night05_NeusLastDate
                    
label aftermorning05_beachafter_Stay_SexYes:

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Como quieras."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿En serio...?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Sí."

    if ("battleThem" in aftermorning05_beachafter_Stay_list or 
        "runningPolice" in aftermorning05_beachafter_Stay_list):

        $ df_eye = "front02"
        show didacf_mouth happy_Talkingx02
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "Y yo que pensaba que estabas enfadado conmigo"

        $ df_eye = "right01"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        if "battleThem" in aftermorning05_beachafter_Stay_list:

            d "por lo de la paliza..."

        elif "runningPolice" in aftermorning05_beachafter_Stay_list:

            d "por lo de la policía..."

        $ df_eye = "down05"
        show didacf_mouth happybiting_Silentx05
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        p "..."

    show didacfbodybelow_naked_drops 00:
        dfbody_center_superclose
    show didacfhandr leg_naked:
        dfbody_center_superclose
    show didacfbodytop park:
        dfbody_center_superclose
    show didacfhandl hip_naked:
        dfbody_center_superclose
    show didacf_blush 03:
        dexpressions_center_superclose
    show didacf_eyes 04:
        dexpressions_center_superclose
    show didacf_pupils front04:
        dexpressions_center_superclose
    show didacf_eyebrows angryx01:
        dexpressions_center_superclose
    show didacfbodytop_hair wet_01:
        dfbody_center_superclose
    show didacf_mouth happybiting_Silentx02:
        dexpressions_center_superclose
    with Dissolve(1.0)

    n "Se te acerca aún más."

    if afternight04__MMouth_Tongue_Deep_Success > 0:

        $ df_eye = "front05"
        show didacf_mouth happybiting_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        n "Agarrándote por las mejillas"

        scene bg ped_04
        show kiss_ f_d_11:
            truecenter
            xzoom -1.0
        with fade

        n "te arranca un apasionado beso con lengua."

        show kiss_ f_d_12
        with Dissolve(0.5)

        n "Te desliza una mano por detrás del cuello"

        show kiss_ f_d_10
        with Dissolve(0.5)

        n "mientras desciende la otra hasta tu pecho"

        show kiss_ f_d_02
        with Dissolve(0.5)

        n "sin abandonar por un instante el calor de tu boca."

        show kiss_ f_d_03
        with Dissolve(0.5)

        p "..."

        scene morning04_bg_livingroom_others_morning

        show didacfbodybelow_naked_drops 00:
            dfbody_center_superclose
        show didacfhandr leg_naked:
            dfbody_center_superclose
        show didacfbodytop park:
            dfbody_center_superclose
        show didacfhandl hip_naked:
            dfbody_center_superclose
        show didacf_blush 03:
            dexpressions_center_superclose
        show didacf_eyes 05:
            dexpressions_center_superclose
        show didacf_pupils front05:
            dexpressions_center_superclose
        show didacf_eyebrows sadx01:
            dexpressions_center_superclose
        show didacfbodytop_hair wet_01:
            dfbody_center_superclose
        show didacf_mouth happybiting_Silentx04:
            dexpressions_center_superclose
        with fade

        n "Finalmente se aparta mirándote con apetito y deseo."

        $ df_eye = "front01"
        show didacf_mouth sadbiting_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "Pensaba que no te gustaba hacer estas \"mariconadas\"."

        $ df_eye = "right03"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Hmmm..."

        $ df_eye = "right02"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "Sé lo cachondo que te pone..."

        $ df_eye = "front01"
        show didacf_mouth sadbiting_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "Lo dices como si a ti no."

        $ df_eye = "left04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "Tssk..."

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "Lo que tú digas."

    else:

        $ df_eye = "front04"
        show didacf_mouth happybiting_Silentx05
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        n "Te agarra por la barbilla y con un rostro serio como pocas veces le has visto."

        $ df_eye = "front05"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "Ni se te ocurra cambiar de idea."

    scene morning04_bg_livingroom_others_morning

    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfbodytop park:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair wet_01:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx05:
        dfexpressions_atright_closex2
    with Dissolve(1.0)

    n "Se aleja de forma sugerente"

    scene morning04_bg_livingroom_others_morning
    with dissolve

    n "dirigiéndose al pasillo que conduce a vuestro cuarto."

    p "¿Hmm...?"

    d "¿A qué estás esperando?"

    p "¿Puedo saber a dónde vas?"

    d "Coño,"

    d "pues a la cama."

    d "Es mucho más cómodo que hacerlo en el sofá."

    p "..."

    scene afternight03_bg_hallway_day
    with fade

    n "Sigues sus pasos hasta vuestra habitación."

    scene beds_midday_lightOff_blindUp_DemptyMCempty
    with fade

    n "Al entrar encuentras el lugar vacío."

    p "¿Dónde...?"

    scene black
    with hpunch

    n "Te empuja con ímpetu desde atrás"

    n "lanzándote encima de tu alcoba"

    show morning04_bg bedroom_neus_a
    show morning04_bedroom_Didac_body_ass 02c: 
        truecenter
    show morning04_bedroom_Didac_body_body 02c
    #show morning04_bedroom_Neus_Prove
    show morning04_bedroom_Didac_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_mouth happy_Silentx03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows serious:
        morning04_bedroom_exp_position
    # show morning04_bedroom_Didac_exp_glasses:
    #     morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c

    # show light 01:
    #     light01_topside_position

    with fade

    n "para luego ponerse encima de ti a cuatro patas."

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx02
    with dissolve

    d "Espero que aguantes más que ayer,"

    if afternight04_didac_orgasms == 0:

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
        show morning04_bedroom_Didac_exp_eyebrows angryx03
        with dissolve

        d "¡Por que ayer no me diste ni un mísero orgasmo!"

        show morning04_bedroom_Didac_exp_mouth sad_Silentx06
        show morning04_bedroom_Didac_exp_eyebrows angryx04
        with dissolve

    elif afternight04_didac_orgasms == 1:

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        d "¡Por que ayer me diste solo un maldito orgasmo!"

        show morning04_bedroom_Didac_exp_mouth sad_Silentx05
        show morning04_bedroom_Didac_exp_eyebrows angryx03
        with dissolve

    elif afternight04_didac_orgasms == 2:

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "Por que ayer solo me diste dos orgasmos de mierda."

        show morning04_bedroom_Didac_exp_mouth sad_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

    else:

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "por que realmente estoy muy,"

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows sadx01
        with dissolve

        d "pero que muy cachonda."

    # if mc_body.orgasm >=3:

    #     pt "Tres corridas suele ser mi máximo..."

    if afternight04_didac_orgasms == 3:

        show morning04_bedroom_Didac_exp_mouth sad_Silentx01
        show morning04_bedroom_Didac_exp_eyebrows surprisex01
        with dissolve

        p "Pero ayer te corriste tres veces, no?"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
        show morning04_bedroom_Didac_exp_eyebrows angryx03
        with dissolve

        d "¡¿Y eso te parece mucho?!"

        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

    elif afternight04_didac_orgasms == 4:

        show morning04_bedroom_Didac_exp_mouth sad_Silentx03
        show morning04_bedroom_Didac_exp_eyebrows surprisex02
        with dissolve

        p "Pero ayer te llegaste a correr cuatro veces, no?"

        show morning04_bedroom_Didac_exp_mouth sad_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        d "..."

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "¿Y se supone que me tengo conformar con eso?"

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

    elif afternight04_didac_orgasms > 5:

        show morning04_bedroom_Didac_exp_mouth sad_Silentx03
        show morning04_bedroom_Didac_exp_eyebrows normal
        with dissolve

        p "Si mal no recuerdo,"

        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows surprisex02
        with dissolve

        p "ayer te di más de [afternight04_didac_orgasms] orgasmos,"

        extend " al menos."

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
        show morning04_bedroom_Didac_exp_eyebrows sadx01
        with dissolve

        d "Pues a ver si hoy consigues darme alguno más."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx05
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

    pt "Aunque sea una mujer,"

    if afternight04_didac_orgasms < 4:

        pt "sigue siendo igual de exigente que siempre..."

    else:

        pt "sigue siendo el mismo idiota de siempre..."

    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    n "Va desabrochando uno a uno los botones de tu camisa."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "¿Por qué coño me pones tan cachonda?"

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx03
    show morning04_bedroom_Didac_exp_eyebrows sadx01

    show morning04_bedroom_Didac_body_ass 02c: 
        morning04_bedroom_Neus_bodyass_anim01

    with dissolve

    n "Sientes su entrepierna frotándose contra tu paquete."

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows serious
    with dissolve

    d "Parece que ya la tienes bastante dura."

    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx05
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    pause 0.2
    with dissolve

    scene day05
    with fade

    p "..."

    n "Al llegar al último,"

    n "centra sus dedos en el botón de tu pantalón,"

    n "y luego:"

    ono "ziiip"

    $ pdaytime = "05_afterMorning"
    $ p_bg = "bed_mcRoom"

    $ p_prot = Pedrera_Body()
    $ p_didac = Pedrera_Girl()
    $ p_neus = Pedrera_Girl() # Necessary to work
    $ p_txell = Pedrera_Girl() # Necessary to work

    $ p_prot.id = "p_prot"
    $ p_didac.id = "p_didac"

    $ p_active = "p_didac"
    $ p_activen = "didac" # didac, txell, neus
    $ p_activeno = "_d" # _d, _m, _n

    $ p_girl_active = p_didac # I need a default here.

    $ p_deyespCond = False # Is it has to be changed?

    $ p_deyesp = deyesp
    #$ p_prot.posit = ""

    $ ped_sex_general_expression_Cond = "talk"
    $ p_prot.pos = "oral"
    $ ped_sex_general_zoom_Cond = "talk_close"

    scene pedrera_sex_didac_oral blowjob_general:
        truecenter
        zoom 0.8 xpos 0.6 ypos 1.1

    call pedrera_sex_p_general_talk

    $ df_blush = 4

    $ df_eye = "down03"
    show gensex_oral_d_frontHead_exp_mouth happybiting_Silentx03
    show gensex_oral_d_frontHead_exp_eyebrows sadx02
    call gensex_oral_c_frontHead_exp_label
    with fade

    d "Hmmm..."

    $ df_eye = "down04"
    show gensex_oral_d_frontHead_exp_mouth happybiting_Silentx05
    show gensex_oral_d_frontHead_exp_eyebrows sadx02
    call gensex_oral_c_frontHead_exp_label
    with dissolve

    n "Muerde sus labios mientras observa con hambre"

    $ df_eye = "down05"
    show gensex_oral_d_frontHead_exp_mouth happybiting_Silentx06
    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
    call gensex_oral_c_frontHead_exp_label
    with dissolve

    n "tu polla alzándose en el aire."

    menu:

        pt "Parece que la mira con ganas..."

        "¿Por qué no le das un poco de cariño con tu lengua?":
            call p_Help

            $ df_eye = "front01"
            show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows normal
            call gensex_oral_c_frontHead_exp_label
            with dissolve

            pause 0.2

            if afternight04_CumInMouth > 0 or afternight04_CumInThroat > 0:
                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                if afternight04_CumInThroat > 0:

                    d "¿Para que te corras de nuevo en mi garganta?"

                else:

                    d "¿Para que te corras de nuevo en mi boca?"

                $ df_eye = "front05"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx003
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "No,"

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "gracias..."

                $ df_eye = "right05"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

            elif afternight04__MMouth_dick_Success > 0:

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx02
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "..."

                $ df_eye = "down05"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                p "..."

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "Ya la tienes lo suficientemente dura."

                $ df_eye = "down04"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                pt "Por lo menos no se ha negado en rotundo."

                $ df_eye = "front05"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows sadx04
                call gensex_oral_c_frontHead_exp_label
                with dissolve

            elif afternight04__MMouth_dick_Done > 0:

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "..."

                $ df_eye = "front05"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx005
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "¿Es que quieres que te rompa las pelotas?"

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

            else:

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "No pienso meterme eso en la boca."

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

        "Chúpamela.":
            call p_Help

            $ df_eye = "front01"
            show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx03
            show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
            call gensex_oral_c_frontHead_exp_label
            with dissolve

            d "..."

            if afternight04__MMouth_dick_Success > 0:

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "¿Por quién coño me tomas?"

                $ df_eye = "front01"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows surprisex01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                p "Ayer bien que me lo hiciste."

                $ df_eye = "front02"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "¡Porque me la metiste en la boca sin mi permiso!"

                $ df_eye = "front00"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows surprisex02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                p "Tampoco parecía que te disgustara tanto..."

                $ df_eye = "right02"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "..."

                $ df_eye = "right04"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "Tssk..."

                $ df_eye = "right05"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx004
                show gensex_oral_d_frontHead_exp_eyebrows sadx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "Imbécil."

                $ df_eye = "down05"
                show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows sadx03
                call gensex_oral_c_frontHead_exp_label
                with dissolve

            else:

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx03
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                n "Acerca su mano a tu miembro."

                $ df_eye = "front05"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx04
                show gensex_oral_d_frontHead_exp_eyebrows suspiciousx02
                call gensex_oral_c_frontHead_exp_label

                with hpunch
                p "¡Ugh!"

                $ df_eye = "front05"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx05
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                n "Te la agarra con tanta fuerza que por un momento"

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                n "tienes la sensación de que te la va a arrancar."

                $ df_eye = "front01"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx14
                show gensex_oral_d_frontHead_exp_eyebrows angryx04
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "¡No me vengas con gilipolleces!"

                $ df_eye = "front02"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx09
                show gensex_oral_d_frontHead_exp_eyebrows angryx03
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                n "Finalmente te la suelta."

                $ df_eye = "front04"
                show gensex_oral_d_frontHead_exp_mouth sad_Talkingx07
                show gensex_oral_d_frontHead_exp_eyebrows angryx02
                call gensex_oral_c_frontHead_exp_label
                with dissolve

                d "Ahora fóllame y déjate de chorradas."

                $ df_eye = "front08"
                show gensex_oral_d_frontHead_exp_mouth sad_Silentx06
                show gensex_oral_d_frontHead_exp_eyebrows angryx01
                call gensex_oral_c_frontHead_exp_label
                with dissolve

        "...":
            call p_Help
            pass

    jump aftermorning05_beachafter_Stay_takingShirtOff


label aftermorning05_beachafter_Stay_takingShirtOff:

    pause 0.2

    $ df_eye = "front04"
    show gensex_oral_d_frontHead_exp_mouth sadbiting_Silentx05
    show gensex_oral_d_frontHead_exp_eyebrows suspiciousx01
    call gensex_oral_c_frontHead_exp_label
    with dissolve

    n "Te quitas la camisa del todo"

    $ df_eye = "down03"
    show gensex_oral_d_frontHead_exp_mouth happybiting_Silentx05
    show gensex_oral_d_frontHead_exp_eyebrows sadx02
    call gensex_oral_c_frontHead_exp_label
    with dissolve

    n "mientras Dídac hace lo propio con tus pantalones, calcetines y zapatos."

    $ df_eye = "down05"
    show gensex_oral_d_frontHead_exp_mouth happybiting_Silentx06
    show gensex_oral_d_frontHead_exp_eyebrows angryx02
    call gensex_oral_c_frontHead_exp_label
    with dissolve

    n "Apenas te da tiempo a reaccionar"

    scene day05
    with fade

    n "cuando descubres a Dídac poniéndose de pie acercándote su entrepierna"

    n "dispuesta a meterse tu polla en su empapada vagina."

    p "¡Ey,{w=0.25}{nw}"

    extend " ey,{w=0.25}{nw}"

    extend " ey!"

    scene bg_ped_04

    show didacfbodybelow_naked_drops 00:
        dfbody_center_superclose
    show didacfhandr leg_naked:
        dfbody_center_superclose
    show didacfbodytop_naked_drops 00:
        dfbody_center_superclose
    show didacfhandl hip_naked:
        dfbody_center_superclose
    show didacf_blush 03:
        dexpressions_center_superclose
    show didacf_eyes 05:
        dexpressions_center_superclose
    show didacf_pupils front05:
        dexpressions_center_superclose
    show didacf_eyebrows sadx01:
        dexpressions_center_superclose
    show didacfbodytop_hair:
        dfbody_center_superclose
    show didacf_mouth happybiting_Silentx04:
        dexpressions_center_superclose

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with fade

    d "¿Qué pasa?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¡¿Y el preservativo?!"

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "left03"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¿Hace falta?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "¡Pues claro que hace falta!"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¡¿No querrás que te deje preñada, no?!"

    $ df_eye = "down04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "..."

    jump aftermorning05_DC_soBad

label aftermorning05_DC_soBad:

    if DidacPregnant or pl.dp > 80:

        $ df_eye = "right02"
        show didacf_mouth sad_Talkingx02
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "¿Tan malo sería?"

        $ df_blush += 1

        $ df_eye = "right04"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx05
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "right01"
        show didacf_mouth sad_Talkingx004
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        d "Tampoco sería el fin del mundo..."

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

    p "¿Qué?"

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "¡¿Es que has perdido la razón?!"

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¡¿Acaso no recuerdas que si te quedas embarazada"

    $ df_eye = "right05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "nunca más volverás a ser un hombre?!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¡Pues claro que lo recuerdo!!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¡¿Entonces de qué coño estás hablando?!"

    $ df_eye = "right03"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "¿Y si no quisiera volver a ser hombre?"

    $ df_eye = "right05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    p "Dídac,"

    extend " no es momento para hacer este tipo de bromas."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Hablo en serio."

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    p "..."

    if DidacPregnant:

        $ aftermorning05_DC_pregnantConver_Cond = True

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "De hecho,"

        extend " es posible que ya esté embarazada..."

        $ df_eye = "right01"
        show didacf_mouth sadbiting_Silentx03
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front06"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows sadx05
        call dfeye_lab
        with dissolve

        p "¡¿CÓMO DICES?!"

        $ df_eye = "front04"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        p "¡¿Quien coño se ha corrido dentro de ti?!"

        if not DidacMCPregnant:

            aj "¿Is it possible to get here without being you the father? ERROR 26795"

        $ df_eye = "front01"
        show didacf_mouth sad_Talkingx07
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "¿Quién coño quieres que sea?"

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "¡¿YO?!"

        $ df_eye = "right01"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¡¿CUÁNDO?!"

        $ df_eye = "right02"
        show didacf_mouth happybiting_Silentx02
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        p "¡Pero si me puse un condón nuevo cada vez!"

        $ df_eye = "left03"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx002
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "Sí..."

        $ df_eye = "right04"
        show didacf_mouth happy_Talkingx02
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "Pero el último condón que te di..."

        $ df_eye = "left03"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "right05"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front03"
        show didacf_mouth sadbiting_Silentx06
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        p "¡¿Qué coño le hiciste al último condón?!"

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx01
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "Le corté la punta."

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx06
        show didacf_eyebrows sadx05
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front06"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows sadx06
        call dfeye_lab
        with dissolve

        p "¡¿LO DICES EN SERIO?!"

        $ df_eye = "right04"
        show didacf_mouth sad_Talkingx002
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "Sí."

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        p "¡¿POR QUÉ COÑO HICISTE ESO?!"

        $ df_eye = "left04"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front05"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "¡¿Y si te has quedado embarazada?!"

        $ df_eye = "right02"
        show didacf_mouth happy_Talkingx02
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "De hecho, es muy probable."

        $ df_eye = "right04"
        show didacf_mouth happybiting_Silentx02
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front04"
        show didacf_mouth happy_Talkingx01
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "Aunque fue tu tercera corrida,"

        $ df_eye = "front05"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "la verdad es que soltaste un montón..."

        $ df_eye = "down05"
        show didacf_mouth happybiting_Silentx04
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        p "¿Qué...?"

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "No te haces a la idea del efecto,"

    extend " del placer,"

    extend " de la puta sensación,"

    if DidacPregnant:

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "de lo que experimenté cuándo tu lefa estaba saliendo y llenándome por dentro."

        $ df_eye = "down04"
        show didacf_mouth happy_Talkingx02
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "Toda tu polla palpitando..."

    else:

        $ df_eye = "down04"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        if afternight04_Pussy_dick_deep_Speed_0_Done > 0:

            d "de lo que experimenté al tenerla entera dentro de mí."

        elif afternight04_Pussy_dick_med_Speed_0_Done > 0:

            d "de lo que experimenté al tenerla dentro de mí."

        else:

            d "de lo que experimenté al tenerla desnuda cerca de mí."

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Fue algo..."

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¡DÍDAC!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡¿QUE?!"

    $ df_eye = "front07"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡JODER!"

    if DidacPregnant:

        $ df_eye = "right02"
        show didacf_mouth sad_Talkingx07
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¡Ya sé que es muy probable que no vuelva a ser el de antes nunca más!"

    else:

        $ df_eye = "right02"
        show didacf_mouth sad_Talkingx07
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¡Ya sé que si te corres dentro"

        $ df_eye = "left03"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "es posible que no vuelva a ser nunca más el de antes!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Y QUÉ?!"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Me importa una mierda!"

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Como hombre,"

    if afternight04_didac_orgasms > 0:

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

        d "nunca había tenido un orgasmo parecido,"

    else:

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx002
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "nunca había sentido nada parecido,"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "ni por asomo,"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "a lo que sentí ayer!"

    if afternight04_didac_orgasms > 0:

        if afternight04_didac_orgasms == 1:

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡Aunque solo tuviera un mísero orgasmo!"

        elif afternight04_didac_orgasms < 4:

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Aunque solo tuve [afternight04_didac_orgasms] de ellos!"

        else:

            $ df_eye = "front01"
            show didacf_mouth happy_Talkingx05
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "¡Y tuve hasta [afternight04_didac_orgasms] de ellos!"

    else:

        $ df_eye = "right02"
        show didacf_mouth sad_Talkingx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "Aunque en realidad,"

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "no me corrí ni una puñetera vez..."

    $ df_eye = "front06"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡JODER!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡No te haces ni la más puta remota idea de lo que es eso!"

    $ df_eye = "down02"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡A la mierda mi polla!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Quiero que me sigas follando!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Quiero que me la metas por la mañana,"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "que me folles por la tarde,"

    $ df_eye = "front01"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡que me empotres por el resto de mi vida!"

    if afternight04_didac_orgasms == 0:

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "¡Que me des al menos un jodido orgasmo!"

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿Hablas en serio?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Nunca he hablado más en serio."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Pe-"

    extend "pero..."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "¿Y si después de mañana,"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "por la razón que sea,"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "no sientes el mismo placer que ayer?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Eso sería una putada."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Pero ni aunque fuera una décima parte de lo que sentí ayer,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "de verdad,"

    $ df_eye = "front05"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "ya valdría la pena."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¡¿Vas a poner en riesgo tu vida"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "simplemente para tener mejores orgasmos?!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿Simplemente?!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¿SIMPLEMENTE?!"

    if afternight04_didac_orgasms == 0:

        $ df_eye = "front00"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "Pero si ni siquiera te di un orgasmo."

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "front02"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¡No tienes ni puta idea de lo que estás hablando!"

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx005
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

    d "¡No son son solo los \"simples\" orgasmos, joder!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Es encima, {b}TODO{/b} lo demás!"

    $ df_eye = "front03"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "¿A qué te refieres?"

    $ df_eye = "right04"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Hoy he querido ir a la playa porque quería comprobar algo."

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "¿El qué?"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Quería saber si la puta manía que tengo por tu jodida polla"

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "me ocurría solo con la tuya,"

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "o si podía sentir lo mismo con cualquier otra."

    $ df_eye = "right04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Ni estando,"

    extend " literalmente,"

    $ df_eye = "front06"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "rodeados por un campo de nabos,"

    $ df_eye = "front00"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "algunos incluso casi tan grandes como el tuyo,"

    if aftermorning05_BallWakeUp_Cond:

        $ df_eye = "left01"
        show didacf_mouth sad_Talkingx06
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "ni siquiera tocándolos con disimulo bajo el agua"

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "cuando te pedí que fueras a buscar el balón,"

    else:

        $ df_eye = "left03"
        show didacf_mouth sad_Talkingx03
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "ni siquiera estando tan cerca de ellos que casi los podía tocar"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "sentía ni una milésima parte de lo que siento"

    $ df_eye = "down04"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "cuando no te tengo ni siquiera cerca!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¡Ni por puto asomo!!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Joder!"

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Es como,"

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "no sé..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Es como si tu polla fuera mi puta droga!"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Y aunque no me considero un drogadicto,"

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "he probado alguna,"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡y te juro que no he sentido nada parecido!"

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "..."

    if aftermorning05_DidacFar_01_Cond:

        $ df_eye = "right04"
        show didacf_mouth sad_Talkingx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "Cuando estaba con esos tipos,"

        $ df_eye = "right05"
        show didacf_mouth sad_Talkingx02
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "los he tocado..."

        $ df_eye = "front06"
        show didacf_mouth sad_Talkingx06
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "¡Joder!"

        if aftermorning05_howYouGetHome == "runningPolice":

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "¡Si hasta he pasado mi lengua por dos de sus pollas,"

            $ df_eye = "down02"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "y tenía a ese imbécil ahí debajo haciéndome la limpieza de alfombra...!"

            $ df_eye = "front05"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Y NADA!"

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx09
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡ABSOLUTAMENTE NADA!"

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Esas pollas sabían simplemente a salado"

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "y el de abajo es como si me estuviera haciendo simplemente un puto masaje!"

            $ df_eye = "down03"
            show didacf_mouth sad_Talkingx04
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "Sin embargo,"

            extend " ahora..."

            $ df_eye = "front05"
            show didacf_mouth sad_Talkingx03
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "Simplemente con estar cerca de ti,"

            extend " siento..."

    $ df_eye = "downLeft01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "No sé..."

    $ df_eye = "downLeft02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "No sé cómo puedo hacértelo entender."

    $ df_eye = "downLeft04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡No puedo pensar en nada más!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¿VALE?!"

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Solo pienso en tu polla!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "En tu cuerpo desnudo,"

    extend " en tu lengua,"

    extend " en tus manos,"

    extend " en tus pectorales,"

    $ df_eye = "downLeft04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "en cómo me agarras y me estampas contra la pared"

    $ df_eye = "down04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "y me la metes hasta el fondo,"

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx001
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    d "en tu esperma..."

    $ df_eye = "front06"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡JODER!"

    if afternight04__MMouth_dick_Done > 0:

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "¡SI HASTA TENÍA MINI-ORGASMOS SOLO CON CHUPARTE LA PUTA POLLA!"

        $ df_eye = "down05"
        show didacf_mouth sadbiting_Silentx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        pt "¿Mini-orgasmos?"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿Te crees que me gusta sentirme así?!"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Ahora te contradices."

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Me refiero a que no me gusta la idea de tener que depender de alguien."

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Me siento cómo..."

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "cómo si fuera una jodida prostituta adicta al crack"

    $ df_eye = "front01"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "y tú fueras mi maldita dosis."

    $ df_eye = "front06"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Tener que rebajarme a pedirte esto de esta manera..."

    $ df_eye = "front05"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "Pero al mismo tiempo,"

    $ df_eye = "down04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    d "No puedo volver a ser el de antes."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Simplemente,"

    extend " no podría..."

    if DidacPregnant:

        $ df_eye = "right04"
        show didacf_mouth sad_Talkingx004
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "No puedo."

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Tú..."

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx01
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Quiero que me folles [protname]."

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Quiero que me folles cada día durante el resto de tu vida."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Y si para ello tienes que besarme"

    $ df_eye = "right05"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "o dejarme preñada,"

    $ df_eye = "right01"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡pues que así sea!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Me da igual!"

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows sadx06
    call dfeye_lab
    with dissolve

    d "Solo quiero..."


####

    $ df_eye = "front02"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Hoy tengo la última cita con la chica que te convirtió en mujer."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "No vayas."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "Pe-"

    extend "pero..."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡No la necesitamos!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Te chantajeó con ir a sus citas"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "para que pudiera volver a ser el de antes,"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿no es así?"

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Bueno,"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡pues a tomar por el culo!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Ya no quiero volver a ser un hombre!"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Lo único que quiero es que sigas a mi lado."

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Aunque no me follaras,"

    $ df_eye = "front06"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "la sensación que tengo"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "ni que sea estando simplemente a tu lado,"

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx01
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "es..."

    $ df_eye = "front06"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "¿O es que piensas abandonarme?"

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    menu:

        pt "¿Abandonarlo?"

        "Por supuesto que no te voy a abandonar.":
            call p_Help
            $pl.ch_pts("dp",1)

            $ df_eye = "front02"
            show didacf_mouth happybiting_Silentx05
            show didacf_eyebrows sadx03
            call dfeye_lab
            with dissolve

            pass

        "...":
            call p_Help
            $pl.ch_pts("dp",-2)

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front00"
            show didacf_mouth sad_Talkingx09
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡¿En serio te lo estás pensando?!"

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

    d "..."

    jump aftermorning05_DC_withOthers

label aftermorning05_DC_withOthers:

    if aftermorning05_DC_pregnantConver_Cond:

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¡Pero por lo menos podrías habérmelo consultado"

        $ df_eye = "front02"
        show didacf_mouth sadbiting_Silentx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        p "antes de cortar el condón por tu cuenta!"

        $ df_eye = "front05"
        show didacf_mouth sad_Talkingx002
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        d "Si te lo hubiera dicho"

        $ df_eye = "front03"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "te hubieras negado en rotundo."

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "Te conozco demasiado bien."

        $ df_eye = "front05"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "No me importa si lo haces con otras,"

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx02
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "lo entendería perfectamente..."

    if pl.dp > 80:

        $ df_eye = "right04"
        show didacf_mouth sad_Talkingx02
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "Aunque..."

        $ df_eye = "right05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx04
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "right05"
        show didacf_mouth sadbiting_Silentx03
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

    p "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "No te estoy pidiendo amor eterno."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Solo te pido que..."

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Que sigas mi lado."

    $ df_eye = "right04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "Pero por lo que más quieras,"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "no vayas con esa bruja del demonio."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿Es que te acuerdas de ella?"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Fue ella quien me convirtió en lo que soy,"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿no?!"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¡Porque tú la intentaste violar!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "En serio..."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "¡¿Realmente me ves capaz de hacer algo así?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Yo no la intenté violar!"

    $ df_eye = "right03"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "O por lo menos no recuerdo haberlo hecho."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "¿De verdad no te acuerdas?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Que no joder!"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "..."

##

    pt "¿Y si me está diciendo la verdad?"

    pt "¿Neus le borró la memoria?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    pt "Pero..."

    pt "¿Para qué castigar a alguien de esta manera"

    pt "si luego no recuerda el motivo?"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Y bien?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Y bien,"

    extend " ¿qué?"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Joder!"

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Pues..."

    if pl.dp > 80:

        $ df_eye = "front02"
        show didacf_mouth sad_Talkingx06
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "¿Crees que podrás permanecer a mi lado?"

    else:

        $ df_eye = "front01"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "¿¡Es que no has escuchado nada de lo que he dicho?!"

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Desde luego,"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "si sigues siendo el gilipollas de siempre,"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "lo veo complicado."

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Tssk..."

    if pl.dp > 80:

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "Te prometo que intentaré comportarme mejor."

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx004
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "Puedo intentar comportarme mejor..."

        $ df_eye = "left04"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

    menu:

        pt "¿Qué entenderá por \"comportarse mejor\"?"

        "¿Intentarás ser más femenina?":

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows surprisex02
            call dfeye_lab
            with dissolve

            d "..."

            if pl.dp > 80:

                $ df_eye = "right01"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "No prometo nada."

                $ df_eye = "right04"
                show didacf_mouth sadbiting_Silentx04
                show didacf_eyebrows sadx03
                call dfeye_lab
                with dissolve

                pt "¿En serio se lo está planteando?"

            else:

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx004
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                d "Tampoco te pases..."

                $ df_eye = "front08"
                show didacf_mouth sad_Talkingx05
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "Además,"

                $ df_eye = "right04"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows surprisex01
                call dfeye_lab
                with dissolve

                d "como si no hubieran marimachos por ahí"

                $ df_eye = "right03"
                show didacf_mouth happy_Talkingx02
                show didacf_eyebrows sadx01
                call dfeye_lab
                with dissolve

                d "actuando y vistiendo igual que los tíos."

                $ df_eye = "right05"
                show didacf_mouth sadbiting_Silentx03
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                menu:

                    pt "\"Marimachos\" por ahí..."

                    "¿Entonces tendré que llamarte ninfómana marimacho?":
                        call p_Help

                        $ df_eye = "front01"
                        show didacf_mouth sadbiting_Silentx02
                        show didacf_eyebrows surprisex01
                        call dfeye_lab
                        with dissolve

                        pause 0.2

                        $ df_eye = "front04"
                        show didacf_mouth sad_Talkingx05
                        show didacf_eyebrows angryx03
                        call dfeye_lab
                        with dissolve

                        d "Serás imbécil..."

                    "...":
                        call p_Help
                        pass

        "¿Intentarás pedirme las cosas antes de hacerlas?":

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "left05"
            show didacf_mouth sad_Talkingx001
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "Es posible."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "Perdona,"

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "no te he escuchado bien."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡Que sí joder,"

            $ df_eye = "right03"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "que lo intentaré!"

        "...":
            call p_Help
            pass

    if  DidacPregnant:

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "Bueno,"

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "si te quedas embarazada,"

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "te ahorrarás el tener que comprar tampones."

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "Al menos durante nueve meses..."

        $ df_eye = "front08"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "right04"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "Mira que eres capullo cuando quieres."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "¿Eres consciente de la responsabilidad que es tener un bebé?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿Del dolor que sufrirás durante los últimos meses antes del parto,"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "de los vómitos,"

    extend " del mal estar,"

    extend " del dolor del parto...?"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Antes de parir se sufre?"

    $ df_eye = "right01"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Bueno,"

    $ df_eye = "left03"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "siempre podría abortar."

    $ df_eye = "front08"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Al fin y al cabo,"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "por lo que me dijiste al menos,"

    $ df_eye = "front05"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    if DidacPregnant:

        d "solo hacía falta quedarme embarazada."

    else:

        d "solo hace falta que me dejes embarazada."

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "No dijiste nada sobre cuánto tiempo tenía que estar en ese estado"

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "o de si realmente tenía que dar a luz,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "¿no?"

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    menu:

        pt "¿Qué pasaría si abortase?"

        "Si abortaras, volverías a ser un hombre.":
            $pl.ch_pts("dp",-1)

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "Eso no es lo que me dijiste."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "En ese momento no sabía toda la verdad."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx02
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "No suenas muy convincente..."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "Piensa lo que quieras."

            $ df_eye = "right04"
            show didacf_mouth sad_Talkingx002
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "Ya..."

            $ df_eye = "down05"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

        "En eso quizás tienes razón...":
            call p_Help

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "Por supuesto que tengo razón."

            $ df_eye = "front08"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

        "¿Y yo no tengo nada que decir al respecto?":
            call p_Help

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "Tú no eres quien va a tener que llevarlo nueve meses en la jodida tripa."

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            p "Pero también será mi bebé."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "No me vengas con gilipolleces."

            $ df_eye = "front03"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "No es ninguna gilipollez."

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            pause 0.2

            $ df_eye = "right04"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            d "Tssk..."

            $ df_eye = "right05"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            d "Lo que tú digas."

            $ df_eye = "right05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

        "No estoy a favor de matar a una vida inocente.":
            call p_Help

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            d "¿Y estás a favor de que dos tipos como nosotros"

            $ df_eye = "front02"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "sin oficio y viviendo en un piso de mierda"

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            d "tengamos un bebé?"

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            menu:
                pt "Sin oficio ni beneficio..."

                "Eres tú el que hace meses que no estás pagando nada.":
                    call p_Help
                    $pl.ch_pts("dp",-1)

                    $ df_eye = "front01"
                    show didacf_mouth sad_Talkingx07
                    show didacf_eyebrows angryx03
                    call dfeye_lab
                    with dissolve

                    d "¡Pues razón de más!"

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx05
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with dissolve

                "Después de nueve meses quizás pienses de otra forma.":
                    call p_Help

                    $ df_eye = "front01"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    d "..."

                    $ df_eye = "front05"
                    show didacf_mouth sad_Talkingx003
                    show didacf_eyebrows surprisex01
                    call dfeye_lab
                    with dissolve

                    d "¿De verdad te crees eso?"

                    $ df_eye = "front01"
                    show didacf_mouth sad_Silentx03
                    show didacf_eyebrows suspiciousx02
                    call dfeye_lab
                    with dissolve

                    p "Creo que subestimas el poder del amor maternal."

                    $ df_eye = "front05"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex02
                    call dfeye_lab
                    with dissolve

                    d "..."

                    $ df_eye = "right04"
                    show didacf_mouth sad_Talkingx004
                    show didacf_eyebrows serious
                    call dfeye_lab
                    with dissolve

                    d "Vaya gilipollez."

                    $ df_eye = "right05"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows angryx01
                    call dfeye_lab
                    with dissolve

                "Siempre podríamos darlo en adopción.":
                    call p_Help

                    $ df_eye = "front01"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    pause 0.2

                    $ df_eye = "front02"
                    show didacf_mouth sad_Talkingx08
                    show didacf_eyebrows angryx03
                    call dfeye_lab
                    with dissolve

                    d "¡Pues entonces quédate tu embarazado!"

                    $ df_eye = "front02"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex01
                    call dfeye_lab
                    with dissolve

                    p "Ha sido tu elección,"

                    extend " no la mía."

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx06
                    show didacf_eyebrows angryx04
                    call dfeye_lab
                    with dissolve

                    d "..."

                    $ df_eye = "right02"
                    show didacf_mouth sad_Silentx05
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    d "Tssk..."

                    $ df_eye = "front02"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    p "Quizás esto de ser madre te haga cambiar"

                    $ df_eye = "front05"
                    show didacf_mouth sad_Silentx06
                    show didacf_eyebrows suspiciousx02
                    call dfeye_lab
                    with dissolve

                    p "y te pongas más las pilas."

                    $ df_eye = "left04"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with dissolve

                    d "..."

                    $ df_eye = "front08"
                    show didacf_mouth sad_Talkingx003
                    show didacf_eyebrows angryx03
                    call dfeye_lab
                    with dissolve

                    d "Serás idiota."

                    $ df_eye = "right05"
                    show didacf_mouth sadbiting_Silentx04
                    show didacf_eyebrows sadx01
                    call dfeye_lab
                    with dissolve

                "...":
                    call p_Help
                    pass

        "...":
            call p_Help
            pass

    p "..."

    jump am05_DSex_horny

#####


