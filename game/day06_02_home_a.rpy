

default day06_night_homeDidacMale = False
default beds_time = ""

default DidacStillMemory = False

label day06_night_home:

    #$ pdaytime = "06morning"
    $ pday_day = 6

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    $ day06_home_tablePhone = True
    if MShooter_Bracelet in MShooter_Bracelet_var:
        $ day06_home_tableBracelet = True
    else:
        $ day06_home_tableBracelet = False

    # You wak up at home at night, but if you were raped by Neus, you can't move and then wake up at next morning.

    # aj "You wake up at your home, with DIDAC or not (Depend if it's pregnant)"
    # progcheck "Is Didac Pregnant?"
    # 
    if p_ao_started:

        call day06_home_energySucked
        # It's gonna be Tuesday.

    # else:
    #     # It's Monday.

    pause

    $ saturation_tint_level = "default"

    n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."

    if DidacPregnant:
        ##Didac is not at home.
        jump day06_night_homeWithoutDidac
    else:
        jump day06_home_withDidac


label day06_home_energySucked:

    $ pdaytime = "06night"
    $ pday_day = 6

    $ saturation_tint_level = "verydark"

    pause

    with hpunch
    ono "RIIIIING"

    # You can't move at night. Monday at Night.

    pt "¿Qué...?"

    n "Reconoces la particular alarma de tu móvil."

    pt "¡¿Por qué diablos está sonando ahora?!"

    scene morning04_bg bedroom_neus_a_night
    show morning04_bedroom_DMast_blinkeye
    with fade_long1s

    n "Consigues entreabrir tus ojos y descubres que estás en un lugar bastante familiar."

    show morning04_bg bedroom_neus_b_night
    with Dissolve(0.5)

    pt "¡¿Qué...?!"

    show morning04_bg bedroom_neus_c_night
    with Dissolve(0.5)

    pt "¡¿Qué diablos hago en mi habitación?!"

    scene black
    with fade



    if DidacPregnant:

        $ beds_time = "_night_lightOff_blindUp_DemptyMCbusy"

        p "Ughh..."

        scene beds__comp_bracelet_phone
        #show beds_D02
        show morning04_bedroom_DMast_blinkeye
        with fade

        pt "¡¿Dónde está Dídac?!"

    else:

        $ beds_time = "_night_lightOff_blindUp_Dbusy02MCbusy"

        d "¡Uuughh!..."

        scene beds__comp_bracelet_phone
        show beds_D02
        show morning04_bedroom_DMast_blinkeye
        with fade

        p "¡¿Dídac?!"

        p "¡¿Eres tú?!"

    scene morning04_bg bedroom_neus_c_night
    show morning04_bedroom_DMast_blinkeye
    with fade_long1s

    n "Intentas levantarte,"

    with vpunch

    n "pero descubres que eres incapaz de mover un solo músculo de tu cuerpo."

    pt "¡Maldita sea!"

    pt "¡Me duele todo el cuerpo!"

    n "Cuando te fijas en tu cuerpo,"

    n "descubres un bulto en la sábana que te cubre a la altura de tu entrepierna."

    pt "¡¿En serio?!"

    pt "¡¿Por qué cojones sigue dura?!"

    if DidacPregnant:
        $ beds_time = "_night_lightOff_blindUp_DemptyMCbusy"
        scene beds__comp_bracelet_phone:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5

        #show morning04_bedroom_DMast_blinkeye
    else:  
        $ beds_time = "_night_lightOff_blindUp_Dbusy02MCbusy"
        scene beds__comp_bracelet_phone:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
        show beds_D02:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
        #show morning04_bedroom_DMast_blinkeye
    with fade


    n "Te fijas en la ventana y ves que el cielo está oscuro."

    pt "¿Está amaneciendo o anocheciendo?"

    if not DidacPregnant:

        d "¡UUghhh...!"

        pt "Está gimiendo de dolor,"

        pt "como cuando se transformó en mujer."

    n "Sigues intentando mover tu cuerpo,"

    n "pero apenas eres capaz de mover tus dedos."

    pt "Mierda..."

    pt "Después de lo que me hizo [neusname],"

    pt "lo que me sorprende es que siga con vida..."

    if not DidacPregnant:

        pt "¡¿Pero qué diablos estamos haciendo en nuestra habitación?!"

    else:

        pt "¡¿Pero qué diablos estoy haciendo en mi habitación?!"

    scene morning04_bg bedroom_neus_c_night
    show morning04_bedroom_DMast_blinkeye
    with fade_long1s

    n "Sientes tus párpados cada vez más pesados."

    pt "¡No!"

    extend " ¡No!"

    show morning04_bg bedroom_neus_b_night
    with Dissolve(1.0)

    pt "¡No puedo volver a dormirme!"

    pt "¡Tengo que saber qué demonios está ocurriendo!"

    show morning04_bg bedroom_neus_a_night
    with Dissolve(1.0)

    pt "Tengo que levantarme..."

    pt "Tengo que..."

    scene black
    with fade

    return


