default night05_DidacHome_NeusLate_Cond = False

label night05_DidacHome:

    $ saturation_tint_level = "verydark"

    with hpunch
    ono "RIIIING"

    p "Hmmm..."

    n "Oyes el particular sonido de llamada de tu móvil."

    scene morning04_bg bedroom_neus_a_night
    with fade_long1s

    pt "¿Qué hora es?"

    show morning04_bg_bedroom_neus_b_night
    with Dissolve(0.5)

    n "Antes de que seas capaz de reaccionar"

    with hpunch
    n "Dídac se levanta a toda prisa dirigiéndose al suelo"

    show morning04_bg_bedroom_neus_c_night
    with Dissolve(0.5)

    n "dónde -escondido entre tus pantalones- está tu celular."

    d "Neus..."

    #$ saturation_tint_level = "verydark"
    $ df_blush = 3

    scene beds_night_lightOff_blindUp_DemptyMCempty_blur03

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


    $ df_eye = "down04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with fade

    d "¿Es este el nombre de la bruja?"

    $ df_eye = "down05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    pt "¡¿Ya son las nueve de la noche?!"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Dídac,"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "dame el teléfono."

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿No es así cómo se llama esa enana morenita que está en nuestra clase de ilustración?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Dídac."

    if DidacPregnant:

        jump night05_DidacHome_DidacHungPhone

    else:

        $ df_eye = "front08"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        n "Te entrega el móvil y presionas el botón verde."

        jump night05_DidacHome_AnswerCall

label night05_DidacHome_DidacHungPhone:

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    n "El tono de llamada cesa de inmediato cuando ves que presiona el botón de colgar."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¡Te he dicho que me dieras el móvil!"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Para qué?"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Ya no la necesitamos."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "¡¿No crees que tengo algo que decir al respecto?!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Además,"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "¡¿qué crees que hará si ve que no respondo?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Piensas que vendrá hasta aquí?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Y qué demonios harías tú?"

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Dame el móvil."

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx001
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "No."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Dídac."

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "down01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    ono "RIIIIING"

    menu:

        pt "Tiene que ser Neus de nuevo."

        "<Abalanzarte encima de él para quitarle el móvil>":
            call p_Help
            jump night05_DidacHome_DidacOverHerPhone

        "...":
            call p_Help
            #$pl.ch_pts("dp",1)

            $ df_eye = "down04"
            show didacf_mouth happy_Silentx03
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            n "Dídac hace un gesto con el dedo y cesa el sonido de la llamada."

            $ df_eye = "front05"
            show didacf_mouth happy_Talkingx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "Así me gusta."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            p "¿Crees que eso es una buena idea?"

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "¿A qué te refieres?"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            p "¿Qué harías tú si hubiéramos quedado en un sitio"

            $ df_eye = "right02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            p "y vieras que no te respondo al teléfono?"

            $ df_eye = "right05"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx04
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "¿Crees que vendrá hasta aquí?"

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            p "Es lo que yo haría."

            $ df_eye = "front02"
            show didacf_mouth sad_Talkingx06
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "Entonces llámala y dile que no venga."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "..."

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "Bueno, si no lo haces tú ya lo haré yo."

            $ df_eye = "down03"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with disslove

            p "¡Dídac!"

            $ df_eye = "down04"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "down05"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            n "Ves que frunce el ceño mirando el móvil"

            $ df_eye = "down05"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            n "como si estuviera haciendo un esfuerzo mayúsculo."

            $ df_eye = "down03"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            pt "¿Qué le pasa?"

            $ df_eye = "down04"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "Tssk..."

            $ df_eye = "down01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡¿Qué cojones?!"

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "Si quieres llamarla solo tienes que pulsar rellamada..."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Ya lo sé!"

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "¿Y por qué no lo haces?"

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡No puedo!"

            $ df_eye = "down04"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "..."

            $ df_eye = "down01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡¿Por qué coño no puedo?!"

            $ df_eye = "down04"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            p "..."

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            p "No sé si ha sido una buena idea ignorar su llamada."

            $ df_eye = "down03"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "right04"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "Tssk..."

            $ df_eye = "front08"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            n "Ves que lanza el móvil por la habitación."

            $ df_eye = "left04"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows angryx02
            call dfeye_lab
            with hpunch

            d "Como si me importara."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            p "¡Tío!"

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "¡Que es mi puto móvil!"

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "left03"
            show didacf_mouth happy_Talkingx02
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            d "Vale,"

            $ df_eye = "front06"
            show didacf_mouth happy_Talkingx04
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "quizás eso no venía a cuento..."

            $ df_eye = "right01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Pero es que me he puesto de los nervios, joder!"

            $ df_eye = "right04"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "..."

            $ df_eye = "front08"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "..."

            jump night05_DidacHome_DidacLookingDown
                # n "Ves que su mirada se fija de nuevo en tu entrepierna."
                # p "..."
                # d "..."
                # p "¡¿En serio no puedes pensar en otra cosa?!"
                # d "¡Eres tú el que la tiene tiesa como una piedra!"

label night05_DidacHome_DidacOverHerPhone:

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    pause 0.2

    scene black
    with vpunch

    n "Te abalanzas sobre ella"

    n "y con cierto forcejeo consigues arrebatarle el teléfono."

    scene beds_night_lightOff_blindUp_DemptyMCmessy

    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows sadx01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright_closex2

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx03
    call dfeye_lab
    with fade

    d "No hacía falta que fueras tan bruto."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    p "Es lo que te has buscado."

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    n "Respondes la llamada."

    jump night05_DidacHome_AnswerCall

label night05_DidacHome_AnswerCall:

    scene beds_night_lightOff_blindUp_DemptyMCmessy

    show morning04_bg_livingroom_mc_resting_phone neus_calling:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with fade

    p "¿Sí...?"

    ne "[protname],"

    ne "eres tú?"

    p "Sí,"

    extend " soy yo."

    ne "Son las nueve de la noche,"

    ne "recuerdas que aún nos queda la última cita,"

    ne "¿verdad?"

    p "Hmm..."

    ne "¿O es que no piensas venir?"

    menu:

        pt "Acudir a la última cita con Neus..."

        "Lo siento Neus, pero no acudiré a nuestra última cita.":
            call p_Help
            $pl.ch_pts("np",-10)

            jump night05_DidacHome_tellNeusYouWontGo

        "Siento el retraso, ahora mismo vengo.":
            call p_Help

            $pl.ch_pts("dp",-7)

            n "Oyes un profundo suspiro por el otro lado de la línea."

            d "¡¿Qué?!"

            ne "Me alegra oír eso."

            p "Nos vemos."

            scene beds_night_lightOff_blindUp_DemptyMCmessy
            with Dissolve(0.5)

            n "Antes de que Dídac tenga tiempo de decir alguna estupidez"

            scene beds_night_lightOff_blindUp_DemptyMCmessy

            show didacfbodybelow_naked_drops 00:
                dfbody_atright_closex2
            show didacfhandr leg_naked:
                dfbody_atright_closex2
            show didacfbodytop_naked_drops 00:
                dfbody_atright_closex2
            show didacfhandl hip_naked:
                dfbody_atright_closex2
            show didacf_blush 03:
                dfexpressions_atright_closex2
            show didacf_eyes 05:
                dfexpressions_atright_closex2
            show didacf_pupils front05:
                dfexpressions_atright_closex2
            show didacf_eyebrows sadx01:
                dfexpressions_atright_closex2
            show didacfbodytop_hair:
                dfbody_atright_closex2
            show didacf_mouth happybiting_Silentx04:
                dfexpressions_atright_closex2

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            n "cuelgas la llamada."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx004
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "Estás de coña,"

            extend " ¡¿Verdad?!"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            p "No,"

            extend " no estoy de broma."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            p "No estás bien Dídac"

            $ df_eye = "front03"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "y la única forma de ayudarte"

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            p "es acudir a la última cita con Neus."

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx09
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡¿Es que no me has oído cuando te he dicho que seguramente ya me has dejado preñada?!"

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "Eso no lo sabes con seguridad."

            $ df_eye = "front02"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            p "Y en cualquier caso,"

            $ df_eye = "front03"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            p "no es buena idea hacer enfadar a alguien con semejante poder."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            n "Su rostro es de todo menos alegre."

            $ df_eye = "front08"
            show didacf_mouth sad_Silentx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            p "Entiéndelo."

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡No!"

            $ df_eye = "front00"
            show didacf_mouth sad_Talkingx09
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡No lo entiendo!"

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡Ya no la necesitamos!"

            $ df_eye = "front03"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            p "¡Dídac!"

            $ df_eye = "right04"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "right05"
            show didacf_mouth sad_Silentx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            p "Por favor."

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            p "Solo te pido esta noche."

            $ df_eye = "front08"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            p "¿Eres capaz de comportarte hasta mañana?"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "¿O tengo que buscarte una niñera?"

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡¿Por quién me tomas?!"

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            p "Responde."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx005
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "No haré ninguna estupidez ni saldré de casa"

            $ df_eye = "right01"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "si es eso lo que te preocupa."

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            p "¿Me lo prometes?"

            $ df_eye = "front02"
            show didacf_mouth sad_Talkingx05
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡Que sí!"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "No te he oído prometerlo."

            $ df_eye = "front08"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡Te lo prometo, joder!"

            $ df_eye = "front01"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡¿Contento?!"

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            if p_prot_analgesic == "accepted":

                menu:

                    pt "También podría usar lo que me dio esa rubia para asegurarme..."

                    "<Drogarla y luego atarla en la cama>":
                        call p_Help

                        call WIP

                        # NOT_FINISHED

                    "...":
                        call p_Help
                        pass

            else:

                pt "Supongo que tendré que fiarme de su palabra."

            $ df_eye = "front04"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            pause 0.2

            scene afternight03_bg_hallway_day
            with fade

            n "Te diriges al baño para acicalarte"

            n "mientras Dídac te lanza una mirada no demasiado amistosa."

            scene bg an04_flat_gate_composition002:
                subpixel True
                truecenter
                zoom 0.5 xpos 0.25 ypos -0.3 #General view door.
                ease 20.0 zoom 1.5 xpos -0.9 ypos -2.3
            with fade

            n "Poco después te preparas para ir a buscar el metro"

            n "que te lleva dónde te está esperando la morenita de ojos verdes."

            $ night05_DidacHome_NeusLate_Cond = True

            jump night05_NeusLastDate


label night05_DidacHome_tellNeusYouWontGo:

    ne "..."

    ne "¿Qué...?"

    ne "¿Por-"

    extend "por qué?"

    menu:

        pt "¿Por qué?"

        "<Decirle que no hace falta porque Dídac ya no quiere volver a ser un hombre>":
            # $pl.ch_pts("dp",1)
            # $pl.ch_pts("np",-1)

            p "Euuhh..."

            ne "¿[protname]?"

            n "Usas todas tus fuerzas para poder comunicárselo,"

            p "Buehg..."

            n "pero lo único que consigues es balbucear cosas sin sentido."

            ne "..."

            pt "¡¿En serio?!"

            pt "¡¿Por qué diablos no le puedo decir la verdad?!"

            ne "¿Estás bien?"

            p "..."

            p "Lo lamento,"

            p "pero no voy a venir."

        "...":

            ne "Dime algo,"

            extend " por favor."

    jump night05_DidacHome_NeusYoureAtHome


label night05_DidacHome_NeusYoureAtHome:

    ne "..."

    ne "Estás en casa,"

    extend " ¿verdad?"

    p "..."

    ne "Ahora vengo."

    p "Neus,"

    extend " yo..."

    show morning04_bg_livingroom_mc_resting_phone neus
    with dissolve

    ono "pip-pip"

    scene beds_night_lightOff_blindUp_DemptyMCmessy
    with Dissolve(0.5)

    n "Oyes ese particular sonido después de que te cuelguen la llamada."

    scene beds_night_lightOff_blindUp_DemptyMCmessy

    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows sadx01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright_closex2

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows serious
    call dfeye_lab
    with Dissolve(0.25)

    d "¿Qué ha dicho?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "Que ahora viene."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Cómo que ahora viene?"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Pero si le has dicho que no quieres ir!"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Por qué no le has dicho la verdad?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Por que no puedo."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿Qué quieres decir que no puedes?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Por alguna razón soy incapaz de decírselo."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Dame el maldito teléfono y ya se lo diré yo!"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    $ night05_DidacHome_DidacPhoneGrab_Cond = False

    menu:

        pt "Que se lo diga Dídac..."

        "No creo que sea buena idea.":
            call p_Help

            $ night05_DidacHome_DidacPhoneGrab_Cond = True

            $ df_eye = "front02"
            show didacf_mouth sad_Talkingx08
            show didacf_eyebrows angryx03
            call dfeye_lab
            with dissolve

            d "¡¿Y puedo saber por qué no?!"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            p "No creo que se lo tome demasiado bien."

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx09
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡No me seas nenaza!"

            scene beds_night_lightOff_blindUp_DemptyMCempty_blur03
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

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx03
            call dfeye_lab
            with hpunch

            n "Con un rápido gesto te roba el móvil."

            $ df_eye = "down02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            p "¡Dídac!"

        "<Darle el teléfono>":
            call p_Help

            scene beds_night_lightOff_blindUp_DemptyMCempty_blur03
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

            $ df_eye = "front05"
            show didacf_mouth happy_Silentx02
            show didacf_eyebrows angryx01
            call dfeye_lab
            with Dissolve(0.5)

            p "Toma."

            $ df_eye = "down02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            pause 0.2

    $ df_eye = "down04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    n "Se queda mirando el móvil que tiene en las manos."

    $ df_eye = "down01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    if night05_DidacHome_DidacPhoneGrab_Cond:

        $ df_eye = "down05"
        show didacf_mouth sad_Silentx08
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        p "¿Qué ocurre?"

        $ df_eye = "down04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "down05"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "down05"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        p "Solo tienes que hacer rellamada."

        $ df_eye = "front04"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "¡Ya lo sé!"

        $ df_eye = "down02"
        show didacf_mouth sad_Silentx07
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "¿Y entonces por qué no lo haces?"

        $ df_eye = "front01"
        show didacf_mouth sad_Talkingx09
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "¡¿Y qué te crees que estoy intentando hacer?!"

        $ df_eye = "down05"
        show didacf_mouth sad_Silentx08
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

    p "¿Tampoco puedes?"

    $ df_eye = "down05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "No,"

    extend " no puedo..."

    $ df_eye = "down03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡¿Qué cojones está pasando?!"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "No lo sé."

    $ df_eye = "down04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "Pero por alguna razón hay algo que nos impide decirle la verdad."

    $ df_eye = "down05"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¿En serio va a venir?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "Eso creo."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "Supongo que quiere verlo con sus propios ojos,"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "o..."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿O qué?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "No creo que esté muy contenta."

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Tssk..."

    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "Como si me importara su opinión."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Fue ella la que te convirtió en mujer."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    d "¿Y?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Pues que ella puede volver a convertirte en hombre."

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "O incluso hacernos algo peor..."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿Cómo qué?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "¡No lo sé Dídac!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "¡Simplemente digo que no es muy inteligente hacer enfadar a alguien con estos poderes!"

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    jump night05_DidacHome_DidacLookingDown

###

label night05_DidacHome_DidacLookingDown:

    $ df_blush += 1

    $ df_eye = "down03"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "Ves que su mirada se fija de nuevo en tu entrepierna."

    $ df_eye = "down04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    pause 0.2

    $ df_eye = "down05"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¡¿En serio no puedes pensar en otra cosa?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Eres tú el que la tiene tiesa como una piedra!"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "¡Porque me estoy meando!"

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Pues vete a mear!"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Pero luego vuelves aquí."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Es que no te das cuenta de la situación?"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Claro que me doy cuenta!"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡¿Pero qué quieres hacer?!"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Podríamos ir a un hotel e intentar escondernos de ella..."

    $ df_eye = "right02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Hmmm..."

    $ df_eye = "right03"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Quizás no es tan mala idea."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "¿Pero hasta cuándo?"

    $ df_eye = "front03"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "A duras penas nos queda algo en el banco,"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "especialmente desde que tú no trabajas."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Me dijiste que no me lo volverías a echar en cara."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¡Estoy exponiendo la situación!"

    $ df_eye = "down05"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Por lo que me ha dicho,"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "creo que sabe que me gano la vida en el gimnasio"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "y entrenando a esos chicos."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "Con lo cual tampoco podríamos escondernos de ella durante mucho tiempo"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "y lo más probable es que no se tome muy bien"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "el que hayamos intentado escondernos de ella..."

    $ df_eye = "down05"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "down05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    pt "¡Así no puedo pensar con claridad!"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    pause 0.2

    scene morning04_bg_bedroom_youleaving 01
    with fade

    n "Te diriges a la puerta de la habitación."

    d "¡¿A dónde vas ahora?!"

    p "¡Ya te he dicho que me estoy meando!"

    d "¡Vale,"

    extend " vale!"

    scene morning04_bg_bedroom_youleaving 02
    with dissolve

    d "Quizás tenga que ir yo después."

    jump night05_DidacHome_MCpissing

label night05_DidacHome_MCpissing:

    scene night05_bg_tibidabo_bathroom_toilet:
        subpixel True
        truecenter
        zoom 2.0 ypos -0.3 #Down
        easein_quad 50.0 zoom 1.8 ypos 1.0 # Up?
    with fade

    pt "¿Y ahora qué?"

    pt "Lo de ir a un hotel es una pésima idea."

    pt "Lo mejor será enfrentarme a ella con la verdad."

    pt "Pero..."

    pt "¿Seguro que es una buena idea?"

    ono "neeec"

    n "Oyes la puerta del baño abriéndose."

    p "¡Dídac!"

    p "¡Que estoy meando, joder!"

    d "Como si fuera la primera vez que te veo en pelotas."

    p "Hmm..."

    d "¿Tienes para mucho?"

    p "¿Acaso no lo oyes?"

    d "Vale,"

    extend " vale..."

    d "ya me espero."

    p "..."

    p "Por cierto."

    d "¿Qué?"

    p "A ver si meas sentada,"

    p "que tu puntería ya no es lo que era."

    d "Tsssk..."

    d "¡Solo lo hice una vez"

    d "y fue para intentar ver si podía!"

    p "¡Pero al menos lo podrías haber limpiado mejor!"

    p "¡Lo limpié!"

    p "¡Pero no con productos de limpieza,"

    p "que el baño es muy pequeño y cerrado!"

    d "Vale,"

    extend " vale..."

    d "Ya aprendí la lección,"

    d "no lo volveré hacer."

    p "..."

    d "Aunque,"

    d "quizás es cuestión de práctica..."

    p "¡No seas tan guarra, joder!"

    n "Una sutil sonrisa se dibuja en sus labios."

    p "¿Hmmm...?"

    p "¿Qué pasa ahora?"

    d "Cada vez usas más el femenino para referirte a mí."

    p "..."

    d "Pedazo de meada que estás pegando, ¿no?"

    pt "Y uno aquí con la esperanza de que llegue a cambiar..."

    jump night05_DidacHome_backToRoom


label night05_DidacHome_backToRoom:

    scene beds_night_lightOff_blindUp_DemptyMCmessy
    with fade

    n "Vuelves a tu habitación y te dispones a recoger tus cosas del suelo."

    n "A medida que te vas vistiendo le echas un ojo al móvil."

    show morning04_bg_livingroom_mc_resting_phone neus:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with Dissolve(0.5)

    pt "No me ha vuelto a llamar."

    pt "¿Qué se supone que tenemos que hacer ahora?"

    scene beds_night_lightOff_blindUp_DemptyMCmessy
    with Dissolve(0.5)

    n "Justo cuando estás abrochándote el último botón de la camisa."

    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows sadx01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright_closex2

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with Dissolve(0.25)

    d "¡¿Se puede saber qué estás haciendo?!"

    
    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "Creo que es obvio."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Pues no."

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Ya te puedes estar quitando la ropa."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "Dídac,"

    extend " no me jodas."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "Neus está a punto de llegar y tenemos que decidir..."

