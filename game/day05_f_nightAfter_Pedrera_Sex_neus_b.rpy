##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##

default pwawSysImage = ""
default pwawSysZoom = 1.0
default p_ao_mcAssSmacks_list = []

##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
# SHE CUMS

default p_ao_background = "ground" # Background for Blowjob Neus

default p_ao_whispers_n = 5.0

default p_ao_n_showDick = False

default p_neus_dickG_wants = False
default p_neus_dickG02_wants = "" # After you cum being fucked ,you want to keep being fucked in the ass.
default p_prot_aoNight_analReceived = ""

default p_ao_action_Cond = ""
default p_ao_action_b_Cond = ""
default p_ao_action_tongue_Cond = ""
default p_ao_dickState_Cond = ""

default ped_sex_general_expressionJaw_Cond = ""

default p_ao_mc_legs = ""

default p_ao_assSmack = ""
default p_ao_assSmacked = "right"
default p_ao_assSmacksR = 0
default p_ao_assSmacksL = 0

default p_ao_n_hipsImg = "_open"
default p_ao_n_hipsTrans = 0.5
default p_ao_n_tongue = ""
default p_ao_n_horns = ""
default p_ao_n_horns_num = 0
default p_ao_n_tail = ""
default p_ao_n_tail_num = 0
default p_ao_n_wings = ""
default p_ao_n_wings_num = 0
default p_ao_n_fur = ""
default p_ao_n_fur_num = 0
default p_ao_n_dick = ""
default p_ao_n_dick_num = 0
default p_ao_n_size = ""
default p_ao_n_size_num = 0
default p_ao_n_blur = ""
default p_ao_n_blur_num = 0
default p_ao_mc_dick = "" # How Reddish it is.
default p_ao_mc_dick_num = 6 # How Big it is.
default p_ao_ground = "ground"

default p_ao_sexPart = "_v"

default p_ao_neusLastSecret = False

default p_ao_started = False

label p_neus_orgasmRealScene:

    # $ p_ao_started = True
    # $ p_ao_mcAssSmacks_list = []

    $ ped_neus_whispers_sfx04 = 1.0

    # ne "¡Mi-"
    # extend "mierda!"
    # ne "¡¡No!!"
    # ne "¡[protname]!"
    # ne "¡Te-"
    # extend "te había dicho que no!"
    
    if p_prot.pos == "oral":

        progcheck "Oral position is even possible??"

        $ nteye = "front01"
        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx18
        show gensex_oral_n_frontHead_exp_eyebrows angryx05
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "missionary":

        $ nteye = "front01"
        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx18
        show gensex_missionary_n_head_exp_eyebrows angryx05
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "69":

        show gensex_69_L_d_mouth sadbiting_Silentx08
        with dissolve


    n "Su cuerpo empieza a tambalear mientras sus ojos brillan aún con más intensidad."

    #########################################################

    if config.version < "00.16.03": # NeusAfterHerOrgasm: Beginning
        call endupdatescript
    
    #######################################################

    python:
        # import struct
        # versionStruct = struct.calcsize("P")*8

        from sys import maxsize
        if not maxsize > 2**32:
            pwawSysImage = "_32"

    if pwawSysImage == "_32":

        aj "Debido a que tu sistema no es de 64 bits, los orbes rojos no se verán muy bien."

        ##### Low Image is at 40% of the original.
        $ pwawSysZoom = 2.5 # Original 1.0
        ## p_ao_ghost_body_All_trans_32 // zoom 1.3 # Original 0.5


    if p_prot.pos == "oral":

        # progcheck "Oral position is even possible??" # YEP, is possible.

        $ nteye = "front07"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx012
        show gensex_oral_n_frontHead_exp_eyebrows sadx06
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "missionary":

        $ nteye = "front07"
        show gensex_missionary_n_head_exp_mouth sad_Talkingx013
        show gensex_missionary_n_head_exp_eyebrows sadx06
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "69":

        show gensex_69_L_d_mouth sad_Talkingx009
        with dissolve

    play sound "audio/characters/neus/orgasm02.ogg"

    with hpunch
    
    ne "{size=60}¡¡AAAHHHMMM!!{/size}"

    stop sound fadeout 0.5

    if p_prot.pos == "oral":

        #progcheck "Oral position is even possible??" # YEP, is possible.

        $ nteye = "front00"
        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx15
        show gensex_oral_n_frontHead_exp_eyebrows angryx07
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "missionary":

        $ nteye = "front00"
        show gensex_missionary_n_head_exp_mouth sadbiting_Silentx15
        show gensex_missionary_n_head_exp_eyebrows angryx08
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

    elif p_prot.pos == "69":

        show gensex_69_L_d_mouth sadbiting_Silentx10
        with dissolve

    play sound "audio/sfx/fall18.ogg"

    scene black
    with vpunch

    p "¡AUCH!"

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    scene black
    hide screen Points_PedreraSex
    with fade

    $ ntlong = 0

    $ p_ao_started = True
    # $ p_ao_mcAssSmacks_list = []

    $ saturation_tint_level = "reallydark"
    call saturation_ting_values_check

    $ p_ao_ghost_standing_resolution = "low"

    play sound "audio/characters/neus/moan18.ogg"
    
    n "Con una fuerza casi sobrehumana,"

    play sound "audio/characters/neus/orgasm01.ogg"

    n "sales despedido cayendo de bruces contra el frío suelo."

    if gensex_YoureAMonster:

        p "¡Joder!"

        p "¡Me has hecho daño!"

    else:

        p "¿Qué..?"

    with hpunch

    play sound "audio/characters/neus/moan13.ogg"

    n "A través de tus pies, manos y nalgas desnudas, sientes el piso vibrar."

    play sound "audio/characters/neus/moan20.ogg"

    pt "¡¿Qué demonios?!"

    play sound "audio/characters/neus/moan19.ogg"

    n "Como si estuviera poseída,"

    if music_play != "malicious":
        play music "audio/music/kevinmacleod/malicious.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "malicious"

    $ renpy.music.set_volume(1.0, delay=0.8, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    ## ILUSTRATION Neus on the bed shacking? A001


# #####
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_n_orgasm_comp:
#         truecenter
#         zoom 0.2
#     pause
# ####

    scene p_ao_n_orgasm_comp:
        subpixel True
        truecenter
        zoom 2.0 xpos 3.0 ypos -0.5 # Foot?
        easein_quad 12.0 zoom 0.4 xpos 0.5 ypos 0.5 # General View

    show border_darkness:
        subpixel True
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    #$ p_neus.orgasm += 1 # NOT NECESSARY.


    $ renpy.music.set_volume(0.2, delay=8.0, channel='sfx1')

    $ ped_neus_whispers_sfx04 = 0.4

    n "[neusname] retuerce sus articulaciones en posiciones inhumanas"

    n "al mismo tiempo que te parece ver la cama levitar."

    n "Su cuerpo empieza a desprender un vapor denso y extraño."

    window hide dissolve
    pause

    $ n_withoutGlasses_story = True

    scene black02
    show night04_pedrera_baba01_background:
        zoom 0.6
    show night04_pedrera_baba01_door:
        zoom 0.5
    show night04_pedrera_baba01_frame:
        zoom 0.5
    show p_ao_neusShouting_comp empty
    show border_lines empty
    show border_darkness:
        subpixel True
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 50.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    d "¡¿Se puede saber qué coño pasa ahí dentro?!"

    play sound "audio/sfx/door_old_short_open01.ogg"

    ## ILUSTRATION Didac Door?

    show night04_pedrera_baba01_background:
        subpixel True
        zoom 0.6
        easein_quad 15.0 zoom 0.4
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4 xanchor -0.1
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.5
        easein_quad 15.0 zoom 0.4
    with dissolve

    n "Oyes la voz de Dídac que entre abre la puerta para ver qué está ocurriendo."

    show black
    with fade

    show black empty
    show p_ao_neusShouting_comp:
        subpixel True
        truecenter
        xpos -1.0 ypos 1.15
        zoom 1.5
        easein_quad 1.0 xpos 0.0

    show border_lines 05:
        subpixel True
        truecenter
        zoom 0.6
        ease_bounce 3.0 zoom 0.3

    with hpunch

    n "Al ver el diabólico rostro y los brillantes ojos de [neusname],"

    play sound "audio/sfx/door_close01.ogg"

    show p_ao_neusShouting_comp empty
    show border_lines empty
    show night04_pedrera_baba01_background:
        subpixel True
        zoom 0.4
        easein_quad 0.5 zoom 0.6
    show night04_pedrera_baba01_door:
        subpixel True
        zoom 0.4
        easein_quad 0.5 zoom 0.5 xanchor 0.0
    show night04_pedrera_baba01_frame:
        subpixel True
        zoom 0.4
        easein_quad 0.5 zoom 0.5
    with hpunch

    ono "{size=50}PAM{/size}"

    n "Didac cierra la puerta de inmediato."

    n "Con una voz casi demoníaca:"

# ###
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_neusShouting_comp:
#         truecenter
#         zoom 0.2
#     pause
# ###

    show p_ao_neusShouting_comp:
        subpixel True
        truecenter
        xpos 0.35 ypos 0.1 zoom 1.0 # Mouth
        pause 0.3
        ease_elastic 1.5 zoom 0.3 xpos 0.5 ypos 0.5 # Whole Picture
        
    show border_lines 05:
        subpixel True
        truecenter
        zoom 1.0
        pause 0.7
        ease_bounce 1.5 zoom 0.3

    ne "{size=40}¡OS HE DICHO QUE NO ENTRÁRAIS!{/size}"

    scene black
    with vpunch

    p "¡Ugh!"

    stop music fadeout 2.0

    n "Sientes que pierdes las fuerzas y que eres incapaz de moverte."

    pt "¡¿Qué está pasando?!"

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    n "Sin apenas darte cuenta, cesa el temblor y se hace el silencio absoluto."

    ## ILUSTRATION Ceiling-Blink Eye- Darkness
    # with fade

    scene bg ped_ceiling
    show p_ao_ghost_surrounded_comp empty
    show night05_Cemetery_smoke_b_comp:
        subpixel True
        truecenter
        ypos 1.7 # Hide?
        easein_quad 100 ypos 1.0
        # easein_quad 50.0 ypos 0.5 # Full
    show border_darkness:
        subpixel True
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 50.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    
    show morning04_bedroom_DMast_blinkeye
    with fade

    $ p_ao_n_dick_num += 1 # First time. You didn't cum, but your dick is kinda tired.
    call p_ao_n_changes

    pt "¿Habrá terminado?"

    $ p_ao_ghost_standing_resolution = "low"

    $ ped_neus_whispers_sfx04 = 0.1

    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx3')
    $ renpy.music.set_volume(0.0, delay=0.1, channel='sfx4')

    $ renpy.music.play("audio/sfx/whispers_child01.ogg", channel="sfx3",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ renpy.music.play("audio/sfx/whispers_creepy01.ogg", channel="sfx4",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    $ p_ao_whispers_n = 5.0
    call p_ao_whispers_label

    show night05_Cemetery_smoke_b_comp:
        subpixel True
        truecenter
        ypos 1.7 # Hide?
        easein_quad 100 ypos 1.0
        # easein_quad 50.0 ypos 0.5 # Full


    if music_play != "echoesOfTimev2":
        play music "audio/music/kevinmacleod/creepy/echoesOfTimev2.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "echoesOfTimev2"


    # scene black
    # with fade

    n "No eres ni capaz de voltear la cabeza para mirar a tu alrededor."

    #Smoke appearing

    n "Ese extraño humo que emanaba del cuerpo de [neusname] empieza a rodearte."

    pt "Pero..."

    extend " ¡Que peste!"

    n "Un hedor nauseabundo -como de huevos podridos- inunda la habitación."

    # Red eyes appearing.

    $ ped_neus_whispers_sfx04 = 0.4
    $ renpy.music.set_volume(ped_neus_whispers_sfx04, delay=5.0, channel='sfx4')

    show p_ao_ghost_surrounded_comp:
        truecenter
    with Dissolve(2.0)


    n "Entre la oscuridad y ese espeso humo hediondo..."

    if night04_pedrera_blowjob_DONE:

        pt "Otra vez esos ojos rojos..."

    else:
        pt "¡¿Qué coño?!"

    $ renpy.music.set_volume(1.0, delay=0, channel='sfx2')
    $ renpy.music.play("audio/sfx/step_bare01.ogg", channel="sfx2",loop=False, fadeout=0.0, synchro_start=True, fadein=0.0)

    call p_ao_n_changes
    ono "tap"
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx2')
    $ renpy.music.play("audio/sfx/step_bare02.ogg", channel="sfx2",loop=False, fadeout=0.0, synchro_start=True, fadein=0.0)

    call p_ao_n_changes
    extend " {size=50}tap{/size}"
    $ renpy.music.set_volume(1.0, delay=0, channel='sfx2')
    $ renpy.music.play("audio/sfx/step_bare03.ogg", channel="sfx2",loop=False, fadeout=0.0, synchro_start=True, fadein=0.0)

    call p_ao_n_changes
    extend " {size=60}tap{/size}"

    n "Oyes sus pasos -desnudos y como si pisara sobre mojado- acercándose."

    scene black
    with fade

    pt "¡No puedo moverme!"

    $ p_ao_whispers_n = 0.1
    call p_ao_whispers_label

    n "Ni siquiera eres capaz de orbitar tus ojos para mirar a otro lugar que no sea el techo."

    ne "Travieso..."

    # Wet smoky fingers touching your toes.

    $ ped_neus_whispers_sfx04 = 0.4

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"

    $ p_ao_action_Cond = "foot"

    show p_ao_ground_comp:
        zoom 2.0 xpos -2.6 ypos -1.3 # Foot Camera
    show night05_Cemetery_smoke_b_comp:
        truecenter
        alpha 0.75
        ypos 1.4
        easein_quad 100 ypos 1.0
    with fade

    # ##### ## Testing

    # $ p_ao_ghost_standing_resolution = "low"
    # $ ped_neus_whispers_sfx04 = 1.0

    # scene p_ao_ground_comp:
    #     truecenter
    #     zoom 0.2

    # pause

    # $ p_ao_ghost_standing_resolution = ""
    # scene p_ao_ground_comp:
    #     truecenter
    #     zoom 0.2

    # ######

    n "Como si fueran gotas de cera líquida ardiendo sobre tu piel,"

    n "sientes sus dedos en la planta de tus pies que -de modo juguetón-"

    $ p_ao_action_Cond = "legs"

    show p_ao_ground_comp:
        zoom 2.0 xpos -1.65 ypos -1.3 # Legs Camera
    with Dissolve(0.5)

    n "empiezan a ascender por tus piernas."

    $ p_ao_action_Cond = "crotch"

    show p_ao_ground_comp:
        zoom 2.0 xpos -0.5 ypos -1.3
    with Dissolve(0.5)


    ne "Has sido un chico muy travieso..."

    # ILLUSTRATION Her mouth next to your balls.

    $ p_ao_action_Cond = "sigh"

    show p_ao_ground_comp:
        zoom 2.0 xpos -0.5 ypos -1.5
        ease 10.0 xpos -0.5 ypos -1.2
    with Dissolve(0.5)

    n "Su aliento, mucho más abrasador de lo que habías sentido hasta ahora,"

    n "acaricia tus partes púdicas al descubierto."

    if gensex_YoureAMonster:

        ne "Dices que soy un monstruo,"

        ne "y aún así te has atrevido a darme un orgasmo..."

        ne "No sé si te ha empujado la estupidez,"

        extend " la ignorancia,"

        extend " o la curiosidad..."

        n "Intentas responder, pero eres incapaz de despegar tus labios."

    else:

        ne "¿Qué voy a hacer contigo?..."


    play sound "audio/sfx/fall18.ogg"

    # ILLUSTRATION She sits over you. (Touching your dick.)

    $ p_ao_action_Cond = "over"
    show p_ao_ground_comp:
        zoom 2.0 xpos -0.6 ypos -1.8
        ease 5.0 zoom 2.0 xpos -0.3 ypos -0.7
    with vpunch
    p "¡AAuuuhh...!"

    n "Como si se tratara de una enorme bolsa con agua hirviendo,"

    n "sientes sus nalgas posándose sobre tus piernas"

    # same illustration showing her fingers touching your dick.

    #$ p_ao_ground = "bed" # Delete this one because it should be implemented before...

    $ p_ao_action_Cond = "soft"
    show p_ao_ground_comp:
        zoom 2.0 xpos -0.3 ypos -0.7
    with Dissolve(0.5)

    n "al mismo tiempo que sus dedos acarician tu enorme miembro"

    n "para acercárselo peligrosamente a su -no menos hirviente- barriga."

    p "¡Estás ardiendo!"

    #  ILLUSTRATION her face in the darknes sorrounded by fog and red eyes. (NO EXPRESSIONS!!!!!)

    $ p_ao_action_Cond = "grab"
    show p_ao_ground_comp:
        zoom 2.0 xpos -0.3 ypos -0.7
    with Dissolve(0.5)

    ne "¿Verdad que sí?"

    p "¡Lo digo en serio!"

    ne "Es que me pones muy caliente,"

    if gensex_ILoveYouNeus:

        extend " cariño..."

    else:

        extend " [protname]..."

    # LEGS AGAIN.

    p "¡Me estás quemando las piernas!"

    ne "Vamos,"

    ne "un poquito de calor no puede hacerle ningún daño a un valeroso y apuesto caballero como tú,"

    ne "¿verdad que no?,"

    if gensex_YoureAMonster:

        extend " mi apuesto caballero..."

    elif gensex_ILoveYouNeus:

        extend " mi amado Lancelot..."
    else: 

        extend " mi querido Lancelot..."

    # ILLUSTRATION está de cuclillas sobre el suelo para ponerse tu polla en su interior, esta vez lo ves de frente. 

    $ p_ao_action_Cond = "nride01"

    scene p_ao_ride_comp 01:
        subpixel True
        truecenter
        zoom 1.0
        ypos -0.5
        pause 0.5
        easein_quad 20 ypos 0.5
    with fade_long1s

    n "Despega su abrasador trasero de tus piernas mientras sigue acariciando tu erecto miembro."

    p "¿Qué...?"

    play sound "audio/characters/neus/shh02.ogg"

    ne "Shhh..."

    ne "Sé lo que me hago..."

    if p_neus.vaginalDeep_received > 0:

        ne "Al fin y al cabo ya me la has metido entera."

    elif p_neus.vaginal_received > 0:

        ne "Al fin y al cabo ya me la has metido,"

        ne "aunque no haya sido entera..."

    elif p_neus.anal_received > 0:

        ne "Aunque solo me la hayas metido por detrás..."

    else:

        ne "Aunque no te hayas atrevido a metérmela,"

        extend " ni siquiera por detrás..."

    # ILLUSTRATION Cuclillas: Coño tocando la punta de tu nabo.


    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    $ p_ao_action_Cond = "nride01"

    show p_ao_ride_comp 01:
        ease 5 ypos 1.0

    n "Cuando sus labios vaginales alcanzan la punta de tu glande sufres en él un ardor punzante."

    # Cuclillas: Tu polla dentro de su coño.(Glande)
    $ p_ao_action_Cond = "nride02"

    show p_ao_ride_comp 01:
        truecenter
        zoom 1.0 xpos 0.5 ypos 1.0
    with Dissolve(1.5)

    pt "¡Joder!"

    $ p_ao_action_Cond = "nride03"
    show p_ao_ride_comp 01:
        ease 10 ypos 0.75
    with Dissolve(1.5)

    n "Como si introdujeras tu polla en cera ardiente,"
    # Cuclillas: Polla casi en la mitad.

    $ p_ao_action_Cond = "nride04"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    n "sientes que sus caderas van descendiendo al mismo tiempo que ves tu polla desaparecer en su interior."

    p "[neusname]..."

    play sound "audio/characters/neus/shh01.ogg"

    ne "Shhh..."

    # ILLUSTRATION Ojos brlilantes en la oscuridad. fog and darkness. A002

    $ ped_neus_whispers_sfx04 = 0.4
    call p_ao_whispers_label

    scene p_ao_n_watchingYou_comp:
        subpixel True
        truecenter
        ### zoom 1.2 xpos 0.5 ypos 1.2 # Her face Close
        ### zoom 0.7 xpos 0.5 ypos 0.8 # Her face Far
        zoom 1.5 xpos 0.5 ypos 0.1 # Down
        easein_quad 12.0 zoom 0.7 xpos 0.5 ypos 0.8 # Her face Far
    with fade

    n "Sus ojos brillantes destacan por encima de los demás orbes rojos que te rodean en la oscuridad de la habitación."

    ne "Poco a poco te irás acostumbrando al ardor,"

    ne "ya verás que con el paso de los minutos no te hará tanto daño."

    window hide dissolve
    pause

    $ p_ao_whispers_n = 0.15
    call p_ao_whispers_label

    # Cuclillas. polla mitad.

    $ p_ao_action_Cond = "nride04"
    scene p_ao_ride_comp 01:
        truecenter
        ypos 0.75
    with fade_long1s

    $ p_ao_action_Cond = "nride05"
    show p_ao_ride_comp 01:
        ease 5 ypos 0.6
    with Dissolve(1.5)

    pt "¡Lo que pasará al final es que me dejarás sin polla!"

    # Cucllas. Polla Glande.

    $ p_ao_action_Cond = "nride04"
    show p_ao_ride_comp 01:
        ease 5 ypos 0.75
    with Dissolve(1.5)

    $ p_ao_action_Cond = "nride03"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    n "Lentamente empieza a volver a subir sus caderas, dejando respirar a tu ahogado y abrasado miembro,"

    # Cuclillas. polla mitad.

    $ p_ao_action_Cond = "nride04"
    show p_ao_ride_comp 01:
        ease 5 ypos 0.6
    with Dissolve(1.5)

    $ p_ao_action_Cond = "nride05"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    n "para luego volver a descender."

    # Cuclillas. Casi entera.

    $ p_ao_action_Cond = "nride04"
    show p_ao_ride_comp 01:
        ease 5 ypos 1.0
    with Dissolve(1.5)

    $ p_ao_action_Cond = "nride03"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    $ p_ao_action_Cond = "nride02"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    $ p_ao_action_Cond = "nride01"
    show p_ao_ride_comp 01
    with Dissolve(1.5)

    n "A pesar de tus gruñidos de dolor,"

    # Cuclillas. Animación ENTERA-MITAD-GLANDE

    $ p_ao_n_vel = 1

    $ p_ao_action_Cond = "nride06_anim"
    show p_ao_ride_comp 01:
        ypos 1.0
        block:
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.5
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.75
            repeat
    with Dissolve(1.5)

    n "se desplaza lentamente desde la punta hasta casi tragarse por entero tu miembro."

    n "No solo su cuerpo transpira vapor por todos lados,"

    n "sino que además exhala en sus jadeos un vaho aún más denso."

    # Rostro ojos brillantes con jadeo.

    pt "Joder..."

    ne "Estás a punto,"

    extend " ¿verdad?"

    scene black
    with fade

    # Beso en los labios


    show kiss_ f_n_07:
        truecenter
        xzoom -1.0
        rotate -60
        zoom 1.2

    show night05_Cemetery_smoke_b_comp:
        truecenter
        # ypos 1.7 # Hide?
        # easein_quad 100 ypos 1.0
        ypos 1.0

    with Dissolve(1.0)

    pause 0.2

    show kiss_ f_n_10
    with Dissolve(0.75)

    show kiss_ f_n_11
    with Dissolve(0.75)

    show kiss_ f_n_08
    with Dissolve(0.75)

    show kiss_ f_n_12
    with Dissolve(0.75)

    n "Inclina su cuerpo para acariciar con sus labios -que arden como si acabaran de salir del horno- los tuyos."

    # Labios negros con los tuyos.

    # if music_play != "almost_new_kevin":
    #     play music "audio/music/kevinmacleod/almost_new_kevin.ogg" fadein 3.0 fadeout 3.0
    #     $ music_play = "almost_new_kevin"


    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nblush = "05"
    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade_short

    ne "Me pones realmente caliente,"

    if gensex_ILoveYouNeus:

        extend " cariño."

    else:

        extend " [protname]."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx06
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    pt "¡No lo había notado!"

    play sound "audio/sfx/fall01.ogg"

    scene black
    with hpunch

    p "¡Ugh!"

    $ ped_neus_whispers_sfx04 += 0.3
    $ p_ao_whispers_n += 0.3
    $ p_ao_n_vel = 3

    $ p_ao_action_Cond = "nride06_anim"
    scene black
    show p_ao_ride_comp 01:
        truecenter
        ypos 1.0
        block:
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.5
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.75
            repeat
    with Dissolve(1.5)

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    # Imagen de su trasero engulliendo tu polla-animación

    n "Sus caderas aceleran el ritmo."

    $ p_ao_n_vel = 5

    $ p_ao_action_Cond = "nride06_anim"
    show p_ao_ride_comp 01:
        ypos 1.0
        block:
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.5
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.75
            repeat
    with Dissolve(1.0)

    # Labios negros con los tuyos (de nuevo) (Abiertos y cerrados sonriendo)

    ne "Córrete,"

    ne "córrete dentro de mi."

    $ p_ao_n_vel = 7

    $ p_ao_action_Cond = "nride06_anim"
    show p_ao_ride_comp 01:
        ypos 1.0
        block:
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.5
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.75
            repeat
    with Dissolve(0.5)

    p "[neusname]..."

    $ p_ao_n_vel = 3

    $ p_ao_action_Cond = "nride07_anim"
    show p_ao_ride_comp 01:
        ypos 1.0
        block:
            easein 5.0/p_ao_n_vel ypos 0.5
            pause 0.5/p_ao_n_vel
            easeout 4.5/p_ao_n_vel ypos 0.75
            repeat
    with Dissolve(0.5)

    ne "Quiero sentir tu esperma fluyendo en mi interior."

    if gensex_YoureAMonster:

        p "¡¿Quien te ha dicho que quiera dejarte embarazada?!"

        ne "..."

        ne "¿Acaso crees que te lo estoy  pidiendo?"

    # Animación de trasero follandote aumentando de ritmo.

    $ p_ao_action_Cond = "nbVaginalRide_00"

    $ p_ao_n_vel = 2

    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        xpos 0.5
        zoom 1.5 ypos -1.5 # Down?
        ease 4.0 zoom 1.0 ypos 1.0 # Up
    with fade_long1s

    n "Sus manos - como si fueran dos planchas a media potencia- se agarran a tu pecho,"

    $ p_ao_n_vel = 5
    $ p_ao_action_Cond = "nbVaginalRide_03"

    show gensex_n_briding_comp vaginal_01:
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            ease 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "mientras su pelvis incrementa la marcha."

    $ p_ao_n_vel = 8
    $ p_ao_action_Cond = "nbVaginalRide_04"

    show gensex_n_briding_comp vaginal_01:
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(0.5)

    n "Sus nalgas chocan contra tus piernas"

    $ p_ao_n_vel = 10
    #$ p_ao_action_Cond = "nbVaginalRide_04"

    show gensex_n_briding_comp vaginal_01:
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(0.5)

    n "al mismo tiempo que su vagina consume tu polla entera en cada embestida."

    # Labios hablando.

    $ ped_neus_whispers_sfx04 = 0.7

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with vpunch

    ne "No te resistas,"

    extend " y córrete conmigo."

    $ nteye = "front06"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with vpunch

    p "No voy a aguantar mucho más..."

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx10
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with vpunch

    ne "Dame un hijo [protname]."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx14
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with vpunch

    pause 0.2

    # Nalgas follándote. (Fondo ojos rojos?)

    $ p_ao_n_vel = 12
    $ p_ao_action_Cond = "nbVaginalRide_04"

    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat

    show closetocum_mc

    with Dissolve(0.5)

    if gensex_YoureAMonster:

        pt "¡Mierda!"

        pt "¡No puedo hacer nada!"

    $ renpy.music.set_volume(1.0, delay=1.0, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_post_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)
    $ p_ao_whispers_n = 5.0
    call p_ao_whispers_label

    n "Vuelves a sentir ese temblor,"

    $ renpy.music.set_volume(0.2, delay=8.0, channel='sfx1')

    $ ped_neus_whispers_sfx04 = 2.0

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front00"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    show closetocum_mc
    with vpunch

    n "sus ojos se iluminan con más intensidad,"

    $ nteye = "front08"
    show n_closefromup_mouth happybiting_Silentx14
    show n_closefromup_eyebrows sadx10
    call n_closefromup_tears_tears
    with vpunch

    pause 0.2

    # Techo oscuro ojos rojos

    # ##### ## Test

    # pause

    # scene p_ao_ride_comp 01:
    #     truecenter
    #     zoom 0.2

    # pause

    # ###

    #$ ped_neus_whispers_sfx04 = 0.5
    call p_ao_whispers_label

    $ p_ao_n_vel = 14
    $ p_ao_action_Cond = "nride07_anim"
    scene p_ao_ride_comp 01:
        subpixel True
        truecenter
        ypos 1.0
        block:
            easein 5.0/p_ao_n_vel ypos 0.5
            pause 0.5/p_ao_n_vel
            easeout 4.5/p_ao_n_vel ypos 0.75
            repeat

    show closetocum_mc

    with fade

    n "Crece el murmullo de esas voces extrañas,"

    n "y esos misteriosos orbes rojos proliferan entre la neblina y la oscuridad."

    # Nalgas Follándote.

    $ p_ao_n_vel = 14
    $ p_ao_action_Cond = "nbVaginalRide_04"

    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    show closetocum_mc
    with fade

    p "Uhh..."

    $ p_ao_n_vel = 20
    $ p_ao_action_Cond = "nbVaginalRide_04"

    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.4 # Down ALL IN
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    show closetocum_mc
    with Dissolve(0.5)

    # Corrida en su interior.

    window hide dissolve
    pause 1.5
    show cumming_mc
    pause 1.5

    $ p_ao_whispers_n = 0.1
    call p_ao_whispers_label

    scene black
    with fade

    n "Finalmente sientes tu esperma fluir por tu enorme y dolorido miembro sin que ella se detenga."

    # Nalgas parándose con tu corrida en su interior.

    # Techo # NOT FINISHED
    $ p_ao_n_vel = 3

    $ p_ao_action_Cond = "nride06_anim"
    show p_ao_ride_comp 01:
        ypos 1.0
        block:
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.5
            pause 1.0/p_ao_n_vel
            ease 5.0/p_ao_n_vel ypos 0.75
            repeat

    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0

    show morning04_bedroom_DMast_blinkeye

    show tired_mc

    with fade

    n "Sin apenas ser consciente,"

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    scene black
    with fade

    n "tus párpados se cierran."

    pause

    $ p_ao_n_dick_num += 1
    call p_ao_n_changes

    $ p_prot.orgasm += 1
    $ p_neus.orgasm += 1

    $ ped_neus_whispers_sfx04 = 0.2

######### Her First cumshot, Your Third Cumshot.
    play sound "audio/sfx/lickL01.ogg"
    ono "lick"
    play sound "audio/sfx/lickR01.ogg"
    extend " lick"
    play sound "audio/sfx/lickL02.ogg"
    extend " lick"

    p "¿Hhmmm...?"

    p "[neusname]..."

    p "¿Qué-"

    extend "qué estás haciendo?"

    if music_play != "fairytaleWaltz":
        play music "audio/music/kevinmacleod/sad/fairytaleWaltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "fairytaleWaltz"

    ## Illustration she Licks your middle-soft dick. A003

    $ p_ao_action_Cond = "lickBalls"

    scene gensex_oral_n_lick_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 
        ypos -2.0 # ChestDown
        easein 12.0 ypos 0.25 # Her tongue Close
    with fade

    n "Su abrasadora lengua acaricia tu -algo más blando- miembro."

    ne "Intento que se te vuelva a poner dura."

    p "Llevo tres corridas casi seguidas..."

    p "No-"

    extend "no creo que pueda seguir..."

    ne "Tonterías."

# ####
#     $ ped_neus_whispers_sfx04 = 1.0
#     $ p_ao_ghost_standing_resolution = ""
#     show gensex_oral_n_lick_comp_01:
#         truecenter
#         zoom 0.2
#     pause
#     $ p_ao_ghost_standing_resolution = "low"
#     show gensex_oral_n_lick_comp_01:
#         truecenter
#         zoom 0.2
#     pause
# ####

    show gensex_oral_n_lick_comp_01:
        ease_quad 6.0 zoom 0.6 ypos 0.3 # General View

    ne "Lo único que necesitas es un poco más de estimulación."

    $ p_ao_action_Cond = "lickStomach"
    show gensex_oral_n_lick_comp_01
    with Dissolve(1.0)

    p "¡Ey!"

    window hide dissolve
    pause

    ## ILLUSTRATION: Two finger touching your ass. A004
    scene p_ao_mc_ass_comp 01:
        subpixel True
        truecenter
        #zoom 0.2
        #zoom 1.0 xpos 1.5 ypos -0.5 # Left South Corner
        zoom 1.0 xpos 0.0 ypos 1.5 # Right North Corner?
        easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5 # Asshole Centered?
    with fade

    n "Dos de sus juguetones dedos trastean con tu parte trasera."

    p "¡¿Se puede saber qué estás haciendo?!"

    # Licks Again Illustration. A003
    scene gensex_oral_n_lick_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 
        ypos 0.25 # Her tongue Close
        easein_quad 20.0 zoom 0.6 ypos 0.3 # General View
    with fade

    ne "Tranquilo,"

    ne "tengo experiencia en esto,"

    ne "ya verás lo rápido que se te vuelve a poner bien dura."

    # FIngers ass again. A004
    scene p_ao_mc_ass_comp 02:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.5 ypos 0.5 # Asshole Centered?
        ease 10.0 zoom 0.75
    with fade


    # CHOICE

    menu:

        pt "¡¿Me quiere meter los dedos por el culo?!"

        "¡Te prohíbo que lo hagas!":
            call p_Help
            $pl.ch_pts("np",-1)

            ne "¿Me lo prohíbes?"

            if gensex_YoureAMonster:

                ne "¿No dices que soy un monstruo?"

                p "..."

        "Por favor, no lo hagas.":
            call p_Help

            ne "¿Tanto miedo tienes de que te haga daño,"

            ne "o es que tienes miedo de que te guste demasiado?"

        "...":
            call p_Help

    # #$ ped_neus_whispers_sfx04 = 0.2
    # ###
    # $ ped_neus_whispers_sfx04 = 1.0
    # ##

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front02"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with fade_short

    ne "¿Acaso quieres que use otra cosa que no sean mis dedos?"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    p "¿Qué...? "

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with dissolve

    p "¿De qué estás hablando?!"

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx13
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    ## She show you her Dick or just her pussy.

    if night05_Interrogation_UseYourDick_Cond or night04_NeusInterview_MenAttraction02_Answer_Maybe or gensex_YoureAMonster:
        $ p_ao_n_showDick = True

    if p_ao_n_showDick:
        $ p_ao_action_Cond = "nride01_p01"

    else:
        $ p_ao_action_Cond = "nride01"

    scene p_ao_ride_comp 01:
        subpixel True
        truecenter
        zoom 2.0
        ypos 3.3 # Top
        ease 10 ypos 2.5 # Before Dick
        #ypos 1.8 # Dick
    with fade_long1s

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    n "Apenas con fuerzas, inclinas tu cuello y descubres el cuerpo desnudo de [neusname],"

    n "cubierto en sudor, con una mirada espeluznante y..."

    # You're both still on the ground.

    if p_ao_n_showDick:

        jump p_neus_orgasmReal_dickgirl_label

    else:

        show p_ao_ride_comp 01:
            ease 5 ypos 1.8

        p "¡Me habías asustado!"

        if music_play != "bittersweet":
            play music "audio/music/kevinmacleod/bittersweet.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "bittersweet"

        play sound "audio/characters/neus/giggle05.ogg"

        ne "Jejeje..." # machiavelous childish giggle

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab
        show n_closefromup_body naked

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with fade_short

        ne "¿Esperabas otra cosa?"

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Del modo en que lo decías..."

        stop music fadeout 3.0

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo de que quiero que se te vuelva a poner dura lo decía muy en serio."

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx09
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        jump p_neus_orgasmReal_beforeAmazonic
        # n "Agarrándote del brazo te levanta del suelo"
        # p "¡Ugh!"
        # n "y te lanza sobre la cama."

label p_neus_orgasmReal_dickgirl_label:

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    show p_ao_ride_comp 01:
        ease 5 ypos 1.8
    
    p "¡¿Qué coño es eso?!"

    window hide dissolve
    pause

    ne "Sabes muy bien lo que es."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    
    if night05_Interrogation_UseYourDick_Cond == False and night04_NeusInterview_MenAttraction02_Answer_Maybe == False and gensex_YoureAMonster == True:

        $ p_neus_dickG_wants = False

        $ nteye = "front03"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with fade_short

        ne "¿Acaso no has dicho que soy un monstruo?"

        ne "Ahora verás lo monstruosa que puedo llegar a ser."

    else:

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx06
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade_short

        pause 0.2

        if night05_Interrogation_UseYourDick_Cond:

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "Esta noche parecías muy interesado"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "cuando me has preguntado si alguna vez había usado mi polla oscura para sodomizar a alguien."

            if night04_NeusInterview_MenAttraction02_Answer_Maybe == False:

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx08
                show n_closefromup_eyebrows angryx01
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Realmente tienes tanta curiosidad?"

        if night04_NeusInterview_MenAttraction02_Answer_Maybe:

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx005
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "Ayer, mientras esperábamos la cena,"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            ne "¿no me dijiste que te gustaría probarlo?"

            if night04_NeusInterview_MenAttraction02_Answer_Maybe_Hairy:

                $ nteye = "right01"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "Hasta me dijiste que te gustaban peludos y barbudos..."

            elif night04_NeusInterview_MenAttraction02_Answer_Maybe_Ambiguous:

                $ nteye = "right02"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "Hasta me dijiste que te gustaban con una fisonomía algo ambigua..."

            elif night04_NeusInterview_MenAttraction02_Answer_Maybe_Muscle:

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Hasta me dijiste que te gustaban machotes y con cierto músculo,"

                $ nteye = "right01"
                show n_closefromup_mouth sad_Talkingx002
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "de hecho, esa respuesta me hizo sospechar que quizás Dídac ya te gustaba antes de que se volviera mujer..."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Bien,"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "pues ahora es tu oportunidad."

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx06
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "¡¿Está hablando en serio?!"

            "¡Estaba hablando de forma hipotética!":
                call p_Help

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows suspiciousx01
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front04"
                show n_closefromup_mouth happy_Talkingx07
                show n_closefromup_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Pues yo hablo de forma práctica."

            "Me refería siendo yo el que penetra, no al revés.":
                call p_Help

                $ nteye = "front05"
                show n_closefromup_mouth happybiting_Silentx04
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "Te gusta ser dominante,"

                extend " ¿verdad?"

                $ nteye = "front01"
                show n_closefromup_mouth sadbiting_Silentx03
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                p "¿Algún problema con eso?"

                $ nteye = "right00"
                show n_closefromup_mouth sad_Talkingx002
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "Pues que a veces,"

                $ nteye = "front03"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                ne "a mi también me gusta dominar."

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx07
                show n_closefromup_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Especialmente cuando voy tan cachonda."

            "La verdad es que si es contigo, me gustaría probarlo.":
                call p_Help

                $ p_neus_dickG_wants = True

                $ nteye = "front00"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                if gensex_YoureAMonster:

                    $ nteye = "front03"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Ahora no soy un monstruo?"

                    $ nteye = "front04"
                    show n_closefromup_mouth sad_Silentx04
                    show n_closefromup_eyebrows angryx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "..."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No te creas que voy a ser suave contigo,"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx004
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "simplemente porque me has dicho esto."

                    $ nteye = "front04"
                    show n_closefromup_mouth happy_Talkingx06
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Quizás sea al contrario y todo."

                else:

                    $pl.ch_pts("np",2)

                    $ nteye = "front04"
                    show n_closefromup_mouth happy_Talkingx04
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿De verdad?"

                    $ nteye = "front06"
                    show n_closefromup_mouth happy_Talkingx06
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Cómo no me vas a poner caliente diciéndome estas cosas?"

            "...":
                call p_Help

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.3

    # ILLUSTRATION Little Neus Dick close to your anus. A004

    if p_neus_dickG_wants:
        if music_play != "deadly_roulette":
            play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "deadly_roulette"

    else:

        if music_play != "playWithMe":
            play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "playWithMe"

    $ p_ao_n_vel = 1
    scene p_ao_mc_ass_comp 03:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.5 ypos 0.6
        easein_quad 3.0 zoom 1.0 xpos 0.5 ypos 0.5
    with fade

    n "Percibes la punta de ese pequeño y oscuro falo acariciando tu agujero anal."

    if p_neus_dickG_wants:

        p "..."

    else:

        p "¡[neusname]!"

    ne "Tranquilo,"

    extend " he elegido un tamaño adecuado para no hacerte daño,"

    ne "al menos al principio..."

    ne "Ya verás cómo se te pone dura rápidamente."

    if p_neus_dickG_wants == False:

        p "¡Pero si ya has recibido mi corrida!"

        p "¡Y encima es posible que te haya dejado preñada!"

        p "¡¿No era eso lo que querías?!"

        if music_play != "malicious":
            play music "audio/music/neus_theme.ogg" fadein 0.5 fadeout 3.0
            $ music_play = "malicious"

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front02"
        show n_closefromup_mouth sad_Talkingx15
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with hpunch

        ne "¡Lo que quería es que te corrieras antes que yo!"

        $ nteye = "front01"
        show n_closefromup_mouth sad_Talkingx008
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¡Te dije que me hicieras caso,"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        ne "porque una vez logro un orgasmo...!"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "No..."

        $ nteye = "right03"
        show n_closefromup_mouth sad_Talkingx02
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "no puedo parar..."

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

    else:

        p "..."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with fade_short

    if p_neus_dickG_wants:
        if music_play != "deadly_roulette":
            play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "deadly_roulette"

    else:

        if music_play != "playWithMe":
            play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "playWithMe"

    ne "Estoy caliente,"

    extend " ardiendo,"

    extend " hambrienta..."

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx16
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Mataría a cualquiera que se interpusiera ahora mismo entre nosotros."

    $ nteye = "down02"
    show n_closefromup_mouth happybiting_Silentx11
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    ne "No me has querido hacer caso,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "así que no voy a parar hasta que esté satisfecha;"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "ahora ya no."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "¿Se está vengando o está aprovechando la excusa?"

        "¡Fóllame el trasero de una vez y déjate de excusas!" if gensex_YoureAMonster and p_neus_dickG_wants:
            call p_Help
            $pl.ch_pts("np",1)

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx01
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            ne "Hmmm..."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "No sabía esa cara oculta de ti, [protname]."

            $ nteye = "front02"
            show n_closefromup_mouth happy_Silentx07
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            pt "¡¿PERO QUÉ PUTAS POLLAS ME PASA?!"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Pero tranquilo,"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx09
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "ya tenía pensado follarte bien duro,"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx07
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "pero empezaré despacio."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "por muy gallito que te hagas,"

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            pt "¡¿ES QUE ME HE VUELTO LOCO?!"

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx05
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "sé que eres virgen y no quiero que te desmayes demasiado pronto."

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            pt "¡¿POR QUÉ COÑO LE HE DICHO ESTO?!"

        "¿Es que acaso intentas justificarte?" if gensex_YoureAMonster:
            call p_Help

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            ne "Para nada,"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx10
            show n_closefromup_eyebrows suspiciousx01
            call n_closefromup_tears_tears
            with dissolve

            ne "simplemente te estoy preparando para lo que te haré."

            $ nteye = "down05"
            show n_closefromup_mouth happybiting_Silentx07
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

        "Solo quería hacerte disfrutar este momento tanto como yo." if gensex_YoureAMonster == False:
            call p_Help
            $pl.ch_pts("np",1)

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "Oh..."

            $ nteye = "front07"
            show n_closefromup_mouth happy_Talkingx09
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "y lo he disfrutado,"

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx07
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "no te quepa la menor duda."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx07
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            p "¿Entonces?"

            $ nteye = "front00"
            show n_closefromup_mouth happy_Talkingx14
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Quiero que disfrutes de lo mismo."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx10
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

        "Así solo me demuestras que tengo razón. Eres un monstruo." if gensex_YoureAMonster and p_neus_dickG_wants == False:
            call p_Help

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex03
            call n_closefromup_tears_tears
            with dissolve

            ne "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx004
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "¿Acaso te he dicho lo contrario?"

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx10
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

        "Lo siento." if not gensex_YoureAMonster:
            call p_Help
            $pl.ch_pts("np",1)

            if gensex_YoureAMonster:

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve


                ne "..."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Lamentas no haberme hecho caso,"

                $ nteye = "front00"
                show n_closefromup_mouth sad_Talkingx007
                show n_closefromup_eyebrows suspiciousx01
                call n_closefromup_tears_tears
                with dissolve

                ne "o haberme llamado monstruo?"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Silentx07
                show n_closefromup_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                p "..."

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "No pasa nada [protname],"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx07
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with dissolve

            ne "no estoy enfadada,"

            $ nteye = "front00"
            show n_closefromup_mouth happy_Talkingx17
            show n_closefromup_eyebrows serious
            call n_closefromup_tears_tears
            with dissolve

            ne "tan solo estoy realmente caliente."

            $ nteye = "front01"
            show n_closefromup_mouth happy_Silentx11
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

        "...":
            call p_Help

    if p_neus_dickG_wants == False:

        menu:

            pt "¡¿En serio me va a follar el culo?!"

            "¡¿Es que acaso quieres violarme?!":
                call p_Help
                $pl.ch_pts("np",-1)

                stop music fadeout 1.0

                $ nteye = "front00"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                ne "..."

                if gensex_YoureAMonster:

                    if music_play != "rightBehindYou":
                        play music "audio/music/kevinmacleod/creepy/rightBehindYou.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "rightBehindYou"

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx002
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Acaso no es obvio?"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx04
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Tú lo has dicho,"

                    extend " ¿no?"

                    $ nteye = "front03"
                    show n_closefromup_mouth happy_Talkingx16
                    show n_closefromup_eyebrows angryx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Soy un monstruo."

                    $ nteye = "front05"
                    show n_closefromup_mouth happy_Silentx10
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                elif pl.np > 150: # NOT FINISHED how many points should be here?

                    if music_play != "wounded":
                            play music "audio/music/kevinmacleod/sad/wounded.ogg" fadein 3.0 fadeout 3.0
                            $ music_play = "wounded"

                    $ nteye = "right02"
                    show n_closefromup_mouth sad_Talkingx003
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No..."

                    $ nteye = "left03"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo que quiero es ponértela dura y que lo disfrutes tanto como yo."

                    $ nteye = "front01"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pues haciendo algo en contra de mi voluntad,"

                    extend " no es la manera."

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx10
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¡Yo también te he pedido que parases"

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx13
                    show n_closefromup_eyebrows angryx04
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "y has acabado haciendo lo que te ha dado la gana!"

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx10
                    show n_closefromup_eyebrows suspiciousx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¿Acaso no ves la diferencia?"

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx08
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right04"
                    show n_closefromup_mouth sadbiting_Silentx07
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡A ti te estaba encantando!"

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Silentx07
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    p "¡Esa es la diferencia!"

                    $ nteye = "right05"
                    show n_closefromup_mouth sadbiting_Silentx09
                    show n_closefromup_eyebrows sadx08
                    call n_closefromup_tears_tears
                    with dissolve

                    p "No querías que continuara por que te disgustase,"

                    $ nteye = "front05"
                    show n_closefromup_mouth sadbiting_Silentx10
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    p "si no por todo lo contrario."

                    $ nteye = "left04"
                    show n_closefromup_mouth sadbiting_Silentx12
                    show n_closefromup_eyebrows sadx09
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pero lo que tú pretendes hacerme,"

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx15
                    show n_closefromup_eyebrows sadx10
                    call n_closefromup_tears_tears
                    with dissolve

                    p "es por puro egoísmo."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx02
                    show n_closefromup_eyebrows sadx08
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "No,"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx006
                    show n_closefromup_eyebrows sadx07
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "eso no es verdad..."

                    $ nteye = "front04"
                    show n_closefromup_mouth happy_Talkingx03
                    show n_closefromup_eyebrows sadx08
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Sé que también te gustará."

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx02
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "No opino lo mismo."

                    $ nteye = "front03"
                    show n_closefromup_mouth sadbiting_Silentx04
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "..."

                    $ nteye = "right02"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Qui-"

                    extend "quizás tengas razón..."

                    $ nteye = "right05"
                    show n_closefromup_mouth sad_Talkingx03
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo siento..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "es que cuando tengo un orgasmo,"

                    $ nteye = "right01"
                    show n_closefromup_mouth sad_Talkingx09
                    show n_closefromup_eyebrows sadx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "me-"

                    extend "me desboco,"

                    $ nteye = "front02"
                    show n_closefromup_mouth sad_Talkingx07
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "me pongo demasiado cachonda."

                    $ nteye = "front05"
                    show n_closefromup_mouth sad_Talkingx05
                    show n_closefromup_eyebrows sadx05
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Lo siento [protname]."

                    $ nteye = "front08"
                    show n_closefromup_mouth sadbiting_Silentx10
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    p "No pasa nada."

                    $ nteye = "front03"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx02
                    call n_closefromup_tears_tears
                    with dissolve

                    p "Pero por favor,"

                    $ nteye = "front01"
                    show n_closefromup_mouth sad_Silentx03
                    show n_closefromup_eyebrows surprisex01
                    call n_closefromup_tears_tears
                    with dissolve

                    p "aleja eso de mi trasero..."

                    $ nteye = "down00"
                    show n_closefromup_mouth sad_Talkingx001
                    show n_closefromup_eyebrows surprisex03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "¿Uh...?"

                    $ nteye = "front06"
                    show n_closefromup_mouth happy_Talkingx05
                    show n_closefromup_eyebrows sadx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Sí..."

                    $ nteye = "down05"
                    show n_closefromup_mouth sadbiting_Silentx05
                    show n_closefromup_eyebrows sadx06
                    call n_closefromup_tears_tears
                    with dissolve

                    pause 0.2

                    $ p_ao_n_vel = 3

                    $ p_ao_action_Cond = "nride01_move"
                    show p_ao_ride_comp 01:
                        truecenter
                        zoom 2.0 ypos 1.6
                    with fade_long1s

                    p "¿[neusname]?"

                    if music_play != "fairytaleWaltz":
                        play music "audio/music/kevinmacleod/sad/fairytaleWaltz.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "fairytaleWaltz"

                    $ p_ao_n_vel = 2
                    show p_ao_ride_comp 01
                    with dissolve

                    ne "Lo siento..."

                    ne "pero sigo estando tremendamente caliente"

                    $ p_ao_n_vel = 4
                    show p_ao_ride_comp 01
                    with dissolve

                    ne "y necesito que se te ponga dura."

                    $ p_prot_aoNight_analReceived = "False"

                    jump p_neus_orgasmReal_beforeAmazonic
                    # n "Agarrándote del brazo te levanta del suelo"
                    # p "¡Ugh!"
                    # n "y te lanza sobre la cama."

                else:

                    if music_play != "airPrelude":
                        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
                        $ music_play = "airPrelude"

                    $ nteye = "front02"
                    show n_closefromup_mouth happy_Talkingx05
                    show n_closefromup_eyebrows angryx01
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "Relájate,"

                    if gensex_ILoveYouNeus:

                        extend " mi amor..."

                    else:

                        extend " mi querido Lancelot..."

                    $ nteye = "front08"
                    show n_closefromup_mouth sad_Talkingx005
                    show n_closefromup_eyebrows surprisex02
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "En el fondo,"

                    $ nteye = "front01"
                    show n_closefromup_mouth happy_Talkingx10
                    show n_closefromup_eyebrows suspiciousx03
                    call n_closefromup_tears_tears
                    with dissolve

                    ne "sé que te va a gustar."

                    $ nteye = "front03"
                    show n_closefromup_mouth happy_Silentx07
                    show n_closefromup_eyebrows angryx03
                    call n_closefromup_tears_tears
                    with dissolve

            "...":

                $ nteye = "down05"
                show n_closefromup_mouth happybiting_Silentx14
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                pause 0.1

                call p_Help


    #########################################################

    if config.version < "00.99.99": # You're being raped.
        call endupdatescript
    
    #######################################################

    pause 0.3

    $ p_prot_aoNight_analReceived = "True"

    if p_neus_dickG_wants:
        if music_play != "twisted":
            play music "audio/music/kevinmacleod/twisted.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "twisted"
    else:

        if music_play != "morgana_rides":
            play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "morgana_rides"

    $ p_ao_n_vel = 1
    scene p_ao_mc_ass_comp 03:
        subpixel True
        truecenter
        zoom 0.75 xpos 0.5 ypos 0.6
        easein_quad 3.0 zoom 1.5 xpos 0.48 ypos 0.7 # Close Asshole
    with fade

    pause 0.5

    play sound "audio/sfx/fall02.ogg"

    $ p_ao_mc_dick_num = 1
    $ p_ao_n_hipsImg = "_open"
    $ p_ao_n_hipsTrans = 0.0

    $ p_ao_action_Cond = "02_stop_trans"
    show p_ao_mc_ass_comp 04:
        truecenter
        # zoom 1.5 xpos 0.48 ypos 0.7 # Close Asshole
        # ease 15.0 zoom 0.5 xpos 0.45 ypos 0.5 # Far Asshole (ForSmallCock)
        #zoom 0.5 xpos 0.4 ypos 0.6 # Far Asshole (ForBigCock)

        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with hpunch
    with hpunch

# ####### TEST
#     $ p_ao_n_vel = 20
#     $ p_ao_action_Cond = "06"
#     $ saturation_tint_level = "default" # NOT FINISHED, just for test.
#     show p_ao_mc_ass_comp 04:
#         truecenter
#         zoom 0.5
#     progcheck "06"

#     $ p_ao_action_Cond = "05"
#     show p_ao_mc_ass_comp 04
#     progcheck "05"

#     $ p_ao_action_Cond = "01"
#     show p_ao_mc_ass_comp 04
#     progcheck "01"

#     $ p_ao_action_Cond = "03"
#     show p_ao_mc_ass_comp 04
#     progcheck "03"

#     $ p_ao_action_Cond = "02"
#     show p_ao_mc_ass_comp 04
#     progcheck "02"

#     $ p_ao_action_Cond = "04"
#     show p_ao_mc_ass_comp 04
#     progcheck "04"
# ########

    p "¡Ugh!"

    ne "HMmmm..."

    $ p_ao_mc_dick_num = 1
    $ p_ao_n_hipsTrans = 1.0
    $ p_ao_ground = "bed" # Is he now on bed?
    show p_ao_mc_ass_comp 04:
        easein_quad 8.0 zoom 0.5 xpos 0.45 ypos 0.5 # Far Asshole (ForSmallCock)
    with Dissolve(2.0)

    n "Ardiente, dura, pero al mismo tiempo carnosa,"

    n "Detectas su pequeña -pero tersa- polla en tu ceñido y apenas lubricado ano."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx13
    show n_closefromup_eyebrows suspiciousx04
    call n_closefromup_tears_tears
    with fade

    ne "¿Qué se siente al perder la virginidad [protname]?"

    if p_neus_dickG_wants:

        $ nteye = "down05"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Hmmmm..."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Vaya,"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx09
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        ne "Cualquiera diría que lo estás disfrutando y todo..."

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx09
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx07
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        pt "¡La madre que la...!"

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx09
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

    $ p_ao_mc_dick_num = 2
    $ p_ao_n_hipsTrans = 0.5
    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "02"

    play sound "audio/sfx/fall02.ogg"

    show p_ao_mc_ass_comp 04:
        truecenter
        # zoom 1.5 xpos 0.48 ypos 0.7 # Close Asshole
        # ease 15.0 zoom 0.5 xpos 0.45 ypos 0.5 # Far Asshole (ForSmallCock)
        #zoom 0.5 xpos 0.4 ypos 0.6 # Far Asshole (ForBigCock)
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
            easeout 4.0/p_ao_n_vel zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
            repeat
    with hpunch
    with hpunch

    n "Paulatinamente empieza a desplazarse."

    ne "Realmente estás bien estrecho aquí dentro."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with fade

    ne "¿No habías jugado nunca antes con tu trasero?"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Ni siquiera con los dedos?"

    if p_neus_dickG_wants:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        p "La-"

        extend "la verdad es que no..."

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Siempre hay una primera vez..."

    else:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx01
        show n_closefromup_eyebrows surprisex04
        call n_closefromup_tears_tears
        with dissolve

        p "¡No es lo que me gusta!"

    $ nteye = "down03"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Mira tu polla."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx06
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2


# ###### TEST
#     $ p_ao_mc_dick_num = 1
#     scene p_ao_mc_ass_comp 04:
#         truecenter
#         zoom 0.2
#     progcheck "01"
#     $ p_ao_mc_dick_num = 2
#     show p_ao_mc_ass_comp 04
#     progcheck "02"
#     $ p_ao_mc_dick_num = 3
#     show p_ao_mc_ass_comp 04
#     progcheck "03"
#     $ p_ao_mc_dick_num = 4
#     show p_ao_mc_ass_comp 04
#     progcheck "04"
#     $ p_ao_mc_dick_num = 5
#     show p_ao_mc_ass_comp 04
#     progcheck "05"
#     $ p_ao_mc_dick_num = 6
#     show p_ao_mc_ass_comp 04
#     progcheck "06"
# ######

    $ p_ao_mc_dick_num = 1
    $ p_ao_n_hipsTrans = 1.0
    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "02"

    play sound "audio/sfx/fall02.ogg"

    scene p_ao_mc_ass_comp 04:
        subpixel True
        truecenter
        # zoom 1.5 xpos 0.48 ypos 0.7 # Close Asshole
        # ease 15.0 zoom 0.5 xpos 0.45 ypos 0.5 # Far Asshole (ForSmallCock)
        #zoom 0.5 xpos 0.4 ypos 0.6 # Far Asshole (ForBigCock)
        # zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        # block:
        #     easein 4.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
        #     easeout 4.0/p_ao_n_vel zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        #     repeat

        #zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
        zoom 1.5 xpos 0.48 ypos 0.7 # Close Asshole
        easein_quad 10.0 zoom 0.75 xpos 1.25 ypos 1.25 # Focus on Dick.

    n "En pequeñas olas, experimentas el impulso sanguíneo de tu entrepierna fluyendo hacia tu falo"

    $ p_ao_mc_dick_num = 2
    $ p_ao_n_vel = 3
    show p_ao_mc_ass_comp 04
    with Dissolve(1.5)

    n "que poco a poco consigue recuperar su erección."

    $ p_ao_mc_dick_num = 3
    $ p_ao_n_vel = 4
    show p_ao_mc_ass_comp 04
    with Dissolve(1.5)

    if p_neus_dickG_wants:

        pt "Realmente se me está poniendo dura..."

    else:

        pt "Puta polla..."

    ne "¡Y ni siquiera te la estoy tocando!"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    if p_neus_dickG_wants:

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade

        ne "Al final serás más sumiso de lo que pensaba."

    else:

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx07
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade

        ne "Quizás te gusta más de lo que tu orgullo varonil es capaz de admitir..."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx10
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    p "..."

    if p_neus_dickG_wants == False:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        p "¡Una cosa es cómo mi cuerpo reaccione,"

        $ nteye = "front02"
        show n_closefromup_mouth sad_Silentx03
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        p "y la otra muy distinta es lo que realmente quiero hacer!"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        ne "Bueno,"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows surprisex04
        call n_closefromup_tears_tears
        with dissolve

        ne "te di la opción a elegir;"

        $ nteye = "front02"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "y elegiste darme el control."

        $ nteye = "front00"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Elegí darte placer y un orgasmo,"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Silentx06
        show n_closefromup_eyebrows angryx01
        call n_closefromup_tears_tears
        with dissolve

        p "no creo que eso fuera una elección precisamente egoísta."

        $ nteye = "right05"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Tienes razón,"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows surprisex03
        call n_closefromup_tears_tears
        with dissolve

        ne "pero no puedes culparme ahora por querer darte lo mismo."

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Así que no te quejes tanto,"

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx14
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "y disfruta."

        $ ped_neus_whispers_sfx04 = 0.95

        $ nteye = "front00"
        show n_closefromup_mouth happy_Silentx11
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        p "No..."



    else:

        $ nteye = "down05"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "Te gusta,"

        $ nteye = "down03"
        show n_closefromup_mouth happy_Talkingx10
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¿verdad que sí?"

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Perra..."

        $ nteye = "down05"
        show n_closefromup_mouth happy_Silentx09
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "¿Si me gusta que me esté dando por detrás?"

            "Por favor, se delicada...":
                call p_Help

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows normal
                call n_closefromup_tears_tears
                with dissolve

                ne "Tranquilo,"

                $ nteye = "front02"
                show n_closefromup_mouth happy_Talkingx04
                show n_closefromup_eyebrows sadx01
                call n_closefromup_tears_tears
                with dissolve

                ne "como te he dicho,"

                $ nteye = "front03"
                show n_closefromup_mouth happy_Talkingx08
                show n_closefromup_eyebrows angryx01
                call n_closefromup_tears_tears
                with dissolve

                ne "sé lo que me hago."



            "No pares..." if p_neus_dickG_wants:
                call p_Help

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "No tenía ninguna intención de parar..."

            "¡Dame más caña!" if p_neus_dickG_wants:
                call p_Help

                $ nteye = "front01"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                pt "¡¿Que me de más caña?!"

                $ nteye = "front03"
                show n_closefromup_mouth happy_Silentx08
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                pt "¡¿Estoy gilipollas o qué me pasa?!"

                $ nteye = "front08"
                show n_closefromup_mouth happy_Silentx05
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

            "...":
                call p_Help

    $ ped_neus_whispers_sfx04 = 0.95
    $ nteye = "front00"
    show n_closefromup_mouth happy_Silentx11
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2


    if p_neus_dickG_wants:
        if music_play != "loopster":
            play music "audio/music/kevinmacleod/happy/loopster.ogg" fadein 0.5 fadeout 0.5
            $ music_play = "loopster"
    else:

        if music_play != "malicious":
            play music "audio/music/kevinmacleod/malicious.ogg" fadein 0.5 fadeout 0.5
            $ music_play = "malicious"


####
    $ ped_neus_whispers_sfx04 =  0.3
    $ p_ao_mc_dick_num = 2
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_n_vel = 5
    $ p_ao_action_Cond = "02"

    play sound "audio/sfx/fall02.ogg"

    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
            easeout 4.0/p_ao_n_vel zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
            repeat
    with hpunch
    with hpunch
    with vpunch
    with vpunch

    p "¡Uugh!"

    n "Sin darte tiempo a responder,"

    n "acelera ligeramente sus embestidas sintiendo su abrasadora polla penetrándote a más profundidad."

    ne "Tranquilo,"

    extend " no te dolerá,"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with fade

    ne "al menos no mucho..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "El sudor de mi cuerpo crea un tipo de lubricante"

    $ nteye = "front07"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with dissolve

    ne "que ayuda a que quizás no te cause ningún desgarro."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    if p_neus_dickG_wants:

        p "¡Me está ardiendo por dentro!"

    else:

        p "¡Me estás quemando el culo!"

    $ nteye = "left01"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "Por eso he dicho quizás..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Silentx06
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_n_vel = 1
    $ p_ao_n_hipsTrans = 0.0
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
            easeout 4.0/p_ao_n_vel zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
            repeat
    with fade

    n "Te sujeta por las nalgas -y con una fuerza sobrehumana-"

    n "te levanta del suelo manteniendo su polla dentro de ti,"

    n "Mientras te sujeta ambas piernas, da unos pasos hacia la cama"

    play sound "audio/sfx/hit02.ogg"

    scene black
    with vpunch
    # scene p_ao_nRap_ankles_back:
    #     truecenter
    #     zoom 2.0 xpos 0.5 ypos -0.2 #  Stomach
    #     #zoom 2.0 xpos 1.7 ypos -1.5 #His Face
    #     easein_quad 1.0zoom 1.5 xpos 1.4 ypos -1.1 # HIs face
    # #with vpunch
    p "¡Ugh!"

    n "y luego te lanza sobre ella."

    play sound "audio/sfx/fall02.ogg"

    # not finished, your ankle over her shoulders, she is on feet, teasing your ass.
    $ p_ao_action_b_Cond = "back"
    scene p_ao_nRap_ankles_02 general_comp_01: # Her hand on your leg.
        truecenter
        zoom 2.0 xpos 0.7 ypos 0.9
    with vpunch
    n "Te agarra de las piernas y arrastra tu trasero hasta el borde de la cama."

    show p_ao_nRap_ankles_02 general_comp_01:
        #truecenter
        zoom 2.0 xpos 1.55 ypos 0.55 # MCface
    with fade

    p "¡¿Qué qué estás haciendo?!"

    #show p_ao_nRap_ankles_02_back:
    $ p_ao_action_b_Cond = "back"
    show p_ao_nRap_ankles_02 general_comp_01:
        subpixel True
        #zoom 2.0 xpos -0.5 ypos -0.7 # Neus Ass
        ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5 # Whole picture

    n "Estando delante de tu entrepierna y de pie,"

    n "levanta tus piernas y posa tus rodillas sobre sus hombros al contacto con sus mejillas,"

# ################# TEST
#     $ ped_neus_whispers_sfx04 = 1.0
#     $ p_ao_n_vel = 5

#     $ p_ao_action_b_Cond = "back"
#     scene p_ao_nRap_doggy general_comp_01:
#         truecenter
#         zoom 0.34 xpos 0.5 ypos 0.5 # Whole picture
#         ease 10.0 zoom 1.0
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggy_back_comp_01"

#     $ p_ao_action_b_Cond = "front"
#     show p_ao_nRap_doggy general_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggy_front_comp_01"

#     show p_ao_nRap_doggy anim_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggy_anim_comp_01"


#     ###
#     $ p_ao_action_b_Cond = "back"
#     scene p_ao_nRap_doggyHard general_comp_01:
#         truecenter
#         zoom 0.34 xpos 0.5 ypos 0.5 # Whole picture
#         ease 10.0 zoom 1.0
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggyHard_general_comp_01"

#     $ p_ao_action_b_Cond = "front"
#     show p_ao_nRap_doggyHard general_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggyHard_general_comp_01"

#     show p_ao_nRap_doggyHard anim_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_doggyHard_anim_comp_01"

#     ###
#     $ p_ao_action_b_Cond = "back"
#     scene p_ao_nRap_ankles_02 general_comp_01:
#         truecenter
#         zoom 0.4 xpos 0.5 ypos 0.5 # Whole picture
#         ease 10.0 zoom 1.0
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_ankles_02_general_comp_01_back"

#     $ p_ao_action_b_Cond = "front"
#     show p_ao_nRap_ankles_02 general_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_ankles_02_general_comp_01_front"
    
#     show p_ao_nRap_ankles_02 anim_comp_01
#     with Dissolve(0.5)
#     progcheck "p_ao_nRap_ankles_02_anim_comp_01"
# #################

    n "con su pequeña -pero palpitante- polla rozándote tu afligido y rojizo ano."

    window hide dissolve
    pause

    #show p_ao_nRap_ankles_02_back:
    $ p_ao_action_b_Cond = "back"
    scene p_ao_nRap_ankles_02 general_comp_01:
        truecenter
        zoom 1.5 xpos 0.3 ypos 1.4 # Neusface
    with dissolve

    ne "Así entrará mejor y estoy más cómoda."

    n "Usando tus piernas como anclaje,"

    $ p_ao_n_vel = 7
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_action_Cond = "02_stop"

    play sound "audio/sfx/fall02.ogg"

    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    with vpunch
    p "¡Ugh!"

    n "vuelve a metértela"

    n "con la misma velocidad pero con más hincapié al penetrarte."


    $ p_ao_n_vel = 3
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_action_Cond = "02_stop"
    play sound "audio/sfx/fall02.ogg"

    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    p "Ugh,"

    $ p_ao_n_vel = 6
    play sound "audio/sfx/fall02.ogg"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    extend " ugh,"

    $ p_ao_n_vel = 12
    play sound "audio/sfx/fall02.ogg"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    extend " ugh..."

    $ p_ao_n_vel = 3


###
    
    # scene p_ao_nRap_ankles_02_comp_01:
    #     truecenter
    #     zoom 2.0 xpos -0.5 ypos -0.7 # Neus Ass
    #     easein_quad 15.0 zoom 0.6 xpos 0.5 ypos 0.5 # Image but closer
    #     #ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5 # Whole picture
    # with fade

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade

    ne "Puedes quejarte tanto como desees,"

    if gensex_ILoveYouNeus:

        extend " mi amor,"

    elif gensex_YoureAMonster:

        extend " perra,"

    else:

        extend " mi querido Lancelot,"

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    if p_neus_dickG_wants:

        ne "A pesar de tus gruñidos,"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx11
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "parece que te está gustando más de lo que me imaginaba."

    else:

        ne "a pesar de que te cueste admitirlo,"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx10
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "desde luego,"

        extend " físicamente lo estás disfrutando,"

    # $ Pedrera_char_Cond = "NeusSuperClose"
    # call Pedrera_char_lab

    # show n_closefromup_body naked

    # $ nteye = "front03"
    # show n_closefromup_mouth happy_Talkingx08
    # show n_closefromup_eyebrows sadx01
    # call n_closefromup_tears_tears
    # with fade


    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "a la vista está."

    $ nteye = "down03"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Tu polla vuelve estar realmente tensa y dura..."

    if p_neus_dickG_wants and gensex_YoureAMonster == False:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Lo siento,"

        extend " pero es que duele un poco..."

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo siento cariño,"

        $ nteye = "front02"
        show n_closefromup_mouth happy_Talkingx07
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "te prometo que pronto sentirás más placer."

    elif not p_neus_dickG_wants:

        $ nteye = "front03"
        show n_closefromup_mouth happybiting_Silentx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pt "¡Maldita polla!"

    else:

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx06
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        p "¡Lo dices cómo si pudiera controlarlo!"

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx11
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmm..."

    $ ped_neus_whispers_sfx04 = 0.9

    $ nteye = "down02"
    show n_closefromup_mouth happy_Silentx10
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ ped_neus_whispers_sfx04 = 0.3
    $ n_exp_shine = 0.005


    if p_neus_dickG_wants:
        if music_play != "playWithMe":
            play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "playWithMe"
    else:

        if music_play != "darkestChild":
            play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "darkestChild"

    # Tongue Touching you While fucking your ass.
    $ p_ao_n_vel = 1
    $ p_ao_n_hipsTrans = 0.95
    $ p_ao_action_Cond = "02"
    $ p_ao_action_b_Cond = "tongueAss00"
    scene p_ao_mc_ass_comp 04:
        subpixel True
        truecenter
        zoom 0.75 xpos 1.25 ypos 1.25 # Focus on Dick.
        ease 10.0 zoom 0.5 xpos 0.83 ypos 0.83 # Show all picture?
    with fade

    pt "¡¿Qué demonios hace ahora?!"

    n "El tacto ardiente de su lengua acaricia tu erecta polla sin dejar de embestirte."

    if night04_pedrera_blowjob_DONE:

        pt "Otra vez su monstruosa lengua..."

    else:

        if p_neus_dickG_wants:

            pt "¡¿Pero cuánto le mide la lengua?!"

        else:

            pt "¡¿Pero cuánto le mide la lengua a esta?!"

    ne "Ya sabes que me encanta el sabor,"

    ne "además creo que esto te gustará."

    $ p_ao_n_vel = 24
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_action_Cond = "02_stop"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    with vpunch
    play sound "audio/sfx/slap02.ogg"
    ono "SPLASH"
    $ p_ao_n_vel = 48
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_action_Cond = "02_stop"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    with vpunch
    play sound "audio/sfx/slap03.ogg"
    extend " SPLASH"
    $ p_ao_n_vel = 64
    $ p_ao_n_hipsTrans = 0.0
    $ p_ao_action_Cond = "02_stop"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.8 xpos 0.5 ypos 0.75 # 02 Out
        easein 12.0/p_ao_n_vel zoom 2.5 xpos 0.95 ypos 0.85 # 02 In
    with vpunch
    with vpunch
    play sound "audio/sfx/slap02.ogg"
    extend " SPLASH"

    $ p_ao_n_vel = 12
    $ p_ao_action_Cond = "02"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 1.5 xpos 0.6 ypos 0.6 # 03 In
            easeout 4.0/p_ao_n_vel zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
            repeat
    with dissolve

    n "Padeces repetidamente el duro impacto de sus caderas chocando contra tus nalgas."

    ne "Es hora de darle un poco más de forma."

    if p_neus_dickG_wants:
        if music_play != "loopster":
            play music "audio/music/kevinmacleod/loopster.ogg" fadein 1.0 fadeout 1.0
            $ music_play = "loopster"
    else:

        if music_play != "movementProposition":
            play music "audio/music/kevinmacleod/fast/movementProposition.ogg" fadein 1.0 fadeout 1.0
            $ music_play = "movementProposition"

    $ p_ao_action_Cond = "03"
    $ p_ao_n_vel = 20
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 1.5 xpos 0.6 ypos 0.6 # 03 In
            easeout 4.0/p_ao_n_vel zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
            repeat
    with Dissolve(1.5)

    n "al mismo tiempo que te percatas de que su polla aumenta -ligeramente- de tamaño en cada embestida."

    p "[neusname]..."

    ne "Un poco más grande no te hará ningún daño..."

    $ p_ao_n_vel = 5
    scene p_ao_POVnFuckingYou:
        subpixel True
        truecenter
        #zoom 0.2
        #zoom 1.5 xpos 0.5 ypos -0.8 # Down
        #zoom 1.5 xpos 0.5 ypos 1.0 # Up dick.
        zoom 1.2 xpos 0.5 ypos 0.0 # Base Dick
        easein_quad 15.0 zoom 0.75 xpos 0.5 ypos 0.5 # Whole image visible
    with fade

    n "Su longeva lengua rodea tu enorme pollón y poco después, empieza a mecerla."

    if p_neus_dickG_wants:

        p "E-"

        extend "estoy a..."

    else:

        pt "¡La madre que la parió!"

    pause

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with fade

    ne "Estás a punto de nuevo,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx10
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "¿verdad?"

    $ nteye = "down04"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Menos mal que no podías volver a tenerla dura..."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    play sound "audio/sfx/hit02.ogg"

    #show p_ao_nRap_ankles_02_back: # Her hand on your leg.
    $ p_ao_action_b_Cond = "back"
    scene p_ao_nRap_ankles_02 general_comp_01:
        truecenter
        zoom 2.0 xpos 0.7 ypos 0.9
    with vpunch

    # scene p_ao_nRap_ankles_back:
    #     truecenter
    #     zoom 2.0 xpos 0.7 ypos 0.9
    #     # truecenter
    #     # zoom 2.0 xpos -0.5 ypos -0.7 # Neus Ass
    #     # easein_quad 15.0 zoom 0.6 xpos 0.5 ypos 0.5 # Image but closer
    #     # #ease 10.0 zoom 0.4 xpos 0.5 ypos 0.5 # Whole picture
    # with fade

    n "Agarrándote de nuevo de las piernas con fuerza,"

    $ p_ao_action_Cond = "03"
    $ p_ao_n_vel = 1
    $ p_ao_action_b_Cond = ""
    $ p_ao_n_hipsTrans = 0.0
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 1.5 xpos 0.6 ypos 0.6 # 03 In
            easeout 4.0/p_ao_n_vel zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
            repeat
        zoom 0.2
    with fade
    
    n "se impulsa para hacértela sentir bien dura hasta el fondo."

    $ p_ao_action_Cond = "04"
    show p_ao_mc_ass_comp 04:
        truecenter
        zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
        block:
            easein 4.0/p_ao_n_vel zoom 1.5 xpos 0.6 ypos 0.6 # 03 In
            easeout 4.0/p_ao_n_vel zoom 1.0 xpos 0.4 ypos 0.55 # 02 Out
            repeat
    with Dissolve (1.5)

    p "¡Te-"

    extend "te está creciendo!"

    # scene p_ao_nRap_ankles_02_comp_01:
    #     truecenter
    #     zoom 2.0 xpos -0.5 ypos -0.7 # Neus Ass
    #     easein_quad 15.0 zoom 0.6 xpos 0.5 ypos 0.5 # Image but closer
    # with fade

    ne "La tuya es como cuatro veces más grande que lo que tienes ahora mismo en tu trasero,"

    ne "así que no te quejes tanto."

    #$ ped_neus_whispers_sfx04 = 0.4
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    if p_neus_dickG_wants:

        $ nteye = "front00"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with fade

        p "No me estoy quejando..."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx08
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        p "Hmmm..."

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx09
        show n_closefromup_eyebrows normal
        call n_closefromup_tears_tears
        with dissolve

        ne "Así me gusta."

    else:

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with fade

        ne "Aunque también es verdad que es tu primera vez..."

        $ nteye = "down03"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Pero no parece que te esté disgustando."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx09
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_background = "pedrera"
    if p_neus_dickG_wants:
        if music_play != "nonstop":
            play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "nonstop"
    else:

        if music_play != "movementProposition":
            play music "audio/music/kevinmacleod/fast/movementProposition.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "movementProposition"


    $ p_ao_n_vel = 7
    scene p_ao_POVnFuckingYou:
        subpixel True
        truecenter
        #zoom 0.2
        #zoom 1.5 xpos 0.5 ypos -0.8 # Down
        #zoom 1.5 xpos 0.5 ypos 1.0 # Up dick.
        zoom 1.2 xpos 0.5 ypos 0.0 # Base Dick
        easein_quad 15.0 zoom 0.75 xpos 0.5 ypos 0.5 # Whole image visible
    show closetocum_mc
    with fade

    n "Experimentas el cosquilleo previo a una nueva erupción."

    p "[neusname]..."

    n "De la comisura de sus labios eres capaz de percibir el brillo de una gota que empieza a descender por su barbilla."

    p "¡Ugh!"

    # She deepthroats your dick. # Ground shouldn't be visible here: # NOT FINISHED
    scene black
    $ ped_sex_general_zoom_Cond = "faceCentered"
    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_action_Cond = "o04_04"
    $ p_prot.pos = "oral"
    $ ped_sex_general_expressionJaw_Cond = ""
    call pedrera_sex_p_general_talk

    with fade

    n "Rápidamente desplaza su cuerpo y cabeza hasta tu entrepierna y engulle tu enorme miembro por completo."

    show cumming_mc
    with vpunch
    with vpunch

    pause 0.5

    stop music fadeout 3.0

    scene black
    with fade

    n "Vuelves a explotar,"

    n "pero esta vez dentro de esa ardiente garganta que te quema el miembro por completo."

    pause 0.5

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    # She keeps sucking your dick.
    scene black
    $ ped_sex_blow_Cond = True
    $ ped_sex_general_zoom_Cond = "faceCentered"
    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_action_Cond = "o04_01"
    $ p_prot.pos = "oral"
    $ ped_sex_general_expressionJaw_Cond = ""
    call pedrera_sex_p_general_talk
    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    #show tired_mc
    with fade_long1s

    p "-Ahhhh-"
    extend "ahhhh-"
    extend "ahhhh-..."

    scene black
    with fade

    p "Ughh..."

    # She licks your dick.

    $ p_ao_n_tongue = ""
    $ ped_sex_blow_Cond = False
    $ ped_sex_general_expression_Cond = "lustSmile"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_05_happy"

    scene pedrera_sex_neus_oral softLicking:
        subpixel True
        truecenter
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    n "Sin prisas -y aún jugueteando con su lengua en tu dolorido extenuado miembro viril-"

    n "se va desprendiendo de ti con una sonrisa de oreja a oreja"

    n "y una expresión perturbadora."

    p "Ya no puedo más..."

    play sound "audio/sfx/hit02.ogg"

    #show p_ao_nRap_ankles_02_back: # Her hand on your leg.
    $ p_ao_action_b_Cond = "back"
    scene p_ao_nRap_ankles_02 general_comp_01:
        truecenter
        zoom 2.0 xpos 0.7 ypos 0.9
    with vpunch

    # scene p_ao_nRap_ankles_back:
    #     truecenter
    #     zoom 2.0 xpos 0.7 ypos 0.9
    # with fade

    n "Te agarra de una pierna y con un rápido gesto"

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"

    # You're over the bead not doggystyle yet.

    play sound "audio/sfx/fall03.ogg"

    scene black
    with hpunch

    p "¡Ouch!"


    #scene p_ao_nRap_doggy_back:
    $ p_ao_action_b_Cond = "back"  
    scene p_ao_nRap_doggy general_comp_01:
        subpixel True
        truecenter
        #zoom 0.4 xpos 0.5 ypos 0.5
        zoom 2.0 xpos -0.8 ypos -1.7 # Her foot
        easein 5.0 zoom 1.5 xpos 1.3 ypos -1.1 # your face
    with fade

    n "revuelve tu cuerpo ciento ochenta grados poniéndote boca abajo sobre la cama."

    window hide dissolve
    pause

    $ p_ao_action_Cond = "ahead_hands"

    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.6 ypos -0.67 # Your face close shot.
        ease_quad 10.0 zoom 1.5 xpos 0.7 ypos -0.5 # Closing to your face
    with fade

    p "¡¿Qué-"

    extend "qué estás haciendo?!"

    #$ ped_neus_whispers_sfx04 = 0.5
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front00"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade

    ne "Aún no hemos terminado."

    $ nteye = "down03"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # You're on doggystyle.
    #scene p_ao_nRap_doggy_back:
    $ p_ao_action_b_Cond = "back"  
    scene p_ao_nRap_doggy general_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 1.3 ypos -1.1 # your face
        ease 10.0 zoom 0.6 xpos 0.6 ypos 0.2
    with fade

    n "Te agarra por la cintura y te levanta las caderas dejando tu trasero expuesto,"

    n "con sus rodillas te separa las piernas y te agarra las nalgas con ambas manos"

    n "mientras padeces la tentación de morder la almohada."

    p "¿Qué-"

    extend "qué estás haciendo?"

    window hide dissolve
    pause

    #Doggystyle different perspective.
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.7 ypos -0.5 # Closing to your face
        ease_quad 10.0 zoom 2.0 xpos 0.5 ypos 1.0 # Closing to her face.
    with fade

    ne "¿Acaso no es obvio?"

    pause

    #$ ped_neus_whispers_sfx04 = 0.6
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front00"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with fade

    ne "Quiero que se te vuelva a poner dura,"

    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows suspiciousx04
    call n_closefromup_tears_tears
    with dissolve

    ne "y parece que darte por detrás funciona bastante bien..."

    $ nteye = "down03"
    show n_closefromup_mouth happy_Silentx10
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # Grabbing your testicles.

    play sound "audio/characters/protagonist/au_late01.ogg"

    scene black
    show p_ao_n_grabBalls_comp 01:
        truecenter
        xzoom -1.0
        zoom 1.0
        easein_elastic 1.0 zoom 0.5 xpos 0.6 ypos 0.55 # InvertedCentered the Grab
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with vpunch

    p "¡Auch!"

    n "Te agarra con fuerza uno de tus testículos."

    p "¡Me haces daño!"

    #$ ped_neus_whispers_sfx04 = 0.7
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "down01"
    show n_closefromup_mouth happy_Talkingx16
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade

    ne "El dolor no es malo si se te acaba poniendo dura."

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "Sé lo que me hago..."

    $ nteye = "down02"
    show n_closefromup_mouth happy_Silentx11
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    $ p_ao_mc_dick_num = 3
    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "01_NAss"

    pause 0.2

    # Preparing to LICK your ass.
    scene p_ao_mc_ass_n_lick_comp_01:
        truecenter
        ## xpos     0.0=Right    1.0=Left
        ## ypos     0.0=Down      1.0=Up
        zoom 1.0 xpos 0.0 ypos 1.0 # Up
        easein_quad 8.0 zoom 1.2 xpos 0.4 ypos 0.25 # Asshole Centered.
    with fade

    n "Presionando tus nalgas en direcciones opuestas, deja al descubierto tu afligido agujero anal."

    n "Percibes su aliento acercándose a él."

    if p_neus_dickG_wants == False:

        pt "No..."

    $ p_ao_action_Cond = "02_NAss"
    $ p_ao_n_vel = 1
    show p_ao_mc_ass_n_lick_comp_01:
        easein_quad 15.0 zoom 0.75 xpos 0.4 ypos 0.3
    with Dissolve(1.5)

    n "A modo juguetón, relame la parte superficial externa"

    n "mientras sientes que juguetea con penetrarte con ella."

    if p_neus_dickG_wants:

        pt "¿Hará lo que pienso que va a...?"

    else:

        pt "No será capaz..."


    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "03_NAss"
    show p_ao_mc_ass_n_lick_comp_01:
        easein_quad 15.0 zoom 0.6 xpos 0.38 ypos 0.35
    with Dissolve(0.5)

    n "Se va a abriendo paso a través"

    n "y es incluso más caliente, húmeda y gruesa."

    $ p_ao_n_vel = 5
    show p_ao_mc_ass_n_lick_comp_01:
        easein_quad 15.0 zoom 0.75 xpos 0.35 ypos 0.3
    with Dissolve(0.5)

    pt "Joder..."

    # Hundes tu rostro sobre la alomohada??
    # You're on doggystyle.
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.7 ypos -0.5 # Closing to your face
        ease_quad 10.0 zoom 1.0 xpos 0.6 ypos -0.67 # Your face close shot.
    with fade

    n "Hundes tu rostro sobre la almohada al mismo tiempo que te agarras fuertemente a la sábana."

    n "Lentamente va profundizando;"

    if music_play != "bentAndBroken":
        play music "audio/music/kevinmacleod/creepy/bentAndBroken.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "bentAndBroken"

    $ p_ao_action_Cond = "04_NAss" # Deeper Tongue
    $ p_ao_n_vel = 2
    scene p_ao_mc_ass_n_lick_comp_01:
        truecenter
        zoom 1.2 xpos 0.4 ypos 0.25 # Asshole Centered.
        easein_quad 20.0 zoom 0.5 xpos 0.33 ypos 0.35 # Very Far
    with fade

    n "al mismo tiempo, experimentas que la mueve a voluntad -como si se tratara de una serpiente-"

    n "a través de la estrecha y dolorida carne intestinal,"

    $ p_ao_action_Cond = "05_NAss" # Deeper Tongue Lips Touching ass.
    $ p_ao_n_vel = 3
    show p_ao_mc_ass_n_lick_comp_01:
        easein_quad 15.0 zoom 0.75 xpos 0.35 ypos 0.3
    with Dissolve(1.0)
        
    n "mientras sus labios succionan y empapan tu carne exterior."

    n "No solo su longitud aumenta,"

    n "sino que además se va volviendo más y más gruesa."

    n "Como si fuera un reptil huyendo de su presa,"

    n "empieza a desplazarse a lo largo y ancho de tu cavidad anal sin ninguna piedad."

    #$ p_ao_action_Cond = "06_NAss" # Deeper Tongue Lips Touching ass.
    $ p_ao_n_vel = 5
    show p_ao_mc_ass_n_lick_comp_01:
        easein_quad 8.0 zoom 1.2 xpos 0.4 ypos 0.25 # Asshole Centered.
    with Dissolve(0.5)

    n "Tienes la sensación de que te llega tan profundo,"

    n "que te revuelve hasta el estómago."

    p "¿Qué-"

    extend "qué estás haciendo?"

    scene black
    with fade

    n "Como si de una correa retráctil se tratara,"

    n "distingues que regresa por dónde había serpenteado, tramo a tramo."

    n "Finalmente, y sintiéndote mucho más ligero -incluso más que antes-,"

    n "saca su lengua por completo para luego secarse -con una mirada lasciva- la barbilla."

    #$ ped_neus_whispers_sfx04 = 0.8

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade

    ne "Es obvio,"

    extend " ¿No crees?"

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Estoy preparando el camino."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Técnicamente,"

    $ nteye = "right01"
    show n_closefromup_mouth happy_Talkingx10
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "sigue siendo tu primera vez,"

    $ nteye = "down04"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "así que creo que es buena idea preparar un poco el camino,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Ya que,"

    extend " a diferencia de mi,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "tú si has cenado esta noche,"

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "y obviamente no te habías hecho ninguna {a=https://es.wikipedia.org/wiki/Enema}lavativa{/a}."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Qué?!"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "No queremos ninguna sorpresa desagradable,"

    extend " ¿verdad?"

    $ nteye = "down04"
    show n_closefromup_mouth sadbiting_Silentx08
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Cómo dice?!"

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    if p_neus_dickG_wants:
        if music_play != "playWithMe":
            play music "audio/music/kevinmacleod/creepy/playWithMe.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "playWithMe"
    else:
        if music_play != "nervous":
            play music "audio/music/kevinmacleod/creepy/nervous.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "nervous"

    # Her dick inside again, becoming bigger.
    $ p_ao_action_Cond = "ahead_hands"
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.7 ypos -0.5 # Closing to your face
        #ease_quad 10.0 zoom 1.0 xpos 0.6 ypos -0.67 # Your face close shot.
        ease_quad 5.0 zoom 2.0 xpos 0.5 ypos 0.5 # your ASS.
    with fade

    n "Vuelves a sentir el tacto ardiente de la punta de su oscuro miembro,"

# #### TEST

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "02"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "02"

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "03"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "03"

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "04"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "04"

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "05"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "05"


#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "06"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "06"

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "04_tease"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "04_tease"

#     $ p_ao_n_vel = 1
#     $ p_ao_action_Cond = "05_tease"
#     scene p_ao_mc_ass_comp 04_doggy:
#         truecenter
#         zoom 0.5 xpos 0.5 ypos 0.5

#     progcheck "05_tease"

# ###

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "04_tease"
    scene p_ao_mc_ass_comp 04_doggy:
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.35
        easein_quad 8.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade


    n "pero esta vez,"

    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "05_tease"
    show p_ao_mc_ass_comp 04_doggy
    with Dissolve(3.0)


    n "es mucho más grueso que antes."

    if p_neus_dickG_wants:

        p "Ve con cuidado,"

        extend " por favor..."

        ne "Eres tan tierno cuando quieres..."

    else:

        p "¡Claro que sigue siendo mi primera vez!"

        ne "Hmmm..."

    window hide dissolve
    pause

    #$ ped_neus_whispers_sfx04 = 0.8

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with fade

    ne "Pero creo que esta vez puedo aumentar un poco más el tamaño,"

    $ nteye = "front00"
    show n_closefromup_mouth happy_Talkingx12
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    ne "al fin y al cabo no es justo que seas el único con un pollón enorme,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "¿No crees?"

    if p_neus_dickG_wants:

        $ nteye = "front03"
        show n_closefromup_mouth happy_Silentx08
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        p "..."

    else:

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Acaso no me has oído cuando he dicho que sigue siendo mi primera vez?!"

        $ nteye = "front01"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        ne "No seas tan quejica."

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Eres un hombre,"

        extend " o no?"

        $ nteye = "front03"
        show n_closefromup_mouth happybiting_Silentx07
        show n_closefromup_eyebrows suspiciousx04
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Y eso qué tiene que ver?!"

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # Increase time or size fucking your ass. (DoggyStyle)
    $ p_ao_n_vel = 3
    $ p_ao_action_Cond = "05_tease"
    scene p_ao_mc_ass_comp 04_doggy:
        truecenter
        zoom 1.5 xpos 0.5 ypos 0.35
        easein_quad 3.0 zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
    with fade

    n "Sin darte tiempo a réplica,"

    if p_neus_dickG_wants:
        if music_play != "darkestChild":
            play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "darkestChild"
    else:
        if music_play != "morgana_rides":
            play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "morgana_rides"



    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "05_stop"
    show p_ao_mc_ass_comp 04_doggy:
        #truecenter
        easein 12.0/p_ao_n_vel zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
        # # xpos 1.0=Left xpos 0.0=Right // ypos 1.0=Up ypos 0.0=Down
        ##zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
        ##zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
        # block:
        #     easein 4.0/p_ao_n_vel zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
        #     easeout 4.0/p_ao_n_vel zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
        #     repeat
    with vpunch

    if p_neus_dickG_wants:

        p "¡HHHmmm...!"

    else:

        p "¡Joder!"

    n "su -ligeramente más grueso- capullo vuelve a penetrar tu reciente desvirgado ano."

    if not p_neus_dickG_wants:

        pt "¡No puedo ni moverme!"

    ne "Caray..."

    # Her fucking from different perspective.
    #$ p_ao_n_vel = 1
    #scene p_ao_nRap_doggy_front:
    $ p_ao_action_b_Cond = "front"  
    scene p_ao_nRap_doggy general_comp_01:
        subpixel True
        truecenter
        #zoom 1.5 xpos 1.3 ypos -1.1 # your face
        zoom 1.5 xpos 0.45 ypos 0.32 # Your ass
        easein_quad 8.0 zoom 0.6 xpos 0.6 ypos 0.2
    with fade

    ne "Ha entrado mejor de lo que pensaba."

    ne "Está bien estrecho, pero..."

    window hide dissolve
    pause

    #$ ped_neus_whispers_sfx04 = 0.8

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with fade

    ne "¿Seguro que nunca te habías hecho ni un dedo aquí detrás?"

    if p_neus_dickG_wants:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Silentx04
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        p "La verdad es que no..."

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx09
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Mentiroso..."

    else:

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx10
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        pt "¡Joder!"

    $ nteye = "down01"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # Increase a bit her movement with a big dick. (Doggy)
    
    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "05"
    scene p_ao_mc_ass_comp 04_doggy:
        truecenter
        zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
        ##zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
        block:
            easein 4.0/p_ao_n_vel zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
            easeout 4.0/p_ao_n_vel zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
            repeat
    with fade

    n "Vuelve a mover lentamente sus caderas -esta vez teniéndote a cuatro patas sobre la cama-"

    n "a medida que su ardiente polla ahonda en tu cavidad anal."

    if p_neus.buttockSlaps_received > 1:

        call p_ao_smashImage

        play sound "audio/sfx/slap01.ogg"
        with hpunch
        ono "SMACK"

        p "¡Oye!"

        #$ ped_neus_whispers_sfx04 = 0.8

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab
        show n_closefromup_body naked  

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx09
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with fade

        ne "Viendo lo mucho que has disfrutado azotándome las nalgas,"

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx11
        show n_closefromup_eyebrows angryx01
        call n_closefromup_tears_tears
        with dissolve

        ne "he pensado que quizás también eres de los que disfrutan recibirlas,"

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "especialmente cuando te estoy follando a cuatro patas como a una perra."

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx10
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¿O es que solo te gusta dar,"

        extend " pero no recibir?"

        $ nteye = "front05"
        show n_closefromup_mouth sadbiting_Silentx10
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "¿Si me gusta que me azote las nalgas mientras me folla el trasero?"

            "Dame tan duro como quieras." if p_neus_dickG_wants:
                call p_Help
                $pl.ch_pts("np",1)

                $ nteye = "front00"
                show n_closefromup_mouth sadbiting_Silentx12
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx08
                show n_closefromup_eyebrows angryx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Así me gusta"

                if gensex_YoureAMonster:

                    extend " perra..."

                else:

                    extend " semental..."

                $ nteye = "down03"
                show n_closefromup_mouth happybiting_Silentx12
                show n_closefromup_eyebrows sadx02
                call n_closefromup_tears_tears
                with dissolve

                call p_ao_smashImage

                play sound "audio/sfx/slap01.ogg"
                with hpunch
                ono "SMACK"

                $ nteye = "down02"
                show n_closefromup_mouth happybiting_Silentx08
                show n_closefromup_eyebrows sadx03
                call n_closefromup_tears_tears
                with dissolve

                pt "¡¿Pero qué coño estoy diciendo?!"

                $ nteye = "down05"
                show n_closefromup_mouth happy_Silentx06
                show n_closefromup_eyebrows suspiciousx01
                call n_closefromup_tears_tears
                with dissolve

                pt "¡¿Quien está tomando decisiones por mi?!"

            "Prefiero solo dar.":
                call p_Help
                $pl.ch_pts("np",-1)

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx005
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "Pues es una pena,"

                $ nteye = "front03"
                show n_closefromup_mouth happy_Talkingx13
                show n_closefromup_eyebrows angryx01
                call n_closefromup_tears_tears
                with dissolve

                ne "porque ahora mismo me apetece darte bien duro."

            "...":
                call p_Help

                $ nteye = "front05"
                show n_closefromup_mouth happy_Silentx04
                show n_closefromup_eyebrows suspiciousx01
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

        $ nteye = "down01"
        show n_closefromup_mouth happybiting_Silentx14
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

    #Increase RYTHYM fucking you. # not finished, change camera shake.
    $ p_ao_n_vel = 4
    #scene p_ao_nRap_doggy_anim_comp_01:
    #$ p_ao_action_b_Cond = "front"  
    scene p_ao_nRap_doggy anim_comp_01:
        subpixel True
        truecenter
        #zoom 1.5 xpos 1.3 ypos -1.1 # your face
        zoom 1.5 xpos 0.45 ypos 0.32 # Your ass
        easein_quad 8.0 zoom 0.6 xpos 0.6 ypos 0.2
    with fade

    n "Vuelve a aumentar el ritmo mientras percibes el grosor de su polla aumentar ligeramente en cada embestida."

    if p_neus.buttockSlaps_received > 1:

        call p_ao_smashImage

        play sound "audio/sfx/slap01.ogg"
        with hpunch
        ono "SPLASH"

        call p_ao_smashImage

        play sound "audio/sfx/slap02.ogg"
        with hpunch
        extend " SPLASH"

        call p_ao_smashImage

        play sound "audio/sfx/slap01.ogg"
        with hpunch
        extend " SPLASH"

        p "¡JODER!"

        $ p_ao_action_Cond = "05"
        scene p_ao_mc_ass_comp 04_doggy:
            truecenter
            zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
            block:
                easein 4.0/p_ao_n_vel zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
                easeout 4.0/p_ao_n_vel zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
                repeat
        with fade

        ne "Puedes decirme lo que quieras,"

        if gensex_ILoveYouNeus:

            extend " mi amor;"

        elif gensex_YoureAMonster:

            extend " perra;"

        else:

            extend " mi querido corcel;"

        ne "pero tu polla se está poniendo más dura a cada nueva nalgada,"

        ne "y ni siquiera te la he tocado."

    #$ ped_neus_whispers_sfx04 = 0.8
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx15
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with fade

    ne "Admite de una vez que te gusta más recibir que dar."

    if p_neus.buttockSlaps_received > 1:

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx09
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        call p_ao_smashImage

        play sound "audio/sfx/slap01.ogg"
        with hpunch
        #ono "{size=50}SMACK{/size}{w=0.6}{nw}"

        $ nteye = "down05"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Te gusta más que te folle el trasero o que te azote las nalgas?"

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx07
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        call p_ao_smashImage

        play sound "audio/sfx/slap02.ogg"
        with hpunch
        #ono "{size=50}SMACK{/size}{w=0.6}{nw}"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows serious
        call n_closefromup_tears_tears
        with dissolve

        ne "Quizás ya prefieres que haga ambas cosas a la vez."

        if p_neus_dickG_wants:

            $ nteye = "front03"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            p "Me las estás dejando rojas..."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "No es lo único que te voy a dejar rojizo."

        else:

            $ nteye = "front01"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            p "¡Me las vas a dejar rojas!"

            $ nteye = "front05"
            show n_closefromup_mouth happy_Talkingx08
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya estaban bien rojas antes de azotarlas."

    else:  

        $ nteye = "front02"
        show n_closefromup_mouth sadbiting_Silentx08
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        menu:

            pt "Que lo admita dice..."

            "¡¿Te sientes bien violándome?!" if not p_neus_dickG_wants:
                call p_Help

                $ nteye = "front00"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                ne "Hmmm..."

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx08
                show n_closefromup_eyebrows angryx05
                call n_closefromup_tears_tears
                with dissolve

                ne "Has sido tú quien me ha llevado a esto."

                $ nteye = "down05"
                show n_closefromup_mouth sad_Talkingx003
                show n_closefromup_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                ne "Tampoco parece que estés sufriendo tanto,"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                ne "al menos no por aquí detrás."

                $ nteye = "down03"
                show n_closefromup_mouth happy_Talkingx05
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                ne "Aunque..."

            "No pienso admitir eso.":
                call p_Help

                $ nteye = "front03"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx06
                show n_closefromup_eyebrows normal
                call n_closefromup_tears_tears
                with dissolve

                ne "Eso ya lo veremos..."

            "Es posible." if p_neus_dickG_wants:
                call p_Help

                $ nteye = "front05"
                show n_closefromup_mouth happybiting_Silentx05
                show n_closefromup_eyebrows suspiciousx02
                call n_closefromup_tears_tears
                with dissolve

                ne "Hmmm..."

            "Cállate y fóllame." if p_neus_dickG_wants:
                call p_Help

                $ nteye = "front00"
                show n_closefromup_mouth sad_Silentx02
                show n_closefromup_eyebrows surprisex03
                call n_closefromup_tears_tears
                with dissolve

                pause 0.2

                $ nteye = "front05"
                show n_closefromup_mouth happy_Talkingx06
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve

                ne "¿Quieres más?"

            "...":
                call p_Help

                $ nteye = "front05"
                show n_closefromup_mouth happy_Silentx06
                show n_closefromup_eyebrows suspiciousx03
                call n_closefromup_tears_tears
                with dissolve
                

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx15
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # Increase RYTHYM.

    #Show the camera moving as she is fucking you. # NOT FINISHED
    $ p_ao_n_vel = 6
    #scene p_ao_nRap_doggy_anim_comp_01:
    #$ p_ao_action_b_Cond = "front"  
    scene p_ao_nRap_doggy anim_comp_01:
        subpixel True
        truecenter
        #zoom 1.5 xpos 1.3 ypos -1.1 # your face
        zoom 1.5 xpos 0.45 ypos 0.32 # Your ass
        easein_quad 8.0 zoom 0.6 xpos 0.6 ypos 0.2
    with fade

    ne "Como puedes comprobar,"

    ne "me gusta follar duro."

    p "..."

    p "Mañana no me podré ni sentar..."

    ne "No te preocupes por eso."

    if p_neus_dickG_wants:
        if music_play != "funkorama":
            play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "funkorama"
    else:
        if music_play != "movementProposition":
            play music "audio/music/kevinmacleod/fast/movementProposition.ogg" fadein 3.0 fadeout 3.0
            $ music_play = "movementProposition"

    show closetocum_mc

    if p_neus_dickG_wants:

        pt "Me está tratando como a un trapo sucio..."

        pt "¡¿Por qué coño me pone esto tan caliente?!"

    else:

        pt "Mierda..."



## NOT FINISHED --- Nalgadas y cuando te dice lo del niño.
    
    #$ ped_neus_whispers_sfx04 = 0.8
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "down01"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears

    show closetocum_mc

    with fade

    ne "¿En serio?"

    $ nteye = "front02"
    show n_closefromup_mouth sad_Talkingx05
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Tan pronto?"

    $ nteye = "down03"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero si ni siquiera he llegado a tocártela..."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Silentx06
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmm..."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows suspiciousx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Quizás es que en el fondo eres masoquista y aún no lo sabías."

    $ nteye = "down05"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows surprisex03
    call n_closefromup_tears_tears
    with dissolve

    ne "Tenerte a cuatro patas viendo como se te va poniendo tensa en cada nueva arremetida,"

    if p_neus.buttockSlaps_received > 1:

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx04
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        call p_ao_smashImage
        with hpunch
        play sound "audio/sfx/slap01.ogg"
        #ono "SPLASH"

    $ nteye = "down01"
    show n_closefromup_mouth happy_Talkingx13
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "me está poniendo muy perra."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx15
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2


    # + Rythym

    $ p_ao_n_vel = 10
    scene p_ao_nRap_doggyHard anim_comp_01:
        subpixel True
        truecenter
        #zoom 1.5 xpos 1.3 ypos -1.1 # your face
        zoom 1.5 xpos 0.45 ypos 0.32 # Your ass
        easein_quad 8.0 zoom 0.6 xpos 0.6 ypos 0.2

    show closetocum_mc

    with vpunch

    p "ugh..."

    n "Vuelve a aumentar el ritmo sin darte apenas tiempo a reaccionar."

    n "No solo su crudeza es más encarnizada,"

    n "sino que además su miembro va aumentando de temperatura."

    # If if p_neus.buttockSlaps_received > 1: she slaps your ass, otherwise she fucks your harder.

    call p_ao_smashImage
    with hpunch
    play sound "audio/sfx/slap02.ogg"
    #ono "SPLASH{w=0.6}{nw}"

    ne "¡Córrete!"

    call p_ao_smashImage
    with hpunch
    play sound "audio/sfx/slap03.ogg"
    #ono "SPLASH{w=0.6}{nw}"

    ne "¡Córrete sin que tenga que tocártela!"

    call p_ao_smashImage
    with hpunch
    play sound "audio/sfx/slap02.ogg"
    #ono "SPLASH{w=0.6}{nw}"

    n "Su voz es mordaz y dominante."

    ne "¡Córrete como una perra en celo!"

    if p_neus_dickG_wants == False:

        pt "¡La madre que la parió...!"

        pt "No..."

    p "¡Ugh!"

    $ p_ao_action_Cond = "05"
    scene p_ao_mc_ass_comp 04_doggy:
        truecenter
        zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
        ##zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
        block:
            easein 4.0/p_ao_n_vel zoom 1.2 xpos 0.6 ypos 0.18 # 05 In
            easeout 4.0/p_ao_n_vel zoom 0.8 xpos 0.15 ypos 0.3 # 05 Out
            repeat
    show closetocum_mc
    with fade

    n "Justo cuando experimentas el hormigueo del flujo que empieza a gorgotear en tus adentros,"

    n "Una sensación más dolorosa que placentera -con la polla completamente al rojo vivo- emerge de tu interior."

    scene black
    show closetocum_mc
    with fade

    n "[neusname] libera sus manos de tus nalgas mientras mantiene el ritmo de sus embestidas"

    # testicles
    scene black
    show p_ao_n_grabBalls_comp 01:
        truecenter
        xzoom -1.0
        zoom 1.0
        easein_elastic 1.0 zoom 0.5 xpos 0.6 ypos 0.55 # InvertedCentered the Grab
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    show closetocum_mc
    with vpunch

    n "usando una de ellas para agarrarte con fiereza tus testículos,"

    # Grabbing your Dick with your cumshot, caressing it.
    $ p_ao_n_vel = 3
    $ p_ao_action_Cond = "rubbing"
    scene p_ao_cumOnHand_comp_01:
        truecenter
        #zoom 1.0
        zoom 1.8 xpos 0.75 ypos 0.1 # Down
        block:
            easein_quad 4.0/p_ao_n_vel zoom 2.0 xpos 0.4 ypos 0.4 # Up
            easeout_quad 4.0/p_ao_n_vel zoom 1.8 xpos 0.75 ypos 0.1 # Down
            repeat
        #zoom 2.0 xpos 0.4 ypos 0.4 # Up
        #zoom 2.2 xpos 1.0 ypos -0.1 # Capullo
    show closetocum_mc
    with fade

    n "mientras desplaza la otra delante del glande de tu polla."

    n "Percibes la palma de su mano y sus dedos juguetear con tu rojizo glande"

    #$ p_ao_n_vel = 3
    $ p_ao_action_Cond = "cumming"
    show p_ao_cumOnHand_comp_01:
        easein_expo 2.0 zoom 2.2 xpos 1.0 ypos -0.1 # Capullo
    with Dissolve(1.0)
    
    pause 0.2

    with hpunch
    with hpunch

    show cumming_mc

    n "mientras derramas -lo que te queda de- tu semilla sobre esa mano."

    $ p_ao_n_dick_num += 1
    call p_ao_n_changes

    $ p_prot.orgasm += 1

    stop music fadeout 3.0

    scene black
    with fade

    ne "Caray..."

    ne "A pesar del trote que ya llevas,"

    ne "me has dejado la mano bastante empapada."

    $ p_ao_n_horns_num += 1 # In theory the first one.

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    #$ ped_neus_whispers_sfx04 = 0.8
    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    show n_closefromup_body naked  

    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    show border_darkness:
        zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
    show n_closefromup_handL lick_full:
        ###truecenter #No need
        xpos 0.4 ypos 1.0

    show morning04_bedroom_DMast_blinkeye
    with fade

    ne "Cualquiera diría que es tu cuarta corrida."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx13
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Eres todo un semental,"

    if gensex_YoureAMonster:

        extend " mi perrita."

    else:

        extend " [protname]."

    $ nteye = "down02"
    show n_closefromup_mouth sad_Talkingx04
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque esta vez haya sido de un modo..."

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows suspiciousx04
    call n_closefromup_tears_tears
    with dissolve

    ne "digamos,"

    extend " poco varonil..."

    $ nteye = "front06"
    show n_closefromup_mouth extra_tongueOut
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears

    show n_closefromup_handL lick_full:
        easein_quad 2.0 xpos 0.35 ypos 0.7
        
    with dissolve


    ono "slurp" # 01

    $ nteye = "front07"
    show n_closefromup_mouth extra_tongueOut
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears

    show n_closefromup_handL lick_full:
        easein_quad 2.0 xpos 0.45 ypos 0.5
    with dissolve

    extend " slurp" # 02

    $ nteye = "front08"
    show n_closefromup_mouth extra_tongueOut
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears

    show n_closefromup_handL lick_clean:
        easein_quad 2.0 xpos 0.4 ypos 0.4
    with Dissolve(0.5)

    extend " slurp" # 03


    $ nteye = "front05" 
    show n_closefromup_mouth happy_Silentx05
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears

    show n_closefromup_handL lick_clean:
        easein_quad 2.0 xpos 0.4 ypos 1.0
    with dissolve

    n "Sin el control que tenía [neusname] sobre ti"

    $ nteye = "down05"
    show n_closefromup_mouth happy_Silentx04
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    show n_closefromup_handL lick_clean:
        easein_quad 2.0 xpos 1.0 ypos 1.5
    with dissolve

    n "y la falta de fuerzas en tus piernas,"

    scene black
    with vpunch
    with vpunch

    n "caes rendido sobre la cama."

    stop music fadeout 3.0

    $ ped_neus_whispers_sfx04 = 0.5
    $ n_exp_shine = 0.0

    jump p_neus_orgasmReal_amazonic_label

############################################################################################################
##############################################################################################################

############################################################################################################
##############################################################################################################
############################################################################################################
##############################################################################################################

label p_neus_orgasmReal_beforeAmazonic:

    scene black
    with hpunch

    play sound "audio/sfx/fall01.ogg"

    n "Agarrándote del brazo te levanta del suelo."

    p "¡¿Euh?!"

    n "y con una fuerza increíble, especialmente teniendo en cuenta su tamaño,"

    n "te hace andar hasta la pared"

# #####
#     pause
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene gensex_stan02_comp_01:
#         truecenter
#         zoom 0.2
#     pause
# ######

    $ ped_neus_whispers_sfx04 = 0.3

    stop music fadeout 0.5
    play sound "audio/sfx/fall18.ogg"

    $ p_ao_action_Cond = "aloneSoft"

    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        zoom 2.0 ypos 0.5
        xpos 0.0
        ease_elastic 1 xpos -0.9 #Final

    with hpunch
    with hpunch

    p "¡Ugh!"

    if music_play != "classichorror01":
        play music "audio/music/kevinmacleod/creepy/classichorror01.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "classichorror01"

    show gensex_stan02_comp_01:
        ease 10 zoom 3.0 xpos -1.6 ypos 0.3

    n "y te empuja hasta que tu espalda choca contra ella."

    p "¿Hace falta que seas tan bruta?"

    ne "No te quejes tanto."

    $ p_ao_action_Cond = "neusBalls"
    show gensex_stan02_comp_01:
        # xpos 0.5 ypos 0.5 zoom 0.2 # GENERAL for TESTING
        zoom 3.0 xpos -1.6 ypos 0.3
    with Dissolve(1.0)

    n "Con un rostro serio y no demasiado juguetón"

    n "se pone de rodillas ante ti."

    n "Vuelves a sentir su ardiente respiración cerca de tu miembro"

    n "mientras una mano te masaje los testículos,"

    $ p_ao_action_Cond = "neusBallsAss"
    show gensex_stan02_comp_01:
        # xpos 0.5 ypos 0.5 zoom 0.2 # GENERAL for TESTING
        ease 10 xpos -1.8 ypos 0.4
    with Dissolve(0.5)

    n "la otra te acaricia con dos dedos..."

    with hpunch

    p "¡Te he dicho que por ahí no!"

    ne "Tienes el culo contra el muro."

    ne "¡Relájate!"

    pt "¡Y esta frío de narices!"

    ne "No te voy a quitar ni tu orgullo masculino ni tu virginidad anal."

    ne "Confía en mi,"

    ne "sé lo que me hago.."

    menu:

        pt "¿Orgullo masculino?"

        "Preferiría que fuera sin usar mi trasero":
            call p_Help

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_body naked

            $ nteye = "front05"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with fade_short

            ne "Como no se te ponga dura"

            if p_prot_aoNight_analReceived == "False":

                $ nteye = "front02"
                show n_closefromup_mouth sad_Talkingx09
                show n_closefromup_eyebrows angryx03
                call n_closefromup_tears_tears
                with dissolve

                ne "voy a tener que usar lo otro para estimularte ahí detrás"

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "y como ya te he dicho,"

                $ nteye = "front05"
                show n_closefromup_mouth sad_Talkingx03
                show n_closefromup_eyebrows surprisex02
                call n_closefromup_tears_tears
                with dissolve

                ne "no serán precisamente mis dedos."

            else:

                $ nteye = "front08"
                show n_closefromup_mouth sad_Talkingx004
                show n_closefromup_eyebrows surprisex01
                call n_closefromup_tears_tears
                with dissolve

                ne "voy a tener que usar otra cosa para estimularte ahí detrás."

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx06
            show n_closefromup_eyebrows suspiciousx04
            call n_closefromup_tears_tears
            with dissolve

            p "Sino se me pone dura es porque..."

            $ nteye = "front01"
            show n_closefromup_mouth sad_Talkingx15
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with vpunch

            ne "¡Es porque no te da la puñetera gana de hacerme caso!"

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx11
            show n_closefromup_eyebrows angryx05
            call n_closefromup_tears_tears
            with dissolve

            ne "¡Así que cállate un poco y confía en mi!"

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx008
            show n_closefromup_eyebrows angryx06
            call n_closefromup_tears_tears
            with dissolve

            ne "¡No te pido tanto!"

            $ nteye = "front04"
            show n_closefromup_mouth sad_Talkingx10
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            ne "¡¿No crees?!"

            $ nteye = "front05"
            show n_closefromup_mouth sad_Silentx07
            show n_closefromup_eyebrows angryx05
            call n_closefromup_tears_tears
            with dissolve

            pt "Desde luego,"

            extend " no es tan dócil como antes..."

        "...":
            call p_Help

    #$ p_ao_action_Cond = "aloneSoft"

    $ p_ao_action_Cond = "neusBallsAss"
    show gensex_stan02_comp_01:
        truecenter
        zoom 3.0
        xpos -1.8 ypos 0.4
    with fade

    n "Su hirviente lengua juguetea con tu dolorida -y bastante flácida- polla"

    n "mientras sus dedos danzan alrededor de tu orificio trasero."

    n "Ejerce cierta presión con sus ardientes dedos alrededor de la tierna carne que cubre tu agujero de salida,"

    n "así como también juguetea con esa brecha sin llegar a introducirte ningún dedo,"

    n "casi como si te hiciera dudar de si lo hará o no."


    $ p_ao_action_Cond = "lickDick_01" # Soft
    $ nblushNumber = "06"
    $ ped_sex_general_expression_Cond = "lustToYou"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_02"
    $ p_ao_n_vel = 2

    ## REMEMBER!! IT¡S STILL SMALLLLLLHLÑSHEIRLÑESHRILESÑHRESI!!!!!!

    ## Tongue around your semihard Cock. Alt001

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    scene pedrera_sex_neus_oral tongue:
        subpixel True
        truecenter
        zoom 3.0 ypos -3.0
        easein_quad 20.0/p_ao_n_vel zoom 2.0 ypos 0.6 # Up #Close Camera to the dick sorrounded (Neus eyes?)
        block:
            ease 10.0/p_ao_n_vel zoom 2.0 ypos 0.28 #Down
            ease 10.0/p_ao_n_vel zoom 2.0 ypos 0.6 # Up #Close Camera to the dick sorrounded (Neus eyes?)
            repeat
    with fade

    n "Su extraordinariamente longeva lengua"

    n "contornea tu miembro viril hasta abrazarla por completo,"

    n "desde el glande hasta la base."

    window hide dissolve
    pause

    $ ped_sex_general_expressionJaw_Cond = "blow_below_05_happy"
    $ p_ao_action_Cond = "lickDick_02" # Medium
    show pedrera_sex_neus_oral tongue:
        easein_quad 20.0/p_ao_n_vel zoom 1.5 ypos 0.9 #Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.35 #Down
            ease 10.0/p_ao_n_vel ypos 0.9 #Up
            repeat
    with Dissolve(10.0/p_ao_n_vel)

    n "Lentamente, la desplaza en vertical masturbándote con ella"

    n "mientras te mira con la comisura de sus labios de oreja a oreja con una sonrisa perturbadora."

    # pause
    # $ p_ao_action_Cond = "lickDick_03" # Hard
    # show pedrera_sex_neus_oral tongue

    pt "No estoy seguro si esto me pone cachondo,"

    pt "pero desde luego me está dando escalofríos..."

    n "Una de sus abrasadoras manos se dirige a tus testículos"

    window hide dissolve
    pause

    play sound "audio/characters/protagonist/auau_late01.ogg"

    # Grabbing Testicles A005
    scene black
    show p_ao_n_grabBalls_comp 01:
        truecenter
        #zoom 0.2
        # zoom 2.0
        # easein_elastic 1.0 zoom 0.5
        zoom 1.0
        easein_elastic 1.0 zoom 0.5 xpos 0.4 ypos 0.55 # Centered the Grab
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with hpunch

    p "¡ugh...!"

    n "y empieza a presionarlos con fuerza."

    p "No creo que esto..."

    play sound "audio/characters/neus/shh02.ogg"

    ne "Shhh..."

    ## Tongue around your semihard Cock. Alt001

    $ ped_sex_general_expressionJaw_Cond = ""
    $ p_active = "p_neus"
    $ p_prot.pos = "oral"
    $ ped_sex_general_action_Cond = "o01_02"
    $ ped_sex_general_zoom_Cond = "faceCentered"

    call pedrera_sex_p_general_talk

    # show pedrera_sex_neus_oral blowjob_general:
    #     zoom 1.3
    #     ypos 1.2 # DOWN
    #     block:
    #         ease 4.0/p_ao_n_vel ypos 1.25 #Up
    #         ease 4.0/p_ao_n_vel ypos 1.2 # DOWN
    #         repeat
        
    with fade

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"


# ###### TEST
#     $ ped_sex_general_action_Cond = "o01_04"
#     call pedrera_sex_p_general_talk
#     progcheck "01"
#     $ ped_sex_general_action_Cond = "o02_04"
#     call pedrera_sex_p_general_talk
#     progcheck "02"
#     $ ped_sex_general_action_Cond = "o03_04"
#     call pedrera_sex_p_general_talk
#     progcheck "03"
#     $ ped_sex_general_action_Cond = "o04_04"
#     call pedrera_sex_p_general_talk
#     progcheck "04"
# #####

    n "Aún teniendo tu polla completamente arropada por su lengua,"

    n "besa tu glande con sus calcinantes labios para luego succionarla con vigor"

    n "sin dejar de mecer tu -algo más erecto- miembro."

    $ ped_sex_blow_Cond = False
    $ ped_sex_general_expressionJaw_Cond = "blow_below_03"
    $ p_ao_action_Cond = "lickDick_02" # Medium
    $ ped_sex_general_zoom_Cond = "face"
    #$ ped_sex_general_action_Cond = "o01_05"

    ## Tongue around your semihard Cock. A004
    scene p_ao_mc_ass_comp 02:
        subpixel True
        truecenter
        rotate 180 xzoom -1.0
        zoom 1.0 xpos 0.5 ypos 0.5 # Asshole Centered?
        ease 15.0 zoom 0.65 ypos 0.3
    with fade

    n "Uno de los dedos de la mano, que sigue jugueteando con tu parte trasera,"

    n "empieza a indagar por tu agujero"

    n "mientras su otra mano masajea con más rudeza tus doloridos testículos."

    p "Ugh..."

    ## Tongue around your semihard Cock. Alt001(Blowjob? GLANS)
    $ ped_sex_general_expressionJaw_Cond = "blow_below_03"
    $ p_ao_action_Cond = "lickDick_02" # Medium
    show pedrera_sex_neus_oral tongue:
        truecenter
        ypos 1.2 #Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.35 #Down
            ease 10.0/p_ao_n_vel ypos 0.9 #Up
            repeat
    with fade

    $ ped_sex_general_expressionJaw_Cond = "blow_below_04"
    $ p_ao_action_Cond = "lickDick_03" # Medium
    show pedrera_sex_neus_oral tongue:
        truecenter
        ypos 1.2 #Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.35 #Down
            ease 10.0/p_ao_n_vel ypos 0.9 #Up
            repeat
    with Dissolve(10.0/p_ao_n_vel)

    window hide dissolve
    pause

    ## NOW COMES BLOWJOB

    $ p_ao_background = "pedrera"

    $ ped_sex_general_expressionJaw_Cond = ""
    $ p_active = "p_neus"
    $ p_prot.pos = "oral"
    $ ped_sex_general_action_Cond = "o01_02"
    $ ped_sex_general_zoom_Cond = "faceCenteredClose"

    call pedrera_sex_p_general_talk
    # show pedrera_sex_neus_oral blowjob_general:
    #     zoom 1.3
    #     ypos 1.2 # DOWN
    #     block:
    #         ease 4.0/p_ao_n_vel ypos 1.25 #Up
    #         ease 4.0/p_ao_n_vel ypos 1.2 # DOWN
    #         repeat
        
    with Dissolve(1.0)

# ### TEST
#     #$ ped_sex_general_zoom_Cond = "faceCentered"
#     $ ped_sex_general_zoom_Cond = "faceCenteredClose"
#     $ ped_sex_general_expressionJaw_Cond = ""
#     $ p_active = "p_neus"
#     $ p_prot.pos = "oral"
#     $ ped_sex_general_action_Cond = "o01_01"
#     call pedrera_sex_p_general_talk
#     progcheck "01"
#     $ ped_sex_general_action_Cond = "o02_01"
#     call pedrera_sex_p_general_talk
#     progcheck "02"
#     $ ped_sex_general_action_Cond = "o03_01"
#     call pedrera_sex_p_general_talk
#     progcheck "03"
#     $ ped_sex_general_action_Cond = "o04_01"
#     call pedrera_sex_p_general_talk
#     progcheck "04"
# ####

    n "Sus labios arropan cada vez más tu dolorido miembro"

    # Illustration Tongue going down? # NOT FINISHED

    n "mientras su lengua te libera de esa presión;"

    n "esta se desplaza por la parte inferior de tu polla,"

    n "sin abandonar el tacto con tu piel,"

    $ ped_sex_general_zoom_Cond = "faceCenteredClose"
    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_action_Cond = "o02_01"
    $ p_ao_n_vel = 1
    call pedrera_sex_p_general_talk

    # show pedrera_sex_neus_oral blowjob_general:
    #     zoom 1.3
    #     ypos 1.25 #Up
    #     block:
    #         ease 4.0/p_ao_n_vel ypos 1.0 # DOWN
    #         ease 4.0/p_ao_n_vel ypos 1.25 #Up
            
    #         repeat
    with Dissolve(0.5)

    n "hasta llegar a la mano que masajea tus testículos,"

    # ######
    # $ ped_neus_whispers_sfx04 = 1.0
    # show pedrera_sex_neus_oral blowjob_general:
    #     truecenter
    #     zoom 0.2
    # pause 
    # ###

    n "relamiendo aquella parte donde estas no alcanzan."

    $ ped_sex_general_expression_Cond = "indifferent"
    $ ped_sex_general_action_Cond = "o03_01"
    $ p_ao_n_vel = 1
    call pedrera_sex_p_general_talk

    # show pedrera_sex_neus_oral blowjob_general:
    #     zoom 1.3
    #     ypos 1.25 #Up
    #     block:
    #         ease 4.0/p_ao_n_vel ypos 0.8 # DOWN
    #         ease 4.0/p_ao_n_vel ypos 1.25 #Up
    #         repeat

    with Dissolve(0.5)

    if night04_pedrera_blowjob_DONE:

        pt "Coño..."

    else:

        pt "¡Coño!"

        pt "Que mamada más rara,"

        pt "pero joder..."

    n "La sangre va regresando en pequeños impulsos a tu revivido miembro"

    n "que va poniéndose más tenso a cada segundo que pasa."

    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_action_Cond = "o04_01"
    call pedrera_sex_p_general_talk
    show pedrera_sex_neus_oral blowjob_general:
        zoom 1.5 
        ypos 1.4 #Up
        block:
            ease 4.0/p_ao_n_vel ypos 0.4 # Down
            ease 4.0/p_ao_n_vel ypos 1.4 #Up
            repeat
    with Dissolve(0.5)

    n "Tramo a tramo, [neusname] va alojando tu miembro"

    n "hasta casi ocultarlo por completo en el interior de su boca."

    # Tongue coming back # NOT FINISHED

    n "Su lengua regresa de nuevo pasando por la misma parte inferior de tu miembro"

    $ ped_sex_general_expression_Cond = "lustToYou"

    show pedrera_sex_neus_oral blowjob_general:
        zoom 1.5 
        ypos 1.4 #Up
        block:
            ease 4.0/p_ao_n_vel ypos 0.4 # Down
            ease 4.0/p_ao_n_vel ypos 1.4 #Up
            repeat
    with Dissolve(0.5)

    n "hasta esconderse de nuevo en su boca mientras te mira con unos ojos de niña traviesa."

    if music_play != "frost_waltz":
        play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "frost_waltz"

    $ p_ao_action_Cond = "neusFront_still"
    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        #zoom 0.2 xpos 0.5 ypos 0.5 # TEST
        #zoom 1.5 xpos -0.5 ypos 0.5
        # zoom 2.0 ypos 0.5
        # xpos 0.0
        # ease_elastic 1 xpos -0.9 #Final

        zoom 3.0 xpos -1.7 ypos -2.0 # Feet
        pause 0.5
        ease 15 zoom 3.0 xpos -1.5 ypos 1.1 # Top
    with fade

    ne "Creo que ya está suficientemente dura."

    n "La ves ponerse de pie apoyando su cuerpo desnudo contra el tuyo."

    n "Su ardiente barriga presiona superficialmente tu polla aplastada contra tu frío cuerpo"

    n "mientras sus húmedos y candentes pezones acarician tus abdominales."

    $ p_ao_action_Cond = "neusFront_moving"
    show gensex_stan02_comp_01:
        #ease 5 zoom 3.0 xpos -1.5 ypos 1.1 # Top
        block:
            ease 4 zoom 3.0 xpos -1.5 ypos 0.8 # Low Anim
            ease 4 zoom 3.0 xpos -1.5 ypos 1.0 # Top Anim
            repeat
    with Dissolve(0.5)

    n "A modo juguetón desplaza su cuerpo verticalmente,"

    n "rozando cada tramo de tu desnuda anatomía en contacto con su ardiente piel."

    ## A006 Biting Nipple

    $ p_ao_action_Cond = ""
    scene p_ao_n_nipple_comp:
        subpixel True
        truecenter
        zoom 1.5
        xpos -1.5 ypos 0.5 # To the right
        ease 5.0 xpos 0.5
    with fade
    
    pause

    play sound "audio/characters/protagonist/au_late01.ogg"

    $ p_ao_action_Cond = "biteNipple"
    show p_ao_n_nipple_comp:
        #truecenter
        easein_quad 1.0 zoom 0.4 xpos 0.5 ypos 0.5 
    with vpunch
    with vpunch

    p "¡Auh!"

    $ p_ao_action_Cond = ""
    show p_ao_n_nipple_comp
    with Dissolve(0.5)

    ne "Tienes unos pezones muy apetitosos,"

    if gensex_ILoveYouNeus:

        extend " cariño..."

    else:

        extend " [protname]..."

    # Tongue around nipple

    $ p_ao_action_Cond = "lickNipple"
    show p_ao_n_nipple_comp:
        easein_quad 25.0 zoom 0.5
    with Dissolve(1.0)

    n "Su hirviente lengua se desliza por la zona de tu mordido pezón"

    n "mientras posa sus manos bajo tus nalgas agarrándolas con fuerza contra la pared."

    pt "¿Qué pretende...?"

    play sound "audio/sfx/fall02.ogg"

    $ p_ao_action_Cond = "neusFront_still"
    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        #zoom 0.2 xpos 0.5 ypos 0.5 # GENERAL TEST
        zoom 5.0 xpos -3.5 ypos 0.4 ## Ass
        #zoom 3.0 xpos -1.8 ypos 2.0
    with hpunch

    n "Desde tu trasero,"

    $ p_ao_action_Cond = "neusFront_abs"
    show gensex_stan02_comp_01:
        ease 5 zoom 5.0 xpos -3.4 ypos 1.4 # abs
    with Dissolve(1.0)

    n "sus dedos corretean por los laterales de tu espalda,"

    $ p_ao_action_Cond = "neusFront_pec"
    show gensex_stan02_comp_01:
        ease 5 zoom 5.0 xpos -3.3 ypos 2.5 # pec

    n "pasando por tu pecho,"

    $ p_ao_action_Cond = "neusFront_neck"
    show gensex_stan02_comp_01:
        ease 5 zoom 5.0 xpos -3.4 ypos 3.2 # belowneck

    n "tus hombros,"

    n "hasta alcanzar tu cuello."

    if music_play != "nightOfChaos":
        play music "audio/music/kevinmacleod/creepy/nightOfChaos.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nightOfChaos"


    $ p_ao_action_Cond = "neusFront_neckGrab"
    show gensex_stan02_comp_01:
        zoom 5.0 xpos -3.5 ypos 3.5 # neck
    with Dissolve(0.5)

    # Hands on the neck

    n "Esas manos te agarran por el gaznate mientras sus uñas arañan esa delgada piel cerca de tu garganta."

    pt "¡¿Es que me quiere estrangular?!"

    $ p_ao_action_Cond = "neusRide_01"
    show gensex_stan02_comp_01:
        #zoom 6.0 xpos -4.5 ypos 4.0 # Hair is visible here.
        zoom 7.0 xpos -5.5 ypos 4.5 # Is hair still visible?
    with Dissolve(1.0)

    n "Poco después, te liberan para deslizarse hasta tus hombros"

    n "agarrándote fuertemente por la región posterior del cuello -{a=https://es.wikipedia.org/wiki/Músculo_trapecio}trapecio{/a}-."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with fade_short

    ne "No hace falta que hagas nada,"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "lo único que te pido"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "es que tus piernas aguanten,"

    if gensex_ILoveYouNeus:

        extend " mi amor."

    else:
        extend " mi querido Lancelot."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx06
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    play sound "audio/sfx/fall02.ogg"

    $ p_ao_action_Cond = "neusRide_01"
    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        zoom 7.0 xpos -5.5 ypos 4.5
        easein_quad 20 zoom 3.0 xpos -1.8 ypos 0.5 # Feet
        #zoom 3.0 xpos -1.8 ypos 2.0 # Hand?
    with hpunch

    p "¿Euh?"

    n "Sujetándose aún con fuerza por el músculo que sustenta tu cuello,"

    n "libera tu polla de la presión que estaba ejerciendo con su barriga"

    n "elevando los pies del suelo para ponerlos en la pared justo al lado de tus nalgas."

    n "Soportando el -relativamente liviano- peso de su cuerpo con sus manos agarrándote cerca de los hombros,"

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade_short

    n "te dedica una siniestra sonrisa."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_action_Cond = "neusRide_01"
    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        ###zoom 1.5 xpos -0.5 ypos 0.7 # Perspective for Fucking
        zoom 3.5 xpos -1.5 ypos 2.0 # Don'¡t know where to puc the first focus
        easein_quad 5 zoom 3.0 xpos -1.2 ypos 1.1 # Close To dick-Ass
    with fade_short
        

    n "Desciende sus caderas hasta que la punta de tu miembro en erección acaricia sus ardientes labios vaginales."

    window hide dissolve
    pause

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows angryx01
    call n_closefromup_tears_tears
    with fade_short

    ne "Ahora te voy a follar."

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Pobre de ti que te caigas"

    extend " o te corras demasiado pronto."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows sadx08
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    if music_play != "funkorama":
        play music "audio/music/neus_theme.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "funkorama"

    $ p_ao_action_Cond = "neusRide_01"
    scene gensex_stan02_comp_01:
        subpixel True
        truecenter
        zoom 3.0 xpos -1.2 ypos 1.1 
        easein_quad 15 zoom 1.5 xpos -0.5 ypos 0.7 # Perspective for Fucking
    with fade

    n "Usando la pared de palanca y agarrada a tus hombros a modo de soporte,"

    $ p_ao_action_Cond = "neusRide_02"
    show gensex_stan02_comp_01
    with Dissolve(1.0)

    # $ p_ao_n_vel = 3
    # $ p_ao_action_Cond = "nride01_move"

    $ p_ao_action_Cond = "nbVaginalRide_00"
    $ p_ao_mc_legs = "stand"

    $ p_ao_n_vel = 1

    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        xpos 0.5
        #zoom 1.5 ypos -1.5 # Down?
        zoom 1.5 ypos 2.0 # OverUp
        easein_quad 4.0 zoom 1.0 ypos 1.0 # Up
    with fade_long1s

    n "empieza a introducirse tu erecto miembro en su ardiente interior."

    #Show image from other perspective, it's the first time entering and I must show the pussy getting in from that perspective.

    $ p_ao_action_Cond = "nbVaginalRide_01"
    $ p_ao_n_vel = 2
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.8 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    pt "¡Joder como quema!"

    $ p_ao_action_Cond = "nbVaginalRide_02"
    $ p_ao_n_vel = 3
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "Sin prisas, pero sin pausas, logra engullir hasta la mitad,"

    n "para luego volver a retroceder,"

    n "y así balancearse lentamente aguantándose en ti."

    scene black
    with fade

    n "De sus labios reaparece su longeva lengua que se acerca a tu otro pezón para lamerlo juguetonamente"

    $ p_ao_action_Cond = "nbVaginalRide_02"
    $ p_ao_n_vel = 4
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "mientras va aumentando el ritmo en cada nueva envestida."

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 2
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "Casi ves desaparecer por completo tu miembro en su interior."

    n "Su peso es bastante ligero, pero debido a sus fuertes acometidas contra tu pelvis,"

    n "cada vez te cuesta más mantener tus piernas firmes."

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 6
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "Sus uñas se te clavan en la carne,"

    p "Ughh..."

    n "una gota desciende hasta que se mezcla con la pared al contacto con tu espalda."

    $ p_ao_n_horns_num += 1
    call p_ao_n_changes

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 8
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(1.0)

    n "Al fijarte en Neus, en su desquiciada expresión de placer y locura,"

    n "observas en la parte frontal de su cráneo dos extrañas protuberancias."

    n "Sus ojos vuelven a brillar con intensidad."

    $ p_ao_n_vel = 6

    $ p_ao_action_Cond = "neusRide_01_06"
    show gensex_stan02_comp_01:
        truecenter
        #zoom 1.5 xpos -0.5 ypos 0.7 # General Ride camera
        # zoom 2.5 xpos -0.9 ypos 0.9 # Top ass Original
        zoom 2.5 xpos -1.05 ypos 0.75 # Top ass
        block:
            easeout 3.0/p_ao_n_vel zoom 2.5 xpos -1.2 ypos 0.6 # Down ass
            easein_quad 2.5/p_ao_n_vel zoom 2.5 xpos -1.05 ypos 0.75 # Top ass
            repeat
    with hpunch

    p "¡Ugh...!"

    $ renpy.music.set_volume(0.5, delay=2.0, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_post_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "Sus embestidas son cada vez más bruscas,"

    $ renpy.music.set_volume(0.1, delay=10.0, channel='sfx1')

    n "apenas eres capaz de mantener el tipo y tus piernas empiezan a tambalear."

    if music_play != "malicious":
        play music "audio/music/kevinmacleod/malicious.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "malicious"

    ## Alt002 #Tongue around your neck.
    $ p_ao_action_Cond = "neusTongueNeck"
    show gensex_stan02_comp_01:
        truecenter
        zoom 6.0 xpos -4.5 ypos 2.5 # Start the camming.
        ease 55.0/p_ao_n_vel zoom 5.0 xpos -3.5 ypos 3.6 # Close Shot to your Neck
        block:
            easeout 3.0/p_ao_n_vel xpos -3.5
            easein_quad 2.5/p_ao_n_vel xpos -3.4
            repeat
    with fade_short

    n "Su lengua sube por tu pecho hasta llegar a tu gaznate donde, sin prisas,"

    n "empieza a envolverse en tu cuello;"

    n "para luego presionarte con tanta fuerza"

    n "que sufres para poder respirar."

    p "[neusname],"

    extend " me estás a..."

    $ p_ao_n_vel = 8
    $ p_ao_action_Cond = "neusRide_01_06"
    show gensex_stan02_comp_01:
        truecenter
        zoom 2.5 xpos -1.05 ypos 0.75 # Top ass
        block:
            easeout_quad 3.0/p_ao_n_vel zoom 2.5 xpos -1.2 ypos 0.6 # Down ass
            easein_quad 2.5/p_ao_n_vel zoom 2.5 xpos -1.05 ypos 0.75 # Top ass
            repeat

    with hpunch
    ono "PAM"

    with hpunch
    extend " PAM"

    with hpunch
    extend " PAM"

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 15
    scene gensex_n_briding_comp vaginal_01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein_quad 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout_quad 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with fade

    n "Sin ninguna piedad sigue azotando tus caderas con una intensidad inhumana,"

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 22
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein_cubic 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout_quad 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(0.5)

    n "tienes la sensación que de seguir así, derribarás el muro con tus quebrantadas nalgas."

    $ p_ao_action_Cond = "nbVaginalRide_04"
    $ p_ao_n_vel = 40
    show gensex_n_briding_comp vaginal_01:
        truecenter
        zoom 1.0 ypos 1.0 # Up
        block:
            easein_cubic 4.0/p_ao_n_vel zoom 1.0 ypos 0.6 #
            easeout_quad 4.0/p_ao_n_vel zoom 1.0 ypos 1.0 # Up
            repeat
    with Dissolve(0.5)

    pause 1.5

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    stop music fadeout 1.0
    play sound "audio/sfx/fall02.ogg"

    scene black
    with vpunch

    p "¡ugh!"

    n "Tus piernas finalmente flaquean y caes rendido al suelo junto a ella."

    $ ped_neus_whispers_sfx04 = 0.6 # More bright in her eyes.

    p "Ughh..."

    pt "Joder,"

    extend " como me duele el trasero..."

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx08
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with fade

    ne "[protname],"

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Estás bien?"

    $ nteye = "front05"
    show n_closefromup_mouth sad_Silentx08
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    menu:

        pt "Parece preocupada y todo..."

        "¡¿A ti te parece que estoy bien después de lo que me estás haciendo?!":
            call p_Help
            $pl.ch_pts("np",-2)

            $ nteye = "front01"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "right05"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx07
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo siento,"

            $ nteye = "right03"
            show n_closefromup_mouth sad_Talkingx09
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "pero es que realmente estoy muy cachonda."

            $ nteye = "front00"
            show n_closefromup_mouth sadbiting_Silentx06
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            p "¿Y se supone que eso es una disculpa?"

            $ nteye = "front03"
            show n_closefromup_mouth sad_Talkingx09
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Tendrás que conformarte con eso,"

            $ nteye = "front02"
            show n_closefromup_mouth sad_Talkingx008
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            ne "porque no pienso parar."

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx10
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            p "..."

        "No me lo has puesto demasiado fácil, precisamente...":
            call p_Help

            $ nteye = "front00"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            p "Además tienes las uñas bastante largas..."

            $ nteye = "down01"
            show n_closefromup_mouth sadbiting_Silentx04
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            ne "Lo siento..."

            $ nteye = "right02"
            show n_closefromup_mouth sad_Talkingx08
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Es que cuando me pongo caliente pierdo un poco el control."

            $ nteye = "right05"
            show n_closefromup_mouth sadbiting_Silentx07
            show n_closefromup_eyebrows sadx05
            call n_closefromup_tears_tears
            with dissolve

            pt "Un poco dice..."

            $ nteye = "front08"
            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_eyebrows suspiciousx03
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

        "Lo siento, pero mis piernas ya no podían aguantar más.":
            call p_Help

            $ nteye = "down05"
            show n_closefromup_mouth sad_Talkingx07
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Supongo que embestirte de esa manera,"

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx04
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "mientras me agarraba a ti"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Talkingx08
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "no ha sido la mejor idea."

            $ nteye = "front07"
            show n_closefromup_mouth happybiting_Silentx07
            show n_closefromup_eyebrows sadx04
            call n_closefromup_tears_tears
            with dissolve

            pt "Supone..."

        "Me has dejado el culo hecho mierda.":
            call p_Help

            $ nteye = "front00"
            show n_closefromup_mouth sad_Silentx02
            show n_closefromup_eyebrows surprisex01
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            $ nteye = "right02"
            show n_closefromup_mouth sad_Talkingx003
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            ne "Sí..."

            $ nteye = "front07"
            show n_closefromup_mouth happy_Talkingx06
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            ne "quizás he sido un poco bruta,"

            extend " ¿verdad?"

            $ nteye = "front06"
            show n_closefromup_mouth happy_Silentx08
            show n_closefromup_eyebrows sadx03
            call n_closefromup_tears_tears
            with dissolve

            pt "Y encima se ríe."

        "...":
            call p_Help

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx06
            show n_closefromup_eyebrows suspiciousx02
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

    if music_play != "loopster":
        play music "audio/music/kevinmacleod/loopster.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "loopster"


    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Ponte de pie."

    scene black
    with vpunch

    n "Te agarra por las axilas y te vuelve a poner de pie."

    play sound "audio/sfx/fall02.ogg"

    $ p_ao_action_Cond = "alone_semi_soft"
    show gensex_stan02_comp_01:
        truecenter
        #zoom 2.5 xpos -1.5 ypos -1.65 # Feet
        #zoom 2.5 xpos -1.5 ypos 0.3 # Dick?
        zoom 2.5 xpos -1.5 ypos 1.75 # Pectoral-Mouth?
        easein_quad 20 zoom 2.5 xpos -1.5 ypos -1.65 # Feet
    with hpunch

    pt "¿Para que me lo pide si es ella misma la que me levanta?"

    ne "Esta vez intentaré algo distinto."

    pt "¡¿Es que aún no ha tenido suficiente?!"

    n "Volviendo a tener tu espalda contra la pared,"

    $ p_ao_action_Cond = "neusSback"
    show gensex_stan02_comp_01:
        ease 5 zoom 2.5 xpos -1.3 ypos -1.65 # Feet
    with Dissolve(1.0)

    n "[neusname] te da la espalda posando su trasero sobre tus piernas."

    show gensex_stan02_comp_01:
        easein_quad 10 zoom 2.5 xpos -1.3 ypos 0.2 # Neus Small Ass

    n "Incluso a pesar de estar de puntillas, debido a su altura,"

    $ p_ao_n_vel = 1

    $ p_ao_action_Cond = "neusSback_rubbing"
    show gensex_stan02_comp_01:
        # zoom 0.2 xpos 0.5 ypos 0.5 ## GENERAL TEST
        zoom 2.5 xpos -1.3 ypos 0.2
    with Dissolve(0.5)

    n "apenas llega rozarte los testículos con sus nalgas."

    $ p_ao_n_vel = 3
    show gensex_stan02_comp_01
    with Dissolve(0.5)

    n "A pesar del esfuerzo, lo único que consigue es agitar un poco tu -algo más flácido- miembro."

    $ p_ao_n_vel = 2
    show gensex_stan02_comp_01
    with Dissolve(0.5)

    ne "Hmmm...."

    p "Quizás sería mejor hacer esto en la cama."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "right02"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with hpunch

    ne "No."

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx07
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Tengo ganas de hacértelo contra la pared."

    $ nteye = "down05"
    show n_closefromup_mouth sadbiting_Silentx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_action_Cond = "neusSback"
    scene gensex_stan02_comp_01:
        subpixel True
        #zoom 0.2 xpos 0.5 ypos 0.5 # GENERAL VISION
        zoom 2.5 xpos -2.5 ypos -2.8 # Feet
        ease 15 zoom 2.0 xpos -1.75 ypos 0.25 # Her body
    with fade

    n "Te percatas de que su cuerpo desprende mucho más vapor que hasta ahora."

    $ p_ao_action_Cond = "neusBback"
    show gensex_stan02_comp_01
    with Dissolve(7.5)

    n "Quizás es tu vista nublada, pero tienes la sensación de que su cuerpo aumenta de tamaño."

#########################################################

    if config.version < "00.16.05": # NeusAfterHerOrgasm: SheGrowsSliding his ass on you.
        call endupdatescript
    
#######################################################

    pt "¡Joder!"

    pt "¡Pero si ahora es más alta que yo y todo!"

    $ p_ao_action_Cond = "neusBback_rubbing"
    show gensex_stan02_comp_01:
        subpixel True
        zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
        block:
            easein 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.5 ## Ass Up
            easeout 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
            repeat
    with Dissolve(1.0)

    n "Vuelve a posar su trasero contra ti,"

    n "y esta vez sí,"

    n "aprecias sus nalgas -bastante más esponjosas- masajeandote el escroto con suavidad."

    $ p_ao_action_Cond = "neusBback"
    # show gensex_stan02_comp_01:
    #     #zoom 3.0 xpos -2.95 ypos 0.95 # Her Face
    #     zoom 4.0 xpos -4.0 ypos 1.1 # Her Face
    # with Dissolve(1.0)
    
    show p_ao_n_behindLook_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 1.0 ypos 0.5 #Her eye Close
        easein_quad 5.0 zoom 0.5 xpos 0.75 ypos 0.5 #Her eye Far
    with fade

    ne "Mucho mejor,"

    extend " ¿no crees?"

# ###### 
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_n_behindLook_comp:
#         truecenter
#         zoom 0.2
#     pause
# ######

    p "¡¿No has dicho que tenías que ahorrar energía?!"

    show p_ao_n_behindLook_comp:
        ease_quad 5.0 zoom 1.0 xpos 1.0 ypos 0.5 #Her eye Close

    ne "Eso fue cuando solo podías tener tres corridas."

    ne "Ahora voy a ordeñar tanto tus huevos,"

    # scene gensex_stan02_comp_01:
    #     zoom 4.0 xpos -4.0 ypos 1.1 # Her Face
    # with fade

    $ p_ao_action_Cond = "neusBback_rubbing"
    scene gensex_stan02_comp_01:
        subpixel True
        zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
        block:
            easein 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.5 ## Ass Up
            easeout 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
            repeat
    with fade

    ne "que estoy convencida de que habrá esperma de sobras."

    $ p_ao_action_Cond = "neusBback_rubbing_hard"
    show gensex_stan02_comp_01:
        #truecenter
        zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
        block:
            easein 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.5 ## Ass Up
            easeout 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
            repeat
    with Dissolve(2.0)

    p "¡¿Es que se piensa que soy una vaca?!"

    n "Sufres su ardiente vagina acariciando la punta de tu glande."

    $ p_ao_action_Cond = "alone_hard"
    show gensex_stan02_comp_01:
        easein_quad 2 zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
    with Dissolve(1.0)

    n "Sin embargo, al poco tiempo de estar acariciándose con él, se aparta."

    p "¿Qué pasa?"

    ne "Tengo ganas de probar otro agujero..."

    $ p_ao_n_vel = 1

    $ p_ao_action_Cond = "neusBbackAss_analTeasing"
    #$ p_ao_action_Cond = "neusBbackAss_analHalf"
    #$ p_ao_action_Cond = "neusBbackAss_analWhole"
    

    if music_play != "coldFunk":
        play music "audio/music/kevinmacleod/happy/coldFunk.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "coldFunk"

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        #zoom 0.2 xpos 0.5 ypos 0.5 # GENERAL TEST
        zoom 1.0 ypos -0.5 # Center?
        easein_quad 20 zoom 1.0 ypos 1.0 # Dick Glans
    with fade

    n "Percibes el mismo calor en el mismo lugar,"

    n "pero esta vez no proviene de sus labios vaginales."

    if p_neus.anal_received > 0:

        ne "Al fin y al cabo,"

        extend " ya me has follado por aquí..."

        if p_neus.analDeep_received > 0:

            ne "Y no poco,"

            extend " precisamente..."

    else:

        ne "Ya que no has querido metérmela por ahí antes..."

        if p_neus.vaginal_received > 0:

            p "Porque he pensado que te gustaría más por delante."

            ne "Y lo prefiero,"

            extend " lo prefiero..."

            ne "pero también quiero que me folles por detrás..."

            pt "¡Pero si eres tú quien me está follando!"

    $ p_ao_action_Cond = "neusBbackAss_analHalf"
    show p_ao_wall_neus_b_back_comp 01:
        easein_quad 20 zoom 0.5 xpos 0.5 ypos 0.5
    with Dissolve(1.0)

    n "Lentamente, va introduciéndose tu polla en su estrecho agujero trasero."

    pt "Joder..."

    pt "Vista así parece otra mujer con este cuerpo."

    $ p_ao_action_Cond = "neusBbackAss_analHalf_round"
    show p_ao_wall_neus_b_back_comp 01:
        ease 10 zoom 0.75 xpos 0.5 ypos 0.6
    with Dissolve(1.0)

    n "Cuando apenas ha engullido la mitad de tu miembro se detiene."

    n "Dando pequeños círculos con sus caderas"

    n "sintiendo la estrecha y ardiente pared carnosa de su interior."

    $ p_ao_action_Cond = "neusBbackAss_analTeasing"

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        easein_quad 5 zoom 1.0 ypos 1.0 # Dick Glans
    with Dissolve(1.5)

    n "Con la misma parsimonia, vuelve a retroceder hasta sacársela del todo."

    $ p_ao_action_Cond = "neusBback_rubbing_hard"
    show gensex_stan02_comp_01:
        zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
        block:
            easein 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.5 ## Ass Up
            easeout 5.0/p_ao_n_vel zoom 2.5 xpos -2.5 ypos -0.75 ## Ass? Down
            repeat
    with fade

    n "Posando de nuevo sus fogosos y carnosos glúteos por tu erecto miembro"

    n "aplastándolo contra tu fría -por contraste- barriga masturbándote con ellas."

    $ p_ao_action_Cond = "neusBbackAss_analTeasing"

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        easein_quad 5 zoom 1.0 ypos 1.0 # Dick Glans
    with fade

    n "Cuando vuelve a tener la punta de tu miembro en la entrada de su orificio,"

    $ p_ao_action_Cond = "neusBbackAss_analHalfPlus"

    show p_ao_wall_neus_b_back_comp 01:
        truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 4.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 4.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    n "la zambulle de nuevo en su estrecho e hirviente interior."

    n "Esta vez consigue tragarse mucho más que la mitad."

    n "Vuelve a subir para luego bajar, moviendo su trasero"

    n "hasta que, finalmente, prácticamente toda tu polla es soterrada en su interior"

    n "con sus nalgas acariciando la carne de tu pelvis,"

    n "sin que puedas hacer nada al respecto."

    pt "¡No puedo ni mover las manos...!"

    ## You see her side face with two little horns on her front.

    $ p_ao_n_horns_num += 1
    call p_ao_n_changes

    scene p_ao_n_behindLook_comp:
        subpixel True
        truecenter
        zoom 0.5 xpos 0.75 ypos 0.5 #Her eye Far
        easein_quad 10.0 zoom 1.0 xpos 1.0 ypos 0.5 #Her eye Close
    with fade

    n "Ladeando ligeramente su cabeza te observa de reojo con un rostro mucho más adulto"

    n "pero manteniendo esa sonrisa de niña traviesa en sus labios,"

    n "una mirada lasciva"

    show p_ao_n_behindLook_comp:
        ease 5.0 zoom 0.4 xpos 0.6 ypos 0.55 #Her eye Far

    n "y lo que antes eran dos pequeñas protuberancias en su cráneo,"

    n "ahora son dos pequeños cuernos pronunciados y puntiagudos."

    ne "Te gustaría azotarme..."

    ne "¿Verdad?"

    $ p_ao_action_Cond = "neusBbackAss_analWhole"
    $ p_ao_n_vel = 2

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with fade

    n "Vuelves a sentir el vaivén de sus caderas,"

    n "pero esta vez enterrando tu polla por completo en su interior."

    $ p_ao_n_vel = 4

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    pt "¡Joder!..."

    ne "Tranquilo,"

    ne "te aseguro que van a quedar bien rojizas;"

    ne "Tanto o peor que tu pelvis."

    $ p_ao_n_vel = 8

    show p_ao_wall_neus_b_back_comp 01:
        truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    p "Ugh..."

    n "Sus caderas te embisten con más dureza."

    # Bifide Tongue-Short

    # scene black # NOT FINISHED
    # with fade

    scene bg 01
    show kiss_ f_n_07:
        truecenter
        zoom 1.5 rotate 20 ypos 0.4
    with fade

    n "Acariciando tu mejilla, acerca sus labios a los tuyos."

    show kiss_ f_n_10
    with Dissolve(0.5)

    n "Cuando entre mezcláis vuestras lenguas te percatas de que la suya es distinta,"

    show kiss_ f_n_09
    with Dissolve(0.5)

    n "no solo más caliente -obviamente-, sino como si estuviera dividida,"

    show kiss_ f_n_12
    with Dissolve(0.5)

    n "como si en realidad te estuvieran besando dos lenguas al mismo tiempo."

    show kiss_ f_n_08
    with Dissolve(0.5)

    pause 0.2
    ## p_ao_n_horns_num which number it is here?
    ## You see her adult face with those two horns. # NOT FINISHED

    $ p_ao_action_Cond = "neusBback"
    scene gensex_stan02_comp_01:
        zoom 4.0 xpos -4.0 ypos 1.1 # Her Face
    with fade

    n "Al apartarse, observas en su rostro una [neusname] mucho más adulta."

    n "parecida a la que viste en ese hotel tan extraño."

    #$ p_ao_n_vel = 1
    $ p_ao_n_vel = 12

    $ p_ao_action_Cond = "neusBback_analSex"
    show gensex_stan02_comp_01:
        # TRUECENTER no need. I kinda forgot apparently.
        zoom 2.5 
        xpos -2.1 ypos -0.6 # Tip
        block:
            easeout 6.0/p_ao_n_vel xpos -2.5 ypos -0.75 # Deep
            easein 6.0/p_ao_n_vel xpos -2.1 ypos -0.6 # Tip
            repeat
    with hpunch

    n "Sus recientes y enormes pechos se balancean en cada una de sus arremetidas"

    n "mientras sigue mirándote con lascivia y deseo."

    n "Sus ojos vuelven a brillar con intensidad,"

    n "sus jadeos aumentan,"

    n "y sus acometidas no cesan en lo más mínimo."

    # Bifide Tongue-Longer-

    ## NOT FINISHED

    $ p_ao_n_tongue = "bifid"

    scene bg 01
    show p_ao_nKiss skin:
        truecenter
        zoom 1.5
        easein_quad 5.0 zoom 0.5
    with fade

    pause 1.0

    show p_ao_nKiss bifid
    with Dissolve(5.0)

    # show kiss_ f_n_07:
    #     truecenter
    #     zoom 1.5 rotate 20 ypos 0.4
    # with fade

    n "Regresa a tu boca, esta vez con una lengua {a=https://es.wikipedia.org/wiki/Lengua_bífida}bífida{/a} mucho más larga y hambrienta."

    $ p_ao_action_Cond = "neusBbackAss_analWhole"

    $ p_ao_n_vel = 15

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0
        block:
            easeout 6.0/p_ao_n_vel ypos 0.4 #
            easein_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with vpunch

    n "Sus nalgas te impactan con tanta rudeza"

    n "que sufres los huesos de sus caderas clavándose contra tu pelvis,"

    n "presientes que finalmente tu culo romperá la pared en la que se apoya,"

    n "tus piernas vuelven a temblar"

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    show closetocum_mc

    n "y experimentas el cosquilleo particular previo a la explosión."

    n "Apartando su lengua..."

    # Her adult face watching you.

    scene black
    with fade

    ne "Estás a punto,"

    extend " ¿verdad?"


    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "alone_hardThrobbing"

    $ p_ao_dThrob_vel = 5
    $ p_ao_dickState_Cond = "throbbing"

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0
        ypos 0.4
        ease 10 ypos 1.0 # Dick Glans

    show closetocum_mc

    with fade_long1s

    n "Detiene su movimiento de cadera, y con delicadeza,"

    n "se aparta hasta sacársela por completo,"

    n "A pesar del terrible estado en el que se encuentra tu abrasada y castigada polla,"

    n "sigue palpitando manteniéndose en el aire con claros indicios de estar a punto de estallar."


    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "neusBbackAss_vaginalTeasing"
    show p_ao_wall_neus_b_back_comp 01
    with Dissolve(1.0)

    n "El abrasador tacto de sus labios vaginales vuelve acariciar la dolorida punta de tu miembro"

    $ p_ao_action_Cond = "neusBbackAss_vaginalWhole"

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    n "para luego volver a descender"

    n "hasta volver a sentirla completamente prisionera de su carnoso y ardiente interior vaginal."

    $ p_ao_n_vel = 8

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    ne "Córrete,"

    if gensex_ILoveYouNeus:

        extend " mi amor,"

    else:

        extend " [protname],"

    ne "córrete conmigo."

    $ p_ao_n_vel = 16

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    n "Reconoces el impulso de tu flujo acercarse,"

    n "recorriendo tu baja entrepierna,"

    $ p_ao_n_vel = 24

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    n "pasando por tu palpitante miembro,"

    $ p_ao_n_vel = 45

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    show cumming_mc

    $ p_ao_n_dick_num += 1
    call p_ao_n_changes

    $ p_prot.orgasm +=1
    $ p_neus.orgasm += 1

    with hpunch
    with vpunch

    pause 0.5

    $ ped_neus_whispers_sfx04 += 0.1
    play sound "audio/characters/protagonist/aaah01.ogg"

    scene black

    with hpunch
    with vpunch

    n "hasta explosionar en su ardiente interior."

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    n "Experimentas una mezcla de un incómodo placer y un punzante dolor por toda tu entrepierna."

    n "El orificio de tu glande, después de tantas corridas"

    n "y debido al ardor sufrido por el infernal interior de [neusname],"

    n "está tan sensible, que lo único que apenas experimentas en esa parte es dolor."

    $ ped_neus_whispers_sfx04 += 0.1

    if music_play != "killers":
        play music "audio/music/kevinmacleod/killers.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "killers"

    $ p_ao_n_vel = 40

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 50.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade_long1s

    n "Sus embestidas no solo aumentan de ritmo, sino que su brutalidad se vuelve tan inhumana"

    n "que ya ni siquiera tus pies tocan el suelo"

    n "y percibes -a través de tus nalgas- la pared temblar en cada nueva arremetida."

    $ ped_neus_whispers_sfx04 += 0.1
    $ p_ao_n_vel = 53

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with vpunch

    n "Apenas puedes mantener la respiración y eres incapaz de despegarte de la pared."

    $ p_ao_n_vel = 65

    show p_ao_wall_neus_b_back_comp 01:
        #truecenter
        zoom 1.0 ypos 1.0
        block:
            easein_quad 6.0/p_ao_n_vel ypos 0.4 #
            easeout_quad 6.0/p_ao_n_vel ypos 1.0
            repeat
    with vpunch

    p "[neusname]..."

    $ ped_neus_whispers_sfx04 = 1.0
    scene black

    $ renpy.music.set_volume(1.0, delay=0.8, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    with hpunch
    with hpunch
    ne "{size=50}¡AAAHHHMMmmm!{/size}"

    
    #scene black
    with fade

    n "Finalmente percibes que desacelera el ritmo de sus acometidas."

    $ ped_neus_whispers_sfx04 = 0.1
    stop music fadeout 3.0
    $ renpy.music.set_volume(0.2, delay=8.0, channel='sfx1')

    n "Vuelves a sentir el frío suelo en la planta de tus pies."

    $ p_ao_n_vel = 1
    $ p_ao_dThrob_vel = 1
    $ p_ao_dickState_Cond = "throbbing"

    $ p_ao_action_Cond = "alone_afterCum"

    play sound "audio/sfx/pop01.ogg"

    scene p_ao_wall_neus_b_back_comp 01:
        subpixel True
        truecenter
        zoom 1.0 ypos 0.4
        ease 5.0 ypos 1.0

    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 50.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with hpunch
    ono "PLOP"

    n "Como si fuera el corcho de una botella,"

    n "tu polla es liberada de su infernal vagina y cae rendida en el suelo."

    play sound "audio/sfx/fall02.ogg"

    scene black
    with vpunch
    n "Tus piernas desfallecen y caes igualmente exhausto en el suelo."

    scene black
    with fade

    jump p_neus_orgasmReal_beforeAmazonic_afterWall


label p_neus_orgasmReal_beforeAmazonic_afterWall:

    pt "¿Sigo con vida...?"

    ## NEUS ON THE GROUND

    $ renpy.music.set_volume(0.5, delay=0.8, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_post_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    scene p_ao_n_orgasmAfter_comp:
        subpixel True
        truecenter
        zoom 1.5 xpos -0.5 ypos 0.6 # Her pussy
        easein_quad 15.0 zoom 0.4 xpos 0.5 ypos 0.5 # General view
    with fade_long1s

    n "Al recobrar la vista,"

    $ renpy.music.set_volume(0.1, delay=8.0, channel='sfx1')

    n "te encuentras el trasero de [neusname] con su cuerpo original y tu corrida fluyendo por su entrepierna."

    p "[neusname],"

    extend " ¿estás bien?"

    # if music_play != "thereIsRomance":
    #     play music "audio/music/kevinmacleod/happy/thereIsRomance.ogg" fadein 3.0 fadeout 3.0
    #     $ music_play = "thereIsRomance"

    ne "Seeeh..."

    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    ne "estoy bien..."

    p "..."

    p "Quizás deberíamos descansar un poco,"

    p "pronto se hará de día."

    with vpunch

    ne "¡Ni hablar!"

    window hide dissolve
    pause

    scene black
    with fade

    n "Se pone de pie y mirándote con un deseo perturbador,"

    if music_play != "twisted":
        play music "audio/music/kevinmacleod/twisted.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "twisted"

    $ ped_neus_whispers_sfx04 = 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front00"
    show n_closefromup_mouth happy_Talkingx12
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade

    ne "¡No hay tiempo para descansar!"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    n "te agarra por debajo de los sobacos, te levanta"

    $ nteye = "front01"
    show n_closefromup_mouth happybiting_Silentx15
    show n_closefromup_eyebrows angryx06
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    #play sound "audio/sfx/fall02.ogg"

    scene black
    with vpunch

    play sound "audio/sfx/fall02.ogg"

    p "¡Ugh!"

    with hpunch

    $ p_ao_ground = "bed"

    n "y te lanza sobre la cama."

    p "¡¿Qué estás haciendo?!"

    n "Salta encima de ti con esa mirada enfermiza y unos enormes cuernos."

    # NOT FINISHED, not sure about this one.
    $ p_ao_n_horns_num += 1
    call p_ao_n_changes

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx14
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with fade

    ne "Aún no hemos terminado,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx11
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    if gensex_ILoveYouNeus:

        ne "cariño."

    else:

        ne "mi querido Lancelot."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx05
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    p "Pero [neusname]..."

    $ nteye = "front03"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with dissolve

    p "Mi polla ya no puede más..."

    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx10
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Eso es lo que tú te crees."

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx13
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Voy a hacerte una mamada que nunca antes te han hecho."

    if night04_pedrera_blowjob_DONE:

        $ nteye = "front00"
        show n_closefromup_mouth sad_Silentx03
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with dissolve

        p "Ya me la diste ayer..."

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx10
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Creo que esta vez,"

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx13
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "la sentirás algo distinta..."

    $ ped_neus_whispers_sfx04 = 0.6

    $ nteye = "front03"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with Dissolve(1.0)

    pause 1.0

    scene black
    with fade

    n "Sus ojos vuelven a brillar con intensidad mientras desciende hasta tu dolorida entrepierna."

    ## image Balt001 ... kissing dick

    # Blowjob kissing the tip of the dick being this one pretty flaccid (YOu're on the bed now.)

    $ ped_neus_whispers_sfx04 = 0.3

    # scene black
    # with fade
    $ ped_sex_general_expressionJaw_Cond = "blow_below_01"
    #$ ped_sex_general_expressionJaw_Cond = ""
    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_action_Cond = "o01_01"
    call pedrera_sex_p_general_talk
    $ ped_sex_blow_Cond = False
    $ p_ao_n_vel = 2

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"

    scene pedrera_sex_neus_oral kissingTip:
        subpixel True
        truecenter
        zoom 1.3
        ypos 2.0 # Up
        easein_quad 30.0/p_ao_n_vel ypos 0.45 # Down
        block:
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            repeat
    with fade

    n "Acariciando con sus dedos tu flácido y castigado miembro"

    # ###
    # $ ped_neus_whispers_sfx04 = 1.0
    # scene pedrera_sex_neus_oral kissingTip:
    #     truecenter
    #     zoom 0.2
    # pause
    # ###

    n "se lo acerca a sus labios mientras le da pequeños mimos y besos."

    p "No creo que eso sea suficiente,"

    p "ahora mismo me duele demasiado."

    $ ped_sex_general_expression_Cond = "lustAngry"
    show pedrera_sex_neus_oral kissingTip:
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    with Dissolve(0.5)

    ne "No seas impaciente..."

    ## image Balt002 ... licking dick

    $ p_ao_n_tongue = ""

    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_04"

    show pedrera_sex_neus_oral softLicking:
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    with Dissolve(1.0)

    n "Su lengua -más ardiente incluso que sus dedos o sus labios- empieza a lamer tu flácido y rojizo miembro"

    p "Ughh..."

    p "Duele..."

    $ ped_sex_general_expression_Cond = "lustAngry"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_01"
    show pedrera_sex_neus_oral kissingTip:
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    with Dissolve(0.5)

    play sound "audio/characters/neus/shh02.ogg"

    ne "Shhh..."

    ne "Sé lo que me hago."

    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_04"

    show pedrera_sex_neus_oral softLicking:
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    with Dissolve(1.0)

    n "Su lengua acaricia la parte inferior del extremadamente sensible glande,"

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "tongueAss00"

    ## Tongue in Ass # Balt004
    scene p_ao_mc_ass_tongues_comp 02:
        subpixel True
        truecenter
        zoom 1.0
        xpos 0.5 ypos 0.6 # Asshole Close?
        ease_quad 5.0 xpos 1.2 ypos 1.3 # Testicles Close
        #zoom 0.4 xpos 0.6 ypos 0.6 ## Whole IMage
    with fade

    n "pero al mismo tiempo, percibes otra lengua rozar la base de tus testículos,"

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "tongueAss02"
    show p_ao_mc_ass_tongues_comp 02:
        ease 15.0 zoom 0.4 xpos 0.6 ypos 0.6 ## Whole IMage
    with Dissolve(1.0)

    n "y otra, como si se pegara en el lateral derecho de la misma y te succionara con pequeños besos,"

    
    $ p_ao_n_vel = 3
    $ p_ao_action_Cond = "tongueAss03"
    show p_ao_mc_ass_tongues_comp 02
    with Dissolve(1.0)

    n "y otra..."

    $ p_ao_n_vel = 4
    $ p_ao_action_Cond = "tongueAss03"
    show p_ao_mc_ass_tongues_comp 02
    with Dissolve(1.0)

    p "¡¿Pero qué cojones?!"

    p "¡¿Pero cuántas lenguas tienes?!"

    window hide dissolve
    pause

    scene black
    with fade
    pause 0.2

    ## close face

    $ ped_neus_whispers_sfx04 = 0.2

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front08"
    show n_closefromup_mouth extra_tongueOut
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with fade_long1s

    pause 0.2

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "¿Quieres verlo?"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    menu:

        "Preferiría que no.":
            call p_Help

            $ nteye = "front08"
            show n_closefromup_mouth sad_Talkingx002
            show n_closefromup_eyebrows surprisex02
            call n_closefromup_tears_tears
            with dissolve

            ne "Como prefieras..."

            $ nteye = "front08"
            show n_closefromup_mouth sadbiting_Silentx05
            show n_closefromup_eyebrows sadx02
            call n_closefromup_tears_tears
            with dissolve

            pause 0.2

            ## image Balt003 ... sucking glans

            $ ped_sex_general_expression_Cond = "closed"
            $ ped_sex_general_action_Cond = "o02_01"
            call pedrera_sex_p_general_talk
            $ ped_sex_general_expressionJaw_Cond = ""
            $ p_ao_n_vel = 2

            show pedrera_sex_neus_oral blowjob_general:
                zoom 1.5 
                ypos 1.5 #Up
                block:
                    ease 8.0/p_ao_n_vel ypos 1.2 # Down # 8/3 = 2.66
                    ease 8.0/p_ao_n_vel ypos 1.45 #Up
                    repeat
            with Dissolve(0.5)

            n "Sin más dilación regresa a tu entrepierna con su infernal boca."

            n "Succionando por todas partes a tu afligida polla,"

            n "que a pesar del extraordinario dolor que padeces,"

            $ ped_sex_general_action_Cond = "o03_01"
            call pedrera_sex_p_general_talk
            $ p_ao_n_vel = 3

            show pedrera_sex_neus_oral blowjob_general:
                zoom 1.5 
                ypos 1.5 #Up
                block:
                    ease 12.0/p_ao_n_vel ypos 0.8 # Down # 12/3 = 4
                    ease 12.0/p_ao_n_vel ypos 1.45 #Up
                    repeat
            with Dissolve(0.5)

            n "poco a poco va recuperando su erección."

            window hide dissolve
            pause

            $ ped_neus_whispers_sfx04 = 0.2

            $ Pedrera_char_Cond = "NeusSuperClose"
            call Pedrera_char_lab

            show n_closefromup_body naked

            $ nteye = "front08"
            show n_closefromup_mouth happy_Silentx06
            show n_closefromup_eyebrows sadx01
            call n_closefromup_tears_tears
            with fade

            pause 0.2

            jump p_neus_orgasmReal_beforeAmazonic_manyTongues

        "Por supuesto que sí.":
            call p_Help

            $ nteye = "front03"
            show n_closefromup_mouth happy_Talkingx10
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Chico valiente..."

            $ nteye = "front05"
            show n_closefromup_mouth happybiting_Silentx08
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            jump p_neus_orgasmReal_beforeAmazonic_manyTongues_image

        "...":
            call p_Help

            $ nteye = "front02"
            show n_closefromup_mouth happy_Talkingx10
            show n_closefromup_eyebrows angryx02
            call n_closefromup_tears_tears
            with dissolve

            ne "Ya que no me respondes,"

            $ nteye = "front04"
            show n_closefromup_mouth happy_Talkingx08
            show n_closefromup_eyebrows angryx04
            call n_closefromup_tears_tears
            with dissolve

            ne "me imagino que tienes curiosidad..."

            $ nteye = "front05"
            show n_closefromup_mouth happy_Silentx09
            show n_closefromup_eyebrows angryx03
            call n_closefromup_tears_tears
            with dissolve

            jump p_neus_orgasmReal_beforeAmazonic_manyTongues_image


label p_neus_orgasmReal_beforeAmazonic_manyTongues_image:

    if music_play != "dayOfChaos":
        play music "audio/music/kevinmacleod/creepy/dayOfChaos.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "dayOfChaos"

    scene p_ao_nMouth_tongues:
        subpixel True
        truecenter
        zoom 2.0 ypos  1.0
        easein_quad 15.0 zoom 0.35 ypos 0.45
        ## zoom 0.3 xpos 0.5 ypos 0.5 # Whole Image.
    with fade_long1s

    p "¡¿QUÉ...?!"

    n "En lugar de un interior vació,"

    n "hay un montón de lenguas que rodean la carne de su boca,"

    n "no logras ver ningún diente,"

    n "y su lengua es ahora una especie de tentáculo invertido."

    p "¡¿QUÉ DEMONIOS?!"

    window hide dissolve
    pause

    $ ped_neus_whispers_sfx04 = 0.2

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with fade

    ne "Quizás no sea muy agradable a la vista,"

    $ nteye = "down04"
    show n_closefromup_mouth happy_Talkingx04
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "pero desde luego a tu pollón no le disgusta..."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    n "Sin dejar de rozar tu miembro con su entrepierna,"

    if music_play != "airPrelude":
        play music "audio/music/kevinmacleod/creepy/airPrelude.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "airPrelude"

    #scene bg dark_a
    scene bg_ped_04
    show kiss_ n_n_03
    with fade

    n "Se acerca a tus labios con esa monstruosa boca"

    show kiss_ f_n_07
    with Dissolve(0.5)

    n "y con sus múltiples lenguas juguetea con con la comisura de los labios"

    show kiss_ f_n_12
    with Dissolve(0.5)

    n "hasta conseguir penetrar en el interior de tu boca"

    show kiss_ f_n_11
    with Dissolve(0.5)

    n "dándote el beso más extraño que hayas sentido nunca."

    show kiss_ f_n_12
    with Dissolve(0.5)

    n "Succionando tu lengua con esos extraños tentáculos"

    # B001 # Differnt tongues inside your mouth
    scene black
    with fade

    n "mientras sus otras lenguas juguetean alrededor de esta y en tu boca entera,"

    n "como si fueran varias personas -con una boca ardiente- besándote al mismo tiempo."

    # window hide dissolve
    # pause

    if music_play != "frost_waltz":
        play music "audio/music/kevinmacleod/frost_waltz.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "frost_waltz"

    $ ped_neus_whispers_sfx04 = 0.3

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front06"
    show n_closefromup_mouth happy_Silentx07
    show n_closefromup_eyebrows normal
    call n_closefromup_tears_tears
    with fade

    n "Finalmente te libera y mirándote con cara de niña traviesa."

    $ nteye = "down03"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Creo que ya la tienes suficientemente dura."

    jump p_neus_orgasmReal_beforeAmazonic_manyTongues


label p_neus_orgasmReal_beforeAmazonic_manyTongues:

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    ne "Como puedes ver, hay pocos mortales que sean capaces de escapar a mis encantos femeninos."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    pt "No llamaría \"esto\", precisamente algo femenino..."

    if music_play != "fearless_first":
        play music "audio/music/kevinmacleod/fearless_first.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "fearless_first"

    $ p_ao_action_Cond = "back_up"

    # image B002 - She grabbing your leg

    scene p_ao_sex_legup_back_comp:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.5 ypos -0.5 # Low
        easein_quad 2.0 zoom 1.0 xpos 1.4 ypos 1.4 # MC leg
    with fade

    play sound "audio/sfx/grabarm01.ogg"

    # ###
    # $ ped_neus_whispers_sfx04 = 1.0
    # scene p_ao_sex_legup_back_comp:
    #     truecenter
    #     zoom 0.2
    # pause
    # ###

    n "Una de sus manos agarra tu pierna derecha y la eleva hasta su hombro mientras inclina tu cuerpo a un lado."

    show p_ao_sex_legup_back_comp:
        ease_quad 5.0 zoom 0.6 xpos 0.6 ypos 0.1
    with dissolve

    pt "¡¿Qué pretende hacer ahora?!"

    show p_ao_sex_legup_back_comp:
        ease_quad 5.0 zoom 1.3 xpos 0.8 ypos 0.3
    with dissolve

    n "Sujetándose en tu pierna y teniendo tu polla en erección,"

    show p_ao_sex_legup_back_comp:
        block:
            ease 2.0 xpos 0.78 ypos 0.25
            ease 2.0 xpos 0.8 ypos 0.3
            repeat
    with dissolve

    n "acaricia sus labios vaginales sobre ella."

    ## Image B003 of your dick entering her pussy?

    $ p_ao_action_Cond = "back_down"
    show p_ao_sex_legup_back_comp:
        ease 5.0 zoom 1.3 xpos 0.7 ypos -0.5 # Down 
    with Dissolve(2.0)

    n "Poco después, se la introduce de nuevo."

    n "Tu polla sufre ahogada en su estrecha y volcánica vagina."


    $ p_ao_whispers_n = 5.0
    call p_ao_whispers_label
    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 5

    $ p_ao_action_Cond = "back_moving_01"
    show p_ao_sex_legup_back_comp:
        #ease 5.0 zoom 1.3 xpos 0.7 ypos -0.5 # Down
        easein_quad 10.0 zoom 0.6 xpos 0.6 ypos 0.05
    with Dissolve(2.0)

    n "Sin ninguna compasión te empieza a cabalgar -teniendo las piernas completamente abiertas-"

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 10

    $ p_ao_action_Cond = "back_moving_a"
    show p_ao_sex_legup_back_comp:
        ease 25.0 zoom 1.3 xpos 0.7 ypos -0.5 # Down Close 
    with dissolve

    n "y sin que puedas hacer otra cosa que agarrarte a la sábana mientras te galopa."

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 20

    $ p_ao_action_Cond = "back_moving_a"
    show p_ao_sex_legup_back_comp
    with dissolve

    n "En cada nueva acometida consigue profundizar más su entrepierna en tu erecto miembro"

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 30

    $ p_ao_action_Cond = "back_moving_c"
    show p_ao_sex_legup_back_comp
    with dissolve

    n "hasta sentir sus labios vaginales contra tu pelvis."

    $ ped_neus_whispers_sfx04 -= 2
    $ p_ao_n_vel = 2

    $ p_ao_action_Cond = "back_moving_01"
    show p_ao_sex_legup_back_comp:
        easein_quad 10.0 zoom 0.6 xpos 0.6 ypos 0.05 # Far
    with Dissolve(1.0)

    ne "Hmmm..."

    $ ped_neus_whispers_sfx04 = 0.3

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "down03"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with fade

    ne "La tienes realmente enorme."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx08
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    pt "¡Como si no lo supiera!"

    ## Image B003
    # Faster

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 20
    $ p_ao_action_Cond = "back_moving_b"
    scene p_ao_sex_legup_back_comp:
        subpixel True
        truecenter
        zoom 1.3 xpos 0.7 ypos -0.5 # Down Close
        block:
            ease 4.0/p_ao_n_vel xpos 0.75 ypos -0.4 # DownUp
            ease 4.0/p_ao_n_vel xpos 0.7 ypos -0.5 # Down Close
            repeat
        
        #zoom 0.6 xpos 0.6 ypos 0.05 # Far
        #ease 30.0 zoom 1.3 xpos 0.7 ypos -0.5 # Down Close 
    with fade

    n "Su rudeza aumenta hasta que empiezas a sentir el hueso de sus caderas"

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 30
    $ p_ao_action_Cond = "back_moving_b"
    show p_ao_sex_legup_back_comp:
        zoom 1.3 xpos 0.7 ypos -0.5 # Down Close
        block:
            ease 4.0/p_ao_n_vel xpos 0.75 ypos -0.4 # DownUp
            ease 4.0/p_ao_n_vel xpos 0.7 ypos -0.5 # Down Close
            repeat
    with dissolve

    n "clavándose en tu dolorida entrepierna en cada nueva embestida."

    $ ped_neus_whispers_sfx04 += 1
    $ p_ao_n_vel = 40
    $ p_ao_action_Cond = "back_moving_c"
    show p_ao_sex_legup_back_comp:
        zoom 1.3 xpos 0.7 ypos -0.5 # Down Close
        block:
            ease 4.0/p_ao_n_vel xpos 0.75 ypos -0.4 # DownUp
            ease 4.0/p_ao_n_vel xpos 0.7 ypos -0.5 # Down Close
            repeat
    with dissolve

    pt "¡Jodeeeeer!"

    # Stops

    $ ped_neus_whispers_sfx04 -= 1
    $ p_ao_n_vel = 2

    $ p_ao_action_Cond = "back_moving_01"
    show p_ao_sex_legup_back_comp:
        easein_quad 10.0 zoom 0.6 xpos 0.6 ypos 0.05 # Far
    with vpunch

    ne "Hmmmm..."

    # Her face

    $ ped_neus_whispers_sfx04 = 0.4

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with fade

    ne "Tengo ganas de probar algo viendo lo grande que la tienes,"

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "creo que será posible y todo..."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx09
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene black
    with fade

    

    n "Suelta tu pierna que cae rendida sobre la sábana quedándote boca abajo."

    # B004  (you being alone.)
    scene black
    with fade

    n "Agarrándote fuertemente de tu afligida polla"

    scene black
    with hpunch

    n "te impulsa hacia arriba elevando tu trasero hasta posar tus rodillas sobre la cama"

    $ p_ao_action_Cond = "before_noHand"


    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 2.0 xpos -1.5 ypos -1.4 # Feet
        easein_quad 10.0 zoom 1.5 xpos 0.0 ypos 0.2 # Your ass
    with fade

    n "sin que puedas ofrecer ninguna resistencia."

    pt "¡¿Por qué coño me pone a cuatro patas?!"

    #Her hand on your buttock

    # $ p_ao_action_Cond = "before_hand"
    # show p_ao_sex_doggy_side_n_before_comp_01:
    #     zoom 1.5 xpos 0.0 ypos 0.2 # Your ass
    # with hpunch

    $ p_ao_action_Cond = "front_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        zoom 1.5 xpos 0.0 ypos 0.2 # Your ass
    with hpunch

    n "Sus manos te agarran de las nalgas con rudeza mientras posa su entrepierna justo entre tus nalgas."

    # Fucks you without a dick.
    $ p_ao_action_Cond = "back_hand"
    show p_ao_sex_doggy_side_n_before_comp_01
    pause 0.2

    #$ p_ao_assSmack = "lSmack"
    $ p_ao_action_Cond = "front_hand"
    play sound "audio/sfx/slap01.ogg"
    show p_ao_sex_doggy_side_n_before_comp_01
    with hpunch

    ono "SPLASH{w=0.3}{nw}"

    #$ p_ao_assSmack = ""
    $ p_ao_action_Cond = "back_hand"
    #$ p_ao_mcAssSmacks_list.append("l01")
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.3)

    pause 0.3

    #$ p_ao_assSmack = "lSmack"
    $ p_ao_action_Cond = "front_hand"
    play sound "audio/sfx/slap02.ogg"
    show p_ao_sex_doggy_side_n_before_comp_01
    with hpunch
    extend " SPLASH{w=0.3}{nw}"

    #$ p_ao_assSmack = ""
    $ p_ao_action_Cond = "back_hand"
    #$ p_ao_mcAssSmacks_list.append("l02")
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.3)

    pause 0.3

    #$ p_ao_assSmack = "lSmack"
    $ p_ao_action_Cond = "front_hand"
    play sound "audio/sfx/slap01.ogg"
    show p_ao_sex_doggy_side_n_before_comp_01
    with hpunch
    
    extend " SPLASH{w=0.3}{nw}"

    #$ p_ao_assSmack = ""
    $ p_ao_action_Cond = "before_hand"
    #$ p_ao_mcAssSmacks_list.append("l03")
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.3)

    pause 0.3

    # Stops having her body touching your ass.

    $ p_ao_action_Cond = "front_hand"
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(2.0)

    n "Te da tres fuertes arremetidas en tus nalgas con su entrepierna carente de cualquier objeto fálico,"

# ##### # TEST
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_sex_doggy_side_n_before_comp_01:
#         truecenter
#         zoom 0.2
#     pause
# ####

    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_quad 5.0 zoom 1.0 xpos 0.8 ypos -0.3 # Your face?

    n "como si te estuviera follando el trasero."

    # You front being doggystyle

    
# ################################

#     $ p_ao_action_Cond = "ahead_hands"

#     scene tikitesting_comp:
#         truecenter
#         zoom 0.5

#     progcheck "TESTING 01"


#     scene takeTesting_comp:
#         truecenter
#         zoom 2.5

#     progcheck "TESTING02"

#     scene p_ao_sex_doggy_front_comp_01:
#         truecenter
#         zoom 0.5

#     progcheck "TESTING03"

#     $ p_ao_action_Cond = "back_front_Hardsex"

#     scene p_ao_sex_doggy_front_comp_01:
#         truecenter
#         zoom 0.5

#     progcheck "TESTING04"

# # ############################ ## TEST

#     $ p_ao_action_Cond = "ahead_hands"

#     scene p_ao_sex_doggy_front_comp_01:
#         truecenter
#         zoom 0.4

#     progcheck "HELLOU WOROLD!"

# # ############################

    $ p_ao_action_Cond = "ahead_hands"

    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        #zoom 0.5
        #zoom 1.0 xpos 0.6 ypos -0.4 # Your face close shot.
        #ease_quad 15.0 zoom 2.0 xpos 0.5 ypos 1.4 # Closing to her face.

        zoom 1.0 xpos 0.6 ypos -0.67 # Your face close shot.
        ease_quad 15.0 zoom 2.0 xpos 0.5 ypos 1.0 # Closing to her face.

    with fade

    # pause
    # $ p_ao_assSmack = "lSmack" # Test
    # show p_ao_sex_doggy_front_comp_01
    # pause
    # $ p_ao_assSmack = "rSmack" # Test
    # show p_ao_sex_doggy_front_comp_01
    # pause



# ###### ## TEST

#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_sex_doggy_front_comp_01:
#         truecenter
#         zoom 0.2
#     pause
# ######

    p "[neusname],"

    extend " te he dicho que..."

    # She talking... which is the best veersion to show here?
    ## B005 Back?

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front07"
    show n_closefromup_mouth happy_Talkingx13
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with fade

    ne "Tranquilo hombretón,"

    extend " no voy a follarte."

    $ nteye = "down05"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Bueno,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    ne "al menos no voy a follarte tu virginal trasero..."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows angryx06
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    ## B004 Dick and her hand grabbing it.

    $ p_ao_action_Cond = "before_hand"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 1.0 xpos 0.8 ypos -0.3 # Your face?
        #easein_quad 5.0 zoom 1.5 xpos 0.0 ypos 0.2 # Your ass
        easein_quad 5.0 zoom 1.5 xpos -0.3 ypos -0.15 # Dick Streteched
    with fade

    pause 1.0

    $ p_ao_action_Cond = "before_mcDick"
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(1.0)

    n "Te agarra el mandoble y te lo retuerce hacia atrás haciendo que sobresalga de entre tus piernas"

    n "comprimiendo tus testículos con tu propia polla en el proceso."

    $ p_ao_n_vel = 3

    $ p_ao_action_Cond = "before_back_mcDick"
    show p_ao_sex_doggy_side_n_before_comp_01:
        ease_quad 15.0 zoom 0.7 xpos 0.2 ypos 0.1
    with Dissolve(1.0)

    n "Sufres el calor de sus labios vaginales juguetear con tu polla invertida"

    n "al mismo tiempo que un dolor importante en tus aplastados cojones."

    $ p_ao_action_Cond = "ahead_hands"

    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.6 ypos -0.67 # Your face close shot.
        ease_quad 15.0 zoom 2.0 xpos 0.5 ypos 1.0 # Closing to her face.
    with fade

    p "[neusname],"

    extend " mis huevos..."
    
    ne "No seas nenaza,"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with fade

    ne "tampoco te vas a quedar {a=https://es.wikipedia.org/wiki/Eunuco}eunuco{/a} por esto."

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx16
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Si en el fondo el dolor te pone más de lo que eres capaz de confesar,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    if gensex_ILoveYouNeus:

        ne "mi amor..."

    else:

        ne "cariño..."

    $ nteye = "front02"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"


    ## B004 Long tongue around your body (with her hair)

    $ p_ao_action_Cond = "back_tongue"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 3.0 xpos -0.5 ypos 1.3 # Beginning tongue
        ease 8.0 zoom 2.5 xpos -0.2 ypos 0.3 ## Ass TOngue
    with fade

    n "Por tu espalda adviertes del calor de lo que parece su lengua,"

    n "junto con algo que no es tan caliente ni húmedo,"

    n "como si estuviera arrastrando algo."

    pt "¿Qué...?"

    #########################################################

    if config.version < "00.16.07": # NeusAfterHerOrgasm: LongTongueoverYourBackToStrangle
        call endupdatescript
    
    #######################################################

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 5.0 zoom 2.5 xpos 0.7 ypos -0.7 # Back

    n "Recorre por tus omóplatos,"

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 5.0 zoom 2.5 xpos 1.5 ypos -1.2 # Shoulder

    n "pasando por tu hombro izquierdo,"

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 5.0 zoom 2.5 xpos 1.8 ypos -1.5 # Neck

    n "hasta acercarse a tu cuello,"

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 15.0 zoom 0.75 xpos 0.6 ypos 0.2 # Whole tongue picture

    n "a esa altura consigues ver lo que lleva arrastrando."

    pt "¡¿Tan largo tenía el cabello?!"

    pt "¡¿O es que también puede estirarlo como su lengua?!"

    n "Empieza a rodearte el cuello con ese mechón de pelo"

    n "hasta que finalmente lo remata con un nudo"

    n "gracias a su inhumana y habilidosa lengua."

    pause

    $ p_ao_action_Cond = "before_mcDick"
    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 15.0 zoom 2.5 xpos 1.8 ypos -1.5 # Neck
    with Dissolve(2.0)

    n "Regresa solitaria por tu espalda"

    n "hasta que pierdes su tacto a la altura de tus nalgas."

    ## B004  Your neck sorrounded by her hair.

    play sound "audio/characters/protagonist/au01.ogg"

    $ p_ao_action_Cond = "front_knot"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        zoom 1.0 xpos 0.7 ypos 0.7 # Neck Up
        ease 5.0 zoom 0.75 xpos 0.6 ypos 0.5
    with vpunch

    p "¡Ugh!"

    n "Sufres un fuerte tirón en la atadura del cuello."

    ne "Ni se te ocurra correrte hasta que te de permiso,"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with fade_short

    ne "¿me explico?"

    $ nteye = "front02"
    show n_closefromup_mouth happy_Talkingx12
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Estoy disfrutando demasiado este momento como para que me termines pronto."

    $ nteye = "front03"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    n "Con la mano que no está sujetando el pelo..."

    play sound "audio/sfx/slap01.ogg"

    $ p_ao_assSmack = "lSmack"
    $ p_ao_action_Cond = "front_knot_slap"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 0.0 ypos 0.2 ## Ass Smack
        ease 10.0 zoom 0.75 xpos 0.6 ypos 0.5
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    ono "SLAP{w=0.4}{nw}"


    # $ p_ao_mcAssSmacks_list.append("l01")
    # $ p_ao_assSmack = ""
    # $ p_ao_action_Cond = "front_knot"

    $ p_ao_assSmacked = "left"
    call p_ao_n_changes

    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(1.0)

    p "¡Auch!"

    p "¡¿Hace falta que me azotes las nalgas?!"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    
    if p_neus.buttockSlaps_received > 1:

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows surprisex02
        call n_closefromup_tears_tears
        with fade_short

        ne "No parecía que te molestara tanto cuando me lo has hecho a mi."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx006
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        ne "Así que no te quejes."

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx09
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade_short

        ne "Da las gracias que no te haga otra cosa ahora mismo."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        ne "Además..."

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows surprisex03
        call n_closefromup_tears_tears
        with dissolve

        ne "si no me las has azotado antes,"

        $ nteye = "front02"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        ne "es porque no has querido."

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx06
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

    $ p_ao_action_Cond = "back_sex_hair"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos -0.4 ypos -0.2 # Ass
        ease_quad 15.0 zoom 0.7 xpos 0.43 ypos 0.28 # General View  
    with fade

    n "Agarrando tu polla invertida e inclinando ligeramente su cuerpo hacia atrás,"

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "back_front_sex_hair"
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(1.0)
        # truecenter
        # #zoom 0.2
        # zoom 1.0 xpos 0.15 ypos 0.25 # Front
        # block:
        #     easeout_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.1 ypos 0.2 # Back
        #     easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.15 ypos 0.22 # Front
        #     repeat

    n "logra introducirse tu miembro en su diabólico interior"

    n "mientras te sigue estrangulando con su propio pelo forzándote a levantar la cabeza."

    n "Va aplicando presión a sus caderas, agarrándose a tus nalgas, para introducirse tu miembro."

    $ p_ao_action_Cond = "back_front_sex_hair"
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 ypos 0.4 #Your Ass (Not back)
        ease 5.0 zoom 2.5 zoom 2.5 xpos 0.5 ypos 1.32 # Close to her face.
    with fade

    p "[neusname],"

    extend " no..."

    p "no hace falta que me estrangules..."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows surprisex03
    call n_closefromup_tears_tears
    with fade_short

    ne "Tranquilo,"

    extend " sé lo que me hago."

    $ nteye = "down05"
    show n_closefromup_mouth happy_Silentx05
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pt "No estoy yo muy seguro a estas alturas..."

    $ p_ao_action_Cond = "back_front_sex_hair"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos -0.4 ypos -0.2 # Ass
        ease 5.0 zoom 0.85 xpos 0.6 ypos 0.6 # Your face up
        #zoom 2.0 xpos -0.4 ypos -0.2 # Ass
        #ease_quad 15.0 zoom 0.7 xpos 0.43 ypos 0.28 # General View 
    with fade

    n "Desplaza su pelvis en horizontal hasta que la ardiente piel de sus caderas acaricia tus nalgas."

    play sound "audio/sfx/fall01.ogg"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        truecenter
        zoom 0.85 xpos 0.6 ypos 0.6 # Your face up
        easein_elastic 1.0 zoom 1.5 xpos 1.3 ypos -0.8 #Your face down
    with vpunch

    n "Finalmente aligera la presión que te hacía con su correa-pelo"

    p "Aaaahhh-{w=0.4}{nw}"

    extend "aaahhh-{w=0.4}{nw}"

    extend "aaahhh...."

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 5.0 zoom 1.0 xpos 0.2 ypos 0.25 # Back to your ass.

    n "y tu cabeza cae rendida sobre la sábana mientras recuperas el aliento."

    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "back_front_sex"
    show p_ao_sex_doggy_side_n_before_comp_01
    with dissolve

    n "Con tranquilidad y un toque de malicia,"

    n "emprende el movimiento de vaivén en sus caderas,"

    n "tragándose completamente tu miembro en cada acometida."

    pt "¡¿Me está follando?!"

    pt "¡¿O auto-follándose?!"

    $ p_ao_n_vel = 3
    show p_ao_sex_doggy_side_n_before_comp_01:
        zoom 1.0 xpos 0.2 ypos 0.25 # Back to your ass
        block:
            easeout 4.0/p_ao_n_vel xpos 0.13
            easein_elastic 4.0/p_ao_n_vel xpos 0.18
            repeat

    with dissolve

    n "A pesar de que apenas percibes nada del ombligo para abajo,"

    n "tienes la sensación de que tu cuerpo está completamente calcinado y destruido,"

    n "del agarrotamiento y dolor extremo en tu miembro;"

    n "no puedes evitar experimentar una presión extraordinaria que lejos de ahogarte y aplastar tu miembro,"

    n "logra reavivar el impulso sanguíneo que recorre de nuevo esa castigada y moribunda parte."

    pt "¡¿Por qué diablos sigue poniéndose dura?!"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easeout 4.0/p_ao_n_vel xpos 0.13
    with Dissolve(0.5)

    pause 0.5

    play sound "audio/sfx/slap01.ogg"

    $ p_ao_action_Cond = "front_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 4.0/p_ao_n_vel xpos 0.18

    with hpunch
    ono "SPLASH"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easeout 4.0/p_ao_n_vel xpos 0.13
    with Dissolve(0.5)

    pause 0.5

    play sound "audio/sfx/slap02.ogg"

    $ p_ao_action_Cond = "front_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 4.0/p_ao_n_vel xpos 0.18

    with hpunch
    extend " SPLASH"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easeout 4.0/p_ao_n_vel xpos 0.13
    with Dissolve(0.5)

    pause 0.5

    play sound "audio/sfx/slap03.ogg"

    $ p_ao_action_Cond = "front_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 4.0/p_ao_n_vel xpos 0.18

    with hpunch
    extend " SPLASH"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 4.0/p_ao_n_vel xpos 0.13
    with Dissolve(0.5)

    pause

    $ p_ao_n_vel = 5

    $ p_ao_action_Cond = "back_front_hardSex"
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        zoom 2.0 ypos 3.3 # Over HER hEAD.
        easein_quad 15.0 zoom 1.5 ypos 0.5 # YOur ass.
    with fade

    n "Al mismo tiempo que sufres sus caderas impactando con tu trasero sin clemencia alguna,"

    window hide dissolve
    pause

    play sound "audio/sfx/slap02.ogg"

    $ p_ao_assSmack = "rSmack"
    $ p_ao_action_Cond = "back_front_hardSex"
    show p_ao_sex_doggy_front_comp_01:
        truecenter
        zoom 1.0 ypos 0.5
        easein_elastic 1.5 zoom 1.5 # YOur ass.
        ease 5.0 zoom 1.0
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch

    n "su mano vuelve azotarte tus doloridas y rojizas nalgas."
    
    $ p_ao_action_Cond = "back_hands"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("r01")

    $ p_ao_assSmacked = "right"
    call p_ao_n_changes

    show p_ao_sex_doggy_front_comp_01:
        zoom 0.8 ypos 0.8 # Mostly her face?
    with Dissolve(1.0)

    ne "Aún no perra."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx10
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with fade_short

    ne "Quiero disfrutar esto un poco más."

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx09
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    play sound "audio/characters/protagonist/au01.ogg"

    $ p_ao_action_Cond = "back_sex_hair"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        zoom 1.5 xpos 1.3 ypos -0.8 #Your face down
        easein_elastic 1.0 zoom 1.5 xpos 1.1 ypos 0.6 #His face upClose
    with hpunch

    n "Te tira tan fuerte del cuello que sin poder evitarlo levantas parte de tu cuerpo y necesitas tus manos para sujetarte."

    show p_ao_sex_doggy_side_n_before_comp_01:
        ease 5.0 zoom 0.85 xpos 0.6 ypos 0.6 # Your face up
    with dissolve

    p "[neusname]..."

    p "no puedo respirar..."

    play sound "audio/sfx/slap03.ogg"

    $ p_ao_action_Cond = "front_sex_hair"
    $ p_ao_assSmack = "lSmack"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 1.0 zoom 2.0 xpos -0.1 ypos 0.2 # Ass Smack
        ease 2.0 zoom 1.5 xpos 0.0 ypos 0.3 # Ass a bit far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    ono "SPLASH"

    $ p_ao_action_Cond = "back_sex_hair"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("l02")

    $ p_ao_assSmacked = "left"
    call p_ao_n_changes
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.5)
    pause 0.4

    play sound "audio/sfx/slap01.ogg"

    $ p_ao_action_Cond = "front_sex_hair"
    $ p_ao_assSmack = "lSmack"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 1.0 zoom 2.0 xpos -0.1 ypos 0.2 # Ass Smack
        ease 2.0 zoom 1.5 xpos 0.0 ypos 0.3 # Ass a bit far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    extend " SPLASH"

    $ p_ao_action_Cond = "back_sex_hair"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("l03")

    $ p_ao_assSmacked = "left"
    call p_ao_n_changes

    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.5)
    pause 0.4

    play sound "audio/sfx/slap02.ogg"

    $ p_ao_action_Cond = "front_sex_hair"
    $ p_ao_assSmack = "lSmack"
    show p_ao_sex_doggy_side_n_before_comp_01:
        easein_elastic 1.0 zoom 2.0 xpos -0.1 ypos 0.2 # Ass Smack
        ease 2.0 zoom 1.5 xpos 0.0 ypos 0.3 # Ass a bit far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    extend " SPLASH"

    $ p_ao_action_Cond = "back_sex_hair"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("l04")

    $ p_ao_assSmacked = "left"
    call p_ao_n_changes

    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.5)
    pause 0.4

    n "Haciendo oídos sordos y sin ninguna compasión,"

    $ p_ao_n_vel = 4
    $ p_ao_action_Cond = "back_front_hardSex_hair"
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(0.5)

    n "sigue dándote tan fuerte que tus nalgas pasan del rojizo vibrante al morado,"

    n "si sus cachetadas no fueran suficientes, el impacto de su caderas con tu trasero, tampoco ayuda."

    if music_play != "deadly_roulette":
        play music "audio/music/kevinmacleod/deadly_roulette.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "deadly_roulette"

    $ p_ao_n_vel = 2
    # Is inverted??? I DON'T GET IT!
    scene p_ao_mc_ass_tongueAss_invert_comp 01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 1.3 xpos 0.5 ypos 1.5
        easein_quad 5.0 zoom 1.0 xpos 0.5 ypos 0.3
    with fade

    n "Su longeva y ardiente lengua empieza a juguetear con tu orificio anal."

    p "[neusname]..."

    n "El impulso de correrte regresa a pesar del estrangulamiento."

    window hide dissolve
    pause

    play sound "audio/characters/protagonist/auau_late01.ogg"

    scene black
    show p_ao_n_grabBalls_comp 01:
        truecenter
        xzoom -1.0
        zoom 1.0
        easein_elastic 1.0 zoom 0.5 xpos 0.6 ypos 0.55 # InvertedCentered the Grab
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
    with vpunch

    p "¡AUCH!"

    n "Padeces un fuerte pinchazo en tus aplastados testículos."

    ne "Aún no te he dado permiso."

    $ p_ao_n_size = "_big"

    n "Tienes la sensación que su cuerpo aumenta de tamaño."

    play sound "audio/sfx/slap03.ogg"

    $ p_ao_assSmack = "rSmack"
    $ p_ao_action_Cond = "ahead_noHand"
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 1.75 xpos 0.7 ypos 0.4 # A bit Far.
        easein_elastic 1.0 zoom 2.5 xpos 0.9 ypos 0.35 # Close to your Right ass.
        ease 2.0 zoom 1.75 xpos 0.5 ypos 0.4 # A bit Far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    ono "SPLASH"

    
    $ p_ao_action_Cond = "back_hands"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("r02")
    $ p_ao_assSmacked = "right"
    call p_ao_n_changes

    show p_ao_sex_doggy_front_comp_01
    with Dissolve(0.5)
    pause 0.5

    play sound "audio/sfx/slap01.ogg"

    $ p_ao_assSmack = "rSmack"
    $ p_ao_action_Cond = "ahead_noHand"
    show p_ao_sex_doggy_front_comp_01:
        easein_elastic 1.0 zoom 2.5 xpos 0.9 ypos 0.35 # Close to your Right ass.
        ease 2.0 zoom 1.75 xpos 0.5 ypos 0.4 # A bit Far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    extend "SPLASH"

    
    $ p_ao_action_Cond = "back_hands"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("r02")

    $ p_ao_assSmacked = "right"
    call p_ao_n_changes

    show p_ao_sex_doggy_front_comp_01
    with Dissolve(0.5)
    pause 0.5

    play sound "audio/sfx/slap02.ogg"

    $ p_ao_assSmack = "rSmack"
    $ p_ao_action_Cond = "ahead_noHand"
    show p_ao_sex_doggy_front_comp_01:
        easein_elastic 1.0 zoom 2.5 xpos 0.9 ypos 0.35 # Close to your Right ass.
        ease 2.0 zoom 1.75 xpos 0.5 ypos 0.4 # A bit Far.
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    extend "SPLASH"

    $ p_ao_action_Cond = "back_hands"

    # $ p_ao_assSmack = ""
    # $ p_ao_mcAssSmacks_list.append("r02")

    $ p_ao_assSmacked = "right"
    call p_ao_n_changes

    show p_ao_sex_doggy_front_comp_01:
        ease 5.0 zoom 1.0 xpos 0.5 ypos 0.75
    with Dissolve(0.5)

    ne "Que pollón tienes,"

    if gensex_ILoveYouNeus:

        extend " cariño..."
    else:

        extend " tigre..."

    window hide dissolve
    pause

    $ p_ao_action_Cond = "back_sex_hair"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        truecenter
        zoom 1.5 xpos 1.0 ypos 0.7 # Your face up Close
    with fade

    pause 0.2

    play sound "audio/sfx/fall01.ogg"

    $ p_ao_action_Cond = "back_sex_hand"
    show p_ao_sex_doggy_side_n_before_comp_01:
        truecenter
        #zoom 0.85 xpos 0.6 ypos 0.6 # Your face up
        easein_elastic 1.0 zoom 1.5 xpos 1.3 ypos -0.8 #Your face down
    with vpunch

    n "Tu cabeza cae de nuevo sobre la cama al sentirse libre de la presión que ejercía sobre tu cuello."

    $ p_ao_n_vel = 5
    $ p_ao_action_Cond = "back_front_hardSex"
    show p_ao_sex_doggy_side_n_before_comp_01:
        #ease 5.0 zoom 1.0 xpos 0.2 ypos 0.25 # Back to your ass.
        ease 5.0 zoom 0.5 xpos 0.5 ypos 0.45
    with dissolve

    n "Unas manos mucho más grandes te sujetan de las nalgas para que tus piernas no desfallezcan"

    $ p_ao_n_blur = "_b01"
    $ p_ao_n_vel = 10
    $ p_ao_action_Cond = "back_front_hardSex"
    show p_ao_sex_doggy_side_n_before_comp_01:
        zoom 0.6 ypos 0.45 xpos 0.4
        block:
            ease 4.0/p_ao_n_vel xpos 0.45 # Left
            easein_elastic 4.0/p_ao_n_vel xpos 0.43 # Right
            repeat
    with dissolve

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    n "mientras sigue embistiéndote con rudeza."

    $ p_ao_whispers_n = 5.0
    $ ped_neus_whispers_sfx04 += 0.1
    call p_ao_whispers_label

    $ p_ao_n_blur = "_b02"
    $ p_ao_n_vel = 20
    show p_ao_sex_doggy_side_n_before_comp_01:
        zoom 0.75 ypos 0.3 xpos 0.3
        block:
            ease 4.0/p_ao_n_vel xpos 0.3 # Left
            easein_elastic 4.0/p_ao_n_vel xpos 0.27 # Right
            repeat
    with dissolve

    n "Cuando el flujo de tu esperma vuelve a removerse en tu interior..."

    $ ped_neus_whispers_sfx04 += 0.1
    call p_ao_whispers_label

    $ p_ao_action_Cond = "back_front_sex"
    $ p_ao_n_blur = "_b03"
    $ p_ao_n_vel = 30
    show p_ao_sex_doggy_side_n_before_comp_01:
        zoom 1.0 ypos 0.25 xpos 0.2
        block:
            ease_elastic 4.0/p_ao_n_vel xpos 0.17 # Left
            ease_elastic 4.0/p_ao_n_vel xpos 0.1 # Right
            repeat
    with vpunch

    p "¡AUCH!"

    $ ped_neus_whispers_sfx04 += 0.1
    call p_ao_whispers_label

    $ p_ao_action_Cond = "back_front_hardSex"
    $ p_ao_n_blur = ""
    #$ p_ao_n_vel = 5
    scene p_ao_sex_doggy_front_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 1.5 xpos 0.5 ypos 0.5 # your ASS.
        block:
            easein_quad 4.0/p_ao_n_vel ypos 0.55
            easein_elastic 4.0/p_ao_n_vel ypos 0.4
            repeat

    show closetocum_mc
    with hpunch

    p "No puedo más..."

    $ p_ao_n_vel = 2
    show p_ao_sex_doggy_front_comp_01:
        #ease 5.0 zoom 1.0 xpos 0.5 ypos 0.5
        ease 8.0/p_ao_n_vel zoom 0.8 xpos 0.5 ypos 1.0 # Closer to her Face-Smile
        block:
            easein_quad 4.5/p_ao_n_vel ypos 0.95
            easein_elastic 3.5/p_ao_n_vel ypos 1.0
            repeat
    with Dissolve(1.0)

    ne "Suplícamelo."

    menu:

        pt "¡¿Que lo suplique?!"

        "No pienso hacer eso.":
            call p_Help

            play sound "audio/sfx/slap03.ogg"

            $ p_ao_assSmack = "rSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            #$ p_ao_mcAssSmacks_list.append("r03")

            $ p_ao_assSmacked = "right"
            call p_ao_n_changes

            play sound "audio/characters/protagonist/auau_late01.ogg"

            scene black
            show p_ao_n_grabBalls_comp 01:
                truecenter
                xzoom -1.0
                zoom 1.0
                easein_elastic 1.0 zoom 0.5 xpos 0.6 ypos 0.55 # InvertedCentered the Grab
                easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5
            with vpunch

            n "Vuelves a sentir sus dedos clavándose en tus testículos impidiéndote lograr el orgasmo."

            ne "Suplícamelo."

            window hide dissolve
            pause

            play sound "audio/sfx/slap01.ogg"

            $ p_ao_assSmack = "rSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            pause 0.5

            $ p_ao_assSmacked = "right"
            call p_ao_n_changes
            $ p_ao_action_Cond = "back_front_hardSex"

            show p_ao_sex_doggy_front_comp_01:
                #ease 5.0 zoom 1.0 xpos 0.5 ypos 0.5
                ease 8.0/p_ao_n_vel zoom 0.8 xpos 0.5 ypos 1.0 # Closer to her Face-Smile
                block:
                    easein_quad 4.5/p_ao_n_vel ypos 0.95
                    easein_elastic 3.5/p_ao_n_vel ypos 1.0
                    repeat
            with Dissolve(1.0)

            menu:
                pt "¡¿Se puede saber dónde está esa chica cándida y tímida?!"

                "¡He dicho que no pienso suplicártelo!":
                    call p_Help

                    ne "Te gusta hacerte el duro, ¿Verdad?"

                    ne "Chico travieso..."

                    play sound "audio/sfx/slap02.ogg"

                    $ p_ao_assSmack = "rSmack"
                    $ p_ao_action_Cond = "ahead_noHand"
                    scene p_ao_sex_doggy_front_comp_01:
                        subpixel True
                        truecenter
                        zoom 1.0
                        easein_bounce 1.0 zoom 2.0 # your ASS.
                        ease 5.0 zoom 1.0
                    $ p_ao_assSmacked = "before"
                    call p_ao_n_changes
                    with hpunch
                    ono "SPLASH"

                    #$ p_ao_mcAssSmacks_list.append("r04")

                    $ p_ao_assSmacked = "right"
                    call p_ao_n_changes
                    show p_ao_sex_doggy_front_comp_01
                    with dissolve
                    pause 0.5

                    play sound "audio/sfx/slap03.ogg"

                    $ p_ao_assSmack = "lSmack"
                    $ p_ao_action_Cond = "ahead_noHand"
                    show p_ao_sex_doggy_front_comp_01:
                        truecenter
                        zoom 1.0
                        easein_bounce 1.0 zoom 2.0 # your ASS.
                        ease 5.0 zoom 1.0
                    $ p_ao_assSmacked = "before"
                    call p_ao_n_changes
                    with hpunch
                    ono "SPLASH"

                    #$ p_ao_mcAssSmacks_list.append("l05")

                    $ p_ao_assSmacked = "left"
                    call p_ao_n_changes
                    $ p_ao_assSmack = ""
                    $ p_ao_action_Cond = "back_front_hardSex"
                    show p_ao_sex_doggy_front_comp_01:
                        #ease 5.0 zoom 1.0 xpos 0.5 ypos 0.5
                        ease 8.0/p_ao_n_vel zoom 0.8 xpos 0.5 ypos 1.0 # Closer to her Face-Smile
                        block:
                            easein_quad 4.5/p_ao_n_vel ypos 0.95
                            easein_elastic 3.5/p_ao_n_vel ypos 1.0
                            repeat
                    with Dissolve(0.5)

                    p "¡Ugh...!"

                    jump p_neus_orgasmReal_beforeAmazonic_p_refuse

                "Por favor...":
                    call p_Help

                    jump p_neus_orgasmReal_beforeAmazonic_p_please

        "Por favor...":
            call p_Help

            jump p_neus_orgasmReal_beforeAmazonic_p_please

        "...":
            call p_Help

            ne "¡He dicho que me lo supliques!"

            play sound "audio/sfx/slap03.ogg"

            $ p_ao_assSmack = "rSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            $ p_ao_action_Cond = ""
            show p_ao_sex_doggy_front_comp_01:
                ease 5.0 zoom 0.75 xpos 0.5 ypos 0.6 ## Talkative
            with Dissolve(0.5)

            jump p_neus_orgasmReal_beforeAmazonic_p_refuse

label p_neus_orgasmReal_beforeAmazonic_p_refuse:

    ne "Podemos estar así toda la noche..."

    p "Eres tú quien ha dicho que tenemos el tiempo limitado..."

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"

    $ p_ao_action_Cond = "back_hands"
    show p_ao_sex_doggy_front_comp_01:
        easein_quad 2.0 zoom 0.8 ypos 0.5
    with Dissolve(0.5)

    ne "..."

    $ ped_neus_whispers_sfx04 = 0.6
    call p_ao_whispers_label

    ne "Maldita sea..."

    ne "Se me había olvidado."

    pt "¡¿Se le había olvidado?!"

    jump p_neus_orgasmReal_beforeAmazonic_doggyOrgasm

label p_neus_orgasmReal_beforeAmazonic_p_please:

    play sound "audio/sfx/slap01.ogg"

    $ p_ao_assSmack = "rSmack"
    $ p_ao_action_Cond = "ahead_noHand"
    show p_ao_sex_doggy_front_comp_01:
        truecenter
        zoom 1.0
        easein_bounce 1.0 zoom 2.0 # your ASS.
        ease 5.0 zoom 1.0
    $ p_ao_assSmacked = "before"
    call p_ao_n_changes
    with hpunch
    ono "SPLASH"

    $ p_ao_assSmacked = "right"
    call p_ao_n_changes

    $ p_ao_action_Cond = ""
    show p_ao_sex_doggy_front_comp_01:
        ease 5.0 zoom 0.75 xpos 0.5 ypos 0.6 ## Talkative
    with Dissolve(0.5)

    ne "¡¿Esto lo llamas suplicar?!"

    $ p_ao_action_Cond = "back_hands"
    show p_ao_sex_doggy_front_comp_01
    with vpunch

    n "Sufres sus dedos clavándose con más fuerza."

    menu:

        pt "Suerte que era tímida..."

        "Te lo pido...":
            call p_Help

            play sound "audio/sfx/slap02.ogg"

            $ p_ao_assSmack = "lSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            $ p_ao_assSmacked = "left"
            call p_ao_n_changes

            $ p_ao_action_Cond = ""
            show p_ao_sex_doggy_front_comp_01:
                ease 5.0 zoom 0.75 xpos 0.5 ypos 0.6 ## Talkative
            with Dissolve(0.5)

            ne "¡¿Qué clase de súplica es esta?!"

            ne "¡¿Es que quieres que te desvirgue?!"

            p "¡No!"

            p "No por favor..."

            ne "Entonces suplícamelo."

            p "¡Te lo suplico!"

            p "¡Te lo ruego!"

            p "¡Déjame terminar!"

            jump p_neus_orgasmReal_beforeAmazonic_p_supplication

        "¡Te lo suplico! ¡Te lo ruego! ¡Déjame terminar!":
            call p_Help

            jump p_neus_orgasmReal_beforeAmazonic_p_supplication

        "¡No soy tu esclavo!":
            call p_Help

            play sound "audio/sfx/slap03.ogg"

            $ p_ao_assSmack = "lSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            $ p_ao_assSmacked = "left"
            call p_ao_n_changes

            $ p_ao_action_Cond = ""
            show p_ao_sex_doggy_front_comp_01:
                ease 5.0 zoom 0.75 xpos 0.5 ypos 0.6 ## Talkative
            with Dissolve(0.5)

            ne "No..."

            $ p_ao_action_Cond = "back_hands"
            show p_ao_sex_doggy_front_comp_01
            with dissolve

            ne "Ahora eres mi perro."

            p "¡No soy ningún perro!"

            play sound "audio/sfx/slap01.ogg"

            $ p_ao_assSmack = "rSmack"
            $ p_ao_action_Cond = "ahead_noHand"
            show p_ao_sex_doggy_front_comp_01:
                truecenter
                zoom 1.0
                easein_bounce 1.0 zoom 2.0 # your ASS.
                ease 5.0 zoom 1.0
            $ p_ao_assSmacked = "before"
            call p_ao_n_changes
            with hpunch
            ono "SPLASH"

            $ p_ao_assSmacked = "right"
            call p_ao_n_changes

            $ p_ao_action_Cond = ""
            show p_ao_sex_doggy_front_comp_01:
                ease 5.0 zoom 0.75 xpos 0.5 ypos 0.6 ## Talkative
            with Dissolve(0.5)

            menu:

                pt "¡La madre que la parió!"

                "¡Te lo suplico! ¡Te lo ruego! ¡Déjame terminar!":
                    call p_Help

                    jump p_neus_orgasmReal_beforeAmazonic_p_supplication

                "¡Me niego a suplicarte nada!":
                    call p_Help

                    ne "Hmmm..."

                    jump p_neus_orgasmReal_beforeAmazonic_p_refuse

label p_neus_orgasmReal_beforeAmazonic_p_supplication:

    ne "Hmmmm..."

    ne "Esto está mucho mejor."

    jump p_neus_orgasmReal_beforeAmazonic_doggyOrgasm


label p_neus_orgasmReal_beforeAmazonic_doggyOrgasm:

    $ p_ao_n_blur = ""
    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "front_sex_hair"
    scene p_ao_sex_doggy_side_n_before_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 1.0 
        xpos 0.8 ypos 0.6 # Your neck
        easein_quad 5.0 xpos 0.0 ypos 0.3 # YourAss
    show closetocum_mc
    with fade

    pause 0.2

    $ p_ao_action_Cond = "back_sex_hair"
    show p_ao_sex_doggy_side_n_before_comp_01
    with Dissolve(1.0)

    n "Se aparta de tus nalgas liberando tu polla de su infernal vagina"

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    n "Sin abandonar la correa-pelo en tu cuello se pone boca arriba en la cama"

    ## Neus below you (Big Neus) ## NOT FINISHED

    $ p_ao_n_dick = "_r_05" # It should be 5 already...
    #$ saturation_tint_level = "default" # NOT FINISHED, just for test.
    $ p_ao_action_b_Cond = ""
    $ p_ao_action_Cond = "slideDown"

    scene p_ao_cumInMouthAdult_comp_01:
        subpixel True
        truecenter
        zoom 1.0 xpos -0.3 ypos 0.1 # Her body
        pause 1.3
        easein_quad 1.0 zoom 1.0 xpos 0.6 ypos 0.1 # Her face.
    show closetocum_mc
    with fade

# #### TEST
#     $ p_ao_action_Cond = "slideDown"
#     show p_ao_cumInMouthAdult_comp_01
#     progcheck "slideDown"
#     #cumFace
#     $ p_ao_action_Cond = "cumFace"
#     show p_ao_cumInMouthAdult_comp_01
#     progcheck "cumFace"
#     $ p_ao_action_Cond = "suckDown"
#     show p_ao_cumInMouthAdult_comp_01
#     progcheck "suckDown"
#     $ p_ao_action_b_Cond = "armAss"
#     $ p_ao_action_Cond = "suckUp"
#     show p_ao_cumInMouthAdult_comp_01
#     progcheck "suckUp"
# ####

    n "e intenta agarrarse a tus nalgas mientras desliza su cabeza entre tus piernas."

    n "Pero debido a la libertad de la que goza ahora tu polla, tus testículos recuperan su espacio y sin que puedas evitarlo,"

    $ p_ao_action_Cond = "cumFace"
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    pause 1.5

    show cumming_mc
    with dissolve

    $ p_ao_n_dick_num += 1
    call p_ao_n_changes

    $ p_prot.orgasm +=1

    ## Neus below you with cum on her face.
    with vpunch
    p "¡Uugh...!"

    scene black
    with fade

    n "explosionas en el rostro de [neusname], sin que esta haya tenido tiempo de meterse tu miembro en su boca."

    ## Neus below you with cum on her face.

    stop music fadeout 2.0

    scene p_ao_nABelowIllustration:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.7 ypos 0.5 #Her face
        easein_quad 10.0 zoom 0.4 xpos 0.5 ypos 0.5 ## Full IMage?
    with fade

    ne "Hmmm..."

    if music_play != "magic_forest":
        play music "audio/music/kevinmacleod/magic_forest.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "magic_forest"

    ne "Supongo que realmente tenías ganas de correrte..."

    pause

    # Neus sucking your dick from below.

    $ p_ao_action_b_Cond = "armAss"
    $ p_ao_action_Cond = "suckDown"
    show p_ao_cumInMouthAdult_comp_01:
        truecenter
        zoom 1.0 xpos 0.6 ypos 0.1
    with fade

    n "Usando sus manos en tu trasero como soporte alarga su cuello hasta engullir por completo tu miembro su garganta."

    $ p_ao_action_Cond = "suckUp"
    show p_ao_cumInMouthAdult_comp_01
    with Dissolve(1.0)

    pt "¡Joder!"

    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "sucking"
    show p_ao_cumInMouthAdult_comp_01:
        ease 15.0 zoom 0.5 xpos 0.5 ypos 0.4 # End image?
    with Dissolve(1.0)

    n "A pesar de que realmente no te queda mucho más que ofrecer,"

    $ p_ao_n_vel = 3
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    n "sus labios se anclan en la base de tu entrepierna."

    $ p_ao_n_vel = 4
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    n "Oyes el sonido de su faringe absorbiendo lo poco que te queda."

    $ p_ao_n_vel = 5
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    n "Su ardiente respiración acaricia tu piel a la altura de tu ombligo."

    $ p_ao_n_vel = 6
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    pt "¡¿Pero cuántas lenguas tiene?!"

    scene black
    show p_ao_nVagSex_sex_rest:
        truecenter
        zoom 1.5 xpos 0.3 ypos 1.8 rotate -50
        ease 15.0 zoom 1.0 xpos 0.7 ypos 0.0 rotate -60
    with fade

    n "Como si fueran decenas de lenguas lamiendo y recorriendo tu polla,"

    n "presionan con fuerza desde la base hasta la punta,"

    pause

    $ p_ao_n_vel = 12
    $ p_ao_action_Cond = "sucking"
    scene p_ao_cumInMouthAdult_comp_01:
        subpixel True
        truecenter
        zoom 0.4 xpos 0.5 ypos 0.4 # Whole Image
        ease_quad 15.0 zoom 1.0 xpos 0.6 ypos 0.1 # Her face.
    with fade

    n "pareciera que quisiera escarbar hasta la última gota escondida de tu moribundo miembro."

    $ p_ao_n_vel = 24
    $ p_ao_action_Cond = "sucking"
    show p_ao_cumInMouthAdult_comp_01
    with dissolve

    pause

    play sound "audio/sfx/fall02.ogg"
    scene black
    with vpunch
    with vpunch

    n "A pesar de que tus piernas desfallecen y caes rendido sobre su rostro,"

    n "empañando tu entrepierna del esperma que tiene en su cara,"

    n "[neusname] no cesa en su movimiento bucal."

    play sound "audio/sfx/fall01.ogg"

    ono "plof"

    n "Te aparta con sus manos -como si fueras un muñeco de trapo- y caes boca arriba sobre la cama."

    $ ped_neus_whispers_sfx04 = 0.7

    # She licks your body.
    scene gensex_oral_n_lick_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 
        ypos 0.25 # Her tongue Close
        easein_quad 20.0 zoom 0.6 ypos 0.3 # General View
    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    n "Igual que una perra hambrienta recorre tu entrepierna con su lengua,"

    n "relamiendo todo el esperma que se había desparramado al caer sobre su rostro."

    pt "Parece que ha recuperado su forma original..."

    n "A pesar del ardor de su lengua en tu pelvis,"

    stop music fadeout 2.0

    n "poco a poco vas cerrando los párpados."

    scene black
    with fade

    jump p_neus_orgasmReal_amazonic_label
        # ne "No-no-no-no..."
        # ne "Aún no hemos terminado,"
        # te agarra de la muñeca y te pone cara arriba sobre la cama.


    # NOT FINISHED Here should be also 2 cumshots.

    # Primero te agarra y te pone contra la pared y te folla de cara contra la pared mientras te muerde los pezones.

    # Luego se gira y te embiste con su trasero contra la pared metiéndose la polla en su agujero anal.

    # Finalmente te tira sobre la cama y levantándote una pierna te folla agarrándote de esa pierna levantada. (Aquí le empiezan a crecer los cuernos)

    # Caes rendido sobre la cama.


### NEW LABEL HERE.
label p_neus_orgasmReal_amazonic_label:

    pause

    $ ped_neus_whispers_sfx04 = 0.7
    $ p_ao_whispers_n = 0.4
    call p_ao_whispers_label

    if music_play != "coldFunk":
        play music "audio/music/kevinmacleod/happy/coldFunk.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "coldFunk"

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with vpunch

    ne "No-{w=0.4}{nw}"

    extend "no-{w=0.4}{nw}"

    extend "no-{w=0.4}{nw}"

    extend "no..."

    $ nteye = "front03"
    show n_closefromup_mouth sad_Talkingx06
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears

    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with dissolve

    ne "Aún no hemos terminado,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows angryx04
    call n_closefromup_tears_tears
    with dissolve

    if gensex_ILoveYouNeus:

        ne "mi amor."

    elif gensex_YoureAMonster:

        ne "perra."

    else:

        ne "mi querido Lancelot."

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows serious
    call n_closefromup_tears_tears
    with dissolve

    p "[neusname],"

    extend " no puedo más..."

    $ nteye = "front00"
    show n_closefromup_mouth happy_Talkingx11
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero yo sigo hambrienta,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows angryx06
    call n_closefromup_tears_tears
    with dissolve

    ne "muy hambrienta..."

    $ nteye = "down03"
    show n_closefromup_mouth happybiting_Silentx15
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    scene black
    with fade

    n "Vuelve agarrarte de una pierna y con un fuerte y veloz movimiento de muñeca"

    play sound "audio/sfx/fall01.ogg"

    ## your dick being soft in oral position.
    scene black
    with hpunch
    p "¡Ugh!"

    # scene black
    # with fade

    #show gensex_oral_n_frontHead_exp_blush 01
    $ p_neuspos = "gensex_oral_n_frontHead_exp_"
    $ ped_sex_general_expressionJaw_Cond = ""
    $ ped_sex_general_expression_Cond = "talk"
    $ ped_sex_general_action_Cond = ""
    $ ped_sex_blow_Cond = False
    call pedrera_sex_p_general_talk

    $ ped_sex_num = 1
    $ p_ao_n_vel = 1
    show pedrera_sex_neus_oral CloseTip:
        truecenter
        zoom 1.0
        ypos 0.55 # Up

    ##

    #$ ped_sex_general_expression_Cond = "talk"

    ##

    show gensex_oral_n_frontHead_exp_mouth empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over

    if ped_sex_general_expression_Cond == "talk":
        show gensex_oral_n_frontHead_exp_blush 01:
            p_ao_sex_oral_n_frontHead_CloseTip_Over
            
    show gensex_oral_n_frontHead_exp_eyes empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_iris empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_l_iris empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
        alpha 1.0
    show gensex_oral_n_frontHead_exp_tears empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_iLight empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
        additive 1.0
    # show gensex_oral_n_frontHead_exp_mouth_b empty:
    #     p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_eyebrows empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over

    if ped_sex_general_expression_Cond == "talk":
        show gensex_oral_n_frontHead_hair:
            p_ao_sex_oral_n_frontHead_CloseTip_Over
    else:
        show gensex_oral_n_frontHead_hair empty:
            p_ao_sex_oral_n_frontHead_CloseTip_Over

    show pedrera_sex_neus_oral_CloseTipOver:
        truecenter
        zoom 1.0
        ypos 0.55


# ##### ## TEST
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene pedrera_sex_neus_oral CloseTip:
#         truecenter
#         zoom 0.2
#     pause
# ####


    ## 

    $ nteye = "down03"
    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx03
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx01
    call gensex_oral_n_frontHead_exp_tears_tears
    with fade_long1s

    n "te pone de nuevo boca arriba."

    $ nteye = "front08"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx002
    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Uy-{w=0.6}{nw}"

    extend "uy-{w=0.6}{nw}"

    extend "uy..."

    $ nteye = "front03"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx08
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "¿Dónde está esa enorme,"

    extend " palpitante"

    extend " y hermosa polla?"

    $ nteye = "down04"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx04
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Vista así no parece tan grande,"

    $ nteye = "down02"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx05
    show gensex_oral_n_frontHead_exp_eyebrows sadx01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "más bien parece un gusano rojizo moribundo."

    $ nteye = "front07"
    show gensex_oral_n_frontHead_exp_mouth happy_Silentx12
    show gensex_oral_n_frontHead_exp_eyebrows sadx05
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    play sound "audio/characters/neus/giggle05.ogg"

    ne "*je,je,je...*" #Machiavelous giggle.

    $ nteye = "down05"
    show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx10
    show gensex_oral_n_frontHead_exp_eyebrows angryx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "[neusname]..."

    $ nteye = "down03"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx06
    show gensex_oral_n_frontHead_exp_eyebrows angryx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Habrá que reanimar esto."

    $ nteye = "down05"
    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx12
    show gensex_oral_n_frontHead_exp_eyebrows angryx06
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pause 0.2

    play sound "audio/sfx/hit02.ogg"

    scene p_ao_sex_amazon_front_comp_01:
        subpixel True
        truecenter
        #zoom 0.2
        zoom 2.0
        xpos 1.3 ypos -0.7 # Down his Ankle
        easein_quad 1.0 xpos 1.55 ypos 0.8 # His Lfoot
    with vpunch

    n "Levantando tus piernas al aire,"

    $ p_ao_action_Cond = "slappingBalls"
    $ p_ao_n_vel = 2 # Just Testing

    play sound "audio/sfx/slap01.ogg"

    scene p_ao_sex_amazon_side_comp_01:
        subpixel True
        truecenter
        #zoom 0.6
        #xpos 0.2 ypos 0.2
        zoom 2.0 xpos -0.2 ypos -0.5
        easein_quad 1.0 zoom 1.8 xpos 0.0 ypos -0.5
    show p_ao_sex_smack_effect
    with hpunch

    p "¡OUCH!"

    n "Padeces un fuerte abofeteo en tus testículos."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab
    $ ped_neus_whispers_sfx04 = 0.3

    show n_closefromup_body naked

    $ nteye = "down01"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "¡Ponte dura!"

    $ nteye = "down05"
    show n_closefromup_mouth sad_Silentx08
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    p "[neusname]..."

    play sound "audio/sfx/slap02.ogg"

    show p_ao_sex_amazon_side_comp_01:
        truecenter
        zoom 2.0 xpos -0.2 ypos -0.5
        easein_quad 1.0 zoom 1.8 xpos 0.0 ypos -0.5
    show p_ao_sex_smack_effect
    with hpunch

    ne "¡Que te pongas dura!"

    hide p_ao_sex_amazon_side_comp_01

    $ nteye = "down05"
    show n_closefromup_mouth sadbiting_Silentx02
    show n_closefromup_eyebrows suspiciousx04
    call n_closefromup_tears_tears
    with fade

    n "Sin apenas fuerzas."

    $ nteye = "front03"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    p "No-"

    extend "no creo que esta sea..."

    $ nteye = "front02"
    show n_closefromup_mouth happy_Silentx03
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    p "la mejor manera..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Lo sé,"

    $ nteye = "down01"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "pero tenía ganas de hacerlo."

    play sound "audio/characters/neus/giggle02.ogg"

    $ nteye = "front07"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # She getting closer to your bollocks with her warm breath.

    $ p_ao_action_Cond = "breathingBalls"
    $ p_ao_n_vel = 2 # Just Testing

    scene p_ao_sex_amazon_side_comp_01:
        subpixel True
        truecenter
        zoom 2.0 xpos 0.5 ypos -0.4 # Your dick
        ease 5.0 zoom 2.5 xpos -0.3 ypos -0.7 # Her face.
    with fade

    n "Percibes su abrasadora respiración cerca de tus maltratadas pelotas"

    $ p_ao_action_Cond = "bitingBalls"

    play sound "audio/characters/protagonist/auau_late01.ogg"

    scene p_ao_sex_amazon_side_comp_01:
        subpixel True
        truecenter
        zoom 2.5 xpos 0.0 ypos -0.5
        easein_elastic 1.0 zoom 3.0 xpos -0.5 ypos -0.9 # Bite Zone
    show p_ao_sex_smack_effect
    with hpunch
    p "¡AUCH!"

    scene black
    with fade

    n "dándoles un mordisco."

    p "¡¿Pero qué pretendes?!"

    p "¡¿{a=https://es.wikipedia.org/wiki/Castración}Castrarme{/a}?!"

    $ p_neuspos = "gensex_oral_n_frontHead_exp_"
    $ ped_sex_general_expressionJaw_Cond = ""
    $ ped_sex_general_expression_Cond = "talk"
    $ ped_sex_general_action_Cond = "o01_01"
    call pedrera_sex_p_general_talk

    $ ped_sex_num = 1
    $ p_ao_n_vel = 1
    show pedrera_sex_neus_oral CloseTip:
        truecenter
        zoom 1.0
        ypos 0.55 # Up

    ##

    $ ped_sex_general_expression_Cond = "talk"

    ##

    show gensex_oral_n_frontHead_exp_mouth empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over

    if ped_sex_general_expression_Cond == "talk":
        show gensex_oral_n_frontHead_exp_blush 01:
            p_ao_sex_oral_n_frontHead_CloseTip_Over
            
    show gensex_oral_n_frontHead_exp_eyes empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_iris empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_l_iris empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
        alpha 1.0
    show gensex_oral_n_frontHead_exp_tears empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_iLight empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over
        additive 1.0
    # show gensex_oral_n_frontHead_exp_mouth_b empty:
    #     p_ao_sex_oral_n_frontHead_CloseTip_Over
    show gensex_oral_n_frontHead_exp_eyebrows empty:
        p_ao_sex_oral_n_frontHead_CloseTip_Over

    if ped_sex_general_expression_Cond == "talk":
        show gensex_oral_n_frontHead_hair:
            p_ao_sex_oral_n_frontHead_CloseTip_Over
    else:
        show gensex_oral_n_frontHead_hair empty:
            p_ao_sex_oral_n_frontHead_CloseTip_Over

    show pedrera_sex_neus_oral_CloseTipOver:
        truecenter
        zoom 1.0
        ypos 0.55

    ## 

    $ nteye = "front05"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx005
    show gensex_oral_n_frontHead_exp_eyebrows surprisex02
    call gensex_oral_n_frontHead_exp_tears_tears
    with fade

    ne "Es lo último que desearía,"

    $ nteye = "front01"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx07
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "pero estoy empezando a pensar que te pone más el dolor que el placer."

    if p_neus_dickG_wants:

        $ nteye = "down01"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx007
        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "No-"

        extend "no veo que se esté poniendo dura."

    else:

        $ nteye = "down01"
        show gensex_oral_n_frontHead_exp_mouth sad_Talkingx009
        show gensex_oral_n_frontHead_exp_eyebrows angryx03
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "¡No veo que se esté poniendo dura!"

    $ nteye = "down05"
    show gensex_oral_n_frontHead_exp_mouth sad_Silentx06
    show gensex_oral_n_frontHead_exp_eyebrows suspiciousx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Hmmm..."

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx08
    show gensex_oral_n_frontHead_exp_eyebrows sadx01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Realmente la tienes muy rojiza;"

    $ nteye = "front07"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx10
    show gensex_oral_n_frontHead_exp_eyebrows sadx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "probablemente debe dolerte bastante."

    $ nteye = "front06"
    show gensex_oral_n_frontHead_exp_mouth happy_Silentx08
    show gensex_oral_n_frontHead_exp_eyebrows sadx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pt "Probablemente dice..."

    $ nteye = "front03"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx09
    show gensex_oral_n_frontHead_exp_eyebrows angryx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Pero te garantizo que no he conocido humano capaz de resistir el arte de mi lengua,"

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx10
    show gensex_oral_n_frontHead_exp_eyebrows angryx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "ni siquiera cuando están tan agotados y vacíos"

    $ nteye = "front00"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx13
    show gensex_oral_n_frontHead_exp_eyebrows angryx03
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "que están a las puertas de la muerte."

    $ nteye = "front01"
    show gensex_oral_n_frontHead_exp_mouth sad_Silentx03
    show gensex_oral_n_frontHead_exp_eyebrows surprisex002
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    p "¡¿Es que quieres matarme?!"

    $ nteye = "front04"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx07
    show gensex_oral_n_frontHead_exp_eyebrows angryx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "No seas tonto."

    $ nteye = "front08"
    show gensex_oral_n_frontHead_exp_mouth sad_Talkingx007
    show gensex_oral_n_frontHead_exp_eyebrows surprisex01
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Eres mi hermano."

    $ nteye = "right01"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx09
    show gensex_oral_n_frontHead_exp_eyebrows angryx04
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "La sangre que corre por tus venas está hecha de..."

    $ nteye = "right04"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx13
    show gensex_oral_n_frontHead_exp_eyebrows angryx05
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "otra pasta,"

    extend " podríamos decir."

    $ nteye = "front07"
    show gensex_oral_n_frontHead_exp_mouth happy_Talkingx11
    show gensex_oral_n_frontHead_exp_eyebrows sadx02
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    ne "Estoy convencida de que sobrevivirás."

    if night04_pedrera_blowjob_DONE:

        $ nteye = "front04"
        show gensex_oral_n_frontHead_exp_mouth happy_Talkingx09
        show gensex_oral_n_frontHead_exp_eyebrows suspiciousx02
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        ne "Al fin y al cabo sobreviviste a mi mamada de ayer,"

        $ nteye = "front05"
        show gensex_oral_n_frontHead_exp_mouth happy_Talkingx10
        show gensex_oral_n_frontHead_exp_eyebrows angryx02
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        ne "¿no es así?"

        $ nteye = "front01"
        show gensex_oral_n_frontHead_exp_mouth sadbiting_Silentx05
        show gensex_oral_n_frontHead_exp_eyebrows surprisex01
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        p "¡Ayer no me corrí tantas veces!"

        $ nteye = "front07"
        show gensex_oral_n_frontHead_exp_mouth happy_Talkingx11
        show gensex_oral_n_frontHead_exp_eyebrows sadx04
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        ne "No mientras estabas consciente,"

        extend " al menos..."

        $ nteye = "down04"
        show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx10
        show gensex_oral_n_frontHead_exp_eyebrows sadx05
        call gensex_oral_n_frontHead_exp_tears_tears
        with dissolve

        pt "¡¿Cómo?!"

    $ nteye = "down05"
    show gensex_oral_n_frontHead_exp_mouth happybiting_Silentx12
    show gensex_oral_n_frontHead_exp_eyebrows sadx06
    call gensex_oral_n_frontHead_exp_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_action_Cond = "lickDick_01" # Soft
    $ nblushNumber = "06"
    $ ped_sex_general_expression_Cond = "lustToYou"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_02"
    $ ped_sex_blow_Cond = False
    $ p_ao_n_vel = 2

    ## REMEMBER!! IT¡S STILL SMALLLLLLHLÑSHEIRLÑESHRILESÑHRESI!!!!!!

    if music_play != "funkorama":
        play music "audio/music/kevinmacleod/happy/funkorama.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "funkorama"

    ## Tongue around your semihard Cock. Alt001
    scene pedrera_sex_neus_oral tongue:
        subpixel True
        truecenter
        zoom 2.0 ypos 0.6 # Up #Close Camera to the dick sorrounded (Neus eyes?)
        block:
            ease 10.0/p_ao_n_vel zoom 2.0 ypos 0.28 #Down
            ease 10.0/p_ao_n_vel zoom 2.0 ypos 0.6 # Up #Close Camera to the dick sorrounded (Neus eyes?)
            repeat
    with fade

    n "Sientes su longeva lengua rodeando tu flácida y dolorida polla,"

    $ p_ao_ground = "bed" # Delete this one because it should be implemented before...

    show p_ao_mc_ass_comp 01:
        truecenter
        #zoom 0.2
        #zoom 1.0 xpos 1.5 ypos -0.5 # Left South Corner
        zoom 1.0 xpos 0.0 ypos 1.5 # Right North Corner?
        easein_quad 5.0 zoom 0.5 xpos 0.5 ypos 0.5 # Asshole Centered?
    with fade

    n "al mismo tiempo que sus dedos acarician tu rojizo y afligido ano."

    p "Ughh..."

    hide p_ao_mc_ass_comp 01
    with fade

    if p_prot_aoNight_analReceived in ["False", ""]:

        if p_prot_aoNight_analReceived == "False":

            p "¡¿Por qué vuelves a magrearme el culo?!"

            ne "Te he dicho que no metería mi polla,"

            ne "pero no he dicho nada de mis dedos."

        else:

            p "¡¿Qué pretendes magreándome el culo así?!"

            ne "No seas tan puritano."

    ne "¿Acaso quieres dejarme con hambre [protname]?"

    progcheck "[protname] lleva [p_prot.orgasm] corridas."

    if p_prot.orgasm == 4: # - 2.

        p "¡Pero si ya te has tragado dos corridas!"
    elif p_prot.orgasm == 5:

        p "¡Peros si ya te has tragado tres corridas!"

    else:

        p "¡Pero si ya te has tragado un montón de corridas!"

    ne "Pero quiero más..."

    $ ped_sex_general_expressionJaw_Cond = "blow_below_04"
    $ p_ao_action_Cond = "lickDick_02" # Medium
    show pedrera_sex_neus_oral tongue:
        easein_quad 20.0/p_ao_n_vel zoom 1.5 ypos 0.9 #Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.35 #Down
            ease 10.0/p_ao_n_vel ypos 0.9 #Up
            repeat
    with Dissolve(10.0/p_ao_n_vel)

    p "Te recuerdo,"

    extend " que según has dicho,"

    p "cuando salga el sol tenemos que huir."

    p "¡A este paso no podré ni andar!"

    ne "No te preocupes por eso,"

    ne "si hace falta ya te llevaremos dentro de una caja."

    ne "Ahora lo importante es que me des de comer."

    pt "¡¿En una caja?!"

    if p_prot_aoNight_analReceived == "True":

        ne "¿Prefieres mi lengua o mi polla para estimularte ahí detrás?"

        menu:

            pt "¿Lengua o polla?"

            "Prefiero tu polla." if p_neus_dickG_wants:
                call p_Help

                $ p_neus_dickG02_wants = "dick"

                pt "¡¿Es que me he vuelto loco?!"

                pt "¡Tengo el culo hecho mierda!"

                pt "¡¿Y desde cuando me gusta que me den por detrás?!"

                p "No creo que mi culo pueda aguantar otra de tus embestidas..."

                ne "Es verdad que lo tienes bastante dolorido..."

            "Prefiero tu lengua.":
                call p_Help

                $ p_neus_dickG02_wants = "tongue"

                ne "Me alegra saber que disfrutas tanto de mi lengua."

                n "La percibes por la parte superficial de tu tierna carne, húmeda y ardiente"

                n "relamiendo toda esa parte de modo juguetón."

                n "Te penetra con ella lentamente mientras la retuerce dando vueltas justo en la entrada,"

                n "para finalmente sentir como vuelve a sacarla."

                ne "Pero creo que esta vez te estimularé de otro modo."

                pt "¡¿Cómo dice?!"

            "¡Ni una cosa ni la otra!":
                call p_Help

                ne "Hmmm..."

                ne "Es verdad que lo tienes bastante dolorido..."

        $ p_ao_n_tail_num = 1
        #$ p_ao_n_tail = "01"
        $ p_ao_action_Cond = "teasing_feet_01"
        scene p_ao_sex_amazon_front_comp_02:
            subpixel True
            truecenter
            ypos -0.4 # Your head
            easein_quad 8.0 ypos 0.3
        with fade

        pause 1.5

        $ p_ao_action_Cond = "teasing_feet_02"
        show p_ao_sex_amazon_front_comp_02
        with Dissolve(1.0)

        pause 1.5

        $ p_ao_action_Cond = "teasing_feet_03"
        show p_ao_sex_amazon_front_comp_02
        with Dissolve(1.0)

        n "Sus pies abandonan el suelo para posarse sobre la cama al lado de tus nalgas a modo de cuclillas."

        window hide dissolve
        pause

    if p_neus_dickG02_wants == "":

        $ p_ao_n_vel = 5
        $ p_ao_mc_dick_num = 5
        $ ped_sex_general_expressionJaw_Cond = "blow_below_05_happy"
        $ p_ao_action_Cond = "lickDick_02" # Medium
        scene pedrera_sex_neus_oral tongue:
            subpixel True
            truecenter
            zoom 1.5 ypos 0.9 #Up
            block:
                ease 10.0/p_ao_n_vel ypos 0.35 #Down
                ease 10.0/p_ao_n_vel ypos 0.9 #Up
                repeat
        with Dissolve(10.0/p_ao_n_vel)

    else:

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab
        #$ ped_neus_whispers_sfx04 = 0.3

        show n_closefromup_body naked

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx07
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with fade_short

        pause 0.2

        $ nteye = "front05"
        show n_closefromup_mouth happy_Silentx07
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ nteye = "front07"
        show n_closefromup_mouth happy_Silentx10
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

    n "Al fijarte en su rostro observas que te dedica una sonrisa de niña traviesa."

    if not p_neus_dickG02_wants == "":
        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx09
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

    if p_prot_aoNight_analReceived == "True":

        $ p_ao_n_vel = 2

        $ p_ao_ground = "bed"
        $ p_ao_action_Cond = "tail_01"
        scene p_ao_mc_ass_comp 04:
            subpixel True
            truecenter
            ## xpos 0.0=Right    xpos 1.0=Left
            ## ypos 0.0=Down    ypos 1.0=Up
            zoom 0.8 xpos -0.3 ypos 1.2 # UpRight
            ease 10.0 zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
        with fade

# ########  TEST
#         $ p_ao_action_Cond = "tail_01"
#         show p_ao_mc_ass_comp 04:
#             #zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
#             zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
#             block:
#                 ease 4.0/p_ao_n_vel zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
#                 ease 4.0/p_ao_n_vel zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
#                 repeat
#         progcheck "01"
#         $ p_ao_action_Cond = "tail_02"
#         show p_ao_mc_ass_comp 04:
#             #zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
#             zoom 0.9 xpos 0.4 ypos 0.6 # UpRight
#             block:
#                 easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
#                 easeout_quad 4.0/p_ao_n_vel zoom 0.9 xpos 0.4 ypos 0.6 # UpRight
#                 repeat
#         progcheck "02"
#         $ p_ao_action_Cond = "tail_03"
#         show p_ao_mc_ass_comp 04:
#             #zoom 1.0 xpos 0.55 ypos 0.6 # Close Ass
#             zoom 0.8 xpos 0.3 ypos 0.65 #UpRight
#             block:
#                 easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.55 ypos 0.6 # Close Ass
#                 easeout_quad 4.0/p_ao_n_vel zoom 0.8 xpos 0.3 ypos 0.65 #UpRight
#                 repeat
#         progcheck "03"
#         $ p_ao_action_Cond = "tail_04"
#         show p_ao_mc_ass_comp 04:
#             #zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
#             zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
#             block:
#                 easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
#                 easeout_quad 4.0/p_ao_n_vel zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
#                 repeat
#         progcheck "04"
#         $ p_ao_action_Cond = "tail_05"
#         show p_ao_mc_ass_comp 04:
#             #zoom 1.0 xpos 0.7 ypos 0.6 # Close Ass
#             zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
#             block:
#                 easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.7 ypos 0.6 # Close Ass
#                 easeout_quad 4.0/p_ao_n_vel zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
#                 repeat
#         progcheck "05"
#         $ p_ao_action_Cond = "tail_06"
#         show p_ao_mc_ass_comp 04:
#             zoom 0.6 xpos 0.05 ypos 0.8 # TopRight
#             block:
#                 easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.8 ypos 0.6 # Close Ass
#                 easeout_quad 4.0/p_ao_n_vel zoom 0.6 xpos 0.05 ypos 0.8 # TopRight
#                 repeat
#             #zoom 1.0 xpos 0.65 ypos 0.6 # Close Ass
#         progcheck "06"
# ########

        n "Algo húmedo y terso está acariciando de nuevo la superficie de tu agujero anal."

        p "¿Qué-"

        extend "qué estás haciendo?"

        ne "Quizás es hora de que pruebes otra parte de mi."

        p "¡¿Qué coño es eso?!"

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with fade_short

        ne "Tú tienes una cola delante,"

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx12
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "y yo tengo una detrás."

        $ nteye = "right03"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Bueno,"

        extend " en realidad también puedo tenerla delante."

        play sound "audio/characters/neus/giggle05.ogg"

        $ nteye = "front06"
        show n_closefromup_mouth happy_Silentx10
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "*je-je-je...*" # michavelous apparently innocent giggle.

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx08
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

        $ p_ao_n_vel = 1
        $ p_ao_action_Cond = "tail_01"
        scene p_ao_mc_ass_comp 04:
            subpixel True
            truecenter
            zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
            block:
                ease 4.0/p_ao_n_vel zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
                ease 4.0/p_ao_n_vel zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
                repeat
        with fade

        n "Esa punta húmeda, gruesa, y dura,"

        $ p_ao_n_vel = 2
        $ p_ao_action_Cond = "tail_02"
        show p_ao_mc_ass_comp 04:
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.9 xpos 0.4 ypos 0.6 # UpRight
                repeat
        with Dissolve(0.5)

        n "empieza abrirse paso en tu interior."

        $ p_ao_n_vel = 3
        $ p_ao_action_Cond = "tail_03"
        show p_ao_mc_ass_comp 04:
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.55 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.8 xpos 0.3 ypos 0.65 #UpRight
                repeat
        with hpunch

        pt "¡Joder!"

        if p_neus_dickG_wants:

            p "Pe-"

            extend "pero si es más gruesa que tu polla..."

        else:

            p "¡Pero si es más gruesa que tu polla!"

        ne "Y además mucho más larga..."

        ne "Pero así tengo vía libre para poder hacer esto..."

    else:

        $ p_ao_n_vel = 2
        $ p_ao_mc_dick_num = 4
        $ p_ao_action_Cond = "teasing_feet_03_04"

        scene p_ao_sex_amazon_front_comp_02:
            subpixel True
            truecenter
            #zoom 0.2
            zoom 2.0 xpos 1.2 ypos -0.8 # Left Ankle
            easein_quad 3.0 zoom 2.0 xpos 1.4 ypos 0.8 # Left Leg
        with vpunch

        n "Sientes que se aparta y se pone de pie elevando tus piernas dejando tu erecta polla en el aire."

    # TEASING
    $ p_ao_n_vel = 2
    $ p_ao_action_Cond = "teasing_feet_02_04"

    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        #zoom 0.2  #zoom 1.0 ypos 0.25 # ONe view.
        zoom 4.0 ypos -1.2 # Base Dick.
        ease 5.0 zoom 2.0 ypos -0.15 # Whole Dick.
    with fade

# ####
#     pause
#     $ ped_neus_whispers_sfx04 = 1.0
#     scene p_ao_sex_amazon_front_comp_02:
#         truecenter
#         zoom 0.2
#     pause
# ###

    n "Sufres sus ardientes labios vaginales a lo largo y ancho de tu -bastante dolorido- miembro."

    pause

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    if p_prot_aoNight_analReceived == "True":

        $ nteye = "down04"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with fade_short

        ne "Me ha encantado follarte con mi polla;"

        $ nteye = "down05"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "pero,"

        $ nteye = "front07"
        show n_closefromup_mouth happy_Talkingx10
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "no hay comparación."

        $ nteye = "down03"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows sadx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Sentirla al contacto con mi entrepierna es mucho más..."

        $ nteye = "front08"
        show n_closefromup_mouth happybiting_Silentx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

    else:

        $ nteye = "front08"
        show n_closefromup_mouth happybiting_Silentx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with fade_short

    ne "Hmfhmm..." # Pleasure moan while biting lips. (like hungry)

    if p_prot_aoNight_analReceived == "True":

        $ p_ao_n_vel = 3
        $ p_ao_action_Cond = "tail_03"
        show p_ao_mc_ass_comp 04:
            truecenter
            zoom 0.8 xpos 0.3 ypos 0.65 #UpRight
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.55 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.8 xpos 0.3 ypos 0.65 #UpRight
                repeat
        with fade

        pause 0.2

        $ p_ao_n_vel = 1
        $ p_ao_action_Cond = "tail_04"
        show p_ao_mc_ass_comp 04:
            zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
                repeat
        with Dissolve(1.0)

        n "Padeces la punta de su cola abriéndose camino en tu interior"

        $ p_ao_n_vel = 3
        show p_ao_mc_ass_comp 04:
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
                repeat
        with dissolve

        n "al mismo tiempo que se remueve dando vueltas lentamente."

        $ p_ao_n_vel = 6
        show p_ao_mc_ass_comp 04:
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
                repeat
        with dissolve

        p "Joder..."

        hide p_ao_mc_ass_comp

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    ne "Dios..."

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Quiero que vuelvas a correrte dentro de mi,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    if gensex_ILoveYouNeus:

        ne "mi amor."

    elif gensex_YoureAMonster:

        ne "mi perrita."

    else:

        ne "mi apuesto caballero."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "quiero sentirla toda dentro de mi."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx07
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    pt "¡Pero si la tengo que me la tendría mirar un médico!"

    #Her wings start to grow, 

    $ p_ao_n_tail = ""
    $ p_ao_n_tail_num = 0
    $ p_ao_n_wings = "05"
    $ p_ao_n_wings_num = 5
    $ p_ao_n_vel = 5
    #$ p_ao_action_Cond = "teasing_02_04"
    $ p_ao_mc_dick_num = 3
    $ p_ao_n_horns_num += 1
    $ p_ao_n_fur_num += 1
    $ p_ao_n_fur = "_fur"
    call p_ao_n_changes

    $ p_ao_action_Cond = "teasing_feet_02" ## TESTING
    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        #zoom 0.5
        #zoom 1.0 ypos 0.0 # Down Zoom
        #zoom 0.32 ypos 0.7 # Wings Whole Visible
        zoom 2.0 xpos 1.55 ypos 0.8 # His Lfoot
        easein_quad 15.0 zoom 0.6 xpos 1.04 ypos 1.2  #Her Right Wing Visible
        #ease 15.0 zoom 0.32 xpos 0.5 ypos 0.7 # Wings Whole Visible
    with fade


    n "Hay algo que te hace sombra."

    p "¿Qué...?"

    n "Dos enormes, delgadas y venosas alas -carentes de pelo- se agitan en la espalda de Neus"

    n "cubriendo la poca luz que radia en la habitación a través de la espesa neblina."

    # Her furred legs.

    window hide dissolve
    pause

    ## NOT FINISHED - NEXT UPDATE.
    # scene black
    # with fade_short

    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        #zoom 2.5 xpos 0.5 ypos -0.5 # Your head?
        zoom 2.0 xpos 1.2 ypos -0.8 # Left Ankle
        ease 5.0 zoom 2.0 xpos 0.9 ypos 0.1 # Her Furred Right Leg

        #zoom 0.5 ypos 0.4 # Positioning the damn Dick.
    with fade_short

    n "Palpas entre las piernas que acarician las tuyas, una especie de tupido pelo,"

    show p_ao_sex_amazon_front_comp_02:
        ease 10.0 zoom 1.25 xpos 0.5 ypos 1.3 # her face and horns.

    n "al mismo tiempo que esos dos cuernos que estaban en su cráneo"

    n "son ahora mucho más longevos y ostentosos."

    show p_ao_sex_amazon_front_comp_02:
        #zoom 1.0 xpos 0.5 ypos 0.5 # Whole body
        easein_quad 10.0 zoom 0.32 xpos 0.5 ypos 0.7 # Wings Whole Visible

    p "¡¿Qué diablos...?!"

    window hide dissolve
    pause

    #$ ped_neus_whispers_sfx04 = 0.2 # TESTING

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front04"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with fade_short

    ne "Tengo ganas de follarte [protname],"

    $ ped_neus_whispers_sfx04 = 0.2

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "follarte tan duro,"

    $ nteye = "front01"
    show n_closefromup_mouth happy_Talkingx15
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    ne "que en tus pelotas solo quede el vacío."

    $ nteye = "down00"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pt "Me va a matar..."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx13
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ nteye = "front03"
    $ ped_sex_general_expression_Cond = "sharp_closed_angryx02"

    ## Neus Sharp Teeth.

    if music_play != "darkestChild":
        play music "audio/music/kevinmacleod/creepy/darkestChild.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "darkestChild"

    #scene bg dark_a
    scene bg_ped_04
    show n_closefromup_p_ao_01:
        subpixel True
        truecenter
        zoom 2.0
        xpos 0.5
        ypos -2.3 # Down
        easein_quad 10.0 ypos 0.2 # Centering Her mouth?
    
    with fade

    n "Observas unos extraños brillos cuando separa sus labios"

    n "unos afilados y largos dientes se vislumbran en su escalofriante y tenebrosa sonrisa,"

    window hide dissolve
    pause

    # NOT FINISHED, wHAT Do I do here?

    scene black
    with fade

    if p_prot_aoNight_analReceived == "True":

        $ p_ao_n_vel = 8
        $ p_ao_action_Cond = "tail_04"
        show p_ao_mc_ass_comp 04:
            subpixel True
            truecenter
            zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.6 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.7 xpos 0.2 ypos 0.7 #UpRight
                repeat
        with fade_short

        pause 0.3

        $ p_ao_n_vel = 2
        $ p_ao_action_Cond = "tail_05"
        show p_ao_mc_ass_comp 04:
            zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.7 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
                repeat
        with Dissolve(1.0)

        n "su cola -completamente húmeda- empieza a balancearse dentro y fuera de tu cavidad anal"

        $ p_ao_n_vel = 8
        show p_ao_mc_ass_comp 04:
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.7 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
                repeat
        with Dissolve(0.5)

        n "impidiéndote poder articular más de dos sílabas seguidas."

    if p_prot_aoNight_analReceived == "True":
        $ p_ao_mc_dick_num = 3
    else:
        $ p_ao_mc_dick_num = 2
    $ p_ao_action_tongue_Cond = "02"
    $ p_ao_action_Cond = "teasing_feet_02" ## TESTING
    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        zoom 4.0 xpos 0.5 ypos 2.2 # Close to Mouth, without Eyes.
        ease 5.0 zoom 0.75 xpos 0.5 ypos 0.4 # WholeTongue02
         
    with fade

    #########################################################

    if config.version < "00.16.09": # NeusAfterHerOrgasm: SharpTeeth
        call endupdatescript
    
    #######################################################

    n "Su hirviente entrepierna y su longeva -aunque no menos abrasadora- lengua"

# ### TEST
#     $ p_ao_mc_dick_num = 6
#     $ p_ao_action_tongue_Cond = "02"
#     $ p_ao_action_Cond = "teasing_feet_02" ## TESTING
#     scene p_ao_sex_amazon_front_comp_02:
#         truecenter
#         zoom 0.75 xpos 0.5 ypos 0.4 # WholeTongue02
#     progcheck "06"
#     $ p_ao_mc_dick_num = 5
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "05"
#     $ p_ao_mc_dick_num = 4
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "04"
#     $ p_ao_mc_dick_num = 3
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "03"
#     $ p_ao_mc_dick_num = 2
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "02"
#     $ p_ao_mc_dick_num = 1
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "01"
#     $ p_ao_mc_dick_num = 0
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "00"
# ####

    if p_prot_aoNight_analReceived == "True":

        n "empiezan a jugar con tu -ya no tan flácido- rojizo y dolorido miembro viril."

    else:

        n "empiezan a jugar con tu completamente flácido, rojizo y dolorido gusanillo."

    pause

    scene bg_ped_04
    show kiss_ n_n_04:
        truecenter
        xzoom -1.0
        rotate -60
        zoom 1.2
    with fade

    n "Recibes el caluroso vaho a escasos centímetros de tu rostro"

    show kiss_ n_n_05:
        truecenter
        xzoom -1.0
        rotate -60
        zoom 1.2
    with Dissolve(0.5)

    n "y abandonando tu afligida polla por unos segundos,"

    #scene bg dark_a
    show kiss_ f_n_01:
        truecenter
        xzoom -1.0
        rotate -60
        zoom 1.2
    with Dissolve(0.5)

    pause 0.2

    show kiss_ f_n_12
    with Dissolve(0.5)

    pause 0.2

    show kiss_ f_n_11
    with Dissolve(0.5)

    n "te da un beso profundo con esa ardiente lengua."

    $ Pedrera_char_Cond = "NeusSuperSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows suspiciousx03
    call n_closefromup_tears_tears
    with fade_short

    ne "¿Te gusta el sabor de tu polla en mi lengua?"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx06
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    pt "¿Ahora me lo pregunta?"

    scene black
    with fade

    if gensex_YoureAMonster and pl.np < 150:

        $ p_ao_neusLastSecret = True

        n "Ves que se te arrima a la mejilla, pero no para besarte."

        n "Sus labios se acercan a la base de tu oreja,"

        n "mientras te susurra..."

        #scene bg dark_a
        scene bg_ped_04
        with fade_short

        ne "Tenías razón."

        ne "Llevo años negando la verdad,"

        ne "pero me has hecho abrir los ojos."

        ne "soy un monstruo,"

        extend " siempre lo he sido."

        ne "No soy tan distinto a Padre..."

        p "..."

        menu:

            pt "¡¿Ahora me dice esto?!"

            "Eres un monstruo, pero tampoco lo eres tanto como él.":
                call p_Help

            "Desde luego que lo eres.":
                call p_Help

            "...":
                call p_Help

        $ Pedrera_char_Cond = "NeusSuperSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with fade

        ne "¿Quieres que te cuente un último secreto?"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx12
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with dissolve

        ne "¿Quieres saber cómo sacrifiqué a ese niño?"

        $ nteye = "front03"
        show n_closefromup_mouth extra_sharp_closed
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        p "¿Cómo lo mataste...?"

        $ Pedrera_char_Cond = "NeusNotSuper"
        call Pedrera_char_lab

        show n_closefromup_body naked_FULL

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with Dissolve(0.5)

        ne "Bueno..."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows surprisex03
        call n_closefromup_tears_tears
        with dissolve

        ne "La verdad es que no lo maté."

        $ nteye = "right04"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Al menos,"

        $ nteye = "right03"
        show n_closefromup_mouth happy_Talkingx12
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "no en ese instante."

        $ nteye = "front05"
        show n_closefromup_mouth extra_sharp_closed
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2


        show black
        with fade

        n "Su ardiente mano agarra la tuya para llevársela a su barriga."

        ne "Quizás aún puedas sentirlo..."

        p "¡¿El qué?!"

        ne "Aunque a estas alturas es bastante difícil..."

        p "..."

        hide black
        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with fade

        ne "¿Por qué crees que me ausenté de venir a clase durante tres días?"

        $ nteye = "right01"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "Está claro que no lo hice por miedo a Dídac."

        $ nteye = "right05"
        show n_closefromup_mouth happy_Talkingx07
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "No..."

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo hice porque tenía la barriga tan llena"

        $ nteye = "front05"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "que hubiera parecido que estuviera embarazada."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows surprisex04
        call n_closefromup_tears_tears
        with dissolve

        ne "Además,"

        extend " tardó casi el mismo tiempo en dejar de darme patadas."

        $ nteye = "front07"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Te hubiera dado una mala impresión viéndome así,"

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "¿no crees?"

        $ nteye = "front04"
        show n_closefromup_mouth sadbiting_Silentx03
        show n_closefromup_eyebrows suspiciousx01
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Te-"

        extend "te lo comiste vivo?!"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows surprisex05
        call n_closefromup_tears_tears
        with dissolve

        ne "Más bien me lo tragué."

        $ nteye = "front01"
        show n_closefromup_mouth sad_Silentx04
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        p "¡Pensaba que solo con el sexo y el sacrificio conseguías el poder!"

        $ nteye = "right05"
        show n_closefromup_mouth sadbiting_Silentx07
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        p "¡¿Qué necesidad había de comértelo vivo?!"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "El pesar,"

        extend " la agonía,"

        extend " el dolor,"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx09
        show n_closefromup_eyebrows sadx01
        call n_closefromup_tears_tears
        with dissolve

        ne "es lo que alimenta estas criaturas."

        $ nteye = "right03"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "cuanto más cantidad haya mejor funciona,"

        $ nteye = "left02"
        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "pero también funciona en menor cantidad si la intensidad es mayor."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx005
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Y te garantizo que ser digerido durante tres días,"

        $ nteye = "right05"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows suspiciousx04
        call n_closefromup_tears_tears
        with dissolve

        ne "bueno,"

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "en realidad dos y medio..."

        $ nteye = "front07"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "al final del tercer día ya casi ni se movía;"

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "no es algo que sea precisamente placentero."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx04
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with Dissolve(1.0)

        ne "Especialmente cuando eres un niño que te limitas a gritar y a llamar a tus padres"

        $ nteye = "front01"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows suspiciousx04
        call n_closefromup_tears_tears
        with dissolve

        ne "entre sollozos y gritos de desesperación"

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        ne "sin entender lo que te está pasando."

        $ nteye = "front05"
        show n_closefromup_mouth happybiting_Silentx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        p "..."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx04
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "Sentir por última vez el placer de escuchar a un niño suplicar por su vida..."

        $ nteye = "front07"
        show n_closefromup_mouth happybiting_Silentx13
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "Hmmm..."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows suspiciousx02
        call n_closefromup_tears_tears
        with dissolve

        ne "Es verdad que Madre me convenció para hacerlo"

        $ nteye = "right01"
        show n_closefromup_mouth sad_Talkingx06
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears
        with dissolve

        ne "como también me advirtió encarecidamente que no te contara nada sobre ello."

        $ nteye = "right03"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Según sus palabras:"

        $ nteye = "right04"
        show n_closefromup_mouth sad_Talkingx05
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "{i}Él no conoce a Padre,{/i}"

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx003
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "{i}no sabe de lo que es capaz{/i}"

        $ nteye = "left04"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "{i}no como nosotras{/i}."

        $ nteye = "front08"
        show n_closefromup_mouth sad_Talkingx07
        show n_closefromup_eyebrows sadx07
        call n_closefromup_tears_tears
        with dissolve

        ne "Me he querido convencer a mi misma que fue ella quien me manipuló para hacer esta monstruosidad."

        $ nteye = "right02"
        show n_closefromup_mouth sad_Talkingx08
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Al fin y al cabo es verdad que cualquier reserva de energía es útil para combatir a Padre,"

        $ nteye = "right05"
        show n_closefromup_mouth sad_Talkingx03
        show n_closefromup_eyebrows sadx06
        call n_closefromup_tears_tears
        with dissolve

        ne "pero..."

        $ nteye = "front08"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Me has hecho ver la verdad,"

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "no lo hice porque Madre me manipulara,"

        $ nteye = "left05"
        show n_closefromup_mouth happy_Talkingx08
        show n_closefromup_eyebrows angryx03
        call n_closefromup_tears_tears
        with dissolve

        ne "ni siquiera para protegernos de Padre."

        $ nteye = "front00"
        show n_closefromup_mouth happy_Talkingx13
        show n_closefromup_eyebrows angryx05
        call n_closefromup_tears_tears
        with dissolve

        ne "Lo hice porque realmente lo deseaba,"

        $ nteye = "front07"
        show n_closefromup_mouth happy_Talkingx11
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "porque echaba de menos esta sensación de regocijo y placer,"

        $ nteye = "front03"
        show n_closefromup_mouth happy_Talkingx14
        show n_closefromup_eyebrows angryx04
        call n_closefromup_tears_tears
        with dissolve

        ne "porque es lo que soy,"

        $ nteye = "front01"
        show n_closefromup_mouth extra_sharp_open
        show n_closefromup_eyebrows angryx05
        call n_closefromup_tears_tears
        with dissolve

        ne "un monstruo."

        $ nteye = "front00"
        show n_closefromup_mouth sad_Silentx02
        show n_closefromup_eyebrows surprisex01
        call n_closefromup_tears_tears
        with dissolve

        p "Pe-"

        extend "pero tu boca no es tan grande..."

        $ nteye = "front05"
        show n_closefromup_mouth sad_Talkingx004
        show n_closefromup_eyebrows suspiciousx06
        call n_closefromup_tears_tears
        with dissolve

        ne "Sabes que soy capaz de aumentar el tamaño de mi cuerpo."

        $ nteye = "front03"
        show n_closefromup_mouth sad_Silentx03
        show n_closefromup_eyebrows suspiciousx03
        call n_closefromup_tears_tears
        with dissolve

        p "Sí,"

        extend " pero me dijiste que no durante mucho tiempo."

        $ nteye = "front04"
        show n_closefromup_mouth happy_Talkingx06
        show n_closefromup_eyebrows suspiciousx04
        call n_closefromup_tears_tears
        with dissolve

        ne "¿De verdad quieres verlo?"

        $ nteye = "front05"
        show n_closefromup_mouth extra_sharp_closed
        show n_closefromup_eyebrows angryx05
        call n_closefromup_tears_tears
        with Dissolve(0.5)

        pause 0.2

        # IMAGE

        show p_ao_nMouth_creepy_comp:
            truecenter
            zoom 2.0 xpos 0.5 ypos 0.5 # Inside Mouth
            ease 7.0 zoom 0.45 xpos 0.5 ypos 0.43 # Final Image
            #zoom 0.3 xpos 0.5 ypos 0.5 # Whole Image.
        with fade_long1s

        p "¡COÑO!"

        n "Tu cuerpo tiembla de forma incontrolada sin que puedas mover ni un solo músculo a voluntad."

        n "Tu respiración se acelera tanto que sufres falta de aire. "

        window hide dissolve
        pause

        show black
        with fade

        ne "Tranquilo,"

        hide black
        hide p_ao_nMouth_creepy_comp

        $ nteye = "front06"
        show n_closefromup_mouth happy_Talkingx03
        show n_closefromup_eyebrows sadx03
        call n_closefromup_tears_tears

        with fade

        ne "no tengo ninguna intención de comerte vivo."

        $ nteye = "down05"
        show n_closefromup_mouth happy_Talkingx05
        show n_closefromup_eyebrows sadx04
        call n_closefromup_tears_tears
        with dissolve

        ne "Con tu esperma,"

        extend " de momento,"

        $ nteye = "front07"
        show n_closefromup_mouth happy_Talkingx09
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        ne "tengo suficiente."

        $ nteye = "down05"
        show n_closefromup_mouth happybiting_Silentx08
        show n_closefromup_eyebrows sadx05
        call n_closefromup_tears_tears
        with dissolve

        pause 0.2

    scene black
    with fade

    n "Su lengua se desplaza detrás de tu nuca,"

    n "para luego rodearte el cuello con ella."

    with hpunch
    p "¡Ugh!"

    n "Ejerciendo una mayor presión te impide respirar con normalidad."

    p "[neusname]..."

    n "Lentamente debilita esa fuerza y vuelve a liberarte."

    pt "¡¿Qué cojones pretende?!"

    n "Pasa de nuevo su lengua por tu cuello para relamerte esa dolorida parte."

    ne "Te ves tan delicioso..."

    n "Acerca sus labios a tu cuello y con sus puntiagudos dientes;"

    play sound "audio/characters/protagonist/au01.ogg"
    with hpunch
    p "¡AUCH!"

    n "Sufres lo que te parecen sus dientes desgarrando tu piel y clavándose en tu carne."

    p "[neusname]..."

    #scene bg dark_a
    scene bg_ped_04
    with fade

    n "Finalmente te libera de su mordisco y acercándose a tu oreja:"

    ne "Bésame."

    show kiss_ f_n_07:
        truecenter
        xzoom -1.0
        rotate -60
        zoom 2.0
        xpos 0.8 ypos 0.8
    with Dissolve(1.0)

    n "Sin darte tiempo a responder,"

    show kiss_ f_n_12
    with Dissolve(1.0)

    n "vuelve a pasar su lengua por el interior de tu boca saboreando su -ardiente- saliva mezclada con -lo que parece- tu sangre."

    $ nteye = "front03"
    $ ped_sex_general_expression_Cond = "sharp_closed_blood_angryx02"

    #scene bg dark_a
    scene bg_ped_04
    show n_closefromup_p_ao_01:
        subpixel True
        truecenter
        zoom 1.5
        xpos 0.5 
        ypos -1.0 # Neck
        easein_quad 5.0 ypos 0.2
    with fade


    p "¡¿Me-"

    extend "me has mordido?!"

    $ nteye = "front05"
    $ ped_sex_general_expression_Cond = "sharp_open_blood_angryx02"
    show n_closefromup_p_ao_01:
        subpixel True
        easein 15.0 zoom 0.4 ypos 0.5
    with dissolve

    ne "Solo un poquito..."

    $ nteye = "front05"
    $ ped_sex_general_expression_Cond = "sharp_closed_blood_angryx02"
    show n_closefromup_p_ao_01
    with dissolve

    pause

    show black
    with fade

    n "Observas como se relame los labios y la barbilla para limpiarse de tu sangre."

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with fade_short

    p "¡Pensaba que no eras un vampiro!"

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx004
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "Y no lo soy."

    $ nteye = "front07"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Pero eso no quita que me encanta el sabor de la sangre,"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx005
    show n_closefromup_eyebrows suspiciousx01
    call n_closefromup_tears_tears
    with dissolve

    ne "aunque sinceramente,"

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows sadx01
    call n_closefromup_tears_tears
    with dissolve

    ne "prefiero tu delicioso esperma."

    $ nteye = "front05"
    show n_closefromup_mouth happybiting_Silentx05
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    n "Percibes en tu espalda la fría humedad de tu sangre cubriendo las sábanas."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx003
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Aunque te recuerdo que sigo con hambre,"

    $ nteye = "front01"
    show n_closefromup_mouth extra_sharp_open
    show n_closefromup_eyebrows angryx05
    call n_closefromup_tears_tears
    with dissolve

    ne "así que no me hagas esperar mucho."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "[neusname],"

    extend " mi cuello..."

    $ nteye = "front05"
    show n_closefromup_mouth sadbiting_Silentx05
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmm..."

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx07
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Es verdad,"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx08
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    ne "supongo que no puedo dejar que mueras desangrado,"

    $ nteye = "front07"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx07
    call n_closefromup_tears_tears
    with dissolve

    ne "¿verdad?"

    $ nteye = "front05"
    show n_closefromup_mouth extra_sharp_closed
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with Dissolve(0.5)

    pause 0.2

    scene black
    with fade

    n "Su longeva y abrasadora lengua vuelve a pasar por tu dolorido cuello"

    n "y como si fuera un hierro ardiente;"

    p "¡Auuuhh!"

    n "pasa por cada una de -las que sospechas que son- las heridas abiertas de sus dentelladas."

    ne "No te quejes tanto..."

    # AMAZONIC POSE FINALLY! (or again?)

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "teasing_feet_02"
    $ p_ao_mc_dick_num = 1
    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        #zoom 0.2
        # zoom 2.0 xpos 1.2 ypos -0.8 # Left Ankle
        # easein_quad 3.0 zoom 2.0 xpos 1.4 ypos 0.8 # Left Leg
        zoom 4.0 xpos 0.5 ypos 2.2 # Close to Mouth, without Eyes.
        ease 8.0 zoom 4.0 xpos 0.5 ypos -1.05 # Base of your dick.
        #ease 5.0 zoom 0.75 xpos 0.5 ypos 0.4 # WholeTongue02
    with fade

    n "Vuelve a levantar tus piernas para ponerse encima de tu flácido, rojizo y dolorido miembro."

    # n "Agarrándote de los tobillos, pone tus muslos sobre tu abdomen y ejerciendo cierta fuerza,"
    # n "te levanta la cadera ligeramente mientras se pone justo encima de tu flácido, rojizo y dolorido miembro."

    p "[neusname]..."

    $ p_ao_n_vel = 1
    
    $ p_ao_action_tongue_Cond = "02_01"
    show p_ao_sex_amazon_front_comp_02:
        ease 5.0 zoom 2.5 xpos 0.5 ypos -0.4 # A bit far from the dick.
    with Dissolve(1.0)

    n "Acerca su lengua a ese afligido gusano para rodearla con ella."

    if p_prot_aoNight_analReceived == "True":

        n "-y sin dejar de jugar con su cola en tu trasero-"

    $ p_ao_n_vel = 2
    $ p_ao_action_tongue_Cond = "02_01"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    p "Ya-"

    extend "ya no puedo más..."

    $ p_ao_n_vel = 3
    $ p_ao_mc_dick_num = 2
    $ p_ao_action_tongue_Cond = "02_02"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    n "Agitándola de arriba a abajo."

    $ p_ao_n_vel = 4
    $ p_ao_mc_dick_num = 3
    $ p_ao_action_tongue_Cond = "02_03"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    ne "Tranquilo,"

    extend " no hace falta que hagas nada,"

    $ p_ao_n_vel = 5
    $ p_ao_mc_dick_num = 4
    $ p_ao_action_tongue_Cond = "02_04"
    show p_ao_sex_amazon_front_comp_02:
        ease 5.0 zoom 2.0 xpos 0.5 ypos -0.1 # A bit more far from the dick.
    with Dissolve(1.0)

    ne "yo me encargo."

    $ p_ao_n_vel = 6
    $ p_ao_mc_dick_num = 5
    $ p_ao_action_tongue_Cond = "02_05"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    pause

# ####
#     $ p_ao_action_tongue_Cond = "02_00"
#     $ p_ao_mc_dick_num = 0
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "00"
#     $ p_ao_action_tongue_Cond = "02_01"
#     $ p_ao_mc_dick_num = 1
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "01"
#     $ p_ao_action_tongue_Cond = "02_02"
#     $ p_ao_mc_dick_num = 2
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "02"
#     $ p_ao_action_tongue_Cond = "02_03"
#     $ p_ao_mc_dick_num = 3
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "03"
#     $ p_ao_action_tongue_Cond = "02_04"
#     $ p_ao_mc_dick_num = 4
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "04"
#     $ p_ao_action_tongue_Cond = "02_05"
#     $ p_ao_mc_dick_num = 5
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "05"
#     $ p_ao_action_tongue_Cond = "02_06"
#     $ p_ao_mc_dick_num = 6
#     show p_ao_sex_amazon_front_comp_02
#     progcheck "06"
# ###
    
    $ p_ao_n_vel = 4
    $ p_ao_mc_dick_num = 6
    $ p_ao_action_tongue_Cond = "02_06"
    show p_ao_sex_amazon_front_comp_02:
        ease 5.0 zoom 1.5 xpos 0.5 ypos 0.1 # Dick Whole
    with Dissolve(1.0)

    n "Al percibir que tu polla empieza a recuperar su erección,"

    $ p_ao_n_vel = 1
    $ p_ao_mc_dick_num = 6
    $ p_ao_action_tongue_Cond = ""
    $ p_ao_action_Cond = "teasing_feet_01"
    show p_ao_sex_amazon_front_comp_02:
        ease 5.0 zoom 0.75 xpos 0.5 ypos 0.4 # WholeTongue02
    with Dissolve(1.5)

    n "retira su lengua"

    $ p_ao_action_Cond = "fucking_feet_02"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    n "mientras se acerca su entrepierna."

    $ p_ao_action_Cond = "fucking_feet_03"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    $ p_ao_action_Cond = "fucking_feet_02"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    n "Sufres su ardiente interior consumiendo tu afligido miembro"

    $ p_ao_action_Cond = "fucking_feet_03"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    if p_prot_aoNight_analReceived == "True":

        $ p_ao_n_vel = 5
        $ p_ao_action_Cond = "tail_05"
        show p_ao_mc_ass_comp 04:
            subpixel True
            truecenter
            zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
            block:
                easein_quad 4.0/p_ao_n_vel zoom 1.0 xpos 0.7 ypos 0.6 # Close Ass
                easeout_quad 4.0/p_ao_n_vel zoom 0.65 xpos 0.1 ypos 0.75 #UpRight
                repeat
        with fade

        pause 0.5

        $ p_ao_n_vel = 1
        $ p_ao_action_Cond = "tail_01"
        show p_ao_mc_ass_comp 04:
            zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
            block:
                ease 4.0/p_ao_n_vel zoom 1.0 xpos 0.45 ypos 0.55 # Close Ass
                ease 4.0/p_ao_n_vel zoom 0.95 xpos 0.44 ypos 0.58 # UpRight
                repeat
        with Dissolve(1.5)


        n "al mismo tiempo que percibes su cola abandonando tu trasero."

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

    else:

        $ Pedrera_char_Cond = "NeusSuperClose"
        call Pedrera_char_lab

        show n_closefromup_body naked

        $ nteye = "front03"
        show n_closefromup_mouth extra_sharp_closed
        show n_closefromup_eyebrows angryx02
        call n_closefromup_tears_tears
        with fade_short

        n "mientras te sonríe con un rostro escalofriante."


    $ nteye = "down02"
    show n_closefromup_mouth sad_Talkingx002
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    if p_prot_aoNight_analReceived == "True":
        with fade_short
    else:
        with dissolve

    ne "No está tan dura como antes,"

    $ nteye = "down05"
    show n_closefromup_mouth extra_sharp_open
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "pero creo que bastará..."

    $ nteye = "front05"
    show n_closefromup_mouth extra_sharp_closed
    show n_closefromup_eyebrows suspiciousx05
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Có-"

    extend "cómo es posible que siga poniéndose tiesa?!"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Silentx03
    show n_closefromup_eyebrows surprisex01
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmm..."

    $ nteye = "right03"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "No me suele gustar hacer este tipo de trucos,"

    $ nteye = "down02"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "pero viendo lo rojiza, flácida y destruida que la tienes"

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows surprisex03
    call n_closefromup_tears_tears
    with dissolve

    ne "he tenido que usar algo más fuerte que mi saliva y mis dotes femeninas para ponértela dura."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx06
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pt "¡¿Qué entenderá esta mujer por \"dotes femeninas\"?!"

    $ nteye = "front04"
    show n_closefromup_mouth sad_Silentx05
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    p "¡¿Te refieres a...?!"

    $ nteye = "front05"
    show n_closefromup_mouth happy_Silentx08
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Hmmmm..."

    $ nteye = "front03"
    show n_closefromup_mouth extra_sharp_open
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Mezclando mi sangre con la tuya, puedo conseguir mejores resultados,"

    $ nteye = "right01"
    show n_closefromup_mouth sad_Talkingx03
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "pero no es lo más aconsejable."

    $ nteye = "front08"
    show n_closefromup_mouth sad_Talkingx006
    show n_closefromup_eyebrows suspiciousx02
    call n_closefromup_tears_tears
    with dissolve

    ne "No solo me deja agotada,"

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx05
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "sino que es posible que tardes unos días en poder volver a caminar."

    $ nteye = "front01"
    show n_closefromup_mouth sad_Silentx02
    show n_closefromup_eyebrows surprisex02
    call n_closefromup_tears_tears
    with dissolve

    p "¡Pe-"

    extend "pero si está a punto de amanecer!"

    $ nteye = "front05"
    show n_closefromup_mouth sad_Talkingx008
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    ne "Te he dicho que no te preocupes por eso."

    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx12
    show n_closefromup_eyebrows sadx06
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    # $ p_ao_action_Cond = "nOverUp" ## Maybe in another place, what about wings?
    # scene p_ao_sex_amazon_side_comp_01:
    #     truecenter
    #     zoom 0.2
    # with fade

    $ p_ao_action_Cond = "teasing_feet_01"
    scene p_ao_sex_amazon_front_comp_02:
        truecenter
        xpos 0.5 ypos 0.5
    with Dissolve(0.5)

    n "Balancea sus caderas sobre ti"

    $ p_ao_action_Cond = "fucking_feet_02"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
    with Dissolve(0.5)

    n "como si fuera ella la que te estuviera penetrando con su infernal vagina"

    $ p_ao_action_Cond = "fucking_feet_03"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.3
    with Dissolve(0.5)

    n "mientras te sigue agarrando de las piernas."

    $ p_ao_action_Cond = "fucking_feet_02"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(0.5)

    $ p_ao_action_Cond = "fucking_feet_03"
    show p_ao_sex_amazon_front_comp_02
    with Dissolve(1.0)

    p "Ughh..."

    $ p_ao_action_Cond = "fucking_feet_04"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.2
    with Dissolve(2.5)

    n "Hasta que termina tragándosela por completo"

    $ p_ao_n_vel = 4
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        ypos 0.4
        block:
            pause 0.5/p_ao_n_vel
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 7.5/p_ao_n_vel ypos 0.4
            repeat
    with Dissolve(1.0)

    n "al mismo tiempo que aumenta de ritmo"

    $ p_ao_n_vel = 8
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with Dissolve(0.5)

    n "sin que puedas hacer nada al respecto."

    $ p_ao_n_vel = 12
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with Dissolve(0.5)

    pause

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "down05"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with fade_short

    ne "Me encanta sentirla así de dura..."

    $ ped_neus_whispers_sfx04 += 0.30 # How is now?

    $ nteye = "down03"
    show n_closefromup_mouth happy_Silentx11
    show n_closefromup_eyebrows angryx02
    call n_closefromup_tears_tears
    with dissolve

    n "Sus ojos vuelven a iluminarse con intensidad"

    $ ped_neus_whispers_sfx04 += 0.30 # How is now?

    $ nteye = "down00"
    show n_closefromup_mouth extra_sharp_closed
    show n_closefromup_eyebrows angryx03
    call n_closefromup_tears_tears
    with dissolve

    n "al mismo tiempo que te muestra una expresión particularmente perturbadora."

    $ p_ao_n_vel = 30
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        zoom 1.0
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.23
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.38
            repeat
    with fade

    n "Entre un placer agónico y un dolor abrasador,"

    if music_play != "nonstop":
        play music "audio/music/kevinmacleod/nonstop.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "nonstop"

    show closetocum_mc

    n "Experimentas de nuevo el tenue cosquilleo que precede a una nueva explosión."

    $ p_ao_n_vel = 40
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        zoom 1.2
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.15
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.35
            repeat

    pause 0.5

    $ p_ao_n_vel = 50
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        zoom 1.4
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.05
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.3
            repeat

    p "[neusname]..."

    $ p_ao_n_vel = 10
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        zoom 1.0
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.23
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.38
            repeat
    with Dissolve(1.0)

    pause 1.0

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        subpixel True
        zoom 0.5
        ypos 0.5
        block:
            easeout 7.0/p_ao_n_vel ypos 0.42
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.5
            repeat
    with Dissolve(1.0)

    pause

    hide p_ao_sex_amazon_front_comp_02

    $ nteye = "front05"
    show n_closefromup_mouth happy_Talkingx03
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with fade_short

    ne "Lo sé,"

    $ nteye = "front06"
    show n_closefromup_mouth happy_Talkingx06
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with dissolve

    ne "también estoy a punto."

    $ nteye = "front03"
    show n_closefromup_mouth happy_Talkingx09
    show n_closefromup_eyebrows sadx02
    call n_closefromup_tears_tears
    with dissolve

    ne "Creo que hacía décadas que no tenía tantos orgasmos seguidos fuera de un {a=https://es.wikipedia.org/wiki/Aquelarre}Aquelarre{/a}..."

    $ nteye = "down05"
    show n_closefromup_mouth extra_sharp_closed
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with dissolve

    pause 0.2

    $ p_ao_n_vel = 40
    $ p_ao_action_Cond = "fucking_feet_02_04"
    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        zoom 1.0
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    show closetocum_mc
    with fade

    n "Sus embestidas incrementan su rudeza y apenas eres capaz de resistir el abrasador dolor que desprende su cuerpo entero."

    $ p_ao_n_vel = 50
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        zoom 1.2
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.15
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.35
            repeat

    p "¡Ugh!"

    $ p_ao_n_vel = 60
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        zoom 1.4
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.0
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.2
            repeat

    ne "¡Dame hasta la última gota!"

    $ p_ao_n_vel = 70
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02:
        zoom 1.8
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos -0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.0
            repeat

    $ renpy.music.set_volume(1.0, delay=0.8, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    n "Tu cuerpo tambalea al mismo tiempo que oyes la madera de la cama golpear contra el suelo y la pared."

    $ p_ao_n_vel = 80
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02

    $ renpy.music.set_volume(0.2, delay=2.0, channel='sfx1')

    n "El cosquilleo te revuelve por dentro, presientes que apenas te quedan reservas,"

    $ p_ao_n_vel = 100
    $ p_ao_action_Cond = "fucking_feet_02_04"
    show p_ao_sex_amazon_front_comp_02

    pause

    with vpunch
    with vpunch

    show cumming_mc
    with dissolve

    $ p_ao_n_dick_num += 1
    call p_ao_n_changes

    $ p_prot.orgasm += 1
    $ p_neus.orgasm += 1

    n "pero aún así tu miembro logra expulsar de nuevo una -bastante más liviana- corrida en su interior."

    stop music fadeout 1.0

    scene black
    with fade_long1s

    pause

    $ renpy.music.set_volume(1.0, delay=0.8, channel='sfx1')
    $ renpy.music.play("audio/characters/neus/orgasm_post_long01.ogg", channel="sfx1",loop=True, fadeout=2.0, synchro_start=True, fadein=3.0)

    if music_play != "killers":
        play music "audio/music/kevinmacleod/killers.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "killers"

    $ p_ao_n_vel = 50
    $ p_ao_action_Cond = "fucking_feet_02_04"
    scene p_ao_sex_amazon_front_comp_02:
        subpixel True
        truecenter
        zoom 1.0
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    show border_darkness:
        zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.8 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    n "Pero ella no se detiene en ningún momento y sigue auto-penetrándose salvajemente"

    $ renpy.music.set_volume(0.2, delay=2.0, channel='sfx1')

    $ p_ao_n_vel = 40
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with dissolve

    n "mientras exclama de placer -y quizás con tintes de locura enfermiza-."

    $ p_ao_n_vel = 30
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with dissolve

    n "A medida que sus gritos disminuyen de volumen, también desacelera el ritmo;"

    $ p_ao_n_vel = 20
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with dissolve

    n "Sin embargo, aumenta la fuerza de cada lenta arremetida,"

    $ p_ao_n_vel = 10
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        block:
            easeout 7.0/p_ao_n_vel ypos 0.2
            pause 1.0/p_ao_n_vel
            easeout 8.0/p_ao_n_vel ypos 0.4
            repeat
    with dissolve

    n "hasta que finalmente aprieta con fuerza clavando el hueso de sus caderas contra tu frágil entrepierna"

    $ p_ao_n_vel = 1
    $ p_ao_action_Cond = "fucking_feet_04"
    show p_ao_sex_amazon_front_comp_02:
        ypos 0.4
        ease 1.0 ypos 0.2
    with Dissolve(1.0)

    n "para luego dar círculos removiendo tu polla desde la base hasta la punta."

    n "En ese volcánico interior, sientes \"cosas\" moviéndose a lo largo y ancho de tu miembro,"

    scene black
    show p_ao_nVagSex_cum_rest:
        truecenter
        zoom 1.5 xpos -0.5 ypos 1.1 # Whole Right Top
        ease 10.0 zoom 1.0 xpos 0.9 ypos 0.5 # Point Dick.
        ease 5.0 zoom 0.5 xpos 0.5 ypos 0.5
    with fade

    n "como si fueran lenguas internas que acarician y al mismo tiempo presionan"

    n "tu afligido, demolido, y exhausto miembro, desde la base hasta la punta,"

    n "del mismo modo que si intentara sacar los resquicios de una agotada pasta de dientes."

    if not p_prot_aoNight_analReceived == "True":

        pt "¡¿Puede hacer lo mismo con su coño?!"
    else:

        pt "¿¡Qué coño le pasa en su coño?!"

    pause

    stop music fadeout 2.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)

    $ ped_neus_whispers_sfx04 = 1.0

    $ Pedrera_char_Cond = "NeusSuperClose"
    call Pedrera_char_lab

    show n_closefromup_body naked

    $ nteye = "down03"
    show n_closefromup_mouth happybiting_Silentx15
    show n_closefromup_eyebrows sadx09
    call n_closefromup_tears_tears
    with fade_short

    n "El temblor cesa,"

    $ ped_neus_whispers_sfx04 = 0.5

    call Pedrera_char_lab
    show n_closefromup_body naked
    $ nteye = "down04"
    show n_closefromup_mouth happybiting_Silentx10
    show n_closefromup_eyebrows sadx05
    call n_closefromup_tears_tears
    with Dissolve(1.0)

    pause 0.2

    $ ped_neus_whispers_sfx04 = 0.1

    call Pedrera_char_lab
    show n_closefromup_body naked
    $ nteye = "down05"
    show n_closefromup_mouth happybiting_Silentx07
    show n_closefromup_eyebrows sadx04
    call n_closefromup_tears_tears
    with Dissolve(1.0)

    n "sus ojos se apagan,"

    $ ped_neus_whispers_sfx04 = 0.0

    call Pedrera_char_lab
    show n_closefromup_body naked
    $ nteye = "front08"
    show n_closefromup_mouth happybiting_Silentx03
    show n_closefromup_eyebrows sadx03
    call n_closefromup_tears_tears
    with Dissolve(1.0)

    pause 0.2

    scene black
    with fade

    n "y sus manos te sueltan."

    play sound "audio/sfx/fall01.ogg"

    with vpunch

    n "Sin que puedas evitarlo, tus piernas caen de nuevo rendidas sobre la cama."

    pause

    play sound "audio/sfx/lickL01.ogg"
    ono "lick"
    play sound "audio/sfx/lickR01.ogg"
    extend " lick"
    play sound "audio/sfx/lickL02.ogg"
    extend " lick"

    pt "No..."

    if music_play != "morgana_rides":
        play music "audio/music/kevinmacleod/morgana_rides.ogg" fadein 3.0 fadeout 3.0
        $ music_play = "morgana_rides"


    $ p_ao_n_tongue = "bifid"
    $ ped_sex_general_expression_Cond = "closed"
    $ ped_sex_general_expressionJaw_Cond = "blow_below_04"
    $ p_ao_n_vel = 1
    show pedrera_sex_neus_oral softLicking:
        subpixel True
        truecenter
        ypos 0.55 # Up
        block:
            ease 10.0/p_ao_n_vel ypos 0.45 # Down
            ease 10.0/p_ao_n_vel ypos 0.55 # Up
            repeat
    show border_darkness:
        subpixel True
        zoom 1.0 xalign 0.5 yalign 0.5 alpha 1.0
        easein_quad 30.0 zoom 0.5 xalign 0.5 yalign 0.5 alpha 1.0
    show morning04_bedroom_DMast_blinkeye
    with fade

    n "Una -no menos ardiente -lengua {a=https://es.wikipedia.org/wiki/Lengua_bífida}bífida{/a} -partida en dos- acaricia tu extenuado y rendido miembro,"

    $ p_ao_n_vel = 2
    show pedrera_sex_neus_oral softLicking
    with Dissolve(2.0)

    n "algo que -a estas alturas- te causa muchísimo más dolor que placer."

    $ p_ao_n_vel = 4
    show pedrera_sex_neus_oral softLicking
    with Dissolve(1.0)

    pt "Otra vez no..."

    $ p_ao_n_vel = 8
    show pedrera_sex_neus_oral softLicking
    with Dissolve(0.5)

    n "Con las fuerzas completamente agotadas,"

    $ p_ao_n_vel = 16
    show pedrera_sex_neus_oral softLicking
    with dissolve

    pt "Ya..."

    $ p_ao_n_vel = 24
    show pedrera_sex_neus_oral softLicking
    with dissolve

    n "y a pesar del terrible tormento que padeces al contacto con sus manos y su lengua,"

    $ p_ao_n_vel = 48
    show pedrera_sex_neus_oral softLicking
    with dissolve

    pt "ya no puedo más..."

    $ p_ao_n_vel = 64
    show pedrera_sex_neus_oral softLicking
    with dissolve

    scene black
    with fade_long1s

    stop music fadeout 3.0

    #n "Tus párpados se cierran por completo."

    stop music fadeout 3.0
    $ renpy.music.stop(channel='sfx1', fadeout=3.0)
    $ renpy.music.stop(channel='sfx2', fadeout=3.0)
    $ renpy.music.stop(channel='sfx3', fadeout=3.0)
    $ renpy.music.stop(channel='sfx4', fadeout=3.0)
    $ renpy.music.stop(channel='sfx5', fadeout=3.0)
    $ renpy.music.stop(channel='sfx6', fadeout=3.0)

    pause

    # END

    jump day06_night_label

    # $ p_neus.orgasm += 1
    # $ p_neus.closeOrgasm = 0
    # $ p_neus.pleasure = -50


## Neus se pone muy caliente y empieza a cabalgarte sin que puedas siquiera moverte.
## Terminas dentro de ella mientras entra en extásis, pero no orgasmo.
## # 4th ORGASM
## Ve que tu polla se vuelve flácida, te pregunta si ya no te pone caliente, le respondes que ya llevas un buen trote y que 3 es tu máximo.
## No era ella la que decía que solo necesitaba una corrida, pero ella quiere más...
## Empieza a juguetear con tu agujero anal.
## Aquí es cuando puedes empezar a mover tus ojos y ver que empieza a crecerle una polla de su entrepierna, te recuerda que le dijiste que no te había disgustado tanto antes... Si has sido malo con ella, te va a follar igual.

## Si te folla el trasero, ella no se corre, pero te masturba mientras te folla cogiéndote por las piernas, cuando ve que apenas se te pone dura, te pone a cuatro patas y empieza  a follarte duramente a cuatro patas mientras te agarra por los huevos y se te empieza a poner dura, cuando sientes que estás a punto de correrte pone las manos para parar la corrida y luego relamer su mano. Luego se pone debajo de ti y termina de succionarte la polla. Cuando ve que se te vuelve a poner flácida, estando aún a cuatro patas, empieza a darte un beso negro mientras te aprieta los huevos y te masturba, cuando ve que se te vuelve  aponer dura.

## # 5th ORGASM(Optional)

## Levanta tus piernas y vuelve a ponerse la polla dentro "Amazon sexual pose" y empieza a follarte salvajamente mientras te abofetea y luego te estrangula para sentir que se te va poinendo dura.
## Cuando por fin te corres sigue cabalgándote, tu polla está completamente rojiza y los huevos te duelen un montón.
##  # 5/6th ORGASM

## Pero aún así, se pone anti ti y vuelve a meterse la polla en tu boca succionándola de nuevo mientras sientes sus dedos de nuevo tu trasero. Sientes que se te vuelve a poner dura, pero empiezas a perder la consciencia.
## Poco a poco vas sintiendo un nuevo orgasmo y finalmente pierdes la consciencia.
## # 6/7th ORGASM

##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################






##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
# YOU CUM


label p_neus_pre_wrong_received_label:

    if p_neus.cumReceived == "buttocks":
        progcheck "You try to cum on her buttocks."


    elif p_neus.cumReceived == "stomach":
        progcheck "You try to cum on her stomach."

    scene day05
    with fade

    ###


    if p_prot.action in ["cunnilingus_done", "annilingus_done"]:

        n "Apartas rápidamente tu lengua de su entrepierna,"

    else:
        
        n "Te apartas rápidamente,"

    n "agarras tu latente polla,"

    n "a punto de entrar en erupción,"

    if p_neus.cumReceived == "buttocks":

        n "y apuntas hacia sus nalgas."

    else:

        n "y apuntas hacia su barriga."

    ne "¡¿Se puede saber qué estás haciendo?!"

    p "¡Ugh!"

    n "Un torrente de esperma emerge de tu palpitante polla"

    if p_neus.cumReceived == "buttocks":

        if p_neus.buttockSlaps_received > 1:

            n "cayendo sobre sus suaves y azotadas nalgas."

        else:

            n "cayendo sobre sus suaves y esponjosas nalgas."

    else:

        n "cayendo sobre la blanca y tersa piel de su estómago."

    ne "¡¿Qué?!"

    ne "¡Rápido!"

    ne "¡Métemela antes de que termines del todo!"

    n "Agarras tu polla y te masturbas con fogosidad hasta sacar otro chorro de esperma"

    n "que termina de nuevo en su cálida piel."

    ne "..."

    # if gensex_ILoveYouNeus == True
    # if gensex_INotLoveYouNeus == True
    # if gensex_YoureAMonster == True
    
    if gensex_YoureAMonster:

        ne "¡¿Por qué?!"

    else:

        ne "[protname]..."

        ne "¿Por qué?..."

    $ p_neus_cumOut_whatYouDeserve = False

    menu:

        "Porque me gusta verte embadurnada con mi esperma.":

            #$pl.ch_pts("np",-1)

            ne "..."

            ne "¿En serio...?"

            jump p_neus_cumOut_dontUnderstand

        "Porque es lo que te mereces.":
            $pl.ch_pts("np",-4)

            $ p_neus_cumOut_whatYouDeserve = True
            
            ne "¡¿Es lo que me merezco?!"

            jump p_neus_cumOut_dontUnderstand

        "No sé por qué he hecho esto...":
            $pl.ch_pts("np",-1)

            ne "..."

            ne "Padre no está influyendo en ti ahora,"

            ne "así que no me vengas con esa excusa."

            p "..."

            jump p_neus_cumOut_dontUnderstand

        "...":
            $pl.ch_pts("np",-1)

            jump p_neus_cumOut_dontUnderstand

label p_neus_cumOut_dontUnderstand:

    ne "¡¿Es que acaso no lo entiendes?!"

    ne "¡Te he dicho que cuando salga el sol tenemos que salir de aquí cuanto antes!"

    ne "¡¿Acaso no entiendes que necesitaré mis poderes para lograr escapar?!"

    p "¿Para qué?"

    ne "¡Para empezar,"

    ne "explicar en aduana quien demonios es Dídac!"

    ne "¡Te recuerdo que en su {a=https://es.wikipedia.org/wiki/DNI_(España)}DNI{/a} pone que es un hombre,"

    ne "y no es que se parezca demasiado a su foto de perfil!"

    p "¡¿Por qué tenemos que pasar por aduana?!"

    ne "¡PARA ESCAPAR DE PADRE!"

    ne "¡¿Por qué te cuesta tanto entenderlo?!"

    p "..."

    menu:

        pt "Para escapar de Padre..."

        "Lo siento." if p_neus_cumOut_whatYouDeserve == False:

            if gensex_YoureAMonster:

                $pl.ch_pts("np",-1)

                ne "Después de llamarme monstruo,"

                ne "tus disculpas tienen poco valor."

                jump p_neus_cumOut_whatIsImportant

            else:

                $pl.ch_pts("np",1)

                jump p_neus_cumOut_ImSorry

        "No sé cual de los dos es más monstruo." if not gensex_ILoveYouNeus:

            $pl.ch_pts("np",-4)

            jump p_neus_cumOut_whatIsImportant


        "...":
            jump p_neus_cumOut_whatIsImportant

label p_neus_cumOut_ImSorry:

    ne "..."

    ne "¿Qué se supone que tengo que hacer ahora contigo?"

    p "..."

    ne "-Profundo suspiro-*Aaaish...*"

    n "Vuelve a separar sus párpados donde sus enormes y brillantes ojos violáceos"

    n "destacan por encima de los rojizos orbes que orbitan alrededor de la oscura habitación."

    n "De su boca desciende su longeva lengua,"

    n "tan inhumanamente larga,"

    if p_neus.cumReceived == "buttocks":

        n "que surca su abdomen desnudo hasta llegar hasta su desnudo trasero"

    else:

        n "que desciende por sus pechos hasta llegar cerca de su ombligo"

    n "dónde relame su suave piel en busca de tu frío esperma,"

    n "como si su vida dependiera de que no quedase ni el más mínimo rastro."

    #n "como si fuera una heladera rascando las últimas gotas que quedan al fondo del pote."

    n "Finalmente, regresa grácilmente a su boca."

    ono "glup"

    extend " glup"

    n "En su rostro ves una expresión de regocijo y deleite,"

    n "como si fuera el primer vaso de vino que ha bebido en años."
    
    ne "-Profundo suspiro-*Aahhh...*"

    p "..."

    n "A pesar de que hace escasos segundos su expresión era de éxtasis,"

    n "sus ojos están ahora fijados en ti, con un rostro iracundo y famélico."

    ne "Te dije que te corrieras dentro."

    ne "¡Podías incluso elegir dónde!"

    menu:

        "No parece que te haya disgustado.":
            call p_Help
            #$pl.ch_pts("np",-1)

            ne "¡Por supuesto que no me ha disgustado!"

            ne "Pero una vez frío,"

            ne "no es lo mismo..."

            p "..."

            n "Sus brillantes ojos se dirigen a tu entrepierna."

            p "¿Qué?"

            ne "Por tu culpa,"

            ne "sigo con hambre."

        "Lo lamento.":
            call p_Help

            $pl.ch_pts("np",1)

            ne "No,"

            extend " aún no lo lamentas lo suficiente."

        "...":
            call p_Help

            ne "¿No vas a decir nada?"

            p "..."

            ne "Entonces mejor quédate calladito."


    jump p_neus_received_overYou
        # with hpunch
        # p "¡Ugh!"
        # n "Con un rápido empujón te tira de espaldas sobre la cama."
        # pt "¡Joder!"
        # n "Al abrir los ojos, te encuentras un montón de ojos rojos observándote en la oscuridad."

label p_neus_cumOut_whatIsImportant:

    ne "..."

    ne "[protname],"

    ne "puedes pensar lo que quieras de mi,"

    ne "pero ahora, lo más importante,"

    ne "es que nos vayamos lo más lejos posible cuando salga el sol"

    ne "y para ello necesito tu esperma,"

    ne "te guste,"

    extend " o no."

    p "¿Acaso me vas a obligar?"

    ne "Aparentemente,"

    ne "no me dejas otra alternativa."

    p "¿Có-"

    scene black
    with hpunch

    p "¡Ugh!"

    n "De una fuerte patada, te tira sobre la cama."

    p "¡¿Qué...?!"

    n "Sientes la presión de su desnudo pie sobre tu mejilla."

    ne "Si no fuera porque no tardará en despuntar el sol,"

    ne "ahora mismo te violaría."

    pt "¡¿Cómo dice?!"

    n "Aparta su pie, liberando tu cabeza,"

    n "pero justo cuando abres los ojos,"

    n "te encuentras su rostro ante ti con sus ojos brillantes."

    p "Ughh..."

    pt "No puedo moverme..."

    ne "Bueno,"

    extend " como entenderás,"

    if p_neus.cumReceived == "buttocks":

        ne "no me llego a las nalgas,"

    else:

        ne "no me llego a la barriga."

    ne "así que ahora me vas a ayudar con esto."

    if p_neus.cumReceived == "buttocks":

        n "Gira su cuerpo y acerca su trasero a tu rostro."

    else:

        n "Se aparta y estando a cuatro patas,"

        n "acerca su ombligo a tu cara."

    p "¡¿Qué-"

    extend "qué demonios se supone que estás haciendo?!"

    ne "Creo que es bastante obvio..."

    ne "Ya puedes empezar."

    ne "Y que no quede ni una sola gota."

    ne "Ah,"

    ne "y ni se te ocurra tragarlo,"

    ne "o meteré mi lengua por todo tu esófago hasta sacártelo de tu estómago."

    ne "¡¿Me has entendido?!"

    p "..."

    $ p_neus_cumOut_noLicking_num = 0

    menu p_neus_cumOut_lick_question:

        #pt "¡¿Por mi esófago?!" # Better no text here.

        "<Lamer su trasero>" if p_neus.cumReceived == "buttocks":
            $pl.ch_pts("np",1)
            jump p_neus_cumOut_licking

        "<Lamer su barriga>"if p_neus.cumReceived == "stomach":
            $pl.ch_pts("np",1)
            jump p_neus_cumOut_licking

        "No pienso hacer eso.":
            $pl.ch_pts("np",-1)

            $ p_neus_cumOut_noLicking_num += 1

            jump p_neus_cumOut_noLicking

label p_neus_cumOut_noLicking:

    if p_neus_cumOut_noLicking_num == 1:

        ne "Haberlo pensado antes."

        ne "¡Empieza!"

        ne "No tenemos toda la noche."

    elif p_neus_cumOut_noLicking_num == 2:

        p "Ya te he dicho que no pienso hacerlo."

        ne "Hmmm..."

        if p_neus.cumReceived == "buttocks":

            n "Posa su culo en tu cara"

        else:

            n "Posa su ombligo en tu cara"

        n "empapándote el rostro con tu frío esperma,"

        n "intentas morderla,"

        n "pero eres incapaz de ejercer fuerza en tus mandíbulas,"

        n "apenas puedes mover tu lengua."

        ne "O te pones a lamer,"

        ne "o no te dejaré respirar."

        p "Grrrghhmm..."

        n "Empiezas a notar la falta de aire."

        p "¡HMGHFH-Hgghmm-fhhghmm!"

        n "Eres incapaz de articular palabra alguna"

        if p_neus.cumReceived == "buttocks":

            n "teniendo tu boca y nariz completamente bloqueados por sus nalgas."

        else:

            n "teniendo tu boca y nariz completamente bloqueados por su barriga."

        ne "Mira que eres infantil cuando quieres..."

        n "Sientes que te va faltando la respiración."

        if p_neus.cumReceived == "buttocks":

            ne "No voy a apartar mi culo,"

        else:

            ne "No voy a apartarme,"

        ne "hasta que empiece a sentir tu lengua."

        p "..."

    elif p_neus_cumOut_noLicking_num == 3:

        n "Sigues intentando morder sus nalgas,"

        n "pero lo único que consigues es perder aún más oxígeno."

        ne "Te lo digo en serio."

        p "..."

    elif p_neus_cumOut_noLicking_num >= 4:

        p "..."

        scene black
        with fade
        # Pierdes la consciencia.

        pause

        jump day06_night_label

    jump p_neus_cumOut_lick_question

label p_neus_cumOut_licking:

    n "Alargas tu lengua para acariciar su cálida piel."

    ne "Mmm..."

    if p_neus_cumOut_noLicking_num > 1:

        ne "Veo que por fin has entrado en razón."

    p "Puagh!"

    ne "Oh,"

    extend " vamos..."

    ne "tampoco es tan asqueroso,"

    ne "al fin y al cabo ha salido de ti."

    p "Podría usar mis dedos en lugar de..."

    ne "Ni hablar."

    ne "Has sido tú quien has querido correrte fuera,"

    ne "así que ahora apechuga con tu elección."

    ne "Aunque no tendrá el mismo sabor,"

    ne "me encantará poder besarte con eso mezclando nuestras lenguas."

    p "..."

    ne "Sigue lamiendo."

    ne "Pero recuerda, ni se te ocurra tragarte ni una sola gota."

    p "..."

    ne "Sigo esperando..."

    n "Vuelves a alargar la lengua lamiendo su terso y suave nalga,"

    n "saboreando el frío, pegajoso y salado líquido blanco que lo cubre."

    n "Sientes que se aparta un poco de ti para luego acercarte la parte que aún no has lamido."

    n "Sigues deslizando tu lengua,"

    n "intentando evitar en lo posible tragar lo más mínimo de ese -ya no tan espeso- líquido,"

    n "que va cubriendo tu boca a cada nuevo lametón."

    n "Cuando tienes la sensación que has terminado,"

    n "se aparta para darte la otra nalga."

    ne "Es sorprendente la cantidad que has llegado a sacar,"

    n "teniendo en cuenta que ha sido tu tercera corrida..."

    p "..."

    ne "No te he dicho que pares."

    ono "lick"

    extend " lick"

    n "A pesar de tu esfuerzo,"

    n "el hecho de que tu saliva se mezcle con tu esperma,"

    n "de que tu lengua no se está quieta en ningún momento,"

    n "y de que encima estás boja abajo,"

    n "no te pone nada fácil evitar que el esperma se deslice por tu faringe."

    n "Vuelves a desplazar la lengua por cálida piel,"

    n "hasta que finalmente sientes que ya no queda ni una sola gota."

    n "Se aparta,"

    n "para regresar de nuevo."

    ne "Aún te falta esta parte."

    p "..."

    pt "Tengo la garganta seca,"

    pt "no voy a poder aguantar mucho más..."

    $ p_neus_cumOut_swallow = False

    menu:

        "<Tragar>":

            ono "glup"
            $ p_neus_cumOut_swallow = True


        "<No tragar>":
            $ p_neus_cumOut_swallow = False


    n "Obedeces y sigues lamiendo,"

    n "a pesar de que tienes la sensación de que realmente ya no queda ni una gota,"

    n "y te obliga a seguir por simple capricho."

    n "Finalmente se aparta,"

    if p_neus.cumReceived == "buttocks":

        n "se da la vuelta,"

    else:

        n "desciende,"

    n "y se acerca a tu rostro."

    ne "Buen chico."

    n "Sientes su lengua acariciando tus labios"

    n "hasta que finalmente penetra tu boca para entremezclar vuestras lenguas."

    n "Sus labios succionan tu lengua para luego relamerte los dientes y debajo de la lengua,"

    n "incluso llega a tocar tu campanilla."

    n "Finalmente separa vuestros labios."

    if p_neus_cumOut_swallow:

        jump p_neus_cumOut_throatLick

    else:

        ne "Hmmm..."

        ne "Parece que te has tragado algo..."

        ne "Pero es obvio que has hecho lo posible para evitarlo."

        ne "Además,"

        ne "me ha encantado besarte de este modo."

        ne "Supongo que te mereces una recompensa."

        pt "¿Una recompensa?"

        jump p_neus_received_overYou
            # with hpunch
            # p "¡Ugh!"
            # n "Con un rápido empujón te tira de espaldas sobre la cama."
            # pt "¡Joder!"
            # n "Al abrir los ojos, te encuentras un montón de ojos rojos observándote en la oscuridad."

label p_neus_cumOut_throatLick:

    ne "..."

    ne "Te lo has tragado,"

    ne "¿verdad?"

    p "..."

    menu:

        "Ya no podía más.":

            $pl.ch_pts("np",-1)

            ne "No deberías haberlo hecho."

        "Ha sido tu culpa, por esperar tanto rato.":

            $pl.ch_pts("np",-3)

            ne "Ha sido tu castigo por correrte fuera."

            ne "Pero viendo que no eres capaz de aprender,"

            ne "supongo que necesitas que te castigue de nuevo..."

        "Pues sí, algún problema?":

            $pl.ch_pts("np",-4)

            ne "No,"

            ne "ningún problema."

            ne "Solo que ahora vas a pasarlo un poco mal."

    p "¿Qué?"

    n "Sus ojos brillan de nuevo con intensidad."

    n "Vuelve a cogerte de la mejilla y a besarte con intensidad,"

    n "pero esta vez sientes que su lengua va más allá de tu campanilla."

    n "Se desliza por tu gaznate hasta que sientes que no puedes ni respirar."

    n "Ni siquiera eres capaz de mover la lengua."

    n "Tienes la sensación de que su lengua está ocupando todo tu esófago,"

    n "hasta el punto que realmente está lamiendo tu estómago a través de tu boca."

    p "Ughh!"

    pt "¡No puedo respirar!"

    n "Su lengua se mueve enérgicamente a través de todo tu aparato digestivo"

    n "sin que seas capaz de hacer nada para impedirlo."

    pt "No..."

    n "Debido a la falta de aire"

    pt "puedo..."

    n "Vas perdiendo la consciencia."

    pt "respirar..."

    n "Hasta que finalmente tus párpados se cierran."

    jump p_neus_afterOrgasm


label p_neus_pre_received_label:

    scene day05
    with fade

    if p_prot.action in ["cunnilingus_done", "annilingus_done"]:

        n "Apartas rápidamente tu lengua de su entrepierna,"

    else:
        
        n "Te apartas rápidamente,"

    n "y con tu polla palpitante,"

    n "a punto de entrar en erupción..."

    if p_neus.cumReceived == "anal":

        if p_neus.anal_received > 0:

            ne "¡Uughh...!"

            n "logras volver a metérsela en su cavidad anal."

        else:

            ne "¡¡UUughh!!"

            n "logras penetrar su cavidad anal."

    elif p_neus.cumReceived == "vaginal":

        if p_neus.vaginal_received > 0:

            ne "¡HHmmm...!"

            n "logras volver a metérsela en su ardiente coño."

        else:

            ne "¡HHHGGhmm!"

            n "logras penetrar en su ardiente y estrecha vagina."

            ne "Por fin..."

    else:

        progcheck "Dónde coño se corre?"

    n "Dónde sientes tu polla contraerse y expandirse"

    n "mientras lo poco que te queda en tus afligidos testículos"

    n "sale abruptamente en su ardiente interior."

    pt "Joder..."

    pt "¿Soy yo?"

    pt "¿O está aún más caliente?"

    jump p_neus_received_label


label p_neus_received_label:

    scene black
    with fade

    $ p_neus.seal = "sealed"

    #NOT FINISHED, ILLUSTRATIONS?

    # CUm in Pussy:

    #if p_prot.pos == "missionary":
    #if p_neus.cumReceived == "vaginal":

    if p_prot.pos in ["missionary", "doggy"]:

        if p_prot.pos == "missionary":

            n "Sus manos se agarran a tu espalda y te arropa hacia su pecho desnudo con una fuerza inhumana."

        if p_prot.pos == "doggy":

            n "Entre jadeos observas como [neusname] gira su rostro para mirarte con esos ojos brillantes."

        ne "No te detengas ahora..."

        n "Menea sus caderas con más energía,"

        n "mientras tu polla sigue palpitando y expulsando esperma en su interior."

        pt "¿Qué diablos...?"

        if p_neus.cumReceived == "vaginal":

            n "Su carne interina, que envuelve toda tu polla,"

        else:

            n "Su cavidad anal, que envuelve toda tu polla,"

        n "empieza a vibrar y agitarse como si tuviera vida propia."

        pt "¡Está ardiendo!"

        if p_neus.cumReceived == "vaginal":

            n "Lo que te parece que es una ardiente lengua,"

            n "lame la parte inferior de la punta de tu glande,"

            n "al mismo tiempo que todo su interior te succiona como si fuera una aspiradora."

        else:

            n "La vibración se vuelve tan intensa que sientes todo tu cuerpo temblar."

        pt "Dios..."

        n "Observas los brillantes ojos de [neusname] que te miran con anhelo y deseo."

        if gensex_ILoveYouNeus:

            ne "Te amo."

        elif gensex_YoureAMonster:

            ne "No me importa lo que opines de mi,"

            ne "yo sé lo que siento por ti."

        else:

            ne "Te deseo tanto..."

        if p_prot.pos == "missionary":

            n "Entremezcla su lengua con la tuya"

            n "mientras sientes tu polla siendo succionada por su ardiente y extraño interior."

        n "A pesar de que estás convencido que no queda ni una sola gota en tus apenadas pelotas,"

        n "sigue moviendo sus caderas y acariciando tu polla desde ese ardiente interior."

        n "Intentas apartarte un poco de ella,"

        if p_prot.pos == "missionary":

            n "pero sigue agarrándote con tanta fuerza que sientes sus uñas clavándose en tu espalda."

            pt "No puedo ni moverme..."

        else:

            n "pero descubres que eres incapaz de mover un dedo."

            pt "Qué..."

            pt "¡¿Qué diablos?!"

        n "Sientes tu polla volviéndose flácida en su interior."

    elif p_prot.pos in ["oral", "69"]:

        n "Sus manos se agarran a tus caderas y profundiza aún más su garganta."

        p "¡Ugh!"

        n "Sientes su lengua recorrer tu afligida y rojiza polla"

        n "mientras te succiona con una fuerza que parece que te la quiera arrancar de cuajo."

        pt "¡Dios!"

        pt "Qué..."

        pt "¡¿Qué demonios es esto?!"

        n "Su lengua, que ahora está lamiéndote la base de tus testículos,"

        n "no solo ha incrementado su temperatura,"

        n "sino que además, ahora percibes lo que parece otra lengua,"

        n "acariciándote la parte inferior del glande al mismo tiempo."

        pt "¡¿Tiene dos lenguas?!"

        n "Una de sus manos te agarra con fuerza de los testículos"

        n "mientras los usa a modo de palanca para meterse más profundamente tu polla en su garganta."

        if p_neus.blowjobDeep_done > 0:

            pt "Con lo pequeña que es, y lo mucho que se llega a tragar..."

        else:

            pt "¡Joder!"

            pt "¡Si se la ha metido entera!"

        n "Sientes una de sus lenguas envolverse en tu miembro,"

        n "arropándolo firmemente desde la base"

        n "para luego desplazarlo, ejerciendo aún más presión, hasta la base de tu glande"

        n "como si estuviera sacándole las últimas gotas a una agotada pasta de dientes."

        n "Al mismo tiempo, su otra lengua juguetea con tu glande,"

        n "acariciando su base como si pulsara un botón imaginario que le diera más golosinas,"

        n "todo eso mientras su garganta sigue aspirando con una fuerza inhumana."

        pt "¡Dios!"

        n "A pesar de sus esfuerzos,"

        n "tu polla no es capaz de proporcionar más esperma"

        n "y lentamente va volviéndose más flácida en su ardiente boca."

    else:

        progcheck "Is there any other option? 1298"

    p "[neusname]..."

    p "No puedo más..."

    ne "Seguro que aún te queda algo."

    jump p_neus_received_overYou

label p_neus_received_overYou:

    with hpunch
    p "¡Ugh!"

    n "Con un rápido empujón te tira de espaldas sobre la cama."

    pt "¡Joder!"

    n "Al abrir los ojos, te encuentras un montón de ojos rojos observándote en la oscuridad."

    pt "Joder..."

    p "Ughh..."

    n "Sientes una ardiente lengua lamiéndote de nuevo tu dolorida y flácida entrepierna."

    p "[neusname]..."

    ne "Tranquilo."

    p "Te he dicho que tres es mi..."

    p "Ugh..."

    n "Un largo y ardiente lametón recorre tu blando y afligido miembro desde tus testículos hasta la punta."

    ne "Sé lo que me hago."

    p "No..."

    p "No puedo ni moverme..."

    ne "Tú descansa."

    n "Sientes tu polla arropada de nuevo por su boca,"

    n "pero esta vez incluso más ardiente que antes."

    n "Su lengua recorre y juguetea por tu miembro"

    n "pasando por la parte inferior que une tu miembro con tus testículos,"

    n "así como por la parte de debajo de tu glande,"

    n "mientras masajea con sus manos tu doloridos testículos."

    n "Sus acciones te producen entre un abrasador dolor y un tortuoso placer."

    n "Cada vez te resulta más difícil mantener tus párpados separados."

    p "Me..."

    play sound "audio/characters/neus/shh02.ogg"

    ne "Shhh..."

    n "A pesar del dolor,"

    n "percibes palpitaciones en tu entrepierna que vuelven a endurecer tu castigado miembro."

    ne "Descansa."

    n "Tus párpados finalmente se cierran."

    scene black
    with fade

    jump p_neus_afterOrgasm

# You can Cum:

    # Her mouth.
    # Her pussy.
    # Her ass.

# Wherever you cum, later you fall on bed and she starts to sucking your dick like the previous night with those red eyes, (just this time she is naked). She keeps sucking hard, your dick gets hard again and you cum once again losing your consciusness.