label day06_home_withDidac:

    $ saturation_tint_level = "default"

    if p_ao_started:
        # It's Tuesday.
        $ pdaytime = "07morning"
        $ pday_day = 7
    else:
        # It's Monday.
        $ pdaytime = "06morning"
        $ pday_day = 6

    $ day06_night_homeDidacMale = True

    scene morning04_bg bedroom_neus_a
    show light 01:
        light01_rightside_position
    show white:
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade_long1s
    
    window hide dissolve
    pause

    n "Pero hay otro sonido extraño que te llama más la atención."

    show morning04_bg bedroom_neus_b
    with Dissolve(0.5)

    d "¡Ughhh!"

    if p_ao_started:

        pt "Es Dídac..."

    else:

        pt "¡¿Es Dídac?!"

    n "Sientes tu cuerpo entumecido y apenas eres capaz moverte,"

    show morning04_bg bedroom_neus_c
    with Dissolve(0.5)

    n "pero con esfuerzo logras sentarte sobre la cama."

    scene black
    with vpunch

    n "Caes de rodillas sobre el suelo y agarrándote a su cama,"

    n "logras acercarte a él."

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01

    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade

    pt "Está sudando como hace tres días..."

    if p_ao_started:

        pt "¿O son cuatro ya?"
        $ beds_time = "_morning_lightOff_blindUp_Dbusy01MCmessy"

    else:
        $ beds_time = "_morning_lightOff_blindUp_Dbusy02MCbusy"


    scene beds__comp_bracelet_phone:
        truecenter
        zoom 2.5 xpos 0.85 ypos 1.2
        ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5

    if p_ao_started:
        show beds_D01b:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    else:
        show beds_D02b:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Cuando alzas la vista para fijarte en la ventana,"

    n "descubres que está amaneciendo."

    if p_ao_started:

        pt "¡¿Cuanto tiempo llevo durmiendo?!"

    else:

        pt "¡¿Me he pasado el día entero durmiendo?!"

    d "¡Uugh!"

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    show light_screen_01:
        light_screen_01_position
        alpha 0.5
    with fade

    p "¿Estás bien?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿A ti qué coño te parece?!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    pt "Supongo que ha sido una pregunta estúpida..."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "¿Necesitas una aspirina?"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "Ayudaría..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pause 0.2

    scene beds__comp_bracelet_phone:
        truecenter
        zoom 2.5 xpos 0.85 ypos 1.2
        ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5

    if p_ao_started:
        show beds_D01b:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    else:
        show beds_D02b:
            truecenter
            zoom 2.5 xpos 0.85 ypos 1.2
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Con esfuerzo, te agarras a la mesita de noche y a pesar del temblor de tus piernas, consigues ponerte de pie."

    scene afternight03_bg_hallway_day
    with fade

    n "Agarrándote a la pared y vigilando cada paso consigues llegar a la cocina,"

    n "Donde rellenas un vaso de agua y coges la caja de aspirinas."

    n "Con la misma fragilidad, regresas a vuestra habitación."

    scene 01_aspiring_b_bg
    show 01_aspirin:
        truecenter
        zoom 0.6
        ease 2.0 zoom 0.5
    show light_screen_01:
        light_screen_01_position
        alpha 0.5
    with fade

    p "Espero que esto te ayude."

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    show light_screen_01:
        light_screen_01_position
        alpha 0.5
    with Dissolve(1.0)

    pause 0.2

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "¿Y a ti qué te pasa?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "No te preocupes por mi."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Pareces un jodido anciano."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "¿Acaso te has visto en un espejo?"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Hehe-"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Ugh!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Joder,"

    extend " yo también espero que funcione."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "No sé qué coño me está pasando..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡¿Qué demonios bebimos ayer?!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "¿Bebimos?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "No tengo ni la más jodida remota idea de qué coño hicimos ayer..."

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    pt "¿No se acuerda de nada?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¡¿En qué mierda de garito nos metimos para que estemos así de mal, joder?!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    if p_ao_started:

        pt "Su cuerpo ya casi vuelve a ser el de siempre..."

    else:

        pt "¿Acaso no ve que aún conserva parte de su cuerpo femenino?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡¿Y por qué coño estoy peor que tú?!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¿Acaso me dejaste beber alguna mierda extraña?"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "Sueles tomarte cosas raras sin preocuparte de las consecuencias, Dídac."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Por eso te pregunto, joder!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Quizás tendríamos que ir al hospital..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    pt "No se acuerda de nada."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Pero por alguna extraña razón,"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    d "tengo la sensación de que eso sería una mala idea..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¡¿Se me estará yendo la cabeza?!"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    pt "pero sin embargo,"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    pt "sospecha que no debe ir al hospital..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pt "¡¿Qué demonios le habrán hecho en su memoria?!"

    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve


    jump day06_home_withDidac_footbal

# label day06_home_withDidac_school:

#     # It's morning and you should go to school.