label night05_DidacHome_NeusArrive:

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with hpunch

    ono "RIIIIING"

    $ df_eye = "right01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    n "El timbre de la puerta del piso resuena en todo el apartamento."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Es ella?"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¿Es que esperas otra visita?"

    $ df_eye = "right03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    pause 0.2

    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade

    p "Te diriges a la entrada y recoges el interfono que está al lado de la puerta."

    p "¿Sí...?"

    ne "Baja."

    p "Neus,"

    extend " yo..."

    ne "Baja,"

    extend " por favor."

    p "..."

    show didacfbodybelow_naked_drops 00:
        df_body_ontheleftInverted_close
    show didacfhandr leg_naked:
        df_body_ontheleftInverted_close
    show didacfbodytop_naked_drops 00:
        df_body_ontheleftInverted_close
    show didacfhandl hip_naked:
        df_body_ontheleftInverted_close

    show didacf_blush 03:
        df_exp_ontheleftInverted_close
    show didacf_eyes 05:
        df_exp_ontheleftInverted_close
    show didacf_pupils front05:
        df_exp_ontheleftInverted_close
    show didacf_eyebrows sadx01:
        df_exp_ontheleftInverted_close
    show didacfbodytop_hair:
        df_body_ontheleftInverted_close
    show didacf_mouth happybiting_Silentx04:
        df_exp_ontheleftInverted_close

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx01
    call dfeye_lab
    with Dissolve(0.25)

    d "¿Qué te ha dicho?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Espera aquí."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Qué?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    pause 0.2

    scene bg an04_flat_outside
    with fade

    $ neyesp = "True"
    $ ntlong = 3

    n "Cierras la puerta al salir"

    n "y decides coger el ascensor."

    scene bg an04_flat_gate_composition003:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.0 ypos 0.0
        easein_quad 10.0 zoom 0.5 xpos 0.25 ypos -0.3 #General view door.

        
    with fade

    n "Al llegar a la planta baja, a través del cristal,"

    n "ves la figura de Neus esperándote tras el portal que da a la calle."

    show bg an04_flat_gate_composition003:
        ease 10.0 zoom 1.5 xpos -0.9 ypos -2.3

    window hide dissolve
    pause

    n "Suspiras con profundidad y con aparente paso seguro te desplazas hasta ahí."

    $ saturation_tint_level = "default"
    scene neus_comp_001:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -2.6 # Bottom
        ease 18.0 zoom 0.7 xpos 0.48 ypos 0.45 # Face
    with fade

    n "Al abrir la puerta"

    n "ves a Neus con un vestido distinto,"

    n "mucho más revelador que la noche anterior,"

    n "con un maquillaje oscuro en sus párpados"

    n "y con los ojos húmedos,"

    # show neus_exp_mouth sadbiting_Silentx07
    # show neus_exp_eyebrows sadx05
    # $ nteye = "front05"
    # call n_closefromup_tears_tears
    # with fade

    n "mirándote con un rostro entre la ira y la incomprensión."

    window hide dissolve
    pause

    #scene bg an04_flat_gate_back_alone
    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3
    $ Pedrera_char_Cond = "NeusFarRight"

    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with fade

    ne "¿Puedo saber por qué no has venido?"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "Yo..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Tan-"

    extend "tanto asco te doy?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Acaso dije algo que te molestara?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "Algo que me molestara..."

        "No, no es eso.":
            call p_Help
            $pl.ch_pts("np",1)

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx02
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Entonces?"

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx04
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

        "Tampoco es que fueras tan agradable.":
            call p_Help
            $pl.ch_pts("np",-3)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows sadx01
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ ntlong += 1

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front05"
            call n_closefromup_tears_tears
            with dissolve

    p "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pe-"

    if pl.np > 100:

        extend "pensé que sentías algo por mí..."

    elif pl.np > 50:

        extend "pensé que no lo habías pasado tan mal."

    else:

        extend "pensé que..."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "left03"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    if night04_pedrera_blowjob_DONE:

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Fue por lo de ayer?"

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx02
        $ nteye = "right03"
        call n_closefromup_tears_tears
        with dissolve

        ne "Sabía que no tendría que habértelo hecho,"

        show neus_exp_mouth sad_Talkingx002
        show neus_exp_eyebrows sadx03
        $ nteye = "right05"
        call n_closefromup_tears_tears
        with dissolve

        ne "aunque fuera en la oscuridad..."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "Esos ojos y esa lengua..."

            "No, no es eso.":
                call p_Help
                $pl.ch_pts("np",1)

                show neus_exp_mouth sad_Silentx02
                show neus_exp_eyebrows serious
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                show neus_exp_mouth sad_Talkingx003
                show neus_exp_eyebrows sadx02
                $ nteye = "front03"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Entonces por qué?"

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

            "La verdad es que fue algo desagradable.":
                call p_Help
                $pl.ch_pts("np",-3)

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_eyebrows sadx01
                $ nteye = "front01"
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                $ ntlong += 1

                show neus_exp_mouth sad_Talkingx04
                show neus_exp_eyebrows sadx03
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                ne "Si es por eso te prometo que no lo volveré a hacer."

                show neus_exp_mouth sadbiting_Silentx06
                show neus_exp_eyebrows sadx04
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

            "...":
                call p_Help
                $pl.ch_pts("np",-1)
                pass

    pt "¡JODER!"

    pt "¡¿Por qué cojones no le puedo decir la verdad?!"

    jump night05_DidacHome_NeusDidacAppear

###

label night05_DidacHome_NeusDidacAppear:

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    d "¡No ha ido a vuestra última cita porque ya no hace falta!"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    pt "¡Dídac!"

    if DidacPregnant:
        $ df_blush = 1
    else:
        $ df_blush = 3

    scene didacf_comp_001:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -1.9 # Bottom
        ease 18.0 zoom 0.7 xpos 0.48 ypos 0.45 # Face
            ## zoom 0.2 ypos 0.2 # General
    with fade

    n "Al girarte ves a tu compañera de piso"

    ## CONDITIONAL if you saw her with that cloth... is that possible to get here without getting there?

    n "con esa lencería verde y con forma gatuna"

    n "que te mostró en esa tienda de ropa"

    n "saliendo de la puerta del ascensor."

    if not DidacPregnant:

        pt "¿Por qué está sudando?"

    window hide dissolve
    pause

    #scene bg an04_flat_gate_back_alone
    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ df_eye = "left03"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with fade

    ne "¿Qué...?"

    $ df_eye = "left04"
    show didacf_mouth happy_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Qué quieres decir...?"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Por qué coño aparece con esta ropa interior?!"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows serious
    $ nteye = "left00"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¡¿Es que no es obvio?!"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "No hace falta que vaya"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "left00"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "porque no quiero volver a ser hombre."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    ne "[protname]..."

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    ne "¿qué-"

    extend "qué...?"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Soy yo quien te está hablando!"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows serious
    $ nteye = "front02"
    call n_closefromup_tears_tears

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Dídac,"

    extend " no lo empeores."

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¿Que no lo empeore?!"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows surprisex01
    $ nteye = "left00"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡Fue ella la que me convirtió en lo que soy!"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left02"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Así que como mínimo que no se haga la jodida víctima!"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left04"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿Me equivoco?!"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    ne "¿Qué...?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    ne "¿Qué habéis hecho?"

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "..."

    if DidacPregnant:

        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyebrows sadx01
        $ nteye = "left04"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth happy_Talkingx04
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Para empezar,"

        show neus_exp_mouth sadbiting_Silentx01
        show neus_exp_eyebrows surprisex02
        $ nteye = "left00"
        call n_closefromup_tears_tears

        $ df_eye = "left04"
        show didacf_mouth happy_Talkingx05
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "me ha dejado preñada."

        show neus_exp_mouth sad_Talkingx09
        show neus_exp_eyebrows surprisex01
        $ nteye = "front00"
        call n_closefromup_tears_tears

        $ df_eye = "left05"
        show didacf_mouth happy_Silentx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        ne "¡¿Qué?!"

        show neus_exp_mouth sad_Silentx05
        show neus_exp_eyebrows surprisex01
        $ nteye = "left00"
        call n_closefromup_tears_tears

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx004
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        d "Si lo que dijiste es cierto,"

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows suspiciousx01
        $ nteye = "left01"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth happy_Talkingx05
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "ya no puedes hacer nada para que vuelva a ser lo que era."

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears

        $ df_eye = "left03"
        show didacf_mouth happy_Silentx05
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "..."

        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyebrows normal
        $ nteye = "left01"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx06
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Así que ya no tienes nada con qué hacerle chantaje."

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front02"
        call n_closefromup_tears_tears

        $ df_eye = "left04"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx01
        $ nteye = "front01"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        ne "¿Eso es verdad?"

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx03
        $ nteye = "front02"
        call n_closefromup_tears_tears

        $ df_eye = "front08"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        p "..."

        show neus_exp_mouth sad_Silentx06
        show neus_exp_eyebrows angryx01
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Talkingx09
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "¡Pues claro que es verdad!"

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex01
        $ nteye = "front00"
        call n_closefromup_tears_tears

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        p "Aún no es seguro Dídac."

        show neus_exp_mouth sad_Silentx08
        show neus_exp_eyebrows angryx02
        $ nteye = "front01"
        call n_closefromup_tears_tears

        $ df_eye = "right04"
        show didacf_mouth sad_Silentx07
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "..."

    else:

        # CONDITIONAL # Morning sex and beach sex are left yet... m6_d is not necessary.

        if ((afternight04__Pussy_dick_med_Success > 0 or
            "vaginal_doneOrReceived?" in af5_d._sexActions
            )
            or 
            (afternight04__Anal_dick_med_Success > 0 or
            "anal" in af5_d._sexActions
                )):

            if ((afternight04__Pussy_dick_deep_Success > 0 or
                "vaginalDeep" in af5_d._sexActions
                )
                and 
                (afternight04__Anal_dick_deep_Success > 0 or
                "analDeep" in af5_d._sexActions
                    )):

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_eyebrows surprisex02
                $ nteye = "left00"
                call n_closefromup_tears_tears

                $ df_eye = "left01"
                show didacf_mouth happy_Talkingx06
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "¡Me ha follado hasta el fondo por delante y por detrás!"

            elif ((afternight04__Pussy_dick_med_Success > 0 or
                "vaginal" in af5_d._sexActions
                )
                and
                (afternight04__Anal_dick_med_Success > 0 or
                "anal" in af5_d._sexActions
                    )):

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyebrows surprisex01
                $ nteye = "left01"
                call n_closefromup_tears_tears

                $ df_eye = "left01"
                show didacf_mouth happy_Talkingx05
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "¡Me ha follado por delante y por detrás!"

            else:

                show neus_exp_mouth sadbiting_Silentx03
                show neus_exp_eyebrows surprisex01
                $ nteye = "left01"
                call n_closefromup_tears_tears

                $ df_eye = "left01"
                show didacf_mouth happy_Talkingx05
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "Me ha follado hasta decir basta."

            if (afternight04__Pussy_dick_med_Success == 0 and
            "vaginal" not in af5_d._sexActions
                ):

                show neus_exp_mouth sadbiting_Silentx04
                show neus_exp_eyebrows surprisex01
                $ nteye = "left01"
                call n_closefromup_tears_tears

                $ df_eye = "left04"
                show didacf_mouth sad_Talkingx004
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "Aunque solo hay sido por detrás..."

            if (afternight04__MMouth_dick_Success > 0 or
                "blowjob" in af5_d._sexActions
                ):

                show neus_exp_mouth sadbiting_Silentx02
                show neus_exp_eyebrows surprisex02
                $ nteye = "left00"
                call n_closefromup_tears_tears

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx004
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "¡Si hasta me la ha metido por la garganta!"

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx01
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "De hecho,"

        show neus_exp_mouth sadbiting_Silentx01
        show neus_exp_eyebrows surprisex02
        $ nteye = "left00"
        call n_closefromup_tears_tears

        $ df_eye = "left04"
        show didacf_mouth happy_Talkingx04
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "es muy probable que ya esté embarazada."

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows surprisex01
        $ nteye = "front01"
        call n_closefromup_tears_tears

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "¡Eso no es verdad Dídac!"

        show neus_exp_mouth sadbiting_Silentx07
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears

        $ df_eye = "right04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "..."

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx03
        $ nteye = "front08"
        call n_closefromup_tears_tears

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "¡Siempre he usado condón!"


    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "front02"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    ne "¿Ha-"

    extend "habéis follado?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¡Pues claro que sí!"

    if DidacPregnant:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¡¿Cómo si no me habría quedado embarazada?!"

    else:

        show neus_exp_mouth sadbiting_Silentx05
        show neus_exp_eyebrows sadx02
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¿Para qué habríamos usado los condones si no?"

        show neus_exp_mouth sadbiting_Silentx03
        show neus_exp_eyebrows sadx01
        $ nteye = "left01"
        call n_closefromup_tears_tears

        $ df_eye = "front02"
        show didacf_mouth sad_Talkingx003
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "De hecho habría que ir a comprar una nueva"

        show neus_exp_mouth sadbiting_Silentx02
        show neus_exp_eyebrows surprisex01
        $ nteye = "left00"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth happy_Talkingx04
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "porque creo que estamos a punto de terminarla..."

        show neus_exp_mouth sadbiting_Silentx06
        show neus_exp_eyebrows sadx01
        $ nteye = "front00"
        call n_closefromup_tears_tears

        $ df_eye = "left04"
        show didacf_mouth happy_Silentx05
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        ne "..."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¡A diferencia de lo que dicen otras,"

    show neus_exp_mouth sadbiting_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "left00"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "yo no violo a la gente!"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    pt "Bueno,"

    extend " eso es discutible..."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    ne "Pe-"

    extend "pero..."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    ne "No..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    $ nteye = "right04"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    ne "No es posible..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows serious
    $ nteye = "left02"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Pues claro que es posible!"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front03"
    call n_closefromup_tears_tears

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "¡Dídac!"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "¡¿Te quieres callar?!"

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front07"
    call n_closefromup_tears_tears

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "..."

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows sadx06
    $ nteye = "front06"
    call n_closefromup_tears_tears

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Tssk..."

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx04
    $ nteye = "right01"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    ne "E-"

    extend "esto no..."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left02"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    ne "Dídac no debería sentir atracción por ti,"

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "down04"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    ne "anulé su libido por completo."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx07
    $ nteye = "down05"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    ne "Esto no es lo que..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx07
    $ nteye = "front06"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab

    show bg an04_flat_gate_back_blur

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows normal
    $ nteye = "right00"
    call n_closefromup_tears_tears
    with fade

    ne "A menos que..."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    p "¿A menos que qué?"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Papá..."

    show neus_exp_mouth sad_Silentx10
    show neus_exp_eyebrows angryx03
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Papá?"

    show neus_exp_mouth sad_Talkingx08
    show neus_exp_eyebrows angryx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "Me ha encontrado."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows angryx02
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "¿De qué estás hablando?"

    show neus_exp_mouth sad_Talkingx09
    show neus_exp_eyebrows angryx03
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¡¿Por qué no me habías dicho nada sobre Dídac?!"

    show neus_exp_mouth sad_Silentx10
    show neus_exp_eyebrows angryx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    show neus_exp_mouth sad_Talkingx002
    show neus_exp_eyebrows normal
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "No podías,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿verdad?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows angryx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero aún así..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows angryx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Por mucho que te hubiera insistido,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "por muy caliente que te haya puesto..."

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "No me esperaba esto."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "No de ti..."

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx06
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "¿No de mí?"

        "No es lo que parece.":
            call p_Help
            $pl.ch_pts("dp",-3)
            $pl.ch_pts("np",-1)

            scene bg an04_flat_gate_composition002:
                truecenter
                zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

            if not DidacPregnant:
                show didacfbodybelow_naked_drops 01:
                    df_body_atleft
                show didacfbodybelow_naked_wet 01:
                    df_body_atleft
                show didacfbodybelow_panties green:
                    df_body_atleft
                show didacfhandr_leg_naked_drops 01:
                    df_body_atleft
                show didacfbodytop bracat_02:
                    df_body_atleft
                show didacfhandl_hip_naked_drops 01:
                    df_body_atleft
            else:
                show didacfbodybelow_naked_drops 00:
                    df_body_atleft
                show didacfbodybelow_naked_wet 01:
                    df_body_atleft
                show didacfbodybelow_panties green:
                    df_body_atleft
                show didacfhandr_leg_naked_drops 00:
                    df_body_atleft
                show didacfbodytop bracat:
                    df_body_atleft
                show didacfhandl_hip_naked_drops 00:
                    df_body_atleft

            show didacf_blush 03:
                df_exp_atleft
            show didacf_eyes 05:
                df_exp_atleft
            show didacf_pupils front05:
                df_exp_atleft
            show didacf_eyebrows sadx01:
                df_exp_atleft
            show didacfbodytop_hair:
                df_body_atleft
            show didacf_mouth happybiting_Silentx04:
                df_exp_atleft

            $ Pedrera_char_Cond = "NeusFarRight"
            call Pedrera_char_lab

            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx02
            call dfeye_lab

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "left00"
            call n_closefromup_tears_tears
            with dissolve

            d "¿Puedo saber qué es lo que parece?"

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows angryx01
            call dfeye_lab

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows serious
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "¡¿Te quieres callar?!"

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows angryx02
            $ nteye = "front02"
            call n_closefromup_tears_tears
            with dissolve

            ne "No."

            $ Pedrera_char_Cond = "NeusClose"
            call Pedrera_char_lab

            show bg an04_flat_gate_back_blur

            show neus_exp_mouth sad_Talkingx04
            show neus_exp_eyebrows angryx03
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "Dídac tiene razón."

        "Supongo que no me conoces lo suficiente.":
            call p_Help
            $pl.ch_pts("dp",1)

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows surprisex01
            $ nteye = "front00"
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows angryx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            ne "No,"

            $ ntlong += 1

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx06
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            ne "está claro que no."

        "...":
            call p_Help

            show neus_exp_mouth sadbiting_Silentx07
            show neus_exp_eyebrows sadx07
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            pass

##
    
    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows angryx03
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "Eres como él."

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows angryx04
    $ nteye = "right03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Cómo quién?"

    show neus_exp_mouth sad_Silentx08
    show neus_exp_eyebrows angryx03
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    n "Todo su cuerpo tiembla notablemente."

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx09
    show neus_exp_eyebrows angryx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    with dissolve

    n "Abundantes lágrimas brotan por sus mejillas."

    show neus_exp_mouth sad_Silentx10
    show neus_exp_eyebrows sadx06
    $ nteye = "right05"
    call n_closefromup_tears_tears
    with dissolve

    n "Su respiración es convulsa y acelerada."

    show neus_exp_mouth sad_Silentx10
    show neus_exp_eyebrows sadx07
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    $ night05_DidacHome_MCpreference = ""

    menu:

        pt "Parece que le falte el aire..."

        "<Acercar tu mano a su hombro para intentar tranquilizarla>":
            call p_Help

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears
            with dissolve

            p "Neus..."

            if DidacPregnant:

                show neus_exp_mouth sad_Talkingx11
                show neus_exp_eyebrows angryx05
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with hpunch

                ne "¡No me toques!"

                show neus_exp_mouth sad_Silentx08
                show neus_exp_eyebrows angryx04
                $ nteye = "front02"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                show neus_exp_mouth sadbiting_Silentx07
                show neus_exp_eyebrows sadx07
                $ nteye = "right04"
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

            else:

                show neus_exp_mouth sad_Talkingx03
                show neus_exp_eyebrows angryx03
                $ nteye = "front04"
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Por-?"

        "...":
            call p_Help

            pass

    if DidacPregnant:

        jump night05_DidacHome_NeusAbsurd

    else:

        jump night05_DidacHome_NeusEscape


label night05_DidacHome_NeusEscape:

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx05
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Por qué...?"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows sadx02
    $ nteye = "front00"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Acaso prefieres a Dídac?"

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows angryx01
    $ nteye = "front05"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

