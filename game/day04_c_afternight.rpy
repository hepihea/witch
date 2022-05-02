
default afternight04_Didac_Leaving_Cond = False
default afternight04_Didac_FollowHim_Yes_Cond = False

## AfterNight with Didac at Park.

default afternight04_didac_pregnantRapeOkupa  = False #Raped and pregnant by Okupa.

default afternight04_DidacisNOTatHome = False
default afternight04_sexbattle_started = False

default afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond = False #Impides que Fumetas le folle el culo sin condón
default afternight04_Park_DidacFuckAnal_Cond = False # Fumetas Follando a Dídac sin condón en el culo.

default afternight04_Park_DidacFuckWithoutCondom_Aborted_Cond = False #Has impedido que se quede preñada por el Okupa, cosa que te agradece.
default afternight04_Park_DidacFuckWithoutCondom_Pregnant = False #No impides que se quede preñada por el Okupa.
default afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant = False #Te largas de la escena sin pelear, Dídac queda preñada.Dídac queda preñada sin que lo veas

default DidacOKUPregnant = False # Didac is pregnant by Squitter (Okupa).
default DidacMCPregnant = False # Didac is pregnant by the Main Character.

default afternight04_Park_HelpDidacPolice_Cond = False #Después de quedarse preñado, ayudas a Dídac a salir de ahí, 
#sin que este se lo tome demasiado bien el hecho de que hubieras estado observándole sin haber hecho nada.

default afternight04_Park_AbandonDidacPolice_Cond = False # Después de quedarse preñado, lo abandonas con los policías sin que supiera que estabas ahí.

default afternight04_Park_Battle_Punch_GetBackHomewithDidac_Cond = False #You get back home with Didac after a fight.
default afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond = False #You don´t get back home with Didac, They changed place. You were punched on the face.

default an04_Park_Battle_Punch_pothead_otherpunch = False

default afternight04_Park_LookingForDidac_yes_Cond = False

default potheadCum = ""
default pimpCum = ""
default squatterCum = ""

##
## #########################################################
## #########################################################
## #########################################################
##

label afternight04:
    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)
    
    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0

    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade

    $ saturation_tint_level = "superdark"
    
    pt "Las luces están apagadas..."

    if aftermorning04_calmdidac_Failed == False:

        pt "eso significa que Dídac estará durmiendo..."

#########################################################
    
    # if config.version <= "00.07.01": #After 2nd date with Neus, Didac is not sleeping.

    #     aj "Esta parte no estará disponible hasta la versión 0.7.1, que es la versión dónde finaliza la cita con la chica tetuda misteriosa."

    #     aj "A menos que tengas la cuenta Premium..."
        
    #     call endupdatescript
    
#######################################################

    if night04_Neus_Blowjob_Cum_Affirmative  == True:
    
        pt "¿Qué tipo de droga me ha dado esa chica?"

        pt "Ojos que brillan en la oscuridad,"

        pt "una lengua larga como una serpiente,"

        pt "sus ojos..."
        
        pt "Sabría que todo esto es un sueño,"

        pt "si no fuera porque tengo a mi compañero de piso durmiendo con dos melones,"

        extend " y sin polla;"

        pt "en nuestra habitación..."

        if afternoon04_MACBA_TxellTruth_Cond == True:
        
            pt "Hay muchas cosas que coinciden con lo que me dijo {b}Meritxell{/b}..."

    if afternoon04_MACBA_TxellTruth_Cond == True and night04_Neus_Blowjob_Cum_Affirmative  == False:

        pt "No sé si he hecho bien en hacer caso a la advertencia de {b}Meritxell{/b} sobre el peligro de Neus..."

        pt "Pero sinceramente,"

        pt "toda esta situación ha sido bastante extraña..."
    
    n "Entras en el piso intentando hacer el menor ruido dejando las llaves con suavidad"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve
    
    n "en la mesita de entrada."

    if aftermorning04_calmdidac_Failed == True:

        pt "Espero que el muy idiota se haya comportado,"

        pt "y le hayan dejado salir de esa celda..."

    else:
    
        pt "A estas horas ya debe de estar durmiendo..."

    scene afternight03_bg hallway_dark
    with fade
    
    n "Cuidando cada paso que das,"
    
    n "te diriges con cautela a vuestra habitación."

    # Si la puntuación es baja no estará en la cama.

    if pl.dp >= 9:
        if PlatinumHelp:
            $ renpy.notify("[p_pos] 9[hd]")
        jump afternight04_Didacishome
    else:
        if PlatinumHelp:
            $ renpy.notify("[p_neg] 9[hd]")
        jump afternight04_DidacisNOThome

label afternight04_DidacisNOThome:

    scene beds_night_lightOff_blindUp_DemptyMCempty
    with fade

    $ afternight04_DidacisNOTatHome = True

    # NOT FINISHED ## Aquí es cuando miras de ir a buscar a Dídac a la calle o directamente ir a dormir y que le den.

    p "¡¿Dónde coño se ha metido ahora este?!"

    p "Maldito seas..."

    p "¿Qué demonios se supone que tengo que hacer ahora?"

    p "¿Hacerte de niñera e ir a buscarte?"

    p "¿Y por dónde empiezo?"

    p "¡Maldita sea!"

    p "Ya tienes una edad..."

    p "..."

    p "Solo espero que no hagas nada de lo que puedas arrepentirte Dídac..."

    scene afternight03_bg hallway_dark
    with fade

    n "Con cierta frustración e ira contenida te diriges al baño para asearte"

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    n "antes de ir a la cama a reunirte con {a=https://es.wikipedia.org/wiki/Morfeo}Morfeo{/a}."

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    with dissolve

    p "Mañana será otro día..."

    scene black
    with fade

    window hide dissolve
    pause

    jump afternight04_NeusCallForDidac

    #ono "{size=30}RIIIIING{/size}"

    #n "Un sonoro timbre del teléfono móvil te despierta abruptamente."

    #pt "¿A estas horas?"

    #pt "¿Qué diablos querrán?"

    #p "..."

label afternight04_Didacishome:

    scene beds_night_lightOff_blindUp_DemptyMCempty
    show beds_D03b_night_lightOff_blindUp
    with fade
    
    pt "Efectivamente,"

    extend " está durmiendo."

    if aftermorning04_calmdidac_Failed == True:

        pt "Menos mal..."
    
    n "Piensas en ir a la cama,"

    extend " cuando de pronto oyes un ruido."

    show beds_D03b_night_lightOff_blindUp
    with hpunch
    
    play sound "audio/sfx/stomach01.ogg"

    n "Brrrrrrrbrrr..." # *Ruido de estómago*
    
    pt "Maldita sea..."
    
    pt "No puedo meterme en la cama con el estómago vacío..."
    
    pt "Lo poco que he comido durante la cena lo he acabado echando en el baño del restaurante..."
    
    pt "Supongo que habrá algo en la nevera para comer antes de ir a dormir."
    
    n "Te diriges al comedor pasando por la sala de estar,"

    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff:
        livingroom_room_pos_generalview
    with fade
    
    n "y en ella descubres un montón de ropa interior femenina desperdigada por el sofá y la mesa."
    
    p "..."

    if aftermorning04_calmdidac_Failed == True:

        pt "¡¿A qué hora le han soltado para que le haya dado tiempo a comprar todo esto?!"

    else:

        pt "¿Es que se ha comprado medio almacén?"

    pt "Es posible que su cuerpo se haya vuelto femenino..."
    
    pt "Pero sin duda,"

    pt "sigue siendo igual de desordenado que el Dídac que yo conozco."

    show morning04_bg livingroom_room_night_lingerie_others_LightOff:
        livingroom_room_pos_panningsofa
    with fade
    
    n "Sin poder evitarlo, te viene a la mente el cuerpo femenino de tu actual compañero de piso"
    
    n "vistiendo una de estas piezas de lencería femenina"
    
    n "y tu miembro empieza a erguirse."

    show morning04_bg livingroom_room_night_lingerie_others_LightOff:
        livingroom_room_pos_panningchairs
    with dissolve
    
    pt "Soy un puñetero enfermo mental..."

    jump afternight04_Didac_FromBehind
        
label afternight04_Didac_FromBehind:

    # SFXSOUND Naked Footsteps aproaching. NOT FINISHED
    
    n "Oyes los pasos de pies desnudos detrás de ti."
    
    n "Sin que te dé tiempo a darte la vuelta,"

    # Didac agarrándote la camiseta con botones por detrás casi como si quisiera arrancártela.

    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 0.5 fadeout 0.5

    scene black
    show an04_Dgrabbingshirt_scene 01:
        subpixel True
        zoom 1.5 xanchor 0.25 yanchor 0.25
        easein_quad 20.0 zoom 1.25 xanchor 0.6 yanchor 1.0 #Hand Soft Pecho

        #easein_quad 10.0 zoom 1.0 xanchor 0.5 yanchor 1.0 #Hand Hard Pecho
        #easein_quad 10.0 zoom 1.5 xanchor 0.6 yanchor 2.3 #Hand Dick
    with hpunch
    
    n "sientes unos brazos femeninos abrazando todo tu cuerpo."
    
    p "¡Dídac!"
    
    p "¡¿Qué haces?!"
    
    d "¿Qué son estas horas de llegar a casa?"
    
    d "Ya pensaba que no volverías..."
    
    d "¿Cómo te ha ido la cita con esa..."

    extend " {b}bruja{/b}..?"
    
    p "¿Euh?"
    
    p "¿Te refieres a Neus?"

    show an04_Dgrabbingshirt_scene 02:
        subpixel True
        easein_quad 5.0 zoom 1.0 xanchor 0.5 yanchor 1.0 #Hand Hard Pecho
    with dissolve
    
    d "¿Y a quién si no?"

#########################################################
    
    if config.version <= "00.07.02": #After 2nd date with Neus, Didac Grabbing you from behind.
        
        call endupdatescript
    
#######################################################
    
    p "Bueno..."
    
    p "Ha ido bien,"

    extend " supongo..."

    if night04_Neus_Blowjob_Cum_Affirmative  == False:

        pt "Aunque tampoco he querido arriesgarme a ir demasiado lejos..."

    #Su mano desplazándose hacia abajo...

    show an04_Dgrabbingshirt_scene 03:
        subpixel True
        easein_expo 5.0 zoom 1.0 xanchor 0.5 yanchor 2.2 #Hand Dick

    with vpunch
    
    p "¡Oye!"

    #Susurrándote en el oído. Como Txell.

    scene black
    show an04_Dgrabbingshirt_background:
        zoom 0.6
    show whisper_mc_front:
        whisper_didac_night_pos_01
    show whisper_d_mouth Talking:
        whisper_didac_night_pos_01
    show whisper_d_nose:
        whisper_didac_night_pos_01
    
    d "\"Muy bien no te habrá ido\"..."
    
    d "Si vuelves a casa con este cañón aún cargado..."

    scene black
    show an04_Dgrabbingshirt_scene 03:
        subpixel True
        zoom 1.5 xanchor 0.6 yanchor 2.4 #Hand Dick
    with dissolve
    
    if night04_Neus_Blowjob_Cum_Affirmative == True:
        
        p "..."

        pt "Ahora que lo menciona..."
    
        pt "Es cierto,"

        pt "que esté así de duro,"

        extend " después de lo muerto que me he quedado con la mamada de Neus..."
        
        jump afternight04_Didac_LoadedCannon
        
    else:
        
        jump afternight04_Didac_LoadedCannon
        
label afternight04_Didac_LoadedCannon:

    scene black
    show an04_Dgrabbingshirt_scene 04:
        subpixel True
        zoom 1.5 xanchor 0.6 yanchor 2.4 #Hand Dick
        easein_bounce 3.0 zoom 1.2 xanchor 0.5 yanchor 2.25 
    with vpunch

    #Movimiento de mano en tus calzoncillos.
    play sound "audio/sfx/fall07.ogg"
        
    n "Empieza a apretar con fuerza y a mover su mano con tu miembro bien agarrado por encima de tus pantalones."
    
    p "Dídac..."

    extend " ¡¿Qué haces?!"

    #Susurro de nuevo.

    scene black
    show an04_Dgrabbingshirt_background:
        zoom 0.6
    show whisper_mc_front:
        whisper_didac_night_pos_02
    show whisper_d_mouth Talking:
        whisper_didac_night_pos_02
    show whisper_d_nose:
        whisper_didac_night_pos_02
    with dissolve
    
#########################################################
    
    if config.version <= "00.07.02": #After 2nd date with Neus, Didac is not sleeping.
        
        call endupdatescript
    
#######################################################

    d "Estoy comprobando lo contenta que la tienes..."

    d "Siempre me ha resultado curioso lo enorme que la llegas a tener,"

    d "pero ahora simplemente me obsesiona..."

    show whisper_d_mouth Smiling
    with dissolve
    
    p "Dídac..."

    #Vuelve a mano en el pecho.

    scene black
    show an04_Dgrabbingshirt_scene 04:
        subpixel True
        zoom 1.25 xanchor 0.75 yanchor 1.25 #Hand Dick
    with dissolve
    
    d "¡Oye!"

    d "A mí no me culpes;"

    extend " ya la tenías así de dura antes de que siquiera te tocara..."

    #Susurro de nuevo.

    show morning04_bg livingroom_room_night_lingerie_others_LightOff:
        livingroom_room_pos_panningsofa
    with dissolve
    
    d "¿Acaso te has puesto caliente al ver la lencería que hay en la sala de estar?"

    if morning04_ShoppingDidac_Cond == True:

        d "Eso no tendría sentido."

        d "En la sección de lencería femenina no se te puso así de dura..."

    #Mano dentro de los pantalones.

    scene black
    show an04_Dgrabbingshirt_scene 05:
        subpixel True
        zoom 1.25 xanchor 0.2 yanchor 1.0 #Hand Dick
        easein_bounce 1.5 zoom 0.8 xanchor 0.35 yanchor 2.08
    with dissolve
    
    p "¡Dídac!"

    #Susurro de nuevo.

    scene black
    with dissolve
    
    d "¿O es que quizás me has imaginado probándome esta ropa tan íntima?"

    scene black
    show an04_Dgrabbingshirt_scene 05:
        subpixel True
        zoom 1.0 xanchor 0.0 yanchor 0.0 #zoom 0.8 xanchor 0.35 yanchor 2.08
        easein_quad 30.0 zoom 1.25 xanchor 0.45 yanchor 2.4 #Hand Dick
    with dissolve

    if morning04_DidacHotforyou_Cond == True:

        d "Además..."

        extend " después de que te masturbaras en la habitación conmigo adentro..."

        p "¡Tú eres el que se estaba masturbando!"

        d "Pero bien que luego hiciste lo mismo..."

        d "Podías haberte ido o haberme dicho algo..."

        extend " Y en lugar de eso..."

        p "..."

    if aftermorning04_FittingRoom_ButtocksDickOver == True:

        d "Eso sin mencionar que pusiste tu polla sobre mis nalgas..."

    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True:

        d "Eso sin mencionar que te masturbaste con mis nalgas y acabaste corriéndote sobre mi espalda y trasero..."

    if aftermorning04_FittingRoom_FuckherConsent == True:

        d "Eso sin mencionar que me metiste la puta polla sin lubricación ni condón mientras hablaba con la dependienta..."

    if morning04_Shopping_didaccum_Cond == True:

        d "Eso sin mencionar que hiciste que me corriera con tus dedos en el probador..."

    if morning04_Shopping_didaccumANAL_Cond == True: #Didac cum, but only for anal.

        d "Eso sin mencionar que hiciste que me corriera con tus dedos en el probador..."

        p "Sí..."

        extend " Pero ¿dónde tenía esos dedos?"

    if morning04_Shopping_youcum_Cond == True:

        d "Eso sin mencionar lo que llegaste a correrte en el suelo del probador..."

    d "después de lo que me has llegado a hacer..."

    d "¿Te me pones moralista?"
    
    p "Euh..."

    extend " Yo..."

    #Susurro
    scene black
    show an04_Dgrabbingshirt_background:
        zoom 0.6
    show whisper_mc_front:
        whisper_didac_night_pos_02
    show whisper_d_mouth Talking:
        whisper_didac_night_pos_02
    show whisper_d_nose:
        whisper_didac_night_pos_02
    with dissolve

    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True:

        d "Eres un puto cerdo,"

    else:
    
        d "Eres un cerdo,"

    extend " [protname]."
    
    d "¿Lo sabías?"

    #Mordida en la oreja.
    show whisper_d_mouth bite_bite
    show whisper_d_nose bite
    with vpunch

    play sound "audio/characters/protagonist/au01.ogg"
    
    p "¡AUH!"

    #Oreja de protagonista desaparece de escena.
    scene black
    show an04_Dgrabbingshirt_background:
        zoom 0.6
    show whisper_d_mouth bite_smile02:
        whisper_didac_night_pos_03
    show whisper_d_nose bite:
        whisper_didac_night_pos_03
    with hpunch
    
    n "Te apartas de ella instintivamente sin que te ofrezca mucha resistencia."

    #Observas a Dídac con ropa interior ¿Amarilla?

    scene bg_dark_a
    show didacfbody_fullbody_scene:
        subpixel True
        zoom 1.5 xanchor 0.6 yanchor 3.3 #From Bottom
        easein 50.0 zoom 1.5 xanchor 0.75 yanchor 1.1 #Top face without eyes.
    with dissolve
    
    n "Contemplas su cuerpo, al cual solo le cubren dos prendas íntimas de color amarillo,"
    
    n "dejando al descubierto su reducido, pero esculpido cuerpo femenino,"
    
    n "con unas caderas marcadas, y dos pechos voluptuosos."

    window hide dissolve
    pause
    
    d "Te estás ruborizando,"

    extend " [protname]."

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little

    show didacfbodybelow naked:
        dfbody_atright_little
    show didacfbodybelow_panties yellowblack:
        dfbody_atright_little
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_little
    show didacfbodytop brayellowblack:
        dfbody_atright_little
    show didacfbodytop_naked_drops 00:
        dfbody_atright_little
    show didacfhandr leg_naked:
        dfbody_atright_little
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_little
    show didacfbodycloth_top empty:
        dfbody_atright_little
    show didacfhandl hip_naked:
        dfbody_atright_little
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_little
    #show didacfbody_afternight03_hallway03_b:
        #dfbody_atright_little
    show didacf_eyebrows angryx02:
        dfexpressions_atright_little
    show didacf_blush 02:
        dfexpressions_atright_little
    show didacf_eyes 03:
        dfexpressions_atright_little
    show didacf_pupils down03:
        dfexpressions_atright_little
    show didacfbodytop_hair:
        dfbody_atright_little
    show didacf_mouth happy_Talkingx03:
        dfexpressions_atright_little
    with fade
    
    d "Y no veo que eso de ahí se te esté bajando..."

    show didacf_eyebrows suspiciousx01
    show didacf_blush 02
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth happy_Silentx03
    with dissolve
    
    p "..."

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Talkingx05
    with dissolve
    
    d "¿No te gusta lo que ves?"

    show didacf_eyebrows serious
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happybiting_Silentx04
    with dissolve

    pt "Pero si con lo oscuro que está esto,"

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happybiting_Silentx06
    with dissolve

    pt "¡Apenas veo nada!"

#########################################################
    
    if config.version <= "00.07.03": #After 2nd date with Neus, Didac no longer grabs you.
        
        call endupdatescript
    
#######################################################

    show didacf_eyebrows surprisex01
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Dídac..."

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little
    show bg livingroom_roomOthersLingerie_night_LightOff_blur01:
        subpixel True
        alpha 0.0 
        easein_quad 2.0 alpha 1.0
    show didacfbodybelow naked:
        dfbody_atright_closex2
    show didacfbodybelow_panties yellowblack:
        dfbody_atright_closex2
    show didacfbodybelow_naked_drops 00:
        dfbody_atright_closex2
    show didacfbodytop brayellowblack:
        dfbody_atright_closex2
    show didacfbodytop_naked_drops 00:
        dfbody_atright_closex2
    show didacfhandl hip_naked:
        dfbody_atright_closex2
    show didacfhandl_hip_naked_drops 00:
        dfbody_atright_closex2
    show didacf_blush 02:
        dfexpressions_atright_closex2
    show didacf_eyes 04:
        dfexpressions_atright_closex2
    show didacf_pupils down04:
        dfexpressions_atright_closex2
    show didacf_eyebrows surprisex01:
        dfexpressions_atright_closex2
    show didacfbodytop_hair:
        dfbody_atright_closex2
    show didacf_mouth happybiting_Silentx04:
        dfexpressions_atright_closex2
    show didacfhandr leg_naked:
        dfbody_atright_closex2
    show didacfhandr_leg_naked_drops 00:
        dfbody_atright_closex2
    with dissolve
    
    pt "¡Dídac!"

    pt "¡No!"

    pt "¡¿Qué haces?!"

    pt "¡No te me acerques tanto!"

    show didacf_eyebrows normal
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "Dime..."

    extend " [protname]."

    show didacf_eyebrows surprisex02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Si me sigues provocando así,"

    extend " no sé si podré retenerme..."

    show didacf_blush 03
    show didacf_eyebrows angryx02
    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¿Y qué te detiene?"

    show didacf_blush 02
    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Ya sabes lo que me detiene..."

    show didacf_blush 01
    show didacf_eyebrows angryx03
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "No,"

    extend " no lo sé."

    show didacf_blush 02
    show didacf_eyebrows surprisex02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Y si te dejo preñada;"

    extend " ¡¿Qué?!"

    show didacf_blush 03
    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Eso solo ocurriría si llegaras a correrte dentro de mí..."

    show didacf_blush 02
    show didacf_eyebrows normal
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "Por las experiencias que me has llegado a contar..."

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "dices que sabes controlar muy bien ese impulso y sacarla cuando es el momento."

    show didacf_blush 01
    show didacf_eyebrows surprisex01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Pero en este caso,"

    extend " es demasiado arriesgado."

    show didacf_blush 02
    show didacf_eyebrows suspiciousx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¿Así que lo que te impide hacer nada conmigo es solo eso?"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "..."

    show didacfhandr taking_centerbra
    show didacf_eyebrows suspiciousx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happy_Silentx01
    with dissolve
    
    n "Una de las manos de Dídac se desliza dentro de su sujetador,"

    show didacfhandr condoms_xxl3
    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx04
    with dissolve
    
    n "y regresa enfrente de ti mostrándote un {i}pack{/i} de tres condones {b}XXL{/b}."

    show didacf_eyebrows surprisex01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "En ese caso..."

    extend " ¿Por qué no te pones uno de estos?"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx05
    with dissolve
    
    p "..."

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happybiting_Silentx05
    with dissolve

    pt "Me lo podría haber dicho antes..."

    show didacf_eyebrows serious
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx03
    with dissolve

    p "¿De dónde...?"

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "¿Te crees que tengo diez años?"

    show didacf_eyebrows surprisex01
    show didacf_eyes 02
    show didacf_pupils downLeft02
    show didacf_mouth happy_Talkingx03
    with dissolve
    
    d "Siempre tengo alguno de reserva."

    show didacf_blush 03
    show didacf_eyebrows sadx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth happy_Talkingx04
    with dissolve
    
    d "Aunque nunca me imaginé que te los daría a ti,"

    extend " para que los usaras conmigo..."

    show didacf_eyebrows surprisex02
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Pero..."

    extend " ¡¿Por qué?!"

    show didacf_eyebrows sadx03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "¡Dídac!"

    p "¡¿Acaso has olvidado que eras un tío?!"

    show didacfhandr taking_centerbra
    show didacf_eyebrows angryx02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "No."

    show didacfhandr leg_naked
    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Tengo muy presente qué era,"

    extend " y quién soy."

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "No te confundas."

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "Lo siento,"

    p "¡pero esto que estás haciendo ahora jamás lo habría hecho el Dídac que yo conozco!"

    show didacf_eyebrows angryx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "No tienes ni puñetera idea de lo que estás hablando."

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "No sabes una puta mierda..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Desde que he llegado de compras,"

    d "¿sabes cuántas horas han pasado...?"

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Llevo toda la tarde y toda la noche masturbándome como una jodida ninfómana."

    show didacf_eyebrows angryx03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "Ya he probado todo..."

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "Los dedos,"

    extend " los mangos de los cubiertos gruesos,"

    extend " restregarme por los cojines,"

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "duchas frías,"

    extend " duchas calientes usando el chorro de agua como estimulante,"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "los plátanos que teníamos en la nevera..."

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "¡Hasta he salido a la calle para ir a un sex-shop y comprarme un consolador enorme!"

    show didacf_eyebrows serious
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¡Y otro con vibración y extra-estimulación para el clítoris!"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "..."

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_mouth sad_Silentx05
    with dissolve

    pt "¡¿Cómo que esos plátanos que teníamos en la nevera?!"

    show didacf_eyebrows sadx01
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    pt "Son los que me iba a comer antes de ir a dormir."

    show didacf_eyebrows sadx03
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    pt "Bueno,"

    extend " ahora ya no,"

    extend " está claro..."

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¡¿Y sabes qué?!"

    show didacf_eyebrows angryx04
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Talkingx09
    with vpunch
    
    d "¡No ha servido de nada!"

    show didacf_eyebrows angryx03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx08
    with dissolve
    
    p "..."

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx04
    with dissolve
    
    d "..."

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "¿Y qué te hace pensar que,"

    extend " si yo hiciera el amor contigo,"

    extend " quedarías satisfecho?"

    show didacf_eyebrows surprisex01
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Después de todo lo que has probado..."

    show didacf_eyebrows sadx02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx07
    with dissolve
    
    p "Yo no hago milagros..."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "Hacer el amor..."


    d "¡¿De qué siglo vienes?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "El sexo no tiene nada que ver con el amor."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx07
    with dissolve
    
    d "¡Idiota!"

    show didacf_eyebrows surprisex01
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "No estoy completamente de acuerdo con eso..."

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "Y de todos modos,"

    p "¿por qué tiene que ser conmigo?"

    show didacf_eyebrows serious
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Hay montones de tíos ahí fuera que estarían dispuestos a ayudarte en eso."

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "¡Eres mi amigo!"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx01
    with dissolve
    
    p "¡Mi compañero de piso!"

    show didacf_eyebrows sadx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx06
    with dissolve
    
    p "¡¿Cómo voy a mirarte a la cara cuando regreses a tu cuerpo original?!"

    show didacf_eyebrows sadx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."

    show didacf_eyebrows sadx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "Te prometo que jamás te volveré a sacar el tema,"

    d "ni te lo reprocharé..."

    show didacf_blush 02
    show didacf_eyebrows sadx02
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "Y si después de esto,"

    extend " no quieres volver a verme,"

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx003
    with dissolve
       
    d "te aseguro que te ayudaré a buscar un nuevo compañero de piso para compartir gastos."

    show didacf_eyebrows serious
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "¡¿Pero por qué conmigo?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡¿Y por qué no?!"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "¡Eres el único tío con el que tengo la suficiente confianza para hacer esto!"

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "El único tío que sé que no se quitará el condón justo antes de correrse para dejarme preñada."

    show didacf_eyebrows sadx01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Sabes que eso no es verdad..."

    show didacf_eyebrows serious
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "No todos los tíos son así de imbéciles."

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Además,"

    extend " ¡siempre podrías pagar a un profesional!"

    show didacf_eyebrows angryx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx04
    with dissolve
    
    d "..."

    show didacf_blush 03
    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Joder [protname]..."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¿¡Por qué me lo pones tan difícil?!"

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "¿Qué?"

    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "¡Estoy intentando buscar soluciones al problema!"

    p "¡¿No lo ves?!"

    show didacf_blush 04
    show didacf_eyebrows angryx04
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡Tienes que ser tú idiota!"

    show didacf_blush 03
    show didacf_eyebrows angryx03
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "¡¿Pero por qué?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¡Porque cada vez que casi logro alcanzar un orgasmo,"

    show didacf_eyebrows angryx04
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "es porque me imagino tu polla dentro de mí!"

    show didacf_eyebrows angryx03
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Porque cada vez que consigo conciliar el sueño,"

    show didacf_blush 04
    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx002
    with dissolve
    
    d "fantaseo con que me arrancas la ropa,"

    extend " y me embistes contra la pared."

    show didacf_eyebrows serious
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "Porque en cada cilindro,"

    extend " rulo,"

    extend " rollo,"

    extend " rodillo,"

    extend " tubo,"

    extend " columna..."

    show didacf_eyebrows sadx01
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "sea en la calle o en casa..."

    show didacf_eyebrows sadx02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Talkingx004
    with dissolve
    
    d "¡Solo veo tu polla en erección y no tengo otro remedio que ir a algún lugar a masturbarme!"

    show didacf_eyebrows sadx03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "..."

    show didacf_eyebrows sadx02
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_mouth sad_Silentx04
    with dissolve
    
    d "..."

    show didacf_eyebrows angryx01
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "..."

    show didacf_blush 03
    show didacf_eyebrows angryx04
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx09
    with dissolve
    
    d "¡¡DI ALGO JODER!!"

    show didacf_blush 04
    show didacf_eyebrows sadx01
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sad_Silentx03
    with dissolve

    p "¿Casi consigues un orgasmo?"

    show didacf_blush 03
    show didacf_eyebrows sadx02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Después de todo esto que me has contado,"

    p "¿no has tenido ni un solo orgasmo?"

    show didacf_blush 04
    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "Solo uno..."

    d "y prefiero no contarte los detalles..."

    show didacf_eyebrows angryx04
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx04
    with dissolve

    p "..."

    show didacf_blush 03
    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx03
    with dissolve

    #Cara de ira contenida.
    
    p "Has dicho que el sexo no era necesariamente hacer el amor..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "¡Y así es!"

    show didacf_blush 04
    show didacf_eyebrows normal
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "¿Y cómo definirías el no poder dejar de pensar en mí a cada instante?"

    show didacf_eyebrows angryx04
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Talkingx08
    with dissolve
    
    d "Gilipollas."

    show didacf_blush 03
    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx04
    with dissolve
    
    p "¡¿Qué?!"

    extend " ¡Tío!"

    show didacf_blush 02
    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth sad_Silentx03
    with dissolve

    p "¡Me preocupas!"

    extend " ¡¿Vale?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "Pues no te preocupes tanto..."

    extend " ¡Y ayúdame!"

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx05
    with dissolve
    
    p "¡¿Cómo?!"

    show didacf_eyebrows angryx04
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Talkingx09
    with vpunch
    
    d "¡Follándome!"

    d "¡JODER!"

    show didacf_eyebrows angryx02
    show didacf_eyes 01
    show didacf_pupils down01
    show didacf_mouth sad_Talkingx06
    with dissolve
    
    d "¡Mírate cómo tienes la polla!"

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "¡Estás igual o peor que yo!"

    show didacf_eyebrows sadx01
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_mouth sadbiting_Silentx05
    with dissolve
    
    menu afternight04_Didac_FuckMe:
            
        pt "¿Qué coño se supone que tengo que hacer?" 
            
        "Dídac... ¡Eres un puto tío! ¡Mi amigo! Jamás haría eso.":

            call p_Help
            
            $pl.ch_pts("dp",-1)
                    
            jump afternight04_Didac_FuckMe_No
            
        "De acuerdo... ":

            call p_Help
            
            $pl.ch_pts("dp",2)
                    
            jump afternight04_Didac_FuckMe_Yes

    
label afternight04_Didac_FuckMe_Yes:

    show didacf_eyebrows surprisex01
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Talkingx02
    with dissolve
    
    d "¿Qué?"

    play music "audio/music/alcaknight/are_you_still_dreaming.ogg" fadein 3.0 fadeout 3.0

    show didacf_eyebrows normal
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "¡He dicho que vale!"

    show didacf_blush 03
    show didacf_eyebrows surprisex01
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Talkingx03
    with dissolve
    
    d "¿En serio?"

    show didacf_eyebrows normal
    show didacf_eyes 00
    show didacf_pupils left00
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Oye..."

    extend " si te lo estás pensando..."

    show didacf_eyebrows serious
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Talkingx04
    with dissolve
    
    d "¡No!"

    extend " ¡No!"

    show didacf_eyebrows sadx01
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx003
    with dissolve
    
    d "Es solo que..."

    d "pensaba que iba a costarme más..."

    show didacf_eyebrows sadx02
    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_mouth happy_Silentx01
    with dissolve
    
    pt "¿Más aún?"

    jump afternight04_Didac_FuckMe_Yes02

label afternight04_Didac_FuckMe_Yes02:

    show didacf_eyebrows sadx03
    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_mouth happy_Silentx02
    with dissolve
    
    p "..."

    show didacf_eyebrows normal
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_mouth sad_Silentx02
    with dissolve
    
    d "..."

    show didacf_blush 04
    show didacf_eyebrows surprisex01
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sad_Silentx01
    with dissolve
    
    pt "¿Y ahora qué?"

    show didacf_eyebrows sadx01
    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_mouth happybiting_Silentx03
    with dissolve
    
    d "..."

    show didacf_eyebrows sadx02
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_mouth happybiting_Silentx04
    with dissolve
    
    pt "Joder..."

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_mouth sadbiting_Silentx05
    with dissolve
    
    pt "Qué situación tan jodidamente incómoda..."

    show didacf_eyebrows surprisex02
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx03
    with dissolve
    
    p "Dídac..."

    show didacf_eyebrows sadx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happy_Silentx03
    with dissolve
    
    p "¿De verdad estás seguro?"

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx05
    with dissolve

#########################################################
    
    if config.version <= "00.07.06": #After 2nd date with Neus, You decide to Fuck Didac.
        
        call endupdatescript
    