label day06_home_withDidac_footbal:

    #It's MONDAY morning... SO MAKES NO SENSE THIS SCENE NOW.
    pause 0.2

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02

    with hpunch
    ono "RRIIIINNNGG"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Arghh!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¿Es tu jodida alarma?"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "Eso parece."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¿Qué cojones hace sonándote la alarma a estas horas?"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    pause 0.2

    scene 01_aspiring_b_bg

    if p_ao_started:
        show morning04_bg_livingroom_mc_resting_phone_home_tuesday:
            xpos 0.485 ypos 0.125

    else:
        show morning04_bg_livingroom_mc_resting_phone_home_monday:
            xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    show light_screen_01:
        light_screen_01_position
        alpha 0.2
    with Dissolve(1.0)

    n "Aún de rodillas, alargas tu brazo para coger el móvil,"

    n "y cuando te fijas en la hora que es:"

    p "Mierda..."

    d "¿Qué?"

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    show light_screen_01:
        light_screen_01_position
        alpha 0.2
    with Dissolve(1.0)

    p "En una hora tengo entreno con los {a=https://es.wikipedia.org/wiki/Fútbol_base}alevines{/a}."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "Esta semana me toca la sustitución por la mañana."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¡¿Esos mocosos entrenan a estas horas de la mañana en un fin de semana?!"

    if p_ao_started:

        show didac_bed_d_mouth sad_Silentx03
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows normal
        with dissolve

        p "Hoy es Martes."

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        d "..."

        show didac_bed_d_mouth sad_Talkingx02
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        d "¿Has dicho Martes?"

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows surprisex02
        with dissolve

        p "Así es."

        show didac_bed_d_mouth sad_Talkingx04
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        d "¡¿Y qué coño ha pasado con el Lunes?!"

        show didac_bed_d_mouth sad_Silentx03
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        p "..."

        show didac_bed_d_mouth sad_Silentx02
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup upleft03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        pt "Lo dice como si recordara lo que ha hecho estos últimos días..."

        show didac_bed_d_mouth sad_Talkingx04
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows normal
        with dissolve

        d "¡¿Qué cojones hicimos ayer?!"

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

        p "Básicamente dormir."

        show didac_bed_d_mouth sad_Silentx02
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows surprisex02
        with dissolve

        d "..."

        show didac_bed_d_mouth sad_Talkingx04
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows angryx02
        with dissolve

        d "¡¿Pero qué coño nos tomamos este puto fin de semana?!"

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

    else:

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows surprisex02
        with dissolve

        p "Hoy es Lunes."

        show didac_bed_d_mouth sad_Talkingx04
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows angryx02
        with dissolve

        d "¡¿Qué?!"

        show didac_bed_d_mouth sad_Talkingx02
        show didac_bed_d_eyes 06
        show didac_bed_d_eyespup empty
        show didac_bed_d_eyebrows angryx04
        with dissolve

        d "¡Joder!"

        show didac_bed_d_mouth sad_Talkingx04
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup upleft03
        show didac_bed_d_eyebrows angryx04
        with dissolve

        d "¡¿Por qué coño no pasa así de rápido el resto de la semana?!"

        show didac_bed_d_mouth sad_Silentx01
        show didac_bed_d_eyes 03
        show didac_bed_d_eyespup front03
        show didac_bed_d_eyebrows suspiciousx02
        with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    d "Me temo que esta vez no voy a poder echarte una mano con esos mequetrefes..."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "Tranquilo,"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "me voy a quedar para asegurarme que estás bien."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡¿Es que te crees que tengo cinco años?!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Lárgate joder!"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "¡¿Acaso no has notado que ni siquiera yo puedo moverme?!"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "No pienso dejarte solo en este estado Dídac."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡¿Vas a dejar tirado a esos mocosos?!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Te vas a llevar el móvil,"

    extend " ¿verdad?"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "Si me pasa algo ya te llamaré, joder..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Pero..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Ni peros ni hostias!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Tienes la obligación de ir a entreno,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "y esos muchachos confían en ti!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Joder!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Si hasta con la pierna enyesada has asistido a esos dichosos entrenos!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Una mierda de cansancio no te servirá como excusa!"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "¡Acabas de decir que te estás muriendo!"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    d "Quizás he exagerado un poco..."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Joder!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "¡Y me quejaba del puto {a=https://es.wikipedia.org/wiki/Pandemia_de_COVID-19}corona-virus{/a}!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "¡¿En qué quedamos?!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "Aunque me estuviera muriendo,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "no pienso tener a un búho observándome a todas horas mientras estoy así."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows normal
    with dissolve

    d "No me preguntes por qué,"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "pero sé que voy a estar bien."

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "Sé que suena a puta locura,"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "pero es la sensación que tengo."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Además,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "como no vayas,"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "esos renacuajos me van a echar la culpa,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "y luego me lo estarás recordando el resto de la temporada!"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "Esos niños son más maduros y sensatos que tú y yo juntos."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "..."

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "Creo que es más importante la vida de mi compañero que un entreno."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "Solo tengo que enviar un mensaje a..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿Qué coño tengo que hacer para que te largues?!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Mira que me levanto y voy yo mismo al jodido entreno!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    p "Vale,"

    extend " vale..."

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "Ya me largo,"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "pero pobre de ti que no me llames si la cosa empeora."

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "¡¿Me has oído?!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡Que sí joder,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "que te largues!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    jump day06_home_withDidac_leaving

#####

label day06_home_withDidac_leaving:

    # Can be DAY-SCHOOL or NIGHT-TRAINING

    scene black
    with fade

    n "Con cierto esfuerzo, logras ponerte en pie."

    scene afternight03_bg_room02_day
    with fade

    n "Te diriges al armario dónde te vistes"

    n "y te preparas para la sesión de entreno que te espera."

    pt "¡¿Qué demonios está pasando?!"

    pt "¡¿Dónde están [neusname] y Meritxell?!"

    pt "Está claro que no lo he soñado."

    pt "Dídac está..."

    scene beds__comp_bracelet_phone:
        truecenter
        zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
        ease 5.0 zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 

    if p_ao_started:
        show beds_D01:
            truecenter
            zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
            ease 5.0 zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 
    else:
        show beds_D02:
            truecenter
            zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
            ease 5.0 zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 

    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty

    show light_screen_01:
        light_screen_01_position
        alpha 0.2
    with fade

    n "Cuando diriges tu mirada al móvil que sueles dejar sobre la mesita de noche,"

    #if MShooter_Bracelet in ["PLASTIC", "BRONZE", "SILVER", "GOLD"]:
    if MShooter_Bracelet in MShooter_Bracelet_var:

        n "encuentras la pulsera que ganaste en esa feria de disparos y que luego le regalaste."

        n "En el mismo smartphone,"

    n "descubres un mensaje escrito en un documento en blanco en él."

    $ day06_home_tablePhone = False

    show beds__comp_bracelet_phone:
        truecenter
        zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 
        ease_quad 15.0 zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position

    if p_ao_started:
        show beds_D01b:
            truecenter
            zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 
            ease_quad 15.0 zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
    else:
        show beds_D02b:
            truecenter
            zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 
            ease_quad 15.0 zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position


    call day06_night_homeLetter

    p "..."

    pt "[neusname]..."

    pt "¡¿Se ha asegurado?!"

    pt "¡¿Qué diablos significa eso?"

    pt "¡¿Realmente no volverán a molestarme?!"

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx05
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    show light_screen_01:
        light_screen_01_position
        alpha 0.2
    with fade

    n "Vuelves a mirar a tu compañero de piso que sigue sufriendo en la cama."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡¿Aún sigues aquí?!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Al final te voy a dar una hostia!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "Deja de decir estupideces."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    p "Ni siquiera eres capaz de levantarte."

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿Que no?!"

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    scene black
    with hpunch
    pt "¡La madre que lo parió!"

    p "¡Dídac!"

    d "¡Mierda!"

    d "Eso me ha dolido..."

    p "¡Estás como una puta cabra!"

    show beds__comp_bracelet_phone:
        truecenter
        #zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
        zoom 2.5 xpos 0.85 ypos 1.2 # Window Close
        ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5

    if p_ao_started:
        show beds_D01b:
            truecenter
            #zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
            zoom 2.5 xpos 0.85 ypos 1.2 # Window Close
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    else:
        show beds_D02b:
            truecenter
            #zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
            zoom 2.5 xpos 0.85 ypos 1.2 # Window Close
            ease_quad 15.0 zoom 1.0 xpos 0.5 ypos 0.5
    show light_screen_01:
        light_screen_01_position
        alpha 0.2
    with fade

    pt "Será mejor que le baje la persiana o no dormirá demasiado."

    d "¡¿Pero aún sigues aquí?!"

    d "¡Al final te voy a lanzar la lámpara!"

    pt "Su cuerpo se habrá transformado,"

    pt "pero desde luego, su personalidad no ha cambiado en lo más mínimo en todo este tiempo."

    # if p_ao_started:

    #     jump day06_home_withDidac_school

    # else:

    jump day06_home_withDidac_afterTraining

####

label day06_home_withDidac_school:

    # YOu go to school at morning. It's Tuesday.

    call morning06_AtSchool
        # if day06_night_homeDidacMale:
        #     n "Un Martes normal, como cualquier otro,"
        # else:
        #     n "Un Lunes normal como cualquier otro,"
        # n "a escasos días de las vacaciones de verano."

    jump aftermorning06_DidacMan_Routine03

label day06_home_withDidac_afterTraining:

    scene black
    with fade

    pause 0.2

    # It's LateMorning-afternoon

    scene morning04_bg_livingroom_others_morning
    with fade

    n "Después de la sesión de entreno con los niños,"

    n "a la que has llegado con cierta dificultad,"

    n "vuelves a casa."

    n "Esta vez con menos esfuerzo,"

    $ saturation_tint_level = "verydark"

    if p_ao_started:
        $ beds_time = "_midday_lightOff_blindDown_Dbusy01MCempty"
    else:
        $ beds_time = "_midday_lightOff_blindDown_Dbusy02MCempty"

    scene beds__comp_bracelet_phone
    if p_ao_started:
        show beds_D01
    else:
        show beds_D02
    with fade

    n "te diriges lo más rápido posible a la habitación."

    n "Dídac sigue sufriendo entre gemidos de dolor."

    pt "No parece que haya cambiado mucho la cosa."

    scene didac_bed_bed over
    if p_ao_started:
        show didac_bed_d_body 02
    else:
        show didac_bed_d_body 04
    show didac_bed_d_sweat 02
    show didac_bed_d_blush 04
    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 06
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    if p_ao_started:
        show didac_bed_d_hair 02
    else:
        show didac_bed_d_hair 04
    show didac_bed_headtowel empty
    show didac_bed_d_blanket 01
    with fade

    p "¿Cómo te encuentras?"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows angryx02
    with dissolve

    d "¡De fábula!"

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¡Estoy por correr dos maratones seguidas!"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿A ti qué coño te parece?!"

    show didac_bed_d_mouth sad_Silentx03
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    p "..."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "¡¿No tienes que ir a clase?!"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows surprisex02
    with dissolve

    p "Primero quería ver cómo estabas."

    show didac_bed_d_mouth sad_Talkingx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    d "Claro,"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows suspiciousx02
    with dissolve

    d "por que te viene de camino,"

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡¿Verdad?!"

    show didac_bed_d_mouth sad_Silentx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "¿Quieres que te traiga una aspirina?"

    show didac_bed_d_mouth sad_Talkingx01
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup upleft03
    show didac_bed_d_eyebrows sadx01
    with dissolve

    d "Te lo agradecería..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pause 0.2

    show didac_bed_d_mouth sad_Talkingx04
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows angryx04
    with dissolve

    d "¡Pero después te largas!"

    show didac_bed_d_mouth sad_Silentx02
    show didac_bed_d_eyes 03
    show didac_bed_d_eyespup front03
    show didac_bed_d_eyebrows normal
    with dissolve

    p "Que sí hombre,"

    extend " que sí..."

    show didac_bed_d_mouth sad_Silentx04
    show didac_bed_d_eyes 07
    show didac_bed_d_eyespup empty
    show didac_bed_d_eyebrows sadx01
    with dissolve

    pt "Espero que pueda descansar mejor esta noche."

    scene black
    with fade

    pause 0.2

    call aftermorning06_DidacMan_Routine02

    call morning06_AtSchool

    jump aftermorning06_DidacMan_Routine03

########################################################################################################
########################################################################################################
########################################################################################################

########################################################################################################
########################################################################################################
########################################################################################################

label day06_night_homeLetter:

    show morning04_bg_livingroom_mc_resting_phone messageEmpty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with Dissolve(1.0)

    txxt "Lamento que las cosas no salieran como habría deseado."

    if MShooter_Present_Necklace_Ankh:

        txxt "Siento haberte cogido el collar que te regalé,"

        txxt "pero créeme, no tuve opción."

    if MShooter_Bracelet in MShooter_Bracelet_var:

        txxt "Te devuelvo el brazalete,"

        txxt "al fin y al cabo, fuiste tú quien lo ganaste."

    txxt "No te preocupes por Padre,"

    txxt "me he asegurado de que nunca vuelva a molestarte,"

    txxt "siempre y cuando no indagues en lo que no debas."

    txxt "De corazón,"

    extend " espero que seas feliz."

    if DidacPregnant:

        txxt "PostData:"

        txxt "Desearía que no te hubieras despertado solo en la habitación."

        if DidacMCPregnant:

            txxt "No debiste haberlo dejado embarazado."

        else:

            txxt "No debiste haberlo dejado solo."

    return


    
########################################################################################################
########################################################################################################
########################################################################################################

########################################################################################################
########################################################################################################
########################################################################################################

label day06_night_homeWithoutDidac:
    # n "El cantar de los pájaros es lo primero que te llama la atención por su agudo silbido."
    $ pday_day += 1

    if pday_day == :
        $ pdaytime = "07morning"
    else:
        $ pdaytime = "06morning"

    scene morning04_bg bedroom_neus_a
    show light 01:
        light01_rightside_position
    show white:
        additive 1.0
        alpha 1.0
        easein_quad 5.0 alpha 0.0
    show morning04_bedroom_DMast_blinkeye
    show light_screen_01:
        light_screen_01_position
    with fade_long1s
    
    window hide dissolve
    pause

    if p_ao_started:

        show morning04_bg bedroom_neus_b
        with Dissolve(0.5)

        pt "Sigo en mi habitación..."

    else:

        pt "¿Qué...?"

        show morning04_bg bedroom_neus_b
        with Dissolve(0.5)

        pt "¡¿Es mi habitación?!"

    show morning04_bg bedroom_neus_c
    with Dissolve(1.5)

    window hide dissolve
    pause

    n "Tuerces el cuello para mirar hacia la ventana."

    $ beds_time = "_morning_lightOff_blindUp_DemptyMCbusy"

    scene beds__comp_bracelet_phone:
        truecenter
        zoom 2.5 xpos 0.85 ypos 1.2 # Window Close
        ease_quad 15.0 zoom 2.0 xpos 0.8 ypos 1.0 # Not So far

    show light_screen_01:
        light_screen_01_position
    with fade_long1s

    if p_ao_started:

        pt "Parece que está amaneciendo."

    else:

        pt "¿Está amaneciendo o anocheciendo?"

    if p_ao_started:

        pt "Dídac..."

    else:

        pt "¡¿Dídac?!"

    if not p_ao_started:

        p "Ughh..."

        pt "¿Qué le pasa a mi cuerpo?"

        pt "Es como si estuviera completamente agotado...."

    scene morning04_bg bedroom_neus_c
    show light 01:
        light01_rightside_position

    show light_screen_01:
        light_screen_01_position

    with Dissolve(1.0)

    n "Con el cuerpo dolorido y bastante entumecido,"

    n "ejerces fuerza en tus piernas y brazos para poder levantarte"

    scene black
    with fade

    n "y apenas logras mantenerte sentado sobre la cama."

    pt "¡Estoy hecho mierda!"

    #$ beds_time = "_morning_lightOff_blindUp_DemptyMCmessy"

    scene beds__comp_bracelet_phone:
        truecenter
        #zoom 2.5 xpos 0.85 ypos 1.2 # Window Close
        zoom 2.0 xpos 0.8 ypos 1.0 # Not So far
        easein_quad 7.0 zoom 1.0 xpos 0.5 ypos 0.5

    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty

    show light_screen_01:
        light_screen_01_position
    with fade

    n "Levantas la cabeza para mirar hacia la cama de Dídac."

    pt "¡¿Dónde demonios está?!"

    pt "¡¿Qué está pasando?!"

    pt "¡¿Dónde está [neusname] y la rubia esa?!"

    n "Tus ojos se mueven rápidamente alrededor de la habitación en busca de respuestas"

    $ beds_time = "_morning_lightOff_blindUp_DemptyMCmessy"
    show beds__comp_bracelet_phone:
        truecenter
        zoom 2.5 xpos -0.1 ypos 0.45 # Phone Close position
        ease 5.0 zoom 4.0 xpos -0.38 ypos 0.4 # Phone SuperClose position. 
    with fade

    n "hasta que finalmente alcanzas a ver el móvil que tienes encima de la mesita de noche."

    if MShooter_Bracelet in MShooter_Bracelet_var:

        n "pero justo al lado de este,"

        n "encuentras la pulsera que ganaste en esa feria de disparos y que luego le regalaste."

        $ day06_home_tablePhone = False

        scene beds__comp_bracelet_phone:
            truecenter
            #zoom 1.0 xpos 0.5 ypos 0.5
            zoom 2.0 xpos 0.2 ypos 0.55

        show morning04_bg_livingroom_mc_resting_phone empty:
            xpos 0.485 ypos 0.125
        show morning04_livingroom_mc_resting_handphone empty

        show light_screen_01:
            light_screen_01_position
        with fade

        n "Al coger el móvil ves un mensaje escrito en un documento en blanco."

    else:

        $ day06_home_tablePhone = False

        scene beds__comp_bracelet_phone:
            truecenter
            zoom 1.0 xpos 0.5 ypos 0.5

        show morning04_bg_livingroom_mc_resting_phone empty:
            xpos 0.485 ypos 0.125
        show morning04_livingroom_mc_resting_handphone empty

        show light_screen_01:
            light_screen_01_position
        with fade

        n "Al cogerlo ves que hay un mensaje escrito en un documento en blanco."

    call day06_night_homeLetter

    pt "¡¿No va a poder volver?!"

    show morning04_bg_livingroom_mc_resting_phone empty
    show morning04_livingroom_mc_resting_handphone empty
    with dissolve

    pt "¡¿De qué demonios está hablando?!"

    show beds__comp_bracelet_phone:
        ease 10.0 zoom 1.0 xpos 0.5 ypos 0.5

    if DidacMCPregnant:

        pt "{i}No debiste haberlo dejado embarazado{/i}..."

    else:

        pt "{i}No debiste haberlo dejado solo{/i}..."

    
    pt "¡¿Qué demonios le habrá hecho esa bruja?!"

    menu:

        pt "\"{i}siempre y cuando no indagues en lo que no debas{/i}\"."

        "<Llamar a la policía>":

            jump day06_night_homeWithoutDidac_phonePolice

        "<Pensártelo mejor>":

            jump day06_night_homeWithoutDidac_notPhone

label day06_night_homeWithoutDidac_notPhone:

    pt "¿Por qué estoy vivo?"

    pt "{i}No te preocupes por Padre{/i}..."

    pt "¿Acaso lo habrá ofrecido en sacrificio...?"

    pt "Pero entonces..."

    pt "¿Por qué no me ha sacrificado a mí también?"

    pt "Si voy con esta nota a comisaría me van a echar a patadas."

    # pt "Tengo que buscar más pruebas..."

    # show morning04_bg_livingroom_mc_resting_phone empty
    # show morning04_livingroom_mc_resting_handphone empty
    # with Dissolve(0.5)
    
    with hpunch
    ono "RIIIIING"

    pt "¿La alarma del móvil?"

    pt "Mierda..."

    pt "Es verdad que hoy empezaba entreno con los muchachos."

    

    n "Alzas la vista para fijarte mejor en tu habitación."

    pt "No sé que es,"

    pt "pero la habitación parece distinta,"

    pt "huele distinta..."

    scene black
    with fade

    # NOT FINISHED -illustration-

    n "Pones un pie en el suelo para intentar levantarte"

    n "pero sientes que tiembla tanto que tu equilibrio tambalea"

    with vpunch

    n "y terminas cayendo de rodillas contra el suelo."

    p "¡Joder!"

    n "Tienes la sensación de que no te has hecho mucho daño,"

    n "pero aún sigues sin ser capaz de ponerte en pie."

    n "Te agarras a la cama y consigues volver a ponerte de pie."

    scene beds__comp_bracelet_phone:
        truecenter
        zoom 1.0 xpos 0.5 ypos 0.5

    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty

    show light_screen_01:
        light_screen_01_position
    with fade

    pt "Siguen temblando..."

    pt "Apenas puedo moverme."

    pt "Está claro que tengo que llamarles para decirles que hoy no podré asistir a su entreno..."

    n "A duras penas y casi arrastrándote logras llegar hasta el armario."

    scene black # Not finished -illustration- wardrobe Half empty
    with fade

    pt "¡No es posible!"

    pt "¡¿Dónde demonios están sus cosas?!"

    scene morning04_bg bedroom_neus_c
    show light 01:
        light01_rightside_position
    show light_screen_01:
        light_screen_01_position
    with fade

    n "Con tus agotados brazos, empiezas a abrir sus cajones."

    pt "Están vacíos."

    # scene beds__comp_bracelet_phone:
    #     truecenter
    #     zoom 1.0 xpos 0.5 ypos 0.5
    # show light_screen_01:
    #     light_screen_01_position
    # with fade

    with hpunch
    n "Estirándote de nuevo en el suelo,"

    n "te arrastras como un moribundo por tu habitación"

    n "hasta que logras ver lo que hay debajo de la cama de tu compañero de piso."

    p "..."

    n "Dónde solía haber revistas porno, pelotas de goma,"

    n "y hasta algún que otro condón usado,"

    n "ahora no hay ni tan solo una mota de polvo."

    pt "¡Maldita sea!"

    n "Te agarras de nuevo sobre la cama y vuelves a intentar ponerte de pie,"

    n "tus piernas siguen temblando, pero esta vez,"

    n "parece que eres capaz de mantener el equilibrio."

    n "Sujetándote a la pared,"

    n "logras salir de la habitación y te diriges al baño."

    scene afternight03_bg_hallway_day
    with fade

    pt "¡El mismo olor!"

    n "Al abrir el pequeño armario que también sirve como espejo, solo encuentras tus cosas."

    n "Ni siquiera hay su estúpido jabón de marca innombrable en la ducha."

    pt "¡¿Pero qué...?!"

    n "Sujetándote a la paredes y a lo que encuentras por el camino,"

    n "te diriges tan rápido como te es posible a la cocina,"

    n "dónde miras dentro del frigorífico."

    scene black #Not finished -illustration- Fridge Half Empty
    with fade

    pt "No es posible..."

    n "Dónde solía haber bebidas energéticas no demasiado saludables,"

    n "productos que sobrepasaban por meses la data de caducidad;"

    n "ahora solo hay aquello que pertenece a tu parte de la compra."

    pt "Pero..."

    pt "¡¿Cómo demonios han sabido qué diablos era lo suyo?!"

    pt "¡Si la mayor parte del tiempo ni nosotros mismos lo sabíamos!"

    n "Aún con las piernas algo temblorosas, te diriges a la sala de estar,"

    scene morning04_bg_livingroom_others_morning_clean

    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty

    show light_screen_01:
        light_screen_01_position
    with fade

    n "el lugar dónde pasabais la mayor parte del tiempo."

    n "Con lo desordenado y guarro que ha sido siempre tu compañero de piso,"

    n "jamás has podido tener decente esta parte de la casa,"

    n "pero sin embargo, ahora,"

    n "está impoluta."

    n "Y ese extraño olor sigue inundando tu nariz."

    scene black
    with vpunch
    n "Tus piernas flaquean y tus rodillas impactan de nuevo contra el suelo."

    pt "Es-"

    extend "Es como si nunca hubiera vivido en esta casa."

    scene morning04_bg_livingroom_others_morning_clean
    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty
    show light_screen_01:
        light_screen_01_position
###
    show morning04_livingroom_mc_resting_handphone
    if p_ao_started:
        show morning04_bg_livingroom_mc_resting_phone home_tuesday
    else:
        show morning04_bg_livingroom_mc_resting_phone home_monday
    with fade

    n "Rápidamente vuelves a coger el móvil y accedes tu galería de fotos."

    # NOT FINISHED, -illustration- gallery photos?

    pt "¡Tiene que ser una broma!"

    n "Entre el montón de fotos que tienes en tu smartphone,"

    n "intentas buscar alguna de las fotos que os soléis sacar cuando estáis entrenando"

    n "o saliendo de fiesta"

    n "mientras hace el capullo ligando de forma horrible"

    n "con alguna que otra chica que ha bebido un poco de más."

    n "Ni una sola foto."

    # fACEBOOK? -illustration-

    n "Rápidamente accedes a las redes sociales dónde soléis compartir este tipo de fotos."

    pt "No..."

    n "No solo no encuentras ninguno de sus perfiles,"

    n "sino que tampoco encuentras ninguna foto en la que aparezca,"

    n "ni siquiera de fondo."

    pt "¡Es imposible!"

    n "Vas deslizando el dedo buscando en distintos {a=https://en.wikipedia.org/wiki/Posting_style}posts{/a} de amigos y conocidos"

    n "dónde sabes que el idiota de Dídac ha dejado algún que otro comentario absurdo,"

    n "y con el que un compañero o amigo le ha dejado un {a=https://es.wikipedia.org/wiki/Hashtag}hastag{/a} con su nombre para etiquetarlo."

    n "Nada."

    n "Haces clic sobre uno de vuestros compañeros de clase para poder llamarlo."

    show morning04_bg_livingroom_mc_resting_phone empty
    show morning04_livingroom_mc_resting_handphone empty
    with dissolve

    b01 "¡Ey tío!"

    if p_ao_started:

        b01 "¿Qué te pasó ayer?"

        b01 "No te vimos por clase."

        p "Tranquilo, simplemente no me encontraba bien."

        b01 "Vaya, espero que estés mejor."

    else:

        b01 "¡¿Cómo va?!"

    p "Oye,"

    extend " una pregunta."

    b01 "Dime."

    p "¿Por qué has borrado todos los comentarios de Dídac?"

    b01 "¿Quién es Dídac?"

    scene black
    with vpunch
    ono "Pum"

    n "Tu cuerpo tiembla de tal modo que eres incapaz de mover un músculo."

    n "hasta que finalmente tus piernas ceden y caes de culo en el suelo."

    pt "¡No es posible!"

    scene morning04_bg_livingroom_others_morning_clean
    show morning04_bg_livingroom_mc_resting_phone empty:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone empty
    show light_screen_01:
        light_screen_01_position
    with fade

    b01 "Espera..."

    b01 "Te refieres al chico con el que sueles hablar que está sentado detrás en la esquina."

    b01 "¿No es así?"

    p "¡Claro que me refiero a él!"

    pt "¡¿A quien si no?!"

    b01 "¿No es tu compañero de piso?"

    pt "¿Cómo es posible que no se acuerde de nada más?"

    b01 "Tío,"

    if p_ao_started:

        b01 "¿de verdad estás bien?"

    else:
        
        b01 "¿estás bien?"

    b01 "¿Es que te ha pasado algo con él?"

    p "..."

    p "¡¿Acaso no te acuerdas de las noches que hemos salido de fiesta los tres?!"

    b01 "¿Con él?"

    pt "¿Me estará tomando el pelo?"

    b01 "Si es de esas noches en las que bebo más de la cuenta,"

    b01 "es posible que no me acuerde."

    p "¿En serio no te acuerdas de él?"

    b01 "Recuerdo haberlo saludado alguna vez en clase,"

    b01 "pero en realidad, no mucho más."

    p "..."

    b01 "¿Es que habéis tenido una pelea?"

    p "No,"

    p "no es eso..."

    b01 "Ahmm..."

    b01 "Es solo que he oído en clase que alguien se ha ido de viaje"

    b01 "y ahora que lo mencionas, es posible que se trate de él."

    p "¡¿Qué?!"

    b01 "¿No te ha dicho nada?"

    pt "¡¿De viaje?!"

    pt "¡¿De qué está hablando?!"

    b01 "Por eso he pensado que quizás habías tenido problemas con él."

    p "No,"

    extend " no..."

    p "Tranquilo,"

    p "no pasa nada."

    p "Solo quería comprobar algo."

    b01 "¿Estás seguro?"

    p "Sí,"

    extend " sí,"

    p "estoy bien."

    b01 "Bueno,"

    b01 "espero haberte sido de ayuda."

    ono "clic"

    pt "Apenas recuerda su nombre,"

    pt "¡¿y no se acuerda que hace más de un año que vamos de fiesta juntos?!"

    show morning04_livingroom_mc_resting_handphone 
    if p_ao_started:
        show morning04_bg_livingroom_mc_resting_phone home_tuesday

    else:
        show morning04_bg_livingroom_mc_resting_phone home_monday
    with dissolve

    n "Miras otros perfiles,"

    n "incluso ex-compañeros de clase,"

    n "y en todos se repite el mismo panorama."

##
    
    show morning04_livingroom_mc_resting_handphone  empty
    show morning04_bg_livingroom_mc_resting_phone empty
    with dissolve

    n "Pasas varios minutos en silencio sin saber muy bien qué hacer."

    pt "En lugar de hacerlo desaparecer,"

    pt "lo que han hecho es volverlo una persona olvidable..."

    show light_screen_01:
        #alpha 1.0
        ease 40.0 alpha 0.0

    # if not p_ao_started:

    #     n "Lentamente el cielo se va oscureciendo"

    #     n "hasta que quedas a oscuras sentado en el frío suelo del comedor."

    show morning04_livingroom_mc_resting_handphone 
    if p_ao_started:
        show morning04_bg_livingroom_mc_resting_phone home_tuesday

    else:
        show morning04_bg_livingroom_mc_resting_phone home_monday
    with dissolve

    n "Con la mano temblando, decides llamar a los padres de Dídac."

    show morning04_livingroom_mc_resting_handphone  empty
    show morning04_bg_livingroom_mc_resting_phone empty
    with dissolve

    df "¡[protname]!"

    df "¡¿Cómo estas?!"

    p "Bien,"

    extend " bien..."

    df "¿Y a qué debo el honor de tu llamada?"

    p "Dídac,"

    extend " está..."

    df "Desde luego..."

    df "¡El chico es de lo que no hay!"

    df "Pero me alegro que por fin esté motivado en hacer algo con su vida."

    p "¿Cómo?"

    df "Su madre y yo aún lo estamos asimilando,"

    df "pero en el fondo me alegro por él."

    df "No es lo que me habría esperado,"

    df "pero mientras él sea feliz,"

    df "nosotros también lo estaremos."

    p "¡¿Qué?!"

    df "¿No te lo ha contado?"

    p "¿El qué?"

    df "Ha decidido dar la vuelta al globo terráqueo para descubrir mundo"

    df "y conseguir nuevas oportunidades de ganarse la vida."

    p "¡¿Cómo?!"

    df "Nos llamó ayer por la noche emocionado y motivado por su proyecto,"

    df "al principio pensaba que lo decía en broma,"

    df "pero realmente se le notaba ilusionado y con una energía"

    df "que hacía años que no le veía en él."

    df "Dijo que se pasaría años dando vueltas por el mundo,"

    df "alcanzando rincones inhóspitos y salvajes,"

    df "y que por lo tanto tardaríamos años en volverlo a ver."

    df "Pero nos prometió llamarnos de tanto en cuando para saber que se encuentra bien."

    p "..."

    pt "¡¿Qué?!"

    p "¡¿No os parece extraño que haya tomado esta idea de un día para otro?!"

    df "Conociendo a mi hijo,"

    df "hay pocas cosas que me sorprendan de él."

    df "Lo que sí sería una sorpresa"

    df "es que fuera capaz de sobrevivir de este modo durante más de un mes."

    df "Seguramente para entonces ya habrá vuelto a casa."

    df "Ya sabes como es."

    p "..."

    df "Pero si es lo que quiere,"

    df "no somos nadie para contradecirle."

    p "Pe..."

    df "Lo que me parece vergonzoso es que no se despidiera de ti;"

    df "eso sí me parece imperdonable."

    p "Su voz..."

    df "¿Hmmm?"

    p "¿Sonaba igual que siempre?"

    df "¿Si sonaba igual?"

    df "¿A qué te refieres?"

    p "¿Sonaba igual de masculina?"

    df "¿Estás bien?"

    p "..."

    p "Sí,"

    extend " Sí..."

    p "estoy bien."

    df "¿Necesitas que llame a alguien?"

    p "No,"

    extend " no..."

    p "estoy bien,"

    extend " de verdad."

    df "¿Ya has encontrado a alguien que le sustituya como compañero de piso?"

    p "¿Cómo?"

    df "Me imagino que tú solo tendrás problemas para pagar el alquiler."

    p "..."

    df "No te preocupes,"

    df "te pagaré su mensualidad los meses que necesites hasta que encuentres a un sustituto,"

    df "al fin y al cabo es lo mínimo que puedo hacer después de que ni te haya avisado."

    p "De verdad que no hace falta."

    p "El piso está cerca de {a=https://es.wikipedia.org/wiki/Plaza_de_Cataluña}Plaza Cataluña{/a},"

    p "no creo que tarde mucho en encontrar a alguien interesado."

    pt "En realidad no creo que me resulte tan fácil,"

    pt "pero total, estos últimos meses ya estaba pagando yo solo el alquiler."

    pt "Pero no quiero decirle eso a su padre."

    df "Escríbeme tu número de cuenta cuando puedas,"

    df "al menos déjame pagarte un mes."

    p "Ya te he..."

    df "No es negociable."

    p "..."

    pt "Cuando se pone así, es incluso más testarudo que Dídac."

    p "Como quieras,"

    extend " pero solo un mes."

    df "Cuando me pases la foto de tu nuevo compañero de piso cancelaré la cuenta."

    p "..."

    pt "A veces me pregunto si no fue adoptado."

    df "En cuanto a Dídac no te preocupes,"

    extend " te mantendré al día cuando llame,"

    df "de todos modos ya verás que no aguantará mucho tiempo,"

    df "ya lo conoces..."

    p "..."

    df "¡Ya va!"

    extend " ¡Ya va!"

    df "Esta mujer..."

    df "Ha sido un placer hablar contigo [protname],"

    df "pero tengo que seguir con mi tarea"

    df "o mi mujer me obligará a dormir en el sofá otra vez."

    df "Si nos necesitas para cualquier cosa,"

    df "sabes que puedes contar con nosotros,"

    extend " ¿verdad?"

    p "Sí,"

    extend " sí..."

    p "No te molesto más."

    p "Gracias por atenderme."

    df "¡Faltaría más!"

    df "Siempre has sido un gran amigo de Dídac,"

    df "y ya sabes que eres como de la familia."

    p "Gracias."

    ono "clic"

####

    

    p "..."

    pt "¡¿Qué cojones?!"

    pt "¡¿Se ha ido a dar la vuelta al mundo?!"

    pt "¡¿Es que se ha vuelto el puto {a=https://es.wikipedia.org/wiki/La_vuelta_al_mundo_de_Willy_Fog}WILLY FOG{/a}?!"

    pt "¡¿Acaso no ven que no tiene sentido?!"

    pt "¡Nunca ha sido capaz de entender un mapa"

    pt "y casi siempre llega tarde a los lugares nuevos porque se equivoca de parada de metro"

    pt "o simplemente se pierde por Barcelona!"

    pt "¡Pero si es peor que {a=https://ranma.fandom.com/es/wiki/Ryoga_Hibiki}Ryoga{/a}!"

    pt "¡¿Cómo es posible que acepten algo tan absurdo y tan a la ligera?!"

    pt "Es como si les hubieran..."

    p "..."

    n "Sigues sin ser capaz de moverte o reaccionar,"

    n "hasta que decides levantarte al notar que tus piernas se están quedando dormidas."

    n "Finalmente enciendes el portátil del comedor que está conectado al televisor"

    n "y te sientas al sofá para mirar algún vídeo en internet."

    n "Vas pasando de vídeo en vídeo sin saber muy bien qué estás viendo realmente."

    jump day06_ending_withoutDidac

## Credits? # Can you have sense of touch? if you're a soul leaving the body.
label day06_ending_withoutDidac:

    $ day06_ending_city = "barcelona"

    call day06_ending_window

    p "No creo que sea una buena idea llamar a la policía..."

    p "No solo pondría mi vida en peligro,"

    p "si no que además, hasta sus padres están convencidos que se ha ido de viaje."

    p "Lo único que lograría es parecer un jodido loco de manicomio"

    p "si les cuento que ha sido secuestrado por una puta secta de brujas y cabras..."

    ##

    p "De tanto en cuando los llamará..."

    p "¿Significa eso que sigue con vida?"

    p "¿O que alguien es capaz de imitar su voz?"

    p "Después de las cosas que he visto,"

    p "tampoco me sorprendería tanto..."

    p "¡¿Se supone que debo olvidarlo y ya está?!"

    p "Tampoco he visto ninguna foto de Meritxell por ninguna parte."

    p "Supongo que habrá hecho algo parecido con ella..."

    p "¿Y qué diablos será de mi?!"

    p "{i}No te preocupes por Padre,{/i}"

    p "{i}me he asegurado de que nunca vuelva a molestarte.{/i}"

    p "¿Qué se supone que significa esto?"

    p "¡¿Realmente esa cabra loca no volverá a molestarme?!"

    p "¿Debería irme de Barcelona?"

    p "¡¿Pero dónde?!"

    p "¡Si apenas puedo permitirme pagar este piso!"

    p "Está claro que tendré que buscarme otro..."

    p "u otro compañero de piso..."

    p "Dídac..."

    #n "Lentamente tus párpados van cediendo hasta que finalmente cierras los ojos."

    pause

    #aj "Final alternativo número: ??"

    jump gameover