###

    $ night05_DidacHome_NeusEscape_both = False
    $ night05_DidacHome_NeusEscape_silence = False

    menu night05_DidacHome_NeusEscape_menu:

        pt "¿Si prefiero a Dídac?"

        "<Decirle que la prefieres a ella>":
            call p_Help

            $pl.ch_pts("dp",-5)
            $pl.ch_pts("np", 2)

            show neus_exp_mouth sadbiting_Silentx02
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears

            $ df_eye = "front01"
            show didacf_mouth sad_Silentx06
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

        "La verdad es que os preferiría a las dos." if night05_DidacHome_NeusEscape_both == False:
            call p_Help
            $pl.ch_pts("dp",-1)
            $pl.ch_pts("np",-1)

            $ night05_DidacHome_NeusEscape_both = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows serious
            $ nteye = "front00"
            call n_closefromup_tears_tears
            
            $ df_eye = "front01"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows suspiciousx02
            call dfeye_lab
            with dissolve

            ne "..."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows angryx02
            $ nteye = "front04"
            call n_closefromup_tears_tears
            
            $ df_eye = "front04"
            show didacf_mouth sad_Talkingx003
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            d "Con dos cojones..."

            show neus_exp_mouth sad_Talkingx08
            show neus_exp_eyebrows angryx03
            $ nteye = "front02"
            call n_closefromup_tears_tears

            $ df_eye = "front05"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            ne "¡Esto no es una broma [protname]!"

            show neus_exp_mouth sad_Talkingx06
            show neus_exp_eyebrows angryx02
            $ nteye = "front03"
            call n_closefromup_tears_tears

            $ df_eye = "left02"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows serious
            call dfeye_lab
            with dissolve

            ne "Elige."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows sadx07
            $ nteye = "front04"
            call n_closefromup_tears_tears
            
            $ df_eye = "front04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            jump night05_DidacHome_NeusEscape_menu

        "<Decirle que prefieres estar con Dídac>":
            call p_Help
            $pl.ch_pts("dp",2)
            $pl.ch_pts("np",-8)

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex02
            $ nteye = "front00"
            call n_closefromup_tears_tears
            
            $ df_eye = "front03"
            show didacf_mouth sad_Silentx03
            show didacf_eyebrows serious
            call dfeye_lab
            with dissolve

            p "Sí,"

            show neus_exp_mouth sad_Silentx05
            show neus_exp_eyebrows surprisex01
            $ nteye = "front01"
            call n_closefromup_tears_tears

            $ df_eye = "front00"
            show didacf_mouth sad_Silentx02
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            p "prefiero estar con Dídac."

            show neus_exp_mouth sad_Silentx06
            show neus_exp_eyebrows normal
            $ nteye = "left01"
            call n_closefromup_tears_tears
            
            $ df_eye = "front01"
            show didacf_mouth sad_Silentx01
            show didacf_eyebrows normal
            call dfeye_lab
            with dissolve

            pause 0.2

            $ ntlong += 1

            show neus_exp_mouth sad_Silentx07
            show neus_exp_eyebrows angryx02
            $ nteye = "right02"
            call n_closefromup_tears_tears
            
            $ df_eye = "left02"
            show didacf_mouth happybiting_Silentx04
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            ne "..."

            jump night05_DidacHome_NeusAbsurd

        "..." if night05_DidacHome_NeusEscape_silence == False:
            call p_Help
            $pl.ch_pts("np",-1)

            $ night05_DidacHome_NeusEscape_silence = True

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows surprisex01
            $ nteye = "left00"
            call n_closefromup_tears_tears
            
            $ df_eye = "front03"
            show didacf_mouth sad_Talkingx07
            show didacf_eyebrows angryx04
            call dfeye_lab
            with dissolve

            d "¡Al menos responde a la pregunta!"

            show neus_exp_mouth sadbiting_Silentx05
            show neus_exp_eyebrows sadx02
            $ nteye = "left01"
            call n_closefromup_tears_tears
            
            $ df_eye = "front03"
            show didacf_mouth sad_Silentx05
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            ne "..."

            show neus_exp_mouth sadbiting_Silentx06
            show neus_exp_eyebrows sadx05
            $ nteye = "front04"
            call n_closefromup_tears_tears
            
            $ df_eye = "front04"
            show didacf_mouth sad_Silentx04
            show didacf_eyebrows angryx02
            call dfeye_lab
            with dissolve

            jump night05_DidacHome_NeusEscape_menu

    pause 0.2

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab
    show bg an04_flat_gate_back_blur

    show neus_exp_mouth happy_Talkingx01
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    p "Yo..."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    n "Antes de que seas capaz de decir algo más,"

    show aftermorning04_fr_rape_after_body bracat_blur:
        truecenter
        zoom 1.6 xpos 0.3 ypos 0.4
    show aftermorning04_fr_rape_after_face back_blur:
        truecenter
        zoom 1.6 xpos 0.3 ypos 0.4

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    # scene day05 # Image of Didac in front of you.
    # with fade

    n "ves a Dídac pasando por tu lado acercándose a Neus."

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Hmm...?"

    show aftermorning04_fr_rape_after_body bracat:
        zoom 1.2 xpos 0.45 ypos 0.42
    show aftermorning04_fr_rape_after_face front:
        zoom 1.2 xpos 0.45 ypos 0.42

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows normal
    $ nteye = "left01"
    call n_closefromup_tears_tears
    with dissolve

    n "Sin pizca de vergüenza, arrima sus labios a su oreja"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows suspiciousx01
    $ nteye = "left02"
    call n_closefromup_tears_tears
    with dissolve

    n "mientras te da la sensación que le susurra algo al oído."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows suspiciousx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué...?"

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows angryx01
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué le estás diciendo?"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "left00"
    call n_closefromup_tears_tears
    with dissolve

    n "La expresión de Neus cambia por completo,"

    hide aftermorning04_fr_rape_after_body
    hide aftermorning04_fr_rape_after_face

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows surprisex02
    $ nteye = "left00"
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    n "mientras ves a Dídac retroceder -sin darse la vuelta- para volver a dónde estaba."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows surprisex01
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx09
    show neus_exp_eyebrows sadx06
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    ne "..."

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx10
    show neus_exp_eyebrows angryx05
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx06
    show neus_exp_eyebrows sadx05
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    p "..."

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx05
    $ nteye = "front05"
    call n_closefromup_tears_tears
    with dissolve

    ne "[protname]."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Lamento mucho todo lo que ha pasado."

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Te prometo que nunca había sido mi intención que todo terminara de esta manera."

    show neus_exp_mouth sad_Silentx11
    show neus_exp_eyebrows sadx07
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ ntlong += 1

    show neus_exp_mouth happybiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    n "Una forzada sonrisa se dibuja en su labios con su rostro cubierto de lágrimas."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "De corazón,"

    show neus_exp_mouth happy_Talkingx07
    show neus_exp_eyebrows sadx05
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "espero que podáis llegar a ser felices."

    $ ntlong += 1

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx06
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    n "Sin esperar tu respuesta,"

    scene bg an04_flat_gate_back_blur
    with Dissolve(0.25)

    n "regresa a la calle desapareciendo de tu vista al cruzar el muro del portal."

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ deyesc = "_red"

    $ df_eye = "left05"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab

    with fade_short

    p "¡Neus!{w=0.75}{nw}"

    # scene bg an04_flat_gate_back_alone
    # with fade_short

    scene bg an04_flat_gate_composition002:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus
        easein_quad 5.0 zoom 2.5 xpos -1.45 ypos -3.7 # More close to the middle door
    with dissolve

    $ deyesc = ""

    n "Justo cuando intentas ir tras ella"


    show bg an04_flat_gate_composition002:
        zoom 2.5 xpos -1.45 ypos -3.7
    with hpunch

    n "percibes un fuerte agarrón en ambos hombros por parte de Dídac que te impide avanzar."

    p "¡Dídac!"

    n "Con un veloz y violento amago intentas deshacerte de sus manos,"

    n "algo que suele darte buenos resultados."

    n "Pero esta vez..."

    show morning04_bedroom_DMast_blinkeye
    with vpunch
    p "¡Ugh!"

    n "Sientes sus dedos clavándose con aún más fuerza en tus hombros,"

    pt "¡Pero qué coño?!"

    n "casi como si se hundieran en tu piel."

    p "¡Me estás haciendo daño, joder!"

    n "Su agarrón es tan fuerte que tus piernas flaquean"

    show black
    with vpunch

    n "y terminas cayendo de rodillas al suelo."

    p "¡Suéltame!"

    n "Intentas torcer el cuello para mirarle,"

    n "pero el dolor es tan intenso que eres incapaz de lograrlo."

    p "¡Ugh!"

    hide black
    with fade

    n "Suaviza el agarre, aunque sigue sin soltarte."

    p "¡DÍDAC!"

    hide morning04_bedroom_DMast_blinkeye
    with Dissolve(0.5)

    n "Finalmente te libera."

    p "¡Joder!"

    p "¿A qué coño ha venido esto?!"

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat_02:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 01:
            df_body_ontheleftInverted_close
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 00:
            df_body_ontheleftInverted_close

    show didacf_blush 03:
        df_exp_ontheleftInverted_close
    show didacf_eyes 05:
        df_exp_ontheleftInverted_close
    show didacf_pupils front05:
        df_exp_ontheleftInverted_close
    show didacf_eyebrows sadx01:
        df_exp_ontheleftInverted_close
    show didacfbodytop_hair:
        df_body_ontheleftInverted_close
    show didacf_mouth happybiting_Silentx04:
        df_exp_ontheleftInverted_close

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with Dissolve(0.3)

    d "¿Qué?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Qué coño haces en el suelo?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "¡¿Euh?!"

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "¿Y la enana morenita?"

    $ df_eye = "right01"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¿A dónde ha ido?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¡¿Me estás tomando el puto pelo?!"

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    pause 0.2

    $ df_eye = "front02"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿Ya se ha ido?"

    $ df_eye = "down04"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    pause 0.2

    scene bg an04_flat_gate_back_alone
    with fade_short

    n "Sales a la calle a toda prisa para ver si logras ver por dónde se ha ido."

    d "¡¿A dónde coño vas?!"

    scene bg an04_street_01:
        subpixel True
        truecenter
        zoom 2.0
        ease 15.0 zoom 0.5
    with fade_short

    n "Corres calle abajo en la dirección a la que has visto que se dirigía,"

    n "pero no ves ni rastro de ella por ninguna parte."

    p "Mierda..."

    window hide dissolve
    pause

    scene bg an04_flat_gate_back_alone
    with fade

    n "Resignado, vuelves con Dídac."

    $ saturation_tint_level = "verydark"

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿Qué cojones haces?"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Eso tú."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿Qué coño le has susurrado al oído?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿A quién?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¡¿A quién va a ser?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Yo le he susurrado algo?"

    $ df_eye = "right01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "right02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    pt "Suele tener mucha fuerza,"

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    pt "a veces incluso más que yo,"

    pt "pero el modo en que me ha agarrado de los hombros..."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    pt "Ese no parecía Dídac."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "¿Se ha ido por siempre?"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Eso creo."

    $ df_eye = "front03"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "O sea que por fin estamos libres de esa bruja."

    $ df_eye = "front06"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Te encuentras bien?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Por qué?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Estás sudando bastante."

    $ df_eye = "down02"
    show didacf_mouth sad_Talkingx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Bueno,"

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "quizás me duele un poco la cabeza,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "pero tampoco es nada grave."

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "¿Podemos volver a casa?"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Sí,"

    extend " quizás sea mejor."

    $ df_eye = "front04"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    pause 0.2

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Especialmente teniendo en cuenta cómo vas vestida."

    $ df_eye = "down02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Si a eso se le puede llamar ir \"vestida\"."

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Lo dices como si no te gustara..."

    $ df_eye = "front03"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Miauuuu..."

    $ df_eye = "front04"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¡No hagas eso!"

    $ df_eye = "front05"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "¿Acaso prefieres que ronronee sobre tu polla desnuda?"

    $ df_eye = "down04"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front06"
    show didacf_mouth happy_Silentx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    n "Una dulce sonrisa se dibuja en su rostro."

## Closer
    
    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat_02:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 01:
            df_body_ontheleftInverted_close
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 00:
            df_body_ontheleftInverted_close

    show didacf_blush 03:
        df_exp_ontheleftInverted_close
    show didacf_eyes 05:
        df_exp_ontheleftInverted_close
    show didacf_pupils front05:
        df_exp_ontheleftInverted_close
    show didacf_eyebrows sadx01:
        df_exp_ontheleftInverted_close
    show didacfbodytop_hair:
        df_body_ontheleftInverted_close
    show didacf_mouth happybiting_Silentx04:
        df_exp_ontheleftInverted_close

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    n "Sientes su mano agarrándote de la muñeca para arrastrarte hacia el ascensor."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "No hace falta que me cojas de la mano."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Vale,"

    extend " vale..."

    $ df_eye = "down05"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    scene bg an04_flat_gate_composition002:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus
    with fade

    jump night05_DidacHome_DidacStops
        # n "Sin darte cuenta, vuelves la vista atrás,"
        # n "rememorando ese rostro cubierto de lágrimas a la luz de la farola."
        # with hpunch
        # p "Ugh..."
        # p "¿Por qué te detienes ahora?"

    ## Here Didac comes near to Neus and whispers in her ear. It's daddy telling her to go fuck herself... She leaves in tears without saying a word. and Didac says then... What... what happened? where is Neus?


label night05_DidacHome_NeusAbsurd:

    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab
    show bg an04_flat_gate_back_blur

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears

    # $ df_eye = "left04"
    # show didacf_mouth happy_Silentx03
    # show didacf_eyebrows serious
    # call dfeye_lab
    with Dissolve(0.5)

    ne "No..."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "down04"
    call n_closefromup_tears_tears
    
    # $ df_eye = "left03"
    # show didacf_mouth sad_Silentx03
    # show didacf_eyebrows suspiciousx01
    # call dfeye_lab
    with dissolve

    ne "Tú no..."

    show neus_exp_mouth sad_Talkingx10
    show neus_exp_eyebrows angryx04
    $ nteye = "front07"
    call n_closefromup_tears_tears
    
    # $ df_eye = "left01"
    # show didacf_mouth sad_Silentx02
    # show didacf_eyebrows surprisex01
    # call dfeye_lab
    with dissolve

    ne "¡¿Por qué?!"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows sadx06
    $ nteye = "front06"
    call n_closefromup_tears_tears
    
    # $ df_eye = "left04"
    # show didacf_mouth sad_Silentx04
    # show didacf_eyebrows serious
    # call dfeye_lab
    with dissolve

    ne "¿por qué...?"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front05"
    call n_closefromup_tears_tears
    
    # $ df_eye = "left03"
    # show didacf_mouth sad_Silentx03
    # show didacf_eyebrows serious
    # call dfeye_lab
    with dissolve

    ne "Podía llegar a aceptar que yo no te gustase,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "down04"
    call n_closefromup_tears_tears
    
    # $ df_eye = "left00"
    # show didacf_mouth sad_Silentx02
    # show didacf_eyebrows surprisex01
    # call dfeye_lab
    with dissolve

    if DidacPregnant:

        ne "pero que le hicieras esto a Dídac..."

    else:

        ne "pero que te hayas aprovechado así de Dídac..."

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows surprisex02
    $ nteye = "left01"
    call n_closefromup_tears_tears
    
    $ df_eye = "left04"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with fade_short

    d "Dice la que me usa a modo de chantaje."

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "left02"
    call n_closefromup_tears_tears
    
    $ df_eye = "left03"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    ne "..."

    show neus_exp_mouth sadbiting_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears
    
    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Eso sin mencionar que no me ha obligado a nada."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx04
    $ nteye = "right04"
    call n_closefromup_tears_tears
    
    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Eso que quede claro!"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    pause 0.2

###
    
    $ Pedrera_char_Cond = "NeusClose"
    call Pedrera_char_lab
    show bg an04_flat_gate_back_blur

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows sadx05
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "..."

    $ ntlong += 1

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx04
    $ nteye = "down04"
    call n_closefromup_tears_tears
    with dissolve

    ne "Supongo que es absurdo."

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx05
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "Al fin y al cabo él tenía razón"

    show neus_exp_mouth happy_Talkingx05
    show neus_exp_eyebrows sadx07
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "y Mamá no..."

    $ ntlong += 1

    show neus_exp_mouth sad_Silentx09
    show neus_exp_eyebrows angryx03
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    p "Papá,"

    extend " mamá,"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows angryx02
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué problema tienes con tu familia?"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows angryx03
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    n "Te mira con ojos húmedos y un rostro que muestra una rojiza cólera"

    show neus_exp_mouth sadbiting_Silentx07
    show neus_exp_eyebrows angryx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    n "y al mismo tiempo una profunda tristeza."

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx05
    $ nteye = "right02"
    call n_closefromup_tears_tears
    with dissolve

    ne "La culpa es mía por ser tan estúpida de creer"

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    n "que aún había algo de esperanza."

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx02
    $ nteye = "front06"
    call n_closefromup_tears_tears
    with dissolve

    ne "A pesar de los años,"

    show neus_exp_mouth sad_Talkingx07
    show neus_exp_eyebrows angryx02
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    ne "no aprendo."

    show neus_exp_mouth sad_Silentx07
    show neus_exp_eyebrows angryx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

####
    
    #$ Pedrera_char_Cond = "NeusClose"
    $ Pedrera_char_Cond = "NeusBitClose"
    call Pedrera_char_lab
    show bg an04_flat_gate_back_blur

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with Dissolve(1.0)

    n "Ves que da unos pasos hacia atrás."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "left04"
    call n_closefromup_tears_tears
    with dissolve

    p "..."

#####

    show neus_exp_mouth sad_Talkingx02
    show neus_exp_eyebrows sadx02
    $ nteye = "left03"
    call n_closefromup_tears_tears
    with dissolve

    ne "Dídac."

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    if DidacPregnant:

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows angryx01
        $ nteye = "left01"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "Quiero que seas consciente de algo."

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows serious
        $ nteye = "left02"
        call n_closefromup_tears_tears
        with dissolve

        ne "Aunque te pintes el pelo de otro color,"

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows serious
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "te cambies de nombre,"

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows serious
        $ nteye = "left03"
        call n_closefromup_tears_tears
        with dissolve

        ne "logres falsificar convincentemente tus documentos de identidad"

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows serious
        $ nteye = "left01"
        call n_closefromup_tears_tears
        with dissolve

        ne "o incluso te quemes regularmente la yema de los de dedos."

        # huellas dactilares, huella digital

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows angryx01
        $ nteye = "left02"
        call n_closefromup_tears_tears
        with dissolve

        ne "Siempre cabe la posibilidad de que sufras un accidente"

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx01
        $ nteye = "left03"
        call n_closefromup_tears_tears
        with dissolve

        ne "o simplemente necesites una transfusión de sangre."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "left04"
        call n_closefromup_tears_tears
        with dissolve

        d "¿De qué coño me estás hablando?"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        p "¿No podrá hacerse una transfusión de sangre?"

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "..."

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "Su sangre ya no es enteramente humana,"

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx01
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        ne "y es mejor que eso no lo sepa nadie."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "left02"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows sadx01
        $ nteye = "right02"
        call n_closefromup_tears_tears
        with dissolve

        ne "Si alguien investigara su pasado,"

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "descubriera quien fue y cómo se convirtió en mujer,"

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows serious
        $ nteye = "right01"
        call n_closefromup_tears_tears
        with dissolve

        ne "su vida correría un grave peligro."

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows normal
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        p "Me dijiste que estas criaturas no atacan a mujeres embarazadas."

        show neus_exp_mouth sad_Talkingx005
        show neus_exp_eyebrows angryx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "No atacan sin razón."

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows sadx01
        $ nteye = "front04"
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero en general,"

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears
        with dissolve

        ne "las entes que moran en las sombras del conocimiento humano,"

        show neus_exp_mouth sad_Talkingx004
        show neus_exp_eyebrows sadx01
        $ nteye = "right02"
        call n_closefromup_tears_tears
        with dissolve

        ne "son muy recelosas de su anonimato."

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows serious
        $ nteye = "front01"
        call n_closefromup_tears_tears
        with dissolve

        ne "Si pones en riesgo el secreto de su existencia,"

        show neus_exp_mouth sad_Talkingx08
        show neus_exp_eyebrows angryx01
        $ nteye = "front02"
        call n_closefromup_tears_tears
        with dissolve

        ne "aunque sea mínimamente,"

        if night04_pedrera_blowjob_DONE:

            show neus_exp_mouth sad_Talkingx05
            show neus_exp_eyebrows angryx02
            $ nteye = "front03"
            call n_closefromup_tears_tears
            with dissolve

            ne "no solo deberás preocuparte de los espectros de ojos rojos que viste el otro día."

            show neus_exp_mouth sad_Silentx04
            show neus_exp_eyebrows serious
            $ nteye = "front04"
            call n_closefromup_tears_tears
            with dissolve

            p "¿Te refieres a que hay cosas peores?"

            show neus_exp_mouth sad_Talkingx03
            show neus_exp_eyebrows sadx01
            $ nteye = "right04"
            call n_closefromup_tears_tears
            with dissolve

            ne "No te haces una idea."

            show neus_exp_mouth sad_Silentx02
            show neus_exp_eyebrows serious
            $ nteye = "left04"
            call n_closefromup_tears_tears
            with dissolve

            d "¿Ojos rojos?"

            show neus_exp_mouth sad_Silentx03
            show neus_exp_eyebrows sadx01
            $ nteye = "front08"
            call n_closefromup_tears_tears
            with dissolve

            d "¿De qué mierdas estáis hablando?"

        else:

            show neus_exp_mouth sad_Talkingx003
            show neus_exp_eyebrows angryx01
            $ nteye = "left04"
            call n_closefromup_tears_tears
            with dissolve

            ne "estarás en grave peligro."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx01
        $ nteye = "left04"
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    else:

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows serious
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "Los restos de mi sangre aún tardarán algunas semanas en desaparecer de tu cuerpo,"

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx01
        $ nteye = "front08"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        ne "al menos los que pueden rastrear los humanos;"

        show neus_exp_mouth sad_Talkingx05
        show neus_exp_eyebrows sadx02
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "así que sería mejor que evitaras el hospital durante al menos un mes."

        show neus_exp_mouth sad_Talkingx06
        show neus_exp_eyebrows sadx03
        $ nteye = "left04"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        ne "Si por accidente descubrieran algo que no debieran..."

        show neus_exp_mouth sad_Talkingx07
        show neus_exp_eyebrows sadx01
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left00"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        ne "podrías sufrir una muerte bastante desagradable."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx03
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Talkingx05
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "¡¿Muerte?!"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx04
        $ nteye = "front08"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "..."

        show neus_exp_mouth sadbiting_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "front01"
        show didacf_mouth sad_Talkingx07
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "¿De qué coño está hablando?!"

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx01
        $ nteye = "front02"
        call n_closefromup_tears_tears

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        p "Simplemente no hagas tonterías"

        show neus_exp_mouth sad_Silentx02
        show neus_exp_eyebrows sadx02
        $ nteye = "front03"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "y evita ir al hospital durante un mes."

        show neus_exp_mouth sad_Silentx03
        show neus_exp_eyebrows sadx02
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "Tampoco es tan difícil."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "left04"
        call n_closefromup_tears_tears

        $ df_eye = "right04"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        d "..."

    ##

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    ne "Lo lamento mucho,"

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx01
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    ne "te prometo que no es lo que pensaba que iba a pasar."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx03
    $ nteye = "right02"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    ne "Si pudiera..."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "left02"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Mira tía,"

    show neus_exp_mouth sad_Silentx02
    show neus_exp_eyebrows normal
    $ nteye = "left01"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "me da igual que mierdas te pasó por la cabeza para convertirme en mujer"

    show neus_exp_mouth sad_Silentx01
    show neus_exp_eyebrows surprisex01
    $ nteye = "left00"
    call n_closefromup_tears_tears

    $ df_eye = "left05"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "con la excusa de que te violé."

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx03
    $ nteye = "right03"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡Cuando yo no recuerdo nada de eso!"

    show neus_exp_mouth sadbiting_Silentx05
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx08
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    ne "..."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows serious
    $ nteye = "left02"
    call n_closefromup_tears_tears

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Pero sabes qué?"

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "left03"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Me da igual."

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears

    $ df_eye = "left04"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "En realidad tengo que darte las gracias."

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx03
    $ nteye = "left05"
    call n_closefromup_tears_tears

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Joder..."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "left03"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "¡Nunca había sentido nada parecido!"

    show neus_exp_mouth sad_Silentx04
    show neus_exp_eyebrows sadx01
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿Y ahora dices que quieres volver a convertirme en un hombre?"

    show neus_exp_mouth sad_Silentx06
    show neus_exp_eyebrows sadx03
    $ nteye = "right04"
    call n_closefromup_tears_tears

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx09
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡Ni de puta coña!"

    show neus_exp_mouth sad_Silentx03
    show neus_exp_eyebrows sadx01
    $ nteye = "front02"
    call n_closefromup_tears_tears

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Dídac,"

    scene bg an04_flat_gate_back_blur:
        xzoom -1.0

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat_02:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 01:
            df_body_ontheleftInverted_close
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 00:
            df_body_ontheleftInverted_close

    show didacf_blush 03:
        df_exp_ontheleftInverted_close
    show didacf_eyes 05:
        df_exp_ontheleftInverted_close
    show didacf_pupils front05:
        df_exp_ontheleftInverted_close
    show didacf_eyebrows sadx01:
        df_exp_ontheleftInverted_close
    show didacfbodytop_hair:
        df_body_ontheleftInverted_close
    show didacf_mouth happybiting_Silentx04:
        df_exp_ontheleftInverted_close

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    if night04_pedrera_blowjob_DONE:

        extend " esto es más serio de lo que crees."

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "Estas criaturas de ojos rojos que mencionaba antes no son una broma."

        $ df_eye = "front03"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "Si fueras al hospital"

        $ df_eye = "front03"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "o alguien descubriera tu pasado,"

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "morirías."

    else:

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx04
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "¿eres consciente de lo que estás hablando?"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    p "¿Estás seguro que vale la pena arriesgar tanto por gozar de unos orgasmos?"

    $ df_eye = "front01"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¿unos orgasmos?"

    $ df_eye = "front00"
    show didacf_mouth sad_Talkingx005
    show didacf_eyebrows angryx04
    call dfeye_lab
    with dissolve

    d "¡¿UNOS ORGASMOS?!"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx08
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "No tienes ni puta idea de lo que estás hablando."

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Que sí,"

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "que será una putada y todo eso si no puedo ir al hospital"

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "y si sufro un accidente pues seguramente tendré que buscarme algún veterinario"

    $ df_eye = "right03"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "como en {a=https://en.wikipedia.org/wiki/John_Wick_(film)}John Wick{/a}."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡Pero ni de coña pienso volver a ser un hombre!"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "¡Dídac, joder!"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    p "¡Esto no es una película!"

