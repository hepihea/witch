

default day06_didacAlone_cunnilingus_Cond = False

default day06_didacAlone_sex_order_begin_Cond = False
default day06_didacAlone_orderExplanation_Cond = False
default day06_didacAlone_sex_WarnHer = ""

label day06_didacAlone_01:

    $ pdaytime = "06morning"
    $ pday_day = 6

    $ day06_company = "didacAlone"

    play music "audio/sfx/birds01.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx1')
    $ renpy.music.play("audio/sfx/rubbingPussy01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene black with fade
    
    $ renpy.notify("Day 06")

    # "You wake up at the hotel room, but Neus is not there."

    n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."

    n "Pero hay otro sonido extraño que te llama más la atención."

    gd "Mfff... mm... ah..." #Strong Feminine Moans

    n "Sientes una cálida y húmeda sensación en tu entrepierna."

    pt "¡¿Es otra vez el mismo jodido sueño?!"

    n "Una suave piel roza tu ombligo,"

    n "mientras tu polla se encuentra ahogada en una ardiente y húmeda carne."

    gd "Mmmm... mfh..." #Strong Feminine Moans

    pt "Estos gemidos..."

    pt "¡Son de Dídac!"

    gd "Aahhmm... Ghmmgh..." #Strong Feminine Moans

    scene morning04_bg bedroom_neus_a
    show morning04_bedroom_Didac_body 01a:
        morning04_bedroom_Neus_body_anim
        
    show morning04_bedroom_Didac_bodyass 01a:
        morning04_bedroom_Neus_bodyass_anim02

    show light 01:
        light01_topside_position
    

    show white:
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light_01b :
        light01_topside_position

    with fade
    
    window hide dissolve
    pause

    n "Entreabres los ojos y te encuentras un oscuro y borroso cuerpo justo encima de ti."

    show morning04_bedroom_Didac_body 01b
    show morning04_bedroom_Didac_bodyass 01b
    with Dissolve(0.5)

    n "Esa extraña silueta hace temblar tu cuerpo mientras te cabalga."

    p "Dídac..."

    show morning04_bedroom_Didac_body 01c
    show morning04_bedroom_Didac_bodyass 01b
    with Dissolve(0.5)

    p "¿Realmente eres tú?"

    n "Con un movimiento brusco y nada sugerente, se vuelve hacia ti."

    hide morning04_bedroom_Didac_body 
    hide morning04_bedroom_Didac_bodyass
    hide light
    hide morning04_bedroom_DMast_blinkeye
    hide light_screen_01
    show morning04_bg bedroom_neus_a
    show morning04_bedroom_Didac_body_ass 02c: 
        morning04_bedroom_Neus_bodyass_anim01
    show morning04_bedroom_Didac_body_body 02c
    #show morning04_bedroom_Neus_Prove
    show morning04_bedroom_Didac_exp_blush 03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyes 04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyepupils front_04:
        morning04_bedroom_exp_position
    show morning04_bedroom_Didac_exp_eyebrows normal:
        morning04_bedroom_exp_position
    # show morning04_bedroom_Didac_exp_glasses:
    #     morning04_bedroom_exp_position
    show morning04_bedroom_Didac_body_hair 02c

    show light 01:
        light01_topside_position

    with fade

    d "¿Por qué?"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
    show morning04_bedroom_Didac_exp_eyebrows serious
    with dissolve

    d "¿Acaso esperabas a esa enana morenita?"

    show morning04_bedroom_Didac_exp_mouth sad_Silentx02
    show morning04_bedroom_Didac_exp_eyebrows surprisex01
    with dissolve

    p "¿Dónde está [neusname]?"

    # CONDITIONAL

    if neusname == "Elur":

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows serious
        with dissolve

        d "¿Elur?"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows surprisex02
        with dissolve

        d "¿Es así como la llamas?"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows serious
    with dissolve

    d "Está en la otra habitación con esa rubia tetona."

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
    show morning04_bedroom_Didac_exp_eyebrows sadx01
    with dissolve

    d "Aparentemente le va más el pescado,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
    with dissolve

    d "o quizás es que no te has portado demasiado bien con ella..."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
    show morning04_bedroom_Didac_exp_eyebrows surprisex02
    with dissolve

    d "En cualquier caso, no me quejo,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    d "prefiero tenerte para mi sola."

    show morning04_bedroom_Didac_exp_mouth happy_Silentx05
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    pause 0.2

    show morning04_bedroom_Didac_comp01:
        truecenter
        #zoom 1.8 xpos 0.85 ypos 0.15 # Close shot
        zoom 1.6 xpos 0.75 ypos 0.2 # not so far.
        easein_bounce 1.0 zoom 2.3 xpos 1.15 ypos -0.15 #Super close

    pause 0.2
    with vpunch
    p "¡Ugh!"

    # show morning04_bedroom_Didac_exp_mouth happybiting_Silentx03
    # show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
    # with dissolve

    n "Sientes tu polla completamente arropada por su vagina"

    hide morning04_bedroom_Didac_comp01
    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx02
    with Dissolve(0.5)

    n "cuando baja bruscamente sus caderas."

    show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
    with dissolve

    p "¡Dídac!"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
    show morning04_bedroom_Didac_exp_eyebrows surprisex01
    with dissolve

    d "¿Qué?"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx02
    with dissolve

    d "¿Es que no te gusta?"

    show morning04_bedroom_Didac_exp_mouth sad_Silentx02
    show morning04_bedroom_Didac_exp_eyebrows surprisex02
    with dissolve

    p "¡La tengo delicada!"

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
    show morning04_bedroom_Didac_exp_eyebrows surprisex01
    with dissolve

    d "No me extraña,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    d "le diste un buen trote ayer."

    if p_ao_started or p_neus.vaginal_received > 5 or p_neus.anal_received > 5 or p_neus.blowjob_received > 5:

        d "Y por lo visto,"

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        d "cuando te quedaste a solas con ella"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
        show morning04_bedroom_Didac_exp_eyebrows surprisex02
        with dissolve

        d "aún te dio más caña."

        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx03
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        if p_ao_started:

            pt "Bastante, en realidad..."

        else:

            pt "En realidad perdí el conocimiento..."

    show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
    show morning04_bedroom_Didac_exp_eyebrows surprisex02
    with dissolve

    d "Pienso que lo justo es que ahora me des a mi un poco de caña,"

    show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
    show morning04_bedroom_Didac_exp_eyebrows serious
    with dissolve

    d "¿no te parece?"

    show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
    show morning04_bedroom_Didac_exp_eyebrows angryx01
    with dissolve

    menu:

        "¡¿Es que no me has oído cuando te he dicho que la tengo hecho mierda?!":
            call p_Help

            show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
            show morning04_bedroom_Didac_exp_eyebrows surprisex02
            with dissolve

            pause 0.2

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "Eso son excusas."

            show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx02
            show morning04_bedroom_Didac_exp_eyebrows surprisex01
            with dissolve

            p "Claro,"

            extend " está rojiza porque me la he pintado con un spray."

            show morning04_bedroom_Didac_exp_mouth sad_Silentx03
            show morning04_bedroom_Didac_exp_eyebrows serious
            with dissolve

            p "¡No te jode!"

            show morning04_bedroom_Didac_exp_mouth sad_Silentx05
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "Tssk..."

        "Ya me gustaría, pero no creo que sea capaz...":
            call p_Help

            $pl.ch_pts("dp",1)

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
            show morning04_bedroom_Didac_exp_eyebrows surprisex01
            with dissolve

            d "Si te esfuerzas un poco,"

            show morning04_bedroom_Didac_exp_mouth happy_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows angryx01
            with dissolve

            d "estoy segura que serás capaz de hacer algo."

            show morning04_bedroom_Didac_exp_mouth sad_Silentx01
            show morning04_bedroom_Didac_exp_eyebrows surprisex01
            with dissolve

            p "¡¿Es que no ves cómo está?!"

            show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
            show morning04_bedroom_Didac_exp_eyebrows angryx02
            with dissolve

            d "No me seas quejica."

            show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx03
            show morning04_bedroom_Didac_exp_eyebrows sadx01
            with dissolve

            p "..."

        "...":
            call p_Help

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with fade

    d "Además la enana me ha ordenado que te ordeñe antes de que se ponga el sol."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¡¿Qué?!"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "¡¿Por qué?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Yo que sé."

    $ df_eye = "right03"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Por mierdas de rituales y esas cosas raras."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Y por qué...?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Por qué no te está ordeñando ella misma?"

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Por lo visto ha pensado que sería mejor que fuera yo misma la que lo haga."

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Algo me dice que vuestras citas no fueron tan bien como ella esperaba."

    $ df_eye = "right03"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Por la expresión en su cara,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "diría que la cosa va por ahí."

    $ df_eye = "front03"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Me equivoco?"

    $ df_eye = "front05"
    show didacf_mouth happy_Silentx05
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    menu:

        "Quizás no me he comportado de la mejor manera con ella.":
            call p_Help

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            d "Quizás no..."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows surprisex02
            call dfeye_lab
            with dissolve

            d "¿pero quien soy yo para juzgar?"

            $ df_eye = "front05"
            show didacf_mouth happybiting_Silentx04
            show didacf_eyebrows serious
            call dfeye_lab
            with dissolve

            p "..."

        "No te haces a la idea del tipo de monstruo que es.":
            call p_Help

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows surprisex02
            call dfeye_lab
            with dissolve

            pause 0.2

            $ df_eye = "right01"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            d "A mi en el fondo me da igual."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx04
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "Pero creo que deberías saber lo mucho que se ha preocupado por ti durante todo el día de hoy"

            $ df_eye = "front02"
            show didacf_mouth sad_Talkingx03
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "y las molestias que se ha tomado para poder traernos hasta aquí de forma segura."

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows serious
            call dfeye_lab
            with dissolve

            p "Aparte..."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            p "No tienes ni idea de lo que pesas, cabrón."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "..."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx04
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "Si no se preocupara por ti,"

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx03
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "no creo que hubiera hecho todo esto."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows serious
            call dfeye_lab
            with dissolve

            p "No te equivoques,"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            p "no lo está haciendo por mi,"

            $ df_eye = "right02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "sino por ella misma."

        "...":
            call p_Help

            $ df_eye = "front05"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "Eres todo un {a=https://es.wikipedia.org/wiki/Don_Juan}Don Juan{/a},"

            extend " ¿verdad?"

            $ df_eye = "front05"
            show didacf_mouth happy_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Ey,"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "que lo entiendo."

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "Con esa altura y ese pecho tan plano, "

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "hasta la arpía tetuda resulta más interesante."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Aunque sinceramente,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "a mi ya me está bien."

    $ df_eye = "front05"
    show didacf_mouth happy_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    pause 0.2

    show morning04_bedroom_Didac_comp01:
        truecenter
        #zoom 1.8 xpos 0.85 ypos 0.15 # Close shot
        zoom 1.6 xpos 0.75 ypos 0.2 # not so far.
        easein_bounce 1.0 zoom 2.3 xpos 1.15 ypos -0.15 #Super close

    pause 0.2
    with vpunch
    p "¡Ugh!"

    n "Vuelves a sentir una de sus embestidas."

    p "¡¿No podrías ser un poco más delicada?!"

    hide morning04_bedroom_Didac_comp01

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with Dissolve(0.5)

    d "¡Se un hombre, joder!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    n "Intentas quitártela de encima,"

    $ df_eye = "down03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    n "pero tu cuerpo apenas es capaz de moverse."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    if p_ao_started:

        pt "Después de lo que me hizo esa bruja,"

        pt "estoy hecho mierda..."

    else:

        pt "Realmente estoy hecho polvo..."

###

    scene day06
    with fade

    n "Apartas tus ojos de ella para ver a tu alrededor."

    p "¿Dónde estamos?"

    d "En una habitación de hotel."

    p "Eso ya lo he notado."

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with fade

    d "¿Entonces para qué preguntas?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Me refiero dónde está este hotel?"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "{a=https://es.wikipedia.org/wiki/París}París{/a}."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¡¿París?!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿Qué diablos hacemos aquí?"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    d "Cosas de la brujita."

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Por lo visto tiene una red de contactos que la pueden ayudar a camuflarse en esta ciudad,"

    $ df_eye = "right03"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "personas muy turbias si me preguntas,"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "aunque tampoco es que entienda muy bien el {a=https://es.wikipedia.org/wiki/Idioma_francés}francés{/a}..."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    pause 0.2

    scene day06
    with fade

    n "Te fijas en la ventana."

    p "¡¿Está anocheciendo?!"

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows serious
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with fade

    d "¿Ahora te das cuenta?"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Te has pasado el puto día sobando."

    $ df_eye = "down04"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Pero por suerte tu polla se ha despertado antes que tú."

    $ df_eye = "down05"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "No puedes culparme por aprovecharme de ello."

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    pause 0.2

    show morning04_bedroom_Didac_comp01:
        truecenter
        #zoom 1.8 xpos 0.85 ypos 0.15 # Close shot
        zoom 1.6 xpos 0.75 ypos 0.2 # not so far.
        easein_bounce 1.0 zoom 2.3 xpos 1.15 ypos -0.15 #Super close

    pause 0.2
    with vpunch
    ono "pam"

    p "¡La madre que te parió!"

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front07"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with fade_short

    d "Hmmm..."

    $ df_eye = "up05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "Joder..."

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    show closetocum_mc
    with Dissolve(0.5)

    d "¿Por qué se siente tan bien?"

    $ df_eye = "down02"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¡Ey,"

    extend " ey,"
    
    extend " ey!"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Por qué coño está reaccionando así?"

    $ df_eye = "front00"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¿Cuanto hace que me estás cabalgando de esta manera?"

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "No hace tanto..."

    $ df_eye = "right05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Bueno,"

    extend " quizás un rato."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Pues entonces no te sorprendas."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡¿Pero que mierda de aguante tienes?!"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¡Ha!"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¡Me gustaría saber cuanto aguantabas tú!"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Tskk..."

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    jump day06_didacAlone_CanYouStandUp

label day06_didacAlone_CanYouStandUp:

    pause 0.2

    scene black
    with fade

    n "Levanta sus caderas y te libera de su cálido interior."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with fade

    d "¿Te puedes levantar?"

    $ df_eye = "down04"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "No lo sé..."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Realmente siento que me faltan fuerzas,"

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "es como si tuviera el cuerpo adormecido."


    if p_prot_anal_fingered_received_from_p_txell > 0:

        scene day06
        with fade

        n "Sientes que te separa las piernas."

        p "¡Ey!"

        n "Y empieza a juguetear con sus dedos por tu orificio anal."

        p "¡¿Qué coño haces?!"

        d "No veía que te quejaras tanto cuando te lo hacía la rubia tetuda."

        p "..."

        d "¿Te lo hacía mejor,"

        d "o es que solo dejas que te hagan esto"

        d "si quien te lo hace tiene las tetas más grandes que la cabeza?"

        $ df_eye = "front05"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        show light 01:
            light01_topside_position
            alpha 0.5
        with fade

        p "..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Levántate joder,"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "esto no es manera de follar!"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Parece que esté montándome un muñeco en lugar de una persona."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¡¿Me has escuchado cuanto te he dicho que ayer me dejasteis para el arrastre?!"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Cuántas corridas tuviste?"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx005
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Tres,"

    extend " cuatro,"

    extend " seis?"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "No creo que fuera la cantidad,"

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "sino la intensidad..."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¿Esa es tu excusa?!"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Ya me hubiera gustado verte a ti en mi situación!"

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Tssk..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Vaya semental de mierda estás hecho."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "¡¿Qué?!"

    $ Pedrera_char_Cond = "DidacSuperClose"
    call Pedrera_char_lab

    $ df_eye = "front01"
    show didacf_mouth happy_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    show light 01:
        light01_topside_position
        alpha 0.5
    with Dissolve(0.5)

    pause 0.2

    scene day06

    with vpunch
    p "¡UGHMM!"

    n "Sientes su cálido coño empapado en sus jugos por toda tu cara."

    d "Ya que por lo visto no tienes mucho aguante,"

    # CONDITIONAL, did you lick her?

    if p_didac.cunnilingus_received > 1 or p_didac.anilingus_received > 1:

        d "por lo menos demuestra que puedes usar un poco más esa lengua tuya,"

        d "al fin y al cabo ayer no lo hiciste tan mal..."

    else:

        d "por lo menos demuestra que esa lengua no la tienes solo para decir tonterías."

        if p_didac.cunnilingus_received < 1 and p_didac.anilingus_received < 1:

            d "Al fin y al cabo ayer ni siquiera me la pasaste por detrás."

        elif p_didac.anilingus_received > 1:

            d "Al final y al cabo ayer ni siquiera la usaste por ahí."

    p "..."

    d "¡Oh,"

    extend " vamos!"

    d "Solo un poco."

    menu:

        pt "Puto Dídac..."

        "Lo siento, pero paso.":
            call p_Help
            $pl.ch_pts("np",-2)

            d "Hmmm..."

            d "Con que esas tenemos,"

            d "¿verdad?"

                # n "Aparta ligeramente su entrepierna de tu cara"
                # n "y rápidamente pone una mano sobre tu nariz."
                # n "Cuando abres la boca para poder respirar"
                # n "te hace tragar el contenido de un frasco que contiene un líquido rojo y espeso"

        "¡¿Es que no me has dicho que necesita mi esperma antes de que anochezca?!":
            call p_Help

            d "¡Pues date prisa y empieza!"

            p "¡¿Qué tiene que ver una cosa con la otra?!"

            d "¡Pues que me gustaría tener más de un orgasmo, joder!"

            if p_didac.orgasm >= 5:

                p "Lo dices como si ayer no hubieras tenido ninguno..."

                d "..."

                d "Bueno..."

                d "tuve unos cuantos..."

                p "¿Entonces?"

                d "..."

                d "¡Pues que quiero tener más, joder!"

            if p_didac.orgasm >= 4:
                
                d "Ayer solo me diste cuatro orgasmos."

                p "¿Te parecen pocos?"

                d "Mejor hubieran sido cinco..."

                p "O seis."

                d "Lo vas pillando."

                p "..."

            elif p_didac.orgasm == 3:

                d "Ayer me dejaste con las ganas con solo tres orgasmos."

                pt "Solo dice..."

            elif p_didac.orgasm == 2:
                
                d "¡Ayer me diste solo dos orgasmos de mierda!"

                p "Son más de los que me diste tú a mí."

                d "¡Vete a cagar!"

            elif p_didac.orgasm == 1:
                
                d "¡AYER ME DISTE UN JODIDO MÍSER ORGASMO!"

                d "¡Así que espero que hoy me des bastante más!"

            elif p_didac.orgasm == 0:

                d "¡AYER NO ME DISTE NI UN JODIDO ORGASMO!"

                d "¡Así que espero que hoy me des algo más que NADA!"
            
            if p_didac.orgasm < 3:

                p "..."

            d "¡¿Sabes qué?!"

            d "¡Da igual!"

            d "Ya que no participas,"

            d "tendré que recurrir a esto."

            p "¡¿A qué?!"

        "<Lamerle el coño>":
            call p_Help

            $ day06_didacAlone_cunnilingus_Cond = True

            n "Acercas tu lengua a su empapada vagina"

            n "dónde la deslizas a lo largo y ancho de su tierna rosada carne."

            d "Hmm..."

            d "¡No me seas delicado y métela dentro!"

            menu:

                pt "Que no sea delicado, dice..."

                "¿Por qué tienes que ser siempre tan impaciente?":
                    call p_Help

                    d "¡¿Impaciente...?!"

                    d "Mientras tú dormías como un perro,"

                    d "He tenido que llevarte de un coche a otro durante todo el jodido día"

                    d "para luego estar apretujada contigo y esas dos frikis"

                    d "durante {b}casi doce horas{/b} sin aire acondicionado {b}con este puto calor{/b},"

                    d "teniendo tu polla a escasos centímetros,"

                    d "¡sin mencionar que llevo todo el puto día más cachonda que una mona en celo!"

                    d "¡Creo que ya he esperado lo suficiente!"

                    pt "¿Por qué se compara con una mona?"

                    d "No siento que se mueva esa lengua tuya."

                "<Obedecer sin rechistar>":
                    call p_Help

                    pass

            n "Profundizas tu lengua en el interior de su cálida carne"

            n "mientras saboreas su espeso jugo que se mezcla con tu saliva."

            d "Hmmm..."

            d "Mucho mejor."

            n "Intentas levantar tus manos para agarrarla de las nalgas,"

            n "pero tus músculos no te responden."

            n "Apenas eres capaz tu lengua y tu mandíbula."

            n "Eso no le impide seguir moviendo sus caderas para restregarse aún más en tu rostro"

            n "dejándote empapado todo el rostro con sus jugos."

            d "Dale más caña, joder."

            n "Sigues moviendo tu lengua tan rápido y profundo cómo te es posible."

            d "Seeehh...!"

            d "No pares!"

            n "Sientes que sus piernas empiezan a temblar descontroladamente."

            p "Ughh..."

            $ day06_morning_Didac_orgasms += 1

            n "Hasta que finalmente explosiona en tu boca."

            d "Hmmm..."

            d "Cuánto necesitaba esto..."

            n "Su entrepierna está tan pegada a tu cara que apenas te deja respirar."

            p "Dí-"

            extend "dac..."

            d "Hmmm..."

            d "No se te da mal,"

            d "pero necesitaré algo más que tu lengua..."

            jump day06_didacAlone_bloodDrink
                # n "Aparta ligeramente su entrepierna de tu cara"
                # n "y rápidamente pone una mano sobre tu nariz."
                # n "Cuando abres la boca para poder respirar"
                # n "te hace tragar el contenido de un frasco que contiene un líquido rojo y espeso"

###

label day06_didacAlone_bloodDrink:

    n "Aparta ligeramente su entrepierna de tu cara"

    n "y rápidamente pone una mano sobre tu nariz."

    n "Cuando abres la boca para poder respirar"

    n "te hace tragar el contenido de un frasco que contiene un líquido rojo y espeso"

    n "sin que puedas hacer nada para evitarlo."

    with hpunch
    p "¡KOF KOF KOF!"

    p "¡¿Qué coño me has hecho tragar?!"

    d "Tranquilo,"

    d "no es veneno."

    d "Yo también he bebido un poco de ella."

    n "Te levantas algo furibundo ante sus narices."

    p "¡Te estoy preguntando qué coño era!"

    d "Pero mírate..."

    p "¡¿Que?!"

    d "Estás de pie."

    n "Has dado un brinco tan rápido debido a tu cólera,"

    n "que apenas has sido consciente de ello."

    d "Y fíjate en tu polla,"

    d "quizás está algo rojiza,"

    d "pero sigue estando bien dura..."

    d "Dídac."

    p "¿Qué coño me has hecho beber?"

    d "¿No lo adivinas?"

    p "..."

    n "El sabor te resulta familiar, algo metálico y salado."

    p "¿Es sangre?"

    d "Seh."

    p "¡¿Por qué diablos me has hecho beber sangre?"

    d "Sé que habías dicho que esa mujer es una bruja,"

    d "pero sinceramente,"

    d "entre lo del esperma y la sangre,"

    d "al final pensaré que es una vampiresa en realidad..."

    p "¿Es su sangre?"

    d "Me dijo que si tenías problemas de erección te hiciera beber el frasco,"

    d "que te daría energía."

    p "¡Pero no tenía problemas de erección!"

    d "No..."

    d "Eso es verdad."

    d "Pero te ha ido bien,"

    extend " ¿no?"

    p "¡¿Y si ahora tengo un puto ataque al corazón o me pasa algo raro, qué?!"

    d "Joder..."

    d "vaya {a=https://en.wiktionary.org/wiki/drama_queen}drama-queen{/a} estás hecho..."

    p "¡Lo digo en serio Dídac!"

    d "Tranquilo..."

    d "Me ha dicho que si te pasaba algo que la llamara por teléfono."

    p "..."

    d "La chica puede ser muy rara y misteriosa, pero no creo que te quiera muerto."

    p "Ella quizás no, pero de ti empiezo a tener mis dudas."

    d "¡Serás imbécil!"

    d "¡Lo único que quiero es que me folles!"

    d "¿O acaso quieres que te monte como si fueras un muñeco de goma?"

    p "..."

    menu:

        pt "¿Siempre ha sido así cuando iba tan caliente?"

        "Quizás tengas razón.":
            call p_Help
            $pl.ch_pts("dp",1)

            d "Pues claro que tengo razón."

            d "Al fin y al cabo la rubia no quiere ni verte."

            d "Y la morenita,"

            jump day06_didacAlone_brunetteTalk

        "Casi preferiría follarme a la rubia antes que tú.":
            call p_Help

            d "..."

            d "Bah."

            d "¿Para qué mentirte?"

            d "Yo también querría follármela."

            d "No veas las cosa que me hizo ayer..."

            d "Pero el caso es que la chica es más tortillera que una tortilla de patatas."

            d "Me temo que no vas a conseguir nada con ella."

            d "Con la morenita tampoco creo que tengas mucha más suerte,"

            jump day06_didacAlone_brunetteTalk

        "¡¿Es que no te importa que pueda palmarla con tal de que te folle?!":
            call p_Help
            $pl.ch_pts("dp",-1)

            d "¿De verdad crees que quiero que la palmes?"

            p "..."

            d "Joder, lo único que quiero es que me folles,"

            d "si realmente fuera tan peligroso,"

            d "como ya te he dicho,"

            d "no creo que me hubiera dado este bote."

            d "Al fin y al cabo con la rubia no vas a follar,"

            d "y con la morenita..."


label day06_didacAlone_brunetteTalk:

    $ day06_didacAlone_checkOrder_Cond = False

    if day06_morning_rejection == "neus":
        
        d "Bueno..."

        d "Ha sido elección tuya."

    else:

        d "no parecía demasiado..."

        extend " feliz,"

        d "después de como han terminado las cosas entre vosotros."

    p "..."

    d "Así que tendrás que conformarte conmigo."

    menu:

        pt "Conformarme con ella..."

        "¿Y si no me da la gana?":
            call p_Help

            d "..."

            d "Entonces tengo órdenes de ordeñarte como una vaca."

            menu:

                pt "¡¿Como una vaca?!"

                "¿Y cómo piensas obligarme ahora que puedo moverme?":
                    call p_Help

                    jump day06_didacAlone_checkOrder

                "Tranquila, solo era curiosidad.":
                    call p_Help

                    d "Hmmm..."

                    d "Así me gusta."

                    jump day06_didacAlone_showingHerself
                        # n "Completamente desnuda y de forma sugerente"
                        # n "se encuentra sobre la cama a cuatro patas mostrándote su abierta entrepierna"
                        # n "moviendo sus caderas a modo de invitación."

                "...":
                    call p_Help

                    jump day06_didacAlone_showingHerself

        "Supongo que puedo conformarme.":
            call p_Help

            d "¡¿Supones?!"

            d "Vaya Romeo estás hecho..."

            p "Como si tu fueras una Julieta ejemplar..."

            d "Tssk..."

            jump day06_didacAlone_showingHerself
                # n "Completamente desnuda y de forma sugerente"
                # n "se encuentra sobre la cama a cuatro patas mostrándote su abierta entrepierna"
                # n "moviendo sus caderas a modo de invitación."

        "Por supuesto que me conformo contigo.":
            call p_Help

            d "..."

            d "Supongo que me lo tomaré como un elogio."

            jump day06_didacAlone_showingHerself
                # n "Completamente desnuda y de forma sugerente"
                # n "se encuentra sobre la cama a cuatro patas mostrándote su abierta entrepierna"
                # n "moviendo sus caderas a modo de invitación."


label day06_didacAlone_checkOrder:

    $ day06_didacAlone_checkOrder_Cond = True

    d "Me parece que no conoces demasiado bien lo retorcida que puede ser la morenita esa..."

    p "¿Cómo dices?"

    d "¡Dame la mano!"

    n "Sientes tu brazo alzándose para luego reposar tu mano sobre la suya."

    p "¡¿Euh?!"

    d "¡Ponte a cuatro patas!"

    n "Tus piernas flaquean y caes de rodillas sobre el suelo"

    n "para luego posar tus manos sobre el adoquinado simulando la posición de un perrito."

    pt "¡¿Qué?!"

    d "¡Ladra!"

    p "¡WOF"

    extend " WOF"

    extend " WOF!"

    pt "¡¿Qué cojones?!"

    d "¡Date un puñetazo!"

    n "Sientes que tu mano se alza hasta acercarse a tu mejilla,"

    n "pero se detiene al poco de llegar a rozar tu piel."

    pt "¡¿Qué diablos?!"

    d "Vaya..."

    d "por lo visto tiene sus límites."

    p "¡La madre que te parió Dídac!"

    d "Oh,"

    extend " vamos..."

    d "No te pongas así."

    d "Solo quería ver si realmente funcionaba."

    d "Para ser sincera,"

    d "aún tengo mis dudas."

    pt "¡¿Aún?!"

    d "Veamos..."

    p "¡Ni se te ocurra!"

    d "¡Métete el puño por el culo!"

    p "¡¿Qué?!"

    n "Sientes tu mano acercándose a tu trasero,"

    n "justo cuando tus dedos acarician la parte superficial de tu orificio anal se detienen."

    d "Vaya..."

    p "¡¿Te piensas que soy un puto juguete?!"

    d "No me seas hipócrita,"

    d "en mi lugar estarías haciendo lo mismo."

    # CHOICE

    menu:

        "Es posible...":
            call p_Help

            d "¿Lo ves?"

            d "Tranquilo,"

            d "solo quería ver si lo que me había dicho la morenita era cierto o no."

        "¡¿Por quien coño me tomas?!":
            call p_Help

            d "Tío,"

            d "que nos conocemos."

            p "¡Yo jamás te hubiera hecho meterte el puño por el culo!"

            d "Te hubiera detenido antes de que eso ocurriera."

            p "¡No te lo crees ni tú!"

            d "Eso ha dolido."

            p "¡Mírame!"

            p "¡Estoy a cuatro patas con una mano en el culo!"

            p "¡¿A qué coño llamas tú confianza?!"

            d "Vale,"

            extend " vale..."

    n "Vuelves a tener el control sobre tu cuerpo e instintivamente te pones de pie."

    d "¿Ya estás contento?"

    p "¿Qué-"

    extend "qué estás haciendo?"

label day06_didacAlone_showingHerself:

    n "Completamente desnuda y de forma sugerente"

    n "se pone a cuatro patas sobre la cama mostrándote su abierta entrepierna"

    n "moviendo sus caderas a modo de invitación."

    d "¿Acaso no ves lo húmeda que estoy?"

    p "..."

    d "¿Qué es lo que quieres?"

    d "¿una paloma mensajera,"

    d "un puto letrero?"

    d "Fóllame de una vez."

    if day06_didacAlone_checkOrder_Cond:

        p "Después de lo que me has hecho hacer, ¿crees que tengo ganas de follarte?"

        d "Tu polla sigue estando bien dura."

        p "¡Deja mi polla en paz joder!"

        d "Vale,"

        extend " vale..."
        
        d "Te pido disculpas,"

        d "no lo volveré a hacer..."

        d "¿Así mejor?"

        p "¿Te crees que soy imbécil?"

        d "Lo que veo es que estás cachondo,"

        d "que yo estoy cachonda,"

        d "que necesitas correrte cuanto antes,"

        d "y quiero que me folles."

        d "Dime,"

        d "¡¿qué más coño quieres?!"

    menu:

        pt "Desde luego..."

        "Preferiría que me trataras como a una persona normal." if not day06_didacAlone_checkOrder_Cond:
            call p_Help

            jump day06_didacAlone_normalPerson

        "Lo que quiero es que me trates como una persona normal." if day06_didacAlone_checkOrder_Cond:
            call p_Help

            jump day06_didacAlone_normalPerson

        "<Follártela>":
            call p_Help

            jump day06_didacAlone_fuckHer_begin


label day06_didacAlone_normalPerson:

    d "..."

    d "¿Quieres que te diga cuánto te quiero y te amo?"

    menu:

        pt "¿Es una indirecta?"

        "No te pido amor, solo un poco de empatía.":
            call p_Help

            d "..."

            d "¿Empatía?"

            d "¡¿Pero qué mierdas estás diciendo?!"

            d "¿Es que esa morenita te ha vuelto un maldito mariposón en tres días?"

            p "Eres tú quien me está pidiendo sexo."

            d "¡Por que ahora tengo coño, joder!"

            d "No me vengas con gilipolleces ahora."

        "Tampoco hace falta eso.":
            call p_Help

            d "¿Entonces qué coño quieres?"

        "¿Por qué? ¿Acaso es verdad?":

            d "..."

            if pl.dp > 120:

                d "¡Por supuesto que no idiota!"

            else:

                d "¡Por supuesto que no imbécil!"

            menu:

                pt "Ya..."

                "¿Estás segura?":
                    call p_Help

                    if pl.dp > 120:
                        $pl.ch_pts("np",1)

                        d "..."

                        d "Tsssk..."

                        d "Serás imbécil..."

                    else:
                        $pl.ch_pts("np",-1)

                        d "¡Claro que estoy segura!"

                        d "¡Me encanta tu polla,"

                        d "pero no pienses cosas raras ahora!"
                "...":
                    call p_Help
                    pass

        "No estaría mal.":
            call p_Help

            d "Ya sabes que no me van esas mariconadas, joder..."
        
        "...":
            call p_Help

    p "No cambiarás nunca,"

    p "¿verdad?"

    d "Mientras te sigas poniendo cachondo de esta manera,"

    d "¿qué necesidad hay?"

    pt "La madre que lo..."

    d "¡Vamos hijo de puta,"

    d "dame duro con esa polla que tienes!"

    if (p_didac.anal_received + afternight04__Anal_dick_med_Success) > 0:

        d "Hasta te dejo metérmela por el culo si es lo que prefieres..."

        p "¿No te disgustaba tanto?"

        d "Bueno..."

        d "por lo visto,"

        d "quizás no está tan mal después de todo..."

        if (p_didac.analDeep_received + afternight04__Anal_dick_deep_Success) > 4:

            p "Especialmente después de habértela metido hasta el fondo"

            p "y hayas descubierto que no te disgusta tanto,"

            p "¿No es así?"

            d "..."

        else:

            p "Vaya,"

            extend " vaya..."

            d "Tssk..."

    else:

        p "¿Y si te la quiero meter por detrás?"

        d "..."

        d "¿Y a qué viene eso ahora?"

        p "Pregunto..."

        d "Tssk..."

    d "¡Métemela dónde quieras,"

    d "pero fóllame de una vez!"

    menu:

        pt "Dónde quiera..."

        "¿Y si te la quiero meter por la garganta?":
            call p_Help

            jump day06_didacAlone_whatAboutThroat


        "<Follártela>":
            call p_Help

            jump day06_didacAlone_fuckHer_begin

label day06_didacAlone_whatAboutThroat:

    d "..."

    d "Tío..."

    d "¿Por qué?"

    menu:

        pt "¿Por qué...?"

        "Por lo que me has obligado a hacer." if day06_didacAlone_checkOrder_Cond:
            call p_Help

            d "..."

            d "Solo quería probar si funcionaba o no la mierda esta..."

            d "no te pongas así,"

            extend " joder."

            d "Te he pedido disculpas,"

            d "¿no?"

            p "Vaya mierda de disculpas me has dado."

            d "¿Qué coño más quieres que haga?"

        "Porque me apetece.":
            call p_Help

            d "..."

            d "¡¿Estás de coña?!"

            p "No."

            d "..."

            if p_didac.blowjob_done > 5:

                $pl.ch_pts("np",-1)

                d "Tssk..."

            if p_didac.blowjob_done > 0:

                $pl.ch_pts("np",-2)

                d "Tampoco es que me lo pidieras tanto ayer..."

                p "..."

            else:

                $pl.ch_pts("np",-4)

                d "¡Si ayer no me lo pediste ni una sola vez!"

                p "..."

        "Porque me gusta cómo la chupas.":
            call p_Help

            d "..."

            if p_didac.blowjob_done > 1:

                if p_didac.blowjob_done > 5:

                    d "Hmm..."

                    if p_didac.blowjobDeep_done > 2:

                        p "Si hasta llegaste a tenerla entera en la garganta sin que protestaras demasiado."

                        d "¡Pero si casi me ahogas!"

                        p "Te gustó,"

                        p "y lo sabes."

                        d "..."

                    d "Supongo que el haber tenido polla"

                    d "me sirve de referencia para chuparla mejor..."

                    p "Me alegra ver que te esfuerzas en complacerme."

                    d "..."

                    d "¡Lo hago para que luego me folles como un hombre!"

                    d "Así que no me decepciones."

                    menu:

                        "¿Como el hombre que ya no eres?":
                            call p_Help

                            $pl.ch_pts("np",-2)

                        "Como si fuera lo único que disfrutas...":

                            $pl.ch_pts("np",1)

                            d "¿Y tú qué vas a saber?"

                            p "Con verte la expresión que haces cuando me la estás chupando,"

                            p "tengo suficiente."

                        "¿Por qué sigues engañándote a estas alturas?":
                            call p_Help

                            d "¡No me estoy engañando!"

                            d "¡No tienes ni puta idea de lo jodidamente bien que se siente cuando...!"

                            p "Cuando..."

                            p "¿qué?"

                            d "..."

                            d "¡Que te follen!"

                            p "No,"

                            p "eres tú quien me está pidiendo que te folle."

                        "...":
                            call p_Help

                    d "..."

                    d "Tsssk..."

                else:

                    d "Tampoco te la he chupado tanto para que me digas esto..."

                    if (afternight04__MMouth_dick_Success + afternight04__MMouth_dick_Deep_Success) > 3:

                        if afternight04__MMouth_dick_Deep_Success > 2 and p_didac.blowjobDeep_done > 2:

                            p "Pero bien que tanto antes de ayer como ayer te la tragaste entera..."

                        elif p_didac.blowjobDeep_done > 2:

                            p "Pero bien que ayer te la tragaste entera..."

                        elif afternight04__MMouth_dick_Deep_Success > 2:

                            p "Pero antes de ayer bien que te la tragaste entera..."

                        else:

                            p "Pero antes de ayer bien que me la chupaste bastante..."

                        d "¡¿y quien fue el que me forzó a ello?!"

                        p "Tampoco te quejaste tanto..."

                        d "..."

                        d "Tsssk..."

                    else:

                        $pl.ch_pts("np",-2)

                        p "Eso no quita que me gusta."

                        d "¡Eso no quita que me estés mintiendo a la cara!"

                        p "No te estoy mintiendo."

                        d "Lo que tú digas."

                        d "..."

            else:

                $pl.ch_pts("np",-4)

                d "Claro..."

                d "Te gustó tanto que ayer ni siquiera me lo pediste una sola vez."

                d "¡No me seas hipócrita de mierda!"

                p "..."


    jump day06_didacAlone_blowjob_Possible


label day06_didacAlone_blowjob_Possible:

    d "Si quieres te la puedo chupar un poco,"

    d "pero no te me corras en la boca..."

    d "no seas así."

    if DidacMCPregnant:

        d "Al fin y al cabo fuiste tú quien me dejó preñada."

        p "¿Y puedo saber quién fue el que le hizo un agujero al jodido condón?"

        d "..."

    else:

        d "Al fin y al cabo,"

        d "dejaste que me preñara un desconocido."

        p "¿Y eso es mi culpa?!"

    d "Está claro que yo no estaba en mis facultades para decidir por mí misma,"

    d "¿no crees?"

    p "¡¿Y por eso es mi culpa?!"

    if DidacMCPregnant:

        d "No he dicho que fuera tu culpa..."

        p "¿Entonces qué quieres decir?"

        d "Nada."

        d "Déjalo..."

        pt "Cada vez se parece más a una mujer..."

    else:

        d "..."

    menu:

        pt "Que no me corra en su boca..."

        "Chúpamela y luego ya veré dónde decido correrme.":
            call p_Help

            d "..."

            if pl.dp > 110:

                d "Si no hay otra opción..."

            else:

                $pl.ch_pts("np",-2)

                d "Como te corras en mi boca,"

                d "te corto los huevos."

        "Te prometo que no me correré en tu boca.":
            call p_Help

            $pl.ch_pts("np",1)

            d "..."

            d "Se agradece."

            p "¿Me estás dando las gracias?"

            d "No me seas gilipollas."

        "Si tanto te va a disgustar, quizás es mejor que pasemos al plato principal.":
            call p_Help

            d "Hmmm..."

            d "Me alegra saber que por fin lo entiendes."

            n "Sugerentemente se aparta de ti y se pone de cuatro patas sobre la cama"

            n "meneando su trasero a modo de invitación."

            jump day06_didacAlone_fuckHer_begin

    jump day06_didacAlone_blowjob_Preparation

label day06_didacAlone_orderExplanation_label:

    if day06_didacAlone_orderExplanation_Cond == False:

        if day06_didacAlone_sex_order_begin_Cond:

            p "¿Y cómo es que antes te he obedecido y ahora no?"

            d "..."

            d "Aparentemente, para que sea una orden tiene que ser algo simple y posible."

            d "Además de que se debe decir con autoridad y seguridad."

            d "Eso es lo que me ha dicho al menos."

            p "..."

        $ day06_didacAlone_orderExplanation_Cond = True

    return


label day06_didacAlone_blowjob_Preparation:

    d "Tssk..."

    d "Vale..."

    d "Estírate al menos."

    p "¿Es una orden?"

    d "Si lo fuera,"

    d "ya lo estarías haciendo."
    
    call day06_didacAlone_orderExplanation_label

    n "Te pones sobre la cama, y cómodamente relajas tu espalda y tus pies sobre la sábana."

    n "Sientes su aliento acercándose a tu erecto miembro."

    p "No me des más órdenes."

    d "Si haces lo que quiero,"

    d "¿para qué coño querría darte órdenes?"

    p "..."

    n "Sientes su aliento acercándose a tu entrepierna."

    d "..."

    p "¿Qué pasa?"

    d "Ya sé que te la estuve chupando ayer,"

    d "pero me sigue pareciendo muy raro todo esto..."

    p "¿A qué te refieres?"

    d "¿Tú me chuparías la polla si fueras mujer?"

    menu:

        pt "¿Y lo de follarle el coño, qué?"

        "No creo.":
            call p_Help

            d "Pues a eso me refiero, joder."


        "Es posible.":
            call p_Help
            #$pl.ch_pts("np",-2)

            call day06_didacAlone_blowjob_ofCourse

        "Por supuesto.":
            call p_Help
            #$pl.ch_pts("np",-2)

            call day06_didacAlone_blowjob_ofCourse

            p "¿Por qué te cuesta tanto de creerme?"

            d "¡Por que nunca se la has chupado a nadie!"

            p "¡¿Y tú qué sabes?!"

            d "¡Joder!"

            d "¡Te conozco desde el puto {a=https://ast.wikipedia.org/wiki/Educación_preescolar}parvulario{/a}!"

            d "¡Si te hubieran interesado los rabos lo habría notado!"

            p "Te veo muy seguro..."

            d "¡Hace años que dormimos bajo el mismo techo!"

            d "¡Te aseguro que lo sabría!"

            pt "A decir verdad, me conoce bastante bien."

            menu:

                pt "Aunque estos últimos días he estado actuando de una forma bastante extraña..."

                "Quizás te sorprendería.":
                    call p_Help
                    $pl.ch_pts("np",-2)

                    d "..."

                    d "Lo dudo."

                    d "Pero lo que tú digas..."

                "Vale, tienes razón, solo quería ver cómo reaccionabas.":
                    call p_Help
                    $pl.ch_pts("np",-1)

                    d "..."

                    d "Serás gilipollas..."

                "¿Tanto te molestaría haber dormido con una persona gay?":
                    call p_Help
                    $pl.ch_pts("np",-3)

                    d "..."

                    d "¡¿A qué viene esta pregunta tan estúpida?!"

                    d "¡Sabes perfectamente que algunos de los compañeros del gimnasio son gays!"

                    d "¡Salimos de copas y de fiesta con ellos!"

                    d "¡No me vengas con tonterías ahora!"

                    p "¿Entonces?"

                    d "Nunca te has fijado en los paquetes de los tíos,"

                    d "ni siquiera te he visto fisgonear páginas porno de tíos cachas o nada por el estilo,"

                    d "más bien todo lo contrario,"

                    d "¡así que no me vengas con estas mierdas ahora!"

                    p "¿Es que me espías?"

                    d "¡VIVIMOS JUNTOS JODER!"

                    p "..."

                    d "¿Qué coño te pasa?"

                    p "..."

                    pt "Eso me gustaría saber también..."

        "...":
            call p_Help

            d "¡Pues eso!"

    jump day06_didacAlone_blowjob_excuse

label day06_didacAlone_blowjob_ofCourse:

    d "..."

    p "¿Qué?"

    d "No te lo crees ni tú."

    return

label day06_didacAlone_blowjob_excuse:

    # p "¡Pero si me has estado follando mientras dormía!"

    # d "No es lo mismo!"

    if p_didac.blowjob_done > 3:

        p "No parecía que lo estuvieras pasando tan mal ayer mientras me la estabas chupando."

        d "..."

    n "Su cálida lengua se posa sobre tu aún sensible glande,"

    n "para luego percibir sus labios rodeando la punta de tu miembro."

    p "Hmmm..."

    p "¿Ves como se te da bien si te pones a ello?"

    d "¡Vegte a la miegda!"

    n "Profundiza aún más con su habilidosa garganta metiéndose la mitad de tu falo en su interior."

    p "Hmmm..."

    p "Y luego dices que no te gusta."

    d "..."

    p "¡Ugh...!"

    n "Su mano te agarra con fuerza los testículos."

    p "Oye,"

    p "eso no hace falta."

    n "Haciendo oídos sordos sigue con lo suyo."

    p "¡Ugh!"

    if p_didac.blowjobDeep_received > 1:

        n "Su garganta logra profundizar aún más en tu miembro,"

        n "hasta que sientes sus labios y su nariz en la tierna piel de tu ombligo."

        p "¿Lo ves...?"

        p "¡Te has vuelto a meter la polla entera en la garganta!"

        p "Y luego dices que no te gusta..."

        n "Su mirada es desafiante, pero sigue en su labor sin decir palabra alguna."

        n "No solo su habilidad consigue llegar hasta lo más profundo,"

        n "si no que además es capaz de aumentar el ritmo de sus cabezadas."

    else:

        n "A pesar de sus intentos, no logra llegar más allá de la mitad de tu miembro."

        p "¿Quieres que te ayude con la mano?"

        d "..."

    pt "Dios..."

    if p_didac.blowjobDeep_received > 1:

        n "Sientes tu polla palpitar en su garganta."

    else:

        n "Sientes tu polla palpitar en el interior de su boca."

    n "Rápidamente saca su cabeza de entre tus piernas."

    d "¡Oye!"

    d "¡Te estoy haciendo esto porque me lo has pedido!"

    d "¡Pero yo también te he pedido algo!"

    d "¡¿Recuerdas?!"

    p "Lo recuerdo."

    d "Creo que ya te la he chupado lo suficiente."

    if p_didac.blowjobDeep_received > 1:

        d "¡Hasta me la he metido entera en la jodida garganta!"

        d "¡¿No crees?!"

    p "Supongo..."

    d "¡¿Entonces?!"

    menu:

        pt "Ya me la ha chupado lo suficiente..."

        "Tienes razón.":
            call p_Help

            d "Pues claro que tengo razón."

            n "Sugerentemente, vuelve a ponerse a cuatro patas sobre la cama."

            jump day06_didacAlone_fuckHer_begin

        "He decidido correrme en tu garganta.":
            call p_Help

            jump day06_didacAlone_blowjob_wantCumIn

label day06_didacAlone_blowjob_wantCumIn:

    d "..."

    d "Estás de coña,"

    d "¿verdad?"

    p "No."

    if day06_didacAlone_checkOrder_Cond:

        p "Con lo que me has hecho antes,"

        p "creo que es lo justo."

        d "Te estoy haciendo esta mamada precisamente para pedirte disculpas por eso."

        d "¡Aunque tampoco te he obligado a hacer nada del otro mundo!"

        p "Pero lo has intentado."

        d "¡Te hubiera parado antes de que lo hubieras hecho."

        menu:

            pt "Me hubiera parado..."

            "No te lo crees ni tú.":
                call p_Help
                $pl.ch_pts("np",-2)

                d "¿Tan bajo concepto tienes de mí?"

                p "No me harás cambiar de opinión, Dídac."

            "Es posible.":
                call p_Help
                $pl.ch_pts("np",-3)

                d "..."

                p "Pero no me harás cambiar de opinión."

    else:

        $pl.ch_pts("np",-5)

        d "¿Hablas en serio?"

        p "Sí."

        d "..."

    d "Con que esas tenemos..."

## FUCK HER in ORDERING style.

label day06_didacAlone_sex_order_begin:

    $ day06_didacAlone_sex_order_begin_Cond = True

    n "Ves que se aparta de ti y se vuelve a poner a cuatro patas sobre la cama."

    pt "No estará haciendo lo que creo que está..."

    with vpunch
    d "¡FÓLLAME!"

    n "Tu cuerpo se levanta instintivamente con tu polla aún en una tersa y dura erección,"

    n "mientras tus manos se agarran a sus nalgas."

    d "E-"

    extend "espera un po..."

    with vpunch
    with vpunch
    d "¡AAAUUCHH!"

    n "Y sin piedad alguna, se la metes de golpe casi entera."

    d "Mierda..."

    d "Podrías haber ido un poco más con cuida..."

    n "Tus caderas empiezan a embestir la estrecha vagina de Dídac."

    d "¡Ughh...!"

    n "En cada nueva arremetida, tu polla logra profundizar más en su estrecho interior"

    n "hasta que finalmente la piel de tus caderas impacta duramente contra sus nalgas."

    d "¡Un poco más despacio no te haría ningún daño!"

    p "Te recuerdo que no me estoy moviendo por voluntad propia."

    d "Ughhmm..."

    pt "También podría ordenarme que fuera más lento..."

    n "Sientes toda tu polla empapada en sus cálidos jugos vaginales mientras sigues embistiéndola sin piedad."

    d "¡Joder!"

    n "Tus caderas se desplazan progresivamente con más intensidad"

    n "al sentir que su interior se vuelve menos hostil."

    d "Hmmm..."

    n "Tus manos se agarran con más fuerza en sus nalgas"

    n "al sentir que un repentino -y algo doloroso- hormigueo recorre tu entrepierna."

    pt "No voy a tardar mucho..."

    n "Tus caderas siguen embistiendo con dureza su rojizas nalgas"

    n "mientras esta se agarra a la sábana a la par que gime como una perra en celo."

    d "¡No pares!"

    p "Parece que ya no le duele tanto..."

    p "¡Ghh...!"

    d "¡¡NO PARES!!"

    n "Tu polla palpita con dureza mientras percibes tu esperma recorrer tu entrepierna"

    n "hasta que finalmente explota en su interior."

    d "¡¡DIOOS!!"

    n "Tus caderas siguen embistiéndola con dureza mientras tu esperma se derrama en su interior."

    n "Empiezas a notar que eres capaz de mover los dedos de las manos a voluntad"

    n "y que progresivamente, vuelves a ser dueño de tus acciones"

    n "al ser capaz de disminuir paulatinamente el movimiento de tus caderas."

    pt "¿Ha sido porque me he corrido"

    pt "o porque ya he cumplido su orden?"

    n "Finalmente logras detenerte."

label day06_didacAlone_sex_Stop:

    d "No pares..."

    d "¡FÓLLAME!"

    p "..."

    d "¿Por qué coño no sigues?"

    if day06_didacAlone_checkOrder_Cond or day06_didacAlone_sex_order_begin_Cond:

        p "Parece que ya no tengo por que obedecer tus órdenes."

        d "Joder..."

    d "¡¿En serio?!"

    p "¡Ugh!"

    d "¿Solo te vas a correr una vez?"

    with vpunch

    n "Pierdes las fuerzas de tus piernas y caes rendido de espaldas en la cama."

    pt "Mierda..."

    n "Ese dolor punzante arremete con más intensidad en tu entrepierna."

    n "Tu polla vuelve a ponerse rojiza y percibes en ella un mordaz ardor."

    p "¡¿Qué coño le está pasando?!"

    d "..."

    d "No lo sé,"

    d "pero parece que sigue estando dura..."

    p "Dídac,"

    p "¡me está doliendo un montón!"

    if day06_didacAlone_sex_WarnHer == "False":

        d "¡Quizás si me hubieras avisado antes de correrte,"

        d "sentiría algo de pena por ti!"

        p "Dídac..."

        d "Tssk..."

    else:

        if day06_morning_Didac_orgasms > 2:

            d "..."

        elif day06_morning_Didac_orgasms == 2:

            d "¡Solo he tenido dos orgasmos de mierda!"

        elif day06_morning_Didac_orgasms == 1:

            d "¡SOLO ME HAS DADO UN ORGASMO DE MIERDA!"

        else:

            aj "Didac had 0 orgasms. Is that possible? 1578"

        if day06_morning_Didac_orgasms < 3:

            p "¡¿Es que me quieres matar?!"

            if day06_morning_Didac_orgasms < 2:

                d "Quizás te lo merezcas..."

                p "¡Dídac!"

            else:

                d "..."

    d "Veamos..."

    n "Sientes que acerca su rostro a tu polla y le da un lametón."

    p "Hmm..."

    n "Sientes una mezcla de intenso escozor y un placer masoquista."

    d "No parece que te haya dolido."

    p "Dídac,"

    extend " para."

    # You're lying on the bed.

    n "Posa su cuerpo sobre el tuyo, sin metérsela dentro."

    d "Vale,"

    extend " vale..."

    d "Te dejaré descansar unos minutos."

    p "¡¿Unos minutos?!"

    d "Le prometí a la enana que cuando te hubieras corrido,"

    d "me fuera a verlas."

    p "¿A verlas?"

    d "Aparentemente tenemos que compartir tu esperma entre las tres..."

    d "No solo quería que te corrieras en mi coño porque me encanta sentir tu polla ahí,"

    d "si no porque..."

    d "Bueno,"

    if p_didac.cumReceived == "vaginal":

        d "quería comprobar de nuevo lo bueno que es tu amiguita morena con su longeva lengua."

    elif day06_didacAlone_sex_vag:

        d "quiero comprobar lo buena que es tu amiguita morena con su lengua también."

    else:

        d "quería comprobar lo buena que es tu amiguita morena con su lengua también."

    d "No te voy a engañar."

    menu:

        pt "¿Las tres juntas?"

        "Preferiría que no fueras con ellas.":
            call p_Help

            if pl.dp > 110:

                call day06_didacAlone_evenIfSheWanted

            else:

                if day06_didacAlone_sex_order_begin_Cond:

                    d "¡Y yo hubiera preferido que me hubieras follado!"

                    if day06_didacAlone_fuckHer_beforeAnal_Str == "beg":

                        d "¡Especialmente cuando te lo he suplicado!"

                    elif day06_didacAlone_fuckHer_beforeAnal_Str == "please":

                        d "¡Especialmente cuando te lo he pedido como me has pedido!"

                else:

                    if day06_didacAlone_sex_WarnHer == "False" or not day06_didacAlone_sex_vag:

                        if day06_didacAlone_sex_WarnHer == "False":

                            d "¡Y yo hubiera preferido que me hubieras avisado antes de correrte!"

                            d "¡¿Después de ni siquiera haberme avisado antes de que te corrieras?!"

                        elif day06_didacAlone_sex_vag == False:

                            d "¡Y yo hubiera preferido que me follaras el coño!"

                    else:

                        d "¡Y yo hubiera preferido que me dieras muchos más orgasmos de los que me has dado!"

                p "..."

                d "Pero como puedes ver,"

                d "no todo el mundo tiene lo que quiere."

        "Te prohíbo que vayas con ellas.":
            call p_Help

            d "..."

            d "¿Me lo prohíbes?"

            if pl.dp < 110:

                d "¡¿Tú?!"

            if day06_didacAlone_sex_order_begin_Cond:

                d "¡¿Después de haberte negado a follarme?!"

                if day06_didacAlone_fuckHer_beforeAnal_Str == "beg":

                    d "¡CUANDO TE LO HE SUPLICADO Y TODO!"

                elif day06_didacAlone_fuckHer_beforeAnal_Str == "please":

                    d "¡Cuando te lo he pedido del modo en que me has ordenado y todo!"

            else:

                if day06_didacAlone_sex_WarnHer == "False" or not day06_didacAlone_sex_vag:

                    if day06_didacAlone_sex_WarnHer == "False":

                        d "¡¿Después de ni siquiera haberme avisado antes de que te corrieras?!"

                    if day06_didacAlone_sex_vag == False:

                        d "¡¿Después de haberme follado el culo"

                        d "cuando te he pedido explícitamente que me follaras el coño?!"

                else:

                    d "¡¿Me lo prohíbes?!"

                    p "Sí."

            if pl.dp > 110:

                d "..."

                d "¡Debería meterte el puño por el culo!"

                p "¿Y por qué no lo haces?"

                d "..."

                d "¡Tssk...!"

                d "Por que a pesar de lo imbécil que llegas a ser,"

                d "Tienes pegada esa polla que..."

                p "¿Sí?"

                d "¡Al final te voy a dar de hostias!"

                n "Deja ir un suspiro profundo."

                call day06_didacAlone_evenIfSheWanted

            else:

                d "¡VETE A LA MIERDA!"

        "También se podrían venir aquí y así veo lo que hacéis.":
            call p_Help

            d "..."

            d "Creo que no conoces demasiado bien a la rubia..."

            d "Y en cuanto a la morenita,"

            if day06_morning_rejection == "neus":

                d "bueno..."

                d "eso ha sido cosa tuya."

            else:

                d "por lo que me ha parecido,"

                d "no está demasiado contenta contigo."

            d "Yo en tu lugar,"

            d "especialmente en tu estado,"

            d "no la haría cabrear demasiado..."

        "¡¿Es que acaso prefieres la compañía de esa bruja mal nacida?!":
            call p_Help

            d "..."

            d "No es que lo prefiera,"

            d "pero tengo esa extraña tendencia a intentar permanecer con vida."

            menu:

                "¿Y crees que ella te protegerá?":
                    call p_Help

                    d "Lo que tengo claro es que tú ahora mismo"

                    d "no tienes muchas posibilidades de ayudar a nadie..."

                "¿Acaso no ves que te está manipulando?":
                    call p_Help

                    d "¿Manipulándome?"

                    d "¿Cómo?"

                    menu:

                        "Haciendo exactamente lo que ella te pide.":
                            call p_Help

                            d "¡Duh!"

                            d "Obviamente."

                        "Haciendo que te alejes de mí.":
                            call p_Help

                            d "¿Alejarme de ti?"

                            d "Estoy aquí intentando follar contigo a solas en esta habitación."

                            d "¿De qué manera funciona eso de alejarme de ti?"

                            p "..."

                    d "Pero a ver..."

                    d "¿Qué quieres que haga?"

                    d "¿Llevarle la contraria a alguien que con su sola mirada"

                    d "puede hacerte lo que quiera?"

                    d "No me parece la cosa más inteligente, sinceramente."

                    d "Especialmente viendo que tiene a un padre psicótico"

                    d "y tú no puedes ni moverte."


                "...":
                    call p_Help

                    d "No te hagas sangre,"

                    d "no te voy a discutir que esto que nos ha estado pasando estos últimos días"

                    d "es jodidamente de manicomio,"

                    d "pero viéndolo por el lado positivo,"

                    d "joder..."

                    d "nunca había tenido unos orgasmos como estos."

                    p "¿Es que para ti todo se reduce a eso?"

                    d "No..."

                    d "¿Pero qué le voy a hacer?"

                    d "¿Amargarme y llorar?"

                    p "..."

                    pt "No sé por que me sorprende si siempre ha sido de vivir el presente"

                    pt "sin pensar demasiado en el futuro."

            p "..."

        "¿Es que no eres consciente del tipo de monstruo que es ella?":
            call p_Help

            d "Precisamente por esa razón creo que no es la mejor idea llevarle la contraria."

            d "¿No crees?"

            p "..."

            d "Además,"

            d "en tu estado,"

            d "tampoco es que vayas a ser de mucha ayuda..."

        "...":
            call p_Help


        # HERE DEPENDS ON HOW POINTS AND ORGAMS YOU GIVED HER, SHE WILL BE A BIT MORE COMPREHENSIVE WIT YOU OR COMPLETELY MAD.

    jump day06_didacAlone_didacLeaving

label day06_didacAlone_evenIfSheWanted:

    d "Aunque prefiriese estar contigo,"

    d "me ha dejado bien claro que es una cuestión de vida o muerte."

    d "Y lo siento,"

    d "pero después de lo todo lo que vi ayer,"

    d "creo que desobedecerla no es la mejor idea."

    p "..."

    return


label day06_didacAlone_didacLeaving:

    #p "Maldito seas Dídac..."

    p "Ughh..."
    
    n "Intentas mover tu cuerpo,"

    n "pero te resulta imposible."

    d "Ni siquiera eres capaz de levantar un brazo."

    d "¡Después de una sola corrida!"

    d "Vaya semental estás hecho."

    #Conditional?

    p "¡Por culpa de lo que me has obligado a tragarme!"

    #if day06_didacAlone_checkOrder_Cond:

    d "..."

    n "Se aparta de ti saliendo de la cama y poniéndose de pie."

    n "Ves que se dirige desnuda a la puerta de la habitación."

    p "¡¿Me vas a dejar solo y desnudo cuando no puedo ni moverme?!"

    d "¿Por qué?"

    d "¿Tienes miedo que venga alguien a violarte?"

    # CHOICE

    menu:

        "¡¡Qué clase de amigo eres?!":
            call p_Help

            d "No me seas nenaza..."

            d "¿No pedías descanso?"

        "Con lo solicitado que es mi esperma últimamente, tampoco me extrañaría...":
            call p_Help

            d "Eso es por culpa de la brujita,"

            d "así que tampoco te creas el centro del universo ahora...."

        "...":
            call p_Help

    jump day06_didacAlone_afterSex_DidacLeaving

label day06_didacAlone_afterSex_DidacLeaving:

    d "Dentro de un ratito volveré y espero que me puedas durar un poco más."

    p "¡Oye!"

    n "Al abrir la puerta descubrís a [neusname] en el pasadizo."

    d "..."

    d "¿Y tú qué haces aquí?"

    ne "Bueno..."

    d "¿Tanto confías en mí?"

    ne "No eres alguien que me inspire demasiada confianza, precisamente."

    d "..."

    ne "Sin mencionar que te dije que usaras el frasco solo en caso de verdadera necesidad."

    d "¡Si no se podía ni mover!"

    ne "Pero tenía la polla dura,"

    ne "¿No es así?"

    d "..."

    d "Supongo..."

    ne "*Largo suspiro*"

    n "Ves a Dídac dispuesto a salir por la puerta."

    ne "Dídac..."

    d "¿Sí?"

    ne "Vas desnuda."

    d "¿Y qué?"

    ne "¡Ponte algo, por favor!"

    d "Ahora la chica es tímida."

    ne "Hay otra gente en este hotel,"

    ne "gente que prefieres no provocar."

    d "..."

    ne "No es una broma."

    ne "Ve al baño y coge una bata al menos."

    d "Tssk..."

    n "Regresa con la bata puesta."

    d "¿Así estoy mejor para la señorita?"

    ne "..."

    ne "Venga,"

    extend " vamos,"

    ne "antes de que se enfríe demasiado."

    menu:

        pt "Me siento un tanto ignorado..."

        "¡Esperad!":
            call p_Help
            pass

        "No me vais a dejar aquí, ¡¿Verdad?!":
            call p_Help
            pass

        "¡Confiesa que estabas detrás la puerta porque eres una pervertida de narices!":
            call p_Help

            $pl.ch_pts("np",-1)

            d "..."

            ne "Nunca he negado que sea una pervertida,"

            ne "pero si no entiendes el riesgo que sufrimos todos esta noche,"

            ne "es que no has entendido nada."

            d "..."

            ne "Vámonos Dídac."

        "...":
            call p_Help
            pass

    ono "PUM"

    p "Maldita sea..."

    pt "Cuando vuelva,"

    pt "lo va a follar su..."

    n "El punzante dolor en tu entrepierna te impide pensar con claridad."

    pt "¡¿Por qué coño sigue dura como una piedra?!"

    p "Ughh..."

    n "Sigues sin ser capaz de mover tus músculos."

    n "Tus párpados te pesan cada vez más."

    pt "¿Por qué estoy tan cansado?"

    n "Fijas tu mirada en la ventana y descubres sin demasiada sorpresa"

    n "que ha caído finalmente la oscura noche."

    n "Tus párpados cesan por completo."

    scene black
    with fade

    jump day06_ending_DidacAlone_motionless


## Credits

label day06_ending_DidacAlone_motionless:

    call day06_ending_window

    p "¿Dídac?"

    p "¿Eres tú?"

    d "¿Soy tan obvia?"

    p "¿Se puede saber qué estás haciendo?"

    d "Eso también es obvio,"

    d "¿no crees?"

    p "¿Es que no has tenido suficiente antes?"

    d "¿Por qué me haces preguntas tan obvias?"

    p "Me vas a dejar la polla hecha una mierda."

    d "¡Ey!"

    d "No me eches solo a mí la culpa."

    d "Por lo visto con una sola corrida la bruja no ha tenido suficiente,"

    d "así que he venido a por más."

    d "Aunque tampoco me voy a quejar."

    p "¿Se puede saber qué habéis estado haciendo las tres?"

    d "Creo que eso también es obvio..."

    p "¿Ahora te mola el rollo lésbico?"

    d "¿Cuándo me ha dejado de gustar?"

    p "..."

    d "Y no te imaginas lo larga que la tiene la morenita de las narices..."

    if p_ao_started:

        pt "Está hablando de su lengua,"

        extend " ¿verdad?"

    elif night04_pedrera_blowjob_DONE:

        pt "Sí..."

        extend " me hago una idea..."

    else:

        pt "Espero que esté hablando de su lengua..."

    p "¡Ugh!"

    p "¡Intenta ser un poco más delicada!"

    d "La tienes enorme."

    p "¡Y también está muy sensible!"

    d "No te quejes tanto,"

    d "¡si se nota que te encanta!"

    p "¡¿Es que me vas a follar así todos los días?!"

    d "Espero que no,"

    d "también me gustaría que fueras tú quien me folle a mi."

    p "..."

    d "Pero por lo visto ahora no puedes ni moverte."

    p "No sé de quien es la culpa..."

    d "Eso digo yo."

    p "..."

    # CONDITIONAL?
    # d "Si hubieras decidido follarme en lugar de forzarme a usar ese frasquito,"

    # d "ahora no sería un jodido inválido."

    p "Ughh..."

    d "¿Otra vez tan pronto?"

    d "Déjame disfrutarla un poco más..."

    if day06_didacAlone_cunnilingus_Cond:

        if day06_morning_Didac_orgasms > 3:

            aj "Is it possible she had more than 3 orgasms? 57892"

        elif day06_morning_Didac_orgasms == 3:

            d "Apenas me has dado dos orgasmos de pacotilla."

        elif day06_morning_Didac_orgasms == 2:

            d "Apenas he tenido un mísero orgasmo."

    else:

        if day06_morning_Didac_orgasms > 2:

            d "Por que te recuerdo que apenas he tenido solo [day06_morning_Didac_orgasms] orgasmos."

            p "¿Y te parecen pocos?"

            d "¡Por supuesto que sí!"

        elif day06_morning_Didac_orgasms == 2:

            d "Por que te recuerdo que solamente he tenido dos orgasmos de pacotilla."

        elif day06_morning_Didac_orgasms == 1:

            d "¡Porque te recuerdo que solamente he tenido una mierda de orgasmo!"

        else:

            aj "This text shouldn't appear. 5798"


    if day06_didacAlone_cunnilingus_Cond:

        p "Te recuerdo que antes también te me has corrido en la boca."

        d "Ese no cuenta."

        p "¡¿Y por qué coño no va a contar?!"

        d "Por que no se siente igual."

        d "Con tu polla..."

        d "no sé por qué,"

        d "pero es distinto."

    p "¡Pues no seas tan brusca!"

    d "Joder..."

    d "¡Es que me encanta!"

    p "Eres insaciable."

    d "Acostúmbrate."


    window hide dissolve
    pause

    call false_gameover

    jump textless_gameover