#######################################################

    # Te muestra sus dedos mojados  # NOT FINISHED
    
    n "Una de sus manos se desplaza hasta su entrepierna y con un sutil movimiento te la pone ante tus ojos."

    show didacf_blush 03
    show didacf_eyebrows normal
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happy_Talkingx04
    show didacfhandr wetfingers_brayellowblack
    with dissolve
    
    d "¿Ves esto?"

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx03
    with dissolve
    
    n "Sus dedos están empapados de un líquido transparente y espeso."

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth happy_Silentx05
    with dissolve
    
    p "Sí..."

    show didacf_eyebrows normal
    show didacf_eyes 02
    show didacf_pupils downLeft02
    show didacf_mouth happy_Talkingx02
    with dissolve
    
    d "Esto ha sido solo de haberte abrazado y estar agarrándotela..."

    show didacf_eyebrows serious
    show didacf_eyes 05
    show didacf_pupils downLeft05
    show didacf_mouth happy_Silentx03
    with dissolve
    
    p "..."

    show didacf_eyebrows sadx01
    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_mouth sad_Talkingx003
    show didacfhandr wetfingers_mouth
    with dissolve

    # Lamiendo sus dedos húmedos # NOT FINISHED
    
    n "Se acerca esa mano empapada a los labios,"

    n "y empieza a relamer la punta de sus dedos."

    show didacf_blush 02
    show didacf_eyebrows surprisex01
    show didacf_eyes 04
    show didacf_pupils downLeft04
    show didacf_mouth happy_Talkingx02
    show didacfhandr leg_naked
    with dissolve
    
    d "¿Sabes...?"

    show didacf_eyebrows normal
    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_mouth happy_Talkingx04
    with dissolve
    
    d "Siempre me ha encantado este sabor en otras chicas..."

    show didacf_blush 03
    show didacf_eyebrows serious
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth happy_Talkingx03
    with dissolve
    
    d "Y creo que mi sabor es especialmente dulce..."

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx05
    with dissolve
    
    pt "Está claro que intenta provocarme..."

    #Close shot your pants. Finished.

    scene black
    show an04_Dgrabbingshirt_scene 06:
        subpixel True
        zoom 1.0 xanchor 1.0 yanchor 2.0
        easein_quad 15.0 zoom 1.25 xanchor 0.45 yanchor 2.4 #Hand Dick
    with dissolve
    
    n "Y, por lo que respecta a tu entrepierna,"

    n "lo está consiguiendo."
    
    n "Sientes tus pantalones a punto de estallar de lo dura que la tienes."

    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 0.5 fadeout 3.0

    scene morning04_bg livingroom_roomOthersLingerie_night_LightOff_blur01
    show bg livingroom_roomOthersLingerie_night_LightOff_blur02:
        subpixel True
        alpha 0.0 
        easein_quad 10.0 alpha 1.0
    show didacfbodybelow naked:
        dfbody_close_
        dfbody_closeX2
    show didacfbodybelow_panties yellowblack:
        dfbody_close_
        dfbody_closeX2
    show didacfbodybelow_naked_drops 00:
        dfbody_close_
        dfbody_closeX2
    show didacfbodytop brayellowblack:
        dfbody_close_
        dfbody_closeX2
    show didacfbodytop_naked_drops 00:
        dfbody_close_
        dfbody_closeX2
    show didacfbodycloth maleshirt_empty:
        dfbody_close_
        dfbody_closeX2
    show didacfhandl hip_naked:
        dfbody_close_
        dfbody_closeX2
    show didacfhandl_hip_naked_drops 00:
        dfbody_close_
        dfbody_closeX2
    #show dfbody_afternight03_hallway03_b_superdark:
        #dfbody_closeX2
    show didacf_blush 02:
        dexpressions_close_ 
        dexpressions_closeX2
    show didacf_eyes 04:
        dexpressions_close_
        dexpressions_closeX2
    show didacf_pupils down04:
        dexpressions_close_
        dexpressions_closeX2
    show didacf_eyebrows suspiciousx01:
        dexpressions_close_
        dexpressions_closeX2
    show didacfbodytop_hair:
        dfbody_close_
        dfbody_closeX2
    show didacf_mouth happy_Talkingx05:
        dexpressions_close_
        dexpressions_closeX2
    show didacfhandr leg_naked:
        dfbody_close_
        dfbody_closeX2
    show didacfhandr_leg_naked_drops 00:
        dfbody_close_
        dfbody_closeX2
    with dissolve
    
    d "¿Por qué no te los quitas?"

    show didacf_eyebrows angryx01
    show didacf_eyes 03
    show didacf_pupils downLeft03
    show didacf_mouth happy_Talkingx06
    with dissolve
    
    d "A mí apenas me queda ropa..."

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Talkingx06
    with dissolve
    
    d "Y tú aún vas demasiado vestido..."

    show didacf_eyebrows angryx01
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Silentx05
    with dissolve
    
    p "..."

    show didacf_eyebrows normal
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth happy_Talkingx03
    with dissolve
    
    d "¿O es que prefieres que te desnude yo misma?"

    show didacf_eyebrows normal
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx02
    with dissolve
    
    p "Tú lo has dicho,"

    p "apenas..."

    show didacf_eyebrows surprisex01
    show didacf_eyes 02
    show didacf_pupils down02
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    p "Aún llevas algo de ropa."

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx05
    with dissolve
    
    d "..."

    scene bg_dark_a
    show didacfbody_fullbody_naked_scene:
        subpixel True
        zoom 1.25 xanchor 0.75 yanchor 0.55 #Face
        ease_quad 15.0 zoom 1.25 xanchor 0.6 yanchor 1.6 #Boobs
        easein_quad 20.0 zoom 1.0 xanchor 0.6 yanchor 3.0 #From Bottom distance
    with dissolve

    d "¿Mejor...?"

    p "..."
    
    n "Hasta ese instante no te habías percatado del ligero temblor que sufría en sus piernas."
    
    pt "Qué raro..."

    window hide dissolve
    pause

    scene morning04_bg livingroom_roomOthersLingerie_night_LightOff_blur02
    show didacfbodybelow naked:
        dfbody_closeX2_little_
    show didacfbodybelow_naked_drops 00:
        dfbody_closeX2_little_
    show didacfbodytop naked:
        dfbody_closeX2_little_
    show didacfbodytop_naked_drops 00:
        dfbody_closeX2_little_
    show didacfhandr leg_naked:
        dfbody_closeX2_little_
    show didacfhandr_leg_naked_drops 00:
        dfbody_closeX2_little_
    show didacfbodycloth maleshirt_empty:
        dfbody_closeX2_little_
    show didacfhandl hip_naked:
        dfbody_closeX2_little_
    show didacfhandl_hip_naked_drops 00:
        dfbody_closeX2_little_
    #show dfbody_afternight03_hallway03_b_superdark:
        dfbody_closeX2_
    show didacf_blush 02:
        dexpressions_closeX2_little_
    show didacf_eyes 05:
        dexpressions_closeX2_little_
    show didacf_pupils front05:
        dexpressions_closeX2_little_
    show didacf_eyebrows serious:
        dexpressions_closeX2_little_
    show didacfbodytop_hair:
        dfbody_closeX2_little_
    show didacf_mouth happybiting_Silentx04:
        dexpressions_closeX2_little_
    with dissolve

    #Ella se desnuda.

    pt "Coño..."

    pt "No se está por tonterías..."

    show didacf_blush 03
    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx05
    with dissolve
    
    d "Si no te desnudas ya..."

    d "¡Voy a ir a por unas tijeras!"

    d "¡Te lo juro!"

    show didacf_blush 03
    show didacf_eyebrows angryx02
    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_mouth sad_Silentx05
    with dissolve
    
    n "Crees que lo más sensato es obedecerle..."

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_mouth sadbiting_Silentx02
    with dissolve
    
    n "Empiezas por quitarte los pantalones, pues realmente empezaban a hacerte hasta daño."

    show didacf_blush 04
    show didacf_eyebrows sadx03
    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    n "Pero apenas consigues bajártelos hasta las rodillas..."
    
    window hide dissolve
    pause

    stop music fadeout 3.0

    scene black
    with hpunch

    # NOT FINISHED

#########################################################
    
    if config.version <= "00.07.07": #After 2nd date with Neus, She pushes you over the sofa.
        
        call endupdatescript
    
#######################################################

    # Black screen

    play sound "audio/sfx/fall06.ogg"

    n "Dídac te empuja hasta el sofá."

    play sound "audio/sfx/click02.ogg"

    play music "audio/music/kevinmacleod/fearless_first.ogg" fadein 3.0 fadeout 3.0

    # Scroll Up of the Didac HD image while she is biting her lip.
    scene afternight04_beforesexbattle_body_01:
        subpixel True
        zoom 3.0 xanchor 0.19 yanchor 0.0 #Face
        ease_quad 30.0 zoom 1.5 xanchor 0.08 yanchor 0.13  #Dick
        
    show white:
        subpixel True
        additive 1.0
        alpha 1.0
        easein_quad 10.0 alpha 0.0
    
    with dissolve

    n "Sin tiempo para reaccionar,"

    n "sientes que se pone encima de ti, quitándote por completo los pantalones junto con tus bóxers,"

    n "y poniéndose encima de tu erecto miembro,"

    n "después de haber encendido la lámpara para iluminar la estancia."

    n "Sus caderas empiezan a moverse frotando su lubricada entrepierna con tu desnudo miembro."

    window hide dissolve
    pause

    # First shot of one of the condoms on her hand.

    scene an04_Dgrabbingshirt_background:
        zoom 0.5
    show an04_holding_xxlcondom:
        subpixel True
        zoom 1.0 xanchor 0.2 yanchor 0.0
        easein_quad 5.0 zoom 0.5 xanchor 0.0 yanchor 0.0
    with dissolve
    
    d "Toma..."

    extend " póntelo ya."
    
    n "Ves en su mano uno de los condones que te había mostrado anteriormente."
    
    p "Eumm..."
    
    p "¿Así?"

    p "¿Directamente?"

    p "¿Sin juego previo?"

    window hide dissolve
    pause

    # Scene of Didac over you (without being in the battle., but being the same image.)

    scene afternight04_beforesexbattle_body_02:
        zoom 3.0 xanchor 0.19 yanchor 0.0 #Face
    show afternight04_sexbattle_d_blush 01_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyes 04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_pupils front04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyebrows normal_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_hair HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_mouth sad_Talkingx003_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    with dissolve
    
    d "¿Juego previo?"

    d "¿A qué coño te refieres?"

    show afternight04_sexbattle_d_eyes 03_HD_a
    show afternight04_sexbattle_d_pupils front03_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx03_HD_a
    with dissolve
    
    p "No sé..."

    extend " pues..."
    
    menu afternight04_Didac_OralSexOrKiss:
            
        pt "¿Acaso quieres que lo hagamos como animales?" 
            
        "Quizás un poco de sexo oral...":
            
            $pl.ch_pts("dp",-2)
                    
            jump afternight04_Didac_OralSexOrKiss_pansy
            
        "Por lo menos un beso...":
            
            $pl.ch_pts("dp",-1)
                    
            jump afternight04_Didac_OralSexOrKiss_pansy
            
        "Bien, entonces... ¡Follemos como animales!":
        
            $pl.ch_pts("dp",2)

            show afternight04_sexbattle_d_blush 01_HD_a
            show afternight04_sexbattle_d_eyes 05_HD_a
            show afternight04_sexbattle_d_pupils front05_HD_a
            show afternight04_sexbattle_d_eyebrows serious_HD_a
            show afternight04_sexbattle_d_mouth happy_Talkingx03_HD_a
            with dissolve
            
            d "¡Eso me gusta más cómo suena!"
                    
            jump afternight04_Didac_OralSexOrKiss_LikeAnimals
    
label afternight04_Didac_OralSexOrKiss_pansy:

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils front05_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx02_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx002_HD_a
    with dissolve
    
    d "¿Eres marica o qué?"

    show afternight04_sexbattle_d_eyes 03_HD_a
    show afternight04_sexbattle_d_pupils front03_HD_a
    show afternight04_sexbattle_d_eyebrows angryx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx04_HD_a
    with dissolve
    
    d "No voy a meter mi boca ahí."

    show afternight04_sexbattle_d_eyes 04_HD_a
    show afternight04_sexbattle_d_pupils front04_HD_a
    show afternight04_sexbattle_d_eyebrows angryx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx04_HD_a
    with dissolve
    
    p "..."

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils right05_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx03_HD_a
    with dissolve
    
    pt "Coño..."

    extend " creo que cada vez lo entiendo menos..."

    show afternight04_sexbattle_d_eyes 04_HD_a
    show afternight04_sexbattle_d_pupils front04_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx02_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx04_HD_a
    with dissolve
    
    d "A ver si así lo entiendes mejor..."

    show afternight04_sexbattle_d_eyes 01_HD_a
    show afternight04_sexbattle_d_pupils front01_HD_a
    show afternight04_sexbattle_d_eyebrows normal_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx004_HD_a
    with dissolve

    d "Voy"

    extend " CA-"

    extend "CHON-"

    extend "DA."

    show afternight04_sexbattle_d_eyes 04_HD_a
    show afternight04_sexbattle_d_pupils front04_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx03_HD_a
    with dissolve
    
    d "¿Lo entiendes?"

    show afternight04_sexbattle_d_blush 02_HD_a
    show afternight04_sexbattle_d_eyes 02_HD_a
    show afternight04_sexbattle_d_pupils down02_HD_a
    show afternight04_sexbattle_d_eyebrows normal_HD_a
    show afternight04_sexbattle_d_mouth happy_Talkingx02_HD_a
    with dissolve
    
    d "Lo que quiero es desahogarme."
    
    jump afternight04_Didac_OralSexOrKiss_LikeAnimals
    
label afternight04_Didac_OralSexOrKiss_LikeAnimals:

    scene afternight04_beforesexbattle_body_02:
        zoom 3.0 xanchor 0.19 yanchor 0.0 #Face
    show afternight04_sexbattle_d_blush 01_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyes 04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_pupils front04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyebrows normal_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_hair HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_mouth sad_Talkingx003_HD_a:
        afternight04_beforesexbattle_close_expressions_HD

    show afternight04_sexbattle_d_blush 02_HD_a
    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils down05_HD_a
    show afternight04_sexbattle_d_eyebrows sadx03_HD_a
    show afternight04_sexbattle_d_mouth happybiting_Silentx04_HD_a
    with dissolve
    
    pt "Eumm..."

    pt " quizás no esté enamorada al fin y al cabo..."

    # 1rst shots 

    scene afternight04_beforesexbattle_body_03:
        subpixel True
        zoom 3.0 xanchor 0.19 yanchor 0.0 #BelowFace # Resoultion should be no problem
        easein_quad 10.0 zoom 1.5 xanchor 0.08 yanchor 0.13  #Dick # Resoultion should be no problem

    with dissolve

    n "Su entrepierna es ligeramente más ardiente y su movimiento es cada vez más acelerado,"

    n "acercándose peligrosamente al glande."
    
    p "..."

    p "Dídac..."

    window hide dissolve
    pause

    # Volviendo a su rostro.

    scene afternight04_beforesexbattle_body_02:
        zoom 3.0 xanchor 0.19 yanchor 0.0 #Face
    show afternight04_sexbattle_d_blush 03_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyes 05_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_pupils down05_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_eyebrows sadx04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_hair HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    show afternight04_sexbattle_d_mouth happybiting_Silentx04_HD_a:
        afternight04_beforesexbattle_close_expressions_HD
    with dissolve
    
    d "¿Sifhh...?"
    
    pt "Si le estoy hablando,"

    pt "¿por qué me sigue mirando la polla y no me mira a la cara?"

    p "¿Ya me has puesto el condón?"

    show afternight04_sexbattle_d_eyes 01_HD_a
    show afternight04_sexbattle_d_pupils front01_HD_a
    show afternight04_sexbattle_d_eyebrows surprisex01_HD_a
    show afternight04_sexbattle_d_mouth happybiting_Silentx01_HD_a
    with dissolve
    
    d "..."

    show afternight04_sexbattle_d_eyes 00_HD_a
    show afternight04_sexbattle_d_pupils down00_HD_a
    show afternight04_sexbattle_d_eyebrows surprisex02_HD_a
    show afternight04_sexbattle_d_mouth sadbiting_Silentx01_HD_a
    with dissolve
    
    p "..."

    show afternight04_sexbattle_d_blush 02_HD_a
    show afternight04_sexbattle_d_eyes 03_HD_a
    show afternight04_sexbattle_d_pupils front03_HD_a
    show afternight04_sexbattle_d_eyebrows angryx02_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx04_HD_a
    with dissolve
    
    d "¿No te lo habías puesto tú?"

    show afternight04_sexbattle_d_eyes 04_HD_a
    show afternight04_sexbattle_d_pupils front04_HD_a
    show afternight04_sexbattle_d_eyebrows angryx02_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx04_HD_a
    with dissolve
    
    p "¡Si ni siquiera me lo has llegado a dar!"

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils front05_HD_a
    show afternight04_sexbattle_d_eyebrows angryx03_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx06_HD_a
    with dissolve
    
    d "Joder..."

    d "¡pues póntelo!"

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils right05_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx04_HD_a
    with dissolve
    
    p "Pero si lo tienes tú..."

    show afternight04_sexbattle_d_eyes 02_HD_a
    show afternight04_sexbattle_d_pupils front02_HD_a
    show afternight04_sexbattle_d_eyebrows normal_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx02_HD_a
    with dissolve
    
    p "¿Por qué no me lo pones tú mismo?"

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils front05_HD_a
    show afternight04_sexbattle_d_eyebrows angryx01_HD_a
    show afternight04_sexbattle_d_mouth sad_Talkingx003_HD_a
    with dissolve
    
    d "No pienso tocarte la polla..."

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils front05_HD_a
    show afternight04_sexbattle_d_eyebrows suspiciousx02_HD_a
    show afternight04_sexbattle_d_mouth sad_Silentx05_HD_a
    with dissolve
    
    p "..."

    show afternight04_sexbattle_d_eyes 05_HD_a
    show afternight04_sexbattle_d_pupils right05_HD_a
    show afternight04_sexbattle_d_eyebrows serious_HD_a
    show afternight04_sexbattle_d_mouth sadbiting_Silentx03_HD_a
    with dissolve
    
    pt "Está fatal..."

    extend " está fatal..."
    
    n "Coges el condón que te ofrece Dídac,"

    n "y con la polla bien tiesa -y lubricada-,"
    
    n "no te resulta nada complicado ponerte el chubasquero."

    $ afternight04_sexbattle_started = True

    hide screen Points
    
    jump afternight04_sexbattle_start

    #jump morning05
    
    ##HERE IT COMES a Scene Sex with points with Didac.


#########################################################################################################
########################################################################################################
#######################################################################################################
######################################################################################################
#####################################################################################################


label afternight04_Didac_FuckMe_No:

    #"Dídac... ¡Eres un puto tío! ¡Mi amigo! Jamás haría eso.":

#########################################################
    
    if config.version <= "00.07.04": #After 2nd date with Neus, You reject to fuck Didac.
        
        call endupdatescript
    
#######################################################

    show didacf_eyebrows suspiciousx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "O sea... "

    if morning04_DidacHotforyou_Cond == True: #Te masturbas en la habitación mientras lo hace Didac.

        show didacf_eyebrows surprisex01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "te meneas la polla cuando me oyes gemir al masturbarme,"

        #d "Además... después de que te masturbaras en la habitación conmigo adentro..."

    if aftermorning04_FittingRoom_ButtocksDickOver == True: #Polla sobre las nalgas.

        show didacf_eyebrows surprisex01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "me bajas los pantalones para meter tu polla desnuda sobre mis nalgas,"

        #d "Eso sin mencionar que pusiste mi polla sobre mis nalgas..."

    if aftermorning04_FittingRoom_ButtocksDickOverMasturbate == True: #Polla sobre nalgas masturbándose.

        show didacf_eyebrows surprisex01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "me bajas los pantalones y usas mis nalgas para masturbar tu puta polla,"

        #d "Eso sin mencionar que te masturbaste con mis nalgas y acabaste corriéndote sobre mi espalda y trasero..."

    if aftermorning04_FittingRoom_FuckherConsent == True: #Penetración sin lubricación

        show didacf_eyebrows surprisex01
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_mouth sad_Talkingx03
        with dissolve

        d "si no llega a ser por la dependienta y mi grito,"

        extend " me hubieras follado sin condón,"

        #d "Eso sin mencionar que me metiste la puta polla sin lubricación ni condón mientras hablaba con la dependienta..."

    if morning04_Shopping_didaccum_Cond == True: #Didac Cum with your fingers.

        show didacf_eyebrows serious
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_mouth sad_Talkingx04
        with dissolve

        d "me metes el dedo hasta el fondo hasta que me corro en tu mano,"

        #d "Eso sin mencionar que hiciste que me corriera con tus dedos en el probador..."

    if morning04_Shopping_didaccumANAL_Cond == True: #Didac cum, but only for anal.

        show didacf_eyebrows serious
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_mouth sad_Talkingx04
        with dissolve

        d "me metes el dedo en el culo hasta el fondo hasta que me corro,"

        #d "Eso sin mencionar que hiciste que me corriera con tus dedos en el probador..."

        #p "Sí... ¿Pero dónde tenía esos dedos?"

    if morning04_Shopping_youcum_Cond == True: # You cum on ground.

        show didacf_eyebrows serious
        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_mouth sad_Talkingx04
        with dissolve

        d "te me corres en la mano mientras me estás metiendo el puto dedo,"

        #d "Eso sin mencionar lo que llegaste a correrte en el suelo del probador..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "Y encima tienes los santos cojones para decirme que como soy tu puto amigo,"

    extend " jamás harías eso..."

    show didacf_eyebrows angryx04
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx09
    with vpunch

    d "¡¿De qué coño vas hipócrita de mierda?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx08
    with dissolve

    p "¡Fuiste tú el que me provocaste!"

    show didacf_eyebrows angryx04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡Lo dices como si te hubiese obligado a punta de pistola!..."

    if aftermorning04_FittingRoom_FuckherConsent == True: #Penetración sin lubricación

        show didacf_eyebrows angryx03
        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "¿Y qué coño pensabas cuando me metiste la polla en el coño sin condón?"

    show didacf_eyebrows angryx02
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx07
    with dissolve

    p "Iba muy caliente, Didac..."

    show didacf_eyebrows angryx03
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡¿Y cómo coño vas ahora?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Una cosa es hacer preliminares..."

    p "otra muy distinta es follar..."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "O sea,"

    extend " meterle mano y poner cachonda a una tía está bien,"

    show didacf_eyebrows angryx03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx005
    with dissolve

    d "pero cuando esta te pide follar,"

    extend " le dices que la zurzan..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "Nunca te había tomado por un {b}calienta-bragas{/b},"

    extend " [protname]."

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx07
    with dissolve

    p "¡Dídac!"

    p "¡No eres una tía!"

    extend " ¡Eres un puto tío!"

    show didacf_eyebrows angryx02
    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Joder..."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "Eres pesado macho..."

    show didacf_eyebrows angryx01
    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡Ya sé que soy tío!"

    show didacf_eyebrows sadx01
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡¿Vale?!"

    show didacf_eyebrows sadx03
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡No hace falta que lo vayas repitiendo!"

    show didacf_eyebrows angryx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx06
    with dissolve

    p "¿Entonces qué quieres que te diga?"

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡Quiero que me folles y te dejes de hostias!"

    show didacf_eyebrows angryx04
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Silentx08
    with dissolve

    p "Pero cuando vuelvas a ser..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡¿Otra vez con eso?!"

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡Déjate ya de hostias!"

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "En serio [protname],"

    d "no tienes ni la más remota idea de qué coño viví ayer"

    d "y especialmente hoy..."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "No te puedes hacer ni puta idea."

    show didacf_eyebrows angryx02
    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_mouth sad_Talkingx003
    with dissolve

    d "Me dijiste que arreglarías el problema,"

    d "y sé que lo estás intentando."

    show didacf_eyebrows angryx03
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "Pero ya no puedo esperar más."

    show didacf_eyebrows angryx04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "Te lo juro [protname],"

    d "si no me follas tú,"

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡Buscaré a alguien para que lo haga!"

    show didacf_eyebrows angryx04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡¿Te queda claro?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Silentx06
    with dissolve

    menu afternight04_Didac_FuckMe02:
            
        pt "¿Lo dice en serio?" 

        "De acuerdo... ":
            call p_Help
            
            $pl.ch_pts("dp",5)
                    
            jump afternight04_Didac_FuckMe_Yes02
            
        "Lo siento, pero me niego a hacer lo que me pides. (AVISO: Esta ruta lleva a Dídac a follar con otros)":
            call p_Help
            
            $pl.ch_pts("dp",-1)
                    
            jump afternight04_Didac_FuckMe_No02

        "<Usar el maletín que te dio la rubia en el museo>" if p_prot_analgesic == "accepted":
            call p_Help

            jump afternight04_Didac_FuckMe_NCloro
            

label afternight04_Didac_FuckMe_No02:

    #with vpunch

    $ afternight04_Didac_Leaving_Cond = True

    play music "audio/music/alcaknight/bury_it.ogg" fadeout 0.2 fadein 0.1

    show didacf_eyebrows angryx04
    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_mouth sad_Talkingx09
    with vpunch

    d "{size=50}¡VETE A LA MIERDA!{/size}"

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little
    with hpunch

    n "Sientes que se desprende de ti bruscamente para luego ver cómo se aleja desnuda hacia su habitación."

    n "Oyes el ruido característico del armario abriéndose y sus respectivos cajones,"

    pt "¿En serio se va a ir a buscar a alguien para que se lo folle?"

    pt "¡¿Es que se le ha ido completamente la pinza?!"

    n "Aparece de nuevo cerrando la puerta tras de él de un modo brusco y sonoro."

    n "Lo ves dirigiéndose hacia la entrada del piso."

    $ saturation_tint_level = "default"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    scene afternight03_bg entrance_lighton
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with dissolve

    p "Dídac,"

    extend " escucha..."

    # show didacfbodybelow naked:
    #     dfbody_close_
    # show didacfbodybelow_panties park:
    #     dfbody_close_
    # show didacfbodybelow_naked_drops 00:
    #     dfbody_close_
    show didacfbodytop park:
        dfbody_close_
    show didacfbodytop_naked_drops 00:
        dfbody_close_
    show didacfhandr leg_naked:
        dfbody_close_
    show didacfhandr_leg_naked_drops 00:
        dfbody_close_
    show didacfhandl hip_naked:
        dfbody_close_
    show didacfhandl_hip_naked_drops 00:
        dfbody_close_
    show didacf_blush 02: 
        dexpressions_close_
    show didacf_eyes 03:
        dexpressions_close_
    show didacf_pupils front03:
        dexpressions_close_
    show didacf_eyebrows angryx02:
        dexpressions_close_
    show didacfbodytop_hair:
        dfbody_close_
    show didacfbodycloth_whole gabardine:
        dfbody_close_
    show didacf_mouth sad_Talkingx06:
        dexpressions_close_
    with dissolve

    d "¡¿Qué?!"

    show didacf_eyebrows angryx03
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx03
    with dissolve

    p "..."

    show didacf_eyebrows suspiciousx02
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "¡¿Te lo has repensado quizás?!"

    show didacf_eyebrows angryx01
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Sé coherente,"

    p "¿qué pretendes hacer saliendo así a la calle?"

    show didacf_eyebrows serious
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Si consigues encontrar a alguien a estas horas de la noche,"

    show didacf_eyebrows angryx01
    show didacf_eyes 02
    show didacf_pupils right02
    show didacf_mouth sad_Silentx03
    with dissolve

    p "lo más probable es que sean puros {a=https://es.wikipedia.org/wiki/Drogodependencia}{b}yonkis{/b}{/a} que probablemente te violen en manada sin ningún tipo de escrúpulo,"

    show didacf_eyebrows angryx02
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_mouth sad_Silentx06
    with dissolve

    p "y que probablemente tengan algún tipo de enfermedad de transmisión sexual."

    show didacf_eyebrows angryx03
    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_mouth sad_Silentx07
    with dissolve

    d "..." #Su mirada estaba fija ahora a la puerta con una ira contenida.

    show didacf_eyebrows angryx04
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "En ese caso,"

    d "sabrás que,"

    extend " si hubieras aceptado,"

    d "esto lo habrías podido evitar."

    play sound "audio/sfx/metal_keys_deposit.ogg"

    scene afternight03_bg entrance_lighton
    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    with hpunch

    play sound "audio/sfx/door_slam01.ogg"

    n "Rápidamente recoge sus llaves que estaban sobre la mesa de entrada, y sale al replano dando un portazo como nunca antes."

    p "..."

    pt "¡¿Qué coño?!"

    pt "¡Maldito imbécil!"

    pt "Está claro que no está en sus cabales..."

    pt "¡Esto no es normal!"

    pt "¡Va a conseguir que lo maten!"

    pt "Pero en el fondo él se lo ha buscado,"

    pt "¡no será porque no he intentado razonar con él!"

    pt "¡¿Qué culpa tengo yo?!"

    pt "¡Todo lo que he hecho hasta ahora es intentar ayudarle!"

    pt "¡Fue él quien se metió en todo este lío al intentar violar a Neus!"

    pt "¡Soy yo el que le está sacando sus castañas del fuego!"

    pt "¡¿Ahora él me hace chantaje emocional para que me lo folle?!"

    pt "¡Es su puto problema!"

    p "..."

    pt "Por otro lado..."

    pt "Dídac nunca se había comportado así,"

    pt "siempre ha sido alcornoque,"

    extend " terco,"

    extend " descuidado,"

    extend " misógino,"

    extend " salido..."

    pt "Pero jamás habría puesto su vida en riesgo por un polvo..."

    pt "¿Y si actúa así debido a la mordida?"

    pt "Me ha pedido ayuda primero,"

    extend " antes de hacer semejante locura..."

    pt "¡Puto Dídac!"

    menu afternight04_Didac_FollowHim_question:
            
        pt "¡¿Qué coño se supone que tengo que hacer ahora?!" 

        "<Ir a dormir>":
            
            #$pl.ch_pts("dp",-1)
                    
            jump afternight04_Didac_FollowHim_No
            
        "<Seguirle>":
            
            #$pl.ch_pts("dp",1)
                    
            jump afternight04_Didac_FollowHim_Yes
            