###
    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ Pedrera_char_Cond = "NeusFarRight"
    call Pedrera_char_lab

    if DidacPregnant:

        show neus_exp_mouth sad_Talkingx02
        show neus_exp_eyebrows sadx02
        $ nteye = "front08"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "En realidad si estás embarazada,"

        ne "ya no puedo hacer nada."

        d "..."

        d "Pues mejor."

        ne "Ten en cuenta que [protname] es el único capaz de darte este placer."

    else:

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows sadx02
        $ nteye = "left02"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        ne "Ten en cuenta de que si te quedaras embarazada"

        show neus_exp_mouth sad_Talkingx04
        show neus_exp_eyebrows sadx03
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex02
        call dfeye_lab
        with dissolve

        ne "[protname] sería el único capaz de darte este placer."

    show neus_exp_mouth sad_Talkingx004
    show neus_exp_eyebrows sadx04
    $ nteye = "front08"
    call n_closefromup_tears_tears

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    ne "Nadie más."

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    ne "Si un día muere o desaparece,"

    show neus_exp_mouth sad_Talkingx06
    show neus_exp_eyebrows serious
    $ nteye = "left03"
    call n_closefromup_tears_tears

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    if DidacPregnant:

        ne "jamás volverás a sentir nada igual."

    else:

        ne "jamás volverías a sentir nada igual."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows sadx01
    $ nteye = "left03"
    call n_closefromup_tears_tears

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "..."

    if not DidacPregnant:

        show neus_exp_mouth sad_Talkingx003
        show neus_exp_eyebrows sadx01
        $ nteye = "front08"
        call n_closefromup_tears_tears

        $ df_eye = "left02"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        ne "Espero que sea cierto y no estés embarazada."

        show neus_exp_mouth sad_Talkingx03
        show neus_exp_eyebrows sadx03
        $ nteye = "left04"
        call n_closefromup_tears_tears

        $ df_eye = "left01"
        show didacf_mouth sadbiting_Silentx03
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        ne "Nunca te he deseado tanto mal."

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "left04"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

    else:

        show neus_exp_mouth sad_Silentx04
        show neus_exp_eyebrows sadx02
        $ nteye = "left03"
        call n_closefromup_tears_tears

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

    pause 0.2

    show neus_exp_mouth sadbiting_Silentx04
    show neus_exp_eyebrows sadx02
    $ nteye = "left04"
    call n_closefromup_tears_tears

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab

    with dissolve

    d "Tsssk..."

###
    
    $ Pedrera_char_Cond = "NeusBitClose"
    call Pedrera_char_lab
    show bg an04_flat_gate_back_blur

    show neus_exp_mouth sad_Talkingx05
    show neus_exp_eyebrows angryx01
    $ nteye = "front02"
    call n_closefromup_tears_tears
    with dissolve
    
    ne "[protname]."

    show neus_exp_mouth sad_Silentx05
    show neus_exp_eyebrows serious
    $ nteye = "front01"
    call n_closefromup_tears_tears
    with dissolve

    p "¿Hmm...?"

    show neus_exp_mouth sad_Talkingx03
    show neus_exp_eyebrows sadx02
    $ nteye = "front03"
    call n_closefromup_tears_tears
    with dissolve

    if DidacPregnant:

        ne "Cuídala,"

    else:

        ne "Cuídalo,"

    extend " por favor."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx02
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Sé que no tengo derecho a pedirte esto,"

    show neus_exp_mouth sad_Talkingx04
    show neus_exp_eyebrows sadx01
    $ nteye = "right01"
    call n_closefromup_tears_tears
    with dissolve

    ne "y quizás ni siquiera me creas."

    show neus_exp_mouth sad_Talkingx003
    show neus_exp_eyebrows sadx03
    $ nteye = "front08"
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero de corazón,"

    $ ntlong += 1

    show neus_exp_mouth happy_Talkingx04
    show neus_exp_eyebrows sadx04
    $ nteye = "front04"
    call n_closefromup_tears_tears
    with dissolve

    ne "os deseo la mayor felicidad posible."

    show neus_exp_mouth happy_Silentx04
    show neus_exp_eyebrows sadx06
    $ nteye = "front07"
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene bg an04_flat_gate_back_blur
    with Dissolve(0.5)

    pause 0.2

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 01:
            df_body_atleft
        show didacfbodytop bracat_02:
            df_body_atleft
        show didacfhandl_hip_naked_drops 01:
            df_body_atleft
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_atleft
        show didacfbodybelow_naked_wet 01:
            df_body_atleft
        show didacfbodybelow_panties green:
            df_body_atleft
        show didacfhandr_leg_naked_drops 00:
            df_body_atleft
        show didacfbodytop bracat:
            df_body_atleft
        show didacfhandl_hip_naked_drops 00:
            df_body_atleft

    show didacf_blush 03:
        df_exp_atleft
    show didacf_eyes 05:
        df_exp_atleft
    show didacf_pupils front05:
        df_exp_atleft
    show didacf_eyebrows sadx01:
        df_exp_atleft
    show didacfbodytop_hair:
        df_body_atleft
    show didacf_mouth happybiting_Silentx04:
        df_exp_atleft

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex02
    call dfeye_lab

    with fade

    n "Entre lágrimas se da la vuelta para alejarse."

    scene bg an04_flat_gate_back_alone
    with fade

    n "Intentas sacar la cabeza para ver a dónde va cuando..."

label night05_DidacHome_NeusLeaving:

    $ saturation_tint_level = "verydark"

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 01:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat_02:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 01:
            df_body_ontheleftInverted_close
    else:
        show didacfbodybelow_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodybelow_naked_wet 01:
            df_body_ontheleftInverted_close
        show didacfbodybelow_panties green:
            df_body_ontheleftInverted_close
        show didacfhandr_leg_naked_drops 00:
            df_body_ontheleftInverted_close
        show didacfbodytop bracat:
            df_body_ontheleftInverted_close
        show didacfhandl_hip_naked_drops 00:
            df_body_ontheleftInverted_close

    show didacf_blush 03:
        df_exp_ontheleftInverted_close
    show didacf_eyes 05:
        df_exp_ontheleftInverted_close
    show didacf_pupils front05:
        df_exp_ontheleftInverted_close
    show didacf_eyebrows sadx01:
        df_exp_ontheleftInverted_close
    show didacfbodytop_hair:
        df_body_ontheleftInverted_close
    show didacf_mouth happybiting_Silentx04:
        df_exp_ontheleftInverted_close

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx03
    call dfeye_lab

    with hpunch
    p "¡Ugh!"

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "¡¿Por qué coño eres tan bruto?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Deja que se vaya."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "No la necesitamos."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Quizás tienes razón."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Aunque tengo la sensación de que..."

####

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            dfbody_atright
        show didacfbodybelow_naked_wet 01:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright
        show didacfbodytop bracat_02:
            dfbody_atright
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright
    else:
        show didacfbodybelow_naked_drops 00:
            dfbody_atright
        show didacfbodybelow_naked_wet 01:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright
        show didacfbodytop bracat:
            dfbody_atright
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright

    show didacf_blush 03:
        df_exp_onthecenter_superClose
    show didacf_eyes 05:
        df_exp_onthecenter_superClose
    show didacf_pupils front05:
        df_exp_onthecenter_superClose
    show didacf_eyebrows sadx01:
        df_exp_onthecenter_superClose
    show didacfbodytop_hair:
        df_body_onthecenter_superClose
    show didacf_mouth happybiting_Silentx04:
        df_exp_onthecenter_superClose

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    n "Se te acerca aún más."

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Te lo digo en serio [protname]."

    if afternight04__MMouth_Tongue_Success > 0 and pl.dp > 80:

        $ df_eye = "front05"
        show didacf_mouth sad_Silentx06
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        pause 0.2

        show black
        show kiss_ f_d_12:
            transform_anchor True
            xalign 0.5 yalign 0.5
        with hpunch

        p "¿Hmmm...?"

        show kiss_ f_d_11
        with Dissolve(0.5)

        n "Te agarra por el pescuezo y te da un beso con lengua."

        show kiss_ f_d_10
        with Dissolve(0.5)

        pause 0.2

        show kiss_ f_d_02
        with Dissolve(0.5)

        pause 0.2

        hide kiss_
        hide black

        $ df_blush += 1

        $ df_eye = "front05"
        show didacf_mouth sadbiting_Silentx05
        show didacf_eyebrows sadx04
        call dfeye_lab
        with Dissolve(1.0)

        p "¿Qué...?"

    if pl.dp > 80:

        $ df_eye = "front01"
        show didacf_mouth sad_Talkingx07
        show didacf_eyebrows angryx03
        call dfeye_lab
        with dissolve

        d "Ni se te ocurra abandonarme."

        $ df_eye = "front02"
        show didacf_mouth sad_Talkingx08
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "O te romperé los huevos."

        $ df_eye = "front03"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        p "Por lo visto,"

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "si haces eso tampoco podrás disfrutar mucho de tu nuevo cuerpo."

        $ df_eye = "front04"
        show didacf_mouth sad_Silentx05
        show didacf_eyebrows angryx04
        call dfeye_lab
        with dissolve

        d "Tsssk..."

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx004
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        d "Serás imbécil."

    scene bg an04_flat_gate_back_alone
    with hpunch

    n "Sientes su agarrón en en tu muñeca"

    #$ saturation_tint_level = "default"

    scene bg an04_flat_gate_composition002:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.7 ypos -2.3 # flat_gate_Didac+Neus
        ease 10.0 zoom 0.5 xpos 0.25 ypos -0.3 #General view door.
    with fade

    n "arrastrándote para que lo sigas hasta el ascensor."

    jump night05_DidacHome_DidacStops

label night05_DidacHome_DidacStops:

    $ saturation_tint_level = "default"

    show bg an04_flat_gate_composition002:
        ease 20.0 zoom 1.5 xpos -0.9 ypos -2.3

    n "Sin darte cuenta, vuelves la vista atrás,"

    n "rememorando ese rostro cubierto de lágrimas a la luz de la farola."

    show bg an04_flat_gate_composition002:
        # zoom 0.5 xpos 0.25 ypos -0.3 #General view door.
        zoom 0.75 xpos -0.1 ypos -1.0 # Enough?
    with hpunch
    p "Ugh..."

    p "¿Por qué te detienes ahora?"

    show neigh_body:
        neigh_pos_atLeft_body

    show neigh_exp_eyes 03:
        neigh_pos_atLeft_exp
    show neigh_exp_piris left03:
        neigh_pos_atLeft_exp
    show neigh_exp_eyebrows surprisex02:
        neigh_pos_atLeft_exp
    show neigh_exp_mouth sad_Silentx01:
        neigh_pos_atLeft_exp
    show neigh_hairFront:
        neigh_pos_atLeft_exp


    if not DidacPregnant:

        show didacfbodybelow_naked_drops 01:
            dfbody_atright
        show didacfbodybelow_naked_wet 01:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright
        show didacfbodytop bracat_02:
            dfbody_atright
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright
    else:

        show didacfbodybelow_naked_drops 00:
            dfbody_atright
        show didacfbodybelow_naked_wet 01:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright
        show didacfbodytop bracat:
            dfbody_atright
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright

    show didacf_blush 03:
        dfexpressions_atright
    show didacf_eyes 05:
        dfexpressions_atright
    show didacf_pupils front05:
        dfexpressions_atright
    show didacf_eyebrows sadx01:
        dfexpressions_atright
    show didacfbodytop_hair:
        dfbody_atright
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright

    $ df_eye = "left03"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "¡Buenas!"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows suspiciousx01
    show neigh_exp_mouth sad_Talkingx01

    $ df_eye = "left04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    m01 "Euh..."

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows sadx01
    show neigh_exp_mouth sad_Talkingx03

    $ df_eye = "left01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    m01 "[protname],"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows suspiciousx01
    show neigh_exp_mouth sad_Talkingx04

    $ df_eye = "left02"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    m01 "¿quién es esta chica?"

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows surprisex01
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "Euh..."

    show neigh_exp_eyes 00
    show neigh_exp_piris left00
    show neigh_exp_eyebrows surprisex02
    show neigh_exp_mouth sad_Silentx01

    $ df_eye = "front00"
    show didacf_mouth happy_Talkingx07
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¡Soy la hermana de Dídac!"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows surprisex01
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "front07"
    show didacf_mouth happy_Talkingx06
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "Encantada de conocerte."

    if DidacPregnant:

        show neigh_exp_eyes 03
        show neigh_exp_piris left03
        show neigh_exp_eyebrows suspiciousx02
        show neigh_exp_mouth sad_Silentx02

        $ df_eye = "left02"
        show didacf_mouth happy_Talkingx05
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "A partir de ahora seré parte de la comunidad."

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows suspiciousx02
    show neigh_exp_mouth sad_Silentx04

    $ df_eye = "left03"
    show didacf_mouth happybiting_Silentx06
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    m01 "..."

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows sadx01
    show neigh_exp_mouth sad_Talkingx04

    $ df_eye = "left00"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    m01 "¿Y por qué estás desnuda?"

    show neigh_exp_eyes 00
    show neigh_exp_piris left00
    show neigh_exp_eyebrows surprisex02
    show neigh_exp_mouth sad_Silentx01

    $ df_eye = "left03"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "No estoy desnuda."

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows surprisex01
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "left04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    m01 "..."

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows suspiciousx02
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "left05"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows surprisex01
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Simplemente he salido así porque tenía prisa"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows serious
    show neigh_exp_mouth sad_Silentx02

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "y tenía que decirle algo importante."

    show neigh_exp_eyes 00
    show neigh_exp_piris left00
    show neigh_exp_eyebrows surprisex02
    show neigh_exp_mouth sad_Silentx01

    $ df_eye = "left02"
    show didacf_mouth sad_Talkingx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿Por qué siempre estás pensando lo peor de la gente?!"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows suspiciousx02
    show neigh_exp_mouth sad_Talkingx04

    $ df_eye = "left00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    m01 "¿Nos conocemos?"

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows sadx01
    show neigh_exp_mouth sad_Silentx03

    $ df_eye = "front00"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "..."

    show neigh_exp_eyes 03
    show neigh_exp_piris left03
    show neigh_exp_eyebrows suspiciousx01
    show neigh_exp_mouth sad_Silentx04

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx07
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "¡No,"

    extend " claro que no!"

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows suspiciousx01
    show neigh_exp_mouth sad_Silentx03

    if not DidacPregnant:

        show didacfbodybelow_naked_drops 01:
            df_body_onthecenter_superClose
        show didacfbodybelow_naked_wet 01:
            df_body_onthecenter_superClose
        show didacfbodybelow_panties green:
            df_body_onthecenter_superClose
        show didacfhandr_leg_naked_drops 01:
            df_body_onthecenter_superClose
        show didacfbodytop bracat_02:
            df_body_onthecenter_superClose
        show didacfhandl_hip_naked_drops 01:
            df_body_onthecenter_superClose
    else:

        show didacfbodybelow_naked_drops 00:
            df_body_onthecenter_superClose
        show didacfbodybelow_naked_wet 01:
            df_body_onthecenter_superClose
        show didacfbodybelow_panties green:
            df_body_onthecenter_superClose
        show didacfhandr_leg_naked_drops 00:
            df_body_onthecenter_superClose
        show didacfbodytop bracat:
            df_body_onthecenter_superClose
        show didacfhandl_hip_naked_drops 00:
            df_body_onthecenter_superClose

    show didacf_blush 03:
        df_exp_onthecenter_superClose
    show didacf_eyes 05:
        df_exp_onthecenter_superClose
    show didacf_pupils front05:
        df_exp_onthecenter_superClose
    show didacf_eyebrows sadx01:
        df_exp_onthecenter_superClose
    show didacfbodytop_hair:
        df_body_onthecenter_superClose
    show didacf_mouth happybiting_Silentx04:
        df_exp_onthecenter_superClose

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    n "Sin decir otra palabra"

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows suspiciousx02
    show neigh_exp_mouth sad_Silentx04

    $ df_eye = "front05"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    n "sigue arrastrándote pasando por su lado en dirección al ascensor."

    scene bg an04_flat_gate_composition002:
        truecenter
        zoom 0.75 xpos -0.1 ypos -1.0

    show neigh_body:
        neigh_pos_atLeft_body

    show neigh_exp_eyes 03:
        neigh_pos_atLeft_exp
    show neigh_exp_piris left03:
        neigh_pos_atLeft_exp
    show neigh_exp_eyebrows surprisex02:
        neigh_pos_atLeft_exp
    show neigh_exp_mouth sad_Silentx01:
        neigh_pos_atLeft_exp
    show neigh_hairFront:
        neigh_pos_atLeft_exp

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows normal
    show neigh_exp_mouth sad_Silentx03

    with dissolve

    # Missing the lady here.

    p "Lo siento, por lo visto tenemos algo de prisa..."

    show neigh_exp_eyes 03
    show neigh_exp_piris front03
    show neigh_exp_eyebrows surprisex02
    show neigh_exp_mouth sad_Silentx02
    with dissolve

    pause 0.2

    scene black
    with fade

    n "Dando un portazo y tecleando el número de vuestra planta."

    scene bg night05_bg_cups_ridebg_comp_04:
        subpixel True
        truecenter
        rotate 90
        ypos -6.3 # Below
        block:
            linear 25.0 ypos 8.6 # Top
            ypos -6.3 # Below
            repeat
        #ypos 4.5 # Middle?
 
    show bg_homeElevator:
        truecenter
        zoom 0.5

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodybelow_naked_wet 01:
            dfbody_atright_closex2
        show didacfbodybelow_panties green:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 01:
            dfbody_atright_closex2
        show didacfbodytop bracat_02:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 01:
            dfbody_atright_closex2
    else:
        show didacfbodybelow_naked_drops 00:
            dfbody_atright_closex2
        show didacfbodybelow_naked_wet 01:
            dfbody_atright_closex2
        show didacfbodybelow_panties green:
            dfbody_atright_closex2
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright_closex2
        show didacfbodytop bracat:
            dfbody_atright_closex2
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright_closex2

    show didacf_blush 03:
        dfexpressions_atright_closex2
    show didacf_eyes 05:
        dfexpressions_atright_closex2
    show didacf_pupils front05:
        dfexpressions_atright_closex2
    show didacf_eyebrows sadx01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright_closex2

    $ df_eye = "left04"
    show didacf_mouth sadbiting_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with fade

    d "..."

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Hermana de Dídac?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Se te ocurre algo mejor?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Podrías haber dicho prima..."

    $ df_eye = "left01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "left02"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Sí,"

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "quizás hubiera sido mejor."

    $ df_eye = "left04"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Oye."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "¿Sí?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "¿Qué es lo que pasaría realmente"

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "si la gente descubriera que en realidad soy Dídac?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Nada bueno,"

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "eso te lo aseguro."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "¿Y cómo estás tan seguro?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Alguien que es capaz de convertirte en una mujer"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "en menos de dos días con una sola mordida,"

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "no es alguien a quien tomarse a broma."

    $ df_eye = "right04"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "¿Crees que podría morir?"

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Es muy probable."

    show bg ped_04:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5

    # show bg night05_bg_cups_ridebg_comp_04:
    #     ypos 4.5 # Middle?

    $ df_eye = "right01"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows serious
    call dfeye_lab
    with Dissolve(0.75)

    n "El ascensor se detiene."

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    d "Eso sería una putada."

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows sadx06
    call dfeye_lab
    with dissolve

    jump night05_DidacHome_afterNeus