label afternight04_Didac_FollowHim_No:

    pt "¡Que le follen!"

    pt "Estoy hasta las narices de hacerle de niñera al malcriado de los cojones..."

    pt "¡Es él quien se lo ha buscado!"

    pt "Si no es capaz de controlarse,"

    pt "¡¿qué problema tengo yo?!"

    pt "De hecho, aún no sé ni por qué accedí a quedar con Neus..."

    pt "Quizás hasta pase de quedar con ella y todo"

    pt "con el plan que lleva el capullo este..."

    pt "Bah..."

    pt "Da igual..."

    play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0

    play sound "audio/sfx/metal_keys_deposit.ogg"

    scene afternight03_bg_entrance_lightoff_night
    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    pt "Estoy cansado y mañana será otro día..."

    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene afternight03_bg_shower
    with fade

    n "A regañadientes te diriges al baño a asearte,"

    stop music fadeout 3.0
    $ renpy.music.set_volume(0.05, delay=5.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    n "poco después llegas al dormitorio, donde -bajo las sábanas-, te reúnes de nuevo con {b}Morfeo{/b}."

    $ renpy.music.stop(channel='sfx1', fadeout = 5.0)

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    with dissolve

    window hide dissolve
    pause

    jump morning05

label afternight04_Didac_FollowHim_Yes:

    $ afternight04_Didac_FollowHim_Yes_Cond = True

    pt "¡JODER!"

    scene afternight03_bg entrance_lighton
    with dissolve

    n "A toda prisa te vuelves a poner las zapatillas deportivas, recoges las llaves y sales por la puerta intentando no dar un portazo."

    scene bg an04_flat_outside
    with dissolve

#########################################################
    
    if config.version <= "00.07.05": #After 2nd date with Neus, You decide to follow her.
        
        call endupdatescript
    
#######################################################

    $ saturation_tint_level = "dark"

    n "Observas que el ascensor está aún en funcionamiento"

    n "y que por lo tanto, te toca bajar las escaleras a toda prisa."

    scene bg an04_flat_stairs
    with dissolve

    n "Por suerte, tu cuerpo atlético te permite hacer tal proeza en menos tiempo de lo esperado" 

    scene bg an04_flat_gate_composition001:
        subpixel True
        zoom 1.0 xanchor 0.0 yanchor 0.0
        easein_quad 10.0 zoom 0.5 xanchor 0.0 yanchor 1.4 #General view door.
    with dissolve

    n "y consigues llegar a la planta baja justo cuando Dídac cierra la puerta de la calle."

    p "Ahh-Ahh-Ahh..." #Jadeo

    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0 

    pt "No creo que sea buena idea que me descubra,"

    pt "por lo visto no voy a conseguir hacerle cambiar de opinión"

    pt "y lo único que conseguiré es cabrearlo más..."

    pt "Lo mejor que puedo hacer es tratar de seguirlo sin que me descubra..."

    pt "Espero no perderlo de vista..."

    show bg an04_flat_gate_composition002:
        easein_quad 10.0 zoom 1.0 xanchor 0.8 yanchor 1.8 #Close to the gate.

    n "Decides esperar unos pocos segundos para seguir los pasos de tu compañero de piso,"

    scene bg an04_street_01_composition001:
        subpixel True
        zoom 0.5
        easein_quad 30.0 zoom 1.0 xanchor 0.5 yanchor 0.7
    with fade

    n "Al salir a la calle, al fondo de esta,"

    n "consigues vislumbrar su inconfundible pelo rojizo."

    pt "Por suerte, sus ropajes y su pelo son poco convencionales,"

    show bg an04_street_01_composition002
    with dissolve

    pt "así no me resultará del todo imposible seguirle la pista..."

    show bg an04_street_01_composition003
    with dissolve

    n "Durante varias calles, sigues a Dídac sin tener la más mínima idea de a dónde diablos se dirige."

    scene night03_bg street_catalunya_square
    with fade

    n "Las noches de verano en Barcelona son calurosas, iluminadas por el frío color rojizo y azulado de las inertes farolas de la ciudad."

    $ saturation_tint_level = "verydark"

    n "Vivir cerca del centro de la ciudad ayuda a poder llegar a casi cualquier lugar importante de forma bastante rápida,"

    n "aunque el alquiler no es precisamente barato,"

    n "pero también impide poder vivir en un lugar mínimamente tranquilo."

    scene bg an04_corteingles_composition 01:
        subpixel True
        xanchor 1.0 yanchor 1.0 zoom 1.0
        ease_quad 10.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    n "A pesar de la hora, aún sigue habiendo bastantes transeúntes recorriendo las calles,"

    show bg an04_corteingles_composition 02
    with dissolve

    n "especialmente, teniendo en cuenta que vivís en el corazón de la metrópolis, donde la ciudad nunca duerme."

    show bg an04_corteingles_composition 03
    with dissolve

    window hide dissolve
    pause

    scene bg an04_vialayetana_composition:
        subpixel True
        xanchor 0.5 yanchor 0.0 zoom 1.0
        ease_quad 8 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    n "Los coches no cesan de ir y venir en todas partes, los extranjeros, que recién vienen de tomar unas copas de más,"

    n "hacen de esta parte de la ciudad un lugar menos idóneo para el descanso,"

    n "y mucho menos para encontrar un lugar oscuro y silencioso."

    window hide dissolve
    pause

    scene bg an04_palaumusica_composition:
        subpixel True
        xanchor 0.0 yanchor 0.0 zoom 0.5
        ease_quad 12.0 xanchor 0.0 yanchor 1.9 zoom 0.5
    with fade

    pt "¡¿Ahora va al {a=https://es.wikipedia.org/wiki/Palacio_de_la_Música_Catalana}{i}Palau de la música{/i}{/a}!"

    pt "Me imagino que tarde o temprano se cansará de buscar y volverá a casa..."

    $ saturation_tint_level = "dark"

    pt "Lo que tenía pensado era una locura desde el principio..."

    window hide dissolve
    pause

    scene bg an04_street02_composition 01:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        easein_quad 12.0 xanchor 0.5 yanchor 0.0 zoom 0.67
    with fade

    n "A medida que lo ves andar a lo largo de las estrechas calles,"

    n "notas cómo su paso es irregular, sus piernas tambalean,"

    n "y en ocasiones usa la pared como apoyo."

    show bg an04_street02_composition 02
    with Dissolve (1.0)

    pt "¡¿Qué diablos le pasa?!"

    pt "¿Es que va borracho?"

    show bg an04_street02_composition 03
    with dissolve

    window hide dissolve
    pause

    scene bg an04_placasantagustivell_composition 01:
        subpixel True
        xanchor 1.0 yanchor 0.7 zoom 1.0
        ease_quad 12.0 xanchor 0.0 yanchor 0.5 zoom 1.0
    with fade

    pt "¿A dónde diablos va?"

    n "Su paso es cada vez más tambaleante y aunque estés a cierta distancia,"

    show bg an04_placasantagustivell_composition 02
    with Dissolve (1.0)

    n "te parece observar que la mano que no usa para apoyarse a la pared o los postes,"

    show bg an04_placasantagustivell_composition 03
    with Dissolve (1.0)

    n "la usa para agarrarse la entrepierna."

    show bg an04_placasantagustivell_composition 04
    with dissolve

    $ saturation_tint_level = "default"

    window hide dissolve
    pause

    scene bg an04_arctriumf_composition 01:
        subpixel True
        ###xanchor 0.0 yanchor 0.0 zoom 0.5 #Whole Picture
        ###xanchor 0.15 yanchor 1.0 zoom 0.85 #Arc Triomf
        xanchor 0.0 yanchor 1.3 zoom 1.0
        ease_quad 12.0 xanchor 0.15 yanchor 0.65 zoom 0.6
    with fade

    n "Su andar excéntrico -y aparentemente errático- os lleva hasta el conocido monumento {a=https://es.wikipedia.org/wiki/Arco_de_Triunfo_de_Barcelona}{i}Arc de Triomf{/i}{/a}."

    pt "¿Acaso quiere coger el metro...?"

    pt "Podría haberlo cogido en {a=https://es.wikipedia.org/wiki/Plaza_de_Cataluña}{i}Plaça Catalunya{/i}{/a}..."

    show bg an04_arctriumf_composition 02
    with dissolve

    pt "Espera..."

    extend " está yendo al paseo que lleva al parque..."

    show bg an04_arctriumf_composition 03:
        easein_quad 08.0 xanchor 1.1 yanchor 1.3 zoom 1.5
    with dissolve

    pt "¡Pero si está cerrado a estas horas!"

    show bg an04_arctriumf_composition 04
    with dissolve

    pt "Mierda,"

    extend " con este lugar tan iluminado no tengo dónde esconderme,"

    pt "tendré que dar un rodeo..."

    $ saturation_tint_level = "dark"

    window hide dissolve
    pause

    scene bg an04_park_entrance_far_background_compisition 01:
        subpixel True
        xanchor 0.0 yanchor 0.0 zoom 0.5
        easein_quad 12.0 xanchor 0.5 yanchor 0.5 zoom 1.0
    show an04_park_entrance_far_foreground 01:
        subpixel True
        xanchor 0.0 yanchor 0.25 zoom 1.5
        ease_quad 8.0 xanchor 0.15 yanchor 0.2 zoom 1.0
    with fade

    n "Después de atravesar toda la vía por la cera colindante, algo más oscura,"

    show bg an04_park_entrance_far_background_compisition 02
    show an04_park_entrance_far_foreground 02
    with Dissolve (2.0)

    n "regresas al luminoso paseo,"

    n "ocultándote detrás de la estatua que hay justo antes de cruzar el paso de cebra."

    show bg an04_park_entrance_far_background_compisition 03
    with Dissolve (1.0)

    window hide dissolve
    pause

    scene black
    with dissolve

    play sound "audio/sfx/hit01.ogg"

    ono "pum"

    $ saturation_tint_level = "dark"

    n "Con la esperanza de que Dídac no te haya oído."

    n "Te desplazas a la otra cera y te ocultas rápidamente tras una superficie metalizada que pertenece a una tienda cerrada de helados ambulante,"

    scene bg an04_entranceciutadella_composition 01:
        xanchor 0.0 yanchor 0.4 zoom 0.5

    show an04_entranceciutadella_foreground 01:
        subpixel True
        xanchor 0.0 yanchor 0.0 zoom 1.0
        easein_quad 8.0 xanchor 0.6 yanchor 0.0 zoom 0.5
    with fade

    pt "No será capaz..."

    show bg an04_entranceciutadella_composition 02
    show an04_entranceciutadella_foreground 02
    with Dissolve (2.0)

    n "En pocos segundos ves que tu amigo de la infancia, con cierta destreza,"

    n "salta la valla de seguridad que rodea el parque de {a=https://es.wikipedia.org/wiki/Parque_de_la_Ciudadela}{i}la Ciutadella{/i}{/a}, una de las plazas más grandes de la ciudad,"

    n "pero cerrada completamente por la noche, debido en parte, porque ahí reside el edificio del {a=https://es.wikipedia.org/wiki/Parlamento_de_Cataluña}{i}Parlament de Catalunya{/i}{/a}."

    show bg an04_entranceciutadella_composition 03
    with dissolve

    pt "¡Joder Dídac!"

    pt "¡También podrías haberlo hecho en cualquier otra parte que no fuera la puerta principal!"

    pt "Aunque debo reconocer que tiene su mérito saltar esta valla con semejantes taconazos que llevas..."

    pt "Pese a todo,"

    extend " quizás hubiese sido mejor que te pillaran..."

    pt "Si encuentras a alguien ahí dentro,"

    pt "¡solo serán idiotas haciendo {a=https://es.wikipedia.org/wiki/Botellón}botellón{/a} o yonkis!"

    $ renpy.music.set_volume(0.00, delay=0.0, channel='sfx1')

    window hide dissolve
    pause

    scene black
    with vpunch

    play sound "audio/sfx/hit01.ogg"

    $ saturation_tint_level = "default"

    $ renpy.music.set_volume(0.5, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "Sigues sus pasos saltando el portón, con suma atención,"

    $ renpy.music.set_volume(0.02, delay=30.0, channel='sfx1')


    n "mirando a todos lados para que no te pille ningún agente de seguridad o transeúnte."

    scene bg an04_park_path01_composition 01:
        subpixel True
        xanchor 1.25 yanchor 1.25 zoom 1.5
        easein_quad 10.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    show bg_an04_park_path01_bush a:
        subpixel True
        transform_anchor True
        xalign 0.5 yalign 0.5
        xpos -0.5 ypos -0.5 zoom 1.5
        easein_quad 12.0 xpos 0.5 ypos 0.5 zoom 0.5
    with fade

    show bg_an04_park_path01_bush b
    with Dissolve (5.0)

    n "Una vez dentro, y resguardado por la cierta penumbra que te ofrecen las ramas de los árboles,"

    show bg an04_park_path01_composition 02
    with Dissolve (2.0)

    n "consigues acercarte algo más al inconsciente de tu amigo."

    show bg an04_park_path01_composition 03
    with dissolve

    window hide dissolve
    pause

    scene bg an04_park_fountain:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        ease_quad 12.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    pt "Este lugar de noche y a oscuras, acojona un poco..."

    n "La espectacular y famosa fuente del parque de la {i}Ciutadella{/i}, no te deja indiferente,"

    n "especialmente porque al estar el recinto cerrado,"

    n "nunca antes la habías visto sumida en semejante oscuridad."

    n "A lo lejos, una aguda voz rompe el silencio del lugar."

    if music_play != "lightless_dawn":
        play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "lightless_dawn"

    $ saturation_tint_level = "verydark"

    b02 "¡Ey!"

    b02 "¡Muñeca!"

    extend " ¡¿Te has perdido?!"

#########################################################
    
    if config.version < "00.09.08": # After 2nd date with Neus, Stranger Talking with Didac in a Park.
        
        call endupdatescript
    
#######################################################

    scene black
    with fade

    n "Con tus limitadas habilidades de sigilo, consigues acercarte hacia el origen de ese griterío escondiéndote detrás de un arbusto."

    scene bg an04_park_bank_veryfar_composition 01:
        subpixel True
        xanchor 0.5 yanchor 1.0 zoom 1.0
        ease_quad 20.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    show an04_park_bank_veryfar_plants 01:
        subpixel True
        xanchor 0.5 yanchor 0.65 zoom 1.5
        ease_quad 20.0 xanchor 0.0 yanchor -0.25 zoom 0.5
    with fade

    b01 "Gilipollas,"

    extend " no grites tan alto..."

    show bg an04_park_bank_veryfar_composition 02
    show an04_park_bank_veryfar_plants 02
    with Dissolve (2.0)

    n "Apenas iluminados por la escasa luz amarillenta de las demás farolas que sí funcionan en el resto del parque,"

    n "y por la magnífica luz de la luna llena,"

#########################################################
    
    if config.version < "00.09.09": # Park Scene following Didac, You find them.
        
        call endupdatescript
    
#######################################################

    n "en ese rincón del parque reservado para el aseo de las mascotas llamado {a=https://en.wikipedia.org/wiki/Dog_park}{b}Pipican{/b}{/a},"

    n "consigues vislumbrar a tres individuos, dos de ellos sentados en un banco;"

    n "el otro, medio escondido en la cepa del árbol cercano."

    b02 "Tampoco es para tanto,"

    b02 "solo la estoy saludando,"

    b02 "además..."

    extend " está un rato buena..."

    b01 "No cambiarás nunca {b}Fumetas{/b}..."

    d "Eso que fumáis,"

    extend " es {a=https://es.wikipedia.org/wiki/Cannabis_(género)}{b}maría{/b}{/a} de la buena,"

    d "¿Verdad?"

    scene black
    with fade

    n "Aprovechando que parecen distraídos en la conversación y aparentemente en las curvas de tu compañero/a de piso,"

    n "decides acercarte un poco más."

    scene bg an04_park_bank_far_background_composition 02:
        subpixel True
        xanchor 0.0 yanchor 2.9 zoom 0.5
        ease_quad 15.0 xanchor 0.0 yanchor 0.3 zoom 0.5

    show an04_park_bank_far_bush 01 zorder 99:
        subpixel True
        xanchor 0.0 yanchor 0.59 zoom 0.5
        ease_quad 20.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    b01 "¿Y tú de dónde sales?" #Chulo #chu #Pimp

    n "Con lo que parece una botella oculta en una bolsa de cartón en una mano,"

    n "y con un porro encendido -parecido al que lleva su compañero- en la otra,"

    n "junto con mochilas -visiblemente repletas de más material- en el suelo."

    fum "En realidad es {a=https://es.wikipedia.org/wiki/Hachís}{b}costo{/b}{/a},"

    fum "pero sí..."

    extend " es del bueno..." #Fumeta #fum #CupHead

    b03 "¡Weeeh!"

    scene bg an04_park_bank_far_background_composition 01:
        xanchor 0.0 yanchor 0.3 zoom 0.5

# bank bg
    show an04_park_bank_bg_bank 01:
        xanchor -1.135 yanchor -0.75 zoom 0.4

    show an04_park_bank_bg_bank_cum empty:
        xanchor -1.135 yanchor -0.75 zoom 0.4

# smoke
    show cigarette_smoke_pimp_anim 01: #PIMP
        xanchor -2.0 yanchor -1.4 zoom 0.2 alpha 0.5

    show cigarette_smoke_pot_anim 01: #POTHEAD
        xanchor -2.745 yanchor -1.4 zoom 0.2 alpha 0.5

    show cigarette_smoke_sqt_anim 01: #SQUITTER
        xanchor -3.8 yanchor -1.78 zoom 0.2 alpha 0.5

# pimp

    show an04_park_bank_pimp_01_body:
        xanchor -4.475 yanchor -1.155 zoom 0.4
    show an04_park_bank_pimp_01_arm_L bottle:
        xanchor -4.475 yanchor -1.155 zoom 0.4
    show an04_park_bank_pimp_01_head right:
        xanchor -4.475 yanchor -1.155 zoom 0.4

# pothead

    show an04_park_bank_pothead_01_body:
        xanchor -5.455 yanchor -1.16 zoom 0.4
    show an04_park_bank_pothead_01_head right:
        xanchor -5.455 yanchor -1.16 zoom 0.4

# squitter
    show an04_park_bank_squitter_01_legs_shadow:
        xanchor -3.382 yanchor -1.455 zoom 0.4
    show an04_park_bank_squitter_01_body Drinking:
        xanchor -3.382 yanchor -1.455 zoom 0.4
    show an04_park_bank_squitter_01_legs:
        xanchor -3.382 yanchor -1.455 zoom 0.4


# didac
    show an04_park_bank_didac_01_head right:
        xanchor -1.5085 yanchor -0.76 zoom 0.4
    show an04_park_bank_didac_01_body gabardine:
        xanchor -1.5085 yanchor -0.76 zoom 0.4

    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.0 zoom 0.5
    with Dissolve (2.0)

    n "Un extraño gemido, como de animal moribundo, dirige tu mirada al tercer componente del grupo."

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    b03 "Aunque yo de ti..."

    b03 "no olería el plástico que lo envuelve..."

    extend " Eehh..." #Okupa #oku  Squatter.

    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    b01 "No seas guarro {b}Okupa{/b}..."

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "Huele que alimentaaaahh..."

    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    n "Su tono de voz es inconexo, como si llevase una cuba de mil narices."

    fum "jaja" 

    fum "puto yonki de mierda estás hecho cabrón..."

    show an04_park_bank_pothead_01_head left
    show an04_park_bank_didac_01_head back
    with dissolve

    b01 "¡¿Queréis hacer el puto favor de bajar la voz?!"

    b01 "Joder..."

    b01 "Como venga la pasma,"

    b01 "os voy a meter tal hostia a los dos,"

    b01 "que en lugar de a prisión,"

    extend " os van a llevar a urgencias."

    fum "A prisión, dice..."

    extend " ¡¿Te crees que esto es el {a=https://es.wikipedia.org/wiki/El_Bronx}{i}Bronx{/i}{/a}?!"

    pt "Es evidente que llevan algo más que alcohol en las venas, todos ellos."

    show an04_park_bank_pimp_01_head left
    with dissolve

    d "Os..."

    extend " ¿Os molesta si me siento cerca de vosotros?"

    d "Tengo algo de frío..."

    pt "¿Frío?"

    extend " ¿Tú?"

    extend " ¡¿En verano?!"

    pt "Anda ya..."

    show an04_park_bank_didac_01_head right
    show an04_park_bank_pothead_01_head right
    show an04_park_bank_pimp_01_head right
    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "Puesh..."

    oku "si te pones entre nosotros vas a salir calentita,"

    extend " calentitaaa..."

    oku "Aquí no folla ni el tato tú..."

    show an04_park_bank_squitter_01_body Silent
    with dissolve

    b01 "Eso lo dirás por ti,"

    b01 "que se te apartan hasta las ratas de la peste que haces,"

    extend " cacho guarro."

    show an04_park_bank_pothead_01_head left
    with dissolve

    fum "¡Ey!"

    fum "Que yo follo cada semana,"

    extend " no me jodas."

    show an04_park_bank_pothead_01_head right
    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "Khoñoo..."

    oku "si yo tuviera pashtaah para pagarlas..."

    extend " también lo haría..."

    oku "Anda que nooo..."

    show an04_park_bank_squitter_01_body Silent
    with dissolve

    fum "¿De qué vas Okupa?"

    fum "Joder..."

    extend " ¿encima que te dejo dormir a menudo en mi casa?"

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "Me dejas dormir en el suelo del sótanoo..."

    extend " Soh cabrooong..."

    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    n "La voz de este último muestra indicios de que además de estar ebrio perdido, había algo mucho peor en su sangre."

    fum "Tío..."

    extend " ¿Eres consciente de cuánto hace que no te duchas?"

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "¡Eeey...!"

    oku "Que en la Edad Media o por ahí..."

    oku "tampoco se bañaba ni Diooshh..."

    oku "por lo que he oídooo..."

    oku "solo lo hacían una vez al año o a veces ni esoo..."

    oku "y vivían bien feliceees..."

    show an04_park_bank_squitter_01_body Silent
    with dissolve

    b01 "Sí,"

    extend " y la esperanza de vida no superaba los cuarenta y cinco,"

    b01 "y a causa de ello,"

    extend " la peste mató a un tercio de la población."

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "Joder machooo..."

    extend " qué listo ereees..."

    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    pt "No lo dice con sarcasmo,"

    extend " lo dice en serio..."

    pt "Esta gente está fatal..."

    show an04_park_bank_didac_01_head back
    show an04_park_bank_pothead_01_head left
    show an04_park_bank_pimp_01_head right
    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    fum "¡Siéntate mujer!"

    fum "Al final te vas a volver estatua ahí tan quieta..."

    show an04_park_bank_pimp_01_head right
    with dissolve

    b01 "Oye..."

    extend " ¿y a ti quién te ha dado permiso para elegir por los tres?"

    show an04_park_bank_pothead_01_head right
    with dissolve

    fum "Okupa,"

    extend " ¿A ti te importa que esta macizorra se siente con nosotros?"

    show an04_park_bank_squitter_01_body Talking
    with dissolve

    oku "¿A mí...?"

    oku "mientras compartáish..."

    extend " cuando haya que repartir..."

    show an04_park_bank_pothead_01_head left
    show an04_park_bank_squitter_01_body Drinking
    with dissolve

    fum "¿Lo ves?"

    extend " dos contra uno."

    b01 "Esto no es una democracia."

    fum "Cierto,"

    extend " ni a ti nadie te ha nombrado líder de nadie."

    fum "Solo porque vengas de escuela pija,"

    extend " no significa nada."

    b01 "..."

    show an04_park_bank_didac_01_body gabardine:
        #xanchor -1.5085 yanchor -0.76 zoom 0.4 #Original
        xanchor -4.2 yanchor -0.9 zoom 0.35 #Close to Squitter
    show an04_park_bank_didac_01_head right:
        xanchor -4.2 yanchor -0.9 zoom 0.35 #Close to Squitter
    show an04_park_bank_pothead_01_head right
    with Dissolve (2.0)

    n "Dídac avanza cautelosamente hacia ellos,"

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head
    show an04_park_bank_didac_01_whole stink:
        xanchor -4.2 yanchor -0.9 zoom 0.35 #Close to Squitter
    with dissolve

    n "observas cómo se tapa la nariz y se aleja del tipo al que llaman \"{b}Okupa{/b}\""

    show an04_park_bank_pothead_01_head left
    hide an04_park_bank_didac_01_whole
    show an04_park_bank_didac_01_body gabardine:
        #xanchor -1.5085 yanchor -0.76 zoom 0.4 #Original
        xanchor -4.0 yanchor -0.9 zoom 0.35 xzoom -1.0 #Close to Squitter 
    show an04_park_bank_didac_01_head right:
        xanchor -4.0 yanchor -0.9 zoom 0.35 xzoom -1.0 #Close to Squitter
    with dissolve

    pause


    hide an04_park_bank_didac_01_body 
    hide an04_park_bank_didac_01_head
    show an04_park_bank_bg_bank 02
    #show an04_park_bank_bg_bank_cum empty
    show an04_park_bank_didac_02_arm_L rest:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    show an04_park_bank_didac_02_arm_R rest:
        xanchor -3.098 yanchor -1.82 zoom 0.4

    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -3.098 yanchor -1.82 zoom 0.4

    show an04_park_bank_didac_02_head front:
        xanchor -3.098 yanchor -1.82 zoom 0.4

    show an04_park_bank_didac_02_body clothed:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    with dissolve

    n "y apartando las botellas, decide sentarse en medio de los dos que discuten."

    show an04_park_bank_didac_02_head left
    with dissolve

    d "¿Podría beber algo de lo que estáis tomando?"

    fum "No veo por qué no..."

    show an04_park_bank_didac_02_head right
    with dissolve

    b01 "Claro,"

    extend " como no lo has pagado tú..."

    fum "{b}Chulo{/b},"

    extend " deja que la chica se tome algo..."

    fum "no seas tan \"catalán\"..."

    show an04_park_bank_didac_02_head left

    chu "Grumm..." # Grunt

    hide an04_park_bank_didac_02_arm_L
    hide an04_park_bank_didac_02_arm_R
    hide an04_park_bank_didac_02_body
    hide an04_park_bank_didac_02_head

    show an04_park_bank_pimp_01_arm_L rest

    show an04_park_bank_didac_02_whole drinking:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    with dissolve

    n "Dídac coge la botella que el chico le ofrece y le da un largo trago."

    chu "¡Ey!"

    fum "Tranquila, muñeca,"

    extend " tiene que durarnos toda la noche..."

    hide an04_park_bank_didac_02_whole 
    show an04_park_bank_didac_02_arm_L rest:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    show an04_park_bank_didac_02_arm_R rest:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    show an04_park_bank_didac_02_head front:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    show an04_park_bank_didac_02_body clothed:
        xanchor -3.098 yanchor -1.82 zoom 0.4
    with Dissolve (2.0)

    d "Ahhh..." #*Sigh* 

    show an04_park_bank_didac_02_head right02
    with dissolve

    d "No me llames muñeca."

    n "Una mirada de odio contenido se dibuja en su rostro."

    pt "Parece que aún hay algo de mi compañero de piso en su mente..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005

    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_01_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_head right:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_arm_L rest:
        xanchor -1.25 yanchor -0.168
#
## pothead
    show an04_park_bank_pothead_01_body:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_01_head left:
        xanchor -2.23 yanchor -0.168

#
## didac_sit
    show an04_park_bank_didac_02_arm_R rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_arm_L rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -0.99 yanchor -0.52 
    show an04_park_bank_didac_02_head right02:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body clothed:
        xanchor -0.99 yanchor -0.52 
#
## Smoke

    show cigarette_smoke_pimp_anim 01: #PIMP
        xanchor -0.57 yanchor -0.2 zoom 0.5 alpha 0.5

    show cigarette_smoke_pot_anim 01: #POTHEAD
        xanchor -1.28 yanchor -0.2 zoom 0.5 alpha 0.5
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0

    with Dissolve (1.0)

    n "Tu visión se iba acostumbrando cada vez más a la casi absoluta oscuridad del lugar"

    n "y te permite observar mejor los detalles, incluso en la lejanía."

    show an04_park_bank_didac_02_head right
    with dissolve

    oku "No jodas machooo..."

    oku "¿La tía se ha meadoo...?"

    show an04_park_bank_didac_02_head left
    with dissolve

    chu "¡¿Qué?!"

    show an04_park_bank_didac_02_head front
    with dissolve

    fum "Hostias..."

    extend " sí que está mojada de la entrepierna..."

    show an04_park_bank_didac_02_head right02
    with dissolve

    fum "¿Te pasa algo muñeca?"

    hide an04_park_bank_didac_02_arm_R
    hide an04_park_bank_didac_02_arm_L
    hide an04_park_bank_didac_02_body_clothed_back
    hide an04_park_bank_didac_02_head
    hide an04_park_bank_didac_02_body

    show an04_park_bank_didac_03_arm_L onleg:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back empty:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_03_head right:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_03_body clothed:
        xanchor -0.99 yanchor -0.52


    with dissolve

    n "Didac se desplaza sugerentemente a su izquierda y posa su mano sobre la pierna del que llaman {b}Fumeta{/b}"

    show an04_park_bank_pothead_01_head left02
    with dissolve

    n "y acercando su rostro a escasos centímetros del suyo..."

    d "Esto no es meado..."

    extend " es otra cosa,"

    d "y te he dicho que no me llames muñeca."

    show an04_park_bank_pothead_01_body erection
    with Dissolve (1.0)

    fum "..."

    n "Un silencio incómodo inunda la situación varios segundos,"

    n "mientras el llamado {b}Okupa{/b} sigue fumando y bebiendo de la botella al mismo tiempo."

    p "..."

    pt "La madre que te parió Dídac..."

    pt "¿Estás haciendo esto porque me has visto y te estás tirando un farol?"

    pt "¿O realmente lo vas a hacer...?"

    n "La mirada de Dídac sigue firme y sin pestañear directa a los ojos del que llaman \"Fumeta\"."

    fum "Eh..."

    extend " Vaya..."

    fum "Una chica directa..."

    extend " Me gust..."

    play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 0.5 fadeout 0.5

    show an04_park_bank_didac_03_arm_L ondick
    with dissolve

    n "Consigues ver en la penumbra del lugar como Dídac le agarra fuertemente la polla que empieza a emerger de sus pantalones anchos."

    fum "¡Coño...!"

    d "¿Lo ves?"

    d "Tú también empiezas a mojarte,"

    d "solo que en lugar de empapar tus sucios bóxeres,"

    show an04_park_bank_didac_03_arm_L mast_a
    with dissolve

    n "Con suma rapidez y osadía, logra bajar su bragueta, sacar su miembro, y agarrarlo con fuerza."

    d "estás rellenando este globo de sangre..."

    fum "..."

    show an04_park_bank_didac_03_arm_L empty
    hide an04_park_bank_didac_03_head
    hide an04_park_bank_didac_03_body

    show an04_park_bank_didac_03_arm_L_mast_a:
        xanchor -0.99 yanchor -0.52
        alpha 1.1
        block:
            linear 0.5 alpha 0.0
            pause 0.5
            linear 0.5 alpha 0.0
            pause 0.5
            linear 0.5 alpha 1.1
            pause 0.5
            repeat

    show an04_park_bank_didac_03_arm_L_mast_b:
        xanchor -0.99 yanchor -0.52
        alpha 0.0
        block:
            linear 0.5 alpha 1.1
            pause 0.5
            linear 0.5 alpha 0.0
            pause 0.5
            linear 0.5alpha 0.0
            pause 0.5
            repeat

    show an04_park_bank_didac_03_arm_L_mast_c:
        xanchor -0.99 yanchor -0.52
        alpha 0.0
        block:
            linear 0.5 alpha 0.0
            pause 0.5
            linear 0.5 alpha 1.1
            pause 0.5
            linear 0.5 alpha 0.0
            pause 0.5
            repeat

    show an04_park_bank_didac_03_head right:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_03_body clothed:
        xanchor -0.99 yanchor -0.52 

    with dissolve

    n "Su mano empieza a moverse masturbando el erecto pene del chico,"

    n "que por momentos olvida que sigue teniendo un cigarro en la mano,"

    n "mientras queda atónito y sin saber cómo reaccionar ante la acción de esa musculosa chica desconocida."

    show an04_park_bank_didac_03_arm_L_mast_a:
        subpixel True
        alpha 2.0
        block:
            ease 0.3 alpha 0.0
            ease 0.3 alpha 0.0
            ease 0.3 alpha 1.5
            repeat

    show an04_park_bank_didac_03_arm_L_mast_b:
        subpixel True
        alpha 0.0
        block:
            ease 0.3 alpha 1.5
            ease 0.3 alpha 0.0
            ease 0.3 alpha 0.0
            repeat

    show an04_park_bank_didac_03_arm_L_mast_c:
        subpixel True
        alpha 0.0
        block:
            ease 0.3 alpha 0.0
            ease 0.3 alpha 1.5
            ease 0.3 alpha 0.0
            repeat

    with dissolve


    n "Dídac agarra cada vez con más fuerza la polla del desconocido,"

    n "sin quitarle ojo de encima y mordiéndose el labio inferior,"

    show an04_park_bank_didac_03_arm_L_mast_a:
        subpixel True
        alpha 2.0
        block:
            ease 0.15 alpha 0.0
            ease 0.15 alpha 0.0
            ease 0.15 alpha 1.5
            repeat

    show an04_park_bank_didac_03_arm_L_mast_b:
        subpixel True
        alpha 0.0
        block:
            ease 0.15 alpha 1.5
            ease 0.15 alpha 0.0
            ease 0.15 alpha 0.0
            repeat

    show an04_park_bank_didac_03_arm_L_mast_c:
        subpixel True
        alpha 0.0
        block:
            ease 0.15 alpha 0.0
            ease 0.15 alpha 1.5
            ease 0.15 alpha 0.0
            repeat

    with dissolve

    n "mientras la mueve a un ritmo mayor a medida que pasan los segundos."

    show an04_park_bank_didac_03_arm_L_mast_a:
        alpha 1.0
    show an04_park_bank_didac_03_arm_L_mast_b:
        alpha 0.0
    show an04_park_bank_didac_03_arm_L_mast_c:
        alpha 0.0
    show an04_park_bank_pothead_01_head left03
    with Dissolve (1.0)

    pause

## didac_sit
    hide an04_park_bank_didac_03_arm_L_mast_a
    hide an04_park_bank_didac_03_arm_L_mast_b
    hide an04_park_bank_didac_03_arm_R
    hide an04_park_bank_didac_03_arm_L
    hide an04_park_bank_didac_03_body
    hide an04_park_bank_didac_03_head
#
    show an04_park_bank_didac_03_whole handface:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_pothead_01_head left02
    show an04_park_bank_pothead_01_body dickout
    with hpunch

    d "¡¿Qué coño haces?!"

    fum "¡¿Qué?!"

    fum "¿Qué pasa?"

    d "¡¿Por qué coño me besas imbécil?!"

    fum "Joder..."

    extend " Eres tú la que te me has acercado y te me has puesto a gemir en mi puta cara,"

    fum "Además,"

    extend " me estás masturbando la polla,"

    fum "¿qué querías que hiciera?"

    d "Tú lo has dicho,"

    d "te estoy masturbando la polla,"

    extend " lo que hay aquí no es meado,"

    d "voy jodidamente cachonda."

    d "Quiero tu polla,"

    extend " no que hagamos mariconadas."
    
    chu "Joder..."

    extend " la tía no va con sutilezas..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_01_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_head right:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_arm_L rest:
        xanchor -1.25 yanchor -0.168
#
## pothead
    show an04_park_bank_pothead_01_body dickout:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_01_head left:
        xanchor -2.23 yanchor -0.168

#
## didac_sit
    show an04_park_bank_didac_02_arm_R rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_arm_L rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -0.99 yanchor -0.52 
    show an04_park_bank_didac_02_head left:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body clothed:
        xanchor -0.99 yanchor -0.52        

#
## Smoke

    show cigarette_smoke_pimp_anim 01: #PIMP
        xanchor -0.57 yanchor -0.2 zoom 0.5 alpha 0.5

    show cigarette_smoke_pot_anim 01: #POTHEAD
        xanchor -1.28 yanchor -0.2 zoom 0.5 alpha 0.5
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0

    with Dissolve (1.0)

    d "¿Es que acaso tienes celos?"

#########################################################
    
    if config.version < "00.10.00": # Park Scene following Didac, Didac doing naughty things with the Pothead guy.
        
        call endupdatescript
    
#######################################################

    chu "No negaré que algo de envidia tengo..."

    d "Si no te acercas es porque no quieres..."

    show an04_park_bank_didac_02_head right02
    show an04_park_bank_pothead_01_head right
    with hpunch

    ono "THUMP"

    d "¿Qué ha sido este golpe?"

    fum "Euh..."

    fum "Eso ha sido el Okupa cayéndose redondo al suelo de lo fumado que está..."

    fum "a saber qué se habrá tomado esta noche..."

    show an04_park_bank_didac_02_head right
    show an04_park_bank_pothead_01_head left
    with dissolve
    
    fum "Aunque, teniéndote aquí tan cerca,"

    extend " y haciéndome lo que me haces,"

    fum "me pregunto cuánto de drogado estoy yo..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs semiclosed_cloth:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head right:
        xanchor -1.25 yanchor -0.168
    #show an04_park_bank_pimp_arm_L 02_rest:
        #xanchor -1.25 yanchor -0.168
#
## pothead
    show an04_park_bank_pothead_01_body dickout:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_01_head left:
        xanchor -2.23 yanchor -0.168

#
## didac_sit
    show an04_park_bank_didac_02_arm_R rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_arm_L rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -0.99 yanchor -0.52 
    show an04_park_bank_didac_02_head left:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body clothed:
        xanchor -0.99 yanchor -0.52        

#
## Smoke

    #show cigarette_smoke_pimp_anim 01: #PIMP
        #xanchor -0.57 yanchor -0.2 zoom 0.5 alpha 0.5

    show cigarette_smoke_pot_anim 01: #POTHEAD
        xanchor -1.28 yanchor -0.2 zoom 0.5 alpha 0.5
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0

    with Dissolve (1.0)

    n "Al que llaman \"Chulo\" se acerca a Dídac acariciando la rodilla con la suya..."

    d "Veamos cuál de las dos es más grandota..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head right:
        xanchor -1.25 yanchor -0.168
    #show an04_park_bank_pimp_arm_L 02_rest:
        #xanchor -1.25 yanchor -0.168
#
## pothead
    show an04_park_bank_pothead_01_body dickout:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_01_head left:
        xanchor -2.23 yanchor -0.168

#
## didac_sit
    show an04_park_bank_didac_02_arm_R empty:
        xanchor -0.99 yanchor -0.52

    show an04_park_bank_didac_sit_arm_R_02_mast_action 01:

        contains:
            "an04_park_bank_didac_02_arm_R_mast_a"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 1.0

            block:

                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_R_mast_b"
            subpixel True
            xanchor -0.99 yanchor -0.52  alpha 0.0

            block:

                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_R_mast_c"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 0.0

            block:

                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                repeat

    show an04_park_bank_didac_02_arm_L rest:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -0.99 yanchor -0.52 
    show an04_park_bank_didac_02_head left:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body clothed:
        xanchor -0.99 yanchor -0.52        

#
## Smoke

    #show cigarette_smoke_pimp_anim 01: #PIMP
        #xanchor -0.57 yanchor -0.2 zoom 0.5 alpha 0.5

    show cigarette_smoke_pot_anim 01: #POTHEAD
        xanchor -1.28 yanchor -0.2 zoom 0.5 alpha 0.5
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0


    with dissolve

    n "Sin ningún pudor,"

    n "Dídac pone la mano dentro de sus pantalones y agarra su polla,"

    n "la cual ya empezaba a dar muestras de erección con fuerza."

    chu "Directa al grano,"

    extend " así me gusta..."

    # Chulo mete mano bajo falda de Dídac # NOT FINISHED

    show an04_park_bank_didac_02_bodyover pimppussy:
        xanchor -0.99 yanchor -0.52   

    n "Con menos vergüenza aún, este último hace lo mismo y pone su mano dentro de la gabardina de Dídac."

    chu "Caray..."

    chu "sí que estás bien mojada,"

    extend " sí..."

    fum "Oye..."

    extend " estaba yo primero aquí..."

    chu "Sí,"

    extend " pero yo he sido el que ha dado el primer paso."

    show an04_park_bank_didac_02_head right
    show an04_park_bank_pothead_01_head left02
    with dissolve

    d "Tranquilos, fieras,"

    extend " hay para ambos..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head right:
        xanchor -1.25 yanchor -0.168
    #show an04_park_bank_pimp_arm_L 02_rest:
        #xanchor -1.25 yanchor -0.168
#
## pothead

    show an04_park_bank_pothead_02_shoes semiclosed:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_armR rest:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_body cloth:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_legs semiclosed_naked:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_head left:
        xanchor -2.23 yanchor -0.168

#
## didac_sit
    show an04_park_bank_didac_02_arm_R empty:
        xanchor -0.99 yanchor -0.52

    show an04_park_bank_didac_sit_arm_R_02_mast_action 01:

        contains:
            "an04_park_bank_didac_02_arm_R_mast_a"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 1.0

            block:

                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_R_mast_b"
            subpixel True
            xanchor -0.99 yanchor -0.52  alpha 0.0

            block:

                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_R_mast_c"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 0.0

            block:

                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                repeat

###
    show an04_park_bank_didac_sit_arm_L_02_mast_action 01:

        contains:
            "an04_park_bank_didac_02_arm_L_mast_a"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 1.0

            block:

                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_L_mast_b"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 0.0

            block:

                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                easeout_quad 0.5 alpha 0.0
                pause 0.5
                repeat

        contains:

            "an04_park_bank_didac_02_arm_L_mast_c"
            subpixel True
            xanchor -0.99 yanchor -0.52 alpha 0.0

            block:

                easeout_quad 0.5 alpha 0.0
                pause 0.5
                pause 0.5
                pause 0.5
                easein_quad 0.5 alpha 1.0
                pause 0.5
                repeat

    show an04_park_bank_didac_02_arm_L empty:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body_clothed_back:
        xanchor -0.99 yanchor -0.52 
    show an04_park_bank_didac_02_head right:
        xanchor -0.99 yanchor -0.52
    show an04_park_bank_didac_02_body clothed:
        xanchor -0.99 yanchor -0.52        

#
## Smoke

    #show cigarette_smoke_pimp_anim 01: #PIMP
        #xanchor -0.57 yanchor -0.2 zoom 0.5 alpha 0.5

    #show cigarette_smoke_pot_anim 01: #POTHEAD
        #xanchor -1.28 yanchor -0.2 zoom 0.5 alpha 0.5
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0
    with dissolve

    n "Finalmente mete la mano dentro del pantalón de ambos agarrando sus pollas y moviéndolas a cierto ritmo."

    chu "¿Vas a limitarte a solo masturbarnos?"

    chu "¿o vas a hacer algo más?"

    d "Impaciente el chico..."

    show an04_park_bank_didac_02_arm_L empty
    hide an04_park_bank_didac_sit_arm_L_02_mast_action
    show an04_park_bank_pothead_02_dick erect_naked:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_didac_02_arm_L_handbra:
        xanchor -0.99 yanchor -0.52
    with dissolve

    n "Aparta la mano de este para meterla dentro de la camisa entre sus pechos,"

    hide an04_park_bank_didac_02_arm_L_handbra
    show an04_park_bank_didac_02_arm_L condoms
    with dissolve

    n "de donde saca los mismos tres condones XXL que te había enseñado en el piso."

    d "Fumetas, te llaman,"

    extend " ¿verdad?"

    fum "Euh..."

    fum "sí..."

    d "Ponte esto."

    pt "Joder..."

    extend " joder..."

    pt "Dídac..."

    extend " ¡¿Qué coño haces?!"

    menu afternight04_Park_DidactobeFucked_question:
        
        pt "¡Son dos putos desconocidos!"
        
        "<Detener esta locura>":
            
            call p_Help

            jump afternight04_Park_DidactobeFucked_No

        "<No hacer nada>":

            call p_Help

            jump afternight04_Park_DidactobeFucked_Yes

label afternight04_Park_DidactobeFucked_Yes:


#########################################################
    
    if config.version < "00.10.01": # You decide to watch how they fuck her with condom.
        
        call endupdatescript
    
#######################################################

    show an04_park_bank_didac_02_arm_L rest
    with dissolve

    n "Separa un condón del resto y se lo da al {b}Fumetas{/b}"

    pt "No parece tenerla enorme al menos..."

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005
#
## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head right:
        xanchor -1.25 yanchor -0.168
    #show an04_park_bank_pimp_arm_L 02_rest:
        #xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_dick erect_naked:
        xanchor -1.25 yanchor -0.168
#
## pothead

    show an04_park_bank_pothead_02_shoes semiclosed:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_armR rest:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_body cloth:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_legs semiclosed_naked:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_head left:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_dick erect_naked:
        xanchor -2.23 yanchor -0.168
#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0
    
    show an04_park_bank_didac_01_head back:
        zoom 0.85 xanchor -1.05 yanchor -0.04
    show an04_park_bank_didac_01_body gabardine:
        zoom 0.85 xanchor -1.05 yanchor -0.04

    with dissolve

    d "Humm..."

    d "Bueno,"

    extend " es mejor que nada supongo."

    fum "¿Qué?"

    n "Al mismo tiempo, Dídac se quita la gabardina,"

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head

    show an04_park_bank_bg_bank 03
    #show an04_park_bank_bg_bank_cum empty


    show an04_park_bank_didac_01_body lingerie:
        zoom 0.85 xanchor -1.05 yanchor -0.04
    show an04_park_bank_didac_01_head back:
        zoom 0.85 xanchor -1.05 yanchor -0.04
    with dissolve

    # Fondo Con Gabardina NOT FINISHED

    n "mostrando un conjunto de lencería semitransparente de color rojo con un bustier de encaje"

    n "que apenas oculta sus voluptuosos pechos,"

    n "faldita con ligueros, braguitas de vinilo abiertas con volante y lacito,"

    n "con pequeños -y espesos- fluidos procedentes de su entrepierna, recorriendo ambas extremidades."

    pt "La madre que la parió..."

    show an04_park_bank_pothead_02_armR condom
    show an04_park_bank_pothead_02_head left02
    with dissolve

    fum "Hostias..."

    chu "Madre mía..."

    extend " sí que estás en forma,"

    chu "y un rato buena también..."

    show an04_park_bank_pothead_02_head left
    with dissolve

    d "Venga, póntelo."

    show an04_park_bank_pothead_02_head left02
    with dissolve

    fum "¡Coño!"

    fum "¡Si este condón es de tamaño {b}XXL{/b}..!"

    d "¿Algún problema?"

    fum "Euh..."

    show an04_park_bank_pothead_02_head left
    with dissolve

    fum "Yo no tengo la polla tan grande..."

    d "Es mejor eso que nada..."

    d "¿O prefieres que se lo pida a tu amigo?"

    show an04_park_bank_pothead_02_head left02
    with dissolve

    fum "No..."

    extend " no es eso..."

    show an04_park_bank_pothead_02_head left
    with dissolve

    d "¿Entonces a qué esperas?"

    n "Con su lencería rojo pasión, sus ligueros, su cuerpo voluptuoso,"

    n "Dídac muestra un aspecto realmente imponente y difícil de rechazar."

    fum "Cla-"

    extend "claro..."

    show an04_park_bank_pothead_02_armR rest
    show an04_park_bank_pothead_02_legs open_naked
    show an04_park_bank_pothead_02_shoes open
    show an04_park_bank_pothead_02_dick erect_condom_a
    with dissolve

    n "Apenas le ha dado tiempo al chico de ponerse el condón, que obviamente le va un poco grande, demasiado,"

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head
    show an04_park_bank_pothead_02_head frontup
    show an04_park_bank_didac_fuckriding_legs:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_didac_fuckriding_thighs a:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_didac_fuckriding_head back:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_didac_fuckriding_body:
        xanchor -2.23 yanchor -0.168
    with dissolve

    n "y Dídac se sienta sobre él, metiéndose toda su polla dentro."

    show an04_park_bank_didac_fuckriding_head back:
        yanchor -0.25
    show an04_park_bank_didac_fuckriding_body:
        yanchor -0.22
    show an04_park_bank_didac_fuckriding_thighs d
    with dissolve

    fum "Oye..."

    extend " ¿No deberías quitarte antes las bragas o algo?"

    d "Es lencería abierta,"

    extend " no hace falta."

    hide an04_park_bank_didac_fuckriding_head
    hide an04_park_bank_didac_fuckriding_body
    hide an04_park_bank_didac_fuckriding_thighs
    hide an04_park_bank_didac_fuckriding_legs

    show an04_park_bank_didac_fuckriding 01
    with dissolve

    chu "Desde luego,"

    extend " no se está para hostias esta chica..."

    fum "Jo..."

    extend " Joder..."

    fum "ha entrado de golpe..."

    d "Aahhhh..." # *moan*

    chu "Tampoco es de extrañar,"

    chu "con lo mojada que está,"

    extend " le cabría hasta una botella entera..."

    pt "Y tampoco es que tenga una polla como la mía..."

    d "Mmm-Ahhh" #*moans*

    extend " Aaahh..." #*moan*

    fum "Ufff..."

    extend " Joder..."

    fum "Cómo me está poniendo la pava esta..."

    fum "Así no voy a durar mucho..."

    chu "Mierda de resistencia que tienes macho..."

    fum "Gilipollas,"

    extend " se nota que no es tu polla la que está aquí dentro,"

    fum "no veas cómo lo tiene de estrecho,"

    extend " jugoso,"

    extend " y caliente,"

    fum "la muy zorra..."

    n "Dídac agarra por la barbilla al chico que se está follando y cuando tiene su rostro en frente;"

    show an04_park_bank_didac_fuckriding 00 
    with hpunch

    play sound "audio/sfx/sput03.ogg"
    ono "SPUT"

    fum "¡Ey!"

    show an04_park_bank_didac_fuckriding 01
    with dissolve

    fum "¿Por qué cojones me escupes en la cara?"

    d "Por llamarme zorra,"

    extend " imbécil."

    show an04_park_bank_didac_fuckriding 02
    with dissolve

    n "Cogiéndose de sus hombros, empieza a acelerar el ritmo de sus caderas,"

    n "oyéndose el ruido de sus nalgas chocando contra su entrepierna."

    d "Aaah-Ahhh..." #*moan*

    fum "Jodeeer..."

    fum "Como sigas así..."

    chu "Esta escena me está poniendo muy,"

    extend " pero que muy cachondo,"

    extend " cabrones..."

    pt "Mi polla no piensa lo contrario..."

    fum "Aaaahh-"

    extend "aaahh" #*moans*

    fum "Joder..."

    fum "en serio..."

    extend " me voy a..."

    n "las caderas de Dídac siguen moviéndose a un ritmo frenético aplastando la entrepierna del \"Fumetas\" en cada embestida."

    d "Aaaahh-MMmm-Aahh..." #*moans*

    fum "{size=50}¡ME CORROOO!{/size}"

    chu "¡Gilipollas!"

    chu "¡No grites tan alto joder!"

    fum "AAAAaaaahhh..." #*moan*

    n "El cuerpo rendido del chico da muestras de haber tenido un orgasmo realmente placentero,"

    n "sin embargo, Dídac sigue moviendo sus caderas sin la más mínima intención de detenerse,"

    n "sobre el cuerpo casi inerte de su amante,"

    show an04_park_bank_pothead_02_dick aftercum
    show an04_park_bank_pothead_condom_ground:
        xanchor -2.23 yanchor -0.168
    with dissolve

    n "hasta que la polla del chico sale resbalando en una de las embestidas,"

    n "cayendo el condón junto con todo el esperma sobre sus piernas."

    show an04_park_bank_didac_fuckriding 00
    with dissolve

    n "Al sentir esa humedad, Dídac detiene su movimiento y sale de su \"trance\","

    n "observando a su aparentemente dormido \"amante\"."

    d "Ahhhrgh..." #*Suspiro longevo con cierta rabia contenida*

    n "Vuelve a poner su mano en el sujetador, del que saca los dos condones restantes,"

    n "arranca uno y se lo lanza al {b}Chulo{/b}."

    hide an04_park_bank_didac_fuckriding

    show an04_park_bank_pothead_02_head left

    show an04_park_bank_didac_01_body lingerie:
        zoom 0.85 xanchor -1.2 yanchor -0.04 xzoom -1.0
    show an04_park_bank_didac_01_head back:
        zoom 0.85 xanchor -1.2 yanchor -0.04 xzoom -1.0
    with dissolve

    d "A ver si tú aguantas un poco más que tu amigo."

    chu "Estoy seguro que sí..."

    pt "Su actitud no me sorprendería tanto, si él fuera el tío que recuerdo..."

    pt "pero siendo ahora una chica,"

    pt "lo que está ocurriendo no tiene nada que ver con el Dídac que yo conozco..."

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head

    show an04_park_bank_pimp_02_head frontup

    show an04_park_bank_didac_fuckriding 00:
        xanchor 0.178
    with dissolve

    chu "¡Ey!"

    chu "Para,"

    extend " para..."

    chu "¡Que aún no me lo he puesto mujer...!"

    d "He visto tortugas más rápidas..."

    d "¡Date prisa hostias!"

    chu "Joder con la ninfómana..."

    d "No me llames así capullo..."

    show an04_park_bank_didac_fuckriding 01
    show an04_park_bank_pimp_02_dick erect_condom
    with dissolve

    n "Justo cuando consigue ponérselo, Dídac se acomoda y se mete su polla de golpe."

    d "Mmm..."

    extend " No es que hayamos mejorado mucho,"

    d "pero algo es algo..."

    chu "¿De qué coño hablas?"

    d "Nada, déjalo..."

    n "Hace presión con su polla para intentar profundizar más en su interior y sentirla toda dentro de ella."

    d "Mhmm..." #*moan*

    chu "Tienes un coño realmente estrecho, muñeca..."

    d "Pesadito con lo de muñeca..."

    chu "¿Y cómo coño quieres que te llame entonces?"

    d "..."

    d "Llámame {a=https://es.wikipedia.org/wiki/Dafne}Dafne{/a}."

    chu "¿En serio?"

    chu "Un nombre de origen griego que significa Laurel."

    chu "Nombre de una ninfa protagonista de una desgraciada historia de amor con Apolo..."

    d "¿Me vas a contar un puto rollo que no me interesa?"

    d "¿o me vas a follar?"

    d "Porque si no, despierto al yonki ese que se ha metido una leche,"

    d "quizás tendrá más ganas..."

    n "Sus manos agarran con fuerza las nalgas de Dídac,"

    n "haciendo presión para poder sentir bien profunda su polla."

    chu "Como quieras, {b}Dafne{/b}."

    n "Este le da un empujón para sacársela de encima,"

    hide an04_park_bank_didac_fuckriding

    hide an04_park_bank_pimp_02_head
    hide an04_park_bank_pimp_02_body
    hide an04_park_bank_pimp_02_legs
    hide an04_park_bank_pimp_02_dick

    show an04_park_bank_didac_fucklegsup_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_didac_fucklegsup_head front:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_didac_fucklegsup_legs:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_didac_fucklegsup_shoes:
        xanchor -1.25 yanchor -0.168

    show an04_park_bank_pimp_fuckstand_head back:
        xanchor -1.12 yanchor -0.175
    show an04_park_bank_pimp_fuckstand_body a:
        xanchor -1.25 yanchor -0.168
    with dissolve

    n "y una vez de pie, con la misma acción hace que se siente en el banco de forma brusca."

    d "¡¿Qué coño haces?!"

    chu "Follarte,"

    extend " como me has pedido."

    show an04_park_bank_pimp_fuckstand_head back:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_fuckstand_body d:
        xanchor -1.25 yanchor -0.168
    with dissolve

    n "Separa sus piernas con la misma delicadeza y se la mete de golpe de nuevo hasta el fondo."

    n "Posando sus piernas abiertas encima de sus hombros y agarrándola por la cadera,"

    hide an04_park_bank_pimp_fuckstand_head
    hide an04_park_bank_pimp_fuckstand_body

    show an04_park_bank_pimp_fuckstand 02
    with dissolve

    n "empieza a embestirla duramente contra el banco con una posición, francamente, algo incómoda."

    show an04_park_bank_didac_fucklegsup_head up

    d "Mff-mmm-aaahh..." #*moans*

    chu "¡¿Es así..."

    extend " como te gusta...?!"

    d "Mmm-AAhh-Mff..." #*moans*

    chu "Y luego dices que no eres una zorra..."

    n "Sigue dándole duro mientras la agarra con fuerza y penetrándola tan al fondo como le es posible."

    chu "Jodeer..."

    extend " si al final resulta que el puto \"Fumetas\" tenía razón..."

    fum "Jeje..." #*risilla maquiavelica*

    show an04_park_bank_pimp_fuckstand 01
    with dissolve

    fum "Te lo dije..."

    chu "..."

    show an04_park_bank_didac_fucklegsup_head front

    d "¡No te distraigas imbécil!"

    chu "Lo que diga la señorita {b}Dafne{/b}..."

    show an04_park_bank_pimp_fuckstand 02
    with dissolve

    n "Vuelve a retomar el ritmo, mientras Dídac se agarra en el banco tan bien como le es posible,"

    show an04_park_bank_didac_fucklegsup_head up
    show an04_park_bank_pothead_02_dick erect_naked
    with dissolve

    n "mientras el otro los sigue observando a medida que se le va recuperando la polla"

    n "y al que llaman \"Okupa\" sigue ahí, en el suelo."

    d "Mmm-AAhh-Mff..." #*moans*

    fum "Venga,"

    extend " date prisa..."

    fum "Tengo ganas de repetir con la guarra esta."

    chu "Siento decepcionarte macho,"

    chu "pero tengo para rato..."

    chu "Sé muy bien cómo controlarme para no correrme antes de tiempo,"

    chu "por muy estrecho que esta tenga el {b}chumino{/b}."

    fum "¡No me jodas!"

    fum "¿Me vas a hacer esperar mientras veo cómo te la follas?"

    chu "Jajaja" #*Risa maquiavelica*

    chu "Es tu culpa si te corriste tan temprano,"

    extend " idiota."

    fum "Y un cuerno..."

    fum "Si hace falta probaré a metérsela por el otro agujero."

    chu "No sé yo si esta chica te va a dejar,"

    chu "tiene bastante mala leche..."

    d "Mmm-AAhh-Aahh..." #*moans*

    fum "Creo que no me dirá nada,"

    fum "cuando va así de cachonda,"

    extend " parece que esté bien drogada..."

    chu "Haz lo que quieras,"

    chu "pero ni se te ocurra tocarme con tu polla."

    chu "¿Queda claro?"

    fum "¡Ni ganas!"

    fum "Pero,"

    extend " ¿podrías volver a la postura de antes?"

    fum "Me sería mucho más fácil..."

    chu "Lo que uno tiene que hacer..."

    show an04_park_bank_pimp_fuckstand 00
    with dissolve

    n "Saca su polla de su chorreante coño y por lo visto también del condón,"

    n "que se queda pegado en los labios de Dídac al ser este mucho más ancho que su polla."

    n "Dídac parece volver en sí poco a poco."

    d "Ey..."

    d "Pero..."

    d "¡¿Por qué coño me la sacas?!"

    chu "No te pongas nerviosa fiera..."

    hide an04_park_bank_didac_fucklegsup_body
    hide an04_park_bank_didac_fucklegsup_head
    hide an04_park_bank_didac_fucklegsup_legs
    hide an04_park_bank_didac_fucklegsup_shoes
    hide an04_park_bank_pimp_fuckstand

    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head left:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_dick erect_condom:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_didac_01_body lingerie:
        zoom 0.85 xanchor -0.5 yanchor -0.04
    show an04_park_bank_didac_01_head back:
        zoom 0.85 xanchor -0.5 yanchor -0.04
    with dissolve

    n "El chico recoge el condón y se lo vuelve a poner de la mejor manera que puede y se sienta al lado de ella."

    chu "Siéntate otra vez con Papi,"

    extend " nena."

    n "Dídac obedece y vuelve a la misma postura en la que había estado antes,"

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head

    show an04_park_bank_didac_fuckriding 00:
        xanchor 0.178
    with dissolve

    n "poniéndose encima del chico metiéndose su polla entera."

    d "No os cansáis de llamarme de cualquier manera,"

    extend " ¿verdad?"

    chu "Me gustan las zorras rebeldes,"

    chu "culpable de los cargos señoría..."

    show an04_park_bank_didac_fuckriding 00b
    with dissolve

    d "Gilipollas."

    show an04_park_bank_didac_fuckriding 02
    with dissolve

    n "Sin más dilación, Dídac vuelve a cabalgar al chico con cierta celeridad."

    d "Mhmn-Sí..." #*moans*

    chu "Dios,"

    extend " qué coño más estrecho tienes jodía..."

    hide an04_park_bank_pothead_02_shoes
    hide an04_park_bank_pothead_02_armR
    hide an04_park_bank_pothead_02_body
    hide an04_park_bank_pothead_02_head
    hide an04_park_bank_pothead_02_legs
    hide an04_park_bank_pothead_02_dick

    show an04_park_bank_pothead_condom_ground 02
    show an04_park_bank_pothead_groundcondom_body:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_pothead_groundcondom_head down:
        xanchor -0.176 yanchor 0.005
    with dissolve

    fum "Mierda,"

    extend " está hecho una mierda."

    n "El llamado \"Fumetas\", una vez levantado del banco, se ha puesto de cuclillas,"

    n "para recoger el condón que hacía poco había usado,"

    n "empapado en su esperma, jugos vaginales de Dídac, y suciedad del suelo."

    chu "Ahh-mmm..." #*moans*

    show an04_park_bank_pothead_groundcondom_head left
    with dissolve

    chu "No seas guarro,"

    extend " macho..."

    chu "Mhmmm..." #*moan*

    chu "Ponte uno nuevo..."

    fum "¿Dónde coño está el condón que falta?"

    chu "¡Y yo qué sé!"

    chu "Busca en su sujetador,"

    extend " o algo..."

    chu "de ahí los ha sacado antes."

    hide an04_park_bank_pothead_groundcondom_body
    hide an04_park_bank_pothead_groundcondom_head
    show an04_park_bank_pothead_condom_ground

    show an04_park_bank_pothead_lookingcondom_hand:
        subpixel True
        xanchor 0.0 yanchor -0.02
        easein_quad 20.0 xanchor 0.06
    show an04_park_bank_pothead_lookingcondom_body:
        xanchor 0.05 yanchor -0.02
    with dissolve

    n "El chico titubeante se acerca a Dídac, que sigue cabalgando sin descanso encima de su compañero,"

    n "y alarga su brazo para palparle sus pechos al descubierto por ese extraño y revelador sujetador."

    play sound "audio/sfx/punch01.ogg"

    hide an04_park_bank_pothead_lookingcondom_hand
    hide an04_park_bank_pothead_lookingcondom_body
    hide an04_park_bank_didac_fuckriding
    #show an04_park_bank_didac_fuckriding 00:
        #xanchor 0.178 alpha 0.5
    show an04_park_bank_didac_fuckriding_legs:
        xanchor -1.45 yanchor -0.168
    show an04_park_bank_didac_fuckriding_thighs b:
        xanchor -1.45 yanchor -0.168
    show an04_park_bank_didac_fuckriding_elbowing:
        xanchor -1.45 yanchor -0.168
    show an04_park_bank_pothead_body_receivingelbow:
        subpixel True
        xanchor 0.15 yanchor 0.0
        easein_quad 0.5 xanchor -0.05

    with hpunch

    n "Con un fuerte codazo el chico cae redondo al suelo."

    hide an04_park_bank_pothead_body_receivingelbow

    show an04_park_bank_pothead_body_afterelbowing:
        xanchor -1.3 yanchor -0.52
    with dissolve

    fum "¡Joder!"

    fum "¡Me has hecho daño puta!"

    hide an04_park_bank_didac_fuckriding_legs
    hide an04_park_bank_didac_fuckriding_thighs
    hide an04_park_bank_didac_fuckriding_elbowing

    show an04_park_bank_didac_fuckriding 00right:
        xanchor 0.178
    with dissolve

    d "Que me metáis la polla,"

    extend " bien,"

    d "¡pero no me magrees las tetas!" 

    d "¡¿Qué coño estabas pensando hacer?! ¡idiota!"

    chu "Tiene mal genio la muy jodía,"

    extend " ¿verdad?"

    show an04_park_bank_didac_fuckriding 01
    with dissolve

    chu "Jajaja" # *condescending laugh* 

    fum "Hija de puta..."

    hide an04_park_bank_pothead_body_afterelbowing

    show an04_park_bank_pothead_body_standingup_spit:
        xanchor -1.05 yanchor -0.4
    show an04_park_bank_pothead_body_standingup_hand:
        xanchor -1.05 yanchor -0.4
    show an04_park_bank_pothead_body_standingup_body:
        xanchor -0.9 yanchor -0.4
    with dissolve

    n "El chico se levanta del suelo sangrando por la nariz y con bastantes malas pulgas se escupe en la mano."

    play sound "audio/sfx/sput05.ogg"

    show an04_park_bank_pothead_body_standingup_hand:
        subpixel True
        xanchor -1.05 yanchor -0.4
        easein_quad 0.5 xanchor -0.9
    show an04_park_bank_pothead_body_standingup_spit:
        subpixel True
        xanchor -1.05 yanchor -0.3
        pause 0.5
        easein_quad 0.25 xanchor -0.9 yanchor -0.4
        ease_quad 1.0 alpha 0.0
    show an04_park_bank_pothead_body_standingup_body:
        xanchor -0.9 yanchor -0.4
    with dissolve

    pt "¡¿Va a hacer lo que creo que va a hacer?!"

    pt "¡¿Sin condón?!"

    pt "¡Joder Dídac!"

    hide an04_park_bank_pothead_body_standingup_hand
    hide an04_park_bank_pothead_body_standingup_spit
    hide an04_park_bank_pothead_body_standingup_body

    show an04_park_bank_pothead_fuckstand_legs:
        xanchor -1.43 yanchor -0.168
    show an04_park_bank_pothead_fuckstand_body a:
        xanchor -1.43 yanchor -0.168
    with dissolve

    pt "Esto se te está yendo de las manos..."

    menu afternight04_Park_DidacFuckAnal_question:
        
        pt "¡Son dos putos desconocidos!"
        
        "<Detener esta locura>":
            
            call p_Help

            $ afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond = True

            jump afternight04_Park_DidacFuckAnal_No

        "<No hacer nada>":

            call p_Help

            $ afternight04_Park_DidacFuckAnal_Cond = True

            jump afternight04_Park_DidacFuckAnal_Yes

label afternight04_Park_DidacFuckAnal_Yes:

    chu "Date prisa tío,"

    extend " no creo que vaya a durar mucho más así..."

#########################################################
    
    if config.version < "00.99.99": # You decide to keep wathing them fucking Didac without condom.
        
        call endupdatescript
    
#######################################################

    d "Ahhh-"

    extend "mMMM..."

    d "¡¿Euh?!"

    show an04_park_bank_didac_fuckriding 00right
    with dissolve

    d "¿Qué coño haces magreándome el culo gilipollas?"

    show an04_park_bank_didac_fuckriding 02
    with dissolve

    n "El llamado \"Chulo\" le agarra por las piernas para incrementar el ritmo y así mantener a Dídac callada con sus gemidos."

    d "AAAHh-"

    extend "Mmmf..."

    d "Cabrón..."

    fum "Algo que te va a gustar,"

    extend " zorra."

    show an04_park_bank_pothead_fuckstand_body d
    show an04_park_bank_didac_fuckriding 00b
    with vpunch

    d "¡¡AAAAH... MMFFFfff...!"

    show an04_park_bank_didac_fuckriding 00
    with dissolve

    n "El chico de atrás consigue meterle la polla entera por el agujero anal de forma algo brusca,"

    n "mientras su compañero de delante, le tapa la boca para que sus gritos no se oigan en la lejanía."

    show an04_park_bank_pothead_fuckstand_body a
    show an04_park_bank_didac_fuckriding 02
    with dissolve

    chu "Shhh..."

    chu "No grites tigresa,"

    extend " o vas a llamar demasiado la atención..."

    show an04_park_bank_didac_fuckriding 00b
    with hpunch

    chu "¡AUH!"

    chu "¡Cabrona!"

    chu "¡me has mordido!"

    show an04_park_bank_didac_fuckriding 00
    with dissolve

    d "Hijos de puta."

    d "¿Quién os ha dado permiso para metérmela por el culo?"

    show an04_park_bank_didac_fuckriding 02
    with dissolve

    hide an04_park_bank_pothead_fuckstand_body
    hide an04_park_bank_pothead_fuckstand_legs

    show an04_park_bank_didac_fuckriding 02b
    with dissolve

    n "El de atrás empieza a embestirla cogiéndola por las nalgas y metiéndosela hasta el fondo."

    #Con cara de placer

    d "MMMFFF..." #*moans*

    chu "Joder,"

    chu "si es que al final te va a gustar más por el culo que por el coño,"

    extend " jodía..."

    chu "¿O me dirás que no te gusta la sensación de tener dos pollas dentro de ti?"

    #Con cara de pocos amigos.

    d "..." 

    chu "{i}No te pares y sigue follando{/i}."

    chu "¿No me habías dicho algo parecido?"

    d "Hijo de..."

    d "AAAhhh-mmmm..." #*moans*

    fum "Joder,"

    extend " el culo tampoco lo tiene nada mal..."

    n "El choque con las nalgas de Dídac era tan pronunciado,"

    n "que parecía que le estuviera dando cachetes ahí detrás."

    ono "SPLASH"

    extend " SPLASH"

    extend " SPLASH"

    #show an04_park_bank_pothead_fuckstand_legs:
        #xanchor -1.43 yanchor -0.168
    #show an04_park_bank_pothead_fuckstand_body a_right:
        #xanchor -1.43 yanchor -0.168
    show an04_park_bank_didac_fuckriding 00right_b
    #show an04_park_bank_didac_fuckriding 00right
    with hpunch

    oku "¡No me pegues!"

    # NOT FINISHED, KEEP ADDING ART.

    # Didac and Pothead looking right.

    n "Los tres quedan atónitos mirando al que se ha caído en redondo después de ese grito."

    fum "Puto yonki de mierda,"

    extend " está tan colgado,"

    fum "que confunde las cachetes con la pasma dándole de hostias..."

    
    show an04_park_bank_didac_fuckriding 01
    show an04_park_bank_pothead_fuckstand_legs:
        xanchor -1.43 yanchor -0.168
    show an04_park_bank_pothead_fuckstand_body a_right:
        xanchor -1.43 yanchor -0.168
    with dissolve

    # Didac keeps moving.

    n "Aunque poco después, Dídac sigue moviendo su cadera exigiendo a sus dos compañeros sexuales que no se detengan."

    # Pothead looks front again.

    show an04_park_bank_didac_fuckriding 01
    show an04_park_bank_pothead_fuckstand_body a
    with dissolve

    chu "A esta no la detiene ni la poli,"

    extend " del modo en que está..."

    hide an04_park_bank_pothead_fuckstand_legs
    hide an04_park_bank_pothead_fuckstand_body

    show an04_park_bank_didac_fuckriding 01b
    with dissolve

    fum "Joder,"

    extend " pero vaya culo tiene la macizorra esta,"

    #show an04_park_bank_didac_fuckriding 02b
    #with dissolve
    
    fum "me dan ganas de darle cachetes de verdad..."

    chu "No seas majara..."

    chu "Aunque ya de por sí estamos haciendo un ruido de la hostia,"

    chu "tampoco se nos vaya más la pinza..."

    fum "Lo mejor sería que le taparas la boca a esta,"

    fum "que empieza a gemir demasiado fuerte..."

    #scene day04
    #with fade

    #stop music fadeout 3.0

    chu "¿Para que me muerda de nuevo?"

    chu "Paso."

    show an04_park_bank_didac_fuckriding 02b
    with dissolve

    chu "Prefiero largarme echando leches de aquí si viene la pasma,"

    chu "antes de que la muy enferma me arranque un dedo..."

    fum "Pues ponle un trapo o algo..."

    chu "..."

    chu "Mhmm..." #*moan*

    chu "Joder,"

    chu "con tanta sangre ahí abajo,"

    chu "resulta que el capullo del \"Fumetas\" tiene hasta más materia gris que yo y todo..."

    fum "Te estás buscando una hostia,"

    extend " cabrón..."

    show an04_park_bank_didac_fuckriding 01b
    with dissolve

    n "Palpando el banco, consigue llegar a los bóxeres que se había quitado previamente."

    d "AMMFFF-MMFFF-MMM..." #*Gemidos ahogados por la tela*

    chu "Mira tú por dónde,"

    extend " su mala leche se le funde cuando va tan cachonda..."

    show an04_park_bank_didac_fuckriding 02b
    with dissolve

    n "Las dos pollas siguen perforando ambas cavidades y Dídac vuelve a disfrutar del placer de su nueva compañía."

    chu "Este condón es una mierda,"

    extend " se me está saliendo la polla cada dos por tres..."

    fum "Pues quítatelo..."

    chu "Paso,"

    chu "a saber qué putas infecciones tendrá esta ninfómana,"

    chu "si va por la calle a follarse al primero que pilla..."

    fum "Tío..."

    fum "yo no voy a poder aguantar mucho más a este ritmo..."

    fum "me voy a correr..."

    chu "Ughh..."

    chu "La verdad es que yo tampoco voy a tardar mucho..."

    d "Mmmfff-MMFFF..."  #*gemidos ahogados por la tela* 

    show an04_park_bank_didac_fuckriding 03b
    with dissolve

    fum "AAAhmm..."

    $ potheadCum = "_cum"

    fum "No puedo más..."

    fum "Joder..."

    show an04_park_bank_didac_fuckriding 02
    show an04_park_bank_pothead_fuckstand_legs:
        xanchor -1.43 yanchor -0.168
    show an04_park_bank_pothead_fuckstand_body d:
        xanchor -1.43 yanchor -0.168
    with dissolve

    # Change of image Fumeta STop Fucking Didac has sperm in her ass and legs and some on the bank so Fumeta don't sit down.

    show an04_park_bank_pothead_fuckstand_body c
    with dissolve

    show an04_park_bank_pothead_fuckstand_body b
    with dissolve

    show an04_park_bank_pothead_fuckstand_body a
    with dissolve

    n "Al sacar su polla del agujero anal de Dídac,"

    # Corrida en culo, zapato de tacón derecho de Dídac y banco.

    show an04_park_bank_bg_bank_cum 01
    with dissolve

    pause 0.5

    hide an04_park_bank_pothead_fuckstand_body
    hide an04_park_bank_pothead_fuckstand_legs

    show an04_park_bank_pothead_ground_hand empty:
        truecenter
        xpos 0.7 ypos 0.55
    show an04_park_bank_pothead_ground_body:
        truecenter
        xpos 0.7 ypos 0.55
    show an04_park_bank_pothead_ground_head left:
        truecenter
        xpos 0.7 ypos 0.55
    
    with dissolve


    n "parte de la corrida empieza a salir y a recorrer una de sus femeninas piernas."

    # Pothead also looks right.

    show an04_park_bank_pothead_ground_head right
    show an04_park_bank_pimp_02_head right
    with dissolve

    oku "Hijos de putaaah..."

    oku "Os la estáis follando de verdáaa..."

    oku "¡Y este hijoputa se ha corrido sin condón ahíii...!"

    n "El colgado de turno ha conseguido despertar de la hostia que se había metido."

    n "Observando aún sin levantarse del suelo"

    n "cómo su compañero -sentado en el banco-, sigue follándosela,"

    n "mientras el otro sigue reposando en el suelo completamente satisfecho."

    show an04_park_bank_pimp_02_head frontup
    with dissolve

    chu "Mhmm..." #*masculine moan*

    show an04_park_bank_pimp_02_head front
    show an04_park_bank_pothead_ground_head left
    with dissolve

    chu "Mierda..."

    chu " ya estoy al límite..."

    # Fumetas en el suelo fumando un porro.

    fum "BUUufff..." # *Sigh*

    n "El llamado \"Fumetas\" encuentra en su mochila uno de los porros que se había hecho previamente"

    show an04_park_bank_pothead_ground_hand smoke
    with dissolve

    show cigarette_smoke_pot_anim 01b: # POTHEAD
        transform_anchor True
        xalign 0.5 yalign 0.8
        xpos 0.678 ypos 0.5 zoom 0.5
    with Dissolve (1.0)

    n "y sin pensárselo demasiado, desnudo de cadera hacia abajo,"

    n "disfruta sentado en el suelo de su droga, totalmente satisfecho."

    fum "Joder..."

    fum "Vaya corrida..."

    fum "Esto de follar al aire libre con una desconocida,"

    fum "con la posibilidad de que te pillen,"

    fum "es otro nivel..."

    chu "¡Uuughhh!"

    n "Un gemido extraño -pero agudo- emana del chico que seguía follando con ese condón extremadamente enorme para él."

    # Didac es tirada al suelo por el Chulo putas con el boxer que tenía en la boca por el suelo.

    hide an04_park_bank_didac_fuckriding
    show an04_park_bank_pimp_02_head left
    show an04_park_bank_pimp_02_dick erect_naked
    show an04_park_bank_didac_falling:
        subpixel True
        truecenter
        xpos 0.38 ypos 0.4 rotate 15 # beginning
        ease_quad 0.5 xpos 0.3 ypos 0.53 rotate -15
    with vpunch

    #ono "PAM"

    pause 0.3

    hide an04_park_bank_didac_falling
    show an04_park_bank_onground_pimp_body empty:
        truecenter
        xpos 0.28 ypos 0.43
    show an04_park_bank_onground_pimp_cum empty:
        truecenter
        xpos 0.28 ypos 0.43
    show an04_park_bank_onground_pimp_head empty:
        truecenter
        xpos 0.28 ypos 0.43
    show an04_park_bank_onground_didac_body:
        truecenter
        xpos 0.28 ypos 0.43
    show an04_park_bank_onground_didac_head down:
        truecenter
        xpos 0.28 ypos 0.43
    with dissolve

    d "¡AAAUH!"

    n "Con un empujón, Dídac cae al suelo a los pies del \"Chulo\", mientras le cae el bóxer que tenía en la boca, por el impacto."

    d "¿Qué...?"

    show an04_park_bank_onground_didac_head up
    with dissolve

    d "¡¿Qué coño haces imbécil?!"

    # Chulo se corre en el cuerpo y cara de Dídac.

    hide an04_park_bank_pimp_02_body
    hide an04_park_bank_pimp_02_head
    hide an04_park_bank_pimp_02_dick
    hide an04_park_bank_pimp_02_legs

    show an04_park_bank_onground_pimp_body
    show an04_park_bank_onground_pimp_head up
    with dissolve

    n "El \"Chulo\" se agarra la polla y dándole una buena maniobra,"

    show an04_park_bank_onground_pimp_cum
    with dissolve

    n "consigue derramar toda su semilla sobre el cuerpo y rostro de Dídac, tendido en el suelo."

    hide an04_park_bank_onground_pimp_cum
    with Dissolve(1.0)

    # Dídac se cabrea, tiene pegado el condón de Chulo en Su coño.

    d "Hijo de puta..."

    show an04_park_bank_onground_pimp_head down
    with dissolve

    d "¡¿Qué coño haces?!"

    show an04_park_bank_onground_pimp_head up
    with dissolve

    chu "AAAAhhhh..." #*suspiro de relajación*

    n "Su cuerpo sigue aún convulso, y su polla aún gotea esperma en la punta."

    show an04_park_bank_onground_pimp_head down
    with dissolve

    chu "¿Qué...?"

    chu "¿Qué coño querías que hiciera...?"

    chu "¿Correrme dentro?"

    d "¡¿No te he dado un condón?!"

    chu "Mira..."

    chu "mira dónde se ha quedado,"

    extend " tu condón de los cojones..."

    d "¿Euh?"

    show an04_park_bank_onground_didac_head down
    with dissolve

    chu "Lo tienes pegado en tu chumino,"

    extend " idiota..."

    # Chulo sentado en el banco cansado. SOFT DICK ( NOT FINISHED )

    hide an04_park_bank_onground_pimp_body
    hide an04_park_bank_onground_pimp_head

    hide an04_park_bank_onground_didac_body
    hide an04_park_bank_onground_didac_head

    ## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head left:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_dick soft_naked:
        xanchor -1.25 yanchor -0.168

    ## Didac Gorund

    show an04_park_bank_onground_didac_body:
        truecenter
        xpos 0.28 ypos 0.43
    show an04_park_bank_onground_didac_head up:
        truecenter
        xpos 0.28 ypos 0.43

    # show an04_park_bank_pimp_01_body:
    #     xanchor -1.25 yanchor -0.168
    # show an04_park_bank_pimp_01_head left:
    #     xanchor -1.25 yanchor -0.168
    # show an04_park_bank_pimp_01_arm_L rest:
    #     xanchor -1.25 yanchor -0.168
    with Dissolve (0.5)

    n "Acto seguido, cae rendido en el banco, recuperando su antigua posición."

    n "El rostro de Dídac entremezcla asombro, desconcierto y cierto temor"

    show an04_park_bank_onground_didac_head down
    with dissolve

    n "al descubrir ese condón recién usado pegado en sus adentros."

    pt "Idiota,"

    extend " has tenido suerte que al menos el capullo este ha tenido un poco de sentido común..."

    
    hide an04_park_bank_onground_didac_head
    hide an04_park_bank_onground_didac_body

    show an04_park_bank_didac_01_body lingerie_dirt01:
        truecenter
        zoom 0.8 xpos 0.23 ypos 0.48
        #zoom 0.85 xanchor -0.5 yanchor -0.04
    show an04_park_bank_didac_01_armL relax:
        truecenter
        zoom 0.8 xpos 0.23 ypos 0.48
    show an04_park_bank_didac_01_armR relax:
        truecenter
        zoom 0.8 xpos 0.23 ypos 0.48
    show an04_park_bank_didac_01_head down:
        truecenter
        zoom 0.8 xpos 0.23 ypos 0.48
    with Dissolve (0.75)

    n "Dídac se levanta del suelo observando su cuerpo empapado en enfriado semen;"

    show an04_park_bank_didac_01_armR condomUsed
    show an04_park_bank_didac_01_head back
    with dissolve

    n "y sacándose el condón de su coño aún caliente."

    # Todos miran al Okupa.

    show an04_park_bank_pimp_02_head right
    show an04_park_bank_pothead_ground_head right
    show an04_park_bank_didac_01_head right
    with dissolve

    oku "Ahora me toca a mí..."

    extend " ¿No?"

    # El okupa llega a escena sin pantalones y con la polla al aire. El doble de tamaño que sus compañeros. (aún menor que MC)

    
    show an04_park_bank_bg_bank 04

    show an04_park_bank_didac_01_armR relax

    show an04_park_bank_squatter_onfeet_armR relax:
        truecenter
        xpos 1.0 ypos 0.53
    show an04_park_bank_squatter_onfeet_body:
        truecenter
        xpos 1.0 ypos 0.53

    show an04_park_bank_squatter_onfeet_head down:
        truecenter
        xpos 1.0 ypos 0.53
    show an04_park_bank_squatter_onfeet_armL relax:
        truecenter
        xpos 1.0 ypos 0.53
    with dissolve

    n "El tercer integrante del grupo logra ponerse en pie,"

    show an04_park_bank_squatter_onfeet_armR relax:
        xpos 0.95
    show an04_park_bank_squatter_onfeet_head down:
        xpos 0.95
    show an04_park_bank_squatter_onfeet_body:
        xpos 0.95
    show an04_park_bank_squatter_onfeet_armL relax:
        xpos 0.95
    with dissolve

    n "además de haberse desprendido de sus pantalones y ropa interior,"

    show an04_park_bank_pothead_ground_head squatter

    show an04_park_bank_squatter_onfeet_armR relax:
        xpos 0.9
    show an04_park_bank_squatter_onfeet_head down:
        xpos 0.9
    show an04_park_bank_squatter_onfeet_body:
        xpos 0.9
    show an04_park_bank_squatter_onfeet_armL relax:
        xpos 0.9
    with dissolve

    n "mostrando una tercera pierna de un tamaño considerablemente mayor que el de sus dos compañeros."

    show an04_park_bank_didac_01_armR hips
    show an04_park_bank_didac_01_armL hips

    #show an04_park_bank_didac_01_head right
    show an04_park_bank_pimp_02_head left
    show an04_park_bank_pothead_ground_head left
    with dissolve

    d "Vaya..."

    d "Esto,"

    extend " ya tiene otra pinta..."

    d "Ponte cómodo en el banco,"

    extend " y yo me pondré encima de ti."

    show an04_park_bank_pimp_02_head right
    show an04_park_bank_pothead_ground_head squatter
    show an04_park_bank_squatter_onfeet_head left
    with dissolve

    oku "No,"

    extend " no..."

    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    oku "pasooo de que me toqueee esa corrida de ahí..."

    oku "Ponte a cuatrooo..."

    oku "Quiero follarteee yo..."

    show an04_park_bank_pimp_02_head left
    show an04_park_bank_pothead_ground_head left
    with dissolve

    d "Hmmm..."

    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    d "La verdad es que las rodillas empiezan a dolerme..."

    n "Dídac vuelve su mirada otra vez a la entrepierna de este nuevo individuo y no puede evitar morderse el labio."

    d "Bien,"

    extend " tú ganas..."

    d "aunque espero que no me decepciones"

    d "Tus dos amigos aquí presentes no han conseguido sacarme ni un solo orgasmo..."

    pt "¡¿Lo dice en serio?!"

    show an04_park_bank_pimp_02_head right
    show an04_park_bank_pothead_ground_head squatter
    show an04_park_bank_squatter_onfeet_head left
    with dissolve

    oku "Ponte a cuatroooo..."

    extend " y ya veráaas..."

    # Dídac saca condón de su pecho.

    show an04_park_bank_didac_01_head down
    show an04_park_bank_didac_01_armR bra
    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    n "Dídac vuelve a poner su mano en su pecho derecho, debajo del extraño sujetador y saca el último condón."

    
    show an04_park_bank_didac_01_armR condomNew
    show an04_park_bank_didac_01_head right
    show an04_park_bank_pimp_02_head left
    show an04_park_bank_pothead_ground_head left
    with dissolve

    d "Toma,"

    extend " ponte esto."

    show an04_park_bank_squatter_onfeet_head left
    with dissolve

    oku "..."

    show an04_park_bank_pimp_02_head right
    show an04_park_bank_pothead_ground_head squatter
    with dissolve

    oku "A mí no me van las gomas..."

    show an04_park_bank_pimp_02_head left
    show an04_park_bank_pothead_ground_head left
    with dissolve

    d "Y a mí no me van las bromas de nueve meses."

    d "¡Póntelo, coño!"

    d "Además,"

    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    extend " a ti quizás te encaje mejor,"

    d "no te quejes."

    # Dídac se pone a cuatro cogíendose del banco con el culo en pompa con el semen en su ano y piernas.

    hide an04_park_bank_didac_01_body
    hide an04_park_bank_didac_01_head
    hide an04_park_bank_didac_01_armR
    hide an04_park_bank_didac_01_armL

    hide an04_park_bank_pothead_ground_body
    hide an04_park_bank_pothead_ground_head
    hide an04_park_bank_pothead_ground_hand

    hide an04_park_bank_pimp_02_body
    hide an04_park_bank_pimp_02_legs open_naked
    hide an04_park_bank_pimp_02_head front
    hide an04_park_bank_pimp_02_dick erect_naked

    hide cigarette_smoke_pot_anim

    ## pimp
    show an04_park_bank_pimp_01_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_head right:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_01_arm_L rest:
        xanchor -1.25 yanchor -0.168

    #pot head

    show an04_park_bank_pothead_ground_hand smoke:
        truecenter
        xzoom -1.0 xpos 0.42 ypos 0.55
    show an04_park_bank_pothead_ground_body:
        truecenter
        xzoom -1.0 xpos 0.42 ypos 0.55
    show an04_park_bank_pothead_ground_head left:
        truecenter
        xzoom -1.0 xpos 0.42 ypos 0.55

    
    # squatter

    show an04_park_bank_squatter_onfeet_head bank

    # Didac

    show an04_park_bank_fucking4_didac_armR back:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_head down:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_squatter_body empty:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_body:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_legs:
        an04_park_bank_fucking4_pos
    

    # show an04_park_bank_fucking4_didac_legs_PROVE:
    #     an04_park_bank_fucking4_pos
    #     alpha 0.0

    show an04_park_bank_fucking4_didac_ass:
        truecenter
        xpos 0.81 ypos 0.434
    show an04_park_bank_fucking4_didac_skirt:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_squatter_arm empty:
        an04_park_bank_fucking4_pos

    show cigarette_smoke_pot_anim 01b: # POTHEAD
        transform_anchor True
        xalign 0.5 yalign 0.8
        xpos 0.44 ypos 0.5 zoom 0.5
    

    with Dissolve (1.0)

    

    show cigarette_smoke_pimp_anim 01b: # PIMP
        transform_anchor True
        xalign 0.5 yalign 0.8
        xpos 0.33 ypos 0.41 zoom 0.5

    with Dissolve (1.0)

    n "Con todo su cuerpo empapado en semen frío, vuelve a poner sus manos sobre el banco,"

    n "poniendo su culo en pompa y abriendo las piernas, donde aún siguen fluyendo esperma y jugos vaginales;"

    n "al mismo tiempo que el {b}Fumetas{/b} se aparta, y el {b}Chulo{/b} se pone más cómodo."

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    d "Joder..."

    extend " realmente apestas tío..."

    show an04_park_bank_fucking4_didac_head down

    show an04_park_bank_squatter_onfeet_head down
    show an04_park_bank_squatter_onfeet_armR condom
    with dissolve

    # Okupa se mira el condón.

    n "El llamado \"Okupa\" se queda mirando la mano con la que sujeta el condón,"

    show an04_park_bank_squatter_onfeet_armL relax:
        truecenter
        zoom 0.95 xpos 0.9 ypos 0.42
    show an04_park_bank_squatter_onfeet_body:
        truecenter
        zoom 0.95 xpos 0.9 ypos 0.42
    show an04_park_bank_squatter_onfeet_head down:
        truecenter
        zoom 0.95 xpos 0.9 ypos 0.42
    show an04_park_bank_squatter_onfeet_armR relax:
        truecenter
        zoom 0.95 xpos 0.9 ypos 0.42
    with dissolve


    n "mientras se acerca detrás de Dídac contemplando su espectacular trasero."

    show an04_park_bank_squatter_onfeet_head left
    with dissolve

    d "..."

    
    show an04_park_bank_fucking4_didac_head right

    show an04_park_bank_squatter_onfeet_head down
    show an04_park_bank_squatter_onfeet_armR condom
    with dissolve

    d "Da igual,"

    extend " ya no puedo más..."

    show an04_park_bank_squatter_onfeet_head left
    with dissolve

    d "¡Métemela de una vez!"

    show an04_park_bank_fucking4_didac_head down

    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    pt "Su impaciencia es enfermiza..."

    # Okupa lanza el condón hacia ti.

    show an04_park_bank_squatter_onfeet_head left
    show an04_park_bank_squatter_onfeet_armR relax
    show an04_park_bank_squatter_onfeet_armL condomThrow:
        subpixel True
        xpos 0.89 ypos 0.41 
        easein_quad 0.5 xpos 0.902 ypos 0.422
        #truecenter
        #zoom 0.95 xpos 0.9 ypos 0.45

    with dissolve

    pause 0.3

    show an04_park_bank_squatter_onfeet_armL relax:
        zoom 0.95 xpos 0.9 ypos 0.42
    with dissolve

    n "Observas cómo el chico hace un gesto brusco con una de las manos."

    ono "TOC"

    show an04_park_bank_squatter_onfeet_head down
    with dissolve

    n "Acto seguido oyes el ruido de un pequeño objeto cayendo cerca de dónde estás."

    pt "¡¿Ha tirado el condón?!"

    pt "¡La madre que lo parió!"

    # Okupa se pone en posición para follar a Dídac a cuatro.

    hide an04_park_bank_squatter_onfeet_body
    hide an04_park_bank_squatter_onfeet_armL
    hide an04_park_bank_squatter_onfeet_armR
    hide an04_park_bank_squatter_onfeet_head

    show an04_park_bank_fucking4_squatter_body 01
    show an04_park_bank_fucking4_squatter_arm 01
    with Dissolve(0.5)

    pt "¡Se va a follar a Dídac a pelo!"

    pt "¡Tengo que parar esto antes de que pueda correrse dentro o será demasiado tarde!"

    menu afternight04_Park_DidacFuckWithoutCondom_question:
        
        pt "Si no detengo esto, Dídac no volverá nunca más a ser un chico."
        
        "<Detener esta locura>":
            
            call p_Help

            $pl.ch_pts("dp",10) #Te agradece mucho el hecho de que le hayas salvado. Podrás dejarlo preñado en la playa?

            $ afternight04_Park_DidacFuckWithoutCondom_Aborted_Cond = True #Has impedido que se quede preñada por el Okupa, cosa que te agradece.

            jump afternight04_Park_DidacFuckWithoutCondom_No

        "<No hacer nada>":

            call p_Help

            $ afternight04_Park_DidacFuckWithoutCondom_Pregnant = True
            $ DidacOKUPregnant = True

            jump afternight04_Park_DidacFuckWithoutCondom_Yes

label afternight04_Park_DidacFuckWithoutCondom_Yes:

    pt "Tú te lo has buscado Dídac..."

    pt "Si el capullo este te deja preñada,"

    extend " será tu culpa,"

    pt "no la mía."

    n "Con una de sus manos agarra fuertemente una de sus nalgas,"

    n "y con la otra dirige su polla hacia la entrepierna de Dídac."

    oku "Jodéee..."

    oku "Su culo sigue echando lefa..."

    extend " Qué ascoohh..."

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    d "¡Me follas ya!"

    d "¡¿O qué?!"

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    oku "A tomáaa por culooh..."

    # Didac
    #hide an04_park_bank_fucking4_didac_armR
    #hide an04_park_bank_fucking4_didac_head
    # squatter
    hide an04_park_bank_fucking4_squatter_body
    hide an04_park_bank_fucking4_didac_body
    hide an04_park_bank_fucking4_didac_legs
    
    # didac ass
    hide an04_park_bank_fucking4_didac_ass
    # squatter hand
    hide an04_park_bank_fucking4_didac_skirt
    hide an04_park_bank_fucking4_squatter_arm 01


    show an04_park_bank_fucking4_didac_head down

    show an04_park_bank_fucking4_splash empty
    show an04_park_bank_fucking4_comp 02
    with dissolve

    # Okupa empieza a moverse y a follar a Dídac lentamente.

    d "Aaaaahhh..."

    d "Síii..."

    extend " esto ya es otra cosa..."

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    d "Parece que me esté follando un cerdo,"

    d "con esta peste..."

    show an04_park_bank_fucking4_didac_head down
    with dissolve

    d "pero..."

    extend " joder..."

    d "cómo necesitaba esto..."

    show an04_park_bank_fucking4_comp 03
    with dissolve

    n "La enorme polla al desnudo del guarro del {b}Okupa{/b},"

    n "empieza a penetrar con profundidad su húmeda y caliente cavidad vaginal,"

    n "mientras posa ambas manos sobre sus nalgas."

    # Le azota una nalga.

    play sound "audio/sfx/punch06.ogg"

    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    #ono "SPLASH"

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    d "¡Aahh!"

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    d "No hace falta que me des de hosti..."

    # Luego la otra.

    play sound "audio/sfx/punch04.ogg"

    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0
    show an04_park_bank_fucking4_didac_head down

    #ono "SPLASH"

    show an04_park_bank_fucking4_didac_head down
    with dissolve

    d "¡Aauh!"

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    oku "Cájate Sorraaa..."

    # Okupa Aumenta el ritmo de follar a Dídac. (Salpica?)

    show an04_park_bank_fucking4_didac_head down
    with dissolve

    show an04_park_bank_fucking4_comp 05
    with dissolve

    n "Empieza a embestirla fuertemente en sus adentros,"

    play sound "audio/sfx/punch06.ogg"
    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    n "mientras sigue azotándole las nalgas,"

    play sound "audio/sfx/punch04.ogg"
    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    n "y chocando con su cadera en cada embestida,"

    play sound "audio/sfx/punch06.ogg"
    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    n "penetrándola casi hasta el fondo,"

    play sound "audio/sfx/punch04.ogg"
    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    n "y haciendo surgir sus jugos vaginales como si salpicara agua."

    d "AAAaahhh-mmm-MMmfff..."

    n "Los gemidos de Dídac van subiendo de tono y de intensidad, al mismo tiempo que el chico sigue dándole duro sin compasión."

    # Sigue azotándole las nalgas.

    play sound "audio/sfx/punch04.ogg"
    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    ono "SPLASH"

    play sound "audio/sfx/punch06.ogg"

    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    extend " SPLASH"

    play sound "audio/sfx/punch04.ogg"

    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    extend " SPLASH"

    n "Sus cachetes son cada vez más fuertes y frecuentes,"

    n "pero a Dídac parece que no le importa lo más mínimo,"

    n "su rostro es de lujuria y éxtasis absoluto."

    d "AAAmmm-AAAAHHH-AAAHHH..."

    n "Sus gemidos son cada vez más agudos, las embestidas cada vez más sonoras y sus cachetes cada vez más violentos."

    play sound "audio/sfx/punch04.ogg"

    show an04_park_bank_fucking4_splash 01:
        subpixel True
        truecenter
        additive 1.0 #xpos 0.81 ypos 0.4 # Default
        parallel:
            zoom 0.3 xpos 0.8 ypos 0.43 rotate -30 #size (81, 81) # Beginning
            easein_quad 0.5 zoom 1.5 xpos 0.81 ypos 0.4 rotate 10 #Finish
        parallel:
            linear 0.0 alpha 0.0
            easeout_quad 0.1 alpha 1.0
            easein_quad 0.4 alpha 0.0

    show an04_park_bank_fucking4_comp 06
    with dissolve

    oku "¡COÑOOOH!"

    oku "¡QUÉ COÑOOOHH!"

    show an04_park_bank_fucking4_comp 05
    with dissolve

    d "AAAAAH-AAAAHHH-AAAHHH..."

    n "La visión que ofrece Dídac es de que ha olvidado dónde está,"

    n "con quién está;"

    n "y se limita a disfrutar inconscientemente de la situación."

    n "A diferencia de sus dos compañeros,"

    n "este último parece no tener ningún reparo en alterar el silencio del lugar."

    oku "{size=40}¡¡ME CORRO JODER!!{/size}"

    pt "Si lo que me dijo Neus es cierto,"

    pt "nunca más volveré a ver a mi amigo siendo un chico..."

    pt "Aunque quizás, si se toma la pastilla del día después,"

    pt "puede que aún tenga alguna esperanza,"

    extend " aunque lo dudo bastante..."

    #show an04_park_bank_pimp_01_head left # They didn´t heard it yeat.
    #show an04_park_bank_pothead_ground_head right
    #with dissolve
    #
    play sound "audio/sfx/door_old_open01_otherroom.ogg"

    ono "{size=12}Riiick{/size}"

    n "Un agudo chirrido metálico se oye en la lejanía."

    pt "¡La puerta del parque!"

    pt "Con tanto ruido,"

    extend " habrán llamado la atención del vecindario,"

    pt "y seguramente algún agente estará al caer."

    # Chulo empieza a vestirse para lagarse.

    menu afternight04_Park_HelpDidacPolice_question:
        
        pt "¡Si no saco de aquí a Dídac inmediatamente se pondrá en un follón mayor!"
        
        "<Ayudar a Dídac a salir de ahí>":
            
            call p_Help

            $ afternight04_Park_HelpDidacPolice_Cond = True #Después de quedarse preñado, ayudas a Dídac a salir de ahí, 
            #sin que este se lo tome demasiado bien el hecho de que hubieras estado observándole sin haber hecho nada.

            jump afternight04_Park_HelpDidacPolice_Yes

        "<No hacer nada>":

            call p_Help

            $ afternight04_Park_AbandonDidacPolice_Cond = True

            jump afternight04_Park_HelpDidacPolice_No

label afternight04_Park_HelpDidacPolice_No:

    pt "Que le den..."

    pt "Intenté razonar con él,"

    pt "si es tan idiota,"

    extend " que asuma las consecuencias."

    # Change position?

    pt "Aunque quizás tendría que esconderme mejor," # Not sure if I will keep this

    extend " desde aquí es posible que me vean..."

    show an04_park_bank_fucking4_comp 07 #Cumming
    with dissolve

    oku "{size=40}¡¡AAARRRGHHHH!!{/size}"

    window hide dissolve
    pause 0.5

    #show an04_park_bank_fucking4_didac_armR back
    #show an04_park_bank_fucking4_didac_head down
    show an04_park_bank_fucking4_comp 08 # Taking off Dick
    with dissolve

    # Okupa saca la polla del coño de Dídac que empieza a brotar semen de él. con su colo completamente rojizo, 
    # semen antiguo del culo y del nuevo del coño.
    
    n "El llamado \"Okupa\" saca su polla del rojizo coño de Dídac,"

    n "del que acto seguido empieza a brotar el abundante semen vertido dentro de él."

    n "Empapando sus piernas de nuevo mezclando el solidificado frío semen con el más licuoso caliente actual,"

    n "junto con sus jugos vaginales."

    oku "Jodéee..."

    extend " qué corrida..."

    chu "Serás..."

    extend " ¡¿Te has corrido dentro sin condón?!"

    fum "¡Estás hecho un cabronazo, Okupa!"

    oku "Jejeje"

    oku "Yo creooo que tengo ya más retoños esparcidos por ahí,"

    extend " que {a=https://es.wikipedia.org/wiki/Julio_Iglesias}Julio Iglesiaasss{/a},"

    extend " túuu..."

    d "..."

    n "Los tres empiezan a reír a carcajadas, aunque la del \"Okupa\" es la más estridente."

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    d "¿Qué...?"

    fum "Lo mejor será que nos vayamos preparando para largarnos;"

    fum "con el ruido que han hecho estos dos,"

    fum "habrá despertado a todo el vecindario..."

    chu "Yo ya hace rato que estoy listo..."

    # Dídac recobrando el sentido común. Fumetas vistiéndose.

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    n "Apenas empezando a recobrar un poco el retorno a la realidad,"

    # tocándose la entrepierna para comprobar el semen ahí.

    show an04_park_bank_fucking4_didac_head down
    with dissolve

    n "siente que el caliente flujo seminal fluye rebosando desde sus labios vaginales hasta sus piernas."

    d "Y..."

    d "¡¿Y el condón?!"

    oku "¡Mucho mejor a pelooo!"

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    oku "¡Me vas a comparáaa!"

    stop music fadeout 0.25
    play sound "audio/sfx/meme_surprise02.ogg"

    # Una luz a la izquierda de los guardias de seguridad.

    hide an04_park_bank_fucking4_comp

    show an04_park_bank_p_A_stand_arm_R empty:
        an04_park_bank_p_A_stand_pos
    show an04_park_bank_p_A_stand_body empty:
        an04_park_bank_p_A_stand_pos
    show an04_park_bank_p_A_stand_head empty:
        an04_park_bank_p_A_stand_pos
    

    # Didac

    show an04_park_bank_fucking4_didac_armR back:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_head down:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_squatter_body 01_left:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_body:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_legs:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_ass:
        truecenter
        xpos 0.81 ypos 0.434 

    show an04_park_bank_fucking4_didac_skirt:
        an04_park_bank_fucking4_pos

    show an04_park_bank_p_A_stand_jacket empty:
        an04_park_bank_fucking4_pos

    show an04_park_bank_p_A_stand_arm_L empty:
        an04_park_bank_p_A_stand_pos

    show an04_park_bank_fucking4_squatter_arm 01:
        an04_park_bank_fucking4_pos
    with dissolve



    show an04_park_bank_pimp_01_head left
    show an04_park_bank_pothead_ground_head right
    show an04_park_bank_fucking4_didac_head left

    show light 01 zorder 98:
        additive 1.0
        truecenter
        rotate -90
    
    with dissolve

    n "Una luz cegadora deja sin visión a los cuatro integrantes durante unos segundos."

    # Aparecen los dos agentes en escena.

    if music_play != "twisted":
        play music "audio/music/kevinmacleod/twisted.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "twisted"

    s "¡¿Se puede saber qué está pasando aquí?!"

    # Fumetas, Chulo y sus pertenencias desaparecen de escena.

    n "Tanto el \"Chulo\" como el \"Fumetas\","

    hide an04_park_bank_pimp_01_head
    hide an04_park_bank_pimp_01_body
    hide an04_park_bank_pimp_01_arm_L

    hide an04_park_bank_pothead_ground_head
    hide an04_park_bank_pothead_ground_body
    hide an04_park_bank_pothead_ground_hand_smoke
    hide an04_park_bank_bg_bank_cum
    hide an04_park_bank_pothead_condom_ground

    hide cigarette_smoke_pimp_anim
    hide cigarette_smoke_pot_anim
    hide an04_park_bank_pothead_ground_hand

    show an04_park_bank_bg_bank 06
    with dissolve

    n "agarran sus respectivas mochilas del suelo,"

    n "arrancando a correr con sus pertenencias, tan deprisa como pueden."

    # Okupa cae al sueloi ntentando escapar sin pantalones y la polla al aire.

    hide an04_park_bank_fucking4_squatter_arm
    hide an04_park_bank_fucking4_squatter_body

    show an04_park_bank_fucking4_didac_head down
    
    show an04_park_bank_p_A_ground_police_body empty:
        an04_park_bank_p_A_ground_pos
    show an04_park_bank_p_A_ground_police_head empty:
        an04_park_bank_p_A_ground_pos
    show an04_park_bank_p_A_ground_squatter fall:
        an04_park_bank_p_A_ground_pos
    with dissolve

    n "El que queda, en su intento de escapar, tropieza estúpidamente, cayendo al suelo en redondo,"

    # Un agente se tira encima de él inmovilizándolo.

    
    show an04_park_bank_p_A_ground_police_body
    show an04_park_bank_p_A_ground_police_head toSquatter
    show an04_park_bank_p_A_ground_squatter handcuffed
    with dissolve

    n "mientras uno de los agentes se lanza encima de él inmovilizándole."

    # El otro policía desaparece de escena.

    hide light
    show an04_park_bank_p_B_running:
        subpixel True
        truecenter
        xpos -0.2 ypos 0.47
        easein 1.2 xpos 1.4
    with dissolve

    n "El otro corre tan deprisa como puede para alcanzar a los dos restantes."

    # Policí esposando a Okupa.

    hide an04_park_bank_p_B_running

    s "¡Tienes derecho a guardar silencio!"

    s "Cualquier cosa que digas podrá ser usada en tu contra en un tribunal de..."

    # Agente mirando a Dídac aún de pie y en shock.

    show an04_park_bank_p_A_ground_police_head toDidac
    with dissolve

    n "Justo cuando el agente consiguió ponerle las esposas al sujeto del suelo,"

    n "su mirada se fija en Dídac."

    n "La visión de una mujer luciendo una lencería femenina rojiza,"

    n "con todo su cuerpo cubierto en semen y sudor,"

    n "con ambos agujeros rebosando esperma recorriéndole ambas piernas,"

    n "dejan al agente un tanto perplejo."

    # Policía poniendo chaqueta encima de Dídac y para preguntarle como se encuentra.

    
    hide an04_park_bank_p_A_ground_police_body
    hide an04_park_bank_p_A_ground_police_head

    hide an04_park_bank_fucking4_didac_skirt

    show an04_park_bank_p_A_stand_arm_R rest
    show an04_park_bank_p_A_stand_body
    show an04_park_bank_p_A_stand_head toDidac
    show an04_park_bank_p_A_stand_arm_L toDidac
    show an04_park_bank_p_A_stand_jacket

    show an04_park_bank_bg_bank cum_03
    with dissolve

    n "Cuando consigue dejar completamente inmovilizado al llamado \"Okupa\","

    n "se levanta, recoge al abrigo que hay debajo del banco, y lo usa para cubrir el cuerpo de Dídac."

    s "..."

    s "Señorita,"

    extend " ¿se encuentra bien?"

    d "..."

    n "Su mirada está dirigida al vacío, con una expresión totalmente ausente."

    n "Todo su cuerpo tiembla en espasmos leves y fuertes."

    # LInterna del guardia  mirando alrededor.

    show an04_park_bank_p_A_stand_head around
    show an04_park_bank_p_A_stand_arm_L around
    show an04_park_bank_p_A_stand_arm_L_around_light:
        additive 1.0
        alpha 0.9
        an04_park_bank_p_A_stand_arm_L_around_light_pos
    with dissolve

    n "El agente aparta su mirada de la chica para observar el lugar con su linterna."

    n "Dos condones usados, arrugados y sucios,"

    n "esperma y fluidos diluyéndose en la arena del suelo,"

    n "así como marcas de múltiples pies y nalgas justo delante del banco."

    # Walkie con la mano que no sujeta linterna ( NOT FINISHED !!)

    show an04_park_bank_p_A_stand_arm_R walkie
    with dissolve

    n "El agente levanta la mano en la que lleva un {a=https://es.wikipedia.org/wiki/Walkie-talkie}walkie-talkie{/a}."

    n "Desde la lejanía no entiendes perfectamente lo que dice,"

    n "pero te da la sensación de que está pidiendo efectivos y una ambulancia."

    n "Dídac seguía como ausente, sumida como en un trance extraño,"

    n "agarrándose al abrigo del agente y sin dejar de temblar."

    pt "Es lo mejor que puedes hacer Dídac..."

    extend " o realmente te pondrás en un buen..."

    # Luz de la linterna te enfoca a ti.

    play sound "audio/sfx/meme_surprise02.ogg"
    stop music fadeout 0.5
    $ music_play = ""

    hide an04_park_bank_p_A_stand_arm_L_around_light

    show an04_park_bank_p_A_stand_head camera
    show an04_park_bank_p_A_stand_arm_L camera
    #show sunglow 02:
    show sunglow 01:
        truecenter
        additive 1.0
        xpos 0.852 ypos 0.275
        block:
            linear 100.0 rotate 360
            linear 0.0 rotate 0
            repeat

    with dissolve

    #n "Un foco cegador te nubla completamente la vista."

    s "¡¿Quién anda ahí?!"

    # Bajas la cabeza mirando a los arbustos.

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    show an04_park_bank_far_bush 01:
        subpixel True
        xanchor 0.0 yanchor 0.0 zoom 0.5
        easein_quad 1.0 xanchor 0.0 yanchor 0.59 zoom 0.5
    with dissolve

    pt "¡Mierda!"

    extend " ¡Me ha visto!"

    # escena en Negro.

    scene bg an04_park_path01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.4 # Beginning
        easein 5.0 zoom 1.0 xpos 1.0 ypos 0.2 # Going to Left.
    with hpunch

    $ renpy.music.set_volume(0.0, delay=0.0, channel='sfx2')

    n "Sales de ahí como alma que lleva el diablo sin mirar atrás,"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    $ renpy.music.set_volume(0.8, delay=15.0, channel='sfx2')
    $ renpy.music.play("audio/sfx/police_siren_01.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene bg an04_entranceciutadella_fence_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.6 ypos 0.3
        easein 15.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "saltando la valla de seguridad del parque,"

    # Sonido de cuerpos policiales acercándose.

    n "mientras oyes a no mucha distancia, varias sirenas de la policía acercándose."

    # Callejón de la ciudad.

    $ renpy.music.set_volume(0.1, delay=15.0, channel='sfx2')

    scene bg an04_placasantagustivell_composition 04:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        easein 5.0 xanchor 1.0 yanchor 0.7 zoom 1.0
    with fade

    n "Después de recorrer varias calles,"

    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    scene bg an04_street02:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.5
        easein 20.0 zoom 1.0 xpos 0.25 ypos 0.5
    with fade

    n "decides descansar un poco, al pensar que la policía te ha perdido la pista completamente."

    p "Ufff..."

    p "Por qué poco..."

    p "¡Tú mismo te lo has buscado imbécil!"

    p "La madre que te parió..."

    # Imagen del piso.

    stop music fadeout 3.0
    $ music_play = ""

    scene afternight03_bg_entrance_lightoff_night
    with fade

    pause 0.5
    play sound "audio/sfx/click_turnofflights.ogg"
    scene afternight03_bg_entrance_lighton
    with dissolve

    p "..."

    if music_play != "aura":
        play music "audio/music/alcaknight/aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "aura"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    with dissolve

    n "Con resignación vuelves andando hasta vuestro piso, obviamente vacío."

    n "Debido a los nervios y a la precipitada fuga, tu cuerpo está cubierto en sudor."

    # Ducha.

    $ renpy.music.set_volume(0.8, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene afternight03_bg shower
    with fade

    n "Decides tomarte una ducha, comer algo,"

    $ renpy.music.stop(channel='sfx1', fadeout=1.0)

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    n "y poco después,"

    play sound "audio/sfx/click_turnofflights.ogg"

    stop music fadeout 3.0
    $ music_play = ""

    show beds_night_lightOff_blindUp_DemptyMCbusy
    with Dissolve (1.0)

    n "reunirte con Morfeo."

    scene black
    with fade

    # Escena de cama de noche con la cama de Dídac vacía.

    jump morning05

label afternight04_NeusCallForDidac:

    scene black
    
    pause 5.0

    play sound "audio/sfx/ring_phone01.ogg"
    scene black
    with hpunch
    ono "{size=30}RIIIIING{/size}"

    $ renpy.music.set_volume(0.02, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "Un sonoro timbre del teléfono móvil te despierta abruptamente."

    pt "¿A estas horas?"

    pt "¿Qué diablos querrán?"

    p "..."

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        pt "Como sea Dídac lo voy a enviar a la mierda..."

    else:

        pt "¡Quizás es Dídac!"

    scene black
    with hpunch

    play sound "audio/sfx/ring_phone01.ogg"

    ono "{size=30}RIIIIING{/size}"

    n "Alargas el brazo para coger el móvil que está encima de la mesita de noche."

    #Si ha ido a prisión, la pregunta sería distinta. NOT FINISHED

    pt "¿En qué tipo de follón se habrá metido ahora el muy imbécil?"

    play sound "audio/sfx/click01.ogg"
    ono "Clic"

    p "¿Diga...?"

    ne "[protname],"

    extend " perdona que te llame a estas horas..."

    play music "audio/music/neus_theme.ogg" fadein 3.0 fadeout 3.0
    $ renpy.music.stop(channel = 'sfx1', fadeout = 10.0) 

    p "¡¿Neus?!"

    pt "¡¿Qué diablos hace llamándome en plena noche?!"

    ne "¿Está Dídac ahí contigo?"

    p "¿Euh?"

    p "¿Dídac?"

    scene beds_night_lightOff_blindDown_DemptyMCbusy
    with Dissolve (2.0)

    n "Con tus ojos algo borrosos por estar aún sumidos en el descanso nocturno,"

    n "fuerzas tu mirada hacia la cama de tu compañero que sigue igual de intacta."

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        pt "¿Aún sigue con esos capullos...?"

    else:

        pt "Mierda Dídac..."

        extend " ¿Aún no has llegado?"

    n "Rápidamente miras la hora en tu móvil."

    pt "¡Son las tres de la madrugada!"

    ne "No está..."

    extend " ¿Verdad?"

    p "No,"

    extend " no está..."

    ne "..."

    p "¿Có-"

    extend "cómo sabes que no está aquí?"

    p "¿Tienes idea de dónde puede estar?"

    ne "No..."

    extend " no lo sé..."

    p "¿Le ha pasado algo?"

    ne "..."

    ne "No estoy segura..."

    p "¿A qué te refieres?"

    ne "Es difícil de explicar..."

    ne "Simplemente he tenido una sensación de que algo le ha podido pasar..."

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        p "¿Crees que está en peligro?"

    else:

        p "¡¿Te refieres a que está en peligro?!"

    ne "..."

    ne "Es posible..."

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        p "¿Y dónde está?"

    else:

        p "Pero ¡¿dónde está?!"


    ne "No lo sé, [protname]..."

    p "¿Y cómo es que me has llamado?"

    ne "Porque he tenido un mal presentimiento..."

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        p "Ya veo..."

    else:

        p "Pero,"

        extend " ¿dónde puedo empezar a buscarlo?"


    ne "Lo siento [protname],"

    ne "quizás no es nada y ha sido un error llamarte a estas horas..."

    ne "espero que Dídac esté bien y esto simplemente haya sido una locura mía..."

    ne "Buenas noches."

    play sound "audio/sfx/click01.ogg"
    ono "Clic"

    p "¿Qué diablos...?"

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant or afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        jump afternight04_Park_LookingForDidac_No

    else:

        p "Pero ¿dónde puedo empezar a buscarlo?"

        pt "¿Qué se supone que tengo que hacer ahora?"

        jump afternight04_Park_LookingForDidac_question

    menu afternight04_Park_LookingForDidac_question:
        
        pt "Siempre tiene que estar tocando las narices..."
        
        "<Salir a la calle a buscar a Dídac>":
            
            call p_Help

            jump afternight04_Park_LookingForDidac_Yes

        "<Irte a dormir>":

            call p_Help

            jump afternight04_Park_LookingForDidac_No

label afternight04_Park_LookingForDidac_Yes:

    $ afternight04_Park_LookingForDidac_yes_Cond = True

    p "¡Maldita sea!"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    hide afternight03_bg_entrance_keysmc lightoff_night
    with dissolve

    n "Recoges las llaves de la entrada,"

    scene bg an04_flat_outside
    with fade

    window hide dissolve
    pause 

    $ saturation_tint_level = "default"

    scene bg an04_flat_gate_composition002:
        subpixel True
        zoom 1.0 xanchor 0.0 yanchor 0.0
        easein_quad 3.0 zoom 0.5 xanchor 0.0 yanchor 1.4 #General view door.
    with fade

    n "y decides salir a la calle."

    scene night03_bg street_catalunya_square
    with fade

    n "Crees que lo más sensato es ir a los lugares donde soléis pasar la mayor parte del tiempo,"

    scene bg an04_palaumusica_composition:
        subpixel True
        xanchor 0.0 yanchor 0.0 zoom 0.5
        ease_quad 20.0 xanchor 0.0 yanchor 1.9 zoom 0.5
    with fade

    n "recorres los callejones del barrio antiguo de Barcelona,"

    scene bg an04_street02_composition 03:
        subpixel True
        xanchor 0.4 yanchor 0.5 zoom 1.0
        easein_quad 20.0 xanchor 0.5 yanchor 0.0 zoom 0.67
    with fade

    n "buscas en los bares nocturnos que soléis frecuentar, incluso algún {b}puticlub{/b} cercano por si las moscas."

    scene bg an04_placasantagustivell_composition 04:
        subpixel True
        xanchor 0.2 yanchor 0.7 zoom 1.0
        ease_quad 20.0 xanchor 0.0 yanchor 0.5 zoom 1.0
    with fade

    p "Esto es como buscar una aguja en un pajar..."

    show morning04_bg_livingroom_mc_resting_phone didac:
        
        xpos 0.485 ypos 0.125
        
    show morning04_livingroom_mc_resting_handphone
    with dissolve

    n "Sigues enviándole mensajes a través de {i}WhatsApp{/i},"

    n "pero solo recibes el silencio por respuesta."

    pt "Quizás debería llamar a la policía..."

    pt "Pero ¿qué diablos les digo?"

    pt "Buenas,"

    extend " me pregunto si saben algo sobre mi compañero de piso,"

    pt "que no sé dónde está,"

    pt "ah,"

    extend " y además ahora se ha transformado en una mujer."

    pt "Cuando descubran más sobre él,"

    pt "o peor aún,"

    extend " su identificación,"

    extend " DNI,"

    extend " o huellas dactilares;"

    pt "me temo lo peor..."

    hide morning04_bg_livingroom_mc_resting_phone
    hide morning04_livingroom_mc_resting_handphone
    with dissolve

    pt "Dídac..."

    extend " ¡¿Dónde diablos te has metido?!"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    scene afternight03_bg entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "Con resignación vuelves al piso con la esperanza de encontrártelo ahí,"

    scene beds_night_lightOff_blindUp_DemptyMCempty
    with fade

    n "pero esa ilusión se diluye completamente al comprobar que es completamente errónea."

    n "Decides que lo más sensato es esperar a mañana y desear que nada malo haya ocurrido."

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    with dissolve

    n "Te aseas en el baño y luego vuelves a tu solitaria habitación a reunirte de nuevo con Morfeo."

    scene black
    with fade

    jump morning05

label afternight04_Park_LookingForDidac_No:

    p "¡¿Ahora tengo que ir a salir a buscar al inútil de Dídac?!"

    p "Para empezar..."

    extend " ¡¿Dónde diablos empiezo a buscarle?"

    extend " ¿En las alcantarillas?"

    if afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant == True:

        p "¡¿En el parque?!"

        extend " Donde seguramente ya habrán terminado de violarlo..."

    elif afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond == True:

        p "En el parque no estarán..."

        p "seguramente lo habrán llevado a algún lugar para hacerle un {a=https://es.wikipedia.org/wiki/Gang_bang}gangbang{/a} entre diez,"

        extend " o veinte tíos..."

    else:

        p "Pero ¿dónde puedo empezar a buscarlo?"

    p "¡Si no me responde a las llamadas ni a los mensajes de {i}WhatsApp{/i},"

    extend " es su puñetero problema!"

    p "¡A tomar viento!"

    p "¡Ya se las apañará!"

    stop music fadeout 5.0

    n "Con cierta irritación, decides asearte en el baño y acto seguido volver a la solitaria habitación para reunirte con Morfeo."

    jump morning05

label afternight04_Park_DidactobeFucked_No:

    #fum "sí..."

    #d "Ponte esto."

    #pt "Joder... joder... Dídac... ¡¿Qué coño haces?!"
        
    #pt "¡Son dos putos desconocidos!"
        
    #"<Detener esta locura>" #The one Chosen.

    #You appear to stop this maddness, Didac refuse. You can insist or leave. If you insist you have to battle them, 

    #if you fail, you just wake up in the police station.

    play music "audio/music/didac_theme.ogg" fadeout 3.0 fadein 3.0

    p "¡¿Se puede saber qué está pasando aquí?!"

    scene bg an04_park_bank_far_closer_background_01:
       zoom 0.5
    #scene bg_an04_park_bank_far_closer_background_prove03:
       #zoom 0.5
#
## background bank
    show an04_park_bank_bg_bank 02:
        xanchor -0.176 yanchor 0.005
    show an04_park_bank_bg_bank_cum empty:
        xanchor -0.176 yanchor 0.005

#
## pothead

    show an04_park_bank_pothead_02_shoes semiclosed:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_armR rest:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_body cloth:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_legs semiclosed_naked:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_head front:
        xanchor -2.23 yanchor -0.168
    show an04_park_bank_pothead_02_dick erect_naked:
        xanchor -2.23 yanchor -0.168
#
## didac_sit

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:
        show an04_park_bank_didac_02_arm_L rest:
            xanchor -0.99 yanchor -0.52
        show an04_park_bank_didac_02_arm_R rest:
            xanchor -0.99 yanchor -0.52
    else:

        show an04_park_bank_didac_02_arm_L restnaked:
            xanchor -0.99 yanchor -0.52
        show an04_park_bank_didac_02_arm_R restnaked:
            xanchor -0.99 yanchor -0.52

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == True:

        show an04_park_bank_didac_02_body clothed_crossedlegs_lingerie:
            xanchor -0.99 yanchor -0.52
    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show an04_park_bank_didac_02_body_clothed_back:
            xanchor -0.99 yanchor -0.52 

    show an04_park_bank_didac_02_head front02:
        xanchor -0.99 yanchor -0.52

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show an04_park_bank_didac_02_body clothed_crossedlegs:
            xanchor -0.99 yanchor -0.52

#
## pimp
    show an04_park_bank_pimp_02_body:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_legs open_naked:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_head front:
        xanchor -1.25 yanchor -0.168
    show an04_park_bank_pimp_02_dick erect_naked:
        xanchor -1.25 yanchor -0.168

#
## Bush
    show an04_park_bank_far_bush 02 zorder 99:
        xanchor 0.0 yanchor 0.13 zoom 1.0
    with dissolve

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        n "Todos ahí presentes se quedan enmudecidos, sorprendidos y asustados al mismo tiempo observándote entre la penumbra."

    else:

        n "Rápidamente los tres vuelven a sentarse en el banco, mientras Dídac intenta cerrar sus piernas lo mejor que puede para mostrar disimulo."

    show an04_park_bank_pothead_02_head left
    with dissolve

    fum "¡Mierda!"

    fum "¡La pasma!"

    show an04_park_bank_pothead_02_head front
    with dissolve


    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show an04_park_bank_didac_02_arm_L rest
        with dissolve

        n "Dídac absurdamente se el cubre cuerpo mientras disimula lo mejor que puede."

    show an04_park_bank_pimp_02_head right
    with dissolve

    chu "No..."

    show an04_park_bank_pimp_02_head front
    with dissolve

    chu "Es un solo tío,"

    extend " no tiene linterna y además no viste de traje..."

    fum "¿Cómo?"

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

###
    ## PIMP

    show an04_park_pimp_armR clear:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_body pants:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_eyes 02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_pupils front02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_eyebrows angryx02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_mouth sad_Silentx03:
        an04_park_pimp_middle_expressions

    with dissolve

    n "Sin demasiada demora, observas al más tranquilo de ellos levantarse,"

    n "subirse los pantalones, y acercarse hasta donde te encuentras."

    show an04_park_pimp_eyebrows angryx03
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Talkingx05
    with dissolve

    chu "¡¿Quién coño eres?!"

    show an04_park_pimp_eyebrows serious
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Silentx03
    with dissolve

    p "Eso no es de tu incumbencia."

    show an04_park_pimp_eyebrows surprisex01
    show an04_park_pimp_eyes 03
    show an04_park_pimp_pupils front03
    show an04_park_pimp_mouth sad_Silentx03
    with dissolve

    p "He venido a buscar a la chica."

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    # show didacfbodybelow naked:
    #     zoom 0.25 xanchor 0.2
    # show didacfbodybelow_panties park:
    #     zoom 0.25 xanchor 0.2
    show didacfbodytop park:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show didacfbodycloth_whole gabardine:
            zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 01:
        an04_park_didacf_left_expressions

    show didacf_eyes 04:
        an04_park_didacf_left_expressions

    show didacf_pupils front04:
        an04_park_didacf_left_expressions

    show didacf_eyebrows angryx03:
        an04_park_didacf_left_expressions

    ##

    ###show didacf_aprove:
        ###zoom 0.25 xanchor 0.2 alpha 0.2

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Talkingx04:
        an04_park_didacf_left_expressions

###

    ## POTHEAD

    show an04_park_pothead_body pants:
        zoom 0.5 xanchor -0.85

    show an04_park_pothead_eyes 02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_pupils left02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_eyebrows normal:
        an04_park_pothead_right_expressions
    show an04_park_pothead_mouth sad_Silentx02:
        an04_park_pothead_right_expressions

###
    ## PIMP

    show an04_park_pimp_armR clear:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_body pants:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_eyes 02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_pupils left02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_eyebrows normal:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_mouth sad_Silentx03:
        an04_park_pimp_middle_expressions

        
    ###show an04_park_pimp_body_prove:
        ###zoom 0.5 xanchor -0.3 alpha 0.5
    with dissolve

    d "¡[protname]!"

    show didacf_mouth sad_Silentx04

    show an04_park_pothead_eyebrows surprisex01
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils left02
    show an04_park_pothead_mouth sad_Talkingx03

    with dissolve

    fum "¿Lo conoces?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05

    show an04_park_pimp_eyebrows serious
    show an04_park_pimp_eyes 02
    show an04_park_pimp_pupils front02
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows surprisex02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx03
    with dissolve

    p "Dejadla en paz."

    show an04_park_pimp_eyebrows angryx01
    show an04_park_pimp_eyes 03
    show an04_park_pimp_pupils front03
    show an04_park_pimp_mouth sad_Talkingx02

    show an04_park_pothead_eyebrows normal
    with dissolve

    chu "Porque tú lo digas..."

    extend " ¿No?"

    show didacf_eyes 00
    show didacf_pupils front01
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx02

    show an04_park_pimp_eyebrows surprisex01
    show an04_park_pimp_eyes 00
    show an04_park_pimp_pupils front00
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows surprisex02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx01
    with dissolve

    p "¡¿No veis que está enferma?!"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx06

    show an04_park_pimp_eyebrows surprisex01
    show an04_park_pimp_eyes 00
    show an04_park_pimp_pupils left00
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows surprisex01
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils left02
    show an04_park_pothead_mouth sad_Silentx02
    with dissolve

    pause

    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07

    show an04_park_pothead_mouth sad_Talkingx03

    fum "¡¿Qué tipo de enfermedad tienes tía?!"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx04

    show an04_park_pimp_eyebrows normal
    show an04_park_pimp_eyes 02
    show an04_park_pimp_pupils left02
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows surprisex01
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils left02
    show an04_park_pothead_mouth sad_Silentx02
    with dissolve

    d "Idiotas..."

    extend " no estoy enferma,"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡¿No veis lo que pretende?!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "Está crispado porque antes no me ha querido follar,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "y le he dicho que si no me follaba él,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "ya encontraría a alguien para que lo hiciese."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "Pero el muy egoísta no quiere que nadie más me toque..."

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == True:

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx04

        show an04_park_pimp_eyebrows surprisex01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils front02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows sadx02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils front02
        show an04_park_pothead_mouth happy_Silentx03
        with dissolve

        p "¡¿No ves que se ha quitado el condón?!"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx004
        with dissolve

        d "¿Qué?"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05

        show an04_park_pimp_eyebrows surprisex01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils right02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows surprisex02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx03
        with dissolve

        d "¡¿Es cierto?!"

        show didacf_eyes 01
        show didacf_pupils right01
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx04

        show an04_park_pothead_eyebrows sadx03
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Talkingx03
        with dissolve

        fum "Sí,"

        extend " pero te lo iba a meter por el culo..."

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08

        show an04_park_pimp_pupils left02

        show an04_park_pothead_eyebrows sadx02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx04
        with dissolve

        d "Gilipollas,"

        extend " os he dicho que me folléis por el coño y con condón..."

        show didacf_eyes 00
        show didacf_pupils right00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with dissolve

        d "¡¿Quién os ha dado permiso para follarme por el culo?!"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx06

        show an04_park_pimp_eyebrows normal
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils left02
        show an04_park_pimp_mouth sad_Talkingx02

        show an04_park_pothead_eyebrows surprisex01
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx03
        with dissolve

        chu "En realidad no has especificado por dónde teníamos que follarte,"

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx04
        with dissolve

        chu "solo has dicho \"folladme\"."

        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx05

        show an04_park_pimp_eyebrows normal
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils left02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows surprisex01
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx01
        with dissolve

        d "..."

        show didacf_eyes 05
        show didacf_pupils right05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "Pero creo que me he hecho entender..."

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx03

        show an04_park_pimp_pupils front02

        show an04_park_pothead_pupils front02

        with dissolve

        p "Será mejor que volvamos a casa."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx04

        show an04_park_pimp_pupils left02

        show an04_park_pothead_pupils left02

        with dissolve

        d "¡No!"

        show didacf_eyes 05
        show didacf_pupils down05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "Por si no lo has notado,"

        extend " sigo chorreando..."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "y la cosa no se ha calmado."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "Y mucho menos gracias a ti,"

        extend " precisamente."

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07

        show an04_park_pimp_pupils front02

        show an04_park_pothead_pupils front02

        with dissolve

        p "¿No te das cuenta que lo que estás haciendo aquí es una puta majadería?"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08
        with dissolve

        d "Vete a la mierda [protname]."

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09

        show an04_park_pimp_pupils left02

        show an04_park_pothead_pupils left02

        with dissolve

        d "¡Has sido tú quien no ha querido ayudarme!"

        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "No quiero que estés aquí,"

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx004
        with dissolve

        d "y mucho menos que vayas de jodido salvador de los cojones."

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "Das pena."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08
        with dissolve

        d "¡¿Lo sabías?!"

        show didacf_eyes 03
        show didacf_pupils right03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx08
        with dissolve

        p "..."

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "Lárgate."

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx05

        show an04_park_pimp_pupils front02

        show an04_park_pothead_pupils front02

        with dissolve

        n "Su tono de voz es seco, gélido, y aun en la penumbra, te parece ver sus ojos húmedos."

    else:

        show didacf_eyes 05
        show didacf_pupils front05
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Silentx06

        show an04_park_pimp_eyebrows angryx01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils front02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows angryx02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils front02
        show an04_park_pothead_mouth sad_Silentx03
        with dissolve

        p "..."

        p "¡Sé razonable!"

        show didacf_eyes 08
        show didacf_pupils front08
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07

        show an04_park_pimp_pupils left02

        show an04_park_pothead_pupils left02
        with dissolve

        p "¡Sabes que no estás bien!"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx07
        with dissolve

        d "¡Vete a casa idiota!"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx04

        show an04_park_pimp_pupils front02

        show an04_park_pothead_pupils front02
        with dissolve

        d "Ya tuviste tu oportunidad y la rechazaste."

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows angryx01
        show didacf_mouth happy_Talkingx02

        with dissolve

        d "Ahora estoy en muy buena compañía..."

        show didacf_eyes 04
        show didacf_pupils right04
        show didacf_eyebrows normal
        show didacf_mouth happy_Talkingx04

        show an04_park_pimp_eyebrows surprisex01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils left02
        show an04_park_pimp_mouth happy_Silentx03

        show an04_park_pothead_eyebrows surprisex01
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx01
        with dissolve

        d "¿Verdad, chicos?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx03

    show an04_park_pimp_eyebrows angryx02
    show an04_park_pimp_eyes 02
    show an04_park_pimp_pupils front02
    show an04_park_pimp_mouth sad_Talkingx04

    show an04_park_pothead_eyebrows angryx02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx02
    with dissolve

    chu "Ya has oído a la señorita..."

    show an04_park_pimp_eyebrows angryx03
    show an04_park_pimp_eyes 03
    show an04_park_pimp_pupils front03
    show an04_park_pimp_mouth sad_Talkingx05
    with dissolve

    chu "Lárgate, imbécil."

    show an04_park_pimp_eyebrows angryx01
    show an04_park_pimp_eyes 03
    show an04_park_pimp_pupils front03
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows angryx03
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Talkingx03
    with dissolve

    fum "O sino los tres te reventaremos a hostias."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04

    show an04_park_pimp_eyebrows normal
    show an04_park_pimp_eyes 00
    show an04_park_pimp_pupils front00
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows normal
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx03
    with dissolve

    p "Dirás los dos,"

    extend " uno lo tenéis ahí durmiendo la mona."

    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx03

    show an04_park_pimp_eyebrows surprisex01
    show an04_park_pimp_eyes 00
    show an04_park_pimp_pupils right00
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows surprisex02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils right02
    show an04_park_pothead_mouth sad_Silentx02
    with dissolve

    oku "{size=10}Zzzz...{/size}"

    play sound "audio/sfx/metal_knive01.ogg"

    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx02

    show an04_park_pimp_eyebrows angryx02
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Silentx03
    show an04_park_pimp_armR knife

    show an04_park_pothead_eyebrows surprisex01
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils left02
    show an04_park_pothead_mouth sad_Silentx01
    with dissolve

    pause

    n "Del bolsillo de su pantalón, el llamado \"Chulo\" saca una navaja plegable,"

    n "con la que muestra su maestría para intimidarte."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx03

    show an04_park_pimp_eyebrows angryx02
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Talkingx04
    with dissolve

    chu "Oye,"

    extend " pimpollo,"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02

    show an04_park_pimp_eyebrows angryx03
    show an04_park_pimp_eyes 05
    show an04_park_pimp_pupils front05
    show an04_park_pimp_mouth sad_Talkingx05

    show an04_park_pothead_eyebrows normal
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils left02
    show an04_park_pothead_mouth sad_Silentx03
    with dissolve

    chu "como no te largues de una vez,"

    extend " te vamos a abrir en canal..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03

    show an04_park_pimp_eyebrows angryx02
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Talkingx06
    with dissolve

    chu "¿Queda claro?"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx002

    show an04_park_pimp_eyebrows angryx03
    show an04_park_pimp_eyes 05
    show an04_park_pimp_pupils front05
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows angryx02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx03
    with dissolve

    d "Lárgate de aquí [protname],"

    extend " como puedes ver,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows suspiciousx02
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "estos me darán lo que tú no has querido darme."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    menu afternight04_Park_DidactobeFucked_Leave_question:
        
        pt "¡Si no saco a Dídac inmediatamente de aquí se pondrá en un follón mayor!"
        
        "<Irte a casa y que le den a Dídac>":
            
            call p_Help

            $ afternight04_Park_DidactobeFucked_Leave_DidacOKUPregnant = True #Te largas de la escena sin pelear, Dídac queda preñada.
            $ DidacOKUPregnant = True

            jump afternight04_Park_DidactobeFucked_Leave_Yes

        "<Enfrentarte a los capullos para sacar a Dídac de ahí>":

            call p_Help

            jump afternight04_Park_DidactobeFucked_Leave_No

label afternight04_Park_DidactobeFucked_Leave_Yes:

    #You decide to go home.

    p "¿Sabes qué?"

    play music "audio/music/kevinmacleod/happy_boy_end_theme.ogg" fadein 3.0 fadeout 3.0

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    # show didacfbodybelow naked:
    #     zoom 0.25 xanchor 0.2
    # show didacfbodybelow_panties park:
    #     zoom 0.25 xanchor 0.2
    show didacfbodytop park:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show didacfbodycloth_whole gabardine:
            zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 01:
        an04_park_didacf_left_expressions

    show didacf_eyes 03:
        an04_park_didacf_left_expressions

    show didacf_pupils front03:
        an04_park_didacf_left_expressions

    show didacf_eyebrows surprisex01:
        an04_park_didacf_left_expressions

    ##

    ###show didacf_aprove:
        ###zoom 0.25 xanchor 0.2 alpha 0.2

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Silentx02:
        an04_park_didacf_left_expressions

###

    ## POTHEAD

    show an04_park_pothead_body pants:
        zoom 0.5 xanchor -0.85
        
    show an04_park_pothead_eyes 02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_pupils front02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_eyebrows normal:
        an04_park_pothead_right_expressions
    show an04_park_pothead_mouth sad_Silentx02:
        an04_park_pothead_right_expressions

###
    ## PIMP

    show an04_park_pimp_armR knife:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_body pants:
        zoom 0.5 xanchor -0.3

    show an04_park_pimp_eyes 02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_pupils front02:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_eyebrows angryx01:
        an04_park_pimp_middle_expressions

    show an04_park_pimp_mouth sad_Silentx03:
        an04_park_pimp_middle_expressions

    with dissolve

    p "Paso de ti,"

    extend " y de tus \"amigos\"."

    p "Si quieres que te violen y te dejen preñada,"

    extend " es tu puto problema."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx04
    with dissolve

    p "No me vengas luego con lloros ni gilipolleces."

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == True:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows serious
        show didacf_mouth sad_Silentx05
        with dissolve

        p "Total,"

        extend " si te dejas follar sin condón..."

        p "¿Qué malo puede pasar?"

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx06

        show an04_park_pothead_eyebrows surprisex01
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx01

        show an04_park_pimp_eyebrows surprisex01
        show an04_park_pimp_pupils left02

        with dissolve

        p "¡¿Solo que te quedes preñada y nunca más vuelvas a ser el que eras?!"

        show didacf_eyes 05
        show didacf_pupils left05
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07
        with dissolve

        d "..."

        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "Eso no volverá a pasar."

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows angryx01
        show didacf_mouth sad_Silentx05

        show an04_park_pothead_pupils front02
        show an04_park_pimp_pupils front02

        with dissolve

        p "Iba a pasar hasta que os detuve,"

        p "si eres tan idiota como para creer que tienes la situación controlada,"

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows surprisex01
        show didacf_mouth sad_Silentx04

        show an04_park_pothead_pupils front02
        show an04_park_pimp_pupils front02

        with dissolve

        p "es que te has vuelto incluso más imbécil de lo que ya eras."

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09

        show an04_park_pothead_pupils left02
        show an04_park_pimp_pupils left02

        with dissolve

        d "¡Vete al carajo gilipollas!"

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx08
        with dissolve

        d "¡Siempre te has creído superior a mí simplemente porque eres más ordenado que yo!"

        show didacf_eyes 01
        show didacf_pupils front01
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07

        show an04_park_pothead_pupils front02
        show an04_park_pimp_pupils front02

        with dissolve

        p "Y porque el piso lo pago mayormente yo;"

        p "pero no es una cuestión de superioridad,"

        p "sino de \"responsabilidad\"."

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx08
        with dissolve

        p "No eres más que un crío malcriado,"

        extend " viviendo en el cuerpo de un adulto,"

        p "que además ahora tiene melones."

        show didacf_eyes 03
        show didacf_pupils left03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx09

        show an04_park_pimp_eyebrows suspiciousx02
        show an04_park_pimp_eyes 00
        show an04_park_pimp_pupils left00
        show an04_park_pimp_mouth sad_Talkingx04

        show an04_park_pothead_eyebrows surprisex02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx03
        with dissolve

        chu "¿Ahora tiene melones?"

        chu "¿De qué diablos está hablando?"

        show didacf_eyes 04
        show didacf_pupils left04
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx08

        show an04_park_pimp_eyebrows suspiciousx01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils right02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows suspiciousx02
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Talkingx03
        with dissolve

        fum "No parecen operados..."

        extend " ¿Verdad?"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx05

        show an04_park_pimp_eyebrows surprisex01
        show an04_park_pimp_eyes 02
        show an04_park_pimp_pupils left02
        show an04_park_pimp_mouth sad_Silentx03

        show an04_park_pothead_eyebrows surprisex01
        show an04_park_pothead_eyes 02
        show an04_park_pothead_pupils left02
        show an04_park_pothead_mouth sad_Silentx03
        with dissolve

        d "Lárgate ya,"

        d "¡o seré yo mismo el que te reviente a hostias!"

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx09

        show an04_park_pothead_pupils front02
        show an04_park_pimp_pupils front02

        with dissolve

        p "Solo espero que sepas lo que haces."

        show didacf_eyes 00
        show didacf_pupils front00
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Talkingx09
        with dissolve

        d "¡¡Lárgate!!"

    else:

        show didacf_eyes 03
        show didacf_pupils front03
        show didacf_eyebrows angryx03
        show didacf_mouth sad_Talkingx06
        with dissolve

        d "¿Te crees que tengo doce años?"

        d "¡¿o qué?!"

        show didacf_eyes 02
        show didacf_pupils front02
        show didacf_eyebrows angryx02
        show didacf_mouth sad_Talkingx05
        with dissolve

        d "Sé cuidarme..."

        show didacf_eyes 04
        show didacf_pupils front04
        show didacf_eyebrows angryx04
        show didacf_mouth sad_Silentx07
        with dissolve

        p "Lo que tú digas..."

    scene bg an04_park_fountain:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        ease_quad 12.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    n "Decides dejar a tu amigo a su suerte y volver al piso a esperar en la cama un nuevo día."

    play sound "audio/sfx/metal_keys_deposit.ogg"

    if music_play != "bittersweet":
        play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bittersweet"

    scene afternight03_bg_entrance_lightoff_night
    with fade
    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    pt "Él se lo ha buscado,"

    pt "desde luego siempre ha sido un poco capullo..."

    pt "Al fin y al cabo,"

    extend " si no vuelve a su estado original por quedar preñado..."

    pt "¿O sería preñada?"

    pt "¿Qué más da?"

    pt "Tener a una mujer como compañera de piso tampoco estaría tan mal..."

    pt "Aunque viendo qué compañías puede frecuentar,"

    pt "quizás sería mejor ir buscando otro compañero,"

    extend " u otro piso..."

    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0

    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene afternight03_bg_shower
    with fade

    n "Te aseas en el baño justo antes de acostarte y apagas las luces para reunirte con Morfeo."

    stop music fadeout 3.0
    $ renpy.music.set_volume(0.05, delay=5.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    pause

    play sound "audio/sfx/click_turnofflights.ogg"

    scene beds_night_lightOff_blindDown_DemptyMCbusy
    with Dissolve (1.0)

    $ renpy.music.set_volume(0.01, delay=5.0, channel='sfx1')

    stop music fadeout 5.0

    pause

    scene black
    with fade

    pause

    jump afternight04_NeusCallForDidac #NOT FINISHED, here you should know what could had happened to her...

label afternight04_Park_DidactobeFucked_Leave_No:

    #You decide to battle those bastards.

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03

    show an04_park_pimp_eyebrows angryx01
    show an04_park_pimp_eyes 02
    show an04_park_pimp_pupils front02
    show an04_park_pimp_mouth sad_Silentx03
    with dissolve

    p "Muy bien,"

    p "hasta aquí ha llegado la broma."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx04

    show an04_park_pimp_eyebrows angryx03
    show an04_park_pimp_eyes 04
    show an04_park_pimp_pupils front04
    show an04_park_pimp_mouth sad_Silentx03

    show an04_park_pothead_eyebrows angryx02
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx04
    with dissolve

    p "Te vienes conmigo por las buenas,"

    extend " o por las malas."

    p "Tú decides."

    scene bg an04_park_bank_far_closer_background_03:
        zoom 0.5

    show an04_park_pimp_body pants:
        subpixel True
        zoom 1.5 xanchor 0.23 yanchor 0.1

    ###show an04_park_pimp_body_prove:
        ###zoom 1.5 xanchor 0.23 yanchor 0.1 alpha 0.5


    play music "audio/music/alcaknight/bury_it.ogg" fadeout 0.2 fadein 0.1


    show an04_park_pimp_eyes 04:
        an04_park_pimp_middle_x2close_expressions
    show an04_park_pimp_pupils front04:
        an04_park_pimp_middle_x2close_expressions
    show an04_park_pimp_eyebrows angryx03:
        an04_park_pimp_middle_x2close_expressions
    show an04_park_pimp_mouth sad_Silentx03:
        an04_park_pimp_middle_x2close_expressions

    with Dissolve (2.0)

    n "El tipo al que llaman \"Chulo\" se acerca hasta llegar a escasos centímetros de ti con una expresión corporal que da honor a su apodo."

    show an04_park_pimp_eyebrows angryx04
    show an04_park_pimp_eyes 03
    show an04_park_pimp_pupils front03
    show an04_park_pimp_mouth sad_Talkingx06
    with dissolve

    chu "¿Es que no me has oído {b}Besugo{/b}?"

    show an04_park_pimp_eyebrows angryx04
    show an04_park_pimp_eyes 05
    show an04_park_pimp_pupils front05
    show an04_park_pimp_mouth sad_Silentx03
    with dissolve

    menu afternight04_Park_Battle_question:
        
        pt "Se cree que puede intimidarme al acercarse tanto..."
        
        "<Meterle una hostia>":
            
            call p_Help

            jump afternight04_Park_Battle_Punch

        "<Intentar razonar con el tipo>":

            call p_Help

            p "No lo entiendes..."

            p "¿Acaso no ves que la chica no está bien de la cabeza?"

            show an04_park_pimp_eyebrows angryx03
            show an04_park_pimp_eyes 05
            show an04_park_pimp_pupils front05
            show an04_park_pimp_mouth sad_Talkingx04
            with dissolve

            chu "El que no está bien de la cabeza eres tú, macho."

            show an04_park_pimp_eyebrows angryx03
            show an04_park_pimp_eyes 04
            show an04_park_pimp_pupils front04
            show an04_park_pimp_mouth sad_Silentx03
            with dissolve

            show an04_park_violence_pimp_threat:
                subpixel True
                alpha 1.0
                zoom 0.25 xanchor 0.0 yanchor -0.5 #Far
                easein_quad 1.0 zoom 0.7 xanchor 0.15 yanchor 0.15 alpha 0.0 #Super Close

            show an04_park_violence_pimp_threat_blur:
                subpixel True
                alpha 0.0
                zoom 0.25 xanchor 0.0 yanchor -0.5 #Far
                easein_quad 1.0 zoom 0.7 xanchor 0.15 yanchor 0.15 alpha 1.0 #Super Close
            with dissolve

            n "Acerca el cuchillo hasta tu garganta."

            show an04_park_pimp_eyebrows angryx03
            show an04_park_pimp_eyes 03
            show an04_park_pimp_pupils front03
            show an04_park_pimp_mouth sad_Talkingx05
            with dissolve

            chu "Te lo diré por última vez."

            chu "Lárgate o te rajo el pescuezo."

            show an04_park_pimp_eyebrows angryx03
            show an04_park_pimp_eyes 04
            show an04_park_pimp_pupils front04
            show an04_park_pimp_mouth sad_Silentx03
            with dissolve

            pt "Este tipo tiene pinta de ser de escuela pija,"

            pt "por su forma de vestir y de hablar..."

            pt "dudo que haya usado alguna vez este cuchillo contra alguien,"

            pt "más allá de la simple intimidación..."

            show an04_park_pimp_eyebrows angryx04
            show an04_park_pimp_eyes 05
            show an04_park_pimp_pupils front05
            show an04_park_pimp_mouth sad_Silentx03
            with dissolve

            pt "Se le ve gallito,"

            extend " pero no asesino."

            menu afternight04_Park_Battle02_question:
                
                pt "Aunque si me equivoco..."
                
                "<Meterle una hostia>":
                    
                    call p_Help

                    jump afternight04_Park_Battle_Punch

                "<Volver a casa>":

                    call p_Help

                    jump afternight04_Park_DidactobeFucked_Leave_Yes

label afternight04_Park_Battle_Punch:

    scene hit 15:
        truecenter
        zoom 1.5 rotate 90 ypos 0.25
    pause 0.05
    show hit 16
    pause 0.05
    show hit 17
    pause 0.05
    show hit 21
    pause 0.05
    show hit 22
    pause 0.05
    show hit 23
    pause 0.05

    play sound "audio/sfx/punch01.ogg"

    scene bg an04_park_bank_far_closer_background_03:
        zoom 0.5

    show an04_park_violence_pimp_punchface_body:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.5 xanchor 0.0 yanchor 0.0 # Middle Step
        easein_quad 10.0 zoom 0.4 xanchor 0.0 yanchor 0.0 # Final Step

    show an04_park_violence_pimp_punchface_hand:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.4 xanchor 0.0 yanchor 0.0 # Middle Step
        easein_quad 10.0 zoom 0.5 xanchor 0.0 yanchor 0.0 # Final Step

    show an04_park_violence_pimp_punchface_spit:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.4 xanchor -0.1 yanchor -0.05 # Middle Step
        easein_quad 10.0 zoom 0.7 xanchor 0.17 yanchor 0.2 # Final Step

    with hpunch

    ono "{size=30}PAM{/size}"

    n "Con un derechazo directo a su mandíbula,"

    n "el chico cae en redondo al suelo perdiendo de vista el cuchillo,"

    n "que sale disparado hacia la oscura espesura del césped."

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    # show didacfbodybelow naked:
    #     zoom 0.25 xanchor 0.2
    # show didacfbodybelow_panties park:
    #     zoom 0.25 xanchor 0.2
    show didacfbodytop park:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show didacfbodycloth_whole gabardine:
            zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 02:
        an04_park_didacf_left_expressions

    show didacf_eyes 00:
        an04_park_didacf_left_expressions

    show didacf_pupils front00:
        an04_park_didacf_left_expressions

    show didacf_eyebrows angryx02:
        an04_park_didacf_left_expressions

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Talkingx004:
        an04_park_didacf_left_expressions

###

    ## POTHEAD

    show an04_park_pothead_body pants:
        zoom 0.5 xanchor -0.85
    show an04_park_pothead_eyes 02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_pupils front02:
        an04_park_pothead_right_expressions
    show an04_park_pothead_eyebrows angryx04:
        an04_park_pothead_right_expressions
    show an04_park_pothead_mouth sad_Silentx06:
        an04_park_pothead_right_expressions

    with dissolve

    d "[protname]..."

    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx06

    show an04_park_pothead_eyebrows angryx04
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Talkingx03
    with dissolve

    fum "¡La madre que te parió!"

    show an04_park_pothead_eyebrows angryx04
    show an04_park_pothead_eyes 02
    show an04_park_pothead_pupils front02
    show an04_park_pothead_mouth sad_Silentx05
    with dissolve

    n "Mientras el del cuchillo sigue recuperándose del duro golpe,"

    scene bg an04_park_bank_far_closer_background_03:
        zoom 0.5

    show an04_park_violence_pothead_before_punch 01:
        subpixel True
        zoom 0.25 xanchor -0.3 yanchor 0.0 # Begin
        easein_quad 10.0 zoom 0.8 xanchor 0.18 yanchor 0.25 # Final Pose

    show an04_park_violence_pothead_before_face:
        subpixel True
        zoom 0.4 xanchor 0.0 yanchor 0.0 # Begin
        easein_quad 10.0 zoom 0.6 xanchor 0.15 yanchor 0.1 # Final Pose

    n "el otro con un trote torpe e iracundo llega a escasos centímetros de ti con el puño en el aire dispuesto a partirte la cara."

    menu afternight04_Park_Battle_Punch01_question:
        
        pt "Parece que es diestro..."
        
        "<Esquivar a la izquierda>":
            
            call p_Help

            $ afternight04_Park_Battle_Punch_GetBackHomewithDidac_Cond = True #You get back home with Didac after a fight.

            $pl.ch_pts("dp",3)

            jump afternight04_Park_Battle_Punch01_GetBackHomewithDidac

        "<Esquivar a la derecha>":

            call p_Help

            scene bg an04_park_bank_far_closer_background_03:
                zoom 0.5

            show an04_park_violence_pothead_aftersuccess:
                subpixel True
                zoom 0.2 xanchor -0.45 yanchor -0.45 # Punch Far
                easeout_quad 0.5 zoom 0.5 xanchor 0.15 yanchor 0.15 #Al Screen
                easein_quad 0.5 zoom 1.5 xanchor 0.4 yanchor 0.4 # Really Close

            show border_lines 03:
                subpixel True
                zoom 0.25 xanchor 0.0 yanchor 0.0 #FullScreen
                easeout_quad 0.5 zoom 1.0 xanchor 0.375 yanchor 0.375 # Big
                easein_quad 0.5 zoom 0.5 xanchor 0.25 yanchor 0.25 # Middle
                ease_quad 5.0 zoom 1.0 xanchor 0.375 yanchor 0.375 # Big


            with hpunch

            pause 0.5

            scene hit_15
            pause 0.05
            scene hit_16
            pause 0.05
            scene hit_17
            pause 0.05
            scene hit_21
            pause 0.05
            scene hit_22
            pause 0.05
            scene hit_23
            pause 0.05

            play sound "audio/sfx/punch01.ogg"

            scene black
            with fade

            n "Recibes un fuerte derechazo en tu mejilla izquierda que te deja unos segundos extraviado."

            scene bg an04_park_bank_far_closer_background_03:
                zoom 0.5

            show an04_park_violence_pothead_before_punch 01:
                subpixel True
                zoom 0.25 xanchor -0.3 yanchor 0.0 xzoom -1.0 # Begin
                easein_quad 10.0 zoom 0.8 xanchor 0.18 yanchor 0.25 # Final Pose

            show an04_park_violence_pothead_before_face:
                subpixel True
                zoom 0.4 xanchor 0.0 yanchor 0.0  xzoom -1.0 # Begin
                easein_quad 10.0 zoom 0.6 xanchor 0.15 yanchor 0.1 # Final Pose

            show black:
                subpixel True
                alpha 0.0

                block:
                    ease 0.5 alpha 0.0
                    ease 1.0 alpha 0.5
                    ease 0.5 alpha 0.2
                    ease 0.5 alpha 0.6
                    ease 1.0 alpha 1.0
                    ease 0.5 alpha 0.0
                    ease 1.0 alpha 0.2
                    ease 0.5 alpha 0.5
                    ease 0.5 alpha 0.0
                    ease 0.5 alpha 0.2
                    repeat
            with dissolve

            n "Con la vista aún borrosa, percibes levemente cómo el chico va a darte un segundo golpe con el otro puño."

            menu afternight04_Park_Battle_Punch02_question:
                
                pt "Si recibo otro golpe, creo que voy a perder el conocimiento."
                
                "<Esquivar a la izquierda>":
                    
                    call p_Help

                    $ afternight04_Park_Battle_Punch_NotGetBackHomewithDidac_Cond = True #You don´t get back home with Didac, They changed place.

                    scene bg an04_park_bank_far_closer_background_03:
                        zoom 0.5

                    show an04_park_violence_pothead_aftersuccess:
                        subpixel True
                        zoom 0.2 xanchor -0.45 yanchor -0.45 xzoom -1.0 # Punch Far
                        easeout_quad 0.5 zoom 0.5 xanchor 0.15 yanchor 0.15 #Al Screen
                        easein_quad 0.5 zoom 1.5 xanchor 0.4 yanchor 0.4 # Really Close

                    show border_lines 03:
                        subpixel True
                        zoom 0.25 xanchor 0.0 yanchor 0.0 #FullScreen
                        easeout_quad 0.5 zoom 1.0 xanchor 0.375 yanchor 0.375 # Big
                        easein_quad 0.5 zoom 0.5 xanchor 0.25 yanchor 0.25 # Middle
                        ease_quad 5.0 zoom 1.0 xanchor 0.375 yanchor 0.375 # Big

                    with hpunch

                    pause 0.5

                    scene hit_15
                    pause 0.05
                    scene hit_16
                    pause 0.05
                    scene hit_17
                    pause 0.05
                    scene hit_21
                    pause 0.05
                    scene hit_22
                    pause 0.05
                    scene hit_23
                    pause 0.05

                    play sound "audio/sfx/punch01.ogg"

                    stop music fadeout 3.0

                    scene black
                    with fade

                    pause

                    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
                    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

                    p "Mierda..."

                    extend " la cabeza me da vueltas..."

                    n "El sonido de los grillos,"

                    n "junto con el motor de algunas motocicletas, inunda la quietud del lugar."

                    p "¿Dónde están...?"

                    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
                    $ renpy.music.set_volume(0.2, delay=3.0, channel='sfx1')

                    scene bg_an04_park_bank_far_closer_background_bur:
                        zoom 0.5

                        contains:
                            "bg an04_park_bank_far_closer_background_03"

                        contains:
                            "bg an04_park_bank_far_closer_background_02"
                            subpixel True
                            alpha 0.0
                            easein_quad 8.0 alpha 1.0

                        contains:
                            "bg an04_park_bank_far_closer_background_01"
                            subpixel True
                            alpha 0.0
                            pause 10.0
                            ease_quad 20.0 alpha 1.0

                    show black:
                        subpixel True
                        alpha 0.0

                        block:
                            ease 1.0 alpha 0.0
                            ease 2.0 alpha 0.5
                            ease 1.0 alpha 0.2
                            ease 1.0 alpha 0.6
                            ease 3.0 alpha 1.0
                            ease 1.0 alpha 0.0
                            ease 1.0 alpha 0.2
                            ease 3.0 alpha 0.5
                            ease 2.0 alpha 0.0
                            ease 1.0 alpha 0.2
                            repeat
                    with Dissolve (1.0)

                    n "Diriges tu mirada al banco donde previamente estaban Dídac y los demás con las mochilas -y las botellas- por el suelo,"

                    n "pero lo encuentras completamente vacío y en silencio."

                    n "Vuelves tus ojos al reloj que tienes en la muñeca."

                    p "Joder..."

                    extend " ha pasado casi una hora..."

                    p "Huuhh..." # Grunt

                    p "Qué puto dolor de cabeza..."

                    n "Te acercas los dedos a la nariz al sentir algo extraño en esa zona,"

                    n "y descubres sangre reseca cerca de tus labios."

                    p "Debo de estar hecho un cromo..."

                    p "Bah..." # Sigh

                    p "Maldito imbécil..."

                    p "¡¿A dónde coño has ido?!"

                    p "¡Me has dejado aquí tirado en el suelo,"

                    p "y te has largado con esos tres desconocidos a follar!"

                    p "¿¡Mientras yo me desangraba aquí!?"

                    p "¡Por mí te puedes pudrir!"

                    scene bg an04_park_bank_far_closer_background_01:
                        zoom 0.5
                    with dissolve

                    n "Te levantas tan dignamente como te es posible,"

                    n "a pesar de que no hay público alguno que te juzgue,"

                    n "y te diriges hasta la valla más cercana,"

                    n "observando que nadie te esté echando el ojo para poder saltar impunemente."

                    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
                    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0 

                    scene afternight03_bg entrance_lightoff_night
                    with fade

                    n "Dentro de tus posibilidades logras llegar al piso de una pieza,"

                    play sound "audio/sfx/metal_keys_deposit.ogg"

                    show afternight03_bg_entrance_keysmc lightoff_night:
                        afternight03_bg_entrance_keys
                    with dissolve

                    n "justo después de dejar las llaves en la mesita de entrada,"

                    scene beds_night_lightOff_blindUp_DemptyMCempty
                    with fade

                    n "abres la puerta de la habitación con la esperanza de encontrarte a Dídac ahí durmiendo."

                    p "Eres un imbécil integral."

                    n "Después de comprobar que se trataban de falsas esperanzas, te diriges al baño para ducharte y asearte,"

                    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
                    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

                    scene afternight03_bg_shower
                    with fade

                    stop music fadeout 3.0
                    $ renpy.music.set_volume(0.05, delay=5.0, channel='sfx1')
                    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

                    n "para poco después volver a tu habitación a reunirte con Morfeo."

                    scene beds_night_lightOff_blindUp_DemptyMCempty
                    with fade

                    scene beds_night_lightOff_blindDown_DemptyMCbusy
                    with Dissolve (2.0)

                    p "Espero que tengas cuatrillizos,"

                    extend " hijo de puta..."

                    stop music fadeout 5.0

                    scene black
                    with fade

                    jump afternight04_NeusCallForDidac

                "<Esquivar a la derecha>":

                    call p_Help

                    $ an04_Park_Battle_Punch_pothead_otherpunch = True

                    $ afternight04_Park_Battle_Punch_GetBackHomewithDidac_Cond = True #You get back home with Didac after a fight.

                    $pl.ch_pts("dp",3)

                    jump afternight04_Park_Battle_Punch01_GetBackHomewithDidac

label afternight04_Park_Battle_Punch01_GetBackHomewithDidac:

    if an04_Park_Battle_Punch_pothead_otherpunch == False:

        scene bg an04_park_bank_far_closer_background_03:
            zoom 0.5

        show an04_park_violence_pothead_afterfail:
            subpixel True
            zoom 0.4 xanchor 0.05 yanchor 0.05 #Initial Pose
            easein_quad 5.0 zoom 0.7 xanchor 0.0 yanchor 0.0 #Final Pose.
        with dissolve

    else:

        scene bg an04_park_bank_far_closer_background_03:
            zoom 0.5

        show an04_park_violence_pothead_afterfail:
            subpixel True
            zoom 0.4 xanchor 0.0 yanchor 0.05 xzoom -1.0 #Initial Pose
            easein_quad 5.0 zoom 0.7 xanchor 0.5 yanchor 0.0 xzoom-1.0 #Final Pose.
        with dissolve

    play sound "audio/sfx/zas01.ogg"

    n "El ruido de su puño cortando el aire a escasos centímetros no te deja indiferente."

    n "Aun así, aprovechas su desconcierto para propinarle un buen golpe de puño en medio de la cara,"

    play sound "audio/sfx/punch01.ogg"

    scene bg an04_park_bank_far_closer_background_03:
        zoom 0.5

    show an04_park_violence_pothead_punchface_body:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.5 xanchor 0.0 yanchor 0.0 # Middle Step
        easein_quad 10.0 zoom 0.4 xanchor 0.0 yanchor 0.0 # Final Step

    show an04_park_violence_pothead_punchface_hand:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.4 xanchor 0.0 yanchor 0.0 # Middle Step
        easein_quad 10.0 zoom 0.5 xanchor 0.0 yanchor 0.0 # Final Step

    show an04_park_violence_pimp_punchface_spit:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.4 xanchor -0.1 yanchor -0.05 # Middle Step
        easein_quad 10.0 zoom 0.7 xanchor 0.17 yanchor 0.2 # Final Step

    show an04_park_violence_pothead_punchface_blood:
        subpixel True
        zoom 2.0 xanchor 0.3 yanchor 0.18 #Original pose
        easeout_quad 0.5 zoom 0.4 xanchor -0.1 yanchor -0.05 # Middle Step
        easein_quad 10.0 zoom 0.7 xanchor 0.17 yanchor 0.2 # Final Step

    with hpunch

    n "sintiendo en tus nudillos la fractura de su nariz,"

    n "para poco después, ver cómo cae en redondo al suelo con todo su rostro ensangrentado."

    if music_play != "torn_apart":
        play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "torn_apart"

    scene bg an04_park_bank_far_closer_background_03:
        zoom 0.5
    show an04_park_violence_pimp_afterpunch_body pants:
        truecenter
        zoom 0.5
    show an04_park_violence_pimp_afterpunch_mouth sad_Talking:
        truecenter
        zoom 0.5
    show an04_park_violence_pimp_afterpunch_pupils front:
        truecenter
        zoom 0.5
    with fade

    chu "¡Hijo de puta!"

    chu "¡Le has roto la nariz!"

    show an04_park_violence_pimp_afterpunch_mouth sad_Silent
    with dissolve

    p "Os lo advertí."

    show an04_park_violence_pimp_afterpunch_mouth sad_Talking
    with dissolve

    chu "¡Te vamos a matar!"

    show an04_park_violence_pimp_afterpunch_mouth sad_Silent
    with dissolve

    p "Tú,"

    extend " ¿y cuántos más?"

    show an04_park_violence_pimp_afterpunch_pupils right
    with dissolve

    n "El chico, aún tendido en el suelo, y con la mano en la mejilla por el dolor del puñetazo, mira a su alrededor."

    show an04_park_violence_pimp_afterpunch_pupils left
    with dissolve

    n "Dídac está inmóvil sin saber cómo reaccionar ante la situación."

    n "El llamado \"Okupa\" sigue durmiendo la mona,"

    n "y aunque consiguiera despertarse, sabe que tampoco sería de mucha ayuda."

    show an04_park_violence_pimp_afterpunch_pupils right
    with dissolve

    n "El \"Fumetas\" sigue inconsciente con la cara hecha un cuadro abstracto de color rojizo."

    show an04_park_violence_pimp_afterpunch_pupils leftdown
    with dissolve

    n "Luego, su mirada se dirige hacia donde -en teoría- salió disparada su navaja plegable,"

    n "pero de noche y con tanta hierba, es evidente que le resultaría imposible encontrarla a tiempo."

    show an04_park_violence_pimp_afterpunch_pupils front
    with dissolve

    p "Sin el pincho no eres tan valiente,"

    extend " ¿verdad?"

    show an04_park_violence_pimp_afterpunch_pupils right
    with dissolve

    chu "..."

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    # show didacfbodybelow naked:
    #     zoom 0.25 xanchor 0.2
    # show didacfbodybelow_panties park:
    #     zoom 0.25 xanchor 0.2
    show didacfbodytop park:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    if afternight04_Park_DidacFuckAnal_WithoutCondomDanger_Cond == False:

        show didacfbodycloth_whole gabardine:
            zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 01:
        an04_park_didacf_left_expressions

    show didacf_eyes 05:
        an04_park_didacf_left_expressions

    show didacf_pupils front05:
        an04_park_didacf_left_expressions

    show didacf_eyebrows angryx03:
        an04_park_didacf_left_expressions

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Silentx07:
        an04_park_didacf_left_expressions

    with fade

###

    n "Te alejas del tipejo a paso seguro llegando cerca de donde está Dídac."

    p "¿Nos vamos?"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "No podías dejarme en paz..."

    extend " ¿verdad?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx08
    with dissolve

    p "No."

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx09
    with dissolve

    p "No estás bien, Dídac."

    p "Lo que estás haciendo no es normal..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡Claro que no es normal!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with dissolve

    d "¡¿Por qué te crees que te pedí ayuda?!"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx09
    with dissolve

    p "Piensa con lógica,"

    p "¡me pediste que te follara!"

    p "Tú hubieras hecho lo mismo."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "No,"

    extend " yo te hubiera ayudado..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx06
    with dissolve

    p "¿Y qué crees que estoy haciendo aquí?"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx06
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Recoges su ropa del suelo y se la das."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Ponte esto y salgamos de aquí cuanto antes."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve

    d "..."

    show didacfbodycloth_whole gabardine:
        zoom 0.25 xanchor 0.2
    with dissolve

    n "Dídac acepta a regañadientes después de ver el panorama,"

    n "y ambos volvéis a saltar la valla para dirigiros a casa."

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    play sound "audio/sfx/metal_keys_deposit.ogg"

    if music_play != "didac_theme":
        play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "didac_theme"

    scene afternight03_bg_entrance_lightoff_night
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with fade
    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "Apenas te da tiempo a dejar las llaves sobre la mesita de la entrada,"

    play sound "audio/sfx/door_slam01.ogg"

    show empty
    with hpunch

    n "y Dídac entra en el baño dando un portazo."

    pt "Parece que sigue sin estar del todo contento..."

    pt "Solo espero que no se vaya durante la noche mientras duermo..."

    pt "¿Debería atarlo?"

    pt "Eso quizás sería excesivo..."

    pt "creo que en el fondo sigue siendo razonable cuando recapacita,"

    pt "y su riego sanguíneo no va por ahí abajo..."

    pt "Pero es como si estuviera teniendo el síndrome de abstinencia,"

    extend " y su droga fuera el sexo,"

    pt "con un mono muy fuerte por lo visto..."

    n "Esperas pacientemente que termine su ducha,"

    $ renpy.music.set_volume(0.8, delay=3.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/shower01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene afternight03_bg_shower
    with fade

    n "para luego ser tú quien usa el baño."

    stop music fadeout 3.0
    $ renpy.music.set_volume(0.05, delay=5.0, channel='sfx1')
    $ renpy.music.play("audio/sfx/cricket_sounds01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    stop music fadeout 3.0

    scene beds_night_lightOff_blindUp_Dbusy02MCempty
    show beds_D02_night_lightOff_blindUp
    with fade

    pt "Parece que ha conseguido calmarse."

    scene beds_night_lightOff_blindUp_Dbusy02MCbusy
    show beds_D02_night_lightOff_blindUp
    with Dissolve (1.5)

    n "Decides tomar su ejemplo,"

    scene black
    with Dissolve (3.0)

    pt "y esperar a mañana a ver si todo va mejor..."

    

    

    jump morning05


label afternight04_Park_DidacFuckAnal_No:

    #You decide to stop this madness. helping her to be raped in the ass. She accepts it not being really happy about it.

    jump afternight04_Park_DidactobeFucked_No



label afternight04_Park_DidacFuckWithoutCondom_No:

    #n "Observas como el chico hace un gesto brusco con la mano en la que sujeta el condón."

    #ono "TOC"

    #n "Acto seguido oyes el ruido de un pequeño objeto cayendo cerca de dónde estás."

    #pt "¡Ha tirado el condón!"

    #pt "¡La madre que lo parió! ¡Se va a follar a Dídac a pelo!"

    #pt "¡Tengo que parar esto antes de que pueda correrse dentro o será demasiado tarde!"

    # Detienes a Okupa de correrse dentro del coño de Dídac y sacándolo de ahí sin demasiada resistencia y Dídac al final agradeciéndotelo.

    show an04_park_bank_far_bush empty
    with dissolve

    n "Sales de tu escondite mientras los observas."

    oku "Jodéee..."

    extend " Su culo sigue echando lefa..."

    oku "Que ascoohh..."

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    d "¡Me follas ya!"

    extend " ¡¿O qué?!"

    show an04_park_bank_fucking4_didac_head right
    with dissolve

    oku "A tomáaa por culooh..."

    # Didac
    #hide an04_park_bank_fucking4_didac_armR
    #hide an04_park_bank_fucking4_didac_head
    # squatter
    hide an04_park_bank_fucking4_squatter_body
    hide an04_park_bank_fucking4_didac_body
    hide an04_park_bank_fucking4_didac_legs
    
    # didac ass
    hide an04_park_bank_fucking4_didac_ass

    hide an04_park_bank_fucking4_didac_skirt
    # squatter hand
    hide an04_park_bank_fucking4_squatter_arm 01

    show an04_park_bank_fucking4_didac_head down

    show an04_park_bank_fucking4_comp 02
    with dissolve

    d "Aaaaahhh..." #*moan*

    d "Síii..."

    extend " esto ya es otra cosa..."

    hide an04_park_bank_fucking4_comp

    # Didac

    show an04_park_bank_fucking4_didac_armR back:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_head down:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_squatter_body 01:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_body:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_legs:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_didac_ass:
        truecenter
        xpos 0.81 ypos 0.434 

    show an04_park_bank_fucking4_didac_skirt:
        an04_park_bank_fucking4_pos
    show an04_park_bank_fucking4_squatter_arm 01:
        an04_park_bank_fucking4_pos
    with dissolve

    p "¡Dídac!"

    play sound "audio/sfx/meme_surprise02.ogg"
    stop music fadeout 0.5
    $ music_play = ""

    show an04_park_bank_fucking4_squatter_body 01_camera
    show an04_park_bank_fucking4_didac_head camera_surprise

    show an04_park_bank_pimp_01_head front
    show an04_park_bank_pothead_ground_head camera
    with dissolve

    n "Todos se paralizan al instante al oír esa voz."

    d "¿[protname]?"

    d "¡¿Eres tú...?!"

    play music "audio/music/didac_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "didac_theme"

    show an04_park_bank_fucking4_didac_head camera_angry
    with dissolve

    d "¿Qué...?"

    extend " ¡¿Qué coño estás haciendo aquí?!"

    p "Eso me pregunto yo..."

    p "Sabía que ibas cachondo,"

    p "pero nunca me hubiera imaginado,"

    p "que llegarías a querer quedarte preñado de este subproducto de la sociedad..."

    # Didac eyebrows angry.

    d "¡Idiota!"

    extend " ¡¿Te crees que soy imbécil?!"

    show an04_park_bank_pimp_01_head right
    show an04_park_bank_pothead_ground_head left
    with dissolve

    d "¡Me está follando con un condón!"

    d "¡El que tú no quisiste usar!"

    show an04_park_bank_pimp_01_head front
    show an04_park_bank_pothead_ground_head camera
    with dissolve

    p "¿Te refieres a este?"

    n "Le muestras el condón que previamente habías recogido del suelo, sucio de arena."

    show an04_park_bank_fucking4_didac_head camera_surprise
    with dissolve

    d "¿Qué...?"

    n "El \"Okupa\" seguía sin inmutarse, solo observaba esa situación como quien observa una nube."

    n "Los otros dos miraban la escena sin preocuparse demasiado,"

    n "al fin y al cabo, ellos ya habían quedado satisfechos."

    p "Supongo que no estarás acostumbrado a tu nuevo atributo femenino,"

    p "pero me imagino que la sensación de tener una polla con condón,"

    p "o sin él,"

    p "se debería de notar..."

    d "¿De qué estás...?"

    show an04_park_bank_fucking4_didac_head right_b
    with dissolve

    n "Su mirada se fija entonces en el sujeto pestilente."

    d "¡Oye capullo!"

    show an04_park_bank_pimp_01_head right
    show an04_park_bank_pothead_ground_head left

    show an04_park_bank_fucking4_squatter_body 01_left
    with dissolve

    d "Te has puesto el condón..."

    d "¡¿Verdad?!"

    show an04_park_bank_fucking4_squatter_body 01
    with dissolve

    oku "Yaaa te he dixooo que no me van las goooomas..."

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    show didacfbodytop park_dirt_01:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    show didacfbodycloth_whole empty:
        zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 01:
        an04_park_didacf_left_expressions

    show didacf_eyes 02:
        an04_park_didacf_left_expressions

    show didacf_pupils right02:
        an04_park_didacf_left_expressions

    show didacf_eyebrows angryx02:
        an04_park_didacf_left_expressions

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Silentx04:
        an04_park_didacf_left_expressions
    with Dissolve (1.0)


    n "Dídac aparta rápidamente su cuerpo de ese enfermizo drogadicto"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve

    n "y ve con sus propios ojos que efectivamente su polla está desnuda."

    show didacf_eyes 01
    show didacf_pupils down01
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx02
    with dissolve

    d "..."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Si quieres, puedes continuar..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx08
    with dissolve

    p "Creo que tendrías unos hijos encantadores con este tipo..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "Encima no te cachondees imbécil..."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx08
    with dissolve

    p "¡¿Que no me cachondee?!"

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve

    p "¡Si no llego a estar aquí!"

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx06
    with dissolve

    p "¡¿Qué cojones habría pasado?!"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx08
    with dissolve

    d "..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows suspiciousx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Ya te dije lo que te pasaría si te quedabas encinta..."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡Sí!"

    extend " ¡Me lo dejaste muy claro!"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡Lo que no me contaste es qué cojones es lo que me sucedió para que me haya pasado esto!"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx07
    with dissolve

    p "¿Cómo que no?"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx05
    with dissolve

    d "¡Pues como que no!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx07
    with dissolve

    d "¡Sigo sin saber qué cojones hago con este cuerpo!"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx08
    with dissolve

    d "¡Con esta puta obsesión por tu puta polla!"

    show didacf_eyes 04
    show didacf_pupils down04
    show didacf_eyebrows sadx04
    show didacf_mouth sadbiting_Silentx06
    with dissolve

    p "..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve

    p  "Dídac..."

    extend " fuiste tú el que..."

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx01
    with dissolve

    play sound "audio/sfx/door_old_open01_otherroom.ogg"
    ono "{size=12}Riiick{/size}"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Un chirrido metálico a la lejanía os deja a todos los presentes en estado de alerta,"

    n "a excepción de uno."

    show didacf_eyes 00
    show didacf_pupils right00
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    oku "Entonces..."

    extend " ¿qué...?"

    
    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Silentx03

    show an04_park_squatter_body:
        transform_anchor True
        xalign 0.34 yalign 0.46 zoom 0.5
        xpos 0.9 ypos 0.54

    show an04_park_squatter_exp_mouth Talkingx03:
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 0.5
        xpos 0.9 ypos 0.54
    with Dissolve(0.5)


    oku "Seguimos follaaaandooo..."

    extend " ¿O nooo...?"

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx04

    show an04_park_squatter_body:
        transform_anchor True
        xalign 0.34 yalign 0.46 zoom 0.5
        xpos 0.8 ypos 0.54

    show an04_park_squatter_exp_mouth Silentx03:
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 0.5
        xpos 0.8 ypos 0.54
    with Dissolve(0.5)

    n "Los dos que están en el banco empiezan a recoger las botellas -que aún contienen algo de alcohol- en las mochilas,"

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve

    n "mientras acaban de vestirse rápidamente."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx02
    with dissolve

    p "Dídac..."

    show didacf_eyes 03
    show didacf_pupils left03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Talkingx04
    with dissolve

    d "Sí..."

    extend " yo también lo he oído."

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    n "Agarras rápidamente su gabardina del suelo."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx01
    with dissolve

    p "Vístete,"

    extend " ¡rápido!"

    show didacfbodycloth_whole gabardine

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    n "Sin necesidad de que le des ninguna otra directriz, consigue vestirse en tiempo récord."

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows normal
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    n "Apenas le ha dado tiempo a ajustar el nudo del cinturón,"

    scene bg an04_park_bank_far_closer_background_01:
        zoom 0.5
    show an04_park_bank_bg_bank_cum 03:
        #xanchor -1.135 yanchor -0.75 zoom 0.4
        xanchor -0.176 yanchor 0.005

    show an04_park_squatter_body:
        transform_anchor True
        xalign 0.34 yalign 0.46 zoom 0.5
        xpos 0.8 ypos 0.54

    show an04_park_squatter_exp_mouth Silentx01:
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 0.5
        xpos 0.8 ypos 0.54

    with Dissolve(0.5)

    n "que ambos empezáis a correr para salir de ahí por patas,"

    n "al igual que hicieron previamente los otros dos individuos."

    show an04_park_squatter_body:
        xpos 0.7
    show an04_park_squatter_exp_mouth Silentx01:
        xpos 0.7
    with dissolve

    oku "..."

    show an04_park_squatter_body:
        xpos 0.6
    show an04_park_squatter_exp_mouth Talkingx002:
        xpos 0.6
    with dissolve

    oku "¡Eyyyy...!"

    show an04_park_squatter_body:
        xpos 0.5
    show an04_park_squatter_exp_mouth Talkingx03:
        xpos 0.5
    with dissolve

    oku "¿Me la vas a dejar así de duraaa...?"

    show an04_park_squatter_exp_mouth Silentx02
    with dissolve

    oku "..."

    show light 01 zorder 98:
        additive 1.0
        truecenter
        rotate -90

    with dissolve

    #n "Un foco cegador te nubla completamente la vista."

    s "¡¿Quién anda ahí?!"

    show an04_park_squatter_exp_mouth Talkingx01
    with dissolve

    oku "Mierda..."

    show an04_park_squatter_exp_mouth Silentx03
    with dissolve

    window hide dissolve
    pause

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)

    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "torn_apart"

    scene bg an04_placasantagustivell_composition 04:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        ease 30.0 xanchor 1.0 yanchor 0.7 zoom 1.0
    with fade

    n "Apenas habéis cruzado unas calles, empezáis a aminorar el paso, relajando la acción trepidante llevada a cabo,"

    n "pero el silencio entre vosotros sigue siendo tan frío como el invierno en {a=https://es.wikipedia.org/wiki/Oimiakón}Oimiakón{/a}."

    n "En ese estado enmudecido, seguís andando pesadamente,"

    n "mientras Dídac no deja de agarrarse los hombros protegiendo de forma casi enfermiza su cuerpo,"

    scene bg an04_flat_gate_composition002:
        subpixel True
        zoom 0.5 xanchor 0.0 yanchor 1.4 #General view door.
        ease 50.0 zoom 1.0 xanchor 0.0 yanchor 0.0
    with fade

    n "hasta llegar a vuestro bloque de pisos."

    n "Por suerte, Dídac ha adoptado la postura americana de estar cara a la puerta,"

    n "ahorrándoos así la incomodidad de entrecruzaros la mirada en ese espacio tan reducido."

    n "Aun así, te da la sensación de que no está mirando a ningún lugar en concreto,"

    $ saturation_tint_level = "superdark"

    n "más bien como si tuviera la vista perdida."

    scene afternight03_bg_entrance_lightoff_night
    with fade

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lightoff_night:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lightoff_night:
        afternight03_bg_entrance_keys
    with dissolve

    n "Poco después de entrar al piso,"

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little

    ###  DIDAC
    
    show didacfbodytop park_dirt_01:
        dfbody_center
    show didacfhandl hip_naked:
        dfbody_center
    show didacfhandr leg_naked:
        dfbody_center

    show didacfbodycloth_whole gabardine_dirt_01:
        dfbody_center

    #  D expressions

    show didacf_blush 03:
        dexpressions_center

    show didacf_eyes 05:
        dexpressions_center

    show didacf_pupils right05:
        dexpressions_center

    show didacf_eyebrows sadx03:
        dexpressions_center

    # Hair

    show didacfbodytop_hair:
        dfbody_center

    show didacf_mouth sad_Silentx05:
        dexpressions_center
    with fade

    n "y llegar a la sala de estar..."

    play sound "audio/sfx/click_turnofflights.ogg"

    $ saturation_tint_level = "default"

    show morning04_bg livingroom_room_night_lingerie_others_LightOn:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 0.2

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx04
    show didacf_mouth sadbiting_Silentx03
    with dissolve

    ono "clic"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "Gracias, [protname]..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows sadx04
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    p "..."

    show didacf_eyes 04
    show didacf_pupils right04
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "Tranquilo,"

    extend " no hay de qué..."

    p "Soy consciente de que lo debes de estar pasando fatal..."

    show didacf_eyes 05
    show didacf_pupils right05
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx04
    with dissolve

    p "en mi lugar hubieras hecho lo mismo."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx04
    show didacf_mouth sad_Silentx04
    with dissolve

    d "..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "¿Tienes que ir al baño?"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows sadx03
    show didacf_mouth sadbiting_Silentx02
    with dissolve

    p "..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows sadx01
    show didacf_mouth sadbiting_Silentx01
    with dissolve

    p "No..."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx01
    with dissolve

    p "Puedes ir."

    scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 0.2
    with dissolve

    n "Sin siquiera haberte dirigido la mirada un solo instante,"

    n "anda aún temblando hasta el baño, cerrando la puerta con pestillo, una vez dentro."

    p "..."

    pt "Creo que, de algún modo,"

    extend " ha recobrado un poco su cordura,"

    pt "aunque espero,"

    extend " que por lo menos,"

    pt "le pueda durar toda la noche..."

    pt "Realmente estoy cansado."

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    n "Con las escasas fuerzas que te quedan, te diriges a la habitación,"

    play sound "audio/sfx/click_turnofflights.ogg"

    scene beds_night_lightOff_blindUp_DemptyMCbusy
    with Dissolve (0.5)

    n "en la que apagas la lámpara de noche, te desprendes de tu ropa,"

    # scene beds_night_lightOff_blindDown_DemptyMCbusy
    # with Dissolve (0.5)

    # n "bajas la cortina,"

    stop music fadeout 3.0
    $ music_play = ""

    scene black
    with fade

    n "y cierras los ojos."

    jump morning05

label afternight04_Park_HelpDidacPolice_Yes:

    #n "A diferencia de sus dos compañeros, este último parecía no tener ningún reparo en alterar el silencio del lugar."

    #oku "{size=30}¡¡ME CORRO JODER!!{/size}"

    #pt "Si lo que me dijo Neus es cierto, nunca más volveré a ver a mi amigo siendo un chico..."

    #pt "Aunque quizás si se toma la pastilla del día después, puede que aún tenga alguna esperanza... supongo..."

    #ono "CRRRIICK"

    #n "Un agudo chirrido metálico se oye en la lejanía."

    #pt "¡La puerta del parque!"

    #pt "Con tanto ruido habrán llamado la atención del vecindario y seguramente algún agente estará al caer..."

    #pt "¡Sino saco de aquí a Dídac inmediatamente se pondrá en un follón mayor!"

    show an04_park_bank_far_bush empty
    with dissolve

    play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "nonstop"

    n "Sales disparado de tu escondite corriendo a toda velocidad hasta donde está Dídac."

    scene bg an04_park_bank_far_closer_background_03
    show an04_park_bank_cum_squatter 01:
        truecenter
        zoom 0.5
    show an04_park_bank_cum_didacass:
        truecenter
        zoom 0.5
    with fade

    n "Apartas con una mano al sujeto que está encima de Dídac,"

    show an04_park_bank_cum_squatter 02:
        subpixel True
        easein_quad 5.0 xpos 0.6
    with hpunch

    n "sacándole al mismo tiempo su miembro."

    show an04_park_bank_cum_squatter 03:
        subpixel True
        xpos 0.45
        easein_quad 7.0 xpos 1.0
    with dissolve

    pause 0.3

    show an04_park_bank_cum_didacass_sperm:
        truecenter
        zoom 0.5
    with dissolve

    ono "SPURT"

    hide an04_park_bank_cum_squatter
    with dissolve

    n "Una salpicadura, impulsada por su polla al hacer palanca, queda impregnada en tu camiseta."

    n "Como si descorcharas una botella de cava, todo el esperma vertido dentro de su vagina empieza a brotar hacia fuera."

    pt "Se ha corrido ahí dentro que da gusto..."

    n "El llamado \"Okupa\" cae rendido al suelo después de semejante corrida entrando de nuevo en su estado vegetativo anterior,"

    n "mientras que sus otros dos compañeros se quedan mirando la escena entre sorpresa y curiosidad."

    n "Sin más dilación recoges la ropa de Dídac del suelo."

    p "¡Date prisa!"

    extend " están al caer."

    p "¡No hay tiempo!"

    n "Al oírte, los dos individuos que están cerca del banco,"

    n "desvían su mirada para fijarla en la lejanía -de la que no quitas ojo-,"

    n "y observan -por ellos mismos- cómo se acercan dos individuos trajeados con linterna."

    n "Con cierta celeridad, empiezan a recoger las botellas -que aún contienen algo de alcohol- en sus mochilas,"

    n "mientras terminan de vestirse."

    d "..."

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5

    ###  DIDAC

    show didacfbodytop park_dirt_02:
        zoom 0.25 xanchor 0.2
    show didacfhandl hip_naked:
        zoom 0.25 xanchor 0.2
    show didacfhandr leg_naked:
        zoom 0.25 xanchor 0.2

    show didacfbodycloth_whole empty:
        zoom 0.25 xanchor 0.2

    #  D expressions

    show didacf_blush 04:
        an04_park_didacf_left_expressions

    show didacf_eyes 05:
        an04_park_didacf_left_expressions

    show didacf_pupils front05:
        an04_park_didacf_left_expressions

    show didacf_eyebrows suspiciousx01:
        an04_park_didacf_left_expressions

    # Hair

    show didacfbodytop_hair:
        zoom 0.25 xanchor 0.2

    show didacf_mouth sad_Talkingx002:
        an04_park_didacf_left_expressions
    with fade

    d "¿[protname]..?"

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx03
    with dissolve

    p "¡Te he dicho que no hay tiempo!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx04
    show didacfbodycloth_whole gabardine
    with dissolve

    n "Le pones rápidamente la gabardina por encima, la agarras por la muñeca"

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx02
    with dissolve

    scene bg an04_park_bank_far_closer_background_02:
        zoom 0.5
    with dissolve

    n "y arrastrándola te la llevas corriendo a un lugar seguro -en dirección opuesta a la de los tipos de las linternas-."

    play music "audio/music/kevinmacleod/happy_boy_end_theme.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "happy_boy_end_theme"

    show an04_park_squatter_body:
        transform_anchor True
        xalign 0.34 yalign 0.46 zoom 0.5
        xpos 0.85 ypos 0.54

    show an04_park_squatter_exp_mouth Talkingx002:
        transform_anchor True
        xalign 0.5 yalign 0.5 zoom 0.5
        xpos 0.85 ypos 0.54

    with Dissolve(0.5)

    oku "Jodéee..."

    extend " qué corrida..."

    show an04_park_squatter_body:
        xpos 0.75
    show an04_park_squatter_exp_mouth Silentx02:
        xpos 0.75
    with dissolve

    oku "..."

    show an04_park_squatter_body:
        xpos 0.6
    show an04_park_squatter_exp_mouth Talkingx03:
        xpos 0.6
    with dissolve

    oku "¿Por qué se ha largado todo el mundo...?"

    show an04_park_squatter_body:
        xpos 0.5
    show an04_park_squatter_exp_mouth Silentx01:
        xpos 0.5
    with dissolve

    show light 01 zorder 98:
        additive 1.0
        truecenter
        rotate -90

    with dissolve

    s "¡¿Quién anda ahí?!"

    show an04_park_squatter_exp_mouth Silentx02
    with dissolve

    oku "..."

    show an04_park_squatter_body
    show an04_park_squatter_exp_mouth Talkingx02
    with dissolve

    oku "Mierda..."

    show an04_park_squatter_exp_mouth Silentx03
    with dissolve

    window hide dissolve
    pause

    play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "torn_apart"

    scene bg an04_park_fountain:
        subpixel True
        xanchor 0.5 yanchor 0.5 zoom 1.0
        ease_quad 20.0 xanchor 0.0 yanchor 0.0 zoom 0.5
    with fade

    n "Algo en la lejanía, oyes los murmullos del llamado \"Okupa\" hablando con los hombres de las linternas,"

    n "pero decides que lo más sensato, es no averiguar cómo continua esa conversación."

    $ saturation_tint_level = "verydark"

    scene bg an04_park_path01_composition 01b:
        truecenter
    with fade

    d "[protname],"

    extend " me haces daño..."

    n "Consigues esconderte junto a Dídac lo mejor que te es posible, entre los arbustos."

    window hide dissolve
    pause

    show didacfbodytop park_dirt_02:
        dfbody_center_superclose
    show didacfhandl hip_naked:
        dfbody_center_superclose
    show didacfhandr leg_naked:
        dfbody_center_superclose

    show didacfbodycloth_whole gabardine_dirt_02:
        dfbody_center_superclose

    #  D expressions

    show didacf_blush 04:
        dexpressions_center_superclose

    show didacf_eyes 04:
        dexpressions_center_superclose

    show didacf_pupils front04:
        dexpressions_center_superclose

    show didacf_eyebrows suspiciousx01:
        dexpressions_center_superclose

    # Hair

    show didacfbodytop_hair:
        dfbody_center_superclose

    show didacf_mouth sad_Talkingx002:
        dexpressions_center_superclose
    with dissolve

    d "¿Qué...?"

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx03
    with dissolve

    d "¡¿Qué diablos haces aquí?!"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Shhhh..."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx06
    with dissolve

    p "Si gritas,"

    extend " esos guardias de seguridad nos van a oír."

    show didacf_eyes 01
    show didacf_pupils left01
    show didacf_eyebrows normal
    show didacf_mouth sad_Silentx02
    with dissolve

    n "Dídac alza la vista por encima de las hojas y comprueba la veracidad de tus palabras."

    show didacf_eyes 02
    show didacf_pupils left02
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx002
    with dissolve

    d "Mierda..."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Ya te lo he dicho."

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx01
    show didacf_mouth sad_Silentx04
    with dissolve

    p "Ahora será mejor largarnos cuanto antes."

    show didacf_eyes 05
    show didacf_pupils down05
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx06
    with dissolve

    n "A regañadientes, no tiene otra opción que darte la razón."

    show didacf_eyes 03
    show didacf_pupils down03
    show didacf_eyebrows normal
    show didacf_mouth sad_Talkingx02
    with dissolve

    d "¿Qué...?"

    extend " ¿Qué coño...?"

    show didacf_eyes 01
    show didacf_pupils down01
    show didacf_eyebrows surprisex01
    show didacf_mouth sad_Silentx07
    with dissolve

    n "Al fijarte en Dídac, observas que con sus dedos está tocando el sólido esperma"

    n "que aún brota del interior de su vagina."

    show didacf_eyes 00
    show didacf_pupils down00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¡¿Se me ha corrido dentro?!..."

    play music "audio/music/alcaknight/crimson_waltz.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "crimson_waltz"

    show didacf_eyes 00
    show didacf_pupils down00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx06
    with dissolve

    n "Su tono de voz es frío como un témpano de hielo."

    pt "Mierda..."

    pt "Ahora se ha dado cuenta de que se ha quedado preñado,"

    extend " el muy imbécil..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows surprisex02
    show didacf_mouth sad_Silentx05
    with dissolve

    window hide dissolve
    pause

    # play music "audio/music/alcaknight/torn_apart.ogg" fadein 3.0 fadeout 3.0
    # $ music_play = "torn_apart"

    scene bg an04_park_path01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.4 # Beginning
        easein 10.0 zoom 1.0 xpos 1.0 ypos 0.2 # Going to Left.
    with fade

    n "Le agarras por la muñeca y le ayudas a llegar a la entrada del parque."

    window hide dissolve
    pause

    scene bg an04_entranceciutadella_fence_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.6 ypos 0.3
        easein 20.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "La sigues arrastrando, hasta que ambos conseguís saltar la valla de seguridad sin ser vistos,"

    n "en teoría, por nadie."

    scene bg an04_placasantagustivell_composition 04:
        subpixel True
        xanchor 0.0 yanchor 0.5 zoom 1.0
        easein 30.0 xanchor 1.0 yanchor 0.7 zoom 1.0
    with fade

    n "Recorréis varias calles para alejaros del parque a paso ligero sin llamar demasiado la atención."

    pt "Si alguien ve a Dídac así,"

    pt "¿pensará que ha ido a hacer ejercicio y que se ha meado al mismo tiempo?"

    pt "Lo mejor es que lleguemos a casa cuanto antes..."

    window hide dissolve
    pause

    scene bg an04_street02:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.5
        easein 20.0 zoom 1.0 xpos 0.25 ypos 0.5
    with fade

    n "Dídac seguía en silencio con la mirada perdida."

    n "Sujetándole con fuerza su muñeca,"

    n "no tenía demasiado tiempo para réplicas."

    n "Tu expresión facial junto con la celeridad del paso"

    n "tampoco le ofrecen demasiadas oportunidades de conversación."

    window hide dissolve
    pause

    scene bg an04_flat_gate_composition002:
        subpixel True
        zoom 0.5 xanchor 0.0 yanchor 1.4 #General view door.
        ease 50.0 zoom 1.0 xanchor 0.0 yanchor 0.0
    with fade

    n "Los minutos que transcurren en el ascensor, tampoco son precisamente muy cómodos,"

    n "decidís no dirigiros la mirada."

    scene afternight03_bg_entrance_lightoff_night
    with fade

    pause 0.5
    scene afternight03_bg_entrance_lighton
    with dissolve

    play sound "audio/sfx/click_turnofflights.ogg"

    n "Poco después de abrir la puerta del piso,"

    play sound "audio/sfx/metal_keys_deposit.ogg"

    show afternight03_bg_entrance_keysmc lighton:
        afternight03_bg_entrance_keys
    show afternight03_bg_entrance_keysd lighton:
        afternight03_bg_entrance_keys
    with dissolve

    $ saturation_tint_level = "default"

    play music "audio/music/kevinmacleod/lightless_dawn.ogg" fadein 3.0 fadeout 3.0
    $ music_play = "lightless_dawn"

    n "ambos lográis, por fin, relajar la tensión vivida hasta ese instante."

    scene morning04_bg livingroom_room_night_lingerie_others_LightOff_little
    with fade

    pause 0.5

    play sound "audio/sfx/click_turnofflights.ogg"

    show morning04_bg livingroom_room_night_lingerie_others_LightOn:
        transform_anchor True
        xalign 0.5 yalign 0.5
        zoom 0.2
    with Dissolve (0.5)

    pause 0.5

    show didacfbodytop park_dirt_02:
        dfbody_center
    show didacfhandl hip_naked:
        dfbody_center
    show didacfhandr leg_naked:
        dfbody_center

    show didacfbodycloth_whole gabardine_dirt_02:
        dfbody_center

    #  D expressions

    show didacf_blush 01:
        dexpressions_center

    show didacf_eyes 05:
        dexpressions_center

    show didacf_pupils right05:
        dexpressions_center

    show didacf_eyebrows serious:
        dexpressions_center

    # Hair

    show didacfbodytop_hair:
        dfbody_center

    show didacf_mouth sad_Silentx05:
        dexpressions_center
    with dissolve
    

    d "..."

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Talkingx01
    with dissolve

    d "[protname],"

    show didacf_eyes 04
    show didacf_pupils left04
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx02
    with dissolve

    extend " ¿cuánto hacía que estabas ahí espiando?"

    show didacf_eyes 05
    show didacf_pupils left05
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "..."

    menu afternight04_Park_HelpDidacPolice_No_Time_question:
        
        pt "Ya tardaba en hacerme la pregunta..."
        
        "Acababa de llegar.":
            
            call p_Help

            $pl.ch_pts("dp",-5)

            if music_play != "aura":
                play music "audio/music/alcaknight/aura.ogg" fadein 1.0 fadeout 1.0
                $ music_play = "aura"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx02
            show didacf_mouth sad_Silentx06
            with dissolve

            d "..."

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Silentx08
            with dissolve

            p "..."

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx04
            with dissolve

            d "Y justo cuando llegas,"

            extend " es cuando se me corre el tipo dentro..."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx05
            with dissolve

            d "¿Verdad?"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx03
            show didacf_mouth sad_Talkingx06
            with dissolve

            d "¡Qué puta casualidad!"

            show didacf_eyes 08
            show didacf_pupils front08
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx09
            with dissolve

            p "No sé..."

            extend " a veces las casualidades ocurren..."

            if music_play != "bury_it":
                play music "audio/music/alcaknight/bury_it.ogg" fadein 0.5 fadeout 0.5
                $ music_play = "bury_it"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx09
            with vpunch

            d "¡HIJO DE PUTA!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¿ERES CONSCIENTE QUE SE ME HA CORRIDO DENTRO UN PUTO YONKI DE MIERDA?!"

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx07
            with dissolve

            jump afternight04_Park_HelpDidacPolice_No_Time_Continuation

        "Desde el principio.":

            call p_Help

            $pl.ch_pts("dp",-10)

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows normal
            show didacf_mouth sad_Silentx05
            with dissolve

            d "..."

            if music_play != "colorless_aura":
                play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
                $ music_play = "colorless_aura"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows serious
            show didacf_mouth sad_Talkingx01
            with dissolve

            d "Y no..."

            extend " ¿No se te ocurrió detener esto antes...?"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Te refieres al;"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            show didacf_mouth sad_Silentx05
            with dissolve

            p "{i}Ya encontraré a alguien que me haga lo que tú no quieres hacerme{/i}?"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx06
            with dissolve

            d "..."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows serious
            show didacf_mouth sad_Talkingx03
            with dissolve

            d "[protname]..."

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows normal
            show didacf_mouth sad_Talkingx005
            with dissolve

            d "Se me ha corrido dentro..."

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡UN PUTO YONKI DE MIERDA!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx09
            with dissolve

            d "¡SIN CONDÓN!"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            show didacf_mouth sad_Silentx05
            with dissolve

            p "Es algo que suele pasar cuando lo haces con alguien que no conoces,"

            extend " en la calle,"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows normal
            show didacf_mouth sad_Silentx03
            with dissolve

            p "que es adicto a la heroína,"

            extend " o a cualquier otra mierda..."

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx02
            with dissolve

            d "..."

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows serious
            show didacf_mouth sad_Talkingx02
            with dissolve

            d "¿Te estás cachondeando?"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx02
            with dissolve

            p "¿Yo?"

            extend " ¿Tú crees...?"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx03
            with dissolve

            d "..."

            show didacf_eyes 04
            show didacf_pupils front04
            show didacf_eyebrows sadx01
            show didacf_mouth sad_Talkingx04
            with dissolve

            d "Lo que me dijiste de si me quedaba preñada era una broma..."

            extend " ¿Verdad...?"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx01
            with dissolve

            p "No."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows serious
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Dudo seriamente que fuera una broma."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows normal
            show didacf_mouth sad_Silentx03
            with dissolve

            d "..."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows serious
            show didacf_mouth sad_Talkingx01
            with dissolve

            d "¿A qué coño estás jugando...?"

            show didacf_eyes 02
            show didacf_pupils front02
            show didacf_eyebrows normal
            show didacf_mouth sad_Silentx02
            with dissolve

            p "Yo no sé,"

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows surprisex01
            show didacf_mouth sad_Silentx05
            with dissolve

            p "pero a ti,"

            extend " parece que se te ha ido un poco de las manos,"

            show didacf_eyes 00
            show didacf_pupils front00
            show didacf_eyebrows surprisex02
            show didacf_mouth sad_Silentx06
            with dissolve

            p "eso de jugar a papás y a mamás..."

            show didacf_eyes 01
            show didacf_pupils front01
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx09
            with dissolve

            d "¡HIJO DE PUTA!"

            show didacf_eyes 03
            show didacf_pupils front03
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Talkingx08
            with dissolve

            d "¡¿ERES CONSCIENTE QUE POSIBLEMENTE NO PUEDA VOLVER A SER EL QUE ERA?!"

            show didacf_eyes 05
            show didacf_pupils front05
            show didacf_eyebrows angryx04
            show didacf_mouth sad_Silentx09
            with dissolve

            jump afternight04_Park_HelpDidacPolice_No_Time_Continuation

label afternight04_Park_HelpDidacPolice_No_Time_Continuation:

    $ afternight04_didac_pregnantRapeOkupa = True
    #$ afternight04_DidacisNOTatHome = True # not anymore.

    p "Sí,"

    extend " soy consciente de que ya te advertí de ello."

    if music_play != "colorless_aura":
        play music "audio/music/kevinmacleod/colorless_aura.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "colorless_aura"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows angryx03
    show didacf_mouth sad_Silentx05
    with dissolve

    d "..."

    show didacf_blush 04
    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx06
    with dissolve

    n "Su rostro desprende una cólera digna del {a=https://es.wikipedia.org/wiki/Dioses_olímpicos}Olimpo{/a}."

    show didacf_blush 05
    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve

    n "Sus mejillas rojizas, sus ojos húmedos, su cuerpo temblando."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx08
    with dissolve

    p "Me imagino que querrás tomarte la pastilla del día después..."

    show didacf_eyes 00
    show didacf_pupils front00
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Talkingx09
    with vpunch

    d "¡¡CLARO QUE ME QUIERO TOMAR LA PUTA PASTILLA!!"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows angryx01
    show didacf_mouth sad_Silentx05
    with dissolve

    p "Yo de ti,"

    extend " me tomaría primero una ducha antes de ir a comprarla a la farmacia de guardia."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx07
    with dissolve

    n "Su mandíbula tirita de la rabia contenida."

    show didacf_eyes 05
    show didacf_pupils front05
    show didacf_eyebrows angryx04
    show didacf_mouth sad_Silentx08
    with dissolve

    p "Aunque para serte sincero,"

    extend " desconozco si tomarte esa pastilla solucionará el problema..."

    show didacf_blush 04
    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows angryx02
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "[protname],"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Talkingx06
    with dissolve

    d "¿por qué me haces esto?"

    show didacf_blush 03
    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx06
    show didacf_mouth sad_Talkingx004
    with dissolve

    d "¿Por qué no detuviste al puto yonki cuando viste que me iba a follar sin condón...?"

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx05
    with dissolve

    p "¿Sabes lo que he estado haciendo estos días?"

    show didacf_eyes 02
    show didacf_pupils front02
    show didacf_eyebrows sadx02
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    p "Básicamente ayudarte en algo,"

    extend " de lo que tú has sido el único responsable."

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx04
    show didacf_mouth sad_Silentx06
    with dissolve

    p "¿Y cómo me lo has agradecido?"

    show didacf_eyes 03
    show didacf_pupils right03
    show didacf_eyebrows sadx05
    show didacf_mouth sadbiting_Silentx05
    with dissolve

    p "Con insultos,"

    extend " gilipolleces,"

    extend " y haciendo lo que te ha dado la puta gana."

    show didacf_eyes 08
    show didacf_pupils front08
    show didacf_eyebrows sadx06
    show didacf_mouth sad_Silentx06
    with dissolve

    d "..."

    show didacf_eyes 01
    show didacf_pupils front01
    show didacf_eyebrows serious
    show didacf_mouth sad_Silentx03
    with dissolve

    p "Tómate una ducha,"

    show didacf_eyes 03
    show didacf_pupils front03
    show didacf_eyebrows sadx02
    show didacf_mouth sad_Silentx05
    with dissolve

    p "luego vete a buscar la pastilla de las narices,"

    show didacf_eyes 04
    show didacf_pupils front04
    show didacf_eyebrows sadx05
    show didacf_mouth sad_Silentx06
    with dissolve

    p "para que no tengas al bastardo de ese puto yonki de mierda;"

    show didacf_eyes 06
    show didacf_pupils front06
    show didacf_eyebrows sadx06
    show didacf_mouth sad_Silentx07
    with dissolve

    p "y reza para que eso no impida que puedas volver a ser el que eras."

    scene morning04_bg livingroom_room_night_lingerie_others_LightOn:
        truecenter
        zoom 0.5 xpos 0.7 ypos 0.65
    with Dissolve (0.5)

    n "Te alejas de tu compañero de piso en dirección a vuestra habitación,"

    play sound "audio/sfx/fall02.ogg"

    n "mientras oyes cómo cae de rodillas al suelo."

    p "Tú te lo has buscado Dídac."

    p "Agradece que haya impedido que fueras a comisaría,"

    p "si te llegan a identificar..."

    p "es posible que hubieras acabado peor."

    show morning04_bg livingroom_room_night_lingerie_others_LightOn:
        zoom 0.75 xpos 1.0 ypos 0.8
    with Dissolve (0.5)

    n "Dídac sigue en el suelo totalmente destrozada."

    p "Buenas noches."

    play sound "audio/sfx/door_close01.ogg"
    $ renpy.music.set_volume(0.8, delay=0.5, channel='sfx2')
    $ renpy.music.play("audio/sfx/crying_woman01_far.ogg", channel="sfx2",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.set_volume(0.5, delay=6.0, channel='sfx2')
    scene afternight03_bg_hallway_dark
    with fade

    n "Al cerrar la puerta, oyes sus gemidos y sollozos, como nunca le habías oído antes."

    n "Sin volver atrás, te diriges agotado hasta tu cama."

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with fade

    pause 0.5

    $ renpy.music.stop(channel='sfx2', fadeout=3.0)

    show morning04_bg_livingroom_mc_resting_phone home_message:
        xpos 0.485 ypos 0.125
    show morning04_livingroom_mc_resting_handphone
    with dissolve

    n "Observas en tu teléfono móvil, que está encima de la mesita de noche,"

    n "que tienes una llamada perdida de Neus."

    pt "Ha sido un día largo..."

    pt "Ahora no estoy para conversaciones..."

    scene beds_night_lightOn_blindUp_DemptyMCempty
    with dissolve

    pt "ya no puedo más..."

    play sound "audio/sfx/click_turnofflights.ogg"

    show beds_night_lightOff_blindUp_DemptyMCempty
    with Dissolve (1.0)

    n "Y apagando la luz,"

    scene black
    with fade

    n "te reencuentras con el sueño."

    jump morning05



#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####
#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####


label afternight04_Didac_FuckMe_NCloro:

    pt "¿Seguro que es buena idea?"

    pt "Al fin y al cabo es posible que se trate de una trampa,"

    pt "además, aún quedan 24 horas para la cita con Neus."

    pt "¿Lo voy a tener atado y encerrado en la habitación todo el día de mañana?"

    pt "Sin mencionar cuanto hace que debe de estar caducado este producto..."

    menu:

        "<Cambiar de idea>":
            call p_Help

            jump afternight04_Didac_FuckMe02

        "<Hacerlo>":
            call p_Help

            pass

    call WIP

    jump gameover