label night05_DidacHome_afterNeus:

    pause 0.2

    scene afternight03_bg entrance_lighton
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    with fade
    pause 0.2
    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with dissolve

    n "Dejas las llaves sobre la mesita de la entrada"

    scene morning04_bg_livingroom_others_night_lightOn
    with fade

    n "mientras te diriges al comedor sin saber muy bien qué hacer."

    ##

    if not DidacPregnant:
        show didacfbodybelow_naked_drops 02:
            dfbody_atright
        show didacfbodybelow_naked_wet 02:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 02:
            dfbody_atright
        show didacfbodytop bracat_02:
            dfbody_atright
        show didacfhandl_hip_naked_drops 02:
            dfbody_atright
    else:
        show didacfbodybelow_naked_drops 00:
            dfbody_atright
        show didacfbodybelow_naked_wet 01:
            dfbody_atright
        show didacfbodybelow_panties green:
            dfbody_atright
        show didacfhandr_leg_naked_drops 00:
            dfbody_atright
        show didacfbodytop bracat:
            dfbody_atright
        show didacfhandl_hip_naked_drops 00:
            dfbody_atright

    show didacf_blush 03:
        dfexpressions_atright
    show didacf_eyes 05:
        dfexpressions_atright
    show didacf_pupils front05:
        dfexpressions_atright
    show didacf_eyebrows sadx01:
        dfexpressions_atright
    show didacfbodytop_hair:
        dfbody_atright
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿Y si retomamos dónde lo habíamos dejado?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Dídac..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¿Qué pasa ahora?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Hemos follado toda la tarde."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "Y no sé tú,"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "pero mi cuerpo tiene un límite."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Bien que habrías follado con ella si hubieras acudido a la cita."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Eso no lo sabes."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Ya..."

    $ df_eye = "front00"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with hpunch

    ono "Brrrgghhh..."

    $ df_eye = "down01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "Dídac se te queda mirando la barriga."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Bueno,"

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "quizás también tengo algo de hambre."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Podríamos aprovechar y ver al mismo tiempo una película."

    $ df_eye = "right01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    pt "Aunque sea para quitarme a Neus de la cabeza."

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿Y si miramos una porno?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Joder Dídac."

    $ df_eye = "front08"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "¿No puedes pensar en otra cosa?"

    $ df_eye = "right04"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Vale,"

    extend " vale..."

    if not DidacPregnant:

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Estás seguro que estás bien?"

        $ df_eye = "front02"
        show didacf_mouth sad_Silentx01
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "No tienes buena pinta."

        $ df_eye = "front08"
        show didacf_mouth sad_Talkingx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "No te preocupes,"

        $ df_eye = "left02"
        show didacf_mouth sad_Talkingx04
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "antes de comer me tomaré una aspirina."

        $ df_eye = "left03"
        show didacf_mouth sadbiting_Silentx04
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        p "..."

    $ df_eye = "front02"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Vete pidiéndote unas pizzas mientras busco algo para mirar por internet,"

    $ df_eye = "front03"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "¿te parece bien?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Y si nos hacemos unas palomitas?"

    $ df_eye = "front04"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Vaya cutrez de cita me estás ofreciendo."

    $ df_eye = "right05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    pt "¿Cita?"

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Nuestra economía no está para tirar cohetes precisamente."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Además,"

    extend " como si unas pizzas en casa fuera comer en un restaurante de lujo..."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Seguro que con ella hubieras comido algo mejor."

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    pt "Eso es discutible..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Vale,"

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "unas palomitas van bien."

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¿Qué tipo de peli te apetece?"

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Yo que sé..."

    $ df_eye = "right03"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "elige algo que nos distraiga un poco."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Pero no me pongas una porno."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx003
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Que sí,"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx04
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "que ya me ha quedado claro."

    $ df_eye = "right05"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿No prefieres primero ir a ponerte algo más cómodo?"

    $ df_eye = "down01"
    show didacf_mouth sad_Silentx01
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front02"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Esto es bastante cómodo."

    $ df_eye = "front03"
    show didacf_mouth happy_Silentx04
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    pt "Ya..."

    $ df_eye = "front04"
    show didacf_mouth happybiting_Silentx04
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    pt "y una mierda."

    scene bg kitchen:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5
        ease 15.0 zoom 1.0 xpos 0.7 ypos 1.0
    with fade

    n "Te diriges a la cocina en busca de esos paquetes"

    n "que tenéis ahí desde hace sabe quién cuándo"

    n "y los pones en el microondas"

    n "mientras Dídac se pone a mirar por internet."

    if DidacPregnant:

        jump night05_DidacHome_moviePopCorn

    else:

        jump night05_DidacHome_DidacIll

label night05_DidacHome_moviePopCorn:

    scene bg tv_background_movie:
        subpixel True
        truecenter
        zoom 1.0
        ease 18.0 zoom 0.5
    with fade

    n "Pasáis la noche comiendo palomitas y mirando una comedia ligera,"

    n "no sin que Dídac haga alguna que otra tentativa tocándote el paquete"

    n "pero al ver tu expresión y que tu entrepierna no responde como ella esperaba"

    n "regresa su atención hacia la pantalla."

    scene afternight03_bg_hallway_day:
    with fade

    n "Cuando la termináis te diriges al baño para lavarte los dientes"

    n "y poco después regresas a vuestra habitación."

    $ saturation_tint_level = "dark"

##
    
    scene beds_night_lightOn_blindUp_DemptyMCmessy

    show didacfbodybelow_naked_drops 00:
        dfbody_atright
    show didacfbodybelow_naked_wet 01:
        dfbody_atright
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright
    show didacfbodytop_naked_drops 00:
        dfbody_atright
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright

    show didacf_blush 03:
        dfexpressions_atright
    show didacf_eyes 05:
        dfexpressions_atright
    show didacf_pupils front05:
        dfexpressions_atright
    show didacf_eyebrows sadx01:
        dfexpressions_atright
    show didacfbodytop_hair:
        dfbody_atright
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright

    with fade 

    p "..."

    n "Te la encuentras en frente de ti completamente desnuda."

    $ df_eye = "front02"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "Por lo menos podrías lavarte los dientes."

    $ df_eye = "front03"
    show didacf_mouth sad_Talkingx004
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Ya lo he hecho antes."

    $ df_eye = "down04"
    show didacf_mouth happybiting_Silentx03
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Me has dicho que después de la película haríamos algo."

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "Estoy cansado Dídac."

    $ df_eye = "front03"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    p "Mejor dejémoslo para mañana."

    $ df_eye = "down04"
    show didacf_mouth sad_Silentx07
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "front08"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Tssk..."

    $ df_eye = "right02"
    show didacf_mouth sad_Talkingx06
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Vale."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Como quieras."

    $ df_eye = "down05"
    show didacf_mouth sadbiting_Silentx05
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    pt "¿En serio me va a dejar descansar?"

    scene beds_night_lightOn_blindDown_Dbusy02MCmessy
    show beds_D02
    with Dissolve(0.5)

    n "Cierras la ventana,"

    scene beds_night_lightOn_blindDown_Dbusy02MCbusy
    show beds_D02
    with Dissolve(0.5)

    n "ambos os ponéis en la cama,"

    $ saturation_tint_level = "superdark"

    scene beds_night_lightOff_blindDown_Dbusy02MCbusy
    show beds_D02
    with Dissolve(0.5)

    pause 0.2

    scene black
    with fade

    n "y cierras tus párpados."

    jump morning06_Df_wakeUp


label night05_DidacHome_DidacIll:

    scene bg tv_background_movie:
        subpixel True
        truecenter
        zoom 1.0
        ease 18.0 zoom 0.5
    with fade

    n "A lo largo de la noche que os la pasáis mirando una comedia ligera,"

    n "te sorprende que apenas haya comido alguna que otra palomita,"

    n "especialmente cuando suele ser el que termina comiéndoselas todas."

    p "¿De verdad estás bien?"

    d "..."

    d "Quizás debería descansar un poco."

    show bg tv_background_off
    with Dissolve(0.25)

    n "Apagas el televisor."

    scene bg ped_04

    show didacfbodybelow_naked_drops 02:
        df_body_onthecenter_superClose
    show didacfbodybelow_naked_wet 02:
        df_body_onthecenter_superClose
    show didacfbodybelow_panties green:
        df_body_onthecenter_superClose
    show didacfhandr_leg_naked_drops 02:
        df_body_onthecenter_superClose
    show didacfbodytop bracat_02:
        df_body_onthecenter_superClose
    show didacfhandl_hip_naked_drops 02:
        df_body_onthecenter_superClose

    show didacf_blush 03:
        df_exp_onthecenter_superClose
    show didacf_eyes 05:
        df_exp_onthecenter_superClose
    show didacf_pupils front05:
        df_exp_onthecenter_superClose
    show didacf_eyebrows sadx01:
        df_exp_onthecenter_superClose
    show didacfbodytop_hair:
        df_body_onthecenter_superClose
    show didacf_mouth happybiting_Silentx04:
        df_exp_onthecenter_superClose

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows sadx01
    call dfeye_lab
    with fade

    d "No..."

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx03
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    d "Termina tú la película..."

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx04
    show didacf_eyebrows sadx04
    call dfeye_lab
    with dissolve

    p "Puedo verla otro día,"

    $ df_eye = "front05"
    show didacf_mouth sad_Silentx05
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    p "además, también estoy algo cansado."

    scene black
    with fade

    n "Hace el intento de ponerse de pie,"

    n "pero justo cuando está a punto de caerse"

    with vpunch
    n "logras agarrarlo al vuelo."

    # scene morning04_bg_livingroom_others_night_lightOn
    scene bg ped_04

    show didacfbodybelow_naked_drops 02:
        df_body_onthecenter_superClose
    show didacfbodybelow_naked_wet 02:
        df_body_onthecenter_superClose
    show didacfbodybelow_panties green:
        df_body_onthecenter_superClose
    show didacfhandr_leg_naked_drops 02:
        df_body_onthecenter_superClose
    show didacfbodytop bracat_02:
        df_body_onthecenter_superClose
    show didacfhandl_hip_naked_drops 02:
        df_body_onthecenter_superClose

    show didacf_blush 03:
        df_exp_onthecenter_superClose
    show didacf_eyes 05:
        df_exp_onthecenter_superClose
    show didacf_pupils front05:
        df_exp_onthecenter_superClose
    show didacf_eyebrows sadx01:
        df_exp_onthecenter_superClose
    show didacfbodytop_hair:
        df_body_onthecenter_superClose
    show didacf_mouth happybiting_Silentx04:
        df_exp_onthecenter_superClose

    $ df_eye = "front08"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows sadx04
    call dfeye_lab
    with fade

    d "Joder..."

    $ df_eye = "front06"
    show didacf_mouth happy_Talkingx02
    show didacf_eyebrows sadx05
    call dfeye_lab
    with dissolve

    d "Quizás estoy peor de lo que pensaba."

    $ df_eye = "front06"
    show didacf_mouth sad_Silentx06
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    pause 0.2

    scene beds_night_lightOn_blindUp_DemptyMCmessy
    with fade

    n "Agarrándolo por el hombro lo acompañas a vuestra habitación"

    $ saturation_tint_level = "candle"

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
    show didac_bed_d_blanket 02
    with fade

    n "le ayudas a desvestirse y a ponerlo en la cama."

    show didac_bed_d_mouth happy_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Je, je..."

    show didac_bed_d_mouth happy_Talkingx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Realmente pensé que pasaríamos la noche de una forma muy distinta..."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "Voy a traerte otra aspirina."

    show didac_bed_d_mouth happy_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Si no es mucho pedir, que sea una de Arkham."

    show didac_bed_d_mouth happy_Talkingx01
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "La marca que me he tomado antes me parece que no ha hecho mucho efecto."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx03
    with dissolve

    p "¡¿Por qué te tomas otra si sabes que las de Arkham son las que mejor funcionan?!"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup right03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Como bien has dicho antes,"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "nuestra economía no es muy buena..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "No seas imbécil."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx03
    with dissolve

    pause 0.2

    show black
    with fade

    n "Te diriges a la cocina y le preparas un vaso con algo de azúcar junto a la aspirina."

    hide black

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "Ten,"

    extend " tómatelo."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth happy_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Gracias."

    show didac_bed_d_mouth happy_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "En el fondo eres un buen amigo."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx02
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows sadx03
    with dissolve

    pause 0.2

    scene beds_night_lightOn_blindUp_Dbusy02MCmessy
    show beds_D02b
    with fade

    scene beds_night_lightOn_blindDown_Dbusy02MCmessy
    show beds_D02
    with Dissolve(0.5)

    n "Decides bajar la persiana,"

    $ saturation_tint_level = "superdark"

    scene beds_night_lightOff_blindDown_Dbusy02MCbusy
    show beds_D02
    with Dissolve(0.5)

    n "apagar la luz"

    scene black
    with fade

    n "y tomar descanso en tu cama."

    jump morning06_Df_wakeUp


    ####

label morning06_Df_wakeUp:

    pause

    scene black
    with fade

    $ saturation_tint_level = "default"

    if DidacPregnant == True and p_prot_analgesic == "accepted":

        n "Sientes unas manos cálidas cogiéndote una de las manos"

        n "para luego sentir algo frío en la muñeca."

        ono "click"

        pt "¿Qué...?"

        n "Sientes exactamente lo mismo en la otra mano."

        ono "click"

        pt "¿Lo estoy soñando?"

        n "El cantar de los pájaros te llama la atención por su agudo silbido."

    else:

        n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."
        
    n "Pero hay otro sonido extraño que te llama la atención."

    if DidacPregnant:

        play sound "audio/characters/didac/moan03.ogg"

    else:

        d "Ughh..."
    
    n "Percibes un exótico y desconocido olor en la habitación."

    if not DidacPregnant:

        jump morning06_Dm_wakeUp

    play sound "audio/characters/didac/moan03.ogg"

    p "Hmm..."

    n "Pero también percibes tu polla atrapada"

    n "en una cálida, húmeda y familiar cavidad."

    play sound "audio/characters/didac/moanings02.ogg"

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

    pt "¿En serio...?"

    show morning04_bedroom_Didac_body 01b
    show morning04_bedroom_Didac_bodyass 01b
    with Dissolve(0.5)

    n "Al separar tus párpados ves a tu compañera de piso encima de ti,"
    
    n "moviendo sutilmente su entrepierna sobre tus caderas."

    show morning04_bedroom_Didac_body 01c
    show morning04_bedroom_Didac_bodyass 01b
    with Dissolve(0.5)

    d "Buenos días, semental."

    p "¿No podías esperar a que me despertara?"

    d "Te he dejado dormir,"

    extend " ¿no?"

    p "¿A esto lo llamas dejar dormir?"

    d "..."

    d "La tenías tan dura que no he podido resistirme."

    p "Sabes perfectamente por qué está así de dura por las mañanas."

    d "Sí,"

    extend " lo sé."

    pt "La madre que lo parió."

    if p_prot_analgesic == "accepted":

        n "Al intentar mover tus manos"

        n "descubres que están rodeadas por un duro metal que te limita el movimiento."

        $ mc_stat = "_cuffed"

        $ mc_cuff_handTensed = False
        $ mc_cuff_cuffed = "closed"
        $ mc_cuff_right = True

        scene d06_cuffHand_mc_hand_comp:
            subpixel True
            truecenter
            zoom 1.2 xpos -0.0 ypos -0.2 # Beginning?
            ease 5.0 zoom 1.0 xpos 0.9 ypos 0.6 # Center Hand

        show morning04_bedroom_DMast_blinkeye

        show light_01b :
            light01_topside_position

        with fade

        p "¿Qué?"

        $ mc_cuff_handTensed = True
        hide morning04_bedroom_DMast_blinkeye
        show d06_cuffHand_mc_hand_comp:
            ease 10.0 zoom 0.5 xpos 0.5 ypos 0.5 # Complete
        with Dissolve(0.5)

        p "¿Qué coño has hecho?"

        d "Eso tú."

        p "¡¿Me has esposado?!"

        show morning04_bg bedroom_neus_a
        show morning04_bedroom_Didac_body_ass 02c: 
            morning04_bedroom_Neus_bodyass_anim01
        show morning04_bedroom_Didac_body_body 02c
        #show morning04_bedroom_Neus_Prove
        show morning04_bedroom_Didac_exp_blush 02:
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

        d "Lo que te deberías de preguntar es de dónde las he sacado."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx04
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        p "..."

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        d "¿Puedo saber por qué escondías un maletín con estas esposas"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "y con este pote que tiene un líquido bastante misterioso?"

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx03
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        p "¿Cómo...?"

        show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "Reconozco que estaba bien escondido,"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows surprisex01
        with dissolve

        d "no sabía que había un compartimento secreto bajo la madera del armario."

        show morning04_bedroom_Didac_exp_mouth happybiting_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        pt "¡¿Y cómo es que se le ha dado por mirar ahí?!"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
        show morning04_bedroom_Didac_exp_eyebrows normal
        with dissolve

        d "¿Siempre ha estado ahí"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        d "o hiciste venir a un carpintero un día que yo no estaba?"

        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        p "¿Qué...?"

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
        show morning04_bedroom_Didac_exp_eyebrows angryx02
        with dissolve

        d "No te hagas el tonto ahora."

        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
        show morning04_bedroom_Didac_exp_eyebrows angryx01
        with dissolve

        d "¿Qué pretendías hacer con esto?"

        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx02
        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
        with dissolve

        $ morning06_Df_analgesic_answer = []

        menu morning06_Df_analgesic_question:

            pt "El maletín de la rubia..."

            "Dídac, no sé de qué demonios me estás hablando." if "dontKnow" not in morning06_Df_analgesic_answer:
                call p_Help

                $pl.ch_pts("dp",-1)
                $ morning06_Df_analgesic_answer.append("dontKnow")

                show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "..."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "Te conozco demasiado bien para saber cuándo estás mintiendo, [protname]."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx04
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                p "..."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx002
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "Te repito la pregunta."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "¡¿Qué coño intentabas hacer con esto?!"

                show morning04_bedroom_Didac_exp_mouth sad_Silentx04
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                jump morning06_Df_analgesic_question

            "Lo tenía ahí escondido para un caso de necesidad.":
                call p_Help

                $ morning06_Df_analgesic_answer.append("justInCase")

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "¿De necesidad?"

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "¡¿Necesidad de qué?!"

                show morning04_bedroom_Didac_exp_mouth sad_Silentx02
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                p "Por si se te daba por salir por ahí a follar con cualquiera"

                show morning04_bedroom_Didac_exp_mouth sad_Silentx03
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                p "para luego descubrir que te has quedado embarazada por accidente."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx05
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "..."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx01
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "O sea,"

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "follar contigo bien."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
                show morning04_bedroom_Didac_exp_eyebrows angryx03
                with dissolve

                d "Pero follar con otros..."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx04
                show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
                with dissolve

                menu:

                    pt "¿Se está cachondeando de mí?"

                    "¡Pero si has sido tú quien me ha obligado a follarte bajo amenaza!":
                        call p_Help
                        $pl.ch_pts("dp",-1)

                        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
                        show morning04_bedroom_Didac_exp_eyebrows surprisex01
                        with dissolve

                        p "¡Sin mencionar que cortaste el jodido condón sin que yo lo supiera!"

                        show morning04_bedroom_Didac_exp_mouth sad_Silentx04
                        show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
                        with dissolve

                        d "..."

                        show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
                        show morning04_bedroom_Didac_exp_eyebrows sadx01
                        with dissolve

                        d "Tampoco hace falta que lo expreses de esa manera..."

                        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx03
                        show morning04_bedroom_Didac_exp_eyebrows sadx02
                        with dissolve

                        pt "¡La madre que lo parió!"


                    "Lo dices como si hubiera sido yo el que te hubiera obligado.":
                        call p_Help

                        show morning04_bedroom_Didac_exp_mouth sad_Silentx02
                        show morning04_bedroom_Didac_exp_eyebrows surprisex01
                        with dissolve

                        p "Sin mencionar que fuiste tú quien cortó el condón"

                        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx03
                        show morning04_bedroom_Didac_exp_eyebrows sadx01
                        with dissolve

                        p "sin que me dijeras nada al respecto."

                        show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx04
                        show morning04_bedroom_Didac_exp_eyebrows sadx03
                        with dissolve

                        d "..."

                $ Pedrera_char_Cond = "DidacClose"
                call Pedrera_char_lab
                show bg bedroom_neus_a

                show light 01:
                    light01_topside_position

                $ df_eye = "front08"
                show didacf_mouth sad_Talkingx002
                show didacf_eyebrows sadx01
                call dfeye_lab
                with fade

                d "Vale,"

                extend " vale..."

                $ df_eye = "right02"
                show didacf_mouth sad_Talkingx004
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "Quizás en eso tienes algo de razón."

                $ df_eye = "right04"
                show didacf_mouth sadbiting_Silentx05
                show didacf_eyebrows suspiciousx02
                call dfeye_lab
                with dissolve

                pt "¡¿Quizás?!"

                $ df_eye = "front05"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows suspiciousx02
                call dfeye_lab
                with dissolve

                d "Pero tanto como para dejarme esposada..."

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx05
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                d "¿Acaso tenías pensado irte con la brujita de las narices"

                $ df_eye = "front02"
                show didacf_mouth sad_Talkingx06
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "dejándome atada en la cama?"

                $ df_eye = "front05"
                show didacf_mouth sad_Talkingx05
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                p "..."

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows surprisex01
                call dfeye_lab
                with dissolve

                d "¿Y si me entraban ganas de ir al baño?"

                $ df_eye = "front02"
                show didacf_mouth sad_Talkingx02
                show didacf_eyebrows serious
                call dfeye_lab
                with dissolve

                d "Un momento,"

                extend " en ese maletín..."

                $ df_eye = "left00"
                show didacf_mouth sad_Talkingx08
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "¡¿Para eso iban a servir la bolsa y el tubo de plástico?!"

                $ df_eye = "front01"
                show didacf_mouth sadbiting_Silentx04
                show didacf_eyebrows suspiciousx02
                call dfeye_lab
                with dissolve

                p "..."

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx06
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                d "Tienes que estar de coña."

                $ df_eye = "front02"
                show didacf_mouth sad_Silentx04
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                p "Al final no he sido yo quien lo ha usado."

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                d "No."

                $ df_eye = "front08"
                show didacf_mouth sad_Talkingx05
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "Pero el simple hecho de que lo tuvieras escondido,"

                $ df_eye = "front04"
                show didacf_mouth sad_Talkingx004
                show didacf_eyebrows angryx04
                call dfeye_lab
                with dissolve

                d "significa que seguías pensando en que podrías necesitarlo."

                $ df_eye = "front05"
                show didacf_mouth sad_Silentx05
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                p "..."

                $ df_eye = "front08"
                show didacf_mouth sad_Talkingx003
                show didacf_eyebrows surprisex01
                call dfeye_lab
                with dissolve

                d "Así que ahora lo usaré yo."

                $ df_eye = "front05"
                show didacf_mouth sad_Silentx04
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                p "Dídac."

                $ df_eye = "front04"
                show didacf_mouth sad_Silentx03
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                p "Sabes que por la mañana tengo entreno con los chicos"

                $ df_eye = "right05"
                show didacf_mouth sad_Silentx04
                show didacf_eyebrows surprisex01
                call dfeye_lab
                with dissolve

                p "y no nos podemos permitir el lujo de perder otra fuente de ingresos."

                $ df_eye = "front08"
                show didacf_mouth sad_Talkingx03
                show didacf_eyebrows serious
                call dfeye_lab
                with dissolve

                d "Tranquilo,"

                $ df_eye = "front04"
                show didacf_mouth happy_Talkingx03
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                d "no te dejaré tirado durante horas atado a la cama"

                $ df_eye = "front02"
                show didacf_mouth sad_Talkingx05
                show didacf_eyebrows angryx03
                call dfeye_lab
                with dissolve

                d "como tenías pensado hacer conmigo."

                $ df_eye = "front03"
                show didacf_mouth happy_Talkingx04
                show didacf_eyebrows sadx01
                call dfeye_lab
                with dissolve

                d "Simplemente te voy a usar un poquito mientras estás atado"

                $ df_eye = "front04"
                show didacf_mouth happy_Talkingx06
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                d "y a mi merced..."

                $ df_eye = "down04"
                show didacf_mouth happybiting_Silentx05
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                p "..."

            "¿Cómo es que se te ha dado por mirar ahí?" if "why" not in morning06_Df_analgesic_answer:
                call p_Help

                $ morning06_Df_analgesic_answer.append("why")

                show morning04_bedroom_Didac_exp_mouth sadbiting_Silentx01
                show morning04_bedroom_Didac_exp_eyebrows surprisex02
                with dissolve

                d "..."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows normal
                with dissolve

                d "Sinceramente no te sabría responder a eso."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx02
                show morning04_bedroom_Didac_exp_eyebrows suspiciousx01
                with dissolve

                pt "¡¿Cómo?!"

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx02
                show morning04_bedroom_Didac_exp_eyebrows sadx01
                with dissolve

                d "Tampoco sé muy bien por que he me levantado tan temprano."

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
                show morning04_bedroom_Didac_exp_eyebrows sadx02
                with dissolve

                d "Simplemente lo he hecho"

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx03
                show morning04_bedroom_Didac_exp_eyebrows serious
                with dissolve

                d "y por alguna razón he mirado ahí."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "Pero está claro que eso lo has puesto tú ahí."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx02
                show morning04_bedroom_Didac_exp_eyebrows surprisex01
                with dissolve

                p "¿Y por qué crees eso?"

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx003
                show morning04_bedroom_Didac_exp_eyebrows surprisex02
                with dissolve

                d "Por que te conozco demasiado bien para saber la cara que pones"

                show morning04_bedroom_Didac_exp_mouth happy_Talkingx03
                show morning04_bedroom_Didac_exp_eyebrows sadx01
                with dissolve

                d "cuando algo te sorprende."

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx04
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                d "Y no es la cara que has puesto"

                show morning04_bedroom_Didac_exp_mouth sad_Talkingx05
                show morning04_bedroom_Didac_exp_eyebrows angryx01
                with dissolve

                d "cuando te he hablado de la parte secreta del armario."

                show morning04_bedroom_Didac_exp_mouth sad_Silentx04
                show morning04_bedroom_Didac_exp_eyebrows angryx02
                with dissolve

                p "..."

                jump morning06_Df_analgesic_question


    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Qué hora es?"

    $ df_eye = "front02"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Aún falta casi una hora para que tengas que ir a entrenar a los chicos."

    $ df_eye = "front04"
    show didacf_mouth sadbiting_Silentx03
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front05"
    show didacf_mouth sad_Talkingx05
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "No seas así,"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx04
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "sabes que te gusta tanto como a mí."

    if p_prot_analgesic == "accepted":

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Qué te hace pensar que me gusta estar estado?"

        # CONDITIONAL #Did yesterday fucked you dominantely? # FOR_FUTURE

        $ df_eye = "front02"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "Aún no has perdido la erección..."

        $ df_eye = "front05"
        show didacf_mouth sad_Silentx03
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Quizás por que la sigo teniendo dentro de tu coño"

        $ df_eye = "down05"
        show didacf_mouth sadbiting_Silentx02
        show didacf_eyebrows surprisex02
        call dfeye_lab
        with dissolve

        p "sin que pares de moverte?"

        $ df_eye = "front05"
        show didacf_mouth happy_Silentx03
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front04"
        show didacf_mouth happy_Talkingx03
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Puede..."

        $ df_eye = "down05"
        show didacf_mouth happybiting_Silentx05
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        menu:

            "Dídac, quítame las esposas.":
                call p_Help

                $ df_eye = "front04"
                show didacf_mouth sadbiting_Silentx03
                show didacf_eyebrows suspiciousx01
                call dfeye_lab
                with dissolve

                d "..."

                $ df_eye = "front08"
                show didacf_mouth happybiting_Silentx05
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                n "Aprecias que sigue meciendo sus caderas."

                $ df_eye = "front02"
                show didacf_mouth sadbiting_Silentx01
                show didacf_eyebrows normal
                call dfeye_lab
                with dissolve

                p "¡Dídac!"

                if pl.dp > 100:

                    $ p_prot_analgesic = "takenOff"

                    $ df_eye = "front08"
                    show didacf_mouth sad_Silentx05
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with dissolve

                    d "Tssk..."

                    $ df_eye = "front02"
                    show didacf_mouth sad_Talkingx05
                    show didacf_eyebrows angryx04
                    call dfeye_lab
                    with dissolve

                    d "Eres un aguafiestas."

                    $ df_eye = "front04"
                    show didacf_mouth sadbiting_Silentx05
                    show didacf_eyebrows angryx03
                    call dfeye_lab
                    with dissolve

                    p "..."

                    scene day05
                    with fade

                    n "Pone sus pechos encima de tu rostro."

                    p "Ugh..."

                    ono "click"

                    extend " click"

                    n "Acto seguido, sientes tus manos libres de esas ataduras."

                    n "Apartándose de tu cara."

                    d "Bien..."

                    d "¿Y ahora qué te apetece hacer?"

                else:

                    $ df_eye = "front02"
                    show didacf_mouth happy_Talkingx03
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with dissolve

                    d "Me pone demasiado cachonda verte así."

                    $ df_eye = "front01"
                    show didacf_mouth sad_Silentx02
                    show didacf_eyebrows normal
                    call dfeye_lab
                    with dissolve

                    p "Lo digo en serio."

                    $ df_eye = "front04"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex01
                    call dfeye_lab
                    with dissolve

                    p "¡Libérame de inmediato!"

                    $ df_eye = "front05"
                    show didacf_mouth sad_Talkingx002
                    show didacf_eyebrows serious
                    call dfeye_lab
                    with dissolve

                    d "Nop."

                    $ df_eye = "front08"
                    show didacf_mouth sad_Silentx04
                    show didacf_eyebrows surprisex02
                    call dfeye_lab
                    with dissolve

                    p "..."

                    show day05 # Both hands
                    with hpunch

                    n "Ejerces vigor en tus extremidades"

                    n "para intentar ver si eres capaz de liberarte por ti mismo"

                    n "pero lo único que consigues es hacer ruido."

                    pt "¡La madre que la parió!"

                    hide day05

                    $ df_eye = "front05"
                    show didacf_mouth happy_Silentx06
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with fade

                    n "Una sonrisa pícara se dibuja en sus labios."
                
            "...":
                call p_Help
                $pl.ch_pts("dp",1)
                pass

    $ df_eye = "front01"
    show didacf_mouth sad_Silentx02
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Vas a ser así todos los días?"

    $ df_eye = "front04"
    show didacf_mouth happy_Talkingx03
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Es posible..."

    $ df_eye = "front05"
    show didacf_mouth happybiting_Silentx03
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "down04"
    show didacf_mouth happybiting_Silentx05
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "Dejas ir un profundo suspiro."

    if p_prot_analgesic == "accepted": 

        pass

    else:
        ## CONDITIONAL had you been dominant or submissive in Afternoon Sex?

        $ df_eye = "front01"
        show didacf_mouth sad_Silentx02
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "Si esas tenemos."

        $ df_eye = "down00"
        show didacf_mouth sad_Silentx01
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        n "Agarras a Dídac, y con un rápido gesto"

        scene day05
        with hpunch

        n "te pones encima de ella sobre tu cama."

        d "Uhhmmm..."

        d "Me gusta cuando te pones así."

        p "Eres una zorra."

        d "Quizás..."

        d "Fóllame [protname]."

    jump morning06_Df_Sex

    #### 

    
label morning06_Df_afterSex:

    ono "Riiiiiing"

    P "Uhhmm..."

    ## CONDITIONAL how tired is Didac here?

    d "¿Aún estás en la cama?"

    scene day05
    with fade

    n "Ves a Dídac de pie con una toalla"

    n "y con el pelo mojado"

    n "como si se hubiera terminado de duchar."

    p "¿Cómo es que tienes tanta energía?"

    $ df_eye = "front04"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "¿La cuestión es cómo es que tú aguantas tan poco?"

    p "..."

    d "Por cierto,"

    d "¿has visto lo que hay encima de la mesita de noche?"

    p "¿Euh...?"

    n "Al fijarte allí, ves lo que parece una tarjeta"

    n "y un papel con algo escrito al lado."

    p "¿Qué...?"

    n "Al mirar más detenidamente el trozo de plástico"

    n "ves que se trata de un {a=https://es.wikipedia.org/wiki/Documento_nacional_de_identidad_(España)}Documento nacional de identidad español{/a} con la foto de Dídac"

    n "pero con un nombre que pone {b}Ermerejilda{/b}."

    p "¿Qué demonios?"

    n "Al mirar el trozo de papel:"

    let "Con esto quizás no hará falta que se queme la yema de los dedos todos los días."

    let "Si el nombre no os gusta, siempre se lo puede cambiar."

    let "Todo es legal."

    let "Pero intentad que nadie hurgue demasiado en su pasado,"

    let "ni que tampoco le saquen sangre en el hospital,"

    let "tened en cuenta que aunque los papeles sean legales,"

    let "sigue siendo solo una fachada."

    let "Espero que con esto sea suficiente."

    let "P.D. Recuerda quemar esta carta si no quieres tener problemas."

    p "¿Qué...?"

    p "¿Cómo ha llegado esto aquí?"

    d "Y yo que sé."

    d "Estaba ahí cuando me desperté."

    p "¡¿Y no me lo has dicho hasta ahora?!"

    d "Si te lo hubiera comentado antes,"

    d "no habrías querido follar."

    p "..."

    p "Dídac,"

    p "¡alguien ha entrado en nuestra casa mientras estábamos durmiendo!"

    d "Sí,"

    extend " eso parece."

    p "¡¿Y no se te ha pasado por la cabeza que podría seguir estando por la casa?!"

    d "¡Por supuesto que sí!"

    d "¡¿Qué crees que he hecho antes de ponerme encima de ti?!"

    p "..."

    d "Pero he revisado todos los rincones de la casa"

    d "y la puerta no está forzada."

    d "Alguien debe de tener la llave,"

    d "¡o yo qué coño sé!"

    p "..."

    d "Pero has visto lo que es,"

    extend " ¿no?"

    p "Sí."

    d "¿Crees que ha sido ella?"

    p "¿Y quién si no?"

    d "¿Pero por qué lo ha hecho?"

    d "Después de haberla dejado tirada,"

    d "¿encima nos echa una mano?"

    p "..."

    p "Supongo que fue sincera al decir que no nos desea ningún mal."

    d "Hmmm..."

    pt "Aunque la forma en la que está escrita,"

    pt "no estoy seguro si realmente es de ella..."

    d "Como no te des prisa,"

    d "llegarás tarde."

    p "..."

    p "¿Por?"

    p "Suelo ponerme la alarma a una hora razonable."

    d "Te la he adelantado un poco..."

    p "¿Qué?!"

    d "Tampoco mucho..."

    d "Solo unos veinte o treinta minutos."

    p "¡¿QUÉ?!"

    n "Te levantas a toda prisa de la cama para recoger tus cosas del suelo."

    d "Si no lo hubiera hecho,"

    d "no habrías querido hacer nada."

    n "Te dice mientras te vistes a toda prisa."

    p "¡La madre que te parió Dídac!"

    p "¡Que necesitamos el dinero!"

    d "No seas tan dramático,"

    d "tampoco te van a echar porque llegues por primera vez unos minutos tarde."

    p "¡Ni se te ocurra volverlo hacer!"

    n "Le gritas mientras te diriges al baño."

    d "¡Pues entonces déjame bien satisfecha por la noche"

    d "y no te molestaré por la mañana!"

    p "¡SI LO HARÁS IGUAL!"

    d "..."

    ###

    n "Después de entrenar a los juveniles te diriges a la escuela de ilustración."

    pt "Por lo menos Dídac me ha hecho caso y no ha venido."

    jump morning06_Df_IllustSchoolIn

label morning06_Df_IllustSchoolIn:

    scene morning02_bg schoolwall
    with fade

    n "Buscas por todos lados a Neus,"

    n "pero no la encuentras por ninguna parte."

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

    $ m_exp_eyez = "front03"
    show m_exp_mouth sad_Silentx02
    show m_exp_eyebrows surprisex01
    call m_exp_label
    with dissolve

    p "Euh..."

    $ m_exp_eyez = "front02"
    show m_exp_mouth sad_Talkingx02
    show m_exp_eyebrows suspiciousx01
    call m_exp_label
    with dissolve

    tx "¿Ocurre algo?"

    if not morning03_Meritxell_Phonenumber_Accepted:

        p "No..."

        tx "..."

        n "Pasa de largo sin prestarte más atención."

        pt "¿De qué coño va esta tía?"

    else:

        if afternoon04_MACBA_TxellName_Know:

            $ m_exp_eyez = "front02"
            show m_exp_mouth sad_Silentx04
            show m_exp_eyebrows surprisex001
            call m_exp_label
            with dissolve

            p "Meritxell..."

        $ m_exp_eyez = "front03"
        show m_exp_mouth sad_Silentx03
        show m_exp_eyebrows surprisex02
        call m_exp_label
        with dissolve

        p "¿No te acuerdas de mí?"

        $ m_exp_eyez = "front03"
        show m_exp_mouth sad_Silentx05
        show m_exp_eyebrows suspiciousx02
        call m_exp_label
        with dissolve

        tx "..."

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Talkingx03
        show m_exp_eyebrows serious
        call m_exp_label
        with dissolve

        tx "Creo que vamos a la misma clase de ilustración, ¿verdad?"

        $ m_exp_eyez = "front05"
        show m_exp_mouth sad_Talkingx003
        show m_exp_eyebrows suspiciousx01
        call m_exp_label
        with dissolve

        tx "[protname],"

        extend " si mal no recuerdo."

        $ m_exp_eyez = "front02"
        show m_exp_mouth sad_Silentx03
        show m_exp_eyebrows serious
        call m_exp_label
        with dissolve

        p "Sí..."

        $ m_exp_eyez = "front01"
        show m_exp_mouth sad_Silentx03
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        p "¿No recuerdas nada más?"

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Talkingx04
        show m_exp_eyebrows suspiciousx02
        call m_exp_label
        with dissolve

        tx "¿Debería?"

        $ m_exp_eyez = "front03"
        show m_exp_mouth sad_Silentx04
        show m_exp_eyebrows suspiciousx01
        call m_exp_label
        with dissolve

        p "..."

        $ m_exp_eyez = "front08"
        show m_exp_mouth sad_Talkingx002
        show m_exp_eyebrows sadx01
        call m_exp_label
        with dissolve

        tx "Lo siento,"

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Talkingx05
        show m_exp_eyebrows angryx01
        call m_exp_label
        with dissolve

        tx "pero no creo que hayamos hablado mucho más."

        $ m_exp_eyez = "front08"
        show m_exp_mouth sad_Talkingx04
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        tx "De todos modos no creo que me vuelvas a ver por aquí."

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyebrows serious
        call m_exp_label
        with dissolve

        tx "Hoy es mi último día."

        $ m_exp_eyez = "front03"
        show m_exp_mouth sad_Silentx02
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        p "¿Por qué?"

        $ m_exp_eyez = "front08"
        show m_exp_mouth sad_Talkingx05
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        tx "En primer lugar,"

        $ m_exp_eyez = "right02"
        show m_exp_mouth sad_Talkingx06
        show m_exp_eyebrows suspiciousx01
        call m_exp_label
        with dissolve

        tx "porque ni siquiera recuerdo la razón por la que me apunté a estas clases."

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Talkingx004
        show m_exp_eyebrows sadx01
        call m_exp_label
        with dissolve

        tx "No es por ofender,"

        $ m_exp_eyez = "front08"
        show m_exp_mouth happy_Talkingx03
        show m_exp_eyebrows sadx01
        call m_exp_label
        with dissolve

        tx "pero realmente no lo necesito."

        $ m_exp_eyez = "front04"
        show m_exp_mouth sad_Silentx03
        show m_exp_eyebrows serious
        call m_exp_label
        with dissolve

        menu:

            pt "¿Ni siquiera lo recuerda?"

            "¿Entonces por qué crees que te apuntaste?":
                call p_Help

                $ m_exp_eyez = "front01"
                show m_exp_mouth sad_Silentx02
                show m_exp_eyebrows surprisex002
                call m_exp_label
                with dissolve

                pause 0.2

                $ m_exp_eyez = "front08"
                show m_exp_mouth sad_Talkingx05
                show m_exp_eyebrows sadx01
                call m_exp_label
                with dissolve

                tx "Como ya te he dicho,"

                extend " no lo recuerdo."

                $ m_exp_eyez = "front04"
                show m_exp_mouth sad_Silentx04
                show m_exp_eyebrows suspiciousx01
                call m_exp_label
                with dissolve

                p "..."

            "...":
                call p_Help

                pass

        $ m_exp_eyez = "front08"
        show m_exp_mouth sad_Talkingx04
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        tx "Bueno [protname],"

        $ m_exp_eyez = "front03"
        show m_exp_mouth happy_Talkingx04
        show m_exp_eyebrows sadx01
        call m_exp_label
        with dissolve

        tx "aunque no nos hayamos conocido con demasiada profundidad,"

        $ m_exp_eyez = "front04"
        show m_exp_mouth happy_Talkingx03
        show m_exp_eyebrows serious
        call m_exp_label
        with dissolve

        tx "espero que a ti sí te sirvan las clases."

        $ m_exp_eyez = "front03"
        show m_exp_mouth happy_Talkingx02
        show m_exp_eyebrows normal
        call m_exp_label
        with dissolve

        tx "Que tengas un buen día."

        $ m_exp_eyez = "front04"
        show m_exp_mouth happy_Silentx04
        show m_exp_eyebrows sadx01
        call m_exp_label
        with dissolve

        pause 0.2

        scene morning02_bg schoolwall
        with dissolve

        n "Sin decir otra palabra se aleja en dirección a la recepción."

        p "No recuerda absolutamente nada."

        if afternoon04_MACBA_TxellName_Know:

            p "Ni siquiera a Neus..."

    scene afternoon01_bg Toilet
    with fade

    n "Revisas por todos lados,"

    scene afternoon01_bg Bathroom
    with fade

    n "incluso en los murales que hay colgados por las paredes a lo largo de la escuela"

    n "en busca de alguna pista o información sobre ella."

    scene morning02_bg schoolwall
    with fade

    n "No encuentras ni uno de sus dibujos,"

    n "ni siquiera de otros compañeros de clase"

    n "dónde la hubieran retratado o mencionado,"

    n "ninguna foto en la que aparezca remotamente."

    n "Preguntas por todos lados, incluso en dirección,"

    n "y nadie se acuerda de ella,"

    n "como si nunca hubiera existido."

    if DidacPregnant:
        jump night06_Dmf_IllustSchoolAfter
    else:
        jump afternoon06_Dm_IllustSchoolAfter
        # It later goes to after schoold

    ###

label night06_Dmf_IllustSchoolAfter:

    # It's night (twilight) // It's either for Male Didac and Female Didac.

    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade

    if DidacPregnant:

        n "Después de las clases y del curso en educación física que impartes en el gimnasio"

        n "regresas al piso."

    else:

        pause 0.2

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "Dejas las llaves sobre la mesita de la entrada."

    with hpunch
    ono "CRASH"

    n "Oyes el ruido de un cristal rompiéndose."

    scene morning04_bg_livingroom_others_night_lightOn
    with fade

    p "¡Dídac!"

    if DidacPregnant:

        if afternight04__Anal_dick_med_Success > 0:
            show didacfbodycloth_top_mTail:
                didacm_body_atRight

        show didacfbodybelow_naked_drops 00:
            dfbody_atright
        show didacfhandr duster:
            dfbody_atright
        show didacfbodytop_naked_drops 00:
            dfbody_atright
        show didacfhandl hip_naked:
            dfbody_atright
        show didacfbodycloth_top maid:
            dfbody_atright

        show didacf_blush 03:
            dfexpressions_atright
        show didacf_eyes 05:
            dfexpressions_atright
        show didacf_pupils front05:
            dfexpressions_atright
        show didacf_eyebrows sadx01:
            dfexpressions_atright
        show didacfbodytop_hairBelow:
            dfbody_atright
        show didacf_mouth happybiting_Silentx04:
            dfexpressions_atright
        show didacfbodytop_hMask:
            dfbody_atright
        show didacfbodytop_hairTop:
            dfbody_atright
        show didacfbodytop_hairOver maid:
            dfbody_atright

    else:
        #show D_damagedIndifferent_body at right

        if afternight04__Anal_dick_med_Success > 0:
            show didacfbodycloth_top_mTail:
                didacm_body_atRight

        show didacmbody:
            didacm_body_atRight
        show didacmhandl rest:
            didacm_body_atRight

        show didacfhandr duster:
            dfbody_atright

        show didacmbodycloth_top maid:
            didacm_body_atRight
        
        show didacf_blush 03:
            didacm_exp_atRight
        show didacf_eyes 05:
            didacm_exp_atRight
        show didacf_pupils front05:
            didacm_exp_atRight
        show didacf_eyebrows sadx01:
            didacm_exp_atRight
        show didacfbodytop_hairBelow:
            didacm_bodyf_atRight
        show didacf_mouth happybiting_Silentx04:
            didacm_exp_atRight
        show didacfbodytop_hMask:
            didacm_bodyf_atRight
        show didacfbodytop_hairTop:
            didacm_bodyf_atRight
        show didacfbodytop_hairOver maid:
            didacm_bodyf_atRight

    $ df_eye = "front00"
    show didacf_mouth sad_Talkingx002
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "¡¿Qué?!"

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    n "Al llegar al comedor te lo encuentras llevando un delantal,"

    $ df_eye = "front01"
    show didacf_mouth sadbiting_Silentx02
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    n "un trapo en la boca"

    $ df_eye = "front03"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "y un plumero en la mano."

    $ df_eye = "front02"
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    p "¿Qué...?"

    $ df_eye = "front04"
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Joder..."

    $ df_eye = "front08"
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "Se me ha caído un vaso,"

    $ df_eye = "front03"
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "eso le puede pasar a cualquiera,"

    $ df_eye = "front04"
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡¿no?!"

    $ df_eye = "left04"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    pt "¿Un vaso en el comedor?"

    if DidacPregnant:

        $ df_eye = "front01"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Qué estás haciendo?"

        $ df_eye = "front03"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "¿A ti que te parece?"

    else:

        $ df_eye = "front02"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Ya estás bien?"

        $ df_eye = "front03"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "Me encuentro algo mejor..."

    $ df_eye = "front01"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¡Pero si nunca has limpiado la casa!"

    $ df_eye = "right03"
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Tanto como nunca!"

    $ df_eye = "right04"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Alguna vez lo he hecho..."

    $ df_eye = "front01"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "Hace más de dos años que no tocas una escoba."

    $ df_eye = "right01"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "right02"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Porque tú lo sueles hacer muy bien..."

    $ df_eye = "left01"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "front08"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Vale,"

    extend " vale..."

    $ df_eye = "front02"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Como ya me has repetido varias veces que no estoy trabajando"

    $ df_eye = "front03"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "ni generando ingresos para pagar el alquiler,"

    $ df_eye = "right02"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "he pensado que por lo menos podría echar una mano en algo."

    $ df_eye = "front01"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Pero de dónde has sacado este delantal?"

    $ df_eye = "down01"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "..."

    $ df_eye = "down02"
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Euhhh..."

    $ df_eye = "front06"
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Es una de las cosas que compré el otro día."

    $ df_eye = "right04"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Y ya sé que no es muy funcional para limpiar,"

    $ df_eye = "front08"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "pero es lo único que tenía a mano."

    $ df_eye = "front04"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Y sí..."

    $ df_eye = "front02"
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "Las orejas de gato venían con el pack."

    $ df_eye = "front04"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    menu:

        pt "Venían con el pack..."

        "Tampoco hacía falta que te pusieras esa diadema.":

            $ df_eye = "front01"
            show didacf_eyebrows surprisex01
            call dfeye_lab
            with dissolve

            p "Al fin y al cabo tampoco te recoge el pelo."

            $ df_eye = "down02"
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "..."

            $ df_eye = "front04"
            show didacf_eyebrows angryx01
            call dfeye_lab
            with dissolve

            d "¿Eso es que no te gustan?"

            $ df_eye = "right04"
            show didacf_eyebrows sadx01
            call dfeye_lab
            with dissolve

            menu:

                pt "Creo que ya se encuentra bastante mejor..."

                "En realidad no te queda mal.":
                    call p_Help
                    $pl.ch_pts("dp",1)

                    $ df_eye = "front01"
                    show didacf_eyebrows normal
                    call dfeye_lab
                    with dissolve

                    d "Hmmm..."

                    $ df_eye = "down03"
                    show didacf_eyebrows sadx01
                    call dfeye_lab
                    with dissolve

                    d "Yo opino igual."

                    $ df_eye = "front06"
                    show didacf_eyebrows sadx02
                    call dfeye_lab
                    with dissolve

                "Es un poco cutre.":
                    call p_Help
                    $pl.ch_pts("dp",-2)

                    $ df_eye = "front00"
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    pause 0.2

                    $ df_eye = "front01"
                    show didacf_eyebrows angryx04
                    call dfeye_lab
                    with dissolve

                    d "¡Tú sí que eres cutre!"

                    $ df_eye = "front08"
                    show didacf_eyebrows angryx03
                    call dfeye_lab
                    with dissolve

                "Me pone un poco cachondo, no te lo voy a negar.":
                    call p_Help
                    $pl.ch_pts("dp",2)

                    $ df_eye = "front01"
                    show didacf_eyebrows surprisex02
                    call dfeye_lab
                    with dissolve

                    d "..."

                    $ df_eye = "right02"
                    show didacf_eyebrows suspiciousx01
                    call dfeye_lab
                    with dissolve

                    d "Bueno,"

                    $ df_eye = "right03"
                    show didacf_eyebrows sadx01
                    call dfeye_lab
                    with dissolve

                    d "tampoco hace falta exagerar..."

                    $ df_eye = "right04"
                    show didacf_eyebrows sadx02
                    call dfeye_lab
                    with dissolve

                "...":
                    call p_Help
                    $pl.ch_pts("dp",-1)

                    $ df_eye = "front01"
                    show didacf_eyebrows angryx01
                    call dfeye_lab
                    with dissolve

                    d "Al menos podrías haber dicho algo."

                    $ df_eye = "front08"
                    show didacf_eyebrows angryx01
                    call dfeye_lab
                    with dissolve

            if afternight04__Anal_dick_med_Success > 0:

                menu:

                    pt "Tiene pinta de ser..."

                    "¿Y esa cola que tienes ahí colgando dónde está pegada?":
                        call p_Help

                        $ df_eye = "front00"
                        show didacf_eyebrows surprisex01
                        call dfeye_lab
                        with dissolve

                        pause 0.2

                        $ df_eye = "down01"
                        show didacf_eyebrows suspiciousx01
                        call dfeye_lab
                        with dissolve

                        d "¿Euh...?"

                        $ df_eye = "down02"
                        show didacf_eyebrows suspiciousx02
                        call dfeye_lab
                        with dissolve

                        d "Pues..."

                        $ df_eye = "front08"
                        show didacf_eyebrows angryx02
                        call dfeye_lab
                        with dissolve

                        d "¡Iba con el pack!"

                        $ df_eye = "right02"
                        show didacf_eyebrows suspiciousx01
                        call dfeye_lab
                        with dissolve

                        d "No iba a ir desconjuntada..."

                        $ df_eye = "front01"
                        show didacf_eyebrows serious
                        call dfeye_lab
                        with dissolve

                        p "Eso no es lo que te he preguntado."

                        $ df_eye = "left04"
                        show didacf_eyebrows angryx02
                        call dfeye_lab
                        with dissolve

                        d "..."

                        $ df_eye = "left05"
                        show didacf_eyebrows angryx01
                        call dfeye_lab
                        with dissolve

                    "...":
                        call p_Help
                        pass

        "...":
            call p_Help
            pass

###
    pause 0.2

    $ df_eye = "front08"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "También he aprovechado la mañana para buscar trabajo por internet."

    if not DidacPregnant:
        menu:

            pt "Cualquiera diría que se estaba casi muriendo esta mañana..."

            "Me parece una buena idea.":
                call p_Help

                $pl.ch_pts("dp",1)

                $ df_eye = "front01"
                show didacf_eyebrows normal
                call dfeye_lab
                with dissolve

                d "..."

                $ df_eye = "right02"
                show didacf_eyebrows serious
                call dfeye_lab
                with dissolve

                d "Ya..."

            "¿Seguro que ya te encuentras bien?":
                call p_Help

                $pl.ch_pts("dp",1)

                $ df_eye = "front02"
                show didacf_eyebrows serious
                call dfeye_lab
                with dissolve

                d "Sí..."

                $ df_eye = "front04"
                show didacf_eyebrows sadx01
                call dfeye_lab
                with dissolve

                d "Ya me encuentro bastante mejor."

            "...":
                call p_Help
                pass

    else:

        $ df_eye = "front01"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "¿Estás seguro que es una buena idea?"

        $ df_eye = "front02"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "¿Por qué no?"

        $ df_eye = "right01"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Al fin y al cabo el {a=https://es.wikipedia.org/wiki/Documento_nacional_de_identidad_(España)}DNI{/a} parece que es real,"

        $ df_eye = "front02"
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "¿no?"

        $ df_eye = "front03"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front08"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "Tampoco me voy a pasar toda la vida encerrada en este piso."

        $ df_eye = "front01"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "Recuerda que es muy arriesgado que termines en el hospital."

        $ df_eye = "front04"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Tranquilo,"

        $ df_eye = "front08"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "tampoco soy tan estúpida como para buscar trabajos que me puedan poner en peligro."

        $ df_eye = "front05"
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "Hmmm..."

        $ df_eye = "front02"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "Mis padres me han llamado."

        $ df_eye = "front03"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        p "¿Qué?"

        $ df_eye = "front01"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "¿Qué les has dicho?"

        $ df_eye = "right01"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        d "Por lo visto nada que no supieran ya."

        $ df_eye = "front02"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "¿A qué te refieres?"

        $ df_eye = "front03"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "Aparentemente alguien les ha puesto al día de la situación."

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Saben que ahora soy una mujer"

        $ df_eye = "front03"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "y que no deben decírselo a nadie más"

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "si no quieren poner mi vida en peligro."

        $ df_eye = "front01"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        p "¿Quién?"

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Esa es la parte más extraña,"

        $ df_eye = "front03"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "se han despertado con esa idea,"

        $ df_eye = "front02"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "como si alguien en sueños les hubiera contado todo."

        $ df_eye = "front02"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front03"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Lo más raro ha sido la naturalidad con la que parece que se lo han tomado..."

        $ df_eye = "left01"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "También me han dicho que se han pasado el día"

        $ df_eye = "left02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "quemando mis fotos de cuando era pequeño,"

        $ df_eye = "left01"
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "como si mi yo masculino nunca hubiera existido."

        $ df_eye = "left02"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front02"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "Aunque eso sí,"

        $ df_eye = "front08"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "me ha jodido bastante cuando mi madre me ha dicho"

        $ df_eye = "right04"
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "que está encantada de poder tener al fin una hija."

        $ df_eye = "right05"
        show didacf_eyebrows suspiciousx02
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Incluso he estado revisando mis redes sociales,"

        $ df_eye = "front03"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "todas mis fotos han desaparecido,"

        $ df_eye = "front01"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "incluso he perdido todas las amistades que tenía"

        $ df_eye = "right02"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "y cuando me he puesto a inspeccionar sus perfiles"

        $ df_eye = "front02"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        d "lo que más me ha sorprendido"

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "es que habían desaparecido todas las fotografías en las que aparecía yo."

        $ df_eye = "right01"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front02"
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "Tenías razón cuando dijiste que esta chica era un tanto extraña."

        $ df_eye = "left03"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        pt "No estoy muy seguro si ha sido ella sola la que ha hecho todo esto..."

        $ df_eye = "left04"
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        pt "Pero de ser así,"

        $ df_eye = "front08"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        pt "me pregunto por qué y quién la habrá ayudado."

    if pl.dp > 80:

        $ df_eye = "front02"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "Estoy pensando en dejarme el pelo largo..."

        $ df_eye = "front03"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        p "..."

        $ df_eye = "front04"
        show didacf_eyebrows sadx02
        call dfeye_lab
        with dissolve

        d "¿O crees que me queda mejor corto?"

        $ df_eye = "front05"
        show didacf_eyebrows sadx03
        call dfeye_lab
        with dissolve

        menu:

            pt "¿El pelo largo?"

            "Eso es cosa tuya.":
                call p_Help

                $ df_eye = "front01"
                show didacf_eyebrows normal
                call dfeye_lab
                with dissolve

                d "..."

                if DidacPregnant:

                    $ df_eye = "right04"
                    show didacf_eyebrows angryx02
                    call dfeye_lab
                    with dissolve

                    d "Que soso eres cuando quieres..."

                else:

                    $ df_eye = "front02"
                    show didacf_eyebrows sadx01
                    call dfeye_lab
                    with dissolve

                jump night06_Df_pinkClothes

            "Creo que te favorecería.":
                call p_Help

                $ df_eye = "front01"
                show didacf_eyebrows normal
                call dfeye_lab
                with dissolve

                d "..."

                $ df_eye = "front02"
                show didacf_eyebrows sadx01
                call dfeye_lab
                with dissolve

                d "Sí,"

                $ df_eye = "front06"
                show didacf_eyebrows normal
                call dfeye_lab
                with dissolve

                d "yo pienso lo mismo."

                jump night06_Df_pinkClothes

            "¿Por qué?":
                call p_Help

                jump night06_Df_grabHair

            "...":
                call p_Help

                $pl.ch_pts("dp",-1)

                $ df_eye = "front02"
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                d "Al menos podrías decirme qué opinas."

                $ df_eye = "front03"
                show didacf_eyebrows angryx02
                call dfeye_lab
                with dissolve

                p "..."

                $ df_eye = "right04"
                show didacf_eyebrows angryx01
                call dfeye_lab
                with dissolve

                d "Tssk..."

                jump night06_Df_pinkClothes

    else:

        jump night06_Df_pinkClothes


label night06_Df_grabHair:

    if DidacPregnant:

        $ df_eye = "front01"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "¿No te gustaría poder cogérmelo mientras me tienes a cuatro patas?"

    else:

        $ df_eye = "front01"
        show didacf_eyebrows normal
        call dfeye_lab
        with dissolve

        d "..."

        if pl.dp > 100:

            $ df_eye = "right04"
            show didacf_eyebrows sadx02
            call dfeye_lab
            with dissolve

            d "Por nada..."

        else:

            $ df_eye = "front02"
            show didacf_eyebrows suspiciousx01
            call dfeye_lab
            with dissolve

            d "¿Y por qué no?"

    jump night06_Df_pinkClothes

label night06_Df_pinkClothes:

    pause 0.2

    $ df_eye = "right01"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Por cierto..."

    $ df_eye = "front06"
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Espero que no te disguste el color rosa."

    $ df_eye = "front02"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "¿Por?"

    $ df_eye = "right01"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "Digamos que he intentado hacer una lavadora,"

    $ df_eye = "right02"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "y..."

    $ df_eye = "right03"
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    d "Bueno..."

    $ df_eye = "front08"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "La ropa que era blanca,"

    $ df_eye = "front06"
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "ya no es blanca."

    $ df_eye = "right04"
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    menu:

        pt "Un día volveré y no tendré casa."

        "¿Qué ofertas de trabajo has estado buscando?":
            call p_Help

            jump night06_Dmf_jobOffers


        "...":
            call p_Help

            jump night06_Dmf_smell

label night06_Dmf_jobOffers:

    $ df_eye = "front01"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    d "¿Euh?"

    $ df_eye = "front02"
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    d "Pues no sé..."

    $ df_eye = "front08"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "algo saldrá."

    if DidacPregnant:

        $ df_eye = "front08"
        show didacf_eyebrows surprisex02
        call dfeye_lab
        with dissolve

        d "Total,"

        $ df_eye = "front06"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "ahora que soy mujer"

        $ df_eye = "right03"
        show didacf_eyebrows serious
        call dfeye_lab
        with dissolve

        d "seguro que las ofertas de trabajo me lloverán del cielo."

        $ df_eye = "down02"
        show didacf_eyebrows sadx01
        call dfeye_lab
        with dissolve

        d "Especialmente con este cuerpo que tengo."

        $ df_eye = "front04"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "¿No crees?"

        $ df_eye = "front01"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

        p "Me parece que no sabes muy bien de lo que estás hablando."

        $ df_eye = "front04"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Psst..."

        $ df_eye = "right04"
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        d "¿Qué sabrás tú?"

        $ df_eye = "right05"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

    else:

        $ df_eye = "front01"
        show didacf_eyebrows surprisex02
        call dfeye_lab
        with dissolve

        p "Quizás ayudaría si practicaras un poco tu dibujo,"

        $ df_eye = "front02"
        show didacf_eyebrows suspiciousx01
        call dfeye_lab
        with dissolve

        p "retomaras tus estudios,"

        $ df_eye = "front02"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        p "o no fueras tan borde con tus clientes cuando haces de entrenador personal."

        $ df_eye = "right03"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

        d "..."

        $ df_eye = "front08"
        show didacf_eyebrows angryx01
        call dfeye_lab
        with dissolve

        d "Tampoco soy tan borde..."

        $ df_eye = "front08"
        show didacf_eyebrows angryx02
        call dfeye_lab
        with dissolve

    jump night06_Dmf_smell

label night06_Dmf_smell:

    pause 0.2

    n "Al prestar más atención a tu sentido del olfato,"

    $ df_eye = "front04"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    n "percibes un olor a quemado."

    $ df_eye = "front02"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    p "Dídac..."

    $ df_eye = "front03"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    p "¿No hueles eso?"

    $ df_eye = "front02"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "¿Qué?"

    $ df_eye = "left00"
    show didacf_eyebrows surprisex02
    call dfeye_lab
    with dissolve

    d "¡MIERDA!"

    show bg morning04_bg_livingroom_others_night_lightOn
    with dissolve

    n "Rápidamente se dirige a la cocina"

    n "y abre el pequeño horno que hay cerca de la nevera."

    d "¡Joder!"

    d "¡Me cago en todo lo que se menea!"

    p "..."

    hide bg

    $ df_eye = "front06"
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    d "¿Qué te parece si hoy volvemos a comer palomitas?"

    $ df_eye = "front05"
    show didacf_eyebrows sadx03
    call dfeye_lab
    with dissolve

    n "Dejas ir un profundo suspiro."

    $ df_eye = "front02"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    if DidacPregnant:

        p "Tranquila,"

    else:

        p "Tranquilo,"

    $ df_eye = "front02"
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "Ya intentaré cocinar algo yo,"

    $ df_eye = "front03"
    show didacf_eyebrows sadx02
    call dfeye_lab
    with dissolve

    p "no te preocupes."

    $ df_eye = "front08"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "Hmm..."

    $ df_eye = "front01"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    d "Quizás no es tan mala idea."

    $ df_eye = "front01"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    p "No lo habrás calcinado expresamente para darme a entender"

    $ df_eye = "front02"
    show didacf_eyebrows serious
    call dfeye_lab
    with dissolve

    p "que soy el único que sabe cocinar,"

    $ df_eye = "front03"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    p "¿verdad?"

    $ df_eye = "front04"
    show didacf_eyebrows angryx02
    call dfeye_lab
    with dissolve

    d "¡Que no joder!"

    $ df_eye = "front08"
    show didacf_eyebrows angryx03
    call dfeye_lab
    with dissolve

    d "¡De verdad que lo he intentado!"

    $ df_eye = "left03"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Si no se hubiera quemado,"

    $ df_eye = "front01"
    show didacf_eyebrows suspiciousx01
    call dfeye_lab
    with dissolve

    d "quizás habría sido hasta comestible."

    $ df_eye = "left02"
    show didacf_eyebrows sadx01
    call dfeye_lab
    with dissolve

    p "..."

    $ df_eye = "left03"
    show didacf_eyebrows suspiciousx02
    call dfeye_lab
    with dissolve

    pt "Entonces, gracias a que se ha carbonizado"

    $ df_eye = "front02"
    show didacf_eyebrows normal
    call dfeye_lab
    with dissolve

    pt "es posible que pueda vivir un día más..."

    $ df_eye = "front08"
    show didacf_eyebrows surprisex01
    call dfeye_lab
    with dissolve

    d "Bueno,"

    extend " qué le vamos a hacer..."

    show bg morning04_bg_livingroom_others_night_lightOn
    with dissolve

    n "Pone esa incinerada comida bajo el agua"

    n "y una vez cierra el grifo"

    n "vuelve al comedor."

    hide bg

    if DidacPregnant:
        jump night06_Df_horny

    else:
        jump night06_Dm_possibleHorny


label night06_Dm_possibleHorny:

    $ creditsRolling = False

    if pl.dp > 80 and afternight04__Anal_dick_med_Success > 0:
        $ creditsRolling = False

    else:
        $ creditsRolling = True
        # Credits Rolling

        $ day06_ending_city = "barcelona"
        call day06_ending_window

    if not creditsRolling:
        $ df_eye = "front08"
        show didacf_eyebrows surprisex01
        call dfeye_lab
        with dissolve

    d "Mientras tú cocinas,"

    d "yo puedo buscar una película."

    d "¿Tienes ganas de ver algún género en particular?"

    p "Podrías poner una porno."

    d "..."

    p "Es una broma, hombre."

    d "Muy gracioso el tío..."

    p "..."

    p "Oye..."

    d "¿Sí?"

    p "Te acuerdas de todo lo que ha pasado estos días,"

    p "¿no?"

    d "..."

    d "Sí."

    p "..."

    d "Pre-"

    extend "preferiría no tener que hablar de ello..."

    d "Ya me cuesta mirarte a la cara"

    if afternight04_sexbattle_started:

        d "después de lo que te obligué hacerme ayer..."

    else:

        d "después de lo que te he hecho pasar estos días..."

    p "..."

    p "Lo siento,"

    p "no debería haberte sacado el tema."

    d "No pasa nada, joder."

    d "Lo entiendo."

    d "Pero..."

    d "No podemos hablar de esto con nadie,"

    d "¿verdad?"

    p "Mejor que no."

    d "¿Ni con mis padres?"

    p "No,"

    extend " a menos que quieras ponerlos en peligro."

    d "..."

    d "Dios..."

### 
    
    if afternight04_Pussy_dick_med_Speed_0_Success > 0:

        d "Me llegaste a follar el coño..."

        if afternight04_Pussy_dick_deep_Speed_0_Success > 0:

            d "Hasta el fondo..."

    else:

        d "Aunque en realidad no llegaste ni a follarme..."

        if afternight04__Anal_dick_med_Success> 0:

            d "Bueno,"

            d "si no contamos por detrás..."

        else:

            d "Ni siquiera por detrás..."

    p "¡¿No me acabas de decir que no querías hablar de ello?!"

    d "¡Joder!"

    d "¡Ya lo sé!"

    d "¡Pero es que no puedo sacármelo de la cabeza!"

    p "..."

    p "No tendrás aún las mismas ganas de..."

    d "..."

#### Point of inflexion.

    if pl.dp > 80 and afternight04__Anal_dick_med_Success > 0:

        jump night06_Dm_horny

    else:

        jump night06_Dm_noHorny

label night06_Dm_noHorny:

    p "¿Dídac?"

    d "¡No joder!"

    p "Ahh..."

    if afternight04__Anal_dick_med_Success > 0:

        d "Aunque cuando me follaste por detrás,"

        d "tampoco estuvo tan mal..."

        if afternight04__Anal_dick_deep_Success > 0:

            d "Me la metiste entera y todo..."

    elif afternight04_Pussy_dick_med_Speed_0_Success > 0:

        d "Tampoco tengo coño ahora..."

    else:

        d "Aunque en realidad tampoco me la llegaste a meter."

        d "Ni siquiera por detrás..."

    p "..."

    d "¡Que es una broma, hostias!"

    p "Ya..."

    if girl_1.orgasm == 1:

        d "Aunque vaya pedazo de orgasmo me diste..."

        d "A pesar de que fuera solo uno."

    elif girl_1.orgasm > 1:

        d "Aunque vaya pedazo de orgasmos me diste..."

        if girl_1.orgasm == 2:

            d "A pesar de que fueran solo dos..."

        elif girl_1.orgasm > 4:

            d "Creo que después del cuarto ya perdí la cuenta..."

    else:

        d "Aunque es una lástima que no me dieras ni un solo orgasmo..."

    p "¡Dídac!"

    d "¡Te juro que ya paro!"

    p "..."

    p "¿Se te está poniendo dura?"

    d "¿Y tú por qué me miras el paquete?"

    p "¡Por que no dejas hablar del tema!"

    d "Al final resultará que el pervertido de verdad aquí eres tú."

    p "Me dice el que no deja de hablar del tema..."

    d "¡Pero si has empezado tú!"

    p "¡Solo quería saber si volvías a ser el de antes!"

    d "..."

    d "¿Y lo soy?"

    p "..."

    window hide dissolve
    pause

    call false_gameover

    jump textless_gameover

    ## Ending Didac Male where he is not horny for you.

label night06_Dm_horny:

        # p "¡¿No me acabas de decir que no querías hablar de ello?!"
        # d "¡Joder!"
        # d "¡Ya lo sé!"
        # d "¡Pero es que no puedo sacármelo de la cabeza!"
        # p "..."
        # p "No tendrás aún las mismas ganas de..."
        # d "..."

    p "..."

    d "..."

    p "¿Dídac?"

    d "¡¿Qué?!"

    p "Te he hecho una pregunta."

    d "Tssk..."

    d "No soy sordo..."

    p "¿Pues entonces por qué no me respondes?"

    d "¡Por que no te va a gustar la respuesta!"

    p "..."

    d "..."

    p "¿Lo dices en serio?"

    d "..."

    d "¡¿Por qué coño me te tuviste que follar el culo?!"

    p "¿Qué...?"

    d "Sí [protname],"

    d "sí..."

    d "Tu polla sigue poniéndome cachondo."

    p "¡Pero ahora eres un tío!"

    d "¡Ya lo sé joder!"

    p "¿Entonces?"

    jump night06_DmS_start

    # Here Didac is male, but still is really horny for you.


##########################################################################################
##########################################################################################
#############################################
#############################################
##########################################################################################
##########################################################################################
##########################################################################################

label night06_Df_horny:

    $ df_eye = "front02"
    show didacf_eyebrows angryx01
    call dfeye_lab
    with dissolve

    d "Pero antes de ir al postre,"

    show didacfhandr leg_naked

    $ df_eye = "front03"
    show didacf_eyebrows angryx02
    show didacf_mouth happybiting_Silentx04
    call dfeye_lab
    with Dissolve(0.75)

    n "Ves que una a una se va quitando va quitando la ropa."

    hide didacfbodytop_hMask
    
    $ df_eye = "front05"
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Talkingx002
    call dfeye_lab
    with Dissolve(0.75)

    d "toca el plato principal."

    hide didacfbodycloth_top

    $ df_eye = "front04"
    show didacf_eyebrows sadx02
    show didacf_mouth happybiting_Silentx05
    call dfeye_lab
    with Dissolve(0.75)

    pause 0.75

    $ df_eye = "front01"
    show didacf_eyebrows serious
    show didacf_mouth sadbiting_Silentx02
    call dfeye_lab
    with dissolve

    p "Dídac..."

    $ df_eye = "front08"
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx09
    call dfeye_lab
    with dissolve

    d "¡NO ME JODAS!"

    $ df_eye = "front01"
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx004
    call dfeye_lab
    with dissolve

    d "¡Que llevo todo el puto día aquí encerrada"

    $ df_eye = "front03"
    show didacf_eyebrows sadx02
    show didacf_mouth happy_Talkingx05
    call dfeye_lab
    with dissolve

    d "y necesito que me des un poco de caña!"

    $ df_eye = "front05"
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    call dfeye_lab
    with dissolve

    d "¡No me seas rata!"

    $ df_eye = "front04"
    show didacf_eyebrows sadx02
    show didacf_mouth happybiting_Silentx04
    call dfeye_lab
    with dissolve

    p "..."

    $ Pedrera_char_Cond = "DidacClose"
    call Pedrera_char_lab

    show bg morning04_bg_livingroom_others_night_lightOn

    $ df_eye = "down03"
    show didacf_eyebrows sadx03
    show didacf_mouth happybiting_Silentx05
    call dfeye_lab
    with Dissolve(0.5)

    n "Ves que se te acerca sutilmente."

    $ df_eye = "front04"
    show didacf_eyebrows sadx01
    show didacf_mouth happy_Talkingx03
    call dfeye_lab
    with dissolve

    d "Además,"

    $ df_eye = "down05"
    show didacf_eyebrows sadx03
    show didacf_mouth happy_Talkingx04
    call dfeye_lab
    with dissolve

    d "seguro que ya estás algo más cargadito que esta mañana..."

    $ df_eye = "front05"
    show didacf_eyebrows angryx02
    show didacf_mouth happy_Silentx05
    call dfeye_lab
    with dissolve

    pause 0.2

    scene black
    with hpunch
    p "¡Ugh!"

    n "Con un fuerte empujón te lanza sobre el sofá."

    jump night06_DfHome_credits

    #####

label night06_DfHome_credits:
    $ day06_ending_city = "barcelona"
    call day06_ending_window

    p "¿No decías que era mejor hacerlo en la cama?"

    d "No tenemos por qué hacerlo siempre en el mismo sitio,"

    d "además estoy demasiado caliente para esperar a llegar a la habitación."

    p "¿No será que en realidad te mola hacerlo en el primer lugar dónde lo hicimos?"

    d "Tssk..."

    d "Puede..."

    p "Algún día podrías intentar ser algo más femenina, también."

    d "¿Y eso qué coño significa?"

    p "..."

    p "Por lo menos ser algo más delicada."

    d "..."

    d "Mientras se te ponga así de dura..."

    p "Mira que eres básica cuando quieres."

    d "Como si eso no te gustara."

    p "Podrías pasarle un poco la lengua."

    d "¡Pero si ya está dura!"

    p "..."

    if afternight04__MMouth_dick_Success > 0:

        d "Vale,"

        d "¡pero ni se te ocurra correrte en mi boca!"

        p "No parece que te disgustara tanto la última vez."

        d "¡No me seas imbécil!"

        p "Hmmm..."

        p "La verdad es que cada vez se te da mejor..."

        d "Ghhmm..."

    else:

        d "No pienso meterme eso en la boca."

        p "Pero sin embargo no tienes ningún reparo que en te folle el coño"

        p "que no hace ni tres días que tienes."

    d "Si no estuviera tan cachonda te metería de hostias..."

    p "Pero si siempre estás cachonda."

    d "..."

    p "¡AUH!"

    p "¡Me has hecho daño!"

    d "¡Te lo mereces!"

    p "..."

    d "Joder..."

    d "¿Por qué coño me pones tan caliente?"

    p "..."

    p "¿Vas a ser así todos los días?"

    d "No."

    d "Voy a ser mucho peor..."

    p "..."

    window hide dissolve
    pause

    call false_gameover

    jump textless_gameover



    # Una cosa que sí te comenta es... espero que te guste el color rosa. Cuando te dice el por qué es porque en la lavadora ha mezclado ropa de color blanco con su lencería rojca y ahora todo lo que era blanco es ahora de color rosado.

    # Cuando le pregutnas de qué va a trabajar, te dice.. yo que sé... de algo... total ahora soy mujer, seguro que las ofertas de trabajo me lloverán del cielo. ## Tú mejor ni respondes.

    # Hasta te comenta que ha intentado hacer la cena... pero quizás mejor que hoy volvais a comer palomitas...

    # Aunque antes... Empieza a desnudarse.

    # Ya no puedo más protname.

    # Fóllame de una vez.

    # Dios... esto será la historia del nunca acabar...







    ### Didac te pide de volver a follar y tú le dices, no sé tú, pero yo tengo algo de hambre y además estoy bastante cansado.

    ## A la mañana del día siguiente si Dídac está embarazada estará encima de ti montándote de buena mañana, puedes seguir y cuando terminais te comenta que hay algo sobre la mesita de noche.


    # Documentos de Dídac, con su DNI con un nuevo nombre e identidad, con los mismos padres con un papel en el que pone.

    # Con esto quizás no hará falta que se queme la yema de los dedos cada día, si el nombre no os gusta siempre os lo podéis cambiar. Espero que con esto sea suficiente. # O algo así.




    ## DADDY CAN  POSSESS DIDAC AND TELL NEUS GET THE FUCK OUT HERE IF SHE TRIES TO DO ANYTHING.

    # REMINDER, if she weren't pregnant, she could earse her memory and the continue the date once you get to the station to get to the TIBIDABO.



    # ne "¿Puedo saber por qué no has venido?"

    # NOPE, NOPE NOPE... you told her about Didac... so fuck it! she asks you about him!

    # ne "¿Puedo saber qué ha pasado?"

    # p "..."

    # ne "¿Por qué no has venido a la última cita?"

    # p "Yo..."

    # n "Después de la cita de ayer, yo pensé que... que tampoco había ido tan mal..."

    # ne "¿Tanto... tanto te disgustó lo que te hice ayer en la Pedrera?"

    # p "No, no es eso."

    # ne "¿Entonces por qué?"


    # here is where you wake up after having sex with Didac and the phone rings.
    # Is Neus asking you where are you. It's DATE TIME.. you must take a decision, but before you can do such thing, Didac takes the phone of your hand and hangs up the phone.

    # If you don't call her back Neus gets back to your home and rings the bell.
    # You get down the stairs to talk with her far from Didac.
    # There she asks you what's happening, why didn't you come to the date as you pacted.
    # Then appears Didac in lingerie telling her you don't need to go since she is already accepting being a woman.

    # Neus asks you what's the meaning of this...

label morning06_Dm_wakeUp:

        # n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."
        # n "Pero hay otro sonido extraño que te llama la atención."

    scene morning04_bg bedroom_neus_a
    show light 01:
        light01_rightside_position

    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0

    show morning04_bedroom_DMast_blinkeye

    show light_screen_01:
        light_screen_01_position
    with fade

    d "¡Ughhh...!"

    show morning04_bg bedroom_neus_c
    with Dissolve(0.75)

    p "¡Dídac!"

    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 00

    # show light 01:
    #     light01_leftside_position

    show light_screen_01:
        light_screen_01_position
    with fade

    n "Te levantas de la cama al descubrir a tu compañero de piso sudando mares"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows sadx03
    with dissolve

    n "con una notable expresión de dolor."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "AAagghh..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    pt "¿Me lo parece a mí, o...?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx04
    with dissolve

    n "No solo su cuerpo está cubierto de sudor,"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    n "sino que además tienes la sensación de que su busto ha disminuido de tamaño"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx02
    with dissolve

    n "pero sin embargo tanto su altura como su volumen han aumentado."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    pt "¿Está convirtiéndose de nuevo en un hombre?"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Uughh...!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "Dídac,"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "¿estás bien?"

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿A ti te parece que estoy bien?!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "¿Quieres que te traiga una aspirina?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Te lo agradecería..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx04
    with dissolve

    pause 0.2

    show black
    with fade

    n "Te diriges a la cocina mientras oyes de fondo sus gruñidos de dolor."

    hide black

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with fade

    p "Ten,"

    extend " tómate esto."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows sadx03
    with dissolve

    d "Joder..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¿Qué coño me pasa?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "Creo que te estás convirtiendo en hombre otra vez."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡La madre que me puto parió!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¿Por qué coño tiene que doler tanto?"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    ono "RIIIING"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup right03
    show didac_bed_d_eyebrows surprisex01
    with dissolve

    pause 0.2

    show morning04_bg_livingroom_mc_resting_phone home:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with Dissolve(0.5)

    n "Te acercas al despertador de la mesita y desactivas la alarma."

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx01
    with Dissolve(0.5)

    n "Luego vuelves con Dídac."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Ghhh..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¿Qué coño haces ahí...?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "¿Qué...?"

    p "¿A qué te refieres?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "No te quiero ahí mirándome como un imbécil."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx01
    with dissolve

    p "¿Y qué coño quieres que haga?"

    show didac_bed_d_mouth sad_Talkingx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¿Es que no te acaba de sonar la alarma?"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "Sí..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¿Pues a qué coño esperas?"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "Dídac,"

    extend " no te voy a dejar solo."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Pues claro que me vas a dejar solo!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup right03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "No quiero que luego esos mocosos me echen a mi la culpa"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "de que su entrenador no haya acudido a entreno."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "Los chavales lo entenderán."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Me da igual!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "No te quiero aquí como una estatua mirándome todo el rato!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Dídac..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "Ya me has dado la aspirina,"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "¿no?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¿Qué más vas a hacer aparte de mirarme?!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "¿Y si te pasa algo?"

    show didac_bed_d_mouth sad_Talkingx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¿Qué coño me va a pasar?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows serious
    with dissolve

    d "Ya lo has dicho antes,"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "simplemente me estoy transformando."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "Joder..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup right03
    show didac_bed_d_eyebrows serious
    with dissolve

    d "Si me pasa algo ya tengo el móvil para llamarte."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "¿Estás seguro?"

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Pues claro que estoy seguro!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¡Lárgate de una vez!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "Después de entreno volveré para ver cómo estás."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¡Y luego te largas de nuevo para clase de ilustración!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    p "Dídac..."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¡No me discutas o me pongo de pie y te doy una hostia!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¡Que te largues joder!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    pause 0.2

    scene afternight03_bg_room02_day
    with fade

    n "Un poco a regañadientes,"

    n "te vistes, te acicalas en el baño,"

    scene afternight03_bg entrance_lighton
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with fade

    pause 0.2

    hide afternight03_bg_entrance_keysmc
    with dissolve

    n "y te dispones a ir a entrenar a los chicos"

    scene black
    with fade

    pause

    scene afternight03_bg entrance_lightoff
    show afternight03_bg_entrance_keysmc empty:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lightoff:
        afternight03_bg_entrance_keys
    with fade

    pause 0.2

    show afternight03_bg_entrance_keysmc lightoff
    with dissolve

    n "Después del entreno regresas."

    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 04
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    show didac_bed_d_hair 04
    show didac_bed_headtowel wet
    show didac_bed_d_blanket 01
    with fade

    n "Dídac está igual que antes,"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    n "entre gemidos de dolor y sudando por todas partes."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows sadx02
    with dissolve

    n "Le vuelves a dar otra aspirina."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx03
    with dissolve

    pt "Ni siquiera las aspirinas de Arkham consiguen calmarlo demasiado..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "Ya me has dado la aspirina."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "Sí..."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "¡Pues lárgate joder!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "¿Estás seguro?"

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    n "Ves que hace el intento de ponerse de pie."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Vale,"

    extend " vale..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "Ya me largo."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx01
    with dissolve

    p "Mira que eres imbécil a veces cuando quieres."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "Tsskk..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "Mira quien..."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx01
    with dissolve

    pause 0.2

    scene afternight03_bg entrance_lightoff
    show afternight03_bg_entrance_keysmc lightoff:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lightoff:
        afternight03_bg_entrance_keys
    with fade

    pause 0.2

    hide afternight03_bg_entrance_keysmc
    with dissolve

    n "Cogiendo el metro de te diriges a la escuela de ilustración."

    jump morning06_Df_IllustSchoolIn


label afternoon06_Dm_IllustSchoolAfter:

        # n "Preguntas por todos lados, incluso en dirección,"
        # n "y nadie se acuerda de ella,"
        # n "como si nunca hubiera existido."

    scene afternight03_bg entrance_lightoff
    show afternight03_bg_entrance_keysmc empty:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lightoff:
        afternight03_bg_entrance_keys
    with fade

    pause 0.2

    show afternight03_bg_entrance_keysmc lightoff
    with dissolve

    n "Desde el recibidor de vuestro piso oyes de lejos sus gemidos de dolor,"

    n "los cuales suenan cada vez más varoniles."

    $ saturation_tint_level = "candle"

    scene beds_afternoon_lightOff_blindDown_Dbusy02MCempty
    show beds_D02
    with fade

    p "Dídac..."

    scene didac_bed_bed over_sweaty
    show didac_bed_d_body 03
    show didac_bed_d_sweat 03-04
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx02
    show didac_bed_d_hair 03
    show didac_bed_headtowel wet
    show didac_bed_d_blanket 01
    with fade

    n "Observas que su cuerpo va recuperando su antiguo tamaño y volumen."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Talkingx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "¿Cuánto coño va a durar esto?"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx03
    with dissolve

    p "Creo que no te falta mucho."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Espero que no..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows sadx03
    with dissolve

    p "¿Quieres otra aspirina?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Te lo agradecería."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx02
    with dissolve

    pause 0.2

    show black
    with fade


    n "Después de ir a la cocina y preparar el vaso regresas con él."

    hide black

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with fade

    p "Toma."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows sadx02
    with dissolve

    d "Ughh..."

    show didac_bed_d_mouth sad_Talkingx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "Te juro que no tengo ni puta idea si esta mierda sirve de algo."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows suspiciousx01
    with dissolve

    p "Es mejor que nada."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "Tssk..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup front07
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Talkingx03
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¿Qué coño haces ahí?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx01
    with dissolve

    d "¿No tienes que ir al gimnasio?"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx01
    with dissolve

    p "Puedo saltarme un día."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx03
    with dissolve

    d "La madre que te parió..."

    show didac_bed_d_mouth sad_Talkingx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Lárgate de una vez!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx03
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup front06
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pt "Después de todo necesitamos el dinero."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows serious
    with dissolve

    p "Espero que estés mejor cuando vuelva."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 08
    show didac_bed_d_eyespup front08
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Lárgate!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx02
    with dissolve

    pause 0.2

    show didac_bed_d_mouth happy_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pause 0.2

    scene aftermorning04_bg_gothicquarter_02
    with fade

    pause 0.2

    show aftermorning04_bg_gothicquarter_03
    with Dissolve(2.0)

    n "Cuando el sol yace cerca del horizonte regresas a casa."

    jump night06_Dmf_IllustSchoolAfter
        # n "Al llegar a casa y dejar las llaves sobre la mesita de la entrada."
        # ono "CRASH"
        # n "Oyes el ruido de un cristal rompiéndose."
        # p "¡Dídac!"



